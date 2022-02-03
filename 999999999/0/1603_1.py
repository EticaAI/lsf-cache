#!/usr/bin/env python3
# ==============================================================================
#
#          FILE:  1603_1.py
#
#         USAGE:  ./999999999/0/1603_1.py
#                 ./999999999/0/1603_1.py --help
#                 NUMERORDINATIO_BASIM="/dir/ndata" ./999999999/0/1603_1.py
#
#   DESCRIPTION:  ---
#
#       OPTIONS:  ---
#
#  REQUIREMENTS:  - python3
#          BUGS:  ---
#         NOTES:  ---
#       AUTHORS:  Emerson Rocha <rocha[at]ieee.org>
# COLLABORATORS:
#                 <@TODO: put additional non-anonymous names here>
#
#       COMPANY:  EticaAI
#       LICENSE:  Public Domain dedication or Zero-Clause BSD
#                 SPDX-License-Identifier: Unlicense OR 0BSD
#       VERSION:  v0.5.0
#       CREATED:  2022-01-27 17:07 UTC created. Based on 1603_3_12.py
#      REVISION:  ---
# ==============================================================================

# pytest
#    python3 -m doctest ./999999999/0/1603_1.py

# ./999999999/0/1603_1.py ./999999999/0/1603_1.py \
# --codex-de 1603_45_1 > 999999/0/test.md
# ./999999999/0/1603_1.py ./999999999/0/1603_1.py \
# --codex-de 1603_84_1 > 1603/84/1/1603_84_1.mul-Zyyy.codex.md
# ./999999999/0/1603_1.py ./999999999/0/1603_1.py \
# --codex-de 1603_25_1 > 1603/25/1/1603_25_1.mul-Zyyy.codex.md

# quotes
# - https://en.wiktionary.org/wiki/res,_non_verba#Latin
# - https://en.wikipedia.org/wiki/Nullius_in_verba
#   - https://artigos.wiki/blog/en/Nullius_in_verba


from multiprocessing.sharedctypes import Value
import os
import sys
import argparse
# from pathlib import Path
from typing import (
    Type,
    Union,
    List
)
import fnmatch

# from itertools import permutations
# from itertools import product
# valueee = list(itertools.permutations([1, 2, 3]))
import csv

__EPILOGUM__ = """
Exemplōrum gratiā:
    printf "#item+conceptum+codicem,#item+rem+i_qcc+is_zxxx+ix_wikiq" | \
{0} --de-archivum
    cat 1603/1/1/1603_1_1.no1.tm.hxl.csv | \
{0} --de-archivum
    {0} --de-archivum 1603/1/1/1603_1_1.no1.tm.hxl.csv

    {0} ./999999999/0/1603_1.py --dictionaria-numerordinatio

    {0} ./999999999/0/1603_1.py --codex-de 1603_25_1

""".format(__file__)

NUMERORDINATIO_BASIM = os.getenv('NUMERORDINATIO_BASIM', os.getcwd())
NUMERORDINATIO_DEFALLO = int(os.getenv('NUMERORDINATIO_DEFALLO', '60'))  # �
NUMERORDINATIO_MISSING = "�"
DESCRIPTION = """
Explain the dictionaries
"""

# In Python2, sys.stdin is a byte stream; in Python3, it's a text stream
STDIN = sys.stdin.buffer


# a b aa bb
# printf "30160\n31161\n1830260\n1891267\n" | \
# ./999999999/0/2600.py --actionem-decifram

# a aa aaa
# printf "30160\n1830260\n109830360\n" | \
# ./999999999/0/2600.py --actionem-decifram
# ./999999999/0/1603_1.py --actionem-quod-sparql


# SELECT ?item ?itemLabel
# WHERE {
#   # A. Einstein or J.S. Bach
#   VALUES ?item { wd:Q1065 wd:Q82151 wd:Q125761 wd:Q7809}
#   # mother of
#   OPTIONAL { ?item wdt:P25 ?pseudoquery. }
#   SERVICE wikibase:label { bd:serviceParam wikibase:language
# "[AUTO_LANGUAGE],en". }
# }

# Trivia:
# - extēnsiōnēs, f, pl (Nominative)
#   https://en.wiktionary.org/wiki/extensio#Latin
# - archīva, n, pl, (nominative)
#   https://en.wiktionary.org/wiki/archivum
# - pictūrīs, f, pl (Dative)
#   https://en.wiktionary.org/wiki/pictura#Latin
# - ignōrātīs, f, pl, (Dative)
#   https://en.wiktionary.org/wiki/ignoratus#Latin
ARCHIVA_IGNORATIS = [
    '.gitkeep',
    '.gitignore',
    'README.md',
    'LICENSE.md'
]
EXTENSIONES_PICTURIS = [
    'gif',
    'jpg',
    'jpeg',
    'png',
    'tiff',
    'svg',
]
EXTENSIONES_IGNORATIS = [

]


def numerordinatio_neo_separatum(
        numerordinatio: str, separatum: str = "_") -> str:
    resultatum = ''
    resultatum = numerordinatio.replace('_', separatum)
    resultatum = resultatum.replace('/', separatum)
    resultatum = resultatum.replace(':', separatum)
    # TODO: add more as need
    return resultatum


def numerordinatio_ordo(numerordinatio: str) -> int:
    normale = numerordinatio_neo_separatum(numerordinatio, '_')
    return (normale.count('_') + 1)


def numerordinatio_lineam_hxml5_details(rem: dict, title: str = None) -> str:
    # codex = rem['#item+conceptum+codicem']

    title = title if title else rem['#item+conceptum+codicem']

    resultatum = '<details><summary>🔎' + \
        title + '🔍</summary>' + "\n"
    resultatum += '  <dl>' + "\n"
    for clavem, item in rem.items():
        if item:
            resultatum += '    <dt>' + clavem + '</dt>' + "\n"
            resultatum += '    <dd>' + item + '</dd>' + "\n"
        # print(item)

    resultatum += '  </dl>' + "\n"
    resultatum += '</details>' + "\n"
    return resultatum


def numerordinatio_summary(rem: dict, title: str = None) -> str:
    # codex = rem['#item+conceptum+codicem']

    # TODO: maybe remove this?

    # title = title if title else rem['#item+conceptum+codicem']
    resultatum = []

    # status_definitionem = qhxl(rem, '#status+conceptum+definitionem')
    # if status_definitionem:
    #     resultatum.append(
    #         "<progress value='{0}' max='100' title='definitionem: "
    #         "{0}/100'>{0}/100</progress>".format(
    #             status_definitionem))

    # status_codicem = qhxl(rem, '#status+conceptum+codicem')
    # if status_codicem:
    #     resultatum.append(
    #         "<progress value='{0}' max='100' title='cōdex stabilitātī:"
    #         " {0}/100'>{0}/100</progress>".format(
    #             status_codicem))

    # resultatum.append('<ul>')

    # ix_wikiq = qhxl(rem, '+ix_wikiq')
    # if ix_wikiq:
    #     resultatum.append(
    #         "<li><a href='https://www.wikidata.org/wiki/{0}'>"
    #         "{0}</a></li>".format(
    #             ix_wikiq))
    # resultatum.append('</ul>')

    return resultatum


def numerordinatio_nomen(
        rem: dict, objectivum_linguam: str = None,
        auxilium_linguam: list = None) -> str:

    # TODO: this obviously is hardcoded; Implement full inferences
    # if '#item+rem+i_lat+is_latn' in rem and rem['#item+rem+i_lat+is_latn']:
    #     return '/' + rem['#item+rem+i_lat+is_latn'] + '/@lat-Latn'
    if '#item+rem+i_lat+is_latn' in rem and rem['#item+rem+i_lat+is_latn']:
        return rem['#item+rem+i_lat+is_latn']
    if '#item+rem+i_eng+is_latn' in rem and rem['#item+rem+i_eng+is_latn']:
        return '/' + rem['#item+rem+i_eng+is_latn'] + '/@eng-Latn'
    if '#item+rem+i_mul+is_zyyy' in rem and rem['#item+rem+i_mul+is_zyyy']:
        return rem['#item+rem+i_mul+is_zyyy']

    return ''


def numerordinatio_trivium_sarcina(
        trivium: str, de_codex: str) -> str:
    """numerordinatio_trivium_sarcina

    Args:
        trivium (str): /Path to file/@eng-Latn
        de_codex (str): /Numerordinatio/@eng-Latn

    Returns:
        str: sarcina

    Exemplōrum gratiā (et Python doctest, id est, testum automata)
        >>> numerordinatio_trivium_sarcina(
        ...    '1603/84/1/1603_84_1.~1/0.nnx.tm.hxl.csv', '1603_84_1')
        '~1'

        >>> numerordinatio_trivium_sarcina(
        ...    '1603/84/1/1603_84_1.tm.hxl.csv', '1603_84_1')
    """
    radix = numerordinatio_neo_separatum(de_codex, '/')

    temp1 = trivium.replace(radix + '/', '')
    if temp1.find('~') > -1 and temp1.find('/') > -1:
        temp2 = temp1.split('/')[0]
        if temp2.find('~') > -1:
            return '~' + temp2.split('~')[1]

    return None


def trivium_annexum_numerordinatio_locali(
        trivium: str) -> str:
    """trivium_annexum_numerordinatio_locali

    Args:
        trivium (str): /Path to file/@eng-Latn
        de_codex (str): /Numerordinatio/@eng-Latn

    Returns:
        str: numerordinatio_locali

    Exemplōrum gratiā (et Python doctest, id est, testum automata)
        >>> trivium_annexum_numerordinatio_locali(
        ...    '1603/84/1/1603_84_1.~1/0.nnx.tm.hxl.csv')
        '0'
        >>> trivium_annexum_numerordinatio_locali(
        ...    '1603/84/1/1603_84_1.~1/0~0.svg')
        '0'
    """
    if trivium.find('/') > -1:
        trivium = trivium.split('/').pop()
    if trivium.find('.') > -1:
        trivium = trivium.split('.').pop(0)
    if trivium.find('~') > -1:
        trivium = trivium.split('~').pop(0)

    return trivium


def res_interlingualibus_formata(rem: dict, query) -> str:

    if not rem[query]:
        return ''

    if query.find('#status+conceptum+definitionem') > -1:
        return "{0} +++<sup><em>(1-100)</em></sup>+++".format(
            rem[query])
    if query.find('#status+conceptum+codicem') > -1:
        return "{0} +++<sup><em>(1-100)</em></sup>+++".format(
            rem[query])

    if query.find('+ix_wikiq') > -1:
        return "https://www.wikidata.org/wiki/{0}[{0}]".format(
            rem[query])
    if query.find('+ix_ta98') > -1:
        term = rem[query].replace('A', '')
        resultatum = (
            'link:++https://ifaa.unifr.ch/Public/EntryPage/'
            'TA98%20Tree/Entity%20TA98%20EN/{0}%20Entity%20TA98%20EN.htm++['
            '{1}]').format(term, rem[query])
        return resultatum

    # https://ifaa.unifr.ch/Public/EntryPage/TA98%20Tree/Entity%20TA98%20EN/01.1.00.013%20Entity%20TA98%20EN.htm

    return rem[query]

# /Educated guess on stability (1-100) of local identifier
# if dictionary still in use in a century/
# #status+conceptum+codicem
# /Educated guess on comprehensibility (1-100) of concept/
# #status+conceptum+definitionem


def qhxl(rem: dict, query: str):
    for clavem, rem_item in rem.items():
        # print(clavem, rem_item, clavem.find(query))
        if clavem.find(query) > -1:
            return rem_item
    return None

# About github ASCIDoctor
#  - https://gist.github.com/dcode/0cfbf2699a1fe9b46ff04c41721dda74


class Codex:
    """Cōdex

    Trivia:
    - Cōdex, m, s, (Nominative), https://en.wiktionary.org/wiki/codex
    - https://latin.stackexchange.com/questions/2102
      /most-accurate-latin-word-for-book-in-this-context


    - verbīs, n, pl, (Dative) https://en.wiktionary.org/wiki/verbum#Latin
    - https://en.wiktionary.org/wiki/terminus#Latin


    - verba, n, pl (Nominative), https://en.wiktionary.org/wiki/verbum#Latin
    - conceptiō, f, s, (Nominative),
      https://en.wiktionary.org/wiki/conceptio#Latin


    Exemplōrum gratiā (et Python doctest, id est, testum automata)
        # >>> codex = Codex('1603_25_1')
        # >>> codex.sarcinarum.__dict__
    """

    def __init__(
        self,
        de_codex: str,
        objectivum_linguam: str = None,
        auxilium_linguam: list = None,
        formatum: str = 'asciidoctor',

    ):

        self.de_codex = de_codex
        self.formatum = formatum
        if objectivum_linguam:
            self.objectivum_linguam = objectivum_linguam
        if auxilium_linguam:
            self.auxilium_linguam = auxilium_linguam

        self.dictionaria_linguarum = DictionariaLinguarum()
        self.m1603_1_1__de_codex = self._init_1603_1_1()
        self.codex = self._init_codex()
        # self.annexa = self._init_annexa()

        self.annexis = CodexAnnexis(self, self.de_codex)
        self.sarcinarum = CodexSarcinarumAdnexis(self.de_codex)
        self.usus_linguae = set()
        self.usus_ix_qcc = set()

    def _init_1603_1_1(self):
        numerordinatio_neo_codex = numerordinatio_neo_separatum(
            self.de_codex, ':')
        numerordinatio_1603_1_1 = '1603:1:1'
        fullpath = numerordinatio_neo_separatum(numerordinatio_1603_1_1, '/')
        fullpath = fullpath + '/' + \
            numerordinatio_neo_separatum(numerordinatio_1603_1_1, '_')
        fullpath = fullpath + '.no1.tm.hxl.csv'
        # print('test', test, self.de_codex)
        # print('fullpath', fullpath)
        with open(fullpath) as csvfile:
            reader = csv.DictReader(csvfile)
            for lineam in reader:
                if lineam['#item+rem+i_qcc+is_zxxx+ix_n1603'] \
                        == numerordinatio_neo_codex:
                    return lineam

        raise ValueError("{0} not defined on 1603_1_1 [{1}]".format(
            self.de_codex, fullpath))

    def _init_codex(self):
        # numerordinatio = numerordinatio_neo_separatum(self.de_codex, ':')
        basepath = numerordinatio_neo_separatum(self.de_codex, '/')
        basepath = basepath + '/' + \
            numerordinatio_neo_separatum(self.de_codex, '_')
        fullpath_no1 = basepath + '.no1.tm.hxl.csv'
        fullpath_no11 = basepath + '.no11.tm.hxl.csv'

        if os.path.exists(fullpath_no11):
            fullpath = fullpath_no11
        else:
            fullpath = fullpath_no1

        codex_lineam = []
        with open(fullpath) as csvfile:
            reader = csv.DictReader(csvfile)
            for lineam in reader:
                codex_lineam.append(lineam)

        return codex_lineam

    def codex_appendici(self) -> list:
        """cōdex appendicī /book appendix/@eng-Latn

        Trivia:
        - cōdex, m, s, (Nominative), https://en.wiktionary.org/wiki/codex#Latin
        - appendicī, f, s, (Dative), https://en.wiktionary.org/wiki/appendix#Latin

        Returns:
            [list]:
        """
        resultatum = []

        resultatum.append("[appendix]")
        resultatum.append("= //Open issues on exported PDF format//@eng-Latn")
        resultatum.append('')

        resultatum.append('')
        resultatum.append("=== //Documentation about how to use the machine-readable dictionaries//@eng-Latn")
        resultatum.append('')
        resultatum.append('Is necessary to give a quick introduction (or at least mention) the files generated with this implementer documentation.')
        resultatum.append('')

        resultatum.append("=== //Missing fonts to render all term variants//@eng-Latn")
        resultatum.append('The generated PDF does not include all necessary fonts.')
        resultatum.append('Here potential strategy to fix it https://github.com/asciidoctor/asciidoctor-pdf/blob/main/docs/theming-guide.adoc#custom-fonts')

        resultatum.append('')
        resultatum.append("=== //Reliability statuses//@eng-Latn")
        resultatum.append('')
        resultatum.append('Currently, the reliability of numeric statuses are not well explained on PDF version.')

        # resultatum.append("=== First Subsection")
        # resultatum.append("")
        # resultatum.append("=== Second Subsection")
        # resultatum.append("")
        # resultatum.append("[appendix]")
        # resultatum.append("= Second Appendix")

        return resultatum

    def codex_capiti(self) -> list:
        """cōdex capitī /book header/@eng-Latn

        Trivia:
        - cōdex, m, s, (Nominative), https://en.wiktionary.org/wiki/codex#Latin
        - capitī, n, s, (Dative), https://en.wiktionary.org/wiki/caput#Latin

        Returns:
            [list]:
        """
        resultatum = []
        # resultatum.append(self._caput())
        # resultatum.append(
        #     '# [`' +
        #     self.m1603_1_1__de_codex['#item+rem+i_qcc+is_zxxx+ix_n1603'] +
        #     '`] ' + self.m1603_1_1__de_codex['#item+rem+i_mul+is_zyyy'])
        # resultatum.append(
        #     '= [`' +
        #     self.m1603_1_1__de_codex['#item+rem+i_qcc+is_zxxx+ix_n1603'] +
        #     '`] ' + self.m1603_1_1__de_codex['#item+rem+i_mul+is_zyyy'])
        resultatum.append("= Cōdex [{0}]: {1}".format(
            self.m1603_1_1__de_codex['#item+rem+i_qcc+is_zxxx+ix_n1603'],
            self.m1603_1_1__de_codex['#item+rem+i_mul+is_zyyy']
        ))
        resultatum.append(":doctype: book")
        resultatum.append(":title: Cōdex [{0}]: {1}".format(
            self.m1603_1_1__de_codex['#item+rem+i_qcc+is_zxxx+ix_n1603'],
            self.m1603_1_1__de_codex['#item+rem+i_mul+is_zyyy']
        ))
        resultatum.append(":lang: la")
        resultatum.append(":toc:")
        resultatum.append(":toclevels: 4")
        # resultatum.append(":orgname: Etica.AI")
        # resultatum.append(":version: 1.2.3")

        # TODO: see the rest from here
        # https://docs.asciidoctor.org/asciidoctor/latest/localization-support/
        resultatum.append(":toc-title: Tabula contentorum")
        resultatum.append(":table-caption: Tabula")
        resultatum.append(":figure-caption: Pictūra")
        resultatum.append(":example-caption: Exemplum")
        # https://en.wiktionary.org/wiki/renovatio
        resultatum.append(":last-update-label: Renovatio")
        # https://en.wiktionary.org/wiki/versio#Latin
        resultatum.append(":version-label: Versiō")

        # @see https://docs.asciidoctor.org/asciidoc/latest/sections/appendix/
        # https://en.wiktionary.org/wiki/appendix#Latin
        resultatum.append(":appendix-caption: Appendix")

        resultatum.append("\n")
        resultatum.append("toc::[]")

        # TODO: potential list of images
        # @see https://github.com/asciidoctor/asciidoctor/issues/2189
        # @see https://github.com/Alwinator/asciidoctor-lists

        return resultatum

    def codex_praefatio(self) -> list:
        """cōdex praefātiōnī /book preface/@eng-Latn

        Trivia:
        - cōdex, m, s, (Nominative), https://en.wiktionary.org/wiki/codex#Latin
        - praefātiōnī, f, s, (Dative), https://en.wiktionary.org/wiki/praefatio

        Returns:
            [list]:
        """
        resultatum = []
        resultatum.append("[id=0_999_1603_1]")
        # resultatum.append("== [0] /Praefātiō/@lat-Latn \n")
        resultatum.append("== Praefātiō \n")
        # resultatum.append("<a id='0' href='#0'>§ 0</a> \n")

        # https://en.wiktionary.org/wiki/translatio#Latin
        resultatum.append("=== //Cōdex trānslātiōnēs//")

        resultatum.extend(self.conceptum_ad_tabula_verbis(
            self.m1603_1_1__de_codex))

        resultatum.append("=== //Rēs interlinguālibus//")

        resultatum.extend(self.conceptum_ad_tabula_codicibus(
            self.m1603_1_1__de_codex))

        # resultatum.append(
        #     numerordinatio_lineam_hxml5_details(
        #         self.m1603_1_1__de_codex,
        #         self.m1603_1_1__de_codex['#item+rem+i_qcc+is_zxxx+ix_n1603']
        #     ))

        # if len(self.usus_ix_qcc):
        #     resultatum.append("+++<!-- @TODO {0} -->+++".format(
        #         str(self.usus_ix_qcc)))

        if len(self.usus_linguae):
            # resultatum.append("### Linguae in cōdex")
            # resultatum.append("=== Linguae in cōdex")
            # resultatum.append(str(self.usus_linguae))

            resultatum.extend(self.dictionaria_linguarum.imprimere(
                list(self.usus_linguae)))

        # resultatum.append("----\n")


            # resultatum.append("'''''\n")
            # resultatum.append("----\n")

        return resultatum

    # def codex_indici(self) -> list:
    #     """cōdex indicī /book index/@eng-Latn

    #     @deprecated /use ASCIDoctor [toc]/@eng-Latn

    #     Trivia:
    #     - cōdex, m, s, (Nominative), https://en.wiktionary.org/wiki/codex#Latin
    #     - indicī, m, s, (Dative), https://en.wiktionary.org/wiki/index#Latin

    #     Returns:
    #         [list]:
    #     """

    #     resultatum = []
    #     # resultatum.append('----')
    #     # resultatum.append("'''''")
    #     resultatum.append('')
    #     # resultatum.append("- <a href='#0'>[0] /Praefātiō/@lat-Latn</a>")
    #     resultatum.append("* +++<a href='#0'>[0] /Praefātiō/@lat-Latn</a>+++")
    #     for item in self.codex:
    #         codicem_loci = item['#item+conceptum+codicem']

    #         if codicem_loci.find('0_999') == 0:
    #             continue

    #         nomen = numerordinatio_nomen(item)
    #         codicem_normale = numerordinatio_neo_separatum(codicem_loci, '_')
    #         codicem_ordo = numerordinatio_ordo(codicem_loci)

    #         # resultatum.append("{2}- <a href='#{0}'>[{0}] {1}</a>".format(
    #         #     codicem_normale, nomen, ('  ' * (codicem_ordo - 1))))
    #         # resultatum.append("{2}- <a href='#{0}'>[{0}] {1}</a>".format(
    #         #     codicem_normale, nomen, ('  ' * (codicem_ordo - 1))))
    #         # resultatum.append("{2} <a href='#{0}'>[{0}] {1}</a>".format(
    #         #     codicem_normale, nomen, ('*' * (codicem_ordo - 1))))
    #         resultatum.append("{2} +++<a href='#{0}'>[{0}] {1}</a>+++".format(
    #             codicem_normale, nomen, ('*' * (codicem_ordo))))
    #     resultatum.append('')
    #     # resultatum.append('----')
    #     # resultatum.append("'''''")
    #     resultatum.append('')
    #     return resultatum

    def codex_corpori(self) -> list:
        """cōdex corporī /book body/@eng-Latn

        Trivia:
        - cōdex, m, s, (Nominative), https://en.wiktionary.org/wiki/codex#Latin
        - corporī, n, s, (Dative), https://en.wiktionary.org/wiki/corpus#Latin

        Returns:
            [list]:
        """
        resultatum = []

        # TODO: create the codex
        # resultatum.append("[id='{0}']".format(codicem_normale))
        # resultatum.append("== [{0}] {1}".format(
        #     self.m1603_1_1__de_codex['#item+rem+i_qcc+is_zxxx+ix_n1603'],
        #     self.m1603_1_1__de_codex['#item+rem+i_mul+is_zyyy']
        # ))
        resultatum.append("== {0}".format(
            self.m1603_1_1__de_codex['#item+rem+i_mul+is_zyyy']
        ))

        picturae = self.annexis.quod_picturae(numerordinatio_locali='0')
        if picturae:
            codicem_ordo = 2
            # resultatum.append(
            #     ('#' * (codicem_ordo + 2)) + ' ' +
            #     '<span lang="la">Annexa</span>'
            # )
            # resultatum.append(
            #     ('#' * (codicem_ordo + 3)) + ' ' +
            #     '<span lang="la">Pictūrae</span>'
            # )
            resultatum.append('[discrete]')
            resultatum.append(
                ('=' * (codicem_ordo + 2)) + ' ' +
                'Annexa'
            )
            resultatum.append('[discrete]')
            resultatum.append(
                ('=' * (codicem_ordo + 3)) + ' ' +
                'Pictūrae'
            )
            for item in picturae:

                trivium = item.quod_temp_rel_pic()
                titulum = item.quod_temp_titulum()
                link = item.quod_temp_link()
                # resultatum.append('![{0}]({1})\n'.format(titulum, trivium))
                resultatum.append(
                    'image::{1}[title="{0}"]\n'.format(titulum, trivium))
                if link:
                    resultatum.append(
                        'link:{1}[{0}]\n'.format(titulum, link))
                else:
                    resultatum.append('{0}\n'.format(titulum))

        for item in self.codex:
            codicem_loci = item['#item+conceptum+codicem']

            if codicem_loci.find('0_999') == 0:
                continue

            nomen = numerordinatio_nomen(item)
            codicem_normale = numerordinatio_neo_separatum(codicem_loci, '_')
            codicem_ordo = numerordinatio_ordo(codicem_loci)
            # resultatum.append(
            #     ('#' * (codicem_ordo + 1)) +
            #     ' [`' + codicem_loci + '`] ' + nomen + "\n"
            # )
            resultatum.append("[id='{0}']".format(codicem_normale))
            resultatum.append(
                ('=' * (codicem_ordo + 2)) +
                ' [`' + codicem_loci + '`] ' + nomen + "\n"
            )
            # resultatum.append(
            #     "+++<a id='{0}' href='#{0}'>§ {0}</a>+++".format(codicem_normale))

            resultatum.append("\n")
            resultatum.append(numerordinatio_summary(item))
            resultatum.extend(self.conceptum_ad_tabula_codicibus(item))
            resultatum.append("\n")
            resultatum.extend(self.conceptum_ad_tabula_verbis(item))
            resultatum.append("\n")
            # resultatum.append(numerordinatio_lineam_hxml5_details(item))

            picturae = self.annexis.quod_picturae(
                numerordinatio_locali=codicem_normale)
            if picturae:

                resultatum.append('[discrete]')
                resultatum.append(
                    ('=' * (codicem_ordo + 3)) + ' ' +
                    'Annexa'
                )
                resultatum.append('[discrete]')
                resultatum.append(
                    ('=' * (codicem_ordo + 4)) + ' ' +
                    'Pictūrae'
                )
                for item in picturae:
                    trivium = item.quod_temp_rel_pic()
                    titulum = item.quod_temp_titulum()
                    link = item.quod_temp_link()
                    resultatum.append(
                        'image::{1}[title="{0}"]\n'.format(titulum, trivium))
                    # resultatum.append('![{0}]({1})\n'.format(titulum, trivium))
                    if link:
                        resultatum.append(
                            'link:{1}[{0}]\n'.format(titulum, link))
                    # else:
                    #     resultatum.append('{0}\n'.format(titulum))

            # resultatum.append("<!-- " + str(item) + " -->")
            resultatum.append("\n")

        return resultatum

    def conceptum_ad_tabula_verbis(self, rem: dict) -> list:
        """conceptum ad tabula verbīs

        Trivia:
        - conceptum	, n, s, (Nominative),
          https://en.wiktionary.org/wiki/conceptus#Latin
        - tabula, f, s, (Nominative), https://en.wiktionary.org/wiki/tabula
        - verbīs, n, pl, (Dative), https://en.wiktionary.org/wiki/verbum#Latin

        Returns:
            [list]:
        """

        resultatum = []
        resultatum_corpus = []

        for clavem, item_textum in rem.items():
            if clavem.startswith('#item+conceptum'):
                continue
            if clavem.startswith('#status+conceptum'):
                continue
            if clavem.startswith('#item+rem+i_qcc'):
                continue

            if item_textum and len(item_textum) > 0:
                clavem_i18n = clavem
                self.usus_linguae.add(clavem)
                item_text_i18n = item_textum
                dlinguam = self.dictionaria_linguarum.quod(clavem)
                # if dlinguam and dlinguam['#item+rem+i_lat+is_latn']:
                #     clavem_i18n = '<span lang="la">' + \
                #         dlinguam['#item+rem+i_lat+is_latn'] + '</span>'
                if dlinguam and dlinguam['#item+rem+i_lat+is_latn']:
                    clavem_i18n = '' + \
                        dlinguam['#item+rem+i_lat+is_latn'] + ''

                if dlinguam and dlinguam['#item+rem+i_qcc+is_zxxx+ix_wikilngm']:
                    item_text_i18n = '<span lang="{1}">{0}</span>'.format(
                        item_textum,
                        dlinguam['#item+rem+i_qcc+is_zxxx+ix_wikilngm']
                    )
                # resultatum_corpus.append(
                #     "| {0} | {1} |".format(clavem_i18n, item_text_i18n))
                resultatum_corpus.append("| {0}".format(clavem_i18n))
                resultatum_corpus.append("| +++{0}+++".format(item_text_i18n))
                resultatum_corpus.append("")

        if resultatum_corpus:
            resultatum.append("")
            resultatum.append("")
            # resultatum.append('[cols="1,1"]')
            resultatum.append('[%header,cols="~,~"]')
            resultatum.append('|===')
            # resultatum.append(
            #     "| +++<span lang='la'>Lingua de verba</span>+++ | "
            #     "+++<span lang='la'>Verba de conceptiō</span>+++ |")
            # resultatum.append(
            #     "| +++<span lang='la'>Lingua de verba</span>+++")
            # resultatum.append(
            #     "|+++<span lang='la'>Verba de conceptiō</span>+++")
            resultatum.append(
                "| Lingua de verba")
            resultatum.append(
                "| Verba de conceptiō")
            # resultatum.append("| ------------- | ------------- |")
            resultatum.extend(resultatum_corpus)
            resultatum.append('|===')

        return resultatum

    def conceptum_ad_tabula_codicibus(self, rem: dict) -> list:
        """conceptum ad tabula cōdicibus

        Trivia:
        - conceptum	, n, s, (Nominative),
          https://en.wiktionary.org/wiki/conceptus#Latin
        - tabula, f, s, (Nominative), https://en.wiktionary.org/wiki/tabula
        - cōdicibus, m, pl, (Dative), https://en.wiktionary.org/wiki/codex

        Returns:
            [list]:
        """

        resultatum = []
        resultatum_corpus = []

        for clavem, item_textum in rem.items():

            if not clavem.startswith('#item+conceptum') and not \
                    clavem.startswith('#status+conceptum') and not \
                    clavem.startswith('#item+rem+i_qcc'):
                continue
            # if clavem.startswith('#status+conceptum'):
            #     continue
            # if clavem.startswith('#item+rem+i_qcc'):
            #     continue

            if item_textum:
                clavem_i18n = clavem
                item_text_i18n = item_textum
                item_text_i18n = res_interlingualibus_formata(rem, clavem)
                if clavem.startswith('#item+rem+i_qcc'):
                    self.usus_ix_qcc.add(clavem)

                # resultatum_corpus.append("| +++{0}+++".format(clavem_i18n))
                resultatum_corpus.append("| {0}".format(clavem_i18n))
                resultatum_corpus.append("| {0}".format(item_text_i18n))
                resultatum_corpus.append("")

        # - linguālia, https://en.wiktionary.org/wiki/lingualis#Latin
        # -rēs, f, s, (Nominative),
        #   https://en.wiktionary.org/wiki/lingualis#Latin
        if resultatum_corpus:
            resultatum.append("")
            # resultatum.append('[cols="1,1"]')
            # resultatum.append('[%autowidth]')
            # resultatum.append('[cols="25h,~"]')
            resultatum.append('[%header,cols="~,~"]')
            resultatum.append('|===')
            # resultatum.append(
            #     "| +++<span lang='la'>Non lingua</span>+++ | "
            #     #    "<span lang='la'>Verba de conceptiō</span> |")
            #     "+++<span lang='la'>//Rēs interlinguālibus//</span>+++ |")
            # resultatum.append("| +++<span lang='la'>Non lingua</span>+++")
            # resultatum.append("| +++<span lang='la'>//Rēs interlinguālibus//</span>+++")
            resultatum.append("| Non lingua")
            resultatum.append("| //Rēs interlinguālibus//")
            resultatum.append("")

            resultatum.extend(resultatum_corpus)
            resultatum.append('|===')

        return resultatum

    def _sarcinarum(self):
        resultatum = []

        self.sarcinarum
        resultatum.append(
            "<!-- " + str(self.sarcinarum.quod_sarcinarum()) + " -->")

        return resultatum

    def imprimere(self) -> list:
        """imprimere /print/@eng-Latn

        Trivia:
        - cōdex, m, s, (Nominative), https://en.wiktionary.org/wiki/codex#Latin
        - imprimere, v, s, (), https://en.wiktionary.org/wiki/imprimo#Latin
        - pāginae, f, pl, (Nominative), https://en.wiktionary.org/wiki/pagina

        Returns:
            [list]:
        """
        paginae = []
        codex_capiti = self.codex_capiti()
        # codex_indici = self.codex_indici()
        codex_corpori = self.codex_corpori()
        codex_appendici = self.codex_appendici()

        # Compute codex_praefatio last (to receive statistics of others)
        codex_praefatio = self.codex_praefatio()

        paginae.extend(codex_capiti)
        # paginae.extend(codex_indici)
        paginae.extend(codex_praefatio)
        paginae.extend(codex_corpori)
        paginae.extend(codex_appendici)

        # paginae.extend(self.codex_indici())
        # paginae.extend(self.codex_praefatio())
        # paginae.extend(self.codex_corpori())
        # paginae.extend(self._sarcinarum())

        # return "\n".join(paginae)
        return paginae


class CodexAnnexo:
    """Cōdex annexō

    Trivia:
    - cōdex, m, s, (Nominative) https://en.wiktionary.org/wiki/codex#Latin
    - annexō, m, s (Dative) https://en.wiktionary.org/wiki/annexus#Latin
    """

    def __init__(
        self,
        codex: Type['Codex'],
        trivium: str,
    ):
        self.codex = codex
        # self.de_codex = codex.de_codex
        self.trivium = trivium
        self.sarcina = numerordinatio_trivium_sarcina(
            trivium, self.codex.de_codex)

    def quod_temp_rel_pic(self):
        self.radix_codex = numerordinatio_neo_separatum(
            self.codex.de_codex, '/')
        neo_trivium = self.trivium.replace(self.radix_codex + '/', '')
        return neo_trivium

    def quod_temp_titulum(self):
        _sarcina = self.codex.sarcinarum.quod_sarcinarum(self.sarcina)
        titulum = ''

        if _sarcina and 'titulum' in _sarcina['meta'] and \
                _sarcina['meta']['titulum']:
            # titulum = '🖼️ ' + _sarcina['meta']['titulum']
            titulum = _sarcina['meta']['titulum']
        else:
            titulum = 'Sine nomine'

        return titulum

    def quod_temp_link(self):
        _sarcina = self.codex.sarcinarum.quod_sarcinarum(self.sarcina)
        link = ''

        if _sarcina and 'ix_wikip854' in _sarcina['meta'] and \
                _sarcina['meta']['ix_wikip854']:
            link = _sarcina['meta']['ix_wikip854']

        return link


class CodexAnnexis:
    """Cōdex annexīs

    Trivia:
    - cōdex, m, s, (Nominative) https://en.wiktionary.org/wiki/codex#Latin
    - annexīs, m/f/n, pl (Dative) https://en.wiktionary.org/wiki/annexus#Latin
    """

    de_codex = ''
    # complētum	, n, s, (Nominative), https://en.wiktionary.org/wiki/completus
    completum = []
    picturae = None

    def __init__(
        self,
        codex: Type['Codex'],
        de_codex: str,

    ):
        self.codex = codex
        self.de_codex = de_codex
        self.initiari()
        self.initiari_triviis()
        # self.radix, self.sarcinae = self.initiari_triviis()
        # self.picturae = self.initiari_picturae()
        # self.et_al = []

    def initiari(self):
        """initiarī

        Trivia:
        - initiārī, https://en.wiktionary.org/wiki/initio#Latin
        """
        basepath = numerordinatio_neo_separatum(self.de_codex, '/')

        for root, dirnames, filenames in os.walk(basepath):
            for filename in fnmatch.filter(filenames, '*'):
                if filename in ARCHIVA_IGNORATIS:
                    continue
                self.completum.append(os.path.join(root, filename))

    def initiari_triviis(self):
        """initiari_triviīs initiārī triviīs

        Trivia:
        - initiārī, v, pl1, https://en.wiktionary.org/wiki/initio#Latin
        - triviīs, n, pl (Dative) https://en.wiktionary.org/wiki/trivium#Latin

        Returns:
            [dict]:
        """

        radix = ''
        sarcinae = []

        basepath = numerordinatio_neo_separatum(self.de_codex, '/')
        radix = basepath

        for root, dirnames, filenames in os.walk(basepath):
            sarcinae = dirnames
            self.sarcinae = sarcinae

        return [radix, sarcinae]

    def quod_archivum(self) -> List[Type['CodexAnnexo']]:
        """quod_archivum

        Trivia:
        - archīvum, n, s, (nominative) https://en.wiktionary.org/wiki/archivum

        Returns:
            [List[Type['CodexAnnexo']]:
        """
        return self.completum

    def quod_sarcinae(self) -> List[Type[str]]:
        resultatum = []
        # TODO: do it
        return resultatum

    def quod_picturae(
            self,
            numerordinatio_locali: str = None) -> List[Type['CodexAnnexo']]:
        resultatum = []
        for item in self.completum:
            if numerordinatio_locali is not None:
                nl = trivium_annexum_numerordinatio_locali(item)
                if nl != numerordinatio_locali:
                    continue
            if item.endswith(tuple(EXTENSIONES_PICTURIS)):
                resultatum.append(CodexAnnexo(self.codex, item))
        return resultatum
        # debug = []
        # for item in resultatum:
        #     debug.append(item.__dict__)
        # return debug


class CodexSarcinarumAdnexis:
    """Codex Sarcinarum Adnexīs

    //Packages of attachments from Codex//

    Trivia:
    - cōdex, m, s, (Nominative) https://en.wiktionary.org/wiki/codex#Latin
    - adnexīs, m/f/n, pl (Dative) https://en.wiktionary.org/wiki/adnexus#Latin
    - annexīs, m/f/n, pl (Dative) https://en.wiktionary.org/wiki/annexus#Latin
    - sarcinārum, f, pl, (Gengitive) https://en.wiktionary.org/wiki/sarcina

    # >>> ca1603_25_1.quod_picturae()
    """

    # sarcinae = ['todo']
    completum = []
    sarcina_index = []
    sarcina = []

    def __init__(
        self,
        de_codex: str,

    ):
        self.de_codex = de_codex
        self.initiari()
        # print('completum', self.completum)

    def initiari(self):
        """initiarī

        Trivia:
        - initiārī, https://en.wiktionary.org/wiki/initio#Latin
        """
        basepath = numerordinatio_neo_separatum(self.de_codex, '/')

        for root, dirnames, filenames in os.walk(basepath):
            self.completum.extend(dirnames)
            for item in dirnames:
                sarcina_index = item.split('~').pop()
                self.sarcina.append({
                    'index': sarcina_index,
                    'sarcina': item,
                    # @TODO: make this not as hardcoded as it is now
                    'meta': self._quod_meta(
                        root + '/' + item + '/0.nnx.tm.hxl.csv')
                })
                # self.sarcina_index.append(index)

    def _quod_meta(self, trivum):
        meta = {
            'ix_wikip2479': None,  # license
            'ix_wikiq': None,
            'ix_wikip577': None,  # /publication date/
            'ix_wikip1476': None,  # /title of published work.../
            'ix_wikip110': None,  # /illustrator/
            'ix_wikip50': None,   # /author/
            'ix_wikip854': None,  # /reference URL/
            # '__': [],
        }
        # @TODO: allow have more detailed metadata per individual item
        #        for now we're just using global values

        if not os.path.exists(trivum):
            return meta

        with open(trivum) as csvfile:
            reader = csv.DictReader(csvfile)
            for lineam in reader:

                for clavem in meta.keys():
                    ix_item = qhxl(lineam, clavem)
                    if ix_item:
                        meta[clavem] = ix_item

        meta['titulum'] = self._quod_meta_titulum(meta)
        return meta

    def _quod_meta_titulum(self, meta):
        nomen = ''

        if meta['ix_wikip110']:
            nomen += meta['ix_wikip110'] + ' '

        if meta['ix_wikip577']:
            nomen += meta['ix_wikip577'] + ' '

        if meta['ix_wikip1476']:
            nomen += meta['ix_wikip1476'] + ' '

        if meta['ix_wikip2479']:
            nomen += ' [' + meta['ix_wikip2479'] + ']'

        return nomen

    def quod_sarcinarum(self, index: str = None):
        resultatum = []

        for item in self.sarcina:
            if index is not None:
                if item['index'] == index or ('~' + item['index']) == index:
                    return item
            else:
                resultatum.append(item)
        if index is not None:
            raise ValueError('index [{0}] [{1}]'.format(index, self.sarcina))

        return resultatum


class DictionariaLinguarum:
    def __init__(self, fontem_archivum: str = None):
        if fontem_archivum:
            self.D1613_1_51_fontem = fontem_archivum
        else:
            self.D1613_1_51_fontem = NUMERORDINATIO_BASIM + \
                "/1603/1/51/1603_1_51.no1.tm.hxl.csv"

        self.dictionaria_codex = self._init_dictionaria()

    def _init_dictionaria(self):

        datum = {}
        with open(self.D1613_1_51_fontem) as file:
            csv_file = csv.DictReader(file)
            # return list(tsv_file)
            for conceptum in csv_file:
                # print('conceptum', conceptum)
                int_clavem = int(conceptum['#item+conceptum+codicem'])
                datum[int_clavem] = {}
                for clavem, rem in conceptum.items():
                    if not clavem.startswith('#item+conceptum+codicem'):
                        datum[int_clavem][clavem] = rem
        return datum

    def imprimere(self, linguam: list = None) -> list:
        """imprimere /print/@eng-Latn

        Trivia:
        - cōdex, m, s, (Nominative), https://en.wiktionary.org/wiki/codex#Latin
        - imprimere, v, s, (), https://en.wiktionary.org/wiki/imprimo#Latin
        - pāginae, f, pl, (Nominative), https://en.wiktionary.org/wiki/pagina

        Returns:
            [list]:
        """
        resultatum = []
        resultatum_corpus = []
        linguam_clavem = []
        if linguam:
            for item in linguam:
                linguam_clavem.append(
                    item.replace('#item+rem', '')
                )
        # resultatum_corpus.append(linguam_clavem)
        # resultatum_corpus.append(len(linguam_clavem))
        for clavem, lineam in self.dictionaria_codex.items():

            if len(linguam_clavem) > 0:
                if lineam['#item+rem+i_qcc+is_zxxx+ix_hxla'] not in \
                        linguam_clavem:
                    continue

            clavem_i18n = lineam['#item+rem+i_qcc+is_zxxx+ix_uid']
            item_text_i18n = lineam['#item+rem+i_lat+is_latn']
            ix_glottocode = lineam['#item+rem+i_qcc+is_zxxx+ix_glottocode']
            ix_iso639p3a3 = lineam['#item+rem+i_qcc+is_zxxx+ix_iso639p3a3']
            ix_wikiq = lineam['#item+rem+i_qcc+is_zxxx+ix_wikiq+ix_linguam']
            if len(ix_glottocode):
                ix_glottocode = \
                    "https://glottolog.org/resource/languoid/id/{0}[{0}]".format(
                        ix_glottocode)

            if len(ix_iso639p3a3):
                ix_iso639p3a3 = \
                    "https://iso639-3.sil.org/code/{0}[{0}]".format(
                        ix_iso639p3a3)
            if len(ix_wikiq):
                ix_wikiq = \
                    "https://www.wikidata.org/wiki/{0}[{0}]".format(
                        ix_wikiq)
            # resultatum_corpus.append(str(lineam))
            # resultatum_corpus.append(linguam)
            # resultatum_corpus.append(
            #     "| {0} | {1} | {2} | {3} | {4} |".format(clavem_i18n, ix_glottocode, ix_iso639p3a3, ix_wikiq, item_text_i18n))
            resultatum_corpus.append("| {0}".format(clavem_i18n))
            resultatum_corpus.append("| {0}".format(ix_glottocode))
            resultatum_corpus.append("| {0}".format(ix_iso639p3a3))
            resultatum_corpus.append("| {0}".format(ix_wikiq))
            resultatum_corpus.append("| {0}".format(item_text_i18n))
            # resultatum_corpus.append("| {0}".format(clavem_i18n, ix_glottocode, ix_iso639p3a3, ix_wikiq, item_text_i18n))
            # resultatum_corpus.append("| {0}".format(clavem_i18n, ix_glottocode, ix_iso639p3a3, ix_wikiq, item_text_i18n))
            resultatum_corpus.append('')

        if resultatum_corpus:
            resultatum.append("")

            resultatum.append("=== Linguae in cōdex: {0}".format(
                    len(self.dictionaria_codex.keys())))

            # cōdex, m, s, (nominative)
            # tōtālis, m/f, s, (Nominative)
            # linguae, f, s, (Dative)
            resultatum.append(
                "Tōtālis linguae in cōdex: {0}".format(
                    len(self.dictionaria_codex.keys())))
            resultatum.append("")

            resultatum.append('[%header,cols="~,~,~,~,~"]')
            resultatum.append('|===')
            # https://en.wiktionary.org/wiki/latinus#Latin
            # nōmina, n, pl, (Nominative)
            #     shttps://en.wiktionary.org/wiki/nomen#Latin
            # "nōmen Latīnum"
            # https://en.wiktionary.org/wiki/Latinus#Latin
            # resultatum.append(
            #     "| <span lang='la'>Cōdex<br>linguae</span> | "
            #     "<span lang='la'>Glotto<br>cōdicī</span> | "
            #     "<span lang='la'>ISO<br>639-3</span> | "
            #     "<span lang='la'>Wiki QID<br>cōdicī</span> | "
            #     "<span lang='la'>Nōmen Latīnum</span> |")
            # resultatum.append("| --- | --- | --- | --- | --- |")
            resultatum.append("| Cōdex linguae")
            resultatum.append("| Glotto cōdicī")
            resultatum.append("| ISO 639-3")
            resultatum.append("| Wiki QID cōdicī")
            resultatum.append("| Nōmen Latīnum")
            resultatum.append('')
            resultatum.extend(resultatum_corpus)
            resultatum.append('|===')
            resultatum.append("")

        return resultatum

    def quod(self, terminum: str,
             #  factum: str = '#item+rem+i_lat+is_latn',
             clavem: str = None):
        clavem_defallo = [
            '#item+rem+i_qcc+is_zxxx+ix_hxla',
            '#item+rem+i_qcc+is_zxxx+ix_csvsffxm'
        ]
        _clavem = clavem_defallo if clavem is None else [clavem]
        # _clavem = clavem_defallo

        for item in _clavem:
            # print('item', item)
            for _k, linguam in self.dictionaria_codex.items():
                # print('linguam', linguam)
                if terminum.find(linguam[item]) > -1:
                    # return linguam[factum]
                    return linguam

        return None


class DictionariaNumerordinatio:
    def __init__(self):
        self.dictionaria_linguarum = DictionariaLinguarum()

    def _basim(self) -> list:
        resultatum = []
        # ix_regexc | ix_regexvdc | ix_hxlt | ix_hxla | i_mul+is_zyyy
        resultatum.append([
            '{{1603_13_1_2}}',  # hxlhashtag
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '[Rēgula expressiōnī cōnstrūctae (HXL Standard Tag)]',
            ''
        ])
        resultatum.append([
            '{{1603_13_1_3}}',  # HXL Standard attributes
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '[Rēgula expressiōnī cōnstrūctae (HXL Standard attributes)]',
            ''
        ])
        resultatum.append([
            '{{1603_13_1_23}}',  # Trivia: ('2' + '3')
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '[Rēgula expressiōnī cōnstrūctae (HXL Standard ' +
            'composed prefix, Hashtag + attributes)]',
            ''
        ])
        resultatum.append([
            '{{1603_13_1_3_9}}',  # i_ attribute; Trivia: [9] I = 9
            '{{1603_13_1_3}}',  # HXL Standard attributes
            '',
            '',
            '',
            '',
            '',
            '',
            '[Rēgula expressiōnī cōnstrūctae ' +
            '(HXL Standard attributes, language +i_)]',
            ''
        ])
        resultatum.append([
            '{{1603_13_1_3_19}}',  # is_ attribute; Trivia: [19] S = 19
            '{{1603_13_1_3}}',  # HXL Standard attributes
            '',
            '',
            '',
            '',
            '',
            '',
            '[Rēgula expressiōnī cōnstrūctae ' +
            '(HXL Standard attributes, writting system +is_)]',
            ''
        ])
        resultatum.append([
            '{{1603_13_1_3_24}}',  # ix_ attribute; Trivia: [24] X = 24
            '{{1603_13_1_3}}',  # HXL Standard attributes
            '',
            '',
            '',
            '',
            '',
            '',
            '[Rēgula expressiōnī cōnstrūctae (HXL Standard attributes, +ix_)]',
            ''
        ])
        resultatum.append([
            # i_zzz + ix_zzzz attribute; [919] I(9) + S(19)
            '{{1603_13_1_3_919}}',
            '{{1603_13_1_3}}',  # HXL Standard attributes
            '',
            '',
            '',
            '',
            '',
            '',
            '[Rēgula expressiōnī cōnstrūctae ' +
            '(HXL Standard attributes, +i_zzz+is_zzzz)]',
            ''
        ])
        resultatum.append([
            # i_zzz + ix_zzzz attribute; [91924] I(9) + S(19) + X (24)
            '{{1603_13_1_23_91924}}',
            '{{1603_13_1_23}}',
            '',  # '1',
            '',  # '1',
            '',
            '',
            '',
            '',
            '[Rēgula expressiōnī cōnstrūctae ' +
            '(HXL Standard composed prefix ' +
            '#hashtag+rem+i_zzz+is_zzzz+ix_zzzzzzz)]',
            ''
        ])
        resultatum.append([
            '',
            '{{1603_13_1_2}}',
            '',
            '',
            '',
            '#item',
            '',
            '',
            '[Factum ad Rēgula expressiōnī cōnstrūctae (HXL Standard Tag)]',
            ''
        ])
        resultatum.append([
            '',
            '{{1603_13_1_2}}',
            '',
            '',
            '',
            '#status',
            '',
            '',
            '[Status ad Rēgula expressiōnī cōnstrūctae (HXL Standard Tag)]',
            ''
        ])
        resultatum.append([
            '',
            '{{1603_13_1_2}}',
            '',
            '',
            '',
            '#meta',
            '',
            '',
            '[Meta ad Rēgula expressiōnī cōnstrūctae (HXL Standard Tag)]',
            ''
        ])

        resultatum.append([
            '{{1603_13_1_23_3}}',  # [3] C (concept)
            '{{1603_13_1_23}}',
            '1',
            '',
            '',
            '',
            '',
            '',
            '/Concept level information/',
            ''
        ])
        resultatum.append([
            '{{1603_13_1_23_3_10}}',  # 10 local identifier (1), no variant (0)
            '{{1603_13_1_23_3}}',
            '1',
            '',
            '',
            '#item',
            'conceptum+codicem',
            '#item+conceptum+codicem',
            '/Concept level information, local identifier/',
            ''
        ])
        resultatum.append([
            '{{1603_13_1_23_3_11}}',  # [11] local identifier (1), status (1)
            '{{1603_13_1_23_3}}',
            '1',
            '',
            '',
            '#status',
            'conceptum+codicem',
            '#status+conceptum+codicem',
            '/Educated guess on stability (1-100) ' +
            'of local identifier if dictionary still in use in a century/',
            ''
        ])
        resultatum.append([
            '{{1603_13_1_23_3_18}}',  # [11] local identifier (1), metadata (8)
            '{{1603_13_1_23_3}}',
            '1',
            '',
            '',
            '#meta',
            'conceptum+codicem',
            '#meta+conceptum+codicem',
            '/Concept level information, local identifier, metadata/',
            ''
        ])
        resultatum.append([
            '{{1603_13_1_23_3_21}}',
            '{{1603_13_1_23_3}}',
            '1',
            '',
            '',
            '#status',
            'conceptum+definitionem',
            '#status+conceptum+definitionem',
            '/Educated guess on comprehensibility (1-100) of concept/',
            ''
        ])
        resultatum.append([
            '{{1603_13_1_23_91924_26}}',  # [26] Z, external, end of alphabet
            '{{1603_13_1_23_91924}}',
            '1',
            '',
            '',
            '#item',
            'rem+i_qcc+is_zxxx+{{1603_13_1_3_24}}',
            '#item+rem+i_qcc+is_zxxx+{{1603_13_1_3_24}}',
            '/Concept level information, external identifier/',
            ''
        ])
        resultatum.append([
            '{{1603_13_1_23_919}}',
            '{{1603_13_1_23}}',
            '0',
            '1',
            '1',
            '',
            'rem+{{1603_13_1_3_919}}',
            '',
            '/Language and term level information, any type/',
            ''
        ])
        resultatum.append([
            '{{1603_13_1_23_919_1}}',
            '{{1603_13_1_23_919}}',
            '0',
            '0',
            '1',
            '#item',
            'rem+{{1603_13_1_3_919}}',
            '#item+rem+{{1603_13_1_3_919}}',
            '/Language level information, local human label/',
            ''
        ])
        resultatum.append([
            '{{1603_13_1_23_919_13}}',  # [13] M
            '{{1603_13_1_23_919}}',
            '0',
            '0',
            '1',
            '#meta',
            'rem+{{1603_13_1_3_919}}',
            '#meta+rem+{{1603_13_1_3_919}}',
            '/Metadata about the local human label/',
            ''
        ])
        resultatum.append([
            '{{1603_13_1_23_919_19}}',  # Trivia: [19] S, status
            '{{1603_13_1_23_919}}',
            '0',
            '0',
            '1',
            '#status',
            'rem+{{1603_13_1_3_919}}',
            '#status+rem+{{1603_13_1_3_919}}',
            '/Educated guess on reliability (1-100) of the local human label/',
            ''
        ])
        return resultatum

    def _basim_extras(self) -> list:
        resultatum = []
        resultatum.append([
            # https://www.wikidata.org/wiki/Wikidata:Glossary#QID
            # 13_12 is used for Community knowledge/Wikidata
            # 13_12_16 : [16] P
            '{{1603_13_1_23_91924_26_13_12_16}}',
            '{{1603_13_1_23_91924_26}}',
            '1',
            '0',
            '0',
            '#item',
            'rem+i_qcc+is_zxxx+ix_wikiq',
            '#item+rem+i_qcc+is_zxxx+ix_wikiq',
            '/Wikidata, QID/',
            'https://www.wikidata.org/wiki/$1'
        ])
        resultatum.append([
            # https://www.wikidata.org/wiki/Wikidata:Glossary#QID
            # 13_12 is used for Community knowledge/Wikidata
            # 13_12_17 : [17] Q
            '{{1603_13_1_23_91924_26_13_12_17}}',
            '{{1603_13_1_23_91924_26}}',
            '1',
            '0',
            '0',
            '#item',
            'rem+i_qcc+is_zxxx+ix_wikip',
            '#item+rem+i_qcc+is_zxxx+ix_wikip',
            '/Wikidata, P; Property (also attribute)/',
            'https://www.wikidata.org/wiki/Property:$1'
        ])
        return resultatum

    def exportatum(self) -> list:
        resultatum = []
        resultatum.append([
            '#item+conceptum+codicem',
            '#item+rem+i_qcc+is_zxxx+ix_regexc',  # regex constructor
            '#item+rem+i_qcc+is_zxxx+ix_regexvdc',  # Value de regex constr.
            '#item+rem+i_qcc+is_zxxx+ix_tconceptuae',  # if is conceptual
            '#item+rem+i_qcc+is_zxxx+ix_tlinguae',  # if is linguistic
            '#item+rem+i_qcc+is_zxxx+ix_tterminum',  # if varies at term level
            '#item+rem+i_qcc+is_zxxx+ix_hxlt',
            '#item+rem+i_qcc+is_zxxx+ix_hxla',
            '#item+rem+i_qcc+is_zxxx+ix_exemplum',
            '#item+rem+i_mul+is_zyyy',
            '#item+rem+i_qcc+is_zxxx+ix_wikip1630',  # formatter URL
            # '#meta',
        ])

        index = 0
        for item in self._basim():
            # print('item', item)
            index = index + 1
            item.insert(0, str(index))
            resultatum.append(item)

        for item in self._basim_extras():
            # print('item', item)
            index = index + 1
            item.insert(0, str(index))
            resultatum.append(item)

        return resultatum


class A1603z1:
    """1603_1 Main class to load boostrapping tables and explain headers

    [extended_summary]
    """

    def __init__(self):
        # self.D1613_1_51 = self._init_1613_1_51_datum()
        self.dictionaria_codex = DictionariaLinguarum()

        self.ix_csv = []  # Not really used
        self.ix_hxlhstg = []

        self.fontem_separato = ","
        self.resultatum_separato = "\t"

    def _init_1613_1_51_datum(self):
        archivum = NUMERORDINATIO_BASIM + "/1603/1/51/1603_1_51.no1.tm.hxl.csv"
        datum = {}
        with open(archivum) as file:
            # tsv_file = csv.DictReader(file, delimiter="\t")
            csv_file = csv.DictReader(file)
            # return list(tsv_file)
            for conceptum in csv_file:
                # print('conceptum', conceptum)
                int_clavem = int(conceptum['#item+conceptum+codicem'])
                datum[int_clavem] = {}
                for clavem, rem in conceptum.items():
                    if not clavem.startswith('#item+conceptum+codicem'):
                        datum[int_clavem][clavem] = rem

        return datum

    def est_resultatum_separato(self, resultatum_separato: str):
        self.resultatum_separato = resultatum_separato
        return self

    def est_fontem_separato(self, fontem_separato: str):
        self.fontem_separato = fontem_separato
        return self

    def est_lineam(self, lineam):
        # @TODO: this would not work when parsing files strictly not
        #        Numerordinatio
        if self.is_ready():
            return self

        if isinstance(lineam, list):
            self.ix_hxlhstg = lineam
        else:
            self.ix_hxlhstg = lineam.split(self.fontem_separato)
        return self

    # temporary name
    def is_ready(self):
        return len(self.ix_hxlhstg) > 0

    def exportatum(self):
        resultatum = []
        resultatum.append([
            '#item+conceptum+codicem',
            '#item+rem+i_qcc+is_zxxx+ix_hxlhstg',
            '#item+rem+i_qcc+is_zxxx+ix_hxlt',
            '#item+rem+i_qcc+is_zxxx+ix_hxla',
            '#meta',
        ])

        index = 0
        for item in self.ix_hxlhstg:
            # print('item', item)
            index = index + 1
            rem = NumerordinatioItem(
                item, dictionaria_codex=self.dictionaria_codex)

            meta = rem.quod_meta()
            meta_nomen = '' if meta is None else meta['#item+rem+i_lat+is_latn']
            resultatum.append([
                str(index),
                rem.quod_ix_hxlhstg(),
                rem.quod_ix_hxlt(),
                rem.quod_ix_hxla(),
                meta_nomen
            ])
        return resultatum


class NumerordinatioItem:
    """Numerordĭnātĭo item

    _[eng-Latn]
    For an HXL full hashtag, explain what it means
    [eng-Latn]_
    """

    def __init__(
            self, ix_hxlhstg:
            str, dictionaria_codex: Type['DictionariaLinguarum']):
        self.ix_hxlhstg = ix_hxlhstg
        self.dictionaria_codex = dictionaria_codex

    def quod_ix_hxlhstg(self):
        return self.ix_hxlhstg

    def quod_ix_hxla(self):
        return self.ix_hxlhstg.replace(self.quod_ix_hxlt(), '')

    def quod_ix_hxlt(self):
        return self.ix_hxlhstg.split('+')[0]

    def quod_meta(self):
        return self.dictionaria_codex.quod(self.quod_ix_hxla())


class CLI_2600:
    def __init__(self):
        """
        Constructs all the necessary attributes for the Cli object.
        """
        self.pyargs = None
        # self.args = self.make_args()
        # Posix exit codes
        self.EXIT_OK = 0
        self.EXIT_ERROR = 1
        self.EXIT_SYNTAX = 2

    def make_args(self, hxl_output=True):
        parser = argparse.ArgumentParser(
            prog="1603_1",
            description=DESCRIPTION,
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog=__EPILOGUM__
        )

        # https://en.wikipedia.org/wiki/Code_word
        # https://en.wikipedia.org/wiki/Coded_set

        # cōdex verbum tabulae
        # parser.add_argument(
        #     '--actionem',
        #     help='Action to execute. Defaults to codex.',
        #     # choices=['rock', 'paper', 'scissors'],
        #     choices=[
        #         'codex',
        #         'fontem-verbum-tabulae',
        #         'neo-scripturam',
        #     ],
        #     dest='actionem',
        #     required=True,
        #     default='codex',
        #     const='codex',
        #     type=str,
        #     nargs='?'
        # )

        parser.add_argument(
            'infile',
            help='HXL file to read (if omitted, use standard input).',
            nargs='?'
        )

        parser.add_argument(
            '--punctum-separato-de-resultatum',
            help='Character(s) used as separator for generate output. ' +
            'Used only for tabular results. ' +
            'Defaults to tab "\t"',
            dest='resultatum_separato',
            default="\t",
            nargs='?'
        )

        parser.add_argument(
            '--punctum-separato-de-fontem',
            help='Character(s) used as separator from input file ' +
            'Used only for tabular results. ' +
            'Defaults to comma ","',
            dest='fontem_separato',
            default=",",
            nargs='?'
        )

        archivum = parser.add_argument_group(
            "archivum",
            "(DEFAULT USE) Use archive as source (directory not ready yet)")

        archivum.add_argument(
            '--de-archivum',
            help='Parse single archive',
            # metavar='',
            dest='de_archivum',
            # const=True,
            action='store_true',
            # nargs='?'
        )

        dictionaria = parser.add_argument_group(
            "dictionaria",
            "Generate dictionaries. No input required (uses disk 1603 and "
            "999999999/1603 data files)")

        dictionaria.add_argument(
            '--dictionaria-numerordinatio',
            help='Dictionary of all possible values on stricter '
            ' Numerordĭnātĭo (HXLStantad container)',
            # metavar='',
            dest='dictionaria_numerordinatio',
            # const=True,
            action='store_true',
            # nargs='?'
        )

        # https://en.wiktionary.org/wiki/codex#Latin
        codex = parser.add_argument_group(
            "codex",
            "Book/manual creation")

        codex.add_argument(
            '--codex-de',
            help='Generate documentation of dictionaries',
            # metavar='',
            dest='codex_de',
            # const=True,
            nargs='?'
        )

        codex.add_argument(
            '--objectivum-linguam',
            help='Target natural language (use if not auto-detected). '
            'Must be like {ISO 639-3}-{ISO 15924}. Example: arb-Arab. '
            'Default: mul-Zyyy ',
            # metavar='',
            dest='objectivum_linguam',
            default='mul-Zyyy',
            nargs='?'
        )

        codex.add_argument(
            '--auxilium-linguam',
            help='Define auxiliary languages '
            'Must be like {ISO 639-3}-{ISO 15924}. '
            'Example: "ina-Latn,ile-Latn" '
            'Accepts multiple values. ',
            # metavar='',
            dest='auxilium_linguam',
            # default='mul-Zyyy',
            # nargs='?'
            type=lambda x: x.split(',')
        )

        # # --agendum-linguam is a draft. Not 100% implemented
        # parser.add_argument(
        #     '--agendum-linguam', '-AL',
        #     help='(Planned, but not fully implemented yet) ' +
        #     'Restrict working languages to a list. Useful for ' +
        #     'HXLTM to HXLTM or multilingual formats like TBX and TMX. ' +
        #     'Requires: multilingual operation. ' +
        #     'Accepts multiple values.',
        #     metavar='agendum_linguam',
        #     type=lambda x: x.split(',')
        #     # action='append',
        #     # nargs='?'
        # )

        # # --non-agendum-linguam is a draft. Not 100% implemented
        # parser.add_argument(
        #     '--non-agendum-linguam', '-non-AL',
        #     help='(Planned, but not implemented yet) ' +
        #     'Inverse of --agendum-linguam. Document one or more ' +
        #     'languages that should be ignored if they exist. ' +
        #     'Requires: multilingual operation. ' +
        #     'Accept multiple values.',
        #     metavar='non_agendum_linguam',
        #     # action='append',
        #     type=lambda x: x.split(',')
        #     # nargs='?'
        # )

        # dictionaria.add_argument(
        #     '--objectivum-formatum-markdown',
        #     help='(default) Output Markdown format',
        #     # metavar='',
        #     dest='ad_markdown',
        #     # const=True,
        #     action='store_true',
        #     # nargs='?'
        # )

        dictionaria.add_argument(
            '--objectivum-formatum-asciidoctor',
            help='(Default) Output Asciidoctor format',
            # metavar='',
            dest='ad_asciidoctor',
            # const=True,
            action='store_true',
            # nargs='?'
        )

        return parser.parse_args()

    # def execute_cli(self, args, stdin=STDIN, stdout=sys.stdout,
    #                 stderr=sys.stderr):
    def execute_cli(self, pyargs, stdin=STDIN, stdout=sys.stdout,
                    stderr=sys.stderr):
        # print('TODO')

        self.pyargs = pyargs

        a1603z1 = A1603z1()

        # cs1603_1 = cs1603_1()

        # print('self.pyargs', self.pyargs)

        # cs1603_1.est_verbum_limiti(args.verbum_limiti)
        a1603z1.est_resultatum_separato(args.resultatum_separato)
        a1603z1.est_fontem_separato(args.fontem_separato)

        # if self.pyargs.actionem_sparql:
        if self.pyargs.codex_de:
            formatum = 'asciidoctor'
            if self.pyargs.ad_asciidoctor:
                formatum = 'asciidoctor'
            # if self.pyargs.ad_markdown:
            #     formatum = 'markdown'

            codex = Codex(
                self.pyargs.codex_de,
                objectivum_linguam=self.pyargs.objectivum_linguam,
                auxilium_linguam=self.pyargs.auxilium_linguam,
                formatum=formatum
            )
            # data = ['TODO']
            return self.output(codex.imprimere())

        if self.pyargs.dictionaria_numerordinatio:
            dictionaria_numerordinatio = DictionariaNumerordinatio()
            # data = ['TODO']
            return self.output(dictionaria_numerordinatio.exportatum())

        if self.pyargs.de_archivum:

            if stdin.isatty():

                with open(self.pyargs.infile) as csv_file:
                    csv_reader = csv.reader(
                        csv_file, delimiter=args.fontem_separato)
                    line_count = 0
                    for row in csv_reader:
                        if a1603z1.is_ready():
                            break
                        a1603z1.est_lineam(row)

                quod_query = a1603z1.exportatum()
                return self.output(quod_query)

            for line in sys.stdin:
                if a1603z1.is_ready():
                    break
                crudum_lineam = line.replace('\n', ' ').replace('\r', '')
                # TODO: deal with cases were have more than Qcode
                # a1603z1.est_wikidata_q(codicem)
                a1603z1.est_lineam(crudum_lineam)

            quod_query = a1603z1.exportatum()
            # tabulam_numerae = ['TODO']
            # return self.output(tabulam_numerae)
            return self.output(quod_query)

        print('unknow option.')
        return self.EXIT_ERROR

    def output(self, output_collectiom):

        spamwriter = csv.writer(
            sys.stdout, delimiter=self.pyargs.resultatum_separato)
        for item in output_collectiom:
            # TODO: check if result is a file instead of print

            # print(type(item))
            if isinstance(item, int) or isinstance(item, str):
                print(item)
            else:
                spamwriter.writerow(item)

        return self.EXIT_OK


if __name__ == "__main__":

    cli_2600 = CLI_2600()
    args = cli_2600.make_args()
    # pyargs.print_help()

    # args.execute_cli(args)
    cli_2600.execute_cli(args)
