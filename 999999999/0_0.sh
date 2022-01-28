#!/bin/sh
#===============================================================================
#
#          FILE:  0_0.sh
#
#         USAGE:  ./999999999/0_0.sh
#                 time ./999999999/0_0.sh
#                 FORCE_REDOWNLOAD=1 time ./999999999/0_0.sh
#                 FORCE_CHANGED=1 time ./999999999/0_0.sh
#
#   DESCRIPTION:  The happy path to initialy everything from outside sources.
#                 Except the 1613. That data folder is handcrafted.
#
#       OPTIONS:  ---
#
#  REQUIREMENTS:  - Bash shell (or better)
#                 - wget
#                 - Python
#                   - libhxl (https://github.com/HXLStandard/libhxl-python)
#                   - csvkit (https://github.com/wireservice/csvkit)
#          BUGS:  ---
#         NOTES:  ---
#        AUTHOR:  Emerson Rocha <rocha[at]ieee.org>
#       COMPANY:  EticaAI
#       LICENSE:  Public Domain dedication or Zero-Clause BSD
#                 SPDX-License-Identifier: Unlicense OR 0BSD
#       VERSION:  v1.1
#       CREATED:  2022-01-05 23:40 UTC based on scripts from github.com/EticaAI
#                                      /HXL-Data-Science-file-formats
#      REVISION:  2021-01-06 02:21 UTC renamed from 0.sh to 0.0.sh
#                 2021-01-10 05:19 UTC renamed from 0.0.sh to 0_0.sh
#===============================================================================
# Comment next line if not want to stop on first error
set -e

ROOTDIR="$(pwd)"


printf '\n\t\e[1;32m%-6s\e[m\n' "999999999/2600.sh"
bash "${ROOTDIR}/999999999/2600.sh"

printf '\n\t\e[1;32m%-6s\e[m\n' "999999999/1603_17.sh"
bash "${ROOTDIR}/999999999/1603_17.sh"

# TODO: maybe we shoud re-run at the end too?
printf '\n\t\e[1;32m%-6s\e[m\n' "999999999/1603_13.sh"
bash "${ROOTDIR}/999999999/1603_13.sh"

printf '\n\t\e[1;32m%-6s\e[m\n' "999999999/1603_87.sh"
bash "${ROOTDIR}/999999999/1603_87.sh"

printf '\n\t\e[1;32m%-6s\e[m\n' "999999999/1603_47_15924.sh"
bash "${ROOTDIR}/999999999/1603_47_15924.sh"

printf '\n\t\e[1;32m%-6s\e[m\n' "999999999/1603_47_639_3.sh"
bash "${ROOTDIR}/999999999/1603_47_639_3.sh"

printf '\n\t\e[1;32m%-6s\e[m\n' "999999999/1603_45_49.sh"
bash "${ROOTDIR}/999999999/1603_45_49.sh"

printf '\n\t\e[1;32m%-6s\e[m\n' "999999999/1603_3_1603_45_1.sh"
bash "${ROOTDIR}/999999999/1603_3_1603_45_1.sh"

printf '\n\t\e[1;32m%-6s\e[m\n' "9999999999/1603_45_16.sh"
bash "${ROOTDIR}/999999999/1603_45_16.sh"


# sudo apt install fonts-noto fonts-noto-color-emoji
#  Download: 234 MB
#  Disk after: 663 MB


# Deploy (required access to @EticaAIBot account)
#./999999999/0_9.sh

# For a list of POSIX utils _granted_ to be installed everywhere:
# @see https://en.wikipedia.org/wiki/List_of_Unix_commands
