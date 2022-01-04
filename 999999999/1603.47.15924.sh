#!/bin/sh
#===============================================================================
#
#          FILE:  1603.47.15924.sh
#
#         USAGE:  ./999999999/1603.47.15924.sh
#
#   DESCRIPTION:  ...
#
#       OPTIONS:  ---
#
#  REQUIREMENTS:  - POSIX shell (or better)
#                 - wget
#                 - mlr (https://miller.readthedocs.io/en/latest/)
#          BUGS:  ---
#         NOTES:  ---
#        AUTHOR:  Emerson Rocha <rocha[at]ieee.org>
#       COMPANY:  EticaAI
#       LICENSE:  Public Domain dedication or Zero-Clause BSD
#                 SPDX-License-Identifier: Unlicense OR 0BSD
#       VERSION:  v1.0
#       CREATED:  2022-01-04 04:02 UTC based on scripts from github.com/EticaAI
#                                      /HXL-Data-Science-file-formats
#      REVISION:  ---
#===============================================================================
# Comment next line if not want to stop on first error
set -e
set -x

ROOTDIR="$(pwd)"

PRAEFIXUM="1603:47:15924:"

# Source:
# - https://www.unicode.org/iso15924/codelists.html
#   - https://www.unicode.org/iso15924/iso15924.txt

DATA_ISO_15924_TXT="https://www.unicode.org/iso15924/iso15924.txt"


# @TODO: implement some option to use cached file instead of re-download; 
#        for now we're just commenting the next line
wget -qO- "$DATA_ISO_15924_TXT" > "${ROOTDIR}/999999/1603/47/15924/1603.47.15924.txt"


## 1603.47.15924.txt --> 1603.47.15924.hxl.csv
echo "#code+v_iso1524a;#code+v_iso1524n;#item+name+i_eng+is_latn;#item+name+i_fra+is_latn;#meta+pva;#meta+unicode+version;#date" \
  > "${ROOTDIR}/999999/1603/47/15924/1603.47.15924.hxl.csv"
tail -n +8 "${ROOTDIR}/999999/1603/47/15924/1603.47.15924.txt" \
  >> "${ROOTDIR}/999999/1603/47/15924/1603.47.15924.hxl.csv"

### 1603.47.15924.hxl.csv --> 1603.47.15924.tm.hxl.csv _________________________
hxlrename \
  --rename="#code+v_iso1524n:#item+rem+i_zxx+is_zmth+ix_iso1524n" \
  --rename="#code+v_iso1524a:#item+rem+i_zxx+is_latn+ix_iso1524a" \
  --rename="#item+name+i_eng+is_latn:#item+rem+i_eng+is_latn" \
  --rename="#item+name+i_fra+is_latn:#item+rem+i_fra+is_latn" \
  "${ROOTDIR}/999999/1603/47/15924/1603.47.15924.hxl.csv" \
  | hxladd --before --spec="#item+conceptum+codicem={{#item+rem+i_zxx+is_zmth+ix_iso1524n}}" \
  | hxlcut --include="#item+conceptum,#item+rem" \
  | hxlsort --tags="#item+conceptum" \
  > "${ROOTDIR}/999999/1603/47/15924/1603.47.15924.tm.hxl.csv"


# @TODO: only do this if hxl did not removed empty header files ,,,,,,
sed -i '1d' "${ROOTDIR}/999999/1603/47/15924/1603.47.15924.tm.hxl.csv"

hxladd --before --spec="#item+conceptum+numerordinatio=${PRAEFIXUM}{{(#item+conceptum+codicem)+1-1}}" \
  "${ROOTDIR}/999999/1603/47/15924/1603.47.15924.tm.hxl.csv" \
  "${ROOTDIR}/1603/47/15924/1603.47.15924.no1.tm.hxl.csv"

# @TODO: only do this if hxl did not removed empty header files ,,,,,,
sed -i '1d' "${ROOTDIR}/1603/47/15924/1603.47.15924.no1.tm.hxl.csv"

# TODO: make the conversion to JSON format. Or enable the JavaScript to support tm.hxl.csv files

set +x