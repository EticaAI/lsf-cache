#!/bin/bash
#===============================================================================
#
#          FILE:  1603_47_15924.sh
#
#         USAGE:  ./999999999/1603_47_15924.sh
#
#   DESCRIPTION:  ...
#
#       OPTIONS:  ---
#
#  REQUIREMENTS:  - Bash shell (or better)
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
#      REVISION:  2021-01-10 05:19 UTC v1.1 1603.47.15924.sh -> 1603_47_15924.sh
#===============================================================================
# Comment next line if not want to stop on first error
set -e
# set -x

ROOTDIR="$(pwd)"

PRAEFIXUM="1603:47:15924:"

# Source:
# - https://www.unicode.org/iso15924/codelists.html
#   - https://www.unicode.org/iso15924/iso15924.txt

DATA_ISO_15924_TXT="https://www.unicode.org/iso15924/iso15924.txt"

# TODO: implement option to rebuild even if file already on disk
if [ ! -f "${ROOTDIR}/999999/1603/47/15924/1603_47_15924.txt" ]; then
  wget -qO- "$DATA_ISO_15924_TXT" >"${ROOTDIR}/999999/1603/47/15924/1603_47_15924.txt"
else
  echo "Cached: ${ROOTDIR}/999999/1603/47/15924/1603_47_15924.txt"
fi

## 1603_47_15924.txt --> 1603_47_15924.hxl.csv
echo "#code+v_iso1524a;#code+v_iso1524n;#item+name+i_eng+is_latn;#item+name+i_fra+is_latn;#meta+pva;#meta+unicode+version;#date" \
  >"${ROOTDIR}/999999/1603/47/15924/1603_47_15924.hxl.csv"
tail -n +8 "${ROOTDIR}/999999/1603/47/15924/1603_47_15924.txt" \
  >>"${ROOTDIR}/999999/1603/47/15924/1603_47_15924.hxl.csv"

### 1603_47_15924.hxl.csv --> 1603_47_15924.tm.hxl.csv _________________________
hxlrename \
  --rename="#code+v_iso1524n:#item+rem+i_qcc+is_zxxx+ix_iso1524n" \
  --rename="#code+v_iso1524a:#item+rem+i_qcc+is_zxxx+ix_iso1524a" \
  --rename="#item+name+i_eng+is_latn:#item+rem+i_eng+is_latn" \
  --rename="#item+name+i_fra+is_latn:#item+rem+i_fra+is_latn" \
  "${ROOTDIR}/999999/1603/47/15924/1603_47_15924.hxl.csv" |
  hxladd --before --spec="#item+conceptum+codicem={{#item+rem+i_qcc+is_zxxx+ix_iso1524n}}" |
  hxlcut --include="#item+conceptum,#item+rem" |
  hxlsort --tags="#item+conceptum" \
    >"${ROOTDIR}/999999/1603/47/15924/1603_47_15924.tm.hxl.csv"

# @TODO: only do this if hxl did not removed empty header files ,,,,,,
sed -i '1d' "${ROOTDIR}/999999/1603/47/15924/1603_47_15924.tm.hxl.csv"

hxladd --before --spec="#item+conceptum+numerordinatio=${PRAEFIXUM}{{(#item+conceptum+codicem)+1-1}}" \
  "${ROOTDIR}/999999/1603/47/15924/1603_47_15924.tm.hxl.csv" \
  "${ROOTDIR}/1603/47/15924/1603_47_15924.no1.tm.hxl.csv"

# @TODO: only do this if hxl did not removed empty header files ,,,,,,
sed -i '1d' "${ROOTDIR}/1603/47/15924/1603_47_15924.no1.tm.hxl.csv"

if [ -f "${ROOTDIR}/1603/1/4/1603_1_4.no1.tm.hxl.csv" ]; then
  rm "${ROOTDIR}/1603/1/4/1603_1_4.no1.tm.hxl.csv"
fi

cp "${ROOTDIR}/1603/47/15924/1603_47_15924.no1.tm.hxl.csv" "${ROOTDIR}/1603/1/4/1603_1_4.no1.tm.hxl.csv"

# TODO: make the conversion to JSON format. Or enable the JavaScript to support tm.hxl.csv files

hxladd \
  --before --spec="#x_item+lower={{#item+rem+i_qcc+is_zxxx+ix_iso1524a}}" \
  --before --spec="#x_item+upper={{#item+rem+i_qcc+is_zxxx+ix_iso1524a}}" \
  "${ROOTDIR}/1603/47/15924/1603_47_15924.no1.tm.hxl.csv" |
  hxladd --before --spec="#x_item={{#item+rem+i_qcc+is_zxxx+ix_iso1524a}}" |
  hxladd --before --spec="#x_item={{#item+conceptum+codicem}}" |
  hxladd --before --spec="#x_item={{1-1+(#item+conceptum+codicem)}}" |
  hxlclean --lower="#x_item+lower" |
  hxlclean --upper="#x_item+upper" |
  hxlcut --include="#x_item" |
  csvformat --out-tabs --skip-lines 2 \
    >"${ROOTDIR}/999999/999999/1603_47_15924.tsv"


# | hxlreplace --tags="#x_item" --pattern="/(.)/" --substitution="" \
# TypeError: 'TagPattern' object is not iterabl

# TODO: fix the "None from 1603.45.16.tsv"

set +x
