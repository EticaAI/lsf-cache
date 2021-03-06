#!/usr/bin/env python3
# ==============================================================================
#
#          FILE:  999999999_54872.py
#
#         USAGE:  ./999999999/0/999999999_54872.py
#                 ./999999999/0/999999999_54872.py --help
#
#   DESCRIPTION:  RUN /999999999/0/999999999_54872.py --help
#                 - Q54872, https://www.wikidata.org/wiki/Q54872
#                   - Resource Description Framework
#
#       OPTIONS:  ---
#
#  REQUIREMENTS:  - python3
#          BUGS:  ---
#         NOTES:  ---
#       AUTHORS:  Emerson Rocha <rocha[at]ieee.org>
# COLLABORATORS:  ---
#       COMPANY:  EticaAI
#       LICENSE:  Public Domain dedication or Zero-Clause BSD
#                 SPDX-License-Identifier: Unlicense OR 0BSD
#       VERSION:  v1.0.0
#       CREATED:  2022-05-17 18:48 UTC based on 999999999_10263485.py
#      REVISION:  ---
# ==============================================================================
# /opt/Protege-5.5.0/run.sh

import csv
import json
import sys
import os
import argparse
# import csv
# import re
from pathlib import Path
from os.path import exists

# import json
from typing import Type
import yaml
# import urllib.request
# import requests

# l999999999_0 = __import__('999999999_0')
from L999999999_0 import (
    BCP47_AD_HXL,
    RDF_SPATIA_NOMINALIBUS_EXTRAS,
    HXLHashtagSimplici,
    OntologiaVocabularioHXL,
    SetEncoder,
    bcp47_langtag,
    # bcp47_langtag_callback_hxl,
    bcp47_rdf_extension_poc,
    hxl_hashtag_to_bcp47,
    hxltm_carricato,
    HXLTMAdRDFSimplicis,
    hxltm_carricato_brevibus,
    rdf_namespaces_extras
)

STDIN = sys.stdin.buffer

NOMEN = '999999999_54872'

DESCRIPTION = """
{0} Conversor de HXLTM para formatos RDF (alternativa ao uso de 1603_1_1.py, \
que envolve processamento muito mais intenso para datasets enormes)

AVISO: versão atual ainda envolve carregar todos os dados para memória. \
       Considere fornecer tabela HXLTM de entrada que já não contenha \
       informações que pretende que estejam no arquivo gerado.

@see https://github.com/EticaAI/lexicographi-sine-finibus/issues/42

Trivia:
- Q54872, https://www.wikidata.org/wiki/Q54872
  - Resource Description Framework
  - "formal language for describing data models (...)"
""".format(__file__)

__EPILOGUM__ = """
------------------------------------------------------------------------------
                            EXEMPLŌRUM GRATIĀ
------------------------------------------------------------------------------

Generic Numerordinatio to RDF Turtle . . . . . . . . . . . . . . . . . . . . .
(TODO: fix example)
    {0} --methodus=_temp_no1 \
--rdf-sine-spatia-nominalibus=devnull \
--rdf-trivio=5000 \
999999/1603/3/45/16/1/1/1603_3_45_16_1_1.no11.tm.hxl.csv

Configuration-based HXLTM to Numerordinatio . . . . . . . . . . . . . . . . . .
(Experimental; uses YAML to upgrade HXLTM to Numerordinatio tabular)

    cat 999999/0/ibge_un_adm2.tm.hxl.csv | \
{0} --methodus=ad_rdf_ex_configurationi --objectivum-formato=text/csv \
--archivum-configurationi-ex-fonti=999999999/0/999999999_268072.meta.yml \
--praefixum-configurationi-ex-fonti=methodus,ibge_un_adm2 \
> 999999/0/ibge_un_adm2.no1.tm.hxl.csv

    cat 999999/0/ibge_un_adm2.tm.hxl.csv | \
{0} --methodus=ad_rdf_ex_configurationi \
--objectivum-formato=application/x-turtle \
--archivum-configurationi-ex-fonti=999999999/0/999999999_268072.meta.yml \
--praefixum-configurationi-ex-fonti=methodus,ibge_un_adm2 \
> 999999/0/ibge_un_adm2.no1.skos.ttl

    cat 999999/0/ibge_un_adm2.tm.hxl.csv | \
{0} --methodus=ad_rdf_ex_configurationi \
--objectivum-formato=application/x-turtle \
--archivum-configurationi-ex-fonti=999999999/0/999999999_268072.meta.yml \
--praefixum-configurationi-ex-fonti=methodus,ibge_un_adm2 \
| rapper --quiet --input=turtle --output=ntriples /dev/fd/0

    rapper --quiet --input=turtle --output=ntriples \
999999/0/ibge_un_adm2.no1.skos.ttl > 999999/0/ibge_un_adm2.no1.skos.nt

Temporary tests . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
(Debug information in JSON)
    {0} --methodus=_temp_bcp47_meta_in_json \
--punctum-separato-de-fontem=$'\\t' \
999999999/1568346/data/cod-ab-example1-with-inferences.bcp47.tsv \
--numerordinatio-cum-antecessoribus \
--rdf-ontologia-ordinibus=5 --rdf-trivio=5002

    {0} --methodus=_temp_bcp47_meta_in_json \
--punctum-separato-de-fontem=$'\\t' \
--rdf-namespaces-archivo=\
999999999/1568346/data/hxlstandard-rdf-namespaces-example.hxl.csv \
999999999/1568346/data/unesco-thesaurus.bcp47g.tsv

    {0} --methodus=_temp_hxl_meta_in_json \
--punctum-separato-de-fontem=$'\\t' \
999999999/1568346/data/cod-ab-example1-with-inferences.no1.tm.hxl.tsv \
--numerordinatio-cum-antecessoribus \
--rdf-ontologia-ordinibus=5 --rdf-trivio=5002

(Data operations)
    {0} --methodus=_temp_bcp47 \
--punctum-separato-de-fontem=$'\\t' \
999999999/1568346/data/cod-ab-example1-with-inferences.bcp47.tsv \
--numerordinatio-cum-antecessoribus --rdf-ontologia-ordinibus=5 \
--rdf-trivio=5002

    {0} --methodus=_temp_bcp47 \
--punctum-separato-de-fontem=$'\\t' \
--rdf-namespaces-archivo=\
999999999/1568346/data/hxlstandard-rdf-namespaces-example.hxl.csv \
999999999/1568346/data/unesco-thesaurus.bcp47g.tsv \
--numerordinatio-cum-antecessoribus --rdf-trivio=1

    {0} --methodus=_temp_bcp47 --rdf-namespaces-archivo=\
999999999/1568346/data/hxlstandard-rdf-namespaces-example.hxl.csv \
999999999/1568346/data/unesco-thesaurus.bcp47g.tsv \
--numerordinatio-cum-antecessoribus --rdf-trivio=5001

    {0} --methodus=_temp_bcp47 \
--punctum-separato-de-fontem=$'\\t' \
--rdf-namespaces-archivo=\
999999999/1568346/data/hxlstandard-rdf-namespaces-example.hxl.csv \
999999999/1568346/data/unesco-thesaurus.bcp47g.tsv \
| rapper --quiet --input=turtle --output=turtle /dev/fd/0

(Data operation; example of "SKOS version" without OWL/OBO assertions)
    {0} --methodus=_temp_bcp47 \
--punctum-separato-de-fontem=$'\\t' \
999999999/1568346/data/cod-ab-example1-with-inferences.bcp47.tsv \
--rdf-sine-spatia-nominalibus=owl,obo,devnull --rdf-trivio=5002

(Data operation; example of "OWL + OBO" without SKOS linguistic metadata)
    {0} --methodus=_temp_bcp47 \
--punctum-separato-de-fontem=$'\\t' \
999999999/1568346/data/cod-ab-example1-with-inferences.bcp47.tsv \
--rdf-sine-spatia-nominalibus=skos,wdata,devnull --rdf-trivio=5002

(Data operations, header conversion RDF+HXL -> RDF+BCP47)
    varhxl=$(head -n1 \
999999999/1568346/data/cod-ab-example1-with-inferences.no1.tm.hxl.tsv)
    {0} --methodus=_temp_header_hxl_to_bcp47 "$varhxl"

(Data operations, header conversion RDF+BCP47 -> RDF+HXL)
    varbcp47=$(head -n1 \
999999999/1568346/data/cod-ab-example1-with-inferences.bcp47.tsv)
    {0} --methodus=_temp_header_bcp47_to_hxl "$varbcp47"

(Create shorter column names; good for databases, less for command line)
    {0} --methodus=_temp_bcp47_to_bcp47_shortnames \
--punctum-separato-de-fontem=$'\\t' \
999999999/1568346/data/cod-ab-example1-with-inferences.bcp47.tsv

------------------------------------------------------------------------------
                            EXEMPLŌRUM GRATIĀ
------------------------------------------------------------------------------
""".format(__file__)


_ET_AL_URL = [
    # Tools
    'http://prefix.cc/',
    'https://jena.apache.org/',
    'https://www.w3.org/2018/09/rdf-data-viz/',
    'https://rdf2svg.redefer.rhizomik.net/',
    # 'http://robot.obolibrary.org/reason',
    # Papers
    'https://www.w3.org/2009/12/rdf-ws/papers/ws21',
    # https://en.wikipedia.org/wiki/Ontology_engineering
    # 300 page book
    # - https://people.cs.uct.ac.za/~mkeet/files/OEbook.pdf
    # - https://people.cs.uct.ac.za/~mkeet/OEbook/OEsoftware.html#OElang
    'https://www.w3.org/2001/sw/BestPractices/OEP/SimplePartWhole/',
    'https://en.wikipedia.org/wiki/Mereology',
]

# https://github.com/seebi/rdf.sh#installation
# /workspace/bin/rdf
# https://github.com/essepuntato/undo/blob/master/ontology/current/undo.ttl

# autopep8 --list-fixes ./999999999/0/999999999_54872.py
# pylint --disable=W0511,C0103,C0116 ./999999999/0/999999999_54872.py

SYSTEMA_SARCINAE = str(Path(__file__).parent.resolve())
PROGRAMMA_SARCINAE = str(Path().resolve())
# ARCHIVUM_CONFIGURATIONI_DEFALLO = [
#     SYSTEMA_SARCINAE + '/' + NOMEN + '.meta.yml',
#     PROGRAMMA_SARCINAE + '/' + NOMEN + '.meta.yml',
# ]

VENANDUM_INSECTUM = bool(os.getenv('VENANDUM_INSECTUM', ''))

# - https://servicodados.ibge.gov.br/api/v1/localidades
#   /distritos?view=nivelado&oorderBy=municipio-id
# - https://servicodados.ibge.gov.br/api/v1/localidades
#   /municipios?view=nivelado&orderBy=id
# METHODUS_FONTI = {
#     'ibge_un_adm2': 'https://servicodados.ibge.gov.br/api' +
#     '/v1/localidades/municipios?view=nivelado&orderBy=id'
# }


class Cli:

    EXIT_OK = 0
    EXIT_ERROR = 1
    EXIT_SYNTAX = 2

    venandum_insectum: bool = False  # noqa: E701

    def __init__(self):
        """
        Constructs all the necessary attributes for the Cli object.
        """

    def make_args(self, hxl_output=True):
        # parser = argparse.ArgumentParser(description=DESCRIPTION)
        parser = argparse.ArgumentParser(
            prog="999999999_54872",
            description=DESCRIPTION,
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog=__EPILOGUM__
        )

        parser.add_argument(
            'infile',
            help='Input file',
            # required=False,
            nargs='?'
        )

        parser.add_argument(
            '--real-infile-path',
            help='(Quick workaround for edge cases) in case infile becomes'
            'ambigous on shell scripting, use this to force real source path',
            dest='real_infile',
            nargs='?',
            default=None,
            required=False,
        )

        parser.add_argument(
            '--methodus',
            help='Main operation mode',
            dest='methodus',
            nargs='?',
            choices=[
                'auto',  # Uses ad_rdf_ex_configurationi
                'ad_rdf_genericae',
                'ad_rdf_ex_configurationi',
                '_temp_bcp47',
                '_temp_no1',
                '_temp_bcp47_meta_in_json',
                '_temp_hxl_meta_in_json',
                '_temp_hxlstandard_vocab_ix',
                '_temp_header_hxl_to_bcp47',
                '_temp_header_bcp47_to_hxl',
                '_temp_data_hxl_to_bcp47',
                '_temp_bcp47_to_bcp47_shortnames',
                '_temp_no1_to_no1_shortnames',
            ],
            # required=True
            default='auto'
        )

        # objectīvum, n, s, nominativus,
        #                       https://en.wiktionary.org/wiki/objectivus#Latin
        # fōrmātō, n, s, dativus, https://en.wiktionary.org/wiki/formatus#Latin
        # @see about formats and discussion
        # - https://github.com/semantalytics/awesome-semantic-web#serialization
        # - https://ontola.io/blog/rdf-serialization-formats/
        # - doc.wikimedia.org/Wikibase/master/php/md_docs_topics_json.html
        parser.add_argument(
            '--objectivum-formato',
            help='Formato do arquivo exportado',
            dest='objectivum_formato',
            nargs='?',
            choices=[
                'auto',
                'text/csv',
                # https://www.w3.org/TR/turtle/
                'application/x-turtle',
                # https://www.w3.org/TR/n-triples/
                'application/n-triples',
                # # http://ndjson.org/
                # # https://github.com/ontola/hextuples
                # # mimetype???
                # #  - https://stackoverflow.com/questions/51690624
                # #    /json-lines-mime-type
                # #  - https://github.com/wardi/jsonlines/issues/9
                # #  - https://bugzilla.mozilla.org/show_bug.cgi?id=1603986
                # #  - https://stackoverflow.com/questions/41609586
                # #    /loading-wikidata-dump
                # #    - Uses '.ndjson' as extension
                # # 'application/x-ndjson',
                # '_temp_bcp47',
                # '_temp_no1',
                # '_temp_bcp47_meta_in_json',
                # '_temp_hxl_meta_in_json',
                # '_temp_hxlstandard_vocab_ix',
                # '_temp_header_hxl_to_bcp47',
                # '_temp_header_bcp47_to_hxl',
                # '_temp_data_hxl_to_bcp47',
                # '_temp_bcp47_to_bcp47_shortnames',
                # '_temp_no1_to_no1_shortnames',
            ],
            # required=True
            default='auto'
        )

        parser.add_argument(
            '--rdf-trivio',
            help='(Advanced) RDF bag; extract triples from tabular data from '
            'other groups than 1',
            dest='rdf_bag',
            nargs='?',
            # required=True,
            default='1'
        )

        # - spatium, s, n, nominativus, https://en.wiktionary.org/wiki/spatium#Latin
        # - nōminālī, s, n, dativus, https://en.wiktionary.org/wiki/nominalis#Latin
        # - ... /spatium nominali/ (s, n)
        #   - /spatia nōminālibus/ (pl, n)
        #
        parser.add_argument(
            '--rdf-sine-spatia-nominalibus',
            help='Even if source tabular data document how to export to a new '
            'RDF namespace, ignore it. Useful to generate SKOS and OWL '
            'by excluding each other prefixes.',
            dest='rdf_sine_spatia_nominalibus',
            nargs='?',
            # required=True,
            type=lambda x: x.split(',')
        )

        parser.add_argument(
            '--rdf-namespaces-archivo',
            help='HXL file with additional RDF namespaces',
            dest='rdf_namespace_archivo',
            nargs='?',
            # required=True,
            default=None
        )

        # numerordinatio
        # cum (+ ablativus) https://en.wiktionary.org/wiki/cum#Latin
        # antecessōribus, pl, m, ablativus, en.wiktionary.org/wiki/antecessor
        parser.add_argument(
            '--numerordinatio-cum-antecessoribus',
            help='If RDF output should generate implicily Numerordinatio '
            'antecessors',
            metavar="cum_antecessoribus",
            dest="cum_antecessoribus",
            action='store_const',
            const=True,
            default=False
        )

        # numerordinatio
        # ōrdinibus, pl, m, dativus, en.wiktionary.org/wiki/ordo#Latin
        parser.add_argument(
            '--rdf-ontologia-ordinibus',
            help='Of antecessors, the Numerordinatio order which they would '
            'be an [<subject> rdf:type owl:Ontology]. '
            'Requires --numerordinatio-cum-antecessoribus',
            metavar="rdf_ontologia_ordinibus",
            dest="rdf_ontologia_ordinibus",
            nargs='?',
            # required=True,
            type=lambda x: x.split(',')
        )

        # archīvum, n, s, nominativus, https://en.wiktionary.org/wiki/archivum
        # cōnfigūrātiōnī, f, s, dativus,
        #                      https://en.wiktionary.org/wiki/configuratio#Latin
        # ex
        # fontī, m, s, dativus, https://en.wiktionary.org/wiki/fons#Latin
        parser.add_argument(
            '--archivum-configurationi-ex-fonti',
            help='Arquivo de configuração .meta.yml da fonte de dados',
            dest='archivum_configurationi',
            nargs='?',
            # required=True,
            default=None
        )

        # praefīxum	, n, s, nominativus,
        #                         https://en.wiktionary.org/wiki/praefixus#Latin
        # cōnfigūrātiōnī, f, s, dativus,
        #                      https://en.wiktionary.org/wiki/configuratio#Latin
        # ex
        # fontī, m, s, dativus, https://en.wiktionary.org/wiki/fons#Latin
        parser.add_argument(
            '--praefixum-configurationi-ex-fonti',
            help='Prefixo (separado por vírgula) que contém os metadados que'
            'ajudam a entender como HXLTM deveria ser serializado para RDF',
            dest='praefixum_configurationi',
            nargs='?',
            default=None
        )

        parser.add_argument(
            '--punctum-separato-de-fontem',
            help='Character(s) used as separator from input file ' +
            'Used only for tabular results. ' +
            'Defaults to comma ","',
            dest='fontem_separato',
            default=",",
            nargs='?'
        )

        parser.add_argument(
            '--punctum-separato-de-resultatum',
            help='Character(s) used as separator for generate output. ' +
            'Used only for tabular results. ' +
            'Defaults to tab "\t"',
            dest='resultatum_separato',
            default="\t",
            nargs='?'
        )

        parser.add_argument(
            # '--venandum-insectum-est, --debug',
            '--venandum-insectum-est', '--debug',
            help='Habilitar depuração? Informações adicionais',
            metavar="venandum_insectum",
            dest="venandum_insectum",
            action='store_const',
            const=True,
            default=False
        )

        # parser.add_argument(
        #     'outfile',
        #     help='Output file',
        #     nargs='?'
        # )

        return parser.parse_args()

    def execute_cli(self, pyargs, stdin=STDIN, stdout=sys.stdout,
                    stderr=sys.stderr):
        # self.pyargs = pyargs

        if pyargs.real_infile is not None:
            _infile = pyargs.real_infile
            _stdin = False
        else:
            if stdin.isatty():
                _infile = pyargs.infile
                _stdin = False
            else:
                _infile = None
                _stdin = True

        resultatum_separato = pyargs.resultatum_separato
        fontem_separato = pyargs.fontem_separato

        # rdf_namespace_archivo
        if pyargs.rdf_namespace_archivo:
            rdf_namespaces_extras(pyargs.rdf_namespace_archivo)
            # print(RDF_SPATIA_NOMINALIBUS_EXTRAS)
            # pass

        if pyargs.methodus == '_temp_hxlstandard_vocab_ix':
            # Quick draft of an RDF namespace for ix_ attributes;
            # for sake of simplification, should assume they are used
            # on the main direct relation (otherwise would not make sense
            # even if we could pre-compute all relations)
            # raise NotImplementedError('TODO {0}'.format(
            #     pyargs.objectivum_formato))
            hxlvocab = OntologiaVocabularioHXL()
            hxlvocab.praeparatio().imprimere_ad_ttl()
            return self.EXIT_OK

        if pyargs.methodus in [
                '_temp_bcp47_to_bcp47_shortnames',
                '_temp_no1_to_no1_shortnames']:
            # if pyargs.methodus = '_temp_no1_to_no1_shortnames':

            if _stdin and not _infile:
                raise NotImplementedError('{0} not with stdin'.format(
                    pyargs.methodus))

            caput, data = hxltm_carricato_brevibus(
                _infile, _stdin, punctum_separato=fontem_separato)

            est_bcp47 = True
            if pyargs.methodus == '_temp_no1_to_no1_shortnames':
                est_bcp47 = False
                caput_novo = []
                for _item in caput:
                    # print('hxl item     > ', _item)
                    _hxl = HXLHashtagSimplici(_item).praeparatio()
                    _item_bcp47 = _hxl.quod_bcp47(strictum=False)
                    # print('_item_bcp47  > ', _item_bcp47)
                    caput_novo.append(_item_bcp47)
                caput = caput_novo
                # print('caput', caput)

            rdf_sine_spatia_nominalibus = pyargs.rdf_sine_spatia_nominalibus
            if not rdf_sine_spatia_nominalibus:
                rdf_sine_spatia_nominalibus = []
            rdf_sine_spatia_nominalibus.append('devnull')

            meta = bcp47_rdf_extension_poc(
                caput, data, objective_bag=pyargs.rdf_bag,
                rdf_sine_spatia_nominalibus=rdf_sine_spatia_nominalibus,
                cum_antecessoribus=pyargs.cum_antecessoribus,
                rdf_ontologia_ordinibus=pyargs.rdf_ontologia_ordinibus,
                est_meta=True)

            # print('  aa', meta['caput_asa'])
            # print('  bb', meta['caput_asa']['caput_originali'])
            # print('  aa', meta['caput_asa']['caput_ad_columnae_i'])

            numerordinatio_data__sortnames(
                meta['caput_asa'], _infile, est_bcp47=est_bcp47,
                punctum_separato=fontem_separato)

            return self.EXIT_OK

        # _temp_data_hxl_to_bcp47
        # Simplistic conversion of header
        if pyargs.methodus == '_temp_data_hxl_to_bcp47':
            if _stdin:
                raise NotImplementedError('{0} not with stdin'.format(
                    pyargs.methodus))
            # print('oi')

            numerordinatio_data__hxltm_to_bcp47(
                fontem=_infile, punctum_separato=fontem_separato
            )

            # caput, data = hxltm_carricato_brevibus(
            #     _infile, _stdin, punctum_separato=fontem_separato)

            # caput_novo = []
            # for _item in caput:
            #     # print('hxl item     > ', _item)
            #     _hxl = HXLHashtagSimplici(_item).praeparatio()
            #     _item_bcp47 = _hxl.quod_bcp47(strictum=False)
            #     # print('_item_bcp47  > ', _item_bcp47)
            #     caput_novo.append(_item_bcp47)
            # caput = caput_novo

            # print('@TODO')

            return self.EXIT_OK

        # @TODO maybe refactor this temporary part
        # if pyargs.methodus == '_temp_bcp47_meta_in_json':
        if pyargs.methodus in [
                '_temp_bcp47_meta_in_json', '_temp_hxl_meta_in_json']:
            caput, data = hxltm_carricato_brevibus(
                _infile, _stdin, punctum_separato=fontem_separato)

            if pyargs.methodus == '_temp_hxl_meta_in_json':
                caput_novo = []
                for _item in caput:
                    # print('hxl item     > ', _item)
                    _hxl = HXLHashtagSimplici(_item).praeparatio()
                    _item_bcp47 = _hxl.quod_bcp47(strictum=False)
                    # print('_item_bcp47  > ', _item_bcp47)
                    caput_novo.append(_item_bcp47)
                caput = caput_novo
                # print('caput', caput)

            rdf_sine_spatia_nominalibus = pyargs.rdf_sine_spatia_nominalibus
            if not rdf_sine_spatia_nominalibus:
                rdf_sine_spatia_nominalibus = []
            rdf_sine_spatia_nominalibus.append('devnull')

            meta = bcp47_rdf_extension_poc(
                caput, data, objective_bag=pyargs.rdf_bag,
                rdf_sine_spatia_nominalibus=rdf_sine_spatia_nominalibus,
                cum_antecessoribus=pyargs.cum_antecessoribus,
                rdf_ontologia_ordinibus=pyargs.rdf_ontologia_ordinibus,
                est_meta=True)
            print(json.dumps(
                meta, sort_keys=False, ensure_ascii=False, cls=SetEncoder))
            return self.EXIT_OK

        # @TODO remove thsi temporary part
        # if pyargs.methodus == '_temp_bcp47':
        if pyargs.methodus in ['_temp_bcp47', '_temp_no1']:

            caput, data = hxltm_carricato(
                _infile, _stdin, punctum_separato=fontem_separato)

            if pyargs.methodus == '_temp_no1':
                caput_novo = []
                for _item in caput:
                    # print('hxl item     > ', _item)
                    _hxl = HXLHashtagSimplici(_item).praeparatio()
                    _item_bcp47 = _hxl.quod_bcp47(strictum=False)
                    # print('_item_bcp47  > ', _item_bcp47)
                    caput_novo.append(_item_bcp47)
                caput = caput_novo
                # print('caput', caput)

            # print(caput, data)
            # print('')
            meta = bcp47_rdf_extension_poc(
                caput, data, objective_bag=pyargs.rdf_bag,
                rdf_sine_spatia_nominalibus=pyargs.rdf_sine_spatia_nominalibus,
                cum_antecessoribus=pyargs.cum_antecessoribus,
                rdf_ontologia_ordinibus=pyargs.rdf_ontologia_ordinibus)
            # print(json.dumps(meta, sort_keys=True ,ensure_ascii=False))
            # return self.EXIT_OK

            # raise ValueError(meta)

            rdf_spatia_nominalibus = \
                meta['caput_asa']['rdf_spatia_nominalibus']

            for prefix, iri in rdf_spatia_nominalibus.items():
                print('@prefix {0}: <{1}> .'.format(prefix, iri))

            if pyargs.cum_antecessoribus and \
                'antecessoribus_rdf_triplis' in meta and \
                    len(meta['antecessoribus_rdf_triplis']):
                for triple in meta['antecessoribus_rdf_triplis']:
                    print('{0} {1} {2} .'.format(
                        triple[0], triple[1], triple[2]))

            for triple in meta['rdf_triplis']:
                print('{0} {1} {2} .'.format(triple[0], triple[1], triple[2]))

            return self.EXIT_OK

        if pyargs.methodus == '_temp_header_bcp47_to_hxl':
            # delimiter = "\t"
            delimiter = "\t"
            hxl_base = '#item+rem'
            if _stdin is True:
                raise NotImplementedError
            if _infile.find("\t") == -1:
                if _infile.find(",") > -1:
                    delimiter = ','
                else:
                    # If user is requesting only a single header, this will
                    # fail to auto-detect
                    raise NotImplementedError(
                        "Delimiter [{0}]?? Single header item?".format(_infile))

            # Use case: strip line breaks
            _infile = _infile.strip()

            caput = _infile.split(delimiter)
            caput_novo = []
            errors = []

            # TODO: rework this funcion
            # TODO: draft on numerordinatio_caput_bcp47_to_hxlhashtag()
            for item in caput:
                if item in BCP47_AD_HXL:
                    # print(BCP47_AD_HXL[item])
                    # item_meta = bcp47_langtag(BCP47_AD_HXL[item])
                    caput_novo.append(BCP47_AD_HXL[item]['hxltm'])
                    continue
                # item_meta = bcp47_langtag(item,strictum=False)
                item_meta = bcp47_langtag(item)

                if len(item_meta['_error']) == 0 and \
                        item_meta['Language-Tag_normalized']:
                    caput_novo.append('{0}{1}'.format(
                        hxl_base,
                        item_meta['_callbacks']['hxl_attrs']
                    ))
                else:
                    caput_novo.append('qcc-Zxxx-x-error')
                    if len(item_meta['_error']) > 0:
                        errors.append('ERROR: {0}'.format(item))
                        errors.extend(item_meta['_error'])
                    else:
                        errors.append('ERROR: {0} <{1}>'.format(
                            item, item_meta))

                # caput_novo.append('{0}{1}'.format(
                #     hxl_base,
                #     item_meta['_callbacks']['hxl_attrs']
                # ))

            if len(errors) > 0:
                print(errors)
                return self.EXIT_ERROR

            print(delimiter.join(caput_novo))

            # caput, data = hxltm_carricato_brevibus(
            #     _infile, _stdin, punctum_separato="\t")

            # meta = bcp47_rdf_extension_poc(
            #     caput, data, objective_bag=pyargs.rdf_bag,
            #     rdf_sine_spatia_nominalibus=pyargs.rdf_sine_spatia_nominalibus,
            #     est_meta=True)
            # print(json.dumps(meta, sort_keys=False, ensure_ascii=False))
            return self.EXIT_OK

        if pyargs.methodus == '_temp_header_hxl_to_bcp47':
            delimiter = "\t"
            if _stdin is True:
                raise NotImplementedError
            if _infile.find("\t") == -1:
                if _infile.find(",") > -1:
                    delimiter = ','
                else:
                    # If user is requesting only a single header, this will
                    # fail to auto-detect
                    raise NotImplementedError(
                        "Delimiter [{0}]?? Single header item?".format(_infile))

            # Use case: strip line breaks
            _infile = _infile.strip()

            caput = _infile.split(delimiter)
            caput_novo = []
            errors = []

            # print('TODO _temp_header_hxl_to_bcp47', caput)

            for item in caput:
                item_meta = hxl_hashtag_to_bcp47(item)
                # print('')
                # print(item, item_meta)
                if len(item_meta['_error']) == 0 and \
                        item_meta['Language-Tag_normalized']:
                    caput_novo.append(item_meta['Language-Tag_normalized'])
                else:
                    caput_novo.append('qcc-Zxxx-x-error')
                    if len(item_meta['_error']) > 0:
                        errors.append('ERROR: {0}'.format(item))
                        errors.extend(item_meta['_error'])
                    else:
                        errors.append('ERROR: {0} <{1}>'.format(
                            item, item_meta))
                # caput_novo.append('{0}{1}'.format(
                #     hxl_base,
                #     item_meta['_callbacks']['hxl_attrs']
                # ))

            if len(errors) > 0:
                print(errors)
                return self.EXIT_ERROR

            print(delimiter.join(caput_novo))

            return self.EXIT_OK

        # _infile = None
        # _stdin = None
        configuratio = self.quod_configuratio(
            pyargs.archivum_configurationi, pyargs.praefixum_configurationi)
        if pyargs.venandum_insectum or VENANDUM_INSECTUM:
            self.venandum_insectum = True

        climain = CliMain(
            infile=_infile, stdin=_stdin,
            pyargs=pyargs,
            configuratio=configuratio,
            venandum_insectum=self.venandum_insectum
        )

        if pyargs.objectivum_formato == 'auto':
            return climain.actio()
        if pyargs.objectivum_formato == 'text/csv':
            return climain.actio()
        if pyargs.objectivum_formato == 'application/x-turtle':
            return climain.actio()
            # return self.EXIT_OK
        if pyargs.objectivum_formato == 'application/n-triples':
            return climain.actio()
            # return self.EXIT_OK

        # if pyargs.objectivum_formato == 'uri_fonti':
        #     print(METHODUS_FONTI[pyargs.methodus])
        #     return self.EXIT_OK

        # if pyargs.objectivum_formato == 'json_fonti':
        #     return climain.json_fonti(METHODUS_FONTI[pyargs.methodus])

        # if pyargs.objectivum_formato == 'json_fonti_formoso':
        #     return climain.json_fonti(
        #         METHODUS_FONTI[pyargs.methodus],
        #         formosum=True,
        #         # ex_texto=True
        #     )

        # if pyargs.objectivum_formato in ['csv', 'tsv']:
        #     if json_fonti_texto is None:
        #         json_fonti_texto = climain.json_fonti(
        #             METHODUS_FONTI[pyargs.methodus], ex_texto=True)
        #     # print('json_fonti_texto', json_fonti_texto)
        #     return climain.objectivum_formato_csv(json_fonti_texto)

        # if pyargs.objectivum_formato in [
        #         'hxl_csv', 'hxltm_csv', 'hxl_tsv', 'hxltm_tsv']:
        #     if json_fonti_texto is None:
        #         json_fonti_texto = climain.json_fonti(
        #             METHODUS_FONTI[pyargs.methodus], ex_texto=True)
        #     return climain.objectivum_formato_csv(json_fonti_texto)

        print('Unknow option.')
        return self.EXIT_ERROR

    def quod_configuratio(
        self,
        archivum_configurationi: str = None,
        praefixum_configurationi: str = None
    ) -> dict:
        """quod_configuratio

        Args:
            archivum_configurationi (str, optional):

        Returns:
            (dict):
        """
        praefixum = []
        if praefixum_configurationi:
            praefixum = praefixum_configurationi.split(',')

        if exists(archivum_configurationi):
            with open(archivum_configurationi, "r") as read_file:
                datum = yaml.safe_load(read_file)
                while len(praefixum) > 0:
                    ad_hoc = praefixum.pop(0)
                    if ad_hoc in datum:
                        datum = datum[ad_hoc]
                    else:
                        raise ValueError('{0} [{1}]: [{2}?]'.format(
                            archivum_configurationi,
                            praefixum_configurationi,
                            ad_hoc,
                        ))
                return datum

        raise FileNotFoundError(
            'archivum_configurationi {0}'.format(
                str(archivum_configurationi)))


class CliMain:
    """Remove .0 at the end of CSVs from data exported from XLSX and likely
    to have numeric values (and trigger weird bugs)
    """

    delimiter = ','

    hxltm_ad_rdf: Type['HXLTMAdRDFSimplicis'] = None
    pyargs: dict = None
    venandum_insectum: bool = False  # noqa

    def __init__(
            self, infile: str = None, stdin: bool = None,
            pyargs: dict = None, configuratio: dict = None,
            venandum_insectum: bool = False  # noqa
    ):
        """
        Constructs all the necessary attributes for the Cli object.
        """
        self.infile = infile
        self.stdin = stdin
        self.pyargs = pyargs
        self.objectivum_formato = pyargs.objectivum_formato
        # self.methodus = pyargs.methodus
        self.configuratio = configuratio
        self.venandum_insectum = venandum_insectum

        caput, datum = hxltm_carricato(infile, stdin)

        # delimiter = ','
        if self.objectivum_formato in ['tsv', 'hxltm_tsv', 'hxl_tsv']:
            self.delimiter = "\t"
        # print('oi HXLTMAdRDFSimplicis')
        self.hxltm_ad_rdf = HXLTMAdRDFSimplicis(
            configuratio, pyargs.objectivum_formato, caput, datum,
            venandum_insectum=self.venandum_insectum
        )

        # methodus_ex_tabulae = configuratio['methodus'][self.methodus]

        # self.tabula = TabulaAdHXLTM(
        #     methodus_ex_tabulae=methodus_ex_tabulae,
        #     methodus=self.methodus,
        #     objectivum_formato=self.objectivum_formato
        # )

        # self.outfile = outfile
        # self.header = []
        # self.header_index_fix = []

    def actio(self):
        # āctiō, f, s, nominativus, https://en.wiktionary.org/wiki/actio#Latin
        if self.pyargs.objectivum_formato == 'text/csv':
            return self.hxltm_ad_rdf.resultatum_ad_csv()
        if self.pyargs.objectivum_formato == 'application/x-turtle':
            return self.hxltm_ad_rdf.resultatum_ad_turtle()
        if self.pyargs.objectivum_formato == 'application/n-triples':
            raise NotImplementedError(
                'Use turtle output and pipe to rapper '
                '(raptor2-utils) or similar')
            return self.hxltm_ad_rdf.resultatum_ad_ntriples()
            # print('oi actio')
            # numerordinatio_neo_separatum
        # print('failed')


def numerordinatio_data__hxltm_to_bcp47(
    fontem: str, punctum_separato: str = ","
):
    # json.dumps(caput_asa)
    # print(json.dumps(caput_asa))
    # return ''
    # print(caput_asa['caput_originali'])
    # print(caput_asa['caput_ad_columnae_i'])

    caput, _data = hxltm_carricato_brevibus(
        fontem, est_stdin=False, punctum_separato=punctum_separato)

    caput_novo = []
    for _item in caput:
        # print('hxl item     > ', _item)
        _hxl = HXLHashtagSimplici(_item).praeparatio()
        _item_bcp47 = _hxl.quod_bcp47(strictum=False)
        # print('_item_bcp47  > ', _item_bcp47)
        caput_novo.append(_item_bcp47)

    res_novae = []

    with open(fontem, 'r') as _fons:
        _writer = csv.writer(sys.stdout, delimiter=punctum_separato)
        _csv_reader = csv.reader(_fons, delimiter=punctum_separato)

        # discard original header
        next(_csv_reader)
        # _writer.writerow(_header_original)
        _writer.writerow(caput_novo)

        for linea in _csv_reader:
            linea_novae = linea
            if len(res_novae) > 0:
                linea_novae.extend(res_novae)
            _writer.writerow(linea_novae)


def numerordinatio_data__sortnames(
    caput_asa: dict, fontem: str,
    est_bcp47: bool = True, punctum_separato: str = ","
):
    # json.dumps(caput_asa)
    # print(json.dumps(caput_asa))
    # return ''
    # print(caput_asa['caput_originali'])
    # print(caput_asa['caput_ad_columnae_i'])

    caput_novo = []
    res_novae = []

    for item in caput_asa['caput_ad_columnae_i']:
        if isinstance(item, list):
            caput_novo.append(item[0])
            res_novae.append(item[1])
        else:
            caput_novo.append(item)

    if not est_bcp47:
        caput_novo = numerordinatio_caput_bcp47_to_hxlhashtag(caput_novo)

    # print('   oi', caput_novo)

    with open(fontem, 'r') as _fons:
        _writer = csv.writer(sys.stdout, delimiter=punctum_separato)
        _csv_reader = csv.reader(_fons, delimiter=punctum_separato)

        # discard original header
        next(_csv_reader)
        # _writer.writerow(_header_original)
        _writer.writerow(caput_novo)

        for linea in _csv_reader:
            linea_novae = linea
            if len(res_novae) > 0:
                linea_novae.extend(res_novae)
            _writer.writerow(linea_novae)


def numerordinatio_caput_bcp47_to_hxlhashtag(
        caput: str, hxl_base: str = '#item+rem') -> str:

    caput_novo = []
    errors = []
    for item in caput:
        if item in BCP47_AD_HXL:
            # print(BCP47_AD_HXL[item])
            # item_meta = bcp47_langtag(BCP47_AD_HXL[item])
            caput_novo.append(BCP47_AD_HXL[item]['hxltm'])
            continue
        # item_meta = bcp47_langtag(item,strictum=False)
        item_meta = bcp47_langtag(item)

        # print('   333', item_meta['_callbacks']['hxl_attrs'])

        if len(item_meta['_error']) == 0 and \
                item_meta['Language-Tag_normalized']:
            caput_novo.append('{0}{1}'.format(
                hxl_base,
                item_meta['_callbacks']['hxl_attrs']
            ))
        else:
            caput_novo.append('qcc-Zxxx-x-error')
            if len(item_meta['_error']) > 0:
                errors.append('ERROR: {0}'.format(item))
                errors.extend(item_meta['_error'])
            else:
                errors.append('ERROR: {0} <{1}>'.format(
                    item, item_meta))

    if len(errors) > 0:
        raise SyntaxError('<{0}>? <{1}>'.format(
            caput, errors
        ))

    return caput_novo


def numerordinatio_neo_separatum(
        numerordinatio: str, separatum: str = "_") -> str:
    resultatum = ''
    resultatum = numerordinatio.replace('_', separatum)
    resultatum = resultatum.replace('/', separatum)
    resultatum = resultatum.replace(':', separatum)
    # TODO: add more as need
    return resultatum


def numerordinatio_ordo(numerordinatio: str) -> int:
    normale = numerordinatio_neo_separatum(numerordinatio, '_')
    return (normale.count('_') + 1)


def numerordinatio_progenitori(
        numerordinatio: str, separatum: str = "_") -> int:
    # prōgenitōrī, s, m, dativus, https://en.wiktionary.org/wiki/progenitor
    normale = numerordinatio_neo_separatum(numerordinatio, separatum)
    _parts = normale.split(separatum)
    _parts = _parts[:-1]
    if len(_parts) == 0:
        return "0"
    return separatum.join(_parts)


if __name__ == "__main__":

    est_cli = Cli()
    args = est_cli.make_args()
    # print('  >>>>  args', args)
    # raise ValueError(args)

    est_cli.execute_cli(args)
