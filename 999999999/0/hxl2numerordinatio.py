#!/usr/bin/env python3
# ==============================================================================
#
#          FILE:  hxl2numerordinatio.py
#
#         USAGE:  hxl2numerordinatio.py hxlated-data.hxl my-exported-file.example
#                 cat hxlated-data.hxl | hxl2numerordinatio.py > my-exported-file.example
#                 # Via web, in two different terminals, do it
#                     hug -f bin/hxl2numerordinatio.py
#                     ngrok http 8000
#
#   DESCRIPTION:  hxl2numerordinatio.py is an example script to create other scripts with
#                 some bare minimum command line interface that could work.
#                 With exception of external libraries, the hxl2numerordinatio.py is
#                 meant to be somewhat self-contained one-file executable ready
#                 to just be added to the path.
#
#                 Hug API can be used to create an ad-hoc web interface to your
#                 script. This can be both useful if you are using an software
#                 that accepts an URL as data source and you don't want to use
#                 this script to save a file locally.
#
#       OPTIONS:  ---
#
#  REQUIREMENTS:  - python3
#                     - libhxl (@see https://pypi.org/project/libhxl/)
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
#       CREATED:  2022-01-04 03:38 UTC based on hxl2example
#      REVISION:  ---
# ==============================================================================

# ./999999999/0/hxl2numerordinatio.py

import sys
import os
import logging
import argparse

# @see https://github.com/HXLStandard/libhxl-python
#    pip3 install libhxl --upgrade
# Do not import hxl, to avoid circular imports
import hxl.converters
import hxl.filters
import hxl.io

import csv
import tempfile

# # @see https://github.com/hugapi/hug
# #     pip3 install hug --upgrade
# import hug

# In Python2, sys.stdin is a byte stream; in Python3, it's a text stream
STDIN = sys.stdin.buffer


class HXL2Example:
    """
    HXL2Example is a classe to export already HXLated data in the format
    example.
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for the HXL2Example object.
        """
        self.hxlhelper = None
        self.args = None

        # Posix exit codes
        self.EXIT_OK = 0
        self.EXIT_ERROR = 1
        self.EXIT_SYNTAX = 2

        self.original_outfile = None
        self.original_outfile_is_stdout = True

        self.conceptum_hxl = ''
        self.conceptum_caput_index = 0

    def make_args_hxl2example(self):

        self.hxlhelper = HXLUtils()
        parser = self.hxlhelper.make_args(
            description=("hxl2example is an example script to create other "
                         "scripts with some bare minimum command line "
                         "interfaces that could work to export HXL files to "
                         "other formats."))

        parser.add_argument(
            '--conceptum-hxl',
            help='The HXL tag with the numeric code',
            # metavar='number',
            # type=int,
            default=None,
            nargs='?'
        )

        self.args = parser.parse_args()
        return self.args

    def execute_cli(self, args, stdin=STDIN, stdout=sys.stdout,
                    stderr=sys.stderr, hxlmeta=False):
        """
        The execute_cli is the main entrypoint of HXL2Tab when used via command
        line interface.
        """
        # hxltabconverter = HXLTabConverter()

        self.conceptum_hxl = args.conceptum_hxl

        # print('args', args)
        # print('self.conceptum_hxlself.conceptum_hxl 0', self.conceptum_hxl)

        # print(hxltabconverter.ORANGE_REFERENCE)
        # print(hxltabconverter.HXL_REFERENCE)

        # If the user specified an output file, we will save on
        # self.original_outfile. The args.outfile will be used for temporary
        # output
        if args.outfile:
            self.original_outfile = args.outfile
            self.original_outfile_is_stdout = False

        try:
            temp = tempfile.NamedTemporaryFile()
            args.outfile = temp.name

            with self.hxlhelper.make_source(args, stdin) as source, \
                    self.hxlhelper.make_output(args, stdout) as output:
                hxl.io.write_hxl(output.output, source,
                                 show_tags=not args.strip_tags)

            # if args.hxlmeta:
            #     print('TODO: hxlmeta')
            #     # print('output.output', output.output)
            #     # print('source', source)
            #     # # print('source.columns', source.headers())
            #     # hxlmeta = HXLMeta(local_hxl_file=output.output.name)
            #     # hxlmeta.debuginfo()
            # else:
            #     self.execute_numerordinatio(args.outfile, self.original_outfile,
            #                  self.original_outfile_is_stdout)
            self.execute_numerordinatio(args.outfile, self.original_outfile,
                                        self.original_outfile_is_stdout)

        finally:
            temp.close()

        return self.EXIT_OK

    def execute_numerordinatio(self, hxlated_input, tab_output, is_stdout):
        """
        hxl2tab is  is the main method to de facto make the conversion.
        """

        # print('self.conceptum_hxlself.conceptum_hxl 1', self.conceptum_hxl)

        with open(hxlated_input, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            # Hotfix: skip first non-HXL header. Ideally I think the already
            # exported HXlated file should already save without headers.
            next(csv_reader)
            header_original = next(csv_reader)
            # header_new = self.caput_index(header_original)
            caput_index_num = self.caput_index(header_original)
            # print('caput_index_num', caput_index_num)

            if is_stdout:
                txt_writer = csv.writer(sys.stdout, delimiter='\t')
                # txt_writer.writerow(header_new)
                txt_writer.writerow(header_original)
                for line in csv_reader:
                    txt_writer.writerow(line)
            else:

                tab_output_cleanup = open(tab_output, 'w')
                tab_output_cleanup.truncate()
                tab_output_cleanup.close()

                with open(tab_output, 'a') as new_txt:
                    txt_writer = csv.writer(new_txt, delimiter='\t')
                    # txt_writer.writerow(header_new)
                    txt_writer.writerow(header_original)
                    for line in csv_reader:
                        txt_writer.writerow(line)

    def caput_index(self, hxlated_header):
        """
        Detect the _de facto_ numeric index
        """

        if self.conceptum_hxl:
            # print('testando...')
            neo_index = hxlated_header.index(self.conceptum_hxl)
            return neo_index

        # Potential error; we will assume first column have numeric code
        return self.conceptum_caput_index


class HXLUtils:
    """
    HXLUtils contains functions from the Console scripts of libhxl-python
    (HXLStandard/libhxl-python/blob/master/hxl/scripts.py) with few changes
    to be used as class (and have one single place to change).
    Last update on this class was 2021-01-25.

    Author: David Megginson
    License: Public Domain
    """

    def __init__(self):

        self.logger = logging.getLogger(__name__)

        # Posix exit codes
        self.EXIT_OK = 0
        self.EXIT_ERROR = 1
        self.EXIT_SYNTAX = 2

    def make_args(self, description, hxl_output=True):
        """Set up parser with default arguments.
        @param description: usage description to show
        @param hxl_output: if True (default), include options for HXL output.
        @returns: an argument parser, partly set up.
        """
        parser = argparse.ArgumentParser(description=description)
        parser.add_argument(
            'infile',
            help='HXL file to read (if omitted, use standard input).',
            nargs='?'
        )
        if hxl_output:
            parser.add_argument(
                'outfile',
                help='HXL file to write (if omitted, use standard output).',
                nargs='?'
            )
        parser.add_argument(
            '--sheet',
            help='Select sheet from a workbook (1 is first sheet)',
            metavar='number',
            type=int,
            nargs='?'
        )
        parser.add_argument(
            '--selector',
            help='JSONPath expression for starting point in JSON input',
            metavar='path',
            nargs='?'
        )
        parser.add_argument(
            '--http-header',
            help='Custom HTTP header to send with request',
            metavar='header',
            action='append'
        )
        if hxl_output:
            parser.add_argument(
                '--remove-headers',
                help='Strip text headers from the CSV output',
                action='store_const',
                const=True,
                default=False
            )
            parser.add_argument(
                '--strip-tags',
                help='Strip HXL tags from the CSV output',
                action='store_const',
                const=True,
                default=False
            )
        parser.add_argument(
            "--ignore-certs",
            help="Don't verify SSL connections (useful for self-signed)",
            action='store_const',
            const=True,
            default=False
        )
        parser.add_argument(
            '--log',
            help='Set minimum logging level',
            metavar='debug|info|warning|error|critical|none',
            choices=['debug', 'info', 'warning', 'error', 'critical'],
            default='error'
        )
        return parser

    def add_queries_arg(
        self,
        parser,
        help='Apply only to rows matching at least one query.'
    ):
        parser.add_argument(
            '-q',
            '--query',
            help=help,
            metavar='<tagspec><op><value>',
            action='append'
        )
        return parser

    def do_common_args(self, args):
        """Process standard args"""
        logging.basicConfig(
            format='%(levelname)s (%(name)s): %(message)s',
            level=args.log.upper())

    def make_source(self, args, stdin=STDIN):
        """Create a HXL input source."""

        # construct the input object
        input = self.make_input(args, stdin)
        return hxl.io.data(input)

    def make_input(self, args, stdin=sys.stdin, url_or_filename=None):
        """Create an input object"""

        if url_or_filename is None:
            url_or_filename = args.infile

        # sheet index
        sheet_index = args.sheet
        if sheet_index is not None:
            sheet_index -= 1

        # JSONPath selector
        selector = args.selector

        http_headers = self.make_headers(args)

        return hxl.io.make_input(
            url_or_filename or stdin,
            sheet_index=sheet_index,
            selector=selector,
            allow_local=True,  # TODO: consider change this for execute_web
            http_headers=http_headers,
            verify_ssl=(not args.ignore_certs)
        )

    def make_output(self, args, stdout=sys.stdout):
        """Create an output stream."""
        if args.outfile:
            return FileOutput(args.outfile)
        else:
            return StreamOutput(stdout)

    def make_headers(self, args):
        # get custom headers
        header_strings = []
        header = os.environ.get("HXL_HTTP_HEADER")
        if header is not None:
            header_strings.append(header)
        if args.http_header is not None:
            header_strings += args.http_header
        http_headers = {}
        for header in header_strings:
            parts = header.partition(':')
            http_headers[parts[0].strip()] = parts[2].strip()
        return http_headers


class FileOutput(object):
    """
    FileOutput contains is based on libhxl-python with no changes..
    Last update on this class was 2021-01-25.

    Author: David Megginson
    License: Public Domain
    """

    def __init__(self, filename):
        self.output = open(filename, 'w')

    def __enter__(self):
        return self

    def __exit__(self, value, type, traceback):
        self.output.close()


class StreamOutput(object):
    """
    StreamOutput contains is based on libhxl-python with no changes..
    Last update on this class was 2021-01-25.

    Author: David Megginson
    License: Public Domain
    """

    def __init__(self, output):
        self.output = output

    def __enter__(self):
        return self

    def __exit__(self, value, type, traceback):
        pass

    def write(self, s):
        self.output.write(s)


if __name__ == "__main__":

    hxl2example = HXL2Example()
    args = hxl2example.make_args_hxl2example()

    hxl2example.execute_cli(args)
