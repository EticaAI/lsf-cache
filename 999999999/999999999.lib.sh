#!/bin/bash
#===============================================================================
#
#          FILE:  999999999.lib.sh
#
#         USAGE:  #import on other scripts
#                 . "$ROOTDIR"/999999999/999999999.lib.sh
#
#   DESCRIPTION:  Generic utility helper for shell
#
#       OPTIONS:  ---
#
#  REQUIREMENTS:  - Bash shell (or better)
#                 - python3 (call scripts from 999999999/0/)
#                 - s3cmd (https://github.com/s3tools/s3cmd)
#                   - pip3 install s3cmd
#
#          BUGS:  ---
#         NOTES:  ---
#        AUTHOR:  Emerson Rocha <rocha[at]ieee.org>
#       COMPANY:  EticaAI
#       LICENSE:  Public Domain dedication or Zero-Clause BSD
#                 SPDX-License-Identifier: Unlicense OR 0BSD
#       VERSION:  v2.0
#       CREATED:  2022-01-05 02:39 UTC
#      REVISION:  2021-01-10 04:30 UTC 999999999.sh -> 999999999.lib.sh; removed
#                                      allow run as executable by itself
#===============================================================================

# Quick tests
#   ./999999999/999999999.lib.sh

ROOTDIR="$(pwd)"
_S3CFG="$HOME/.config/s3cfg/s3cfg-lsf1603.ini"
S3CFG="${S3CFG:-${_S3CFG}}"

# If columns are defined (and not empty), we may remove some numbers before publishing
NUMERORDINATIO_STATUS_CONCEPTUM_MINIMAM="${NUMERORDINATIO_STATUS_CONCEPTUM_MINIMAM:-10}"
NUMERORDINATIO_STATUS_CONCEPTUM_CODICEM_MINIMAM="${NUMERORDINATIO_STATUS_CONCEPTUM_CODICEM_MINIMAM:-10}"

# FORCE_REDOWNLOAD="1" # Use if want ignore 1day local cache
# FORCE_CHANGED="1" # Use if want default 5 min change

## Directory that stores basic TSVs to allow bare minimum conversions
# These files are also generated as part of bootstrapping step
# 1603_45_49.tsv, 1603_47_639_3.tsv, 1603_47_15924.tsv,
NUMERORDINATIO_DATUM="${ROOTDIR}/999999/999999"

#######################################
# Return if a path (or a file) don't exist or if did not changed recently.
# Use case: reload functions that depend on action of older ones.
# Opposite: stale_archive
#
# Globals:
#   FORCE_CHANGED
# Arguments:
#   path_or_file
#   maximum_time (default: 5 minutes)
# Outputs:
#   1 (if need reload, Void if no reload need)
#######################################
changed_recently() {
  path_or_file="$1"
  maximum_time="${2:-5}"

  if [ -n "$FORCE_CHANGED" ]; then
    echo "1"
    return 0
  fi

  if [ -e "$path_or_file" ]; then
    changes=$(find "$path_or_file" -mmin -"$maximum_time")
    if [ -z "$changes" ]; then
      return 0
    fi
  fi
  echo "1"
}

#######################################
# Return "1" if file is too old (default 24 hours). Use case: fetch
# data from outside sources.
#
# Opposite: changed_recently
#
# About changed times with git clone, see alternatives:
#  https://stackoverflow.com/a/21735986/894546
#  https://stackoverflow.com/a/13284229/894546
#
# Globals:
#   None
# Arguments:
#   path_or_file
#   maximum_time (default: 24h)
# Outputs:
#   1 (if need reload, Void if no reload need)
#######################################
stale_archive() {
  path_or_file="$1"
  maximum_time="${2:-86400}"
  if [ -e "$path_or_file" ]; then
    # set +x
    changes=$(find "$path_or_file" -mmin +"$maximum_time")
    # echo find "$path_or_file" -mmin +"$maximum_time"
    # set -x
    if [ -z "$changes" ]; then
      return 0
    fi
  fi
  echo "1"
}

#######################################
# Return if a path (or a file) don't exist or if did not changed recently.
# Use case: reload functions that depend on action of older ones
#
# Globals:
#   None
# Arguments:
#   path_or_file
#   maximum_time (default: 5 minutes)
# Outputs:
#   1 (if need reload, Void if no reload need)
#######################################
file_update_if_necessary() {
  formatum_archivum="$1"
  fontem_archivum="$2"
  objectivum_archivum="$3"

  # echo "starting file_update_if_necessary ..."
  # echo "fontem_archivum $fontem_archivum"
  # echo "objectivum_archivum $objectivum_archivum"

  echo "${FUNCNAME[0]} ..."

  case "${formatum_archivum}" in
  csv)
    is_valid=$(csvclean --dry-run "$fontem_archivum")
    if [ "$is_valid" != "No errors." ]; then
      echo "$fontem_archivum"
      echo "$is_valid"
      return 1
    fi
    ;;
  *)
    echo "Lint not implemented for this case. Skiping"
    ;;
  esac

  # echo "middle file_update_if_necessary ..."

  if [ -f "$objectivum_archivum" ]; then
    # sha256sum "$objectivum_archivum"
    # sha256sum "$fontem_archivum"

    # if [ -s "$objectivum_archivum" ] && [ "$(cmp "$fontem_archivum" "$objectivum_archivum")" = "" ]; then
    if [ -s "$objectivum_archivum" ] && [ "$(cmp --silent "$fontem_archivum" "$objectivum_archivum")" = "" ]; then
      echo "INFO: already equal. Temporary will be discarted"
      # echo "      [$fontem_archivum]"
      # echo "      [$objectivum_archivum]"
      rm "$fontem_archivum"
    else
      echo "Not equal. Temporary will replace target file"
      rm "$objectivum_archivum"
      mv "$fontem_archivum" "$objectivum_archivum"
    fi
  else
    mv "$fontem_archivum" "$objectivum_archivum"
  fi

  # echo "done file_update_if_necessary ..."
  return 0
}

#######################################
# What relative path from an numerordinatio string?
#
# Example:
#  quod_path_de_numerordinatio 1603:1:2:3 "_"
#  # 1603_1_2_3
#  quod_path_de_numerordinatio 1603:1:2:3 ":"
#  # 1603:1:2:3
#
# Globals:
#   None
# Arguments:
#   numerordinatio
#   separatum
# Outputs:
#   relative path
#######################################
numerordinatio_neo_separatum() {
  numerordinatio="$1"
  separatum="$2"
  _part1=${numerordinatio//_/"$separatum"}
  _part2=${_part1//:/"$separatum"}

  # TODO: make it tolerate more separators
  # _part1=${numerordinatio//_/\/}
  # _part2=${_part1//:/\/}
  # echo "$numerordinatio $_part2"
  # echo "numerordinatio_neo_separatum [$numerordinatio $separatum] [$_part2]"
  echo "$_part2"
}

#######################################
# Download remote file. Only executed if local file is old. Try validate
# downloads before replacing objective files.
# Note: see file_download_1603_xlsx() for download entire xlsx at once.
#
# Globals:
#   ROOTDIR
#   FORCE_REDOWNLOAD
#   FORCE_REDOWNLOAD_REM
# Arguments:
#   iri
#   numerordinatio
#   archivum_typum (Exemplum: csv)
#   archivum_extensionem  (Exemplum: hxl.csv)
#   downloader  (Exemplum: hxltmcli, curl)
# Outputs:
#   Writes to 999999/1603/45/49/1603_45_49.hxl.csv
#######################################
file_download_if_necessary() {
  iri="$1"
  numerordinatio="$2"
  archivum_typum="$3"
  archivum_extensionem="$4"
  downloader="${5:-"hxltmcli"}"
  est_temporarium="${6:-"1"}"

  if [ "$est_temporarium" -eq "1" ]; then
    _basim="${ROOTDIR}/999999"
  else
    _basim="${ROOTDIR}"
  fi
  _path=$(numerordinatio_neo_separatum "$numerordinatio" "/")
  _nomen=$(numerordinatio_neo_separatum "$numerordinatio" "_")

  # objectivum_archivum="${ROOTDIR}/999999/1613/1613.tm.hxl.csv"
  objectivum_archivum="${_basim}/$_path/$_nomen.$archivum_extensionem"
  objectivum_archivum_temporarium="${ROOTDIR}/999999/0/$_nomen.$archivum_extensionem"

  # if [ -d "${_basim}/$_path/" ]; then
  #   echo "${_basim}/$_path/"
  # fi

  # echo "oi $_basim $_path $_nomen"
  # echo "objectivum_archivum $objectivum_archivum"
  # echo "objectivum_archivum_temporarium $objectivum_archivum_temporarium"

  # return 0

  # echo "oi22 FORCE_REDOWNLOAD_REM [${FORCE_REDOWNLOAD_REM}] numerordinatio [$numerordinatio]"
  # if [ -z "${FORCE_REDOWNLOAD_REM}" ]; then
  if [ "${FORCE_REDOWNLOAD_REM}" != "" ]; then
    # echo "testa se é igual"
    _nomen_force=$(numerordinatio_neo_separatum "${FORCE_REDOWNLOAD_REM}" "_")
    if [[ "$_nomen" == "$_nomen_force" ]]; then
      # echo "_nomen_force [$_nomen_force] [$_nomen]"
      _FORCE_REDOWNLOAD="1"
    fi
  fi

  # echo "oi2"
  # echo "$objectivum_archivum"
  # echo "$(stale_archive "$objectivum_archivum")"

  if [ -z "${FORCE_REDOWNLOAD}" ] && [ -z "${_FORCE_REDOWNLOAD}" ]; then
    if [ -z "$(stale_archive "$objectivum_archivum")" ]; then return 0; fi
  else
    echo "[ DOWNLOAD ] ${FUNCNAME[0]} forced re-download [$objectivum_archivum]"
    _FORCE_REDOWNLOAD=""
  fi

  echo "[ DOWNLOAD ] [$iri] [$objectivum_archivum]"

  if [ "$downloader" == "hxltmcli" ]; then
    hxltmcli "$iri" >"$objectivum_archivum_temporarium"
  else
    curl --compressed --silent --show-error \
      -get "$iri" \
      --output "$objectivum_archivum_temporarium"
  fi

  file_update_if_necessary "$archivum_typum" "$objectivum_archivum_temporarium" "$objectivum_archivum"
}

#######################################
# Download Google sheets to local cache
# Default stale time: 10min
#
# Globals:
#   ROOTDIR
#   DATA_1603
# Arguments:
#   est_temporarium
# Outputs:
#   Writes .xlsx
#######################################
file_download_1603_xlsx() {
  est_temporarium="${1:-"1"}"
  iri="$DATA_1603"

  if [ "$est_temporarium" -eq "1" ]; then
    _basim="${ROOTDIR}/999999"
  else
    _basim="${ROOTDIR}"
  fi

  _path=$(numerordinatio_neo_separatum "$numerordinatio" "/")
  _nomen=$(numerordinatio_neo_separatum "$numerordinatio" "_")

  objectivum_archivum="${_basim}/1603/1603.xlsx"
  objectivum_archivum_temporarium="${ROOTDIR}/999999/0/1603.xlsx"

  echo "${FUNCNAME[0]}: 10min tolerance; [$iri] -> [$objectivum_archivum]"

  if [ -f "$objectivum_archivum" ]; then
    # is_stale=$(stale_archive "$objectivum_archivum" "360")
    is_stale=$(stale_archive "$objectivum_archivum" "10")
    if [ "$is_stale" = "1" ]; then
      echo "Cache exist, but more than 5min old, Downloading again"
    else
      echo "Cache exist, but less than 5min old. Wait or delete manually:"
      echo "   $objectivum_archivum"
      return 0
    fi
  fi

  # TODO: make some quick checks to see if the temp xlsx seems okay
  wget "$iri" -O "$objectivum_archivum_temporarium"
  if [ -f "$objectivum_archivum" ]; then
    rm "$objectivum_archivum"
  fi

  mv "$objectivum_archivum_temporarium" "$objectivum_archivum"
}

#######################################
# Convert HXLTM to numerordinatio with these defaults:
# - '#meta' are removed
# - Fields with empty or zeroed concept code are excluded
# - '#status+conceptum' (if defined) less than 0 are excluded
# - '#status' are removed
#
# Globals:
#   ROOTDIR
#   NUMERORDINATIO_STATUS_CONCEPTUM_MINIMAM
#   NUMERORDINATIO_STATUS_CONCEPTUM_CODICEM_MINIMAM
# Arguments:
#   numerordinatio
#   est_temporarium_fontem (default "1", from 99999/)
#   est_temporarium_objectivumm (dfault "0", from real namespace)
# Outputs:
#   Convert files
#######################################
file_convert_csv_de_downloaded_xlsx() {
  numerordinatio="$1"
  est_temporarium_fontem="${2:-"1"}"
  est_temporarium_objectivum="${3:-"1"}"
  # opus_papyro="${4:-"10"}" # Not really necessary if using in2csv
  # (name of sheet). However it still trying to infer
  # the numbers

  _path=$(numerordinatio_neo_separatum "$numerordinatio" "/")
  _nomen=$(numerordinatio_neo_separatum "$numerordinatio" "_")
  _prefix=$(numerordinatio_neo_separatum "$numerordinatio" ":")

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

  fontem_archivum="${_basim_fontem}/1603/1603.xlsx"
  objectivum_archivum="${_basim_objectivum}/$_path/$_nomen.tm.hxl.csv"
  objectivum_archivum_temporarium_csv="${ROOTDIR}/999999/0/$_nomen.csv"
  objectivum_archivum_temporarium="${ROOTDIR}/999999/0/$_nomen.tm.hxl.csv"

  echo "${FUNCNAME[0]}: [$numerordinatio]; [$fontem_archivum] --> [$objectivum_archivum]"

  # set -x
  # hxltmcli --sheet "$opus_papyro" "$fontem_archivum" "$objectivum_archivum_temporarium"
  # hxlclean --sheet "$opus_papyro" "$fontem_archivum" "$objectivum_archivum_temporarium"
  # in2csv --format xlsx --no-inference --skip-lines 17 --sheet "$_nomen" "$fontem_archivum" > "${objectivum_archivum_temporarium_csv}"
  in2csv --format xlsx --no-inference --skip-lines 17 --sheet "$_nomen" "$fontem_archivum" >"${objectivum_archivum_temporarium_csv}"
  # issue: in2csv is adding ".0" to #item+conceptum+codicem for integers. even with --no-inference
  # set +x

  hxlselect --query="#item+conceptum+codicem>0" "${objectivum_archivum_temporarium_csv}" "$objectivum_archivum_temporarium"

  # mlr --csv cat 999999/0/1603_45_1.csv

  # sed 's/.0,/,/'  999999/0/1603_45_1.csv
  # sed 's/.0,/,/' 999999/0/1603_45_1.csv

  # hxlselect --query="#item+conceptum+codicem>0" \
  #   "${objectivum_archivum_temporarium_csv}" |
  #   hxlreplace --tags="item+conceptum+codicem" --pattern=".0" --substitution="" \
  #     >"$objectivum_archivum_temporarium"

  # TODO: remove the ".0" suffixes created by in2csv on
  #       (at least) #item+conceptum+codicem column

  # Strip empty header (already is likely to be ,,,,,,)
  # sed -i '1d' "${objectivum_archivum_temporarium}"

  # HOTFIX (MAY CANSE ISSUES):
  #      replace ".0," (maximum one per line) with "," as temporary hotfix for
  #      type inference. We need better long term solution for this.
  # sed -i 's/.0,/,/' "$objectivum_archivum_temporarium"

  file_update_if_necessary csv "$objectivum_archivum_temporarium" "$objectivum_archivum"
}

#######################################
# Convert HXLTM to numerordinatio with these defaults:
# - '#meta' are removed
# - Fields with empty or zeroed concept code are excluded
# - '#status+conceptum' (if defined) less than 0 are excluded
# - '#status' are removed
#
# Globals:
#   ROOTDIR
#   NUMERORDINATIO_STATUS_CONCEPTUM_MINIMAM
#   NUMERORDINATIO_STATUS_CONCEPTUM_CODICEM_MINIMAM
# Arguments:
#   numerordinatio
#   est_temporarium_fontem (default "1", from 99999/)
#   est_temporarium_objectivumm (dfault "0", from real namespace)
# Outputs:
#   Convert files
#######################################
file_convert_numerordinatio_de_hxltm() {
  numerordinatio="$1"
  est_temporarium_fontem="${2:-"1"}"
  est_temporarium_objectivum="${3:-"0"}"

  _path=$(numerordinatio_neo_separatum "$numerordinatio" "/")
  _nomen=$(numerordinatio_neo_separatum "$numerordinatio" "_")
  _prefix=$(numerordinatio_neo_separatum "$numerordinatio" ":")

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

  fontem_archivum="${_basim_fontem}/$_path/$_nomen.tm.hxl.csv"
  objectivum_archivum="${_basim_objectivum}/$_path/$_nomen.no1.tm.hxl.csv"
  objectivum_archivum_temporarium="${ROOTDIR}/999999/0/$_nomen.no1.tm.hxl.csv"

  # echo "$fontem_archivum"

  # if [ -z "$(changed_recently "$fontem_archivum")" ]; then return 0; fi
  # echo "${FUNCNAME[0]} sources changed_recently. Reloading..."

  if [ ! -e "$objectivum_archivum" ]; then
    echo "${FUNCNAME[0]} objective not exist. Reloading... [$objectivum_archivum]"
  elif [ -z "$(changed_recently "$fontem_archivum")" ]; then
    # echo "${FUNCNAME[0]} objective exist, sources not changed recently"
    return 0
  else
    echo "${FUNCNAME[0]} sources changed_recently. Reloading... [$fontem_archivum]"
  fi

  # @TODO: implement NUMERORDINATIO_STATUS_CONCEPTUM_CODICEM_MINIMAM
  #        instead of hardcode 1|2|3|4|5|6|7|8|9

  hxlcut --exclude="#meta" \
    "$fontem_archivum" |
    hxlselect --query="#item+conceptum+codicem>0" |
    hxlselect --query='#status+conceptum+codicem~^(1|2|3|4|5|6|7|8|9)$' --reverse |
    hxladd --before --spec="#item+conceptum+numerordinatio=${_prefix}:{{#item+conceptum+codicem}}" |
    hxlreplace --map="${ROOTDIR}/1603/13/1603_13.r.hxl.csv" \
      >"$objectivum_archivum_temporarium"

  #     hxlcut --exclude="#status" |
  # hxlselect --query='#status+conceptum!~(-1|-2|-3|-4|-5|-6|-7|-8|-9)' |
  # hxlselect --query="#status+conceptum!=" --query="#status+conceptum<0" --reverse |

  #| hxlreplace --tags="#item+conceptum+numerordinatio" --pattern="_" --substitution=":" \
  # hxlselect --query="#status+conceptum!=" --query="#status+conceptum<0" --reverse |
  # hxlreplace --map="1603/13/1603_13.r.hxl.csv" 999999/999999/2020/4/1/1603_45_1.no1.tm.hxl.csv

  # cp "$fontem_archivum" "$objectivum_archivum_temporarium"

  # Strip empty header (already is likely to be ,,,,,,)
  sed -i '1d' "${objectivum_archivum_temporarium}"

  file_update_if_necessary csv "$objectivum_archivum_temporarium" "$objectivum_archivum"
}

#######################################
# Convert a "full" .no11.tm.hxl.csv to .no11.xml
#
# Globals:
#   ROOTDIR
# Arguments:
#   numerordinatio
# Outputs:
#   Convert files
#######################################
file_convert_xml_de_numerordinatio11() {
  numerordinatio="$1"

  _path=$(numerordinatio_neo_separatum "$numerordinatio" "/")
  _nomen=$(numerordinatio_neo_separatum "$numerordinatio" "_")
  _prefix=$(numerordinatio_neo_separatum "$numerordinatio" ":")

  _basim_fontem="${ROOTDIR}"
  _basim_objectivum="${ROOTDIR}"
  tmeta="${ROOTDIR}/999999999/0/hxltm-exemplum.tmeta.yml"

  fontem_archivum="${_basim_fontem}/$_path/$_nomen.no11.tm.hxl.csv"
  objectivum_archivum="${_basim_objectivum}/$_path/$_nomen.no11.xml"
  # objectivum_archivum_temporarium="${ROOTDIR}/999999/0/$_nomen.no1.tm.hxl.csv"

  echo "${FUNCNAME[0]}: hxltmcli --tmeta-archivum $tmeta --objectivum-XML [$fontem_archivum]"
  hxltmcli --tmeta-archivum "$tmeta" --objectivum-XML "$fontem_archivum" "$objectivum_archivum"
}

#######################################
# Convert a "full" .no11.tm.hxl.csv to .no11.tbx
#
# Globals:
#   ROOTDIR
# Arguments:
#   numerordinatio
# Outputs:
#   Convert files
#######################################
file_convert_tbx_de_numerordinatio11() {
  numerordinatio="$1"

  _path=$(numerordinatio_neo_separatum "$numerordinatio" "/")
  _nomen=$(numerordinatio_neo_separatum "$numerordinatio" "_")
  _prefix=$(numerordinatio_neo_separatum "$numerordinatio" ":")

  _basim_fontem="${ROOTDIR}"
  _basim_objectivum="${ROOTDIR}"

  fontem_archivum="${_basim_fontem}/$_path/$_nomen.no11.tm.hxl.csv"
  objectivum_archivum="${_basim_objectivum}/$_path/$_nomen.no11.tbx"
  tmeta="${ROOTDIR}/999999999/0/hxltm-exemplum.tmeta.yml"
  # objectivum_archivum_temporarium="${ROOTDIR}/999999/0/$_nomen.no1.tm.hxl.csv"

  echo "${FUNCNAME[0]}: hxltmcli --tmeta-archivum $tmeta --objectivum-TBX-Basim $fontem_archivum $objectivum_archivum"
  hxltmcli --tmeta-archivum "$tmeta" --objectivum-TBX-Basim "$fontem_archivum" "$objectivum_archivum"
}

#######################################
# Convert a "full" .no11.tm.hxl.csv to .no11.tmx
#
# Globals:
#   ROOTDIR
# Arguments:
#   numerordinatio
# Outputs:
#   Convert files
#######################################
file_convert_tmx_de_numerordinatio11() {
  numerordinatio="$1"

  _path=$(numerordinatio_neo_separatum "$numerordinatio" "/")
  _nomen=$(numerordinatio_neo_separatum "$numerordinatio" "_")
  _prefix=$(numerordinatio_neo_separatum "$numerordinatio" ":")

  _basim_fontem="${ROOTDIR}"
  _basim_objectivum="${ROOTDIR}"

  fontem_archivum="${_basim_fontem}/$_path/$_nomen.no11.tm.hxl.csv"
  objectivum_archivum="${_basim_objectivum}/$_path/$_nomen.no11.tmx"
  # objectivum_archivum_temporarium="${ROOTDIR}/999999/0/$_nomen.no1.tm.hxl.csv"
  tmeta="${ROOTDIR}/999999999/0/hxltm-exemplum.tmeta.yml"

  echo "${FUNCNAME[0]}: hxltmcli --tmeta-archivum $tmeta --objectivum-TMX [$fontem_archivum]"
  hxltmcli --tmeta-archivum "$tmeta" --objectivum-TMX "$fontem_archivum" "$objectivum_archivum"
}

#######################################
# Create a codex (documentation) from an Numerordinatio standard file
#
# Globals:
#   ROOTDIR
# Arguments:
#   numerordinatio
#   est_temporarium_fontem (default "1", from 99999/)
#   est_temporarium_objectivumm (default "0", from real namespace)
#   est_objectivum_linguam
#   est_auxilium_linguam
# Outputs:
#   Create documentation
#######################################
neo_codex_de_numerordinatio() {
  numerordinatio="$1"
  est_temporarium_fontem="${2:-"1"}"
  est_temporarium_objectivum="${3:-"0"}"
  # est_objectivum_linguam="${4:-"mul-Zyyy"}"
  est_objectivum_linguam="${4:-"mul-Latn"}"
  est_auxilium_linguam="${5:-"lat-Latn,por-Latn,eng-Latn"}"

  _path=$(numerordinatio_neo_separatum "$numerordinatio" "/")
  _nomen=$(numerordinatio_neo_separatum "$numerordinatio" "_")
  _prefix=$(numerordinatio_neo_separatum "$numerordinatio" ":")

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

  fontem_archivum="${_basim_fontem}/$_path/$_nomen.no1.tm.hxl.csv"
  objectivum_archivum="${_basim_objectivum}/$_path/$_nomen.$est_objectivum_linguam.codex.adoc"
  # objectivum_archivum_temporarium="${ROOTDIR}/999999/0/$_nomen.no1.tm.hxl.csv"

  # echo "$fontem_archivum"

  # if [ -z "$(changed_recently "$fontem_archivum")" ]; then return 0; fi
  # echo "${FUNCNAME[0]} sources changed_recently. Reloading..."

  # if [ ! -e "$objectivum_archivum" ]; then
  #   echo "${FUNCNAME[0]} objective not exist. Reloading... [$objectivum_archivum]"
  # elif [ -z "$(changed_recently "$fontem_archivum")" ]; then
  #   # echo "${FUNCNAME[0]} objective exist, sources not changed recently"
  #   return 0
  # else
  #   echo "${FUNCNAME[0]} sources changed_recently. Reloading... [$fontem_archivum]"
  # fi

  echo "${FUNCNAME[0]} [$objectivum_archivum]"

  "${ROOTDIR}/999999999/0/1603_1.py" \
    --objectivum-linguam="$est_objectivum_linguam" \
    --auxilium-linguam="$est_auxilium_linguam" \
    --codex-de "$_nomen" \
    >"$objectivum_archivum"
}

#######################################
# Create a book cover from a numerordinatio
# Trivia:
# - cōdex, s, m, Nom., https://en.wiktionary.org/wiki/codex#Latin
# - copertae, s, f, dativus, https://en.wiktionary.org/wiki/coperta#Latin
#
# Globals:
#   ROOTDIR
# Arguments:
#   numerordinatio
#   est_temporarium_fontem (default "1", from 99999/)
#   est_temporarium_objectivumm (default "0", from real namespace)
#   est_objectivum_linguam
#   est_auxilium_linguam
# Outputs:
#   Create documentation
#######################################
neo_codex_copertae_de_numerordinatio() {
  numerordinatio="$1"
  est_temporarium_fontem="${2:-"1"}"
  est_temporarium_objectivum="${3:-"0"}"
  # est_objectivum_linguam="${4:-"mul-Zyyy"}"
  est_objectivum_linguam="${4:-"mul-Latn"}"
  est_auxilium_linguam="${5:-"lat-Latn,por-Latn,eng-Latn"}"

  _path=$(numerordinatio_neo_separatum "$numerordinatio" "/")
  _nomen=$(numerordinatio_neo_separatum "$numerordinatio" "_")
  _prefix=$(numerordinatio_neo_separatum "$numerordinatio" ":")
  # https://kindlegen.s3.amazonaws.com/AmazonKindlePublishingGuidelines.pdf

  ## Specific vendors
  # https://ebookflightdeck.com/handbook/coverimage
  # https://kdp.amazon.com/en_US/help/topic/G200645690
  # https://kdp.amazon.com/en_US/cover-templates
  # https://stackoverflow.com/questions/26971169/add-cover-page-with-asciidoctor

  ## Specific online guides
  # https://www.youtube.com/watch?v=zcK_tl8mLCo
  # https://blog.reedsy.com/book-cover-dimensions/

  echo "${FUNCNAME[0]} [$numerordinatio]"

  fontem_archivum="${ROOTDIR}/999999999/0/codex_copertae.svg"
  objectivum_archivum="${ROOTDIR}/$_path/$_nomen.$est_objectivum_linguam.codex.svg"
  objectivum_archivum_temporarium="${ROOTDIR}/999999/0/$_nomen.$est_objectivum_linguam.codex.svg"

  if [ -f "$objectivum_archivum" ]; then
    rm "$objectivum_archivum"
  fi

  # cp "$fontem_archivum" "$objectivum_archivum_temporarium"

  # sed -i "s|{{codex_numero}}|${_prefix}|" "$objectivum_archivum_temporarium"

  # # TODO: replace at least the name name the book

  # mv "$objectivum_archivum_temporarium" "$objectivum_archivum"

  # rm "$objectivum_archivum_temporarium"

  # "${ROOTDIR}/999999999/0/1603_1.py" --codex-de 1603_25_1 --codex-copertae

  "${ROOTDIR}/999999999/0/1603_1.py" \
    --objectivum-linguam="$est_objectivum_linguam" \
    --auxilium-linguam="$est_auxilium_linguam" \
    --codex-de "$_nomen" \
    --codex-copertae \
    >"$objectivum_archivum"

  # echo "${FUNCNAME[0]} [$objectivum_archivum]"
  # echo "@TODO this is a draft"

  # rm "$objectivum_archivum_temporarium"
}

#######################################
# From an .codex.adoc, create an epub file
#
# Globals:
#   ROOTDIR
# Arguments:
#   numerordinatio
#   est_temporarium_fontem (default "1", from 99999/)
#   est_temporarium_objectivumm (default "0", from real namespace)
#   est_objectivum_linguam
#   est_auxilium_linguam
# Outputs:
#   Create documentation
#######################################
neo_codex_de_numerordinatio_epub() {
  numerordinatio="$1"
  est_temporarium_fontem="${2:-"1"}"
  est_temporarium_objectivum="${3:-"0"}"
  # est_objectivum_linguam="${4:-"mul-Zyyy"}"
  est_objectivum_linguam="${4:-"mul-Latn"}"
  est_auxilium_linguam="${5:-"lat-Latn,por-Latn,eng-Latn"}"

  _path=$(numerordinatio_neo_separatum "$numerordinatio" "/")
  _nomen=$(numerordinatio_neo_separatum "$numerordinatio" "_")
  _prefix=$(numerordinatio_neo_separatum "$numerordinatio" ":")

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

  fontem_archivum="${_basim_fontem}/$_path/$_nomen.$est_objectivum_linguam.codex.adoc"
  objectivum_archivum="${_basim_objectivum}/$_path/$_nomen.$est_objectivum_linguam.codex.epub"
  objectivum_archivum_temporarium="${ROOTDIR}/999999/0/$_nomen.$est_objectivum_linguam.codex.epub"
  # ascidoctor_custom_library="${ROOTDIR}/999999999/0/custom_pdf_converter.rb"
  # ascidoctor_theme="${ROOTDIR}/999999999/0/1603_1.asciidoctor-pdf-theme-1.yml"
  # ascidoctor_font_dir_neo="/usr/share/fonts/truetype/noto,/usr/share/fonts/opentype/noto"
  # ascidoctor_font_dir_repo="${ROOTDIR}/999999/1603/1/3/"

  # ASCIIDOCTOR_PDF_DIR=$(bundle exec gem contents asciidoctor-pdf --show-install-dir)
  # ascidoctor_font_dir_original="$ASCIIDOCTOR_PDF_DIR/data/fonts"

  # echo "$fontem_archivum"

  # if [ -z "$(changed_recently "$fontem_archivum")" ]; then return 0; fi
  # echo "${FUNCNAME[0]} sources changed_recently. Reloading..."

  # if [ ! -e "$objectivum_archivum" ]; then
  #   echo "${FUNCNAME[0]} objective not exist. Reloading... [$objectivum_archivum]"
  # elif [ -z "$(changed_recently "$fontem_archivum")" ]; then
  #   # echo "${FUNCNAME[0]} objective exist, sources not changed recently"
  #   return 0
  # else
  #   echo "${FUNCNAME[0]} sources changed_recently. Reloading... [$fontem_archivum]"
  # fi

  echo "${FUNCNAME[0]} [$objectivum_archivum]"
  # return 0

  # @see TODO no custom font https://github.com/asciidoctor/asciidoctor-epub3/issues/62

  # bundle exec asciidoctor-pdf \
  # bundle exec asciidoctor-epub3 -a ebook-format=kf8 \
  bundle exec asciidoctor-epub3 \
    "$fontem_archivum" --out-file "$objectivum_archivum_temporarium"

  if [ -f "$objectivum_archivum" ]; then
    rm "$objectivum_archivum"
  fi
  # bundle exec hexapdf optimize "$objectivum_archivum_temporarium" "$objectivum_archivum"
  mv "$objectivum_archivum_temporarium" "$objectivum_archivum"

  # rm "$objectivum_archivum_temporarium"
}

#######################################
# From an .codex.adoc, create an PDF file
#
# Globals:
#   ROOTDIR
#   VELOX  (if =1, ignore fonts)
# Arguments:
#   numerordinatio
#   est_temporarium_fontem (default "1", from 99999/)
#   est_temporarium_objectivumm (default "0", from real namespace)
#   est_objectivum_linguam
#   est_auxilium_linguam
# Outputs:
#   Create documentation
#######################################
neo_codex_de_numerordinatio_pdf() {
  numerordinatio="$1"
  est_temporarium_fontem="${2:-"1"}"
  est_temporarium_objectivum="${3:-"0"}"
  # est_objectivum_linguam="${4:-"mul-Zyyy"}"
  est_objectivum_linguam="${4:-"mul-Latn"}"
  est_auxilium_linguam="${5:-"lat-Latn,por-Latn,eng-Latn"}"

  _path=$(numerordinatio_neo_separatum "$numerordinatio" "/")
  _nomen=$(numerordinatio_neo_separatum "$numerordinatio" "_")
  _prefix=$(numerordinatio_neo_separatum "$numerordinatio" ":")

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

  fontem_archivum="${_basim_fontem}/$_path/$_nomen.$est_objectivum_linguam.codex.adoc"
  objectivum_archivum="${_basim_objectivum}/$_path/$_nomen.$est_objectivum_linguam.codex.pdf"
  objectivum_archivum_temporarium="${ROOTDIR}/999999/0/$_nomen.$est_objectivum_linguam.codex.pdf"
  ascidoctor_theme="${ROOTDIR}/999999999/0/1603_1.asciidoctor-pdf-theme-1.yml"
  ascidoctor_font_dir_neo="/usr/share/fonts/truetype/noto,/usr/share/fonts/opentype/noto"
  ascidoctor_font_dir_repo="${ROOTDIR}/999999/1603/1/3/"
  ascidoctor_custom_library="${ROOTDIR}/999999999/0/custom_pdf_converter.rb"

  ASCIIDOCTOR_PDF_DIR=$(bundle exec gem contents asciidoctor-pdf --show-install-dir)
  ascidoctor_font_dir_original="$ASCIIDOCTOR_PDF_DIR/data/fonts"

  # if [ "$VELOX" -eq "1" ]; then
  #   _ascidoctor_fonts="$ascidoctor_font_dir_original"
  # else
  #   _ascidoctor_fonts="$ascidoctor_font_dir_neo,$ascidoctor_font_dir_original,$ascidoctor_font_dir_repo"
  # fi

  # echo "$fontem_archivum"

  # if [ -z "$(changed_recently "$fontem_archivum")" ]; then return 0; fi
  # echo "${FUNCNAME[0]} sources changed_recently. Reloading..."

  # if [ ! -e "$objectivum_archivum" ]; then
  #   echo "${FUNCNAME[0]} objective not exist. Reloading... [$objectivum_archivum]"
  # elif [ -z "$(changed_recently "$fontem_archivum")" ]; then
  #   # echo "${FUNCNAME[0]} objective exist, sources not changed recently"
  #   return 0
  # else
  #   echo "${FUNCNAME[0]} sources changed_recently. Reloading... [$fontem_archivum]"
  # fi

  echo "${FUNCNAME[0]} [$objectivum_archivum]"
  # return 0

  if [ "$VELOX" = "1" ]; then
    echo "VELOX"
    bundle exec asciidoctor-pdf \
      "$fontem_archivum" --out-file "$objectivum_archivum_temporarium"
  else
    bundle exec asciidoctor-pdf \
      --attribute pdf-theme="$ascidoctor_theme" \
      --attribute pdf-fontsdir="$ascidoctor_font_dir_neo,$ascidoctor_font_dir_original,$ascidoctor_font_dir_repo" \
      --require "$ascidoctor_custom_library" \
      "$fontem_archivum" --out-file "$objectivum_archivum_temporarium"
  fi

  if [ -f "$objectivum_archivum" ]; then
    rm "$objectivum_archivum"
  fi
  bundle exec hexapdf optimize "$objectivum_archivum_temporarium" "$objectivum_archivum"

  rm "$objectivum_archivum_temporarium"
}

## Tem definidos
# cat 999999/1603/1/1/1603_1_1.tm.hxl.csv | hxlselect --query="#status+conceptum<0"
# cat 999999/1603/1/1/1603_1_1.tm.hxl.csv | hxlselect --query='#status+conceptum+codicem~^(1|2|3|4|5|6|7|8|9)$' --reverse
## Nao tem definidos
# cat 1603/45/1/1603_45_1.no1.tm.hxl.csv | hxlselect --query="#status+conceptum<0"
# cat 1603/45/1/1603_45_1.no1.tm.hxl.csv | hxlselect --query='#status+conceptum+codicem~^(1|2|3|4|5|6|7|8|9)$' --reverse

# @TODO: create helper to remove empty translations;
#        @see https://github.com/wireservice/csvkit/issues/962
#        Potential example:
#        csvstat --csv 1603/45/1/1603_45_1.wikiq.tm.csv

#######################################
# Extract Wikipedia QIDs from numerordinatio no1.tm.hxl.csv and generate an
# wikiq.tm.csv
# Extract QCodes from:
#  - '+ix_wikiq'
#  - '+v_wiki_q'
#
# Globals:
#   ROOTDIR
# Arguments:
#   numerordinatio
#   est_temporarium_fontem (default "1", from 99999/)
#   est_temporarium_objectivumm (default "0", from real namespace)
#   always_stale (default "0", if 1, don't run stale_archive check)
# Outputs:
#   Convert files
#######################################
file_translate_csv_de_numerordinatio_q() {
  numerordinatio="$1"
  est_temporarium_fontem="${2:-"1"}"
  est_temporarium_objectivum="${3:-"0"}"
  always_stale="${4:-"0"}"

  _path=$(numerordinatio_neo_separatum "$numerordinatio" "/")
  _nomen=$(numerordinatio_neo_separatum "$numerordinatio" "_")
  _prefix=$(numerordinatio_neo_separatum "$numerordinatio" ":")

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

  fontem_archivum="${_basim_fontem}/$_path/$_nomen.no1.tm.hxl.csv"
  objectivum_archivum="${_basim_objectivum}/$_path/$_nomen.wikiq.tm.hxl.csv"
  objectivum_archivum_temporarium="${ROOTDIR}/999999/0/$_nomen.no1.tm.hxl.csv"
  objectivum_archivum_temporarium_b="${ROOTDIR}/999999/0/$_nomen.q.txt"
  objectivum_archivum_temporarium_b_u="${ROOTDIR}/999999/0/$_nomen.uniq.q.txt"
  objectivum_archivum_temporarium_b_u_wiki="${ROOTDIR}/999999/0/$_nomen.wikiq.tm.hxl.csv"
  objectivum_archivum_temporarium_b_u_wiki_1_5="${ROOTDIR}/999999/0/$_nomen~1.wikiq.tm.hxl.csv"
  objectivum_archivum_temporarium_b_u_wiki_2_5="${ROOTDIR}/999999/0/$_nomen~2.wikiq.tm.hxl.csv"
  objectivum_archivum_temporarium_b_u_wiki_3_5="${ROOTDIR}/999999/0/$_nomen~3.wikiq.tm.hxl.csv"
  objectivum_archivum_temporarium_b_u_wiki_4_5="${ROOTDIR}/999999/0/$_nomen~4.wikiq.tm.hxl.csv"
  objectivum_archivum_temporarium_b_u_wiki_5_5="${ROOTDIR}/999999/0/$_nomen~5.wikiq.tm.hxl.csv"

  objectivum_archivum_temporarium_b_u_wiki_1m2="${ROOTDIR}/999999/0/$_nomen~1+2.wikiq.tm.hxl.csv"
  objectivum_archivum_temporarium_b_u_wiki_1m2m3="${ROOTDIR}/999999/0/$_nomen~1+2+3.wikiq.tm.hxl.csv"
  objectivum_archivum_temporarium_b_u_wiki_1m2m3m4="${ROOTDIR}/999999/0/$_nomen~1+2+3+4.wikiq.tm.hxl.csv"
  # objectivum_archivum_temporarium_b_u_wiki_1m2m3m4m5="${ROOTDIR}/999999/0/$_nomen~1+2+3+4+5.wikiq.tm.hxl.csv"

  # if [ -z "$(changed_recently "$fontem_archivum")" ]; then return 0; fi

  # echo "${FUNCNAME[0]} sources changed_recently. Reloading..."

  if [ -z "$(stale_archive "$objectivum_archivum")" ]; then
    if [ "$always_stale" != '1' ]; then
      return 0
    fi
    echo "Cache may exist, but always_stale enabled [$numerordinatio]"
  fi

  echo "[ DOWNLOAD Wikidata ] ${FUNCNAME[0]} stale data on [$objectivum_archivum], refreshing..."

  hxlcut \
    --include='#*+ix_wikiq,#*+v_wiki_q,#item+conceptum+numerordinatio' \
    "$fontem_archivum" |
    hxlselect --query='#*+ix_wikiq>0' --query='#*+v_wiki_q>0' \
      >"$objectivum_archivum_temporarium"

  hxlcut \
    --include='#*+ix_wikiq,#*+v_wiki_q' \
    "$fontem_archivum" |
    hxlselect --query='#*+ix_wikiq>0' --query='#*+v_wiki_q>0' \
      >"$objectivum_archivum_temporarium_b"

  sed -i '1,2d' "${objectivum_archivum_temporarium_b}"

  # sort --numeric-sort < "$objectivum_archivum_temporarium_b" > "$objectivum_archivum_temporarium_b_u"
  # sort --version-sort < "$objectivum_archivum_temporarium_b" > "$objectivum_archivum_temporarium_b_u"
  # sort --version-sort --field-separator="Q" < "$objectivum_archivum_temporarium_b" > "$objectivum_archivum_temporarium_b_u"
  sort --version-sort --field-separator="Q" <"$objectivum_archivum_temporarium_b" | uniq >"$objectivum_archivum_temporarium_b_u"

  # echo "$objectivum_archivum_temporarium_b_u"
  # echo "${ROOTDIR}/999999999/0/1603_3_12.py" \
  #   --actionem-sparql \
  #   --lingua-divisioni=3 \
  #   --lingua-paginae=1 \
  #   --query <"$objectivum_archivum_temporarium_b_u"

  # exit 1

  # TODO: implement check if return result on 1603_45_1~5.wikiq.tm.hxl.csv
  #       is something such as
  #  ----
  #  #Service load too high,# please come back later
  #
  #
  #  -----
  echo "1/5"
  "${ROOTDIR}/999999999/0/1603_3_12.py" \
    --actionem-sparql \
    --lingua-divisioni=5 \
    --lingua-paginae=1 \
    --query <"$objectivum_archivum_temporarium_b_u" |
    ./999999999/0/1603_3_12.py --actionem-sparql --csv --hxltm \
      >"$objectivum_archivum_temporarium_b_u_wiki_1_5"

  echo "2/5"
  "${ROOTDIR}/999999999/0/1603_3_12.py" \
    --actionem-sparql \
    --lingua-divisioni=5 \
    --lingua-paginae=2 \
    --query <"$objectivum_archivum_temporarium_b_u" |
    ./999999999/0/1603_3_12.py --actionem-sparql --csv --hxltm \
      >"$objectivum_archivum_temporarium_b_u_wiki_2_5"

  echo "3/5"
  "${ROOTDIR}/999999999/0/1603_3_12.py" \
    --actionem-sparql \
    --lingua-divisioni=5 \
    --lingua-paginae=3 \
    --query <"$objectivum_archivum_temporarium_b_u" |
    ./999999999/0/1603_3_12.py --actionem-sparql --csv --hxltm \
      >"$objectivum_archivum_temporarium_b_u_wiki_3_5"

  echo "4/5"
  "${ROOTDIR}/999999999/0/1603_3_12.py" \
    --actionem-sparql \
    --lingua-divisioni=5 \
    --lingua-paginae=4 \
    --query <"$objectivum_archivum_temporarium_b_u" |
    ./999999999/0/1603_3_12.py --actionem-sparql --csv --hxltm \
      >"$objectivum_archivum_temporarium_b_u_wiki_4_5"

  echo "5/5"
  "${ROOTDIR}/999999999/0/1603_3_12.py" \
    --actionem-sparql \
    --lingua-divisioni=5 \
    --lingua-paginae=5 \
    --query <"$objectivum_archivum_temporarium_b_u" |
    ./999999999/0/1603_3_12.py --actionem-sparql --csv --hxltm \
      >"$objectivum_archivum_temporarium_b_u_wiki_5_5"

  # Merging now...
  echo "Merging now..."

  hxlmerge --keys='#item+conceptum+codicem' \
    --tags='#item+rem' \
    --merge="$objectivum_archivum_temporarium_b_u_wiki_2_5" \
    "$objectivum_archivum_temporarium_b_u_wiki_1_5" \
    >"$objectivum_archivum_temporarium_b_u_wiki_1m2"

  sed -i '1d' "${objectivum_archivum_temporarium_b_u_wiki_1m2}"

  hxlmerge --keys='#item+conceptum+codicem' \
    --tags='#item+rem' \
    --merge="$objectivum_archivum_temporarium_b_u_wiki_3_5" \
    "$objectivum_archivum_temporarium_b_u_wiki_1m2" \
    >"$objectivum_archivum_temporarium_b_u_wiki_1m2m3"

  sed -i '1d' "${objectivum_archivum_temporarium_b_u_wiki_1m2m3}"

  hxlmerge --keys='#item+conceptum+codicem' \
    --tags='#item+rem' \
    --merge="$objectivum_archivum_temporarium_b_u_wiki_4_5" \
    "$objectivum_archivum_temporarium_b_u_wiki_1m2m3" \
    >"$objectivum_archivum_temporarium_b_u_wiki_1m2m3m4"

  sed -i '1d' "${objectivum_archivum_temporarium_b_u_wiki_1m2m3m4}"

  hxlmerge --keys='#item+conceptum+codicem' \
    --tags='#item+rem' \
    --merge="$objectivum_archivum_temporarium_b_u_wiki_5_5" \
    "$objectivum_archivum_temporarium_b_u_wiki_1m2m3m4" \
    >"$objectivum_archivum_temporarium_b_u_wiki"

  sed -i '1d' "${objectivum_archivum_temporarium_b_u_wiki}"

  # Merging done!

  # hxlmerge --keys='#item+conceptum+codicem' \
  #   --tags='#item+rem' \
  #   --merge="$objectivum_archivum_temporarium_b_u_wiki_2_3" \
  #   "$objectivum_archivum_temporarium_b_u_wiki_1_3" \
  #   >"$objectivum_archivum_temporarium_b_u_wiki_1m2"

  # hxlmerge --keys='#item+conceptum+codicem' \
  #   --tags='#item+rem' \
  #   --merge="$objectivum_archivum_temporarium_b_u_wiki_3_3" \
  #   "$objectivum_archivum_temporarium_b_u_wiki_1m2" \
  #   >"$objectivum_archivum_temporarium_b_u_wiki"

  # TODO: implement check fo see if there is more than one Q columns, then use
  #       as baseline

  rm "$objectivum_archivum_temporarium"
  rm "$objectivum_archivum_temporarium_b"
  rm "$objectivum_archivum_temporarium_b_u"
  rm "$objectivum_archivum_temporarium_b_u_wiki_1_5"
  rm "$objectivum_archivum_temporarium_b_u_wiki_2_5"
  rm "$objectivum_archivum_temporarium_b_u_wiki_3_5"
  rm "$objectivum_archivum_temporarium_b_u_wiki_4_5"
  rm "$objectivum_archivum_temporarium_b_u_wiki_5_5"
  rm "$objectivum_archivum_temporarium_b_u_wiki_1m2"
  rm "$objectivum_archivum_temporarium_b_u_wiki_1m2m3"
  rm "$objectivum_archivum_temporarium_b_u_wiki_1m2m3m4"

  # cp "$objectivum_archivum_temporarium_b_u_wiki_1_3" "$objectivum_archivum_temporarium_b_u_wiki"

  # mv "$objectivum_archivum_temporarium_b_u_wiki" "$objectivum_archivum"

  # echo "debug objectivum_archivum_temporarium_b_u_wiki $objectivum_archivum_temporarium_b_u_wiki"

  file_update_if_necessary csv "$objectivum_archivum_temporarium_b_u_wiki" "$objectivum_archivum"

  return 0
}

#######################################
# Merge no1.tm.hxl.csv with wikiq.tm.hxl.csv
#
# Globals:
#   ROOTDIR
# Arguments:
#   numerordinatio
#   est_temporarium_fontem (default "1", from 99999/)
#   est_temporarium_objectivumm (dfault "0", from real namespace)
#   est_non_normale
# Outputs:
#   Convert files
#######################################
file_merge_numerordinatio_de_wiki_q() {
  numerordinatio="$1"
  est_temporarium_fontem="${2:-"1"}"
  est_temporarium_objectivum="${3:-"0"}"
  est_non_normale="${4:-"0"}"

  _path=$(numerordinatio_neo_separatum "$numerordinatio" "/")
  _nomen=$(numerordinatio_neo_separatum "$numerordinatio" "_")
  _prefix=$(numerordinatio_neo_separatum "$numerordinatio" ":")

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

  fontem_archivum="${_basim_fontem}/$_path/$_nomen.no1.tm.hxl.csv"
  fontem_q_archivum="${_basim_fontem}/$_path/$_nomen.wikiq.tm.hxl.csv"
  objectivum_archivum="${_basim_objectivum}/$_path/$_nomen.no11.tm.hxl.csv"
  objectivum_archivum_temporarium="${ROOTDIR}/999999/0/$_nomen.no11.tm.hxl.csv"
  fontem_q_archivum_temporarium="${ROOTDIR}/999999/0/$_nomen.wikiq.tm.hxl.csv"
  # objectivum_archivum_temporarium_b="${ROOTDIR}/999999/0/$_nomen.q.txt"
  # objectivum_archivum_temporarium_b_u="${ROOTDIR}/999999/0/$_nomen.uniq.q.txt"
  # objectivum_archivum_temporarium_b_u_wiki="${ROOTDIR}/999999/0/$_nomen.wikiq.tm.hxl.csv"

  # TODO: implement check if necessary to revalidate
  echo "${FUNCNAME[0]} sources changed_recently. Reloading... [$fontem_archivum]"

  if [ "$est_non_normale" -eq "1" ]; then
    # We apply 'hxlclean --lower' only on writting systems which this make
    # sence. On this case at least '+is_latn,+is_cyrl'
    hxlrename \
      --rename='item+conceptum+codicem:#item+rem+i_qcc+is_zxxx+ix_wikiq' \
      "$fontem_q_archivum" |
      hxlclean --lower='#*+is_latn,#*+is_cyrl' \
        >"$fontem_q_archivum_temporarium"
  else
    # We apply 'hxlclean --lower' only on writting systems which this make
    # sence. On this case at least '+is_latn,+is_cyrl'
    hxlrename \
      --rename='item+conceptum+codicem:#item+rem+i_qcc+is_zxxx+ix_wikiq' \
      "$fontem_q_archivum" \
      >"$fontem_q_archivum_temporarium"
  fi

  # hxlmerge --keys='#item+rem+i_qcc+is_zxxx+ix_wikiq' \
  #   --tags='#item+rem' \
  #   --merge="$fontem_q_archivum" \
  #   "$fontem_archivum" \
  #   >"$objectivum_archivum_temporarium"

  # echo "oi2"

  hxlmerge --keys='#item+rem+i_qcc+is_zxxx+ix_wikiq' \
    --tags='#item+rem' \
    --merge="$fontem_q_archivum_temporarium" \
    "$fontem_archivum" \
    >"$objectivum_archivum_temporarium"

  sed -i '1d' "${objectivum_archivum_temporarium}"

  rm "$fontem_q_archivum_temporarium"

  file_update_if_necessary csv "$objectivum_archivum_temporarium" "$objectivum_archivum"

  return 0
}

#######################################
# contains(string, substring)
#
# Returns 0 if the specified string contains the specified substring,
# otherwise returns 1.
#
# Author:
#    https://stackoverflow.com/a/8811800/894546
# Example:
#    contains "abcd" "e" || echo "abcd does not contain e"
#    contains "abcd" "ab" && echo "abcd contains ab"
# Globals:
#   None
# Arguments:
#   string
#   substring
#######################################
contains() {
  string="$1"
  substring="$2"
  if test "${string#*"$substring"}" != "$string"; then
    return 0 # $substring is in $string
  else
    return 1 # $substring is not in $string
  fi
}

#######################################
# Normalization of PCode sheets. The RawSheetname may (or not) have ISO3166p1a3
# so this avoid redundancy.
#
# Globals:
#   None
# Arguments:
#   ISO3166p1a3
#   RawSheetname
#######################################
un_pcode_sheets_norma() {
  number=$(echo "$2" | tr -d -c 0-9)
  echo "$1_$number"
}

#######################################
# Do "the best possible" to infer HXL heading.
# Globals:
#   None
# Arguments:
#   RawSheetHeader
#######################################
un_pcode_hxl_from_header() {
  number=$(echo "$2" | tr -d -c 0-9)
  echo "$1_$number"
}

#######################################
# Return if header is likely be an Pcode
#
# Example:
#  un_pcode_rawheader_is_pcode "admin1Name_ar" || echo "admin1Name_ar not Pcode"
#  un_pcode_rawheader_is_pcode "admin2Pcode" && echo "admin2Pcode is Pcode"
# Globals:
#   None
# Arguments:
#   rawheader
un_pcode_rawheader_is_pcode() {
  rawheader="$1"

  # if echo "$rawheader" | grep -q -E "Pcode|pcode"; then
  if echo "$rawheader" | grep -q -E "Pcode|pcode"; then
    # if echo "$rawheader" | grep -E "Pcode|pcode" | wc -c; then
    # echo "   pentrou"
    return 1
  else
    return 0
  fi

  # if [ "$(contains "$rawheader" "Pcode" )" ] || [ "$(contains "$rawheader" "adm" )" ]; then
  #     return 0
  # fi
  # return 1
  # if [ "$(contains "$rawheader" "Pcode" )" ] && [ "$(contains "$rawheader" "adm" )" ]; then
  # if [ "$(contains "$rawheader" "Pcode" )" ] || [ "$(contains "$rawheader" "pcode" )" ]; then
  #     return 0
  # fi
  # return 1
}

#######################################
# Return if header is likely be an Pcode
#
# Globals:
#   None
# Arguments:
#   rawheader
un_pcode_rawheader_is_name() {
  rawheader="$1"
  if [ ! "$(contains "$rawheader" "Adm")" ] || [ ! "$(contains "$rawheader" "adm")" ]; then
    if [ ! "$(contains "$rawheader" "Name")" ] || [ ! "$(contains "$rawheader" "name")" ]; then
      return 0
    fi
  fi
  return 1
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

# https://stackoverflow.com/questions/6011661/regexp-sed-suppress-no-match-output

#######################################
# Only return numeric PCode admin level if the item matches typical raw CSV
# header of a PCode (excludes administrative names)
#
# Globals:
#   None
# Arguments:
#   csv_header_item
#######################################
un_pcode_csvheader_pcode_level() {
  csv_header_item="$1"
  sed_result=$(echo "${csv_header_item}" | sed -E 's/^(Admin|admin)([0-9]{1})(Pcode|pcode)$/\2/')
  # If sed fail, it returns entire line as it was the input
  if [ "$csv_header_item" != "$sed_result" ]; then
    echo "$sed_result"
  fi
  echo ""
}

#######################################
# Return administrative level either from PCode or administrative name
#
# Globals:
#   None
# Arguments:
#   csv_header_item
#######################################
un_pcode_csvheader_administrative_level() {
  csv_header_item="$1"

  # TODO: test both PCode and Translation type
  sed_result=$(echo "${csv_header_item}" | sed -E 's/^(Admin|admin)([0-9]{1})(Pcode|pcode|Name|RefName|AltName|AltName1|AltName2)(.+)$/\2/')
  # If sed fail, it returns entire line as it was the input
  if [ "$csv_header_item" != "$sed_result" ]; then
    echo "$sed_result"
    # return 0
  fi
  echo ""
  # return 1
}

#######################################
# For a typical CSV header, return if is generic "date"
#
# Globals:
#   None
# Arguments:
#   csv_header_item
#######################################
un_pcode_csvheader_date() {
  csv_header_item="$1"
  # Only one option used. simple comparison
  if [ "$csv_header_item" = "date" ]; then
    echo "$csv_header_item"
  fi
  echo ""
}

#######################################
# For a typical CSV header, return if is generic "date valid on"
#
# Globals:
#   None
# Arguments:
#   csv_header_item
#######################################
un_pcode_csvheader_date_valid_on() {
  csv_header_item="$1"
  # Only one option used. simple comparison
  if [ "$csv_header_item" = "validOn" ]; then
    echo "$csv_header_item"
  fi
  echo ""
}
#######################################
# For a typical CSV header, return if is generic "date valid to"
#
# Globals:
#   None
# Arguments:
#   csv_header_item
#######################################
un_pcode_csvheader_date_valid_to() {
  csv_header_item="$1"
  # Only one option used. simple comparison
  if [ "$csv_header_item" = "validTo" ]; then
    echo "$csv_header_item"
  fi
  echo ""
}

#######################################
# Only return numeric PCode admin level if the item matches typical raw CSV
# header
#
#
# Globals:
#   None
# Arguments:
#   csv_header_item
#######################################
un_pcode_rawheader_name_language() {
  csv_header_item="$1"

  # echo "admin2AltName2_en" | sed -E 's/^(Admin|admin)([0-9]){1}(Name|RefName|AltName|AltName1|AltName2)_([a-z]{2,3})/1:\1 2:\2 3:\3 4:\4/'
  # 1:admin 2:2 3:AltName2 4:en
  sed_result=$(echo "${csv_header_item}" | sed -E 's/^(Admin|admin)([0-9]){1}(Name|RefName|AltName|AltName1|AltName2)_([a-z]{2,3})/\4/')
  # If sed fail, it returns entire line as it was the input
  if [ "$csv_header_item" != "$sed_result" ]; then
    echo "$sed_result"
    # return 0
  fi
  echo ""
  # return 1
}

#######################################
# Generate an HXL Hashtag based on a raw CSV header item
#
# Globals:
#   None
# Arguments:
#   csv_header_item
#######################################
un_pcode_rawhader_to_hxl() {
  csv_header_item="$1"
  hxlheader=""
  _date=$(un_pcode_csvheader_date "$csv_header_item")
  _date_valid_on=$(un_pcode_csvheader_date_valid_on "$csv_header_item")
  _date_valid_to=$(un_pcode_csvheader_date_valid_to "$csv_header_item")
  _administrative_level=$(un_pcode_csvheader_administrative_level "$csv_header_item")
  _pcode_level=$(un_pcode_csvheader_pcode_level "$csv_header_item")
  _name_language=$(un_pcode_rawheader_name_language "$csv_header_item")
  if [ -n "$_date" ] || [ -n "$_date_valid_on" ] || [ -n "$_date_valid_to" ]; then
    hxlheader="#date"
    if [ -n "$_date_valid_on" ]; then
      # Note: Author not sure if this would be the HXL tag used here
      hxlheader="${hxlheader}+valid_on"
    fi
    if [ -n "$_date_valid_to" ]; then
      # Note: Author not sure if this would be the HXL tag used here
      hxlheader="${hxlheader}+valid_to"
    fi
  fi
  if [ -n "$_pcode_level" ]; then
    hxlheader="#adm${_pcode_level}+code+pcode"
  fi
  if [ -n "$_name_language" ]; then
    hxlheader="#adm${_administrative_level}+name+i_${_name_language}"
  fi
  echo "$hxlheader"
}

#######################################
# From a list of comma separated raw headers, return a comma separated
# HXLAted headers. Only for P-Code-like CSV files
#
# Globals:
#   None
# Arguments:
#   csv_input
#   csv_hxlated_output
#######################################
un_pcode_hxlate_csv_header() {
  csv_header_input="$1"
  csv_header_input_lines=$(echo "${csv_header_input}" | tr ',' "\n")
  hxlated_header=""

  # RESULT=""
  for item in $csv_header_input_lines; do
    hxlated_item=$(un_pcode_rawhader_to_hxl "$item")
    hxlated_header="${hxlated_header:+${hxlated_header},}${hxlated_item}"
  done
  echo "$hxlated_header"

  # echo "$csv_header_input_lines" | while IFS= read -r csv_header_item ; do
  #   administrative_level=$(un_pcode_csvheader_administrative_level "${line}")
  #   name_language=$(un_pcode_rawheader_name_language "$line")
  #   hxlhashtag=$(un_pcode_rawhader_to_hxl "$line")
  #   # echo $line
  #   hxlated_header
  # done
}

#######################################
# Generate an HXL Hashtag based on a raw CSV header item
#
# Example:
#    un_pcode_hxlate_csv_file AFG_1.csv > AFG_1.hxl.csv
#
# Globals:
#   None
# Arguments:
#   csv_input
#   csv_hxlated_output
#######################################
un_pcode_hxlate_csv_file() {
  csv_input="$1"
  # csv_hxlated_output="$1"
  # csv_header=$(head -n 1 "${csv_input}")

  linenumber=0
  while IFS= read -r line; do
    if [ "$linenumber" -eq "0" ]; then
      echo "$line"
      un_pcode_hxlate_csv_header=$(un_pcode_hxlate_csv_header "$line")
      echo "$un_pcode_hxlate_csv_header"
    else
      echo "$line"
    fi
    linenumber=$((linenumber + 1))
  done <"${csv_input}"
}

#######################################
# Return an 1603_45_49 (UN m49 numeric code) from other common systems
#
# Example:
#    un_pcode_hxlate_csv_file AFG_1.csv > AFG_1.hxl.csv
#
# Globals:
#   NUMERORDINATIO_DATUM
# Arguments:
#   scienciam_codicem
#   scienciam_variable_pointer
#######################################
__numerordinatio_scientiam_initiale() {
  scienciam_codicem="$1"
  scienciam_variable_pointer="$2" # Ponter, https://tldp.org/LDP/abs/html/ivr.html
  # _data=$(eval "${scienciam_variable}")
  # _data=${scienciam_variable}

  # https://tldp.org/LDP/abs/html/ivr.html
  # https://stackoverflow.com/a/19634966/894546

  echo "----D49-"
  echo "$D49"
  echo "----D49-"

  eval local_variable_content=\$$scienciam_variable_pointer
  echo "local_variable_content  before   $local_variable_content"
  # echo "-----"

  # eval local_variable_content=\$"$scienciam_variable_pointer"
  if [ -z "${local_variable_content}" ]; then
    local_variable_content=$(cat "${NUMERORDINATIO_DATUM}/${scienciam_codicem}.tsv")

    echo "entrou"
  else
    echo "error"
  fi

  echo "    ----D49-"
  echo "   $D49"
  echo "   ----D49-"
  # return 0
}

#######################################
# Basic tests to check of synchronization
#
# CDN (If using Wasabi as CND + Cloudflare as frontend):
# - Check this documentations:
#   - https://wasabi-support.zendesk.com/hc/en-us/articles
#     /360000016712-How-do-I-set-up-Wasabi-for-user-access-separation-
#   - https://wasabi-support.zendesk.com/hc/en-us/articles
#     /360018526192-How-do-I-use-Cloudflare-with-Wasabi-?source=search
#
# - Bucket name:
#   - lsf-cdn.etica.ai
# - DNS Configuration (on CloudFlare frontend, if using eu-central-1)
#   > lsf-cdn CNAME s3.eu-central-1.wasabisys.com
#
# Example
#   upload_cdn_test 1603_1_51
#
# Globals:
#   ROOTDIR
#   S3CFG
# Arguments:
#   numerordinatio
# Outputs:
#   Show results of test
#######################################
upload_cdn_test() {
  numerordinatio="$1"
  _path=$(numerordinatio_neo_separatum "$numerordinatio" "/")
  _nomen=$(numerordinatio_neo_separatum "$numerordinatio" "_")
  _prefix=$(numerordinatio_neo_separatum "$numerordinatio" ":")
  # _path_clean="${$_path/aa/bb}"
  # _path_clean=${_path/1603\//''}

  _basim_fontem="${ROOTDIR}/$_path/"
  _basim_objectivum="s3://lsf-cdn.etica.ai/$_path/"

  # echo "_path_clean [$_path]"
  # echo "_basim_objectivum [$_basim_objectivum]"

  set -x
  s3cmd ls "$_basim_objectivum" --list-md5 --config "$S3CFG"
  s3cmd du "$_basim_objectivum" --config "$S3CFG"
  s3cmd info "s3://lsf1603.etica.ai" --config "$S3CFG"
  set +x

}

#######################################
# Synchronization of files by numerordinatio
#
# Requires:
#   pip3 install s3cmd
#
# Example
#   upload_cdn 1603_1_51
#
# Globals:
#   ROOTDIR
#   S3CFG
# Arguments:
#   numerordinatio
# Outputs:
#   Convert files
#######################################
upload_cdn() {
  numerordinatio="$1"
  _path=$(numerordinatio_neo_separatum "$numerordinatio" "/")
  _nomen=$(numerordinatio_neo_separatum "$numerordinatio" "_")
  _prefix=$(numerordinatio_neo_separatum "$numerordinatio" ":")
  # _path_clean="${$_path/aa/bb}"
  # _path_clean=${_path/1603\//''}

  _basim_fontem="${ROOTDIR}/$_path/"
  _basim_objectivum="s3://lsf-cdn.etica.ai/$_path/"

  # echo "_path_clean [$_path_clean]"
  # echo "_basim_objectivum [$_basim_objectivum]"
  # blue=$(tput setaf 4)
  # normal=$(tput sgr0)
  # printf "%40s\n" "${blue}${FUNCNAME[0]} [$numerordinatio]${normal}"
  echo "${FUNCNAME[0]} [$numerordinatio]"

  # NOTE: we could implement explicit file patterns to (not) syncronize.
  #       However, as long as local disk already have excatly what we need
  #       Leave strict syncronization tend to be better

  # NOTE: the current approach, if current directory does not have
  #       all files re-generated, will delete files on the CDN. This is the
  #       expected behavior (but means only syncronize really at the end
  #       of operations)

  # TODO: check some way to set content always utf-8, such as
  #       > Content-Type: text/html; charset=utf-8.
  #       This file https://lsf-cdn.etica.ai/1603/45/1/1603_45_1.no11.xml
  #       is returning 'content-type: text/plain' without utf-8 on preview

  set -x
  s3cmd sync "$_basim_fontem" "$_basim_objectivum" \
    --recursive --delete-removed --acl-public \
    --no-progress --stats \
    --config "$S3CFG"
  set +x

  temp_save_status "$numerordinatio" "cdn"
}

################################################################################
##### AFTER HERE, POTENTIALY DEPRECATED. Eventually remove it ##################
# Most logit here was replaced with high level python, but parts may still be  #
# in use. Not really a issue remove then, just a matter of test before remove  #
################################################################################

# DEPRECATED! Use 0/2600.60.py
__numerordinatio_codicem_lineam() {
  lineam="$1"
  echo "$lineam" | tr '\t' '\n' | while IFS= read -r value; do
    if [ "$value" = "${terminum}" ]; then
      echo "$line" | cut -f1
      return 0
    fi
  done
}

# DEPRECATED! Use 0/2600.60.py
__numerordinatio_translatio() {
  codewordlist="$1"
  codicem_rem="$2"

  linenumber=0
  echo "${codewordlist}" | tr ',' '\n' | while IFS= read -r line; do
    if [ "${line}" = "${codicem_rem}" ]; then
      echo "$linenumber"
      break
    fi
    linenumber=$((linenumber + 1))
    # echo " tentativa $linenumber"
  done
}

# DEPRECATED! Use 0/2600.60.py
__numerordinatio_translatio_numerum_pariae() {
  local codeword_purum="$1"
  local linenumber=0
  local total=0

  while read -r -n 1 char; do
    # echo "$char"
    # char_intval=$(("$char"))
    total=$((total + char))
  done <<<"$codeword_purum"

  # echo "Debug: input $codeword_purum: Sum: $total; parity; ${total: -1}"
  echo "${total: -1}"
}

# __numerordinatio_translatio_numerum_pariae 123
# __numerordinatio_translatio_numerum_pariae 456

#######################################
# Change Numerordĭnātĭo rank separator
#
# DEPRECATED! Use 0/2600.60.py
#
# Example:
#    # 4
#    numerordinatio_translatio_alpha_in_digito__beta "111" 3
#    # 1111
#    numerordinatio_translatio_alpha_in_digito__beta "aaa" 3
#    # 44136
#    numerordinatio_translatio_alpha_in_digito__beta "ZZZ" 3
#
# Globals:
#   None
# Arguments:
#   codicem
#   total_characters
#   tab_expanded
#######################################
numerordinatio_translatio_in_digito__beta() {
  codicem="$1"
  total_characters="$2"
  tab_expanded="${3}"
  # _TEMPDIR=$(mktemp --directory)
  # _FIFO_total="$_TEMPDIR/total"
  # mkfifo "${_FIFO_total}"

  # Must be betwen 1 and 9. Around 5 start to be impractical
  _exact_packed_chars_number="$total_characters"

  # universum_alpha_usascii="NOP,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP"
  # universum_alpha_usascii="NOP,0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP"
  universum_alpha_usascii="NOP,NOP,0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP"
  # universum_alphanum_usascii="0123456789abcdefghijklmnopqrstuvwxyz"

  # @see https://en.wikipedia.org/wiki/ISO_639-3#Code_space

  codicem=$(echo "$codicem" | tr '[:upper:]' '[:lower:]')
  numeric_total=0

  # mkfifo "${TMPDIR}"/_nmt_total
  # echo "$numeric_total" > "$_FIFO_total" &

  # https://stackoverflow.com/questions/6834347/named-pipe-closing-prematurely-in-script/

  linenumber=0
  # @see https://stackoverflow.com/a/10572879/894546
  # echo "${codicem}" | sed -e 's/\(.\)/\1\n/g'  | while IFS= read -r character; do
  # shellcheck disable=SC2001
  while IFS= read -r character; do
    numerum=$(__numerordinatio_translatio "$universum_alpha_usascii" "$character")
    numerum=$((numerum))

    # echo ">>> numeric_total $numeric_total"
    # _total=$(cat "$_FIFO_total")
    # numeric_now=$((numerum * pow_now))
    numeric_now=$(echo "$numerum ^ $total_characters" | bc)
    # echo "$numerum ^ $total_characters"

    # numeric_total=$(( _total + numeric_now))
    numeric_total=$((numeric_total + numeric_now))
    # echo "$numeric_total" > "$_FIFO_total" &

    # TO Debug, remove next comment
    # echo "c [$character]: cn [$numerum]:cnv [$numeric_now]: p: [$total_characters] :cnt [$numeric_total]"
    linenumber=$((linenumber + 1))
    total_characters=$((total_characters - 1))
    # done
  done <<<"$(echo "${codicem}" | sed -e 's/\(.\)/\1\n/g')"

  # _total=$(cat "$_FIFO_total")
  # TODO: implement a real CRC, to allow check later. 0 means no check
  total_namespace_multiple_of_60="1"
  # crc_check=$(__numerordinatio_translatio_numerum_pariae "$_total")
  crc_check=$(__numerordinatio_translatio_numerum_pariae "$numeric_total")

  # fullcode="${_total}${_exact_packed_chars_number}${total_namespace_multiple_of_60}${crc_check}"
  fullcode="${numeric_total}${_exact_packed_chars_number}${total_namespace_multiple_of_60}${crc_check}"
  if [ -z "$tab_expanded" ]; then
    echo "$fullcode"
  else
    # printf "%s\t%s\t%s\t%s\t%s\n" "$fullcode" "${_total}" "${_exact_packed_chars_number}" "${total_namespace_multiple_of_60}" "${crc_check}"
    printf "%s\t%s\t%s\t%s\t%s\n" "$fullcode" "${numeric_total}" "${_exact_packed_chars_number}" "${total_namespace_multiple_of_60}" "${crc_check}"
    # echo "${_total}\t${_exact_packed_chars_number}${total_namespace_multiple_of_60}${crc_check}"
  fi

  # rm "${_FIFO_total:-'unknow-file'}"

  # separator_finale="$2"
  # separator_initiale="${3:-\:}"
  # resultatum=""
  # if [ -z "$numerordinatio_codicem" ] || [ -z "$separator_finale" ]; then
  #     echo "errorem [$*]"
  #     return 1
  # fi
  # resultatum=$(echo "$numerordinatio_codicem" | sed "s|${separator_initiale}|${separator_finale}|g")
  # echo "$resultatum"
}

# 4314	003
# 4314	012
# 4314	102
# 4314	111
# benchmark
# END=100
# END=100
# for ((i=1;i<=END;i++)); do
#     # echo ">> 111111 6"
#     # numerordinatio_translatio_in_digito__beta "111111" 6 "verbose"
#     numerordinatio_translatio_in_digito__beta "111111" 6 "verbose" >/dev/null
#     # echo ""
#     # echo ">> aaaaaa 6 verbose"
#     # numerordinatio_translatio_in_digito__beta "aaaaaa" 6 "verbose"
#     numerordinatio_translatio_in_digito__beta "aaaaaa" 6 "verbose" >/dev/null
# done

# echo ">> aaa 3"
# numerordinatio_translatio_in_digito__beta "aaa" 3 "verbose"
# echo ""
# echo ">> abc 3"
# numerordinatio_translatio_alpha_in_digito__beta "abc" 3
# echo ""
# echo ">> 123 3"
# numerordinatio_translatio_alpha_in_digito__beta "123" 3
# echo ""
# echo ">> ZZZ 3"
# numerordinatio_translatio_alpha_in_digito__beta "ZZZ" 3
# echo ""
# echo ">> ZZZZ 4"
# numerordinatio_translatio_alpha_in_digito__beta "ZZZZ" 4

#######################################
# Change Numerordĭnātĭo rank separator
#
# Example:
#    # 12/34/56
#    numerordinatio_codicem_transation_separator "12/34/56" "/"
#    # 十二/三十四/五十六
#    numerordinatio_codicem_transation_separator "十二:三十四:五十六" "/"
#    # errorem [ / :]
#    numerordinatio_codicem_transation_separator "" "/" ":"
#
# Globals:
#   None
# Arguments:
#   terminum
#######################################
numerordinatio_codicem_transation_separator() {
  numerordinatio_codicem="$1"
  separator_finale="$2"
  separator_initiale="${3:-\:}"
  resultatum=""
  if [ -z "$numerordinatio_codicem" ] || [ -z "$separator_finale" ]; then
    echo "errorem [$*]"
    return 1
  fi
  resultatum=$(echo "$numerordinatio_codicem" | sed "s|${separator_initiale}|${separator_finale}|g")
  echo "$resultatum"
}

# numerordinatio_codicem_transation_separator "12:34:56" "/"
# numerordinatio_codicem_transation_separator "十二:三十四:五十六" "/"
# numerordinatio_codicem_transation_separator "" "/" ":"

#######################################
# Return an 1603_45_49 (UN m49 numeric code) from other common systems
#
# Example:
#    # > 76
#    numerordinatio_codicem_locali__1603_45_49 "BRA"
#
# Globals:
#   NUMERORDINATIO_DATUM__1603_45_49
# Arguments:
#   terminum
#######################################
numerordinatio_codicem_locali__1603_45_49() {
  terminum="$1"
  codicem_locali=""

  if [ -z "$NUMERORDINATIO_DATUM__1603_45_49" ]; then
    echo "non NUMERORDINATIO_DATUM__1603_45_49 1603_47_639_3.tsv"
    return 1
  fi

  echo "$NUMERORDINATIO_DATUM__1603_45_49" | while IFS= read -r line; do
    codicem_locali=$(__numerordinatio_codicem_lineam "$line")
    if [ -n "$codicem_locali" ]; then
      echo "$codicem_locali"
      return 0
    fi
    # echo "line $line"
  done
  # echo "none for $terminum"
}

#######################################
# Return an 1603_45_49 (UN m49 numeric code) from other common systems
# TODO:
#    Create numeric codes
#
# Example:
#    # > 76
#    numerordinatio_codicem_locali__1603_47_639_3 "pt"
#
# Globals:
#   NUMERORDINATIO_DATUM__1603_47_639_3
# Arguments:
#   terminum
#######################################
numerordinatio_codicem_locali__1603_47_639_3() {
  terminum="$1"
  codicem_locali=""

  if [ -z "$NUMERORDINATIO_DATUM__1603_47_639_3" ]; then
    echo "non NUMERORDINATIO_DATUM__1603_47_15924 1603_45_49.tsv"
    return 1
  fi

  echo "$NUMERORDINATIO_DATUM__1603_47_639_3" | while IFS= read -r line; do
    codicem_locali=$(__numerordinatio_codicem_lineam "$line")
    if [ -n "$codicem_locali" ]; then
      echo "$codicem_locali"
      return 0
    fi
    # echo "line $line"
  done
  # echo "none for $terminum"
}

#######################################
# Return an 1603_45_49 (UN m49 numeric code) from other common systems
# TODO:
#    Create numeric codes
#
# Example:
#    # > 215
#    numerordinatio_codicem_locali__1603_47_15924 "Latn"
#
# Globals:
#   NUMERORDINATIO_DATUM__1603_47_639_3
# Arguments:
#   terminum
#######################################
numerordinatio_codicem_locali__1603_47_15924() {
  terminum="$1"
  codicem_locali=""

  if [ -z "$NUMERORDINATIO_DATUM__1603_47_15924" ]; then
    echo "non NUMERORDINATIO_DATUM__1603_47_15924 1603_47_15924.tsv"
    return 1
  fi

  echo "$NUMERORDINATIO_DATUM__1603_47_15924" | while IFS= read -r line; do
    codicem_locali=$(__numerordinatio_codicem_lineam "$line")
    if [ -n "$codicem_locali" ]; then
      echo "$codicem_locali"
      return 0
    fi
    # echo "line $line"
  done
  # echo "none for $terminum"
}

# https://superuser.com/questions/279141/why-is-reading-a-file-faster-than-reading-a-variable
if [ -f "${NUMERORDINATIO_DATUM}/1603_45_49.tsv" ]; then
  NUMERORDINATIO_DATUM__1603_45_49=$(cat "${NUMERORDINATIO_DATUM}/1603_45_49.tsv")
fi
if [ -f "${NUMERORDINATIO_DATUM}/1603_47_639_3.tsv" ]; then
  NUMERORDINATIO_DATUM__1603_47_639_3=$(cat "${NUMERORDINATIO_DATUM}/1603_47_639_3.tsv")
fi
if [ -f "${NUMERORDINATIO_DATUM}/1603_47_639_3.tsv" ]; then
  NUMERORDINATIO_DATUM__1603_47_15924=$(cat "${NUMERORDINATIO_DATUM}/1603_47_15924.tsv")
fi

# echo ""
# # numerordinatio_codicem_locali__1603_45_49 "br"
# numerordinatio_codicem_locali__1603_45_49 "BRA"
# numerordinatio_codicem_locali__1603_45_49 "SWZ"
# numerordinatio_codicem_locali__1603_45_49 "SWZ"
# numerordinatio_codicem_locali__1603_45_49 "SWZ"
# numerordinatio_codicem_locali__1603_45_49 "SAU"

# echo ""
# numerordinatio_codicem_locali__1603_47_639_3 "pt"
# numerordinatio_codicem_locali__1603_47_639_3 "es"
# numerordinatio_codicem_locali__1603_47_639_3 "en"

# echo ""
# numerordinatio_codicem_locali__1603_47_15924 "Latn"
# numerordinatio_codicem_locali__1603_47_15924 "Arab"
# numerordinatio_codicem_locali__1603_47_15924 "cyrl"

#### wikidata tests
# @see https://github.com/maxlath/wikibase-cli
# npm install -g wikibase-cli

################################################################################
##### BEFORE HERE, POTENTIALY DEPRECATED. Eventually remove it #################
# The last part of this helper is just catch-all functions to abstract other   #
# boring calls.                                                                #
################################################################################

#######################################
# Check if Numerodinatio needs Wikidata Q
#
# Globals:
#   ROOTDIR
# Arguments:
#   numerordinatio
# Outputs:
#   (empty)
# Returns:
#   0: success; have the tag
#   1: fail; do not have the tag
#######################################
quaero__ix_n1603ia__victionarium_q() {
  numerordinatio="$1"

  _nomen=$(numerordinatio_neo_separatum "$numerordinatio" "_")

  resultatum=$("${ROOTDIR}/999999999/0/1603_1.py" \
    --ex-opere-temporibus='cdn' \
    --quaero-ix_n1603ia='{victionarium_q}>=1' \
    --quaero-numerordinatio="$_nomen")

  # resultatum=${resultatum//[[:blank:]]/}

  # echo "resultatum"
  # echo "[$resultatum]"

  if [ -z "$resultatum" ]; then
    echo 1
    return 1
    # return 0
  else
    return 0
    # return 1
  fi
}

#######################################
# Opus temporibus
#
# Globals:
#   ROOTDIR
# Arguments:
#   numerordinatio
# Outputs:
#   Convert files
#######################################
opus_temporibus_cdn() {
  # ...
  # echo "TODO..."
  blue=$(tput setaf 4)
  normal=$(tput sgr0)
  printf "%40s\n" "${blue}${FUNCNAME[0]}${normal}"

  opus_temporibus_temporarium="${ROOTDIR}/999999/0/1603.cdn.statum.tsv"

  ### Dependencies, start -----------------------------------
  ## officinam/999999/1603/1603.xlsx: download all sheets to temp
  # file_download_1603_xlsx "1"
  # Post dependencies (per sheet)
  # file_convert_csv_de_downloaded_xlsx
  ### Dependencies, end -------------------------------------

  # "${ROOTDIR}/999999999/0/1603_1.py" \
  #   --ex-opere-temporibus='cdn' \
  #   --quaero-ix_n1603ia='({publicum}>=10)' \
  #   --in-ordinem=chaos \
  #   --in-limitem=2 \
  #   >"$opus_temporibus_temporarium"

  "${ROOTDIR}/999999999/0/1603_1.py" \
    --ex-opere-temporibus='cdn' \
    --quaero-ix_n1603ia='({publicum}>=1)' \
    --in-ordinem=chaos \
    --in-limitem=2 \
    >"$opus_temporibus_temporarium"

  while IFS=$'\t' read -r -a line; do
    # echo "${line[0]}"

    actiones_completis_publicis "${line[0]}"
    # echo "${line[1]}"
    # echo "${line[2]}"
  done <"${opus_temporibus_temporarium}"

  # ./999999999/0/1603_1.py --ex-opere-temporibus='cdn' --quaero-ix_n1603ia='({publicum}>=1)'
}

#######################################
# TODO...
#
# Globals:
#   ROOTDIR
# Arguments:
#   numerordinatio
# Outputs:
#   Convert files
#######################################
temp_save_status() {
  numerordinatio="$1"
  ex_librario="$2"

  _path=$(numerordinatio_neo_separatum "$numerordinatio" "/")
  _nomen=$(numerordinatio_neo_separatum "$numerordinatio" "_")
  _prefix=$(numerordinatio_neo_separatum "$numerordinatio" ":")
  _ex_librario="$ex_librario"

  status_archivum_codex="${ROOTDIR}/$_path/$_nomen.statum.yml"
  status_archivum_librario="${ROOTDIR}/1603/1603.$_ex_librario.statum.yml"
  objectivum_archivum_temporarium="${ROOTDIR}/999999/0/1603+$_nomen.statum.yml"

  "${ROOTDIR}/999999999/0/1603_1.py" \
    --codex-de "$_nomen" --status-quo \
    >"$status_archivum_codex"

  # echo "$status_archivum_librario status_archivum_librario "

  set -x
  "${ROOTDIR}/999999999/0/1603_1.py" \
    --codex-de "$_nomen" --status-quo --ex-librario="$_ex_librario" \
    >"$objectivum_archivum_temporarium"
  set +x

  # NOTE: this operation should be atomic. But for sake of portability,
  #       we're using temporary file without flog or setlock or something.
  #       Trying to use --status-quo --ex-librario
  #       without temporary file will reset old information. That's why
  #       we're using temp file
  rm "$status_archivum_librario" &&
    mv "$objectivum_archivum_temporarium" "$status_archivum_librario"

}

#######################################
# āctiōnēs complētīs locālī, complete actions (except download references and
# publish online)
#
# Globals:
#   ROOTDIR
# Arguments:
#   numerordinatio
# Outputs:
#   Convert files
#######################################
actiones_completis_locali() {
  numerordinatio="$1"
  echo ""

  blue=$(tput setaf 4)
  normal=$(tput sgr0)
  printf "\t%40s\n" "${blue}${FUNCNAME[0]} [$numerordinatio]${normal}"

  file_convert_csv_de_downloaded_xlsx "$numerordinatio" "1" "1"
  file_convert_numerordinatio_de_hxltm "$numerordinatio" "1" "0"

  # @TODO: implement decent check if need download Wikidata Q again
  #        now is hardcoded as "1" on last parameter
  # file_translate_csv_de_numerordinatio_q "$numerordinatio" "0" "0"

  if [ -z "$(quaero__ix_n1603ia__victionarium_q "$numerordinatio")" ]; then
    # echo "yay"
    file_translate_csv_de_numerordinatio_q "$numerordinatio" "0" "0" "1"
    file_merge_numerordinatio_de_wiki_q "$numerordinatio" "0" "0"
    file_convert_tmx_de_numerordinatio11 "$numerordinatio"
    file_convert_tbx_de_numerordinatio11 "$numerordinatio"
  # else
  #   echo "noop"
  fi

  neo_codex_copertae_de_numerordinatio "$numerordinatio" "0" "0"
  neo_codex_de_numerordinatio "$numerordinatio" "0" "0"
  neo_codex_de_numerordinatio_epub "$numerordinatio" "0" "0"
  neo_codex_de_numerordinatio_pdf "$numerordinatio" "0" "0"
  # temp_save_status "$numerordinatio" "locale"

}

#######################################
# āctiōnēs complētīs pūblicīs, complete actions (and publish online)
#
# Globals:
#   ROOTDIR
# Arguments:
#   numerordinatio
# Outputs:
#   Convert files
#######################################
actiones_completis_publicis() {
  numerordinatio="$1"
  echo ""

  blue=$(tput setaf 4)
  normal=$(tput sgr0)
  printf "\t%40s\n" "${blue}${FUNCNAME[0]} [$numerordinatio]${normal}"

  actiones_completis_locali  "$numerordinatio"
  upload_cdn "$numerordinatio"
}

# TODO: document...
deploy_0_9_markdown() {
  # ROOTDIR assumed to be on officinam
  objectivum_archivum="${ROOTDIR}/README.md"
  echo "${FUNCNAME[0]} [$objectivum_archivum]..."

  "${ROOTDIR}/999999999/0/1603_1.py" \
    --codex-de 1603_1_1 \
    --status-quo \
    --ex-librario="cdn" \
    --status-in-markdown \
    >"$objectivum_archivum"
}
