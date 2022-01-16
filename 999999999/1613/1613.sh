#!/bin/bash
#===============================================================================
#
#          FILE:  1613.sh
#
#         USAGE:  ./999999999/1613/1613.sh
#
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
#      REVISION: ---
#===============================================================================

# humanitarium_responsum_rem="https://proxy.hxlstandard.org/data/download/humanitarium-responsum-rem_hxl.csv?dest=data_edit&filter01=select&filter-label01=%23status%3E-1&select-query01-01=%23status%3E-1&filter02=cut&filter-label02=HXLated&cut-skip-untagged02=on&strip-headers=on&force=on&url=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fd%2F1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4%2Fedit%23gid%3D1331879749"
DATA_1613_3="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=1281616178"
DATA_1603_994_1="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=1366500643"


ROOTDIR="$(pwd)"

PREFIX_1613_3="1613:3"
PREFIX_1603_994_1="1613:994:1"

# shellcheck source=../999999999.lib.sh
. "$ROOTDIR"/999999999/999999999.lib.sh


# if true ; then
#     echo ''
#     wget -qO- "$humanitarium_responsum_rem" > "${ROOTDIR}/999999/1613/vaccinum.tm.hxl.csv"
# fi
# wget -qO- "$humanitarium_responsum_rem" > "${ROOTDIR}/999999/1613/vaccinum.tm.hxl.csv"



#######################################
# Download DATA_1613_3 from external source files
#
# Globals:
#   ROOTDIR
#   DATA_1613_3
# Arguments:
#   None
# Outputs:
#   Writes to 999999/1603/45/49/1603_45_49.hxl.csv
#######################################
1613_3__external_fetch() {
  objectivum_archivum="${ROOTDIR}/999999/1613/1613.tm.hxl.csv"
  objectivum_archivum_temporarium="${ROOTDIR}/999999/0/1613.tm.hxl.csv"

  if [ -z "$(stale_archive "$objectivum_archivum")" ]; then return 0; fi

  echo "${FUNCNAME[0]} stale data on [$objectivum_archivum], refreshing..."

  hxltmcli "$DATA_1613_3" > "$objectivum_archivum_temporarium"

  file_update_if_necessary csv "$objectivum_archivum_temporarium" "$objectivum_archivum"
}

#######################################
# Download DATA_1613_3 from external source files
#
# Globals:
#   ROOTDIR
#   DATA_1603_994_1
# Arguments:
#   None
# Outputs:
#   Writes to 999999/1603/994/1/1603_994_1.tm.hxl.csv
#######################################
1603_994_1__external_fetch() {
  objectivum_archivum="${ROOTDIR}/999999/1603/994/1/1603_994_1.tm.hxl.csv"
  objectivum_archivum_temporarium="${ROOTDIR}/999999/0/1603_994_1.tm.hxl.csv"

  if [ -z "$(stale_archive "$objectivum_archivum")" ]; then return 0; fi

  echo "${FUNCNAME[0]} stale data on [$objectivum_archivum], refreshing..."

  hxltmcli "$DATA_1603_994_1" > "$objectivum_archivum_temporarium"

  file_update_if_necessary csv "$objectivum_archivum_temporarium" "$objectivum_archivum"
}

######################################
# Deploy 1613_3
#
# Globals:
#   ROOTDIR
#   PREFIX_1613_3
# Arguments:
#   [File] 999999/1613/1613.tm.hxl.csv
# Outputs:
#   [File] 1613/1603_3.no1.tm.hxl.tsv
#######################################
1613_3__deploy() {
  fontem_archivum="${ROOTDIR}/999999/1613/1613.tm.hxl.csv"
  objectivum_archivum="${ROOTDIR}/1613/1603_3.no1.tm.hxl.csv"
  objectivum_archivum_temporarium="${ROOTDIR}/999999/0/1603_3.no1.tm.hxl.csv"

  if [ -z "$(changed_recently "$fontem_archivum")" ]; then return 0; fi

  echo "${FUNCNAME[0]} sources changed_recently. Reloading..."


  hxlcut --exclude="#meta" \
    "$fontem_archivum" \
    | hxlselect --query="#item+conceptum+codicem>0" \
    | hxladd --before --spec="#item+conceptum+numerordinatio=${PREFIX_1613_3}:{{#item+conceptum+codicem}}" \
    > "$objectivum_archivum_temporarium"

  # cp "$fontem_archivum" "$objectivum_archivum_temporarium"

  # Strip empty header (already is likely to be ,,,,,,)
  sed -i '1d' "${objectivum_archivum_temporarium}"

  file_update_if_necessary csv "$objectivum_archivum_temporarium" "$objectivum_archivum"
}

######################################
# Deploy 1603_994_1
#
# Globals:
#   ROOTDIR
#   PREFIX_1603_994_1
# Arguments:
#   [File] 999999/1603/994/1/1603_994_1.tm.hxl.csv
# Outputs:
#   [File] 1603/994/1/1603_994_1.no1.tm.hxl.csv
#######################################
1603_994_1__deploy() {
  fontem_archivum="${ROOTDIR}/999999/1603/994/1/1603_994_1.tm.hxl.csv"
  objectivum_archivum="${ROOTDIR}/1603/994/1/1603_994_1.no1.tm.hxl.csv"
  objectivum_archivum_temporarium="${ROOTDIR}/999999/0/1603_994_1.no1.tm.hxl.csv"

  if [ -z "$(changed_recently "$fontem_archivum")" ]; then return 0; fi

  echo "${FUNCNAME[0]} sources changed_recently. Reloading..."

  hxlcut --exclude="#meta" \
    "$fontem_archivum" \
    | hxlselect --query="#item+conceptum+codicem>0" \
    | hxladd --before --spec="#item+conceptum+numerordinatio=${PREFIX_1603_994_1}:{{#item+conceptum+codicem}}" \
    > "$objectivum_archivum_temporarium"

  #| hxlreplace --tags="#item+conceptum+numerordinatio" --pattern="_" --substitution=":" \

  # cp "$fontem_archivum" "$objectivum_archivum_temporarium"

  # Strip empty header (already is likely to be ,,,,,,)
  sed -i '1d' "${objectivum_archivum_temporarium}"

  file_update_if_necessary csv "$objectivum_archivum_temporarium" "$objectivum_archivum"
}

1613_3__external_fetch
1613_3__deploy

1603_994_1__external_fetch
1603_994_1__deploy
