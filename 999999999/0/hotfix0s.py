#!/usr/bin/env python3
# ==============================================================================
#
#          FILE:  hotfix0s.py
#
#         USAGE:  ./999999999/0/hotfix0s.py
#                 ./999999999/0/hotfix0s.py --help
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
#       VERSION:  v1.0.0
#       CREATED:  2022-04-19 21:46 UTC
#      REVISION:  ---
# ==============================================================================

import sys
import argparse
import csv
import re

STDIN = sys.stdin.buffer

DESCRIPTION = """
{0} is a hotfix for some weird formating.
@see https://github.com/EticaAI/multilingual-lexicography/issues/30
""".format(__file__)

LIKELY_NUMERIC = [
    '#item+conceptum+codicem',
    '#status+conceptum',
    '#item+rem+i_qcc+is_zxxx+ix_n1603',
    '#item+rem+i_qcc+is_zxxx+ix_iso5218',
]

# ./999999999/0/hotfix0s.py 999999/0/1603_1_1--old.csv 999999/0/1603_1_1--new.csv


class HotfixCSV:
    """Remove .0 at the end of CSVs from data exported from XLSX and likely
    to have numeric values (and trigger weird bugs)
    """

    def __init__(self, infile, outfile):
        """
        Constructs all the necessary attributes for the Cli object.
        """
        self.infile = infile
        self.outfile = outfile
        self.header = []
        self.header_index_fix = []

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

    def execute(self):
        with open(self.infile, newline='') as infilecsv:
            with open(self.outfile, 'w', newline='') as outfilecsv:
                spamreader = csv.reader(infilecsv)
                spamwriter = csv.writer(outfilecsv)
                for row in spamreader:
                    # spamwriter.writerow(row)
                    spamwriter.writerow(self.process_row(row))
                    # self.data.append(row)


class CLIHotfix0s:
    def __init__(self):
        """
        Constructs all the necessary attributes for the Cli object.
        """

    def make_args(self, hxl_output=True):
        parser = argparse.ArgumentParser(description=DESCRIPTION)

        parser.add_argument(
            'infile',
            help='Input file',
            nargs='?'
        )
        parser.add_argument(
            'outfile',
            help='Output file',
            nargs='?'
        )

        return parser.parse_args()

    def execute_cli(self, pyargs, stdin=STDIN, stdout=sys.stdout,
                    stderr=sys.stderr):
        self.pyargs = pyargs

        hf = HotfixCSV(self.pyargs.infile, self.pyargs.outfile)
        hf.execute()

    # def output(self, output_collectiom):
    #     for item in output_collectiom:
    #         print(item)

    #     return self.EXIT_OK


if __name__ == "__main__":

    cli_2600 = CLIHotfix0s()
    args = cli_2600.make_args()

    cli_2600.execute_cli(args)
