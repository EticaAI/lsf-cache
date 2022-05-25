#!/bin/bash
#===============================================================================
#
#          FILE:  1603_3_12_16_5305.sh
#
#         USAGE:  ./999999999/1603_3_12_16_5305.sh
#                 time ./999999999/1603_3_12_16_5305.sh
#   DESCRIPTION:  Drills related to manage a spark SPARQL endpoint
#                 https://www.wikidata.org/wiki/Property:P5305
#
#       OPTIONS:  ---
#
#  REQUIREMENTS:  - hxltmcli
#          BUGS:  ---
#         NOTES:  ---
#        AUTHOR:  Emerson Rocha <rocha[at]ieee.org>
#       COMPANY:  EticaAI
#       LICENSE:  Public Domain dedication
#                 SPDX-License-Identifier: Unlicense
#       VERSION:  v1.0
#       CREATED:  2022-05-14 15:45 UTC started. based on 999999_1679.sh
#      REVISION:  ---
#===============================================================================
set -e

# time HTTPS_PROXY="socks5://127.0.0.1:9050" ./999999999/1603_3_12_16_5305.sh

ROOTDIR="$(pwd)"

# shellcheck source=999999999.lib.sh
. "$ROOTDIR"/999999999/999999999.lib.sh

# Recommended use the lastest from https://jena.apache.org/download/
SPARQL_ENDPOINT_JENA_VERSION="4.5.0"

# @see https://jena.apache.org/documentation/tools/index.html
JENA_HOME="${ROOTDIR}/999999999/0/1686799/apache-jena"
export FUSEKI_BASE="${ROOTDIR}/999999999/0/1686799/apache-jena-workspace"
export PATH=$PATH:$JENA_HOME/bin

#### Hello world examples ______________________________________________________
## Tutorials from
## - https://jena.apache.org/tutorials/
##   - https://jena.apache.org/tutorials/rdf_api_pt.html
##   - https://jena.apache.org/tutorials/rdf_api_pt.html
##   - https://jena.apache.org/tutorials/sparql_pt.html
##   - https://jena.apache.org/documentation/query/manipulating_sparql_using_arq_pt.html

## https://jena.apache.org/tutorials/sparql_query1_pt.html
# curl https://jena.apache.org/tutorials/sparql_data/q1.rq --output 999999/0/q1.rq
# curl https://jena.apache.org/tutorials/sparql_data/vc-db-1.rdf --output 999999/0/vc-db-1.rdf
# sparql --data=999999/0/vc-db-1.rdf --query=999999/0/q1.rq

# curl https://jena.apache.org/tutorials/sparql_data/q-bp4.rq --output 999999/0/q-bp4.rq
# sparql --data=999999/0/vc-db-1.rdf --query=999999/0/q-bp4.rq

# curl https://jena.apache.org/tutorials/sparql_data/q-f1.rq --output 999999/0/q-f1.rq
# sparql --data=999999/0/vc-db-1.rdf --query=999999/0/q-f1.rq

## See https://stackoverflow.com/questions/35471892/sparql-query-for-skosrelated-field
# echo "prefix skos: <http://www.w3.org/2004/02/skos/core#>

# SELECT ?narrower
# WHERE {
#     ?s skos:narrower ?narrower
# }" > 999999/0/test-skos.rq
# sparql --data=1603/63/101/1603_63_101.no11.skos.ttl --query=999999/0/test-skos.rq
# #### ... _______________________________________________________________________

# @TODO eventualmente talvez anotar as propriedades de campos que tem aqui
#       Cadastro Nacional de Endereços para Fins Estatísticos
#       https://ftp.ibge.gov.br/Censos/Censo_Demografico_2010/Cadastro_Nacional_de_Enderecos_Fins_Estatisticos/

# @TODO https://geoftp.ibge.gov.br/

# @TODO https://geoftp.ibge.gov.br/organizacao_do_territorio/estrutura_territorial/divisao_territorial/2021/
# @TODO https://geoftp.ibge.gov.br/cartas_e_mapas/bases_cartograficas_continuas/bc250/versao2021/geopackage/

# https://github.com/conjecto/docker-blazegraph
# docker run --name some-blazegraph -d conjecto/blazegraph:2.1.6
# https://github.com/lyrasis/docker-blazegraph

# docker run --name blazegraph -d -p 8889:8080 lyrasis/blazegraph:2.1.5
# docker logs -f blazegraph
# http://localhost:8889/bigdata/

# https://wiki.uib.no/info216/index.php/Lab:_SPARQL_Programming

# See https://github.com/blazegraph/database/wiki/Quick_Start
# wget https://raw.githubusercontent.com/blazegraph/blazegraph-samples/53f615248f33f767d2b259472d84f19452d39aa5/sample-sesame-embedded/src/main/resources/data.n3 -o /tmp/data.n3
# xdg-open http://localhost:8889/bigdata/
# Run
#    load <file:///tmp/data.n3>

# https://github.com/apache/jena/blob/main/jena-fuseki2/jena-fuseki-docker/README.md
# https://www.youtube.com/watch?v=5-UfFV5XmTI
# https://jena.apache.org/documentation/io/
# https://github.com/stain/jena-docker
# https://ontola.io/blog/rdf-serialization-formats/

#######################################
# Download Apache JENA to 999999999/0/1686799/
#
# Globals:
#   ROOTDIR
#   SPARQL_ENDPOINT_JENA_VERSION
# Arguments:
#   numerordinatio
# Outputs:
#   Convert files
#######################################
p5305_sparql_endpoint_jena_install() {
  # numerordinatio="$1"
  iri="https://dlcdn.apache.org/jena/binaries/apache-jena-${SPARQL_ENDPOINT_JENA_VERSION}.tar.gz"

  fontem_archivum_temporarium="${ROOTDIR}/999999/0/apache-jena.tar.gz"
  targz_subdir="apache-jena-${SPARQL_ENDPOINT_JENA_VERSION}"
  objectivum_archivum="${ROOTDIR}/999999999/0/1686799/apache-jena"

  echo "${FUNCNAME[0]} ... [$SPARQL_ENDPOINT_JENA_VERSION] [$iri]"

  if [ ! -f "${fontem_archivum_temporarium}" ]; then
    set -x
    curl --compressed --silent --show-error \
      -get "$iri" \
      --output "$fontem_archivum_temporarium"
    set +x
  else
    echo "Already cached at [${fontem_archivum_temporarium}]"
  fi

  set -x
  tar -C "${objectivum_archivum}" \
    -zxf "${fontem_archivum_temporarium}" \
    "${targz_subdir}" \
    --strip-components=1
  set +x
  # @TODO: remove cached downloaded file
}

#######################################
# Download Apache JENA to /opt/apache-jena (requires folder already created)
# Example
#     sudo mkdir /opt/apache-jena
#     sudo chown $USER:$USER /opt/apache-jena
#
# Globals:
#   ROOTDIR
#   SPARQL_ENDPOINT_JENA_VERSION
# Arguments:
#   numerordinatio
# Outputs:
#   Convert files
#######################################
p5305_sparql_endpoint_jena_install_system_opt() {
  # numerordinatio="$1"
  iri="https://dlcdn.apache.org/jena/binaries/apache-jena-${SPARQL_ENDPOINT_JENA_VERSION}.tar.gz"

  fontem_archivum_temporarium="${ROOTDIR}/999999/0/apache-jena.tar.gz"
  targz_subdir="apache-jena-${SPARQL_ENDPOINT_JENA_VERSION}"
  # objectivum_archivum="${ROOTDIR}/999999999/0/1686799/apache-jena"
  objectivum_archivum="/opt/apache-jena"

  echo "${FUNCNAME[0]} ... [$SPARQL_ENDPOINT_JENA_VERSION] [$iri]"

  if [ ! -f "${fontem_archivum_temporarium}" ]; then
    set -x
    curl --compressed --silent --show-error \
      -get "$iri" \
      --output "$fontem_archivum_temporarium"
    set +x
  else
    echo "Already cached at [${fontem_archivum_temporarium}]"
  fi

  set -x
  tar -C "${objectivum_archivum}" \
    -zxf "${fontem_archivum_temporarium}" \
    "${targz_subdir}" \
    --strip-components=1
  set +x

  echo "--- IF REQUIRED TO ADD TO PATH ---"
  # Do it only if sparql --version already not enabled
  # vim ~/.bash_profile
  echo ""
  echo "    vim ~/.bash_profile"
  echo "    #    JENA_HOME=/opt/apache-jena"
  echo "    #    PATH=/opt/apache-jena/bin:\$PATH"
  echo "    source ~/.bash_profile"
  echo "    # test:"
  echo "    sparql --version"
  echo ""
  echo "--- REQUIRES ADD TO YOUR PATH ---"

  # @TODO: remove cached downloaded file
}


#######################################
# Download Apache JENA fuseki to 999999999/0/1686799/
#
# Globals:
#   ROOTDIR
#   SPARQL_ENDPOINT_JENA_VERSION
# Arguments:
#   numerordinatio
# Outputs:
#   Convert files
#######################################
p5305_sparql_endpoint_jena_fuseki_install() {
  # numerordinatio="$1"
  # https://dlcdn.apache.org/jena/binaries/apache-jena-fuseki-4.5.0.tar.gz
  iri="https://dlcdn.apache.org/jena/binaries/apache-jena-fuseki-${SPARQL_ENDPOINT_JENA_VERSION}.tar.gz"
  echo "${FUNCNAME[0]} ... [$SPARQL_ENDPOINT_JENA_VERSION] [$iri]"

  fontem_archivum_temporarium="${ROOTDIR}/999999/0/apache-jena-fuseki.tar.gz"
  targz_subdir="apache-jena-fuseki-${SPARQL_ENDPOINT_JENA_VERSION}"
  objectivum_archivum="${ROOTDIR}/999999999/0/1686799/apache-jena-fuseki"

  if [ ! -f "${fontem_archivum_temporarium}" ]; then
    set -x
    curl --compressed --silent --show-error \
      -get "$iri" \
      --output "$fontem_archivum_temporarium"
    set +x
  else
    echo "Already cached at [${fontem_archivum_temporarium}]"
  fi

  set -x
  tar -C "${objectivum_archivum}" \
    -zxf "${fontem_archivum_temporarium}" \
    "${targz_subdir}" \
    --strip-components=1
  set +x
  # @TODO: remove cached downloaded file
}


#######################################

# Download Apache JENA Fuseki to /opt/apache-jena. Requires folder already
# created like:
#     sudo mkdir /opt/apache-jena-fuseki
#     sudo chown $USER:$USER /opt/apache-jena-fuseki
#
# Globals:
#   ROOTDIR
#   SPARQL_ENDPOINT_JENA_VERSION
# Arguments:
#   numerordinatio
# Outputs:
#   Convert files
#######################################
p5305_sparql_endpoint_jena_fuseki_install_system_opt() {
  # numerordinatio="$1"
  # https://dlcdn.apache.org/jena/binaries/apache-jena-fuseki-4.5.0.tar.gz
  iri="https://dlcdn.apache.org/jena/binaries/apache-jena-fuseki-${SPARQL_ENDPOINT_JENA_VERSION}.tar.gz"
  echo "${FUNCNAME[0]} ... [$SPARQL_ENDPOINT_JENA_VERSION] [$iri]"

  fontem_archivum_temporarium="${ROOTDIR}/999999/0/apache-jena-fuseki.tar.gz"
  targz_subdir="apache-jena-fuseki-${SPARQL_ENDPOINT_JENA_VERSION}"
  # objectivum_archivum="${ROOTDIR}/999999999/0/1686799/apache-jena-fuseki"
  objectivum_archivum="/opt/apache-jena-fuseki"
  objectivum_workdir="${ROOTDIR}/999999999/0/1686799/apache-jena-workspace"

  if [ ! -f "${fontem_archivum_temporarium}" ]; then
    set -x
    curl --compressed --silent --show-error \
      -get "$iri" \
      --output "$fontem_archivum_temporarium"
    set +x
  else
    echo "Already cached at [${fontem_archivum_temporarium}]"
  fi

  set -x
  tar -C "${objectivum_archivum}" \
    -zxf "${fontem_archivum_temporarium}" \
    "${targz_subdir}" \
    --strip-components=1
  set +x
  # @TODO: remove cached downloaded file

  # echo "--- IF REQUIRED TO ADD TO PATH ---"
  # echo ""
  # echo "   # Do it only if sparql --version already not enabled"
  # echo "    vim ~/.bash_profile"
  # echo "    #    JENA_HOME=/opt/apache-jena"
  # echo "    #    PATH=/opt/apache-jena-fuseki/bin:\$PATH"
  # echo "    source ~/.bash_profile"
  # echo "    # test:"
  # echo "    sparql --version"
  # echo ""
  # echo "--- REQUIRES ADD TO YOUR PATH ---"
  echo "--- SEE ALSO ---"
  echo ""
  echo "    cd $objectivum_workdir"
  echo "    /opt/apache-jena-fuseki/fuseki-server"
  echo "    # web interface at http://localhost:3030/#/"
  echo ""
  echo "--- SEE ALSO ---"
}

#######################################
# Run Jena Fuseki (if downloaded to folder)
#
# Globals:
#   ROOTDIR
#   SPARQL_ENDPOINT_JENA_VERSION
# Arguments:
#   numerordinatio
# Outputs:
#   Convert files
#######################################
p5305_sparql_endpoint_jena_fuseki_start() {

  fontem_archivum="${ROOTDIR}/999999999/0/1686799/apache-jena-fuseki"
  objectivum_archivum_basi="${ROOTDIR}/999999999/0/1686799/apache-jena-fuseki"
  objectivum_archivum_bin="${objectivum_archivum_basi}/fuseki-server"
  objectivum_archivum="${ROOTDIR}/999999999/0/1686799/apache-jena-fuseki"
  objectivum_archivum_web="http://localhost:3030/#/"

  echo "${FUNCNAME[0]} ... [$SPARQL_ENDPOINT_JENA_VERSION] [$objectivum_archivum_web]"

  # cd "$objectivum_archivum_workspace"
  # Starts at http://localhost:3030/#/
  # @TODO: change home directory
  "${objectivum_archivum_bin}"

  sparql --version

  # @TODO: remove cached downloaded file
}

#######################################
# Run Jena Fuseki (if installed at /opt/apache-jena-fuseki/fuseki-server)
#
# Globals:
#   ROOTDIR
#   SPARQL_ENDPOINT_JENA_VERSION
# Arguments:
#   numerordinatio
# Outputs:
#   Convert files
#######################################
p5305_sparql_endpoint_jena_fuseki_start_system() {

  # fontem_archivum="${ROOTDIR}/999999999/0/1686799/apache-jena-fuseki"
  # objectivum_archivum_workspace="${ROOTDIR}/999999999/0/1686799/apache-jena-workspace"
  #targz_subdir="apache-jena-fuseki-${SPARQL_ENDPOINT_JENA_VERSION}"
  # objectivum_archivum_basi="${ROOTDIR}/999999999/0/1686799/apache-jena-fuseki"
  objectivum_archivum_bin="/opt/apache-jena-fuseki/fuseki-server"
  # officinam/999999999/0/1686799/apache-jena-fuseki/fuseki-server
  objectivum_archivum="${ROOTDIR}/999999999/0/1686799/apache-jena-fuseki"
  objectivum_archivum_web="http://localhost:3030/#/"

  echo "${FUNCNAME[0]} ... [$SPARQL_ENDPOINT_JENA_VERSION] [$objectivum_archivum_bin] [$objectivum_archivum_web]"

  # cd "$objectivum_archivum_workspace"
  # Starts at http://localhost:3030/#/
  # @TODO: change home directory
  "${objectivum_archivum_bin}"

  sparql --version

  # @TODO: remove cached downloaded file
}

#### Java dependencies _________________________________________________________
# - https://jena.apache.org/download/index.cgi
#   - "Jena4 requires Java 11."
# - https://www.digitalocean.com/community/tutorials/how-to-install-java-with-apt-on-ubuntu-20-04-pt
#
#     sudo apt install default-jre

#### Apache Jena, install ______________________________________________________
# Uncomment these. (local dir)
# p5305_sparql_endpoint_jena_install
# p5305_sparql_endpoint_jena_fuseki_install

# p5305_sparql_endpoint_jena_install_system_opt
# p5305_sparql_endpoint_jena_fuseki_install_system_opt

#### Apache Jena, run ______________________________________________________
## p5305_sparql_endpoint_jena_fuseki_start
p5305_sparql_endpoint_jena_fuseki_start_system

# touch 999999/0/hello-world-sparql-database.rdf
# /opt/apache-jena/src-examples/data/eswc-2006-09-21.rdf


#### Other commends (move or remove later) _____________________________________
# https://www.wikidata.org/wiki/Wikidata:Identifier_migration
# https://www.wikidata.org/wiki/Help:Authority_control

# p5305_sparql_endpoint_jena_fuseki_start

# ln -s /workspace/git/EticaAI/lexicographi-sine-finibus/officinam/999999999/0/1686799/apache-jena/bin /workspace/bin/apache-jena
# vim ~/.bash_profile:
#     PATH="/workspace/bin/apache-jena:$PATH"
# @TODO https://www.digitalocean.com/community/tutorials/how-to-install-java-with-apt-on-ubuntu-20-04-pt
