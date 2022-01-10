#!/bin/bash
#===============================================================================
#
#          FILE:  1603_47_639_3.sh
#
#         USAGE:  ./999999999/1603_47_639_3.sh
#
#   DESCRIPTION:  ...
#
#       OPTIONS:  ---
#
#  REQUIREMENTS:  - Bash shell (or better)
#                 - wget
#          BUGS:  ---
#         NOTES:  ---
#        AUTHOR:  Emerson Rocha <rocha[at]ieee.org>
#       COMPANY:  EticaAI
#       LICENSE:  Public Domain dedication or Zero-Clause BSD
#                 SPDX-License-Identifier: Unlicense OR 0BSD
#       VERSION:  v1.1
#       CREATED:  2022-01-04 03:51 UTC based on scripts from github.com/EticaAI
#                                      /HXL-Data-Science-file-formats
#      REVISION:  2021-01-10 05:19 UTC v1.1 1603.47.639.3.sh -> 1603.47.639.3.sh
#===============================================================================
# Comment next line if not want to stop on first error
set -e
# set -x

ROOTDIR="$(pwd)"

# Source:
# - https://iso639-3.sil.org/code_tables/download_tables
#   - https://proxy.hxlstandard.org/data/edit?tagger-match-all=on&tagger-01-header=id&tagger-01-tag=%23vocab+%2Bid+%2Bv_iso6393_3letter&tagger-02-header=part2b&tagger-02-tag=%23vocab+%2Bcode+%2Bv_iso3692_3letter+%2Bz_bibliographic&tagger-03-header=part2t&tagger-03-tag=%23vocab+%2Bcode+%2Bv_3692_3letter+%2Bz_terminology&tagger-04-header=part1&tagger-04-tag=%23vocab+%2Bcode+%2Bv_6391&tagger-05-header=scope&tagger-05-tag=%23status&tagger-06-header=language_type&tagger-06-tag=%23vocab+%2Btype&tagger-07-header=ref_name&tagger-07-tag=%23description+%2Bname+%2Bi_en&tagger-08-header=comment&tagger-08-tag=%23description+%2Bcomment+%2Bi_en&url=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F1mlc3zLkdgGRMOts36PiK2eFrMazgidKs%2Fview%3Fusp%3Dsharing&header-row=1&dest=data_view
#     - https://proxy.hxlstandard.org/data.csv?tagger-match-all=on&tagger-01-header=id&tagger-01-tag=%23vocab+%2Bid+%2Bv_iso6393_3letter&tagger-02-header=part2b&tagger-02-tag=%23vocab+%2Bcode+%2Bv_iso3692_3letter+%2Bz_bibliographic&tagger-03-header=part2t&tagger-03-tag=%23vocab+%2Bcode+%2Bv_3692_3letter+%2Bz_terminology&tagger-04-header=part1&tagger-04-tag=%23vocab+%2Bcode+%2Bv_6391&tagger-05-header=scope&tagger-05-tag=%23status&tagger-06-header=language_type&tagger-06-tag=%23vocab+%2Btype&tagger-07-header=ref_name&tagger-07-tag=%23description+%2Bname+%2Bi_en&tagger-08-header=comment&tagger-08-tag=%23description+%2Bcomment+%2Bi_en&url=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F1mlc3zLkdgGRMOts36PiK2eFrMazgidKs%2Fview%3Fusp%3Dsharing&header-row=1&dest=data_view

DATA_ISO_639_3_TAB="https://iso639-3.sil.org/sites/iso639-3/files/downloads/iso-639-3.tab"
DATA_ISO_639_3_CSV="https://proxy.hxlstandard.org/data.csv?tagger-match-all=on&tagger-01-header=id&tagger-01-tag=%23vocab+%2Bid+%2Bv_iso6393_3letter&tagger-02-header=part2b&tagger-02-tag=%23vocab+%2Bcode+%2Bv_iso3692a3+%2Bz_bibliographic&tagger-03-header=part2t&tagger-03-tag=%23vocab+%2Bcode+%2Bv_3692_3letter+%2Bz_terminology&tagger-04-header=part1&tagger-04-tag=%23vocab+%2Bcode+%2Bv_6391&tagger-05-header=scope&tagger-05-tag=%23status&tagger-06-header=language_type&tagger-06-tag=%23vocab+%2Btype&tagger-07-header=ref_name&tagger-07-tag=%23description+%2Bname+%2Bi_en&tagger-08-header=comment&tagger-08-tag=%23description+%2Bcomment+%2Bi_en&url=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F1mlc3zLkdgGRMOts36PiK2eFrMazgidKs%2Fview%3Fusp%3Dsharing&header-row=1&dest=data_view"

# shellcheck source=999999999.lib.sh
. "$ROOTDIR"/999999999/999999999.lib.sh

#######################################
# Download external source files.
# Note: using raw tab file for now.
#
# Globals:
#   ROOTDIR
#   DATA_ISO_639_3_CSV
#   DATA_ISO_639_3_TAB
# Arguments:
#   None
#######################################
bootstrap_999999_1603_47_639_3_fetch_data_hxlated() {

  # An Non HXLated version
  if [ ! -f "${ROOTDIR}/999999/1603/47/639/3/1603_47_639_3.tab" ]; then
    wget -qO- "$DATA_ISO_639_3_TAB" >"${ROOTDIR}/999999/1603/47/639/3/1603_47_639_3.tab"
  else
    echo "Cached: ${ROOTDIR}/999999/1603/47/639/3/1603_47_639_3.hxl.csv"
  fi

  # TODO: investigage edge case very peculiar were HXLProxy may forgot
  #       a tab exactly on jrr around 65,8 KB of data.
  #      "It looks like row 2787 should actually have 8 columns, instead of 7. in line 2786."

  if [ ! -f "${ROOTDIR}/999999/1603/47/639/3/1603_47_639_3.hxl.csv" ]; then
    wget -qO- "$DATA_ISO_639_3_CSV" >"${ROOTDIR}/999999/1603/47/639/3/1603_47_639_3.hxl.csv"
  else
    echo "Cached: ${ROOTDIR}/999999/1603/47/639/3/1603_47_639_3.hxl.csv"
  fi

  is_valid=$(csvclean --dry-run "${ROOTDIR}/999999/1603/47/639/3/1603_47_639_3.hxl.csv")
  if [ "$is_valid" != "No errors." ]; then
    csvclean "${ROOTDIR}/999999/1603/47/639/3/1603_47_639_3.hxl.csv"
    if [ -f "${ROOTDIR}/999999/1603/47/639/3/1603_47_639_3.hxl_original.csv" ]; then
      rm "${ROOTDIR}/999999/1603/47/639/3/1603_47_639_3.hxl_original.csv"
    fi
    # mv "${ROOTDIR}/999999/1603/47/639/3/1603_47_639_3.hxl.csv" "${ROOTDIR}/999999/1603/47/639/3/1603_47_639_3.hxl_original.csv"
    rm "${ROOTDIR}/999999/1603/47/639/3/1603_47_639_3.hxl.csv"
    mv "${ROOTDIR}/999999/1603/47/639/3/1603_47_639_3.hxl_out.csv" "${ROOTDIR}/999999/1603/47/639/3/1603_47_639_3.hxl.csv"
  else
    echo "Cached already is valid. Ok."
  fi
}

#######################################
# Download external source files
# Note: using raw tab file for now.
#
# Globals:
#   ROOTDIR
#   DATA_ISO_639_3_CSV
#   DATA_ISO_639_3_TAB
# Arguments:
#   None
#######################################
bootstrap_999999_1603_47_639_3_fetch_data_raw() {

  # TODO: for functions that fetch data from outside,
  #       do different checking
  # if [ -z "$(changed_recently "$fontem_archivum")" ]; then return 0; fi
  # echo "${FUNCNAME[0]} sources changed_recently. Reloading..."

  # An Non HXLated version
  if [ ! -f "${ROOTDIR}/999999/1603/47/639/3/1603_47_639_3.tab" ]; then
    wget -qO- "$DATA_ISO_639_3_TAB" >"${ROOTDIR}/999999/1603/47/639/3/1603_47_639_3.tab"
  else
    echo "Cached: ${ROOTDIR}/999999/1603/47/639/3/1603_47_639_3.hxl.csv"
  fi
}

#######################################
# Generate the 999999/999999/1603_47_639_3.tsv
# DEPRECATED use bootstrap_999999_1603_47_639_3_hxl
#
# Globals:
#   ROOTDIR
#   DATA_ISO_639_3_CSV
# Arguments:
#   None
# Outputs:
#   999999/999999/1603_47_639_3.tsv
#######################################
bootstrap_999999_1603_47_639_3_old() {
  hxladd \
    --before --spec="#x_item+lower={{#vocab+code+v_6391}}" \
    --before --spec="#x_item+upper={{#vocab+code+v_6391}}" \
    "${ROOTDIR}/999999/1603/47/639/3/1603_47_639_3.hxl.csv" |
    hxladd --before --spec="#x_item+lower={{#vocab+code+v_3692_3letter+z_terminology}}" |
    hxladd --before --spec="#x_item+upper={{#vocab+code+v_3692_3letter+z_terminology}}" |
    hxladd --before --spec="#x_item+lower={{#vocab+code+v_iso3692_3letter+z_bibliographic}}" |
    hxladd --before --spec="#x_item+upper={{#vocab+code+v_iso3692_3letter+z_bibliographic}}" |
    hxladd --before --spec="#x_item+upper={{#vocab+id+v_iso6393_3letter}}" |
    hxladd --before --spec="#x_item+lower={{#vocab+id+v_iso6393_3letter}}" |
    hxlclean --lower="#x_item+lower" |
    hxlclean --upper="#x_item+upper" |
    hxlcut --include="#x_item" |
    sed 's/None//' | sed 's/None//' | sed 's/None//' | sed 's/None//' |
    sed 's/NONE//' | sed 's/NONE//' | sed 's/NONE//' | sed 's/NONE//' |
    sed 's/none//' | sed 's/none//' | sed 's/none//' | sed 's/none//' |
    csvformat --out-tabs --skip-lines 2 \
      >"${ROOTDIR}/999999/999999/1603_47_639_3.tsv"
}

#######################################
# Consumes 999999/1603/47/639/3/1603_47_639_3.tab and generate
# 999999/1603/47/639/3/1603_47_639_3.hxl.csv
#
# Globals:
#   ROOTDIR
# Arguments:
#   None
#   File: 999999/1603/47/639/3/1603_47_639_3.tab
# Outputs:
#   File: 999999/1603/47/639/3/1603_47_639_3.hxl.csv
#######################################
bootstrap_999999_1603_47_639_3_hxl() {
  fontem_archivum="${ROOTDIR}/999999/1603/47/639/3/1603_47_639_3.tab"
  temp_archivum="${ROOTDIR}/999999/999999/1603_47_639_3.TEMP.hxl.tsv"
  objectivum_archivum="${ROOTDIR}/999999/1603/47/639/3/1603_47_639_3.hxl.csv"

  if [ -z "$(changed_recently "$fontem_archivum")" ]; then return 0; fi
  echo "${FUNCNAME[0]} sources changed_recently. Reloading..."

  printf "Id\tPart2B\tPart2T\tPart1\tScope\tLanguage_Type\tRef_Name\tComment\n" >"$temp_archivum"
  printf "#vocab+id+code+v_iso639p3a3\t#vocab+code+v_iso639p2a3b\t#vocab+code+v_iso639p2a3t\t#vocab+code+v_iso639p1\t#status\t#vocab+type\t#vocab+name+i_eng+is_latn\t#description+name+i_eng+is_latn\n" \
    >>"$temp_archivum"
  {
    # This read skip first line
    read -r

    while IFS= read -r lineam; do
      echo "$lineam" >>"$temp_archivum"
    done
  } <"$fontem_archivum"
  # } < <(cat "$fontem_archivum" | tr '\t' '|')

  csvformat --delimiter="$(printf '\t')" --out-delimiter="," "$temp_archivum" >"$objectivum_archivum"
  rm "$temp_archivum"
}

#######################################
# Transform 999999/1603/47/639/3/1603_47_639_3.tab into
# 999999/999999/1603_47_639_3.tsv
#
# Globals:
#   ROOTDIR
# Arguments:
#   File: 999999/1603/47/639/3/1603_47_639_3.hxl.csv
# Outputs:
#   999999/999999/1603_45_49.tsv
#######################################
bootstrap_999999_1603_47_639_3_tsv() {
  fontem_archivum="${ROOTDIR}/999999/1603/47/639/3/1603_47_639_3.hxl.csv"
  objectivum_archivum="${ROOTDIR}/999999/999999/1603_45_49.tsv"
  objectivum_archivum_temp="${ROOTDIR}/999999/999999/1603_45_49.TEMP.tsv"

  if [ -z "$(changed_recently "$fontem_archivum")" ]; then return 0; fi

  echo "${FUNCNAME[0]} sources changed_recently. Reloading..."

  csvcut --columns "1,2,3,4" "$fontem_archivum" |
    csvformat --skip-lines=2 --out-tabs \
      >"$objectivum_archivum_temp"

  ./999999999/0/2600.py --actionem-cifram <"$objectivum_archivum_temp" >"$objectivum_archivum"

  rm "$objectivum_archivum_temp"

  # cat "$objectivum_archivum_temp" | ./999999999/0/2600.py --actionem-decifram
  # csvformat --skip-lines=2 --delimiter="$(printf '\t')" --out-tabs "$fontem_archivum" > "$objectivum_archivum_temp"

  # echo "" >"$objectivum_archivum_temp"

  # {
  #     # This read skip first line
  #     read -r
  #     # shellcheck disable=SC2002
  #     while IFS= read -r lineam; do
  #         # arr_csv+=("$line")
  #         # echo "$lineam"
  #         while IFS="|" read -r -a line_arr; do
  #             # echo "${line_arr[0]}"
  #             # echo "${line_arr[1]}"
  #             # echo "${line_arr[2]}"
  #             printf "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" "${line_arr[0]}" "${line_arr[0]^^}" "${line_arr[1]}" "${line_arr[1]^^}" "${line_arr[2]}" "${line_arr[2]^^}" "${line_arr[3]}" "${line_arr[3]^^}"
  #             # echo "${line_arr[0]}"
  #         done <<<"$lineam"
  #         # done <"$fontem_archivum"
  #     done
  # } < <(cat "$fontem_archivum" | tr '\t' '|')

}

### Note: using raw data fetch for now
# bootstrap_999999_1603_47_639_3_fetch_data_hxlated
# bootstrap_999999_1603_47_639_3_old

bootstrap_999999_1603_47_639_3_fetch_data_raw
bootstrap_999999_1603_47_639_3_hxl
bootstrap_999999_1603_47_639_3_tsv
# bootstrap_999999_1603_47_639_3

# find 999999/1603/47/639/3/1603_47_639_3.tab -mtime -1 -type f -exec ls -l {} \;
# find 999999/1603/47/639/3/1603_47_639_3.tab -name

# ls -l --time-style=long-iso find 999999/1603/47/639/3/
# find 999999/1603/47/639/3/ -mmin -60

# echo "changed_recently"
# changed_recently 999999/1603/47/639/3/ 60

set +x
