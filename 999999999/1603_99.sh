#!/bin/bash
#===============================================================================
#
#          FILE:  1603_99.sh
#
#         USAGE:  ./999999999/1603_99.sh
#                 time ./999999999/1603_99.sh
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
#       CREATED:  2022-01-29 07:09 UTC
#      REVISION:  ---
#===============================================================================
# Comment next line if not want to stop on first error
set -e

DATA_1603_99_987="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=2048563869"
DATA_1603_99_876="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=329568466"
ROOTDIR="$(pwd)"


# shellcheck source=999999999.lib.sh
. "$ROOTDIR"/999999999/999999999.lib.sh

file_download_if_necessary "$DATA_1603_99_987" "1603_99_987" "csv" "tm.hxl.csv" "hxltmcli" "1"
file_convert_numerordinatio_de_hxltm "1603_99_987" "1" "0"
# neo_codex_de_numerordinatio "1603_99_876" "0" "0"

file_download_if_necessary "$DATA_1603_99_876" "1603_99_876" "csv" "tm.hxl.csv" "hxltmcli" "1"
file_convert_numerordinatio_de_hxltm "1603_99_876" "1" "0"
# neo_codex_de_numerordinatio "1603_99_876" "0" "0"

exit 0
