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
#  REQUIREMENTS:  ---
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
