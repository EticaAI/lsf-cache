#!/usr/bin/env python3
# ==============================================================================
#
#          FILE:  999999999_521850.py
#
#         USAGE:  ./999999999/0/999999999_521850.py
#                 ./999999999/0/999999999_521850.py --help
#
#   DESCRIPTION:  RUN /999999999/0/999999999_521850.py --help
#                - Q521850, https://www.wikidata.org/wiki/Q521850
#                  - data scraping (Q521850)
#
#       OPTIONS:  ---
#
#  REQUIREMENTS:  - python3
#                   - pip install xlrd
#                   - pip install pandasdmx
#          BUGS:  ---
#         NOTES:  ---
#       AUTHORS:  Emerson Rocha <rocha[at]ieee.org>
# COLLABORATORS:  ---
#       COMPANY:  EticaAI
#       LICENSE:  Public Domain dedication or Zero-Clause BSD
#                 SPDX-License-Identifier: Unlicense OR 0BSD
#       VERSION:  v1.0.0
#       CREATED:  2022-07-27 04:59 UTC based on 999999999_10263485
#      REVISION:  ---
# ==============================================================================

# pytest
#    python3 -m doctest ./999999999/0/999999999_521850.py

import json
import os
import re
import shutil
import sys
import argparse
import csv
# import re
from pathlib import Path
from os.path import exists
from time import sleep

# from functools import reduce
from typing import (
    Any,
    List,
    Pattern,
    Type,
    # Dict,
    # List,
)

import zipfile

from L999999999_0 import (
    # hxltm_carricato,
    NUMERORDINATIO_BASIM,
    hxltm__data_pivot_wide,
    hxltm__data_sort,
    hxltm__ixattr_ex_urn,
    hxltm_hashtag_ix_ad_rdf,
    numerordinatio_neo_separatum,
    # TabulaAdHXLTM
)

import requests

# try:
#     from openpyxl import (
#         load_workbook
#     )
# except ModuleNotFoundError:
#     # Error handling
#     pass

try:
    import xlrd
except ModuleNotFoundError:
    # Error handling
    pass
try:
    import pandasdmx as sdmx
except ModuleNotFoundError:
    # Error handling
    pass

# import yaml

# import xml.etree.ElementTree as XMLElementTree

STDIN = sys.stdin.buffer

NOMEN = '999999999_521850'

DESCRIPTION = f"""
{__file__} Generic pre-processor for data scrapping. Mostly access external
services and prepare their data to HXLTM (which then can be reused by rest of
the tools)

Trivia:
- Q521850, https://www.wikidata.org/wiki/Q521850
  - data scraping (Q521850)
"""

__EPILOGUM__ = f"""
------------------------------------------------------------------------------
                            EXEMPLŌRUM GRATIĀ
------------------------------------------------------------------------------
(Collective of humans / adm0 statistics) . . . . . . . . . . . . . . . . . . . .

    {__file__} --methodus-fonti=undata

    {__file__} --methodus-fonti=undata --methodus=POP

    {__file__} --methodus-fonti=unhcr

    {__file__} --methodus-fonti=unochafts

    {__file__} --methodus-fonti=unwpf

(Total population)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
    {__file__} --methodus-fonti=worldbank --methodus=SP.POP.TOTL

    {__file__} --methodus-fonti=worldbank --methodus=SP.POP.TOTL \
--objectivum-formato=link-fonti

    {__file__} --methodus-fonti=worldbank --methodus=SP.POP.TOTL \
--objectivum-formato=csv

    {__file__} --methodus-fonti=worldbank --methodus=SP.POP.TOTL \
--objectivum-transformationi=annus-recenti --objectivum-formato=hxltm

(Rural population) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
    {__file__} --methodus-fonti=worldbank --methodus=SP.RUR.TOTL \
--objectivum-formato=hxltm

(Subpopulation; population by themes, such as by age, gender/sex, ...) . . . . .
    {__file__} --methodus-fonti=worldbank --methodus=health \
--objectivum-formato=hxltm-wide

    {__file__} --methodus-fonti=worldbank --methodus=health \
--objectivum-transformationi=annus-recenti --objectivum-formato=hxltm-wide

(Everything HXLTMlized and Wide format, all indicators from group) . . . . . .
    {__file__} --methodus-fonti=worldbank --methodus=environment \
--objectivum-transformationi='annus-recenti-exclusivo,hxlize-urn-worldbank' \
--objectivum-formato=hxltm-wide

(Merge several thematic groups from Worldbank, then extract explicity know ) . .

    {__file__} --methodus-fonti=worldbank --methodus=health \
--objectivum-formato=csv > 999999/0/pivot-health.csv
    {__file__} --methodus-fonti=worldbank --methodus=environment \
--objectivum-formato=csv > 999999/0/pivot-environment.csv
    tail -n +2 999999/0/pivot-health.csv > 999999/0/pivot--dataonly.csv
    tail -n +2 999999/0/pivot-environment.csv >> 999999/0/pivot--dataonly.csv
    sort --output=999999/0/pivot--dataonly.csv 999999/0/pivot--dataonly.csv
    head -n 1 999999/0/pivot-health.csv > 999999/0/pivot-merged.csv
    cat 999999/0/pivot--dataonly.csv >> 999999/0/pivot-merged.csv
    {__file__} --methodus-fonti=worldbank \
--methodus=file://999999/0/pivot-merged.csv \
--objectivum-transformationi=annus-recenti-exclusivo \
--objectivum-formato=hxltm-wide > 999999/0/pivot-merged-final.tm.csv.hxl.csv
    frictionless validate 999999/0/pivot-merged-final.tm.csv.hxl.csv

(Individual humans) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
See https://interpol.api.bund.dev/

    {__file__} --methodus-fonti=interpol --methodus=red \
--archivum-objetivum=999999/0/interpol-red.csv

    {__file__} --methodus-fonti=interpol --methodus=un \
--archivum-objetivum=999999/0/interpol-un.csv

    {__file__} --methodus-fonti=interpol --methodus=red \
--objectivum-formato=hxltm \
--archivum-objetivum=999999/0/interpol-red.tm.hxl.csv

    {__file__} --methodus-fonti=interpol --methodus=un \
--objectivum-formato=hxltm \
--archivum-objetivum=999999/0/interpol-un.tm.hxl.csv

(Worldbank, simpler format, without RDF-like mapping) . . . . . . . . . . . . .
    {__file__} --methodus-fonti=worldbank --methodus=aid-effectiveness \
--objectivum-formato=csv
    {__file__} --methodus-fonti=worldbank --methodus=health \
--objectivum-formato=csv

(Etc) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
    {__file__} --methodus-fonti=sdmx-tests

------------------------------------------------------------------------------
                            EXEMPLŌRUM GRATIĀ
------------------------------------------------------------------------------
"""

# @TODO create some sort of unocha-fts-simple and get the spreadsheet from
#       https://fts.unocha.org/global-funding/countries/2022
#       already with country/territory codes (Rocha, 2022-08-10 22:56 UTC)

# @TODO maybe do some data mining from:
#       - https://en.wikipedia.org/wiki/List_of_ongoing_armed_conflicts
#       - https://en.wikipedia.org/wiki/List_of_countries_by_intentional_homicide_rate
#       - https://dataunodc.un.org/content/homicide-country-data

# Other sources here https://pandasdmx.readthedocs.io/en/v1.0/
DATA_SCRAPPING_HELP = {
    'INTERPOL': [
        'https://interpol.api.bund.dev/',
        'https://www.wikidata.org/wiki/Q3088566',  # Interpol notice (Q3088566)
        # Interpol Red Notice (Q47612352)
        'https://www.wikidata.org/wiki/Q47612352',
        # Interpol-United Nations Security Council Special Notice (Q47613015)
        'https://www.wikidata.org/wiki/Q47613015',

    ],
    'UNDATA': [
        'https://data.un.org/',
        'http://data.un.org/Host.aspx?Content=API',
    ],
    'UNHCR': [
        'https://www.unhcr.org/global-public-api.html',
        'https://data.unhcr.org/en/geoservices/',
        'https://www.unhcr.org/refugee-statistics/',
    ],
    'UNOCHAFTS': [
        'https://fts.unocha.org/'
    ],
    'UNWPF': [
        'https://geonode.wfp.org/',
    ],
    'WORLDBANK': [
        'https://data.worldbank.org/',
        # Total population
        'https://data.worldbank.org/indicator/SP.POP.TOTL',
    ],
}

DATA_HXL_DE_CSV_GENERIC = {
    'country name': '#country+name',
    'country code': '#country+code+v_iso3',  # World Bank
    'indicator name': '#indicator+name',  # World Bank
    'indicator code': '#indicator+code',  # World Bank
    'indicator value': '#indicator+value',  # World Bank (if recent-year)
    'indicator date': '#indicator+date',  # World Bank (if recent-year)
    'entity_id': '#item+code+v_interpol',  # INTERPOL
    'un_reference': '#item+code+unref',  # INTERPOL
    'forename': '#item+forename',  # INTERPOL
    'date_of_birth': '#date+birth',  # INTERPOL
    'nationalities': '#item+v_iso2',  # INTERPOL
    '_links.self': '#item+url',  # INTERPOL
}

DATA_HXLTM_DE_HXL_GENERIC = {
    '#meta+rem+i_eng+is_latn+name': '#country+name',

    # Population statistics, with year -----------------------------------------
    # population (P1082)
    '#item+rem+i_qcc+is_zxxx+ix_iso8601v{v1}+ix_xywdatap1082': r"^#population\+t\+year(?P<v1>[0-9]{4})$",
    '#item+rem+i_qcc+is_zxxx+ix_xywdatap1082': r"^#population\+t$",
    '#meta+rem+i_qcc+is_zxxx+ix_xywdatap1082': r"^#meta\+population\+t$",
    # female population (P1539)
    '#item+rem+i_qcc+is_zxxx+ix_iso8601v{v1}+ix_xywdatap1539': r"^#population\+f\+year(?P<v1>[0-9]{4})$",
    # male population (P1540)
    '#item+rem+i_qcc+is_zxxx+ix_iso8601v{v1}+ix_xywdatap1540': r"^#population\+m\+year(?P<v1>[0-9]{4})$",
    # rural population (P6344)
    '#item+rem+i_qcc+is_zxxx+ix_iso8601v{v1}+ix_xywdatap6344': r"^#population\+rural\+year(?P<v1>[0-9]{4})$",
    # urban population (P6343)
    '#item+rem+i_qcc+is_zxxx+ix_iso8601v{v1}+ix_xywdatap6343': r"^#population\+urban\+year(?P<v1>[0-9]{4})$",

    # Houseolds? No data with this yet
    # https://www.wikidata.org/wiki/Property:P1538

    # Population statistics, without year -------------------------------------
    # population (P1082)
    # '#item+rem+i_qcc+is_zxxx+ix_xywdatap1082': r"^#population\+t$",
    # # female population (P1539)
    # '#item+rem+i_qcc+is_zxxx+ix_xywdatap1539': r"^#population\+f$",
    # # male population (P1540)
    # '#item+rem+i_qcc+is_zxxx+ix_xywdatap1540': r"^#population\+m$",

    '#item+rem+i_qcc+is_zxxx+ix_iso8601v{v1}+ix_xyexhxltrivio': r"^#indicator\+value\+year(?P<v1>[0-9]{4})$",

    # HXL hashtags to replace ix_xyexhxltrivio when exploding the coluns
    # '#item+rem+i_qcc+is_zxxx+ix_xyadhxltrivio': None,
}

DATA_NO1_DE_HXLTM_GENERIC = {
    # '^(?P<t>#[a-z0-9]{3,99})\+rem\+i_qcc\+is_zxxx\+ix_xywdatap(?P<v2>[0-9]{1,12})'
    '#{t}+rem+i_qcc+is_zxxx+ix_iso8601v{v1}+rdf_p_wdata_p{v2}_s{trivio}+rdf_t_xsd_int': r"^#(?P<t>[a-z0-9]{3,99})\+rem\+i_qcc\+is_zxxx\+ix_iso8601v(?P<v1>[0-9]{4})\+ix_xywdatap(?P<v2>[0-9]{1,12})"
}

DATA_HXLTM_CASTTYPE = {
    'ix_xywdatap1082': 'rdf_t_xsd_int',
    'ix_xywdatap1539': 'rdf_t_xsd_int',
    'ix_xywdatap1540': 'rdf_t_xsd_int',
    'ix_xywdatap6344': 'rdf_t_xsd_int',
    'ix_xywdatap6343': 'rdf_t_xsd_int',
}

DATA_METHODUS = {
    'worldbank': {
        # https://data.worldbank.org/topic/agriculture-and-rural-development?view=chart
        'agriculture-and-rural-development': {
            'download_url': 'https://api.worldbank.org/v2/en/topic/1?downloadformat=csv'
        },
        # https://data.worldbank.org/topic/aid-effectiveness?view=chart
        'aid-effectiveness': {
            'download_url': 'https://api.worldbank.org/v2/en/topic/2?downloadformat=csv'
        },
        'climate-change': {
            'download_url': 'https://api.worldbank.org/v2/en/topic/19?downloadformat=csv'
        },
        'economy-and-growth': {
            'download_url': 'https://api.worldbank.org/v2/en/topic/3?downloadformat=csv'
        },
        'education': {
            'download_url': 'https://api.worldbank.org/v2/en/topic/4?downloadformat=csv'
        },
        'energy-and-mining': {
            'download_url': 'https://api.worldbank.org/v2/en/topic/5?downloadformat=csv'
        },
        'environment': {
            'download_url': 'https://api.worldbank.org/v2/en/topic/6?downloadformat=csv'
        },
        'external-debt': {
            'download_url': 'https://api.worldbank.org/v2/en/topic/20?downloadformat=csv'
        },
        'financial-sector': {
            'download_url': 'https://api.worldbank.org/v2/en/topic/7?downloadformat=csv'
        },
        'gender': {
            'download_url': 'https://api.worldbank.org/v2/en/topic/17?downloadformat=csv'
        },
        # https://data.worldbank.org/topic/health?view=chart
        'health': {
            'download_url': 'https://api.worldbank.org/v2/en/topic/8?downloadformat=csv'
        },
        'infrastructure': {
            'download_url': 'https://api.worldbank.org/v2/en/topic/9?downloadformat=csv'
        },
        'poverty': {
            'download_url': 'https://api.worldbank.org/v2/en/topic/11?downloadformat=csv'
        },
        'private-sector': {
            'download_url': 'https://api.worldbank.org/v2/en/topic/12?downloadformat=csv'
        },
        'public-sector': {
            'download_url': 'https://api.worldbank.org/v2/en/topic/13?downloadformat=csv'
        },
        'science-and-technology': {
            'download_url': 'https://api.worldbank.org/v2/en/topic/14?downloadformat=csv'
        },
        'social-development': {
            'download_url': 'https://api.worldbank.org/v2/en/topic/15?downloadformat=csv'
        },
        'social-protection-and-labor': {
            'download_url': 'https://api.worldbank.org/v2/en/topic/10?downloadformat=csv'
        },
        'trade': {
            'download_url': 'https://api.worldbank.org/v2/en/topic/21?downloadformat=csv'
        },
        'urban-development': {
            'download_url': 'https://api.worldbank.org/v2/en/topic/16?downloadformat=csv'
        },
    }
}

DATA_HXL_DE_CSV_REGEX = {
    # @see https://data.humdata.org/tools/hxl-example/
    # @see https://data.worldbank.org/indicator
    'worldbank': {

        # Population statistics, thematic
        # Only for numeric
        # https://www.wikidata.org/wiki/Property:P1082
        'SP.POP.TOTL': ['#population+t+year{0}', ['ix_xywdatap1082']],

        # https://data.worldbank.org/indicator/SP.RUR.TOTL
        # https://www.wikidata.org/wiki/Property:P6344
        # 'SP.RUR.TOTL': '#population+ix_xywdatap6344+year{0}',
        'SP.RUR.TOTL': ['#population+rural+year{0}', ['ix_xywdatap6344']],

        # https://data.worldbank.org/indicator/SP.POP.TOTL.FE.IN
        # https://www.wikidata.org/wiki/Property:P1539
        'SP.POP.TOTL.FE.IN': ['#population+f+year{0}', ['ix_xywdatap1539']],

        # https://data.worldbank.org/indicator/SP.POP.TOTL.MA.IN
        # https://www.wikidata.org/wiki/Property:P1540
        'SP.POP.TOTL.MA.IN': ['#population+m+year{0}', ['ix_xywdatap1540']],

        # - minimum age (P2899)
        #   - https://www.wikidata.org/wiki/Property:P2899

        # - maximum age (P4135)
        #   - https://www.wikidata.org/wiki/Property:P4135

        # Population ages 0-14, total
        'SP.POP.0014.TO': ['#population+t_0_14+year{0}', [
            'ix_xywdatap1082', 'ix_xywdatap2899v0', 'ix_xywdatap4135v14']],
        # Population ages 0-14, female
        'SP.POP.0014.FE.IN': ['#population+f_0_14+year{0}', [
            'ix_xywdatap1539', 'ix_xywdatap2899v0', 'ix_xywdatap4135v14']],
        # Population ages 0-14, male
        'SP.POP.0014.MA.IN': ['#population+m_0_14+year{0}', [
            'ix_xywdatap1540', 'ix_xywdatap2899v0', 'ix_xywdatap4135v14']],

        # Population ages 15-64, total
        'SP.POP.1564.TO': ['#population+t_15_64+year{0}', [
            'ix_xywdatap1082', 'ix_xywdatap2899v15', 'ix_xywdatap4135v64']],
        # Population ages 15-64, female
        'SP.POP.1564.FE.IN': ['#population+f_15_64+year{0}', [
            'ix_xywdatap1539', 'ix_xywdatap2899v15', 'ix_xywdatap4135v64']],
        # Population ages 15-64, male
        'SP.POP.1564.MA.IN': ['#population+m_15_64+year{0}', [
            'ix_xywdatap1540', 'ix_xywdatap2899v15', 'ix_xywdatap4135v64']],


        # Population ages 65 and above, total
        'SP.POP.65UP.TO': ['#population+t_65_999+year{0}', [
            'ix_xywdatap1082', 'ix_xywdatap2899v65']],
        # Population ages 65 and above, female
        'SP.POP.65UP.FE.IN': ['#population+f_65_999+year{0}', [
            'ix_xywdatap1539', 'ix_xywdatap2899v65']],
        # Population ages 65 and above, male
        'SP.POP.65UP.MA.IN': ['#population+m_65_999+year{0}', [
            'ix_xywdatap1540', 'ix_xywdatap2899v65']],

        # @TODO if we take the %, there are other age ranges. Eventualy
        #       deal with this

        # ---------------------------------------------------------------------
        # nominal GDP (P2131)
        'NY.GDP.MKTP.CD': ['#indicator+value+year{0}', [
            'ix_xywdatap2131']],
        # area (P2046)
        'AG.SRF.TOTL.K2': ['#indicator+value+year{0}', [
            'ix_xywdatap2046']],
        # literacy rate (P6897)
        'SE.ADT.LITR.ZS': ['#indicator+value+year{0}', [
            'ix_xywdatap6897']],
        # life expectancy (P2250)
        'SP.DYN.LE00.IN': ['#indicator+value+year{0}', [
            'ix_xywdatap2250']],
        # Gini coefficient (P1125)
        'SI.POV.GINI': ['#indicator+value+year{0}', [
            'ix_xywdatap1125']],
        # unemployment rate (P1198)
        # - https://data.worldbank.org/indicator/SL.UEM.TOTL.ZS
        #   - See also https://data.worldbank.org/indicator/SL.EMP.TOTL.SP.ZS
        'SL.UEM.TOTL.ZS': ['#indicator+value+year{0}', [
            'ix_xywdatap1198']],

        # https://data.worldbank.org/indicator/EN.ATM.CO2E.KT
        # https://www.wikidata.org/wiki/Q67201057
        # carbon emission (Q67201057)
        'EN.ATM.CO2E.KT': ['#indicator+value+year{0}', [
            'ix_xywdataq67201057']],

        # https://data.worldbank.org/indicator/AG.LND.PRCP.MM
        # annual precipitation (Q10726724)
        'AG.LND.PRCP.MM': ['#indicator+value+year{0}', [
            'ix_xywdataq10726724']],

        # Money related, thematic
        # https://data.worldbank.org/indicator/BX.GRT.EXTA.CD.WD?view=chart
        'BX.GRT.EXTA.CD.WD': ['#value+funding+usd+year{0}'],
        # https://data.worldbank.org/indicator/BX.GRT.TECH.CD.WD?view=chart
        'BX.GRT.TECH.CD.WD': ['#value+funding+usd+year{0}'],

        # TODOs
        # GINI https://data.worldbank.org/indicator/SI.POV.GINI?view=chart
        # Redugees https://data.worldbank.org/indicator/SM.POP.REFG?view=chart

        # - https://data.worldbank.org/indicator?tab=all
        # From all indicators, the health bring most of agregated data
        # - https://data.worldbank.org/topic/health?view=chart
        # - https://api.worldbank.org/v2/en/topic/8?downloadformat=csv
        'health': ['#indicator+value+year{0}'],
        'environment': ['#indicator+value+year{0}'],
        'aid-effectiveness': ['#indicator+value+year{0}'],

        # - ASCII: 29 GS (Group separator)
        #   - x29 = replace non a-z0-9 with this
        # 'SH.STA.WASH.P5': ['#indicator+value+year{0}', [
        #     'ix_urnx29worldbankx29shx29stax29washx29p5']],

        # used with --methodus=file://(...)
        'file': ['#indicator+value+year{0}'],
    }
}


def data_hxl_de_csv_regex_ex_urn(res: str, urn_basi: str = 'worldbank'):
    """data_hxl_de_csv_regex_ex_urn

    Populate DATA_HXL_DE_CSV_REGEX with URN-like ix_ tags

    Args:
        res (str): _description_
        urn_basi (str, optional): _description_. Defaults to 'worldbank'.
    """
    if res not in DATA_HXL_DE_CSV_REGEX[urn_basi]:
        res_ix = hxltm__ixattr_ex_urn(res, urn_basi)
        DATA_HXL_DE_CSV_REGEX[urn_basi][res] = [
            '#indicator+value+year{0}',
            [res_ix]
        ]


DATA_HXL_AD_HXLTM = {
    'ix_iso5218v1': [
        {'t': "#population", 'a': ['m']}
    ],
    'ix_iso5218v2': [
        {'t': "#population", 'a': ['f']}
    ],
    'ix_iso5218v9': [
        {'t': "#population", 'a': ['i']}
    ],
    'ix_iso8601v{0}': [
        {'t': "#population", 'a': [r"^year(?P<v1>[0-9]{4})$"]}
    ],
}

# DATA_HXLTM_AD_RDFTYPE = {
#     'ix_iso8601v': 'rdf_t_xsd_int'
# }


def parse_hashtag(hashtag: str) -> dict:
    """parse_hashtag

    Convert HXL hashtag to dict.

    @TODO maybe refactor in something more full featured

    Args:
        hashtag (str): full hashtag

    Returns:
        dict: _description_
    """
    resultatum = {
        't': '',
        'a': []
    }
    if not hashtag or not hashtag.startswith('#'):
        raise SyntaxError(hashtag)
    _hashtag_norm = hashtag.lower().rstrip('#').split('+')
    resultatum['t'] = _hashtag_norm.pop(0)
    resultatum['a'] = sorted(_hashtag_norm)
    return resultatum


def parse_hashtag_mached_is(hashtag: str, hashtag_refs: List[dict]) -> bool:
    """parse_hashtag

    Convert HXL hashtag to dict.

    @TODO maybe refactor in something more full featured

    Args:
        hashtag (str): full hashtag

    Returns:
        dict: _description_
    """
    _hashtag = parse_hashtag(hashtag)
    for item in hashtag_refs:
        if not item['t'] or _hashtag['t'] == item['t']:
            if len(item['a']) == 0:
                return True
            for _a in item['a']:
                if isinstance(_a, Pattern):
                    _done = False
                    for _vh in _hashtag['a']:
                        if re.match(_a, _vh):
                            _done = True
                    if not _done:
                        return False
                if _a not in _hashtag['a']:
                    return False
            return True
    return False


# Economic
# - https://www.wikidata.org/wiki/Wikidata:Database_reports/List_of_properties/all
#   - nominal GDP (P2131)
#   - P2132	nominal GDP per capita
#   - P2219	real GDP growth rate
#   - P2299	PPP GDP per capita
#   - P4010	GDP (PPP)


# @TODO https://api.hpc.tools/v1/public/fts/flow?year=2022

# Some extra links
# - http://data.un.org/Host.aspx?Content=API
#   - Uses SDMX, https://sdmx.org/?page_id=4500
#       - https://pandasdmx.readthedocs.io/en/v1.0/
# - https://pandasdmx.readthedocs.io/en/v1.0/example.html


# FTS (do not use SDMX)
# - https://api.hpc.tools/docs/v1/
#   - https://api.hpc.tools/v1/public/fts/flow?year=2016
#   - https://api.hpc.tools/v1/public/location
#   - https://api.hpc.tools/v1/public/organization
#   - https://api.hpc.tools/v1/public/plan/country/SDN

# Triangulation, maybe?
# - https://www.devex.com/news/funding-tracker-who-s-sending-aid-to-ukraine-102887

class Cli:

    EXIT_OK = 0
    EXIT_ERROR = 1
    EXIT_SYNTAX = 2

    def __init__(self):
        """
        Constructs all the necessary attributes for the Cli object.
        """

    def make_args(self):
        # parser = argparse.ArgumentParser(description=DESCRIPTION)
        parser = argparse.ArgumentParser(
            prog="999999999_10263485",
            description=DESCRIPTION,
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog=__EPILOGUM__
        )

        parser.add_argument(
            'infile',
            help='Arquivo de entrada',
            nargs='?'
        )

        parser.add_argument(
            '--methodus-fonti',
            help='External data source',
            dest='methodus_fonti',
            nargs='?',
            choices=[
                'interpol',  # https://interpol.api.bund.dev/
                'undata',  # https://data.un.org/
                'unochafts',  # https://fts.unocha.org/
                'unhcr',  # https://www.unhcr.org/global-public-api.html
                          # https://data.unhcr.org/en/geoservices/
                'unwpf',  # https://geonode.wfp.org/
                'worldbank',  # https://data.worldbank.org/
                'sdmx-tests',
            ],
            # required=True
            default='undata'
        )

        parser.add_argument(
            '--methodus',
            help='Underlining method for the data source',
            dest='methodus',
            nargs='?',
            # default=None
            default='help'
        )
        # objectīvum, n, s, nominativus,
        #                       https://en.wiktionary.org/wiki/objectivus#Latin
        # fōrmātō, n, s, dativus, https://en.wiktionary.org/wiki/formatus#Latin
        parser.add_argument(
            '--objectivum-formato',
            help='Formato do arquivo exportado',
            dest='objectivum_formato',
            nargs='?',
            choices=[
                'csv',
                'hxl',
                'hxltm',
                'hxltm-wide',
                'no1',
                'link-fonti',
                # 'tsv',
                # 'hxl_csv',
                # 'hxl_tsv',
                # 'hxltm_csv',
                # 'hxltm_tsv',
            ],
            # required=True
            default='csv'
        )

        parser.add_argument(
            '--objectivum-transformationi',
            help='Apply additional transformation. Varies by source' +
            'Example: "annus-recenti", "annus-recenti-exclusivo", '
            '"annus-recenti-exclusivo,hxlize-urn-worldbank", ',
            dest='objectivum_transformationi',
            # nargs='?',
            # default=None
            # default='help'
            nargs='?',
            type=lambda x: x.split(','),
            default=None
        )

        parser.add_argument(
            '--hxltm-wide-indicators',
            help='For (mostly only) Worldbank operations in group of '
            'this option can be used to restrict to only these indicators. '
            'Useful when already cached everything on disk. '
            'Example: "SP.POP.TOTL,AG.SRF.TOTL.K2,NY.GDP.MKTP.CD"',
            dest='hxltm_wide_indicators',
            # nargs='?',
            # default=None
            # default='help'
            nargs='?',
            type=lambda x: x.split(','),
            default=None
        )

        # archīvum, n, s, nominativus, https://en.wiktionary.org/wiki/archivum
        # cōnfigūrātiōnī, f, s, dativus,
        #                      https://en.wiktionary.org/wiki/configuratio#Latin
        # parser.add_argument(
        #     '--archivum-configurationi',
        #     help='Arquivo de configuração .meta.yml',
        #     dest='archivum_configurationi',
        #     nargs='?',
        #     default=None
        # )

        # parser.add_argument(
        #     'outfile',
        #     help='Output file',
        #     nargs='?'
        # )

        parser.add_argument(
            '--archivum-objetivum',
            help='Output file (for looping operations)',
            dest='archivum_objetivum',
            nargs='?',
            default=None
        )

        parser.add_argument(
            '--numerordinatio-praefixo',
            help='Numerordĭnātĭo prefix',
            dest='numerordinatio_praefixo',
            nargs='?',
            default='999999:0'
        )

        parser.add_argument(
            '--rdf-trivio',
            help='(Advanced) RDF bag; extract triples from tabular data from '
            'other groups than 1603',
            dest='rdf_trivio',
            nargs='?',
            # required=True,
            default='1603'
        )

        return parser.parse_args()

    def execute_cli(self, pyargs, stdin=STDIN, stdout=sys.stdout,
                    stderr=sys.stderr):
        # self.pyargs = pyargs

        _infile = None
        _stdin = None

        # configuratio = self._quod_configuratio(pyargs.archivum_configurationi)

        if stdin.isatty():
            # print("ERROR. Please pipe data in. \nExample:\n"
            #       "  cat data.txt | {0} --actionem-quod-sparql\n"
            #       "  printf \"Q1065\\nQ82151\\n\" | {0} --actionem-quod-sparql"
            #       "".format(__file__))
            # print('non stdin')
            _infile = pyargs.infile
            # return self.EXIT_ERROR
        else:
            # print('est stdin')
            _stdin = stdin

        # print(pyargs.objectivum_formato)
        # print(pyargs)

        # if _stdin is not None:
        #     for line in sys.stdin:
        #         # print('oi')
        #         codicem = line.replace('\n', ' ').replace('\r', '')

        # hf = CliMain(self.pyargs.infile, self.pyargs.outfile)

        if pyargs.methodus_fonti == 'interpol':
            if pyargs.methodus == 'help':
                print(DATA_SCRAPPING_HELP['INTERPOL'])
                return self.EXIT_OK

            ds_interpol = DataScrappingInterpol(
                pyargs.methodus, pyargs.objectivum_formato,
                pyargs.archivum_objetivum)
            ds_interpol.praeparatio()
            # ds_undata.imprimere()
            return self.EXIT_OK

        if pyargs.methodus_fonti == 'undata':
            if pyargs.methodus == 'help':
                print(DATA_SCRAPPING_HELP['UNDATA'])
                return self.EXIT_OK

            ds_undata = DataScrappingUNDATA(
                pyargs.methodus, pyargs.objectivum_formato)
            ds_undata.praeparatio()
            # ds_undata.imprimere()
            return self.EXIT_OK

        if pyargs.methodus_fonti == 'unhcr':
            if pyargs.methodus == 'help':
                print(DATA_SCRAPPING_HELP['UNHCR'])
            return self.EXIT_OK

        if pyargs.methodus_fonti == 'unochafts':
            if pyargs.methodus == 'help':
                print(DATA_SCRAPPING_HELP['UNOCHAFTS'])
                return self.EXIT_OK
            raise NotImplementedError
            return self.EXIT_OK

        if pyargs.methodus_fonti == 'unwpf':
            if pyargs.methodus == 'help':
                print(DATA_SCRAPPING_HELP['UNWPF'])
            raise NotImplementedError
            return self.EXIT_OK

        if pyargs.methodus_fonti == 'worldbank':
            # print(DATA_SCRAPPING_HELP['WORLDBANK'])
            ds_worldbank = DataScrappingWorldbank(
                pyargs.methodus, pyargs.objectivum_formato,
                pyargs.objectivum_transformationi,
                pyargs.numerordinatio_praefixo,
                pyargs.rdf_trivio,
                hxltm_wide_indicators=pyargs.hxltm_wide_indicators
            )
            ds_worldbank.praeparatio()
            ds_worldbank.imprimere()
            return self.EXIT_OK

        if pyargs.methodus_fonti == 'sdmx-tests':

            # @see https://registry.sdmx.org/organisations/agencies.html#
            # @see https://registry.sdmx.org/items/conceptscheme.html
            # @see https://pandasdmx.readthedocs.io/

            print('')
            print('')
            print('')
            print('UNSD')

            unsd = sdmx.Request('UNSD')
            print(unsd)
            cat_response = unsd.categoryscheme()
            print(cat_response)
            print('')
            print('dataflow')

            print('')
            print('  >>> UNSD all dataflows <<<')
            unsd_dataflow = unsd.dataflow()
            print('unsd_dataflow.response.url', unsd_dataflow.response.url)
            dataflows = sdmx.to_pandas(unsd_dataflow.dataflow)
            print(dataflows.head())
            return True

            print('')
            print('')
            print(unsd_dataflow)
            for _item in unsd_dataflow:
                print(_item)
            print('')
            print('unsd_dataflow.DF_UNDATA_COUNTRYDATA ')
            print(unsd_dataflow.dataflow.DF_UNDATA_COUNTRYDATA)
            # https://pandasdmx.readthedocs.io/en/v1.0/howto.html#use-category-schemes-to-explore-data
            print('UNSD all categories list')
            print(sdmx.to_pandas(cat_response.category_scheme.UNdata_Categories))
            print('')
            print('')

            sdmx_wb = sdmx.Request('WB')
            cat_response = sdmx_wb.categoryscheme()
            print(cat_response)

            print('WB all categories list')
            print(sdmx.to_pandas(cat_response.category_scheme.WITS_Data))

            print('')
            print('')
            print('')
            print('WB_WDI')

            # @see https://datahelpdesk.worldbank.org/knowledgebase/articles/1886701-sdmx-api-queries
            sdmx_wb_wdi = sdmx.Request('WB_WDI')
            # sdmx.
            print(sdmx_wb_wdi)
            print(sdmx_wb_wdi.__dict__)
            print('sdmx_wb_wdi.codelist')
            print(sdmx_wb_wdi.codelist)
            # print(sdmx_wb_wdi.categoryscheme())
            # cat_response = sdmx_wb_wdi.categoryscheme()
            # print(cat_response)

            # print('')
            # print('')
            # print('')
            # metadata = sdmx_wb_wdi.datastructure('A.SP_POP_TOTL.AFG')
            # print(metadata)
            # print(metadata.codelist)
            # print(metadata.codelist.__dict__)

            return True

            estat = sdmx.Request('ESTAT')
            metadata = estat.datastructure('DSD_une_rt_a')
            print(metadata)

            for cl in 'CL_AGE', 'CL_UNIT':
                print(sdmx.to_pandas(metadata.codelist[cl]))
            resp = estat.data(
                'une_rt_a',
                key={'GEO': 'EL+ES+IE'},
                params={'startPeriod': '2007'},
            )
            data = resp.to_pandas(
                datetime={'dim': 'TIME_PERIOD', 'freq': 'FREQ'}).xs(
                    'Y15-74', level='AGE', axis=1, drop_level=False)
            print(data.columns.names)
            print(data.columns.levels)

            print(data.loc[:, ('Y15-74', 'PC_ACT', 'T')])

            print('')
            print('')
            print('')
            print('UNSD')

            unsd = sdmx.Request('UNSD')
            print(unsd)
            # unsd = Request('UNSD')
            cat_response = unsd.categoryscheme()
            print(cat_response)
            # https://pandasdmx.readthedocs.io/en/v1.0/howto.html#use-category-schemes-to-explore-data
            print('UNSD all categories list')
            print(sdmx.to_pandas(cat_response.category_scheme.UNdata_Categories))
            # # print(cat_response.write().categoryscheme)
            # # dsd_id = unsd.categoryscheme().dataflow.NA_MAIN.structure.id
            # # dsd_response = unsd.datastructure(resource_id = dsd_id)
            # print('')
            # print('')
            # print('')
            # print('UNICEF')

            # unicef = sdmx.Request('UNICEF')
            # print(unicef)

            # @see https://pandasdmx.readthedocs.io/en/v1.0/example.html
            # @see https://pandasdmx.readthedocs.io/en/v1.0/walkthrough.html
            print('TODO')
            return self.EXIT_OK

        print('Unknow option.')
        return self.EXIT_ERROR


# ./999999999/0/999999999_7200235.py  --methodus=index_praeparationi 1603_16_1_0 --index-nomini=i1603_16_1_0 --index-ad-columnam='ix_unm49'
class Adm0CodexLocali:

    i1603_16_1_0: dict = None
    i1603_16_1_0_alt: dict = {}

    def __init__(
        self
    ):
        _path = NUMERORDINATIO_BASIM + '/999999/0/i1603_16_1_0.index.json'
        if not exists(_path):
            raise FileNotFoundError(
                "Warm up required. Use ./999999999/0/999999999_7200235.py "
                " --methodus=index_praeparationi 1603_16_1_0 "
                "--index-nomini=i1603_16_1_0 --index-ad-columnam='ix_unm49'")

        with open(_path, 'r') as f:
            self.i1603_16_1_0 = json.load(f)

    def quod(self, res: str) -> str:
        if res and res in self.i1603_16_1_0:
            _v = str(int(self.i1603_16_1_0[res]))
            return _v
        if res and res in self.i1603_16_1_0_alt:
            _v = str(int(self.i1603_16_1_0_alt[res]))
            return _v
        return None

    def est(self, clavem: str, res: str) -> str:
        """est create an on-the-fly code.

        Use for loops, so alternative codes can be remembered

        Args:
            clavem (str): _description_
            res (str): _description_

        Returns:
            str: _description_
        """
        self.i1603_16_1_0_alt[clavem] = res
        return None


class DataScrapping:

    def __init__(
        self, methodus: str,
        objectivum_formato: str,
        objectivum_transformationi: list = None,
        numerordinatio_praefixo: str = '999999:0',
        rdf_trivio: str = '1603',
        hxltm_wide_indicators: list = None
    ):

        self.methodus = methodus
        if numerordinatio_praefixo:
            self.numerordinatio_praefixo = numerordinatio_neo_separatum(
                numerordinatio_praefixo, ':'
            )
        # if rdf_trivio:
        self.rdf_trivio = rdf_trivio

        self.objectivum_formato = objectivum_formato
        self.objectivum_transformationi = objectivum_transformationi
        if hxltm_wide_indicators:
            hxltm_wide_indicators = \
                [x.strip() for x in hxltm_wide_indicators if x]
            if len(hxltm_wide_indicators) == 0:
                hxltm_wide_indicators = None
        self.hxltm_wide_indicators = hxltm_wide_indicators
        self._caput = []
        self._temp = {}

        self._skipLineMetaCsv = [
            {
                'index': 0
            },
            # # Example of rule
            # {
            #     'index': 3,
            #     'not_in': DATA_HXL_DE_CSV_REGEX['worldbank'].keys()
            # },
        ]
        self._hxlPivot = {}
        # self._hxlPivot = DATA_HXL_DE_CSV_REGEX['worldbank']
        self._hxlPivotCode = ['#indicator+code',
                              '#meta+rem+i_qcc+is_zxxx+indicator_code']
        # #item+rem+i_qcc+is_zxxx+ix_xyadhxltrivio

        # Use case: --objectivum-transformationi=annus-recenti-exclusivo
        self._skipHXLTMIndex = []

        self._Adm0CodexLocali = None

    def __del__(self):
        """__del__ remove temporary files

        PROTIP: commenting this part allow to inspect partial files
                generated at 999999/0/*.ext
        """
        for clavem, res in self._temp.items():
            # if clavem in ['__source_zip__', '__source_main_csv__']:
            if clavem in ['__source_zip__']:
                continue
            # if exists(res):
            #     os.remove(res)

    def _init_temp(self, suffixus: str = None):
        if not suffixus:
            suffixus = self.methodus
        self._temp = {
            '__source_zip__': '{0}/999999/0/{1}~{2}.zip'.format(
                NUMERORDINATIO_BASIM, type(self).__name__, suffixus
            ),
            '__source_main_csv__': '{0}/999999/0/{1}~{2}.csv'.format(
                NUMERORDINATIO_BASIM, type(self).__name__, suffixus
            ),
            'csv': '{0}/999999/0/{1}~{2}.norm.csv'.format(
                NUMERORDINATIO_BASIM, type(self).__name__, suffixus
            ),
            'hxl': '{0}/999999/0/{1}~{2}.hxl.csv'.format(
                NUMERORDINATIO_BASIM, type(self).__name__, suffixus
            ),
            'hxltm': '{0}/999999/0/{1}~{2}.tm.hxl.csv'.format(
                NUMERORDINATIO_BASIM, type(self).__name__, suffixus
            ),
            'hxltm_wide': '{0}/999999/0/{1}~{2}~WIDE.tm.hxl.csv'.format(
                NUMERORDINATIO_BASIM, type(self).__name__, suffixus
            ),
            'no1': '{0}/999999/0/{1}~{2}.no1.tm.hxl.csv'.format(
                NUMERORDINATIO_BASIM, type(self).__name__, suffixus
            ),
        }

    def _linea_annus_recenti(
            self, caput: list, linea: list, numerae: bool = True) -> list:
        if len(caput) != len(linea) and (len(caput) - 2) != len(linea):
            raise SyntaxError(
                f'len caput != linea [{len(caput)}, {len(linea)}]')

        _index = len(linea) - 1
        for item in reversed(linea):
            if item and len(item) > 0:
                if numerae is True:
                    if not caput[_index].isnumeric():
                        break
                return [item, caput[_index]]
            _index -= 1
        return ['', '']

    def _codicem(self, res: str, strictum: bool = False, index: int = 0) -> str:
        if self._Adm0CodexLocali is None:
            self._Adm0CodexLocali = Adm0CodexLocali()
        _v = self._Adm0CodexLocali.quod(res)
        if _v:
            return _v
        else:
            # if not strict, and exist res, we create a consistent one
            if strictum is False and res:
                self._Adm0CodexLocali.est(res, str(900 + index))
                _v = self._Adm0CodexLocali.quod(res)
                return _v
            # if strictum or not res:
            #     return None
            # self._Adm0CodexLocali.est(res, str(900 + index))
            # print(self._Adm0CodexLocali)
            # _v = self._Adm0CodexLocali.quod(res)
            # return _v
            return None if strictum else str(900 + index)

    def _hxlize_dummy(self, caput: list):
        resultatum = []
        for res in caput:
            if not res:
                resultatum.append('')
                continue
            if res.lower().strip() in DATA_HXL_DE_CSV_GENERIC:
                resultatum.append(DATA_HXL_DE_CSV_GENERIC[res.lower().strip()])
                continue

            if self.methodus in DATA_HXL_DE_CSV_REGEX['worldbank'].keys():
                if len(res) == 4:
                    resultatum.append(DATA_HXL_DE_CSV_REGEX[
                        'worldbank'][self.methodus][0].format(res))
                    continue

            # if self.methodus.startswith('file://') and \
            #     self.methodus_fonti == 'worldbank':
            if self.methodus.startswith('file://'):
                # print(res, resultatum)
                if len(res) == 4:
                    resultatum.append(DATA_HXL_DE_CSV_REGEX[
                        'worldbank']['file'][0].format(res))
                    continue

            resultatum.append(
                '#meta+{0}'.format(
                    res.lower().strip().replace(
                        ' ', '').replace('-', '_'))
            )
        return resultatum

    # def _hxlize_without_year(self, caput_item: str, referens: str):
    #     # Example '#population+t+year2016'
    #     referens_basi = referens.split('+year')[0]
    #     if caput_item == '#indicator+value':
    #         return referens_basi
    #     if caput_item == '#indicator+date':
    #         return referens_basi.replace('#', '#date+')
    #     else:
    #         raise SyntaxError(f'caput_item [{caput_item}]?')

    def _hxltmize(self, caput: list):
        resultatum = []
        for res in caput:
            if not res:
                resultatum.append('')
                continue

            _done = False
            for _ht_novo, _ht_retest in DATA_HXLTM_DE_HXL_GENERIC.items():

                if isinstance(_ht_retest, str) and _ht_retest == res:
                    resultatum.append(_ht_novo)
                    _done = True
                    break

                _resultatum = re.match(_ht_retest, res)
                if not _resultatum:
                    continue
                _vars = _resultatum.groupdict()
                if _vars and len(_vars.keys()) > 0:
                    resultatum.append(_ht_novo.format_map(_vars))
                else:
                    resultatum.append(_ht_novo)
                _done = True
                break

            if _done is True:
                continue

            # if self.objectivum_transformationi == 'annus-recenti':
            # if self.objectivum_transformationi and \
            #         self.objectivum_transformationi.startswith('annus-recenti'):
            if self.objectivum_transformationi and \
                    ('annus-recenti' in self.objectivum_transformationi or
                        'annus-recenti-exclusivo' in self.objectivum_transformationi):
                # self.objectivum_transformationi.startswith('annus-recenti'):
                if res in ['#indicator+value', '#indicator+date']:
                    # -3 is arbritrary, but will range 1960-2020+
                    resultatum.append(
                        self._hxltmize_without_year(res, resultatum[-3])
                    )
                    continue

                # if caput.find('#indicator+value') == -1:
                if '#indicator+value' not in caput:
                    raise SyntaxError(
                        f'internal error, previus step not ready <{caput}>')

            resultatum.append(
                '#meta+rem+i_qcc+is_zxxx+{0}'.format(
                    res.lower().strip().replace(
                        ' ', '').replace('-', '_').replace(
                            '#', '').replace('+', '_'))
            )

        # We keep the value in the memory, but allow conversors exclude
        # if self.objectivum_transformationi == 'annus-recenti-exclusivo':
        if self.objectivum_transformationi and \
                'annus-recenti-exclusivo' in self.objectivum_transformationi:
            # Use case: --objectivum-transformationi=annus-recenti-exclusivo

            # 1 if generic
            # 2 if wide enabled
            _drift = 1

            # if '#item+rem+i_qcc+is_zxxx+ix_xyadhxltrivio' in resultatum:
            #     _drift += 1

            # if self.objectivum_formato == 'hxltm-wide':
            #     _drift = 2

            for item in resultatum:
                if item.find('+ix_iso8601v') > -1:
                    index_without_codicem = resultatum.index(item)
                    # self._skipHXLTMIndex.append(resultatum.index(item))
                    self._skipHXLTMIndex.append(
                        index_without_codicem + _drift
                    )
            # raise ValueError(len(resultatum), self._skipHXLTMIndex, resultatum)
        return resultatum

    def _hxltmize_without_year(self, caput_item: str, referens: str):
        # Example '#population+t+year2016' (if was HXL)
        # Example '#item+rem+i_qcc+is_zxxx+ix_iso8601v2021+ix_xywdatap1082'
        referens_basi = referens.split('+year')[0]
        if caput_item == '#indicator+value':
            # return referens_basi
            # basi = referens_basi.replace('#item+', '#date+')
            val2 = re.sub('\+ix_iso8601v(.*)?\+', '+', referens)
            # return referens_basi.replace('#item+', '#date+')
            return val2

        if caput_item == '#indicator+date':
            basi = referens_basi.replace('#item+', '#date+')
            val2 = re.sub('\+ix_iso8601v(.*)?\+', '+', basi)
            # return referens_basi.replace('#item+', '#date+')
            return val2
        else:
            raise SyntaxError(f'caput_item [{caput_item}]?')

    def _no1lize(self, caput: list):
        resultatum = []
        for res in caput:
            if not res:
                resultatum.append('')
                continue

            for ix_item, rdf_t_item in DATA_HXLTM_CASTTYPE.items():
                if res.find(ix_item) > -1 and res.find(rdf_t_item) == -1:
                    res = res + '+' + rdf_t_item
                # pass

            res = hxltm_hashtag_ix_ad_rdf(res)
            resultatum.append(res)
            continue

            _done = False
            for _ht_novo, _ht_retest in DATA_NO1_DE_HXLTM_GENERIC.items():

                if isinstance(_ht_retest, str) and _ht_retest == res:
                    resultatum.append(_ht_novo)
                    _done = True
                    break

                _resultatum = re.match(_ht_retest, res)
                if not _resultatum:
                    continue
                _vars = _resultatum.groupdict()

                # print(res, _resultatum, _vars)
                if _vars and len(_vars.keys()) > 0:
                    _vars['trivio'] = self.rdf_trivio
                    resultatum.append(_ht_novo.format_map(_vars))
                else:
                    resultatum.append(_ht_novo)
                _done = True
                break

            if _done is True:
                continue

            # Let at is is
            resultatum.append(res)

            # resultatum.append(
            #     '#meta+rem+i_qcc+is_zxxx+{0}'.format(
            #         res.lower().strip().replace(
            #             ' ', '').replace('-', '_').replace(
            #                 '#', '').replace('+', '_'))
            # )
        return resultatum

    def _skip_line(self, line: list) -> bool:

        # return False

        for rule in self._skipLineMetaCsv:
            if 'not_in' in rule:
                # for r_n_item in rule['not_in']:
                if line[rule['index']] not in rule['not_in']:
                    return True
                # return False
            # Most basic, just check if index exist at all not evaluate to empy
            elif not line[rule['index']] or \
                    len(line[rule['index']].strip()) == 0:
                return True
        return False

    def de_csv_ad_csvnorm(
            self, fonti: str, objetivum: str, caput_initiali: list):
        # print("TODO de_csv_ad_csvnorm")
        with open(objetivum, 'w') as _objetivum:
            with open(fonti, 'r') as _fons:
                _csv_reader = csv.reader(_fons)
                _csv_writer = csv.writer(_objetivum)
                started = False
                started_2 = False
                strip_last = None
                for linea in _csv_reader:

                    if not started:
                        if linea and linea[0].strip() in caput_initiali:
                            started = True
                            strip_last = len(linea[-1]) == 0
                            # if self.objectivum_transformationi == \
                            #         'annus-recenti':
                            #     linea.append('indicator value')
                            #     linea.append('indicator date')
                            self._caput = linea
                        else:
                            continue
                    if strip_last:
                        linea.pop()

                    # if self.objectivum_transformationi == 'annus-recenti':
                    # if self.objectivum_transformationi and \
                    #     self.objectivum_transformationi.startswith(
                    #         'annus-recenti'):
                    if self.objectivum_transformationi and \
                            ('annus-recenti' in self.objectivum_transformationi or
                                'annus-recenti-exclusivo' in self.objectivum_transformationi):
                        if started_2 is False:
                            started_2 = True
                            # print('   >> caput part')
                            linea.append('indicator value')
                            linea.append('indicator date')
                            self._caput = linea
                        else:
                            annus_recenti = self._linea_annus_recenti(
                                self._caput,
                                linea
                            )
                            linea.extend(annus_recenti)

                    _csv_writer.writerow(linea)

        # print("TODO")
    def de_csvnorm_ad_hxl(
            self, fonti: str, objetivum, callback: Type['function'] = None):
        # print("TODO de_csv_ad_csvnorm", self._skipLineMetaCsv)
        with open(objetivum, 'w') as _objetivum:
            with open(fonti, 'r') as _fons:
                _csv_reader = csv.reader(_fons)
                _csv_writer = csv.writer(_objetivum)
                started = False
                for linea in _csv_reader:
                    if not started:
                        started = True
                        caput = self._hxlize_dummy(linea)
                        self._caput = caput
                        _csv_writer.writerow(self._hxlize_dummy(linea))
                        # if callback is not None:
                        #     callback(qself=self, caput=caput)
                        continue
                    if not self._skip_line(linea):
                        _csv_writer.writerow(linea)

    def de_hxl_ad_hxltm(
        self, fonti: str,
        objetivum: str,
        hxl_vocab: bool = False
    ):
        index_linea = 0
        index_ix_xyadhxltrivio = -1
        codicem_inconito = False
        with open(objetivum, 'w') as _objetivum:
            with open(fonti, 'r') as _fons:
                _csv_reader = csv.reader(_fons)
                _csv_writer = csv.writer(_objetivum)
                started = False
                for linea in _csv_reader:
                    if not started:
                        started = True
                        caput = self._hxltmize(linea)
                        if '#item+conceptum+codicem' not in caput:
                            codicem_inconito = True
                            caput.insert(0, '#item+conceptum+codicem')
                        if hxl_vocab is True and \
                                '#item+rem+i_qcc+is_zxxx+ix_xyadhxltrivio' \
                                not in caput:
                            for _p in self._hxlPivotCode:
                                if _p in caput:
                                    # _index_ref = caput.index(self._hxlPivotCode)
                                    _index_ref = caput.index(_p)
                                    break
                            index_ix_xyadhxltrivio = _index_ref + 1
                            caput.insert(
                                index_ix_xyadhxltrivio,
                                '#item+rem+i_qcc+is_zxxx+ix_xyadhxltrivio')

                            # Since we injected new artificial table, lets
                            # increment self._skipHXLTMIndex)
                            if len(self._skipHXLTMIndex) > 0:
                                _old = self._skipHXLTMIndex
                                self._skipHXLTMIndex = []
                                for _val in _old:
                                    self._skipHXLTMIndex.append(_val + 1)

                        self._caput = caput
                        # if self.objectivum_transformationi == \
                        #     'annus-recenti-exclusivo' and \
                        #         len(self._skipHXLTMIndex) > 0:
                        if self.objectivum_transformationi and \
                            'annus-recenti-exclusivo' in self.objectivum_transformationi and \
                                len(self._skipHXLTMIndex) > 0:
                            # raise ValueError('teste', self._skipHXLTMIndex)
                            _caput_new = []
                            for idx, val in enumerate(caput):
                                if idx not in self._skipHXLTMIndex:
                                    _caput_new.append(val)
                            caput = _caput_new
                            # _caput_old = caput
                        _csv_writer.writerow(caput)
                        continue
                    if codicem_inconito is True:
                        # index_linea += 1
                        # linea.insert(0, str(index_linea))
                        # _v = self._codicem(index_linea, index_linea)

                        # Brute force whathever is on first 3 columns
                        _pseudo_hash = ''
                        for i in range(2):
                            _pseudo_hash += linea[i]
                            _v = self._codicem(linea[i], strictum=True)
                            if _v is not None:
                                break
                        if _v is None:
                            index_linea += 1
                            # _v = self._codicem(
                            #     False, index=index_linea, strictum=False)
                            # raise ValueError(caput)
                            # caput will be off-by-one on this check
                            if caput[2].find('code'):
                                _v = self._codicem(
                                    linea[1], index=index_linea, strictum=False)
                            elif caput[1].find('code'):
                                _v = self._codicem(
                                    linea[0], index=index_linea, strictum=False)
                            else:
                                _v = self._codicem(
                                    False, index=index_linea, strictum=False)

                        linea.insert(0, _v)
                    if index_ix_xyadhxltrivio > -1:
                        _v_refs = linea[index_ix_xyadhxltrivio - 1]

                        # Special case: if asked hxlize-urn-worldbank, here
                        # we pre-populate DATA_HXL_DE_CSV_REGEX
                        if self.objectivum_transformationi and \
                            'hxlize-urn-worldbank' in self.objectivum_transformationi and \
                                len(self._skipHXLTMIndex) > 0:
                            data_hxl_de_csv_regex_ex_urn(_v_refs)

                        _v_novo_parts = self._hxlPivot[_v_refs][1]
                        _v_novo_parts = sorted(_v_novo_parts)
                        _v = '+'.join(_v_novo_parts)
                        # _v = "@todo"
                        linea.insert(index_ix_xyadhxltrivio, _v)

                    # if self.objectivum_transformationi == \
                    #     'annus-recenti-exclusivo' and \
                    #         len(self._skipHXLTMIndex) > 0:
                    if self.objectivum_transformationi and \
                        'annus-recenti-exclusivo' in self.objectivum_transformationi and \
                            len(self._skipHXLTMIndex) > 0:

                        _linea_new = []
                        for idx, val in enumerate(linea):
                            if idx not in self._skipHXLTMIndex:
                                _linea_new.append(val)
                        linea = _linea_new

                    _csv_writer.writerow(linea)

    def de_hxltm_ad_hxltm_wide(
        self, fonti: str,
        objetivum: str
    ):
        """de_hxltm_ad_hxltm_wide

        @see https://en.wikipedia.org/wiki/Wide_and_narrow_data

        Args:
            fonti (str): _description_
            objetivum (str): _description_
        """

        # data_sorted = self._data_sort(fonti)

        if '#item+rem+i_qcc+is_zxxx+ix_xyadhxltrivio' in self._caput:
            data_sorted = hxltm__data_sort(
                fonti, ['#item+rem+i_qcc+is_zxxx+ix_xyadhxltrivio'])

            if self.hxltm_wide_indicators:
                indicator_index = data_sorted[0].index(
                    '#meta+rem+i_qcc+is_zxxx+indicator_code')

                data_novo = []
                for linea in data_sorted[1:]:
                    if linea[indicator_index] in self.hxltm_wide_indicators:
                        data_novo.append(linea)

                # print(len(data_novo))
                # print(len(data_sorted[1:]))
                # raise ValueError(indicator_index, data_sorted[0], self.hxltm_wide_indicators, data_novo[0])
                data_sorted = [data_sorted[0]]
                data_sorted.extend(data_novo)
        else:
            data_sorted = hxltm__data_sort(fonti)

        is_hotfix_need = False
        if self.objectivum_transformationi and \
                'annus-recenti-exclusivo' in self.objectivum_transformationi:
            is_hotfix_need = True

        caput, data = hxltm__data_pivot_wide(
            data_sorted[0], data_sorted[1:], is_hotfix_need)

        # # print(data_sorted[0:10])
        # print('is_hotfix_need', is_hotfix_need)
        # print('')
        # print('    > data_sorted sample')
        # print(len(data_sorted[0:10][0]), data_sorted[0:10][0])
        # print(len(data_sorted[0:10][1]), data_sorted[0:10][1])
        # print('')
        # print('')
        # print('')
        # # print(caput, data[0:10])
        # print('    >>>> (final caput, data) sample')
        # print(len(caput), caput)
        # print(len(data[0]), data[0])
        # print('')

        # raise NotImplementedError

        with open(objetivum, 'w') as _objetivum:
            # with open(fonti, 'r') as _fons:
            _csv_writer = csv.writer(_objetivum)
            _csv_writer.writerow(caput)
            for linea in data:
                _csv_writer.writerow(linea)

    def de_hxltm_ad_no1(self, fonti: str, objetivum: str):

        numerordinatio_inconito = False
        codicem_index = -1
        with open(objetivum, 'w') as _objetivum:
            with open(fonti, 'r') as _fons:
                _csv_reader = csv.reader(_fons)
                _csv_writer = csv.writer(_objetivum)
                started = False
                for linea in _csv_reader:
                    if not started:
                        started = True
                        caput = self._no1lize(linea)
                        if '#item+conceptum+numerordinatio' not in caput:
                            numerordinatio_inconito = True
                            codicem_index = caput.index(
                                '#item+conceptum+codicem')
                            caput.insert(0, '#item+conceptum+numerordinatio')
                        self._caput = caput
                        _csv_writer.writerow(caput)
                        continue
                    if numerordinatio_inconito is True:
                        linea.insert(0, '{0}:{1}'.format(
                            self.numerordinatio_praefixo, linea[codicem_index]))
                    _csv_writer.writerow(linea)


class DataScrappingInterpol(DataScrapping):

    link_fonti: str = 'https://interpol.api.bund.dev/'

    def __init__(self, methodus: str, objectivum_formato: str, archivum_objetivum: str):

        _allowed_types = [
            'red', 'yellow', 'un'
        ]

        if methodus not in _allowed_types:
            raise ValueError(
                'objectivum_formato [{0}]?'.format(methodus))

        self.methodus = methodus
        self.objectivum_formato = objectivum_formato
        if not archivum_objetivum:
            raise ValueError('--archivum-objetivum ?')
        self.archivum_objetivum = archivum_objetivum

        self.data_notices = []
        self.data_notices_tabular = []

        self._resultPerPage = 160
        self._page = 1
        self._total = None
        self._done = False

        self._datafields = [
            'entity_id',
            'un_reference',
            'name',
            'forename',
            'date_of_birth',
            'nationalities',
            # '_links.self',
        ]
        self._datafields_date = [
            'date_of_birth'
        ]

    def _quod_date(self, textum) -> str:
        if not textum:
            return textum
        if len(textum) == 0 or textum.find('/') == -1:
            return textum
        return textum.replace('/', '-')

    def _quod_url(self) -> str:
        url = 'https://ws-public.interpol.int/' + \
            'notices/v1/{0}?resultPerPage={1}'.format(
                self.methodus, self._resultPerPage)
        return url

    def _quod_request(self) -> str:
        _url = self._quod_url()
        print(_url)
        r = requests.get(_url)
        print(r)

        result = r.json()

        self._total = result['total']
        self.data_notices.extend(
            result['_embedded']['notices']
        )

        if result['_links']['self']['href'] == result['_links']['last']['href']:
            self._done = True

        return result

    def _praeparatio_tabulae(self) -> str:

        caput = []
        _caput = set()

        for item in self.data_notices:
            for _maybe in self._datafields:
                if _maybe in item:
                    _caput.add(_maybe)

        for _maybe in self._datafields:
            if _maybe in _caput:
                caput.append(_maybe)

        caput.append('_links.self')

        if self.objectivum_formato == 'hxltm':
            self.data_notices_tabular.append(self._hxlize_dummy(caput))
        else:
            self.data_notices_tabular.append(caput)

        for item in self.data_notices:
            linea = []
            for _maybe in caput:
                if _maybe in item:
                    if isinstance(item[_maybe], list):
                        linea.append('|'.join(item[_maybe]))
                    else:
                        if _maybe in self._datafields_date:
                            linea.append(self._quod_date(
                                item[_maybe]
                            ))
                        else:
                            linea.append(item[_maybe])
                elif _maybe == '_links.self':
                    linea.append(item['_links']['self']['href'])
                else:
                    linea.append('')

            # if item['_links']['self']['href']

            # linea.append(item['_links']['self']['href'])

            self.data_notices_tabular.append(linea)

        return True

    def imprimere(self, formatum: str = None) -> list:

        if self.objectivum_formato == 'link-fonti':
            print(self.link_fonti)
            return True

    def praeparatio(self):
        """praeparātiō

        Trivia:
        - praeparātiō, s, f, Nom., https://en.wiktionary.org/wiki/praeparatio
        """
        # return True
        if self.objectivum_formato == 'link-fonti':
            # print(self.link_fonti)
            return True

        # print('@TODO', __class__.__name__)

        self._init_temp()

        while (self._page == 1 and self._total == None) or self._done is False:
            # print(self._quod_request())
            self._quod_request()
            if self._done is True:
                print('DONE!')
                break
            print('sleep 10...')
            sleep(10)

        self._praeparatio_tabulae()
        print('')
        print('')
        print('')
        print('')
        # print(self.data_notices_tabular)

        with open(self.archivum_objetivum, "w") as write_file:
            for linea in self.data_notices_tabular:
                _writer = csv.writer(write_file)
                _writer.writerow(linea)

        print('saved at {0}'.format(self.archivum_objetivum))


class DataScrappingUNDATA(DataScrapping):
    def praeparatio(self):
        """praeparātiō

        Trivia:
        - praeparātiō, s, f, Nom., https://en.wiktionary.org/wiki/praeparatio
        """

        # pip install pandasdmx[cache]

        # Population per city and sex (Somewhat incomplete, but have CENSUS)
        # http://data.un.org/Data.aspx?d=POP&f=tableCode%3a240
        # http://data.un.org/Data.aspx?d=POP&f=tableCode%3a240&c=0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18&s=_countryEnglishNameOrderBy:asc,refYear:desc,areaCode:asc&v=1

        # import pandasdmx as sdmx
        estat = sdmx.Request('ESTAT')
        metadata = estat.datastructure('DSD_une_rt_a')
        print(metadata)

        for cl in 'CL_AGE', 'CL_UNIT':
            print(sdmx.to_pandas(metadata.codelist[cl]))
        resp = estat.data(
            'une_rt_a',
            key={'GEO': 'EL+ES+IE'},
            params={'startPeriod': '2007'},
        )
        data = resp.to_pandas(
            datetime={'dim': 'TIME_PERIOD', 'freq': 'FREQ'}).xs(
                'Y15-74', level='AGE', axis=1, drop_level=False)
        print(data.columns.names)
        print(data.columns.levels)

        print(data.loc[:, ('Y15-74', 'PC_ACT', 'T')])

        print('')
        print('')
        print('')
        print('UNSD')

        unsd = sdmx.Request('UNSD')
        print(unsd)
        # unsd = Request('UNSD')
        cat_response = unsd.categoryscheme()
        print(cat_response)
        # https://pandasdmx.readthedocs.io/en/v1.0/howto.html#use-category-schemes-to-explore-data
        print('UNSD all categories list')
        print(sdmx.to_pandas(cat_response.category_scheme.UNdata_Categories))
        # # print(cat_response.write().categoryscheme)
        # # dsd_id = unsd.categoryscheme().dataflow.NA_MAIN.structure.id
        # # dsd_response = unsd.datastructure(resource_id = dsd_id)
        # print('')
        # print('')
        # print('')
        # print('UNICEF')

        # unicef = sdmx.Request('UNICEF')
        # print(unicef)

        # @see https://pandasdmx.readthedocs.io/en/v1.0/example.html
        # @see https://pandasdmx.readthedocs.io/en/v1.0/walkthrough.html
        print('TODO')
        pass


class DataScrappingWorldbank(DataScrapping):

    methodus: str = 'SP.POP.TOTL'
    numerordinatio_praefixo: str = '999999:0'
    objectivum_formato: str = 'csv'
    # link_fonti: str = 'https://api.worldbank.org/v2/en/indicator/SP.POP.TOTL?downloadformat=excel'
    link_fonti: str = 'https://api.worldbank.org/v2/en/indicator/SP.POP.TOTL?downloadformat=csv'
    temp_fonti_csv: str = ''
    temp_fonti_csvnorm: str = ''
    temp_fonti_hxl: str = ''
    temp_fonti_hxltm: str = ''
    temp_fonti_hxltm_wide: str = ''
    temp_fonti_no1: str = ''

    # print('oioioi', self.dictionaria_codex )

    def imprimere(self, formatum: str = None) -> list:

        if self.objectivum_formato == 'link-fonti':
            print(self.link_fonti)
            return True

        fonti = self.temp_fonti_csvnorm
        if self.objectivum_formato == 'hxl':
            fonti = self.temp_fonti_hxl
        if self.objectivum_formato == 'hxltm':
            fonti = self.temp_fonti_hxltm
        if self.objectivum_formato == 'hxltm-wide':
            fonti = self.temp_fonti_hxltm_wide
        if self.objectivum_formato == 'no1':
            fonti = self.temp_fonti_no1

        with open(fonti, 'r') as _fons:
            _csv_reader = csv.reader(_fons)
            _csv_writer = csv.writer(sys.stdout)
            for linea in _csv_reader:
                _csv_writer.writerow(linea)

    def praeparatio(self):
        """praeparātiō

        Trivia:
        - praeparātiō, s, f, Nom., https://en.wiktionary.org/wiki/praeparatio
        """
        # return True

        if self.methodus in DATA_METHODUS['worldbank']:
            self.link_fonti = DATA_METHODUS['worldbank'][self.methodus][
                'download_url']
        else:
            self.link_fonti = 'https://api.worldbank.org/v2/en/indicator/{0}?downloadformat=csv'.format(
                self.methodus)

        if self.objectivum_formato == 'link-fonti':
            # print(self.link_fonti)
            return True
        # self.temp_fonti = '{0}/999999/0/{1}~{2}.xls'.format(
        #     NUMERORDINATIO_BASIM, __class__.__name__, self.methodus
        # )

        suffixus = self.methodus
        if self.methodus.startswith('file://'):
            suffixus = 'fromlocalfile'

        self._init_temp(suffixus=suffixus)

        # temp_fonti_zip = '{0}/999999/0/{1}~{2}.zip'.format(
        #     NUMERORDINATIO_BASIM, __class__.__name__, self.methodus
        # )
        # self.temp_fonti_csv = '{0}/999999/0/{1}~{2}.csv'.format(
        #     NUMERORDINATIO_BASIM, __class__.__name__, self.methodus
        # )
        # self.temp_fonti_csvnorm = '{0}/999999/0/{1}~{2}.norm.csv'.format(
        #     NUMERORDINATIO_BASIM, __class__.__name__, self.methodus
        # )
        # self.temp_fonti_hxl = '{0}/999999/0/{1}~{2}.hxl.csv'.format(
        #     NUMERORDINATIO_BASIM, __class__.__name__, self.methodus
        # )
        # self.temp_fonti_hxltm = '{0}/999999/0/{1}~{2}.tm.hxl.csv'.format(
        #     NUMERORDINATIO_BASIM, __class__.__name__, self.methodus
        # )
        # self.temp_fonti_hxltm_wide = '{0}/999999/0/{1}~{2}~WIDE.tm.hxl.csv'.format(
        #     NUMERORDINATIO_BASIM, __class__.__name__, self.methodus
        # )
        # self.temp_fonti_no1 = '{0}/999999/0/{1}~{2}.no1.tm.hxl.csv'.format(
        #     NUMERORDINATIO_BASIM, __class__.__name__, self.methodus
        # )

        self.temp_fonti_csv = '{0}/999999/0/{1}~{2}.csv'.format(
            NUMERORDINATIO_BASIM, __class__.__name__, suffixus
        )
        # self.temp_fonti_csv = self._temp['csv']
        self.temp_fonti_csvnorm = self._temp['csv']
        self.temp_fonti_hxl = self._temp['hxl']
        self.temp_fonti_hxltm = self._temp['hxltm']
        self.temp_fonti_hxltm_wide = self._temp['hxltm_wide']
        self.temp_fonti_no1 = self._temp['no1']

        # raise ValueError(self.methodus)

        if not self.methodus.startswith('file://'):

            temp_fonti_zip = self._temp['__source_zip__']

            if not exists(temp_fonti_zip):
                # Download to local cache if alreayd there
                r = requests.get(self.link_fonti)
                with open(temp_fonti_zip, 'wb') as f:
                    f.write(r.content)
            # else:
            #     print('already cached', temp_fonti_zip)

            # zip file handler
            zip = zipfile.ZipFile(temp_fonti_zip)
            data_file_main = ''
            for _res in zip.namelist():
                if _res.lower().find('meta') > -1:
                    continue
                if _res.lower().startswith('api_'):
                    data_file_main = _res
            # list available files in the container
            # print(zip.namelist())

            # extract a specific file from the zip container
            f = zip.open(data_file_main)

            # save the extraced file
            content = f.read()
            # f = open(self.temp_fonti_csv, 'wb')
            f = open(self._temp['__source_main_csv__'], 'wb')
            f.write(content)
            f.close()

            self.de_csv_ad_csvnorm(
                self._temp['__source_main_csv__'], self._temp['csv'], [
                    'Country Name', 'Country Code'
                ]
            )
        else:
            source = self.methodus.replace('file://', '')
            # raise ValueError(source, self.temp_fonti_csv)
            # shutil.copyfile(source, self.temp_fonti_csv)

            self.de_csv_ad_csvnorm(
                source, self._temp['csv'], [
                    'Country Name', 'Country Code'
                ]
            )

            # # We copy the file here since the default behavior of self.__del__
            # # would delete the file
            # shutil.copyfile(source, self.temp_fonti_csvnorm)

            # # We still need to mimic self.de_csv_ad_csvnorm() which
            # # would cache elf._caput
            # with open(self.temp_fonti_csvnorm) as _fons:
            #     # first_line = f.readline()
            #     _csv_reader = csv.reader(_fons)
            #     self._caput = next(_csv_reader)

            # from genericpath import exists
            # raise ValueError(source, self.temp_fonti_csv, exists(
            #     source), exists(self.temp_fonti_csv))

        if self.objectivum_formato in ['hxl', 'hxltm', 'hxltm-wide', 'no1']:
            # raise ValueError(self._caput)
            _indicator_code_index = self._caput.index('Indicator Code')

            # If the output format is HXL, we only require indicator column
            # to not the empty
            if self.objectivum_formato == 'hxl' or \
                (self.objectivum_transformationi and 'hxlize-urn-worldbank'
                    in self.objectivum_transformationi):
                self._skipLineMetaCsv.append(
                    {
                        'index': _indicator_code_index
                    }
                )
            else:
                self._skipLineMetaCsv.append(
                    {
                        'index': _indicator_code_index,
                        'not_in': DATA_HXL_DE_CSV_REGEX['worldbank'].keys()
                    }
                )
            self.de_csvnorm_ad_hxl(
                self._temp['csv'], self._temp['hxl']
            )

        if self.objectivum_formato in ['hxltm',  'hxltm-wide', 'no1']:
            hxl_vocab = False
            # if self.methodus == 'health':
            if self.methodus in DATA_METHODUS['worldbank'] or \
                    self.methodus.startswith('file://'):
                self._hxlPivot = DATA_HXL_DE_CSV_REGEX['worldbank']
                hxl_vocab = True

            self.de_hxl_ad_hxltm(
                self._temp['hxl'], self._temp['hxltm'], hxl_vocab=hxl_vocab
            )

            # raise ValueError(self._temp['hxltm'])

        if self.objectivum_formato == 'hxltm-wide':
            hxl_vocab = False
            # if self.methodus == 'health':
            #     self._hxlPivot = DATA_HXL_DE_CSV_REGEX['worldbank']
            #     hxl_vocab = True
            self.de_hxltm_ad_hxltm_wide(
                self._temp['hxltm'], self._temp['hxltm_wide']
            )

        # We also generate wide data implicitly if result needs it
        if self.objectivum_formato == 'no1' and \
                ('#item+rem+i_qcc+is_zxxx+ix_xyadhxltrivio' in self._caput):
            hxl_vocab = False
            # if self.methodus == 'health':
            #     self._hxlPivot = DATA_HXL_DE_CSV_REGEX['worldbank']
            #     hxl_vocab = True
            self.de_hxltm_ad_hxltm_wide(
                self._temp['hxltm'], self._temp['hxltm_wide']
            )

            self.de_hxltm_ad_no1(
                self._temp['hxltm_wide'], self._temp['no1']
            )

        elif self.objectivum_formato in ['no1']:
            self.de_hxltm_ad_no1(
                self._temp['hxltm'], self._temp['no1']
            )
        else:
            SyntaxError('{}??'.format(self.objectivum_formato))


if __name__ == "__main__":

    est_cli = Cli()
    args = est_cli.make_args()

    est_cli.execute_cli(args)
