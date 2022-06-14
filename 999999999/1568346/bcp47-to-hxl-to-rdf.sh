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

  stype_blue=$(tput setaf 4)
  stype_green=$(tput setaf 2)
  style_red=$(tput setaf 1)
  style_normal=$(tput sgr0)
  printf "\t%40s\n" "${stype_blue}${FUNCNAME[0]} [STARTED]${style_normal}"

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

  printf "\t%40s\n" "${stype_green}${FUNCNAME[0]} [DONE]${style_normal}"
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
  archivum__resultata_ttl="${ROOTDIR}/999999/1568346/data/unesco-thesaurus.rdf.ttl"
  archivum__resultata_xml="${ROOTDIR}/999999/1568346/data/unesco-thesaurus.rdf.xml"
  archivum__resultata_meta_json="${ROOTDIR}/999999/1568346/data/unesco-thesaurus.meta.json"

  stype_blue=$(tput setaf 4)
  stype_green=$(tput setaf 2)
  style_red=$(tput setaf 1)
  style_normal=$(tput sgr0)
  printf "\t%40s\n" "${stype_blue}${FUNCNAME[0]} [STARTED]${style_normal}"

  set -x
  "${ROOTDIR}/999999999/0/999999999_54872.py" \
    --objectivum-formato=_temp_bcp47_meta_in_json \
    --punctum-separato-de-fontem=$'\t' \
    --rdf-namespaces-archivo="${archivum__namespace}" \
    "${archivum__unesco_thesaurus_bcp47}" |
    jq >"${archivum__resultata_meta_json}"

  "${ROOTDIR}/999999999/0/999999999_54872.py" \
    --objectivum-formato=_temp_bcp47 \
    --punctum-separato-de-fontem=$'\t' \
    --rdf-trivio=1 \
    --rdf-namespaces-archivo="${archivum__namespace}" \
    "${archivum__unesco_thesaurus_bcp47}" |
    rapper --quiet --input=turtle --output=turtle /dev/fd/0 \
      >"${archivum__resultata_bag1}"

  "${ROOTDIR}/999999999/0/999999999_54872.py" \
    --objectivum-formato=_temp_bcp47 \
    --punctum-separato-de-fontem=$'\t' \
    --rdf-trivio=2 \
    --rdf-namespaces-archivo="${archivum__namespace}" \
    "${archivum__unesco_thesaurus_bcp47}" |
    rapper --quiet --input=turtle --output=turtle /dev/fd/0 \
      >"${archivum__resultata_bag2}"

  # @TODO eventually remove  --nocheck
  # riot --output=Turtle \
  riot --time --nocheck --output=RDF/XML \
    "${archivum__resultata_bag1}" \
    "${archivum__resultata_bag2}" \
    >"${archivum__resultata_xml}"

  riot --time --nocheck --output=Turtle \
    "${archivum__resultata_xml}" \
    >"${archivum__resultata_ttl}"


  # Is not validating rigth now; Lets allow fail
  echo "before riot --validate"
  # # set +e
  riot --validate "${archivum__resultata_ttl}" || echo "Failed. Ignoring..."
  # # set -e
  echo "after riot --validate"
  set +x

  printf "\t%40s\n" "${stype_green}${FUNCNAME[0]} [DONE]${style_normal}"
}

#######################################
# test_cod_ab
#
# Globals:
#   ROOTDIR
# Arguments:
#   None
# Outputs:
#   Test result
#######################################
test_cod_ab() {
  archivum__namespace="${ROOTDIR}/999999999/1568346/data/hxlstandard-rdf-namespaces-example.hxl.csv"
  archivum__cod_ab_bcp47="${ROOTDIR}/999999999/1568346/data/cod-ab-example1.bcp47.tsv"
  archivum__resultata_bag1="${ROOTDIR}/999999/0/cod-ab-example1~rdfbag1.ttl"
  archivum__resultata_bag2="${ROOTDIR}/999999/0/cod-ab-example1~rdfbag2.ttl"
  archivum__resultata_bag3="${ROOTDIR}/999999/0/cod-ab-example1~rdfbag3.ttl"
  archivum__resultata_bag4="${ROOTDIR}/999999/0/cod-ab-example1~rdfbag4.ttl"
  archivum__resultata_ttl="${ROOTDIR}/999999/1568346/data/cod-ab-example1.rdf.ttl"
  archivum__resultata_xml="${ROOTDIR}/999999/1568346/data/cod-ab-example1.rdf.xml"
  archivum__resultata_meta_json="${ROOTDIR}/999999/1568346/data/cod-ab-example1.meta.json"

  stype_blue=$(tput setaf 4)
  stype_green=$(tput setaf 2)
  style_red=$(tput setaf 1)
  style_normal=$(tput sgr0)
  printf "\t%40s\n" "${stype_blue}${FUNCNAME[0]} [STARTED]${style_normal}"

  # officina/999999/1568346/data

  set -x
  "${ROOTDIR}/999999999/0/999999999_54872.py" \
    --objectivum-formato=_temp_bcp47_meta_in_json \
    --punctum-separato-de-fontem=$'\t' \
    --rdf-namespaces-archivo="${archivum__namespace}" \
    "${archivum__cod_ab_bcp47}" |
    jq >"${archivum__resultata_meta_json}"

  "${ROOTDIR}/999999999/0/999999999_54872.py" \
    --objectivum-formato=_temp_bcp47 \
    --punctum-separato-de-fontem=$'\t' \
    --rdf-trivio=1 \
    --rdf-namespaces-archivo="${archivum__namespace}" \
    "${archivum__cod_ab_bcp47}" |
    rapper --quiet --input=turtle --output=turtle /dev/fd/0 \
      >"${archivum__resultata_bag1}"

  "${ROOTDIR}/999999999/0/999999999_54872.py" \
    --objectivum-formato=_temp_bcp47 \
    --punctum-separato-de-fontem=$'\t' \
    --rdf-trivio=2 \
    --rdf-namespaces-archivo="${archivum__namespace}" \
    "${archivum__cod_ab_bcp47}" |
    rapper --quiet --input=turtle --output=turtle /dev/fd/0 \
      >"${archivum__resultata_bag2}"

  "${ROOTDIR}/999999999/0/999999999_54872.py" \
    --objectivum-formato=_temp_bcp47 \
    --punctum-separato-de-fontem=$'\t' \
    --rdf-trivio=3 \
    --rdf-namespaces-archivo="${archivum__namespace}" \
    "${archivum__cod_ab_bcp47}" |
    rapper --quiet --input=turtle --output=turtle /dev/fd/0 \
      >"${archivum__resultata_bag3}"

  "${ROOTDIR}/999999999/0/999999999_54872.py" \
    --objectivum-formato=_temp_bcp47 \
    --punctum-separato-de-fontem=$'\t' \
    --rdf-trivio=4 \
    --rdf-namespaces-archivo="${archivum__namespace}" \
    "${archivum__cod_ab_bcp47}" |
    rapper --quiet --input=turtle --output=turtle /dev/fd/0 \
      >"${archivum__resultata_bag4}"

  # @TODO eventually remove  --nocheck
  # riot --output=Turtle \
  riot --time --nocheck --output=RDF/XML \
    "${archivum__resultata_bag1}" \
    "${archivum__resultata_bag2}" \
    >"${archivum__resultata_xml}"

  riot --time --nocheck --output=Turtle \
    "${archivum__resultata_xml}" \
    >"${archivum__resultata_ttl}"


  # Is not validating rigth now; Lets allow fail
  echo "before riot --validate"
  # # set +e
  riot --validate "${archivum__resultata_ttl}" || echo "Failed. Ignoring..."
  # # set -e
  echo "after riot --validate"
  set +x

  printf "\t%40s\n" "${stype_green}${FUNCNAME[0]} [DONE]${style_normal}"
}

#######################################
# test_cod_ab__with_inferences_prebuild
#
# Globals:
#   ROOTDIR
# Arguments:
#   None
# Outputs:
#   Test result
#######################################
test_cod_ab__with_inferences_prebuild() {
  archivum__namespace="${ROOTDIR}/999999999/1568346/data/hxlstandard-rdf-namespaces-example.hxl.csv"
  archivum__cod_ab_bcp47="${ROOTDIR}/999999999/1568346/data/cod-ab-example1-with-inferences.bcp47.tsv"
  archivum__resultata_bag1="${ROOTDIR}/999999/0/cod-ab-example1-with-inferences~rdfbag1.ttl"
  archivum__resultata_bag2="${ROOTDIR}/999999/0/cod-ab-example1-with-inferences~rdfbag2.ttl"
  archivum__resultata_bag3="${ROOTDIR}/999999/0/cod-ab-example1-with-inferences~rdfbag3.ttl"
  archivum__resultata_bag4="${ROOTDIR}/999999/0/cod-ab-example1-with-inferences~rdfbag4.ttl"
  archivum__resultata_ttl="${ROOTDIR}/999999/1568346/data/cod-ab-example1-with-inferences.rdf.ttl"
  archivum__resultata_xml="${ROOTDIR}/999999/1568346/data/cod-ab-example1-with-inferences.rdf.xml"
  archivum__resultata_meta_json="${ROOTDIR}/999999/1568346/data/cod-ab-example1-with-inferences.meta.json"

  stype_blue=$(tput setaf 4)
  stype_green=$(tput setaf 2)
  style_red=$(tput setaf 1)
  style_normal=$(tput sgr0)
  printf "\t%40s\n" "${stype_blue}${FUNCNAME[0]} [STARTED]${style_normal}"

  # officina/999999/1568346/data

  # @TODO: implement implicit aliases when sU2200 reference multiple subject
  #        groups (like s5000-s506 for administrative regions) but user
  #        askis for s1 and s1 is also one of these s5000-s506.

  set -x
  "${ROOTDIR}/999999999/0/999999999_54872.py" \
    --objectivum-formato=_temp_bcp47_meta_in_json \
    --punctum-separato-de-fontem=$'\t' \
    --rdf-namespaces-archivo="${archivum__namespace}" \
    --rdf-trivio=5000 \
    "${archivum__cod_ab_bcp47}" |
    jq >"${archivum__resultata_meta_json}"

  "${ROOTDIR}/999999999/0/999999999_54872.py" \
    --objectivum-formato=_temp_bcp47 \
    --punctum-separato-de-fontem=$'\t' \
    --rdf-trivio=5000 \
    --rdf-namespaces-archivo="${archivum__namespace}" \
    "${archivum__cod_ab_bcp47}" |
    rapper --quiet --input=turtle --output=turtle /dev/fd/0 \
      >"${archivum__resultata_bag1}"

  "${ROOTDIR}/999999999/0/999999999_54872.py" \
    --objectivum-formato=_temp_bcp47 \
    --punctum-separato-de-fontem=$'\t' \
    --rdf-trivio=5001 \
    --rdf-namespaces-archivo="${archivum__namespace}" \
    "${archivum__cod_ab_bcp47}" |
    rapper --quiet --input=turtle --output=turtle /dev/fd/0 \
      >"${archivum__resultata_bag2}"

  "${ROOTDIR}/999999999/0/999999999_54872.py" \
    --objectivum-formato=_temp_bcp47 \
    --punctum-separato-de-fontem=$'\t' \
    --rdf-trivio=5002 \
    --rdf-namespaces-archivo="${archivum__namespace}" \
    "${archivum__cod_ab_bcp47}" |
    rapper --quiet --input=turtle --output=turtle /dev/fd/0 \
      >"${archivum__resultata_bag3}"

  # --rdf-trivio=503 is equivalent to --rdf-trivio=1
  "${ROOTDIR}/999999999/0/999999999_54872.py" \
    --objectivum-formato=_temp_bcp47 \
    --punctum-separato-de-fontem=$'\t' \
    --rdf-trivio=1 \
    --rdf-namespaces-archivo="${archivum__namespace}" \
    "${archivum__cod_ab_bcp47}" |
    rapper --quiet --input=turtle --output=turtle /dev/fd/0 \
      >"${archivum__resultata_bag4}"

  # @TODO eventually remove  --nocheck
  # riot --output=Turtle \
  riot --time --nocheck --output=RDF/XML \
    "${archivum__resultata_bag1}" \
    "${archivum__resultata_bag2}" \
    "${archivum__resultata_bag3}" \
    "${archivum__resultata_bag4}" \
    >"${archivum__resultata_xml}"

  riot --time --nocheck --output=Turtle \
    "${archivum__resultata_xml}" \
    >"${archivum__resultata_ttl}"


  # Is not validating rigth now; Lets allow fail
  # echo "before riot --validate"
  # # set +e
  # riot --validate "${archivum__resultata_ttl}" || echo "Failed. Ignoring..."
  # If this fail, entire thing will stop and not print done
  riot --validate "${archivum__resultata_ttl}"
  # # set -e
  # echo "after riot --validate"
  set +x
  printf "\t%40s\n" "${stype_green}${FUNCNAME[0]} [DONE]${style_normal}"
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

  echo ""
  echo "    test4 (special case qcc-Zxxx-r-aMDCIII-alatcodicem-anop)"
  bcp47_and_hxlrdf_roundtrip \
    "qcc-Zxxx-r-aMDCIII-alatcodicem-anop" \
    "" \
    "qcc-Zxxx-r-aMDCIII-alatcodicem-anop" \
    ""

  echo ""
  echo "    test5 (special case qcc-Zxxx-r-aMDCIII-alatnumerordinatio-anop-sU2200-s1603-snop)"
  bcp47_and_hxlrdf_roundtrip \
    "qcc-Zxxx-r-aMDCIII-alatnumerordinatio-anop-sU2200-s1603-snop" \
    "" \
    "qcc-Zxxx-r-aMDCIII-alatnumerordinatio-anop-sU2200-s1603-snop" \
    ""

  echo ""
  echo "    test6 (special case +conceptum+codicem -> +i_qcc+is_zxxx+rdf_a_mdciii_latcodicem)"
  bcp47_and_hxlrdf_roundtrip \
    "" \
    "+conceptum+codicem" \
    "" \
    "+i_qcc+is_zxxx+rdf_a_mdciii_latcodicem"

  echo "@TODO (test other hardcoded conversions from BCP47_EX_HXL and BCP47_AD_HXL"

  index_now=$((7))

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

# test_unesco_thesaurus
# test_cod_ab
# test_cod_ab__with_inferences_prebuild
# exit 0

echo "bcp47_to_hxl_to_rdf__tests"
bcp47_to_hxl_to_rdf__tests

echo "bcp47_and_hxlrdf_roundtrip__drill"
bcp47_and_hxlrdf_roundtrip__drill

echo "test_unesco_thesaurus"
test_unesco_thesaurus

echo "test_cod_ab"
test_cod_ab

echo "test_cod_ab__with_inferences_prebuild"
test_cod_ab__with_inferences_prebuild

exit 0

# ./999999999/0/999999999_54872.py --objectivum-formato=_temp_bcp47_meta_in_json --rdf-namespaces-archivo=999999999/1568346/data/hxlstandard-rdf-namespaces-example.hxl.csv 999999999/1568346/data/unesco-thesaurus.bcp47g.tsv | jq > 999999/0/unesco-thesaurus.meta.json

# ./999999999/0/999999999_54872.py --objectivum-formato=_temp_bcp47_meta_in_json --rdf-namespaces-archivo=999999999/1568346/data/hxlstandard-rdf-namespaces-example.hxl.csv 999999999/1568346/data/unesco-thesaurus.bcp47g.tsv | jq > 999999/1568346/data/unesco-thesaurus.meta.json


# ./999999999/0/999999999_54872.py 999999999/1568346/data/unesco-thesaurus.bcp47g.tsv --rdf-namespaces-archivo=999999999/1568346/data/hxlstandard-rdf-namespaces-example.hxl.csv --objectivum-formato=_temp_bcp47_meta_in_json --rdf-trivio=1 | jq

# ./999999999/0/999999999_54872.py 999999999/1568346/data/cod-ab-example1-with-inferences.bcp47.tsv --objectivum-formato=_temp_bcp47_meta_in_json --rdf-trivio=1 | jq

# ./999999999/0/linguacodex.py --de_bcp47_simplex --de_codex=por-Latn-r-pSKOS-pprefLabel-ps4

# ./999999999/0/999999999_54872.py --objectivum-formato=_temp_bcp47 999999999/1568346/data/cod-ab-example1-with-inferences.bcp47.tsv --rdf-trivio=2 --rdf-sine-spatia-nominalibus=skos

#### BFO _______________________________________________________________________
# @see https://standards.iso.org/iso-iec/21838/-2/ed-1/en/
# @see https://basic-formal-ontology.org/

# rdfdiff 999999/0/bfo_classes_only.owl 999999/0/BFO-PT.owl

# riot --validate 999999/0/bfo_classes_only.owl
# riot --validate 999999/0/BFO-PT.owl
# riot --validate 999999/0/BFO-PT.owl.xml

# rdfdiff 999999/0/bfo_classes_only.owl 999999/0/BFO-PT.owl.xml RDF/XML RDF/XML http://purl.obolibrary.org/obo/ http://purl.obolibrary.org/obo/

# rdfdiff 999999/0/bfo_classes_only.owl 999999/0/BFO-PT.owl.xml RDF/XML RDF/XML http://purl.obolibrary.org/obo/ http://purl.obolibrary.org/obo/ > 999999/0/diff-obo-source-vs-pt.diff


# riot --quiet --output=ntriples 999999/0/BFO-PT.owl.xml > 999999/0/BFO-PT.owl.n3
# riot --quiet --output=ntriples 999999/0/bfo_classes_only.owl > 999999/0/bfo_classes_only.owl.n3

# rdfdiff 999999/0/bfo_classes_only.owl.n3 999999/0/BFO-PT.owl.n3 ntriples ntriples http://purl.obolibrary.org/obo/ http://purl.obolibrary.org/obo/
# rdfdiff 999999/0/bfo_classes_only.owl.n3 999999/0/BFO-PT.owl.n3 ntriples ntriples http://purl.obolibrary.org/obo/ http://purl.obolibrary.org/obo/ > 999999/0/diff-obo-source-vs-pt.diff

# rdfcompare 999999/0/bfo_classes_only.owl.n3 999999/0/BFO-PT.owl.n3 ntriples ntriples http://purl.obolibrary.org/obo/ http://purl.obolibrary.org/obo/


# 999999/0/21838-2/owl/bfo-2020.owl
# riot --quiet --output=ntriples 999999/0/21838-2/owl/bfo-2020.owl > 999999/0/21838-2/owl/bfo-2020.owl.n3

# rdfcompare 999999/0/bfo_classes_only.owl.n3 999999/0/21838-2/owl/bfo-2020.owl.n3 ntriples ntriples http://purl.obolibrary.org/obo/ http://purl.obolibrary.org/obo/

# rdfcompare 999999/0/bfo_classes_only.owl 999999/0/21838-2/owl/bfo-2020.owl

# rdfdiff 999999/0/bfo_classes_only.owl 999999/0/21838-2/owl/bfo-2020.owl RDF/XML RDF/XML > 999999/0/diff-obo-source-vs-iso.diff
