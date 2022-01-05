#!/bin/sh
#===============================================================================
#
#          FILE:  999999999.sh
#
#         USAGE:  #import on other scripts
#                 . "$ROOTDIR"/999999999/999999999.sh
#
#   DESCRIPTION:  Generic utility helper for POSIX shell
#
#       OPTIONS:  ---
#
#  REQUIREMENTS:  - POSIX shell (or better)
#
#          BUGS:  ---
#         NOTES:  ---
#        AUTHOR:  Emerson Rocha <rocha[at]ieee.org>
#       COMPANY:  EticaAI
#       LICENSE:  Public Domain dedication or Zero-Clause BSD
#                 SPDX-License-Identifier: Unlicense OR 0BSD
#       VERSION:  v1.0
#       CREATED:  2022-01-05 02:39 UTC
#      REVISION:  ---
#===============================================================================

# Quick tests
#   ./999999999/999999999.sh

#######################################
# contains(string, substring)
#
# Returns 0 if the specified string contains the specified substring,
# otherwise returns 1.
#
# Author:
#    https://stackoverflow.com/a/8811800/894546
# Example:
#    contains "abcd" "e" || echo "abcd does not contain e"
#    contains "abcd" "ab" && echo "abcd contains ab"
# Globals:
#   None
# Arguments:
#   string
#   substring
#######################################
contains() {
    string="$1"
    substring="$2"
    if test "${string#*"$substring"}" != "$string"
    then
        return 0    # $substring is in $string
    else
        return 1    # $substring is not in $string
    fi
}


#######################################
# Normalization of PCode sheets. The RawSheetname may (or not) have ISO3166p1a3
# so this avoid redundancy.
#
# Globals:
#   None
# Arguments:
#   ISO3166p1a3
#   RawSheetname
#######################################
un_pcode_sheets_norma() {
  number=$(echo "$2" | tr -d -c 0-9)
  echo "$1_$number"
}

#######################################
# Do "the best possible" to infer HXL heading.
# Globals:
#   None
# Arguments:
#   RawSheetHeader
#######################################
un_pcode_hxl_from_header() {
  number=$(echo "$2" | tr -d -c 0-9)
  echo "$1_$number"
}

#######################################
# Return if header is likely be an Pcode
#
# Example:
#  un_pcode_rawheader_is_pcode "admin1Name_ar" || echo "admin1Name_ar not Pcode"
#  un_pcode_rawheader_is_pcode "admin2Pcode" && echo "admin2Pcode is Pcode"
# Globals:
#   None
# Arguments:
#   rawheader
un_pcode_rawheader_is_pcode() {
    rawheader="$1"

    # if echo "$rawheader" | grep -q -E "Pcode|pcode"; then
    if echo "$rawheader" | grep -q -E "Pcode|pcode"; then
    # if echo "$rawheader" | grep -E "Pcode|pcode" | wc -c; then
        # echo "   pentrou"
        return 1
    else
        return 0
    fi


    # if [ "$(contains "$rawheader" "Pcode" )" ] || [ "$(contains "$rawheader" "adm" )" ]; then
    #     return 0
    # fi
    # return 1
    # if [ "$(contains "$rawheader" "Pcode" )" ] && [ "$(contains "$rawheader" "adm" )" ]; then
    # if [ "$(contains "$rawheader" "Pcode" )" ] || [ "$(contains "$rawheader" "pcode" )" ]; then
    #     return 0
    # fi
    # return 1
}

#######################################
# Return if header is likely be an Pcode
#
# Globals:
#   None
# Arguments:
#   rawheader
un_pcode_rawheader_is_name() {
    rawheader="$1"
    if [ ! "$(contains "$rawheader" "Adm" )" ] || [ ! "$(contains "$rawheader" "adm" )" ]; then
        if [ ! "$(contains "$rawheader" "Name" )" ] || [ ! "$(contains "$rawheader" "name" )" ]; then
            return 0
        fi
    fi
    return 1
}

#######################################
# Trim whitespace
# Globals:
#   None
# Arguments:
#   String
#######################################
trim() {
  trimmed=$(echo "$1" | xargs echo -n)
  echo "$trimmed"
}

# contains "abcd" "e" || echo "abcd does not contain e"
# contains "abcd" "ab" && echo "abcd contains ab"

# echo ""

# un_pcode_rawheader_is_pcode "admin1Name_ar" || echo "admin1Name_ar not Pcode"
# un_pcode_rawheader_is_pcode "admin1Name_ar" && echo "admin1Name_ar is Pcode"
# un_pcode_rawheader_is_pcode "admin2Pcode" || echo "admin2Pcode is Pcode"
# un_pcode_rawheader_is_pcode "admin2Pcode" && echo "admin2Pcode is not Pcode"
# un_pcode_rawheader_is_pcode "lalala" || echo "lalala is Pcode"
# un_pcode_rawheader_is_pcode "lalala" && echo "lalala is not Pcode"

# echo ""

# # un_pcode_rawheader_is_name "admin1Name_ar" || echo "admin1Name_ar not name"
# # un_pcode_rawheader_is_name "admin1Name_ar" && echo "admin1Name_ar is name"
# # un_pcode_rawheader_is_name "admin2Pcode" && echo "admin2Pcode is name"

# # un_pcode_rawheader_is_name "admin1Name_ar" || echo "admin1Name_ar not name"
# # un_pcode_rawheader_is_name "admin1Name_ar" && echo "admin1Name_ar is name"
# # un_pcode_rawheader_is_name "admin2Pcode" || echo "admin2Pcode is name"
# # un_pcode_rawheader_is_name "admin2Pcode" && echo "admin2Pcode is not name"
# # un_pcode_rawheader_is_name "lalala" || echo "lalala is name"
# # un_pcode_rawheader_is_name "lalala" && echo "lalala is not name"

# string='This is a sample 123 text and some 987 numbers'
# echo "$string" | sed -rn 's/[^[:digit:]]*([[:digit:]]+)[^[:digit:]]+([[:digit:]]+)[^[:digit:]]*/\1 \2/p'

# echo "ooi"

# string2='admin1Name_ar'
# # echo "$string2" | sed -rn 's/[^[:digit:]]*([[:digit:]]+)[^[:digit:]]+([[:digit:]]+)[^[:digit:]]*/\1 \2/p'
# echo "$string2" | sed -rn 's/[^[:digit:]]*([[:digit:]]+)[^[:digit:]]+([[:digit:]]+)[^[:digit:]]*/\1 \2/p'


# echo "fini"


# all 3 groups
# echo "admin2Pcode" | sed -E 's/^(Admin|admin)([0-9]){1}(Pcode|pcode)$/_\1_ _\2_ _\3_/'
# echo "admin2AltName2_zh" | sed -E 's/^(Admin|admin)([0-9]){1}(Pcode|pcode)$/_\1_ _\2_ _\3_/'

# # Admin level (of only if matches PCode)
# echo "admin2Pcode" | sed -E 's/^(Admin|admin)([0-9])(Pcode|pcode)$/_\1_ _\2_ _\3_/'
# echo "admin3Name_sw" | sed -E 's/^(Admin|admin)([0-9])(Pcode|pcode)$/_\1_ _\2_ _\3_/'
# echo "admin2AltName2_zh" | sed -E 's/^(Admin|admin)([0-9])(Pcode|pcode)$/_\1_ _\2_ _\3_/'


# https://stackoverflow.com/questions/6011661/regexp-sed-suppress-no-match-output


un_pcode_rawheader_admin_level() {
    rawheader="$1"
    sed_result=$(echo "${rawheader}" | sed -E 's/^(Admin|admin)([0-9]){1}(Pcode|pcode)$/\2/')
    # If sed fail, it returns entire line as it was the input
    if [ "$rawheader" != "$sed_result" ]; then
        echo "$sed_result"
        return 0
    fi
    echo ""
    return 1
}

un_pcode_rawheader_admin_level "admin2Pcode" || echo "admin2Pcode no admin of pcode"
un_pcode_rawheader_admin_level "admin2Pcode" && echo "admin2Pcode is admin of pcode"
un_pcode_rawheader_admin_level "admin2AltName2_zh" || echo "admin2AltName2_zh no admin  of pcode"
un_pcode_rawheader_admin_level "admin2AltName2_zh" && echo "admin2AltName2_zh is admin  of pcode"