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

ROOTDIR="$(pwd)"

_2600_b60__dictionarium="NOP,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP"
_2600_b60__US_ASCII_alpha_lowercase="a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
_2600_b60__US_ASCII_alpha_uppercase="A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z"
_2600_b60__US_ASCII_alphanum_lowercase="0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
_2600_b60__US_ASCII_alphanum_uppercase="0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z"
export _2600_b60__US_ASCII_alpha_lowercase
export _2600_b60__US_ASCII_alpha_uppercase
export _2600_b60__US_ASCII_alphanum_lowercase
export _2600_b60__US_ASCII_alphanum_uppercase

# shellcheck source=999999999.sh
. "$ROOTDIR"/999999999/999999999.sh

#######################################
# ...
#
# Globals:
#   ROOTDIR
# Arguments:
#   None
#######################################
bootstrap_999999_2600() {
  codewordlist="$1"
  totalitems=$((${2:-2}))
  codewordlist_arr=$(echo "${codewordlist}" | tr ',' '\n')
  # echo "${codewordlist}" | tr ',' '\n'  | while IFS= read -r a1; do
  finalstring=""
  while IFS= read -r a1; do
    if [ "$totalitems" -lt 2 ]; then
      codenum="$(numerordinatio_translatio_in_digito__beta "$a1" 1)"
      finalstring+="$codenum"$'\t'"$a1"$'\n'
      continue
    fi
    # echo "${codewordlist}" | tr ',' '\n'  | while IFS= read -r b2; do
    while IFS= read -r b2; do
      if [ "$totalitems" -lt 3 ]; then
        codenum="$(numerordinatio_translatio_in_digito__beta "$a1$b2" 2)"
        # printf '%s\t%s\n' "$codenum" "$a1$b2"
        # finalstring+=$(printf '%s\t%s\n' "$codenum" "$a1$b2")
        finalstring+="$codenum"$'\t'"$a1$b2"$'\n'
        continue
      fi
      # echo "${codewordlist}" | tr ',' '\n'  | while IFS= read -r c3; do
      while IFS= read -r c3; do
        if [ "$totalitems" -lt 4 ]; then
          codenum="$(numerordinatio_translatio_in_digito__beta "$a1$b2$c3" 3)"
          # printf '%s\t%s\n' "$codenum" "$a1$b2$c3"
          # finalstring+=$(printf '%s\t%s\n' "$codenum" "$a1$b2$c3")
          finalstring+="$codenum"$'\t'"$a1$b2$c3"$'\n'
          # echo "$a1$b2$c3"
          continue
        fi
        # echo "${codewordlist}" | tr ',' '\n'  | while IFS= read -r d4; do
        while IFS= read -r d4; do
          if [ "$totalitems" -lt 5 ]; then
            codenum="$(numerordinatio_translatio_in_digito__beta "$a1$b2$c3$d4" 4)"
            # printf '%s\t%s\n' "$codenum" "$a1$b2$c3$d4"
            # finalstring+=$(printf '%s\t%s\n' "$codenum" "$a1$b2$c3$d4")
            finalstring+="$codenum"$'\t'"$a1$b2$c3$d4"$'\n'
            # echo "$a1$b2$c3$d4"
            continue
          fi
          # echo "${codewordlist}" | tr ',' '\n'  | while IFS= read -r e5; do
          while IFS= read -r e5; do
            if [ "$totalitems" -lt 6 ]; then
              codenum="$(numerordinatio_translatio_in_digito__beta "$a1$b2$c3$d4$e5" 5)"
              # printf '%s\t%s\n' "$codenum" "$a1$b2$c3$d4$e5"
              # finalstring+=$(printf '%s\t%s\n' "$codenum" "$a1$b2$c3$d4$e5")
              finalstring+="$codenum"$'\t'"$a1$b2$c3$d4$e5"$'\n'
              # echo "$a1$b2$c3$d4$e5"
              continue
            fi
            echo "ERROR: implemented only for short codes"
            return 1
          done  <<< "$codewordlist_arr"
        done  <<< "$codewordlist_arr"
      done  <<< "$codewordlist_arr"
    done  <<< "$codewordlist_arr"
  done <<< "$codewordlist_arr"
  printf "%s" "$finalstring"
}

### US_ASCII_alpha _____________________________________________________________

# TODO: implement some way to rebuild the cache without deleting the files
if [ ! -f "${ROOTDIR}/999999/2600/a-z__1__b60.tsv" ]; then
  bootstrap_999999_2600 "${_2600_b60__US_ASCII_alpha_lowercase}" 1 \
    > "${ROOTDIR}/999999/2600/a-z__1__b60.tsv"
  sort -k1 -n "${ROOTDIR}"/999999/2600/a-z__1__b60.tsv > "${ROOTDIR}"/999999/2600/a-z__1__b60.sorted.tsv
fi

# TODO: implement some way to rebuild the cache without deleting the files
if [ ! -f "${ROOTDIR}/999999/2600/a-z__2__b60.tsv" ]; then
  bootstrap_999999_2600 "${_2600_b60__US_ASCII_alpha_lowercase}" 2 \
    > "${ROOTDIR}/999999/2600/a-z__2__b60.tsv"
  sort -k1 -n "${ROOTDIR}"/999999/2600/a-z__2__b60.tsv > "${ROOTDIR}"/999999/2600/a-z__2__b60.sorted.tsv
fi

# TODO: implement some way to rebuild the cache without deleting the files
if [ ! -f "${ROOTDIR}/999999/2600/a-z__3__b60.tsv" ]; then
  bootstrap_999999_2600 "${_2600_b60__US_ASCII_alpha_lowercase}" 3 \
    > "${ROOTDIR}/999999/2600/a-z__3__b60.tsv"
  sort -k1 -n "${ROOTDIR}"/999999/2600/a-z__3__b60.tsv > "${ROOTDIR}"/999999/2600/a-z__3__b60.sorted.tsv
fi

# # TODO: implement some way to rebuild the cache without deleting the files
# if [ ! -f "${ROOTDIR}/999999/2600/a-z__4__b60.tsv" ]; then
#   bootstrap_999999_2600 "${_2600_b60__US_ASCII_alpha_lowercase}" 4 \
#     > "${ROOTDIR}/999999/2600/a-z__4__b60.tsv"
# fi
# # TODO: implement some way to rebuild the cache without deleting the files
# if [ ! -f "${ROOTDIR}/999999/2600/a-z__5__b60.tsv" ]; then
#   bootstrap_999999_2600 "${_2600_b60__US_ASCII_alpha_lowercase}" 5 \
#     > "${ROOTDIR}/999999/2600/a-z__5__b60.tsv"
# fi


### US_ASCII_alphanum _____________________________________________________________

# TODO: implement some way to rebuild the cache without deleting the files
if [ ! -f "${ROOTDIR}/999999/2600/0-9a-z__1__b60.tsv" ]; then
  bootstrap_999999_2600 "${_2600_b60__US_ASCII_alphanum_lowercase}" 1 \
    > "${ROOTDIR}/999999/2600/0-9a-z__1__b60.tsv"
  sort -k1 -n "${ROOTDIR}"/999999/2600/0-9a-z__1__b60.tsv > "${ROOTDIR}"/999999/2600/0-9a-z__1__b60.sorted.tsv
fi

# TODO: implement some way to rebuild the cache without deleting the files
if [ ! -f "${ROOTDIR}/999999/2600/0-9a-z__2__b60.tsv" ]; then
  bootstrap_999999_2600 "${_2600_b60__US_ASCII_alphanum_lowercase}" 2 \
    > "${ROOTDIR}/999999/2600/0-9a-z__2__b60.tsv"
  sort -k1 -n "${ROOTDIR}"/999999/2600/0-9a-z__2__b60.tsv > "${ROOTDIR}"/999999/2600/0-9a-z__2__b60.sorted.tsv
fi

# TODO: implement some way to rebuild the cache without deleting the files
if [ ! -f "${ROOTDIR}/999999/2600/0-9a-z__3__b60.tsv" ]; then
  bootstrap_999999_2600 "${_2600_b60__US_ASCII_alphanum_lowercase}" 3 \
    > "${ROOTDIR}/999999/2600/0-9a-z__3__b60.tsv"
  sort -k1 -n "${ROOTDIR}"/999999/2600/0-9a-z__3__b60.tsv > "${ROOTDIR}"/999999/2600/0-9a-z__3__b60.sorted.tsv
fi

# # TODO: implement some way to rebuild the cache without deleting the files
# if [ ! -f "${ROOTDIR}/999999/2600/0-9a-z__4__b60.tsv" ]; then
#   bootstrap_999999_2600 "${_2600_b60__US_ASCII_alphanum_lowercase}" 4 \
#     > "${ROOTDIR}/999999/2600/0-9a-z__4__b60.tsv"
# fi
# # TODO: implement some way to rebuild the cache without deleting the files
# if [ ! -f "${ROOTDIR}/999999/2600/0-9a-z__5__b60.tsv" ]; then
#   bootstrap_999999_2600 "${_2600_b60__US_ASCII_alphanum_lowercase}" 5 \
#     > "${ROOTDIR}/999999/2600/0-9a-z__5__b60.tsv"
# fi

# bootstrap_999999_2600 "${_2600_b60__US_ASCII_alpha_lowercase}" 5 999999/2600