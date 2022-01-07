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

ROOTDIR="$(pwd)"

## Directory that stores basic TSVs to allow bare minimum conversions
# These files are also generated as part of bootstrapping step
# 1603.45.49.tsv, 1603.47.639.3.tsv, 1603.47.15924.tsv,
NUMERORDINATIO_DATUM="${ROOTDIR}/999999/999999"

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
# From a list of comma separated raw headers, return a comma separated
# HXLAted headers. Only for P-Code-like CSV files
#
# Globals:
#   None
# Arguments:
#   csv_input
#   csv_hxlated_output
#######################################
un_pcode_hxlate_csv_header() {
    csv_header_input="$1"
    csv_header_input_lines=$(echo "${csv_header_input}" | tr ',' "\n")
    hxlated_header=""

    # RESULT=""
    for item in $csv_header_input_lines
    do
        hxlated_item=$(un_pcode_rawhader_to_hxl "$item")
        hxlated_header="${hxlated_header:+${hxlated_header},}${hxlated_item}"
    done
    echo "$hxlated_header"

    # echo "$csv_header_input_lines" | while IFS= read -r csv_header_item ; do
    #   administrative_level=$(un_pcode_csvheader_administrative_level "${line}")
    #   name_language=$(un_pcode_rawheader_name_language "$line")
    #   hxlhashtag=$(un_pcode_rawhader_to_hxl "$line")
    #   # echo $line
    #   hxlated_header
    # done
}

#######################################
# Generate an HXL Hashtag based on a raw CSV header item
#
# Example:
#    un_pcode_hxlate_csv_file AFG_1.csv > AFG_1.hxl.csv
#
# Globals:
#   None
# Arguments:
#   csv_input
#   csv_hxlated_output
#######################################
un_pcode_hxlate_csv_file() {
    csv_input="$1"
    # csv_hxlated_output="$1"
    # csv_header=$(head -n 1 "${csv_input}")

    linenumber=0
    while IFS= read -r line; do
        if [ "$linenumber" -eq "0" ]; then
            echo "$line"
            un_pcode_hxlate_csv_header=$(un_pcode_hxlate_csv_header "$line")
            echo "$un_pcode_hxlate_csv_header"
        else
            echo "$line"
        fi
        linenumber=$(( linenumber + 1 ))
    done < "${csv_input}"
}

#######################################
# Return an 1603.45.49 (UN m49 numeric code) from other common systems
#
# Example:
#    un_pcode_hxlate_csv_file AFG_1.csv > AFG_1.hxl.csv
#
# Globals:
#   NUMERORDINATIO_DATUM
# Arguments:
#   scienciam_codicem
#   scienciam_variable_pointer
#######################################
__numerordinatio_scientiam_initiale() {
    scienciam_codicem="$1"
    scienciam_variable_pointer="$2" # Ponter, https://tldp.org/LDP/abs/html/ivr.html
    # _data=$(eval "${scienciam_variable}")
    # _data=${scienciam_variable}

    # https://tldp.org/LDP/abs/html/ivr.html
    # https://stackoverflow.com/a/19634966/894546

    echo "----D49-"
    echo "$D49"
    echo "----D49-"

    eval local_variable_content=\$$scienciam_variable_pointer
    echo "local_variable_content  before   $local_variable_content"
    # echo "-----"

    # eval local_variable_content=\$"$scienciam_variable_pointer"
    if [ -z "${local_variable_content}" ]; then
        local_variable_content=$(cat "${NUMERORDINATIO_DATUM}/${scienciam_codicem}.tsv")

        echo "entrou"
    else
        echo "error"
    fi

    echo "    ----D49-"
    echo "   $D49"
    echo "   ----D49-"
    # return 0
}

__numerordinatio_codicem_lineam() {
    lineam="$1"
    echo "$lineam" | tr '\t' '\n' | while IFS= read -r value; do
        if [ "$value" = "${terminum}" ]; then
            echo "$line" | cut -f1
            return 0
        fi
    done
}

__numerordinatio_translatio() {
    codewordlist="$1"
    codicem_rem="$2"

    linenumber=0
    echo "${codewordlist}" | tr ',' '\n'  | while IFS= read -r line; do
        if [ "${line}" = "${codicem_rem}" ];then
            echo "$linenumber"
            break
        fi
        linenumber=$(( linenumber + 1 ))
        # echo " tentativa $linenumber"
    done
}

#######################################
# Change Numerordĭnātĭo rank separator
#
# Example:
#    # 4
#    numerordinatio_translatio_alpha_in_digito__beta "111" 3
#    # 1111
#    numerordinatio_translatio_alpha_in_digito__beta "aaa" 3
#    # 44136
#    numerordinatio_translatio_alpha_in_digito__beta "ZZZ" 3
#
# Globals:
#   None
# Arguments:
#   terminum
#######################################
numerordinatio_translatio_in_digito__beta() {
    codicem="$1"
    total_characters="$2"
    _TEMPDIR=$(mktemp --directory)
    _FIFO_total="$_TEMPDIR/total"
    mkfifo "${_FIFO_total}"

    # Must be betwen 1 and 9. Around 5 start to be impractical
    _exact_packed_chars_number="$total_characters"

    universum_alpha_usascii="NOP,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP,NOP"
    # universum_alphanum_usascii="0123456789abcdefghijklmnopqrstuvwxyz"

    # @see https://en.wikipedia.org/wiki/ISO_639-3#Code_space

    codicem=$(echo "$codicem" | tr '[:upper:]' '[:lower:]')
    numeric_total=0

    # mkfifo "${TMPDIR}"/_nmt_total
    echo "$numeric_total" > "$_FIFO_total" &

    # https://stackoverflow.com/questions/6834347/named-pipe-closing-prematurely-in-script/

    linenumber=0
    # @see https://stackoverflow.com/a/10572879/894546
    echo "${codicem}" | sed -e 's/\(.\)/\1\n/g'  | while IFS= read -r character; do
        numerum=$(__numerordinatio_translatio "$universum_alpha_usascii" "$character")
        numerum=$((numerum))

        _total=$(cat "$_FIFO_total")
        # numeric_now=$((numerum * pow_now))
        numeric_now=$(echo "$numerum ^ $total_characters" | bc)
        # echo "$numerum ^ $total_characters"

        numeric_total=$(( _total + numeric_now))
        echo "$numeric_total" > "$_FIFO_total" &

        # TO Debug, remove next comment
        # echo "c [$character]: cn [$numerum]:cnv [$numeric_now]: p: [$total_characters] :cnt [$numeric_total]"
        linenumber=$(( linenumber + 1 ))
        total_characters=$(( total_characters - 1 ))

    done

    # TODO: implement a real CRC, to allow check later. 0 means no check
    total_namespace_multiple_of_60="1"
    crc_check="0"

    _total=$(cat "$_FIFO_total")
    echo "${_total}${_exact_packed_chars_number}${total_namespace_multiple_of_60}${crc_check}"
    # echo "${codicem}: total [[[[$_total]]]]]"

    rm "${_FIFO_total:-'unknow-file'}"

    # separator_finale="$2"
    # separator_initiale="${3:-\:}"
    # resultatum=""
    # if [ -z "$numerordinatio_codicem" ] || [ -z "$separator_finale" ]; then
    #     echo "errorem [$*]"
    #     return 1
    # fi
    # resultatum=$(echo "$numerordinatio_codicem" | sed "s|${separator_initiale}|${separator_finale}|g")
    # echo "$resultatum"
}

# echo ">> 111 3"
# numerordinatio_translatio_in_digito__beta "111" 3
# echo ""
# echo ">> aaa 3"
# numerordinatio_translatio_alpha_in_digito__beta "aaa" 3
# echo ""
# echo ">> abc 3"
# numerordinatio_translatio_alpha_in_digito__beta "abc" 3
# echo ""
# echo ">> 123 3"
# numerordinatio_translatio_alpha_in_digito__beta "123" 3
# echo ""
# echo ">> ZZZ 3"
# numerordinatio_translatio_alpha_in_digito__beta "ZZZ" 3
# echo ""
# echo ">> ZZZZ 4"
# numerordinatio_translatio_alpha_in_digito__beta "ZZZZ" 4


#######################################
# Change Numerordĭnātĭo rank separator
#
# Example:
#    # 12/34/56
#    numerordinatio_codicem_transation_separator "12/34/56" "/"
#    # 十二/三十四/五十六
#    numerordinatio_codicem_transation_separator "十二:三十四:五十六" "/"
#    # errorem [ / :]
#    numerordinatio_codicem_transation_separator "" "/" ":"
#
# Globals:
#   None
# Arguments:
#   terminum
#######################################
numerordinatio_codicem_transation_separator() {
    numerordinatio_codicem="$1"
    separator_finale="$2"
    separator_initiale="${3:-\:}"
    resultatum=""
    if [ -z "$numerordinatio_codicem" ] || [ -z "$separator_finale" ]; then
        echo "errorem [$*]"
        return 1
    fi
    resultatum=$(echo "$numerordinatio_codicem" | sed "s|${separator_initiale}|${separator_finale}|g")
    echo "$resultatum"
}

# numerordinatio_codicem_transation_separator "12:34:56" "/"
# numerordinatio_codicem_transation_separator "十二:三十四:五十六" "/"
# numerordinatio_codicem_transation_separator "" "/" ":"

#######################################
# Return an 1603.45.49 (UN m49 numeric code) from other common systems
#
# Example:
#    # > 76
#    numerordinatio_codicem_locali__1603_45_49 "BRA"
#
# Globals:
#   NUMERORDINATIO_DATUM__1603_45_49
# Arguments:
#   terminum
#######################################
numerordinatio_codicem_locali__1603_45_49() {
    terminum="$1"
    codicem_locali=""

    if [ -z "$NUMERORDINATIO_DATUM__1603_45_49" ]; then
        echo "non NUMERORDINATIO_DATUM__1603_45_49 1603.47.639.3.tsv"
        return 1
    fi

    echo "$NUMERORDINATIO_DATUM__1603_45_49" | while IFS= read -r line; do
        codicem_locali=$(__numerordinatio_codicem_lineam "$line")
        if [ -n "$codicem_locali" ]; then
            echo "$codicem_locali"
            return 0
        fi
        # echo "line $line"
    done
    # echo "none for $terminum"
}

#######################################
# Return an 1603.45.49 (UN m49 numeric code) from other common systems
# TODO:
#    Create numeric codes
#
# Example:
#    # > 76
#    numerordinatio_codicem_locali__1603_47_639_3 "pt"
#
# Globals:
#   NUMERORDINATIO_DATUM__1603_47_639_3
# Arguments:
#   terminum
#######################################
numerordinatio_codicem_locali__1603_47_639_3() {
    terminum="$1"
    codicem_locali=""

    if [ -z "$NUMERORDINATIO_DATUM__1603_47_639_3" ]; then
        echo "non NUMERORDINATIO_DATUM__1603_47_15924 1603.45.49.tsv"
        return 1
    fi

    echo "$NUMERORDINATIO_DATUM__1603_47_639_3" | while IFS= read -r line; do
        codicem_locali=$(__numerordinatio_codicem_lineam "$line")
        if [ -n "$codicem_locali" ]; then
            echo "$codicem_locali"
            return 0
        fi
        # echo "line $line"
    done
    # echo "none for $terminum"
}

#######################################
# Return an 1603.45.49 (UN m49 numeric code) from other common systems
# TODO:
#    Create numeric codes
#
# Example:
#    # > 215
#    numerordinatio_codicem_locali__1603_47_15924 "Latn"
#
# Globals:
#   NUMERORDINATIO_DATUM__1603_47_639_3
# Arguments:
#   terminum
#######################################
numerordinatio_codicem_locali__1603_47_15924() {
    terminum="$1"
    codicem_locali=""

    if [ -z "$NUMERORDINATIO_DATUM__1603_47_15924" ]; then
        echo "non NUMERORDINATIO_DATUM__1603_47_15924 1603.47.15924.tsv"
        return 1
    fi

    echo "$NUMERORDINATIO_DATUM__1603_47_15924" | while IFS= read -r line; do
        codicem_locali=$(__numerordinatio_codicem_lineam "$line")
        if [ -n "$codicem_locali" ]; then
            echo "$codicem_locali"
            return 0
        fi
        # echo "line $line"
    done
    # echo "none for $terminum"
}

# https://superuser.com/questions/279141/why-is-reading-a-file-faster-than-reading-a-variable
NUMERORDINATIO_DATUM__1603_45_49=$(cat "${NUMERORDINATIO_DATUM}/1603.45.49.tsv")
NUMERORDINATIO_DATUM__1603_47_639_3=$(cat "${NUMERORDINATIO_DATUM}/1603.47.639.3.tsv")
NUMERORDINATIO_DATUM__1603_47_15924=$(cat "${NUMERORDINATIO_DATUM}/1603.47.15924.tsv")

# echo ""
# # numerordinatio_codicem_locali__1603_45_49 "br"
# numerordinatio_codicem_locali__1603_45_49 "BRA"
# numerordinatio_codicem_locali__1603_45_49 "SWZ"
# numerordinatio_codicem_locali__1603_45_49 "SWZ"
# numerordinatio_codicem_locali__1603_45_49 "SWZ"
# numerordinatio_codicem_locali__1603_45_49 "SAU"

# echo ""
# numerordinatio_codicem_locali__1603_47_639_3 "pt"
# numerordinatio_codicem_locali__1603_47_639_3 "es"
# numerordinatio_codicem_locali__1603_47_639_3 "en"

# echo ""
# numerordinatio_codicem_locali__1603_47_15924 "Latn"
# numerordinatio_codicem_locali__1603_47_15924 "Arab"
# numerordinatio_codicem_locali__1603_47_15924 "cyrl"
