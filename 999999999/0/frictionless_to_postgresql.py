#!/usr/bin/env python3
# ==============================================================================
#
#          FILE: frictionless_to_postgresql.py
#
#         USAGE:  ./999999999/0/frictionless_to_postgresql.py
#                 ./999999999/0/frictionless_to_postgresql.py --help
#
#   DESCRIPTION:  ---
#
#       OPTIONS:  ---
#
#  REQUIREMENTS:  - python3
#                   - pip install frictionless[excel]
#          BUGS:  ---
#         NOTES:  ---
#       AUTHORS:  Emerson Rocha <rocha[at]ieee.org>
# COLLABORATORS:  ---
#
#       COMPANY:  EticaAI
#       LICENSE:  Public Domain dedication or Zero-Clause BSD
#                 SPDX-License-Identifier: Unlicense OR 0BSD
#       VERSION:  v1.0.0
#       CREATED:  2022-06-27 04:43 UTC Created; Based on
#                                      frictionless_to_sqlite.py
#      REVISION:  ---
# ==============================================================================

import argparse
import sys
from frictionless import Package
from openpyxl import Workbook

PROGRAM = "frictionless_to_postgresql"
DESCRIPTION = """
------------------------------------------------------------------------------
The {0} is a simple wrapper for frictionless python library to save data
documented with datapackage.json to PostgreSQL

------------------------------------------------------------------------------
""".format(__file__)

__EPILOGUM__ = """
------------------------------------------------------------------------------
                            EXEMPLŌRUM GRATIĀ
------------------------------------------------------------------------------
Quickstart . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
    {0} --datapackage='datapackage.json' \
--postgresql='user:pass@localhost/mdciii'

Validate file with cli . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
(Use this if export does not work for some reason)
    frictionless validate datapackage.json

Create the datapackage.json (requires other tool) . . . . . . . . . . . . . . .
(This command may be outdated eventually)
    ./999999999/0/1603_1.py --methodus='data-apothecae' \
--data-apothecae-ad-stdout --data-apothecae-formato='datapackage' \
--data-apothecae-ex-suffixis='no1.tm.hxl.csv' \
--data-apothecae-ex-praefixis='1603_16,!1603_1_1,!1603_1_51' \
> ./datapackage.json

(same, but now all tables under 1603. Migth run out of memory) . . . . . . . . .
    ./999999999/0/1603_1.py --methodus='data-apothecae' \
--data-apothecae-ad-stdout --data-apothecae-formato='datapackage' \
--data-apothecae-ex-suffixis='no1.tm.hxl.csv' \
--data-apothecae-ex-praefixis='1603' \
> ./datapackage.json

(Use jq to print resources)
    jq .resources[].name < datapackage.json

------------------------------------------------------------------------------
                            EXEMPLŌRUM GRATIĀ
------------------------------------------------------------------------------
""".format(__file__)

STDIN = sys.stdin.buffer


def frictionless_to_postgresql(
        datapackage: str, postgresql_conn: str = 'localhost/mdciii'):
    """frictionless_to_sqlite

    Args:
        datapackage (str): datapackage package path
        postgresql_conn (str, optional): The path. Defaults to 'mdciii'.
    """
    package = Package(datapackage)
    package.to_sql('postgresql://{0}'.format(postgresql_conn))


class CLI_2600:
    def __init__(self):
        """
        Constructs all the necessary attributes for the Cli object.
        """
        self.pyargs = None
        self.EXIT_OK = 0
        self.EXIT_ERROR = 1
        self.EXIT_SYNTAX = 2

    def make_args(self, hxl_output=True):
        """make_args

        Args:
            hxl_output (bool, optional): _description_. Defaults to True.
        """
        parser = argparse.ArgumentParser(
            prog=PROGRAM,
            description=DESCRIPTION,
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog=__EPILOGUM__
        )

        parser.add_argument(
            '--datapackage',
            help='datapackage.json path. Must be at at root path, so can '
            'reference all the tables. Defaults to datapackage.json and'
            'current working directory',
            dest='datapackage',
            default='datapackage.json',
            nargs='?'
        )

        parser.add_argument(
            '--postgresql',
            help='PostgreSQL connection information. Defaults to '
            '"localhost/mdciii" without any special credentials',
            dest='postgresql_conn',
            default='localhost/mdciii',
            nargs='?'
        )
        return parser.parse_args()

    def execute_cli(
            self, pyargs, stdin=STDIN, stdout=sys.stdout,
            stderr=sys.stderr
    ):
        frictionless_to_postgresql(
            pyargs.datapackage, pyargs.postgresql_conn)

        # print('unknow option.')
        return self.EXIT_OK


if __name__ == "__main__":

    cli_2600 = CLI_2600()
    args = cli_2600.make_args()
    # pyargs.print_help()

    # args.execute_cli(args)
    cli_2600.execute_cli(args)
