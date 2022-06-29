#!/usr/bin/env python3
# ==============================================================================
#
#          FILE:  frictionless_to_excel.py
#
#         USAGE:  ./999999999/0/frictionless_to_excel.py
#                 ./999999999/0/frictionless_to_excel.py --help
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

PROGRAM = "frictionless_to_excel"
DESCRIPTION = """
------------------------------------------------------------------------------
The {0} is a simpler wrapper to export frictionless mapped data to Excel.
After 1,048,576 rows it get even faster!

------------------------------------------------------------------------------
""".format(__file__)

__EPILOGUM__ = """
------------------------------------------------------------------------------
                            EXEMPLŌRUM GRATIĀ
------------------------------------------------------------------------------
Quickstart . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
    {0} --datapackage='datapackage.json' --excel='999999/0/mdciii.xlsx'

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


def frictionless_to_excel(
        datapackage: str, excel_path: str = 'mdciii.xlsx'):
    """frictionless_to_excel

    Requires:
        pip install frictionless[excel]

    Args:
        datapackage (str): _description_
        sqlite_path (str, optional): _description_. Defaults to 'mdciii.sqlite'.
    """
    # from frictionless.plugins.excel import ExcelDialect
    # from frictionless import Resource

    supported_types = [
        "boolean",
        "date",
        "datetime",
        "integer",
        "number",
        "string",
        "time",
        "year",
    ]

    package = Package(datapackage)

    # Without write_only=True, a >450 table (XLSX 18MB) would take
    # > 1.900MB of RAM. But with write_only=True takes around in order of
    # ~10 MB of ram
    wb = Workbook(write_only=True)

    # for resource in list(package.resource_names()):
    for item in package.resources:
        resource = package.get_resource(item.name)
        # print(resource)
        # resource.write(excel_path, dialect=ExcelDialect(sheet=item.name))
        wb_new = wb.create_sheet(title=item.name)

        with resource:
            for row in resource.row_stream:
                cells = []
                if row.row_number == 1:
                    wb_new.append(row.field_names)
                cells = row.to_list(types=supported_types)
                wb_new.append(cells)

    wb.save(filename=excel_path)


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
            '--excel',
            help='Relative path and extension to the excel file.'
            'Defaults to mdciii.xlsx on current directory',
            dest='excel',
            default='mdciii.xlsx',
            nargs='?'
        )
        return parser.parse_args()

    def execute_cli(
            self, pyargs, stdin=STDIN, stdout=sys.stdout,
            stderr=sys.stderr
    ):
        frictionless_to_excel(pyargs.datapackage, pyargs.excel)

        # print('unknow option.')
        return self.EXIT_OK


if __name__ == "__main__":

    cli_2600 = CLI_2600()
    args = cli_2600.make_args()
    # pyargs.print_help()

    # args.execute_cli(args)
    cli_2600.execute_cli(args)
