#!/bin/bash
#===============================================================================
#
#          FILE:  2600.sh
#
#         USAGE:  ./999999999/2600.sh
#                 time ./999999999/2600.sh
#
#   DESCRIPTION:  ---
#
#       OPTIONS:  ---
#
#  REQUIREMENTS:  - Bash shell (or better)
#                 - wget
#                 - libhxl (https://github.com/HXLStandard/libhxl-python)
#                 - csvkit (https://github.com/wireservice/csvkit)
#          BUGS:  ---
#         NOTES:  ---
#        AUTHOR:  Emerson Rocha <rocha[at]ieee.org>
#       COMPANY:  EticaAI
#       LICENSE:  Public Domain dedication or Zero-Clause BSD
#                 SPDX-License-Identifier: Unlicense OR 0BSD
#       VERSION:  v1.0
#       CREATED:  2022-01-07 22:57 UTC
#      REVISION:  ---
#===============================================================================
# Comment next line if not want to stop on first error
set -e
# set -x

ROOTDIR="$(pwd)"

_2600_b60__dictionarium="NOP,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP"
_2600_b60__US_ASCII_alpha_lowercase="a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
_2600_b60__US_ASCII_alpha_uppercase="A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z"
_2600_b60__US_ASCII_alphanum_lowercase="0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
_2600_b60__US_ASCII_alphanum_uppercase="0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z"
_2600_b60__US_ASCII_alpha_seed=",a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,"
_2600_b60__US_ASCII_alphanum_seed=",0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,"
export _2600_b60__US_ASCII_alpha_lowercase
export _2600_b60__US_ASCII_alpha_uppercase
export _2600_b60__US_ASCII_alphanum_lowercase
export _2600_b60__US_ASCII_alphanum_uppercase

# shellcheck source=999999999.lib.sh
. "$ROOTDIR"/999999999/999999999.lib.sh

### US_ASCII_alpha _____________________________________________________________

if [ ! -f "${ROOTDIR}/1603/2600/2/a-z__1__b60.tsv" ]; then
  ./999999999/0/2600.py --actionem-codex-tabulae-completum \
    --verbum-limiti=1 \
    --codex-verbum-tabulae="${_2600_b60__US_ASCII_alpha_seed}" \
    >"${ROOTDIR}/1603/2600/2/a-z__1__b60.tsv"

  sort -k1 -n "${ROOTDIR}"/1603/2600/2/a-z__1__b60.tsv >"${ROOTDIR}"/1603/2600/2/a-z__1__b60.sorted.tsv
  cut -f1 "${ROOTDIR}"/1603/2600/2/a-z__1__b60.sorted.tsv | uniq -d | xargs -I '{}' sh -c "grep -w '{}' ""${ROOTDIR}""/1603/2600/a-z__1__b60.sorted.tsv" >"${ROOTDIR}"/1603/2600/2/a-z__1__b60.non-uniq.sorted.tsv
fi

if [ ! -f "${ROOTDIR}/1603/2600/2/a-z__2__b60.tsv" ]; then
  ./999999999/0/2600.py --actionem-codex-tabulae-completum \
    --verbum-limiti=2 \
    --codex-verbum-tabulae="${_2600_b60__US_ASCII_alpha_seed}" \
    >"${ROOTDIR}/1603/2600/2/a-z__2__b60.tsv"

  sort -k1 -n "${ROOTDIR}"/1603/2600/2/a-z__2__b60.tsv >"${ROOTDIR}"/1603/2600/2/a-z__2__b60.sorted.tsv
  cut -f1 "${ROOTDIR}"/1603/2600/2/a-z__2__b60.sorted.tsv | uniq -d | xargs -I '{}' sh -c "grep -w '{}' ""${ROOTDIR}""/1603/2600/a-z__2__b60.sorted.tsv" >"${ROOTDIR}"/1603/2600/2/a-z__2__b60.non-uniq.sorted.tsv
fi

if [ ! -f "${ROOTDIR}/1603/2600/2/a-z__3__b60.tsv" ]; then
  ./999999999/0/2600.py --actionem-codex-tabulae-completum \
    --verbum-limiti=3 \
    --codex-verbum-tabulae="${_2600_b60__US_ASCII_alpha_seed}" \
    >"${ROOTDIR}/1603/2600/2/a-z__3__b60.tsv"

  sort -k1 -n "${ROOTDIR}"/1603/2600/2/a-z__3__b60.tsv >"${ROOTDIR}"/1603/2600/2/a-z__3__b60.sorted.tsv
  cut -f1 "${ROOTDIR}"/1603/2600/2/a-z__3__b60.sorted.tsv | uniq -d | xargs -I '{}' sh -c "grep -w '{}' ""${ROOTDIR}""/1603/2600/a-z__3__b60.sorted.tsv" >"${ROOTDIR}"/1603/2600/2/a-z__3__b60.non-uniq.sorted.tsv
fi

if [ ! -f "${ROOTDIR}/1603/2600/2/a-z__4__b60.tsv" ]; then
  ./999999999/0/2600.py --actionem-codex-tabulae-completum \
    --verbum-limiti=4 \
    --codex-verbum-tabulae="${_2600_b60__US_ASCII_alpha_seed}" \
    >"${ROOTDIR}/1603/2600/2/a-z__4__b60.tsv"

  sort -k1 -n "${ROOTDIR}"/1603/2600/2/a-z__4__b60.tsv >"${ROOTDIR}"/1603/2600/2/a-z__4__b60.sorted.tsv
  cut -f1 "${ROOTDIR}"/1603/2600/2/a-z__4__b60.sorted.tsv | uniq -d | xargs -I '{}' sh -c "grep -w '{}' ""${ROOTDIR}""/1603/2600/a-z__4__b60.sorted.tsv" >"${ROOTDIR}"/1603/2600/2/a-z__4__b60.non-uniq.sorted.tsv
fi

### US_ASCII_alphanum _____________________________________________________________

if [ ! -f "${ROOTDIR}/1603/2600/2/0-9a-z__1__b60.tsv" ]; then
  ./999999999/0/2600.py --actionem-codex-tabulae-completum \
    --verbum-limiti=1 \
    --codex-verbum-tabulae="${_2600_b60__US_ASCII_alphanum_seed}" \
    >"${ROOTDIR}/1603/2600/2/0-9a-z__1__b60.tsv"

  sort -k1 -n "${ROOTDIR}"/1603/2600/2/0-9a-z__1__b60.tsv >"${ROOTDIR}"/1603/2600/2/0-9a-z__1__b60.sorted.tsv
  cut -f1 "${ROOTDIR}"/1603/2600/2/0-9a-z__1__b60.sorted.tsv | uniq -d | xargs -I '{}' sh -c "grep -w '{}' ""${ROOTDIR}""/1603/2600/0-9a-z__1__b60.sorted.tsv" >"${ROOTDIR}"/1603/2600/2/0-9a-z__1__b60.non-uniq.sorted.tsv
fi

if [ ! -f "${ROOTDIR}/1603/2600/2/0-9a-z__2__b60.tsv" ]; then
  ./999999999/0/2600.py --actionem-codex-tabulae-completum \
    --verbum-limiti=2 \
    --codex-verbum-tabulae="${_2600_b60__US_ASCII_alphanum_seed}" \
    >"${ROOTDIR}/1603/2600/2/0-9a-z__2__b60.tsv"

  sort -k1 -n "${ROOTDIR}"/1603/2600/2/0-9a-z__2__b60.tsv >"${ROOTDIR}"/1603/2600/2/0-9a-z__2__b60.sorted.tsv
  cut -f1 "${ROOTDIR}"/1603/2600/2/0-9a-z__2__b60.sorted.tsv | uniq -d | xargs -I '{}' sh -c "grep -w '{}' ""${ROOTDIR}""/1603/2600/0-9a-z__2__b60.sorted.tsv" >"${ROOTDIR}"/1603/2600/2/0-9a-z__2__b60.non-uniq.sorted.tsv
fi

if [ ! -f "${ROOTDIR}/1603/2600/2/0-9a-z__3__b60.tsv" ]; then
  ./999999999/0/2600.py --actionem-codex-tabulae-completum \
    --verbum-limiti=3 \
    --codex-verbum-tabulae="${_2600_b60__US_ASCII_alphanum_seed}" \
    >"${ROOTDIR}/1603/2600/2/0-9a-z__3__b60.tsv"

  sort -k1 -n "${ROOTDIR}"/1603/2600/2/0-9a-z__3__b60.tsv >"${ROOTDIR}"/1603/2600/2/0-9a-z__3__b60.sorted.tsv
  cut -f1 "${ROOTDIR}"/1603/2600/2/0-9a-z__3__b60.sorted.tsv | uniq -d | xargs -I '{}' sh -c "grep -w '{}' ""${ROOTDIR}""/1603/2600/0-9a-z__3__b60.sorted.tsv" >"${ROOTDIR}"/1603/2600/2/0-9a-z__3__b60.non-uniq.sorted.tsv
fi

if [ ! -f "${ROOTDIR}/1603/2600/2/0-9a-z__4__b60.tsv" ]; then
  ./999999999/0/2600.py --actionem-codex-tabulae-completum \
    --verbum-limiti=4 \
    --codex-verbum-tabulae="${_2600_b60__US_ASCII_alphanum_seed}" \
    >"${ROOTDIR}/1603/2600/2/0-9a-z__4__b60.tsv"

  sort -k1 -n "${ROOTDIR}"/1603/2600/2/0-9a-z__4__b60.tsv >"${ROOTDIR}"/1603/2600/2/0-9a-z__4__b60.sorted.tsv
  cut -f1 "${ROOTDIR}"/1603/2600/2/0-9a-z__4__b60.sorted.tsv | uniq -d | xargs -I '{}' sh -c "grep -w '{}' ""${ROOTDIR}""/1603/2600/0-9a-z__4__b60.sorted.tsv" >"${ROOTDIR}"/1603/2600/2/0-9a-z__4__b60.non-uniq.sorted.tsv
fi

# bootstrap_999999_2600 "${_2600_b60__US_ASCII_alpha_lowercase}" 5 999999/1613/2600

# cut -d, -f2 999999/1613/2600/0-9a-z__2__b60.sorted.tsv | uniq -d | grep -Fv 2r
# cut -f1 999999/1613/2600/0-9a-z__2__b60.sorted.tsv | uniq -d
# cut -f1 999999/1613/2600/0-9a-z__2__b60.sorted.tsv | uniq -d
# cut -f1 999999/1613/2600/0-9a-z__2__b60.sorted.tsv | uniq -d | xargs -0 echo "{} lala

# cut -f1 999999/1613/2600/0-9a-z__2__b60.sorted.tsv | uniq -d | xargs -I '{}' sh -c 'echo "{}"'
# cut -f1 999999/1613/2600/0-9a-z__2__b60.sorted.tsv | uniq -d | xargs -I '{}' sh -c 'grep -w "{}" 999999/1613/2600/0-9a-z__2__b60.sorted.tsv'

### TODO: https://www.unicode.org/Public/UCD/latest/ucd/extracted/DerivedNumericType.txt
# ./999999999/0/2600.py --actionem-tabulam-numerae

UNICODE_UCD_DERIVED_NUMERIC_TYPE="https://www.unicode.org/Public/UCD/latest/ucd/extracted/DerivedNumericType.txt"
#######################################
# Download 1603_45_49 from external source files
#
# Globals:
#   ROOTDIR
#   UNICODE_UCD_DERIVED_NUMERIC_TYPE
# Arguments:
#   None
# Outputs:
#   Writes to 999999/1603/87/1603_87__DerivedNumericType.txt
#######################################
1603_87__external_fetch__DerivedNumericType() {
  objectivum_archivum="${ROOTDIR}/999999/1603/87/1603_87__DerivedNumericType.txt"
  objectivum_archivum_temporarium="${ROOTDIR}/999999/0/1603_87__DerivedNumericType.txt"

  if [ -z "$(stale_archive "$objectivum_archivum")" ]; then return 0; fi

  echo "${FUNCNAME[0]} stale data on [$objectivum_archivum], refreshing..."

  curl --header "Accept: text/csv" \
    --compressed --silent --show-error \
    --get "$UNICODE_UCD_DERIVED_NUMERIC_TYPE" \
    --output "$objectivum_archivum_temporarium"

  file_update_if_necessary txt "$objectivum_archivum_temporarium" "$objectivum_archivum"
}

# https://earthly.dev/blog/bash-string/

#######################################
# Download external source files.
# Note: using raw tab file for now.
#
# Globals:
#   ROOTDIR
# Arguments:
#   [File] 999999/1603/87/1603_87__DerivedNumericType.txt
# Outputs:
#   [File] 999999/1603/87/1603_87__DerivedNumericType.txt
#######################################
1603_87__process_DerivedNumericType() {
  fontem_archivum="${ROOTDIR}/999999/1603/87/1603_87__DerivedNumericType.txt"
  objectivum_archivum="${ROOTDIR}//999999/1603/87/1603_87__tabulam-numerae-decimali.hxl.csv"
  objectivum_archivum_temporarium="${ROOTDIR}/999999/0/1603_87__tabulam-numerae-decimali.hxl.csv"
  objectivum_archivum_temporarium_2="${ROOTDIR}/999999/0/1603_87__DerivedNumericType_reduced.txt"

  if [ -z "$(changed_recently "$fontem_archivum")" ]; then return 0; fi

  echo "${FUNCNAME[0]} sources changed_recently. Reloading..."

  grep '; Decimal # Nd' "${fontem_archivum}" > "$objectivum_archivum_temporarium_2"

  echo "#item+id,#item+name,#item+start,#item+end" > "$objectivum_archivum_temporarium"

  while read -r lineam; do
    codicem=""
    initiale=""
    finale=""
    nomen=""
    # echo "$lineam"
    if [[ "$lineam" =~ (.*)\.\.(.*)\ [[:space:]]+\;(.*)\[\1\0\]\ (.*)\ \D\I\G\I\T\ \Z\E\R\O(.*)  ]]; then
      # echo "full = ${BASH_REMATCH[0]}"
      # echo "start = '${BASH_REMATCH[1]}'"
      # echo "end = '${BASH_REMATCH[2]}'"
      # echo "3 = '${BASH_REMATCH[3]}'"
      # echo "4 = '${BASH_REMATCH[4]}'"
      # echo "5 = '${BASH_REMATCH[5]}'"
      # echo "6 = '${BASH_REMATCH[6]}'"
      # initiale=${BASH_REMATCH[1]//[[:space:]]/}
      initiale=${BASH_REMATCH[1]//[[:space:]]/}
      codicem=$(echo "obase=10; ibase=16; $initiale" | bc)
      finale=${BASH_REMATCH[2]//[[:space:]]/}
      nomen=${BASH_REMATCH[4]}

      # echo "codicem = '$codicem'"
      # echo "initiale = '$initiale'"
      # echo "finale = '$finale'"
      # echo "nomen = '$nomen'"

      echo "${codicem},${nomen},'${initiale}','${finale}'" >> "$objectivum_archivum_temporarium"

      # This is just a lazy way to copypaste to officinam/999999999/0/2600.py
      # echo "'${nomen}': [0x${initiale},0x${finale}],"

    else
      # TODO: fix these
      # 0030..0039    ; Decimal # Nd  [10] DIGIT ZERO..DIGIT NINE
      # 1D7CE..1D7FF  ; Decimal # Nd  [50] MATHEMATICAL BOLD DIGIT ZERO..MATHEMATICAL MONOSPACE DIGIT NINE
      echo "ERROR! Not proper format [$lineam]"
    fi

  done <"$objectivum_archivum_temporarium_2"

  rm "$objectivum_archivum_temporarium_2"

  # hxlrename \
  #   --rename="#country+name+i_en+alt+v_unterm:#item+rem+i_eng+is_latn+ix_unterm" \
  #   --rename="#country+name+i_fr+alt+v_unterm:#item+rem+i_fra+is_latn+ix_unterm" \
  #   --rename="#country+name+i_es+alt+v_unterm:#item+rem+i_spa+is_latn+ix_unterm" \
  #   --rename="#country+name+i_ru+alt+v_unterm:#item+rem+i_rus+is_cyrl+ix_unterm" \
  #   --rename="#country+name+i_zh+alt+v_unterm:#item+rem+i_zho+is_hans+ix_unterm" \
  #   --rename="#country+name+i_ar+alt+v_unterm:#item+rem+i_ara+is_arab+ix_unterm" \
  #   "${fontem_archivum}" |
  #   hxlselect --query="#country+code+num+v_m49>0" |
  #   hxladd --before --spec="#item+rem+i_zxx+is_zmth+ix_unfts={{#country+code+v_fts}}" |
  #   hxladd --before --spec="#item+rem+i_zxx+is_zmth+ix_unreliefweb={{#country+code+v_reliefweb}}" |
  #   hxladd --before --spec="#item+rem+i_zxx+is_zmth+ix_unhrinfo={{#country+code+v_hrinfo_country}}" |
  #   hxladd --before --spec="#item+rem+i_zxx+is_zmth+ix_unm49={{#country+code+num+v_m49}}" |
  #   hxladd --before --spec="#item+conceptum+codicem={{#country+code+num+v_m49}}" |
  #   hxlsort --tags="#item+conceptum" \
  #     >"${objectivum_archivum_temporarium}"

  # # Strip empty header (already is likely to be ,,,,,,)
  # sed -i '1d' "${objectivum_archivum_temporarium}"

  file_update_if_necessary csv "$objectivum_archivum_temporarium" "$objectivum_archivum"
}

1603_87__external_fetch__DerivedNumericType
1603_87__process_DerivedNumericType

./999999999/0/2600.py --actionem-tabulam-numerae --tabulam-numerae-finale 10000 > "${ROOTDIR}/1603/2600/1/1603_2600_1.tm.hxl.tsv"

# https://www.unicode.org/Public/UCD/latest/ucd/extracted/DerivedNumericType.txt
