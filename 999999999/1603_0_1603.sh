#!/bin/bash
#===============================================================================
#
#          FILE:  1603_0_1603.sh
#
#         USAGE:  ./999999999/1603_0_1603.sh
#                 DE_FACTO=1 ./999999999/1603_0_1603.sh
#
#   DESCRIPTION:  1603_0_1603.sh is a manual purge of files. Is not intented
#                 to be run automatically
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
#       CREATED:  2022-01-28 20:18 UTC started
#      REVISION:  ---
#===============================================================================
set -e

ROOTDIR="$(pwd)"


# tutorial https://opensource.com/article/18/5/you-dont-know-bash-intro-bash-arrays
PURGATORIA_CONCEPTUM=()
## Reset all files
PURGATORIA_EXTENSIONEM=( "no1.tm.hxl.csv" "wikiq.tm.hxl.csv" "no11.tm.hxl.csv" "tm.hxl.csv" "mul-Latn.codex.pdf" "mul-Latn.codex.adoc" )

## Use cached files (avoid overload Google Sheets), but gives hint to re-generate translations
# PURGATORIA_EXTENSIONEM=( "no1.tm.hxl.csv" "wikiq.tm.hxl.csv" "no11.tm.hxl.csv" )

# PURGATORIA_CONCEPTUM+=( "1603_1_1" )
# PURGATORIA_CONCEPTUM+=( "1603_1_6" )
# PURGATORIA_CONCEPTUM+=( "1603_1_7" )
# PURGATORIA_CONCEPTUM+=( "1603_1_51" )
# PURGATORIA_CONCEPTUM+=( "1603_1_101" )

# PURGATORIA_CONCEPTUM+=( "1603_3_12_6" )

# PURGATORIA_CONCEPTUM+=( "1603_25_1" )
# PURGATORIA_CONCEPTUM+=( "1603_84_1" )
# PURGATORIA_CONCEPTUM+=( "1603_44_1" )
# PURGATORIA_CONCEPTUM+=( "1603_44_142" )
# PURGATORIA_CONCEPTUM+=( "1603_45_1" )
PURGATORIA_CONCEPTUM+=( "1603_45_31" )
# PURGATORIA_CONCEPTUM+=( "1603_45_95" )
# PURGATORIA_CONCEPTUM+=( "1603_64_604" )
# PURGATORIA_CONCEPTUM+=( "1603_1_99" )
# PURGATORIA_CONCEPTUM+=( "1603_23_21" )
# PURGATORIA_CONCEPTUM+=( "1603_23_36" )
# PURGATORIA_CONCEPTUM+=( "1603_63_1" )
# PURGATORIA_CONCEPTUM+=( "1603_45_19" )
# PURGATORIA_CONCEPTUM+=( "1603_64_41" )
# PURGATORIA_CONCEPTUM+=( "1603_63_101" )

DE_FACTO="${DE_FACTO:-'0'}"
# DRYRUM="0"


#######################################
# numerordiatio_caput extract from no1.tm.hxl.csv some quick metadata.
# Mostly focused on patters of the headings.
#
# Globals:
#   ROOTDIR
#   PURGATORIA
#   PURGATORIA_EXTENSIONEM
#   DE_FACTO
# Arguments:
#   basim
# Outputs:
#   HXLated tabular output (not HXLTM neither Numeroordinatio)
#######################################
purgatoria() {
  basim="$1"
  shopt -s nullglob globstar
  # for i in "$basim/"**/*no1.tm.hxl.csv; do
  echo "PURGATORIA_CONCEPTUM (${PURGATORIA_CONCEPTUM[*]})"

  # for i in "$basim/"**/**."${PURGATORIA_EXTENSIONEM[@]}"; do
  for i in "$basim/"**; do
    archivum=$(basename "$i")
    archivum_extension="${archivum#*.}"
    conceptum="${archivum%%.*}"
    for purgatoria_extensionem in "${PURGATORIA_EXTENSIONEM[@]}"; do
      # echo "purgatoria_extensionem $purgatoria_extensionem"
      # echo "archivum_extension $archivum_extension"
      if [[ "$archivum_extension" == "$purgatoria_extensionem" ]]; then

        # echo "Candidate [$i] [$conceptum]"

        for item in "${PURGATORIA_CONCEPTUM[@]}"; do
          if [[ "$conceptum" == "$item" ]]; then
            # echo "    needs purge $i"
            # echo "    DE_FACTO [${DE_FACTO}]"
            if [ "$DE_FACTO" = "1" ]; then
              echo "    $conceptum"
              echo "        > rm $i"
              rm "$i"
            else
              echo "    candidate [$i]"
              echo "    requires run with"
              echo "        DE_FACTO=1 $0"
            fi
            # rm "$i"
          fi
        done
      fi
    done
  done
}


echo "${PURGATORIA[@]}"

# Production directory
purgatoria "1603"

# Temporary directory
purgatoria "999999/1603"
