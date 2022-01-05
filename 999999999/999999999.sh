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
    if [ "$(contains "$rawheader" "Pcode" )" ] || [ "$(contains "$rawheader" "pcode" )" ]; then
        return 0
    fi
    return 1
}

#######################################
# Return if header is likely be an Pcode
#
# Globals:
#   None
# Arguments:
#   rawheader
un_pcode_rawheader_is_admin_name() {
    rawheader="$1"
    if [ "$(contains "$rawheader" "Adm" )" ] || [ "$(contains "$rawheader" "adm" )" ]; then
        if [ "$(contains "$rawheader" "Name" )" ] || [ "$(contains "$rawheader" "name" )" ]; then
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

un_pcode_rawheader_is_pcode "admin1Name_ar" || echo "admin1Name_ar not Pcode"
un_pcode_rawheader_is_pcode "admin1Name_ar" && echo "admin1Name_ar is Pcode"
un_pcode_rawheader_is_pcode "admin2Pcode" && echo "admin2Pcode is Pcode"

# un_pcode_rawheader_is_admin_name "admin1Name_ar" || echo "admin1Name_ar not name"
# un_pcode_rawheader_is_admin_name "admin1Name_ar" && echo "admin1Name_ar is name"
# un_pcode_rawheader_is_admin_name "admin2Pcode" && echo "admin2Pcode is name"