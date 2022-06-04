#!/bin/bash
#===============================================================================
#
#          FILE:  bcp47-to-hxl-to-rdf.sh
#
#         USAGE:  ./999999999/1568346/bcp47-to-hxl-to-rdf.sh
#   DESCRIPTION:  ---
#
#       OPTIONS:  ---
#
#  REQUIREMENTS:  ---
#          BUGS:  ---
#         NOTES:  ---
#        AUTHOR:  Emerson Rocha <rocha[at]ieee.org>
#       COMPANY:  EticaAI
#       LICENSE:  Public Domain dedication
#                 SPDX-License-Identifier: Unlicense
#       VERSION:  v1.0
#       CREATED:  2022-05-28 03:30 UTC started.
#      REVISION:  ---
#===============================================================================
set -e

ROOTDIR="$(pwd)"

#######################################
# bcp47_to_hxl_to_rdf__tests
#
# Globals:
#   ROOTDIR
# Arguments:
#   None
# Outputs:
#   Test result
#######################################
bcp47_to_hxl_to_rdf__tests() {
  # numerordinatio="$1"
  # ex_librario="$2"

  # echo "oi"

  archivum__regulae_exemplis="${ROOTDIR}/999999999/1568346/bcp47-to-hxl-to-rdf.hxl.tsv"
  # echo "oi2"
  archivum__resultata="${ROOTDIR}/999999/1568346/bcp47-to-hxl-to-rdf.jsonl"

  # "${ROOTDIR}/999999999/0/1603_1.py" \
  #   --methodus='status-quo' \
  #   --status-quo-in-yaml \
  #   --codex-de "$_nomen" \
  #   >"$status_archivum_codex"

  echo "[\"#item+bpc47\", \"#item+hxl\", \"#item+rdf\", \"#item+debug\"]" >"$archivum__resultata"

  # while IFS=, read -r iso3 source_url; do
  {
    # remove read -r to not skip first line
    read -r
    while IFS=$'\t' read -r -a linea; do
      bpc47="${linea[0]}"
      hxl="${linea[1]}"
      rdf="${linea[2]}"
      # namespace="${linea[3]}"

      bc47_full=$("${ROOTDIR}/999999999/0/linguacodex.py" \
        --de_bcp47_simplex --de_codex="${bpc47}" --quod=.extension)

      echo "[\"${bpc47}\", \"${hxl}\", \"${rdf}\", ${bc47_full}]" >>"$archivum__resultata"

      # # echo "numerordinatio_praefixo $numerordinatio_praefixo"
      # # bootstrap_1603_45_16__item "1603_45_16_24" "24" "AGO" "AO" "3" "1" "0"
      # bootstrap_1603_45_16__item "$numerordinatio_praefixo" "$unm49" "$v_iso3" "$v_iso2" "$cod_ab_level_max" "1" "0"
      # # bootstrap_1603_45_16__item "$numerordinatio_praefixo" "$unm49" "$v_iso3" "$v_iso2" "1" "0"
      # sleep 5
    done
  } <"${archivum__regulae_exemplis}"

}

# echo "test"

bcp47_to_hxl_to_rdf__tests
