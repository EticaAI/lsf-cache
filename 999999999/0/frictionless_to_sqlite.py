#!/usr/bin/env python3
# ==============================================================================
#
#          FILE:  frictionless_to_sqlite.py
#
#         USAGE:  ./999999999/0/frictionless_to_sqlite.py
#                 ./999999999/0/frictionless_to_sqlite.py --help
#
#   DESCRIPTION:  ---
#
#       OPTIONS:  ---
#
#  REQUIREMENTS:  - python3
#                   - pip install frictionless[sql]
#          BUGS:  ---
#         NOTES:  ---
#       AUTHORS:  Emerson Rocha <rocha[at]ieee.org>
# COLLABORATORS:  ---
#
#       COMPANY:  EticaAI
#       LICENSE:  Public Domain dedication or Zero-Clause BSD
#                 SPDX-License-Identifier: Unlicense OR 0BSD
#       VERSION:  v1.0.0
#       CREATED:  2022-06-27 03:22 UTC created.
#      REVISION:  ---
# ==============================================================================

# @TODO maybe implement other exporters, by using pandas as intermediate
#       format. See pandas.pydata.org/docs/user_guide/io.html#stata-format

################################### PROTIP  ####################################
# if you ONLY need copy paste the core of this file, use this:
#    # @see framework.frictionlessdata.io/docs/tutorials/formats/sql-tutorial
#    from frictionless import Package
#
#    package = Package('datapackage.json')
#    package.to_sql('sqlite:///mdciii.sqlite')
################################### PROTIP  ####################################

# ./999999999/0/frictionless_to_sqlite.py --datapackage='datapackage.json' --sqlite='999999/0/mdciii.sqlite'

import argparse
import sys
from frictionless import Package

PROGRAM = "frictionless_to_sqlite"
DESCRIPTION = """
------------------------------------------------------------------------------
The {0} is a simpler wrapper to export frictionless to SQLite.

As 2022-06-27, no idea why they do not provide this by the community command
like version. This entire like actually have quite few lines of code.
------------------------------------------------------------------------------
""".format(__file__)

__EPILOGUM__ = """
------------------------------------------------------------------------------
                            EXEMPLŌRUM GRATIĀ
------------------------------------------------------------------------------
Quickstart . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
    {0} --datapackage='datapackage.json' --sqlite='999999/0/mdciii.sqlite'

Create the datapackage.json (requires other tool) . . . . . . . . . . . . . . .
(This command may be outdated eventually)
    ./999999999/0/1603_1.py --methodus='data-apothecae' \
--data-apothecae-ad-stdout --data-apothecae-formato='datapackage' \
--data-apothecae-ex-suffixis='no1.tm.hxl.csv' \
--data-apothecae-ex-praefixis='1603_16,!1603_1_1,!1603_1_51' \
> ./datapackage.json

(same, but now all tables under 1603. Migth run out of memory except one)
    ./999999999/0/1603_1.py --methodus='data-apothecae' \
--data-apothecae-ad-stdout --data-apothecae-formato='datapackage' \
--data-apothecae-ex-suffixis='no1.tm.hxl.csv' \
--data-apothecae-ex-praefixis='1603,!1603_45_46' \
> ./datapackage.json

# ex-praefixis='1603_16,1603_45_16,!1603_45_76,!1603_16_76,!1603_45_49'

(Use jq to print resources)
    jq .resources[].name < datapackage.json

------------------------------------------------------------------------------
                            EXEMPLŌRUM GRATIĀ
------------------------------------------------------------------------------
""".format(__file__)

STDIN = sys.stdin.buffer


def frictionless_to_sqlite(
        datapackage: str, sqlite_path: str = 'mdciii.sqlite'):
    """frictionless_to_sqlite

    Args:
        datapackage (str): datapackage package path
        sqlite_path (str, optional): The path. Defaults to 'mdciii.sqlite'.
    """
    package = Package(datapackage)
    package.to_sql(f'sqlite:///{sqlite_path}')


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
            '--sqlite',
            help='Relative path and extension to the sqlite database.'
            'Defaults to mdciii.sqlite on current directory',
            dest='sqlite',
            default='mdciii.sqlite',
            nargs='?'
        )
        return parser.parse_args()

    def execute_cli(
            self, pyargs, stdin=STDIN, stdout=sys.stdout,
            stderr=sys.stderr
    ):

        frictionless_to_sqlite(pyargs.datapackage, pyargs.sqlite)

        return self.EXIT_OK


if __name__ == "__main__":

    cli_2600 = CLI_2600()
    args = cli_2600.make_args()
    # pyargs.print_help()

    # args.execute_cli(args)
    cli_2600.execute_cli(args)
