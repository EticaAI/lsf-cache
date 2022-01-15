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
