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

# pytest
#    python3 -m doctest ./999999999/0/L999999999_0.py


import csv
from genericpath import exists
import json
from multiprocessing.sharedctypes import Value
# import importlib
import os
from pathlib import Path
# from pathlib import Path
import re
import sys
from datetime import date, datetime
from typing import (
    Iterator,
    List,
    Tuple,
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

EXIT_OK = 0
EXIT_ERROR = 1
EXIT_SYNTAX = 2

# def _dictionaria_linguarum():
#     # importlib.import_module('', package=None)
#     L1603_1_51 = importlib.import_module('1603_1_51', package='1603_1_1')

#     return L1603_1_51.DictionariaLinguarum()

BCP47_LANGTAG_EXTENSIONS = {
    'r': lambda r, strictum: bcp47_rdf_extension(r, strictum=strictum)
}
BCP47_LANGTAG_RDF_NAMESPACES = {
    'rdf': 'http://www.w3.org/2000/01/rdf-schema#',
    'rdfs': 'http://www.w3.org/2000/01/rdf-schema#',
    'xsd': 'http://www.w3.org/2001/XMLSchema#',
    'owl': 'http://www.w3.org/2002/07/owl#',
    'skos': 'http://www.w3.org/2004/02/skos/core#',
    # https://www.w3.org/ns/csvw
    # https://www.w3.org/ns/csvw.ttl
    # 'csvw': '<http://www.w3.org/ns/csvw#>',
    'p': 'http://www.wikidata.org/prop/',
    'dct': 'http://purl.org/dc/terms/',
    # @TODO see also https://www.w3.org/ns/prov.ttl boostrapper imported by
    #       https://www.w3.org/ns/csvw.ttl
    'unescothes': 'http://vocabularies.unesco.org/thesaurus/',
}


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
       - 2022-05-28: Uses global variable BCP47_LANGTAG_EXTENSIONS to search
                     for functions to process extensions.
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

    Exemplōrum gratiā (et Python doctest, id est, automata testīs):
        (python3 -m doctest myscript.py)

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

    if len(result['extension'].keys()) > 0 and \
            'BCP47_LANGTAG_EXTENSIONS' in globals():
        for extension_key, extension_raw in result['extension'].items():
            if extension_key in BCP47_LANGTAG_EXTENSIONS:
                result['extension'][extension_key] = \
                    BCP47_LANGTAG_EXTENSIONS[extension_key](
                        extension_raw,
                        strictum=strictum
                )

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


def bcp47_rdf_extension(
        rem: str,
        clavem: Type[Union[str, list]] = None,
        strictum: bool = True
) -> dict:
    """""Public domain python function to process RDF "G" extension for BCP47

    The bcp47_rdf_extension is an public domain python function to
    aid parsing of the IETF BCP 47 language tag. It implements the syntactic
    analysis of RFC 5646 and does not require lookup tables which makes
    it friendly for quick analysis.

    The general description of extensions is described at
    https://www.rfc-editor.org/rfc/rfc5646.html#section-2.2.6

    Args:
        bcp47_extension_r (str):         The r extention part of a BCP47
                                         language tag
        clavem (Type[Union[str, list]]): Key (string) for specific value or keys
                                         (list) to return a dict (optional)
        strictum (bool):                 Throw exceptions. False replace values
                                        with False (optional)

    Returns:
        dict: Python dictionary. None means not found. False means the feature
                                 is not implemented

    Changelog:
        - 2022-05-28: Created.

    Author:
        Emerson Rocha <rocha(at)ieee.org>

    License:
        SPDX-License-Identifier: Unlicense OR 0BSD

    -----
    See also
        - en.wikipedia.org/wiki/Resource_Description_Framework#Vocabulary
        - https://en.wikipedia.org/wiki/Reification_(knowledge_representation)
        - https://en.wikipedia.org/wiki/First-order_logic
        - https://en.wikipedia.org/wiki/Universal_quantification
        - https://en.wikipedia.org/wiki/List_of_logic_symbols
          - "∀" U+2200
          - “🔗” (U+1F517)


    RDF Vocabulary / Properties
        - rdf:subject – the subject of the RDF statement
        - rdf:predicate – the predicate of the RDF statement

    @TODO: - https://en.wikipedia.org/wiki/First-order_logic#Logical_symbols
             - The logical connectives: ∧ for conjunction,
               ∨ for disjunction, → for implication, ↔ for biconditional,
               ¬ for negation. Occasionally other logical connective symbol
               are included. Some authors[7] use Cpq, instead of →,
               and Epq, instead of ↔, especially in contexts where → is used
               for other purposes. Moreover, the horseshoe ⊃ may replace →;
               the triple-bar ≡ may replace ↔;
               a tilde (~), Np, or Fp, may replace ¬;
               a double bar {\displaystyle \|}\|, {\displaystyle +}+ or
               Apq may replace ∨; and ampersand &, Kpq, or the middle dot, ⋅,
               may replace ∧, especially if these symbols are not available
               for technical reasons. (The aforementioned symbols
               Cpq, Epq, Np, Apq, and Kpq are used in Polish notation.)
           - en.wikipedia.org/wiki/Polish_notation#Polish_notation_for_logic
           - https://en.wikipedia.org/wiki/Hungarian_notation
           - https://en.wikipedia.org/wiki/Leszynski_naming_convention

    -----

    Exemplōrum gratiā (et Python doctest, id est, automata testīs):
        (python3 -m doctest myscript.py)

    >>> bcp47_rdf_extension('pskos-prefLabel', 'rdf:predicate')
    ['skos:prefLabel']

    >>> bcp47_rdf_extension('pdc-contributor-pdc-creator-pdc-publisher',
    ... 'rdf:predicate')
    ['dc:contributor', 'dc:creator', 'dc:publisher']

    >>> bcp47_rdf_extension('pdct-modified-txsd-dateTime',
    ... ['rdf:predicate', 'rdfs:Datatype'])
    {'rdf:predicate': ['dct:modified'], 'rdfs:Datatype': 'xsd:dateTime'}

    """
    # For sake of copy-and-paste portability, we ignore a few pylints:
    # pylint: disable=too-many-branches,too-many-statements,too-many-locals
    result = {
        'rdf:Statement_raw': rem,
        # 'bcp47_extension_r_normalized': None,
        'rdf:subject': [],
        'rdf:predicate': [],
        'rdf:object': [],
        'rdfs:Datatype': None,
        '_unknown': [],
        '_error': [],
    }
    _predicates = []
    _subjects = []
    _objects = []

    # result['bcp47_extension_r_normalized'] = \
    #     result['bcp47_extension_r'].lower()

    if rem.find('-') > 0:
        r_parts = rem.split('-')
        r_parts_tot = len(r_parts)
        r_rest = r_parts_tot
        while r_rest > 0:
            r_item_key = r_parts[r_parts_tot - r_rest]
            r_item_value = r_parts[r_parts_tot - r_rest + 1]
            if r_item_key.startswith('p'):
                _predicates.append('{0}:{1}'.format(
                    r_item_key.lstrip('p').lower(),
                    r_item_value
                ))

            # sU2200
            elif r_item_key.lower().startswith('su'):
                _subjects.append('∀{0}'.format(
                    r_item_value.lstrip('s')
                ))
            elif r_item_key.lower().startswith('ss'):
                _subjects.append('{0}'.format(
                    r_item_value.lstrip('s')
                ))

            # oU1F517
            elif r_item_key.lower().startswith('ou'):
                _objects.append('🔗{0}'.format(
                    r_item_value.lstrip('o')
                ))

            elif r_item_key.startswith('t'):
                if result['rdfs:Datatype'] is None:
                    result['rdfs:Datatype'] = '{0}:{1}'.format(
                        r_item_key.lstrip('t'),
                        r_item_value
                    )
                else:
                    result['_error'].append(
                        'rdfs:Datatype [{0}]-[{1}]'.format(
                            r_item_key,
                            r_item_value
                        ))
            else:
                result['_error'].append('Unknow [{0}-{1}]'.format(
                    r_item_key,
                    r_item_value
                ))
            r_rest = r_rest - 2

        if len(_predicates) > 0:
            _predicates.sort()
            result['rdf:predicate'] = _predicates

        if len(_objects) > 0:
            _objects.sort()
            result['rdf:object'] = _objects

        if len(_subjects) > 0:
            _subjects.sort()
            result['rdf:subject'] = _subjects

    else:
        result['_error'].append('G extension do not have -')

    if len(r_parts) % 2 == 0:
        pass
    else:
        result['_error'].append('G extension not even number')

    if strictum and len(result['_error']) > 0:
        raise SyntaxError('[{0}]: <{1}>'.format(
            rem, result['_error']))

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


def bcp47_rdf_extension_relationship(
        header: List[str],
        strictum: bool = True
) -> dict:
    """""Metadata processing of the bcp47_rdf_extension version

    _extended_summary_

    Args:
        caput (List[str]): _description_
        strictum (bool, optional): _description_. Defaults to True.

    Returns:
        dict: _description_
    """
    result = {
        'columns_original': header,
        'columns': [],
        # 'rdf:subject': None,
        # 'rdf:predicate': [],
        # 'rdf:object': None,
        # 'rdfs:Datatype': None,
        # '_unknown': [],
        'rdfs:Container': {},
        'prefixes': {
            'rdf': BCP47_LANGTAG_RDF_NAMESPACES['rdf'],
            'rdfs': BCP47_LANGTAG_RDF_NAMESPACES['rdfs'],
            'xsd': BCP47_LANGTAG_RDF_NAMESPACES['xsd'],
            'owl': BCP47_LANGTAG_RDF_NAMESPACES['owl']
        },
        '_error': [],
    }

    # print('header', header)

    for index, item in enumerate(header):
        item_meta = bcp47_langtag(
            item, ['language', 'script', 'extension'], strictum=False)
        # @TODO; get erros and export them to upper level
        item_meta['_column'] = index
        inline_namespace = None
        inline_namespace_iri = None
        # is_inline_namespace = False
        if 'r' in item_meta['extension'] and \
                len(item_meta['extension']['r']['rdf:object']) > 0:
            for object in item_meta['extension']['r']['rdf:object']:
                if object.startswith('🔗'):
                    # is_inline_namespace = True
                    inline_namespace = object.replace('🔗', '')
                    strictum = True
                    if inline_namespace not in BCP47_LANGTAG_RDF_NAMESPACES:
                        if strictum:
                            raise SyntaxError(
                                'inline_namespace ({0}) ? <{1}> <{2}>'.format(
                                    inline_namespace, header, item_meta
                                ))
                        else:
                            inline_namespace_iri = '_' + inline_namespace
                    else:
                        inline_namespace_iri = \
                            BCP47_LANGTAG_RDF_NAMESPACES[inline_namespace]
                        result['prefixes'][inline_namespace] = inline_namespace_iri

        # print('item inline_namespace_iri', item, inline_namespace_iri)
        if 'r' in item_meta['extension'] and \
                len(item_meta['extension']['r']['rdf:subject']) > 0:
            for subject in item_meta['extension']['r']['rdf:subject']:
                is_pivot_key = False
                if subject.startswith('∀'):
                    is_pivot_key = True
                    subject = subject.replace('∀', '')
                if subject.startswith('🔗'):
                    is_pivot_key = True
                    subject = subject.replace('🔗', '')

                if subject not in result['rdfs:Container']:
                    result['rdfs:Container'][subject] = {
                        'pivot': {
                            'index': -1,
                            'iri': inline_namespace_iri,
                            'prefix': 'urn',
                            # We will fallback the pivots as generic classes
                            # We should enable later override this behavior
                            # via language tag on the pivot
                            'rdf:predicate': ['rdfs:Class'],
                        },
                        'columns': []
                    }

                if inline_namespace is not None:
                    result['rdfs:Container'][subject]['pivot']['prefix'] = \
                        inline_namespace
                result['rdfs:Container'][subject]['columns'].append(index)

                if is_pivot_key:
                    if result['rdfs:Container'][subject]['pivot']['index'] > -1:
                        SyntaxError('{0} <{1}>'.format(header, item_meta))
                    result['rdfs:Container'][subject]['pivot']['index'] = index

        if 'r' in item_meta['extension'] and \
                len(item_meta['extension']['r']['rdf:predicate']) > 0:
                for predicate in item_meta['extension']['r']['rdf:predicate']:
                    prefix, suffix = predicate.split(':')
                    if prefix not in result['prefixes']:
                        if prefix not in BCP47_LANGTAG_RDF_NAMESPACES:
                            raise SyntaxError(
                                'prefix [{0}]? <{1}> <{2}>'.format(
                                prefix, header, BCP47_LANGTAG_RDF_NAMESPACES
                            ))
                        result['prefixes'][prefix] = \
                            BCP47_LANGTAG_RDF_NAMESPACES[prefix]


        result['columns'].append(item_meta)

    return result


def bcp47_rdf_extension_poc(
        header: List[str],
        data: List[List],
        objective_bag: str = '1',
        _auxiliary_bags: List[str] = None,
        namespaces: List[dict] = None,
        strictum: bool = True
) -> dict:
    """bcp47_rdf_extension_poc _summary_

    _extended_summary_

    Args:
        header (List[str]): _description_
        data (List[List]): _description_
        strictum (bool, optional): _description_. Defaults to True.

    Returns:
        dict: _description_

    Exemplōrum gratiā (et Python doctest, id est, automata testīs):
        (python3 -m doctest myscript.py)


    >>> namespaces = [
    ...    {'prefix': 'dc', 'iri': 'http://purl.org/dc/elements/1.1/'}
    ... ]

    >>> header_1 = ['qcc-Zxxx-r-sRDF-subject',
    ...             'eng-Latn-r-pdc-contributor-pdc-creator-pdc-publisher']
    >>> header_2 = ['qcc-Zxxx-r-sU2200-s0',
    ...             'eng-Latn-r-pdc-contributor-pdc-creator-pdc-publisher']
    >>> data_1 = [['<http://vocabularies.unesco.org/thesaurus>'
    ...             'UNESCO']]
    >>> poc1 = bcp47_rdf_extension_poc(header_2, data_1, namespaces)

    # >>> poc1['header_result']
    #'pskos-prefLabel'

    """
    # raise NotImplementedError(header)
    result = {
        'header': header,
        'header_result': [],
        'data': data,
        # 'rdf:subject': None,
        # 'rdf:predicate': [],
        # 'rdf:object': None,
        # 'rdfs:Datatype': None,
        # '_unknown': [],
        'triples': [],
        'prefixes': {},
        '_error': [],
    }
    # return {}

    # print('header', header)

    # header.pop()

    meta = bcp47_rdf_extension_relationship(header, strictum=strictum)
    meta['data'] = data
    # return meta
    if objective_bag not in meta['rdfs:Container']:
        raise SyntaxError('objective_bag({0})? {1} <{1}>'.format(
            objective_bag, header, meta))
    bag_meta = meta['rdfs:Container'][objective_bag]
    is_urn = bag_meta['pivot']['prefix'].startswith('urn')
    prexi_iri = None

    # return bag_meta
    if not is_urn:
        prexi_iri = bag_meta['pivot']['iri']

    index_id = bag_meta['pivot']['index']
    triples_delayed = []

    def _helper_aux(
        bag_meta, bcp47_lang=None, subject=None,
        object_literal=None, linea=[]
    ) -> Tuple:
        triples = []

        # @TODO: implement some way to discover implicit relations
        #        (up to one level). Would need scan table twice
        triples_delayed = []
        # This obviously is simplistic, because we can reference multiple
        # columns for same hashtags.
        for predicate in bag_meta['rdf:predicate']:
            object_result = object_literal
            if not bcp47_lang.startswith('qcc'):
                object_result = '"{0}"@{1}'.format(object_result, bcp47_lang)
            else:
                object_result = '"{0}"'.format(object_result)

            triples.append([subject, predicate, object_result])

        # raise ValueError(bag_meta)

        return triples, triples_delayed

    for linea in data:
        # triple = []
        # First pivot
        if is_urn:
            triple_subject = '<urn:{0}>'.format(linea[index_id])
        else:
            triple_subject = '<{0}{1}>'.format(prexi_iri, linea[index_id])

        # Predicate for self is Subject here
        for predicate in bag_meta['pivot']['rdf:predicate']:
            triple = [triple_subject, 'a', predicate]
            result['triples'].append(triple)

        for referenced_by in bag_meta['columns']:
            if referenced_by == index_id:
                continue

            _bcp47lang = '{0}-{1}'.format(
                meta['columns'][referenced_by]['language'],
                meta['columns'][referenced_by]['script'],
            )
            object_literal = linea[referenced_by]
            aux_triples, triples_delayed = _helper_aux(
                meta['columns'][referenced_by]['extension']['r'],
                bcp47_lang=_bcp47lang,
                subject=triple_subject,
                object_literal=object_literal,
                linea=linea)
            if len(aux_triples) > 0:
                result['triples'].extend(aux_triples)

    # result['prefixes'] = BCP47_LANGTAG_RDF_NAMESPACES
    result['prefixes'] = meta['prefixes']

    return result
    # return result['triples']
    return objective_bag_meta
    main_prefix = '_:'
    main_is_urn = False
    result['triples'].append(meta['rdfs:Container'][objective_bag])

    return result['triples']

    return meta


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
    caput_no1: List[str] = None
    data: List[list] = None
    dictionaria_linguarum: Type['DictionariaLinguarum'] = None
    ordo: int = 1
    numerordinatio_praefixo: str = None
    pcode_praefixo: str = None
    unm49: str = None

    # identitās, f, s, nom., https://en.wiktionary.org/wiki/identitas#Latin
    # ex (+ ablative), https://en.wiktionary.org/wiki/ex#Latin
    # locālī, n, s, dativus, https://en.wiktionary.org/wiki/localis#Latin
    # identitas_locali_ex_hxl_hashtag: str = '#item+conceptum+codicem'
    identitas_locali_index: int = -1
    numerordinatio_indici: int = -2

    # https://en.wiktionary.org/wiki/originalis#Latin

    # caput_originali: List[str] = None
    # _caput_hxl: List[str] = None
    # objectīvō, n, dativus, https://en.wiktionary.org/wiki/dictionarium#Latin
    # objectīvō, n, dativus, https://en.wiktionary.org/wiki/objectivus#Latin
    _objectivo_dictionario: str = None

    def __init__(
        self,
        caput: list,
        data: list = None,
        ordo: int = 1,
        numerordinatio_praefixo: str = None,
        pcode_praefixo: str = None,
        unm49: str = None,
    ):
        """__init__"""
        self.caput_originali = caput
        self.data = data
        self.ordo = ordo
        self.numerordinatio_praefixo = numerordinatio_praefixo
        self.pcode_praefixo = pcode_praefixo
        self.unm49 = unm49

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

        # print(self._objectivo_dictionario)

        caput = self.caput_originali
        data = self.data
        if self._objectivo_dictionario == 'hxl':
            caput = self.caput_hxl
        if self._objectivo_dictionario == 'hxltm':
            caput = self.caput_hxltm
        if self._objectivo_dictionario == 'no1':
            caput = self.caput_no1

        # @TODO potentially re-arrange the order of columns on the result
        return caput, data

    def praeparatio(self, formatum: str):
        """praeparātiō

        Trivia:
        - praeparātiō, s, f, Nom., https://en.wiktionary.org/wiki/praeparatio
        """

        self._objectivo_dictionario = formatum

        self.caput_hxl = []
        self.dictionaria_linguarum = None

        # print('self.data', self.data)

        # Let's assume is a plain CSV (we skip if start with #)
        for index, res in enumerate(self.caput_originali):
            column = []
            if res and len(res) > 0 and not res.startswith('#') and \
                    len(self.data) > 0:
                for l_index, linea in enumerate(self.data):
                    if l_index > 500:
                        break
                    column.append(linea[index])

            self.caput_hxl.append(self.quod_hxl_de_caput_rei(res, column))

        if formatum not in ['hxltm', 'no1']:
            return self
        # if formatum in ['hxltm', 'no1']:
        self.caput_hxltm = []

        self.dictionaria_linguarum = DictionariaLinguarum()

        for index, res in enumerate(self.caput_hxl):
            caput_novi = self.quod_hxltm_de_hxl_rei(res)

            if caput_novi == '#item+conceptum+codicem':
                self.identitas_locali_index = index
            # if caput_novi == '#item+conceptum+numerordinatio':
            #     self.numerordinatio_indici = index

            self.caput_hxltm.append(caput_novi)

        if self.identitas_locali_index < 0:
            self.praeparatio_identitas_locali()

        if formatum == 'no1':
            self.caput_no1 = []

            # self.dictionaria_linguarum = DictionariaLinguarum()

            for index, res in enumerate(self.caput_hxltm):
                caput_novi = self.quod_no1_de_hxltm_rei(res)

                # if caput_novi == '#item+conceptum+codicem':
                #     self.identitas_locali_index = index
                if caput_novi == '#item+conceptum+numerordinatio':
                    self.numerordinatio_indici = index

                self.caput_no1.append(caput_novi)

        # if formatum in ['hxltm', 'no1'] and self.identitas_locali_index < 0:
        #     self.praeparatio_identitas_locali()

        if self.numerordinatio_indici < 0:
            self.praeparatio_numerordinatio()

        return self

    def praeparatio_identitas_locali(self):
        """praeparatio_identitas_locali
        """
        pcode_index = None
        pcode_hashtag_de_facto = ''
        if self.ordo == 0:
            pcode_hashtag = [
                '#country+code+v_pcode', '#country+code+v_iso2',
                '#country+code+v_iso3166p1a2']
        else:
            pcode_hashtag = ['#adm{0}+code+v_pcode'.format(self.ordo)]

        for item in pcode_hashtag:
            if item in self.caput_hxltm:
                pcode_hashtag_de_facto = item
                pcode_index = self.caput_hxltm.index(item)
                break

        if pcode_index is None:
            raise SyntaxError(
                '{0} not in (hxltm)<{1}>/(hxl)<{2}>(csv){3}'.format(
                    pcode_hashtag, self.caput_hxltm,
                    self.caput_hxl, self.caput_originali
                ))
        # pcode_index = self.caput_hxltm.index(pcode_hashtag)

        self.caput_hxltm.insert(0, '#item+conceptum+codicem')
        data_novis = []

        for linea in self.data:
            linea_novae = []
            pcode_completo = linea[pcode_index]
            if self.ordo == 0:
                linea_novae.append(pcode_completo)  # Ex. BR
            else:

                # Ex. 31 ad BR31
                pcode_numeri = pcode_completo.replace(self.pcode_praefixo, '')

                # Ex: Haiti admin3Pcode HT0111-01, HT0111-02, HT0111-03
                pcode_numeri = re.sub('[^0-9]', '', pcode_numeri)

                try:
                    linea_novae.append(int(pcode_numeri))
                except ValueError as err:
                    raise ValueError('<{0}:{1}> -> int({2})?? [{3}]'.format(
                        pcode_hashtag_de_facto,
                        pcode_completo,
                        pcode_numeri,
                        err
                    ))

            linea_novae.extend(linea)
            data_novis.append(linea_novae)

        self.data = data_novis

    def praeparatio_numerordinatio(self):
        """numerordinatio
        """
        identitas_locali_index = self.caput_hxltm.index(
            '#item+conceptum+codicem')
        self.caput_no1.insert(0, '#item+conceptum+numerordinatio')
        data_novis = []

        for linea in self.data:
            linea_novae = ['{0}:{1}:{2}:{3}'.format(
                self.numerordinatio_praefixo,
                self.unm49,
                str(self.ordo),
                linea[identitas_locali_index],

            )]
            linea_novae.extend(linea)
            data_novis.append(linea_novae)

        self.data = data_novis

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

        # print('  ordo', ordo, column)
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
                    elif ordo_codici is None:
                        # Weird case: no data at all on adm0. Lets force
                        # as ISO 3661p1a2
                        suffīxum = '+code+v_iso2'
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
        """quod_hxltm_de_hxl_rei

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

    def quod_no1_de_hxltm_rei(self, hxlhashtag: str) -> str:
        """quod_no1_de_hxltm_rei

        Args:
            res (str):

        Returns:
            str:
        """
        # lingua = ''

        if not hxlhashtag or len(hxlhashtag) == 0 or \
                not hxlhashtag.startswith('#'):
            return ''

        # print('hxlhashtag', hxlhashtag)
        # Time-related hashtags
        # @see https://www.wikidata.org/wiki/Wikidata:List_of_properties/time
        # # https://www.wikidata.org/wiki/Property:P571
        # # inception (P571)
        # # time when an entity begins to exist
        # # equivalent property
        # #  - https://schema.org/dateCreated
        # #  - http://id.nlm.nih.gov/mesh/vocab#dateCreated
        # if hxlhashtag == '#date+start':
        #     return '#item+rem+i_qcc+is_zxxx+ix_wikip571'

        # # P729 service entry
        # # date or point in time on which a piece or class of equipment
        # # https://www.wikidata.org/wiki/Property:P729
        # if hxlhashtag == '#date+start':
        #     return '#item+rem+i_qcc+is_zxxx+ix_wikip729'

        # # P729 service entry
        # # date or point in time on which a piece or class of equipment
        # # https://www.wikidata.org/wiki/Property:P730
        # if hxlhashtag == '#date+end':
        #     return '#item+rem+i_qcc+is_zxxx+ix_wikip730'

        # publication date (P577)
        # date or point in time when a work was first published or released
        # https://www.wikidata.org/wiki/Property:P577
        if hxlhashtag == '#date+start':
            return '#item+rem+i_qcc+is_zxxx+ix_wikip577'

        # discontinued date (P2669)
        # date that the availability of a product was discontinued;
        # see also "dissolved, abolished or demolished" (P576)
        # https://www.wikidata.org/wiki/Property:P2669
        if hxlhashtag == '#date+end':
            return '#item+rem+i_qcc+is_zxxx+ix_wikip2669'

        ## retrieved (P813)
        # - https://www.wikidata.org/wiki/Property:P813
        # - https://wiki.openstreetmap.org/wiki/Key:check_date
        if hxlhashtag == '#date+updated':
            return '#item+rem+i_qcc+is_zxxx+ix_wikip813'

        # ISO 3166-1 alpha-2 code (P297)
        # https://www.wikidata.org/wiki/Property:P297
        if hxlhashtag in [
                '#country+code+v_iso2', '#country+code+v_iso3166p1a2']:
            # @TODO: make qualifier if this is not adm0
            return '#item+rem+i_qcc+is_zxxx+ix_wikip297'

        # @TODO '#adm1+code+v_pcode' likely to be alpha 2 (needs check data)

        return self.quod_hxltm_de_hxl_rei(hxlhashtag)


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


def csv_imprimendo(
        caput: list = None, data: list = None, punctum_separato: str = ",",
        archivum_trivio: str = None):
    if archivum_trivio:
        raise NotImplementedError('{0}'.format(archivum_trivio))
    # imprimendō, v, s, dativus, https://en.wiktionary.org/wiki/impressus#Latin

    _writer = csv.writer(sys.stdout, delimiter=punctum_separato)
    if caput and len(caput) > 0:
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


def hxltm_data_referentibus(data_referentibus_index: str, columna: str):
    _caput_columna = [columna]
    _data_columna = []

    return _caput_columna, _data_columna


def hxltm__est_data_referentibus(*options):
    dr_regex = r'(DATA_REFERENTIBUS)\(\s*(?P<data_referentibus>.*)\s*;\s*(?P<c3>.*)\s*\)'
    resultatum = set()
    for options_l1 in options:
        # print(options_l1)
        if not options_l1:
            continue
        if not isinstance(options_l1, list):
            options_l1 = [options_l1]
        for options_l2 in options_l1:
            # print('options_l2', options_l2)
            _regex_result = re.search(dr_regex, options_l2)
            # print('options_l2 _regex_result', _regex_result)
            if _regex_result:
                resultatum.add(_regex_result.group('data_referentibus'))

    return resultatum


def hxltm__quod_data_referentibus(index_nomini: str):
    _path = '{0}/999999/0/{1}.index.json'.format(
        NUMERORDINATIO_BASIM,
        index_nomini,
    )
    if not exists(_path):
        raise FileNotFoundError(
            '{0} not ready. Please use {1}. [{2}]'.format(
                index_nomini,
                "--methodus='index_praeparationi'",
                _path))
    with open(_path, "r") as archivum:
        data = json.load(archivum)
        return data


def hxltm__data_referentibus(
    # al1: str, b2: str,
    significatus: dict,
    caput: list = None, linea: list = None, data_referentibus: dict = None
):
    # print(significatus)
    # print('TODO hxltm__data_referentibus')
    if not significatus['data_referentibus'] in data_referentibus:
        raise FileNotFoundError(
            '{0} not ready. Please use {1}. [{2}]'.format(
                significatus['data_referentibus'],
                "--methodus='index_praeparationi'"))

    # print(_caput)
    # print(significatus)
    if 'b2h_indici' not in significatus or significatus['b2h_indici'] is None:
        significatus['b2h_indici'] = caput.index(significatus['b2h'])

    res = linea[significatus['b2h_indici']]
    if res in data_referentibus[significatus['data_referentibus']]:
        return data_referentibus[significatus['data_referentibus']][res]
    else:
        # @TODO maybe allow raise error instead of return empty
        return ''


def hxltm__concat(
    # al1: str, b2: str,
    significatus: dict,
    caput: list = None, linea: list = None, data_referentibus: dict = None
):
    if significatus['a1'] in caput and significatus['b2'] in caput:
        return (linea[caput.index(significatus['a1'])] +
                linea[caput.index(significatus['b2'])])
    else:
        raise SyntaxError('{0} <{1}>? <{2}>'.format(
            'hxltm__concat', significatus, caput))


def hxltm__concat_literal(
    # al1: str, bl2: str,
    significatus: dict,
    caput: list = None, linea: list = None, data_referentibus: dict = None
):
    return significatus['al1'] + significatus['bl2']


def hxltm__concat_prefix(
    # al1: str, b2: str,
    significatus: dict,
    caput: list = None, linea: list = None, data_referentibus: dict = None
):
    # if significatus['b2'] in caput:
    if significatus['bh2'] in caput:
        bh2_indici = caput.index(significatus['bh2'])
        # print('bb2', caput.index(significatus['bh2']), linea[bh2_indici])
        # if len(linea[caput[significatus['b2']]]) > 0:
        if len(linea[bh2_indici]) > -1:
            return (significatus['al1'] +
                    linea[bh2_indici])
    else:
        raise SyntaxError('{0} <{1}>? <{2}>'.format(
            'hxltm__concat_prefix', significatus, caput))
    return ''


def hxltm__concat_suffix(
    # al1: str, b2: str,
    significatus: dict,
    caput: list = None, linea: list = None, data_referentibus: dict = None
):
    # print(significatus)
    # print(caput)
    if significatus['a1'] in caput:
        if len(linea[caput.index(significatus['a1'])]) > 0:
            return (linea[caput.index(significatus['a1'])] +
                    significatus['bl2'])
    else:
        raise SyntaxError('{0} <{1}>? <{2}>'.format(
            'hxltm__concat_suffix', significatus, caput))
    return ''


# https://docs.python.org/3/library/operator.html
# https://en.wiktionary.org/wiki/opus#Latin
HXLTM_OPERA_2 = {
    '==': lambda a1, b2: a1 == b2,
    '!=': lambda a1, b2: a1 != b2,
    '>': lambda a1, b2: a1 > b2,
    '<': lambda a1, b2: a1 < b2,
    '>=': lambda a1, b2: a1 >= b2,
    '<=': lambda a1, b2: a1 <= b2,
}
# HXLTM_OPERA_2 = {
#     '==': lambda a1, b2, _q=None, _dr=None: a1 == b2,
#     '!=': lambda a1, b2, _q=None, _dr=None: a1 != b2,
#     '>': lambda a1, b2, _q=None, _dr=None: a1 > b2,
#     '<': lambda a1, b2, _q=None, _dr=None: a1 < b2,
#     '>=': lambda a1, b2, _q=None, _dr=None: a1 >= b2,
#     '<=': lambda a1, b2, _q=None, _dr=None: a1 <= b2,
# }

HXLTM_OPERA_2_EX = {

    # both are existing data columns
    r'(DATA_REFERENTIBUS)\(\s*(?P<data_referentibus>.*)\s*;\s*(?P<b2h>.*)\s*\)': hxltm__data_referentibus,

    # Too generic
    # r'(CONCAT)\((?P<a1>.*)\s?;\s?(?P<b2>.*)\)': lambda a1: print('manual'),

    # both are existing data columns
    r'(CONCAT)\((?P<a1>#.*)\s?;\s?(?P<b2>#.*)\)': hxltm__concat,

    # Harcoded prefix
    # r'(CONCAT)\(\s*[\"\'](?P<al1>.*)[\"\']\s*;\s*(?P<b2>#.*)\s*\)': hxltm__concat_prefix,
    r'(CONCAT)\(\s*[\"\'](?P<al1>.*)[\"\']\s*;\s*(?P<bh2>#.*)\s*\)': hxltm__concat_prefix,

    # Hardcoded suffix
    r'(CONCAT)\(\s*(?P<a1>#.*)\s*;\s*[\"\'](?P<bl2>.*)[\"\']\s*\)': hxltm__concat_suffix,

    # Harcoded prefix and suffix
    r'(CONCAT)\(\s*[\"\'](?P<al1>.*)[\"\']\s*;\s*[\"\'](?P<bl2>.*)[\"\']\s*\)': hxltm__concat_literal,
}

# CONCAT(#meta+a1;#item+a2)
# CONCAT(#meta+a1;"teste after")
# CONCAT("pre";#item+a2)
# CONCAT(#meta+a1 ; #item+a2)
# CONCAT(#meta+a1 ; "teste after")
# CONCAT("pre" ; #item+a2)
# CONCAT("pre" ; "post")

HXLTM_OPERA_1 = {
    r'(CAPITALIZE)\((?P<a1>.*)\)': lambda a1: str(a1).capitalize(),
    r'(LOWER)\((?P<a1>.*)\)': lambda a1: str(a1).lower(),
    r'(UPPER)\((?P<a1>.*)\)': lambda a1: str(a1).upper(),
    r'(TITLE)\((?P<a1>.*)\)': lambda a1: str(a1).title(),
    r'(TRIM)\((?P<a1>.*)\)': lambda a1: str(a1).strip(),
    # ex (+ ablative) https://en.wiktionary.org/wiki/ex#Latin
    # referentibus, pl, m/f/n, dativus, https://en.wiktionary.org/wiki/referens
    # data, pl, n, nominativus, https://en.wiktionary.org/wiki/datum#Latin
    # https://regex101.com/r/3J42kO/1
    r'(DATA_REFERENTIBUS)\(\s*(?P<data_referentibus>.*)\s*;\s*(?P<c3>.*)\s*\)': "<complex>",
}

# CONCAT(#meta+a1;#item+a2)
# CONCAT(#meta+a1;"teste after")
# CONCAT("pre";#item+a2)
# #country+code+v_unm49=DATA_REFERENTIBUS(i1603_45_49; #country+code+v_iso3 )
# CONCAT("BR";DATA_REFERENTIBUS(i1603_45_49; #country+code+v_iso3 ))
# #adm2+code+v_pcode=DATA_REFERENTIBUS(i1603_45_49; #country+code+v_iso3 )

# HXLTM_OPERA_X = {
#     r'(?P<a1>.*)=(?P<b2>.*)': lambda a1, b3: print('manual'),
# }


def hxltm__quaestio_significatis_i(quaestio: str, caput: list = None) -> dict:
    """hxltm__quaestio_significatis_i parse a 1-statement query

    Args:
        quaestio (str): query
        caput (list, optional): HXL header. Defaults to None.

    Raises:
        SyntaxError: _description_

    Returns:
        dict: _description_
    """
    # - quaestiō, f, s,  dativus, https://en.wiktionary.org/wiki/significatus
    # - significātīs, m/f/n, s, dativus,
    #     https://en.wiktionary.org/wiki/significatus
    significātus = {
        'opus': None,
        'opus_rebus': [],
        'a1': '',
        'a1_indici': None,
        # 'a1_operi': None,  # HXLTM_OPERA_1 lambda lambda function call
        '_datetime': False,
    }

    # filtrum = None

    for regex_str, _lambda in HXLTM_OPERA_1.items():
        # print(regex_str)
        _regex_result = re.search(regex_str, quaestio)
        if _regex_result:
            # significātus['a1_operi'] = _lambda
            significātus['opus'] = _lambda
            for _nomen, _res in _regex_result.groupdict().items():
                significātus[_nomen] = _res
                significātus['opus_rebus'].append(_nomen)
            # print('done', _regex_result.groupdict())
            # print('done', significātus)
        # _regex_parsed = regex_str.match(quaestio)
        # print(_regex_result, _regex_result.group('a1'), regex_str)

    if significātus['opus'] is None:
        raise SyntaxError('{0}? quaestio [{1}] [{2}] <[{3}]>'.format(
            'hxltm__quaestio_significatis_i',
            quaestio,
            significātus,
            HXLTM_OPERA_1.keys()
        ))

    if significātus['a1'].startswith('#'):
        significātus['_datetime'] = significātus['a1'].startswith('#date')
        if caput.index(significātus['a1']) > -1:
            significātus['a1_indici'] = caput.index(significātus['a1'])
        else:
            raise SyntaxError('{0}? quaestio [{1}] [{2}] <[{3}]>'.format(
                'hxltm__quaestio_significatis_i (index #)',
                quaestio,
                significātus,
                HXLTM_OPERA_1.keys()
            ))

    # raise NotImplementedError(
    #     '@TODO hxltm__quaestio_significatis_i {0}'.format(significātus))

    return significātus


def hxltm__quaestio_significatis_ii(quaestio: str, caput: list = None) -> dict:
    """hxltm__quaestio_significatis_ii parse a 2 statement query

    Args:
        quaestio (str): query
        caput (list, optional): HXL header. Defaults to None.

    Raises:
        SyntaxError: _description_

    Returns:
        dict: _description_
    """
    # - quaestiō, f, s,  dativus, https://en.wiktionary.org/wiki/significatus
    # - significātīs, m/f/n, s, dativus,
    #     https://en.wiktionary.org/wiki/significatus
    significātus = {
        'opus': None,
        'opus_rebus': ['a1', 'b2'],
        'a1': '',
        'a1_indici': None,
        'a1_operi': None,  # HXLTM_OPERA_1 lambda lambda function call
        'b2': '',
        'b2_indici': None,
        'b2_operi': None,  # HXLTM_OPERA_1 lambda lambda function call
        '_datetime': False,
    }

    for item in HXLTM_OPERA_2.keys():
        if quaestio.find(item) > -1:
            significātus['opus'] = item
            significātus['a1'], significātus['b2'] = quaestio.split(item)
            break

    if len(significātus['a1']) == 0 or len(significātus['b2']) == 0:
        raise SyntaxError(
            '<{0}>? a1 [{1}] b2 [{2}] caput <[{3}>]'.format(
                quaestio,
                significātus['a1'],
                significātus['b2'],
                caput
            ))

    if significātus['a1'].startswith('#'):
        significātus['_datetime'] = significātus['a1'].startswith('#date')
        if caput.index(significātus['a1']) > -1:
            significātus['a1_indici'] = caput.index(significātus['a1'])
        else:
            SyntaxError('{0} <{1}> <{2}>'.format(
                significātus['a1'], quaestio, caput))

    if significātus['b2'].startswith('#'):
        significātus['_datetime'] = significātus['b2'].startswith('#date')
        if caput.index(significātus['b2']) > -1:
            significātus['b2_indici'] = caput.index(significātus['b2'])
        else:
            SyntaxError('{0} <{1}> <{2}>'.format(
                significātus['b2'], quaestio, caput))

    return significātus


def hxltm__quaestio_significatis_x(
    quaestio: str, caput: list = None, data_referentibus: dict = None
) -> dict:
    """hxltm__quaestio_significatis_i parse a assigment (like add columns)

    Args:
        quaestio (str): query
        caput (list, optional): HXL header. Defaults to None.

    Raises:
        SyntaxError: _description_

    Returns:
        dict: _description_
    """
    # - quaestiō, f, s,  dativus, https://en.wiktionary.org/wiki/significatus
    # - significātīs, m/f/n, s, dativus,
    #     https://en.wiktionary.org/wiki/significatus
    significātus = {
        'opus': None,
        # 'opus_rebus': [],
        'data_referentibus': None,
        'a1': '',
        'a1_indici': None,
        # 'a1_operi': None,
        'b2': '',
        'b2_indici': None,
        # 'b2_operi': None,
        '_datetime': False,
        '__len_before': len(caput),
        '__len_after': len(caput),
    }

    HXLTM_OPERA_X_REG = r'(?P<a1>.*)=(?P<b2>.*)'

    # HXLTM_OPERA_X = {
    #     r'(?P<a1>.*)=(?P<b2>.*)': lambda a1, b3: print('manual'),
    # }
    # for regex_str, _lambda in HXLTM_OPERA_X.items():
    #     # print(regex_str)
    #     _regex_result = re.search(regex_str, quaestio)
    #     if _regex_result:
    #         # print('foi', _regex_result)
    #         # significātus['a1_operi'] = _lambda
    #         significātus['opus'] = _lambda
    #         for _nomen, _res in _regex_result.groupdict().items():
    #             significātus[_nomen] = _res
    #             # significātus['opus_rebus'].append(_nomen)

    # print('    quaestio', quaestio)
    _reg1 = re.search(HXLTM_OPERA_X_REG, quaestio)
    # print('_reg1', _reg1, _reg1.groupdict())
    # print('', _reg1.group('a1'))
    # print('', _reg1.group('b2'))

    if _reg1:
        significātus['a1'] = _reg1.group('a1')
        significātus['b2'] = _reg1.group('b2')

    if significātus['a1'].startswith('#'):
        significātus['_datetime'] = significātus['a1'].startswith('#date')
        # print(significātus['a1'])
        # print(caput)
        # if caput.index(significātus['a1']) > -1:
        if significātus['a1'] in caput:
            significātus['a1_indici'] = caput.index(significātus['a1'])
        else:
            # If is not replacing an existing table, we add at the end
            significātus['a1_indici'] = len(caput)
            significātus['__len_after'] = len(caput) + 1
            # SyntaxError('{0} <{1}> <{2}>'.format(
            #     significātus['a1'], quaestio, caput))

    _b2_okay = False
    if significātus['b2'].startswith('#'):
        _b2_okay = True
        significātus['_datetime'] = significātus['b2'].startswith('#date')
        if caput.index(significātus['b2']) > -1:
            significātus['b2_indici'] = caput.index(significātus['b2'])
        else:
            SyntaxError('{0} <{1}> <{2}>'.format(
                significātus['b2'], quaestio, caput))
    else:
        for regex_str, _lambda in HXLTM_OPERA_2_EX.items():
            # print(regex_str)
            _regex_result = re.search(regex_str, quaestio)
            if _regex_result:
                _b2_okay = True
                for _nomen, _res in _regex_result.groupdict().items():
                    significātus[_nomen] = _res.strip()
                significātus['opus'] = _lambda
                # import inspect
                # print(inspect.getsource(_lambda))

                # print('_regex_result', _regex_result)
                # print('_regex_result items',_regex_result.groupdict().items())
                # print('significātus', significātus)

                # significātus['opus_rebus'].append(_nomen.strip())
                # if _regex_result.group('b2h'):
                #     if caput.index(significātus['b2h']) > -1:
                #         significātus['b2h_indici'] = caput.index(
                #             significātus['b2h'])
                #     else:
                #         SyntaxError('{0} <{1}> <{2}>'.format(
                #             significātus['b2h'], quaestio, caput))
                # print(caput)
                # significātus['b2h_incici'] = \
                #     caput.index(significātus['b2h'])
                # print('foi', _regex_result)
                # print('foi', _regex_result.groupdict().items())
                # significātus['a1_operi'] = _lambda

    if _b2_okay is False:
        SyntaxError('{0} <{1}>'.format(
            'hxltm__quaestio_significatis_x', [quaestio, caput, significātus]))
    # print(significātus)
    # raise NotImplementedError(significātus)

    return significātus


class HXLTMAdRDFSimplicis:
    """HXLTM ad RDF

    - ad (+ accusativus),https://en.wiktionary.org/wiki/ad#Latin
    - HXLTM, https://hxltm.etica.ai/
    - RDF, ...
    - simplicis, m/f/n, s, Gen., https://en.wiktionary.org/wiki/simplex#Latin

    """
    # fōns, m, s, nominativus, https://en.wiktionary.org/wiki/fons#Latin
    fons_configurationi: dict = {}
    # methodus_ex_tabulae: dict = {}
    objectivum_formato: str = 'application/x-turtle'
    # methodus: str = ''

    caput: list = []
    data: list = []
    praefixo: str = ''

    # _hxltm: '#meta+{caput}'

    #  '#meta+{{caput_clavi_normali}}'
    # _hxltm_hashtag_defallo: str = '#meta+{{caput_clavi_normali}}'
    # _hxl_hashtag_defallo: str = '#meta+{{caput_clavi_normali}}'

    # identitās, f, s, nom., https://en.wiktionary.org/wiki/identitas#Latin
    # ex (+ ablative), https://en.wiktionary.org/wiki/ex#Latin
    # locālī, n, s, dativus, https://en.wiktionary.org/wiki/localis#Latin
    # identitas_locali_ex_hxl_hashtag: str = '#item+conceptum+codicem'
    identitas_locali_index: int = -1
    venandum_insectum: bool = False  # noqa
    _hxltm_linguae_index: list = []
    _hxltm_linguae_info: dict = {}
    _hxltm_meta_index: list = []
    _hxltm_meta_info: dict = {}
    _hxltm_unlabeled_index: list = []
    _hxltm_unlabeled_info: dict = {}
    _hxltm_labeled = [
        '#item+conceptum+numerordinatio',
        '#item+conceptum+codicem',
        '#status+conceptum+codicem',
        '#status+conceptum+definitionem',
        '#item+rem+i_qcc+is_zxxx+ix_codexfacto',
    ]

    def __init__(
        self,
        fons_configurationi: dict,
        objectivum_formato: str,
        caput: list = None,
        data: list = None,
        venandum_insectum: bool = False  # noqa
    ):
        """__init__ _summary_

        Args:
            methodus_ex_tabulae (dict):
        """
        self.fons_configurationi = fons_configurationi
        self.objectivum_formato = objectivum_formato
        self.venandum_insectum = venandum_insectum
        self.caput = caput
        self.data = data
        # self.methodus = methodus

        self.praefixo = numerordinatio_neo_separatum(
            self.fons_configurationi['numerordinatio']['praefixo'], ':')

        self._post_init()

    def _post_init(self):
        # @TODO esse desgambiarrizar esse _post_init

        if 'identitas_locali_ex_hxl_hashtag' in \
                self.fons_configurationi['numerordinatio']:
            _test = self.fons_configurationi['numerordinatio']['identitas_locali_ex_hxl_hashtag']
            # print("{0}".format(_test))
            # print("{0}".format(self.caput))
            for item in _test:
                if item in self.caput:
                    # self.identitas_locali_ex_hxl_hashtag = item
                    self.identitas_locali_index = self.caput.index(item)
                    break
            if self.identitas_locali_index == -1:
                raise ValueError("HXLTMAdRDFSimplicis [{0}] ?? <{1}>".format(
                    _test, self.caput))

        for _index, item in enumerate(self.caput):
            attrs = item.replace('#item+rem', '')
            bcp47_simplici = qhxl_hxlhashtag_2_bcp47(attrs)
            # lingua = bcp47_langtag(bcp47_simplici, [
            #     # 'Language-Tag',
            #     'Language-Tag_normalized',
            #     'language'
            # ], strictum=False)
            # bcp47_langtag

            if item not in self._hxltm_labeled:
                # _index = self.caput.index(item)
                if item.startswith('#meta'):
                    self._hxltm_meta_index.append(_index)
                    self._hxltm_meta_info[_index] = {
                        'hxltm_hashtag': item,
                        'bcp47': bcp47_simplici
                    }
                    continue
                self._hxltm_unlabeled_index.append(_index)
                self._hxltm_unlabeled_info[_index] = {
                    'hxltm_hashtag': item,
                    'bcp47': bcp47_simplici
                }

            # Language tags only
            if not item.startswith('#item+rem'):
                continue
            # attrs = item.replace('#item+rem', '')
            # hxlattslinguae = qhxl_attr_2_bcp47(attrs)
            # lingua = bcp47_langtag(hxlattslinguae, [
            #     # 'Language-Tag',
            #     'Language-Tag_normalized',
            #     'language'
            # ], strictum=False)
            if bcp47_simplici and not bcp47_simplici.startswith(('qcc', 'zxx')):
                self._hxltm_linguae_index.append(_index)
                self._hxltm_linguae_info[_index] = {
                    'hxltm_hashtag': item,
                    'bcp47': bcp47_simplici
                }

    def resultatum_ad_csv(self):
        """resultatum ad csv text/csv

        Returns:
            (int): status code
        """
        _writer = csv.writer(sys.stdout)
        _writer.writerow(self.caput)
        _writer.writerows(self.data)
        return EXIT_OK

    # resultātum, n, s, nominativus, https://en.wiktionary.org/wiki/resultatum
    def resultatum_ad_ntriples(self):
        """resultatum ad n triples application/n-triples

        Returns:
            (int): status code
        """
        print('# TODO HXLTMAdRDFSimplicis.resultatum_ad_ntriples')
        print('# ' + str(self.fons_configurationi))

        return EXIT_OK

    # resultātum, n, s, nominativus, https://en.wiktionary.org/wiki/resultatum
    def resultatum_ad_turtle(self):
        """resultatum ad n turtle application/x-turtle

        Returns:
            (int): status code
        """
        print('# [{0}]'.format(self.praefixo))
        print('@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .')
        print('@prefix skos: <http://www.w3.org/2004/02/skos/core#> .')
        print('')
        if self.venandum_insectum:
            print('# @TODO melhorar HXLTMAdRDFSimplicis.resultatum_ad_turtle')
            print('# fons_configurationi ' + str(self.fons_configurationi))
            print('# _hxltm_unlabeled_info ' + str(self._hxltm_unlabeled_info))
            print('# _hxltm_meta_info ' + str(self._hxltm_meta_info))
            print('# _hxltm_linguae_info ' + str(self._hxltm_linguae_info))
            print('')
            print('# @TODO adicionar mais prefixos de '
                  'https://www.wikidata.org/wiki/EntitySchema:E49')
            print('')
        # print('<urn:1603:63:101> a skos:ConceptScheme ;')
        # print('  skos:prefLabel "1603:63:101"@mul-Zyyy-x-n1603 .')
        print("<urn:{0}> a skos:ConceptScheme ; \n"
              "  skos:prefLabel \"{0}\"@mul-Zyyy-x-n1603 .".format(
                  self.praefixo))
        print('  # @TODO skos:hasTopConcept')
        print('')

        # @TODO: implementar qhx-Latn (HXLStandard), refs
        #        https://github.com/EticaAI/hxltm/blob/main/docs
        #        /codex-simplex-ontologiae/ontologia.yml

        for linea in self.data:
            # print('# {0}'.format(linea))
            # print('# {0}'.format(self.identitas_locali_index))
            # _codex_locali = self.quod(
            #     linea, '#item+rem+i_qcc+is_zxxx+ix_wikip1585')
            _codex_locali = str(int(linea[self.identitas_locali_index]))
            print('<urn:{0}:{1}> a skos:Concept ;'.format(
                self.praefixo,
                _codex_locali
            ))
            # print('  skos:prefLabel "{0}:{1}"@mul-Zyyy-x-n1603 .'.format(
            print('  skos:prefLabel "{0}:{1}"@mul-Zyyy-x-n1603 ;'.format(
                self.praefixo,
                _codex_locali
            ))
            _skos_related = []
            _skos_related_raw = []
            for _index, item in enumerate(linea):
                if item and _index in self._hxltm_unlabeled_index and \
                        self._hxltm_unlabeled_info[_index]['bcp47']:
                    _skos_related_raw.append('"{0}"@{1}'.format(
                        item.replace('"', '\\"'),
                        self._hxltm_unlabeled_info[_index]['bcp47']
                    ))
                    # pass

            # @TODO add other related
            _skos_related = _skos_related_raw
            # linguae = self._quod_linguae(res)
            if len(_skos_related) > 0:
                print("  skos:related\n    {0} .".format(
                    " ,\n    ".join(_skos_related_raw)
                ))
            for _index, item in enumerate(linea):
                # if len(item) and _index in self._hxltm_unlabeled_index:
                #     print('  # {0} [{1}]'.format(
                #         self._hxltm_unlabeled_info[_index]['hxltm_hashtag'], item))
                if self.venandum_insectum:
                    if len(item) and _index in self._hxltm_meta_index:
                        print('  # verbose: {0} [{1}]'.format(
                            self._hxltm_meta_info[_index]['hxltm_hashtag'],
                            item))

            # linguae = self._quod_linguae(res)
            # if len(linguae) > 0:
            #     print("  skos:prefLabel\n    {0} .".format(
            #         " ,\n    ".join(linguae)
            #     ))

            print('')

        return EXIT_OK

    def quod(self, linea: list, caput_item: str) -> str:
        if caput_item in self.caput:
            index = self.caput.index(caput_item)
            # print('## {0}'.format(linea))
            # print('## {0}'.format(linea[index]))
            return linea[index]
        return ''


def hxltm_adde_columna(
    caput: list, data: list, quaestio: str, data_referentibus: dict = None
) -> Tuple[list, list]:
    """hxltm_cum_columna add new column (variables)
    Trivia:
      - cum (+ ablativus), https://en.wiktionary.org/wiki/cum#Latin
      - columnā, s, f, ablativus, https://en.wiktionary.org/wiki/columna#Latin
      - adde, verbum, sing, imper. https://en.wiktionary.org/wiki/addo#Latin
    Args:
        caput (list): _description_
        data (list): _description_
        quaestio (str): _description_
        data_referentibus (dict): Pre-loaded external referential data
    Returns:
        Tuple[list, list]: _description_
    """

    # https://en.wiktionary.org/wiki/columna#Latin
    significātus = hxltm__quaestio_significatis_x(
        quaestio, caput, data_referentibus)

    caput_novo = caput
    caput_novo.append(significātus['a1'])
    data_novis = []

    # caput.append(significātus['a1'])
    for _, linea in enumerate(data):
        linea_novae = []
        linea_novae.extend(linea)
        if significātus['opus']:
            # import inspect
            # print(inspect.getsource(significātus['opus']))
            res = significātus['opus'](
                significātus,
                caput_novo,
                linea_novae,
                data_referentibus
            )
        else:
            # @TODO: potential bug or simpler cases
            if 'b2' in significātus:
                res = significātus['b2']

        linea_novae.append(res)
        data_novis.append(linea_novae)
        # data[index] = data[index].append(significātus['a1'])

    # print('significātus', significātus)
    # raise NotImplementedError('{0} {1}'.format(
    #     'hxltm_cum_columna', quaestio))
    # # print(caput, columnae)
    # for item in columnae:
    #     index_columnae.append(caput.index(item))

    # raise NotImplementedError(data_novis)
    # _caput = columnae
    return caput_novo, data_novis


def hxltm_carricato(
    archivum_trivio: str = None,
    est_stdin: bool = False,
    punctum_separato=","
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

    if est_stdin:
        _data = []
        for linea in sys.stdin:
            if len(caput) == 0:
                # caput = linea
                # _reader_caput = csv.reader(linea)
                _gambi = [linea, linea]
                _reader_caput = csv.reader(_gambi, delimiter=punctum_separato)
                caput = next(_reader_caput)
            else:
                _data.append(linea)
        _reader = csv.reader(_data)
        return caput, list(_reader)
    # else:
    #     fons = archivum_trivio
    data = []
    with open(archivum_trivio, 'r') as _fons:
        _csv_reader = csv.reader(_fons, delimiter=punctum_separato)
        for linea in _csv_reader:
            if len(caput) == 0:
                # caput = linea
                # _reader_caput = csv.reader(linea)
                # _gambi = [linea, linea]
                # _reader_caput = csv.reader(_gambi)
                # caput = next(_reader_caput)
                caput = linea
            else:
                data.append(linea)
            # print(row)

    # for line in fons:
    #     print(line)
        # json_fonti_texto += line

    # _reader = csv.reader(_data)
    # return caput, list(_reader)
    return caput, data


def hxltm_cum_ordinibus_ex_columnis(
    caput: list, data: list, quaestio: list, data_referentibus: dict = None
) -> Tuple[list, list]:
    """hxltm_cum_columnis_desideriis with preferred order (not enforced)

    Trivia:
      - cum (+ ablativus), https://en.wiktionary.org/wiki/cum#Latin
      - ōrdinibus, pl, m, ablativus, https://en.wiktionary.org/wiki/ordo#Latin
      - ex (+ ablativus) https://en.wiktionary.org/wiki/ex#Latin
      - columnā, s, f, ablativus, https://en.wiktionary.org/wiki/columna#Latin
      - columnīs, pl, f, ablativus,
      - columnae, pl, f, vocātīvus,
      - dēsīderiīs, pl, n, vocātīvus,

    Args:
        caput (list): _description_
        data (list): _description_
        quaestio (str): _description_
        data_referentibus (dict): Pre-loaded external referential data

    Returns:
        Tuple[list, list]: _description_
    """
    # _ordo_novo = []
    caput_novo = []
    data_novis = []
    quaestio_dict = {}
    for index, item in enumerate(caput):
        quaestio_dict[int(index)] = item

    # print('pre quaestio_dict', quaestio_dict)
    for item in quaestio:
        # print(item)
        if item.find(':') == -1:
            raise SyntaxError('{0} ":" et <{1}>?? <{2}>'.format(
                __name__, item, quaestio
            ))
        _num, _hash = item.split(':')
        if _num.lstrip('+-').isnumeric():
            _num = int(_num)
        else:
            raise SyntaxError('{0} "numero" et <{1}> <{2}>?? <{3}>'.format(
                __name__, _num, item, quaestio
            ))

        quaestio_dict[int(_num)] = _hash
    # print('post quaestio_dict', quaestio_dict)
    # ordo_novo = set()
    ordo_novo = []

    # print(sorted(quaestio_dict.items(), key=lambda item: int(item[0])))
    quaestio_dict_sorted = \
        sorted(quaestio_dict.items(), key=lambda item: int(item[0]))

    for index, item in quaestio_dict_sorted:
        # print('quaestio_dict_sorted item', item)
        if item in caput and caput.index(item) not in ordo_novo:
            # print(item, caput.index(item))
            ordo_novo.append(caput.index(item))

    # print('   ordo_novo', ordo_novo)

    # return [], [[]]
    # for index in enumerate(ordo_novo):
    for index in ordo_novo:
        caput_novo.append(caput[index])

    # print(caput)
    # print(caput_novo)
    # print(list(range(0, len(caput) -1)))
    if caput_novo == caput:
        # print('already equal. return same input')
        return caput, data

    for _, linea in enumerate(data):
        linea_novae = []
        for index in ordo_novo:
            linea_novae.append(linea[index])
        # linea_novae.extend(linea)
        data_novis.append(linea_novae)

    return caput_novo, data_novis


def hxltm_cum_aut_sine_columnis_simplicibus(
    caput: list, data: list, columnae: list,
    _data_referentibus: dict = None, cum_columnis: bool = True
) -> Tuple[list, list]:
    """hxltm_cum_aut_sine_columnis_simplicibus select/exclude only these columns

    This function will not do advanced checks.

    Trivia:
      - cum (+ ablativus), https://en.wiktionary.org/wiki/cum#Latin
      - columnīs, pl, f, ablativus, https://en.wiktionary.org/wiki/columna#Latin
      - columnae, pl, f, vocātīvus,
      - columnae, pl, f, nominativus,
      - simplicibus, pl, m/f/n, dativus https://en.wiktionary.org/wiki/simplex

    Args:
        caput (list): _description_
        data (list): _description_
        quaestio (str): _description_
        data_referentibus (dict): Pre-loaded external referential data

    Returns:
        Tuple[list, list]: _description_
    """

    # https://en.wiktionary.org/wiki/columna#Latin
    index_columnae = []
    _data = []
    caput_novo = []
    data_novis = []
    # print('    caput', caput)
    # print('    columnae', columnae)
    if cum_columnis:
        for item in columnae:
            caput_indici = caput.index(item)
            index_columnae.append(caput_indici)
            caput_novo.append(caput[caput_indici])
    else:
        for item in caput:
            if item not in columnae:
                caput_indici = caput.index(item)
                index_columnae.append(caput_indici)
                caput_novo.append(caput[caput_indici])

    # @TODO: return same data if the caput are equal

    for linea in data:
        _linea = []
        for index in index_columnae:
            _linea.append(linea[index])
        data_novis.append(_linea)

    return caput_novo, data_novis


def hxltm_cum_filtro(
        caput: list, data: list, quaestio: list, data_referentibus: dict = None
) -> Tuple[list, list]:
    """hxltm_cum_filtris Apply filters for existing columns.

    Trivia:
      - cum (+ ablativus), https://en.wiktionary.org/wiki/cum#Latin
      - filtrō, n, s, ablativus, https://en.wiktionary.org/wiki/filtrum#Latin
      - filtrīs, n, pl, ablativus, https://en.wiktionary.org/wiki/filtrum#Latin

    Args:
        caput (list): _description_
        data (list): _description_
        quaestio (list): The query
        data_referentibus (dict): Pre-loaded external referential data

    Returns:
        Tuple[list, list]: _description_
    """
    # https://en.wiktionary.org/wiki/columna#Latin

    significātus = hxltm__quaestio_significatis_i(quaestio, caput)

    # @TODO: maybe implement only appli filters if match a rule
    for _index, linea in enumerate(data):
        data[_index][significātus['a1_indici']] = significātus['opus'](
            data[_index][significātus['a1_indici']]
        )

    return caput, data


# def hxltm_ex_columnis(
def hxltm_sine_columnis(
        caput: list, data: list, columnae: list, data_referentibus: dict = None
) -> Tuple[list, list]:
    """hxltm_sine_columnis cut columns (variables)

    Trivia:
      - ex (+ ablativus), https://en.wiktionary.org/wiki/ex#Latin
      - sine (+ ablativus), https://en.wiktionary.org/wiki/sine#Latin
      - columnīs, f, pl, ablativus, https://en.wiktionary.org/wiki/columna#Latin

    Args:
        caput (list): _description_
        data (list): _description_
        columnae (list): _description_
        data_referentibus (dict): Pre-loaded external referential data

    Returns:
        Tuple[list, list]: _description_
    """
    raise DeprecationWarning('use hxltm_sine_columnis')


# def hxltm_sine_columnis(
#         caput: list, data: list, columnae: list, _data_referentibus: dict = None
# ) -> Tuple[list, list]:
#     """hxltm_sine_selectis _summary_

#     Trivia:
#       - sine (+ ablativus), https://en.wiktionary.org/wiki/sine#Latin
#       - columnīs, f, pl, ablativus, https://en.wiktionary.org/wiki/columna#Latin

#     Args:
#         caput (list): _description_
#         data (list): _description_
#         columnae (list): _description_
#         data_referentibus (dict): Pre-loaded external referential data

#     Returns:
#         Tuple[list, list]: _description_
#     """
#     pass


def hxltm_ex_selectis(
        caput: list, data: list, quaestio: str, data_referentibus: dict = None
) -> Tuple[list, list]:
    """hxltm_ex_selectis select rows (lines of data)

    Args:
        caput (list): _description_
        data (list): _description_
        quaestio (list): The query
        data_referentibus (dict): Pre-loaded external referential data

    Returns:
        Tuple[list, list]: _description_
    """
    # _op_list = ['==', '!=', '<', '>=', '>', '<=']
    _op_list = HXLTM_OPERA_2.keys()
    res_1 = ''
    res_1_isdate = False
    res_2 = ''
    res_2_isdate = False
    op = ''
    _data = []

    significātus = hxltm__quaestio_significatis_ii(quaestio, caput)

    for linea in data:
        a1 = significātus['a1']
        b2 = significātus['b2']

        if significātus['a1_indici'] is not None:
            a1 = linea[significātus['a1_indici']]
        if significātus['b2_indici'] is not None:
            b2 = linea[significātus['b2_indici']]

        if significātus['_datetime'] is True:
            a1 = date.fromisoformat(a1)
            b2 = date.fromisoformat(b2)

        op_signifo = HXLTM_OPERA_2[significātus['opus']](a1, b2)
        if op_signifo == True:
            _data.append(linea)
        # else:
        #     print('DEBUG: skip [<{0}> {1} <{2}>]'.format(
        #         _value_1, op, _value_2))
    return caput, _data


def hxltm_index_praeparationi(
    caput: list, data: list,
    index_ad_columnam: str = None, strictum: bool = False
) -> dict:
    """hxltm_index_praeparationi add new columns (variables)

    Trivia:
      - index, s, m, nominativus, https://en.wiktionary.org/wiki/index#Latin
      - ad (+ accusativus) https://en.wiktionary.org/wiki/ad#Latin
      - columnam, s, f, acc., https://en.wiktionary.org/wiki/columna#Latin

    Args:
        caput (list): _description_
        data (list): _description_
        index_ad_columnam (str): _description_
        strictum (str): raise errors if same source keys can point to different
                        objective indexes.

    Returns:
        dict: _description_
    """

    # print('caput', caput)

    if strictum:
        raise NotImplementedError('{0} strictum'.format(
            'hxltm_index_praeparationi'))

    if not index_ad_columnam:
        index_ad_columnam = 0
    else:
        index_ad_columnam = caput.index(index_ad_columnam)

    _data_json = {}
    data_json = {}

    for linea in data:
        _clavis_ad = linea[index_ad_columnam]
        _clavis_ex = set()
        for res in linea:
            if res:
                _clavis_ex.add(res)
        for item in _clavis_ex:
            _data_json[item] = _clavis_ad

    _claves_n = []
    _claves_l = []
    _clāvēs_nl = []

    for item in _data_json.keys():
        if item.isnumeric():
            _claves_n.append(item)
        else:
            _claves_l.append(item)

    if len(_claves_n) > 0:
        _clāvēs_nl.extend(sorted(_claves_n, key=lambda x: int(x)))

    if len(_claves_l) > 0:
        _claves_l.sort(key=lambda item: (len(item), item))
        _clāvēs_nl.extend(_claves_l)

    for item in _clāvēs_nl:
        data_json[item] = _data_json[item]

    return data_json


# def hxltm_per_columnas(
#         caput: list, data: list, columnae: list) -> Tuple[list, list]:
#     """hxltm_per_columnas Apply filters to existing columns.

#     Trivia:
#       - per (+ accusative), https://en.wiktionary.org/wiki/per#Latin
#         - through, by means of
#           - Qua re per exploratores nuntiata
#       - columnās, f, pl, accusativus, https://en.wiktionary.org/wiki/columna

#     Args:
#         caput (list): _description_
#         data (list): _description_
#         columnae (list): _description_

#     Returns:
#         Tuple[list, list]: _description_
#     """
#     # https://en.wiktionary.org/wiki/columna#Latin
#     index_columnae = []
#     _data = []
#     raise NotImplementedError('@TODO implement add new column features')
#     # print(caput, columnae)
#     for item in columnae:
#         index_columnae.append(caput.index(item))

#     for linea in data:
#         _linea = []
#         for index in index_columnae:
#             _linea.append(linea[index])
#         _data.append(_linea)

#     # _caput = columnae
    return columnae, _data


def qhxl_hxlhashtag_2_bcp47(
        hxlhashtag: str, hxlstd11_compat: bool = False) -> str:
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


def numerordinatio_descendentibus(
        numerordinatio: str, collectio: list, ordo_maximo: int = None) -> list:
    """numerordinatio_descendentibus _summary_

    Trivia:
     - collēctiō, s, f, , nominativus
    - dēscendentibus, pl, m/f/n, , dativus,
        https://en.wiktionary.org/wiki/descendens#Latin
    - ōrdō, s, m, nominativus, https://en.wiktionary.org/wiki/ordo#Latin
    - ōrdinī, s, m, dativus,
    - maximō, s, m/n, dativus, https://en.wiktionary.org/wiki/maximus#Latin

    Args:
        numerordinatio (str): _description_
        collectio (list): _description_
        ordo_maximo (int, optional): _description_. Defaults to None.

    Returns:
        list: _description_
    """

    resultatum = []

    if ordo_maximo is not None:
        ordo_maximo = ordo_maximo + numerordinatio_ordo(numerordinatio)

    for item in collectio:
        if item.startswith(numerordinatio) and item != numerordinatio:
            if ordo_maximo is None:
                resultatum.append(item)
            else:
                item_ordini = numerordinatio_ordo(item)
                if item_ordini <= ordo_maximo:
                    resultatum.append(item)

    return resultatum


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


class OntologiaSimplici:
    """Ontologia Simplicī


    Trivia:
    - ontologia, ---, https://en.wiktionary.org/wiki/ontologia#Latin
    - simplicī, s, m/f/b, dativus, https://en.wiktionary.org/wiki/simplex
    - ex (+ ablativus), https://en.wiktionary.org/wiki/ex#Latin
    - rādīcī, s, f, dativus, https://en.wiktionary.org/wiki/radix#Latin
    - archīvō, s, n, dativus, https://en.wiktionary.org/wiki/archivum

    @see https://www.w3.org/2001/sw/BestPractices/OEP/SimplePartWhole
    @see https://www.w3.org/TR/owl2-overview/#Overview

    """

    # No 1603 prefix
    ontologia_radici: str = None

    # dictionaria_radici: This affects how we infer "classes".
    # Without this we may make partsOf as if they're classes,
    # which may be wrong
    dictionaria_radici: str = None

    ordo_radici: int = None
    data_apothecae_ex: str = []
    caput_no1: List[str] = None
    data: List[list] = None

    PRAEFIXUM = [
        '@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .',
        '@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .',
        '@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .',
        '@prefix owl: <http://www.w3.org/2002/07/owl#> .',
        '@prefix skos: <http://www.w3.org/2004/02/skos/core#> .',
        '@prefix p: <http://www.wikidata.org/prop/> .'
    ]

    PARENTES = []

    def __init__(
        self,
        ontologia_radici: str,
        ontologia_ex_archivo: str,
        dictionaria_radici: str = None
    ):

        self.ontologia_radici = numerordinatio_neo_separatum(
            ontologia_radici, ':')
        self.ontologia_ex_archivo = ontologia_ex_archivo
        if dictionaria_radici:
            self.dictionaria_radici = numerordinatio_neo_separatum(
                dictionaria_radici, ':')
        else:
            self.dictionaria_radici = self.ontologia_radici

        self.initiari()

    def initiari(self):
        """initiarī

        Trivia:
        - initiārī, https://en.wiktionary.org/wiki/initio#Latin
        """
        self.caput_no1, self.data = hxltm_carricato(self.ontologia_ex_archivo)

        if self.caput_no1[0] != '#item+conceptum+numerordinatio':
            raise SyntaxError('Non [{0}] index 0 ad [{1}]'.format(
                '#item+conceptum+numerordinatio',
                self.ontologia_ex_archivo
            ))

        if self.caput_no1[1] != '#item+conceptum+codicem':
            raise SyntaxError('Non [{0}] index 1 ad [{1}]'.format(
                '#item+conceptum+codicem',
                self.ontologia_ex_archivo
            ))

        self.ordo_radici = numerordinatio_ordo(self.ontologia_radici)

        _parents__parts = self.dictionaria_radici.split(':')
        _parents__parens = []
        # print('oi', _parents__parts)
        for item in _parents__parts:
            if len(_parents__parens) == 0:
                self.PARENTES.append(
                    '<urn:{0}> rdf:type owl:Ontology .'.format(item))
                self.PARENTES.append(
                    '<urn:{0}> rdf:type owl:Class .'.format(item))
                self.PARENTES.append('')
                _parents__parens.append(item)
                continue

            # if len(_parents__parens) > 0:
            #     # _parents__parens.append(item)
            #     # _aa =
            #     numerordinatio_nunc = ':'.join(_parents__parens)
            # else:
            #     # numerordinatio_nunc = item

            #     self.PARENTES.append(
            #         '<urn:{0}> rdf:type owl:Ontology .'.format(item))
            #     _parents__parens.append(item)
            #     continue
            _parents__parens_old = list(_parents__parens)
            _parents__parens.append(item)
            numerordinatio_nunc = ':'.join(_parents__parens)

            self.PARENTES.append(
                '<urn:{0}> rdf:type owl:Class .'.format(numerordinatio_nunc))
            self.PARENTES.append(
                '<urn:{0}> rdfs:subClassOf <urn:{1}> .'.format(
                    numerordinatio_nunc, ':'.join(_parents__parens_old)))
            # if len(_parents__parens) > 0:
            #     self.PARENTES.append(
            #         '<urn:{0}> rdfs:subClassOf <urn:{1}> .'.format(
            #             numerordinatio_nunc, ':'.join(_parents__parens)))

            self.PARENTES.append('')
        # self.PARENTES = []
        # pass

    def imprimere_ad_tabula(self, punctum_separato: str = ","):
        csv_imprimendo(
            self.caput_no1, self.data, punctum_separato=punctum_separato)
        # return self.resultatum


class OntologiaSimpliciAdOWL(OntologiaSimplici):
    def imprimere_ad_owl(self, punctum_separato: str = ","):
        # - part of (P361)
        #   - https://www.wikidata.org/wiki/Property:P361
        #   - https://www.wikidata.org/wiki/Special:EntityData/P361.ttl
        # - has part or parts (P527)
        #   - https://www.wikidata.org/wiki/Property:P527
        #   - https://www.wikidata.org/wiki/Special:EntityData/P527.ttl
        # - inverse property (P1696)
        #   - https://www.wikidata.org/wiki/Property:P1696
        #   - https://www.wikidata.org/wiki/Property_talk:P1696
        # - https://www.wikidata.org/wiki/EntitySchema:E49
        # ObjectInverseOf
        # owl:inverseOf
        #
        # @TODO parse list of wikidata properties
        # https://www.wikidata.org/wiki/Property:P31

        paginae = []
        paginae.append('# {0}'.format(self.ontologia_radici))
        paginae.extend(self.PRAEFIXUM)
        paginae.append('')
        paginae.append('p:P361 rdf:type owl:ObjectProperty .')
        paginae.append('p:P1696 rdf:type owl:ObjectProperty .')
        paginae.append('p:P361 owl:inverseOf p:P1696 .')
        paginae.append('')
        paginae.extend(self.PARENTES)
        paginae.append('')

        ordo_nunc = self.ordo_radici
        parēns = {
            ordo_nunc: self.ontologia_radici
        }
        # print(parēns)
        for linea in self.data:
            numerordinatio_nunc = numerordinatio_neo_separatum(linea[0], ':')
            if numerordinatio_nunc.startswith(
                    self.ontologia_radici + ':0:1603'):
                continue

            ordo_nunc = numerordinatio_ordo(linea[0])
            parēns[ordo_nunc] = numerordinatio_nunc
            numerordinatio_parentī = parēns[ordo_nunc - 1]

            # paginae.append('# {0} {1} {2}'.format(
            #     linea[0], linea[1], ordo_nunc))

            paginae.append('<urn:{0}> p:P361 <urn:{1}> .'.format(
                numerordinatio_nunc, numerordinatio_parentī,
                parēns[ordo_nunc]))

            paginae.append(
                '<urn:{0}> rdfs:Literal "{1}" .'.format(
                    numerordinatio_nunc, numerordinatio_nunc,
                    parēns[ordo_nunc]))

            paginae.append('')
            # ordo_nunc = self.ordo_radici
            # parēns = self.ontologia_radici

        ttl_imprimendo(paginae)


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


class TabulaAdHXLTM:
    """Tabula ad HXLTM

    - tabula, f, s, nominativus, https://en.wiktionary.org/wiki/tabula
    - ad (+ accusativus),https://en.wiktionary.org/wiki/ad#Latin
    - ex (+ ablativus)
    - HXLTM, https://hxltm.etica.ai/

    """
    methodus_ex_tabulae: dict = {}
    # methodus_ex_tabulae: dict = {}
    objectivum_formato: str = 'hxltm_csv'
    methodus: str = ''

    # _hxltm: '#meta+{caput}'

    #  '#meta+{{caput_clavi_normali}}'
    _hxltm_hashtag_defallo: str = '#meta+{{caput_clavi_normali}}'
    _hxl_hashtag_defallo: str = '#meta+{{caput_clavi_normali}}'

    def __init__(
        self,
        methodus_ex_tabulae: dict,
        objectivum_formato: str,
        methodus: str,
    ):
        """__init__ _summary_

        Args:
            methodus_ex_tabulae (dict):
        """
        self.methodus_ex_tabulae = methodus_ex_tabulae
        self.objectivum_formato = objectivum_formato
        self.methodus = methodus

    def caput_translationi(self, caput: list) -> list:
        """Caput trānslātiōnī

        - trānslātiōnī, f, s, dativus, https://en.wiktionary.org/wiki/translatio
        - caput, n, s, nominativus, https://en.wiktionary.org/wiki/caput#Latin

        Args:
            caput (list): _description_

        Returns:
            list: _description_
        """

        # if self.objectivum_formato.find('hxltm') > -1:
        #     # neo_caput = map(self.clavis_ad_hxl, caput, 'hxltm')
        #     # neo_caput = map(self.clavis_ad_hxl, caput, 'hxltm')
        #     neo_caput = map(self.clavis_ad_hxl, caput)
        #     # neo_caput = map(self.clavis_ad_hxl, caput)
        # if self.objectivum_formato.find('hxl') > -1:
        #     # neo_caput = map(self.clavis_ad_hxl, caput, 'hxl')
        #     neo_caput = map(self.clavis_ad_hxl, caput)
        if self.objectivum_formato.find('hxl') > -1:
            neo_caput = map(self.clavis_ad_hxl, caput)
        else:
            neo_caput = map(self.clavis_normationi, caput)
        return neo_caput

    def clavis_normationi(self, clavis: str) -> str:
        """clāvis nōrmātiōnī

        - clāvis, f, s, normativus, https://en.wiktionary.org/wiki/clavis#Latin
        - nōrmātiōnī, f, s, dativus, https://en.wiktionary.org/wiki/normatio

        Args:
            clavis (str):

        Returns:
            str:
        """
        if not clavis or len(clavis) == 0:
            return ''
        clavis_normali = clavis.strip().lower()\
            .replace(' ', '_').replace('-', '_')

        return clavis_normali

    # def clavis_ad_hxl(self, clavis: str, classis: str = 'hxltm') -> str:
    def clavis_ad_hxl(self, clavis: str) -> str:
        """clavis_ad_hxltm

        - clāvis, f, s, normativus, https://en.wiktionary.org/wiki/clavis#Latin
        - nōrmātiōnī, f, s, dativus, https://en.wiktionary.org/wiki/normatio

        Args:
            clavis (str):

        Returns:
            str:
        """
        clavis_normationi = self.clavis_normationi(clavis)

        if not clavis or len(clavis) == 0:
            return ''
        # print(classis)
        # neo_caput = 'hxl_hashtag'
        # forma = self._hxl_hashtag_defallo
        # if classis == 'hxltm' or not classis:
        if self.objectivum_formato.find('hxltm') > -1:
            neo_caput = 'hxltm_hashtag'
            forma = self._hxltm_hashtag_defallo
        # elif classis == 'hxl':
        elif self.objectivum_formato.find('hxl') > -1:
            neo_caput = 'hxl_hashtag'
            forma = self._hxl_hashtag_defallo

        if clavis_normationi in self.methodus_ex_tabulae['caput'].keys():
            if self.methodus_ex_tabulae['caput'][clavis_normationi] and \
                neo_caput in self.methodus_ex_tabulae['caput'][clavis_normationi] and \
                    self.methodus_ex_tabulae['caput'][clavis_normationi][neo_caput]:
                forma = self.methodus_ex_tabulae['caput'][clavis_normationi][neo_caput]

        hxl_hashtag = forma.replace(
            '{{caput_clavi_normali}}', clavis_normationi)

        return hxl_hashtag

    # def clavis_ad_hxl(self, clavis: str) -> str:
    #     pass


class TabulaSimplici:
    """Tabula simplicī /Simple Table/@eng-Latn

    Trivia:
    - tabula, s, f, nominativus, https://en.wiktionary.org/wiki/tabula#Latin
    - simplicī, s, m/f/n, Dativus, https://en.wiktionary.org/wiki/simplex#Latin
    """

    archivum_trivio: str = ''
    nomen: str = ''
    statum: bool = None
    caput: list = []
    concepta: dict = None
    res_totali: int = 0
    ex_radice: bool = False
    archivum_trivio_ex_radice: str = ''
    archivum_nomini: str = ''
    # codex_opus: list = []
    # opus: list = []
    # in_limitem: int = 0
    # in_ordinem: str = None
    # quaero_numerordinatio: list = []

    def __init__(
        self,
        archivum_trivio: str,
        nomen: str,
        ex_radice: bool = False
    ):
        self.archivum_trivio = archivum_trivio
        self.nomen = nomen
        self.ex_radice = ex_radice
        # self.initiari()

    def _initiari(self):
        """initiarī

        Trivia:
        - initiārī, https://en.wiktionary.org/wiki/initio#Latin
        """
        if not os.path.exists(self.archivum_trivio):
            # print('self.archivum_trivio', self.archivum_trivio)
            self.statum = False
            return self.statum

        self.archivum_trivio_ex_radice = \
            self.archivum_trivio.replace(NUMERORDINATIO_BASIM, '')

        self.archivum_nomini = Path(self.archivum_trivio_ex_radice).name

        with open(self.archivum_trivio) as csvfile:
            reader = csv.reader(csvfile)
            for lineam in reader:
                if len(self.caput) == 0:
                    self.caput = lineam
                    continue
                # TODO: what about empty lines?
                self.res_totali += 1

        self.statum = True
        return self.statum

    def _initiari_v2(self):
        """initiarī

        Trivia:
        - initiārī, https://en.wiktionary.org/wiki/initio#Latin
        """
        if not os.path.exists(self.archivum_trivio):
            self.statum = False
            return self.statum

        self.archivum_trivio_ex_radice = \
            self.archivum_trivio.replace(NUMERORDINATIO_BASIM, '')

        self.archivum_nomini = Path(self.archivum_trivio_ex_radice).name

        self.concepta = {}
        with open(self.archivum_trivio) as csvfile:
            reader = csv.DictReader(csvfile)
            for lineam in reader:
                # de_codex = lineam['#item+conceptum+numerordinatio']
                de_codex = lineam['#item+conceptum+codicem']
                self.concepta[de_codex] = lineam
                # if len(self.caput) == 0:
                #     self.caput = lineam
                #     continue
                # # TODO: what about empty lines?
                # self.res_totali += 1

        self.statum = True
        return self.statum

    def _quod_linguae(self, res: dict) -> list:
        resultatum = []
        # resultatum.append('"todo"@en')
        for clavem, item in res.items():
            if not clavem.startswith('#item+rem') or len(item) == 0:
                continue
            if item.find('"') > -1:
                # item = item.replace('"', 'zzzz')
                item = item.replace('"', '\\"')
            attrs = clavem.replace('#item+rem', '')
            hxlattslinguae = qhxl_attr_2_bcp47(attrs)
            # lingua = bcp47_langtag(clavem, [
            lingua = bcp47_langtag(hxlattslinguae, [
                # 'Language-Tag',
                'Language-Tag_normalized',
                'language'
            ], strictum=False)
            if lingua['language'] not in ['qcc', 'zxx']:
                resultatum.append('"{0}"@{1}'.format(
                    item, lingua['Language-Tag_normalized']))
        return resultatum

    def _quod_descendentia(
            self, dictionaria_codici: list, item_codici: str) -> list:
        # dēscendentia, n, pl, Nominativus,
        #     https://en.wiktionary.org/wiki/descendens#Latin
        resultatum = []

        # de_codex_n = numerordinatio_progenitori(de_codex, ':')

        # for clavem, _item in dictionaria_radici.items():
        for clavem in dictionaria_codici:
            # clavem_n = numerordinatio_progenitori(clavem, ':')
            # print('clavem', de_codex_n, clavem_n)
            progenitor = numerordinatio_progenitori(clavem, ':')
            # print('clavem', item_codici, progenitor)
            if progenitor == item_codici:
                resultatum.append(clavem)
            # pass
        return resultatum

    def praeparatio(self):
        """praeparātiō

        Trivia:
        - praeparātiō, s, f, Nom., https://en.wiktionary.org/wiki/praeparatio
        """
        self._initiari()
        return self.statum

    def quod_datapackage(self) -> dict:
        if self.ex_radice is True:
            _path = self.archivum_trivio_ex_radice
        else:
            _path = self.archivum_nomini

        resultatum = {
            'name': self.nomen,
            # 'path': self.nomen,
            'path': _path,
            'profile': 'tabular-data-resource',
            'schema': {
                'fields': []
            },
            'stats': {
                'fields': len(self.caput),
                'rows': self.res_totali,
            }
        }

        for caput_rei in self.caput:
            item = {
                'name': caput_rei,
                # TODO: actually get rigth type from reference dictionaries
                'type': 'string',
            }
            resultatum['schema']['fields'].append(item)

        return resultatum

    def quod_rdf_skos_ttl_concepta(self) -> list:
        self._initiari_v2()

        paginae = []

        nomen_radici = numerordinatio_neo_separatum(self.nomen, ':')

        # https://www.w3.org/2015/03/ShExValidata/ (near ok)
        # https://skos-play.sparna.fr/skos-testing-tool (needs more work)
        # paginae.append("<urn:{0}> a skos:Concept ;".format(nomen_radici))
        paginae.append("<urn:{0}> a skos:ConceptScheme ;".format(nomen_radici))
        # paginae.append("  skos:prefLabel\n    {0} .".format(
        #     ",\n    ".join(linguae)
        # ))
        paginae.append("  skos:prefLabel \"{0}\"@{1} .".format(
            nomen_radici,
            'mul-Zyyy-x-n1603'
        ))
        paginae.append('')

        dictionaria_codici = []

        # for codex_de, res in enumerate(self.concepta):
        for codex_de, _res in self.concepta.items():
            codex_de_n = numerordinatio_neo_separatum(codex_de, ':')
            numerodinatio = nomen_radici + ':' + str(codex_de_n)
            dictionaria_codici.append(numerodinatio)

        for codex_de, res in self.concepta.items():

            codex_de_n = numerordinatio_neo_separatum(codex_de, ':')
            if codex_de_n.startswith('0:1603'):
                continue
            # This is deprecated use; used on 1603_25_1
            if codex_de_n.startswith('0:999'):
                continue
            numerodinatio = nomen_radici + ':' + str(codex_de_n)
            # paginae.append(':{0} a skos:Concept ;'.format(codex_de))
            paginae.append("<urn:{0}> a skos:Concept ;".format(numerodinatio))

            progenitor = numerordinatio_progenitori(numerodinatio, ':')

            if nomen_radici == progenitor:
                paginae.append('  skos:topConceptOf\n    <urn:{0}> ;'.format(
                    progenitor))

            descendentia = self._quod_descendentia(
                dictionaria_codici, numerodinatio)
            if len(descendentia) > 0:
                # print('descendentia', descendentia)
                # paginae.append('  skos:broader\n    {0} ;'.format(
                paginae.append('  skos:narrower\n    {0} ;'.format(
                    ' ,\n    '.join(
                        map(lambda x: '<urn:' + x + '>', descendentia))
                ))

            # paginae.append('  rdfs:subClassOf <urn:{0}> ;'.format(
            #     progenitor
            # ))
            # paginae.append('  skos:narrowerTransitive <urn:{0}> ;'.format(
            # paginae.append('  skos:narrower\n    <urn:{0}> ;'.format(

            # AVOID: tchbc - Top Concepts Having Broader Concepts
            if nomen_radici != progenitor:
                paginae.append('  skos:broader\n    <urn:{0}> ;'.format(
                    progenitor
                ))
            # @TODO: implement inverse, skos:broader

            linguae = self._quod_linguae(res)
            if len(linguae) > 0:
                paginae.append("  skos:prefLabel\n    {0} .".format(
                    " ,\n    ".join(linguae)
                ))
            else:
                # The "." also need to be on last statement
                raise NotImplementedError('{0} / {0} needs be fixed'.format(
                    nomen_radici, numerodinatio))

            # paginae.append('  rdfs:subClassOf <urn:{0}> . '.format(
            # paginae.append('  skos:topConceptOf <urn:{0}> . '.format(
            #     progenitor
            # ))
            # paginae.append('  skos:topConceptOf <http://vocabularies.unesco.org/thesaurus> .')
            # paginae.append('  skos:topConceptOf <http://vocabularies.unesco.org/thesaurus> ;')
            paginae.append('')

        # @TODO: ...

        # @TODO: edge case, such as 1603:25:1
        #   <urn:1603:25:1:4> a skos:Concept ;
        #   skos:prefLabel
        #       "extremitates"@lat-Latn-x-wikip3982 .

        return paginae


def ttl_imprimendo(
        paginae: Iterator[str],
        archivum_trivio: str = None):
    if archivum_trivio:
        raise NotImplementedError('{0}'.format(archivum_trivio))
    # imprimendō, v, s, dativus, https://en.wiktionary.org/wiki/impressus#Latin

    for linea in paginae:
        print(linea)


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
        # print(archivum_trivio)
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
            # print(row_index, row, self.active_row_end)
            if row_index >= self.active_row_start and \
                    row_index <= self.active_row_end:
                linea = []
                for col_index in range(
                        self.active_col_start, self.active_col_end):
                    textum = row[col_index].value

                    if textum:
                        # if isinstance(textum, datetime.datetime):
                        if isinstance(textum, datetime):
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

        if self.workbook[self.active].max_column is None or \
                self.workbook[self.active].max_row is None:
            # print('Excel was saved without metas; opening without read-only')
            self.workbook = load_workbook(
                self.archivum_trivio, data_only=True, read_only=False)

            self.workbook.iso_dates = True
            self.sheet_active = None

        self.active_col_end = self.workbook[self.active].max_column
        self.active_row_end = self.workbook[self.active].max_row

        # fons = self.workbook[self.active]

        # for row_index, row in enumerate(fons.rows):
        #     # TODO: discover where it starts
        #     pass

        # for index_cols in fons.rows

        # @TODO: calculate if HXL, if have more columns than ideal, etc

        return True
