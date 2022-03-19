#!/usr/bin/env python3
# ==============================================================================
#
#          FILE:  1603_3_4.py
#
#         USAGE:  ./999999999/0/1603_3_4.py
#                 ./999999999/0/1603_3_4.py --help
#                 NUMERORDINATIO_BASIM="/dir/ndata" ./999999999/0/1603_3_4.py
#
#   DESCRIPTION:  ---
#
#       OPTIONS:  ---
#
#  REQUIREMENTS:  - python3
#                   - pywikibot
#                   - wikitextparser
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
#    python3 -m doctest ./999999999/0/1603_3_4.py

# pwb --help
# python3 pwb.py generate_user_files
# pwb generate_user_files
# @see https://www.mediawiki.org/wiki/Manual:Pywikibot/upload.py
# @see https://www.mediawiki.org/wiki/Manual:Pywikibot/user-config.py/pt
# @see https://doc.wikimedia.org/pywikibot/stable/installation.html



### Example of initialization guide for uploader, start ________________________
# @see https://github.com/wikimedia/pywikibot
# @see https://doc.wikimedia.org/pywikibot/stable/installation.html
# pip3 install requests
# pip3 install wikitextparser
# git clone https://gerrit.wikimedia.org/r/pywikibot/core.git \
#   /workspace/git/EticaAI/pywikibot
# cd /workspace/git/EticaAI/pywikibot
# git submodule update --init
# python3 pwb.py generate_user_files
# > options (example)
#   1
#   commons
#   EmericusPetro
#   n
#   BotPassword's "bot name" for EmericusPetroBot: EmericusPetroBot@EmericusPet
#                                                                         roBot
#   BotPassword's "password" for "EmericusPetroBot@EmericusPetroBot " (no 
#                                                      characters will be shown)

# cd /workspace/git/EticaAI/pywikibot
# python3 pwb.py login
# python3 pwb.py upload /workspace/git/EticaAI/multilingual-lexicography-automation/officinam/1603/45/31/1603_45_31.mul-Latn.tab.json

# (...) Using this tutorial (without need to use pywikibot)
# https://www.mediawiki.org/wiki/API:Upload#Python
# (...)
# Test file
# https://raw.githubusercontent.com/EticaAI/n-data/main/1603/45/31/1603_45_31.mul-Latn.tab.json
# https://eticaai.github.io/n-data/1603/45/31/1603_45_31.mul-Latn.tab.json

# URL de teste
#    https://commons.wikimedia.org/wiki/Data:Sandbox/EmericusPetro/Example.tab
# URL (no commons)
#  https://commons.wikimedia.org/wiki/Special:ApiSandbox#action=upload&format=json&filename=File_1.jpg&file=file_contents_here&token=123Token&ignorewarnings=1
#
# https://commons.wikimedia.org/w/api.php?action=upload&format=json&filename=EmericusPetro%2FExample.tab&ignorewarnings=1&url=https%3A%2F%2Feticaai.github.io%2Fn-data%2F1603%2F45%2F31%2F1603_45_31.mul-Latn.tab.json&token=

### Example of initialization guide for uploader, end __________________________

import os
import sys
import argparse
# from pathlib import Path
from typing import (
    # Type,
    Union
)
from pathlib import Path

DESCRIPTION = """
1603_3_4.py is (...)
"""


STDIN = sys.stdin.buffer

_HOME = str(Path.home())


# $HOME/.config/pywikibot/user-config.py
os.environ['PYWIKIBOT_DIR'] = _HOME + '/.config/pywikibot/'

# PYWIKIBOT_DIR=/home/fititnt/.config/pywikibot pwb login

# https://commons.wikimedia.org/wiki/Data:Sandbox/EmericusPetro/Example.tab

import pywikibot
# site = pywikibot.Site('en', 'wikipedia')  # The site we want to run our bot on
# page = pywikibot.Page(site, 'Wikipedia:Sandbox')
site = pywikibot.Site('en', 'wikipedia')  # The site we want to run our bot on
page = pywikibot.Page(site, 'Wikipedia:Sandbox')
page.text = page.text.replace('foo', 'bar')
page.save('Replacing "foo" with "bar"')  # Saves the page

# via https://github.com/wikimedia/pywikibot
# 
# git clone https://gerrit.wikimedia.org/r/pywikibot/core.git /workspace/git/temp/pywikibot-core
# cd /workspace/git/temp/pywikibot-core
# git submodule update --init
# python3 pwb.py script_name
# python3 pwb.py login



# class CLI_2600:
#     def __init__(self):
#         """
#         Constructs all the necessary attributes for the Cli object.
#         """
#         self.pyargs = None
#         # self.args = self.make_args()
#         # Posix exit codes
#         self.EXIT_OK = 0
#         self.EXIT_ERROR = 1
#         self.EXIT_SYNTAX = 2

#     def make_args(self, hxl_output=True):
#         parser = argparse.ArgumentParser(description=DESCRIPTION)

#         # https://en.wikipedia.org/wiki/Code_word
#         # https://en.wikipedia.org/wiki/Coded_set

#         # cōdex verbum tabulae
#         # parser.add_argument(
#         #     '--actionem',
#         #     help='Action to execute. Defaults to codex.',
#         #     # choices=['rock', 'paper', 'scissors'],
#         #     choices=[
#         #         'codex',
#         #         'fontem-verbum-tabulae',
#         #         'neo-scripturam',
#         #     ],
#         #     dest='actionem',
#         #     required=True,
#         #     default='codex',
#         #     const='codex',
#         #     type=str,
#         #     nargs='?'
#         # )

#         parser.add_argument(
#             '--punctum-separato-de-resultatum',
#             help='Character(s) used as separator for generate output.' +
#             'Defaults to tab "\t"',
#             dest='resultatum_separato',
#             default="\t",
#             nargs='?'
#         )

#         neo_codex = parser.add_argument_group(
#             "sparql",
#             "(DEFAULT USE) SPARQL query")

#         neo_codex.add_argument(
#             '--actionem-sparql',
#             help='Define mode to operate with generation of SPARQL ' +
#             'queries',
#             metavar='',
#             dest='actionem_sparql',
#             const=True,
#             nargs='?'
#         )

#         neo_codex.add_argument(
#             '--query',
#             help='Generate SPARQL query',
#             metavar='',
#             dest='query',
#             const=True,
#             nargs='?'
#         )
#         neo_codex.add_argument(
#             '--wikidata-link',
#             help='Generate query.wikidata.org link (from piped in query)',
#             metavar='',
#             dest='wikidata_link',
#             const=True,
#             nargs='?'
#         )
#         neo_codex.add_argument(
#             '--csv',
#             help='Generate TSV output (from piped in query)',
#             metavar='',
#             dest='csv',
#             const=True,
#             nargs='?'
#         )

#         neo_codex.add_argument(
#             '--tsv',
#             help='Generate TSV output (from piped in query)',
#             metavar='',
#             dest='tsv',
#             const=True,
#             nargs='?'
#         )

#         neo_codex.add_argument(
#             '--hxltm',
#             help='Generate HXL-tagged output (from piped in query). ' +
#             'Concepts use #item+conceptum+codicem instead ' +
#             'of #item+code+v_wiki_q',
#             metavar='',
#             dest='hxltm',
#             const=True,
#             nargs='?'
#         )

#         # linguae, f, pl, (Nominative) https://en.wiktionary.org/wiki/lingua
#         # pāginārum, f, pl, (Gengitive) https://en.wiktionary.org/wiki/pagina
#         # dīvīsiōnibus, f, pl, (Dative) https://en.wiktionary.org/wiki/divisio
#         # līmitibus, m, pl, (Dative) https://en.wiktionary.org/wiki/limes#Latin
#         # //linguae pāginārum līmitibus//

#         # lingua, f, s, (Nominative) https://en.wiktionary.org/wiki/lingua#Latin
#         # pāginae, f, s, (Dative) https://en.wiktionary.org/wiki/lingua#Latin
#         # dīvīsiōnī, f, s, (Dative) https://en.wiktionary.org/wiki/lingua#Latin
#         neo_codex.add_argument(
#             '--lingua-divisioni',
#             help='For the languages on [1603:1:51], how many divisions ' +
#             '(or number of chunks) should be done. 1 means no division.' +
#             'If using more than 1, use --lingua-paginae do paginate the ' +
#             'Options. Default: 1',
#             dest='lingua_divisioni',
#             metavar='',
#             default="1",
#             nargs='?'
#         )

#         neo_codex.add_argument(
#             '--lingua-paginae',
#             help='If --lingua-divisioni different from 1, defines which page '
#             'of languages to return. Default 1.',
#             dest='lingua_paginae',
#             metavar='',
#             default="1",
#             nargs='?'
#         )

#         parser.add_argument(
#             '--verbose',
#             help='Verbose output',
#             metavar='verbose',
#             nargs='?'
#         )
#         if hxl_output:
#             parser.add_argument(
#                 'outfile',
#                 help='File to write (if omitted, use standard output).',
#                 nargs='?'
#             )

#         # print('oioioi', parser)
#         return parser.parse_args()

#     # def execute_cli(self, args, stdin=STDIN, stdout=sys.stdout,
#     #                 stderr=sys.stderr):
#     def execute_cli(self, pyargs, stdin=STDIN, stdout=sys.stdout,
#                     stderr=sys.stderr):
#         # print('TODO')

#         self.pyargs = pyargs

#         # cs1603_3_12 = cs1603_3_12()
#         cs1603_3_12 = CS1603z3z12()

#         # cs1603_3_12 = cs1603_3_12()

#         # print('self.pyargs', self.pyargs)

#         # cs1603_3_12.est_verbum_limiti(args.verbum_limiti)
#         cs1603_3_12.est_resultatum_separato(args.resultatum_separato)
#         cs1603_3_12.est_lingua_divisioni(args.lingua_divisioni)
#         cs1603_3_12.est_lingua_paginae(
#             args.lingua_paginae)

#         if self.pyargs.actionem_sparql:
#             # print('oi')

#             if self.pyargs.query:
#                 if stdin.isatty():
#                     print("ERROR. Please pipe data in. \nExample:\n"
#                           "  cat data.txt | {0} --actionem-quod-sparql\n"
#                           "  printf \"Q1065\\nQ82151\\n\" | {0} --actionem-quod-sparql"
#                           "".format(__file__))
#                     return self.EXIT_ERROR

#                 for line in sys.stdin:
#                     codicem = line.replace('\n', ' ').replace('\r', '')
#                     # TODO: deal with cases were have more than Qcode
#                     cs1603_3_12.est_wikidata_q(codicem)

#                 quod_query = cs1603_3_12.exportatum_sparql()
#                 # tabulam_numerae = ['TODO']
#                 # return self.output(tabulam_numerae)
#                 return self.output(quod_query)

#             if self.pyargs.wikidata_link:
#                 if stdin.isatty():
#                     print("ERROR. Please pipe data in. \nExample:\n"
#                           "  cat data.txt | {0} --actionem-sparql --query | {0} --actionem-sparql --wikidata-link\n"
#                           "  printf \"Q1065\\nQ82151\\n\" | {0} --actionem-sparql --query | {0} --actionem-sparql --wikidata-link"
#                           "".format(__file__))
#                     return self.EXIT_ERROR

#                 full_query = []
#                 for line in sys.stdin:
#                     full_query.append(line)

#                 wikidata_backend = "https://query.wikidata.org/#"
#                 quod_query = wikidata_backend + \
#                     urllib.parse.quote("".join(full_query).encode('utf8'))

#                 print(quod_query)
#                 return self.EXIT_OK

#             if self.pyargs.tsv or self.pyargs.csv:
#                 if stdin.isatty():
#                     print("ERROR. Please pipe data in. \nExample:\n"
#                           "  cat data.txt | {0} --actionem-sparql --query | {0} --actionem-sparql --tsv\n"
#                           "  printf \"Q1065\\nQ82151\\n\" | {0} --actionem-sparql --query | {0} --actionem-sparql --tsv"
#                           "".format(__file__))
#                     return self.EXIT_ERROR

#                 full_query = []
#                 for line in sys.stdin:
#                     full_query.append(line)

#                 sparql_backend = "https://query.wikidata.org/sparql"
#                 # sparql_backend = "http://localhost:1234/"
#                 # @see https://stackoverflow.com/questions/10588644

#                 # https://www.mediawiki.org/wiki/Wikidata_Query_Service/User_Manual/en#Supported_formats

#                 if self.pyargs.tsv:
#                     separator = "\t"
#                     headers = {'Accept': 'text/tab-separated-values'}
#                 if self.pyargs.csv:
#                     separator = ","
#                     headers = {'Accept': 'text/csv'}
#                 if self.pyargs.hxltm:
#                     # headers = {'Accept': 'text/tab-separated-values'}
#                     headers = {'Accept': 'text/csv'}

#                 # TODO: make it configurable via command line
#                 headers['User-Agent'] = USER_AGENT
#                 headers['Api-User-Agent'] = USER_AGENT

#                 payload_query = "".join(full_query)
#                 # Lets put an sleep, 3 seconds, just in case
#                 sleep(3)
#                 r = requests.post(sparql_backend, headers=headers, data={
#                     'query': payload_query
#                 })

#                 # @TODO: --tsv --hxltm is know to be bugged (not sure if
#                 #        Wikidata result already skip values)

#                 if self.pyargs.hxltm:
#                     result_string = r.text.strip()

#                     # @TODO: this likely to break with fields with newlines.
#                     #        however no testing sample exists at the moment.
#                     #        Eventually needs be checked.
#                     lines = result_string.splitlines()
#                     # caput = hxltm_hastag_de_csvhxlated(next(iter(lines)).split(","))
#                     caput_crudum = lines.pop(0)
#                     # print('caput_crudum', caput_crudum)
#                     caput = hxltm_hastag_de_csvhxlated(caput_crudum.split(','))
#                     print(separator.join(caput))
#                     print("\n".join(lines))

#                     # reader = csv.reader(lines, delimiter="\t")
#                     # caput = hxltm_hastag_de_csvhxlated(next(reader))
#                     # print(separator.join(caput))
#                     # for row in reader:
#                     #     print(separator.join(row))
#                 else:
#                     print(r.text.strip())

#                 # TODO: generate explicit error messages and return code
#                 # print(r.content)
#                 return self.EXIT_OK

#         # if self.pyargs.verbum_simplex:
#         #     tabulam_multiplicatio = cs1603_3_12.quod_tabulam_multiplicatio()
#         #     return self.output(tabulam_multiplicatio)

#         # if self.pyargs.codex_completum:
#         #     tabulam_multiplicatio = cs1603_3_12.quod_codex()
#         #     return self.output(tabulam_multiplicatio)

#         # if self.pyargs.neo_scripturam:
#         #     scientia = cs1603_3_12.exportatum_scientia_de_scriptura(
#         #         args.neo_scripturam_hxl_selectum)
#         #     return self.output(scientia)

#         # Let's default to full table
#         # tabulam_multiplicatio = cs1603_3_12.quod_codex()
#         # return self.output(tabulam_multiplicatio)
#         print('unknow option.')
#         return self.EXIT_ERROR

#     def output(self, output_collectiom):
#         for item in output_collectiom:
#             # TODO: check if result is a file instead of print

#             # print(type(item))
#             if isinstance(item, int) or isinstance(item, str):
#                 print(item)
#             else:
#                 print(self.pyargs.resultatum_separato.join(item))

#         return self.EXIT_OK

# # if not sys.stdin.isatty():
# #     print ("not sys.stdin.isatty")
# # else:
# #     print ("is  sys.stdin.isatty")

# # import fcntl
# # import os
# # import sys

# # # make stdin a non-blocking file
# # fd = sys.stdin.fileno()
# # fl = fcntl.fcntl(fd, fcntl.F_GETFL)
# # fcntl.fcntl(fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)

# # try:
# #     print(sys.stdin.read())
# # except:
# #     print('No input')

# # from sys import stdin
# # from os import isatty

# # is_pipe = not isatty(stdin.fileno())

# # print('is_pipe', is_pipe)


# if __name__ == "__main__":

#     cli_2600 = CLI_2600()
#     args = cli_2600.make_args()
#     # pyargs.print_help()

#     # args.execute_cli(args)
#     cli_2600.execute_cli(args)
