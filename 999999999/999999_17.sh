#!/bin/bash
#===============================================================================
#
#          FILE:  999999_17.sh
#
#         USAGE:  ./999999999/999999_17.sh
#                 FORCE_REDOWNLOAD=1 ./999999999/999999_17.sh
#                 FORCE_CHANGED=1 ./999999999/999999_17.sh
#                 FORCE_REDOWNLOAD_REM="1603_1_51" ./999999999/999999_17.sh
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
#       CREATED:  2022-01-13 16:43 UTC started. based on 1603_17_0.sh
#      REVISION:  ---
#===============================================================================
set -e

# humanitarium_responsum_rem="https://proxy.hxlstandard.org/data/download/humanitarium-responsum-rem_hxl.csv?dest=data_edit&filter01=select&filter-label01=%23status%3E-1&select-query01-01=%23status%3E-1&filter02=cut&filter-label02=HXLated&cut-skip-untagged02=on&strip-headers=on&force=on&url=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fd%2F1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4%2Fedit%23gid%3D1331879749"
DATA_1603_1_1="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=2095477004"
# DATA_1603_1_6="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=1417450794"
# DATA_1603_1_7="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=1792999005"
DATA_1603_1_99="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=304729260"
# DATA_1603_17_17="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=1281616178"
# DATA_1603_3_12_6="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=1281616178"
# DATA_1603_25_1="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=966182339"
# DATA_1603_45_1="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=1894917893"
# DATA_1603_45_31="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=1610303107"
# DATA_1603_45_95="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=1391701984"
# DATA_1603_994_1="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=1366500643"
# DATA_1603_84_1="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=1366500643"
# DATA_1603_44_1="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=1333477190"
# DATA_1603_44_142="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=455141043"
# DATA_1603_1_51="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=272891124"
# DATA_1603_1_101="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=1902379960"
# DATA_1603_64_604="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=1016692458"
DATA_1603_23_21="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=1939636120"
DATA_1603_23_36="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=2020660171"
DATA_1603_63_1="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=80558354"

ROOTDIR="$(pwd)"

# PREFIX_1613_3="1613:3"
# PREFIX_1603_994_1="1603:994:1"
# PREFIX_1603_44_1="1603:44:1"
# PREFIX_1603_44_142="1603:44:142"

# shellcheck source=999999999.lib.sh
. "$ROOTDIR"/999999999/999999999.lib.sh

file_download_if_necessary "$DATA_1603_1_1" "1603_1_1" "csv" "tm.hxl.csv" "hxltmcli" "1"
file_convert_numerordinatio_de_hxltm "1603_1_1" "1" "0"

file_download_if_necessary "$DATA_1603_1_99" "1603_1_99" "csv" "tm.hxl.csv" "hxltmcli" "1"
file_convert_numerordinatio_de_hxltm "1603_1_99" "1" "0"

# file_download_if_necessary "$DATA_1603_45_1" "1603_45_1" "csv" "tm.hxl.csv" "hxltmcli" "1"
# file_convert_numerordinatio_de_hxltm "1603_45_1" "1" "0"
# file_translate_csv_de_numerordinatio_q "1603_45_1" "0" "0"
# file_merge_numerordinatio_de_wiki_q "1603_45_1" "0" "0"
# neo_codex_de_numerordinatio "1603_45_1" "0" "0"
# neo_codex_de_numerordinatio_pdf "1603_45_1" "0" "0"

# file_download_if_necessary "$DATA_1603_1_7" "1603_1_7" "csv" "tm.hxl.csv" "hxltmcli" "1"
# file_convert_numerordinatio_de_hxltm "1603_1_7" "1" "0"
# # file_merge_numerordinatio_de_wiki_q "1603_1_7" "0" "0"
# neo_codex_de_numerordinatio "1603_1_7" "0" "0"
# neo_codex_de_numerordinatio_pdf "1603_1_7" "0" "0"

# file_download_if_necessary "$DATA_1603_45_31" "1603_45_31" "csv" "tm.hxl.csv" "hxltmcli" "1"
# file_convert_numerordinatio_de_hxltm "1603_45_31" "1" "0"
# file_translate_csv_de_numerordinatio_q "1603_45_31" "0" "0"
# file_merge_numerordinatio_de_wiki_q "1603_45_31" "0" "0"
# neo_codex_de_numerordinatio "1603_45_31" "0" "0"
# neo_codex_de_numerordinatio_pdf "1603_45_31" "0" "0"

file_download_if_necessary "$DATA_1603_23_21" "1603_23_21" "csv" "tm.hxl.csv" "hxltmcli" "1"
file_convert_numerordinatio_de_hxltm "1603_23_21" "1" "0"
file_translate_csv_de_numerordinatio_q "1603_23_21" "0" "0"
file_merge_numerordinatio_de_wiki_q "1603_23_21" "0" "0"
file_convert_xml_de_numerordinatio11 "1603_23_21"
file_convert_tmx_de_numerordinatio11 "1603_23_21"
file_convert_tbx_de_numerordinatio11 "1603_23_21"
neo_codex_de_numerordinatio "1603_23_21" "0" "0"
neo_codex_de_numerordinatio_pdf "1603_23_21" "0" "0"

file_download_if_necessary "$DATA_1603_23_36" "1603_23_36" "csv" "tm.hxl.csv" "hxltmcli" "1"
file_convert_numerordinatio_de_hxltm "1603_23_36" "1" "0"
file_translate_csv_de_numerordinatio_q "1603_23_36" "0" "0"
file_merge_numerordinatio_de_wiki_q "1603_23_36" "0" "0"
neo_codex_de_numerordinatio "1603_23_36" "0" "0"
neo_codex_de_numerordinatio_pdf "1603_23_36" "0" "0"

file_download_if_necessary "$DATA_1603_63_1" "1603_63_1" "csv" "tm.hxl.csv" "hxltmcli" "1"
file_convert_numerordinatio_de_hxltm "1603_63_1" "1" "0"
file_translate_csv_de_numerordinatio_q "1603_63_1" "0" "0"
file_merge_numerordinatio_de_wiki_q "1603_63_1" "0" "0"
neo_codex_de_numerordinatio "1603_63_1" "0" "0"
neo_codex_de_numerordinatio_pdf "1603_63_1" "0" "0"



# hxltmcli --objectivum-TMX 1603/1/7/1603_1_7.no1.tm.hxl.csv 1603/1/7/1603_1_7.tmx
# hxltmcli --objectivum-TBX-Basim 1603/1/7/1603_1_7.no1.tm.hxl.csv 1603/1/7/1603_1_7.tbx
#
# hxltmcli --objectivum-TBX-Basim 1603/45/1/1603_45_1.no11.tm.hxl.csv 1603/45/1/1603_45_1.tbx
