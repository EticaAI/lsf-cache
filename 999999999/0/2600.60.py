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
# from pathlib import Path

import csv

NUMERORDINATIO_BASIM = os.getenv('NUMERORDINATIO_BASIM', os.getcwd())

# print('getcwd:      ', os.getcwd())
# print('oi', NUMERORDINATIO_BASIM)


def quod_1613_2_60():
    with open(NUMERORDINATIO_BASIM + "/1613/1603.2.60.tsv") as file:
        tsv_file = csv.reader(file, delimiter="\t")
        for row in tsv_file:
            print("\t".join(row))


quod_1613_2_60()