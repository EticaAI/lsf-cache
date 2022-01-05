#!/bin/sh
#===============================================================================
#
#          FILE:  1603.45.16.sh
#
#         USAGE:  ./999999999/1603.45.16.sh
#                 time ./999999999/1603.45.16.sh
#
#   DESCRIPTION:  ...
#
#       OPTIONS:  ---
#
#  REQUIREMENTS:  - POSIX shell (or better)
#                 - wget
#                 - csvkit (https://github.com/wireservice/csvkit)
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

PRAEFIXUM="1603.45.16:"
REBUILD_CSV_FROM_XLSX="0" # REBUILD_CSV_FROM_XLSX="0"

# Source:
# - https://data.humdata.org/dataset?ext_cod=1&res_format=XLSX
#   - https://drive.google.com/file/d/1jRshR0Mywd_w8r6W2njUFWv7oDVLgKQi/view?usp=sharing
#     - https://drive.google.com/uc?export=download&id=1jRshR0Mywd_w8r6W2njUFWv7oDVLgKQi

ROOTDIR="$(pwd)"
# shellcheck source=999999999.sh
. "$ROOTDIR"/999999999/999999999.sh


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

echo "#meta,#meta+archivum,#meta+iso3,#meta+sheets+original,#meta+sheets+new" > "${ROOTDIR}"/999999/1603/45/16/meta-de-archivum.csv
echo "" > "${ROOTDIR}"/999999/1603/45/16/meta-de-caput.txt
echo "#meta,#meta+archivum,#meta+caput,#meta+level,#meta+language+#meta+hxlhashtag" > "${ROOTDIR}"/999999/1603/45/16/meta-de-caput.csv

for file_path in "${ROOTDIR}"/999999/1603/45/16/xlsx/*.xlsx; do
  ISO3166p1a3_original=$(basename --suffix=.xlsx "$file_path")
  ISO3166p1a3=$( echo "$ISO3166p1a3_original" | tr '[:lower:]' '[:upper:]')
  file_xlsx="${ISO3166p1a3}.xlsx"

  file_xlsx_sheets=""
  file_xlsx_sheets_new=""

  for sheet_name in $(in2csv --names "$file_path"); do
    # echo "  $sheet_name"
    file_xlsx_sheets="${file_xlsx_sheets} ${sheet_name}"
    file_xlsx_sheets_new_item=$(un_pcode_sheets_norma "$ISO3166p1a3" "$sheet_name")
    file_xlsx_sheets_new="${file_xlsx_sheets_new} ${file_xlsx_sheets_new_item}"

    if [ ! -f "${ROOTDIR}/999999/1603/45/16/csv/${file_xlsx_sheets_new_item}.csv" ] || [ "${REBUILD_CSV_FROM_XLSX}" -eq "1" ]; then
        in2csv --sheet="${sheet_name}" "$file_path" > "${ROOTDIR}/999999/1603/45/16/csv/${file_xlsx_sheets_new_item}.csv"
    fi

    caput=$(head -n 1 "${ROOTDIR}/999999/1603/45/16/csv/${file_xlsx_sheets_new_item}.csv" | tr ',' "\n")
    echo "$caput" >> "${ROOTDIR}"/999999/1603/45/16/meta-de-caput.txt
    # echo "${PRAEFIXUM},$caput" >> "${ROOTDIR}"/999999/1603/45/16/meta-de-caput.csv
    echo "$caput" | while IFS= read -r line ; do
      administrative_level=$(un_pcode_csvheader_administrative_level "${line}")
      name_language=$(un_pcode_rawheader_name_language "$line")
      hxlhashtag=$(un_pcode_rawhader_to_hxl "$line")
      # echo $line
      echo "${PRAEFIXUM},${file_xlsx},${line},${administrative_level},${name_language}${hxlhashtag}" >> "${ROOTDIR}"/999999/1603/45/16/meta-de-caput.csv
    done

  done
  file_xlsx_sheets=$(trim "$file_xlsx_sheets")
  file_xlsx_sheets_new=$(trim "$file_xlsx_sheets_new")

  # Save learned metadata
  echo "${PRAEFIXUM},${file_xlsx},${ISO3166p1a3_original},${file_xlsx_sheets},${file_xlsx_sheets_new}" >> "${ROOTDIR}"/999999/1603/45/16/meta-de-archivum.csv

done

sort "${ROOTDIR}"/999999/1603/45/16/meta-de-caput.txt | uniq > "${ROOTDIR}"/999999/1603/45/16/meta-de-caput.uniq.txt

rm "${ROOTDIR}"/999999/1603/45/16/meta-de-caput.txt

set +x