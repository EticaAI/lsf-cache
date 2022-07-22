#!/usr/bin/env python3
# ==============================================================================
#
#          FILE:  rdf_ttl_canonization.py
#
#         USAGE:  ./999999999/0/rdf_ttl_canonization.py
#                 ./999999999/0/rdf_ttl_canonization.py --help
#
#   DESCRIPTION:  RUN /999999999/0/rdf_ttl_canonization.py --help
#
#       OPTIONS:  ---
#
#  REQUIREMENTS:  - python3
#                 - pip install rdflib
#                   - pip3 install 'rdflib>=6.0.0'
#                     (initially tested with 6.1.1)
#          BUGS:  ---
#         NOTES:  ---
#       AUTHORS:  Emerson Rocha <rocha[at]ieee.org>
# COLLABORATORS:  ---
#       COMPANY:  EticaAI
#       LICENSE:  Public Domain dedication or Zero-Clause BSD
#                 SPDX-License-Identifier: Unlicense OR 0BSD
#       VERSION:  v1.0.0
#       CREATED:  2022-07-22 01:03 UTC based on999999999_10263485.py
#      REVISION:  ---
# ==============================================================================

import sys
import argparse

from pathlib import Path
# from typing import (
#     Any,
#     # Dict,
#     # List,
# )

from rdflib.graph import Graph

# head -n 22 999999/0/teste-4~full.ttl > 999999/0/teste-4~full+head22.ttl
# rdfpipe --input-format=turtle --output-format=turtle 999999/0/teste-4~full+head22.ttl > 999999/0/teste-4~full+head22+formated.ttl
# head -n 22 999999/0/teste-4~full.ttl | rdfpipe --input-format=turtle --output-format=turtle -

STDIN = sys.stdin.buffer

NOMEN = 'rdf_ttl_canonization'

DESCRIPTION = """
{0} RDF/Turtle file formating. Conventions used by Lexicographī sine fīnibus

@see - https://github.com/EticaAI/lexicographi-sine-finibus/issues/46
""".format(__file__)

__EPILOGUM__ = """
------------------------------------------------------------------------------
                            EXEMPLŌRUM GRATIĀ
------------------------------------------------------------------------------
(NOTICE: consider just installing 
    pip3 install 'rdflib>=6.0.0'
Instead of using {0}. For now no need to re-impkement all features)

    {0} 999999/0/teste-4~full.ttl
    head -n 20 999999/0/teste-4~full.ttl | {0}

Using RDFlib cli tools . . . . . . . . . . . . . . . . . . . . . . . . . . . .

    rdfpipe --input-format=turtle --output-format=longturtle \
999999/0/teste-4~full.ttl > 999999/0/teste-4~full~pretty.ttl

Requires:
    pip3 install 'rdflib>=6.0.0'
------------------------------------------------------------------------------
                            EXEMPLŌRUM GRATIĀ
------------------------------------------------------------------------------
""".format(__file__)


SYSTEMA_SARCINAE = str(Path(__file__).parent.resolve())
PROGRAMMA_SARCINAE = str(Path().resolve())


class Cli:

    EXIT_OK = 0
    EXIT_ERROR = 1
    EXIT_SYNTAX = 2

    def __init__(self):
        """
        Constructs all the necessary attributes for the Cli object.
        """

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
                'formatae',
            ],
            # required=True
            default='formatae'
        )

        return parser.parse_args()

    def execute_cli(self, pyargs, stdin=STDIN, stdout=sys.stdout,
                    stderr=sys.stderr):
        # self.pyargs = pyargs

        _infile = None
        _stdin = None

        # configuratio = self._quod_configuratio(pyargs.archivum_configurationi)

        if stdin.isatty():
            _infile = pyargs.infile
        else:
            _stdin = stdin
            _infile = _stdin

        g = Graph()
        # g.parse(_stdin, format="turtle")
        g.parse(_infile, format="turtle")
        # print(g)
        print(g.serialize(format="longturtle"))

        # print('Unknow option.')
        return self.EXIT_ERROR


if __name__ == "__main__":

    est_cli = Cli()
    args = est_cli.make_args()

    est_cli.execute_cli(args)
