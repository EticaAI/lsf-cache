#!/bin/sh
#===============================================================================
#
#          FILE:  1603.45.16.sh
#
#         USAGE:  ./999999999/1603.45.16.sh
#
#   DESCRIPTION:  ...
#
#       OPTIONS:  ---
#
#  REQUIREMENTS:  - POSIX shell (or better)
#                 - wget
#          BUGS:  ---
#         NOTES:  ---
#        AUTHOR:  Emerson Rocha <rocha[at]ieee.org>
#       COMPANY:  EticaAI
#       LICENSE:  Public Domain dedication or Zero-Clause BSD
#                 SPDX-License-Identifier: Unlicense OR 0BSD
#       VERSION:  v1.0
#       CREATED:  2022-01-04 22:02 UTC based on scripts from github.com/EticaAI
#                                      /HXL-Data-Science-file-formats
#      REVISION:  ---
#===============================================================================
# Comment next line if not want to stop on first error
set -e
set -x

# Source:
# - https://data.humdata.org/dataset?ext_cod=1&res_format=XLSX
#   - https://drive.google.com/file/d/1jRshR0Mywd_w8r6W2njUFWv7oDVLgKQi/view?usp=sharing
#     - https://drive.google.com/uc?export=download&id=1jRshR0Mywd_w8r6W2njUFWv7oDVLgKQi


ROOTDIR="$(pwd)"
PRAEFIXUM="1603.45.16:"


#######################################
# Normalization of PCode sheets
# Globals:
#   None
# Arguments:
#   ISO3166p1a3
#   sheetname
#######################################
un_pcode_sheets_norma() {
  # $1
  # $2
  number=$(echo "$2" | tr -d -c 0-9)
  echo "$1_$number"
}

#######################################
# Trim whitespace
# Globals:
#   None
# Arguments:
#   String
#######################################
trim() {
  trimmed=$(echo "$1" | xargs echo -n)
  echo "$trimmed"
}


DATA_UN_PCode_ZIP="https://drive.google.com/uc?export=download&id=1jRshR0Mywd_w8r6W2njUFWv7oDVLgKQi"

# @TODO: implement some way to force full rebuild even if the zip is saved locally
if [ ! -f "${ROOTDIR}/999999/1603/45/16/1603.45.16.zip" ]; then
    wget -qO- "$DATA_UN_PCode_ZIP" > "${ROOTDIR}/999999/1603/45/16/1603.45.16.zip"
    unzip -d "${ROOTDIR}/999999/1603/45/16/xlsx" -o "${ROOTDIR}/999999/1603/45/16/1603.45.16.zip"
fi

if [ -d "${ROOTDIR}/999999/1603/45/16/xlsx/__MACOSX" ]; then
    rm -r "${ROOTDIR}/999999/1603/45/16/xlsx/__MACOSX"
fi

# @see https://github.com/wireservice/csvkit/issues/1112
# export PYTHONWARNINGS="ignore"
# PYTHONWARNINGS="ignore"

echo "#meta,#meta+archivum,#meta+iso3,#meta+sheets+original,#meta+sheets+new" > "${ROOTDIR}"/999999/1603/45/16/___.csv

for file_path in "${ROOTDIR}"/999999/1603/45/16/xlsx/*.xlsx; do
  ISO3166p1a3=$(basename --suffix=.xlsx "$file_path")
  file_xlsx="${ISO3166p1a3}.xlsx"

  file_xlsx_sheets=""
  file_xlsx_sheets_new=""

  for sheet_name in $(in2csv --names "$file_path"); do
    # echo "  $sheet_name"
    file_xlsx_sheets="${file_xlsx_sheets} ${sheet_name}"
    file_xlsx_sheets_new_item=$(un_pcode_sheets_norma "$ISO3166p1a3" "$sheet_name")
    file_xlsx_sheets_new="${file_xlsx_sheets_new} ${file_xlsx_sheets_new_item}"

    in2csv --sheet="${sheet_name}" "$file_path" > "${ROOTDIR}/999999/1603/45/16/csv/${file_xlsx_sheets_new_item}.csv"
  done
  file_xlsx_sheets=$(trim "$file_xlsx_sheets")
  file_xlsx_sheets_new=$(trim "$file_xlsx_sheets_new")

  # Save learned metadata
  echo "${PRAEFIXUM},${file_xlsx},${ISO3166p1a3},${file_xlsx_sheets},${file_xlsx_sheets_new}" >> "${ROOTDIR}"/999999/1603/45/16/___.csv

done

set +x