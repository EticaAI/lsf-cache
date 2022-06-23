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
#       VERSION:  v1.2
#       CREATED:  2022-01-04 22:02 UTC based on scripts from github.com/EticaAI
#                                      /HXL-Data-Science-file-formats
#      REVISION:  2021-01-10 05:19 UTC v1.1 1603.45.16.sh -> 1603_45_16.sh
#                 2022-06-15 22:56 UTC v1.2 library functions moved to
#                                      1603_45_16.lib.sh
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

echo "1603_45_16.sh"

ROOTDIR="$(pwd)"
# shellcheck source=999999999.lib.sh
. "$ROOTDIR"/999999999/999999999.lib.sh
# shellcheck source=1603_45_16.lib.sh
. "$ROOTDIR"/999999999/1603_45_16.lib.sh

#### main ______________________________________________________________________

__temp_fetch_external_indexes() {
  USER_AGENT="EticaAI/lexicographi-sine-finibus/2022.05.19 (https://meta.wikimedia.org/wiki/User:EmericusPetro; rocha@ieee.org) 1603_45_16.sh/0.1"

  echo "${FUNCNAME[0]} ..."

  curl --user-agent "$USER_AGENT" \
    "https://data.humdata.org/api/3/action/package_search?q=vocab_Topics=common+operational+dataset+-+cod" |
    jq >"${ROOTDIR}/999999/1603/45/16/unocha-hdx-cod~cached.search.json"

  curl --user-agent "$USER_AGENT" \
    "https://data.fieldmaps.io/cod.csv" \
    >"${ROOTDIR}/999999/1603/45/16/fieldmaps-cod~cached.csv"
}

__temp_index_praeparationi_1603_45_16() {

  echo "${FUNCNAME[0]} ..."

  echo "    i1603_45_49 (ix_unm49 ex ix_unm49, ix_iso3166p1a2, ix_iso3166p1a3)"
  set -x
  "${ROOTDIR}/999999999/0/999999999_7200235.py" \
    --methodus=index_praeparationi \
    --cum-columnis='#item+rem+i_qcc+is_zxxx+ix_unm49,#item+rem+i_qcc+is_zxxx+ix_iso3166p1a2,#item+rem+i_qcc+is_zxxx+ix_iso3166p1a3' \
    --index-ad-columnam='#item+rem+i_qcc+is_zxxx+ix_unm49' \
    --index-nomini="i1603_45_49" \
    1603_45_49
  set +x

  echo ""

  echo "    i1603_45_49 (ix_iso3166p1a2 ex ix_unm49, ix_iso3166p1a2, ix_iso3166p1a3)"
  set -x
  "${ROOTDIR}/999999999/0/999999999_7200235.py" \
    --methodus=index_praeparationi \
    --cum-columnis='#item+rem+i_qcc+is_zxxx+ix_unm49,#item+rem+i_qcc+is_zxxx+ix_iso3166p1a2,#item+rem+i_qcc+is_zxxx+ix_iso3166p1a3' \
    --index-ad-columnam='#item+rem+i_qcc+is_zxxx+ix_iso3166p1a2' \
    --index-nomini="i1603_45_49__iso3166p1a2" \
    1603_45_49
  set +x

  echo ""

  echo "    i1603_45_49 (iso3166p1a3 ex ix_unm49, ix_iso3166p1a2, ix_iso3166p1a3)"
  set -x
  "${ROOTDIR}/999999999/0/999999999_7200235.py" \
    --methodus=index_praeparationi \
    --cum-columnis='#item+rem+i_qcc+is_zxxx+ix_unm49,#item+rem+i_qcc+is_zxxx+ix_iso3166p1a2,#item+rem+i_qcc+is_zxxx+ix_iso3166p1a3' \
    --index-ad-columnam='#item+rem+i_qcc+is_zxxx+ix_iso3166p1a3' \
    --index-nomini="i1603_45_49__iso3166p1a3" \
    1603_45_49
  set +x

}

__temp_preprocess_external_indexes() {
  fontem_archivum="${ROOTDIR}/999999/1603/45/16/fieldmaps-cod~cached.csv"
  objectivum_archivum_q_temporarium="${ROOTDIR}/999999/0/fieldmaps-cod.hxl.csv"
  objectivum_archivum_q_temporarium_2="${ROOTDIR}/999999/0/fieldmaps-cod~2.hxl.csv"
  objectivum_archivum="${ROOTDIR}/999999/1603/45/16/1603_45_16.index.hxl.csv"

  # id,iso_3,adm0_name,adm0_name1,src_lvl,src_date,src_update,src_name,src_name1,src_lic,src_url,e_gpkg,e_shp,e_xlsx,o_gpkg,o_shp,o_xlsx
  hxlcaput_initial='#meta+id,#country+code+v_iso3,#country+name+ref,#country+name+alt,#meta+source+cod_ab_level,#date+created,#date+updated,#org+name+source,#org+name+contributor1,#meta+license,#item+source+type_ckan,#item+source+extended+type_gpkg,#item+source+extended+type_shp,#item+source+extended+type_xlsx,#item+source+type_gpkg,#item+source+type_shp,#item+source+type_xlsx'

  # hxlcaput_final="#meta+id,#country+code+v_iso3,#meta+source+cod_ab_level,#country+name+ref,#country+name+alt,#date+created,#date+updated,#org+name+source,#org+name+contributor1,#org+name+contributor2,#meta+license,#item+source+type_ckan,#item+source+type_gpkg,#item+source+type_shp,#item+source+type_xlsx"

  # hxlcaput_final="#meta+id,#country+code+v_iso3,#meta+source+cod_ab_level,#country+name+ref,#country+name+alt,#date+created,#date+updated,#org+name+source,#org+name+contributor1,#org+name+contributor2,#meta+license,#item+source+type_ckan,#item+source+type_gpkg,#item+source+type_xlsx"

  # hxlcaput_final="#item+source+type_xlsx!,#country+code+v_iso3!,#meta+id!,#meta+source+cod_ab_level!"

  echo "${FUNCNAME[0]} ... [$fontem_archivum] --> [$objectivum_archivum]"

  if [ -f "$objectivum_archivum_q_temporarium" ]; then
    rm "$objectivum_archivum_q_temporarium"
  fi
  set -x
  echo "$hxlcaput_initial" >"$objectivum_archivum_q_temporarium"
  # cat "$fontem_archivum" | tail -n +2 "$objectivum_archivum_q_temporarium"
  tail -n +2 "$fontem_archivum" >>"$objectivum_archivum_q_temporarium"

  hxladd \
    --spec="__#org+name+contributor2=Fieldmaps.io" \
    "$objectivum_archivum_q_temporarium" >"$objectivum_archivum_q_temporarium_2"

  sed -i '1d' "${objectivum_archivum_q_temporarium_2}"

  csvcut --names "$objectivum_archivum_q_temporarium_2"

  #   1: #meta+id
  #   2: #country+code+v_iso3
  #   3: #country+name+ref
  #   4: #country+name+alt
  #   5: #meta+source+cod_ab_level
  #   6: #date+created
  #   7: #date+updated
  #   8: #org+name+source
  #   9: #org+name+contributor1
  # 10: #meta+license
  # 11: #item+source+type_ckan
  # 12: #item+source+extended+type_gpkg
  # 13: #item+source+extended+type_shp
  # 14: #item+source+extended+type_xlsx
  # 15: #item+source+type_gpkg
  # 16: #item+source+type_shp
  # 17: #item+source+type_xlsx
  # 18: #org+name+contributor2

  csvcut --columns 1,2,5,6,7,17,15,11,18,9,8,10,3,4 "$objectivum_archivum_q_temporarium_2" >"$objectivum_archivum_q_temporarium"

  csvcut --names "$objectivum_archivum_q_temporarium"

  # sed -i '1d' "${objectivum_archivum_q_temporarium_2}"

  # hxladd \
  #   --spec="__#org+name+contributor2=https://fieldmaps.io/" \
  #   "$objectivum_archivum_q_temporarium" |
  #   hxlcut \
  #     --include="$hxlcaput_final" \
  #     "$objectivum_archivum_q_temporarium_2"
  #meta+id,#country+code+v_iso3,#country+name,#country+name+alt,#meta+source+level,#date+created,#date+updated,#org+name+source,#org+name+contributor1,#meta+license,#item+source,#item+source+extended+type_gpkg,#item+source+extended+type_shp,#item+source+extended+type_xlsx,#item+source+type_gpkg,#item+source+type_shp,#item+source+type_xlsx

  "${ROOTDIR}/999999999/0/999999999_7200235.py" \
    --methodus=de_hxltm_ad_hxltm \
    --adde-columnis='#country+code+v_unm49=DATA_REFERENTIBUS(i1603_45_49;#country+code+v_iso3)' \
    --adde-columnis='#country+code+v_iso2=DATA_REFERENTIBUS(i1603_45_49__iso3166p1a2;#country+code+v_iso3)' \
    --cum-ordinibus-ex-columnis='-9:#meta+id|-8:#country+code+v_unm49|-7:#country+code+v_iso3|-6:#country+code+v_iso2' \
    "$objectivum_archivum_q_temporarium" >"$objectivum_archivum_q_temporarium_2"

  set +x
  # file_update_if_necessary csv "$objectivum_archivum_q_temporarium" "$objectivum_archivum"
  # file_update_if_necessary csv "$objectivum_archivum_q_temporarium" "$objectivum_archivum"
  file_update_if_necessary csv "$objectivum_archivum_q_temporarium_2" "$objectivum_archivum"
}

__temp_preproces_quicktest_1603_16_24() {
  # echo "${FUNCNAME[0]} ..."

  # fontem_archivum="${ROOTDIR}/999999/1603/45/16/xlsx/ago.xlsx"
  # objectivum_archivum_ordo_1="${ROOTDIR}/999999/1603/16/24/1/1603_16_24_1.no1.bpc47.csv"
  # "${ROOTDIR}/999999999/0/999999999_7200235.py" \
  #   --methodus=xlsx_ad_no1bcp47 \
  #   --numerordinatio-praefixo=1603_16 \
  #   --unm49=24 \
  #   --ordines=1 \
  #   --pcode-praefixo=AO \
  #   "${fontem_archivum}" > "$objectivum_archivum_ordo_1"
  # return 0

  numerordinatio_praefixo="1603_16"
  unm49="24"
  iso3661p1a3="ago"
  pcode_praefixo="AO"
  cod_ab_level_max="3"
  est_temporarium_fontem="1"
  est_temporarium_objectivum="1"

  if [ "$est_temporarium_fontem" -eq "1" ]; then
    _basim_fontem="${ROOTDIR}/999999"
  else
    _basim_fontem="${ROOTDIR}"
  fi
  if [ "$est_temporarium_objectivum" -eq "1" ]; then
    _basim_objectivum="${ROOTDIR}/999999"
  else
    _basim_objectivum="${ROOTDIR}"
  fi

  _iso3661p1a3_lower=$(echo "$iso3661p1a3" | tr '[:upper:]' '[:lower:]')

  fontem_archivum="${_basim_fontem}/1603/45/16/xlsx/${_iso3661p1a3_lower}.xlsx"
  # objectivum_archivum_basi="${_basim_objectivum}/1603/45/16/${unm49}"
  objectivum_archivum_basi="${_basim_objectivum}/1603/16/${unm49}"
  opus_temporibus_temporarium="${ROOTDIR}/999999/0/${unm49}~lvl.tsv"

  echo "${FUNCNAME[0]} ... [$numerordinatio_praefixo] [$unm49] [$iso3661p1a3] [$pcode_praefixo]"

  ISO3166p1a3_original=$(basename --suffix=.xlsx "$file_path")
  ISO3166p1a3=$(echo "$ISO3166p1a3_original" | tr '[:lower:]' '[:upper:]')

  for ((i = 0; i <= cod_ab_level_max; i++)); do
    cod_level="$i"
    if [ "$_iso3661p1a3_lower" == "bra" ] && [ "$cod_level" == "2" ]; then
      echo ""
      echo "Skiping COD-AB-BR lvl 2"
      echo ""
      continue
    fi

    objectivum_archivum_basi_lvl="${objectivum_archivum_basi}/${cod_level}"
    objectivum_archivum_no1="${objectivum_archivum_basi_lvl}/${numerordinatio_praefixo}_${unm49}_${cod_level}.no1.tm.hxl.csv"
    objectivum_archivum_no1_owl_ttl="${objectivum_archivum_basi_lvl}/${numerordinatio_praefixo}_${unm49}_${cod_level}.no1.owl.ttl"
    # objectivum_archivum_no1bcp47="${objectivum_archivum_basi_lvl}/${numerordinatio_praefixo}_${unm49}_${cod_level}.no1.tm.hxl.csv"

    # set -x
    # rm "$objectivum_archivum_no1" || true
    # set +x
    # continue
    echo "  cod-ab-$_iso3661p1a3_lower-$cod_level [$objectivum_archivum_no1] ..."
    if [ ! -d "$objectivum_archivum_basi_lvl" ]; then
      echo "Pre-creating the directory [$objectivum_archivum_basi_lvl]"
      mkdir "$objectivum_archivum_basi_lvl"
    fi

    set -x
    "${ROOTDIR}/999999999/0/999999999_7200235.py" \
      --methodus=xlsx_ad_no1 \
      --numerordinatio-praefixo="$numerordinatio_praefixo" \
      --ordines="$cod_level" \
      --pcode-praefix="$pcode_praefixo" \
      --unm49="$unm49" \
      "$fontem_archivum" >"${objectivum_archivum_no1}"
    set +x

    frictionless validate "${objectivum_archivum_no1}" || true

    rdf_trivio=$((5000 + cod_level))

    "${ROOTDIR}/999999999/0/999999999_54872.py" \
      --objectivum-formato=_temp_no1 \
      --numerordinatio-cum-antecessoribus \
      --punctum-separato-de-fontem=',' \
      --rdf-trivio="${rdf_trivio}" \
      "${objectivum_archivum_no1}" |
      rapper --quiet --input=turtle --output=turtle /dev/fd/0 \
        >"${objectivum_archivum_no1_owl_ttl}"

    echo "OWL TTL: [${objectivum_archivum_no1_owl_ttl}]"

    # set -x
    # "${ROOTDIR}/999999999/0/999999999_7200235.py" \
    #   --methodus=xlsx_ad_no1bcp47 \
    #   --numerordinatio-praefixo="$numerordinatio_praefixo" \
    #   --ordines="$cod_level" \
    #   --pcode-praefix="$pcode_praefixo" \
    #   --unm49="$unm49" \
    #   "$fontem_archivum" >"${objectivum_archivum_no1bcp47}"
    # set +x

    # frictionless validate "${objectivum_archivum_no1bcp47}" || true

  done
}

__temp_download_external_cod_data() {
  USER_AGENT="EticaAI/lexicographi-sine-finibus/2022.05.19 (https://meta.wikimedia.org/wiki/User:EmericusPetro; rocha@ieee.org) 1603_45_16.sh/0.1"

  fontem_archivum="${ROOTDIR}/999999/1603/45/16/1603_45_16.index.hxl.csv"
  objectivum_archivum_temporarium_todo="${ROOTDIR}/999999/0/1603_45_16.todo.hxl.csv"
  objectivum_archivum_temporarium_todo_txt="${ROOTDIR}/999999/0/1603_45_16.todo.txt"
  objectivum_archivum_temporarium_todo_txt2="${ROOTDIR}/999999/0/1603_45_16.todo~2.txt"
  objectivum_archivum="${ROOTDIR}/999999/1603/45/16/1603_45_16.index.hxl.csv"
  echo "${FUNCNAME[0]} ... USER_AGENT [$USER_AGENT] "

  "${ROOTDIR}/999999999/0/999999999_7200235.py" \
    --methodus=de_hxltm_ad_hxltm \
    --cum-columnis='#meta+id,#country+code+v_unm49,#date+created,#date+updated,#item+source+type_xlsx' \
    "$fontem_archivum" |
    hxldedup --tags='#item+source+type_xlsx' \
      >"$objectivum_archivum_temporarium_todo"

  sed -i '1d' "${objectivum_archivum_temporarium_todo}"

  # echo "$objectivum_archivum_temporarium_todo"

  "${ROOTDIR}/999999999/0/999999999_7200235.py" \
    --methodus=de_hxltm_ad_hxltm \
    --cum-filtris='LOWER(#country+code+v_iso3)' \
    --cum-columnis='#country+code+v_iso3,#item+source+type_xlsx' \
    "$fontem_archivum" |
    hxldedup --tags='#item+source+type_xlsx' \
      >"$objectivum_archivum_temporarium_todo_txt"

  sed -i '1d' "${objectivum_archivum_temporarium_todo_txt}"

  sort "${objectivum_archivum_temporarium_todo_txt}" | uniq \
    >"$objectivum_archivum_temporarium_todo_txt2"

  # while IFS= read -r line; do
  while IFS=, read -r iso3 source_url; do
    # if [ -n "$iso3" ]; then
    if [[ $iso3 != \#* ]]; then

      _iso3=${iso3//[![:print:]]/}
      _source_url=${source_url//[![:print:]]/}
      objectivum_archivum="${ROOTDIR}/999999/1603/45/16/xlsx/${_iso3}.xlsx"

      echo "iso3 [${_iso3}]"
      echo ""
      echo "source_url [${_source_url}]"
      echo ""
      # echo "objectivum_archivum $objectivum_archivum"

      ls -lha "$objectivum_archivum" || true
      sleep 10
      # ls "$objectivum_archivum"
      set -x
      curl --user-agent "$USER_AGENT" \
        "$_source_url" \
        >"${objectivum_archivum}"
      set +x

      ls -lha "$objectivum_archivum" || true
      # 5 min sleep
      sleep 300
    fi
  done <"$objectivum_archivum_temporarium_todo_txt"

  # curl --user-agent "$USER_AGENT" \
  #   "https://data.humdata.org/api/3/action/package_search?q=vocab_Topics=common+operational+dataset+-+cod" |
  #   jq >"${ROOTDIR}/999999/1603/45/16/unocha-hdx-cod~cached.search.json"

}

### From XLSX, start -----------------------------------------------------------
# bootstrap_999999_1603_45_16_fetch_data
# bootstrap_999999_1603_45_16

# __temp_fetch_external_indexes
# __temp_index_praeparationi_1603_45_16
# __temp_preprocess_external_indexes
# exit 1

# @TODO manualy renamed 999999/1603/45/16/xlsx/aze.xlsx[aze_adm1]
#       from 'admin0Name_en' to 'admin0Pcode' (2022-06-12 )

# __temp_download_external_cod_data
# exit 1
# echo "all"
# bootstrap_1603_45_16__all "1603_45_16"
# bootstrap_1603_45_16__item_no1 "1603_45_16" "24" "AGO" "AO" "1" "1" "0"
# bootstrap_1603_45_16__item_rdf "1603_45_16" "24" "AGO" "AO" "3" "1" "0"
# __temp_preproces_quicktest_1603_16_24
# exit 0

# bootstrap_1603_45_16__all "1603_45_16"
# bootstrap_999999_1603_45_16_neo ""
# bootstrap_999999_1603_45_16_neo "BRA"
# bootstrap_999999_1603_45_16_neo "MOZ"
# bootstrap_1603_45_16__apothecae "1" "1" "" ""
# bootstrap_1603_45_16__apothecae "1" "" "" ""

"${ROOTDIR}/999999999/0/999999999_7200235.py" \
  --methodus='cod_ab_index_levels_ttl' \
  --punctum-separato-ad-tab \
  >"${ROOTDIR}/999999/1603/45/16/1603_45_16.index.skos.ttl"

rapper --quiet --input=turtle --output=dot \
  "${ROOTDIR}/999999/1603/45/16/1603_45_16.index.skos.ttl" \
  >"${ROOTDIR}/999999/1603/45/16/1603_45_16.index.dot"
rapper --quiet --input=turtle --output=dot \
  "${ROOTDIR}/999999/1603/45/16/1603_45_16.index.skos.ttl" \
  >"${ROOTDIR}/999999/1603/45/16/1603_45_16.index.dot"

exit 0

# ./999999999/0/1603_1.py --methodus='ontologia-simplici' --ontologia-radici=1603_1_7 --ontologia-ex-archivo=1603/1/7/1603_1_7.no1.tm.hxl.csv | rapper --quiet --input=turtle --output=turtle /dev/fd/0 > /home/fititnt/Downloads/test.ttl
# ./999999999/0/1603_1.py --methodus='ontologia-simplici' --ontologia-radici=1603_1_7 --ontologia-ex-archivo=1603/1/7/1603_1_7.no1.tm.hxl.csv | rapper --quiet --input=turtle --output=dot /dev/fd/0 > /home/fititnt/Downloads/test.dot

# dot -Tsvg \
#   "${ROOTDIR}/999999/1603/45/16/1603_45_16.index.dot" \
#   > "${ROOTDIR}/999999/1603/45/16/1603_45_16.index.svg"

# dot -Tpng \
#   "${ROOTDIR}/999999/1603/45/16/1603_45_16.index.dot" \
#   > "${ROOTDIR}/999999/1603/45/16/1603_45_16.index.png"

exit 1

echo "after here is old scripts that need to be refatored"
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

# pip3 install ckanapi
# ckanapi

# ckanapi action group_list -r https://data.humdata.org/

# ckanapi --remote=https://data.humdata.org/ action group_list

# SITE_URL=https://data.humdata.org/ ckanapi action group_list

# https://data.humdata.org/api/action/package_search?facet.field=[%22tags%22]&facet.limit=10&rows=0

# https://data.humdata.org/api/action/package_search?facet.field=[%22tags%22]&facet.limit=10&rows=0

# ckanapi -r https://data.humdata.org/ action package_search facet.field='["tags"]' facet.limit=10 rows=0

# ckanapi -r https://data.humdata.org/ action package_search facet.field='["tags"]' facet.limit=10 rows=0

# ckanapi -r https://data.humdata.org/ action package_search fq='tags:bra'

# ckanapi -r https://data.humdata.org/ action package_search facet.field:'["organization"]' rows:0

## This one somwwhat return what we need
# https://data.humdata.org/api/3/action/package_search?q=vocab_Topics=common+operational+dataset+-+cod

# https://www.npmjs.com/package/wikidata-taxonomy
# Brazil
#     wdtaxonomy Q155 -P P131 --brief
#     wdtaxonomy Q155 -P P131 --brief -s
#
#     wdtaxonomy Q16502 -P P361
#
# Countryes
#     wdtaxonomy Q6256
#
#     wdtaxonomy Q6256 -P P131
# country (Q6256) •165 ×192
# └──first-level administrative country subdivision (Q10864048) •3 ×106
#    └──second-level administrative country subdivision (Q13220204) ×2726
#       └──third-level administrative country subdivision (Q13221722) ×2922
#          ├──??? (Q10872650) •2 ↑
#          └──fourth-level administrative country subdivision (Q14757767) ×6364
#             └──fifth-level administrative country subdivision (Q15640612) ×1
#                └──sixth-level administrative country subdivision (Q22927291)
#
#     wdtaxonomy Q22927291 -P P131 -r
# sixth-level administrative country subdivision (Q22927291)
# └──fifth-level administrative country subdivision (Q15640612) ×1
#    └──fourth-level administrative country subdivision (Q14757767) ×6364
#       └──third-level administrative country subdivision (Q13221722) ×2922
#          └──second-level administrative country subdivision (Q13220204) ×2726
#             └──first-level administrative country subdivision (Q10864048) •3 ×106
#                └──country (Q6256) •165 ×192

# https://github.com/seebi/rdf.sh (also any23 https://github.com/seebi/rdf.sh/issues/8)
# /workspace/bin/rdf
# rdf desc skos:narrower
# rdf list geo:

# rapper -g 999999/0/ibge_un_adm2.no1.skos.ttl
# rapper --output dot --guess 999999/0/ibge_un_adm2.no1.skos.ttl

#### @TODO: population _________________________________________________________
# - https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/queries/examples#Countries_sorted_by_population
# - https://w.wiki/5CDt
# - https://www.wikidata.org/wiki/Property:P1082
# - https://www.wikidata.org/wiki/Property_talk:P1082
# - https://www.wikidata.org/wiki/Property:P4179
# - https://www.wikidata.org/wiki/Property:P8204
# - https://www.wikidata.org/wiki/Wikidata:Property_proposal/Historical_Population
# - https://www.wikidata.org/wiki/Property:P1539 female population
# - https://www.wikidata.org/wiki/Property:P1539 female population
# - https://www.wikidata.org/wiki/Property:P1540 male population
# - https://www.wikidata.org/wiki/Property:P6344
#   - https://www.wikidata.org/wiki/Wikidata:Property_proposal/rural_population
# - https://www.wikidata.org/wiki/Property:P6343
#   - https://www.wikidata.org/wiki/Wikidata:Property_proposal/urban_population
# - https://www.wikidata.org/wiki/Property:P1538
#   - https://www.wikidata.org/wiki/Wikidata:Property_proposal/Archive/26#P1538
# - https://www.wikidata.org/wiki/Category:Properties_with_tabular-data-datatype
# - https://www.wikidata.org/wiki/Special:ListProperties/tabular-data
# - Exemplo de população
#   - wdt:P1082 "+6747815"^^xsd:decimal ;

#### TEMP / Other tests ________________________________________________________
# ./999999999/0/999999999_7200235.py --methodus=xlsx_ad_no1 --numerordinatio-praefixo=1603_45_16_24 --ordines=0 --pcode-praefix=AO --unm49=24 999999/1603/45/16/xlsx/ago.xlsx
# ./999999999/0/999999999_7200235.py --methodus=xlsx_ad_no1 --numerordinatio-praefixo=1603_45_16_24 --ordines=0 --pcode-praefix=AO --unm49=24 999999/1603/45/16/xlsx/ago.xlsx
# ./999999999/0/999999999_7200235.py --methodus=xlsx_ad_no1 --numerordinatio-praefixo=1603_45_16_24 --ordines=3 --pcode-praefix=AO --unm49=24 999999/1603/45/16/xlsx/ago.xlsx
