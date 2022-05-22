#!/usr/bin/env python3
# ==============================================================================
#
#          FILE:  999999999_268072.py
#
#         USAGE:  ./999999999/0/999999999_268072.py
#                 ./999999999/0/999999999_268072.py --help
#
#   DESCRIPTION:  RUN /999999999/0/999999999_268072.py --help
#                 - Q268072, https://www.wikidata.org/wiki/Q268072
#                   - IBGE - Instituto Brasileiro de Geografia e Estatística
#                     (Brasil)
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
#       CREATED:  2022-05-16 21:16 UTC based on 999999999_10263485.py
#      REVISION:  ---
# ==============================================================================

import sys
import argparse
import csv
# import re
from pathlib import Path
from os.path import exists

import json
import yaml
# import urllib.request
import requests

STDIN = sys.stdin.buffer

NOMEN = '999999999_268072'

DESCRIPTION = """
{0} Processamento de dados de referência do IBGE (Brasil).

@see https://github.com/EticaAI/lexicographi-sine-finibus/issues/42
@see https://servicodados.ibge.gov.br/api/docs

Trivia:
- Q268072, https://www.wikidata.org/wiki/Q268072
  - IBGE - Instituto Brasileiro de Geografia e Estatística
  - "instituto público da administração federal brasileira criado em 1934
     e instalado em 1936 com o nome de Instituto Nacional de Estatística (...)"
""".format(__file__)

__EPILOGUM__ = """
------------------------------------------------------------------------------
                            EXEMPLŌRUM GRATIĀ
------------------------------------------------------------------------------
    {0} --methodus=ibge_un_adm2 --objectivum-formato=uri_fonti

    {0} --methodus=ibge_un_adm2 --objectivum-formato=json_fonti

    {0} --methodus=ibge_un_adm2 --objectivum-formato=csv

    {0} --methodus=ibge_un_adm2 --objectivum-formato=json_fonti_formoso \
> 999999/0/ibge_un_adm2.json
    cat 999999/0/ibge_un_adm2.json | {0} --objectivum-formato=csv \
> 999999/0/ibge_un_adm2.csv
    cat 999999/0/ibge_un_adm2.json | {0} --objectivum-formato=hxl_csv \
> 999999/0/ibge_un_adm2.hxl.csv
    cat 999999/0/ibge_un_adm2.json | {0} --objectivum-formato=hxltm_csv \
> 999999/0/ibge_un_adm2.tm.hxl.csv

------------------------------------------------------------------------------
                            EXEMPLŌRUM GRATIĀ
------------------------------------------------------------------------------
""".format(__file__)

# LIKELY_NUMERIC = [
#     '#item+conceptum+codicem',
#     '#status+conceptum',
#     '#item+rem+i_qcc+is_zxxx+ix_n1603',
#     '#item+rem+i_qcc+is_zxxx+ix_iso5218',
# ]
# https://en.wiktionary.org/wiki/tabula#Latin
# XML_AD_CSV_TABULAE = {
#     'CO_UNIDADE': 'CO_UNIDADE',
#     'NO_FANTASIA': 'NO_FANTASIA',
#     'CO_MUNICIPIO_GESTOR': 'CO_MUNICIPIO_GESTOR',
#     'NU_CNPJ': 'NU_CNPJ',
#     'CO_CNES': 'CO_CNES',
#     'DT_ATUALIZACAO': 'DT_ATUALIZACAO',
#     'TP_UNIDADE': 'TP_UNIDADE',
# }

# CSV_AD_HXLTM_TABULAE = {
#     # @TODO: create wikiq
#     'CO_UNIDADE': '#item+rem+i_qcc+is_zxxx+ix_brcnae',
#     'NO_FANTASIA': '#meta+NO_FANTASIA',
#     'CO_MUNICIPIO_GESTOR': '#item+rem+i_qcc+is_zxxx+ix_wikip1585',
#     'NU_CNPJ': '#item+rem+i_qcc+is_zxxx+ix_wikip6204',
#     'CO_CNES': '#meta+CO_CNES',
#     'DT_ATUALIZACAO': '#meta+DT_ATUALIZACAO',
#     'TP_UNIDADE': '#meta+TP_UNIDADE',
# }

SYSTEMA_SARCINAE = str(Path(__file__).parent.resolve())
PROGRAMMA_SARCINAE = str(Path().resolve())
ARCHIVUM_CONFIGURATIONI_DEFALLO = [
    SYSTEMA_SARCINAE + '/' + NOMEN + '.meta.yml',
    PROGRAMMA_SARCINAE + '/' + NOMEN + '.meta.yml',
]

# https://servicodados.ibge.gov.br/api/v1/localidades/distritos?view=nivelado&oorderBy=municipio-id
# https://servicodados.ibge.gov.br/api/v1/localidades/municipios?view=nivelado&orderBy=id
METHODUS_FONTI = {
    'ibge_un_adm2': 'https://servicodados.ibge.gov.br/api' +
    '/v1/localidades/municipios?view=nivelado&orderBy=id'
}

# @TODO implementar malhas https://servicodados.ibge.gov.br/api/docs/malhas?versao=3
# ./999999999/0/999999999_268072.py 999999/0/1603_1_1--old.csv 999999/0/1603_1_1--new.csv


class Cli:

    EXIT_OK = 0
    EXIT_ERROR = 1
    EXIT_SYNTAX = 2

    def __init__(self):
        """
        Constructs all the necessary attributes for the Cli object.
        """

    def _quod_configuratio(self, archivum_configurationi: str = None) -> dict:
        """_quod_configuratio

        Args:
            archivum_configurationi (str, optional):

        Returns:
            (dict):
        """
        archivae = ARCHIVUM_CONFIGURATIONI_DEFALLO
        if archivum_configurationi is not None:
            if not exists(archivum_configurationi):
                raise FileNotFoundError(
                    'archivum_configurationi {0}'.format(
                        archivum_configurationi))
            archivae.append(archivum_configurationi)

        for item in archivae:
            if exists(item):
                with open(item, "r") as read_file:
                    datum = yaml.safe_load(read_file)
                    return datum

        raise FileNotFoundError(
            'archivum_configurationi {0}'.format(
                str(archivae)))

    def make_args(self, hxl_output=True):
        # parser = argparse.ArgumentParser(description=DESCRIPTION)
        parser = argparse.ArgumentParser(
            prog="999999999_268072",
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
            help='Modo de operação.',
            dest='methodus',
            nargs='?',
            choices=[
                'ibge_un_adm2',
                # 'data-apothecae',
                # 'hxltm-explanationi',
                # 'opus-temporibus',
                # 'status-quo',
                # 'deprecatum-dictionaria-numerordinatio'
            ],
            # required=True
            default='ibge_un_adm2'
        )

        # objectīvum, n, s, nominativus,
        #                       https://en.wiktionary.org/wiki/objectivus#Latin
        # fōrmātō, n, s, dativus, https://en.wiktionary.org/wiki/formatus#Latin
        parser.add_argument(
            '--objectivum-formato',
            help='Formato do arquivo exportado',
            dest='objectivum_formato',
            nargs='?',
            choices=[
                'uri_fonti',
                'json_fonti',
                'json_fonti_formoso',
                'csv',
                'tsv',
                'hxl_csv',
                'hxl_tsv',
                'hxltm_csv',
                'hxltm_tsv',
            ],
            # required=True
            default='csv'
        )

        # archīvum, n, s, nominativus, https://en.wiktionary.org/wiki/archivum
        # cōnfigūrātiōnī, f, s, dativus,
        #                      https://en.wiktionary.org/wiki/configuratio#Latin
        parser.add_argument(
            '--archivum-configurationi',
            help='Arquivo de configuração .meta.yml',
            dest='archivum_configurationi',
            nargs='?',
            default=None
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

        _infile = None
        _stdin = None
        configuratio = self._quod_configuratio(pyargs.archivum_configurationi)

        if stdin.isatty():
            _infile = pyargs.infile
        else:
            _stdin = stdin

        json_fonti_texto = None

        if _stdin is not None:
            json_fonti_texto = ''
            for line in sys.stdin:
                json_fonti_texto += line

        # climain = CliMain(
        #     infile=_infile, stdin=_stdin,
        #     objectivum_formato=pyargs.objectivum_formato,
        #     methodus=pyargs.objectivum_formato,
        #     configuratio=configuratio)
        climain = CliMain(
            infile=_infile, stdin=_stdin,
            pyargs=pyargs,
            configuratio=configuratio)

        if pyargs.objectivum_formato == 'uri_fonti':
            print(METHODUS_FONTI[pyargs.methodus])
            return self.EXIT_OK

        if pyargs.objectivum_formato == 'json_fonti':
            return climain.json_fonti(METHODUS_FONTI[pyargs.methodus])

        if pyargs.objectivum_formato == 'json_fonti_formoso':
            return climain.json_fonti(
                METHODUS_FONTI[pyargs.methodus],
                formosum=True,
                # ex_texto=True
            )

        if pyargs.objectivum_formato in ['csv', 'tsv']:
            if json_fonti_texto is None:
                json_fonti_texto = climain.json_fonti(
                    METHODUS_FONTI[pyargs.methodus], ex_texto=True)
            # print('json_fonti_texto', json_fonti_texto)
            return climain.objectivum_formato_csv(json_fonti_texto)

        if pyargs.objectivum_formato in [
                'hxl_csv', 'hxltm_csv', 'hxl_tsv', 'hxltm_tsv']:
            if json_fonti_texto is None:
                json_fonti_texto = climain.json_fonti(
                    METHODUS_FONTI[pyargs.methodus], ex_texto=True)
            return climain.objectivum_formato_csv(json_fonti_texto)

        # if pyargs.methodus == 'ibge_un_adm2':
        #     return climain.execute_ex_datasus_xmlcnae()
        # if pyargs.methodus == 'datasus-xmlcnae':
        #     return climain.execute_ex_datasus_xmlcnae()

        print('Unknow option.')
        return self.EXIT_ERROR


class CliMain:
    """Remove .0 at the end of CSVs from data exported from XLSX and likely
    to have numeric values (and trigger weird bugs)
    """

    delimiter = ','

    def __init__(
            self, infile: str = None, stdin=None,
            pyargs: dict = None, configuratio: dict = None):
        """
        Constructs all the necessary attributes for the Cli object.
        """
        self.infile = infile
        self.stdin = stdin
        self.objectivum_formato = pyargs.objectivum_formato
        self.methodus = pyargs.methodus
        self.configuratio = configuratio

        # delimiter = ','
        if self.objectivum_formato in ['tsv', 'hxltm_tsv', 'hxl_tsv']:
            self.delimiter = "\t"

        methodus_ex_tabulae = configuratio['methodus'][self.methodus]

        self.tabula = TabulaAdHXLTM(
            methodus_ex_tabulae=methodus_ex_tabulae,
            methodus=self.methodus,
            objectivum_formato=self.objectivum_formato
        )

        # self.outfile = outfile
        # self.header = []
        # self.header_index_fix = []

    def json_fonti(
            self, uri: str, formosum: bool = False, ex_texto: bool = False) -> str:

        # print('oooi', uri)
        # data = urllib.request.urlopen(uri).read()
        r = requests.get(uri)
        # print('oooi2', data)
        output = json.loads(r.text)
        # resultatum = output
        if formosum:
            output = json.dumps(output,
                                indent=2, ensure_ascii=False, sort_keys=False)
        if ex_texto:
            return json.dumps(output)

        print(output)
        return Cli.EXIT_OK

    def objectivum_formato_csv(self, json_fonti_texto: str) -> str:

        objectivum = csv.writer(
            sys.stdout, delimiter=self.delimiter, quoting=csv.QUOTE_MINIMAL)
        # caput = []
        # caput_okay = False
        datus_fonti = json.loads(json_fonti_texto)

        caput_translationi = \
            self.tabula.caput_translationi(datus_fonti[0].keys())

        # objectivum.writerow(datus_fonti[0].keys())
        objectivum.writerow(caput_translationi)
        # return Cli.EXIT_OK
        for item in datus_fonti:
            objectivum.writerow(item.values())

        return Cli.EXIT_OK

    # def execute(self):
    #     with open(self.infile, newline='') as infilecsv:
    #         with open(self.outfile, 'w', newline='') as outfilecsv:
    #             spamreader = csv.reader(infilecsv)
    #             spamwriter = csv.writer(outfilecsv)
    #             for row in spamreader:
    #                 # spamwriter.writerow(row)
    #                 spamwriter.writerow(self.process_row(row))
    #                 # self.data.append(row)


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


if __name__ == "__main__":

    est_cli = Cli()
    args = est_cli.make_args()

    est_cli.execute_cli(args)
