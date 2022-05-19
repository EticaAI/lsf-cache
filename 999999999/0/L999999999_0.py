# ==============================================================================
#
#          FILE:  L999999999_0.py
#
#         USAGE:  It's a python library
#                    from L999999999_0 import (
#                        hxltm_carricato,
#                        qhxl_hxlhashtag_2_bcp47,
#                        # (...)
#                    )
#
#   DESCRIPTION:  Common library for 999999999_*.py cli scripts
#
#       OPTIONS:  ---
#
#  REQUIREMENTS:  - python3
#                   - pip install openpyxl
#          BUGS:  ---
#         NOTES:  ---
#       AUTHORS:  Emerson Rocha <rocha[at]ieee.org>
# COLLABORATORS:  ---
#       COMPANY:  EticaAI
#       LICENSE:  Public Domain dedication or Zero-Clause BSD
#                 SPDX-License-Identifier: Unlicense OR 0BSD
#       VERSION:  v1.0.0
#       CREATED:  2022-05-18 19:52 UTC based on 999999999_10263485.py
#      REVISION:  ---
# ==============================================================================
"""Common library for 999999999_*.py cli scripts
"""


import csv
# import importlib
import os
# from pathlib import Path
import re
import sys
import datetime
from typing import (
    List,
    Type,
    Union
)
import yaml

from openpyxl import (
    load_workbook
)

# pylint --disable=W0511,C0103,C0302,C0116 ./999999999/0/L999999999_0.py

# SYSTEMA_SARCINAE = str(Path(__file__).parent.resolve())
# PROGRAMMA_SARCINAE = str(Path().resolve())
# ARCHIVUM_CONFIGURATIONI_L999999999_0 = [
#     PROGRAMMA_SARCINAE + '/L999999999_0.meta.yml',
#     SYSTEMA_SARCINAE + '/L999999999_0.meta.yml',
# ]
# ARCHIVUM_CONFIGURATIONI_DEFALLO = [
#     # SYSTEMA_SARCINAE + '/' + NOMEN + '.meta.yml',
#     # PROGRAMMA_SARCINAE + '/' + NOMEN + '.meta.yml',
#     PROGRAMMA_SARCINAE + '/{{PROGRAMMA}}.meta.yml',
#     SYSTEMA_SARCINAE + '/{{PROGRAMMA}}.meta.yml',
# ]
NUMERORDINATIO_BASIM = os.getenv('NUMERORDINATIO_BASIM', os.getcwd())
NUMERORDINATIO_DEFALLO = int(os.getenv('NUMERORDINATIO_DEFALLO', '60'))  # �
NUMERORDINATIO_MISSING = "�"
VENANDUM_INSECTUM = bool(os.getenv('VENANDUM_INSECTUM', ''))


# def _dictionaria_linguarum():
#     # importlib.import_module('', package=None)
#     L1603_1_51 = importlib.import_module('1603_1_51', package='1603_1_1')

#     return L1603_1_51.DictionariaLinguarum()

def bcp47_langtag(
        rem: str,
        clavem: Type[Union[str, list]] = None,
        strictum: bool = True
) -> dict:
    """Public domain python function to process BCP47 langtag
    The BCP47Langtag is an public domain python function to
    aid parsing of the IETF BCP 47 language tag. It implements the syntactic
    analysis of RFC 5646 and does not require lookup tables which makes
    it friendly for quick analysis.
    Limitations:
       - subtags such as "-t-" and "-u- '' are not parsed on this current
         version. They are treated as generic BCP47 extensions.
       - The Language-Tag_normalized result would still need external data
         lookups to stricter normalization. Yet BCP47Langtag can be used as
         the very first step to analyze a language tag which is viable to port
         across programming languages.
       - The default behavior is to throw exceptions with at least some types
         of syntactic errors, a feature which can be disabled yet reasoning is
         exposed with _error. However, already very malformated can have
        further bugs which different programming implementations do not need
        to be consistent with each other.
    Versions in other programming languages:
       The initial author encourages versions to other programming languages or
       libraries or tools which make use of this. No need to ask permission
       upfront and there is no problem with using other licenses
       than public domain.
    Changelog:
       - 2021-11-22: Partial implementation of BCP47 (RFC 5646)
       - 2021-01-02: Fixes on Language-Tag_normalized (discoversed when ported
                     JavaScript version was created)
    Args:
        rem (str):                       The BCP47 langtag
        clavem (Type[Union[str, list]]): Key (string) for specific value or keys
                                         (list) to return a dict (optional)
        strictum (bool):                 Throw exceptions. False replace values
                                        with False (optional)
    Returns:
        dict: Python dictionary. None means not found. False means the feature
                                 is not implemented
    Author:
        Emerson Rocha <rocha(at)ieee.org>
    License:
        SPDX-License-Identifier: Unlicense OR 0BSD
    -------------
    The syntax of the language tag in ABNF [RFC5234] is:
    Language-Tag  = langtag             ; normal language tags
                / privateuse          ; private use tag
                / grandfathered       ; grandfathered tags
    langtag       = language
                    ["-" script]
                    ["-" region]
                    *("-" variant)
                    *("-" extension)
                    ["-" privateuse]
    language      = 2*3ALPHA            ; shortest ISO 639 code
                    ["-" extlang]       ; sometimes followed by
                                        ; extended language subtags
                / 4ALPHA              ; or reserved for future use
                / 5*8ALPHA            ; or registered language subtag
    extlang       = 3ALPHA              ; selected ISO 639 codes
                    *2("-" 3ALPHA)      ; permanently reserved
    script        = 4ALPHA              ; ISO 15924 code
    region        = 2ALPHA              ; ISO 3166-1 code
                / 3DIGIT              ; UN M.49 code
    variant       = 5*8alphanum         ; registered variants
                / (DIGIT 3alphanum)
    extension     = singleton 1*("-" (2*8alphanum))
                                        ; Single alphanumerics
                                        ; "x" reserved for private use
    singleton     = DIGIT               ; 0 - 9
                / %x41-57             ; A - W
                / %x59-5A             ; Y - Z
                / %x61-77             ; a - w
                / %x79-7A             ; y - z
    privateuse    = "x" 1*("-" (1*8alphanum))
    grandfathered = irregular           ; non-redundant tags registered
                / regular             ; during the RFC 3066 era
    irregular     = "en-GB-oed"         ; irregular tags do not match
                / "i-ami"             ; the 'langtag' production and
                / "i-bnn"             ; would not otherwise be
                / "i-default"         ; considered 'well-formed'
                / "i-enochian"        ; These tags are all valid,
                / "i-hak"             ; but most are deprecated
                / "i-klingon"         ; in favor of more modern
                / "i-lux"             ; subtags or subtag
                / "i-mingo"           ; combination
                / "i-navajo"
                / "i-pwn"
                / "i-tao"
                / "i-tay"
                / "i-tsu"
                / "sgn-BE-FR"
                / "sgn-BE-NL"
                / "sgn-CH-DE"
    regular       = "art-lojban"        ; these tags match the 'langtag'
                / "cel-gaulish"       ; production, but their subtags
                / "no-bok"            ; are not extended language
                / "no-nyn"            ; or variant subtags: their meaning
                / "zh-guoyu"          ; is defined by their registration
                / "zh-hakka"          ; and all of these are deprecated
                / "zh-min"            ; in favor of a more modern
                / "zh-min-nan"        ; subtag or sequence of subtags
                / "zh-xiang"
    alphanum      = (ALPHA / DIGIT)     ; letters and numbers
    -------------
    Most tests use examples from https://tools.ietf.org/search/bcp47 and
    https://github.com/unicode-org/cldr/blob/main/tools/cldr-code
    /src/main/resources/org/unicode/cldr/util/data/langtagTest.txt
    Exemplōrum gratiā (et Python doctest, id est, testum automata):
    (run with python3 -m doctest myscript.py)
    >>> bcp47_langtag('pt-Latn-BR', 'language')
    'pt'
    >>> bcp47_langtag('pt-Latn-BR', 'script')
    'Latn'
    >>> bcp47_langtag('pt-Latn-BR', 'region')
    'BR'
    >>> bcp47_langtag('de-CH-1996', 'variant')
    ['1996']
    >>> bcp47_langtag('x-fr-CH', ['language', 'region', 'privateuse'])
    {'language': None, 'region': None, 'privateuse': ['fr', 'CH']}
    >>> bcp47_langtag('i-klingon', 'grandfathered')
    'i-klingon'
    >>> bcp47_langtag('zh-min-nan', 'language')
    'zh'
    >>> bcp47_langtag('zh-min-nan', 'variant')
    ['min-nan']
    >>> bcp47_langtag('es-419', 'region')
    '419'
    >>> bcp47_langtag('en-oxendict', 'variant') # Oxford English Dictionary
    ['oxendict']
    >>> bcp47_langtag('zh-pinyin', 'variant') # Pinyin romanization
    ['pinyin']
    >>> bcp47_langtag('zh-pinyin', 'script') # Limitation: cannot infer Latn
    >>> bcp47_langtag('en-a-bbb-x-a-ccc', 'privateuse')
    ['a', 'ccc']
    >>> bcp47_langtag('en-a-bbb-x-a-ccc', 'extension')
    {'a': 'bbb'}
    >>> bcp47_langtag('tlh-a-b-foo', '_error')
    Traceback (most recent call last):
    ...
    ValueError: Errors for [tlh-a-b-foo]: extension [a] empty
    >>> bcp47_langtag('tlh-a-b-foo', '_error', False)
    ['extension [a] empty']
    >>> bcp47_langtag(
    ... 'zh-Latn-CN-variant1-a-extend1-x-wadegile-private1',
    ... ['variant', 'extension', 'privateuse'])
    {'variant': ['variant1'], 'extension': {'a': 'extend1'}, \
'privateuse': ['wadegile', 'private1']}
    >>> bcp47_langtag(
    ... 'en-Latn-US-lojban-gaulish-a-12345678-ABCD-b-ABCDEFGH-x-a-b-c-12345678')
    {'Language-Tag': \
'en-Latn-US-lojban-gaulish-a-12345678-ABCD-b-ABCDEFGH-x-a-b-c-12345678', \
'Language-Tag_normalized': \
'en-Latn-US-lojban-gaulish-a-12345678-ABCD-b-ABCDEFGH-x-a-b-c-12345678', \
'language': 'en', 'script': 'Latn', 'region': 'US', \
'variant': ['lojban', 'gaulish'], \
'extension': {'a': '12345678-ABCD', 'b': 'ABCDEFGH'}, \
'privateuse': ['a', 'b', 'c', '12345678'], \
'grandfathered': None, '_unknown': [], '_error': []}

    # BCP47: "Example: The language tag "en-a-aaa-b-ccc-bbb-x-xyz" is in
    # canonical form, while "en-b-ccc-bbb-a-aaa-X-xyz" is well-formed (...)
    >>> bcp47_langtag(
    ... 'en-b-ccc-bbb-a-aaa-X-xyz')
    {'Language-Tag': 'en-b-ccc-bbb-a-aaa-X-xyz', \
'Language-Tag_normalized': 'en-a-aaa-b-ccc-bbb-x-xyz', \
'language': 'en', 'script': None, 'region': None, 'variant': [], \
'extension': {'a': 'aaa', 'b': 'ccc-bbb'}, 'privateuse': ['xyz'], \
'grandfathered': None, '_unknown': [], '_error': []}
    """
    # For sake of copy-and-paste portability, we ignore a few pylints:
    # pylint: disable=too-many-branches,too-many-statements,too-many-locals
    result = {
        # The input Language-Tag, _as it is_
        'Language-Tag': rem,
        # The Language-Tag normalized syntax, if no errors
        'Language-Tag_normalized': None,
        'language': None,
        'script': None,
        'region': None,
        'variant': [],
        'extension': {},   # Example {'a': ['bbb', 'ccc'], 'd': True}
        'privateuse': [],  # Example: ['wadegile', 'private1']
        'grandfathered': None,
        '_unknown': [],
        '_error': [],
    }

    skip = 0

    if not isinstance(rem, str) or len(rem) == 0:
        result['_error'].append('Empty/wrong type')
        skip = 1
    else:
        rem = rem.replace('_', '-').strip()

    # The weird tags first: grandfathered/irregular
    if rem in [
        'en-GB-oed', 'i-ami', 'i-bnn', 'i-default', 'i-enochian',
        'i-hak', 'i-klingon', 'i-lux', 'i-ming', 'i-navajo', 'i-pwn',
            'i-tao', 'i-tay', 'i-tsu', 'sgn-BE-FR', 'sgn-BE-NL', 'sgn-CH-DE']:
        # result['langtag'] = None
        result['language'] = rem.lower()
        result['grandfathered'] = rem
        skip = 1
    # The weird tags first: grandfathered/regular
    if rem in [
            'art-lojban', 'cel-gaulish', 'no-bok', 'no-nyn', 'zh-guoyu',
            'zh-hakka', 'zh-min', 'zh-min-nan', 'zh-xiang']:

        parts_r = rem.split('-')
        # result['langtag'] = None
        result['language'] = parts_r.pop(0).lower()
        result['variant'].append('-'.join(parts_r).lower())
        result['grandfathered'] = rem
        skip = 1

    parts = rem.split('-')
    leftover = []

    deep = 0
    while len(parts) > 0 and skip == 0 and deep < 100:
        deep = deep + 1

        # BCP47 can start with private tag, without language at all
        if parts[0].lower() == 'x':
            parts.pop(0)
            while len(parts) > 0:
                result['privateuse'].append(parts.pop(0))
            break

        # BCP47 extensions start with one US-ASCII letter.
        if len(parts[0]) == 1 and parts[0].isalpha():
            if parts[0].isalpha() == 'i':
                result['_error'].append('Only grandfathered can use i-')

            extension_key = parts.pop(0).lower()
            if len(parts) == 0 or len(parts[0]) == 1:
                # BCP47 2.2.6. : "Each singleton MUST be followed by at least
                # one extension subtag (...)
                # result['extension'][extension_key] = [None]
                result['extension'][extension_key] = {}
                result['_error'].append(
                    'extension [' + extension_key + '] empty')
                continue

            result['extension'][extension_key] = ''
            while len(parts) > 0 and len(parts[0]) != 1:
                # Extensions may have more strict rules than -x-
                # @see https://datatracker.ietf.org/doc/html/rfc6497 (-t-)
                # @see https://datatracker.ietf.org/doc/html/rfc6067 (-u-)

                # Let's avoid atempt to lowercase extensions, since this is not
                # not explicity on BCP47 for unknow extensions
                # result['extension'][extension_key] = \
                #     result['extension'][extension_key] + \
                #     '-' + parts.pop(0).lower()
                result['extension'][extension_key] = \
                    result['extension'][extension_key] + \
                    '-' + parts.pop(0)

                result['extension'][extension_key] = \
                    result['extension'][extension_key].strip('-')

            continue

        # for part in parts:
        if result['language'] is None:
            if parts[0].isalnum() and len(parts[0]) == 2 or len(parts[0]) == 3:
                result['language'] = parts[0].lower()
            else:
                result['language'] = False
                result['_error'].append('language?')
            parts.pop(0)
            continue

        # Edge case to test for numeric in 4 (not 3): 'de-CH-1996'
        if len(parts[0]) == 4 and parts[0].isalpha() \
                and result['script'] is None:
            # if parts[0].isalpha() and result['script'] is None:
            if parts[0].isalpha():
                if result['region'] is None and len(result['privateuse']) == 0:
                    result['script'] = parts[0].capitalize()
                else:
                    result['script'] = False
                    result['_error'].append('script after region/privateuse')
            else:
                result['script'] = False
                result['_error'].append('script?')
            parts.pop(0)
            continue

        # Regions, such as ISO 3661-1, like BR
        if len(parts[0]) == 2 and result['region'] is None:
            if parts[0].isalpha():
                result['region'] = parts[0].upper()
            else:
                result['region'] = False
                result['_error'].append('region?')
            parts.pop(0)
            continue

        # Regions, such as ISO 3661-1, like 076
        if len(parts[0]) == 3 and result['region'] is None:
            if parts[0].isnumeric():
                result['region'] = parts.pop(0)
            else:
                result['region'] = False
                result['_error'].append('region?')
                parts.pop(0)
            continue

        if len(result['extension']) == 0 and len(result['privateuse']) == 0:
            # 2.2.5. Variant Subtags
            #   4.1 "Variant subtags that begin with a (US-ASCII)* letter
            #       (a-z, A-Z) MUST be at least five characters long."
            #   4.2 "Variant subtags that begin with a digit (0-9) MUST be at
            #       least four characters long."
            if parts[0][0].isalpha() and len(parts[0]) >= 5:
                result['variant'].append(parts.pop(0))
                continue
            if parts[0][0].isnumeric() and len(parts[0]) >= 4:
                result['variant'].append(parts.pop(0))
                continue

        leftover.append(parts.pop(0))

    result['_unknown'] = leftover

    # @TODO: maybe re-implement only for know extensions, like -t-, -u-, -h-
    # if len(result['extension']) > 0:
    #     extension_norm = {}
    #     # keys
    #     keys_sorted = sorted(result['extension'])
    #     # values
    #     for key in keys_sorted:
    #         extension_norm[key] = sorted(result['extension'][key])

    #     result['extension'] = extension_norm

    # Language-Tag_normalized
    if len(result['_error']) == 0:

        if result['grandfathered']:
            result['Language-Tag_normalized'] = result['grandfathered']
        else:
            norm = []
            if result['language']:
                norm.append(result['language'])
            if result['script']:
                norm.append(result['script'])
            if result['region']:
                norm.append(result['region'])
            if len(result['variant']) > 0:
                norm.append('-'.join(result['variant']))

            if len(result['extension']) > 0:
                #  TODO: maybe re-implement only for know extensions,
                #        like -t-, -u-, -h-. For now we're not trying to
                #        normalize ordering of unknow future extensions, BUT
                #        we sort key from different extensions
                sorted_extension = {}
                for key in sorted(result['extension']):
                    sorted_extension[key] = result['extension'][key]
                result['extension'] = sorted_extension

                for key in result['extension']:
                    if result['extension'][key][0] is None:
                        norm.append(key)
                    else:
                        norm.append(key)
                        # norm.extend(result['extension'][key])
                        norm.append(result['extension'][key])

            if len(result['privateuse']) > 0:
                norm.append('x-' + '-'.join(result['privateuse']))

            result['Language-Tag_normalized'] = '-'.join(norm)

    if strictum and len(result['_error']) > 0:
        raise ValueError(
            'Errors for [' + rem + ']: ' + ', '.join(result['_error']))

    if clavem is not None:
        if isinstance(clavem, str):
            return result[clavem]
        if isinstance(clavem, list):
            result_partial = {}
            for item in clavem:
                result_partial[item] = result[item]
            return result_partial
        raise TypeError(
            'clavem [' + str(type(clavem)) + '] != [str, list]')

    return result


class CodAbTabulae:
    """CodAbTabulae simple wrapper to work with raw P-Code/COD-AB tabular data

    - COD:
      - https://cod.unocha.org/
      - https://emergency.unhcr.org/entry/50306/common-operational-datasets-
        cods-and-fundamental-operational-datasets-fods
    - tabulae, f, s, dat./gen/, https://en.wiktionary.org/wiki/tabula
    - simplicī, m/f/n, s, dativus, https://en.wiktionary.org/wiki/simplex#Latin

    @TODO:
    - Check strategies to encode geo data in plain text.
      - https://giswiki.hsr.ch/GeoCSV
      -  https://github.com/hxl-team/HXL-Vocab/blob/master/Tools/static
         /hxl-geolocation-standard-draft.pdf
        - HXL circa 2012 already was using RDF to map information
      - https://www.ogc.org/standards/geosparql
      - https://github.com/hxl-team/HXL-Vocab/blob/master/Tools/static/hxl.ttl
    - SPARQL, Geo, etc
      - http://www.geosparql.org/

    """
    caput_originali: List[str] = None
    caput_hxl: List[str] = None
    caput_hxltm: List[str] = None
    data: List[list] = None
    dictionaria_linguarum: Type['DictionariaLinguarum'] = None

    # https://en.wiktionary.org/wiki/originalis#Latin

    # caput_originali: List[str] = None
    # _caput_hxl: List[str] = None
    # objectīvō, n, dativus, https://en.wiktionary.org/wiki/dictionarium#Latin
    # objectīvō, n, dativus, https://en.wiktionary.org/wiki/objectivus#Latin
    _objectivo_dictionario: str = None

    def __init__(
        self,
        caput: list,
        data: list = None
    ):
        """__init__"""
        self.caput_originali = caput
        self.data = data

    def imprimere(self) -> list:
        """imprimere /print/@eng-Latn

        Trivia:
        - imprimere, v, s, (), https://en.wiktionary.org/wiki/imprimo#Latin
        - fōrmātum, s, n, nominativus, https://en.wiktionary.org/wiki/formatus

        Args:
            formatum (str, optional): output format. Defaults to 'csv'.

        Returns:
            [list]: data, caput
        """
        # pylint: disable=chained-comparison
        # caput = []
        # data = []
        # if formatum:
        #     self._formatum = formatum

        # if formatum is None or formatum == 'csv':

        caput = self.caput_originali
        data = self.data
        if self._objectivo_dictionario == 'hxl':
            caput = self.caput_hxl
        if self._objectivo_dictionario == 'hxltm':
            caput = self.caput_hxltm

        # @TODO potentially re-arrange the order of columns on the result
        return caput, data

    def praeparatio(self, formatum: str = None):
        """praeparātiō

        Trivia:
        - praeparātiō, s, f, Nom., https://en.wiktionary.org/wiki/praeparatio
        """

        self._objectivo_dictionario = formatum

        self.caput_hxl = []
        for index, res in enumerate(self.caput_originali):
            column = []
            if res and len(res) > 0 and not res.startswith('#') and \
                    len(self.data) > 0:
                for l_index, linea in enumerate(self.data):
                    if l_index > 500:
                        break
                    column.append(linea[index])

            self.caput_hxl.append(self.quod_hxl_de_caput_rei(res, column))

        # @TODO refactor from bash scripts
        #       - un_pcode_csvheader_administrative_level
        if formatum is None or formatum == 'hxltm':
            self.caput_hxltm = []

            self.dictionaria_linguarum = DictionariaLinguarum()

            for index, res in enumerate(self.caput_hxl):
                self.caput_hxltm.append(
                    self.quod_hxltm_de_hxl_rei(res))
        # else:
        # print('teste??', self.caput_hxltm)

        # self.caput_hxltm = self.caput_hxl
        # pass

        return self

    @staticmethod
    def quod_columna_alphabeto_orini(column: list = None) -> str:
        """quod_columna_alphabeto_orini

       For a list of values, the non empty ones which have letters, if
       the number of letters are consistent, how many? Used to know
       if data columns could be labeled, as example, as ISO 3661-2 or
       ISO 3661-3.

        Args:
            column (list, optional):. Defaults to None.

        Returns:
            str: _description_
        """
        ordo = None
        _ordo = set()
        if column and len(column) > 0:
            for item in column:
                alpha = re.sub('[0-9]', '', item)
                if alpha and len(alpha) > 1:
                    _ordo.add(len(alpha))
            if len(_ordo) == 1:
                ordo = _ordo.pop()
        return ordo

    @staticmethod
    def quod_hxl_de_caput_rei(res: str, data_exemplis: list = None) -> str:
        """quod_hxl_de_caput_rei

        Args:
            res (str):
            data_exemplis (list):

        Returns:
            str:
        """
        res_originale = res
        if not res or len(res) == 0 or res.startswith('#'):
            # pipelining hxl again? let's not change it.
            return res

        # @see https://data.humdata.org/tools/hxl-example/
        praefīxum = ''
        suffīxum = ''
        # ōrdō  = ''
        lingua = ''
        # iso = ''
        res = res.lower()
        numerus = re.sub('[^0-9]', '', res)
        geo_ōrdinī = ''
        nomen_ōrdinī = ''
        if len(numerus) == 2:
            geo_ōrdinī = numerus[0]
            nomen_ōrdinī = numerus[1]
        if len(numerus) == 1:
            geo_ōrdinī = numerus

        if len(numerus) > 2:
            # Something weird like admin2pcode2016. Better human review
            return ''

        if res in ['date', 'validon', 'validto']:
            praefīxum = '#date'
            if res == 'date':
                suffīxum = '+start'
            if res == 'validon':  # validOn
                suffīxum = '+updated'
            if res == 'validto':  # validTo
                suffīxum = '+end'
        elif res.startswith('adm') and len(geo_ōrdinī) == 1:
            if geo_ōrdinī == '0':
                praefīxum = '#country'
            else:
                praefīxum = '#adm{0}'.format(geo_ōrdinī)

            if res.find('pcode') > -1:
                if geo_ōrdinī == '0':
                    ordo_codici = CodAbTabulae.quod_columna_alphabeto_orini(
                        data_exemplis)
                    if ordo_codici and ordo_codici in [2, 3]:
                        suffīxum = '+code+v_iso{0}'.format(ordo_codici)
                    else:
                        suffīxum = '+code'
                else:
                    suffīxum = '+code+v_pcode'

            elif res.find('code') > -1:
                suffīxum = '+code'

            elif res.find('name') > -1:
                if res.find('nameref') > -1 or res.find('nameref') > -1:
                    suffīxum = '+name+preferred'
                if res.find('altname') > -1:
                    suffīxum = '+name+alt{0}'.format(nomen_ōrdinī)
                else:
                    suffīxum = '+name'
                if res.find('_') > -1:
                    _temp = res.split('_')
                    if len(_temp) == 2:
                        lingua = '+i_' + _temp[1]

        if len(praefīxum) == 0:
            # Something not planned was tagged. Labeling as Meta.
            praefīxum = '#meta'

        # use case: ukr.xlsx
        #   admin2Name_en	admin2Name_ua	admin2Name_ru	admin2Pcode
        #   admin2ClassCode	admin2ClassType	admin2PoliticalType
        #   admin2pcode2016	admin1ClassType	admin1ClassCode
        if len(praefīxum) > 0 and praefīxum != '#date' and len(suffīxum) == 0:
            splitted = re.sub(
                '([A-Z][a-z]+)', r' \1',
                re.sub('([A-Z]+)', r' \1', res_originale)).split()
            praefīxum = '#meta'
            for _item in splitted:
                suffīxum = suffīxum + '+' + _item.lower()

            # Something weird happened
        return '{0}{1}{2}'.format(praefīxum, suffīxum, lingua)

    def quod_hxltm_de_hxl_rei(self, hxlhashtag: str) -> str:
        """quod_hxl_de_caput_rei

        Args:
            res (str):

        Returns:
            str:
        """
        # lingua = ''

        if not hxlhashtag or len(hxlhashtag) == 0 or \
                not hxlhashtag.startswith('#'):
            return ''

        bcp47_rei = qhxl_hxlhashtag_2_bcp47(hxlhashtag, True)
        # raise ValueError('oi1 {0} {1}'.format(hxlhashtag, bcp47_rei))
        # hxlhashtag = '#x_todo+' + hxlhashtag.replace('#', '')
        if bcp47_rei and len(bcp47_rei) < 9:  # < 'zzz-Zzzz'
            _bcp47_rei_copia = bcp47_rei
            if bcp47_rei == 'ua':
                # Ukrainian ISO 639-2 is 'uk', not 'ua' (code of the country)
                # https://iso639-3.sil.org/code/ukr
                bcp47_rei = 'uk'

            res1603_1_51 = self.dictionaria_linguarum.quod(
                bcp47_rei, abecedarium_incognito=True)
            if res1603_1_51 and \
                    '#item+rem+i_qcc+is_zxxx+ix_hxla' in res1603_1_51:
                ix_hxla = res1603_1_51['#item+rem+i_qcc+is_zxxx+ix_hxla']
                if ix_hxla:
                    hxlhashtag = hxlhashtag.replace(
                        '+i_{0}'.format(_bcp47_rei_copia), ix_hxla)

        if hxlhashtag.startswith('#country'):
            hxlhashtag_parts = hxlhashtag.split('+')
            if 'v_iso2' in hxlhashtag_parts:
                hxlhashtag_parts[hxlhashtag_parts.index(
                    'v_iso2')] = 'v_iso3166p1a2'
                hxlhashtag = '+'.join(hxlhashtag_parts)
            if 'v_iso3' in hxlhashtag_parts:
                hxlhashtag_parts[hxlhashtag_parts.index(
                    'v_iso2')] = 'v_iso3166p1a3'
                hxlhashtag = '+'.join(hxlhashtag_parts)

        return hxlhashtag

# def cod_caput_ad_hxl_hastag(caput: list) -> list:
#     """cod_caput_ad_hxl_hastag
#     Convert a raw CSV header to HXL hashtags

#     Args:
#         caput (list):

#     Returns:
#         list:
#     """
#     # un_pcode_csvheader_administrative_level
#     return caput


def configuratio(
        archivum_configurationi: List[str] = None,
        strictum: bool = True
) -> dict:
    """cōnfigūrātiō

    Args:
        archivum_configurationi (str, optional):

    Returns:
        (dict):
    """
    # archivae = ARCHIVUM_CONFIGURATIONI_DEFALLO
    # if archivum_configurationi is not None:
    #     if not os.path.exists(archivum_configurationi):
    #         raise FileNotFoundError(
    #             'archivum_configurationi {0}'.format(
    #                 archivum_configurationi))
    #     archivae.append(archivum_configurationi)

    for item in archivum_configurationi:
        if os.path.exists(item):
            with open(item, "r") as read_file:
                datum = yaml.safe_load(read_file)
                return datum
    if strictum:
        raise FileNotFoundError(
            'archivum_configurationi {0}'.format(
                archivum_configurationi))
    return None


def csv_imprimendo(caput: list = None, data: list = None, delimiter: str = ',',
                   archivum_trivio: str = None):
    if archivum_trivio:
        raise NotImplementedError('{0}'.format(archivum_trivio))
    # imprimendō, v, s, dativus, https://en.wiktionary.org/wiki/impressus#Latin

    _writer = csv.writer(sys.stdout, delimiter=delimiter)
    if caput:
        _writer.writerow(caput)
    _writer.writerows(data)

    # print(type(data), data)
    # print(type(data), caput)


class DictionariaLinguarum:
    """DictionariaLinguarum 1603_1_51
    """

    def __init__(self, fontem_archivum: str = None):
        if fontem_archivum:
            self.D1613_1_51_fontem = fontem_archivum
        else:
            self.D1613_1_51_fontem = NUMERORDINATIO_BASIM + \
                "/1603/1/51/1603_1_51.no1.tm.hxl.csv"

        # self.codex = codex
        self.dictionaria_codex = self._init_dictionaria()

        # print('oioioi', self.dictionaria_codex )

    def _init_dictionaria(self):

        datum = {}
        with open(self.D1613_1_51_fontem) as file:
            csv_file = csv.DictReader(file)
            # return list(tsv_file)
            for conceptum in csv_file:
                # print('conceptum', conceptum)
                int_clavem = int(conceptum['#item+conceptum+codicem'])
                datum[int_clavem] = {}
                for clavem, rem in conceptum.items():
                    datum[int_clavem][clavem] = rem
                    # if not clavem.startswith('#item+conceptum+codicem'):
                    #     datum[int_clavem][clavem] = rem
        return datum

    def imprimere(
            self, linguam: list = None, codex: Type['Codex'] = None) -> list:
        """imprimere /print/@eng-Latn

        Trivia:
        - cōdex, m, s, (Nominative), https://en.wiktionary.org/wiki/codex#Latin
        - imprimere, v, s, (), https://en.wiktionary.org/wiki/imprimo#Latin
        - pāginae, f, pl, (Nominative), https://en.wiktionary.org/wiki/pagina

        Returns:
            [list]:
        """
        # pylint: disable=too-many-locals,too-many-statements

        resultatum = []
        resultatum_corpus = []
        resultatum_corpus_totale = 0

        # resultatum.append('')
        # resultatum.append(str(codex.usus_linguae_concepta))
        # resultatum.append('')

        linguam_clavem = []
        if linguam:
            for item in linguam:
                linguam_clavem.append(
                    item.replace('#item+rem', '')
                )
        # resultatum_corpus.append(linguam_clavem)
        # resultatum_corpus.append(len(linguam_clavem))
        for _clavem, lineam in self.dictionaria_codex.items():

            if len(linguam_clavem) > 0:
                if lineam['#item+rem+i_qcc+is_zxxx+ix_hxla'] not in \
                        linguam_clavem:
                    continue

            clavem_i18n = lineam['#item+rem+i_qcc+is_zxxx+ix_uid']
            item_text_i18n = lineam['#item+rem+i_lat+is_latn']
            ix_glottocode = lineam['#item+rem+i_qcc+is_zxxx+ix_glottocode']
            ix_iso639p3a3 = lineam['#item+rem+i_qcc+is_zxxx+ix_iso639p3a3']
            ix_wikiq = lineam['#item+rem+i_qcc+is_zxxx+ix_wikiq+ix_linguam']
            usus = 0
            if clavem_i18n in codex.usus_linguae_concepta:
                usus = codex.usus_linguae_concepta[clavem_i18n]

            if len(ix_glottocode) > 0:
                ix_glottocode = \
                    "https://glottolog.org/resource" + \
                    "/languoid/id/{0}[{0}]".format(
                        ix_glottocode)

            if len(ix_iso639p3a3) > 0:
                ix_iso639p3a3 = \
                    "https://iso639-3.sil.org/code/{0}[{0}]".format(
                        ix_iso639p3a3)
            if len(ix_wikiq) > 0:
                ix_wikiq = \
                    "https://www.wikidata.org/wiki/{0}[{0}]".format(
                        ix_wikiq)
            # resultatum_corpus.append(str(lineam))
            # resultatum_corpus.append(linguam)
            # resultatum_corpus.append(
            # resultatum_corpus.append("| {0}".format(clavem_i18n))
            resultatum_corpus.append("|")
            resultatum_corpus.append("{0}".format(clavem_i18n))
            resultatum_corpus.append("|")
            resultatum_corpus.append(
                "{0}\n+++<br>+++\n{1}\n+++<br>+++ {2}".format(
                    ix_glottocode, ix_iso639p3a3, ix_wikiq))
            # resultatum_corpus.append("| {0}".format(ix_glottocode))
            # resultatum_corpus.append("| {0}".format(ix_iso639p3a3))
            # resultatum_corpus.append("| {0}".format(ix_wikiq))
            # resultatum_corpus.append("| {0}".format(item_text_i18n))
            resultatum_corpus.append("|")
            resultatum_corpus.append("{0}".format(item_text_i18n))
            resultatum_corpus.append("|")
            resultatum_corpus.append("{0}".format(usus))
            resultatum_corpus.append('')
            resultatum_corpus_totale += 1

        if resultatum_corpus:
            resultatum.append("")

            # resultatum.append("=== Linguae in cōdex: {0}".format(
            #     resultatum_corpus_totale))
            resultatum.append("==== Rēs linguālibus: {0}".format(
                resultatum_corpus_totale))

            # cōdex, m, s, (nominative)
            # tōtālis, m/f, s, (Nominative)
            # linguae, f, s, (Dative)
            # resultatum.append(
            #     "Tōtālis linguae in cōdex: {0}".format(
            #         resultatum_corpus_totale))
            resultatum.append("")

            resultatum.append('[%header,cols="15h,25a,~,17"]')
            resultatum.append('|===')
            # https://en.wiktionary.org/wiki/latinus#Latin
            # nōmina, n, pl, (Nominative)
            #     shttps://en.wiktionary.org/wiki/nomen#Latin
            # "nōmen Latīnum"
            # https://en.wiktionary.org/wiki/Latinus#Latin
            # resultatum.append(
            #     "| <span lang='la'>Cōdex<br>linguae</span> | "
            #     "<span lang='la'>Glotto<br>cōdicī</span> | "
            #     "<span lang='la'>ISO<br>639-3</span> | "
            #     "<span lang='la'>Wiki QID<br>cōdicī</span> | "
            #     "<span lang='la'>Nōmen Latīnum</span> |")
            # resultatum.append("| --- | --- | --- | --- | --- |")
            # resultatum.append("| Cōdex linguae")
            resultatum.append("|")
            resultatum.append("Cōdex linguae")
            # resultatum.append("a| Glotto cōdicī ++<br>++ ISO 639-3 ++<br>++ Wiki QID cōdicī")
            resultatum.append("|")
            resultatum.append(
                "Glotto cōdicī +++<br>+++ ISO 639-3 +++<br>+++ Wiki QID cōdicī")
            # resultatum.append("| ISO 639-3")
            # resultatum.append("| Wiki QID cōdicī")
            resultatum.append("|")
            resultatum.append("Nōmen Latīnum")
            resultatum.append("|")
            resultatum.append("Concepta")
            resultatum.append('')
            resultatum.extend(resultatum_corpus)
            resultatum.append('|===')
            resultatum.append("")

            # concepta, f, pl, Nominative,
            #    https://en.wiktionary.org/wiki/conceptus

        return resultatum

    def quod(
        self,
        terminum: str,
        #  factum: str = '#item+rem+i_lat+is_latn',
        # clavem: str = None
        # clavem: str = None,
        abecedarium_incognito=False,
        _data_exemplis: list = None
    ) -> dict:
        """quod_

        Search 1603_1_51 full from a raw term, like:
          - '+i_rus+is_cyrl'
          - '__i_rus__is_cyrl'
          - 'rus-Cyrl'

        Trivia:
        - abecedārium, n, s, nom., en.wiktionary.org/wiki/incognitus#Latin
        - incognitō, n, s, dat. https://en.wiktionary.org/wiki/incognitus#Latin

        Args:
            terminum (str): _description_
            clavem (str, optional): _description_. Defaults to None.

        Returns:
            dict: _description_
        """
        _clavem = [
            '#item+rem+i_qcc+is_zxxx+ix_hxla',
            # '#item+rem+i_qcc+is_zxxx+ix_hxla',
            '#item+rem+i_qcc+is_zxxx+ix_csvsffxm',
            '#item+rem+i_qcc+is_zxxx+ix_uid'
        ]
        if abecedarium_incognito:
            _clavem.extend([
                # Glottocode Langoid
                '#item+rem+i_qcc+is_zxxx+ix_glottocode',
                # Wikidata QID; language
                '#item+rem+i_qcc+is_zxxx+ix_wikiq+ix_linguam',
                # ISO 639-3 (lang alpha 3)
                '#item+rem+i_qcc+is_zxxx+ix_iso639p3a3',
                # ISO 639-2 or ISO 639-3 (used on Wikidata/Wikipedia)
                '#item+rem+i_qcc+is_zxxx+ix_wikilngm',
            ])
        # _clavem = clavem_defallo if clavem is None else [clavem]
        # _clavem = clavem_defallo

        if _data_exemplis and len(_data_exemplis) > 0:
            raise NotImplementedError(
                '_data_exemplis [{0}] [[@TODO check Unicode range '
                'to infer script]]'.format(
                    _data_exemplis))

        # print(self.dictionaria_codex.items())
        # raise ValueError('b')

        for item in _clavem:
            # print('item', item)
            for _k, linguam in self.dictionaria_codex.items():
                if linguam['#item+conceptum+codicem'].startswith('0_'):
                    continue
                # print('linguam', terminum, item, linguam[item], linguam)
                # print('')
                # if terminum.find(linguam[item]) > -1:
                if terminum == linguam[item]:
                    # return linguam[factum]
                    # raise ValueError([terminum, linguam])
                    return linguam

        return None


class DictionariaInterlinguarum:
    """DictionariaInterlinguarum 1603_1_7
    """

    def __init__(self, fontem_archivum: str = None):
        if fontem_archivum:
            self.D1613_1_7_fontem = fontem_archivum
        else:
            self.D1613_1_7_fontem = NUMERORDINATIO_BASIM + \
                "/1603/1/7/1603_1_7.no1.tm.hxl.csv"

        self.dictionaria = self._init_dictionaria()

    def _init_dictionaria(self):

        datum = {}
        with open(self.D1613_1_7_fontem) as file:
            csv_file = csv.DictReader(file)
            # return list(tsv_file)
            for conceptum in csv_file:
                # print('conceptum', conceptum)
                int_clavem = int(conceptum['#item+conceptum+codicem'])
                datum[int_clavem] = {}
                for clavem, rem in conceptum.items():
                    datum[int_clavem][clavem] = rem
                    # if not clavem.startswith('#item+conceptum+codicem'):
                    #     datum[int_clavem][clavem] = rem
        return datum

    def formatum_nomen(
            self, clavem: str,
            _objectivum_linguam: str = None,
            _auxilium_linguam: list = None) -> str:
        # fōrmātum, f, s, (Nominative) https://en.wiktionary.org/wiki/formatus

        meta_langs = [
            '#item+rem+i_mul+is_zyyy',
            '#item+rem+i_lat+is_latn'
        ]

        ix_clavem = clavem.replace('#item+rem+i_qcc+is_zxxx+', '')
        terminum = None
        dictionaria_res = self.quod(ix_clavem)
        if dictionaria_res:
            terminum = qhxl(dictionaria_res, meta_langs)
            # terminum = terminum + ' lalala'

        return terminum if terminum else ix_clavem

    # def formatum_res_facto(
    #         self, res: dict, clavem: str,
    #         _objectivum_linguam: str = None,
    #         _auxilium_linguam: list = None
    # ) -> str:
    @staticmethod
    def formatum_res_facto(
            res: dict, clavem: str,
            _objectivum_linguam: str = None,
            _auxilium_linguam: list = None
    ) -> str:
        # fōrmātum, f, s, (Nominative) https://en.wiktionary.org/wiki/formatus
        # TODO: this still need improvement
        # return res[clavem]
        return res_interlingualibus_formata(res, clavem)
        # return res[clavem] + '[' + clavem + ']'

    def imprimere(self, linguam: list = None) -> list:
        """imprimere /print/@eng-Latn

        @DEPRECATED using methodo direct from codex

        Trivia:
        - cōdex, m, s, (Nominative), https://en.wiktionary.org/wiki/codex#Latin
        - imprimere, v, s, (), https://en.wiktionary.org/wiki/imprimo#Latin
        - pāginae, f, pl, (Nominative), https://en.wiktionary.org/wiki/pagina

        Returns:
            [list]:
        """
        resultatum = []
        # resultatum_corpus = []
        resultatum_corpus_totale = 0
        resultatum_corpus_obj = []
        linguam_clavem = []
        if linguam:
            for item in linguam:
                linguam_clavem.append(
                    item.replace('#item+rem+i_qcc+is_zxxx+', '')
                )
        # resultatum_corpus.append(linguam_clavem)
        # resultatum_corpus.append(len(linguam_clavem))
        for clavem, lineam in self.dictionaria.items():

            if len(linguam_clavem) > 0:
                if lineam['#item+rem+i_qcc+is_zxxx+ix_hxlix'] not in \
                        linguam_clavem:
                    continue

            neo_lineam = {}
            for k, v in lineam.items():
                # neo_lineam[k] = v
                if v:
                    neo_lineam[k] = v

            resultatum_corpus_obj.append(neo_lineam)

            resultatum_corpus_totale += 1

        if resultatum_corpus_obj:

            resultatum.append("==== Rēs interlinguālibus: {0}".format(
                resultatum_corpus_totale))

            # @TODO: 1603_1_99_10_11; {0} = code complete for this book
            resultatum.extend(descriptio_tabulae_de_lingua(
                'Lingua Anglica (Abecedarium Latinum)',
                'The result of this section is a preview. '
                'We\'re aware it is not well formatted for a book format. '
                'Sorry for the temporary inconvenience.'
            ))

            # About description lists

            # Two columns here (requires some changes on CSS)
            #  https://github.com/asciidoctor/asciidoctor-pdf/issues/327
            #  https://github.com/Mogztter/asciidoctor-web-pdf/tree/main
            #  /examples/cheat-sheet

            # import pprint
            resultatum.append("")
            for res in resultatum_corpus_obj:
                resultatum.append("")
                # resultatum.append('===== {0} '.format(
                #     res['#item+conceptum+numerordinatio'])
                # )
                # resultatum.append('**{0}**'.format(
                #     res['#item+conceptum+numerordinatio'])
                # )
                resultatum.append("")
                resultatum.append("{0}::".format(
                    res['#item+rem+i_lat+is_latn']))

                for clavem, rem_textum in res.items():
                    if clavem in [
                        '#item+conceptum+numerordinatio',
                        '#item+conceptum+codicem',
                        '#status+conceptum+definitionem',
                        '#status+conceptum+codicem',
                        '#item+rem+i_lat+is_latn',
                    ]:
                        continue

                    if len(rem_textum) < 1:
                        continue

                    resultatum.append("{0}::: {1}".format(clavem, rem_textum))
                    # datum[int_clavem][clavem] = rem

                # resultatum.append("")
                # resultatum.append("[source,json]")
                # resultatum.append("----")
                # resultatum.append(json.dumps(
                #     res, indent=4, sort_keys=True, ensure_ascii=False))
                # resultatum.append("----")
                # resultatum.append(pprint.pprint(res))

        return resultatum

    def imprimereTabula(self, linguam: list = None) -> list:
        """imprimere /print/@eng-Latn

        Trivia:
        - cōdex, m, s, (Nominative), https://en.wiktionary.org/wiki/codex#Latin
        - imprimere, v, s, (), https://en.wiktionary.org/wiki/imprimo#Latin
        - pāginae, f, pl, (Nominative), https://en.wiktionary.org/wiki/pagina

        Returns:
            [list]:
        """
        resultatum = []
        resultatum_corpus = []
        resultatum_corpus_totale = 0
        linguam_clavem = []
        if linguam:
            for item in linguam:
                linguam_clavem.append(
                    item.replace('#item+rem+i_qcc+is_zxxx+', '')
                )
        # resultatum_corpus.append(linguam_clavem)
        # resultatum_corpus.append(len(linguam_clavem))
        for _clavem, lineam in self.dictionaria.items():

            if len(linguam_clavem) > 0:
                if lineam['#item+rem+i_qcc+is_zxxx+ix_hxlix'] not in \
                        linguam_clavem:
                    continue

            # clavem_i18n = lineam['#item+rem+i_qcc+is_zxxx+ix_uid']
            clavem_i18n = lineam['#item+rem+i_qcc+is_zxxx+ix_hxlix']
            definitionem = lineam['#item+rem+definitionem+i_eng+is_latn']
            item_text_i18n = lineam['#item+rem+i_lat+is_latn']
            ix_wikip = lineam['#item+rem+i_qcc+is_zxxx+ix_wikip']
            # ix_glottocode = ''
            # ix_iso639p3a3 = lineam['#item+rem+i_qcc+is_zxxx+ix_iso639p3a3']
            ix_iso639p3a3 = ''
            # ix_wikiq = lineam['#item+rem+i_qcc+is_zxxx+ix_wikiq+ix_linguam']
            # ix_wikiq = ''
            ix_wikip = ''
            if len(ix_wikip) > 0:
                ix_wikip = \
                    "https://www.wikidata.org/wiki/Property:{0}[{0}]".format(
                        ix_wikip)

            if len(ix_iso639p3a3) > 0:
                ix_iso639p3a3 = \
                    "https://iso639-3.sil.org/code/{0}[{0}]".format(
                        ix_iso639p3a3)
            # if len(ix_wikiq):
            #     ix_wikiq = \
            #         "https://www.wikidata.org/wiki/{0}[{0}]".format(
            #             ix_wikiq)
            # resultatum_corpus.append(str(lineam))
            # resultatum_corpus.append(linguam)
            # resultatum_corpus.append(
            resultatum_corpus.append("| {0}".format(clavem_i18n))
            resultatum_corpus.append("| {0}".format(ix_wikip))
            resultatum_corpus.append("| {0}".format(ix_iso639p3a3))
            # resultatum_corpus.append("| {0}".format(ix_wikiq))
            resultatum_corpus.append("| {0}".format(item_text_i18n))
            resultatum_corpus.append("| {0}".format(definitionem))
            resultatum_corpus.append('')
            resultatum_corpus_totale += 1

        if resultatum_corpus:
            resultatum.append("")

            resultatum.append("=== Interlinguae in cōdex: {0}".format(
                resultatum_corpus_totale))

            # cōdex, m, s, (nominative)
            # tōtālis, m/f, s, (Nominative)
            # linguae, f, s, (Dative)
            resultatum.append(
                "Tōtālis linguae in cōdex: {0}".format(
                    resultatum_corpus_totale))
            resultatum.append("")

            resultatum.append('[%header,cols="~,~,~,~,~"]')
            resultatum.append('|===')
            # https://en.wiktionary.org/wiki/latinus#Latin
            # nōmina, n, pl, (Nominative)
            #     shttps://en.wiktionary.org/wiki/nomen#Latin
            # "nōmen Latīnum"
            # https://en.wiktionary.org/wiki/Latinus#Latin
            # resultatum.append(
            #     "| <span lang='la'>Cōdex<br>linguae</span> | "
            #     "<span lang='la'>Glotto<br>cōdicī</span> | "
            #     "<span lang='la'>ISO<br>639-3</span> | "
            #     "<span lang='la'>Wiki QID<br>cōdicī</span> | "
            #     "<span lang='la'>Nōmen Latīnum</span> |")
            # resultatum.append("| --- | --- | --- | --- | --- |")
            resultatum.append("| Interlinguae")
            resultatum.append("| /Wiki P/")
            resultatum.append("| ISO 639-3")
            # resultatum.append("| Wiki QID cōdicī")
            resultatum.append("| Nōmen Latīnum")
            resultatum.append("| Definitionem")
            resultatum.append('')
            resultatum.extend(resultatum_corpus)
            resultatum.append('|===')
            resultatum.append("")

        return resultatum

    def quod(self, terminum: str,
             #  factum: str = '#item+rem+i_lat+is_latn',
             clavem: str = None) -> str:
        # clavem_defallo = [
        #     '#item+rem+i_qcc+is_zxxx+ix_hxla',
        #     '#item+rem+i_qcc+is_zxxx+ix_csvsffxm'
        # ]
        # raise ValueError(terminum, self.dictionaria_codex.keys())
        if not terminum:
            return None

        clavem_defallo = [
            '#item+rem+i_qcc+is_zxxx+ix_hxlix',
            '#item+rem+i_qcc+is_zxxx+ix_hxlvoc'
        ]
        _clavem = clavem_defallo if clavem is None else [clavem]
        # _clavem = clavem_defallo

        for item in _clavem:
            # print('item', item)
            for _k, linguam in self.dictionaria.items():
                # print('linguam', linguam)
                if terminum == linguam[item]:
                    # if terminum.find(linguam[item]) > -1 and linguam[item]:
                    # return linguam[factum]
                    return linguam

        return None


def descriptio_tabulae_de_lingua(
        lingua_textum: Union[str, list], rem_textum: Union[str, list]) -> list:

    if isinstance(lingua_textum, str):
        lingua_textum = [lingua_textum]

    if isinstance(rem_textum, str):
        rem_textum = [rem_textum]

    paginae = []
    paginae.append('[%header,cols="25h,~a"]')
    paginae.append('|===')
    paginae.append("|")
    paginae.append("Lingua de verba")
    paginae.append("|")
    paginae.append("Verba de conceptiō")
    paginae.append('')

    for item_lingua in lingua_textum:
        item_textum = rem_textum.pop(0)
        paginae.append('|')
        paginae.append(item_lingua)
        paginae.append('|')
        paginae.append(item_textum.strip())
        # paginae.append(item_textum.strip().replace("\n\n",
        #                " +++<br><br>+++").replace("\n", " "))
        paginae.append('')

    paginae.append('|===')

    return paginae


def hxltm_carricato(
    archivum_trivio: str = None,
    est_stdin: bool = False
) -> list:
    """hxltm_carricato load entire raw CSV file to memory.

    Note: this helper is not as efficent as read line by line. But some
    operations already require such task.

    Trivia:
    - carricātō, n, s, dativus, https://en.wiktionary.org/wiki/carricatus#Latin
      - verbum: https://en.wiktionary.org/wiki/carricatus#Latin

    Args:
        archivum_trivio (str, optional): Path to file. Defaults to None.
        est_stdin (bool, optional): Is the file stdin?. Defaults to False.

    Returns:
        list: list of [caput, data], where data is array of lines
    """
    caput = []
    _data = []

    if est_stdin:
        for linea in sys.stdin:
            if len(caput) == 0:
                # caput = linea
                # _reader_caput = csv.reader(linea)
                _gambi = [linea, linea]
                _reader_caput = csv.reader(_gambi)
                caput = next(_reader_caput)
            else:
                _data.append(linea)
        _reader = csv.reader(_data)
        return caput, list(_reader)
    # else:
    #     fons = archivum_trivio

    with open(archivum_trivio, 'r') as _fons:
        _csv_reader = csv.reader(_fons)
        for linea in _csv_reader:
            if len(caput) == 0:
                # caput = linea
                # _reader_caput = csv.reader(linea)
                _gambi = [linea, linea]
                _reader_caput = csv.reader(_gambi)
                caput = next(_reader_caput)
            else:
                _data.append(linea)
            # print(row)

    # for line in fons:
    #     print(line)
        # json_fonti_texto += line

    _reader = csv.reader(_data)
    return caput, list(_reader)


def qhxl_hxlhashtag_2_bcp47(hxlhashtag: str, hxlstd11_compat: bool = False) -> str:
    """qhxl_hxlhashtag_2_bcp47

    (try) to convert full HXL hashtag to BCP47

    Args:
        hxlhashtag (str):
        hxlstd11_compat (bool):

    Returns:
        str:
    """
    # needs simplification
    if not hxlhashtag:
        return None
    if hxlhashtag.find('i_') == -1:
        return None
    if hxlhashtag.find('is_') == -1 and not hxlstd11_compat:
        return None

    hxlhashtag_parts = hxlhashtag.split('+')
    # langattrs = []
    # print('hxlhashtag_parts', hxlhashtag_parts)
    _bcp_lang = ''
    _bcp_stript = ''
    _bcp_extension = []
    for item in hxlhashtag_parts:
        if item.startswith('i_'):
            _bcp_lang = item.replace('i_', '')
        if item.startswith('is_'):
            _bcp_stript = item.replace('is_', '')
        if item.startswith('ix_'):
            _bcp_extension.append(item.replace('ix_', ''))
        # if not item.startswith(('i_', 'is_', 'ix_')):
        #     continue
        # langattrs.append(item)

    if not _bcp_lang:
        return False
    if not _bcp_stript and hxlstd11_compat:
        return _bcp_lang

    bcp47_simplici = "{0}-{1}".format(
        _bcp_lang.lower(), _bcp_stript.capitalize())
    if len(_bcp_extension) > 0:
        _bcp_extension = sorted(_bcp_extension)
        bcp47_simplici = "{0}-x-{1}".format(
            bcp47_simplici,
            '-'.join(_bcp_extension)
        )

    return bcp47_simplici


def qhxl(rem: dict, query: Union[str, list]):
    if isinstance(query, str):
        query = [query]
    for clavem, rem_item in rem.items():
        # print(clavem, rem_item, clavem.find(query))
        for query_item in query:
            # if clavem.find(query_item) > -1:
            if clavem.find(query_item) > -1 and query_item.endswith(query_item):
                return rem_item
    return None


def qhxl_attr_2_bcp47(hxlatt: str) -> str:
    """qhxl_attr_2_bcp47

    Convert HXL attribute part to BCP47

    Args:
        hxlatt (str):

    Returns:
        str:
    """
    resultatum = ''
    tempus1 = hxlatt.replace('+i_', '')
    tempus1 = tempus1.split('+is_')
    resultatum = tempus1[0] + '-' + tempus1[1].capitalize()
    # @TODO: test better cases with +ix_
    resultatum = resultatum.replace('+ix_', '-x-')

    return resultatum


def qhxl_bcp47_2_hxlattr(bcp47: str) -> str:
    """qhxl_bcp47_2_hxlattr

    Convert BCP47 to HXL attribute part

    Args:
        hxlatt (str):

    Returns:
        str:

    >>> qhxl_bcp47_2_hxlattr('lat-Latn-x-private1-private2')
    '+i_lat+is_latn+ix_private1+ix_private2'
    >>> qhxl_bcp47_2_hxlattr('qcc-Zxxx-x-wikip')
    '+i_qcc+is_zxxx+ix_wikip'
    """
    resultatum = ''
    bcp47_parsed = bcp47_langtag(bcp47)

    resultatum = '+i_' + bcp47_parsed['language']
    resultatum += '+is_' + bcp47_parsed['script'].lower()
    if len(bcp47_parsed['privateuse']) > 0:
        for item in bcp47_parsed['privateuse']:
            resultatum += '+ix_' + item

    return resultatum


def res_interlingualibus_formata(rem: dict, query) -> str:
    # pylint: disable=too-many-return-statements

    if not rem[query]:
        return ''

    if query.find('#status+conceptum+definitionem') > -1:
        return "{0} +++<sup><em>(1-100)</em></sup>+++".format(
            rem[query])
    if query.find('#status+conceptum+codicem') > -1:
        return "{0} +++<sup><em>(1-100)</em></sup>+++".format(
            rem[query])

    if query.find('+ix_wikiq') > -1 and query.endswith('+ix_wikiq'):
        return "https://www.wikidata.org/wiki/{0}[{0}]".format(
            rem[query])

    if query.find('+ix_wikip3916') > -1 and query.endswith('+ix_wikip3916'):
        # No https?
        return "http://vocabularies.unesco.org/thesaurus/{0}[{0}]".format(
            rem[query])

    if query.find('+ix_wikip') > -1 and query.endswith('+ix_wikip'):
        return "https://www.wikidata.org/wiki/Property:{0}[{0}]".format(
            rem[query])

    if query.find('+ix_ta98') > -1 and query.endswith('+ix_ta98'):
        term = rem[query].replace('A', '')
        resultatum = (
            'link:++https://ifaa.unifr.ch/Public/EntryPage/'
            'TA98%20Tree/Entity%20TA98%20EN/{0}%20Entity%20TA98%20EN.htm++['
            '{1}]').format(term, rem[query])
        return resultatum

    return rem[query]


class XLSXSimplici:
    """Read-only wrapper for XLSX files

    - XLSX http://officeopenxml.com/anatomyofOOXML-xlsx.php
    - simplicī, m/f/n, s, dativus, https://en.wiktionary.org/wiki/simplex#Latin
    """

    archivum_trivio: str = ''
    workbook: None
    active: str = None
    active_col_start: int = 0
    active_col_end: int = 1
    active_col_ignore: list = []  # Example: headers without text
    active_row_start: int = 0
    active_row_end: int = 1
    _formatum: str = 'csv'

    def __init__(self, archivum_trivio: str) -> None:
        """__init__

        Args:
            archivum_trivio (str):
        """
        # from openpyxl import load_workbook
        self.archivum_trivio = archivum_trivio
        self.workbook = load_workbook(
            archivum_trivio, data_only=True, read_only=True)
        # self.workbook = load_workbook(
        #     archivum_trivio, data_only=True)

        self.workbook.iso_dates = True
        self.sheet_active = None
        # pass

    def de(self, worksheet_reference: str = None) -> bool:
        if isinstance(worksheet_reference, str) and \
                len(worksheet_reference) == 1:
            meta = self.meta()
            if worksheet_reference in meta['sheet_cod_ab']:
                self.active = meta['sheet_cod_ab'][worksheet_reference]
                return True
        if worksheet_reference in self.workbook:
            self.active = worksheet_reference
            return True
        return False

    def meta(self) -> dict:
        """meta

        Returns:
            dict: _description_
        """
        resultatum = {
            # '_': self.workbook,
            'sheetnames': self.workbook.sheetnames,
            'sheet': {},
            'sheet_active': {},
            'sheet_cod_ab': {},
            'cod_ab_level': [],
        }
        for item in self.workbook.sheetnames:
            resultatum['sheet'][item] = {
                # '__': self.workbook[item],
                # 'max_col': self.workbook[item].max_col
                'max_column': self.workbook[item].max_column,
                'max_row': self.workbook[item].max_row
            }
            _item_num = re.sub('[^0-9]', '', item)
            if len(_item_num) == 1:
                #_likely_ab = _item_num
                resultatum['sheet_cod_ab'][_item_num] = item
                resultatum['cod_ab_level'].append(int(_item_num))
            if len(resultatum['cod_ab_level']) > 0:
                resultatum['cod_ab_level'] = sorted(resultatum['cod_ab_level'])
        # resultatum = wb2
        # print(wb2.keys())
        # workbook.close()
        return resultatum

    def finis(self) -> None:
        """finis Close XLSX file immediately to save memory
        """
        # https://en.wiktionary.org/wiki/finis#Latin
        self.workbook.close()

    def imprimere(self, formatum: str = None) -> list:
        """imprimere /print/@eng-Latn

        Trivia:
        - imprimere, v, s, (), https://en.wiktionary.org/wiki/imprimo#Latin
        - fōrmātum, s, n, nominativus, https://en.wiktionary.org/wiki/formatus

        Args:
            formatum (str, optional): output format. Defaults to 'csv'.

        Returns:
            [list]: data, caput
        """
        # pylint: disable=chained-comparison
        caput = []
        data = []
        if formatum:
            self._formatum = formatum

        fons = self.workbook[self.active]

        for row_index, row in enumerate(fons.rows):
            if row_index >= self.active_row_start and \
                    row_index <= self.active_row_end:
                linea = []
                for col_index in range(
                        self.active_col_start, self.active_col_end):
                    textum = row[col_index].value

                    if textum:
                        if isinstance(textum, datetime.datetime):
                            textum = str(textum).replace(' 00:00:00', '')
                        linea.append(textum)
                    else:
                        linea.append('')

                if len(caput) == 0:
                    caput = linea
                else:
                    data.append(linea)
            # a_dict[row[0].value+','+row[1].value].append(str(row[2].value))

        # return data, caput
        return caput, data

    def praeparatio(self):
        """praeparātiō

        Trivia:
        - praeparātiō, s, f, Nom., https://en.wiktionary.org/wiki/praeparatio
        """

        self.active_col_end = self.workbook[self.active].max_column
        self.active_row_end = self.workbook[self.active].max_row

        # fons = self.workbook[self.active]

        # for row_index, row in enumerate(fons.rows):
        #     # TODO: discover where it starts
        #     pass

        # for index_cols in fons.rows

        # @TODO: calculate if HXL, if have more columns than ideal, etc

        return True
