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

#    ./999999999/0/1603_3_12.py
#    NUMERORDINATIO_BASIM="/external/ndata" ./999999999/0/1603_3_12.py


import os
import sys
import argparse
# from pathlib import Path
from typing import (
    # Type,
    Union
)

# from itertools import permutations
from itertools import product
# valueee = list(itertools.permutations([1, 2, 3]))
import csv

NUMERORDINATIO_BASIM = os.getenv('NUMERORDINATIO_BASIM', os.getcwd())
NUMERORDINATIO_DEFALLO = int(os.getenv('NUMERORDINATIO_DEFALLO', '60'))  # �
NUMERORDINATIO_MISSING = "�"
DESCRIPTION = """
2600.60 is (...)
"""

# In Python2, sys.stdin is a byte stream; in Python3, it's a text stream
STDIN = sys.stdin.buffer

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
# ./999999999/0/1603_3_12.py --actionem-sparql

class CS1603z3z12:
    def __init__(self):
        self.D1613_1_51 = self._init_1613_1_51_datum()
        # self.scientia_de_scriptura = {}
        # self.scientia_de_scriptura = self.D1613_2_60
        # self.cifram_signaturae = 6  # TODO: make it flexible
        # self.codex_verbum_tabulae = []
        # self.verbum_limiti = 2
        self.resultatum_separato = "\t"

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
                int_clavem = int(conceptum['#item+conceptum+codicem'])
                datum[int_clavem] = {}
                for clavem, rem in conceptum.items():
                    if not clavem.startswith('#item+conceptum+codicem'):
                        datum[int_clavem][clavem] = rem

        return datum

    def est_resultatum_separato(self, resultatum_separato: str):
        self.resultatum_separato = resultatum_separato
        return self

    def exportatum_sparql(self):
        resultatum = []
        resultatum.append('#TODO')
        resultatum.append(str(self.D1613_1_51))
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
        parser = argparse.ArgumentParser(description=DESCRIPTION)

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

        # neo_codex.add_argument(
        #     '--actionem-verbum-simplex',
        #     help='Do not generate the codes. Just calculate the full matrix ' +
        #     'of possible codes using the rules',
        #     metavar='',
        #     dest='verbum_simplex',
        #     nargs='?'
        # )

        # neo_codex.add_argument(
        #     '--verbum-limiti',
        #     help='Codeword limit when when creating multiplication tables' +
        #     'Most western codetables are between 2 and 4. ' +
        #     'Defaults to 2',
        #     metavar='verbum_limiti',
        #     default="2",
        #     nargs='?'
        # )

        # neo_codex.add_argument(
        #     '--codex-verbum-tabulae',
        #     help='Multiplication table of the code words. ' +
        #     'First character determine the spliter. ' +
        #     'Example 1: " 0 1 2 3 4 5 6 7 8 9 a b c d e f ". '
        #     'Example 2: ",a,e,i,o,u,"',
        #     nargs='?'
        # )

        # neo_codex.add_argument(
        #     '--resultatum-limiti',
        #     help='Codeword limit when when creating multiplication tables' +
        #     'Most western codetables are between 2 and 4. ' +
        #     'Defaults to 2',
        #     metavar='verbum_limiti',
        #     default="2",
        #     nargs='?'
        # )

        # neo_tabulam_numerae = parser.add_argument_group(
        #     "neo-tabulam-numerae",
        #     "Automated generation of numerical tables")

        # neo_tabulam_numerae.add_argument(
        #     '--actionem-tabulam-numerae',
        #     help='Define mode to numetical tables',
        #     metavar='',
        #     dest='neo_tabulam_numerae',
        #     const=True,
        #     nargs='?'
        # )

        # neo_tabulam_numerae.add_argument(
        #     '--tabulam-numerae-initiale',
        #     help='Start number (default: 0)',
        #     metavar='',
        #     dest='tabulam_numerae_initiale',
        #     default="0",
        #     type=int,
        #     nargs='?'
        # )
        # neo_tabulam_numerae.add_argument(
        #     '--tabulam-numerae-finale',
        #     help='Final number  (default: 9)',
        #     metavar='',
        #     dest='tabulam_numerae_finale',
        #     default="9",
        #     type=int,
        #     nargs='?'
        # )
        # neo_tabulam_numerae.add_argument(
        #     '--tabulam-numerae-gradus',
        #     help='Step between numbers  (default: 1)',
        #     metavar='',
        #     dest='tabulam_numerae_gradus',
        #     default="1",
        #     type=int,
        #     nargs='?'
        # )

        # neo_scripturam = parser.add_argument_group(
        #     "neo-scripturam",
        #     "(internal use) Operations related to associate new symbols " +
        #     "to entire new writing systems without users needing to " +
        #     "pre-translate to existing tables.")

        # neo_scripturam.add_argument(
        #     '--actionem-neo-scripturam',
        #     help='(required) Define mode actionem-neo-scripturam',
        #     metavar='',
        #     dest='neo_scripturam',
        #     const=True,
        #     nargs='?'
        # )

        # # cifram, https://translate.google.com/?sl=la&tl=en&text=cifram&op=translate
        # decifram = parser.add_argument_group(
        #     "decifram",
        #     "Decipher (e.g. the act of decode numeric codes)")

        # decifram.add_argument(
        #     '--actionem-decifram',
        #     help='(required) Define mode decifram',
        #     metavar='',
        #     dest='actionem_decifram',
        #     const=True,
        #     nargs='?'
        # )
        # decifram = parser.add_argument_group(
        #     "cifram",
        #     "Cifram (e.g. the act of encode first column of data on B60)")

        # decifram.add_argument(
        #     '--actionem-cifram',
        #     help='(required) Define mode decifram',
        #     metavar='',
        #     dest='actionem_cifram',
        #     const=True,
        #     nargs='?'
        # )

        # # https://stackoverflow.com/questions/59661738/argument-dependency-in-argparse
        # # Scriptura cuneiformis
        # # https://en.wikipedia.org/wiki/Cuneiform#Decipherment
        # # https://la.wikipedia.org/wiki/Scriptura_cuneiformis
        # neo_scripturam.add_argument(
        #     '--neo-scripturam-tabulae-symbola',
        #     help='(internal use) Inject reference table. ' +
        #     'This requires entire list of the used base system ' +
        #     ' (e.g. 60 items for base64 items.' +
        #     'First character determine the spliter. ' +
        #     'Example 1: ",0,1,(.....),8,9,"',
        #     metavar='neo_scripturam_tabulae',
        #     dest='neo_scripturam_tabulae',
        #     # default="2",
        #     nargs='?'
        # )

        # neo_scripturam.add_argument(
        #     '--neo-scripturam-tabulae-hxl-nomini',
        #     help='(internal use) Inject reference table. ' +
        #     'An HXL Standard tag name.' +
        #     'Default: #item+rem+i_mul+is_zsym+ix_ndt60+ix_neo',
        #     dest='neo_scripturam_nomini',
        #     default="#item+rem+i_mul+is_zsym+ix_ndt60+ix_neo",
        #     nargs='?'
        # )

        # neo_scripturam.add_argument(
        #     '--neo-scripturam-tabulae-hxl-selectum',
        #     help='(internal use) Inject reference table. ' +
        #     'When exporting, define some pattern tags must have' +
        #     'Example: ix_neo',
        #     dest='neo_scripturam_hxl_selectum',
        #     default=None,
        #     nargs='?'
        # )

        parser.add_argument(
            '--verbose',
            help='Verbose output',
            metavar='verbose',
            nargs='?'
        )
        if hxl_output:
            parser.add_argument(
                'outfile',
                help='File to write (if omitted, use standard output).',
                nargs='?'
            )

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

        # if args.codex_verbum_tabulae:
        #     cs1603_3_12.est_codex_verbum_tabulae(args.codex_verbum_tabulae)

        # if args.neo_scripturam_tabulae:
        #     cs1603_3_12.est_neo_scripturam_tabulae(
        #         args.neo_scripturam_tabulae, args.neo_scripturam_nomini)

# printf "abc\tABC\nefg\tEFG\n" | ./999999999/0/2600.py --actionem-cifram
# cat 999999/1603/47/639/3/1603.47.639.3.tab | head | tail -n 4 | ./999999999/0/2600.py --actionem-cifram
        # if self.pyargs.actionem_cifram:

        #     if stdin.isatty():
        #         print("ERROR. Please pipe data in. \nExample:\n"
        #               "  cat data.tsv | {0} --actionem-cifram\n"
        #               "  printf \"abc\\nefg\\n\" | {0} --actionem-cifram"
        #               "".format(__file__))
        #         return self.EXIT_ERROR

        #     for line in sys.stdin:
        #         codicem = line.replace('\n', ' ').replace('\r', '')
        #         neo_lineam = cs1603_3_12.cifram_lineam(codicem)
        #         sys.stdout.writelines("{0}\n".format(neo_lineam))
        #     return self.EXIT_OK

        # if self.pyargs.actionem_decifram:

        #     if stdin.isatty():
        #         print("ERROR. Please pipe data in. \nExample:\n"
        #               "  cat data.txt | {0} --actionem-decifram\n"
        #               "  printf \"1234\\n5678\\n\" | {0} --actionem-decifram"
        #               "".format(__file__))
        #         return self.EXIT_ERROR

        #     for line in sys.stdin:
        #         codicem = line.replace('\n', ' ').replace('\r', '')
        #         fontem = cs1603_3_12.decifram_codicem_numerae(codicem)
        #         sys.stdout.writelines(
        #             "{0}{1}{2}\n".format(
        #                 codicem, args.resultatum_separato, fontem)
        #         )
        #     return self.EXIT_OK

        if self.pyargs.actionem_sparql:
            systema_numerali = cs1603_3_12.exportatum_sparql(
                # self.pyargs.tabulam_numerae_initiale,
                # self.pyargs.tabulam_numerae_finale,
                # self.pyargs.tabulam_numerae_gradus
            )
            tabulam_numerae = ['TODO']
            # return self.output(tabulam_numerae)
            return self.output(systema_numerali)

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

# if not sys.stdin.isatty():
#     print ("not sys.stdin.isatty")
# else:
#     print ("is  sys.stdin.isatty")

# import fcntl
# import os
# import sys

# # make stdin a non-blocking file
# fd = sys.stdin.fileno()
# fl = fcntl.fcntl(fd, fcntl.F_GETFL)
# fcntl.fcntl(fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)

# try:
#     print(sys.stdin.read())
# except:
#     print('No input')

# from sys import stdin
# from os import isatty

# is_pipe = not isatty(stdin.fileno())

# print('is_pipe', is_pipe)


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
