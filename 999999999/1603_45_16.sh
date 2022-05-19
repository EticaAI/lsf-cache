#!/bin/bash
#===============================================================================
#
#          FILE:  1603_45_16.sh
#
#         USAGE:  ./999999999/1603_45_16.sh
#                 time ./999999999/1603_45_16.sh
#
#   DESCRIPTION:  ...
#
#       OPTIONS:  ---
#
#  REQUIREMENTS:  - Bash shell (or better)
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
#      REVISION:  2021-01-10 05:19 UTC v1.1 1603.45.16.sh -> 1603_45_16.sh
#===============================================================================
# Comment next line if not want to stop on first error
set -e
# set -x

PRAEFIXUM="1603:45:16:"
REBUILD_CSV_FROM_XLSX="0" # REBUILD_CSV_FROM_XLSX="0"
DATA_UN_PCode_ZIP="https://drive.google.com/uc?export=download&id=1jRshR0Mywd_w8r6W2njUFWv7oDVLgKQi"
# Source:
# - https://data.humdata.org/dataset?ext_cod=1&res_format=XLSX
#   - https://drive.google.com/file/d/1jRshR0Mywd_w8r6W2njUFWv7oDVLgKQi/view?usp=sharing
#     - https://drive.google.com/uc?export=download&id=1jRshR0Mywd_w8r6W2njUFWv7oDVLgKQi

ROOTDIR="$(pwd)"
# shellcheck source=999999999.lib.sh
. "$ROOTDIR"/999999999/999999999.lib.sh

#######################################
# Download the XLSXs source files to 999999/1603/45/16
#
# Globals:
#   ROOTDIR
#   DATA_UN_PCode_ZIP
# Arguments:
#   None
#######################################
bootstrap_999999_1603_45_16_fetch_data() {

  echo "${FUNCNAME[0]} [$DATA_UN_PCode_ZIP] ..."
  # @TODO: implement some way to force full rebuild even if the zip is saved locally
  if [ ! -f "${ROOTDIR}/999999/1603/45/16/1603_45_16.zip" ]; then
    wget -qO- "$DATA_UN_PCode_ZIP" >"${ROOTDIR}/999999/1603/45/16/1603_45_16.zip"
    unzip -d "${ROOTDIR}/999999/1603/45/16/xlsx" -o "${ROOTDIR}/999999/1603/45/16/1603_45_16.zip"
  fi

  if [ -d "${ROOTDIR}/999999/1603/45/16/xlsx/__MACOSX" ]; then
    rm -r "${ROOTDIR}/999999/1603/45/16/xlsx/__MACOSX"
  fi
}

#######################################
# Convert the XLSXs to intermediate formats on 999999/1603/45/16
#
# Globals:
#   ROOTDIR
# Arguments:
#   None
#######################################
bootstrap_999999_1603_45_16() {
  # @see https://github.com/wireservice/csvkit/issues/1112
  # export PYTHONWARNINGS="ignore"
  # PYTHONWARNINGS="ignore"

  echo "${FUNCNAME[0]} ..."

  echo "#meta,#meta+m49,#meta+archivum,#meta+iso3,#meta+sheets+original,#meta+sheets+new" >"${ROOTDIR}"/999999/1603/45/16/1_meta-de-archivum.csv
  echo "" >"${ROOTDIR}"/999999/1603/45/16/2_meta-de-caput.txt
  echo "#meta,#meta+m49,#meta+archivum,#meta+caput,#meta+level,#meta+language+#meta+hxlhashtag" >"${ROOTDIR}"/999999/1603/45/16/2_meta-de-caput.csv

  for file_path in "${ROOTDIR}"/999999/1603/45/16/xlsx/*.xlsx; do
    ISO3166p1a3_original=$(basename --suffix=.xlsx "$file_path")
    ISO3166p1a3=$(echo "$ISO3166p1a3_original" | tr '[:lower:]' '[:upper:]')
    UNm49=$(numerordinatio_codicem_locali__1603_45_49 "$ISO3166p1a3")

    file_xlsx="${ISO3166p1a3_original}.xlsx"

    echo "  > ${file_xlsx}"

    file_xlsx_sheets=""
    file_xlsx_sheets_new=""

    for sheet_name in $(in2csv --names "$file_path"); do
      # echo "  $sheet_name"
      file_xlsx_sheets="${file_xlsx_sheets} ${sheet_name}"
      file_xlsx_sheets_new_item=$(un_pcode_sheets_norma "$ISO3166p1a3" "$sheet_name")
      file_xlsx_sheets_new="${file_xlsx_sheets_new} ${file_xlsx_sheets_new_item}"

      if [ ! -f "${ROOTDIR}/999999/1603/45/16/csv/${file_xlsx_sheets_new_item}.csv" ] || [ "${REBUILD_CSV_FROM_XLSX}" -eq "1" ]; then
        in2csv --sheet="${sheet_name}" "$file_path" >"${ROOTDIR}/999999/1603/45/16/csv/${file_xlsx_sheets_new_item}.csv"
      fi
      if [ ! -f "${ROOTDIR}/999999/1603/45/16/hxl/${file_xlsx_sheets_new_item}.hxl.csv" ] || [ "${REBUILD_CSV_FROM_XLSX}" -eq "1" ]; then
        un_pcode_hxlate_csv_file "${ROOTDIR}/999999/1603/45/16/csv/${file_xlsx_sheets_new_item}.csv" >"${ROOTDIR}/999999/1603/45/16/hxl/${file_xlsx_sheets_new_item}.hxl.csv"
      fi

      caput=$(head -n 1 "${ROOTDIR}/999999/1603/45/16/csv/${file_xlsx_sheets_new_item}.csv" | tr ',' "\n")
      echo "$caput" >>"${ROOTDIR}"/999999/1603/45/16/2_meta-de-caput.txt
      # echo "${PRAEFIXUM},$caput" >> "${ROOTDIR}"/999999/1603/45/16/meta-de-caput.csv
      echo "$caput" | while IFS= read -r line; do
        administrative_level=$(un_pcode_csvheader_administrative_level "${line}")
        name_language=$(un_pcode_rawheader_name_language "$line")
        hxlhashtag=$(un_pcode_rawhader_to_hxl "$line")
        # echo $line
        echo "${PRAEFIXUM}${UNm49},${UNm49},${file_xlsx},${line},${administrative_level},${name_language}${hxlhashtag}" >>"${ROOTDIR}"/999999/1603/45/16/2_meta-de-caput.csv
      done

    done
    file_xlsx_sheets=$(trim "$file_xlsx_sheets")
    file_xlsx_sheets_new=$(trim "$file_xlsx_sheets_new")

    # Save learned metadata
    echo "${PRAEFIXUM}${UNm49},${UNm49},${file_xlsx},${ISO3166p1a3},${file_xlsx_sheets},${file_xlsx_sheets_new}" >>"${ROOTDIR}"/999999/1603/45/16/1_meta-de-archivum.csv

  done

  sort "${ROOTDIR}"/999999/1603/45/16/2_meta-de-caput.txt | uniq >"${ROOTDIR}"/999999/1603/45/16/2.1_meta-de-caput.uniq.txt

  rm "${ROOTDIR}"/999999/1603/45/16/2_meta-de-caput.txt
}

#######################################
# Convert the XLSXs to intermediate formats on 999999/1603/45/16 using
# 999999999_7200235.py
#
# Globals:
#   ROOTDIR
# Arguments:
#   None
#######################################
bootstrap_999999_1603_45_16_neo() {
  # @see https://github.com/wireservice/csvkit/issues/1112
  # export PYTHONWARNINGS="ignore"
  # PYTHONWARNINGS="ignore"

  echo "${FUNCNAME[0]} ...2"

  echo "#meta,#meta+m49,#meta+archivum,#meta+iso3,#meta+sheets+original,#meta+sheets+new" >"${ROOTDIR}"/999999/1603/45/16/1_meta-de-archivum.csv
  echo "" >"${ROOTDIR}"/999999/1603/45/16/2_meta-de-caput.txt
  echo "#meta,#meta+m49,#meta+archivum,#meta+caput,#meta+level,#meta+language+#meta+hxlhashtag" >"${ROOTDIR}"/999999/1603/45/16/2_meta-de-caput.csv
  echo "${FUNCNAME[0]} ...2"
  for file_path in "${ROOTDIR}"/999999/1603/45/16/xlsx/*.xlsx; do
    ISO3166p1a3_original=$(basename --suffix=.xlsx "$file_path")
    ISO3166p1a3=$(echo "$ISO3166p1a3_original" | tr '[:lower:]' '[:upper:]')
    # UNm49=$(numerordinatio_codicem_locali__1603_45_49 "$ISO3166p1a3")

    file_xlsx="${ISO3166p1a3_original}.xlsx"
    cod_ab_levels=$("${ROOTDIR}/999999999/0/999999999_7200235.py" \
      --methodus=xlsx_metadata \
      --ex-metadatis=.cod_ab_level "$file_path")

    echo "  > ${file_xlsx}"

    file_xlsx_sheets=""
    file_xlsx_sheets_new=""
    echo "TODO [$ISO3166p1a3_original] [$ISO3166p1a3] [$UNm49]"
    # return 0
    # # ./999999999/0/999999999_7200235.py --methodus=xlsx_metadata --ex-metadatis=.cod_ab_level 999999/1603/45/16/xlsx/ago.xlsx
    fontem_archivum="${file_path}"
    for cod_level in $cod_ab_levels; do
      echo "  cod-ab-$ISO3166p1a3-$cod_level ..."

      objectivum_archivum_csv="${ROOTDIR}/999999/1603/45/16/csv/${ISO3166p1a3}_${cod_level}.csv"

      "${ROOTDIR}/999999999/0/999999999_7200235.py" \
        --methodus=xlsx_ad_csv \
        --ordines="$cod_level" "$file_path" > "${objectivum_archivum_csv}"
      return 0
      # continue
    done
    return 0

    for sheet_name in $(in2csv --names "$file_path"); do
      # echo "  $sheet_name"
      file_xlsx_sheets="${file_xlsx_sheets} ${sheet_name}"
      file_xlsx_sheets_new_item=$(un_pcode_sheets_norma "$ISO3166p1a3" "$sheet_name")
      file_xlsx_sheets_new="${file_xlsx_sheets_new} ${file_xlsx_sheets_new_item}"
      echo "TODO [$file_xlsx_sheets_new]"
      continue

      if [ ! -f "${ROOTDIR}/999999/1603/45/16/csv/${file_xlsx_sheets_new_item}.csv" ] || [ "${REBUILD_CSV_FROM_XLSX}" -eq "1" ]; then
        in2csv --sheet="${sheet_name}" "$file_path" >"${ROOTDIR}/999999/1603/45/16/csv/${file_xlsx_sheets_new_item}.csv"
      fi
      if [ ! -f "${ROOTDIR}/999999/1603/45/16/hxl/${file_xlsx_sheets_new_item}.hxl.csv" ] || [ "${REBUILD_CSV_FROM_XLSX}" -eq "1" ]; then
        un_pcode_hxlate_csv_file "${ROOTDIR}/999999/1603/45/16/csv/${file_xlsx_sheets_new_item}.csv" >"${ROOTDIR}/999999/1603/45/16/hxl/${file_xlsx_sheets_new_item}.hxl.csv"
      fi

      caput=$(head -n 1 "${ROOTDIR}/999999/1603/45/16/csv/${file_xlsx_sheets_new_item}.csv" | tr ',' "\n")
      echo "$caput" >>"${ROOTDIR}"/999999/1603/45/16/2_meta-de-caput.txt
      # echo "${PRAEFIXUM},$caput" >> "${ROOTDIR}"/999999/1603/45/16/meta-de-caput.csv
      echo "$caput" | while IFS= read -r line; do
        administrative_level=$(un_pcode_csvheader_administrative_level "${line}")
        name_language=$(un_pcode_rawheader_name_language "$line")
        hxlhashtag=$(un_pcode_rawhader_to_hxl "$line")
        # echo $line
        echo "${PRAEFIXUM}${UNm49},${UNm49},${file_xlsx},${line},${administrative_level},${name_language}${hxlhashtag}" >>"${ROOTDIR}"/999999/1603/45/16/2_meta-de-caput.csv
      done

    done
    file_xlsx_sheets=$(trim "$file_xlsx_sheets")
    file_xlsx_sheets_new=$(trim "$file_xlsx_sheets_new")

    # Save learned metadata
    echo "${PRAEFIXUM}${UNm49},${UNm49},${file_xlsx},${ISO3166p1a3},${file_xlsx_sheets},${file_xlsx_sheets_new}" >>"${ROOTDIR}"/999999/1603/45/16/1_meta-de-archivum.csv

  done

  sort "${ROOTDIR}"/999999/1603/45/16/2_meta-de-caput.txt | uniq >"${ROOTDIR}"/999999/1603/45/16/2.1_meta-de-caput.uniq.txt

  rm "${ROOTDIR}"/999999/1603/45/16/2_meta-de-caput.txt
}

#######################################
# Convert the XLSXs to intermediate formats on 999999/1603/45/16
#
# Globals:
#   ROOTDIR
# Arguments:
#   None
# Outputs:
#   999999/1603/45/16/3_meta-hxl-temp.tm.hxl.csv (temp)
#   999999/1603/45/16/3_meta-hxl.tm.hxl.csv
#######################################
bootstrap_999999_1603_45_16_metadata_pre_deploy() {
  # echo "TODO"

  echo "${FUNCNAME[0]}  ..."
  # About administrative civision https://en.wikipedia.org/wiki/Administrative_division

  echo "#item+conceptum+numerordinatio,#item+conceptum+codicem,#item+rem+i_zxx+is_zmth+ix_unm49,#item+rem+i_zxx+is_zmth+ix_admlevel,#meta+source" \
    >"${ROOTDIR}/999999/1603/45/16/3_meta-hxl-temp.tm.hxl.csv"

  for archivum_loci in "${ROOTDIR}"/999999/1603/45/16/hxl/*.hxl.csv; do
    archivum_rel=$(echo "$archivum_loci" | sed "s|${ROOTDIR}/||")
    archivum_nomen=$(basename --suffix=.hxl.csv "$archivum_loci")
    administrative_level=$(echo "$archivum_nomen" | tr -d -c 0-9)
    ISO3166p1a3=$(echo "$archivum_nomen" | tr -d -c "[:upper:]")
    UNm49=$(numerordinatio_codicem_locali__1603_45_49 "$ISO3166p1a3")
    numerordinatio="${PRAEFIXUM}${UNm49}:${administrative_level}"
    conceptum_codicem="${UNm49}:${administrative_level}"

    echo "  > ${archivum_nomen}"

    # echo "archivum ${numerordinatio} $ISO3166p1a3 ${administrative_level} ${archivum_rel}"
    # echo ""
    echo "${numerordinatio},${conceptum_codicem},${UNm49},${administrative_level},${archivum_rel}" \
      >>"${ROOTDIR}/999999/1603/45/16/3_meta-hxl-temp.tm.hxl.csv"
  done

  # echo "TODO delete 999999/1603/45/16/3_meta-hxl-temp.hxl.csv"

  hxlsort --tags="#item+rem+i_zxx+is_zmth+ix_unm49,#item+rem+i_zxx+is_zmth+ix_admlevel" \
    "${ROOTDIR}/999999/1603/45/16/3_meta-hxl-temp.tm.hxl.csv" \
    "${ROOTDIR}/999999/1603/45/16/3_meta-hxl.tm.hxl.csv"

  # @TODO: only do this if hxl did not removed empty header files ,,,,,,
  sed -i '1d' "${ROOTDIR}/999999/1603/45/16/3_meta-hxl.tm.hxl.csv"

  rm -f "${ROOTDIR}/999999/1603/45/16/3_meta-hxl-temp.tm.hxl.csv"
}

#######################################
# Prepare the directories
# Consumes 999999/1603/45/16/3_meta-hxl.hxl.csv
#
# Globals:
#   ROOTDIR
# Arguments:
#   None
# Outputs:
#   999999/1603/45/16/4_meta-numerordinatio.temp.txt (temp)
#   ${ROOTDIR}/1603/45/16 sub directories
#######################################
deploy_1603_45_16_prepare_directories() {
  # echo "TODO deploy_1603_45_16"

  echo "${FUNCNAME[0]} ..."

  hxlcut --include="#item+conceptum+numerordinatio" \
    "${ROOTDIR}/999999/1603/45/16/3_meta-hxl.tm.hxl.csv" \
    "${ROOTDIR}/999999/1603/45/16/4_meta-numerordinatio.temp.txt"

  sed -i '1,2d' "${ROOTDIR}/999999/1603/45/16/4_meta-numerordinatio.temp.txt"

  while IFS= read -r line; do
    if [ -n "$line" ]; then
      # echo "[[[$line]]]]"
      itemdir=$(numerordinatio_codicem_transation_separator "$line" "/")

      # Note: this will ignore last item of numerordinatio
      newodir=$(dirname "${ROOTDIR}/$itemdir")
      # newodir="llalalala"
      if [ "$newodir" = "${newodir#"${ROOTDIR}"}" ]; then
        echo "ERROR! Outside basedir!"
        # return 1
        break
      else
        # echo "TODO: check directory creation..."
        if [ ! -d "$newodir" ]; then
          echo "Creating directory: [${newodir}]"
          mkdir --parents "${newodir}"
        fi
      fi
    else
      continue
      # echo "nop $lineam"
    fi
  done <"${ROOTDIR}/999999/1603/45/16/4_meta-numerordinatio.temp.txt"

  rm -f "${ROOTDIR}/999999/1603/45/16/4_meta-numerordinatio.temp.txt"
}

#######################################
# Compile Administrative Level X of entire world
#
# Globals:
#   ROOTDIR
# Arguments:
#   administrative_level (integer, usually 0 to 6)
#   [directory] 999999/1603/45/16/hxl
# Outputs:
#   [file] 1603/45/16/999/1603_45_16_1_{{X}}.hxl.csv
#######################################
deploy_1603_45_16_global_admX() {
  administrative_level=${1}
  fontem_semitam="${ROOTDIR}/999999/1603/45/16/hxl"
  objectivum_archivum="${ROOTDIR}/1603/45/16/999/1603_45_16_1_${administrative_level}.hxl.csv"
  objectivum_archivum_temporarium="${ROOTDIR}/1603/45/16/999/1603_45_16_1_${administrative_level}.TEMP.hxl.csv"

  # if [ -z "$(changed_recently "$fontem_semitam")" ]; then return 0; fi

  echo "${FUNCNAME[0]} [$administrative_level] sources changed_recently. Reloading..."

  # echo "#item+conceptum+numerordinatio,#item+conceptum+codicem,#item+rem+i_zxx+is_zmth+ix_unm49,#item+rem+i_zxx+is_zmth+ix_admlevel" \
  #   >"${ROOTDIR}/1603/45/16/1/1603_45_16_1.no1.tm.hxl.csv"
  echo "#adm${administrative_level}+code+pcode,#date,#date+valid_on,#date+valid_to" \
    >"${objectivum_archivum_temporarium}"

  # ls "${ROOTDIR}/999999/1603/45/16/hxl"

  # find 999999/1603/45/16/hxl -name *_0.hxl.csv | hxlcut --include="#adm0+code+pcode"

  # find 999999/1603/45/16/hxl -name *_0.hxl.csv
  for archivum in "${ROOTDIR}"/999999/1603/45/16/hxl/*_"${administrative_level}".hxl.csv; do
    # echo "$archivum"
    # archivum_nomen=$(basename -- "$archivum")
    # hxlcut --include="#adm0+code+pcode,#date,#date+valid_on,#date+valid_to,#meta+archivum" \
    if [ ! -f "$archivum" ]; then
      continue
    fi
    hxlcut --include="#adm${administrative_level}+code+pcode,#date,#date+valid_on,#date+valid_to" \
      "$archivum" |
      tail -n +3 \
        >>"${objectivum_archivum_temporarium}"
  done

  # TODO: maybe create a deploy script
  if [ -f "$objectivum_archivum" ]; then
    rm "$objectivum_archivum"
  fi

  mv "${objectivum_archivum_temporarium}" "$objectivum_archivum"
}

#######################################
# Compile Administrative Level X of entire world
#
# Globals:
#   ROOTDIR
# Arguments:
#   administrative_level (integer, usually 0 to 6)
#   [directory] 999999/1603/45/16/hxl
# Outputs:
#   [file] 1603/45/16/999/1603_45_16_1_{{X}}.hxl.csv
#######################################
deploy_1603_45_16_global_admX_unicum() {
  # administrative_level=${1}
  fontem_semitam="${ROOTDIR}/999999/1603/45/16/hxl"
  objectivum_archivum="${ROOTDIR}/1603/45/16/999/1603_45_16_1_15828996298662.hxl.csv"
  objectivum_archivum_temporarium="${ROOTDIR}/1603/45/16/999/1603_45_16_1_15828996298662.TEMP.hxl.csv"

  # if [ -z "$(changed_recently "$fontem_semitam")" ]; then return 0; fi

  echo "${FUNCNAME[0]} sources changed_recently. Reloading..."

  # printf "01234\n" | ./999999999/0/2600.py --actionem-cifram
  # 15828996298662	01234

  # echo "#item+conceptum+numerordinatio,#item+conceptum+codicem,#item+rem+i_zxx+is_zmth+ix_unm49,#item+rem+i_zxx+is_zmth+ix_admlevel" \
  #   >"${ROOTDIR}/1603/45/16/1/1603_45_16_1.no1.tm.hxl.csv"
  echo "#meta+adm_level,#meta+code+pcode,#date,#date+valid_on,#date+valid_to" \
    >"${objectivum_archivum_temporarium}"

  # ls "${ROOTDIR}/999999/1603/45/16/hxl"

  # find 999999/1603/45/16/hxl -name *_0.hxl.csv | hxlcut --include="#adm0+code+pcode"

  # find 999999/1603/45/16/hxl -name *_0.hxl.csv
  # for archivum in "${ROOTDIR}"/999999/1603/45/16/hxl/*_"${administrative_level}".hxl.csv; do
  for administrative_level in {0..4..1}; do
    fontem_archivum="${ROOTDIR}/1603/45/16/999/1603_45_16_1_${administrative_level}.hxl.csv"
    # echo "$archivum"
    # archivum_nomen=$(basename -- "$archivum")
    # hxlcut --include="#adm0+code+pcode,#date,#date+valid_on,#date+valid_to,#meta+archivum" \
    if [ ! -f "$fontem_archivum" ]; then
      continue
    fi
    hxladd \
      --spec="#meta+adm_level=${administrative_level}" --before \
      "$fontem_archivum" |
      tail -n +3 \
        >>"${objectivum_archivum_temporarium}"
  done

  # TODO: maybe create a deploy script
  if [ -f "$objectivum_archivum" ]; then
    rm "$objectivum_archivum"
  fi

  mv "${objectivum_archivum_temporarium}" "$objectivum_archivum"
}
#### main ______________________________________________________________________

### From XLSX, start -----------------------------------------------------------
# bootstrap_999999_1603_45_16_fetch_data
# bootstrap_999999_1603_45_16

bootstrap_999999_1603_45_16_neo
exit 1

bootstrap_999999_1603_45_16_metadata_pre_deploy

deploy_1603_45_16_prepare_directories

deploy_1603_45_16_global_admX 0
deploy_1603_45_16_global_admX 1
deploy_1603_45_16_global_admX 2
deploy_1603_45_16_global_admX 3
# deploy_1603_45_16_global_admX 4
# deploy_1603_45_16_global_admX 5
# deploy_1603_45_16_global_admX 6

deploy_1603_45_16_global_admX_unicum

# time ./999999999/0/999999999_7200235.py --methodus=xlsx_ad_hxl --ordines=3 999999/1603/45/16/xlsx/ukr.xlsx

# ./999999999/0/999999999_7200235.py --methodus=xlsx_ad_csv --ordines=1 999999/1603/45/16/xlsx/ago.xlsx
# cat 999999/1603/45/16/csv/AGO_1.csv

#---- csv
# ./999999999/0/999999999_7200235.py --methodus=xlsx_ad_csv --ordines=0 999999/1603/45/16/xlsx/ago.xlsx > 999999/0/ago_0.csv
# csv-diff 999999/1603/45/16/csv/AGO_0.csv 999999/0/ago_0.csv

# ./999999999/0/999999999_7200235.py --methodus=xlsx_ad_csv --ordines=1 999999/1603/45/16/xlsx/ago.xlsx > 999999/0/ago_1.csv
# csv-diff 999999/1603/45/16/csv/AGO_1.csv 999999/0/ago_1.csv

# ./999999999/0/999999999_7200235.py --methodus=xlsx_ad_csv --ordines=2 999999/1603/45/16/xlsx/ago.xlsx > 999999/0/ago_2.csv
# csv-diff 999999/1603/45/16/csv/AGO_2.csv 999999/0/ago_2.csv

# ./999999999/0/999999999_7200235.py --methodus=xlsx_ad_csv --ordines=3 999999/1603/45/16/xlsx/ago.xlsx > 999999/0/ago_3.csv
# csv-diff 999999/1603/45/16/csv/AGO_3.csv 999999/0/ago_3.csv

# csv-diff 999999/1603/45/16/csv/AGO_3.csv 999999/0/ago_1.csv

# ---- hxl
# ./999999999/0/999999999_7200235.py --methodus=xlsx_ad_hxl --ordines=0 999999/1603/45/16/xlsx/ago.xlsx > 999999/0/ago_0.hxl.csv
# csv-diff 999999/1603/45/16/hxl/AGO_0.hxl.csv 999999/0/ago_0.hxl.csv

# ---- hxltm
# ./999999999/0/999999999_7200235.py --methodus=xlsx_ad_hxltm --ordines=0 999999/1603/45/16/xlsx/ago.xlsx > 999999/0/ago_0.tm.hxl.csv
# csv-diff 999999/1603/45/16/hxl/AGO_0.hxl.csv 999999/0/ago_0.tm.hxl.csv

### From XLSX, end -------------------------------------------------------------

### From CODV2API, start -------------------------------------------------------
# @see https://github.com/UGA-ITOSHumanitarianGIS/CODV2API
# @see https://apps.itos.uga.edu/CODV2API/api/v1/themes/cod-ab/locations/BRA
# @see https://beta.itos.uga.edu/CODV2API/api/v1/themes
# @see - https://gistmaps.itos.uga.edu/arcgis/rest/services/COD_External
#        - https://gistmaps.itos.uga.edu/arcgis/rest/services/COD_External/MOZ_PT/MapServer

### From CODV2API, end ---------------------------------------------------------

### From HDX, start -------------------------------------------------------
# @see https://data.humdata.org/dashboards/cod
# @see https://data.humdata.org/dataset/cod-ab-bra
# @see https://data.humdata.org/dataset/cod-ab-ukr
# @see https://data.humdata.org/dataset/cod-ab-eth
# ...
# @see https://geonode.wfp.org/

### From HDX, end --------------------------------------------------------------

### FROM OCHA Vocabularies, start ----------------------------------------------
# @see https://vocabulary.unocha.org/
# @see https://data.humdata.org/dataset/countries-and-territories
# @see https://docs.google.com/spreadsheets/d/1NjSI2LaS3SqbgYc0HdD8oIb7lofGtiHgoKKATCpwVdY/edit#gid=1088874596

set +x
