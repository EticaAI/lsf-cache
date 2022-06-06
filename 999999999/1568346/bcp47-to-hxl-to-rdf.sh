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

#######################################
# test_unesco_thesaurus
#
# Globals:
#   ROOTDIR
# Arguments:
#   None
# Outputs:
#   Test result
#######################################
test_unesco_thesaurus() {
  archivum__namespace="${ROOTDIR}/999999999/1568346/data/hxlstandard-rdf-namespaces-example.hxl.csv"
  archivum__unesco_thesaurus_bcp47="${ROOTDIR}/999999999/1568346/data/unesco-thesaurus.bcp47g.tsv"
  archivum__resultata_bag1="${ROOTDIR}/999999/0/unesco-thesaurus~rdfbag1.ttl"
  archivum__resultata_bag2="${ROOTDIR}/999999/0/unesco-thesaurus~rdfbag2.ttl"
  archivum__resultata_ttl="${ROOTDIR}/999999/0/unesco-thesaurus.rdf.ttl"
  archivum__resultata_xml="${ROOTDIR}/999999/0/unesco-thesaurus.rdf.xml"

  set -x
  "${ROOTDIR}/999999999/0/999999999_54872.py" \
    --objectivum-formato=_temp_bcp47_meta_in_json \
    --rdf-namespaces-archivo=999999999/1568346/data/hxlstandard-rdf-namespaces-example.hxl.csv \
    999999999/1568346/data/unesco-thesaurus.bcp47g.tsv |
    jq >999999/1568346/data/unesco-thesaurus.meta.json

  "${ROOTDIR}/999999999/0/999999999_54872.py" \
    --objectivum-formato=_temp_bcp47 \
    --rdf-bag=1 \
    --rdf-namespaces-archivo="${archivum__namespace}" \
    "${archivum__unesco_thesaurus_bcp47}" |
    rapper --quiet --input=turtle --output=turtle /dev/fd/0 \
      >"${archivum__resultata_bag1}"

  "${ROOTDIR}/999999999/0/999999999_54872.py" \
    --objectivum-formato=_temp_bcp47 \
    --rdf-bag=2 \
    --rdf-namespaces-archivo="${archivum__namespace}" \
    "${archivum__unesco_thesaurus_bcp47}" |
    rapper --quiet --input=turtle --output=turtle /dev/fd/0 \
      >"${archivum__resultata_bag2}"

  # riot --output=Turtle \
  riot --time --output=RDF/XML \
    "${archivum__resultata_bag1}" \
    "${archivum__resultata_bag2}" \
    >"${archivum__resultata_xml}"

  riot --time --output=Turtle \
    "${archivum__resultata_xml}" \
    >"${archivum__resultata_ttl}"

  riot --validate "${archivum__resultata_ttl}"
  set -x
}

#######################################
# bcp47_and_hxlrdf_roundtrip item
#
# Globals:
#   ROOTDIR
# Arguments:
#   None
# Outputs:
#   Test result
#######################################
bcp47_and_hxlrdf_roundtrip() {
  bpc47="${1-""}"
  hxlattr="${2-""}"
  bpc47_final="${3-""}"
  hxlattr_final="${4-""}"

  hxlattr_discovered=""
  hxlattr_discovered_2nd=""
  bpc47_discovered=""
  bpc47_discovered_2nd=""

  stype_blue=$(tput setaf 4)
  stype_green=$(tput setaf 2)
  style_red=$(tput setaf 1)
  style_normal=$(tput sgr0)

  if [ -n "$bpc47" ]; then
    echo "[$bpc47] bpc47 input"

    hxlattr_discovered=$("${ROOTDIR}/999999999/0/linguacodex.py" \
      --de_bcp47_simplex --de_codex="$bpc47" \
      --quod=._callbacks.hxl_attrs)

    hxlattr_discovered=${hxlattr_discovered//\"/}
    echo "[$hxlattr_discovered] hxlattr_discovered"

    bpc47_discovered_2nd=$("${ROOTDIR}/999999999/0/linguacodex.py" \
      --de_hxl_simplex --de_hxlhashtag="#item${hxlattr_discovered}" \
      --quod=.Language-Tag_normalized)

    bpc47_discovered_2nd=${bpc47_discovered_2nd//\"/}
    echo "[$bpc47_discovered_2nd] bpc47_discovered_2nd"

    if [ -n "$bpc47_final" ]; then
      if [ "$bpc47_final" = "$bpc47_discovered_2nd" ]; then
        echo "${stype_green}OK [$bpc47_final]${style_normal}"
        # printf "$STARTCOLOR%b$ENDCOLOR" "$1";
      else
        echo "${style_red}FAILED [$bpc47_final] != [$bpc47_discovered_2nd] ${style_normal}"
      fi
    else
      echo "${stype_blue}INFO: No enforced expected result${style_normal}"
    fi
  # else
  #   echo "noop bpc47"
  fi

  if [ -n "$hxlattr" ]; then
    echo "[$hxlattr] hxlattr input"

    bpc47_discovered=$("${ROOTDIR}/999999999/0/linguacodex.py" \
      --de_hxl_simplex --de_hxlhashtag="#item${hxlattr}" \
      --quod=.Language-Tag_normalized)

    bpc47_discovered=${bpc47_discovered//\"/}
    echo "[$bpc47_discovered] bpc47_discovered"

    hxlattr_discovered_2nd=$("${ROOTDIR}/999999999/0/linguacodex.py" \
      --de_bcp47_simplex --de_codex="$bpc47_discovered" \
      --quod=._callbacks.hxl_attrs)

    hxlattr_discovered_2nd=${hxlattr_discovered_2nd//\"/}
    echo "[$hxlattr_discovered_2nd] hxlattr_discovered_2nd"

    if [ -n "$hxlattr_final" ]; then
      if [ "$hxlattr_final" = "$hxlattr_discovered_2nd" ]; then
        echo "${stype_green}OK [$hxlattr_final]${style_normal}"
      else
        echo "${style_red}FAILED [$hxlattr_final] != [$hxlattr_discovered_2nd] ${style_normal}"
      fi
    else
      echo "${stype_blue}INFO: No enforced expected result${style_normal}"
    fi

  # else
  #   echo "noop hxlattr"
  fi
  return 0

}

#######################################
# bcp47_and_hxlrdf_roundtrip item
#
# Globals:
#   ROOTDIR
# Arguments:
#   None
# Outputs:
#   Test result
#######################################
bcp47_and_hxlrdf_roundtrip__drill() {

  archivum__regulae_exemplis="${ROOTDIR}/999999999/1568346/bcp47-to-hxl-to-rdf.hxl.tsv"

  echo ""
  echo "    test1"
  bcp47_and_hxlrdf_roundtrip \
    "qcc-Zxxx-r-sU2203-s2-snop" \
    "" \
    "qcc-Zxxx-r-sU2203-s2-snop" \
    ""

  echo ""
  echo "    test2"
  bcp47_and_hxlrdf_roundtrip \
    "" \
    "+i_qcc+is_zxxx+rdf_s_u2203_s2" \
    "" \
    ""

  echo ""
  echo "    test3 (sort output)"
  bcp47_and_hxlrdf_roundtrip \
    "qcc-Zxxx-r-sU2203-s2-snop-yU001D-yu007c-ynop-yU0002-yunescothes-ynop-pSKOS-pbroader-ps2-tXSD-tdatetime-tnop" \
    "" \
    "qcc-Zxxx-r-pSKOS-pbroader-ps2-sU2203-s2-snop-tXSD-tdatetime-tnop-yU0002-yunescothes-ynop-yU001D-yu007c-ynop" \
    ""

  index_now=$((4))

  # Will fail without manual ajusts:
  #  - lat-Latn-r-pSKOS-pprefLabel-ps1

  # while IFS=, read -r iso3 source_url; do
  {
    # remove read -r to not skip first line
    read -r
    while IFS=$'\t' read -r -a linea; do
      bpc47="${linea[0]}"
      hxl="${linea[1]}"
      rdf="${linea[2]}"
      # namespace="${linea[3]}"

      echo ""
      echo "    test ${index_now}"

      bcp47_and_hxlrdf_roundtrip \
        "${bpc47}" \
        "${hxl}" \
        "${bpc47}" \
        "${hxl}"

      # # echo "numerordinatio_praefixo $numerordinatio_praefixo"
      # # bootstrap_1603_45_16__item "1603_45_16_24" "24" "AGO" "AO" "3" "1" "0"
      # bootstrap_1603_45_16__item "$numerordinatio_praefixo" "$unm49" "$v_iso3" "$v_iso2" "$cod_ab_level_max" "1" "0"
      # # bootstrap_1603_45_16__item "$numerordinatio_praefixo" "$unm49" "$v_iso3" "$v_iso2" "1" "0"
      # sleep 5
      index_now=$((index_now + 1))
    done
  } <"${archivum__regulae_exemplis}"
}

# echo "test"

# bcp47_to_hxl_to_rdf__tests
test_unesco_thesaurus

# bcp47_and_hxlrdf_roundtrip__drill

# ./999999999/0/999999999_54872.py --objectivum-formato=_temp_bcp47_meta_in_json --rdf-namespaces-archivo=999999999/1568346/data/hxlstandard-rdf-namespaces-example.hxl.csv 999999999/1568346/data/unesco-thesaurus.bcp47g.tsv | jq > 999999/0/unesco-thesaurus.meta.json

# ./999999999/0/999999999_54872.py --objectivum-formato=_temp_bcp47_meta_in_json --rdf-namespaces-archivo=999999999/1568346/data/hxlstandard-rdf-namespaces-example.hxl.csv 999999999/1568346/data/unesco-thesaurus.bcp47g.tsv | jq > 999999/1568346/data/unesco-thesaurus.meta.json
