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
#          BUGS:  ---
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

ROOTDIR="$(pwd)"

# Source:
# - https://vocabulary.unocha.org/
#   - https://docs.google.com/spreadsheets/d/1NjSI2LaS3SqbgYc0HdD8oIb7lofGtiHgoKKATCpwVdY/edit#gid=1088874596
#     - https://proxy.hxlstandard.org/data/edit?dest=data_edit&filter01=cut&cut-skip-untagged01=on&filter02=sort&sort-tags02=%23country%2Bcode%2Bnum%2Bv_m49&strip-headers=on&url=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fd%2F1NjSI2LaS3SqbgYc0HdD8oIb7lofGtiHgoKKATCpwVdY%2Fedit%23gid%3D1088874596


DATA_UN_M49_CSV="https://proxy.hxlstandard.org/data.csv?dest=data_edit&filter01=cut&cut-skip-untagged01=on&filter02=sort&sort-tags02=%23country%2Bcode%2Bnum%2Bv_m49&strip-headers=on&url=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fd%2F1NjSI2LaS3SqbgYc0HdD8oIb7lofGtiHgoKKATCpwVdY%2Fedit%23gid%3D1088874596"

wget -qO- "$DATA_UN_M49_CSV" > "${ROOTDIR}/99999999/1603/45/1603.45.49.hxl.csv"
