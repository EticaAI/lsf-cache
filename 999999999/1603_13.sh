#!/bin/bash
#===============================================================================
#
#          FILE:  1603_13.sh
#
#         USAGE:  ./999999999/1603_13.sh

#   DESCRIPTION:  ---
#
#       OPTIONS:  ---
#
#  REQUIREMENTS:  - hxltmcli
#          BUGS:  ---
#         NOTES:  ---
#        AUTHOR:  Emerson Rocha <rocha[at]ieee.org>
#       COMPANY:  EticaAI
#       LICENSE:  Public Domain dedication
#                 SPDX-License-Identifier: Unlicense
#       VERSION:  v1.0
#       CREATED:  2022-01-13 05:24 UTC started, based on 1603_17.sh
#      REVISION:  ---
#===============================================================================
set -e

ROOTDIR="$(pwd)"

# shellcheck source=999999999.lib.sh
# . "$ROOTDIR"/999999999/999999999.lib.sh

#######################################
# numerordiatio_caput extract from no1.tm.hxl.csv some quick metadata.
# Mostly focused on patters of the headings.
#
# Globals:
#   ROOTDIR
# Arguments:
#   basim
# Outputs:
#   HXLated tabular output (not HXLTM neither Numeroordinatio)
#######################################
numerordiatio_summarium() {
  basim="$1"
  shopt -s nullglob globstar
  # for i in "$basim/"**
  echo "#meta+id,#meta+archivum,#meta+conceptum+total,#meta+caput+total,#status+ix_hxlix,#status+ix_hxlvoc,#status+ix_wikip,#status+ix_wikiq,#meta+caput,#meta+value+ix_hxlix,#meta+value+ix_hxlvoc,#meta+value+ix_wikip,#meta+value+ix_wikiq"
  for i in "$basim/"**/*no1.tm.hxl.csv; do
    if [[ "$i" =~ .meta. ]]; then
      # echo "Skiping meta..."
      continue
    fi
    relative_path="${i//$ROOTDIR/'.'}"
    relative_path="${relative_path//\.\//''}"
    status_ix_hxlix="0"
    status_ix_hxlvoc="0"
    #item +rem +i_qcc +is_zxxx +ix_wikiq
    status_ix_wikip="0"
    status_ix_wikiq="0"
    concept_count=$(wc --lines "$relative_path" | cut --fields=1 --delimiter=' ')
    concept_count=$((concept_count - 1))
    # echo "$i"
    # basename "$i"
    # echo "$relative_path"
    numerordiation=$(basename "$i" .no1.tm.hxl.csv)
    # caput=$(head -n 1 "$i" | tr '\n' ' ')
    caput=$(head -n 1 "$i" | tr -d '\n' | tr --squeeze-repeats ',' '|' | tr --delete "[:space:]")

    caput_count=$(echo "$caput" | tr -d -c '|' | wc -c)
    caput_count=$((caput_count + 1))
    values_ix_hxlix=""
    values_ix_hxlvoc=""
    if [[ "$caput" =~ ix_hxlix ]]; then
      status_ix_hxlix="1"
      #echo "status_ix_hxlix $relative_path"
      # hxlcut --include="#item+rem+i_zxx+is_latn+ix_hxl+ix_hxlvoc"  1603/25/1/1603_25_1.no1.tm.hxl.csv
      values_ix_hxlix=$(hxlcut --include="#item+rem+i_qcc+is_zxxx+ix_hxlix" "$relative_path" | tail -n +3 | sort | uniq)
      values_ix_hxlix=$(echo "$values_ix_hxlix" | sed 's/^+//' | tr --squeeze-repeats "\r\n" "|" | tr --delete '"' | sed 's/^|//' | sed 's/|$//')
      values_ix_hxlix=$(echo "$values_ix_hxlix" | tr --delete "[:blank:]")
    fi
    if [[ "$caput" =~ ix_hxlvoc ]]; then
      status_ix_hxlvoc="1"
      #echo "status_ix_hxlvoc $relative_path"
      values_ix_hxlvoc=$(hxlcut --include="#item+rem+i_qcc+is_zxxx+ix_hxlvoc" "$relative_path" | tail -n +3 | sort | uniq)
      values_ix_hxlvoc=$(echo "$values_ix_hxlvoc" | sed 's/^+//' | tr --squeeze-repeats "\r\n" "|" | tr --delete '"' | sed 's/^|//' | sed 's/|$//')
      values_ix_hxlvoc=$(echo "$values_ix_hxlvoc" | tr --delete "[:blank:]")
    fi
    if [[ "$caput" =~ ix_wikip ]]; then
      status_ix_wikip="1"
      #echo "status_ix_wikip $relative_path"
      values_ix_wikip=$(hxlcut --include="#item+rem+i_qcc+is_zxxx+ix_wikip" "$relative_path" | tail -n +3 | sort | uniq)
      values_ix_wikip=$(echo "$values_ix_wikip" | sed 's/^+//' | tr --squeeze-repeats "\r\n" "|" | tr --delete '"' | sed 's/^|//' | sed 's/|$//')
      values_ix_wikip=$(echo "$values_ix_wikip" | tr --delete "[:blank:]")
    fi
    if [[ "$caput" =~ ix_wikiq ]]; then
      status_ix_wikiq="1"
      #echo "status_ix_wikiq $relative_path"

      values_ix_wikiq=$(hxlcut --include="#item+rem+i_qcc+is_zxxx+ix_wikiq" "$relative_path" | tail -n +3 | sort | uniq)
      values_ix_wikiq=$(echo "$values_ix_wikiq" | sed 's/^+//' | tr --squeeze-repeats "\r\n" "|" | tr --delete '"' | sed 's/^|//' | sed 's/|$//')
      values_ix_wikiq=$(echo "$values_ix_wikiq" | tr --delete "[:blank:]")

      # 1603_1_51 have two columns with Q codes for different concepts
      values_ix_wikiq="$(echo "$values_ix_wikiq" | tr "," "|" | sed 's/^|//' | sed 's/|$//' | tr --squeeze-repeats "|" "\r\n" | sort --version-sort --field-separator="Q" | uniq | tr --squeeze-repeats "\r\n" "|" | sed 's/^|//' | sed 's/|$//')"
    fi

    # echo "$caput"
    echo "$numerordiation,$relative_path,$concept_count,$caput_count,$status_ix_hxlix,$status_ix_hxlvoc,$status_ix_wikip,$status_ix_wikiq,$caput,$values_ix_hxlix,$values_ix_hxlvoc,$values_ix_wikip,$values_ix_wikiq"
    # echo "$numerordiation,$relative_path,$concept_count,$caput_count,$status_ix_hxlix,$status_ix_hxlvoc,<$caput>,,"
  done
}

# #######################################
# # numerordiatio_caput extract from no1.tm.hxl.csv their headings
# #
# # Globals:
# #   ROOTDIR
# # Arguments:
# #   basim
# # Outputs:
# #   ...
# #######################################
# numerordiatio_caput_ix_hxlix() {
#   basim="$1"
#   shopt -s nullglob globstar
#   # for i in "$basim/"**
#   echo "#meta+id,#meta+archivum,#status+ix_hxlix"
#   for i in "$basim/"**/*no1.tm.hxl.csv; do
#     if [[ "$i" =~ .meta. ]]; then
#       # echo "Skiping meta..."
#       continue
#     fi
#     relative_path="${i//$ROOTDIR/'.'}"
#     relative_path="${relative_path//\.\//''}"
#     # echo "$i"
#     # basename "$i"
#     # echo "$relative_path"
#     numerordiation=$(basename "$i" .no1.tm.hxl.csv)
#     # caput=$(head -n 1 "$i" | tr '\n' ' ')
#     # caput=$(head -n 1 "$i")
#     caput=$(head -n 1 "$i" | tr -d '\n' | tr ',' '|')
#     # echo "$numerordiation,$relative_path,$caput"
#     if [[ "$caput" =~ ix_hxlix ]]; then
#       # echo "ix_hxlix present"
#       echo "$numerordiation,$relative_path,1,$caput"
#     fi
#   done
# }

# find path/to/dir -name "*.ext1" -o -name "*.ext2"
# echo "$ROOTDIR"
# numerordiatio_search "$ROOTDIR/1603/"
# numerordiatio_caput "$ROOTDIR/1603"
numerordiatio_summarium "$ROOTDIR/1603" >999999/1603/13/1603~meta.hxl.csv
hxlexpand --query="#status+ix_hxlix>0" --tags="#meta+value+ix_hxlix" 999999/1603/13/1603~meta.hxl.csv | hxlcut --include="#meta+id,#meta+value+ix_hxlix" >999999/1603/13/1603~meta__ix_hxlix.hxl.csv
hxlexpand --query="#status+ix_hxlvoc>0" --tags="#meta+value+ix_hxlvoc" 999999/1603/13/1603~meta.hxl.csv | hxlcut --include="#meta+id,#meta+value+ix_hxlvoc" >999999/1603/13/1603~meta__ix_hxlvoc.hxl.csv
hxlexpand --query="#status+ix_wikip>0" --tags="#meta+value+ix_wikip" 999999/1603/13/1603~meta.hxl.csv | hxlcut --include="#meta+id,#meta+value+ix_wikip" >999999/1603/13/1603~meta__ix_wikip.hxl.csv
hxlexpand --query="#status+ix_wikiq>0" --tags="#meta+value+ix_wikiq" 999999/1603/13/1603~meta.hxl.csv | hxlcut --include="#meta+id,#meta+value+ix_wikiq" >999999/1603/13/1603~meta__ix_wikiq.hxl.csv

# hxlexpand --tags="#meta+value+ix_hxlix" 999999/1603/13/1603~meta.hxl.csv | hxlcut --include="#meta+id,#meta+value+ix_hxlix"
# numerordiatio_caput_ix_hxlix "$ROOTDIR/1603" > 999999/0/simple_caput_ix_hxlix.csv

# ./999999999/0/1603_1.py ./999999999/0/1603_1.py --dictionaria-numerordinatio
./999999999/0/1603_1.py --methodus='deprecatum-dictionaria-numerordinatio' --punctum-separato-de-resultatum=',' > 999999/1603/13/1603~dictionaria.hxl.csv
# ./999999999/0/1603_1.py \
#   --objectivum-linguam="lat-Latn" \
#   --auxilium-linguam="mul-Zyyy,por-Latn,eng-Latn" \
#   --methodus='codex' --codex-de 1603_25_1 \
#   >999999/1603/25/1/1603_25_1.mul-Zyyy.codex.md

# ./999999999/0/1603_1.py \
#   --objectivum-linguam="lat-Latn" \
#   --auxilium-linguam="mul-Zyyy,por-Latn,eng-Latn" \
#   --methodus='codex' --codex-de 1603_1_51 \
#   >999999/1603/1/51/1603_1_51.mul-Zyyy.codex.md

# ./999999999/0/1603_1.py \
#   --objectivum-linguam="lat-Latn" \
#   --auxilium-linguam="mul-Zyyy,por-Latn,eng-Latn" \
#   --methodus='codex' --codex-de 1603_1_51 \
#   >999999/1603/1/51/1603_1_51.mul-Zyyy.codex.md

# ./999999999/0/1603_1.py \
#   --objectivum-linguam="lat-Latn" \
#   --auxilium-linguam="mul-Zyyy,por-Latn,eng-Latn" \
#   --methodus='codex' --codex-de 1603_1_1 \
#   >1603/1/1/1603_1_1.mul-Zyyy.codex.md

# officinam/1603/1/1/1603_1_1.no1.tm.hxl.csv

# echo "TODO: compile non-empty '#item+rem+i_qcc+is_zxxx+ix_hxlix'"
# echo "TODO: compile non-empty '#item+rem+i_qcc+is_zxx+ix_hxlvoc'"

# echo "TODO $0"
