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


#######################################
# Only return numeric PCode admin level if the item matches typical raw CSV
# header of a PCode (excludes administrative names)
#
# Globals:
#   None
# Arguments:
#   csv_header_item
#######################################
un_pcode_csvheader_pcode_level() {
    csv_header_item="$1"
    sed_result=$(echo "${csv_header_item}" | sed -E 's/^(Admin|admin)([0-9]{1})(Pcode|pcode)$/\2/')
    # If sed fail, it returns entire line as it was the input
    if [ "$csv_header_item" != "$sed_result" ]; then
        echo "$sed_result"
    fi
    echo ""
}

#######################################
# Return administrative level either from PCode or administrative name
#
# Globals:
#   None
# Arguments:
#   csv_header_item
#######################################
un_pcode_csvheader_administrative_level() {
    csv_header_item="$1"

    # TODO: test both PCode and Translation type
    sed_result=$(echo "${csv_header_item}" | sed -E 's/^(Admin|admin)([0-9]{1})(Pcode|pcode|Name|RefName|AltName|AltName1|AltName2)(.+)$/\2/')
    # If sed fail, it returns entire line as it was the input
    if [ "$csv_header_item" != "$sed_result" ]; then
        echo "$sed_result"
        # return 0
    fi
    echo ""
    # return 1
}

#######################################
# For a typical CSV header, return if is generic "date"
#
# Globals:
#   None
# Arguments:
#   csv_header_item
#######################################
un_pcode_csvheader_date() {
    csv_header_item="$1"
    # Only one option used. simple comparison
    if [ "$csv_header_item" = "date" ]; then
        echo "$csv_header_item"
    fi
    echo ""
}

#######################################
# For a typical CSV header, return if is generic "date valid on"
#
# Globals:
#   None
# Arguments:
#   csv_header_item
#######################################
un_pcode_csvheader_date_valid_on() {
    csv_header_item="$1"
    # Only one option used. simple comparison
    if [ "$csv_header_item" = "validOn" ]; then
        echo "$csv_header_item"
    fi
    echo ""
}
#######################################
# For a typical CSV header, return if is generic "date valid to"
#
# Globals:
#   None
# Arguments:
#   csv_header_item
#######################################
un_pcode_csvheader_date_valid_to() {
    csv_header_item="$1"
    # Only one option used. simple comparison
    if [ "$csv_header_item" = "validTo" ]; then
        echo "$csv_header_item"
    fi
    echo ""
}

#######################################
# Only return numeric PCode admin level if the item matches typical raw CSV
# header
#
#
# Globals:
#   None
# Arguments:
#   csv_header_item
#######################################
un_pcode_rawheader_name_language() {
    csv_header_item="$1"

    # echo "admin2AltName2_en" | sed -E 's/^(Admin|admin)([0-9]){1}(Name|RefName|AltName|AltName1|AltName2)_([a-z]{2,3})/1:\1 2:\2 3:\3 4:\4/'
    # 1:admin 2:2 3:AltName2 4:en
    sed_result=$(echo "${csv_header_item}" | sed -E 's/^(Admin|admin)([0-9]){1}(Name|RefName|AltName|AltName1|AltName2)_([a-z]{2,3})/\4/')
    # If sed fail, it returns entire line as it was the input
    if [ "$csv_header_item" != "$sed_result" ]; then
        echo "$sed_result"
        # return 0
    fi
    echo ""
    # return 1
}

#######################################
# Generate an HXL Hashtag based on a raw CSV header item
#
# Globals:
#   None
# Arguments:
#   csv_header_item
#######################################
un_pcode_rawhader_to_hxl() {
    csv_header_item="$1"
    hxlheader=""
    _date=$(un_pcode_csvheader_date "$csv_header_item")
    _date_valid_on=$(un_pcode_csvheader_date_valid_on "$csv_header_item")
    _date_valid_to=$(un_pcode_csvheader_date_valid_to "$csv_header_item")
    _administrative_level=$(un_pcode_csvheader_administrative_level "$csv_header_item")
    _pcode_level=$(un_pcode_csvheader_pcode_level "$csv_header_item")
    _name_language=$(un_pcode_rawheader_name_language "$csv_header_item")
    if [ -n "$_date" ] || [ -n "$_date_valid_on" ] || [ -n "$_date_valid_to" ]; then
        hxlheader="#date"
        if [ -n "$_date_valid_on" ]; then
            # Note: Author not sure if this would be the HXL tag used here
            hxlheader="${hxlheader}+valid_on"
        fi
        if [ -n "$_date_valid_to" ]; then
            # Note: Author not sure if this would be the HXL tag used here
            hxlheader="${hxlheader}+valid_to"
        fi
    fi
    if [ -n "$_pcode_level" ]; then
        hxlheader="#adm${_pcode_level}+code+pcode"
    fi
    if [ -n "$_name_language" ]; then
        hxlheader="#adm${_administrative_level}+name+i_${_name_language}"
    fi
    echo "$hxlheader"
}

#######################################
# Generate an HXL Hashtag based on a raw CSV header item
#
# Globals:
#   None
# Arguments:
#   csv_input
#   csv_hxlated_output
#######################################
un_pcode_csv_to_hxl() {
    csv_input="$1"
    csv_hxlated_output="$1"
    csv_header=$(head -n 1 "${csv_input}")
    echo "TODO"
}

# un_pcode_rawheader_admin_level "admin2Pcode" || echo "admin2Pcode no admin of pcode"
# un_pcode_rawheader_admin_level "admin2Pcode" && echo "admin2Pcode is admin of pcode"
# un_pcode_rawheader_admin_level "admin2AltName2_zh" || echo "admin2AltName2_zh no admin  of pcode"
# un_pcode_rawheader_admin_level "admin2AltName2_zh" && echo "admin2AltName2_zh is admin  of pcode"


# while read -r raw_header_item; do
#     administrative_level=$(un_pcode_csvheader_administrative_level "$raw_header_item")
#     name_language=$(un_pcode_rawheader_name_language "$raw_header_item")
#     _date=$(un_pcode_csvheader_date "$raw_header_item")
#     _date_valid_on=$(un_pcode_csvheader_date_valid_on "$raw_header_item")
#     _date_valid_to=$(un_pcode_csvheader_date_valid_to "$raw_header_item")
#     _hxlhashtag=$(un_pcode_rawhader_to_hxl "$raw_header_item")
#     echo "${raw_header_item},${administrative_level},${name_language},${_date},${_date_valid_on},${_date_valid_to},${_hxlhashtag}"
# done < "999999/1603/45/16/meta-de-caput.uniq.txt"


# echo "admin2AltName2_en" | sed -E 's/^(Admin|admin)([0-9]){1}(AltName|Name)([0-9]){0,1}\_([a-z])$/\2/'

# echo "admin2AltName2_en" | sed -E 's/^(Admin|admin)([0-9]){1}(Name|RefName|AltName|AltName1|AltName2)_([a-z]{2,3})/_\1_ _\2_ _\3_ _\4_/'
# _admin_ _2_ _AltName2_ _en_

