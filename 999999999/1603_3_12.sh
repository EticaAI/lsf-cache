#!/bin/bash
#===============================================================================
#
#          FILE:  1603_3_12.sh
#
#         USAGE:  ./999999999/1603_3_12.sh
#                 time ./999999999/1603_3_12.sh
#
#   DESCRIPTION:  ---
#
#       OPTIONS:  ---
#
#  REQUIREMENTS:  - Bash shell (or better)
#                 - wikibase-cli (https://github.com/maxlath/wikibase-cli)
#          BUGS:  ---
#         NOTES:  ---
#        AUTHOR:  Emerson Rocha <rocha[at]ieee.org>
#       COMPANY:  EticaAI
#       LICENSE:  Public Domain dedication or Zero-Clause BSD
#                 SPDX-License-Identifier: Unlicense OR 0BSD
#       VERSION:  v1.0
#       CREATED:  2022-01-10 11:03 UTC
#      REVISION:  ---
#===============================================================================
# Comment next line if not want to stop on first error
set -e

ROOTDIR="$(pwd)"

# shellcheck source=999999999.lib.sh
. "$ROOTDIR"/999999999/999999999.lib.sh

# @see https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/queries/examples
# @see https://github.com/maxlath/wikibase-cli
# @see - https://www.wikidata.org/wiki/Template:Wikidata_list
#        - http://magnusmanske.de/wordpress/?p=301
# https://www.wikidata.org/wiki/Property:P299
# ISO 3166-1 numeric code (P299)

# @see also https://www.wikidata.org/wiki/Wikidata:List_of_properties
#  - UN/LOCODE (P1937) https://www.wikidata.org/wiki/Property:P1937
#  - M.49 code (P2082)
#  - UNDP country code (P2983)
#    - This seems to be not used on last decade

# TODO: https://w.wiki/4fMq
# # organização estabelecida pelas Nações Unidas (Q15285626)
# SELECT ?wikidataq  ?wikidataqLabel WHERE {
#    ?wikidataq wdt:P31 wd:Q15285626 .
#    SERVICE wikibase:label {
#     bd:serviceParam wikibase:language "en" .
#    }

#  } ORDER BY ?start

#######################################
# Return list of administrative level 0 codes ("country/territory" codes)
#
# Globals:
#   None
# Arguments:
#   None
# Outputs:
#   csvfile (stdout)
#######################################
1603_3_12_wikipedia_adm0() {
  # fontem_archivum=
  objectivum_archivum="${ROOTDIR}/1603/3/1603_3__adm0.csv"
  objectivum_archivum_temporarium="${ROOTDIR}/1603/3/1603_3__adm0.TEMP.csv"

  if [ -z "$(stale_archive "$objectivum_archivum")" ]; then return 0; fi

  echo "${FUNCNAME[0]} stale data on [$objectivum_archivum], refreshing..."

  curl --header "Accept: text/csv" --silent --show-error \
    --get https://query.wikidata.org/sparql --data-urlencode query='
SELECT ?country ?unm49 ?iso3166n ?iso3166p1a2 ?iso3166p1a3 ?osmrelid ?unescot ?usciafb ?usfips4 ?gadm
WHERE
{
  ?country wdt:P31 wd:Q6256 ;
  OPTIONAL { ?country wdt:P2082 ?unm49. }
  OPTIONAL { ?country wdt:P299 ?iso3166n. }
  OPTIONAL { ?country wdt:P297 ?iso3166p1a2. }
  OPTIONAL { ?country wdt:P298 ?iso3166p1a3. }
  OPTIONAL { ?country wdt:P402 ?osmrelid. }
  OPTIONAL { ?country wdt:P3916 ?unescot. }
  OPTIONAL { ?country wdt:P9948 ?usciafb. }
  OPTIONAL { ?country wdt:P901 ?usfips4. }
  OPTIONAL { ?country wdt:P8714 ?gadm. }   

  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE]". }
}
' >"$objectivum_archivum_temporarium"

  file_update_if_necessary csv "$objectivum_archivum_temporarium" "$objectivum_archivum"
}

#######################################
# Return list of administrative level 0 codes ("country/territory" codes)
#
# Globals:
#   None
# Arguments:
#   None
# Outputs:
#   csvfile (stdout)
#######################################
1603_3_12_wikipedia_adm0_v2() {
  # fontem_archivum=
  objectivum_archivum="${ROOTDIR}/1603/3/1603_3__adm0_v2.csv"
  objectivum_archivum_temporarium="${ROOTDIR}/1603/3/1603_3__adm0_v2.TEMP.csv"
  objectivum_archivum_temporarium_hxltm="${ROOTDIR}/1603/3/1603_3__adm0_v2.TEMP.tm.hxl.csv"
  objectivum_archivum_hxltm="${ROOTDIR}/1603/3/1603_3__adm0.tm.hxl.csv"

  # if [ -z "$(stale_archive "$objectivum_archivum")" ]; then return 0; fi

  echo "${FUNCNAME[0]} stale data on [$objectivum_archivum], refreshing..."

  curl --header "Accept: text/csv" --silent --show-error \
    --get https://query.wikidata.org/sparql --data-urlencode query='
SELECT
  (xsd:integer(?ix_iso3166p1n) AS ?item__conceptum__codicem)
  (STRAFTER(STR(?item), "entity/") AS ?item__rem__i_qcc__is_zxxx__ix_wikiq)
  #?item__rem__i_qcc__is_zxxx__ix_iso3166p1n
  (GROUP_CONCAT(DISTINCT ?ix_iso3166p1n; separator = "|") AS ?item__rem__i_qcc__is_zxxx__ix_iso3166p1n)
  (GROUP_CONCAT(DISTINCT ?ix_unm49; separator = "|") AS ?item__rem__i_qcc__is_zxxx__ix_unm49)
  (GROUP_CONCAT(DISTINCT ?ix_iso3166p1a2; separator = "|") AS ?item__rem__i_qcc__is_zxxx__ix_iso3166p1a2)
  (GROUP_CONCAT(DISTINCT ?ix_iso3166p1a3; separator = "|") AS ?item__rem__i_qcc__is_zxxx__ix_iso3166p1a3)
  (GROUP_CONCAT(DISTINCT ?ix_unescothes; separator = "|") AS ?item__rem__i_qcc__is_zxxx__ix_unescothes)
  (GROUP_CONCAT(DISTINCT ?ix_unagrovoc; separator = "|") AS ?item__rem__i_qcc__is_zxxx__ix_unagrovoc)
  (GROUP_CONCAT(DISTINCT ?ix_osmrelid; separator = "|") AS ?item__rem__i_qcc__is_zxxx__ix_osmrelid)
  (GROUP_CONCAT(DISTINCT ?ix_geonames; separator = "|") AS ?item__rem__i_qcc__is_zxxx__ix_geonames)
  (GROUP_CONCAT(DISTINCT ?ix_geonlp; separator = "|") AS ?item__rem__i_qcc__is_zxxx__ix_geonlp)
  (GROUP_CONCAT(DISTINCT ?ix_worldnet; separator = "|") AS ?item__rem__i_qcc__is_zxxx__ix_worldnet)
  (GROUP_CONCAT(DISTINCT ?ix_usciafb; separator = "|") AS ?item__rem__i_qcc__is_zxxx__ix_usciafb)
  (GROUP_CONCAT(DISTINCT ?ix_githubtopic; separator = "|") AS ?item__rem__i_qcc__is_zxxx__ix_githubtopic)

WHERE
{
  ?item wdt:P31 wd:Q6256 ;
  OPTIONAL { ?item wdt:P2082 ?ix_unm49. }
  ?item wdt:P299 ?ix_iso3166p1n.
  OPTIONAL { ?item wdt:P297 ?ix_iso3166p1a2. }
  OPTIONAL { ?item wdt:P298 ?ix_iso3166p1a3. }
  OPTIONAL { ?item wdt:P3916 ?ix_unescothes. }
  OPTIONAL { ?item wdt:P8061 ?ix_unagrovoc. }
  OPTIONAL { ?item wdt:P402 ?ix_osmrelid. }
  OPTIONAL { ?item wdt:P9100 ?ix_geonames. }
  OPTIONAL { ?item wdt:P5400 ?ix_geonlp. }
  OPTIONAL { ?item wdt:P8814 ?ix_worldnet. }
  OPTIONAL { ?item wdt:P9948 ?ix_usciafb. }
  OPTIONAL { ?item wdt:P9100 ?ix_githubtopic. }
}
GROUP BY ?item ?ix_iso3166p1n
ORDER BY ASC(?item__rem__i_qcc__is_zxxx__ix_iso3166p1n)
' >"$objectivum_archivum_temporarium"

  frictionless validate "$objectivum_archivum_temporarium"

  caput_csvnormali=$(head -n1 "$objectivum_archivum_temporarium")
  caput_hxltm=$(caput_csvnormali_ad_hxltm "${caput_csvnormali}" ",")

  echo "$caput_hxltm" > "$objectivum_archivum_temporarium_hxltm"
  tail -n +2 "$objectivum_archivum_temporarium" >> "$objectivum_archivum_temporarium_hxltm"

  file_update_if_necessary csv "$objectivum_archivum_temporarium" "$objectivum_archivum"
  file_update_if_necessary csv "$objectivum_archivum_temporarium_hxltm" "$objectivum_archivum_hxltm"
}

#######################################
# Return Wikipedia/Wikidata language codes (used to know how many
# languages do wikipedia have)
#
# Globals:
#   None
# Arguments:
#   None
# Outputs:
#   csvfile (stdout)
#######################################
1603_3_12_wikipedia_language_codes() {
  # fontem_archivum=
  objectivum_archivum="${ROOTDIR}/1603/3/1603_3__languages.csv"
  objectivum_archivum_temporarium="${ROOTDIR}/1603/3/1603_3__languages.TEMP.csv"

  if [ -z "$(stale_archive "$objectivum_archivum")" ]; then return 0; fi

  echo "${FUNCNAME[0]} stale data on [$objectivum_archivum], refreshing..."

  # TODO: this alternative query only select the Wikipedia ones
  # #title: All languages with a Wikimedia language code (P424)
  # # Date: 2021-09-24
  # SELECT DISTINCT ?lang_code ?itemLabel ?item
  # WHERE
  # {
  #   # ?lang is one of these options
  #   VALUES ?lang {
  #     wd:Q34770   # language
  #     wd:Q436240  # ancient language
  #     wd:Q1288568 # modern language
  #     wd:Q33215   # constructed language
  #   }
  #   ?item wdt:P31 ?lang ;
  #     # get the language code
  #     wdt:P424 ?lang_code .
  #   SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
  # } ORDER BY ?lang_code

  curl --header "Accept: text/csv" --silent --show-error \
    --get https://query.wikidata.org/sparql --data-urlencode query='
SELECT ?wd ?wmCode ?iso6391 ?iso6392 ?iso6393 ?iso6396 ?native ?label {
  VALUES (?language_type) { (wd:Q34770) (wd:Q25295) }
  ?wd wdt:P31/wdt:P279* ?language_type
      
  { ?wd wdt:P218 ?iso6391 . } UNION
  { ?wd wdt:P219 ?iso6392 . } UNION
  { ?wd wdt:P220 ?iso6393 . } UNION
  { ?wd wdt:P221 ?iso6396 . }

  # OPTIONAL { ?wd wdt:P424 ?wmCode . }
  ?wd wdt:P424 ?wmCode .
  OPTIONAL { ?wd wdt:P1705 ?native }
  OPTIONAL {
    ?wd rdfs:label ?label
    FILTER(LANG(?label) = "en")
  }
}
order by (?wmCode)
' >"$objectivum_archivum_temporarium"

  file_update_if_necessary csv "$objectivum_archivum_temporarium" "$objectivum_archivum"
}

# caput_csvnormali_ad_hxltm "item__conceptum__codicem" ","
# echo ""
# caput_csvnormali_ad_hxltm "item__conceptum__codicem,item__rem__i_qcc__is_zxxx__ix_wikiq" ","
# echo ""
# echo ""
# caput_hxltm_ad_csvnormali "#item+conceptum+codicem" ","
# echo ""
# caput_hxltm_ad_csvnormali "#item+conceptum+codicem,#item+rem+i_qcc+is_zxxx+ix_wikiq" ","
# echo ""
# echo ""
# caput_hxltm_ad_bcp47 "#item+conceptum+codicem,#item+rem+i_qcc+is_zxxx+ix_wikiq" ","
# echo ""
# echo ""
# echo ""
# caput_bcp47_ad_hxltm_ad "qcc-Zxxx-r-aMDCIII-alatcodicem-anop,qcc-Zxxx-x-wikiq" ","
# echo ""
# # caput_hxltm_ad_bcp47 "#item+conceptum+codicem" ","
# # echo ""
# # caput_hxltm_ad_bcp47 "#item+rem+i_qcc+is_zxxx+ix_wikiq" ","
# # echo ""
# exit 0

1603_3_12_wikipedia_language_codes

1603_3_12_wikipedia_adm0

1603_3_12_wikipedia_adm0_v2

# temp, see later
# - https://www.wikidata.org/wiki/Help:Frequently_used_properties
# - https://www.wikidata.org/wiki/Property:P3896
# - https://www.wikidata.org/wiki/Wikidata:Map_data

exit 0

# TODO: maybe check https://www.npmjs.com/package/wikidata-taxonomy
#       npm install -g wikidata-taxonomy
# Examples
# wdtaxonomy P2082

### Current query for download translations (have bugs)
# # Variant of
# # - https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/queries/examples#UN_member_states
# # - https://stackoverflow.com/questions/43258341/how-to-get-wikidata-labels-in-more-than-one-language
# PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
# PREFIX wikibase: <http://wikiba.se/ontology#>
# PREFIX wd: <http://www.wikidata.org/entity/>
# PREFIX wdt: <http://www.wikidata.org/prop/direct/>

# #SELECT DISTINCT ?adm0 ?iso3166p1n ?label (lang(?label) as ?label_lang)
# SELECT DISTINCT ?iso3166p1n ?label (lang(?label) as ?label_lang)
# {
#   ?adm0 wdt:P31/wdt:P279* wd:Q3624078;
#   rdfs:label ?label
#   OPTIONAL { ?adm0 wdt:P2082|wdt:P299 ?iso3166p1n. }

#   #FILTER(?iso3166p1n > xsd:integer(0))
# }
# # order by ?adm0
# order by ASC(?iso3166p1n)
# LIMIT 1000
