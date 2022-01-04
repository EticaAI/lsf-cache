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

ROOTDIR="$(pwd)"

# Source:
# - https://www.unicode.org/iso15924/codelists.html
#   - https://www.unicode.org/iso15924/iso15924.txt

DATA_ISO_15924_TXT="https://www.unicode.org/iso15924/iso15924.txt"

wget -qO- "$DATA_ISO_15924_TXT" > "${ROOTDIR}/99999999/1603/47/15924/1603.47.15924.txt"

# mlr --csv head 99999999/1603/47/15924/1603.47.15924.txt
# mlr --csv skip-trivial-records 99999999/1603/47/15924/1603.47.15924.txt

# tail -n +4 99999999/1603/47/15924/1603.47.15924.txt
# tail -n +8 99999999/1603/47/15924/1603.47.15924.txt | mrl --csv --irs=";" --ors=","

echo "#code+v_iso1524a;#code+v_iso1524n;#item+name+i_eng+is_latn;#item+name+i_fra+is_latn;#meta+pva;#meta+unicode+version;#date" > "${ROOTDIR}/99999999/1603/47/15924/1603.47.15924.hxl.csv"
tail -n +8 "${ROOTDIR}/99999999/1603/47/15924/1603.47.15924.txt" >> "${ROOTDIR}/99999999/1603/47/15924/1603.47.15924.hxl.csv"

# /99999999/1603/47/15924/1603.47.15924.hxl.csv
#  ./999999999/0/hxl2numerordinatio.py 99999999/1603/47/15924/1603.47.15924.csv
# ./999999999/0/hxl2numerordinatio.py --conceptum-hxl-tag="#code+v_iso1524n" 99999999/1603/47/15924/1603.47.15924.csv

# hxlrename --rename="#code+v_iso1524n:#item+conceptum+codicem" --rename="#code+v_iso1524a:#item+rem+i_zxx+is_latn+ix_iso1524a" --rename="#item+name+i_eng+is_latn:#item+rem+i_eng+is_latn" --rename="#item+name+i_fra+is_latn:#item+rem+i_fra+is_latn" 99999999/1603/47/15924/1603.47.15924.hxl.csv | hxlselect --include="#item+conceptum+codicem,#item+rem"
# hxlrename --rename="#code+v_iso1524n:#item+conceptum+codicem" --rename="#code+v_iso1524a:#item+rem+i_zxx+is_latn+ix_iso1524a" --rename="#item+name+i_eng+is_latn:#item+rem+i_eng+is_latn" --rename="#item+name+i_fra+is_latn:#item+rem+i_fra+is_latn" 99999999/1603/47/15924/1603.47.15924.hxl.csv | hxlselect --include="#item+conceptum+codicem,#item+rem"