#!/usr/bin/env python3
# ==============================================================================
#
#          FILE:  999999999_54872.py
#
#         USAGE:  ./999999999/0/999999999_54872.py
#                 ./999999999/0/999999999_54872.py --help
#
#   DESCRIPTION:  RUN /999999999/0/999999999_54872.py --help
#
#       OPTIONS:  ---
#
#  REQUIREMENTS:  - python3
#          BUGS:  ---
#         NOTES:  ---
#       AUTHORS:  Emerson Rocha <rocha[at]ieee.org>
# COLLABORATORS:  ---
#       COMPANY:  EticaAI
#       LICENSE:  Public Domain dedication or Zero-Clause BSD
#                 SPDX-License-Identifier: Unlicense OR 0BSD
#       VERSION:  v1.0.0
#       CREATED:  2022-05-17 18:48 UTC based on 999999999_10263485.py
#      REVISION:  ---
# ==============================================================================

import sys
import os
import argparse
import csv
# import re
from pathlib import Path
from os.path import exists

# import json
from typing import Type
import yaml
# import urllib.request
# import requests

STDIN = sys.stdin.buffer

NOMEN = '999999999_54872'

DESCRIPTION = """
{0} Conversor de HXLTM para formatos RDF (alternativa ao uso de 1603_1_1.py, \
que envolve processamento muito mais intenso para datasets enormes)

AVISO: versão atual ainda envolve carregar todos os dados para memória. \
       Considere fornecer tabela HXLTM de entrada que já não contenha \
       informações que pretende que estejam no arquivo gerado.

@see https://github.com/EticaAI/lexicographi-sine-finibus/issues/42

Trivia:
- Q54872, https://www.wikidata.org/wiki/Q54872
  - Resource Description Framework
  - "formal language for describing data models (...)"
""".format(__file__)

__EPILOGUM__ = """
------------------------------------------------------------------------------
                            EXEMPLŌRUM GRATIĀ
------------------------------------------------------------------------------

    cat 999999/0/ibge_un_adm2.tm.hxl.csv | \
{0} --objectivum-formato=text/csv \
--archivum-configurationi-ex-fonti=999999999/0/999999999_268072.meta.yml \
--praefixum-configurationi-ex-fonti=methodus,ibge_un_adm2 \
> 999999/0/ibge_un_adm2.no1.tm.hxl.csv

    cat 999999/0/ibge_un_adm2.tm.hxl.csv | \
{0} --objectivum-formato=application/x-turtle \
--archivum-configurationi-ex-fonti=999999999/0/999999999_268072.meta.yml \
--praefixum-configurationi-ex-fonti=methodus,ibge_un_adm2 \
> 999999/0/ibge_un_adm2.no1.skos.ttl

    cat 999999/0/ibge_un_adm2.tm.hxl.csv | \
{0} --objectivum-formato=application/n-triples \
--archivum-configurationi-ex-fonti=999999999/0/999999999_268072.meta.yml \
--praefixum-configurationi-ex-fonti=methodus,ibge_un_adm2 \
> 999999/0/ibge_un_adm2.no1.n3

------------------------------------------------------------------------------
                            EXEMPLŌRUM GRATIĀ
------------------------------------------------------------------------------
""".format(__file__)

# autopep8 --list-fixes ./999999999/0/999999999_54872.py
# pylint --disable=W0511,C0103,C0116 ./999999999/0/999999999_54872.py

SYSTEMA_SARCINAE = str(Path(__file__).parent.resolve())
PROGRAMMA_SARCINAE = str(Path().resolve())
# ARCHIVUM_CONFIGURATIONI_DEFALLO = [
#     SYSTEMA_SARCINAE + '/' + NOMEN + '.meta.yml',
#     PROGRAMMA_SARCINAE + '/' + NOMEN + '.meta.yml',
# ]

VENANDUM_INSECTUM = bool(os.getenv('VENANDUM_INSECTUM', ''))

# - https://servicodados.ibge.gov.br/api/v1/localidades
#   /distritos?view=nivelado&oorderBy=municipio-id
# - https://servicodados.ibge.gov.br/api/v1/localidades
#   /municipios?view=nivelado&orderBy=id
# METHODUS_FONTI = {
#     'ibge_un_adm2': 'https://servicodados.ibge.gov.br/api' +
#     '/v1/localidades/municipios?view=nivelado&orderBy=id'
# }


class Cli:

    EXIT_OK = 0
    EXIT_ERROR = 1
    EXIT_SYNTAX = 2

    venandum_insectum: bool = False  # noqa: E701

    def __init__(self):
        """
        Constructs all the necessary attributes for the Cli object.
        """

    def make_args(self, hxl_output=True):
        # parser = argparse.ArgumentParser(description=DESCRIPTION)
        parser = argparse.ArgumentParser(
            prog="999999999_54872",
            description=DESCRIPTION,
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog=__EPILOGUM__
        )

        parser.add_argument(
            'infile',
            help='Input file',
            # required=False,
            nargs='?'
        )

        # parser.add_argument(
        #     '--methodus',
        #     help='Modo de operação.',
        #     dest='methodus',
        #     nargs='?',
        #     choices=[
        #         'ibge_un_adm2',
        #         # 'data-apothecae',
        #         # 'hxltm-explanationi',
        #         # 'opus-temporibus',
        #         # 'status-quo',
        #         # 'deprecatum-dictionaria-numerordinatio'
        #     ],
        #     # required=True
        #     default='ibge_un_adm2'
        # )

        # objectīvum, n, s, nominativus,
        #                       https://en.wiktionary.org/wiki/objectivus#Latin
        # fōrmātō, n, s, dativus, https://en.wiktionary.org/wiki/formatus#Latin
        # @see about formats and discussion
        # - https://github.com/semantalytics/awesome-semantic-web#serialization
        # - https://ontola.io/blog/rdf-serialization-formats/
        # - doc.wikimedia.org/Wikibase/master/php/md_docs_topics_json.html
        parser.add_argument(
            '--objectivum-formato',
            help='Formato do arquivo exportado',
            dest='objectivum_formato',
            nargs='?',
            choices=[
                'text/csv',
                # https://www.w3.org/TR/turtle/
                'application/x-turtle',
                # https://www.w3.org/TR/n-triples/
                'application/n-triples',
                # # http://ndjson.org/
                # # https://github.com/ontola/hextuples
                # # mimetype???
                # #  - https://stackoverflow.com/questions/51690624
                # #    /json-lines-mime-type
                # #  - https://github.com/wardi/jsonlines/issues/9
                # #  - https://bugzilla.mozilla.org/show_bug.cgi?id=1603986
                # #  - https://stackoverflow.com/questions/41609586
                # #    /loading-wikidata-dump
                # #    - Uses '.ndjson' as extension
                # 'application/x-ndjson',
            ],
            # required=True
            default='application/x-turtle'
        )

        # archīvum, n, s, nominativus, https://en.wiktionary.org/wiki/archivum
        # cōnfigūrātiōnī, f, s, dativus,
        #                      https://en.wiktionary.org/wiki/configuratio#Latin
        # ex
        # fontī, m, s, dativus, https://en.wiktionary.org/wiki/fons#Latin
        parser.add_argument(
            '--archivum-configurationi-ex-fonti',
            help='Arquivo de configuração .meta.yml da fonte de dados',
            dest='archivum_configurationi',
            nargs='?',
            required=True,
            default=None
        )

        # praefīxum	, n, s, nominativus,
        #                         https://en.wiktionary.org/wiki/praefixus#Latin
        # cōnfigūrātiōnī, f, s, dativus,
        #                      https://en.wiktionary.org/wiki/configuratio#Latin
        # ex
        # fontī, m, s, dativus, https://en.wiktionary.org/wiki/fons#Latin
        parser.add_argument(
            '--praefixum-configurationi-ex-fonti',
            help='Prefixo (separado por vírgula) que contém os metadados que'
            'ajudam a entender como HXLTM deveria ser serializado para RDF',
            dest='praefixum_configurationi',
            nargs='?',
            default=None
        )

        parser.add_argument(
            # '--venandum-insectum-est, --debug',
            '--venandum-insectum-est', '--debug',
            help='Habilitar depuração? Informações adicionais',
            metavar="venandum_insectum",
            dest="venandum_insectum",
            action='store_const',
            const=True,
            default=False
        )

        # parser.add_argument(
        #     'outfile',
        #     help='Output file',
        #     nargs='?'
        # )

        return parser.parse_args()

    def execute_cli(self, pyargs, stdin=STDIN, stdout=sys.stdout,
                    stderr=sys.stderr):
        # self.pyargs = pyargs

        # _infile = None
        # _stdin = None
        configuratio = self.quod_configuratio(
            pyargs.archivum_configurationi, pyargs.praefixum_configurationi)
        if pyargs.venandum_insectum or VENANDUM_INSECTUM:
            self.venandum_insectum = True

        if stdin.isatty():
            _infile = pyargs.infile
            _stdin = False
        else:
            _infile = None
            _stdin = True

        climain = CliMain(
            infile=_infile, stdin=_stdin,
            pyargs=pyargs,
            configuratio=configuratio,
            venandum_insectum=self.venandum_insectum
        )

        if pyargs.objectivum_formato == 'text/csv':
            return climain.actio()
        if pyargs.objectivum_formato == 'application/x-turtle':
            return climain.actio()
            # return self.EXIT_OK
        if pyargs.objectivum_formato == 'application/n-triples':
            return climain.actio()
            # return self.EXIT_OK

        # if pyargs.objectivum_formato == 'uri_fonti':
        #     print(METHODUS_FONTI[pyargs.methodus])
        #     return self.EXIT_OK

        # if pyargs.objectivum_formato == 'json_fonti':
        #     return climain.json_fonti(METHODUS_FONTI[pyargs.methodus])

        # if pyargs.objectivum_formato == 'json_fonti_formoso':
        #     return climain.json_fonti(
        #         METHODUS_FONTI[pyargs.methodus],
        #         formosum=True,
        #         # ex_texto=True
        #     )

        # if pyargs.objectivum_formato in ['csv', 'tsv']:
        #     if json_fonti_texto is None:
        #         json_fonti_texto = climain.json_fonti(
        #             METHODUS_FONTI[pyargs.methodus], ex_texto=True)
        #     # print('json_fonti_texto', json_fonti_texto)
        #     return climain.objectivum_formato_csv(json_fonti_texto)

        # if pyargs.objectivum_formato in [
        #         'hxl_csv', 'hxltm_csv', 'hxl_tsv', 'hxltm_tsv']:
        #     if json_fonti_texto is None:
        #         json_fonti_texto = climain.json_fonti(
        #             METHODUS_FONTI[pyargs.methodus], ex_texto=True)
        #     return climain.objectivum_formato_csv(json_fonti_texto)

        print('Unknow option.')
        return self.EXIT_ERROR

    def quod_configuratio(
        self,
        archivum_configurationi: str = None,
        praefixum_configurationi: str = None
    ) -> dict:
        """quod_configuratio

        Args:
            archivum_configurationi (str, optional):

        Returns:
            (dict):
        """
        praefixum = []
        if praefixum_configurationi:
            praefixum = praefixum_configurationi.split(',')

        if exists(archivum_configurationi):
            with open(archivum_configurationi, "r") as read_file:
                datum = yaml.safe_load(read_file)
                while len(praefixum) > 0:
                    ad_hoc = praefixum.pop(0)
                    if ad_hoc in datum:
                        datum = datum[ad_hoc]
                    else:
                        raise ValueError('{0} [{1}]: [{2}?]'.format(
                            archivum_configurationi,
                            praefixum_configurationi,
                            ad_hoc,
                        ))
                return datum

        raise FileNotFoundError(
            'archivum_configurationi {0}'.format(
                str(archivum_configurationi)))


class CliMain:
    """Remove .0 at the end of CSVs from data exported from XLSX and likely
    to have numeric values (and trigger weird bugs)
    """

    delimiter = ','

    hxltm_ad_rdf: Type['HXLTMAdRDFSimplicis'] = None
    pyargs: dict = None
    venandum_insectum: bool = False  # noqa

    def __init__(
            self, infile: str = None, stdin: bool = None,
            pyargs: dict = None, configuratio: dict = None,
            venandum_insectum: bool = False  # noqa
    ):
        """
        Constructs all the necessary attributes for the Cli object.
        """
        self.infile = infile
        self.stdin = stdin
        self.pyargs = pyargs
        self.objectivum_formato = pyargs.objectivum_formato
        # self.methodus = pyargs.methodus
        self.configuratio = configuratio
        self.venandum_insectum = venandum_insectum

        caput, datum = hxltm_carricato(infile, stdin)

        # delimiter = ','
        if self.objectivum_formato in ['tsv', 'hxltm_tsv', 'hxl_tsv']:
            self.delimiter = "\t"
        # print('oi HXLTMAdRDFSimplicis')
        self.hxltm_ad_rdf = HXLTMAdRDFSimplicis(
            configuratio, pyargs.objectivum_formato, caput, datum,
            venandum_insectum=self.venandum_insectum
        )

        # methodus_ex_tabulae = configuratio['methodus'][self.methodus]

        # self.tabula = TabulaAdHXLTM(
        #     methodus_ex_tabulae=methodus_ex_tabulae,
        #     methodus=self.methodus,
        #     objectivum_formato=self.objectivum_formato
        # )

        # self.outfile = outfile
        # self.header = []
        # self.header_index_fix = []

    def actio(self):
        # āctiō, f, s, nominativus, https://en.wiktionary.org/wiki/actio#Latin
        if self.pyargs.objectivum_formato == 'text/csv':
            return self.hxltm_ad_rdf.resultatum_ad_csv()
        if self.pyargs.objectivum_formato == 'application/x-turtle':
            return self.hxltm_ad_rdf.resultatum_ad_turtle()
        if self.pyargs.objectivum_formato == 'application/n-triples':
            return self.hxltm_ad_rdf.resultatum_ad_ntriples()
            # print('oi actio')
            # numerordinatio_neo_separatum
        # print('failed')


class HXLTMAdRDFSimplicis:
    """HXLTM ad RDF

    - ad (+ accusativus),https://en.wiktionary.org/wiki/ad#Latin
    - HXLTM, https://hxltm.etica.ai/
    - RDF, ...
    - simplicis, m/f/n, s, Gen., https://en.wiktionary.org/wiki/simplex#Latin

    """
    # fōns, m, s, nominativus, https://en.wiktionary.org/wiki/fons#Latin
    fons_configurationi: dict = {}
    # methodus_ex_tabulae: dict = {}
    objectivum_formato: str = 'application/x-turtle'
    # methodus: str = ''

    caput: list = []
    data: list = []
    praefixo: str = ''

    # _hxltm: '#meta+{caput}'

    #  '#meta+{{caput_clavi_normali}}'
    # _hxltm_hashtag_defallo: str = '#meta+{{caput_clavi_normali}}'
    # _hxl_hashtag_defallo: str = '#meta+{{caput_clavi_normali}}'

    # identitās, f, s, nom., https://en.wiktionary.org/wiki/identitas#Latin
    # ex (+ ablative), https://en.wiktionary.org/wiki/ex#Latin
    # locālī, n, s, dativus, https://en.wiktionary.org/wiki/localis#Latin
    # identitas_locali_ex_hxl_hashtag: str = '#item+conceptum+codicem'
    identitas_locali_index: int = -1
    venandum_insectum: bool = False  # noqa
    _hxltm_linguae_index: list = []
    _hxltm_linguae_info: dict = {}
    _hxltm_meta_index: list = []
    _hxltm_meta_info: dict = {}
    _hxltm_unlabeled_index: list = []
    _hxltm_unlabeled_info: dict = {}
    _hxltm_labeled = [
        '#item+conceptum+numerordinatio',
        '#item+conceptum+codicem',
        '#status+conceptum+codicem',
        '#status+conceptum+definitionem',
        '#item+rem+i_qcc+is_zxxx+ix_codexfacto',
    ]

    def __init__(
        self,
        fons_configurationi: dict,
        objectivum_formato: str,
        caput: list = None,
        data: list = None,
        venandum_insectum: bool = False  # noqa
    ):
        """__init__ _summary_

        Args:
            methodus_ex_tabulae (dict):
        """
        self.fons_configurationi = fons_configurationi
        self.objectivum_formato = objectivum_formato
        self.venandum_insectum = venandum_insectum
        self.caput = caput
        self.data = data
        # self.methodus = methodus

        self.praefixo = numerordinatio_neo_separatum(
            self.fons_configurationi['numerordinatio']['praefixo'], ':')

        self._post_init()

    def _post_init(self):
        # @TODO esse desgambiarrizar esse _post_init

        if 'identitas_locali_ex_hxl_hashtag' in \
                self.fons_configurationi['numerordinatio']:
            _test = self.fons_configurationi['numerordinatio']['identitas_locali_ex_hxl_hashtag']
            # print("{0}".format(_test))
            # print("{0}".format(self.caput))
            for item in _test:
                if item in self.caput:
                    # self.identitas_locali_ex_hxl_hashtag = item
                    self.identitas_locali_index = self.caput.index(item)
                    break
            if self.identitas_locali_index == -1:
                raise ValueError("HXLTMAdRDFSimplicis [{0}] ?? <{1}>".format(
                    _test, self.caput))

        for _index, item in enumerate(self.caput):
            attrs = item.replace('#item+rem', '')
            bcp47_simplici = qhxl_hxlhashtag_2_bcp47(attrs)
            # lingua = bcp47_langtag(bcp47_simplici, [
            #     # 'Language-Tag',
            #     'Language-Tag_normalized',
            #     'language'
            # ], strictum=False)
            # bcp47_langtag

            if item not in self._hxltm_labeled:
                # _index = self.caput.index(item)
                if item.startswith('#meta'):
                    self._hxltm_meta_index.append(_index)
                    self._hxltm_meta_info[_index] = {
                        'hxltm_hashtag': item,
                        'bcp47': bcp47_simplici
                    }
                    continue
                self._hxltm_unlabeled_index.append(_index)
                self._hxltm_unlabeled_info[_index] = {
                    'hxltm_hashtag': item,
                    'bcp47': bcp47_simplici
                }

            # Language tags only
            if not item.startswith('#item+rem'):
                continue
            # attrs = item.replace('#item+rem', '')
            # hxlattslinguae = qhxl_attr_2_bcp47(attrs)
            # lingua = bcp47_langtag(hxlattslinguae, [
            #     # 'Language-Tag',
            #     'Language-Tag_normalized',
            #     'language'
            # ], strictum=False)
            if bcp47_simplici and not bcp47_simplici.startswith(('qcc', 'zxx')):
                self._hxltm_linguae_index.append(_index)
                self._hxltm_linguae_info[_index] = {
                    'hxltm_hashtag': item,
                    'bcp47': bcp47_simplici
                }

    def resultatum_ad_csv(self):
        """resultatum ad csv text/csv

        Returns:
            (int): status code
        """
        _writer = csv.writer(sys.stdout)
        _writer.writerow(self.caput)
        _writer.writerows(self.data)
        return Cli.EXIT_OK

    # resultātum, n, s, nominativus, https://en.wiktionary.org/wiki/resultatum
    def resultatum_ad_ntriples(self):
        """resultatum ad n triples application/n-triples

        Returns:
            (int): status code
        """
        print('# TODO HXLTMAdRDFSimplicis.resultatum_ad_ntriples')
        print('# ' + str(self.fons_configurationi))

        return Cli.EXIT_OK

    # resultātum, n, s, nominativus, https://en.wiktionary.org/wiki/resultatum
    def resultatum_ad_turtle(self):
        """resultatum ad n turtle application/x-turtle

        Returns:
            (int): status code
        """
        print('# [{0}]'.format(self.praefixo))
        print('@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .')
        print('@prefix skos: <http://www.w3.org/2004/02/skos/core#> .')
        print('')
        if self.venandum_insectum:
            print('# @TODO melhorar HXLTMAdRDFSimplicis.resultatum_ad_turtle')
            print('# fons_configurationi ' + str(self.fons_configurationi))
            print('# _hxltm_unlabeled_info ' + str(self._hxltm_unlabeled_info))
            print('# _hxltm_meta_info ' + str(self._hxltm_meta_info))
            print('# _hxltm_linguae_info ' + str(self._hxltm_linguae_info))
            print('')
            print('# @TODO adicionar mais prefixos de '
                  'https://www.wikidata.org/wiki/EntitySchema:E49')
            print('')
        # print('<urn:1603:63:101> a skos:ConceptScheme ;')
        # print('  skos:prefLabel "1603:63:101"@mul-Zyyy-x-n1603 .')
        print("<urn:{0}> a skos:ConceptScheme ; \n"
              "  skos:prefLabel \"{0}\"@mul-Zyyy-x-n1603 .".format(
                  self.praefixo))
        print('  # @TODO skos:hasTopConcept')
        print('')

        # @TODO: implementar qhx-Latn (HXLStandard), refs
        #        https://github.com/EticaAI/hxltm/blob/main/docs
        #        /codex-simplex-ontologiae/ontologia.yml

        for linea in self.data:
            # print('# {0}'.format(linea))
            # print('# {0}'.format(self.identitas_locali_index))
            # _codex_locali = self.quod(
            #     linea, '#item+rem+i_qcc+is_zxxx+ix_wikip1585')
            _codex_locali = str(int(linea[self.identitas_locali_index]))
            print('<urn:{0}:{1}> a skos:Concept ;'.format(
                self.praefixo,
                _codex_locali
            ))
            # print('  skos:prefLabel "{0}:{1}"@mul-Zyyy-x-n1603 .'.format(
            print('  skos:prefLabel "{0}:{1}"@mul-Zyyy-x-n1603 ;'.format(
                self.praefixo,
                _codex_locali
            ))
            _skos_related = []
            _skos_related_raw = []
            for _index, item in enumerate(linea):
                if item and _index in self._hxltm_unlabeled_index and \
                        self._hxltm_unlabeled_info[_index]['bcp47']:
                    _skos_related_raw.append('"{0}"@{1}'.format(
                        item.replace('"', '\\"'),
                        self._hxltm_unlabeled_info[_index]['bcp47']
                    ))
                    # pass

            # @TODO add other related
            _skos_related = _skos_related_raw
            # linguae = self._quod_linguae(res)
            if len(_skos_related) > 0:
                print("  skos:related\n    {0} .".format(
                    " ,\n    ".join(_skos_related_raw)
                ))
            for _index, item in enumerate(linea):
                # if len(item) and _index in self._hxltm_unlabeled_index:
                #     print('  # {0} [{1}]'.format(
                #         self._hxltm_unlabeled_info[_index]['hxltm_hashtag'], item))
                if self.venandum_insectum:
                    if len(item) and _index in self._hxltm_meta_index:
                        print('  # verbose: {0} [{1}]'.format(
                            self._hxltm_meta_info[_index]['hxltm_hashtag'],
                            item))

            # linguae = self._quod_linguae(res)
            # if len(linguae) > 0:
            #     print("  skos:prefLabel\n    {0} .".format(
            #         " ,\n    ".join(linguae)
            #     ))

            print('')

        return Cli.EXIT_OK

    def quod(self, linea: list, caput_item: str) -> str:
        if caput_item in self.caput:
            index = self.caput.index(caput_item)
            # print('## {0}'.format(linea))
            # print('## {0}'.format(linea[index]))
            return linea[index]
        return ''


# @TODO remove TabulaAdHXLTM from this file
class TabulaAdHXLTM:
    """Tabula ad HXLTM

    - tabula, f, s, nominativus, https://en.wiktionary.org/wiki/tabula
    - ad (+ accusativus),https://en.wiktionary.org/wiki/ad#Latin
    - ex (+ ablativus)
    - HXLTM, https://hxltm.etica.ai/

    """
    methodus_ex_tabulae: dict = {}
    # methodus_ex_tabulae: dict = {}
    objectivum_formato: str = 'hxltm_csv'
    methodus: str = ''

    # _hxltm: '#meta+{caput}'

    #  '#meta+{{caput_clavi_normali}}'
    _hxltm_hashtag_defallo: str = '#meta+{{caput_clavi_normali}}'
    _hxl_hashtag_defallo: str = '#meta+{{caput_clavi_normali}}'

    def __init__(
        self,
        methodus_ex_tabulae: dict,
        objectivum_formato: str,
        methodus: str,
    ):
        """__init__ _summary_

        Args:
            methodus_ex_tabulae (dict):
        """
        self.methodus_ex_tabulae = methodus_ex_tabulae
        self.objectivum_formato = objectivum_formato
        self.methodus = methodus

    def caput_translationi(self, caput: list) -> list:
        """Caput trānslātiōnī

        - trānslātiōnī, f, s, dativus, https://en.wiktionary.org/wiki/translatio
        - caput, n, s, nominativus, https://en.wiktionary.org/wiki/caput#Latin

        Args:
            caput (list): _description_

        Returns:
            list: _description_
        """

        # if self.objectivum_formato.find('hxltm') > -1:
        #     # neo_caput = map(self.clavis_ad_hxl, caput, 'hxltm')
        #     # neo_caput = map(self.clavis_ad_hxl, caput, 'hxltm')
        #     neo_caput = map(self.clavis_ad_hxl, caput)
        #     # neo_caput = map(self.clavis_ad_hxl, caput)
        # if self.objectivum_formato.find('hxl') > -1:
        #     # neo_caput = map(self.clavis_ad_hxl, caput, 'hxl')
        #     neo_caput = map(self.clavis_ad_hxl, caput)
        if self.objectivum_formato.find('hxl') > -1:
            neo_caput = map(self.clavis_ad_hxl, caput)
        else:
            neo_caput = map(self.clavis_normationi, caput)
        return neo_caput

    def clavis_normationi(self, clavis: str) -> str:
        """clāvis nōrmātiōnī

        - clāvis, f, s, normativus, https://en.wiktionary.org/wiki/clavis#Latin
        - nōrmātiōnī, f, s, dativus, https://en.wiktionary.org/wiki/normatio

        Args:
            clavis (str):

        Returns:
            str:
        """
        if not clavis or len(clavis) == 0:
            return ''
        clavis_normali = clavis.strip().lower()\
            .replace(' ', '_').replace('-', '_')

        return clavis_normali

    # def clavis_ad_hxl(self, clavis: str, classis: str = 'hxltm') -> str:
    def clavis_ad_hxl(self, clavis: str) -> str:
        """clavis_ad_hxltm

        - clāvis, f, s, normativus, https://en.wiktionary.org/wiki/clavis#Latin
        - nōrmātiōnī, f, s, dativus, https://en.wiktionary.org/wiki/normatio

        Args:
            clavis (str):

        Returns:
            str:
        """
        clavis_normationi = self.clavis_normationi(clavis)

        if not clavis or len(clavis) == 0:
            return ''
        # print(classis)
        # neo_caput = 'hxl_hashtag'
        # forma = self._hxl_hashtag_defallo
        # if classis == 'hxltm' or not classis:
        if self.objectivum_formato.find('hxltm') > -1:
            neo_caput = 'hxltm_hashtag'
            forma = self._hxltm_hashtag_defallo
        # elif classis == 'hxl':
        elif self.objectivum_formato.find('hxl') > -1:
            neo_caput = 'hxl_hashtag'
            forma = self._hxl_hashtag_defallo

        if clavis_normationi in self.methodus_ex_tabulae['caput'].keys():
            if self.methodus_ex_tabulae['caput'][clavis_normationi] and \
                neo_caput in self.methodus_ex_tabulae['caput'][clavis_normationi] and \
                    self.methodus_ex_tabulae['caput'][clavis_normationi][neo_caput]:
                forma = self.methodus_ex_tabulae['caput'][clavis_normationi][neo_caput]

        hxl_hashtag = forma.replace(
            '{{caput_clavi_normali}}', clavis_normationi)

        return hxl_hashtag

    # def clavis_ad_hxl(self, clavis: str) -> str:
    #     pass


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


def numerordinatio_progenitori(
        numerordinatio: str, separatum: str = "_") -> int:
    # prōgenitōrī, s, m, dativus, https://en.wiktionary.org/wiki/progenitor
    normale = numerordinatio_neo_separatum(numerordinatio, separatum)
    _parts = normale.split(separatum)
    _parts = _parts[:-1]
    if len(_parts) == 0:
        return "0"
    return separatum.join(_parts)


def hxltm_carricato(
        archivum_trivio: str = None, est_stdin: bool = False) -> list:
    caput = []
    _data = []
    # data = []

    # print('hxltm_carricato', archivum_trivio, est_stdin)
    # return 'a', 'b'
    if est_stdin:
        for linea in sys.stdin:
            if len(caput) == 0:
                # caput = linea
                # _reader_caput = csv.reader(linea)
                _gambi = [linea, linea]
                _reader_caput = csv.reader(_gambi)
                caput = next(_reader_caput)
            else:
                _data.append(linea)
        _reader = csv.reader(_data)
        return caput, list(_reader)
    # else:
    #     fons = archivum_trivio

    with open(archivum_trivio, 'r') as _fons:
        _csv_reader = csv.reader(_fons)
        for linea in _csv_reader:
            if len(caput) == 0:
                # caput = linea
                # _reader_caput = csv.reader(linea)
                _gambi = [linea, linea]
                _reader_caput = csv.reader(_gambi)
                caput = next(_reader_caput)
            else:
                _data.append(linea)
            # print(row)

    # for line in fons:
    #     print(line)
        # json_fonti_texto += line
    # - carricātō, n, s, dativus, https://en.wiktionary.org/wiki/carricatus#Latin
    #   - verbum: https://en.wiktionary.org/wiki/carricatus#Latin
    _reader = csv.reader(_data)
    return caput, list(_reader)


def qhxl_hxlhashtag_2_bcp47(hxlhashtag: str) -> str:
    """qhxl_hxlhashtag_2_bcp47

    (try) to convert full HXL hashtag to BCP47

    Args:
        hxlatt (str):

    Returns:
        str:
    """
    # needs simplification
    if not hxlhashtag:
        return None
    if hxlhashtag.find('i_') == -1 or hxlhashtag.find('is_') == -1:
        return None
    hxlhashtag_parts = hxlhashtag.split('+')
    # langattrs = []
    _bcp_lang = ''
    _bcp_stript = ''
    _bcp_extension = []
    for item in hxlhashtag_parts:
        if item.startswith('i_'):
            _bcp_lang = item.replace('i_', '')
        if item.startswith('is_'):
            _bcp_stript = item.replace('is_', '')
        if item.startswith('ix_'):
            _bcp_extension.append(item.replace('ix_', ''))
        # if not item.startswith(('i_', 'is_', 'ix_')):
        #     continue
        # langattrs.append(item)

    if not _bcp_lang or not _bcp_stript:
        return False

    bcp47_simplici = "{0}-{1}".format(
        _bcp_lang.lower(), _bcp_stript.capitalize())
    if len(_bcp_extension) > 0:
        _bcp_extension = sorted(_bcp_extension)
        bcp47_simplici = "{0}-x-{1}".format(
            bcp47_simplici,
            '-'.join(_bcp_extension)
        )

    return bcp47_simplici


if __name__ == "__main__":

    est_cli = Cli()
    args = est_cli.make_args()

    est_cli.execute_cli(args)
