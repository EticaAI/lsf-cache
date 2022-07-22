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
# COD AB Index + Wikidata Adm0
#
# Globals:
#   None
# Arguments:
#   None
# Outputs:
#   csvfile (stdout)
#######################################
1603_3_12_cod_ab_et_wdata() {

  # objectivum_archivum="${ROOTDIR}/1603/3/1603_3__adm0.csv"
  # objectivum_archivum_temporarium="${ROOTDIR}/1603/3/1603_3__adm0.TEMP.csv"
  # objectivum_archivum_hxltm_999999="${ROOTDIR}/999999/1603/3/45/16/1/1/1603_3_45_16_1_1.tm.hxl.csv"
  objectivum_archivum_temporarium="${ROOTDIR}/999999/0/1603_3_45_16_1_1.tm.hxl.csv"

  set -x
  "${ROOTDIR}/999999999/0/999999999_7200235.py" \
    --methodus='cod_ab_et_wdata' \
    --numerordinatio-praefixo='1603_16' \
    >"$objectivum_archivum_temporarium"
  set +x

  # file_update_if_necessary csv "$objectivum_archivum_temporarium" "$objectivum_archivum"
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
1603_3_12_wikipedia_adm0() {
  # fontem_archivum=

  echo "DEPRECATED"
  return 0

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
# Other generic functions can be used to extract the .wikiq.tm.hxl.csv
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
  # objectivum_archivum="${ROOTDIR}/1603/3/1603_3__adm0_v2.csv"
  # objectivum_archivum_temporarium="${ROOTDIR}/1603/3/1603_3__adm0_v2.TEMP.csv"
  objectivum_archivum="${ROOTDIR}/999999/0/1603_3__adm0_v2.csv"
  objectivum_archivum_temporarium="${ROOTDIR}/999999/0/1603_3__adm0_v2.TEMP.csv"
  objectivum_archivum_temporarium_hxltm="${ROOTDIR}/999999/0/1603_3__adm0_v2.TEMP.tm.hxl.csv"
  # objectivum_archivum_hxltm="${ROOTDIR}/999999/0/1603_3__adm0.tm.hxl.csv"
  # objectivum_archivum_hxltm_999999="${ROOTDIR}/999999/1603/3/45/16/1/1/1603_3_45_16_1_1.tm.hxl.csv"
  objectivum_archivum_hxltm_999999="${ROOTDIR}/999999/1603/3/45/16/1/1/1603_3_45_16_1_1.no1.tm.hxl.csv"

  # if [ -z "$(stale_archive "$objectivum_archivum")" ]; then return 0; fi

  echo "${FUNCNAME[0]} stale data on [$objectivum_archivum], refreshing..."

  curl --header "Accept: text/csv" --silent --show-error \
    --get https://query.wikidata.org/sparql --data-urlencode query='
SELECT
  (xsd:integer(?ix_unm49) AS ?item__conceptum__codicem)
  (STRAFTER(STR(?item), "entity/") AS ?item__rem__i_qcc__is_zxxx__ix_wikiq)
  (GROUP_CONCAT(DISTINCT ?ix_iso3166p1n; separator = "|") AS ?item__rem__i_qcc__is_zxxx__ix_iso3166p1n)
  (GROUP_CONCAT(DISTINCT ?ix_unm49; separator = "|") AS ?item__rem__i_qcc__is_zxxx__ix_unm49)
  (GROUP_CONCAT(DISTINCT ?ix_iso3166p1a2; separator = "|") AS ?item__rem__i_qcc__is_zxxx__ix_iso3166p1a2)
  (GROUP_CONCAT(DISTINCT ?ix_iso3166p1a3; separator = "|") AS ?item__rem__i_qcc__is_zxxx__ix_iso3166p1a3)
  (GROUP_CONCAT(DISTINCT ?ix_iso3166p2; separator = "|") AS ?item__rem__i_qcc__is_zxxx__ix_iso3166p2)
  (GROUP_CONCAT(DISTINCT ?ix_unescothes; separator = "|") AS ?item__rem__i_qcc__is_zxxx__ix_unescothes)
  (GROUP_CONCAT(DISTINCT ?ix_unagrovoc; separator = "|") AS ?item__rem__i_qcc__is_zxxx__ix_unagrovoc)
  (GROUP_CONCAT(DISTINCT ?ix_xzosmrel; separator = "|") AS ?item__rem__i_qcc__is_zxxx__ix_xzosmrel)
  (GROUP_CONCAT(DISTINCT ?ix_xzgeonames; separator = "|") AS ?item__rem__i_qcc__is_zxxx__ix_xzgeonames)
  (GROUP_CONCAT(DISTINCT ?ix_jpgeolod; separator = "|") AS ?item__rem__i_qcc__is_zxxx__ix_jpgeolod)
  (GROUP_CONCAT(DISTINCT ?ix_usworldnet; separator = "|") AS ?item__rem__i_qcc__is_zxxx__ix_usworldnet)
  (GROUP_CONCAT(DISTINCT ?ix_usfactbook; separator = "|") AS ?item__rem__i_qcc__is_zxxx__ix_usfactbook)
  (GROUP_CONCAT(DISTINCT ?ix_xzgithubt; separator = "|") AS ?item__rem__i_qcc__is_zxxx__ix_xzgithubt)
  (GROUP_CONCAT(DISTINCT ?ix_zzwgs84point; separator = "|") AS ?item__rem__i_qcc__is_zxxx__ix_zzwgs84point)
  (GROUP_CONCAT(DISTINCT ?ix_zzgeojson; separator = "|") AS ?item__rem__i_qcc__is_zxxx__ix_zzgeojson)

WHERE
{
  ?item wdt:P31 wd:Q6256 ;
  wdt:P2082 ?ix_unm49 ;
  OPTIONAL { ?item wdt:P299 ?ix_iso3166p1n . }
  OPTIONAL { ?item wdt:P297 ?ix_iso3166p1a2 . }
  OPTIONAL { ?item wdt:P298 ?ix_iso3166p1a3 . }
  OPTIONAL { ?item wdt:P300 ?ix_iso3166p2 . }
  OPTIONAL { ?item wdt:P3916 ?ix_unescothes . }
  OPTIONAL { ?item wdt:P8061 ?ix_unagrovoc . }
  OPTIONAL { ?item wdt:P402 ?ix_xzosmrel . }
  OPTIONAL { ?item wdt:P1566 ?ix_xzgeonames . }
  OPTIONAL { ?item wdt:P5400 ?ix_jpgeolod . }
  OPTIONAL { ?item wdt:P8814 ?ix_usworldnet . }
  OPTIONAL { ?item wdt:P9948 ?ix_usfactbook . }
  OPTIONAL { ?item wdt:P9100 ?ix_xzgithubt . }
  OPTIONAL { ?item wdt:P625 ?ix_zzwgs84point . }
  OPTIONAL { ?item wdt:P3896 ?ix_zzgeojson . }
}
GROUP BY ?item ?ix_unm49
ORDER BY ASC(?item__conceptum__codicem)
' >"$objectivum_archivum_temporarium"

  frictionless validate "$objectivum_archivum_temporarium"

  caput_csvnormali=$(head -n1 "$objectivum_archivum_temporarium")
  caput_hxltm=$(caput_csvnormali_ad_hxltm "${caput_csvnormali}" ",")

  echo "$caput_hxltm" >"$objectivum_archivum_temporarium_hxltm"
  tail -n +2 "$objectivum_archivum_temporarium" >>"$objectivum_archivum_temporarium_hxltm"

  file_update_if_necessary csv "$objectivum_archivum_temporarium" "$objectivum_archivum"
  file_update_if_necessary csv "$objectivum_archivum_temporarium_hxltm" "$objectivum_archivum_hxltm_999999"
}

#######################################
# Return list of administrative level 1 codes
#
# Globals:
#   None
# Arguments:
#   None
# Outputs:
#   csvfile (stdout)
#######################################
1603_3_12_wikipedia_adm1_v2() {
  # fontem_archivum=
  objectivum_archivum="${ROOTDIR}/1603/3/1603_3__adm1_v2.csv"
  objectivum_archivum_temporarium="${ROOTDIR}/1603/3/1603_3__adm1_v2.TEMP.csv"
  objectivum_archivum_temporarium_hxltm="${ROOTDIR}/1603/3/1603_3__adm1_v2.TEMP.tm.hxl.csv"
  objectivum_archivum_hxltm="${ROOTDIR}/1603/3/1603_3__adm1.tm.hxl.csv"

  # if [ -z "$(stale_archive "$objectivum_archivum")" ]; then return 0; fi

  echo "${FUNCNAME[0]} stale data on [$objectivum_archivum], refreshing..."

  curl --header "Accept: text/csv" --silent --show-error \
    --get https://query.wikidata.org/sparql --data-urlencode query='
SELECT
  (xsd:integer(STRAFTER(STR(?item), "entity/Q")) AS ?item__conceptum__codicem)
  (STRAFTER(STR(?item), "entity/") AS ?item__rem__i_qcc__is_zxxx__ix_wikiq)
  (GROUP_CONCAT(DISTINCT ?ix_iso3166p2; separator = "|") AS ?item__rem__i_qcc__is_zxxx__ix_iso3166p2)
  (GROUP_CONCAT(DISTINCT ?ix_xzosmrel; separator = "|") AS ?item__rem__i_qcc__is_zxxx__ix_xzosmrel)
  (GROUP_CONCAT(DISTINCT ?ix_xzgeonames; separator = "|") AS ?item__rem__i_qcc__is_zxxx__ix_xzgeonames)
  (GROUP_CONCAT(DISTINCT ?ix_jpgeolod; separator = "|") AS ?item__rem__i_qcc__is_zxxx__ix_jpgeolod)
  (GROUP_CONCAT(DISTINCT ?ix_usworldnet; separator = "|") AS ?item__rem__i_qcc__is_zxxx__ix_usworldnet)
  (GROUP_CONCAT(DISTINCT ?ix_zzwgs84point; separator = "|") AS ?item__rem__i_qcc__is_zxxx__ix_zzwgs84point)
  (GROUP_CONCAT(DISTINCT ?ix_zzgeojson; separator = "|") AS ?item__rem__i_qcc__is_zxxx__ix_zzgeojson)

WHERE
{
  # ?item wdt:P31 wd:Q6256 ;
  ?item wdt:P31 wd:Q10864048 ;
  # wdt:P2082 ?ix_unm49 ;
  #  wdt:P300 ?ix_iso3166p2 ;
  OPTIONAL { ?item wdt:P300 ?ix_iso3166p2 . }
  OPTIONAL { ?item wdt:P402 ?ix_xzosmrel . }
  OPTIONAL { ?item wdt:P1566 ?ix_xzgeonames . }
  OPTIONAL { ?item wdt:P5400 ?ix_jpgeolod . }
  OPTIONAL { ?item wdt:P8814 ?ix_usworldnet . }
  OPTIONAL { ?item wdt:P625 ?ix_zzwgs84point . }
  OPTIONAL { ?item wdt:P3896 ?ix_zzgeojson . }
}
GROUP BY ?item ?ix_iso3166p2
ORDER BY ASC(?item)
' >"$objectivum_archivum_temporarium"

  # @see https://stackoverflow.com/questions/44718137/get-wikidata-identifier-for-city-by-gps-location
  # shellcheck disable=SC2034
  _wikidata_by_distance='
SELECT DISTINCT * WHERE {
  ?place (wdt:P31/(wdt:P279*)) wd:Q515.
  SERVICE wikibase:around {
    ?place wdt:P625 ?location.
    bd:serviceParam wikibase:center "Point(8.4024875340491 48.9993762209831)"^^geo:wktLiteral;
      wikibase:radius "100";
      wikibase:distance ?distance.
  }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}
ORDER BY (?distance)
  '

  # https://www.wikidata.org/wiki/Wikidata:Request_a_query/Archive/2021/03#List_of_administrative_divisions_by_country
  # shellcheck disable=SC2034
  _ix_iso3166p2_only='
SELECT DISTINCT ?item ?itemLabel ?p300 WHERE {
  ?item wdt:P300 ?p300 .
  SERVICE wikibase:label { bd:serviceParam wikibase:language "pt,en". }
}
  '

  # Source of the query
  # https://www.wikidata.org/wiki/Wikidata_talk:WikiProject_Country_subdivision/Items
  # @see https://en.wikipedia.org/wiki/List_of_administrative_divisions_by_country
  # shellcheck disable=SC2034
  wikiproject_country_subdivisions='
SELECT ?country ?countryLabel ?item ?itemLabel ?level ?expected ?found ?samenumber
WITH {
  SELECT ?item ?expected ?country ?level (COUNT(DISTINCT ?place) AS ?found) {
    ?item wdt:P279* ?acs ; wdt:P17 ?country.
    FILTER NOT EXISTS { ?country wdt:P576 [] }
    ?acs p:P279 [ ps:P279 wd:Q1799794 ; pq:P1545 ?level ] .
    
    OPTIONAL { ?item wdt:P1114 ?expected }    
    OPTIONAL { 
      ?place p:P31 ?placeStatement .
      ?placeStatement ps:P31 ?item.
      FILTER NOT EXISTS { ?placeStatement wdt:P582 [] }
    }  
  } 
  GROUP BY ?item ?expected ?country ?level
} AS %subdivisions
WHERE {
  include %subdivisions.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
  BIND(IF(?expected = ?found, "✓", "✘") AS ?samenumber).
} 
ORDER BY ?countryLabel ?level DESC(?expected) ?itemLabel
  '

  # SPARQL subquery https://en.wikibooks.org/wiki/SPARQL/Subqueries
  # shellcheck disable=SC2034
  sparq_subquery_1='
SELECT ?x ?y WHERE {
  VALUES ?x { 1 2 3 4 }
  {
    SELECT ?y WHERE { VALUES ?y { 5 6 7 8 }  }
  }  # \subQuery
} # \mainQuery
  '
  # shellcheck disable=SC2034
  sparq_subquery_2='
SELECT ?countryLabel ?population (round(?population/?worldpopulation*1000)/10 AS ?percentage)
WHERE {
  ?country wdt:P31 wd:Q3624078;    # is a sovereign state
           wdt:P1082 ?population.

  { 
    # subquery to determine ?worldpopulation
    SELECT (sum(?population) AS ?worldpopulation)
    WHERE { 
      ?country wdt:P31 wd:Q3624078;    # is a sovereign state
               wdt:P1082 ?population. 
    }
  }

  SERVICE wikibase:label {bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en".}
}
ORDER BY desc(?population)
  '

  frictionless validate "$objectivum_archivum_temporarium"

  caput_csvnormali=$(head -n1 "$objectivum_archivum_temporarium")
  caput_hxltm=$(caput_csvnormali_ad_hxltm "${caput_csvnormali}" ",")

  echo "$caput_hxltm" >"$objectivum_archivum_temporarium_hxltm"
  tail -n +2 "$objectivum_archivum_temporarium" >>"$objectivum_archivum_temporarium_hxltm"

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
# 1603_3_12_cod_ab_et_wdata

# file_translate_csv_de_numerordinatio_q__v2 "1603_3_45_16_1_1" "1" "1"
# file_merge_numerordinatio_de_wiki_q "1603_3_45_16_1_1" "1" "1" "0"
# exit 0

1603_3_12_wikipedia_language_codes

# 1603_3_12_wikipedia_adm0

1603_3_12_wikipedia_adm0_v2
1603_3_12_wikipedia_adm1_v2

1603_3_12_cod_ab_et_wdata

# 1603_3_12_wikipedia_adm0_v2 expansion
file_translate_csv_de_numerordinatio_q__v2 "1603_3_45_16_1_1" "1" "1"
file_merge_numerordinatio_de_wiki_q "1603_3_45_16_1_1" "1" "1" "0"

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
