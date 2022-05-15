#!/bin/bash
#===============================================================================
#
#          FILE:  999999_1679.sh
#
#         USAGE:  ./999999999/999999_1679.sh
#                 FORCE_REDOWNLOAD=1 ./999999999/999999_1679.sh
#                 FORCE_CHANGED=1 ./999999999/999999_1679.sh
#                 FORCE_REDOWNLOAD_REM="1603_1_51" ./999999999/999999_1679.sh
#                 time ./999999999/999999_1679.sh
#   DESCRIPTION:  Temporary tests related to Brazilian namespace. Use case from
#                 https://github.com/EticaAI/lexicographi-sine-finibus/issues/39
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
#       CREATED:  2022-05-12 14:18 UTC started. based on 1603_99.sh
#      REVISION:  ---
#===============================================================================
set -e

# time HTTPS_PROXY="socks5://127.0.0.1:9050" ./999999999/999999_1679.sh

# ./999999999/0/1603_1.py --methodus='codex' --codex-de 1603_45_31 --codex-in-tabulam-json | jq
# ./999999999/0/1603_1.py --methodus='codex' --codex-de 1603_45_31 --codex-in-tabulam-json > 1603/45/31/1603_45_31.mul-Latn.tab.json
# https://commons.wikimedia.org/wiki/Data:Sandbox/EmericusPetro/Example.tab

# @TODO: implement download entire sheet
DATA_1603="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/export?format=xlsx"

ROOTDIR="$(pwd)"

# shellcheck source=999999999.lib.sh
. "$ROOTDIR"/999999999/999999999.lib.sh


#### Manual action, TEST locally, one per time, START --------------------------
# Download entire XLSX to local temp
# file_download_1603_xlsx "1"
# actiones_completis_locali "1603_1_1"
# actiones_completis_locali "1603_1_7"
# actiones_completis_locali "1603_1_51"

# actiones_completis_locali "1679_1_1"


#### Manual action, TEST locally, one per time, END ----------------------------


#### main ______________________________________________________________________
file_download_1603_xlsx "1"
actiones_completis_locali "1603_1_1"


actiones_completis_locali "1603_45_16_76_2"

exit 0

wikidata_p_ex_linguis "1679_45_16_76_2" "1" "1" "P1585" "4" "20"
archivum_copiae "1679_45_16_76_2" "1603_45_16_76_2" "no1.tm.hxl.csv" "1" "0"
archivum_copiae "1679_45_16_76_2" "1603_45_16_76_2" "no11.tm.hxl.csv" "1" "0"

# exit 0

### //Dicionários de bases de dados espaciais do Brasil//@por-Latn
wikidata_p_ex_totalibus "1679_45_16_76_2" "1" "1" "P1585" "P402,P1566,P1937,P6555,P8119"

### P4251 //número da legenda no TSE//@por-Latn
wikidata_p_ex_interlinguis "1679_3_12_4251" "1" "1" "P4251" ""

### P6204 //Cadastro Nacional da Pessoa Jurídica//@por-Latn
# wikidata_p_ex_interlinguis "1679_3_12_6204" "1" "1" "P6204" ""
#     ValueError: invalid literal for int() with base 10: '00.317.929/0001-49'

### P6555 //identificador de Unidade Eleitoral brasileira//@por-Latn
wikidata_p_ex_interlinguis "1679_3_12_6555" "1" "1" "P6555" ""

### P9119 //Identificador LeXML Brasil//@por-Latn
# wikidata_p_ex_interlinguis "1679_3_12_9119" "1" "1" "P9119" ""
#     ValueError: invalid literal for int() with base 10: 'urn:lex:br:advocacia.geral.uniao;procuradoria.geral.federal:portaria:2003-06-13;208'

# @TODO criar funcao que "migre" resultado final arquivos selecionados; exemplo
#        [1679_45_16_76_2] -> [1603_45_16_76_2]
#
#        1679_45_16_76_2.no1.tm.hxl.csv
#        1679_45_16_76_2.no11.tm.hxl.csv
#        1679_45_16_76_2.wikiq.tm.hxl.csv

# @see https://servicodados.ibge.gov.br/api/docs/localidades
# @see https://github.com/search?o=desc&q=ibge&s=stars&type=Repositories
# @see CNAE
#      - https://servicodados.ibge.gov.br/api/docs/CNAE?versao=2#api-_
#      - https://cnae.ibge.gov.br/images/concla/documentacao/CNAE20_Introducao.pdf
# @see https://sidra.ibge.gov.br/home/pnadct/brasil
# @see https://servicodados.ibge.gov.br/api/docs
# @see - https://servicodados.ibge.gov.br/api/docs/produtos?versao=1
#        - https://servicodados.ibge.gov.br/api/v1/produtos/estatisticas
#        - https://servicodados.ibge.gov.br/api/v1/produtos/geociencias
#        - https://biblioteca.ibge.gov.br/visualizacao/livros/liv100600.pdf

exit 1

