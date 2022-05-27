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

# @TODO: considerar entrar nesses Wikidata projects
#        - https://www.wikidata.org/wiki/Wikidata:WikiProject_Brazilian_Laws
#        - https://meta.wikimedia.org/wiki/Wiki_Movement_Brazil_User_Group/pt-br
#        - https://www.wikidata.org/wiki/Wikidata:WikiProject_Hospitals
# @TODO: potenciais listas em breve
#        - https://www.wikidata.org/wiki/Wikidata:WikiProject_Medicine/Hospitals_by_country/Brazil
#        - https://pt.wikipedia.org/wiki/Lista_de_hospitais_universit%C3%A1rios
#        - https://pt.wikipedia.org/wiki/Lista_de_hospitais_do_Cear%C3%A1
#        - pontos de entrada
#          - https://www.wikidata.org/wiki/Wikidata:WikiProject_Hospitals/Properties
#          - https://www.wikidata.org/wiki/Wikidata:WikiProject_Companies/Properties
#            - Caso de uso: nome fantasia e nome oficial de hospitais e afins
#
# @TODO:
#        - ftp://ftp.datasus.gov.br/cnes
#        - ftp://ftp.datasus.gov.br/cnes/Download/SCNES_DICIONARIO_DE_DADOS.ZIP
#        - ftp://ftp.datasus.gov.br/cnes/BASE_DE_DADOS_CNES_202204.ZIP
#          - tbEstabelecimento202204.csv
#        - Ver também
#          - https://wiki.saude.gov.br/cnes/index.php/Principais_Conceitos
#        - https://cnes.datasus.gov.br/pages/downloads/arquivosOutros.jsp
#        - https://purl.org/anac/opendata

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
# actiones_completis_locali "1679_1_1"


# actiones_completis_locali "1603_45_49"
# exit 0

# cat 999999/0/ibge_un_adm2.tm.hxl.csv | ./999999999/0/999999999_54872.py --objectivum-formato=application/x-turtle --archivum-configurationi-ex-fonti=999999999/0/999999999_268072.meta.yml --praefixum-configurationi-ex-fonti=methodus,ibge_un_adm2 > 999999/0/ibge_un_adm2.no1.skos.ttl

# cat 999999/0/xmlCNES.tm.hxl.csv | ./999999999/0/999999999_54872.py --objectivum-formato=application/x-turtle --archivum-configurationi-ex-fonti=999999999/0/999999999_10263485.meta.yml --praefixum-configurationi-ex-fonti=methodus,datasus_xmlcnae > 999999/0/xmlCNES.no1.skos.ttl

# archivum_unzip "999999/0/0/ftp.datasus.gov.br/cnes/CNESBRASIL.ZIP" "xmlCNES.xml" "999999/0/xmlCNES.xml"

# ./999999999/0/999999999_10263485.py \
#   --methodus=datasus_xmlcnae --objectivum-formato=hxltm_csv \
#   "999999/0/xmlCNES.xml" >"999999/0/xmlCNES.tm.hxl.csv"

# ./999999999/0/999999999_10263485.py \
#   --methodus=datasus_xmlcnae --objectivum-formato=hxltm_csv \
#   "999999/0/xmlCNES.xml" >"999999/1603/63/49/76/1603_63_49_76.tm.hxl.csv"

# hxlcut --exclude="#meta" "999999/1603/63/49/76/1603_63_49_76.tm.hxl.csv" | hxlcut --skip-untagged | hxladd --before --spec="#item+conceptum+codicem={{#item+rem+i_qcc+is_zxxx+ix_v76vcnes}}" | hxladd --before --spec="#item+conceptum+numerordinatio=1603:63:49:76:{{#item+conceptum+codicem}}" | hxlsort --tags="#item+conceptum+codicem" >"999999/1603/63/49/76/1603_63_49_76.no1.tm.hxl.csv"

# sed -i '1d' "999999/1603/63/49/76/1603_63_49_76.no1.tm.hxl.csv"

# archivum_copiae "1603_63_49_76" "1603_63_49_76" "no1.tm.hxl.csv" "1" "0"

# wikidata_p_ex_interlinguis "1679_45_16_76_2" "1" "1" "P1585" "P1585,P17,P131,P402,P1566,P1937,P6555,P8119"

# exit 1

file_download_1603_xlsx "1"
actiones_completis_locali "1603_1_1"

# The SKOS generation need optimization. Over 14min. Obviously not optimized
actiones_completis_locali "1603_63_49_76"

exit 0
#### Manual action, TEST locally, one per time, END ----------------------------

#### main ______________________________________________________________________
file_download_1603_xlsx "1"
actiones_completis_locali "1603_1_1"

## Create "1603_45_16_76_2" (refs IBGE municipality) only from Wikidata, start -
# @TODO: this is just a quick test; the ideal is buld from autorative
#        references here https://servicodados.ibge.gov.br/api/docs/localidades
### //Dicionários de bases de dados espaciais do Brasil//@por-Latn
wikidata_p_ex_totalibus "1679_45_16_76_2" "1" "1" "P1585" "P1585,P17,P131,P402,P1566,P1937,P6555,P8119"
archivum_copiae "1679_45_16_76_2" "1603_45_16_76_2" "no1.tm.hxl.csv" "1" "0"
archivum_copiae "1679_45_16_76_2" "1603_45_16_76_2" "no11.tm.hxl.csv" "1" "0"
actiones_completis_locali "1603_45_16_76_2"

### P4251 //número da legenda no TSE//@por-Latn
wikidata_p_ex_interlinguis "1679_3_12_4251" "1" "1" "P4251" "P4251" "0"

### P6204 //Cadastro Nacional da Pessoa Jurídica//@por-Latn
wikidata_p_ex_interlinguis "1679_3_12_6204" "1" "1" "P6204" "P6204,P17,P131" "1"

### P6555 //identificador de Unidade Eleitoral brasileira//@por-Latn
wikidata_p_ex_interlinguis "1679_3_12_6555" "1" "1" "P6555" "P6555,P131" "0"

### P9119 //Identificador LeXML Brasil//@por-Latn
wikidata_p_ex_interlinguis "1679_3_12_9119" "1" "1" "P9119" "P9119,P1476" "1"

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

exit 0
