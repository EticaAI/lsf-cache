#!/bin/bash
#===============================================================================
#
#          FILE:  0_9.sh
#
#         USAGE:  ./999999999/0_9.sh
#                 time ./999999999/0_9.sh
#
#   DESCRIPTION:  Internal script to commit to https://github.com/EticaAI/n-data
#
#       OPTIONS:  ---
#
#  REQUIREMENTS:  - Bash shell (or better)
#                 - wget
#          BUGS:  ---
#         NOTES:  ---
#        AUTHOR:  Emerson Rocha <rocha[at]ieee.org>
#       COMPANY:  EticaAI
#       LICENSE:  Public Domain dedication or Zero-Clause BSD
#                 SPDX-License-Identifier: Unlicense OR 0BSD
#       VERSION:  v1.0
#       CREATED:  2022-01-10 00:42 UTC
#      REVISION:  ---
#===============================================================================
# Comment next line if not want to stop on first error
set -e

# set -x

_DEPLOY_0_9_COMMIT_MESSAGE="$(TZ=":Zulu" date +"%Y-%m-%d %T") 🤖🧮💾"
DEPLOY_0_9_COMMIT_MESSAGE="${DEPLOY_0_9_COMMIT_MESSAGE:-${_DEPLOY_0_9_COMMIT_MESSAGE}}"

cd /workspace/git/EticaAI/n-data-pseudobase

# read  -r -n 1 -p "Input Selection:" mainmenuinput

deploy_0_9_status() {
  git \
    --git-dir /workspace/git/EticaAI/n-data.git-metadata \
    --work-tree /workspace/git/EticaAI/multilingual-lexicography-automation/officinam \
    status

  echo ""
  echo "  manual inspection:"
  echo "  git --git-dir /workspace/git/EticaAI/n-data.git-metadata --work-tree /workspace/git/EticaAI/multilingual-lexicography-automation/officinam gui"
  echo ""
}

deploy_0_9_commit() {
  git \
    --git-dir /workspace/git/EticaAI/n-data.git-metadata \
    --work-tree /workspace/git/EticaAI/multilingual-lexicography-automation/officinam \
    add .
  git \
    --git-dir /workspace/git/EticaAI/n-data.git-metadata \
    --work-tree /workspace/git/EticaAI/multilingual-lexicography-automation/officinam \
    commit -m "$DEPLOY_0_9_COMMIT_MESSAGE"
  git \
    --git-dir /workspace/git/EticaAI/n-data.git-metadata \
    --work-tree /workspace/git/EticaAI/multilingual-lexicography-automation/officinam \
    push
  return 0
}

deploy_0_9_exit() {
  echo "deploy_0_9_exit"
  echo "Ok. Stoping by now."
  return 0
}

deploy_0_9_status

while true; do
  read -r -p "Good to git commit this? [$DEPLOY_0_9_COMMIT_MESSAGE]" yn
  case $yn in
  [Yy]*) deploy_0_9_commit ;;
  [Nn]*) deploy_0_9_exit ;;
  *) echo "Yes y [or] No n" ;;
  esac
done

# git \
#     --git-dir /workspace/git/EticaAI/n-data.git-metadata \
#     --work-tree /workspace/git/EticaAI/multilingual-lexicography-automation/officinam \
#     add .

# cd /workspace/git/EticaAI/n-data-pseudobase
# git --git-dir /workspace/git/EticaAI/n-data.git-metadata --work-tree /workspace/git/EticaAI/multilingual-lexicography-automation/officinam gui
