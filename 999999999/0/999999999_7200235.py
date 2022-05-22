#!/usr/bin/env python3
# ==============================================================================
#
#          FILE:  999999999_7200235.py
#
#         USAGE:  ./999999999/0/999999999_7200235.py --help
#
#   DESCRIPTION:  RUN ./999999999/0/999999999_7200235.py --help
#                 - Q7200235, https://www.wikidata.org/wiki/Q7200235
#                   - Place code - address system used by emergency response
#                     teams
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
# - https://github.com/hxl-team/HXL-Vocab/blob/master/Tools/static/hxl.ttl
# - https://github.com/hxl-team/HXL-Vocab/blob/master/Tools/static
#   /humanitarianProfileSection.dot.png
# - https://github.com/hxl-team/HXL-Vocab/blob/master/Tools/static
#   /hxl-geolocation-standard-draft.pdf

import json
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

# l999999999_0 = __import__('999999999_0')
from L999999999_0 import (
    CodAbTabulae,
    csv_imprimendo,
    # hxltm__data_referentibus,
    hxltm__est_data_referentibus,
    hxltm__quod_data_referentibus,
    hxltm_adde_columna,
    hxltm_carricato,
    NUMERORDINATIO_BASIM,
    hxltm_cum_aut_sine_columnis_simplicibus,
    # hxltm_cum_columna,
    # hxltm_cum_columnis_desideriis,
    hxltm_cum_filtro,
    hxltm_cum_ordinibus_ex_columnis,
    # hxltm_sine_columnis,
    hxltm_ex_selectis,
    hxltm_index_praeparationi,
    qhxl_hxlhashtag_2_bcp47,
    XLSXSimplici
)

STDIN = sys.stdin.buffer

NOMEN = '999999999_7200235'

# @TODO move this _SEE_ALSO for some other place
_SEE_ALSO = [
    'https://en.wikipedia.org/wiki/Geopolitical_ontology'
]

DESCRIPTION = """
{0} Pre-processor of P-Code external data to HXLTM working format.

@see https://github.com/EticaAI/lexicographi-sine-finibus/issues/42

@see - https://sites.google.com/site/ochaimwiki\
/geodata-preparation-manual/p-code-guidelines
     - https://docs.google.com/viewer?a=v&pid=sites&srcid=\
ZGVmYXVsdGRvbWFpbnxvY2hhaW13aWtpfGd4Ojc4YTljNmEwNmM3MjkwNWU
       - Note: on this one, Country level P-Codes start from 1, not 0.
         Today adm0 represent the level
     - https://mtoolbox.unocha.org
     - https://github.com/hxl-team/HXL-Vocab/blob/master/Tools/hxl.ttl

Trivia:
- Q7200235, https://www.wikidata.org/wiki/Q7200235
  - Place code - address system used by emergency response teams
- Related
  - Q56061, https://www.wikidata.org/wiki/Q56061
    - /administrative territorial entity/@eng-Latn
    - //divisio administrativa//@lat-Latn

Maybe for later
- https://www.unsalb.org/data
""".format(__file__)

__EPILOGUM__ = """
------------------------------------------------------------------------------
                            EXEMPLŌRUM GRATIĀ
------------------------------------------------------------------------------


Work with local COD-AB index . . . . . . . . . . . . . . . . . . . . . . . . .
    {0} --methodus='cod_ab_index'

    {0} --methodus='cod_ab_index' --sine-columnis='#country+code+v_iso3'

    {0} --methodus='cod_ab_index' --sine-columnis='#country+code+v_iso3' \
--cum-filtris='LOWER(#country+code+v_iso3)'

    {0} --methodus='cod_ab_index' --sine-columnis='#country+code+v_iso3' \
--ex-selectis='#date+created<2010-01-01' \
--ex-selectis='#date+updated>2020-01-01'

    {0} --methodus='cod_ab_index' --cum-ordinibus-ex-columnis=\
'-9:#meta+id|-8:#country+code+v_iso3|-7:#country+code+v_iso2'

Process XLSXs from external sources . . . . . . . . . . . . . . . . . . . . . .
   {0} --methodus=xlsx_metadata 999999/1603/45/16/xlsx/ago.xlsx
   {0} --methodus=xlsx_ad_csv --ordines=2 999999/1603/45/16/xlsx/ago.xlsx

    cat 999999/1603/45/16/csv/AGO_2.csv | \
{0} --objectivum-formato=text/csv

Generic HXLTM processing . . . . . . . . . . . . . . . . . . . . . . . . . . . .
(equivalent commands)
    {0} --methodus=de_librario 1603_1_1
    {0} --methodus=de_hxltm_ad_hxltm 1603/1/1/1603_1_1.no1.tm.hxl.csv
    cat 1603/1/1/1603_1_1.no1.tm.hxl.csv | {0} --methodus=de_hxltm_ad_hxltm

    {0} --methodus=de_hxltm_ad_hxltm 1603/1/1/1603_1_1.no1.tm.hxl.csv \
--ex-selectis='#item+conceptum+codicem==1'

    {0} --methodus='de_librario' 1603_1_6 --adde-columnis='#meta+novum=test123'
    {0} --methodus='de_librario' 1603_1_6 \
--adde-columnis='#meta+novum=#item+conceptum+codicem'
    {0} --methodus='de_librario' 1603_1_6 \
--adde-columnis='#meta+novum=CONCAT("PREFIX";#item+conceptum+codicem)'
    {0} --methodus='de_librario' 1603_1_6 \
--adde-columnis='#meta+novum=CONCAT(#item+conceptum+codicem;"SUFFIX")'


(Some other examples know to work (at time of testing))
    {0} --methodus=de_librario 1603_45_49 \
--adde-columnis=\
'#meta+v_iso2+alt=LOWER(#item+rem+i_qcc+is_zxxx+ix_iso3166p1a2)' \
--adde-columnis=\
'#meta+v_iso3+alt=LOWER(#item+rem+i_qcc+is_zxxx+ix_iso3166p1a3)' \


Index preparation (warn up cache) . . . . . . . . . . . . . . . . . . . . . . .

(this will pre-create a key-value index at 999999/0/i1603_45_49.index.json)
    {0} --methodus=index_praeparationi 1603_45_49 \
--index-nomini=i1603_45_49 \
--sine-columnis='#item+rem+i_qcc+is_zxxx+ix_unm49,\
#item+rem+i_qcc+is_zxxx+ix_iso3166p1a2,#item+rem+i_qcc+is_zxxx+ix_iso3166p1a3' \
--index-ad-columnam='#item+rem+i_qcc+is_zxxx+ix_unm49'

    {0} --methodus='cod_ab_index' --adde-columnis=\
'#item+rem+i_qcc+is_zxxx+ix_unm49=\
DATA_REFERENTIBUS(i1603_45_49;#country+code+v_iso3)'

------------------------------------------------------------------------------
                            EXEMPLŌRUM GRATIĀ
------------------------------------------------------------------------------
""".format(__file__)

COD_AB_INDEX = NUMERORDINATIO_BASIM + \
    '/999999/1603/45/16/1603_45_16.index.hxl.csv'

# autopep8 --list-fixes ./999999999/0/999999999_7200235.py
# pylint --disable=W0511,C0103,C0116 ./999999999/0/999999999_7200235.py

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
            prog="999999999_7200235",
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

        parser.add_argument(
            '--methodus',
            help='Main operation mode',
            dest='methodus',
            nargs='?',
            choices=[
                # 'pcode_ex_xlsx',
                # 'pcode_ex_csv',
                'cod_ab_index',
                'cod_ab_ad_rdf_skos_ttl',
                'de_hxltm_ad_hxltm',  # load main file directly
                # load main file by number (example: 1603_45_49)
                'de_librario',
                'xlsx_metadata',
                'xlsx_ad_csv',
                'xlsx_ad_hxl',
                'xlsx_ad_hxltm',
                # praeparātiōnī https://en.wiktionary.org/wiki/praeparatio#Latin
                'index_praeparationi',
            ],
            # required=True
            default='cod_ab_index'
        )

        parser.add_argument(
            '--ordines',
            help='ōrdinēs. (literal latin: methodical arrangement, '
            'order; plural). Use to specify explicit administrative '
            'boundaries to work with. Comma separated.',
            dest='ordines',
            nargs='?',
            # choices=[
            #     'pcode_xlsx',
            #     # 'pcode_xlsx_123456789',
            #     # 'data-apothecae',
            #     # 'hxltm-explanationi',
            #     # 'opus-temporibus',
            #     # 'status-quo',
            #     # 'deprecatum-dictionaria-numerordinatio'
            # ],
            # required=True
            type=lambda x: x.split(','),
            default=None
        )

        # - Related
        #   - Q56061, https://www.wikidata.org/wiki/Q56061
        #     - /administrative territorial entity/@eng-Latn
        #     - //divisio administrativa//@lat-Latn
        #       - https://en.wiktionary.org/wiki/divisio#Latin
        #       - https://en.wiktionary.org/wiki/administro#Latin
        # - https://en.wiktionary.org/wiki/ordo#Latin
        parser.add_argument(
            '--ex-metadatis',
            help='For operations related with metadata (nested object) '
            'or with index, this option can be used to filter result. '
            'Mostly used to help with scripts',
            dest='ex_metadatis',
            nargs='?',
            # required=True
            default=None
        )

        # https://en.wiktionary.org/wiki/memoria#Latin
        # https://en.wiktionary.org/wiki/internalis#Latin
        memoria_internalo = parser.add_argument_group(
            "Memoria internālī",
            # '[ --methodus=\'cod_ab_index\' ] '
            "Operations to change internal state of tabular internal memory. "
        )

        # - ex (+ ablativus), https://en.wiktionary.org/wiki/ex#Latin
        # -columnīs, f, pl, ablativus, https://en.wiktionary.org/wiki/columna
        memoria_internalo.add_argument(
            '--sine-columnis',
            help='For operations related with metadata (nested object) '
            'or with index, this option can be used to filter result. '
            'Mostly used to help with scripts',
            dest='sine_columnis',
            nargs='?',
            # required=True
            default=None
        )

        memoria_internalo.add_argument(
            '--ex-selectis',
            help='For operations related with index (limited subset of '
            'hxlselect cli tool. '
            'Mostly used to help with scripts',
            action='append',
            dest='ex_selectis',
            # nargs='?',
            # nargs='*',
            # required=True
            default=None
        )

        memoria_internalo.add_argument(
            '--adde-columnis',
            help='Add columns (advanced processing). '
            'Can use both columns on exiting dataset and, with '
            '"#meta+new=DATA_REFERENTIBUS(iNNNN_NN_NN, #item+existing)", '
            'use external sources.',
            action='append',
            dest='adde_columnis',
            nargs='?',
            # nargs='*',
            # required=True
            default=None
        )

        memoria_internalo.add_argument(
            '--cum-columnis',
            help='Select columns (simple processing). '
            'Mostly used to help with scripts',
            action='append',
            dest='cum_columnis',
            nargs='?',
            # nargs='*',
            # required=True
            default=None
        )

        memoria_internalo.add_argument(
            '--cum-filtris',
            help='Apply filters for existing columns. '
            'Example: --cum-filtris=\'LOWER(#country+code+v_iso3)\'. '
            'Mostly used to help with scripts',
            dest='cum_filtris',
            # nargs='?',
            # nargs='*',
            action='append',
            # required=True
            default=None
        )

        memoria_internalo.add_argument(
            '--cum-ordinibus-ex-columnis',
            help='With this with preferred order of columns (not enforced). '
            'If it cannot find the columns, it will not change the order.'
            'Example: "-999:#meta+id|0:#meta+code|999:#meta+note"',
            dest='cum_ordinibus_ex_columnis',
            nargs='?',
            # required=True
            default=None
        )

        # memoria_internalo.add_argument(
        #     '--per-columnas',
        #     help='Apply filters to existing columns. '
        #     'Mostly used to help with scripts',
        #     dest='per_columnas',
        #     # nargs='?',
        #     nargs='*',
        #     # required=True
        #     default=None
        # )

        # - index, s, m, nominativus, https://en.wiktionary.org/wiki/index#Latin
        # - praeparātiōnī, s, f, dativus
        #   https://en.wiktionary.org/wiki/praeparatio#Latin
        index_praeparationi = parser.add_argument_group(
            "Index praeparātiōnī",
            '[ --methodus=\'index_praeparationi\' ] '
            "Create a key-value temporary file on disk optimized for "
            "uses in advance with data manipulation. "
            "Common use case is to add new columns to final datasets by using "
            "pre-build indexes where all possible keys would "
            "be found on real data and then point (the value) to "
            "what you would want."
        )

        # ad (+ accusativus) https://en.wiktionary.org/wiki/ad#Latin
        # columnam, s, f, acc., https://en.wiktionary.org/wiki/columna#Latin
        index_praeparationi.add_argument(
            '--index-ad-columnam',
            help='Column the index will point to. means both file on temporary directory '
            ' and option to reference on transformations. ',
            dest='index_ad_columnam',
            nargs='?',
            # required=True
            default='#item+conceptum+codicem'
        )

        # nōminī, s, n, dativus, https://en.wiktionary.org/wiki/nomen#Latin
        index_praeparationi.add_argument(
            '--index-nomini',
            help='Name of the index. means both file on temporary directory '
            ' and option to reference on transformations. ',
            dest='index_nomini',
            nargs='?',
            # required=True
            default=None
        )

        #
        # 'index_praeparationi',

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
            # required=True,
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

        # silentium, n, s, nominativus, en.wiktionary.org/wiki/silentium#Latin
        parser.add_argument(
            '--silentium',
            help='Instead of exception with error message, output nothing',
            metavar="silentium",
            dest="silentium",
            action='store_const',
            const=True,
            default=False
        )

        parser.add_argument(
            # '--venandum-insectum-est, --debug',
            '--venandum-insectum-est', '--debug',
            help='Enable debug? Show extra informations',
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

    def execute_cli(self, pyargs, stdin=STDIN, _stdout=sys.stdout,
                    _stderr=sys.stderr):
        # self.pyargs = pyargs

        # _infile = None
        # _stdin = None
        unm49_basi = '24'
        adm_level = '2'
        configuratio = {
            'numerordinatio': {
                'praefixo': '1603:45:16:{0}:{1}'.format(unm49_basi, adm_level)
            }
        }
        # configuratio = self.quod_configuratio(
        #     pyargs.archivum_configurationi, pyargs.praefixum_configurationi)
        if pyargs.venandum_insectum or VENANDUM_INSECTUM:
            self.venandum_insectum = True

        if stdin.isatty():
            _infile = pyargs.infile
            _stdin = False
        else:
            if pyargs.methodus in ['xlsx', 'de_librario']:
                raise ValueError(
                    'stdin not implemented for {0} input'.format(
                        pyargs.methodus))
            _infile = None
            _stdin = True

        if pyargs.methodus in [
            'de_hxltm_ad_hxltm', 'de_librario',
                'index_praeparationi',  'cod_ab_index']:
            # Decide which main file to load.
            # if pyargs.methodus.startswith('de_librario'):
            if pyargs.methodus.startswith(
                    ('de_librario', 'index_praeparationi')):
                _path = '{0}/{1}/{2}.no1.tm.hxl.csv'.format(
                    NUMERORDINATIO_BASIM,
                    numerordinatio_neo_separatum(_infile, '/'),
                    numerordinatio_neo_separatum(_infile, '_')
                )
                # caput, data = hxltm_carricato(_infile, _stdin)
                caput, data = hxltm_carricato(_path)
            elif pyargs.methodus.startswith('de_hxltm_ad_hxltm'):
                caput, data = hxltm_carricato(_infile, _stdin)
            elif pyargs.methodus.startswith('cod_ab_index'):
                caput, data = hxltm_carricato(COD_AB_INDEX)

            est_data_referentibus = hxltm__est_data_referentibus(
                pyargs.adde_columnis,
                pyargs.ex_selectis,
                pyargs.cum_columnis,
                pyargs.cum_filtris,
                pyargs.sine_columnis
            )

            data_referentibus = {}
            if est_data_referentibus:
                for item in est_data_referentibus:
                    data_referentibus[item] = \
                        hxltm__quod_data_referentibus(item)

            # print('    est_data_referentibus', est_data_referentibus)
            # print('data_referentibus', data_referentibus.keys())

            if pyargs.ex_selectis:
                ex_selectis = pyargs.ex_selectis
                # print('ex_selectis', ex_selectis)
                for opus in ex_selectis:
                    caput, data = hxltm_ex_selectis(
                        caput, data, opus, data_referentibus)

            if pyargs.adde_columnis:

                _opus = pyargs.adde_columnis
                if not isinstance(pyargs.adde_columnis, list):
                    _opus = [pyargs.adde_columnis]
                opera = []
                for item in _opus:
                    opera.extend(map(str.strip, item.split(',')))
                # opus = pyargs.cum_columnis.split(',')

                for opus in opera:
                    caput, data = hxltm_adde_columna(
                        caput, data, opus, data_referentibus)

            if pyargs.cum_columnis:

                _opus = pyargs.cum_columnis
                if not isinstance(pyargs.cum_columnis, list):
                    _opus = [pyargs.cum_columnis]
                opus = []
                for item in _opus:
                    opus.extend(map(str.strip, item.split(',')))
                # opus = pyargs.cum_columnis.split(',')
                caput, data = hxltm_cum_aut_sine_columnis_simplicibus(
                    caput, data, opus, data_referentibus, cum_columnis=True)

            if pyargs.cum_filtris:
                cum_filtris = pyargs.cum_filtris
                for opus in cum_filtris:
                    caput, data = hxltm_cum_filtro(
                        caput, data, opus, data_referentibus)

            # if pyargs.ex_metadatis:
            if pyargs.sine_columnis:
                # opus = pyargs.sine_columnis.split(',')
                # caput, data = hxltm_sine_columnis(
                #     caput, data, opus, data_referentibus)

                _opus = pyargs.sine_columnis
                if not isinstance(pyargs.sine_columnis, list):
                    _opus = [pyargs.sine_columnis]
                opus = []
                for item in _opus:
                    opus.extend(map(str.strip, item.split(',')))
                # opus = pyargs.cum_columnis.split(',')
                caput, data = hxltm_cum_aut_sine_columnis_simplicibus(
                    caput, data, opus, data_referentibus, cum_columnis=False)

            # if pyargs.ex_metadatis:
            if pyargs.cum_ordinibus_ex_columnis:
                _opus = pyargs.cum_ordinibus_ex_columnis
                if not isinstance(pyargs.cum_ordinibus_ex_columnis, list):
                    _opus = [pyargs.cum_ordinibus_ex_columnis]
                opus = []
                for item in _opus:
                    opus.extend(map(str.strip, item.split('|')))

                # opus = pyargs.cum_ordinibus_ex_columnis.split('|')
                caput, data = hxltm_cum_ordinibus_ex_columnis(
                    caput, data, opus, data_referentibus)

            if pyargs.methodus == 'index_praeparationi':

                if pyargs.index_nomini:
                    index_nomini = pyargs.index_nomini
                else:
                    # In this case, _infile is just a string like 1603_45_49
                    index_nomini = 'i{0}'.format(str(_infile))

                data_json = hxltm_index_praeparationi(
                    caput, data, pyargs.index_ad_columnam)
                # data_json_len = data_json.keys().len()
                data_json_len = len(data_json.keys())
                data_json_len_uniq = len(set(data_json.values()))

                data_json_str = json.dumps(
                    data_json, indent=4, sort_keys=False, ensure_ascii=False)

                # print(data_json_str)

                _path = '{0}/999999/0/{1}.index.json'.format(
                    NUMERORDINATIO_BASIM,
                    index_nomini,
                )

                with open(_path, "w") as file1:
                    file1.write(data_json_str)
                print('index [{0} -> {1}]: {2}'.format(
                    data_json_len, data_json_len_uniq, _path))
                return self.EXIT_OK

            csv_imprimendo(caput, data)

            return self.EXIT_OK

        if pyargs.methodus.startswith('cod_ab_ad_rdf_skos_ttl'):
            raise NotImplementedError

        if pyargs.methodus.startswith('xlsx'):
            xlsx = XLSXSimplici(_infile)

        if pyargs.methodus == 'xlsx_metadata':
            # xlsx = XLSXSimplici(_infile)

            if pyargs.ex_metadatis:
                # @TODO: maybe implement a jq-like selector.
                ex_metadatis = pyargs.ex_metadatis.replace('.', '')
                xlsx_meta = xlsx.meta()
                if ex_metadatis in xlsx_meta:
                    for item in xlsx_meta[ex_metadatis]:
                        print(str(item))
                    pass
                else:
                    raise ValueError('{0} not found in {1}'.format(
                        pyargs.ex_metadatis,
                        xlsx_meta
                    ))
            else:
                print(json.dumps(xlsx.meta()))
            xlsx.finis()
            return self.EXIT_OK

        if pyargs.methodus in ['xlsx_ad_csv', 'xlsx_ad_hxltm', 'xlsx_ad_hxl']:
            if not pyargs.ordines or \
                    not xlsx.de(pyargs.ordines[0]):

                if pyargs.silentium:
                    return self.EXIT_OK
                caput = ['#status+error', '#meta+item', '#meta+value']
                data = [
                    ['ERROR', '--methodus', pyargs.methodus],
                    ['ERROR', '--ordines', str(pyargs.ordines)],
                    ['ERROR', 'input', _infile],
                    ['ERROR', 'xlsx.meta', xlsx.meta()],
                ]

                csv_imprimendo(caput, data)
                return self.EXIT_ERROR

        if pyargs.methodus == 'xlsx_ad_csv':
            xlsx.praeparatio()
            caput, data = xlsx.imprimere()
            csv_imprimendo(caput, data)

            xlsx.finis()
            return self.EXIT_OK

        if pyargs.methodus in ['xlsx_ad_hxltm', 'xlsx_ad_hxl']:
            schema = 'hxl'
            if pyargs.methodus == 'xlsx_ad_hxltm':
                schema = 'hxltm'

            xlsx.praeparatio()
            caput, data = xlsx.imprimere()

            codt = CodAbTabulae(caput=caput, data=data)
            caput, data = codt.praeparatio(schema).imprimere()
            # print(type(caput), caput)
            # print(type(data), data)
            # raise NotImplementedError('test test')
            csv_imprimendo(caput, data)

            # print()
            # print('@TODO not implemented yet')

            xlsx.finis()
            return self.EXIT_OK

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


if __name__ == "__main__":

    est_cli = Cli()
    args = est_cli.make_args()

    est_cli.execute_cli(args)
