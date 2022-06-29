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
from typing import Tuple, Type
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
    # numerordinatio_descendentibus,
    # numerordinatio_progenitori,
    # qhxl_hxlhashtag_2_bcp47,
    HXLTMAdRDFSimplicis,
    numerordinatio_neo_separatum,
    # numerordinatio_ordo,
    # numerordinatio_progenitori,
    XLSXSimplici
)

STDIN = sys.stdin.buffer

NOMEN = '999999999_7200235'

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

    {0} --methodus='cod_ab_index' --punctum-separato-ad-tab --cum-columnis='\
#country+code+v_unm49,#country+code+v_iso3,#country+code+v_iso2,\
#meta+source+cod_ab_level,#date+created,#date+updated'

    {0} --methodus='cod_ab_index' --sine-columnis='#country+code+v_iso3' \
--cum-filtris='LOWER(#country+code+v_iso3)'

    {0} --methodus='cod_ab_index' --sine-columnis='#country+code+v_iso3' \
--ex-selectis='#date+created<2010-01-01' \
--ex-selectis='#date+updated>2020-01-01'

    {0} --methodus='cod_ab_index' --cum-ordinibus-ex-columnis=\
'-9:#meta+id|-8:#country+code+v_iso3|-7:#country+code+v_iso2'

Work with local COD-AB index (levels) . . . . . . . . . . . . . . . . . . . . .
    {0} --methodus='cod_ab_index_levels' --punctum-separato-ad-tab

    {0} --methodus='cod_ab_index_levels' --sine-capite \
--cum-columnis='#item+conceptum+numerordinatio'

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


Numerordinatio (HXL) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
    {0} --methodus=xlsx_ad_no1 \
--numerordinatio-praefixo=1603_45_16 --unm49=24 --ordines=1 \
--pcode-praefixo=AO 999999/1603/45/16/xlsx/ago.xlsx


Numerordinatio (BCP47) . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
    {0} --methodus=xlsx_ad_no1bcp47 \
--numerordinatio-praefixo=1603_45_16 --unm49=24 --ordines=1 \
--pcode-praefixo=AO 999999/1603/45/16/xlsx/ago.xlsx


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

# @TODO move this _SEE_ALSO for some other place
_SEE_ALSO = [
    'https://en.wikipedia.org/wiki/Geopolitical_ontology'
]

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
                'cod_ab_index_levels',
                'cod_ab_index_levels_ttl',
                'cod_ab_ad_rdf_skos_ttl',
                'cod_ab_ad_no1_csv',  # Temporary hacky way to generate no1
                'de_hxltm_ad_hxltm',  # load main file directly
                # load main file by number (example: 1603_45_49)
                'de_librario',
                'xlsx_metadata',
                'xlsx_ad_csv',
                'xlsx_ad_hxl',
                'xlsx_ad_hxltm',
                'xlsx_ad_no1',
                'xlsx_ad_no1bcp47',
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
            type=lambda x: x.split(','),
            default=None
        )

        # numerus, --, m, https://en.wiktionary.org/wiki/numerus#Latin
        # praefīxō, s, m/n, dativus https://en.wiktionary.org/wiki/praefixus
        parser.add_argument(
            '--numerordinatio-praefixo',
            help='Numerordĭnātĭo prefix (without COD-AB level or UN m49). ',
            dest='numerordinatio_praefixo',
            nargs='?',
            default='1603:45:16'
        )

        parser.add_argument(
            '--pcode-praefixo',
            help='P-Code prefix (the country code letters)',
            dest='pcode_praefixo',
            nargs='?',
            default=None
        )

        parser.add_argument(
            '--unm49',
            help='The UN m49 code',
            dest='unm49',
            nargs='?',
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
            '--punctum-separato-ad-tab',
            help='Change output separator to tab',
            metavar="punctum_separato",
            dest="punctum_separato_ad_tab",
            action='store_const',
            const=True,
            default=False
        )
        # sine (+ ablative) https://en.wiktionary.org/wiki/sine#Latin
        # capite, s, n, ablativus, https://en.wiktionary.org/wiki/caput#Latin
        parser.add_argument(
            '--sine-capite',
            help='Output without header',
            metavar="sine_capite",
            dest="sine_capite",
            action='store_const',
            const=True,
            default=False
        )

        # parser.add_argument(
        #     # '--venandum-insectum-est, --debug',
        #     '--venandum-insectum-est', '--debug',
        #     help='Enable debug? Show extra informations',
        #     metavar="venandum_insectum",
        #     dest="venandum_insectum",
        #     action='store_const',
        #     const=True,
        #     default=False
        # )

        parser.add_argument(
            # '--venandum-insectum-est, --debug',
            '--experimentum-est',
            help='(Internal testing only) Enable undocumented feature',
            metavar="experimentum_est",
            dest="experimentum_est",
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

        punctum_separato = ','
        if pyargs.punctum_separato_ad_tab:
            punctum_separato = "\t"

        # _infile = None
        # _stdin = None
        # unm49_basi = '24'
        # adm_level = '2'
        # configuratio = {
        #     'numerordinatio': {
        #         'praefixo': '1603:45:16:{0}:{1}'.format(unm49_basi, adm_level)
        #     }
        # }
        # configuratio = self.quod_configuratio(
        #     pyargs.archivum_configurationi, pyargs.praefixum_configurationi)
        numerordinatio_praefixo = None
        pcode_praefixo = pyargs.pcode_praefixo
        unm49 = None
        if pyargs.numerordinatio_praefixo:
            numerordinatio_praefixo = numerordinatio_neo_separatum(
                pyargs.numerordinatio_praefixo, ':'
            )
        if pyargs.unm49:
            unm49 = str(int(pyargs.unm49))

        # print('    aaaa', numerordinatio_praefixo, pcode_praefixo, unm49)

        if pyargs.venandum_insectum or VENANDUM_INSECTUM:
            self.venandum_insectum = True

        if stdin.isatty():
            _infile = pyargs.infile
            _stdin = False
        else:
            #     if pyargs.methodus in ['xlsx_metadata', 'de_librario']:
            #         # print('   oi pyargs.infile', pyargs.infile)
            #         raise ValueError(
            #             'stdin not implemented for {0} input'.format(
            #                 pyargs.methodus))
            #     _infile = None
            _stdin = True

        _infile = pyargs.infile
        # raise NotImplementedError(pyargs.methodus)
        if pyargs.methodus in [
            'de_hxltm_ad_hxltm', 'de_librario',
                'index_praeparationi',  'cod_ab_index', 'cod_ab_ad_no1_csv',
                'cod_ab_index_levels', 'cod_ab_index_levels_ttl']:
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

            # if pyargs.methodus == 'cod_ab_index_levels':
            if pyargs.methodus == 'cod_ab_index_levels':
                # @TODO cod_ab_index_levels
                # caput, data = hxltm_carricato(COD_AB_INDEX)
                # raise NotImplementedError(pyargs.methodus)
                caput, data = hxltm_carricato__cod_ab_levels(
                    caput, data,
                    numerordinatio_praefixo=numerordinatio_praefixo)

            if pyargs.methodus == 'cod_ab_ad_no1_csv':
                # @TODO cod_ab_index_levels
                caput, data = hxltm_carricato(COD_AB_INDEX)
                # raise NotImplementedError(pyargs.methodus)
                caput, data = hxltm_carricato__cod_ab_levels(
                    caput, data,
                    numerordinatio_praefixo=numerordinatio_praefixo,
                    no1_simplici=True)

            if pyargs.methodus == 'cod_ab_index_levels_ttl':
                paginae = hxltm_carricato__cod_ab_levels_ttl(
                    caput, data,
                    numerordinatio_praefixo=numerordinatio_praefixo)
                for linea in paginae:
                    print(linea)
                return self.EXIT_OK

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

            if pyargs.sine_capite:
                caput = None

            csv_imprimendo(caput, data, punctum_separato)

            return self.EXIT_OK

        if pyargs.methodus.startswith('cod_ab_ad_rdf_skos_ttl'):
            raise NotImplementedError

        if pyargs.methodus.startswith('xlsx'):
            # print('_infile', _infile)
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

        if pyargs.methodus in [
                'xlsx_ad_csv', 'xlsx_ad_no1', 'xlsx_ad_no1bcp47',
                'xlsx_ad_hxltm', 'xlsx_ad_hxl']:
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

                csv_imprimendo(caput, data, punctum_separato=punctum_separato)
                return self.EXIT_ERROR

        if pyargs.methodus == 'xlsx_ad_csv':
            xlsx.praeparatio()
            caput, data = xlsx.imprimere()
            if pyargs.sine_capite:
                caput = None
            csv_imprimendo(caput, data, punctum_separato=punctum_separato)

            xlsx.finis()
            return self.EXIT_OK

        if pyargs.methodus in [
                'xlsx_ad_no1', 'xlsx_ad_no1bcp47',
                'xlsx_ad_hxltm', 'xlsx_ad_hxl']:

            schema = 'hxl'
            if pyargs.methodus == 'xlsx_ad_hxltm':
                schema = 'hxltm'
            if pyargs.methodus == 'xlsx_ad_no1':
                schema = 'no1'

            if pyargs.methodus == 'xlsx_ad_no1bcp47':
                schema = 'no1bcp47'

            xlsx.praeparatio()
            caput, data = xlsx.imprimere()

            # print(pyargs)
            # print(pyargs.experimentum_est)

            codt = CodAbTabulae(
                caput=caput,
                data=data,
                ordo=int(pyargs.ordines[0]),
                numerordinatio_praefixo=numerordinatio_praefixo,
                pcode_praefixo=pcode_praefixo,
                unm49=unm49,
                experimentum_est=pyargs.experimentum_est
            )
            caput, data = codt.praeparatio(schema).imprimere()
            # print(type(caput), caput)
            # print(type(data), data)
            # raise NotImplementedError('test test')
            if pyargs.sine_capite:
                caput = None
            csv_imprimendo(caput, data, punctum_separato=punctum_separato)

            # print()
            # print('@TODO not implemented yet')

            xlsx.finis()
            return self.EXIT_OK

        # climain = CliMain(
        #     infile=_infile, stdin=_stdin,
        #     pyargs=pyargs,
        #     configuratio=configuratio,
        #     venandum_insectum=self.venandum_insectum
        # )

        # if pyargs.objectivum_formato == 'text/csv':
        #     return climain.actio()
        # if pyargs.objectivum_formato == 'application/x-turtle':
        #     return climain.actio()
        #     # return self.EXIT_OK
        # if pyargs.objectivum_formato == 'application/n-triples':
        #     return climain.actio()
        #     # return self.EXIT_OK

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
        # self.hxltm_ad_rdf = HXLTMAdRDFSimplicis(
        #     configuratio, pyargs.objectivum_formato, caput, datum,
        #     venandum_insectum=self.venandum_insectum
        # )

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


def hxltm_carricato__cod_ab_levels(
    caput: list, data: list, numerordinatio_praefixo: str = '1603_45_16',
    no1_simplici: bool = False
) -> Tuple[list, list]:
    """hxltm_carricato__cod_ab_levels filter cod_ab_index into a list of levels

    Args:
        caput (list): _description_
        data (list): _description_
        numerordinatio_praefixo (str): _description_

    Returns:
        Tuple[list, list]: _description_
    """
    caput_novo = ['#item+conceptum+numerordinatio']
    caput_cum_columnis = [
        '#country+code+v_unm49',
        '#meta+source+cod_ab_level',
        '#country+code+v_iso3',
        '#country+code+v_iso2'
    ]
    # @TODO Need create new function, as this one is plain wrong compared to the
    #       drafted OWL TTL version
    caput_no1 = [
        '#item+conceptum+codicem',
        '#country+code+v_unm49',
        '#meta+source+cod_ab_level',
        '#country+code+v_iso3',
        '#country+code+v_iso2'
    ]
    data_novis = []

    caput, data = hxltm_cum_aut_sine_columnis_simplicibus(
        caput, data, caput_cum_columnis)

    numerordinatio_praefixo = numerordinatio_neo_separatum(
        numerordinatio_praefixo, ':')

    if no1_simplici:
        caput_novo.extend(caput_no1)
    else:
        caput_novo.extend(caput_cum_columnis)

    data.sort(key=lambda linea: int(linea[0]))

    _numerordinatio__done = []

    for linea in data:
        # for cod_ab_level in range(0, int(linea[1])):
        for cod_ab_level in range(0, (int(linea[1]) + 1)):
            linea_novae = []
            numerordinatio = '{0}:{1}:{2}'.format(
                numerordinatio_praefixo, linea[0], cod_ab_level
            )

            if numerordinatio in _numerordinatio__done:
                continue

            _numerordinatio__done.append(numerordinatio)
            linea_novae.append(numerordinatio)
            if no1_simplici:
                linea_novae.append(linea[0])
            linea_novae.append(linea[0])
            linea_novae.append(cod_ab_level)
            linea_novae.append(linea[2])
            linea_novae.append(linea[3])
            # linea_novae.extend(linea)
            data_novis.append(linea_novae)

    # raise NotImplementedError
    # return caput, data
    return caput_novo, data_novis


def hxltm_carricato__cod_ab_levels_ttl(
    caput: list, data: list, numerordinatio_praefixo: str = '1603:45:16'
) -> list:
    """hxltm_carricato__cod_ab_levels filter cod_ab_index into a list of levels

    DEPRECATED (or not fully updated) warning: this helper may not implement
               same functionalities than the RDF from HXLTM parser do, such
               as relations with OBO. However, it still easier to boostrap
               features here than full flexibility of HXLTM

    @see https://www.wikidata.org/wiki/EntitySchema:E49
    @see https://www.wikidata.org/wiki/Wikidata:List_of_properties/geography
    @see https://www.wikidata.org/wiki/Special:ListDatatypes
    @see - wikidata.org/wiki/Wikidata:List_of_properties/transitive_relation
           - located in the administrative territorial entity (P131)
           - contains administrative territorial entity (P150)


    Args:
        caput (list): _description_
        data (list): _description_
        numerordinatio_praefixo (str): _description_

    Returns:
        list: _description_
    """
    paginae = []

    # caput
    # '#meta+id'
    # '#country+code+v_unm49'
    # '#country+code+v_iso3'
    # '#country+code+v_iso2'
    # '#meta+source+cod_ab_level'
    # '#date+created'
    # '#date+updated'
    # '#item+source+type_xlsx'
    # '#item+source+type_gpkg'
    # '#item+source+type_ckan'
    # '#org+name+contributor2'
    # '#org+name+contributor1'
    # '#org+name+source'
    # '#meta+license'
    # '#country+name+ref'
    # '#country+name+alt'

    # https://www.wikidata.org/wiki/Special:EntityData/Q42.ttl
    # https://www.wikidata.org/wiki/Special:EntityData/P297.ttl

    # Brasil uses
    # - https://www.wikidata.org/wiki/Special:EntityData/Q155.ttl
    #   - wdt:P297 "BR" ;
    # Rio de Janeiro uses
    # - https://www.wikidata.org/wiki/Special:EntityData/Q8678.ttl
    #   - wdt:P297 "BR" ;

    data.sort(key=lambda linea: int(linea[1]))

    # note, on this case, we get an list already with only the root
    # items, so we have to deal with

    # https://www.wikidata.org/wiki/EntitySchema:E49

    basi = numerordinatio_neo_separatum(numerordinatio_praefixo, ':')


#     <urn:1603:63:101> a skos:ConceptScheme ;
#   skos:prefLabel "1603:63:101"@mul-Zyyy-x-n1603 ;

    unm49 = list(set(map(lambda x: x[1], data)))
    # print('unm49', unm49)
    unm49.sort(key=lambda x: int(x))
    numerodiatio_collecti = [basi + ':' + x for x in unm49]
    # print('unm49', unm49)
    # return []
    # collectio_sine_ordo = map(lambda b, x: f'{b}:{x}', basi, unm49)

    # print(list(numerodiatio_collecti))
    # return []

    paginae.append('# [{0}]'.format(basi))
    paginae.append(
        '@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .')
    paginae.append('@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .')
    paginae.append('@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .')
    paginae.append('@prefix owl: <http://www.w3.org/2002/07/owl#> .')
    paginae.append('@prefix skos: <http://www.w3.org/2004/02/skos/core#> .')
    # paginae.append('@prefix p: <http://www.wikidata.org/prop/> .')
    # paginae.append('@prefix wdt: <http://www.wikidata.org/prop/direct/> .')
    paginae.append('@prefix p: <http://www.wikidata.org/prop/> .')
    paginae.append('')

    # @see stackoverflow.com/questions/55506715/nested-skos-concept-schemes

    paginae.append(f"<urn:mdciii:{basi}()> a skos:ConceptScheme ;\n"
                   f"  rdfs:label \"({basi})\" .")

    paginae.append('')
    paginae.append(f"<urn:mdciii:{basi}:1()> a skos:Collection ;\n"
                   f"  rdfs:label \"({basi}:1)\" ;\n"
                   f"  skos:inScheme <urn:mdciii:{basi}()> ;\n"
                   f"  skos:member <urn:mdciii:{basi}:1:0()> ."
                   )

    paginae.append('')
    # This pattern is used to reference full URLs and force tools undestand
    # that the path is an OWL ontology
    paginae.append(f"<urn:mdciii:{basi}:1:0(1)> a owl:Ontology .")

    paginae.append('')
    paginae.append("<urn:mdciii:{0}:1:0()> a skos:Collection ;\n"
                   "  rdfs:label \"({0}:1)\" ;".format(
                       basi))
    paginae.append("  skos:member\n    {0} .".format(
        " ,\n    ".join(
            map(lambda x: f'<urn:mdciii:{x}()>', numerodiatio_collecti))
    ))
    # We're not using skos:hasTopConcept anymore, but skos:member
    # paginae.append("  skos:hasTopConcept\n    {0} .".format(
    #     " ,\n    ".join(
    #         map(lambda x: f'<urn:mdciii:{x}:0>', numerodiatio_collecti))
    # ))

    paginae.append('')

    for linea in data:
        numerodiatio_re = basi + ':' + linea[1]
        ordo_maximo = int(linea[4])

        _paginae_basi = []
        _paginae_primus = []
        _paginae_secundus = []
        _paginae_tertius = []
        _paginae_quartus = []
        _paginae_quintus = []
        _paginae_sextus = []

        # paginae.append(
        # f'<urn:mdciii:{numerodiatio_re}:0()> a skos:Collection')
        paginae.append(
            f"<urn:mdciii:{numerodiatio_re}()> a skos:Collection ;\n"
            f"  rdfs:label \"({numerodiatio_re}:0)\" ;\n"
            f"  skos:member <urn:mdciii:{numerodiatio_re}:0> ."
        )
        paginae.append('  # @TODO add lower administrative levels here')
        paginae.append('')
        # _paginae_basi.append(
        #     f'  rdfs:label "{numerodiatio_re}:0"')

        _paginae_basi.append(
            f'<urn:mdciii:{numerodiatio_re}:0> a skos:Concept')
        _paginae_basi.append(
            f'  rdfs:label "{numerodiatio_re}:0"')
        # _paginae_basi.append(
        #     f'  skos:prefLabel "{numerodiatio_re}"@mul-Zyyy-x-n1603')
        _paginae_basi.append(f'  p:P2082 "{linea[1].zfill(3)}"')
        # ISO 3166-1 numeric
        _paginae_basi.append(f'  p:P299 "{linea[1].zfill(3)}"')
        _paginae_basi.append(f'  p:P298 "{linea[2]}"')
        _paginae_basi.append(f'  p:P297 "{linea[3]}"')

        # Disablig topConceptOf
        # _paginae_basi.append(
        #     f'  skos:topConceptOf <urn:mdciii:{basi}:1:0()>')
        # f'  skos:topConceptOf <urn:{basi}>')

        # ordo_nunc = 1

        if ordo_maximo >= 1:
            # _paginae_basi.append(
            #     f'  skos:related <urn:mdciii:{numerodiatio_re}:1()>')

            _paginae_primus.append(
                f'<urn:mdciii:{numerodiatio_re}:1()> a skos:Collection')
            _paginae_primus.append(
                f'  rdfs:label "({numerodiatio_re}:1)"')
            # _paginae_primus.append(
            #     f'  skos:related <urn:mdciii:{numerodiatio_re}:0>')

        if ordo_maximo >= 2:
            # _paginae_primus.append(
            #     f'  skos:related <urn:mdciii:{numerodiatio_re}:2>')

            _paginae_secundus.append(
                f'<urn:mdciii:{numerodiatio_re}:2()> a skos:Collection')
            _paginae_secundus.append(
                f'  rdfs:label "({numerodiatio_re}:2)"')
            # _paginae_secundus.append(
            #     f'  skos:related <urn:mdciii:{numerodiatio_re}:1>')

        if ordo_maximo >= 3:
            # _paginae_secundus.append(
            #     f'  skos:related <urn:mdciii:{numerodiatio_re}:3>')

            _paginae_tertius.append(
                f'<urn:mdciii:{numerodiatio_re}:3()> a skos:Collection')
            _paginae_tertius.append(
                f'  rdfs:label "({numerodiatio_re}:3)"')
            # _paginae_tertius.append(
            #     f'  skos:related <urn:mdciii:{numerodiatio_re}:2>')

        if ordo_maximo >= 4:
            # _paginae_tertius.append(
            #     f'  skos:related <urn:mdciii:{numerodiatio_re}:4>')

            _paginae_quartus.append(
                f'<urn:mdciii:{numerodiatio_re}:4> a skos:Collection')
            _paginae_quartus.append(
                f'  rdfs:label "({numerodiatio_re}:4)"')
            # _paginae_quartus.append(
            #     f'  skos:related <urn:mdciii:{numerodiatio_re}:3>')

        if ordo_maximo >= 5:
            # _paginae_quartus.append(
            #     f'  skos:related <urn:mdciii:{numerodiatio_re}:5>')

            _paginae_quintus.append(
                f'<urn:mdciii:{numerodiatio_re}:5> a skos:Collection')
            _paginae_quintus.append(
                f'  rdfs:label "({numerodiatio_re}:5)"')
            # _paginae_quintus.append(
            #     f'  skos:related <urn:mdciii:{numerodiatio_re}:4>')

        if ordo_maximo == 6:
            # _paginae_quintus.append(
            #     f'  skos:related <urn:mdciii:{numerodiatio_re}:6>')

            _paginae_sextus.append(
                f'<urn:mdciii:{numerodiatio_re}:6()> a skos:Collection')
            _paginae_sextus.append(
                f'  rdfs:label "({numerodiatio_re}:6)"')
            # _paginae_sextus.append(
            #     f'  skos:related <urn:mdciii:{numerodiatio_re}:5>')

        if ordo_maximo > 6:
            raise ValueError

        #     _paginae_basi.append(
        #         f'  skos:broaderTransitive <urn:{numerodiatio_re}:1>')

        #     paginae.append(
        #         f'  skos:broaderTransitive <urn:{numerodiatio_re}:1> ;')
        #     paginae.append('')
        #     paginae.append(
        #         "<urn:{0}:1> a skos:Concept ;".format(numerodiatio_re))
        #     paginae.append("  skos:prefLabel \"{0}:1\"@mul-Zyyy-x-n1603 ;".format(
        #         numerodiatio_re))
        #     paginae.append(
        #         f'  skos:narrowerTransitive <urn:{numerodiatio_re}> .')

        if len(_paginae_basi) > 0:
            paginae.append("{0} .\n".format(
                " ;\n".join(_paginae_basi)
            ))
        if len(_paginae_primus) > 0:
            paginae.append("{0} .\n".format(
                " ;\n".join(_paginae_primus)
            ))
        if len(_paginae_secundus) > 0:
            paginae.append("{0} .\n".format(
                " ;\n".join(_paginae_secundus)
            ))
        if len(_paginae_tertius) > 0:
            paginae.append("{0} .\n".format(
                " ;\n".join(_paginae_tertius)
            ))
        if len(_paginae_quartus) > 0:
            paginae.append("{0} .\n".format(
                " ;\n".join(_paginae_quartus)
            ))
        if len(_paginae_quintus) > 0:
            paginae.append("{0} .\n".format(
                " ;\n".join(_paginae_quintus)
            ))
        if len(_paginae_sextus) > 0:
            paginae.append("{0} .\n".format(
                " ;\n".join(_paginae_sextus)
            ))
        continue

        # paginae_basi = (
        #     f'<urn:{numerodiatio_re}> a skos:ConceptScheme ;\n'
        #     f'  skos:prefLabel "{numerodiatio_re}"@mul-Zyyy-x-n1603 ;\n'
        #     f'  skos:topConceptOf <urn:{basi}> .\n'
        # )
        # paginae_basi += ("  skos:topConceptOf\n    {0} .".format(
        #     " ,\n    ".join(map(lambda x: f'<urn:{x}>', numerodiatio_collecti))
        # ))

        # paginae.append("<urn:{0}> a skos:Concept ;".format(numerodiatio_re))
        # paginae.append('  skos:topConceptOf <urn:{0}> ;'.format(basi))
        # paginae.append("  skos:prefLabel \"{0}\"@mul-Zyyy-x-n1603 ;".format(
        #                numerodiatio_re))

        # paginae.append("  # unm49 {0}".format(linea[1]))
        # paginae.append("  # v_iso3 {0}".format(linea[2]))
        # paginae.append("  # v_iso2 {0}".format(linea[3]))

        paginae.append(paginae_basi)

        if ordo_maximo >= 1:

            _paginae_basi.append(
                f'  skos:broaderTransitive <urn:{numerodiatio_re}:1>')

            paginae.append(
                f'  skos:broaderTransitive <urn:{numerodiatio_re}:1> ;')
            paginae.append('')
            paginae.append(
                "<urn:{0}:1> a skos:Concept ;".format(numerodiatio_re))
            paginae.append("  skos:prefLabel \"{0}:1\"@mul-Zyyy-x-n1603 ;".format(
                numerodiatio_re))
            paginae.append(
                f'  skos:narrowerTransitive <urn:{numerodiatio_re}> .')

        # if ordo_maximo >= 2:

        #     paginae.append(
        #         f'  skos:broaderTransitive <urn:{numerodiatio_re}:2> ;')
        #     paginae.append('')
        #     paginae.append(
        #         "<urn:{0}:2> a skos:Concept ;".format(numerodiatio_re))
        #     paginae.append(
        #         "  skos:prefLabel \"{0}:1\"@mul-Zyyy-x-n1603 ;".format(
        #             numerodiatio_re))
        #     paginae.append(
        #         f'  skos:narrowerTransitive <urn:{numerodiatio_re}:1> ;')

        # if ordo_maximo >= 3:

        #     paginae.append(
        #         f'  skos:broaderTransitive <urn:{numerodiatio_re}:3> ;')
        #     paginae.append('')
        #     paginae.append(
        #         "<urn:{0}:3> a skos:Concept ;".format(numerodiatio_re))
        #     paginae.append(
        #         "  skos:prefLabel \"{0}:1\"@mul-Zyyy-x-n1603 ;".format(
        #             numerodiatio_re))
        #     paginae.append(
        #         f'  skos:narrowerTransitive <urn:{numerodiatio_re}:2> ;')

        # if ordo_maximo >= 4:

        #     paginae.append(
        #         f'  skos:broaderTransitive <urn:{numerodiatio_re}:4> ;')
        #     paginae.append('')
        #     paginae.append(
        #         "<urn:{0}:4> a skos:Concept ;".format(numerodiatio_re))
        #     paginae.append(
        #         "  skos:prefLabel \"{0}:1\"@mul-Zyyy-x-n1603 ;".format(
        #             numerodiatio_re))
        #     paginae.append(
        #         f'  skos:narrowerTransitive <urn:{numerodiatio_re}:3> ;')

        # if ordo_maximo >= 5:

        #     paginae.append(
        #         f'  skos:broaderTransitive <urn:{numerodiatio_re}:5> ;')
        #     paginae.append('')
        #     paginae.append(
        #         "<urn:{0}:5> a skos:Concept ;".format(numerodiatio_re))
        #     paginae.append(
        #         "  skos:prefLabel \"{0}:1\"@mul-Zyyy-x-n1603 ;".format(
        #             numerodiatio_re))
        #     paginae.append(
        #         f'  skos:narrowerTransitive <urn:{numerodiatio_re}:4> ;')

        # if ordo_maximo >= 6:

        #     paginae.append(
        #         f'  skos:broaderTransitive <urn:{numerodiatio_re}:6> ;')
        #     paginae.append('')
        #     paginae.append(
        #         "<urn:{0}:6> a skos:Concept ;".format(numerodiatio_re))
        #     paginae.append(
        #         "  skos:prefLabel \"{0}:1\"@mul-Zyyy-x-n1603 ;".format(
        #             numerodiatio_re))
        #     paginae.append(
        #         f'  skos:narrowerTransitive <urn:{numerodiatio_re}:6> ;')

        paginae.append('')

    return paginae


if __name__ == "__main__":

    est_cli = Cli()
    args = est_cli.make_args()

    est_cli.execute_cli(args)
