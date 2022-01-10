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

# https://w.wiki/4fHT
# SELECT ?country ?unm49 ?iso3166n ?iso3166p1a2 ?iso3166p1a3 ?osmrelid ?unescot ?usciafb ?usfips4 ?gadm
# WHERE
# {
#   ?country wdt:P31 wd:Q6256 ;
#   OPTIONAL { ?country wdt:P2082 ?unm49. }
#   OPTIONAL { ?country wdt:P299 ?iso3166n. }
#   OPTIONAL { ?country wdt:P297 ?iso3166p1a2. }
#   OPTIONAL { ?country wdt:P298 ?iso3166p1a3. }
#   OPTIONAL { ?country wdt:P402 ?osmrelid. }
#   OPTIONAL { ?country wdt:P3916 ?unescot. }
#   OPTIONAL { ?country wdt:P9948 ?usciafb. }
#   OPTIONAL { ?country wdt:P901 ?usfips4. }
#   OPTIONAL { ?country wdt:P8714 ?gadm. }

#   SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE]". }
# }
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

  if [ -n "$(changed_recently "$objectivum_archivum" 3600)" ]; then return 0; fi

  echo "${FUNCNAME[0]} stale data on [$objectivum_archivum], refreshing..."

  curl --header "Accept: text/csv" --silent --show-error \
    --get https://query.wikidata.org/sparql --data-urlencode query='
# SELECT ?wd ?wmCode ?iso6391 ?iso6392 ?iso6393 ?iso6396 ?native ?label {
SELECT ?wmCode ?iso6391 ?iso6392 ?iso6393 ?iso6396 ?native ?label {
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
# echo "oooi"

1603_3_12_wikipedia_language_codes

exit 0
