#!/bin/sh
#===============================================================================
#
#          FILE:  1603.45.49.sh
#
#         USAGE:  ./999999999/1603.45.49.sh
#
#   DESCRIPTION:  ...
#
#       OPTIONS:  ---
#
#  REQUIREMENTS:  - POSIX shell (or better)
#                 - wget
#          BUGS:  1. fix the "None" which may appear on mathematical fields.
#                    Maybe https://github.com/HXLStandard/hxl-proxy/wiki
#                    /Replace-data-filter ?
#         NOTES:  ---
#        AUTHOR:  Emerson Rocha <rocha[at]ieee.org>
#       COMPANY:  EticaAI
#       LICENSE:  Public Domain dedication or Zero-Clause BSD
#                 SPDX-License-Identifier: Unlicense OR 0BSD
#       VERSION:  v1.0
#       CREATED:  2022-01-04 03:38 UTC based on scripts from github.com/EticaAI
#                                      /HXL-Data-Science-file-formats
#      REVISION:  ---
#===============================================================================
# Comment next line if not want to stop on first error
set -e
set -x

ROOTDIR="$(pwd)"

PRAEFIXUM="1603.45.49:"

# Source:
# - https://vocabulary.unocha.org/
#   - https://docs.google.com/spreadsheets/d/1NjSI2LaS3SqbgYc0HdD8oIb7lofGtiHgoKKATCpwVdY/edit#gid=1088874596
#     - https://proxy.hxlstandard.org/data/edit?dest=data_edit&filter01=cut&cut-skip-untagged01=on&filter02=sort&sort-tags02=%23country%2Bcode%2Bnum%2Bv_m49&strip-headers=on&url=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fd%2F1NjSI2LaS3SqbgYc0HdD8oIb7lofGtiHgoKKATCpwVdY%2Fedit%23gid%3D1088874596


DATA_UN_M49_CSV="https://proxy.hxlstandard.org/data.csv?dest=data_edit&filter01=cut&cut-skip-untagged01=on&filter02=sort&sort-tags02=%23country%2Bcode%2Bnum%2Bv_m49&strip-headers=on&url=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fd%2F1NjSI2LaS3SqbgYc0HdD8oIb7lofGtiHgoKKATCpwVdY%2Fedit%23gid%3D1088874596"

# @TODO: implement some option to use cached file instead of re-download; 
#        for now we're just commenting the next line
wget -qO- "$DATA_UN_M49_CSV" > "${ROOTDIR}/999999/1603/45/49/1603.45.49.hxl.csv"


### 1603.45.49.hxl.csv --> 1603.45.49.tm.hxl.csv _______________________________

# Note: ix_iso3166p1 would generate -x-iso3166p1, 9 characters, but BCP limit to 8
# Note: ix_unreliefweb would generate -x-unreliefweb, 11 characters, but BCP limit to 8
hxlrename \
  --rename="#country+name+i_en+alt+v_unterm:#item+rem+i_eng+is_latn+ix_unterm" \
  --rename="#country+name+i_fr+alt+v_unterm:#item+rem+i_fra+is_latn+ix_unterm" \
  --rename="#country+name+i_es+alt+v_unterm:#item+rem+i_spa+is_latn+ix_unterm" \
  --rename="#country+name+i_ru+alt+v_unterm:#item+rem+i_rus+is_cyrl+ix_unterm" \
  --rename="#country+name+i_zh+alt+v_unterm:#item+rem+i_zho+is_hans+ix_unterm" \
  --rename="#country+name+i_ar+alt+v_unterm:#item+rem+i_ara+is_arab+ix_unterm" \
  "${ROOTDIR}/999999/1603/45/49/1603.45.49.hxl.csv" \
  | hxlselect --query="#country+code+num+v_m49>0" \
  | hxladd --before --spec="#item+rem+i_zxx+is_zmth+ix_unfts={{#country+code+v_fts}}" \
  | hxladd --before --spec="#item+rem+i_zxx+is_zmth+ix_unreliefweb={{#country+code+v_reliefweb}}" \
  | hxladd --before --spec="#item+rem+i_zxx+is_zmth+ix_unhrinfo={{#country+code+v_hrinfo_country}}" \
  | hxladd --before --spec="#item+rem+i_zxx+is_zmth+ix_unm49={{#country+code+num+v_m49}}" \
  | hxladd --before --spec="#item+conceptum+codicem={{#country+code+num+v_m49}}" \
  | hxlsort --tags="#item+conceptum" \
  > "${ROOTDIR}/999999/1603/45/49/1603.45.49.tm.hxl.csv"

# @TODO: only do this if hxl did not removed empty header files ,,,,,,
sed -i '1d' "${ROOTDIR}/999999/1603/45/49/1603.45.49.tm.hxl.csv"

### 1603.45.49.tm.hxl.csv --> 1603.45.49.no1.tm.hxl.csv ________________________

hxlrename \
  --rename="#country+code+v_iso2:#item+rem+i_zxx+is_latn+ix_iso3166p1a2" \
  --rename="#country+code+v_iso3:#item+rem+i_zxx+is_latn+ix_iso3166p1a3" \
  "${ROOTDIR}/999999/1603/45/49/1603.45.49.tm.hxl.csv" \
  | hxladd --before --spec="#item+conceptum+numerordinatio=${PRAEFIXUM}{{(#item+conceptum+codicem)+1-1}}" \
  | hxlcut --include="#item+conceptum,#item+rem" \
  > "${ROOTDIR}/1603/45/49/1603.45.49.no1.tm.hxl.csv"

# @TODO: only do this if hxl did not removed empty header files ,,,,,,
sed -i '1d' "${ROOTDIR}/1603/45/49/1603.45.49.no1.tm.hxl.csv"

set +x