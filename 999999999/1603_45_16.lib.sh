#!/bin/bash
#===============================================================================
#
#          FILE:  1603_45_16.lib.sh
#
#         USAGE:  Library. Source the file:
#                 . "$ROOTDIR"/999999999/1603_45_16.lib.sh
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
#                 2022-06-15 22:56 UTC v1.2 1603.45.16.sh -> 1603_45_16.lib.sh
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

__ROOTDIR="$(pwd)"
ROOTDIR="${ROOTDIR:-__ROOTDIR}"
DESTDIR="${DESTDIR:-$ROOTDIR}"
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
# Convert the XLSXs to intermediate formats on 999999/1603/45/16 using
# 999999999_7200235.py to 1603/45/16/{cod_ab_level}/
#
# @TODO: potentially use more than one source (such as IGBE data for BRA)
#        instead of direclty from OCHA
#
# Globals:
#   ROOTDIR
#
# Arguments:
#   objectivum_iso3661p1a3  If given, will restrict processing to one place)
#                           Empty will process all files on disk
#
# Outputs:
#   Convert files
#######################################
bootstrap_1603_45_16__all() {
  numerordinatio_praefixo="${1}"
  # objectivum_unm49="${1:-""}"

  # echo "${FUNCNAME[0]} ... [$objectivum_iso3661p1a3]"
  echo "${FUNCNAME[0]} ... [@TODO]"
  opus_temporibus_temporarium="${ROOTDIR}/999999/0/1603_45_16.todo.tsv"

  set -x
  "${ROOTDIR}/999999999/0/999999999_7200235.py" \
    --methodus='cod_ab_index' \
    --punctum-separato-ad-tab \
    --cum-columnis='#country+code+v_unm49,#country+code+v_iso3,#country+code+v_iso2,#meta+source+cod_ab_level,#date+created,#date+updated' \
    >"${opus_temporibus_temporarium}"
  set +x

  echo ""
  echo "  LIST HERE <${opus_temporibus_temporarium}>"
  echo ""

  # while IFS=, read -r iso3 source_url; do
  {
    # remove read -r to not skip first line
    read -r
    while IFS=$'\t' read -r -a linea; do
      unm49="${linea[0]}"
      v_iso3="${linea[1]}"
      v_iso2="${linea[2]}"
      cod_ab_level_max="${linea[3]}"
      # numerordinatio_praefixo="1603_45_16"
      echo ""
      echo "        ${linea[*]}"
      # echo "unm49 $unm49"
      # echo "v_iso3 $v_iso3"
      # echo "v_iso2 $v_iso2"

      if [ "$unm49" = "426" ]; then
        echo " 2022-05-23: we will skip LSA admin1 for now as it cannot extract"
        echo " number (it use 3-letter P-codes)"
        ## 2022-05-23: we will skip LSA admin1 for now as it cannot extract
        ## number (it use 3-letter P-codes)
        # admin1Name_en	admin1Pcode
        # Maseru	LSA
        # Butha-Buthe	LSB
        # Leribe	LSC
        # (...)
        continue
      fi

      bootstrap_1603_45_16__item_no1 "$numerordinatio_praefixo" "$unm49" "$v_iso3" "$v_iso2" "$cod_ab_level_max" "1" "0"
      bootstrap_1603_45_16__item_bcp47 "$numerordinatio_praefixo" "${unm49}" "$v_iso3" "$v_iso2" "$cod_ab_level_max" "1" "0" "5"
      bootstrap_1603_45_16__item_rdf "$numerordinatio_praefixo" "$unm49" "$v_iso3" "$v_iso2" "$cod_ab_level_max" "1" "0" "5"

      for ((i = 0; i <= cod_ab_level_max; i++)); do
        cod_level="$i"
        gh_repo_name_et_level="${numerordinatio_praefixo}_${unm49}_${cod_level}"
        __group_path=$(numerordinatio_neo_separatum "$gh_repo_name_et_level" "/")

        # archivum_no1__relative="${__group_path}/${gh_repo_name_et_level}.no1.tm.hxl.csv"
        # archivum_bcp47__relative="${__group_path}/${gh_repo_name_et_level}.no1.bcp47.csv"
        # archivum_rdf_owl__relative="${__group_path}/${gh_repo_name_et_level}.no1.owl.ttl"
        # archivum_rdf_skos__relative="${__group_path}/${gh_repo_name_et_level}.no1.skos.ttl"

        # arr__numerodinatio_cod_ab+=("${gh_repo_name_et_level}")

        # if [ "$_iso3661p1a3_lower" == "bra" ] && [ "$cod_level" == "2" ]; then
        #   echo ""
        #   echo "Skiping COD-AB-BR lvl 2"
        #   echo ""
        #   continue
        # fi
        # echo "loop $cod_level [${__group_path}/${gh_repo_name_et_level}.no1.tm.hxl.csv]"
        # echo "loop $cod_level [${gh_repo_local}/${__group_path}/${gh_repo_name_et_level}.no1.tm.hxl.csv]"

        # lsf1603_to_gh_repo_local_file "$gh_repo_name" "$archivum_no1__relative" "${ROOTDIR}"
        # lsf1603_to_gh_repo_local_file "$gh_repo_name" "$archivum_bcp47__relative" "${ROOTDIR}"
        # lsf1603_to_gh_repo_local_file "$gh_repo_name" "$archivum_rdf_owl__relative" "${ROOTDIR}"
        # lsf1603_to_gh_repo_local_file "$gh_repo_name" "$archivum_rdf_skos__relative" "${ROOTDIR}"

        _codex_meta="{\"#item+rem+i_qcc+is_zxxx+ix_n1603\": \"${gh_repo_name_et_level}\", \"#item+rem+i_mul+is_zyyy\": \"${gh_repo_name_et_level}\"}"

        # _datapackage_cod_ab_lvl="${ROOTDIR}/${__group_path}/datapackage.json"
        _datapackage_cod_ab_lvl="${__group_path}/datapackage.json"
        set -x
        # warning: this old method takes way too much time to compile
        #          360	IDN	ID	4	2020-04-08	2020-04-08
        #          (and most of this is not necessary at all, since
        #          it is trying to compile asciidoctor version)
        #          we already have better optimized ways to do it, but
        #          letting this for now (Rocha, 2022-06-30)
        # CODEX_AD_HOC_NUMERORDINATIO="$_codex_meta" \
        #   "${ROOTDIR}/999999999/0/1603_1.py" --methodus='status-quo' \
        #   --status-quo-in-datapackage \
        #   --codex-de="${gh_repo_name_et_level}" \
        #   >"${ROOTDIR}/${_datapackage_cod_ab_lvl}"
        ## Much faster alternative:
        "${ROOTDIR}/999999999/0/1603_1.py" \
          --methodus='data-apothecae-unicae' \
          --data-apothecae-ad-stdout \
          --data-apothecae-formato='datapackage' \
          --data-apothecae-ex="${gh_repo_name_et_level}" \
          >"${ROOTDIR}/${_datapackage_cod_ab_lvl}"
        set +x

        if [ "$unm49" = "104" ]; then
          echo " 2022-07-12: 104 MMR (Myanmar) on this date have letters"
          echo "             in addition to ISO 3166-1 Alha 2 prefix"
          echo "             (e.g. MM014S001 Danu vs MM014D001 Taunggyi; both"
          echo "             coerced to 14001) which may generate non-unique"
          echo "             local identifiers. Skiping for now the"
          echo "             friccionless validation"
          echo "@TODO        Eventually test it again"
          continue
        fi

        if [ "$unm49" = "834" ]; then
          echo " 2022-07-12: 834 TZA (Tanzania) on this date have letters"
          echo "             in addition to ISO 3166-1 Alha 2 prefix"
          echo "             (e.g. TZ2101041b Endokise vs TZ2101041a Mamire; both"
          echo "             coerced to 2101041) which may generate non-unique"
          echo "             local identifiers. Skiping for now the"
          echo "             friccionless validation"
          echo "@TODO        Eventually test it again"
          continue
        fi

        frictionless validate "${ROOTDIR}/${_datapackage_cod_ab_lvl}"
        # lsf1603_to_gh_repo_local_file "$gh_repo_name" "$_datapackage_cod_ab_lvl" "${ROOTDIR}"
      done

      # printf "\t%40s\n" "${tty_red} DEBUG: [Sleep 5 (@TODO disable me later)] ${tty_normal}"
      # exit 1
      # sleep 5
    done
  } <"${opus_temporibus_temporarium}"

}

#######################################
# Convert the XLSXs to intermediate formats on 999999/1603/45/16 using
# 999999999_7200235.py to 1603/45/16/{cod_ab_level}/
#
# @TODO: potentially use more than one source (such as IGBE data for BRA)
#        instead of direclty from OCHA
#
# Globals:
#   ROOTDIR
#
# Arguments:
#   est_meta_datapackage
#   est_tabulae_sqlite
#   est_tabulae_postgresql
#   est_graphicus_rdf
#
# Outputs:
#   Convert files
#######################################
bootstrap_1603_45_16__apothecae() {
  # objectivum_iso3661p1a3="${1:-""}"
  est_meta_datapackage="${1:-""}"
  est_tabulae_sqlite="${2:-""}"
  est_tabulae_postgresql="${3:-""}"
  est_graphicus_rdf="${4:-""}"
  # est_postgresql="${2:-""}"

  nomen="1603_45_16"

  # echo "${FUNCNAME[0]} ... [$objectivum_iso3661p1a3]"
  echo "${FUNCNAME[0]} ... [@TODO]"
  opus_temporibus_temporarium="${ROOTDIR}/999999/0/1603_45_16.apothecae.todo.txt"
  objectivum_archivum_datapackage="apothecae~${nomen}.datapackage.json"
  objectivum_archivum_sqlite="apothecae~${nomen}.sqlite"
  # apothecae.datapackage.json

  set -x
  "${ROOTDIR}/999999999/0/999999999_7200235.py" \
    --methodus='cod_ab_index_levels' \
    --sine-capite \
    --cum-columnis='#item+conceptum+numerordinatio' \
    >"${opus_temporibus_temporarium}"
  set +x

  ## 2022-05-23: we will skip LSA admin1 for now as it cannot extract
  ## number (it use 3-letter P-codes)
  # admin1Name_en	admin1Pcode
  # Maseru	LSA
  # Butha-Buthe	LSB
  # Leribe	LSC
  # (...)
  sed -i '/1603:45:16:426:0/d' "${opus_temporibus_temporarium}"
  sed -i '/1603:45:16:426:1/d' "${opus_temporibus_temporarium}"
  sed -i '/1603:45:16:426:2/d' "${opus_temporibus_temporarium}"

  # @TODO: next line is empty table, the exporter should not generate.
  #        This is just a quick hotfix
  sed -i '/1603:45:16:8:3/d' "${opus_temporibus_temporarium}"

  # @TODO: Tables with over 200 columns raize error with frictionless
  #        SQLAlchemy export to SQL. Need to investigate. For now
  #        avoiding loading the Brazil table with translations
  sed -i '/1603:45:16:76:2/d' "${opus_temporibus_temporarium}"

  echo ""
  echo "  LIST HERE <${opus_temporibus_temporarium}>"
  echo ""

  if [ -n "$est_meta_datapackage" ]; then
    echo " est_meta_datapackage..."
    set -x
    "${ROOTDIR}/999999999/0/1603_1.py" \
      --methodus='data-apothecae' \
      --data-apothecae-ex-archivo="${opus_temporibus_temporarium}" \
      --data-apothecae-ad="$objectivum_archivum_datapackage"
    set +x
  fi

  if [ -n "$est_tabulae_sqlite" ]; then
    echo " est_tabulae_sqlite..."
    set -x
    "${ROOTDIR}/999999999/0/1603_1.py" \
      --methodus='data-apothecae' \
      --data-apothecae-ex-archivo="${opus_temporibus_temporarium}" \
      --data-apothecae-ad="$objectivum_archivum_sqlite"
    set +x
  fi

  if [ -n "$est_tabulae_postgresql" ]; then
    echo "est_tabulae_postgresql requires specify connection"
    echo "skiping for now..."
  fi

  if [ -n "$est_graphicus_rdf" ]; then
    echo "TODO est_graphicus_rdf"
  fi

  # ./999999999/0/1603_1.py --methodus='data-apothecae' --data-apothecae-ex-archivo='999999/0/apothecae-list.txt' --data-apothecae-ad='apothecae.datapackage.json'

}

#######################################
# Convert the XLSXs to intermediate formats on 999999/1603/45/16 using
# 999999999_7200235.py to 1603/45/16/{cod_ab_level}/
#
# @TODO: potentially use more than one source (such as IGBE data for BRA)
#        instead of direclty from OCHA
#
# Globals:
#   ROOTDIR
#   DESTDIR
#
# Arguments:
#   numerordinatio_praefixo
#   unm49
#   iso3661p1a3
#   pcode_praefixo
#   cod_ab_level_max
#   est_temporarium_fontem
#   est_temporarium_objectivum
#
# Outputs:
#   Convert files
#######################################
bootstrap_1603_45_16__item_no1() {
  numerordinatio_praefixo="$1"
  unm49="${2}"
  iso3661p1a3="${3}"
  pcode_praefixo="${4}"
  cod_ab_level_max="${5}"
  est_temporarium_fontem="${6:-"1"}"
  est_temporarium_objectivum="${7:-"0"}"

  if [ "$est_temporarium_fontem" -eq "1" ]; then
    _basim_fontem="${ROOTDIR}/999999"
  else
    _basim_fontem="${ROOTDIR}"
  fi
  if [ "$est_temporarium_objectivum" -eq "1" ]; then
    _basim_objectivum="${DESTDIR}/999999"
  else
    _basim_objectivum="${DESTDIR}"
  fi

  # 1603_45_16 -> 1603/45/16
  __group_path=$(numerordinatio_neo_separatum "$numerordinatio_praefixo" "/")

  _iso3661p1a3_lower=$(echo "$iso3661p1a3" | tr '[:upper:]' '[:lower:]')

  fontem_archivum="${_basim_fontem}/1603/45/16/xlsx/${_iso3661p1a3_lower}.xlsx"
  # objectivum_archivum_basi="${_basim_objectivum}/1603/45/16/${unm49}"
  objectivum_archivum_basi="${_basim_objectivum}/${__group_path}/${unm49}"
  opus_temporibus_temporarium="${DESTDIR}/999999/0/${unm49}~lvl.tsv"

  printf "\t%40s\n" "${tty_blue}${FUNCNAME[0]} STARTED [$numerordinatio_praefixo] [$unm49] [$iso3661p1a3] [$pcode_praefixo]${tty_normal}"
  # echo "${FUNCNAME[0]} ... [$numerordinatio_praefixo] [$unm49] [$iso3661p1a3] [$pcode_praefixo]"

  # for file_path in "${ROOTDIR}"/999999/1603/45/16/xlsx/*.xlsx; do
  # ISO3166p1a3_original=$(basename --suffix=.xlsx "$file_path")
  # ISO3166p1a3=$(echo "$ISO3166p1a3_original" | tr '[:lower:]' '[:upper:]')
  # UNm49=$(numerordinatio_codicem_locali__1603_45_49 "$ISO3166p1a3")

  if [ ! -d "$objectivum_archivum_basi" ]; then
    mkdir "$objectivum_archivum_basi"
  fi

  # file_xlsx="${ISO3166p1a3_original}.xlsx"

  echo "cod_ab_levels $cod_ab_level_max"

  for ((i = 0; i <= cod_ab_level_max; i++)); do
    cod_level="$i"
    if [ "$_iso3661p1a3_lower" == "bra" ] && [ "$cod_level" == "2" ]; then
      echo ""
      echo "Skiping COD-AB-BR lvl 2"
      echo ""
      continue
    fi

    objectivum_archivum_basi_lvl="${objectivum_archivum_basi}/${cod_level}"
    # objectivum_archivum_no1="${objectivum_archivum_basi_lvl}/${numerordinatio_praefixo}_${unm49}_${cod_level}.no1.tm.hxl.csv"
    objectivum_archivum_no1="${objectivum_archivum_basi_lvl}/${numerordinatio_praefixo}_${unm49}_${cod_level}.no1.tm.hxl.csv"

    # set -x
    # rm "$objectivum_archivum_no1" || true
    # set +x
    # continue
    echo "  cod-ab-$_iso3661p1a3_lower-$cod_level [$objectivum_archivum_no1] ..."
    if [ ! -d "$objectivum_archivum_basi_lvl" ]; then
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

  done
  # return 0
  # done
  printf "\t%40s\n" "${tty_green}${FUNCNAME[0]} FINISHED OKAY ${tty_normal}"
}

#######################################
# Convert the XLSXs to intermediate formats on 999999/1603/45/16 using
# 999999999_7200235.py to 1603/45/16/{cod_ab_level}/
#
# @TODO: potentially use more than one source (such as IGBE data for BRA)
#        instead of direclty from OCHA
#
# Globals:
#   ROOTDIR
#   DESTDIR
#
# Arguments:
#   numerordinatio_praefixo
#   unm49
#   iso3661p1a3
#   pcode_praefixo
#   cod_ab_level_max
#   est_temporarium_fontem
#   est_temporarium_objectivum
#   rdf_ontologia_ordinibus     (Tip: "5" if prefix 1603_45_16, "4" if 1603_16)
#
# Outputs:
#   Convert files
#######################################
bootstrap_1603_45_16__item_bcp47() {
  numerordinatio_praefixo="$1"
  unm49="${2}"
  iso3661p1a3="${3}"
  pcode_praefixo="${4}"
  cod_ab_level_max="${5}"
  est_temporarium_fontem="${6:-"1"}"
  est_temporarium_objectivum="${7:-"0"}"
  # shellcheck disable=SC2034
  rdf_ontologia_ordinibus="${8:-"5"}"

  if [ "$est_temporarium_fontem" -eq "1" ]; then
    _basim_fontem="${ROOTDIR}/999999"
  else
    _basim_fontem="${ROOTDIR}"
  fi
  if [ "$est_temporarium_objectivum" -eq "1" ]; then
    _basim_objectivum="${DESTDIR}/999999"
  else
    _basim_objectivum="${DESTDIR}"
  fi

  # 1603_45_16 -> 1603/45/16
  __group_path=$(numerordinatio_neo_separatum "$numerordinatio_praefixo" "/")

  _iso3661p1a3_lower=$(echo "$iso3661p1a3" | tr '[:upper:]' '[:lower:]')

  fontem_archivum="${_basim_fontem}/1603/45/16/xlsx/${_iso3661p1a3_lower}.xlsx"
  # objectivum_archivum_basi="${_basim_objectivum}/1603/45/16/${unm49}"
  objectivum_archivum_basi="${_basim_objectivum}/${__group_path}/${unm49}"
  # opus_temporibus_temporarium="${ROOTDIR}/999999/0/${unm49}~lvl.tsv"
  opus_temporibus_temporarium="${DESTDIR}/999999/0/${unm49}~1.csv"
  opus_temporibus_temporarium_2="${DESTDIR}/999999/0/${unm49}~2.csv"

  printf "\t%40s\n" "${tty_blue}${FUNCNAME[0]} STARTED [$numerordinatio_praefixo] [$unm49] [$iso3661p1a3] [$pcode_praefixo]${tty_normal}"

  # echo "TODO this is just a draft. please implement me later"
  # return 0

  # for file_path in "${ROOTDIR}"/999999/1603/45/16/xlsx/*.xlsx; do
  # ISO3166p1a3_original=$(basename --suffix=.xlsx "$file_path")
  # ISO3166p1a3=$(echo "$ISO3166p1a3_original" | tr '[:lower:]' '[:upper:]')
  # UNm49=$(numerordinatio_codicem_locali__1603_45_49 "$ISO3166p1a3")

  # if [ ! -d "$objectivum_archivum_basi" ]; then
  #   mkdir "$objectivum_archivum_basi"
  # fi

  # file_xlsx="${ISO3166p1a3_original}.xlsx"

  echo "cod_ab_levels $cod_ab_level_max"

  for ((i = 0; i <= cod_ab_level_max; i++)); do
    cod_level="$i"
    if [ "$_iso3661p1a3_lower" == "bra" ] && [ "$cod_level" == "2" ]; then
      echo ""
      echo "Skiping COD-AB-BR lvl 2"
      echo ""
      continue
    fi

    objectivum_archivum_basi_lvl="${objectivum_archivum_basi}/${cod_level}"
    # objectivum_archivum_no1="${objectivum_archivum_basi_lvl}/${numerordinatio_praefixo}_${unm49}_${cod_level}.no1.tm.hxl.csv"
    objectivum_archivum_no1="${objectivum_archivum_basi_lvl}/${numerordinatio_praefixo}_${unm49}_${cod_level}.no1.tm.hxl.csv"
    objectivum_archivum_bcp47="${objectivum_archivum_basi_lvl}/${numerordinatio_praefixo}_${unm49}_${cod_level}.no1.bcp47.csv"

    # objectivum_archivum_no1_owl_ttl="${objectivum_archivum_basi_lvl}/${numerordinatio_praefixo}_${unm49}_${cod_level}.no1.owl.ttl"
    # objectivum_archivum_no1_skos_ttl="${objectivum_archivum_basi_lvl}/${numerordinatio_praefixo}_${unm49}_${cod_level}.no1.skos.ttl"

    # rm "$objectivum_archivum_no1" || true
    # set +x
    # continue
    echo "  cod-ab-$_iso3661p1a3_lower-$cod_level [$objectivum_archivum_no1] ..."
    # if [ ! -d "$objectivum_archivum_basi_lvl" ]; then
    #   mkdir "$objectivum_archivum_basi_lvl"
    # fi

    # echo "TODO"

    rdf_trivio=$((5000 + cod_level))

    set -x
    "${ROOTDIR}/999999999/0/999999999_54872.py" \
      --objectivum-formato=_temp_no1_to_no1_shortnames \
      --real-infile-path="${objectivum_archivum_no1}" >"${opus_temporibus_temporarium}"

    # Temporary fix: remove some generated tags with error: +ix_error
    # Somewhat temporary: remove non-merget alts: +ix_alt1|+ix_alt12|+ix_alt13
    # Non-temporary: remove implicit tags: +ix_hxlattrs
    hxlcut \
      --exclude='#*+ix_error,#*+ix_hxlattrs,#*+ix_alt1,#*+ix_alt2,#*+ix_alt3' \
      "${opus_temporibus_temporarium}" >"${opus_temporibus_temporarium_2}"

    # Delete first line ,,,,,
    sed -i '1d' "${opus_temporibus_temporarium_2}"

    frictionless validate "${opus_temporibus_temporarium_2}"

    "${ROOTDIR}/999999999/0/999999999_54872.py" \
      --objectivum-formato=_temp_data_hxl_to_bcp47 \
      --real-infile-path="${opus_temporibus_temporarium_2}" >"${opus_temporibus_temporarium}"

    frictionless validate "${opus_temporibus_temporarium}"

    # "${ROOTDIR}/999999999/0/999999999_54872.py" \
    #   --objectivum-formato=_temp_no1_to_no1_shortnames \
    #   --numerordinatio-cum-antecessoribus \
    #   --rdf-sine-spatia-nominalibus=skos,devnull \
    #   --rdf-ontologia-ordinibus="${rdf_ontologia_ordinibus}" \
    #   --rdf-trivio="${rdf_trivio}" \
    #   <"${objectivum_archivum_no1}" >"${opus_temporibus_temporarium}"

    set +x

    file_update_if_necessary csv "$opus_temporibus_temporarium" "$objectivum_archivum_bcp47"

    # rm "$opus_temporibus_temporarium"
    rm "$opus_temporibus_temporarium_2"

  done

  # return 0
  # done
  printf "\t%40s\n" "${tty_green}${FUNCNAME[0]} FINISHED OKAY ${tty_normal}"
}

#######################################
# Convert the XLSXs to intermediate formats on 999999/1603/45/16 using
# 999999999_7200235.py to 1603/45/16/{cod_ab_level}/
#
# @TODO: potentially use more than one source (such as IGBE data for BRA)
#        instead of direclty from OCHA
#
# Globals:
#   ROOTDIR
#   DESTDIR
#
# Arguments:
#   numerordinatio_praefixo
#   unm49
#   iso3661p1a3
#   pcode_praefixo
#   cod_ab_level_max
#   est_temporarium_fontem
#   est_temporarium_objectivum
#   rdf_ontologia_ordinibus     (Tip: "5" if prefix 1603_45_16, "4" if 1603_16)
#
# Outputs:
#   Convert files
#######################################
bootstrap_1603_45_16__item_rdf() {
  numerordinatio_praefixo="$1"
  unm49="${2}"
  iso3661p1a3="${3}"
  pcode_praefixo="${4}"
  cod_ab_level_max="${5}"
  est_temporarium_fontem="${6:-"1"}"
  est_temporarium_objectivum="${7:-"0"}"
  rdf_ontologia_ordinibus="${8:-"5"}"

  if [ "$est_temporarium_fontem" -eq "1" ]; then
    _basim_fontem="${ROOTDIR}/999999"
  else
    _basim_fontem="${ROOTDIR}"
  fi
  if [ "$est_temporarium_objectivum" -eq "1" ]; then
    _basim_objectivum="${DESTDIR}/999999"
  else
    _basim_objectivum="${DESTDIR}"
  fi

  # 1603_45_16 -> 1603/45/16
  __group_path=$(numerordinatio_neo_separatum "$numerordinatio_praefixo" "/")

  _iso3661p1a3_lower=$(echo "$iso3661p1a3" | tr '[:upper:]' '[:lower:]')

  fontem_archivum="${_basim_fontem}/1603/45/16/xlsx/${_iso3661p1a3_lower}.xlsx"
  # objectivum_archivum_basi="${_basim_objectivum}/1603/45/16/${unm49}"
  objectivum_archivum_basi="${_basim_objectivum}/${__group_path}/${unm49}"
  # opus_temporibus_temporarium="${ROOTDIR}/999999/0/${unm49}~lvl.tsv"
  opus_temporibus_temporarium="${DESTDIR}/999999/0/${unm49}~1.ttl"
  opus_temporibus_temporarium_2="${DESTDIR}/999999/0/${unm49}~2.ttl"

  printf "\t%40s\n" "${tty_blue}${FUNCNAME[0]} STARTED [$numerordinatio_praefixo] [$unm49] [$iso3661p1a3] [$pcode_praefixo]${tty_normal}"

  # for file_path in "${ROOTDIR}"/999999/1603/45/16/xlsx/*.xlsx; do
  # ISO3166p1a3_original=$(basename --suffix=.xlsx "$file_path")
  # ISO3166p1a3=$(echo "$ISO3166p1a3_original" | tr '[:lower:]' '[:upper:]')
  # UNm49=$(numerordinatio_codicem_locali__1603_45_49 "$ISO3166p1a3")

  # if [ ! -d "$objectivum_archivum_basi" ]; then
  #   mkdir "$objectivum_archivum_basi"
  # fi

  # file_xlsx="${ISO3166p1a3_original}.xlsx"

  echo "cod_ab_levels $cod_ab_level_max"

  for ((i = 0; i <= cod_ab_level_max; i++)); do
    cod_level="$i"
    if [ "$_iso3661p1a3_lower" == "bra" ] && [ "$cod_level" == "2" ]; then
      echo ""
      echo "Skiping COD-AB-BR lvl 2"
      echo ""
      continue
    fi

    objectivum_archivum_basi_lvl="${objectivum_archivum_basi}/${cod_level}"
    # objectivum_archivum_no1="${objectivum_archivum_basi_lvl}/${numerordinatio_praefixo}_${unm49}_${cod_level}.no1.tm.hxl.csv"
    objectivum_archivum_no1="${objectivum_archivum_basi_lvl}/${numerordinatio_praefixo}_${unm49}_${cod_level}.no1.tm.hxl.csv"

    objectivum_archivum_no1_owl_ttl="${objectivum_archivum_basi_lvl}/${numerordinatio_praefixo}_${unm49}_${cod_level}.no1.owl.ttl"
    objectivum_archivum_no1_skos_ttl="${objectivum_archivum_basi_lvl}/${numerordinatio_praefixo}_${unm49}_${cod_level}.no1.skos.ttl"

    # set -x
    # rm "$objectivum_archivum_no1" || true
    # set +x
    # continue
    echo "  cod-ab-$_iso3661p1a3_lower-$cod_level [$objectivum_archivum_no1] ..."
    # if [ ! -d "$objectivum_archivum_basi_lvl" ]; then
    #   mkdir "$objectivum_archivum_basi_lvl"
    # fi

    # echo "TODO"

    rdf_trivio=$((5000 + cod_level))

    ##  Computational-like RDF serialization, "OWL version" --------------------
    set -x
    # @TODO fix generation of invalid format if
    #       --rdf-sine-spatia-nominalibus=skos,devnull is enabled

    # "${ROOTDIR}/999999999/0/999999999_54872.py" \
    #   --objectivum-formato=_temp_no1 \
    #   --numerordinatio-cum-antecessoribus \
    #   --rdf-sine-spatia-nominalibus=skos,devnull \
    #   --rdf-ontologia-ordinibus="${rdf_ontologia_ordinibus}" \
    #   --rdf-trivio="${rdf_trivio}" \
    #   <"${objectivum_archivum_no1}" >"${opus_temporibus_temporarium}"

    "${ROOTDIR}/999999999/0/999999999_54872.py" \
      --objectivum-formato=_temp_no1 \
      --numerordinatio-cum-antecessoribus \
      --rdf-sine-spatia-nominalibus=devnull \
      --rdf-ontologia-ordinibus="${rdf_ontologia_ordinibus}" \
      --rdf-trivio="${rdf_trivio}" \
      <"${objectivum_archivum_no1}" >"${opus_temporibus_temporarium}"

    rapper --quiet --input=turtle --output=turtle \
      "${opus_temporibus_temporarium}" \
      >"${objectivum_archivum_no1_owl_ttl}"

    riot --validate "${objectivum_archivum_no1_owl_ttl}"

    ##  Linguistic-like RDF serialization, "SKOS version" ----------------------
    # @TODO fix invalid generation if disabling OWL with
    #        --rdf-sine-spatia-nominalibus=owl

    # "${ROOTDIR}/999999999/0/999999999_54872.py" \
    #   --objectivum-formato=_temp_no1 \
    #   --numerordinatio-cum-antecessoribus \
    #   --rdf-sine-spatia-nominalibus=owl,obo,p,geo,devnull \
    #   --rdf-ontologia-ordinibus="${rdf_ontologia_ordinibus}" \
    #   --rdf-trivio="${rdf_trivio}" \
    #   <"${objectivum_archivum_no1}" >"${opus_temporibus_temporarium_2}"

    "${ROOTDIR}/999999999/0/999999999_54872.py" \
      --objectivum-formato=_temp_no1 \
      --numerordinatio-cum-antecessoribus \
      --rdf-sine-spatia-nominalibus=obo,p,geo,devnull \
      --rdf-ontologia-ordinibus="${rdf_ontologia_ordinibus}" \
      --rdf-trivio="${rdf_trivio}" \
      <"${objectivum_archivum_no1}" >"${opus_temporibus_temporarium_2}"

    rapper --quiet --input=turtle --output=turtle \
      "${opus_temporibus_temporarium_2}" \
      >"${objectivum_archivum_no1_skos_ttl}"

    riot --validate "${objectivum_archivum_no1_skos_ttl}"
    set +x

    echo "OWL TTL: [${objectivum_archivum_no1_owl_ttl}]"
    echo "SKOS TTL: [${objectivum_archivum_no1_skos_ttl}]"

    rm "$opus_temporibus_temporarium"
    rm "$opus_temporibus_temporarium_2"

  done

  # return 0
  # done
  printf "\t%40s\n" "${tty_green}${FUNCNAME[0]} FINISHED OKAY ${tty_normal}"
}

#######################################
# Convert the XLSXs to intermediate formats on 999999/1603/45/16
# DEPRECATED use bootstrap_999999_1603_45_16_neo
#
# Globals:
#   ROOTDIR
# Arguments:
#   None
#######################################
bootstrap_999999_1603_45_16() {

  # DEPRECATED use bootstrap_999999_1603_45_16_neo
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
# @DEPRECATED
#
# Globals:
#   ROOTDIR
#
# Arguments:
#   objectivum_iso3661p1a3  If given, will restrict processing to one place)
#                           Empty will process all files on disk
#
# Outputs:
#   Convert files
#######################################
bootstrap_999999_1603_45_16_neo() {
  objectivum_iso3661p1a3="${1:-""}"
  # objectivum_unm49="${1:-""}"

  echo "${FUNCNAME[0]} ... [$objectivum_iso3661p1a3]"

  echo "NOTE: this entire function is deprecated."
  echo "  Use bootstrap_1603_45_16__item_no1 (called by bootstrap_1603_45_16__all)"
  echo "  or at least call 999999999_7200235.py with correct --pcode-praefixo="
  sleep 3
  echo "running anyway..."

  for file_path in "${ROOTDIR}"/999999/1603/45/16/xlsx/*.xlsx; do
    ISO3166p1a3_original=$(basename --suffix=.xlsx "$file_path")
    ISO3166p1a3=$(echo "$ISO3166p1a3_original" | tr '[:lower:]' '[:upper:]')
    # UNm49=$(numerordinatio_codicem_locali__1603_45_49 "$ISO3166p1a3")

    file_xlsx="${ISO3166p1a3_original}.xlsx"

    if [ -n "$objectivum_iso3661p1a3" ]; then
      echo "... [$objectivum_iso3661p1a3] [$ISO3166p1a3]"
      if [ "$objectivum_iso3661p1a3" != "$ISO3166p1a3" ]; then
        echo "Skiping [$ISO3166p1a3]"
        continue
      fi
    fi

    cod_ab_levels=$("${ROOTDIR}/999999999/0/999999999_7200235.py" \
      --methodus=xlsx_metadata \
      --ex-metadatis=.cod_ab_level "$file_path")

    echo "  > ${file_xlsx}"

    file_xlsx_sheets=""
    file_xlsx_sheets_new=""
    echo ""
    echo "${file_path}"
    # return 0
    # # ./999999999/0/999999999_7200235.py --methodus=xlsx_metadata --ex-metadatis=.cod_ab_level 999999/1603/45/16/xlsx/ago.xlsx
    fontem_archivum="${file_path}"
    for cod_level in $cod_ab_levels; do
      echo "  cod-ab-$ISO3166p1a3-$cod_level ..."

      objectivum_archivum_csv="${ROOTDIR}/999999/1603/45/16/csv/${ISO3166p1a3}_${cod_level}.csv"
      objectivum_archivum_hxl="${ROOTDIR}/999999/1603/45/16/hxl/${ISO3166p1a3}_${cod_level}.hxl.csv"
      objectivum_archivum_hxltm="${ROOTDIR}/999999/1603/45/16/hxltm/${ISO3166p1a3}_${cod_level}.tm.hxl.csv"

      set -x
      "${ROOTDIR}/999999999/0/999999999_7200235.py" \
        --methodus=xlsx_ad_csv \
        --ordines="$cod_level" "$file_path" >"${objectivum_archivum_csv}"

      "${ROOTDIR}/999999999/0/999999999_7200235.py" \
        --methodus=xlsx_ad_hxl \
        --ordines="$cod_level" "$file_path" >"${objectivum_archivum_hxl}"

      "${ROOTDIR}/999999999/0/999999999_7200235.py" \
        --methodus=xlsx_ad_hxltm \
        --ordines="$cod_level" "$file_path" >"${objectivum_archivum_hxltm}"
      set +x
      # sleep 10
      # return 0
      # continue
    done
    # return 0
  done
}

#######################################
# Convert the XLSXs to intermediate formats on 999999/1603/45/16
#
# @DEPRECATED
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

  echo "#item+conceptum+numerordinatio,#item+conceptum+codicem,#item+rem+i_qcc+is_zxxx+ix_unm49,#item+rem+i_qcc+is_zxxx+ix_admlevel,#meta+source" \
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

  hxlsort --tags="#item+rem+i_qcc+is_zxxx+ix_unm49,#item+rem+i_qcc+is_zxxx+ix_admlevel" \
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
  # fontem_semitam="${ROOTDIR}/999999/1603/45/16/hxl"
  objectivum_archivum="${ROOTDIR}/1603/45/16/999/1603_45_16_1_${administrative_level}.hxl.csv"
  objectivum_archivum_temporarium="${ROOTDIR}/1603/45/16/999/1603_45_16_1_${administrative_level}.TEMP.hxl.csv"

  # if [ -z "$(changed_recently "$fontem_semitam")" ]; then return 0; fi

  echo "${FUNCNAME[0]} [$administrative_level] sources changed_recently. Reloading..."

  # echo "#item+conceptum+numerordinatio,#item+conceptum+codicem,#item+rem+i_qcc+is_zxxx+ix_unm49,#item+rem+i_qcc+is_zxxx+ix_admlevel" \
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
  # fontem_semitam="${ROOTDIR}/999999/1603/45/16/hxl"
  objectivum_archivum="${ROOTDIR}/1603/45/16/999/1603_45_16_1_15828996298662.hxl.csv"
  objectivum_archivum_temporarium="${ROOTDIR}/1603/45/16/999/1603_45_16_1_15828996298662.TEMP.hxl.csv"

  # if [ -z "$(changed_recently "$fontem_semitam")" ]; then return 0; fi

  echo "${FUNCNAME[0]} sources changed_recently. Reloading..."

  # printf "01234\n" | ./999999999/0/2600.py --actionem-cifram
  # 15828996298662	01234

  # echo "#item+conceptum+numerordinatio,#item+conceptum+codicem,#item+rem+i_qcc+is_zxxx+ix_unm49,#item+rem+i_qcc+is_zxxx+ix_admlevel" \
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
      --rdf-ontologia-ordinibus="5" \
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

# set +x
