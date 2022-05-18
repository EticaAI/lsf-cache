#!/usr/bin/env python3
# ==============================================================================
#
#          FILE:  999999999_10263485.py
#
#         USAGE:  ./999999999/0/999999999_10263485.py
#                 ./999999999/0/999999999_10263485.py --help
#
#   DESCRIPTION:  RUn /999999999/0/999999999_10263485.py --help
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
#       CREATED:  2022-05-16 16:29 UTC based on hotfix0s.py
#      REVISION:  ---
# ==============================================================================

import sys
import argparse
import csv
import re
from pathlib import Path
from os.path import exists

from functools import reduce
from typing import (
    Any,
    Dict,
    List,
)

import yaml

import xml.etree.ElementTree as XMLElementTree

STDIN = sys.stdin.buffer

NOMEN = '999999999_10263485'

DESCRIPTION = """
{0} Processamento de dados de referência do CNES (Cadastro Nacional de
Estabelecimentos de Saúde) do Brasil.

@see - https://github.com/EticaAI/lexicographi-sine-finibus/issues/42
     - wiki.saude.gov.br/cnes/index.php/Categoria:Contexto_Hist%C3%B3rico
       - "(...) O CNES possui atualmente quase 300 mil estabelecimentos de
         saúde cadastrados (CNES, jul/2015), dos quais mais de 2/3 não
         atendem ao SUS, sendo que mais de 150 mil são consultórios ou
         pequenas clínicas privadas. (...)"

Trivia:
- Q10263485, https://www.wikidata.org/wiki/Q10263485
  - DATASUS
  - "DATASUS é o departamento de informática do Sistema Único de Saúde do
     Brasil. É responsável, também, pelos sistemas e aplicativos necessários
     para registrar e processar as informações de saúde. Um exemplo
     é o Cadastro Nacional de Estabelecimentos de Saúde (CNES), (...)"
""".format(__file__)

__EPILOGUM__ = """
------------------------------------------------------------------------------
                            EXEMPLŌRUM GRATIĀ
------------------------------------------------------------------------------
    {0} --methodus=datasus_xmlcnae 999999/0/xmlCNES.xml
    cat 999999/0/xmlCNES.xml | {0} --methodus=datasus_xmlcnae

    {0} --methodus=datasus_xmlcnae 999999/0/xmlCNES.xml \
--objectivum-formato=csv > 999999/0/xmlCNES.csv

    {0} --methodus=datasus_xmlcnae 999999/0/xmlCNES.xml \
--objectivum-formato=hxl_csv > 999999/0/xmlCNES.hxl.csv

    {0} --methodus=datasus_xmlcnae 999999/0/xmlCNES.xml \
--objectivum-formato=hxltm_csv > 999999/0/xmlCNES.tm.hxl.csv

@TODO: fazer funcionar com stream de XML (não apenas por arquivo)
------------------------------------------------------------------------------
                            EXEMPLŌRUM GRATIĀ
------------------------------------------------------------------------------
""".format(__file__)

LIKELY_NUMERIC = [
    '#item+conceptum+codicem',
    '#status+conceptum',
    '#item+rem+i_qcc+is_zxxx+ix_n1603',
    '#item+rem+i_qcc+is_zxxx+ix_iso5218',
]
# https://en.wiktionary.org/wiki/tabula#Latin
XML_AD_CSV_TABULAE = {
    'CO_UNIDADE': 'CO_UNIDADE',
    'NO_FANTASIA': 'NO_FANTASIA',
    'CO_MUNICIPIO_GESTOR': 'CO_MUNICIPIO_GESTOR',
    'NU_CNPJ': 'NU_CNPJ',
    'CO_CNES': 'CO_CNES',
    'DT_ATUALIZACAO': 'DT_ATUALIZACAO',
    'TP_UNIDADE': 'TP_UNIDADE',
}

CSV_AD_HXLTM_TABULAE = {
    # @TODO: create wikiq
    'CO_UNIDADE': '#item+rem+i_qcc+is_zxxx+ix_brcnae',
    'NO_FANTASIA': '#meta+NO_FANTASIA',
    'CO_MUNICIPIO_GESTOR': '#item+rem+i_qcc+is_zxxx+ix_wikip1585',
    'NU_CNPJ': '#item+rem+i_qcc+is_zxxx+ix_wikip6204',
    'CO_CNES': '#meta+CO_CNES',
    'DT_ATUALIZACAO': '#meta+DT_ATUALIZACAO',
    'TP_UNIDADE': '#meta+TP_UNIDADE',
}

SYSTEMA_SARCINAE = str(Path(__file__).parent.resolve())
PROGRAMMA_SARCINAE = str(Path().resolve())
ARCHIVUM_CONFIGURATIONI_DEFALLO = [
    SYSTEMA_SARCINAE + '/' + NOMEN + '.meta.yml',
    PROGRAMMA_SARCINAE + '/' + NOMEN + '.meta.yml',
]

# ./999999999/0/999999999_10263485.py 999999/0/1603_1_1--old.csv 999999/0/1603_1_1--new.csv


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

    def make_args(self, hxl_output=True):
        # parser = argparse.ArgumentParser(description=DESCRIPTION)
        parser = argparse.ArgumentParser(
            prog="999999999_10263485",
            description=DESCRIPTION,
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog=__EPILOGUM__
        )

        parser.add_argument(
            'infile',
            help='Arquivo de entrada',
            nargs='?'
        )

        parser.add_argument(
            '--methodus',
            help='Modo de operação.',
            dest='methodus',
            nargs='?',
            choices=[
                'datasus_xmlcnae',
                # 'data-apothecae',
                # 'hxltm-explanationi',
                # 'opus-temporibus',
                # 'status-quo',
                # 'deprecatum-dictionaria-numerordinatio'
            ],
            # required=True
            default='datasus_xmlcnae'
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
            # print("ERROR. Please pipe data in. \nExample:\n"
            #       "  cat data.txt | {0} --actionem-quod-sparql\n"
            #       "  printf \"Q1065\\nQ82151\\n\" | {0} --actionem-quod-sparql"
            #       "".format(__file__))
            # print('non stdin')
            _infile = pyargs.infile
            # return self.EXIT_ERROR
        else:
            # print('est stdin')
            _stdin = stdin

        # print(pyargs.objectivum_formato)
        # print(pyargs)

        # if _stdin is not None:
        #     for line in sys.stdin:
        #         # print('oi')
        #         codicem = line.replace('\n', ' ').replace('\r', '')

        # hf = CliMain(self.pyargs.infile, self.pyargs.outfile)
        climain = CliMain(
            infile=_infile, stdin=_stdin,
            pyargs=pyargs,
            configuratio=configuratio
        )
        if pyargs.methodus == 'datasus_xmlcnae':
            return climain.execute_ex_datasus_xmlcnae()

        print('Unknow option.')
        return self.EXIT_ERROR


class CliMain:
    """Remove .0 at the end of CSVs from data exported from XLSX and likely
    to have numeric values (and trigger weird bugs)
    """
    delimiter = ','

    # def __init__(self, infile: str = None, stdin=None,
    #              objectivum_formato: str = 'hxltm-csv'):
    #     """
    #     Constructs all the necessary attributes for the Cli object.
    #     """
    #     self.infile = infile
    #     self.stdin = stdin
    #     self.objectivum_formato = objectivum_formato

    #     # self.outfile = outfile
    #     self.header = []
    #     self.header_index_fix = []


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
        # self.configuratio = configuratio

        # delimiter = ','
        if self.objectivum_formato in ['tsv', 'hxltm_tsv', 'hxl_tsv']:
            self.delimiter = "\t"

        methodus_ex_tabulae = configuratio['methodus'][self.methodus]

        self.configuratio = methodus_ex_tabulae

        self.tabula = TabulaAdHXLTM(
            methodus_ex_tabulae=methodus_ex_tabulae,
            methodus=self.methodus,
            objectivum_formato=self.objectivum_formato
        )

    def process_row(self, row: list) -> list:
        if len(self.header) == 0:
            if row[0].strip().startswith('#'):
                self.header = row
                for index, item in enumerate(self.header):
                    item_norm = item.strip().replace(" ", "")
                    for likely in LIKELY_NUMERIC:
                        # print(item_norm, likely)
                        if item_norm.startswith(likely):
                            self.header_index_fix.append(index)
                # print('oi header', self.header_index_fix, self.header)
        else:
            for index_fix in self.header_index_fix:
                row[index_fix] = re.sub('\.0$', '', row[index_fix].strip())
        return row

    def execute_ex_datasus_xmlcnae(self):
        # print('@TODO copy logic from https://github.com/EticaAI/hxltm/blob/main/bin/hxltmdexml.py')

        _source = self.infile if self.infile is not None else self.stdin
        delimiter = ','
        if self.objectivum_formato in ['tsv', 'hxltm_tsv']:
            delimiter = "\t"
        objectivum = csv.writer(
            sys.stdout, delimiter=delimiter, quoting=csv.QUOTE_MINIMAL)

        # self.iteratianem = XMLElementTree.iterparse(
        iteratianem = XMLElementTree.iterparse(
            # source=self.fontem_archivum,
            # source=self.infile,
            source=_source,
            events=('start', 'end')
            # events=('end')
        )

        caput = self.configuratio['__de_xml_ad_csv']

        _to_int = []
        if '__de_xml_ad_csv__cast_int' in self.configuratio:
            _to_int = self.configuratio['__de_xml_ad_csv__cast_int']

        if self.objectivum_formato in ['tsv', 'csv']:
            objectivum.writerow(caput)
        else:
            objectivum.writerow(
                self.tabula.caput_translationi(caput))
        # caput = []
        # caput_okay = False
        for event, elem in iteratianem:
            if event == 'end':
                # print(elem)
                if elem.tag.upper() != 'ROW':
                    continue
                if hasattr(elem, 'attrib'):
                    lineam = []

                    for item in caput:
                        if item in elem.attrib:
                            _res = elem.attrib[item]
                            if len(_to_int) > 0 and item in _to_int:
                                _res = int(_res)
                            lineam.append(_res)
                        else:
                            lineam.append('')
                    objectivum.writerow(lineam)

        return Cli.EXIT_OK

    def execute(self):
        with open(self.infile, newline='') as infilecsv:
            with open(self.outfile, 'w', newline='') as outfilecsv:
                spamreader = csv.reader(infilecsv)
                spamwriter = csv.writer(outfilecsv)
                for row in spamreader:
                    # spamwriter.writerow(row)
                    spamwriter.writerow(self.process_row(row))
                    # self.data.append(row)


def de_dotted(self, dotted_key: str,  # pylint: disable=invalid-name
              default: Any = None, fontem: dict = None) -> Any:
    """
    Trivia: dē, https://en.wiktionary.org/wiki/de#Latin
    Examples:
        >>> exemplum = {'a': {'a2': 123}, 'b': 456}
        >>> otlg = HXLTMOntologia(exemplum)
        >>> otlg.de('a.a2', fontem=exemplum)
        123
    Args:
        dotted_key (str): Dotted key notation
        default ([Any], optional): Value if not found. Defaults to None.
        fontem (dict): An nested object to search
    Returns:
        [Any]: Return the result. Defaults to default
    """
    if fontem is None:
        fontem = self.crudum

    keys = dotted_key.split('.')
    return reduce(
        lambda d, key: d.get(
            key) if d else default, keys, fontem
    )


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
        # @TODO: generalize this block with 999999999_268072.py

        # clavis_normationi = self.clavis_normationi(clavis)
        clavis_normationi = clavis

        if not clavis or len(clavis) == 0:
            return ''

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
            '{{caput_clavi}}', clavis)

        hxl_hashtag = forma.replace(
            '{{caput_clavi_normali}}', self.clavis_normationi(clavis))

        return hxl_hashtag


if __name__ == "__main__":

    est_cli = Cli()
    args = est_cli.make_args()

    est_cli.execute_cli(args)
