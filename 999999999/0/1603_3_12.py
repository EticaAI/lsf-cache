#!/usr/bin/env python3
# ==============================================================================
#
#          FILE:  1603_3_12.py
#
#         USAGE:  ./999999999/0/1603_3_12.py
#                 ./999999999/0/1603_3_12.py --help
#                 NUMERORDINATIO_BASIM="/dir/ndata" ./999999999/0/1603_3_12.py
#
#   DESCRIPTION:  ---
#
#       OPTIONS:  ---
#
#  REQUIREMENTS:  - python3
#                   - requests[socks]
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
#       CREATED:  2022-01-21 17:07 UTC created. Based on 2600.py
#      REVISION:  ---
# ==============================================================================

# pytest
#    python3 -m doctest ./999999999/0/1603_3_12.py

# Example with proxy
# export HTTP_PROXY="socks5://127.0.0.1:9050"
# export HTTPS_PROXY="socks5://127.0.0.1:9050"

# TODO: https://sinaahmadi.github.io/posts
#       /10-essential-sparql-queries-for-lexicographical-data-on-wikidata.html
# TODO https://jena.apache.org/documentation/rdf-star/
# TODO https://w3c.github.io/rdf-star/reports/#subj_Apache_Jena_

from dataclasses import replace
import os
import sys
import argparse
# from pathlib import Path
from typing import (
    # Type,
    Union
)
from time import sleep
import math
import urllib.parse
import requests

# from itertools import permutations
from itertools import product
# valueee = list(itertools.permutations([1, 2, 3]))
import csv

NUMERORDINATIO_BASIM = os.getenv('NUMERORDINATIO_BASIM', os.getcwd())
NUMERORDINATIO_DEFALLO = int(os.getenv('NUMERORDINATIO_DEFALLO', '60'))  # �
NUMERORDINATIO_MISSING = "�"
DESCRIPTION = """
Wikidata related query building and execution
"""

__EPILOGUM__ = """
------------------------------------------------------------------------------
                            EXEMPLŌRUM GRATIĀ
------------------------------------------------------------------------------
    printf "Q1065\\nQ82151\\n" | {0} --actionem-sparql --query

    printf "Q1065\\nQ82151\\n" | {0} --actionem-sparql --query \
--lingua-divisioni=5 --lingua-paginae=1

    printf "Q1065\\nQ82151\\n" | {0} --actionem-sparql --query \
--lingua-divisioni=5 --lingua-paginae=1 \
{0} --actionem-sparql --wikidata-link

    printf "Q1065\\nQ82151\\n" | {0} --actionem-sparql --query \
--lingua-divisioni=5 --lingua-paginae=1 \
| {0} --actionem-sparql --tsv --ex-http-methodo=GET --cum-somno=0

    printf "Q1065\\nQ82151\\n" | {0} --actionem-sparql --query \
--lingua-divisioni=5 --lingua-paginae=1 \
| {0} --actionem-sparql --tsv

    printf "Q1065\\nQ82151\\n" | {0} --actionem-sparql --query \
--lingua-divisioni=5 --lingua-paginae=1 \
| {0} --actionem-sparql --csv > 999999/0/test.csv

    printf "Q1065\\nQ82151\\n" | {0} --actionem-sparql --query \
--lingua-divisioni=5 --lingua-paginae=1 \
| {0} --actionem-sparql --csv --hxltm > 999999/0/test.tm.hxl.csv

# (Brazilian municipality code (P1585))
    printf "P1585\\n" | {0} --actionem-sparql --de=P --query \
--ex-interlinguis

    printf "P1585\\n" | {0} --actionem-sparql --de=P --query \
--ex-interlinguis --cum-interlinguis=P402,P1566,P1937,P6555,P8119 \
| {0} --actionem-sparql --csv --hxltm \
> 999999/0/P1585~P402+P1566+P1937+P6555+P8119.tm.hxl.csv

    printf "P1585\\n" | {0} --actionem-sparql --de=P --query \
--lingua-divisioni=20 --lingua-paginae=1 --optimum

    printf "P1585\\n" | {0} --actionem-sparql --de=P --query \
--lingua-divisioni=20 --lingua-paginae=1 --optimum \
| {0} --actionem-sparql --csv --hxltm --optimum \
> 999999/0/P1585~P402+P1566+P1937+P6555+P8119.wikiq~1~20.tm.hxl.csv

# @TODO https://www.wikidata.org/wiki/\
Wikidata:SPARQL_query_service/queries/examples#Countries_sorted_by_population

# country (P17)
    printf "P17\\n" | {0} --actionem-sparql --de=P --query \
--ex-interlinguis
------------------------------------------------------------------------------
                            EXEMPLŌRUM GRATIĀ
------------------------------------------------------------------------------
""".format(__file__)

# In Python2, sys.stdin is a byte stream; in Python3, it's a text stream
STDIN = sys.stdin.buffer

# @see https://meta.wikimedia.org/wiki/User-Agent_policy
# @see https://www.mediawiki.org/wiki/API:Etiquette
USER_AGENT = "EticaAI-multilingual-lexicography/2022.3.9 (https://meta.wikimedia.org/wiki/User:EmericusPetro; rocha@ieee.org) 1603_3_12.py/0.1"

# print('getcwd:      ', os.getcwd())
# print('oi', NUMERORDINATIO_BASIM)


# def quod_1613_2_60_datum():
#     datum = {}
#     with open(NUMERORDINATIO_BASIM + "/1613/1603.2.60.no1.tm.hxl.tsv") as file:
#         tsv_file = csv.DictReader(file, delimiter="\t")
#         return list(tsv_file)

# a b aa bb
# printf "30160\n31161\n1830260\n1891267\n" | ./999999999/0/2600.py --actionem-decifram

# a aa aaa
# printf "30160\n1830260\n109830360\n" | ./999999999/0/2600.py --actionem-decifram
# ./999999999/0/1603_3_12.py --actionem-quod-sparql


# SELECT ?item ?itemLabel
# WHERE {
#   # A. Einstein or J.S. Bach
#   VALUES ?item { wd:Q1065 wd:Q82151 wd:Q125761 wd:Q7809}
#   # mother of
#   OPTIONAL { ?item wdt:P25 ?pseudoquery. }
#   SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
# }


def hxltm_hastag_de_csvhxlated(csv_caput: list) -> list:
    """hxltm_hastag_de_csvhxlated [summary]

    Make this type of conversion:
    - 'item__conceptum__codicem' => '#item+conceptum+codicem'
    - 'item__rem__i_ara__is_arab' => '#item+rem+i_ara+is_arab'
    - '' => ''

    Args:
        csv_caput (list): Array of input items

    Returns:
        [list]:
    """
    resultatum = []
    for item in csv_caput:
        if len(item):
            resultatum.append('#' + item.replace('__', '+').replace('?', ''))
        else:
            resultatum.append('')
    return resultatum

# https://stackoverflow.com/questions/43258341/how-to-get-wikidata-labels-in-more-than-one-language


class CS1603z3z12:
    """ [summary]

    - https://en.wikibooks.org/wiki/SPARQL

    [extended_summary]
    """

    # For items we already use and which SPARQL would return
    # 'http://www.wikidata.org/entity/Q123' instead of 'Q123'
    # Examples:
    # - https://www.wikidata.org/wiki/Property:P131
    # - https://www.wikidata.org/wiki/Property:P17
    wikidata_entity_p = [
        'P17',
        'P131'
    ]

    def __init__(self):
        self.D1613_1_51 = self._init_1613_1_51_datum()

        self.linguae_limitibus = 1000
        self.linguae_paginarum_limitibus = 1
        # langpair_full = self._query_linguam()
        # self.D1613_1_51_langpair = self._query_linguam_limit(langpair_full)
        self.D1613_1_51_langpair = []
        # self.scientia_de_scriptura = {}
        # self.scientia_de_scriptura = self.D1613_2_60
        # self.cifram_signaturae = 6  # TODO: make it flexible
        # self.codex_verbum_tabulae = []
        # self.verbum_limiti = 2
        self.resultatum_separato = "\t"

        self.qid = []
        self.pid = []
        self.identitas_ex_wikiq = False
        self.ex_interlinguis = False
        self.cum_interlinguis = []

    def _init_1613_1_51_datum(self):
        # archivum = NUMERORDINATIO_BASIM + "/1613/1603_2_60.no1.tm.hxl.tsv"
        # archivum = NUMERORDINATIO_BASIM + "/1603/17/2/60/1613_17_2_60.no1.tm.hxl.tsv"
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
                if conceptum['#item+conceptum+codicem'].startswith('0_'):
                    continue
                if not conceptum['#item+rem+i_qcc+is_zxxx+ix_wikilngm']:
                    continue

                for clavem, rem in conceptum.items():
                    if not clavem.startswith('#item+conceptum+codicem'):
                        datum[int_clavem][clavem] = rem

        return datum

    def _query_linguam(self):
        resultatum = []

        for clavem, rem in self.D1613_1_51.items():
            # for clavem, rem in enumerate(self.D1613_1_51):
            # print('clavem rem', clavem, rem)
            if '#item+rem+i_qcc+is_zxxx+ix_wikilngm' not in rem or \
                    '#item+rem+i_qcc+is_zxxx+ix_csvsffxm' not in rem:
                continue
            resultatum.append([
                rem['#item+rem+i_qcc+is_zxxx+ix_wikilngm'],
                'item__rem' + rem['#item+rem+i_qcc+is_zxxx+ix_csvsffxm'],
            ])
        # print(self.D1613_1_51)
        # print('resultatum', resultatum)
        return resultatum

    def _query_linguam_limit(self, langpair_full: list):
        # resultatum = []

        if self.lingua_divisioni < 2:
            return langpair_full

        # @see https://stackoverflow.com/questions/312443
        # /how-do-you-split-a-list-into-evenly-sized-chunks
        # def chunks(lst, n):
        #     """Yield successive n-sized chunks from lst."""
        #     for i in range(0, len(lst), n):
        #         yield lst[i:i + n]
        # if langpair_full

        # def chunks(lst, n):
        #     """Yield successive n-sized chunks from lst."""
        #     for i in range(0, len(lst), n):
        #         yield lst[i:i + n]
        # import math

        divisio_numero = math.ceil(len(langpair_full) / self.lingua_divisioni)

        def chunks(l, n):
            n = max(1, n)
            return (l[i:i+n] for i in range(0, len(l), n))

        # limited = list(chunks(langpair_full, self.lingua_divisioni))
        limited = list(chunks(langpair_full, divisio_numero))

        limited_group = limited[self.lingua_paginae - 1]
        # limited = chunks(langpair_full, self.linguae_limitibus)
        # raise ValueError(limited_group)
        # raise ValueError([limited_group, limited])
        return limited_group

        # # print('resultatum', resultatum)
        # return resultatum

    def est_resultatum_separato(self, resultatum_separato: str):
        self.resultatum_separato = resultatum_separato
        return self

    def est_lingua_divisioni(
            self, lingua_divisioni: Union[str, int]):
        self.lingua_divisioni = int(lingua_divisioni)
        return self

    def est_lingua_paginae(
            self, lingua_paginae: Union[str, int]):
        self.lingua_paginae = int(lingua_paginae)
        return self

    def est_wikidata_q(self, wikidata_codicem: str):
        if wikidata_codicem not in self.qid:
            self.qid.append(wikidata_codicem)

        return self

    def est_wikidata_p(self, wikidata_codicem: str):
        if wikidata_codicem not in self.pid:
            self.pid.append(wikidata_codicem)

        return self

    def est_wikidata_p_identitas_ex_wikiq(self, statum: bool = True):
        self.identitas_ex_wikiq = statum

    def est_wikidata_p_interlinguis(self, statum: bool = True):
        self.ex_interlinguis = statum

    def est_wikidata_p_cum_interlinguis(self, cum_interlinguis: list = None):
        if cum_interlinguis and len(cum_interlinguis):
            for item in cum_interlinguis:
                if len(item.strip()) > 0:
                    self.cum_interlinguis.append(item.upper().replace('P', ''))
            self.cum_interlinguis = sorted(self.cum_interlinguis, key=int)

        return self

    def query_q(self, optimum: bool = False):
        langpair_full = self._query_linguam()
        self.D1613_1_51_langpair = self._query_linguam_limit(langpair_full)

        qid = ['wd:' + x for x in self.qid if isinstance(x, str)]
        # select = '?item ' + " ".join(self._query_linguam())

        # select = ['(?item AS ?item__conceptum__codicem)']
        select = [
            '(STRAFTER(STR(?item), "entity/") AS ?item__conceptum__codicem)']

        filter_otional = []
        for pair in self.D1613_1_51_langpair:
            select.append('?' + pair[1])
            # filter_otional.append(
            #     '?item rdfs:label ?' +
            #     pair[1] + ' filter (lang(?' + pair[1] +
            #     ') = "' + pair[0] + '").'
            # )
            filter_otional.append(
                'OPTIONAL { ?item rdfs:label ?' +
                pair[1] + ' filter (lang(?' + pair[1] +
                ') = "' + pair[0] + '"). }'
            )
        filter_otional_done = ['  ' + x for x in filter_otional]
        # print('select', self.D1613_1_51_langpair)
        # print('select', select)
        # print('filter_otional', filter_otional)
        if optimum:
            est_optimum = '# '
        else:
            est_optimum = ''

        term = """
SELECT {select}
WHERE
{{
  VALUES ?item {{ {qitems} }}
  {est_optimum}bind(xsd:integer(strafter(str(?item), 'Q')) as ?id_numeric) .
{langfilter}
}}
{est_optimum}ORDER BY ASC (?id_numeric)
        """.format(
            qitems=" ".join(qid),
            select=" ".join(select),
            est_optimum=est_optimum,
            langfilter="\n".join(filter_otional_done),
        )
        # """.format(qitems = " ".join(self.qid))

        # [TRY IT ↗]()
        return term

# Teste atual
# SELECT DISTINCT ?item ?itemLabel WHERE {
#   SERVICE wikibase:label {
#     bd:serviceParam wikibase:language "[AUTO_LANGUAGE]".
#   }
#   {
#     SELECT DISTINCT ?item WHERE {
#       {
#         ?item p:P1585 ?statement0.
#         ?statement0 (ps:P1585) _:anyValueP1585.
#         #FILTER(EXISTS { ?statement0 prov:wasDerivedFrom ?reference. })

#         #bind(xsd:integer(strafter(str(?item), 'Q')) as ?id_numeric) .
#       }
#     }
#     #ORDER BY ASC (?id_numeric)
#   }
# }
    def query_p(self, optimum: bool = True):
        langpair_full = self._query_linguam()
        self.D1613_1_51_langpair = self._query_linguam_limit(langpair_full)

        qid = ['wd:' + x for x in self.qid if isinstance(x, str)]

        _pid = self.pid[0]
        # select = '?item ' + " ".join(self._query_linguam())

        # select = ['(?item AS ?item__conceptum__codicem)']
        select = [
            '(STRAFTER(STR(?item), "entity/") AS ?item__conceptum__codicem)']
        # select.append('(?itemLabel AS ?meta____rem__i_por__is_latn)')
        # select = [
        #     '(STRAFTER(STR(?item), "entity/") AS ?item__conceptum__codicem)',
        #     '(STRAFTER(STR(?item), "entity/") AS ?item__rem__i_qcc__is_zxxx__ix_wikiq)'
        # ]
        filter_otional = []
        for pair in self.D1613_1_51_langpair:
            select.append('?' + pair[1])

            filter_otional.append(
                'OPTIONAL { ?item rdfs:label ?' +
                pair[1] + ' filter (lang(?' + pair[1] +
                ') = "' + pair[0] + '"). }'
            )

        filter_optional_done = ['  ' + x for x in filter_otional]

        if optimum:
            est_optimum = '# '
        else:
            est_optimum = ''
#         term = """
# SELECT {select}
# WHERE
# {{
#   VALUES ?item {{ {qitems} }}
#   bind(xsd:integer(strafter(str(?item), 'Q')) as ?id_numeric) .
# {langfilter}
# }}
# ORDER BY ASC (?id_numeric)
#         """.format(
#             qitems=" ".join(qid),
#             select=" ".join(select),
#             langfilter="\n".join(filter_otional_done),
#         )
        term = """
SELECT {select} WHERE {{
  {{
    SELECT DISTINCT ?item WHERE {{
      ?item p:{wikidata_p} ?statement0.
      ?statement0 (ps:{wikidata_p}) _:anyValue{wikidata_p}.
    }}
  }}
{langfilter}
  {est_optimum}bind(xsd:integer(strafter(str(?item), 'Q')) as ?id_numeric) .
}}
{est_optimum}ORDER BY ASC (?id_numeric)
        """.format(
            wikidata_p=_pid,
            qitems=" ".join(qid),
            select=" ".join(select),
            est_optimum=est_optimum,
            langfilter="\n".join(filter_optional_done),
        )

        # [TRY IT ↗]()
        return term

    def query_p_ex_interlinguis(self, optimum: bool = False):
        qid = ['wd:' + x for x in self.qid if isinstance(x, str)]

        _pid = self.pid[0]

        filter_otional = []

        if self.identitas_ex_wikiq:
            select = [
                # '(?wikidata_p_value AS ?item__conceptum__codicem)',
                '(?id_numeric AS ?item__conceptum__codicem)',
                '(STRAFTER(STR(?item), "entity/") AS '
                '?item__rem__i_qcc__is_zxxx__ix_wikiq)'
            ]
            group_by = [
                # '?wikidata_p_value',
                '?id_numeric',
                '?item'
            ]
            order_by = [
                '?item__conceptum__codicem'
            ]
            filter_otional.append(
                "bind(xsd:integer(strafter(str(?item), 'Q')) as ?id_numeric) ."
            )

        else:
            select = [
                '(?wikidata_p_value AS ?item__conceptum__codicem)',
                '(STRAFTER(STR(?item), "entity/") AS '
                '?item__rem__i_qcc__is_zxxx__ix_wikiq)'
            ]
            group_by = [
                '?wikidata_p_value',
                '?item'
            ]
            order_by = [
                '?item__conceptum__codicem'
            ]

        # print('oiii',  self.cum_interlinguis)
        # cum_interlinguis = []
        for item in self.cum_interlinguis:
            # print('item')
            # (GROUP_CONCAT(?subdivisionLabel; separator = ", ") as ?subdivisionLabels)
            # select.append('?item__rem__i_qcc__is_zxxx__ix_wdatap{0}'.format(

            # @TODO maybe this will not work as expected if wikidata_entity_p
            #       have more than one value, but this already is an exception
            if 'P' + item in self.wikidata_entity_p:

                # (GROUP_CONCAT(DISTINCT STRAFTER(STR(?p131_values), "entity/"); separator = "|") AS ?item__rem__i_qcc__is_zxxx__ix_wdatap131)
                # select.append(
                #     '(STRAFTER(STR(?p{0}_values), "entity/") '
                #     'AS ?item__rem__i_qcc__is_zxxx__ix_wdatap{0})'.format(
                #     item
                # ))
                select.append('(GROUP_CONCAT(DISTINCT STRAFTER(STR(?p{0}_values), "entity/"); separator = "|") AS ?item__rem__i_qcc__is_zxxx__ix_wdatap{0})'.format(
                    item
                ))
            else:
                select.append('(GROUP_CONCAT(DISTINCT ?p{0}_values; separator = "|") AS ?item__rem__i_qcc__is_zxxx__ix_wdatap{0})'.format(
                    item
                ))
            # OPTIONAL { ?item wdt:P6555 ?item__rem__i_qcc__is_zxxx__ix_wdatap6555 . }
            filter_otional.append(
                'OPTIONAL { ?item wdt:P' + item +
                ' ?p' + item + '_values . }'
            )
        filter_optional_done = ['  ' + x for x in filter_otional]

        # Not implemented optimum here

        term = """
SELECT DISTINCT {select} WHERE {{
  {{
    SELECT DISTINCT ?item WHERE {{
      ?item p:{wikidata_p} ?statement0.
      ?statement0 (ps:{wikidata_p}) _:anyValue{wikidata_p}.
    }}
  }}
  ?item wdt:{wikidata_p} ?wikidata_p_value .
{optional_filters}
}}
GROUP BY {group_by}
ORDER BY ASC ({order_by})
        """.format(
            wikidata_p=_pid,
            qitems=" ".join(qid),
            select=" ".join(select),
            group_by=" ".join(group_by),
            order_by=" ".join(order_by),
            optional_filters="\n".join(filter_optional_done),
        )

        return term

    def exportatum_sparql(self, optimum: bool = False):
        resultatum = []
        # resultatum.append('#TODO')
        # resultatum.append(str(self.D1613_1_51))
        if len(self.qid) > 0:
            resultatum.append(self.query_q(optimum=optimum))
        if len(self.pid) > 0:
            if self.ex_interlinguis:
                resultatum.append(
                    self.query_p_ex_interlinguis(optimum=optimum))
            else:
                resultatum.append(self.query_p(optimum=optimum))
        return resultatum


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
        # parser = argparse.ArgumentParser(description=DESCRIPTION)
        parser = argparse.ArgumentParser(
            prog="1603_3_12",
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
            '--punctum-separato-de-resultatum',
            help='Character(s) used as separator for generate output.' +
            'Defaults to tab "\t"',
            dest='resultatum_separato',
            default="\t",
            nargs='?'
        )

        neo_codex = parser.add_argument_group(
            "sparql",
            "(DEFAULT USE) SPARQL query")

        neo_codex.add_argument(
            '--actionem-sparql',
            help='Define mode to operate with generation of SPARQL ' +
            'queries',
            metavar='',
            dest='actionem_sparql',
            const=True,
            nargs='?'
        )

        neo_codex.add_argument(
            '--de',
            help='Change default input. Used with --query to change from Q to '
            'P.',
            dest='de',
            nargs='?',
            choices=['Q', 'P'],
            default='Q'
        )
        # linguīs, f, pl, ablativus, https://en.wiktionary.org/wiki/lingua#Latin
        neo_codex.add_argument(
            '--ex-interlinguis',
            help='Change output to return interlingual (codex) only. '
            '',
            metavar='',
            dest='ex_interlinguis',
            const=True,
            nargs='?'
        )

        # cum (+ablativus), https://en.wiktionary.org/wiki/cum#Latin
        neo_codex.add_argument(
            '--cum-interlinguis',
            help='Add additional (but optional value) P. '
            'Accept multiple values (use comma ,). '
            'Used with --ex-interlinguis',
            metavar='',
            dest='cum_interlinguis',
            # default='mul-Zyyy',
            # nargs='?'
            type=lambda x: x.split(',')
        )

        # identitās, f, s, nom., https://en.wiktionary.org/wiki/identitas#Latin
        # ex (+ ablative), https://en.wiktionary.org/wiki/ex#Latin
        # wikiq
        neo_codex.add_argument(
            '--identitas-ex-wikiq',
            help='For query generation totally out of Wikidata P, '
            'use this option if the reference P identifier is not fully '
            'numeric (like brazilian URN Lex and CNPJ)',
            metavar='',
            dest='identitas_ex_wikiq',
            const=True,
            nargs='?'
        )

        neo_codex.add_argument(
            '--query',
            help='Generate SPARQL query',
            metavar='',
            dest='query',
            const=True,
            nargs='?'
        )
        neo_codex.add_argument(
            '--wikidata-link',
            help='Generate query.wikidata.org link (from piped in query)',
            metavar='',
            dest='wikidata_link',
            const=True,
            nargs='?'
        )
        neo_codex.add_argument(
            '--csv',
            help='Generate TSV output (from piped in query)',
            metavar='',
            dest='csv',
            const=True,
            nargs='?'
        )

        neo_codex.add_argument(
            '--tsv',
            help='Generate TSV output (from piped in query)',
            metavar='',
            dest='tsv',
            const=True,
            nargs='?'
        )

        neo_codex.add_argument(
            '--hxltm',
            help='Generate HXL-tagged output (from piped in query). ' +
            'Concepts use #item+conceptum+codicem instead ' +
            'of #item+code+v_wiki_q',
            metavar='',
            dest='hxltm',
            const=True,
            nargs='?'
        )

        # linguae, f, pl, (Nominative) https://en.wiktionary.org/wiki/lingua
        # pāginārum, f, pl, (Gengitive) https://en.wiktionary.org/wiki/pagina
        # dīvīsiōnibus, f, pl, (Dative) https://en.wiktionary.org/wiki/divisio
        # līmitibus, m, pl, (Dative) https://en.wiktionary.org/wiki/limes#Latin
        # //linguae pāginārum līmitibus//

        # lingua, f, s, (Nominative) https://en.wiktionary.org/wiki/lingua#Latin
        # pāginae, f, s, (Dative) https://en.wiktionary.org/wiki/lingua#Latin
        # dīvīsiōnī, f, s, (Dative) https://en.wiktionary.org/wiki/lingua#Latin
        neo_codex.add_argument(
            '--lingua-divisioni',
            help='For the languages on [1603:1:51], how many divisions ' +
            '(or number of chunks) should be done. 1 means no division.' +
            'If using more than 1, use --lingua-paginae do paginate the ' +
            'Options. Default: 1',
            dest='lingua_divisioni',
            metavar='',
            default="1",
            nargs='?'
        )

        neo_codex.add_argument(
            '--lingua-paginae',
            help='If --lingua-divisioni different from 1, defines which page '
            'of languages to return. Default 1.',
            dest='lingua_paginae',
            metavar='',
            default="1",
            nargs='?'
        )

        # cum (+ablativus), https://en.wiktionary.org/wiki/cum#Latin
        # somnō, m, s, ablativus, https://en.wiktionary.org/wiki/somnus#Latin
        neo_codex.add_argument(
            '--cum-somno',
            help='Sleep in seconds. Defaults to "3".'
            'Disable with "0"',
            metavar='cum_somno',
            default="3",
            nargs='?'
        )

        # ex (+ ablativus) https://en.wiktionary.org/wiki/ex#Latin
        # http, https://en.wiktionary.org/wiki/HTTP#English
        # methodō, f, s, ablativus, https://en.wiktionary.org/wiki/methodus
        neo_codex.add_argument(
            '--ex-http-methodo',
            help='HTTP method for SPARQL query execution '
            '(NEEDS FIX: GET request have some bugs)',
            dest='ex_http_methodo',
            nargs='?',
            choices=['POST', 'GET'],
            default='POST'
        )

        # - optimization https://en.wiktionary.org/wiki/optimization
        #   - optimize (1844) Back-formation from optimist.
        #     https://en.wiktionary.org/wiki/optimize#English
        #      - optimist From French optimiste, from Latin optimus (“best”).
        #        https://en.wiktionary.org/wiki/optimist#English
        #        - optimum, n, s, Nominativus,
        #          https://en.wiktionary.org/wiki/optimus#Latin
        neo_codex.add_argument(
            '--optimum',
            help='Undocumented optimizations. '
            'Avoid heavy queries and try to off-load responsability '
            '(like sorting) to client-side operations)',
            metavar='optimum',
            const=True,
            nargs='?'
        )

        # neo_codex.add_argument(
        #     '--verbose',
        #     help='Verbose output',
        #     metavar='verbose',
        #     nargs='?'
        # )
        # if hxl_output:
        #     parser.add_argument(
        #         'outfile',
        #         help='File to write (if omitted, use standard output).',
        #         nargs='?'
        #     )

        # print('oioioi', parser)
        return parser.parse_args()

    # def execute_cli(self, args, stdin=STDIN, stdout=sys.stdout,
    #                 stderr=sys.stderr):
    def execute_cli(self, pyargs, stdin=STDIN, stdout=sys.stdout,
                    stderr=sys.stderr):
        # print('TODO')

        self.pyargs = pyargs

        # cs1603_3_12 = cs1603_3_12()
        cs1603_3_12 = CS1603z3z12()

        # cs1603_3_12 = cs1603_3_12()

        # print('self.pyargs', self.pyargs)

        # cs1603_3_12.est_verbum_limiti(args.verbum_limiti)
        cs1603_3_12.est_resultatum_separato(args.resultatum_separato)
        cs1603_3_12.est_lingua_divisioni(args.lingua_divisioni)
        cs1603_3_12.est_lingua_paginae(
            args.lingua_paginae)

        if self.pyargs.actionem_sparql:
            # print('oi')

            if self.pyargs.query:
                if stdin.isatty():
                    print("ERROR. Please pipe data in. \nExample:\n"
                          "  cat data.txt | {0} --actionem-quod-sparql\n"
                          "  printf \"Q1065\\nQ82151\\n\" | {0} --actionem-quod-sparql"
                          "".format(__file__))
                    return self.EXIT_ERROR

                for line in sys.stdin:
                    codicem = line.replace('\n', ' ').replace('\r', '')
                    # TODO: deal with cases were have more than WikiQ
                    # print(self.pyargs)
                    if self.pyargs.de == 'P':

                        if self.pyargs.cum_interlinguis and \
                                len(self.pyargs.cum_interlinguis):
                            cs1603_3_12.est_wikidata_p_cum_interlinguis(
                                self.pyargs.cum_interlinguis)

                        if self.pyargs.ex_interlinguis == True:
                            cs1603_3_12.est_wikidata_p_interlinguis(True)

                        if self.pyargs.identitas_ex_wikiq == True:
                            cs1603_3_12.est_wikidata_p_identitas_ex_wikiq(True)

                        cs1603_3_12.est_wikidata_p(codicem)

                    elif self.pyargs.de == 'Q':
                        cs1603_3_12.est_wikidata_q(codicem)

                quod_query = cs1603_3_12.exportatum_sparql(
                    optimum=self.pyargs.optimum)
                # tabulam_numerae = ['TODO']
                # return self.output(tabulam_numerae)
                return self.output(quod_query)

            if self.pyargs.wikidata_link:
                if stdin.isatty():
                    print("ERROR. Please pipe data in. \nExample:\n"
                          "  cat data.txt | {0} --actionem-sparql --query | {0} --actionem-sparql --wikidata-link\n"
                          "  printf \"Q1065\\nQ82151\\n\" | {0} --actionem-sparql --query | {0} --actionem-sparql --wikidata-link"
                          "".format(__file__))
                    return self.EXIT_ERROR

                full_query = []
                for line in sys.stdin:
                    full_query.append(line)

                wikidata_backend = "https://query.wikidata.org/#"
                quod_query = wikidata_backend + \
                    urllib.parse.quote("".join(full_query).encode('utf8'))

                print(quod_query)
                return self.EXIT_OK

            if self.pyargs.tsv or self.pyargs.csv:
                if stdin.isatty():
                    print("ERROR. Please pipe data in. \nExample:\n"
                          "  cat data.txt | {0} --actionem-sparql --query | {0} --actionem-sparql --tsv\n"
                          "  printf \"Q1065\\nQ82151\\n\" | {0} --actionem-sparql --query | {0} --actionem-sparql --tsv"
                          "".format(__file__))
                    return self.EXIT_ERROR

                full_query = []
                for line in sys.stdin:
                    full_query.append(line)

                sparql_backend = "https://query.wikidata.org/sparql"
                # sparql_backend = "http://localhost:1234/"
                # @see https://stackoverflow.com/questions/10588644

                # https://www.mediawiki.org/wiki/Wikidata_Query_Service/User_Manual/en#Supported_formats

                if self.pyargs.tsv:
                    separator = "\t"
                    headers = {'Accept': 'text/tab-separated-values'}
                if self.pyargs.csv:
                    separator = ","
                    headers = {'Accept': 'text/csv'}
                if self.pyargs.hxltm:
                    # headers = {'Accept': 'text/tab-separated-values'}
                    headers = {'Accept': 'text/csv'}

                # TODO: make it configurable via command line
                headers['User-Agent'] = USER_AGENT
                headers['Api-User-Agent'] = USER_AGENT

                payload_query = "".join(full_query)
                # Lets put an sleep, 3 seconds, just in case

                # cum_somno = int(self.pyargs.cum_somno)
                if int(self.pyargs.cum_somno) > 0:
                    sleep(int(self.pyargs.cum_somno))

                if self.pyargs.ex_http_methodo == 'POST':
                    r = requests.post(sparql_backend, headers=headers, data={
                        'query': payload_query
                    })
                elif self.pyargs.ex_http_methodo == 'GET':
                    r = requests.get(sparql_backend, headers=headers, data={
                        'query': payload_query
                    })

                # print(r.request.headers)
                # raise NotImplementedError('test')

                # @TODO: --tsv --hxltm is know to be bugged (not sure if
                #        Wikidata result already skip values)

                # def sortq:

                if self.pyargs.hxltm:
                    result_string = r.text.strip()

                    # @TODO: this likely to break with fields with newlines.
                    #        however no testing sample exists at the moment.
                    #        Eventually needs be checked.
                    lines = result_string.splitlines()
                    caput_crudum = lines.pop(0)
                    # print('caput_crudum', caput_crudum)
                    caput = hxltm_hastag_de_csvhxlated(caput_crudum.split(','))

                    if self.pyargs.optimum:
                        if caput[0] == '#item+conceptum+codicem':

                            neo_lines = sorted(
                                lines, key=lambda x: sort_hxltm_q(x))
                            print(separator.join(caput))
                            print("\n".join(neo_lines))
                        else:
                            # Likely error message?
                            print(separator.join(caput))
                            print("\n".join(lines))
                            # raise NotImplementedError('@TODO --optimum')
                    else:
                        print(separator.join(caput))
                        print("\n".join(lines))

                    # reader = csv.reader(lines, delimiter="\t")
                    # caput = hxltm_hastag_de_csvhxlated(next(reader))
                    # print(separator.join(caput))
                    # for row in reader:
                    #     print(separator.join(row))
                else:
                    print(r.text.strip())

                # TODO: generate explicit error messages and return code
                # print(r.content)
                return self.EXIT_OK

        # if self.pyargs.verbum_simplex:
        #     tabulam_multiplicatio = cs1603_3_12.quod_tabulam_multiplicatio()
        #     return self.output(tabulam_multiplicatio)

        # if self.pyargs.codex_completum:
        #     tabulam_multiplicatio = cs1603_3_12.quod_codex()
        #     return self.output(tabulam_multiplicatio)

        # if self.pyargs.neo_scripturam:
        #     scientia = cs1603_3_12.exportatum_scientia_de_scriptura(
        #         args.neo_scripturam_hxl_selectum)
        #     return self.output(scientia)

        # Let's default to full table
        # tabulam_multiplicatio = cs1603_3_12.quod_codex()
        # return self.output(tabulam_multiplicatio)
        print('unknow option.')
        return self.EXIT_ERROR

    def output(self, output_collectiom):
        for item in output_collectiom:
            # TODO: check if result is a file instead of print

            # print(type(item))
            if isinstance(item, int) or isinstance(item, str):
                print(item)
            else:
                print(self.pyargs.resultatum_separato.join(item))

        return self.EXIT_OK


def sort_hxltm_q(lineam: str, index: int = 0, separatum: str = ','):
    """sort_hxltm_q

    Helper to order

    Args:
        item (_type_): _description_

    Returns:
        _type_: _description_
    """
    # Note: not a good idea do this way; it may work for first items
    lineam_list = lineam.split(separatum)
    # if isinstance(clavem, int):
    #     return clavem
    if lineam_list[index].startswith('Q'):
        # return int(clavem.replace('Q', ''))
        # raise ValueError(lineam_list[index])
        return int(lineam_list[index].replace('Q', ''))
    return int(lineam_list[index])


if __name__ == "__main__":

    cli_2600 = CLI_2600()
    args = cli_2600.make_args()
    # pyargs.print_help()

    # args.execute_cli(args)
    cli_2600.execute_cli(args)


# import itertools
# valueee = list(permutations([1, 2, 3]))
# valueee = list(permutations([1, 2, 3]))

# print(valueee)

# cs1603_3_12 = cs1603_3_12()

# # print(quod_1613_2_60_datum())
# # print(cs1603_3_12)

# print('0')
# print(cs1603_3_12.quod_numerordinatio_digitalem('0', True))
# print('05')
# print(cs1603_3_12.quod_numerordinatio_digitalem('05', True))
# print('zz')
# print(cs1603_3_12.quod_numerordinatio_digitalem('zz', True))
