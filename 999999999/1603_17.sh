#!/bin/bash
#===============================================================================
#
#          FILE:  1603_17.sh
#
#         USAGE:  ./999999999/1603_17.sh
#                 FORCE_REDOWNLOAD=1 ./999999999/1603_17.sh
#                 FORCE_CHANGED=1 ./999999999/1603_17.sh
#                 FORCE_REDOWNLOAD_REM="1603_1_51" ./999999999/1603_17.sh
#   DESCRIPTION:  ---
#
#       OPTIONS:  ---
#
#  REQUIREMENTS:  - hxltmcli
#          BUGS:  ---
#         NOTES:  ---
#        AUTHOR:  Emerson Rocha <rocha[at]ieee.org>
#       COMPANY:  EticaAI
#       LICENSE:  Public Domain dedication
#                 SPDX-License-Identifier: Unlicense
#       VERSION:  v1.0
#       CREATED:  2022-01-13 16:43 UTC started, based on EticaAI/
#                                      HXL-CPLP/Auxilium-Humanitarium-API
#                                      /_systema/programma/download-hxl-datum.sh
#      REVISION:  2021-01-17 16:52 UTC 999999999/1613/1613.sh -> 1603_17.sh
#===============================================================================

# humanitarium_responsum_rem="https://proxy.hxlstandard.org/data/download/humanitarium-responsum-rem_hxl.csv?dest=data_edit&filter01=select&filter-label01=%23status%3E-1&select-query01-01=%23status%3E-1&filter02=cut&filter-label02=HXLated&cut-skip-untagged02=on&strip-headers=on&force=on&url=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fd%2F1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4%2Fedit%23gid%3D1331879749"
DATA_1603_1_1="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=2095477004"
# DATA_1603_17_17="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=1281616178"
DATA_1603_3_12_6="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=1281616178"
DATA_1603_45_1="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=1894917893"
# DATA_1603_994_1="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=1366500643"
DATA_1603_84_1="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=1366500643"
DATA_1603_44_1="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=1333477190"
DATA_1603_44_142="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=455141043"
DATA_1603_1_51="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=272891124"
DATA_1603_1_101="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=1902379960"

ROOTDIR="$(pwd)"

# PREFIX_1613_3="1613:3"
# PREFIX_1603_994_1="1603:994:1"
# PREFIX_1603_44_1="1603:44:1"
# PREFIX_1603_44_142="1603:44:142"

# shellcheck source=999999999.lib.sh
. "$ROOTDIR"/999999999/999999999.lib.sh

file_download_if_necessary "$DATA_1603_1_1" "1603_1_1" "csv" "tm.hxl.csv" "hxltmcli" "1"
file_convert_numerordinatio_de_hxltm "1603_1_1" "1" "0"

file_download_if_necessary "$DATA_1603_1_101" "1603_1_101" "csv" "tm.hxl.csv" "hxltmcli" "1"
file_convert_numerordinatio_de_hxltm "1603_1_101" "1" "0"

# FORCE_REDOWNLOAD_REM="1603_1_51"
file_download_if_necessary "$DATA_1603_1_51" "1603_1_51" "csv" "tm.hxl.csv" "hxltmcli" "1"
file_convert_numerordinatio_de_hxltm "1603_1_51" "1" "0"

# file_download_if_necessary "$DATA_1603_17_17" "1603_17_17" "csv" "tm.hxl.csv" "hxltmcli" "1"
# file_convert_numerordinatio_de_hxltm "1603_17_17" "1" "0"
file_download_if_necessary "$DATA_1603_3_12_6" "1603_3_12_6" "csv" "tm.hxl.csv" "hxltmcli" "1"
file_convert_numerordinatio_de_hxltm "1603_3_12_6" "1" "0"

file_download_if_necessary "$DATA_1603_44_142" "1603_44_142" "csv" "tm.hxl.csv" "hxltmcli" "1"
file_convert_numerordinatio_de_hxltm "1603_44_142" "1" "0"

file_download_if_necessary "$DATA_1603_44_1" "1603_44_1" "csv" "tm.hxl.csv" "hxltmcli" "1"
file_convert_numerordinatio_de_hxltm "1603_44_1" "1" "0"

# file_download_if_necessary "$DATA_1603_994_1" "1603_994_1" "csv" "tm.hxl.csv" "hxltmcli" "1"
# file_convert_numerordinatio_de_hxltm "1603_994_1" "1" "0"

file_download_if_necessary "$DATA_1603_84_1" "1603_84_1" "csv" "tm.hxl.csv" "hxltmcli" "1"
file_convert_numerordinatio_de_hxltm "1603_84_1" "1" "0"

file_download_if_necessary "$DATA_1603_45_1" "1603_45_1" "csv" "tm.hxl.csv" "hxltmcli" "1"
file_convert_numerordinatio_de_hxltm "1603_45_1" "1" "0"
