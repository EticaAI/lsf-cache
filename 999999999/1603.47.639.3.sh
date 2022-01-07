#!/bin/bash
#===============================================================================
#
#          FILE:  1603.47.639.3.sh
#
#         USAGE:  ./999999999/1603.47.639.3.sh
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
#       VERSION:  v1.0
#       CREATED:  2022-01-04 03:51 UTC based on scripts from github.com/EticaAI
#                                      /HXL-Data-Science-file-formats
#      REVISION:  ---
#===============================================================================
# Comment next line if not want to stop on first error
set -e
set -x

ROOTDIR="$(pwd)"

# Source:
# - https://iso639-3.sil.org/code_tables/download_tables
#   - https://proxy.hxlstandard.org/data/edit?tagger-match-all=on&tagger-01-header=id&tagger-01-tag=%23vocab+%2Bid+%2Bv_iso6393_3letter&tagger-02-header=part2b&tagger-02-tag=%23vocab+%2Bcode+%2Bv_iso3692_3letter+%2Bz_bibliographic&tagger-03-header=part2t&tagger-03-tag=%23vocab+%2Bcode+%2Bv_3692_3letter+%2Bz_terminology&tagger-04-header=part1&tagger-04-tag=%23vocab+%2Bcode+%2Bv_6391&tagger-05-header=scope&tagger-05-tag=%23status&tagger-06-header=language_type&tagger-06-tag=%23vocab+%2Btype&tagger-07-header=ref_name&tagger-07-tag=%23description+%2Bname+%2Bi_en&tagger-08-header=comment&tagger-08-tag=%23description+%2Bcomment+%2Bi_en&url=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F1mlc3zLkdgGRMOts36PiK2eFrMazgidKs%2Fview%3Fusp%3Dsharing&header-row=1&dest=data_view
#     - https://proxy.hxlstandard.org/data.csv?tagger-match-all=on&tagger-01-header=id&tagger-01-tag=%23vocab+%2Bid+%2Bv_iso6393_3letter&tagger-02-header=part2b&tagger-02-tag=%23vocab+%2Bcode+%2Bv_iso3692_3letter+%2Bz_bibliographic&tagger-03-header=part2t&tagger-03-tag=%23vocab+%2Bcode+%2Bv_3692_3letter+%2Bz_terminology&tagger-04-header=part1&tagger-04-tag=%23vocab+%2Bcode+%2Bv_6391&tagger-05-header=scope&tagger-05-tag=%23status&tagger-06-header=language_type&tagger-06-tag=%23vocab+%2Btype&tagger-07-header=ref_name&tagger-07-tag=%23description+%2Bname+%2Bi_en&tagger-08-header=comment&tagger-08-tag=%23description+%2Bcomment+%2Bi_en&url=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F1mlc3zLkdgGRMOts36PiK2eFrMazgidKs%2Fview%3Fusp%3Dsharing&header-row=1&dest=data_view

DATA_ISO_639_3_CSV="https://proxy.hxlstandard.org/data.csv?tagger-match-all=on&tagger-01-header=id&tagger-01-tag=%23vocab+%2Bid+%2Bv_iso6393_3letter&tagger-02-header=part2b&tagger-02-tag=%23vocab+%2Bcode+%2Bv_iso3692_3letter+%2Bz_bibliographic&tagger-03-header=part2t&tagger-03-tag=%23vocab+%2Bcode+%2Bv_3692_3letter+%2Bz_terminology&tagger-04-header=part1&tagger-04-tag=%23vocab+%2Bcode+%2Bv_6391&tagger-05-header=scope&tagger-05-tag=%23status&tagger-06-header=language_type&tagger-06-tag=%23vocab+%2Btype&tagger-07-header=ref_name&tagger-07-tag=%23description+%2Bname+%2Bi_en&tagger-08-header=comment&tagger-08-tag=%23description+%2Bcomment+%2Bi_en&url=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F1mlc3zLkdgGRMOts36PiK2eFrMazgidKs%2Fview%3Fusp%3Dsharing&header-row=1&dest=data_view"

# shellcheck source=999999999.sh
. "$ROOTDIR"/999999999/999999999.sh

#######################################
# Download external source files
#
# Globals:
#   ROOTDIR
#   DATA_ISO_639_3_CSV
# Arguments:
#   None
#######################################
bootstrap_999999_1603_47_639_3_fetch_data() {
  # TODO: implement option to rebuild even if file already on disk
  if [ ! -f "${ROOTDIR}/999999/1603/47/639/3/1603.47.639.3.hxl.csv" ]; then
      wget -qO- "$DATA_ISO_639_3_CSV" > "${ROOTDIR}/999999/1603/47/639/3/1603.47.639.3.hxl.csv"
  else
      echo "Cached: ${ROOTDIR}/999999/1603/47/639/3/1603.47.639.3.hxl.csv"
  fi
}

#######################################
# Generate the 999999/999999/1603.47.639.3.tsv
#
# Globals:
#   ROOTDIR
#   DATA_ISO_639_3_CSV
# Arguments:
#   None
# Outputs:
#   999999/999999/1603.47.639.3.tsv
#######################################
bootstrap_999999_1603_47_639_3() {
    hxladd \
        --before --spec="#x_item+lower={{#vocab+code+v_6391}}" \
        --before --spec="#x_item+upper={{#vocab+code+v_6391}}" \
        "${ROOTDIR}/999999/1603/47/639/3/1603.47.639.3.hxl.csv" \
        | hxladd --before --spec="#x_item+lower={{#vocab+code+v_3692_3letter+z_terminology}}" \
        | hxladd --before --spec="#x_item+upper={{#vocab+code+v_3692_3letter+z_terminology}}" \
        | hxladd --before --spec="#x_item+lower={{#vocab+code+v_iso3692_3letter+z_bibliographic}}" \
        | hxladd --before --spec="#x_item+upper={{#vocab+code+v_iso3692_3letter+z_bibliographic}}" \
        | hxladd --before --spec="#x_item+upper={{#vocab+id+v_iso6393_3letter}}" \
        | hxladd --before --spec="#x_item+lower={{#vocab+id+v_iso6393_3letter}}" \
        | hxlclean --lower="#x_item+lower" \
        | hxlclean --upper="#x_item+upper" \
        | hxlcut --include="#x_item" \
        | sed 's/None//' | sed 's/None//' | sed 's/None//' | sed 's/None//' \
        | sed 's/NONE//' | sed 's/NONE//' | sed 's/NONE//' | sed 's/NONE//' \
        | sed 's/none//' | sed 's/none//' | sed 's/none//' | sed 's/none//' \
        | csvformat --out-tabs --skip-lines 2 \
        > "${ROOTDIR}/999999/999999/1603.47.639.3.tsv"
}

bootstrap_999999_1603_47_639_3_fetch_data
bootstrap_999999_1603_47_639_3

set +x