#!/bin/bash
#===============================================================================
#
#          FILE:  999999_2020_4_1.sh
#
#         USAGE:  ./999999999/999999_2020_4_1.sh
#                 time ./999999999/999999_2020_4_1.sh
#
#   DESCRIPTION:  ---
#
#       OPTIONS:  ---
#
#  REQUIREMENTS:  - Bash shell (or better)
#          BUGS:  ---
#         NOTES:  ---
#        AUTHOR:  Emerson Rocha <rocha[at]ieee.org>
#       COMPANY:  EticaAI
#       LICENSE:  Public Domain dedication or Zero-Clause BSD
#                 SPDX-License-Identifier: Unlicense OR 0BSD
#       VERSION:  v1.0
#       CREATED:  2022-01-15 16:16 UTC
#      REVISION:  ---
#===============================================================================
# Comment next line if not want to stop on first error
set -e
# set -x

ROOTDIR="$(pwd)"

WORKDIR="${ROOTDIR}/999999/999999/2020/4/1/"

if [ -f "${WORKDIR}/1603_1_1.no1.tm.hxl.csv" ]; then
  rm "${WORKDIR}/1603_1_1.no1.tm.hxl.csv"
fi
if [ -f "${WORKDIR}/1603_1_2.tm.hxl.csv" ]; then
  rm "${WORKDIR}/1603_1_2.tm.hxl.csv"
fi
if [ -f "${WORKDIR}/1603_1_51.tm.hxl.csv" ]; then
  rm "${WORKDIR}/1603_1_51.tm.hxl.csv"
fi
if [ -f "${WORKDIR}/1603_3.no1.tm.hxl.csv" ]; then
  rm "${WORKDIR}/1603_3.no1.tm.hxl.csv"
fi
# if [ -f "${WORKDIR}/1603_1_101.no1.tm.hxl.csv" ]; then
#   rm "${WORKDIR}/1603_1_101.no1.tm.hxl.csv"
# fi
if [ -f "${WORKDIR}/1603_3_12_6.no1.tm.hxl.csv" ]; then
  rm "${WORKDIR}/1603_3_12_6.no1.tm.hxl.csv"
fi
if [ -f "${WORKDIR}/1603_84_1.no1.tm.hxl.csv" ]; then
  rm "${WORKDIR}/1603_84_1.no1.tm.hxl.csv"
fi
if [ -f "${WORKDIR}/1603_44_1.no1.tm.hxl.csv" ]; then
  rm "${WORKDIR}/1603_44_1.no1.tm.hxl.csv"
fi
if [ -f "${WORKDIR}/1603_44_142.no1.tm.hxl.csv" ]; then
  rm "${WORKDIR}/1603_44_142.no1.tm.hxl.csv"
fi
if [ -f "${WORKDIR}/1603_45_1.no1.tm.hxl.csv" ]; then
  rm "${WORKDIR}/1603_45_1.no1.tm.hxl.csv"
fi

cp "${ROOTDIR}/1603/1/1/1603_1_1.no1.tm.hxl.csv" "${WORKDIR}/1603_1_1.no1.tm.hxl.csv"
cp "${ROOTDIR}/1603/1/2/1603_1_2.tm.hxl.csv" "${WORKDIR}/1603_1_2.tm.hxl.csv"
cp "${ROOTDIR}/1603/1/51/1603_1_51.no1.tm.hxl.csv" "${WORKDIR}/1603_1_51.tm.hxl.csv"
# cp "${ROOTDIR}/1603/1/101/1603_1_101.no1.tm.hxl.csv" "${WORKDIR}/1603_1_101.no1.tm.hxl.csv"

cp "${ROOTDIR}/1603/3/12/6/1603_3_12_6.no1.tm.hxl.csv" "${WORKDIR}/1603_3_12_6.no1.tm.hxl.csv"
cp "${ROOTDIR}/1603/44/1/1603_44_1.no1.tm.hxl.csv" "${WORKDIR}/1603_44_1.no1.tm.hxl.csv"
cp "${ROOTDIR}/1603/44/142/1603_44_142.no1.tm.hxl.csv" "${WORKDIR}/1603_44_142.no1.tm.hxl.csv"

cp "${ROOTDIR}/1603/45/1/1603_45_1.no1.tm.hxl.csv" "${WORKDIR}/1603_45_1.no1.tm.hxl.csv"

cp "${ROOTDIR}/1603/84/1/1603_84_1.no1.tm.hxl.csv" "${WORKDIR}/1603_84_1.no1.tm.hxl.csv"
