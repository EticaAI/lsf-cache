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
DATA_1613="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=1281616178"


ROOTDIR="$(pwd)"

PREFIX_1613_3="1613:3"

# shellcheck source=../999999999.lib.sh
. "$ROOTDIR"/999999999/999999999.lib.sh


# if true ; then
#     echo ''
#     wget -qO- "$humanitarium_responsum_rem" > "${ROOTDIR}/999999/1613/vaccinum.tm.hxl.csv"
# fi
# wget -qO- "$humanitarium_responsum_rem" > "${ROOTDIR}/999999/1613/vaccinum.tm.hxl.csv"



#######################################
# Download DATA_1613 from external source files
#
# Globals:
#   ROOTDIR
#   DATA_UN_M49_CSV
# Arguments:
#   None
# Outputs:
#   Writes to 999999/1603/45/49/1603_45_49.hxl.csv
#######################################
1613__external_fetch() {
  objectivum_archivum="${ROOTDIR}/999999/1613/1613.tm.hxl.csv"
  objectivum_archivum_temporarium="${ROOTDIR}/999999/0/1613.tm.hxl.csv"

  # echo "hxltmcli $DATA_1613"

  if [ -z "$(stale_archive "$objectivum_archivum")" ]; then return 0; fi

  echo "${FUNCNAME[0]} stale data on [$objectivum_archivum], refreshing..."

  hxltmcli "$DATA_1613" > "$objectivum_archivum_temporarium"

  # curl --header "Accept: text/csv" \
  #   --compressed --silent --show-error \
  #   --get "$DATA_1613" \
  #   --output "$objectivum_archivum_temporarium"

  file_update_if_necessary csv "$objectivum_archivum_temporarium" "$objectivum_archivum"
}

#######################################
# Download DATA_1613 from external source files
#
# Globals:
#   ROOTDIR
#   DATA_UN_M49_CSV
# Arguments:
#   None
# Outputs:
#   Writes to 999999/1613/1613.tm.hxl.csv
#######################################
1613__external_fetch() {
  objectivum_archivum="${ROOTDIR}/999999/1613/1613.tm.hxl.csv"
  objectivum_archivum_temporarium="${ROOTDIR}/999999/0/1613.tm.hxl.csv"

  # echo "hxltmcli $DATA_1613"

  # if [ -z "$(stale_archive "$objectivum_archivum")" ]; then return 0; fi

  echo "${FUNCNAME[0]} stale data on [$objectivum_archivum], refreshing..."

  hxltmcli "$DATA_1613" > "$objectivum_archivum_temporarium"

  # curl --header "Accept: text/csv" \
  #   --compressed --silent --show-error \
  #   --get "$DATA_1613" \
  #   --output "$objectivum_archivum_temporarium"

  file_update_if_necessary csv "$objectivum_archivum_temporarium" "$objectivum_archivum"
}

######################################
# Download external source files.
# Note: using raw tab file for now.
#
# Globals:
#   ROOTDIR
# Arguments:
#   [File] 999999/1613/1613.tm.hxl.csv
# Outputs:
#   [File] 1613/1603_3.no1.tm.hxl.tsv
#######################################
1613_3_deploy() {
  fontem_archivum="${ROOTDIR}/999999/1613/1613.tm.hxl.csv"
  objectivum_archivum="${ROOTDIR}/1613/1603_3.no1.tm.hxl.csv"
  objectivum_archivum_temporarium="${ROOTDIR}/999999/0/1603_3.no1.tm.hxl.csv"

  # if [ -z "$(changed_recently "$fontem_archivum")" ]; then return 0; fi

  echo "${FUNCNAME[0]} sources changed_recently. Reloading..."

  # Note: ix_iso3166p1 would generate -x-iso3166p1, 9 characters, but BCP limit to 8
  # Note: ix_unreliefweb would generate -x-unreliefweb, 11 characters, but BCP limit to 8

  # hxlrename \
  #   --rename="#country+name+i_en+alt+v_unterm:#item+rem+i_eng+is_latn+ix_unterm" \
  #   --rename="#country+name+i_fr+alt+v_unterm:#item+rem+i_fra+is_latn+ix_unterm" \
  #   --rename="#country+name+i_es+alt+v_unterm:#item+rem+i_spa+is_latn+ix_unterm" \
  #   --rename="#country+name+i_ru+alt+v_unterm:#item+rem+i_rus+is_cyrl+ix_unterm" \
  #   --rename="#country+name+i_zh+alt+v_unterm:#item+rem+i_zho+is_hans+ix_unterm" \
  #   --rename="#country+name+i_ar+alt+v_unterm:#item+rem+i_ara+is_arab+ix_unterm" \
  #   "${fontem_archivum}" |
  #   hxlselect --query="#country+code+num+v_m49>0" |
  #   hxladd --before --spec="#item+rem+i_zxx+is_zmth+ix_unfts={{#country+code+v_fts}}" |
  #   hxladd --before --spec="#item+rem+i_zxx+is_zmth+ix_unreliefweb={{#country+code+v_reliefweb}}" |
  #   hxladd --before --spec="#item+rem+i_zxx+is_zmth+ix_unhrinfo={{#country+code+v_hrinfo_country}}" |
  #   hxladd --before --spec="#item+rem+i_zxx+is_zmth+ix_unm49={{#country+code+num+v_m49}}" |
  #   hxladd --before --spec="#item+conceptum+codicem={{#country+code+num+v_m49}}" |
  #   hxlsort --tags="#item+conceptum" \
  #     >"${objectivum_archivum_temporarium}"
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


1613__external_fetch
1613_3_deploy
