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
# set -x

ROOTDIR="$(pwd)"

PRAEFIXUM="1603.45.16:"

# Source:
# - https://data.humdata.org/dataset?ext_cod=1&res_format=XLSX
#   - https://drive.google.com/file/d/1jRshR0Mywd_w8r6W2njUFWv7oDVLgKQi/view?usp=sharing
#     - https://drive.google.com/uc?export=download&id=1jRshR0Mywd_w8r6W2njUFWv7oDVLgKQi

DATA_UN_PCode_ZIP="https://drive.google.com/uc?export=download&id=1jRshR0Mywd_w8r6W2njUFWv7oDVLgKQi"

if [ ! -f "${ROOTDIR}/999999/1603/45/16/1603.45.16.zip" ]; then
    wget -qO- "$DATA_UN_PCode_ZIP" > "${ROOTDIR}/999999/1603/45/16/1603.45.16.zip"
fi

unzip -d "${ROOTDIR}/999999/1603/45/16/xlsx" -o "${ROOTDIR}/999999/1603/45/16/1603.45.16.zip"

if [ -d "${ROOTDIR}/999999/1603/45/16/xlsx/__MACOSX" ]; then
    rm -r "${ROOTDIR}/999999/1603/45/16/xlsx/__MACOSX"
fi

# https://stackoverflow.com/questions/48559356/how-to-convert-multiple-excel-sheets-to-csv-pytho

# @see https://github.com/wireservice/csvkit/issues/1112
# export PYTHONWARNINGS="ignore"
# PYTHONWARNINGS="ignore"

for file_path in "${ROOTDIR}"/999999/1603/45/16/xlsx/*.xlsx; do
  ISO3166p1a3=$(basename --suffix=.xlsx "$file_path")
#   ISO3166p1a3=$(echo "$i" | sed "s/${ROOTDIR}/999999/1603/45/16/xlsx///")
#   echo "$i"
  echo "$ISO3166p1a3"

  # files
#   PYTHONWARNINGS="ignore" in2csv --names "$file_path"
  in2csv --names "$file_path"

  for sheet_name in $(in2csv --names "$file_path"); do
    echo "  $sheet_name"
  done

done

set +x