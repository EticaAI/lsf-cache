#!/usr/bin/env python3
# ==============================================================================
#
#          FILE:  2600.60.py
#
#         USAGE:  ./999999999/0/2600.60.py
#                 NUMERORDINATIO_BASIM="/dir/ndata" ./999999999/0/2600.60.py
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
#       CREATED:  2022-01-08 04:37 UTC
#      REVISION:  ---
# ==============================================================================

# TL;DR:
#   ./999999999/0/2600.60.py
#   NUMERORDINATIO_BASIM="/external/ndata" ./999999999/0/2600.60.py

import os
import sys
import argparse
# from pathlib import Path
from typing import (
    # Type,
    Union
)
import csv

NUMERORDINATIO_BASIM = os.getenv('NUMERORDINATIO_BASIM', os.getcwd())
NUMERORDINATIO_DEFALLO = int(os.getenv('NUMERORDINATIO_DEFALLO', '60'))  # <?>
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


class NDT2600:
    def __init__(self):
        self.D1613_2_60 = self._init_1613_2_60_datum()
        self.total_namespace_multiple_of_60 = 1
        self.codex_verbum_tabulae = []

    def _init_1613_2_60_datum(self):
        archivum = NUMERORDINATIO_BASIM + "/1613/1603.2.60.no1.tm.hxl.tsv"
        datum = {}
        with open(archivum) as file:
            tsv_file = csv.DictReader(file, delimiter="\t")
            # return list(tsv_file)
            for conceptum in tsv_file:
                int_clavem = int(conceptum['#item+conceptum+numerordinatio'])
                datum[int_clavem] = {}
                for clavem, rem in conceptum.items():
                    if not clavem.startswith('#item+conceptum+numerordinatio'):
                        datum[int_clavem][clavem] = rem

        return datum

    def est_codex_verbum_tabulae(self, tabulae: Union[str, list]):
        if isinstance(tabulae, list):
            self.codex_verbum_tabulae = tabulae
        else:
            separator = tabulae[0]
            if tabulae.count(separator) < 2:
                raise ValueError(
                    "Separator [" + separator + "] of [" + str(tabulae) + "]? --help")
            crudum_tabulae = tabulae.split(separator)
            self.codex_verbum_tabulae = list(filter(None, crudum_tabulae))

    def _quod_crc_check(self, numerum):
        numerum_textum = str(numerum)
        crc = 0
        for pumctum in numerum_textum:
            crc = crc + int(pumctum)
        return str(crc)[-1]

    def _quod_numerordinatio_digitalem_punctum(self, punctum: str):
        # for conceptum in self.D1613_2_60:
        #     print('TODO')
        for clavem, rem in self.D1613_2_60.items():
            if punctum in rem.values():
                return clavem

        return NUMERORDINATIO_DEFALLO

    def quod_numerordinatio_digitalem(
            self, codicem: str = '', verbose: bool = False) -> str:
        # Some unicode code poits may have upper case, but most do not.
        codicem_minor = codicem.lower()
        digitalem_verus = 0
        ordo = 1
        for pumctum in reversed(codicem_minor):
            digitalem_punctum = self._quod_numerordinatio_digitalem_punctum(
                pumctum)
            digitalem_punctum_ordo = pow(digitalem_punctum, ordo)
            digitalem_verus = digitalem_verus + digitalem_punctum_ordo

            # print('pumctum', pumctum, digitalem_punctum,
            #       digitalem_punctum_ordo, digitalem_verus)

            ordo = ordo + 1

        resultatum = [
            str(digitalem_verus),
            str(ordo - 1),
            str(self.total_namespace_multiple_of_60),
            str(self._quod_crc_check(digitalem_verus))
        ]

        if verbose:
            return resultatum

        # print('todo')
        return ''.join(resultatum)


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
        parser.add_argument(
            '--codex-verbum-tabulae',
            help='Multiplication table of the code words. ' +
            'First character determine the splider. ' +
            'Example 1: " 0 1 2 3 4 5 6 7 8 9 a b c d e f ". '
            'Example 2: ",a,e,i,o,u,"',
            metavar='codex_verbum_tabulae',
            nargs='?'
        )
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

        ndt2600 = NDT2600()

        # ndt2600 = NDT2600()

        # print('self.pyargs', self.pyargs)

        if args.codex_verbum_tabulae:
            ndt2600.est_codex_verbum_tabulae(args.codex_verbum_tabulae)

        # print(ndt2600.__dict__)
        # Show help if no option defined
        # pyargs.print_help()
        return self.EXIT_OK


if __name__ == "__main__":

    cli_2600 = CLI_2600()
    args = cli_2600.make_args()
    # pyargs.print_help()

    # args.execute_cli(args)
    cli_2600.execute_cli(args)


# ndt2600 = NDT2600()

# # print(quod_1613_2_60_datum())
# # print(ndt2600)

# print('0')
# print(ndt2600.quod_numerordinatio_digitalem('0', True))
# print('05')
# print(ndt2600.quod_numerordinatio_digitalem('05', True))
# print('zz')
# print(ndt2600.quod_numerordinatio_digitalem('zz', True))
