#!/bin/bash
#===============================================================================
#
#          FILE:  1603_45_49.sh
#
#         USAGE:  ./999999999/1603_45_49.sh
#
#   DESCRIPTION:  ...
#
#       OPTIONS:  ---
#
#  REQUIREMENTS:  - Bash shell (or better)
#                 - curl
#                 - libhxl
#          BUGS:  1. fix the "None" which may appear on mathematical fields.
#                    Maybe https://github.com/HXLStandard/hxl-proxy/wiki
#                    /Replace-data-filter ?
#         NOTES:  ---
#        AUTHOR:  Emerson Rocha <rocha[at]ieee.org>
#       COMPANY:  EticaAI
#       LICENSE:  Public Domain dedication or Zero-Clause BSD
#                 SPDX-License-Identifier: Unlicense OR 0BSD
#       VERSION:  v1.1
#       CREATED:  2022-01-04 03:38 UTC based on scripts from github.com/EticaAI
#                                      /HXL-Data-Science-file-formats
#      REVISION:  2021-01-10 05:19 UTC v1.1 1603.45.49.sh -> 1603_45_49.sh
#===============================================================================
# Comment next line if not want to stop on first error
set -e
# set -x

ROOTDIR="$(pwd)"

PRAEFIXUM="1603:45:49:"

# Source:
# - https://vocabulary.unocha.org/
#   - https://docs.google.com/spreadsheets/d/1NjSI2LaS3SqbgYc0HdD8oIb7lofGtiHgoKKATCpwVdY/edit#gid=1088874596
#     - https://proxy.hxlstandard.org/data/edit?dest=data_edit&filter01=cut&cut-skip-untagged01=on&filter02=sort&sort-tags02=%23country%2Bcode%2Bnum%2Bv_m49&strip-headers=on&url=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fd%2F1NjSI2LaS3SqbgYc0HdD8oIb7lofGtiHgoKKATCpwVdY%2Fedit%23gid%3D1088874596

DATA_UN_M49_CSV="https://proxy.hxlstandard.org/data.csv?dest=data_edit&filter01=cut&cut-skip-untagged01=on&filter02=sort&sort-tags02=%23country%2Bcode%2Bnum%2Bv_m49&strip-headers=on&url=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fd%2F1NjSI2LaS3SqbgYc0HdD8oIb7lofGtiHgoKKATCpwVdY%2Fedit%23gid%3D1088874596"

# shellcheck source=999999999.lib.sh
. "$ROOTDIR"/999999999/999999999.lib.sh

#######################################
# Download 1603_45_49 from external source files
#
# Globals:
#   ROOTDIR
#   DATA_UN_M49_CSV
# Arguments:
#   None
# Outputs:
#   Writes to 999999/1603/45/49/1603_45_49.hxl.csv
#######################################
1603_45_49__external_fetch() {
  objectivum_archivum="${ROOTDIR}/999999/1603/45/49/1603_45_49.hxl.csv"
  objectivum_archivum_temporarium="${ROOTDIR}/999999/0/1603_45_49.hxl.csv"

  if [ -z "$(stale_archive "$objectivum_archivum")" ]; then return 0; fi

  echo "${FUNCNAME[0]} stale data on [$objectivum_archivum], refreshing..."

  curl --header "Accept: text/csv" \
    --compressed --silent --show-error \
    --get "$DATA_UN_M49_CSV" \
    --output "$objectivum_archivum_temporarium"

  file_update_if_necessary csv "$objectivum_archivum_temporarium" "$objectivum_archivum"
}

### 1603_45_49.hxl.csv --> 1603_45_49.tm.hxl.csv _______________________________
#######################################
# Download external source files.
# Note: using raw tab file for now.
#
# Globals:
#   ROOTDIR
# Arguments:
#   [File] 999999/1603/45/49/1603_45_49.hxl.csv
# Outputs:
#   [File] 999999/1603/45/49/1603_45_49.tm.hxl.csv
#######################################
1603_45_49__hxl2hxltm() {
  fontem_archivum="${ROOTDIR}/999999/1603/45/49/1603_45_49.hxl.csv"
  objectivum_archivum="${ROOTDIR}/999999/1603/45/49/1603_45_49.tm.hxl.csv"
  objectivum_archivum_temporarium="${ROOTDIR}/999999/0/1603_45_49.tm.hxl.csv"

  if [ -z "$(changed_recently "$fontem_archivum")" ]; then return 0; fi

  echo "${FUNCNAME[0]} sources changed_recently. Reloading..."

  # Note: ix_iso3166p1 would generate -x-iso3166p1, 9 characters, but BCP limit to 8
  # Note: ix_unreliefweb would generate -x-unreliefweb, 11 characters, but BCP limit to 8

  hxlrename \
    --rename="#country+name+i_en+alt+v_unterm:#item+rem+i_eng+is_latn+ix_unterm" \
    --rename="#country+name+i_fr+alt+v_unterm:#item+rem+i_fra+is_latn+ix_unterm" \
    --rename="#country+name+i_es+alt+v_unterm:#item+rem+i_spa+is_latn+ix_unterm" \
    --rename="#country+name+i_ru+alt+v_unterm:#item+rem+i_rus+is_cyrl+ix_unterm" \
    --rename="#country+name+i_zh+alt+v_unterm:#item+rem+i_zho+is_hans+ix_unterm" \
    --rename="#country+name+i_ar+alt+v_unterm:#item+rem+i_ara+is_arab+ix_unterm" \
    "${fontem_archivum}" |
    hxlselect --query="#country+code+num+v_m49>0" |
    hxladd --before --spec="#item+rem+i_zxx+is_zmth+ix_unfts={{#country+code+v_fts}}" |
    hxladd --before --spec="#item+rem+i_zxx+is_zmth+ix_unreliefweb={{#country+code+v_reliefweb}}" |
    hxladd --before --spec="#item+rem+i_zxx+is_zmth+ix_unhrinfo={{#country+code+v_hrinfo_country}}" |
    hxladd --before --spec="#item+rem+i_zxx+is_zmth+ix_unm49={{#country+code+num+v_m49}}" |
    hxladd --before --spec="#item+conceptum+codicem={{#country+code+num+v_m49}}" |
    hxlsort --tags="#item+conceptum" \
      >"${objectivum_archivum_temporarium}"

  # Strip empty header (already is likely to be ,,,,,,)
  sed -i '1d' "${objectivum_archivum_temporarium}"

  file_update_if_necessary csv "$objectivum_archivum_temporarium" "$objectivum_archivum"
}

#######################################
# Download external source files.
# Note: using raw tab file for now.
#
# Globals:
#   ROOTDIR
# Arguments:
#   [File] 999999/1603/45/49/1603_45_49.tm.hxl.csv
# Outputs:
#   [File] 1603/45/49/1603_45_49.no1.tm.hxl.csv
#######################################
1603_45_49__hxltm2numerordinatio() {
  fontem_archivum="${ROOTDIR}/999999/1603/45/49/1603_45_49.tm.hxl.csv"
  objectivum_archivum="${ROOTDIR}/1603/45/49/1603_45_49.no1.tm.hxl.csv"
  objectivum_archivum_temporarium="${ROOTDIR}/999999/0/1603_45_49.no1.tm.hxl.csv"

  if [ -z "$(changed_recently "$fontem_archivum")" ]; then return 0; fi

  echo "${FUNCNAME[0]} sources changed_recently. Reloading..."

  hxlrename \
    --rename="#country+code+v_iso2:#item+rem+i_zxx+is_latn+ix_iso3166p1a2" \
    --rename="#country+code+v_iso3:#item+rem+i_zxx+is_latn+ix_iso3166p1a3" \
    "${fontem_archivum}" |
    hxladd --before --spec="#item+conceptum+numerordinatio=${PRAEFIXUM}{{(#item+conceptum+codicem)+1-1}}" |
    hxlcut --include="#item+conceptum,#item+rem" \
      >"${objectivum_archivum_temporarium}"

  # @TODO: only do this if hxl did not removed empty header files ,,,,,,
  sed -i '1d' "${objectivum_archivum_temporarium}"

  file_update_if_necessary csv "$objectivum_archivum_temporarium" "$objectivum_archivum"
}

#######################################
# 1603_45_49__numerordinatio2tsv
#
# Globals:
#   ROOTDIR
# Arguments:
#   [File] 1603/45/49/1603_45_49.no1.tm.hxl.csv
# Outputs:
#   [File] 999999/999999/1603_45_49.tsv
#######################################
1603_45_49__numerordinatio2tsv() {
  fontem_archivum="${ROOTDIR}/1603/45/49/1603_45_49.no1.tm.hxl.csv"
  objectivum_archivum="${ROOTDIR}/999999/999999/1603_45_49.tsv"
  objectivum_archivum_temporarium="${ROOTDIR}/999999/0/1603_45_49.tsv"

  if [ -z "$(changed_recently "$fontem_archivum")" ]; then return 0; fi

  echo "${FUNCNAME[0]} sources changed_recently. Reloading..."

  hxladd \
    --before --spec="#x_item+lower={{#item+rem+i_zxx+is_latn+ix_iso3166p1a2}}" \
    --before --spec="#x_item+upper={{#item+rem+i_zxx+is_latn+ix_iso3166p1a2}}" \
    "${fontem_archivum}" |
    hxladd --before --spec="#x_item+lower={{#item+rem+i_zxx+is_latn+ix_iso3166p1a3}}" |
    hxladd --before --spec="#x_item+upper={{#item+rem+i_zxx+is_latn+ix_iso3166p1a3}}" |
    hxladd --before --spec="#x_item={{#item+conceptum+codicem}}" |
    hxladd --before --spec="#x_item={{#item+conceptum+codicem}}" |
    hxlclean --lower="#x_item+lower" |
    hxlclean --upper="#x_item+upper" |
    hxlcut --include="#x_item" |
    csvformat --out-tabs --skip-lines 2 |
    sed 's/None//' | sed 's/None//' | sed 's/None//' | sed 's/None//' |
    sed 's/NONE//' | sed 's/NONE//' | sed 's/NONE//' | sed 's/NONE//' |
    sed 's/none//' | sed 's/none//' | sed 's/none//' | sed 's/none//' \
    >"${objectivum_archivum_temporarium}"

  file_update_if_necessary csv "$objectivum_archivum_temporarium" "$objectivum_archivum"
}

#######################################
# 1603_45_49__numerordinatio2hxlr: generate replace maps to UN m49.
#
# See:
#   https://github.com/HXLStandard/hxl-proxy/wiki/Replacement-maps
#   https://github.com/HXLStandard/libhxl-python/wiki/Replacement-maps
#
# Globals:
#   ROOTDIR
# Arguments:
#   [File] 1603/45/49/1603_45_49.no1.tm.hxl.csv
# Outputs:
#   [File] 1603/45/49/1603_45_49.no1.tm.hxl.csv
#######################################
1603_45_49__numerordinatio2hxlr() {
  fontem_archivum="${ROOTDIR}/1603/45/49/1603_45_49.no1.tm.hxl.csv"
  objectivum_archivum="${ROOTDIR}/1603/13/1603/45/49/1603_13_1603_45_49~1603_47_3166_1.r.hxl.csv"
  objectivum_archivum_temporarium="${ROOTDIR}/999999/0/1603_13_1603_45_49~1603_47_3166_1.r.hxl.csv"
  # objectivum_archivum_temporarium_2="${objectivum_archivum_temporarium}.t2.csv"

  # 1603/13/1603/45/49/1603_13_1603_45_49~1603_47_3166_1.r.hxl.csv

  if [ -z "$(changed_recently "$fontem_archivum")" ]; then return 0; fi

  echo "${FUNCNAME[0]} sources changed_recently. Reloading..."

  echo "#x_pattern,#x_substitution,#x_tag" >"$objectivum_archivum_temporarium"

  # echo "$fontem_archivum"

  # echo "hxlcut --include='#item+conceptum+codicem,#item+rem+i_zxx+is_latn+ix_iso3166p1a2' $fontem_archivum"

  # ISO 3166 part 1 alpha 2
  hxlcut \
    --include='#item+conceptum+codicem,#item+rem+i_zxx+is_latn+ix_iso3166p1a2' \
    "$fontem_archivum" \
    | hxlselect --query='#item+rem+i_zxx+is_latn+ix_iso3166p1a2 is not empty' \
    | hxladd --spec='#x_tag=item+conceptum+codicem+numeralem' \
    | tail -n +3  \
    >>"${objectivum_archivum_temporarium}"

  # ISO 3166 part 1 alpha 3
  hxlcut \
    --include='#item+conceptum+codicem,#item+rem+i_zxx+is_latn+ix_iso3166p1a3' \
    "$fontem_archivum" \
    | hxlselect --query='#item+rem+i_zxx+is_latn+ix_iso3166p1a3 is not empty' \
    | hxladd --spec='#x_tag=item+conceptum+codicem+numeralem' \
    | tail -n +3  \
    >>"${objectivum_archivum_temporarium}"

  # hxlselect --query='#x_substitution is not empty' 999999/0/1603_13_1603_45_49~1603_47_3166_1.r.hxl.csv

  # hxladd \
  #   --before --spec="#x_item+lower={{#item+rem+i_zxx+is_latn+ix_iso3166p1a2}}" \
  #   --before --spec="#x_item+upper={{#item+rem+i_zxx+is_latn+ix_iso3166p1a2}}" \
  #   "${fontem_archivum}" |
  #   hxladd --before --spec="#x_item+lower={{#item+rem+i_zxx+is_latn+ix_iso3166p1a3}}" |
  #   hxladd --before --spec="#x_item+upper={{#item+rem+i_zxx+is_latn+ix_iso3166p1a3}}" |
  #   hxladd --before --spec="#x_item={{#item+conceptum+codicem}}" |
  #   hxladd --before --spec="#x_item={{#item+conceptum+codicem}}" |
  #   hxlclean --lower="#x_item+lower" |
  #   hxlclean --upper="#x_item+upper" |
  #   hxlcut --include="#x_item" |
  #   csvformat --out-tabs --skip-lines 2 |
  #   sed 's/None//' | sed 's/None//' | sed 's/None//' | sed 's/None//' |
  #   sed 's/NONE//' | sed 's/NONE//' | sed 's/NONE//' | sed 's/NONE//' |
  #   sed 's/none//' | sed 's/none//' | sed 's/none//' | sed 's/none//' \
  #   >"${objectivum_archivum_temporarium}"

  file_update_if_necessary csv "$objectivum_archivum_temporarium" "$objectivum_archivum"
}

1603_45_49__external_fetch
1603_45_49__hxl2hxltm
1603_45_49__hxltm2numerordinatio
1603_45_49__numerordinatio2tsv
1603_45_49__numerordinatio2hxlr

set +x
