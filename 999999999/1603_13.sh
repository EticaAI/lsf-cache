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
# numerordiatio_search (...)
#
# Globals:
#   ROOTDIR
# Arguments:
#   basim
# Outputs:
#   ...
#######################################
numerordiatio_search() {
  basim="${1//$ROOTDIR/'.'}"

  echo "path_or_file $basim"
  find "$basim" -type f -name "*no1.tm.hxl.csv" ! -name "*.meta.*"
}

#######################################
# numerordiatio_caput extract from no1.tm.hxl.csv their headings
#
# Globals:
#   ROOTDIR
# Arguments:
#   basim
# Outputs:
#   ...
#######################################
numerordiatio_caput() {
  basim="$1"
  shopt -s nullglob globstar
  # for i in "$basim/"**
  echo "#meta+id,#meta+archivum,#meta+caput"
  for i in "$basim/"**/*no1.tm.hxl.csv; do
    if [[ "$i" =~ .meta. ]]; then
      # echo "Skiping meta..."
      continue
    fi
    relative_path="${i//$ROOTDIR/'.'}"
    relative_path="${relative_path//\.\//''}"
    # echo "$i"
    # basename "$i"
    # echo "$relative_path"
    numerordiation=$(basename "$i" .no1.tm.hxl.csv)
    # caput=$(head -n 1 "$i" | tr '\n' ' ')
    caput=$(head -n 1 "$i")
    caput=$(head -n 1 "$i" | tr -d '\n' | tr ',' '|')
    echo "$numerordiation,$relative_path,$caput"
  done
}

# find path/to/dir -name "*.ext1" -o -name "*.ext2"
# echo "$ROOTDIR"
# numerordiatio_search "$ROOTDIR/1603/"
# numerordiatio_caput "$ROOTDIR/1603"
numerordiatio_caput "$ROOTDIR/1603" > 999999/0/simple_caput.csv

echo "TODO: compile non-empty '#item+rem+i_qcc+is_zxxx+ix_hxlix'"
echo "TODO: compile non-empty '#item+rem+i_qcc+is_zxx+ix_hxlvoc'"

# echo "TODO $0"
