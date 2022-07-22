#!/bin/bash
#===============================================================================
#
#          FILE:  999999_17.sh
#
#         USAGE:  ./999999999/999999_17.sh
#                 FORCE_REDOWNLOAD=1 ./999999999/999999_17.sh
#                 FORCE_CHANGED=1 ./999999999/999999_17.sh
#                 FORCE_REDOWNLOAD_REM="1603_1_51" ./999999999/999999_17.sh
#                 time ./999999999/999999_17.sh
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

# time HTTPS_PROXY="socks5://127.0.0.1:9050" ./999999999/999999_17.sh

# ./999999999/0/1603_1.py --methodus='codex' --codex-de 1603_45_31 --codex-in-tabulam-json | jq
# ./999999999/0/1603_1.py --methodus='codex' --codex-de 1603_45_31 --codex-in-tabulam-json > 1603/45/31/1603_45_31.mul-Latn.tab.json
# https://commons.wikimedia.org/wiki/Data:Sandbox/EmericusPetro/Example.tab

# @TODO: implement download entire sheet
DATA_1603="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/export?format=xlsx"

ROOTDIR="$(pwd)"

# PREFIX_1613_3="1613:3"
# PREFIX_1603_994_1="1603:994:1"
# PREFIX_1603_44_1="1603:44:1"
# PREFIX_1603_44_142="1603:44:142"

# shellcheck source=999999999.lib.sh
. "$ROOTDIR"/999999999/999999999.lib.sh

### Really boostrapping downloads, start _______________________________________
# file_download_if_necessary "$DATA_1603_1_1" "1603_1_1" "csv" "tm.hxl.csv" "hxltmcli" "1"
# file_convert_numerordinatio_de_hxltm "1603_1_1" "1" "0"

# file_download_if_necessary "$DATA_1603_1_99" "1603_1_99" "csv" "tm.hxl.csv" "hxltmcli" "1"
# file_convert_numerordinatio_de_hxltm "1603_1_99" "1" "0"

# file_download_if_necessary "$DATA_1603_1_6" "1603_1_6" "csv" "tm.hxl.csv" "hxltmcli" "1"
# file_convert_numerordinatio_de_hxltm "1603_1_6" "1" "0"

# file_download_if_necessary "$DATA_1603_1_7" "1603_1_7" "csv" "tm.hxl.csv" "hxltmcli" "1"
# file_convert_numerordinatio_de_hxltm "1603_1_7" "1" "0"

# file_download_if_necessary "$DATA_1603_1_51" "1603_1_51" "csv" "tm.hxl.csv" "hxltmcli" "1"
# file_convert_numerordinatio_de_hxltm "1603_1_51" "1" "0"

### Quick tests

# file_extract_ix_wikiq "999999/1603/3/45/16/1/1/1603_3_45_16_1_1.tm.hxl.csv" "999999/0/1603_3_45_16_1_1.uniq.q.txt"
# wikiq=$(file_extract_ix_wikiq "999999/1603/3/45/16/1/1/1603_3_45_16_1_1.tm.hxl.csv")

# wikidata_q_ex_totalibus "$wikiq" "999999/1603/3/45/16/1/1/1603_3_45_16_1_1.wikiq.tm.hxl.csv" 
set -x
./999999999/0/999999999_7200235.py --methodus='cod_ab_et_wdata' --numerordinatio-praefixo='1603_16' > 999999/0/teste.csv
ls -lha 999999/0/teste.csv

./999999999/0/999999999_54872.py --methodus=_temp_no1 --numerordinatio-cum-antecessoribus --rdf-trivio=1603 999999/0/teste.csv > 999999/0/teste.ttl-simplici.ttl

# rapper --quiet --input=turtle --output=turtle 999999/0/teste.ttl-simplici.ttl > 999999/0/teste.ttl
rdfpipe --input-format=turtle --output-format=longturtle 999999/0/teste.ttl-simplici.ttl > 999999/0/teste.ttl

./999999999/0/999999999_54872.py --methodus=_temp_no1 --rdf-sine-spatia-nominalibus=skos,wdata,devnull --rdf-trivio=5000 999999/0/teste-4.csv > 999999/0/teste-4.ttl-simplici.ttl

# rapper --quiet --input=turtle --output=turtle 999999/0/teste-4.ttl-simplici.ttl > 999999/0/teste-4.ttl
rdfpipe --input-format=turtle --output-format=longturtle 999999/0/teste-4.ttl-simplici.ttl > 999999/0/teste-4.ttl

./999999999/0/999999999_54872.py --methodus=_temp_no1 --rdf-sine-spatia-nominalibus=devnull --rdf-trivio=5000 999999/0/teste-4.csv > 999999/0/teste-4~full.ttl-simplici.ttl

# rapper --quiet --input=turtle --output=turtle 999999/0/teste-4~full.ttl-simplici.ttl > 999999/0/teste-4~full.ttl
rdfpipe --input-format=turtle --output-format=longturtle 999999/0/teste-4~full.ttl-simplici.ttl > 999999/0/teste-4~full.ttl

rapper --count --input=turtle 999999/0/teste-4~full.ttl

set +x
exit 0
### Really boostrapping downloads, end _________________________________________

# TODO: the formats .no1.tm.hxl.csv stopped being updated with the default
#       drill, like days ago; need re-implement it (rocha, 2022-04-29)

#### Manual action, TEST locally, one per time, START --------------------------
# Download entire XLSX to local temp
file_download_1603_xlsx "1"
# actiones_completis_locali "1603_1_1"
# actiones_completis_locali "1603_1_7"
# actiones_completis_locali "1603_1_51"
# actiones_completis_locali "1603_1_99"
# actiones_completis_locali "1603_25_1"
# actiones_completis_locali "1603_44_86"
# actiones_completis_locali "1603_45_31"
# actiones_completis_locali "1603_63_101"
# actiones_completis_locali "1603_44_86"
# actiones_completis_locali "1603_99_876"
# actiones_completis_locali "1603_1_8000"

#### Manual action, TEST locally, one per time, END ----------------------------

## Full drill (remote, specific item)
# actiones_completis_publicis "1603_63_101"
# actiones_completis_publicis "1603_25_1"
# actiones_completis_publicis "1603_99_123"
# actiones_completis_publicis "1603_1_8000"
# actiones_completis_locali "1679_1_1"
# deploy_0_9_markdown

## Full drill (remote, randon publish few at time)
opus_temporibus_cdn
deploy_0_9_markdown

# temp_validate_librario "locale"
# temp_validate_librario "cdn"

# @TODO: maybe check ssdiff (diff spreadsheets) to our uses.

#### tests _____________________________________________________________________
# https://github.com/frictionlessdata/frictionless-py
# pip3 install frictionless-py
#     frictionless validate data/invalid.csv
#     frictionless validate 1603/63/101/1603_63_101.no11.tm.hxl.csv
#     frictionless validate 1603/63/101/datapackage.json

# https://github.com/CLARIAH/COW
# pip3 install cow-csvw
#     cow_tool build 1603/63/101/1603_63_101.no11.tm.hxl.csv
#     cow_tool convert 1603/63/101/1603_63_101.no11.tm.hxl.csv

# https://github.com/cldf/csvw

# ./999999999/0/1603_1.py --methodus='data-apothecae' --data-apothecae-ex='1603_45_1,1603_45_31' --data-apothecae-ad='apothecae.datapackage.json'
# ./999999999/0/1603_1.py --methodus='data-apothecae' --data-apothecae-ex='1603_45_1,1603_45_31' --data-apothecae-ad='apothecae.sqlite'

# printf "1603_45_1\n1603_45_31" > 999999/0/apothecae-list.txt
# ./999999999/0/1603_1.py --methodus='data-apothecae' --data-apothecae-ex-archivo='999999/0/apothecae-list.txt' --data-apothecae-ad='apothecae.datapackage.json'

# ./999999999/0/1603_1.py --methodus='status-quo' --status-quo-in-rdf-skos-turtle --codex-de 1603_63_101

# ./999999999/0/1603_1.py --methodus='status-quo' --status-quo-in-rdf-skos-turtle --codex-de 1603_63_101 > 1603/63/101/1603_63_101.no11.skos.ttl
# ./999999999/0/1603_1.py --methodus='status-quo' --status-quo-in-rdf-skos-turtle --codex-de 1603_1_7

# ./999999999/0/1603_1.py --methodus='status-quo' --status-quo-in-rdf-skos-turtle --codex-de 1603_1_7 > ~/Downloads/1603_1_7.no11.skos.ttl


#### TODO ______________________________________________________________________
# GitHub gist, create from command line
# https://cli.github.com/manual/gh_gist_edit
