#!/bin/bash
#===============================================================================
#
#          FILE:  1603_3_1603_45_1.sh
#
#         USAGE:  ./999999999/1603_3_1603_45_1.sh
#                 time ./999999999/1603_3_1603_45_1.sh
#                 time FORCE_CHANGED=1 ./999999999/1603_3_1603_45_1.sh
#
#   DESCRIPTION:  ---
#
#       OPTIONS:  ---
#
#  REQUIREMENTS:  - Bash shell (or better)
#          BUGS:  ---
#         NOTES:  ---
#        AUTHOR:  Emerson Rocha <rocha[at]ieee.org>
#       COMPANY:  EticaAI
#       LICENSE:  Public Domain dedication or Zero-Clause BSD
#                 SPDX-License-Identifier: Unlicense OR 0BSD
#       VERSION:  v1.0
#       CREATED:  2022-01-21 01:22 UTC
#      REVISION:  ---
#===============================================================================
# Comment next line if not want to stop on first error
set -e

ROOTDIR="$(pwd)"

# shellcheck source=999999999.lib.sh
. "$ROOTDIR"/999999999/999999999.lib.sh


# printf "Q1065\nQ82151\n" | ./999999999/0/1603_3_12.py --actionem-sparql --query | ./999999999/0/1603_3_12.py --actionem-sparql --csv

# FORCE_REDOWNLOAD_REM="1603_1_51"
# file_download_if_necessary "$DATA_1603_1_51" "1603_1_51" "csv" "tm.hxl.csv" "hxltmcli" "1"
# file_translate_csv_de_numerordinatio_q "1603_1_51" "1" "0"

file_translate_csv_de_numerordinatio_q "1603_45_1" "0" "0"

# echo "TODO $1"

# Use this to fetch translations from 1603_45_1
