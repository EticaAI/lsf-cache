#!/usr/bin/python3
# ==============================================================================
#
#          FILE:  linguacodex.py
#
#         USAGE:  ./999999999/0/linguacodex.py --help
#
#   DESCRIPTION: _[eng-Latn]
#                Expert system command line tool to aid misuse of language codes
#                [eng-Latn]_
#                Trivia:
#                - lingua cōdex
#                  - https://en.wiktionary.org/wiki/lingua#Latin
#                  - https://en.wiktionary.org/wiki/codex#Latin
#
#       OPTIONS:  See linguacodex.py --help
#
#  REQUIREMENTS:  - python3
#                   - langcodes
#                     - https://github.com/rspeer/langcodes
#          BUGS:  ---
#         NOTES:  ---
#       AUTHORS:  Emerson Rocha <rocha[at]ieee.org>
# COLLABORATORS:  <@TODO: put additional non-anonymous names here>
#       COMPANY:  EticaAI
#       LICENSE:  Public Domain dedication OR Zero-Clause BSD
#                 SPDX-License-Identifier: Unlicense OR 0BSD
#       VERSION:  v0.7
#       CREATED:  2021-11-20 10:37 UTC v0.1 name langcodescli.py
#       CHANGED:  2021-11-21 04:59 UTC v0.5 renamed as linguacodex.py
#                 2021-11-23 09:20 UTC v0.6 --in_bcp47_simplex implemented
#                 -- in_bcp47_simplex -> de_bcp47_simplex
#                 2022-05-08 03:30 UTC v0.7 copied from EticaAI/tico-19-hxltm
#                                           to EticaAI/lexicographi-sine-finibus
# ==============================================================================
"""linguacodex: expert system command line tool to aid misuse of language codes


_[eng-Latn]

Crash course from names in Latin to English
----------

- datum, https://en.wiktionary.org/wiki/datum#Latin:
    - Dataset
- columnam (or crudum columnam), https://en.wiktionary.org/wiki/columna#Latin:
    - Column, spreadsheet column, variable (of a item)
- līneam (or crudum līneam), https://en.wiktionary.org/wiki/linea#Latin:
    - row, spreadsheet row, line (used mostly for 'crudum rem', raw item)
- rem, https://en.wiktionary.org/wiki/res#Latin
    - Thing (generic)
- conceptum, https://en.wiktionary.org/wiki/conceptus#Latin:
    - Concept (used on HXLTM to diferenciate what is translation, rem, from
      concept that applies to all language variants of the sabe thing)
- fontem, https://en.wiktionary.org/wiki/fons#Latin:
    - Source
- objectīvum, https://en.wiktionary.org/wiki/objectivus#Latin:
    - Objective, target (as in target language, output archive)
- linguam, https://en.wiktionary.org/wiki/lingua#Latin:
    - Language, natural language
- bilingue
    - bilingual (as used on operations with source to target language in XLIFF)
- multiplum linguam
    - 1 to n languages (as used on operations that work with many languages
      like TMX and TBX)
- collēctiōnem, https://en.wiktionary.org/wiki/collectio#Latin:
    - collection, List, array (not sure if exist better naming in Latin, sorry)
- obiectum, https://en.wiktionary.org/wiki/obiectum#Latin:
    - Object (or Python Dict)
- Caput, https://en.wiktionary.org/wiki/caput#Latin:
    - Header
- Vēnandum īnsectum, (https://en.wiktionary.org/wiki/venor#Latin,
  https://en.wiktionary.org/wiki/insectum#Latin)
    - Debugging
- 'Exemplōrum gratiā (et Python doctest, id est, testum automata)'
    - 'For example (and python doctest, that is, automated testing)'
    - @see https://docs.python.org/3/library/doctest.html
        - python3 -m doctest hxltmcli-fork-from-marcus.py
        - python3 -m doctest hxlm/core/bin/hxltmcli.py

Some other very frequent generic terms:
----------

- ad:
    - @see https://en.wiktionary.org/wiki/ad#Latin
        - (direction) toward, to
        - up to (indicating direction upwards)
        - in consequence of
        - for, to, toward (indicating purpose or aim)
        - in order to, to, for (indicating means)
        - (...)
- de:
    - @see https://en.wiktionary.org/wiki/de#Latin
        - of, concerning, about
        - from, away from, down from, out of
- in:
    - @see https://en.wiktionary.org/wiki/in#Latin
        - toward, towards, against, at
        - until, for
        - about
        - according to

> Tips:
> - HXL-CPLP-Vocab_Auxilium-Humanitarium-API spreadsheet have additional terms
> - Google _wiktionary term-in-english_. Sometimes Google Translate will
>   give the perfect term, but to keep consistent, we use:
>    - Accusative
>        - Singular
>            - Neuter (You know, inclusive language)
> - 'Marcus loves/likes his dog', in Latin (same meaning different emphasis):
>    - Marcus canem amat.
>    - Canem Marcus amat.
>    - Amat canem Marcus.
>    - Marcus amat canem.
>    - Canem amat Marcus.
>    - Amat Marcus canem.
>    - Marcum canis amat.
>    - Canis Marcum amat.
>    - Amat canis Marcum.
>    - Marcum amat canis.
>    - Canis amat Marcum.
>    - Amat Marcum canis.
> - Latin, while very expressive/verbose language (and great to use on
>   ontologies, naming animals, etc, and this is the reason to use a few terms
>   in Latin on hxltmcli.py), was not what 'the people' used because was
>   hard even for the first class citizen with elite education 2000 years ago.
>   - Most example usages with HXLTM will use the 'prestige dialect' for a
>     ISO 15924 script (like translate from lat-Latn to ara-Arab, zho-Hant,
>     rus-Cyrl, and etc...) even when in fact we, 'the people', will use
>     more specific language/dialects, like por-Latn.

Missing 'good' Latin terms to express meaning in English (for software)
----------

- array, list
    - @see https://en.wiktionary.org/wiki/array
    - Sometimes we use 'Python List' as in
        - "Rem collēctiōnem, id est, Python List"
- output (preferable some short word, not like prōductiōnem)
    - @see https://en.wiktionary.org/wiki/output#English
- input
    - @see https://en.wiktionary.org/wiki/input

To Do
---------
- Improve the terms used for 'questions', like
  'quid'/ 'quod'
    - @see https://dcc.dickinson.edu/grammar/latin/questions


Neologisms on linguacodex
----------

Note: the initial author really tried attested latin terms for these concepts,
but was not viable. They actually are missing translations to non-English
languages, so, this makes sense.

- Base concept Endonym/exonym, no know Latin equivalents
  - "Endonym and exonym" English equivalents (see)
    https://en.wikipedia.org/wiki/Endonym_and_exonym)
    - "Autonym" (English)
      - "αὐτός" greek root "auto
        https://en.wiktionary.org/wiki/%CE%B1%E1%BD%90%CF%84%CF%8C%CF%82
      - "ἔνδον", greek root "endo"
        https://en.wiktionary.org/wiki/%E1%BC%94%CE%BD%CE%B4%CE%BF%CE%BD#Ancient_Greek
    - 'intra-' is more common prefix for latin terms (greek root equivalent, endo)
      - https://en.wiktionary.org/wiki/intra-
- intranomen: "intrā" + "nōmen"
  - "nōmen" https://en.wiktionary.org/wiki/nomen#Latin
  - "intrā-", https://en.wiktionary.org/wiki/intra-
  - Then, the definition:
    - "intranōmen" (from Latin "intra-", a prefix signifying inside, within,
      + "-nōmen", name, also know as endonym/autonym) is a common, internal
      name for a geographical place, group of people, language or dialect,
      meaning that it is used inside that particular place, group,
      or linguistic community in question; it is their self-designated
      name for themselves, their homeland, or their language.
  - References:
    - http://www.perseus.tufts.edu/hopper
      /text?doc=Perseus:text:1999.04.0059:entry=intra
    - http://www.perseus.tufts.edu/hopper
      /text?doc=Perseus:text:1999.04.0059:entry=nomen
- "externomen": "exter-" + "nōmen"
  - (from Latin "exter-", on the outside, outward, of another
    country, foreign, strange ,+ "-nōmen", name, also know as exonym/xenonym)
    is a common, external name for a geographical place, group of people,
    individual person, or a language/dialect, that is used only outside that
    particular place, group, or linguistic community
  - References:
    - http://www.perseus.tufts.edu/hopper
      /text?doc=Perseus:text:1999.04.0059:entry=exter
    - http://www.perseus.tufts.edu/hopper
      /text?doc=Perseus:text:1999.04.0059:entry=nomen


[eng-Latn]_


TODO: - Need a word for Autonym/endonym, but does not exist in latin
        Prefix here https://www.englishhints.com/latin-prefixes.html
      - https://en.wiktionary.org/wiki/Category:Latin_words_by_prefix

# pip install pyglottolog
# - https://github.com/glottolog/pyglottolog
#   - https://github.com/cldf/cldf/tree/master/components/languages
#     - https://github.com/cldf-datasets/wals/blob/master/cldf/languages.csv
#   - https://wals.info/
# - https://github.com/w3c/i18n-discuss/issues/13
# - About criticisms on ISO 639-1 ISO 639-2
#   - https://www.eva.mpg.de/fileadmin/content_files/linguistics
#     /conferences/2015-diversity-linguistics/Drude_slides.pdf

TESTS:
    python3 -m doctest ./scripts/fn/linguacodex.py
    python3 -m doctest -v ./scripts/fn/linguacodex.py
    python3 -m pylint --disable=C0302,W0511 -v ./scripts/fn/linguacodex.py
Manual tests (eventually remove it):
    ./scripts/fn/linguacodex.py --de_codex pt
    ./scripts/fn/linguacodex.py --de_codex pt --de_bcp47_simplex

    # This is well formed, but langcodes 3.3.0 think it is invalid
    ./scripts/fn/linguacodex.py --de_codex en-GB-oxedict | jq

./scripts/fn/linguacodex.py --de_nomen pt --imponendum_praejudicium | jq
./scripts/fn/linguacodex.py --de_nomen Português --imponendum_praejudicium | jq

./scripts/fn/linguacodex.py --de_nomen='Arabicus' --imponendum_praejudicium
    --in_formatum_est_planum --quod='.codex .communitas'
"""
import sys
import os
import io
import argparse
from pathlib import Path
import copy
import csv
import json
from dataclasses import dataclass, InitVar
from typing import (
    Any,
    Dict,
    # Iterable,
    # Optional,
    # List,
    # TextIO,
    Type,
    Union,
)

import langcodes

from L999999999_0 import (
    bcp47_langtag,
    hxl_hashtag_to_bcp47,
    # bcp47_rdf_extension,
    # bcp47_rdf_extension_poc,
)

DESCRIPTION = "_[eng-Latn]Command line to process language codes[eng-Latn]_"
EPILOG = """

EXEMPLUM
1. BCP47 parsing, default JSON output, no enforced prejudgments, export maximum
   information (as long as your initial tag already is right, which may be
   optimistic for people working with several languages they can't even read):

   $ linguacodex --de_codex=ar-Arab
   $ linguacodex --de_codex=ru-Cyrl
   $ linguacodex --de_codex=hi-Deva
   $ linguacodex --de_codex=el-Grek
   $ linguacodex --de_codex=zh-Hans
   $ linguacodex --de_codex=my-Mymr

2. Same as 1, but now ENFORCE prejudgments assuming your BCP47 code already is
   perfect aligned with BCP47. Uses Unicode CLDR to assume the likelySubtags.
   Note that the problem is actually not linguacodex, but in special
   "languages" that actually are macro languages are prone to be mislabeled.

   $ linguacodex --de_codex=ar --imponendum_praejudicium
   $ linguacodex --de_codex=zh --imponendum_praejudicium

3. Statistics of the speakers. How many read/speak Latin in the world? And
   Esperanto in the world? And portuguese in Brazil? And Russian in Devanagari
   on Vatican?

   $ linguacodex --de_codex=la --quod=.communitas
   $ linguacodex --de_codex=eo --quod=.communitas
   $ linguacodex --de_codex=pt-BR --quod=.communitas
   $ linguacodex --de_codex=ru-Deva-VA --quod=.communitas

4. Output format: the default --in_formatum is JSON, but this can be changed to
   CSV. The csv_caput and csv_non_caput can be used when mergint output
   to bigger file.

   $ linguacodex --de_codex=lat-Latn --in_formatum=csv
   $ linguacodex --de_codex=lat-Latn --in_formatum=csv_caput
   $ linguacodex --de_codex=lat-Latn --in_formatum=csv_non_caput

5. Extras from EticaAI/lexicographi-sine-finibus application
   {0} --de_bcp47_simplex \
--de_codex=qcc-Zxxx-r-pDCT-pmodified-ps1-txsd-tdatetime-tnop \
--quod=.Language-Tag_normalized

(Non-sense attribute and hashtag, but all options)
   {0} --de_bcp47_simplex --de_codex=qcc-Zxxx-r-sU2203-s2-snop-\
yU001D-yu007c-ynop-yU0002-yunescothes-ynop-pSKOS-pbroader-ps2-\
tXSD-tdatetime-tnop

   {0} --de_hxl_simplex --de_hxlhashtag=\
'#item+i_qcc+is_zxxx+rdf_p_skos_broader_s2+rdf_s_u2203_s2+rdf_t_xsd_datetime\
+rdf_y_u0002_unescothes+rdf_y_u001d_u007c'

   {0} --de_hxl_simplex --de_hxlhashtag=\
'#item+i_qcc+is_zxxx+rdf_s_u2200_s1+rdf_p_SKOS_related_s2+ix_wikip123' \
--quod=.Language-Tag_normalized

   {0} --de_hxl_simplex --de_bcp47_simplex \
--de_codex=qcc-Zxxx-r-sU2200-s1-snop-pSKOS-prelated-ps2-x-wikip12

ABOUT LANGUAGE-TERRITORY INFORMATION
(--quod .communitas)
    (from python langcodes documentation)
    The estimates for "writing population" are often overestimates,
    as described in the CLDR documentation on territory data.
    In most cases, they are derived from published data about literacy rates
    in the places where those languages are spoken.
    This doesn't take into account that many literate people around the
    world speak a language that isn't typically written,
    and write in a different language.
    See https://unicode-org.github.io/cldr-staging/charts/39/supplemental
    /territory_language_information.html

""".format(__file__)

parser = argparse.ArgumentParser(
    description=DESCRIPTION,
    formatter_class=argparse.RawDescriptionHelpFormatter,
    epilog=EPILOG
)

parser.add_argument(
    '--de_codex', action='store', help="""
    The main natural language to inspect using some well know language code.
    """)

parser.add_argument(
    '--de_hxlhashtag', action='store', help="""
    The HXL Hashtag to to inspect. Requires --de_hxl_simplex
    """)

# This is just in case we start to add new code standards
parser.add_argument(
    '--de_codex_norma', action='store', default='BCP47', help="""
    When using the code, specify the coding standard used. Defaults to BCP47
    """)
parser.add_argument(
    '--de_nomen', action='store', help="""
    The main natural language to inspect using the title of the language
    in some natural language. Requires --imponendum_praejudicium.
    """)
parser.add_argument(
    '--quod', action='store', default=".", help="""
    Dot notation to filter more exact information instead of return all
    information. Example: --quod .codex.BCP47
    """)

parser.add_argument(
    '--de_bcp47_simplex', action='store_true', help="""
    Define output as simple syntax parsing of input code as BCP47, without any
    advanced processing and/or conversion. Works even without download external
    data. Result use same key names as BCP47, except by
    'Language-Tag_normalized', '_unknown' and '_error' (JSON output)
    """)

parser.add_argument(
    '--de_hxl_simplex', action='store_true', help="""
    Parse a full HXL hashtag and try to infer a BCP47 language tag with
    extensions. This is somewhat reverse-engineering of previously created
    tags. Requires --de_hxlhashtag
    """)

# parser.add_argument(
#     '--de_bcp47_simplex_et_rdf', action='store_true', help="""
#     Same as --de_bcp47_simplex, except that will parse experimental -g-
#     extension semantics.
#     """)

# fōrmātum, https://en.wiktionary.org/wiki/formatus#Latin
parser.add_argument(
    '--in_formatum', action='store', default='json', help="""
    Format of the output. Valid values: 'json' (default), 'csv', 'csv_caput',
    'csv_non_caput'.
    """)

# plānum, https://en.wiktionary.org/wiki/planus
parser.add_argument(
    '--in_formatum_est_planum', action='store_true', default=False, help="""
    Flatten the keys of output. Can be used for nested object
    """)

# fōrmātum, https://en.wiktionary.org/wiki/formatus#Latin
# parser.add_argument(
#     '--in_formatum_json', action='store_const',
#     metavar='in_formatum'  help="""
#     If result is a nested object, flatten the keys
#     """)

# Trivia:
# - impōnendum, https://en.wiktionary.org/wiki/enforcier#Old_French
# - praejūdicium, https://en.wiktionary.org/wiki/praejudicium#Latin
parser.add_argument(
    '--imponendum_praejudicium', action='store_true', default=False,
    help="""
    Enforce linguistic prejudgment. Default: disabled.
    """
)
# Trivia: verbōsum, https://en.wiktionary.org/wiki/verbosus#Latin
parser.add_argument(
    '--verbosum', action='store_true',
    help='Verbose mode')

parser.add_argument('--version', action='version', version='0.5.0')


# DATA_EXTERNAL = __file__ .
DATA_EXTERNAL_DEFAULT = str(Path(__file__).parent.parent.resolve()) + \
    '/data-external'
DATA_EXTERNAL_CLDR_JSON = 'https://raw.githubusercontent.com/unicode-org/' + \
    'cldr-json/main/cldr-json/'

# Note: is possible to specify a different place for where store the data files
# with environment variable DATA_EXTERNAL
DATA_EXTERNAL = os.environ.get('DATA_EXTERNAL', DATA_EXTERNAL_DEFAULT)


class LinguaCodex:
    """
    _[eng-Latn]
    Command line to process language codes

    Trivia:
    - lingua cōdex
        - https://en.wiktionary.org/wiki/lingua#Latin
        - https://en.wiktionary.org/wiki/codex#Latin

    [eng-Latn]_
    """
    # pylint: disable=too-few-public-methods,too-many-instance-attributes
    de_codex: str = None
    de_nomen: str = None
    de_exemplum: str = None
    de_codex_norma: str = 'BCP47'
    # nomen_lingua: str = None
    quod: str = '.'
    # de_bcp47_simplex: bool = False
    imponendum_praejudicium: bool = False

    error: list = []

    # TODO: maybe take the systema_locale from the current terminal.
    #       (example from env vars: LANGUAGE=pt_BR:pt:en). For now
    #       we're defaulting to most common scripts
    # @see - https://www.worldatlas.com/articles
    #        /the-world-s-most-popular-writing-scripts.html
    #      - https://github.com/unicode-org/cldr-json/blob/main/cldr-json
    #        /cldr-core/supplemental/likelySubtags.json
    #      - https://unicode.org/iso15924/iso15924-codes.html
    systema_locale: list = [
        # Sorted by script ISO 15924 (latin) letter code
        'ar-Arab',
        'hy-Armn',
        'ru-Cyrl',
        'hi-Deva',
        'gu-Gujr',
        'el-Grek',
        'ka-Geor',
        'pa-Guru',
        'zh-Hans',
        'zh-Hant',
        'he-Hebr',
        'ko-Jamo',
        'jv-Java',
        'ja-Kana',
        'km-Khmr',
        'kn-Knda',
        'lo-Laoo',
        'la-Latn',
        'my-Mymr',
        'su-Sund',
        'ta-Taml',
        'te-Telu',
        'th-Thai',
        'bo-Tibt',
        'ii-Yiii',
    ]

    utilitas: Type['LinguaCodexUtilitas'] = None

    def __init__(
            self, de_codex: str = None,
            de_nomen: str = None,
            de_exemplum: str = None,
            de_codex_norma: str = 'BCP47',
            quod: str = '.',
            systama_locale: list = None,
            imponendum_praejudicium: bool = False
            # de_bcp47_simplex: bool = False
    ):  # pylint: disable=too-many-arguments
        """LinguaCodex initiāle
        """
        if de_codex:
            self.de_codex = de_codex
        if de_nomen:
            self.de_nomen = de_nomen
        if de_exemplum:
            self.de_exemplum = de_exemplum
        if de_codex_norma:
            self.de_codex_norma = de_codex_norma
        if quod:
            self.quod = quod

        if imponendum_praejudicium is not False:
            self.imponendum_praejudicium = imponendum_praejudicium

        if systama_locale is not None:
            self.systama_locale = systama_locale
        # if de_bcp47_simplex:
        #     self.de_bcp47_simplex = de_bcp47_simplex

        self.utilitas = LinguaCodexUtilitas()

    # def quid(self):
    #     return LinguaCodexQuid.in_textum_json(self.__dict__)

    def quid(self, info_in_lang=False):
        """quid [TODO documen]

        [extended_summary]

        Args:
            info_in_lang (bool, optional): [description]. Defaults to False.

        Returns:
            [type]: [description]
        """
        # pylint: disable=too-many-branches,too-many-statements

        # TODO: implement try catch with errors for langcodes
        # TODO: eventually refactor this entire method. Doing too much here

        # imponendum_praejudicium_rem
        ipr = []

        if self.de_codex:
            de_codex = self.de_codex
        elif self.de_nomen:
            de_codex = langcodes.find(self.de_nomen).to_tag()
            ipr.append('de_codex')
            #  = self.de_codex

        result_ = langcodes.Language.get(de_codex)
        if info_in_lang:
            if info_in_lang == 'autonym':
                result = result_.describe(de_codex)
            else:
                result = result_.describe(info_in_lang)
        else:
            result = result_.describe()

        # result['bcp47'] = langcodes.standardize_tag(de_codex)
        # result['codex'] = {
        #     '_crudum': de_codex,
        #     'BCP47': langcodes.standardize_tag(de_codex),
        #     'HXLTMa': '',
        #     'HXLTMt': ''
        # }
        # Trivia:
        # - macro_linguae de
        #   https://books.google.com.br
        #   /books?id=D-5GAAAAcAAJ&pg=PA400&lpg=PA400&dq=%22macro+linguae%22
        result['macro_linguae'] = None
        result['codex'] = {}

        result['codex']['BCP47'] = langcodes.standardize_tag(de_codex)
        if 'de_codex' in ipr and result['codex']['BCP47']:
            ipr.append('codex.BCP47')

        codex_language = bcp47_langtag(de_codex, 'language')
        # print('codex_language', codex_language)

        iso639 = iso639_type(self.utilitas.iso6393, codex_language)

        if iso639 and 'ISO639P3code' in iso639:
            ipr_b = []
            result['codex']['ISO639P3'] = iso639['ISO639P3code']  # type: ignore

            ipr_b.append('codex.ISO639P3')

            if iso639['ISO639P2Bcode']:  # type: ignore
                result['codex']['ISO639P2B'] = \
                    iso639['ISO639P2Bcode']  # type: ignore
                ipr_b.append('codex.ISO639P2B')

            if iso639['ISO639P2Tcode']:  # type: ignore
                result['codex']['ISO639P2T'] = \
                    iso639['ISO639P2Tcode']  # type: ignore
                ipr_b.append('codex.ISO639P2T')

            if iso639['ISO639P1code']:  # type: ignore
                result['codex']['ISO639P1'] = \
                    iso639['ISO639P1code']  # type: ignore
                ipr_b.append('codex.ISO639P1')

            scope = iso639['ISO639P3scope']  # type: ignore
            if scope:
                if scope == 'I':
                    result['macro_linguae'] = False
                elif scope == 'M':
                    result['macro_linguae'] = True

            if result['codex']['ISO639P3'] in self.utilitas.iso6393ToGlottocode:
                result['codex']['Glotto'] = \
                    self.utilitas.iso6393ToGlottocode[
                        result['codex']['ISO639P3']]
                ipr_b.append('codex.Glotto')

            if 'de_codex' in ipr:
                ipr.extend(ipr_b)

        # glottocode

        iso15924a = cldr_likely_iso15924(
            self.utilitas.likely_subtags,
            de_codex,
        )
        if iso15924a['script']:  # type: ignore
            if iso15924a['imponendum_praejudicium'] is False:  # type: ignore
                # cldr_likely_iso15924 found exact match, great
                result['codex']['ISO15924A'] = \
                    iso15924a['script']  # type: ignore
                # pass
            elif self.imponendum_praejudicium is True:

                # cldr_likely_iso15924 not found exact match, inference allowed
                result['codex']['ISO15924A'] = \
                    iso15924a['script']  # type: ignore
                ipr.append('codex.ISO15924A')
                # pass
            # pass

        # result['codex']['ISO15924A'] = iso15924a
        # result['codex']['HXLTMa'] = '@TODO'
        # result['codex']['HXLTMt'] = '@TODO'

        # commūnitās, https://en.wiktionary.org/wiki/communitas#Latin
        result['communitas'] = {
            # litterātum, https://en.wiktionary.org/wiki/litteratus#Latin
            'litteratum': result_.speaking_population(),
            # scrībendum, https://en.wiktionary.org/wiki/scribo#Latin
            'scribendum': result_.writing_population()
        }

        # https://en.wikipedia.org/wiki/Endonym_and_exonym
        # Autonym, https://en.wikipedia.org/wiki/Autonym
        # endonym, https://en.wikipedia.org/wiki/Endonym_and_exonym
        # exonym/xenonym (maybe xenomen??)
        # nōmen, https://en.wiktionary.org/wiki/nomen#Derived_terms
        # *-, https://www.englishhints.com/latin-prefixes.html
        # extra-, http://www.perseus.tufts.edu/hopper
        #         /resolveform?type=start&lookup=extra&lang=la
        result['nomen'] = {}
        if self.de_nomen:
            result['nomen']['_crudum'] = self.de_nomen
        # result['nomen']['autonym'] = langcodes.Language.get(
        #     de_codex).autonym()
        result['nomen']['intranomen'] = langcodes.Language.get(
            de_codex).autonym()
        # result['nomen']['exonym'] = {}
        result['nomen']['externomen'] = {}

        if self.systema_locale is not None and len(self.systema_locale) > 0:
            for lang in self.systema_locale:
                # result['nomen']['exonym'][lang] = langcodes.Language.get(
                #     de_codex).display_name(lang)
                result['nomen']['externomen'][lang] = langcodes.Language.get(
                    de_codex).display_name(lang)

        # TODO: separate part to script
        # scrīptum, https://en.wiktionary.org/wiki/scriptum#Latin

        # 	errōrem, https://en.wiktionary.org/wiki/error#Latin
        # typum, https://en.wiktionary.org/wiki/typus#Latin
        # https://en.wiktionary.org/wiki/syntaxis#Latin
        if not langcodes.tag_is_valid(de_codex):
            result['errorem_syntaxin'] = True

        # result['errorem'] = not langcodes.tag_is_valid(de_codex)
        # result['errorem'] = not langcodes.tag_is_valid(de_codex)

        # print('oi', self.quod)

        result['praejudicium'] = ipr

        result['__meta'] = {}
        if self.de_codex:
            result['__meta']['de_codex'] = self.de_codex
        if self.de_nomen:
            result['__meta']['de_nomen'] = self.de_nomen
        if self.imponendum_praejudicium:
            result['__meta']['imponendum_praejudicium'] = \
                self.imponendum_praejudicium
            # result['__meta']['praejudicium'] = ipr

        return quaerendum_de_punctum(result, self.quod)
        # print(json.dumps(result_item))
        # print('ooi', result)


class LinguaCodexCli:
    """LinguaCodexCli
    """
    argparse_args = None
    linguacodex: Type['LinguaCodex'] = None
    de_bcp47_simplex: bool = False
    de_hxl_simplex: bool = False
    error: list = []

    def __init__(self, argparse_args):
        """Simulationem initiāle
        """
        self.argparse_args = argparse_args

        if argparse_args.de_bcp47_simplex:
            self.de_bcp47_simplex = True

        elif argparse_args.de_hxl_simplex:
            self.de_hxl_simplex = True
            # pass
        else:
            self.linguacodex = LinguaCodex(
                de_codex=argparse_args.de_codex,
                de_codex_norma=argparse_args.de_codex_norma,
                de_nomen=argparse_args.de_nomen,
                quod=argparse_args.quod,
                imponendum_praejudicium=argparse_args.imponendum_praejudicium
                # de_bcp47_simplex=argparse_args.de_bcp47_simplex
            )

    def resultatum(self):
        """resultatum [summary]

        [extended_summary]

        Returns:
            [type]: [description]
        """
        # print('oooi', self.linguacodex)
        # print('oooi5', self.linguacodex.__dict__)
        # print('oooi6', self.linguacodex.quid())

        # print(self)
        # print(self.argparse_args)
        # sys.exit()

        # s = 'U+0041'

        # print(s[2:])
        # # 0041

        # print(chr(int(s[2:], 16)))
        # # A

        # # city = 'Ribeir\xc3\xa3o Preto'
        # unicode_str = 'U+1D53B'
        # unicode_str = 'U+0041'
        # print(unicode_str[2:])
        # print('𝔻')
        # print(len('𝔻'))
        # print('𝔻'.encode('utf-8').decode('utf-16'))
        # print(u'{0}'.format(u'\u3042'))
        # print(u'{0}'.format(u'\u0041'))
        # print(u'{0}'.format("\U00000394"))
        # print(u'{0}'.format("\U0001D53B"))
        # print(u'{0}'.format(u"\U0001D53B"))
        # print('ultimo')
        # print(u'{0}'.format(u"\u001D"))
        # print('ultimo2')
        # print(u'{0}'.format(u"\x1D"))
        # print('ultimo3')
        # print(u'{0}'.format(u"\x02"))
        # # print('U+1D53B'.encode('utf-8').decode(''))
        # # print(u'\U1D53B'.encode('utf-8').decode(''))
        # # print ('𝔻'.encode('utf-8').decode('ascii'))
        # return None

        if not self.argparse_args.de_codex and \
                not self.argparse_args.de_hxlhashtag:
            if not self.argparse_args.de_nomen:
                # raise ValueError('--de_codex? --de_nomen?')
                self.error.append('--de_codex? --de_nomen?')
                return None
            if not self.argparse_args.imponendum_praejudicium:
                self.error.append('--imponendum_praejudicium?')
                return None
                # raise ValueError('--imponendum_praejudicium?')

        if self.de_hxl_simplex:
            de_hxlhashtag = self.argparse_args.de_hxlhashtag
            de_hxlhashtag = hxl_hashtag_to_bcp47(de_hxlhashtag)
            # raise NotImplementedError('todo', self.argparse_args.de_hxlhashtag, de_hxlhashtag)
            return quaerendum_de_punctum(
                de_hxlhashtag,
                self.argparse_args.quod
            )
        if self.de_bcp47_simplex:
            return quaerendum_de_punctum(
                bcp47_langtag(
                    self.argparse_args.de_codex,
                ),
                self.argparse_args.quod
            )

        try:
            resultatum = self.linguacodex.quid()
            if self.argparse_args.in_formatum_est_planum is True:
                resultatum = in_obiectum_planum(resultatum)
            # in_formatum
        except ValueError as err:
            self.error.append(str(err))
            resultatum = None
            # pass
        # catch

        return resultatum

    def resultatum_in_textum(self):
        """resultatum_in_textum

        Returns:
            [type]: [description]
        """
        resultatum = self.resultatum()
        if self.error:
            resultatum_error = {
                'error': self.error
            }
            print(in_textum_json(resultatum_error))
            sys.exit(1)

        if self.argparse_args.in_formatum.lower() == 'json':
            return in_textum_json(resultatum)
        if self.argparse_args.in_formatum.lower() == 'csv':
            return in_textum_csv(resultatum)
        if self.argparse_args.in_formatum.lower() == 'csv_caput':
            return in_textum_csv(resultatum, datum=False)
        if self.argparse_args.in_formatum.lower() == 'csv_non_caput':
            return in_textum_csv(resultatum, caput=False)
        # else:
        self.error.append(
            'in_formatum? non json, csv, csv_caput, csv_non_caput')
        resultatum_error = {
            'error': self.error
        }
        print(in_textum_json(resultatum_error))
        sys.exit(1)


class LinguaCodexUtilitas:
    """LinguaCodexUtilitas
    _[eng-Latn]
    Quick and hacky bunch of staticmethod functions that could be decoupled
    [eng-Latn]_
    Trivia:
    - lingua cōdex
        - https://en.wiktionary.org/wiki/lingua#Latin
        - https://en.wiktionary.org/wiki/codex#Latin
    - ūtilitās
        - https://en.wiktionary.org/wiki/utilitas#Latin
    """
    # pylint: disable=too-few-public-methods

    # DATA_EXTERNAL can be defined as environment variable
    data_external: str = DATA_EXTERNAL
    likely_subtags: dict = {}
    # bcp47langToIso15924: dict = {}
    iso6393ToGlottocode: dict = {}
    iso6393: list = []

    def __init__(
            self
            # self, de_codex: str = None,
            # de_nomen: str = None,
            # de_exemplum: str = None,
            # de_codex_norma: str = 'BCP47',
            # quod: str = '.'
    ):  # pylint: disable=too-many-arguments
        """LinguaCodex initiāle
        """
        self._init_data_cldf()
        self._init_data_cldr()
        self._init_data_iso639_3()

    def _init_data_cldf(self):
        """_init_data_cldf
        """
        cldf_language_path = DATA_EXTERNAL + '/cldf/languages.csv'

        with open(cldf_language_path, 'r') as file_:
            csv_reader = csv.DictReader(file_)
            # line_count = 0
            # print('oi')
            for row in csv_reader:
                if row["ISO639P3code"] and row["Glottocode"]:
                    key = row["ISO639P3code"]

                    # Uncomment the next block to find imperfect ISO6393 to
                    # Glottocode. As 2021-11-23, this happens with
                    # [eus][basq1248][basq1250]
                    # if key in self.iso6393ToGlottocode:
                    #     if self.iso6393ToGlottocode[key] != row["Glottocode"]:
                    #         print('mismatch [' + row["ISO639P3code"] + '][' +
                    #               self.iso6393ToGlottocode[key] +
                    #               '][' + row["Glottocode"] + ']')
                    self.iso6393ToGlottocode[key] = \
                        row["Glottocode"]

    def _init_data_cldr(self):
        """_init_data_cldr
        """
        likely_subtags = DATA_EXTERNAL + '/cldr/likelySubtags.json'

        with open(likely_subtags, 'r') as file_:
            data = json.loads(file_.read())
            self.likely_subtags = data['supplemental']['likelySubtags']

            # for item in data['supplemental']['likelySubtags']:
            #     print(item)

        self._init_data_cldf()

    def _init_data_iso639_3(self):
        """_init_data_iso639_3
        """
        iso639_3_path = DATA_EXTERNAL + '/iso-639-3.csv'

        with open(iso639_3_path, 'r') as file_:
            csv_reader = csv.DictReader(file_)
            # line_count = 0
            for row in csv_reader:
                self.iso6393.append({
                    'ISO639P3code': row['Id'],
                    'ISO639P2Bcode': row['Part2B'],
                    'ISO639P2Tcode': row['Part2T'],
                    'ISO639P1code': row['Part1'],
                    'ISO639P3scope': row['Scope'],
                    'ISO639P3languagetype': row['Language_Type'],
                    'ISO639P3refname': row['Ref_Name'],
                })
                # if row["ISO639P3code"]:
                #     self.iso6393[row["ISO639P3code"]] = \
                #         row["Glottocode"]


@dataclass
class LinguaCodexQuid:
    """LinguaCodexQuid

    Trivia:
        - fōrmātum, https://en.wiktionary.org/wiki/formatus#Latin
    [extended_summary]
    """
    lingua_codex: InitVar[Type['LinguaCodex']] = None

    def __init__(self, lingua_codex: Type['LinguaCodex']):
        """LinguaCodexQuid initiāle
        """
        self.lingua_codex = lingua_codex


def cldr_likely_iso15924(
        dictionarium: dict,
        langtag: str,
        clavem: Type[Union[str, list]] = None,
        strictum_certum: bool = False,
) -> Type[Union[dict, str]]:
    """cldr_likely_iso15924 Likely ISO 15924 (script) from BCP47 tag

    Trivia:
    - CLDR, https://cldr.unicode.org/
    - langtag, https://tools.ietf.org/search/bcp47
    - dictiōnārium, https://en.wiktionary.org/wiki/dictionarium#Latin
    - resultātum, https://en.wiktionary.org/wiki/resultatum#Latin
    - certum, https://en.wiktionary.org/wiki/certus#Latin
    - strictum, https://en.wiktionary.org/wiki/strictus#Latin

    Args:
        dictionarium (dict): Python dictionary keys + values like the
                             CLDR supplemental.likelySubtags
        bcp47_langtag (str): [description]
        clavem (Type[Union[str, list]], optional): Key to return.
                                                   Defaults to None.
        strictum_certum (bool, optional): If only accept exact match.
                                          Defaults to False.

    Returns:
        Type[Union[dict, str]]: Either dict or exact result key

    Exemplōrum gratiā (et Python doctest, id est, testum automata):

    >>> dictionarium = {'pt': 'pt-Latn-BR', 'und-BR': 'pt-Latn-BR', \
'und-419': 'es-Latn-419', 'zh': 'zh-Hans-CN'}

    >>> cldr_likely_iso15924(dictionarium, 'pt-Latn')
    {'Language-Tag': 'pt-Latn', 'script': 'Latn', \
'imponendum_praejudicium': False}

    >>> cldr_likely_iso15924(dictionarium, 'pt')
    {'Language-Tag': 'pt', 'script': 'Latn', 'imponendum_praejudicium': True}

    >>> cldr_likely_iso15924(dictionarium, 'und-BR', 'script')
    'Latn'
    >>> cldr_likely_iso15924(dictionarium, 'und-BR', 'script', True)

    >>> cldr_likely_iso15924(dictionarium, 'und-Latn-BR', 'script', True)
    'Latn'
    """
    resultatum = {
        'Language-Tag': langtag,
        'script': None,
        'imponendum_praejudicium': None
    }
    # exact_scriptum = bcp47_langtag(langtag, 'script')
    langtag_certum = bcp47_langtag(langtag)
    if langtag_certum['script']:
        resultatum['script'] = langtag_certum['script']
        resultatum['imponendum_praejudicium'] = False
    elif not strictum_certum:
        if langtag_certum['region']:
            lpr = langtag_certum['language'] + '-' + langtag_certum['region']
            if lpr in dictionarium:
                langtag_non_certum = bcp47_langtag(dictionarium[lpr])
                resultatum['script'] = langtag_non_certum['script']
                resultatum['imponendum_praejudicium'] = True
        # TODO: try by ISO3 too, or inverse by ISO2
        if not resultatum['script']:
            lll = langtag_certum['language']
            if lll in dictionarium:
                langtag_non_certum = bcp47_langtag(dictionarium[lll])
                resultatum['script'] = langtag_non_certum['script']
                resultatum['imponendum_praejudicium'] = True
            # pass

    # resultatum['__dictionarium'] = dictionarium
    # resultatum['__langtag_certum'] = langtag_certum

    if clavem is not None:
        if isinstance(clavem, str):
            return resultatum[clavem]
        if isinstance(clavem, list):
            rresultatum_partial = {}
            for item in clavem:
                rresultatum_partial[item] = resultatum[item]
            return rresultatum_partial
        raise TypeError(
            'clavem [' + str(type(clavem)) + '] != [str, list]')

    return resultatum


class Simulationem:
    """ [summary]

    TODO: this does not scale well: better emulate outside the script itself
          eventually remove from here. But leave as it still working.

>>> Simulationem('linguacodex --de_codex pt').jq('.codex')
{"BCP47": "pt", "ISO639P3": "por", "ISO639P2B": "por", \
"ISO639P2T": "por", "ISO639P1": "pt", "Glotto": "port1283"}

>>> Simulationem(
...   'linguacodex --de_codex pt --imponendum_praejudicium').jq('.codex')
{"BCP47": "pt", "ISO639P3": "por", "ISO639P2B": "por", \
"ISO639P2T": "por", "ISO639P1": "pt", "Glotto": "port1283", \
"ISO15924A": "Latn"}

>>> Simulationem('linguacodex --de_codex pt').jq('.codex.BCP47')
"pt"

>>> Simulationem(
... 'linguacodex --de_codex en-b-ccc-bbb-a-aaa-X-xyz --de_bcp47_simplex')\
    .jq('.Language-Tag_normalized')
"en-a-aaa-b-ccc-bbb-x-xyz"


# >>> LinguaCodex(de_codex='pt').quid()
# '{"de_codex": "pt", "de_codex_norma": "BCP47"}'

    [extended_summary]
    """
    # pylint: disable=too-few-public-methods
    argumenta: str = None

    def __init__(self, argumenta):
        """Simulationem initiāle
        """
        self.argumenta = argumenta

    # def actio(self):
    #     # āctiō, https://en.wiktionary.org/wiki/actio#Latin
    #     sys.argv = self.argumenta.split(' ')

    #     print('sys.argv', sys.argv)

    #     import re
    #     s = 'abc,def, ghi, "jkl, mno, pqr","stu"'
    #     for r in re.findall(r'".+?"|[\w-]+', s):
    #         print(r)
    #     # for r in re.findall(r'".+?"|[\w-]+', self.argumenta):
    #     for r in re.findall(r'".+?"|[\w-]+', self.argumenta):
    #         print(r)

    def jq(self, jq_argumenta='.'):  # pylint: disable=invalid-name
        """jq [summary]

        [extended_summary]

        Args:
            jq_argumenta (str, optional): [description]. Defaults to '.'.
        """
        sys.argv = self.argumenta.split(' ')
        args = parser.parse_args()
        # result_original = run_cli(args)
        # result_original = LinguaCodexCli(args).resultatum_in_textum()
        # print(result_original)
        # return None
        # sys.exit(0)
        result_original = LinguaCodexCli(args).resultatum()
        # print('ooi7', result_original, type(result_original))
        # TODO: implement jq_argumenta
        result = copy.copy(result_original)
        # result = []
        if len(jq_argumenta.strip('.')) > 0:
            parts = jq_argumenta.strip('.').split('.')
            # print('parts', parts)
            for item in parts:
                # print('item', item, result)
                if result is not None and item in result:
                    result = result[item]
                else:
                    result = '?!?'
                    break

        print(in_textum_json(result))


def iso639_type(
        dictionarium: Type['list[dict]'],
        language: str,
        clavem: Type[Union[str, list]] = None,
        # strictum_certum: bool = False,
) -> Type[Union[dict, str]]:
    """iso639_type Inferecen about ISO 639 type (using ISO 639-3 reference)

    Trivia:
    - ISO 639-3, https://iso639-3.sil.org/
    - langtag, https://tools.ietf.org/search/bcp47
    - dictiōnārium, https://en.wiktionary.org/wiki/dictionarium#Latin
    - resultātum, https://en.wiktionary.org/wiki/resultatum#Latin
    - certum, https://en.wiktionary.org/wiki/certus#Latin
    - strictum, https://en.wiktionary.org/wiki/strictus#Latin

    Args:
        dictionarium (dict): Python dictionary keys + values like the
                             CLDR supplemental.likelySubtags
        bcp47_langtag (str): [description]
        clavem (Type[Union[str, list]], optional): Key to return.
                                                   Defaults to None.
        strictum_certum (bool, optional): If only accept exact match.
                                          Defaults to False.

    Returns:
        Type[Union[dict, str]]: Either dict or exact result key

    Exemplōrum gratiā (et Python doctest, id est, testum automata):

    >>> dictionarium = [{'ISO639P3code':'por', 'ISO639P2Bcode': 'por', \
'ISO639P2Tcode': 'por', 'ISO639P1code': 'pt', 'ISO639P3scope': 'I', \
'ISO639P3languagetype': 'L', 'ISO639P3refname': 'Portuguese'}]

    >>> iso639_type(dictionarium, 'pt', '_type')
    'ISO639P1code'

    >>> iso639_type(dictionarium, 'por', '_type')
    'ISO639P3code'

    >>> iso639_type(dictionarium, 'zzz', '_type')

    """
    resultatum = {}
    for item in dictionarium:
        if language == item['ISO639P3code']:  # type: ignore
            resultatum = item
            resultatum['_type'] = 'ISO639P3code'
            break
        if language == item['ISO639P2Bcode']:  # type: ignore
            resultatum = item
            resultatum['_type'] = 'ISO639P2Bcode'
        if language == item['ISO639P2Tcode']:  # type: ignore
            resultatum = item
            resultatum['_type'] = 'ISO639P2Tcode'
        if language == item['ISO639P1code']:  # type: ignore
            resultatum = item
            resultatum['_type'] = 'ISO639P1code'
            break

    if clavem and resultatum:
        return resultatum[clavem]

    return resultatum if resultatum else None


def in_obiectum_ex_planum(
        rem: dict,
        pydictsep: str = '.',
        pylistsep: str = ' ') -> dict:
    """in_obiectum_planum Unflatten a nested python object

    Note: the pylistsep intentionally have no effect. The object will not
    try to convert back to list what in_obiectum_planum() converted.

    Trivia:
      - obiectum, https://en.wiktionary.org/wiki/obiectum#Latin
      - recursiōnem, https://en.wiktionary.org/wiki/recursio#Latin
      - praefīxum, https://en.wiktionary.org/wiki/praefixus#Latin
      - plānum, https://en.wiktionary.org/wiki/planus

    Args:
        rem (dict): The object to flatten
        pydictsep (pydictsep, optional): The separator for python dict keys
        pylistsep (pydictsep, optional): The separator for python list values

    Returns:
        [dict]: A flattened python dictionary

    Exemplōrum gratiā (et Python doctest, id est, testum automata):

    >>> testum1_inv = {'a0.a1.a2': 'va', 'b0': '1 2 3'}
    >>> testum1_inv5 = {'a0.a1.a2.a3.a4.a5': 'va', 'b0': '1 2 3'}
    >>> in_obiectum_ex_planum(testum1_inv)
    {'a0': {'a1': {'a2': 'va'}}, 'b0': '1 2 3'}

    >>> in_obiectum_ex_planum(testum1_inv5)
    {'a0': {'a1': {'a2': {'a3': {'a4': {'a5': 'va'}}}}}, 'b0': '1 2 3'}

    >>> testum1_inv_sep = {'a0->a1->a2': 'va', 'b0': '1 2 3'}
    >>> in_obiectum_ex_planum(testum1_inv_sep, pydictsep='->')
    {'a0': {'a1': {'a2': 'va'}}, 'b0': '1 2 3'}

    # Be strict about type
    >>> in_obiectum_ex_planum([1, 2, 3, 4])
    Traceback (most recent call last):
    ...
    TypeError: in_obiectum_ex_planum non dict<class 'list'>
    """
    resultatum = {}

    if not isinstance(rem, dict):
        raise TypeError('in_obiectum_ex_planum non dict' + str(type(rem)))

    if pylistsep and pylistsep != ' ':
        raise NotImplementedError(
            'in_obiectum_ex_planum pylistsep ' + pylistsep)

    for clavem, item in rem.items():
        clavem_partem = clavem.split(pydictsep)
        ad_hoc = resultatum
        for part in clavem_partem[:-1]:
            if part not in ad_hoc:
                ad_hoc[part] = {}
            ad_hoc = ad_hoc[part]
        ad_hoc[clavem_partem[-1]] = item
    return resultatum


def in_obiectum_planum(
        rem: Dict,
        pydictsep: str = '.',
        pylistsep: str = ' ') -> dict:
    """in_obiectum_planum Flatten a nested python object

    Trivia:
      - obiectum, https://en.wiktionary.org/wiki/obiectum#Latin
      - recursiōnem, https://en.wiktionary.org/wiki/recursio#Latin
      - praefīxum, https://en.wiktionary.org/wiki/praefixus#Latin
      - plānum, https://en.wiktionary.org/wiki/planus

    Args:
        rem (dict): The object to flatten
        pydictsep (pydictsep, optional): The separator for python dict keys
        pylistsep (pydictsep, optional): The separator for python list values

    Returns:
        [dict]: A flattened python dictionary

    Exemplōrum gratiā (et Python doctest, id est, testum automata):

    >>> testum1 = {'a0': {'a1': {'a2': 'va'}}, 'b0': [1, 2, 3]}
    >>> in_obiectum_planum(testum1)
    {'a0.a1.a2': 'va', 'b0': '1 2 3'}

    >>> in_obiectum_planum(testum1)
    {'a0.a1.a2': 'va', 'b0': '1 2 3'}

    >>> in_obiectum_planum(testum1, pylistsep=',')
    {'a0.a1.a2': 'va', 'b0': '1,2,3'}

    >>> in_obiectum_planum(testum1, pydictsep='->')
    {'a0->a1->a2': 'va', 'b0': '1 2 3'}

    # This is not designed to flat arrays, str, None, int, ..., only dict
    >>> in_obiectum_planum([1, 2, 3, 4])
    Traceback (most recent call last):
    ...
    TypeError: in_obiectum_planum non dict<class 'list'>
    """
    resultatum = {}

    if not isinstance(rem, dict):
        raise TypeError('in_obiectum_planum non dict' + str(type(rem)))

    def recursionem(rrem, praefixum: str = ''):
        praefixum_ad_hoc = '' if praefixum == '' else praefixum + pydictsep
        if isinstance(rrem, dict):
            for clavem in rrem:
                recursionem(rrem[clavem], praefixum_ad_hoc + clavem)
        elif isinstance(rrem, list):
            resultatum[praefixum] = pylistsep.join(map(str, rrem))
        else:
            resultatum[praefixum] = rrem

    recursionem(rem)

    return resultatum
# quaerendum, https://en.wiktionary.org/wiki/quaero#Latin (English "query")
# pūnctum, https://en.wiktionary.org/wiki/punctum#Latin
# , https://en.wiktionary.org/wiki/quaero#Latin (English "point<-period")

# def in_jq(rem, quod: str = '.', incognitum: Any = '?!?'):


def quaerendum_de_punctum(rem: dict, quod: str = '.') -> dict:
    """quaerendum_de_punctum Ad hoc simple JQ-inspired query

    See test examples

    Args:
        rem ([dict]): [description]
        quod (str, optional): Search path. Defaults to '.' (no filter)

    Raises:
        ValueError: Raise errors if keys do not end with ?

    Returns:
        [dict]: Python dict with only selected keys

    Exemplōrum gratiā (et Python doctest, id est, testum automata):

    >>> exemplum_i = {'a': {'aa1': 1, "aa2": 2}, 'b': 10}
    >>> quaerendum_de_punctum(exemplum_i, '.b')
    10

    >>> quaerendum_de_punctum(exemplum_i, '.a')
    {'aa1': 1, 'aa2': 2}

    >>> quaerendum_de_punctum(exemplum_i, '.a.aa1')
    1

    >>> quaerendum_de_punctum(exemplum_i, '.a.aa1 .b')
    {'a': {'aa1': 1}, 'b': 10}

    # Return error for non existing keys without '?' as suffix
    >>> quaerendum_de_punctum(exemplum_i, '.nonclavem')
    Traceback (most recent call last):
    ...
    ValueError: quaerendum_de_punctum [.nonclavem]

    # This key do not exist, but fail without raise exception
    >>> quaerendum_de_punctum(exemplum_i, '.nonclavem?')
    """

    # Note: if have only one query = return only exact value
    # Note: if have , separed values = return object with keys

    def auxilium(arem, quod: str = '.'):
        neo_rem = arem
        vigiliam = True
        # print(quod[:-1])
        # return ('quod', quod, quod[-1], quod[:1], quod[:1] == '?')
        if quod[-1] == '?':
            vigiliam = False
            quod = quod[0:-1]
        if len(quod.strip('.')) > 0:
            parts = quod.strip('.').split('.')
            # print('parts', parts)
            for item in parts:
                # print('item', item, result)
                if neo_rem is not None and item in neo_rem:
                    neo_rem = neo_rem[item]
                else:
                    if vigiliam:
                        raise ValueError(
                            'quaerendum_de_punctum [' + quod + ']')
                    neo_rem = None
                    break
        return neo_rem

    if quod.find(' ') > -1:
        # quod_multiplum =
        quod_multiplum = list(filter(None, quod.split(' ')))
        resultatum_planum = {}
        for quod_item in quod_multiplum:
            resultatum_planum[quod_item.strip('.').strip(
                '?')] = auxilium(rem, quod_item)

        # return resultatum_planum
        return in_obiectum_ex_planum(resultatum_planum)

    resultatum = auxilium(rem, quod)

    return resultatum


def in_textum_csv(
        rem: Type[Union[dict, list]],
        caput: bool = True,
        datum: bool = True,
        non_rn: bool = True,
) -> str:
    """in_textum_csv Convert dict / list[dict] to CSV

    Args:
        rem (Type[Union[dict, list]]): Dict or list of dicts to convert
        caput (bool, optional): Print header?. Defaults to True.
        datum (bool, optional): Return data itself?. Defaults to True.
        non_rn (bool, optional): Remove last new line?. Defaults to True.

    Raises:
        TypeError: [description]

    Returns:
        str: [description]

    Exemplōrum gratiā (et Python doctest, id est, testum automata):

    >>> testum1 = {'a0': {'a1': {'a2': 'va'}}, 'b0': [1, 2, 3]}
    >>> testum1_planum = {'a0.a1.a2': 'va', 'b0': '1 2 3'}
    >>> list_planum = [testum1_planum, testum1_planum, testum1_planum]
    >>> in_textum_csv(testum1)
    'a0,b0\\r\\n{\\'a1\\': {\\'a2\\': \\'va\\'}},"[1, 2, 3]"'

    >>> in_textum_csv(testum1_planum)
    'a0.a1.a2,b0\\r\\nva,1 2 3'

    >>> in_textum_csv(list_planum, caput=False)
    'va,1 2 3\\r\\nva,1 2 3\\r\\nva,1 2 3'

    >>> in_textum_csv(testum1_planum, datum=False)
    'a0.a1.a2,b0'
    """
    if isinstance(rem, dict):
        rem = [rem]
    if not isinstance(rem, list) or not isinstance(rem[0], dict):
        raise TypeError('in_textum_csv non list[dict] ' + str(type(rem)))

    output = io.StringIO()
    wtr = csv.DictWriter(output, rem[0].keys())

    if caput:
        wtr.writeheader()
    for item in rem:
        if datum:
            wtr.writerow(item)

    resultatum = output.getvalue()
    if non_rn:
        resultatum = resultatum.rstrip("\r\n")
    return resultatum


def in_textum_json(
        rem: Any,
        formosum: Union[bool, int] = None,
        clavem_sortem: bool = False,
        imponendum_praejudicium: bool = False
) -> str:
    """Trānslātiōnem: rem in textum JSON

    Trivia:
        - rem, https://en.wiktionary.org/wiki/res#Latin
        - in, https://en.wiktionary.org/wiki/in#Latin
        - json, https://www.json.org/
        - fōrmōsum, https://en.wiktionary.org/wiki/formosus
        - impōnendum, https://en.wiktionary.org/wiki/enforcier#Old_French
        - praejūdicium, https://en.wiktionary.org/wiki/praejudicium#Latin
        - sortem, https://en.wiktionary.org/wiki/sors#Latin
        - clāvem, https://en.wiktionary.org/wiki/clavis#Latin

    Args:
        rem ([Any]): Rem

    Returns:
        [str]: Rem in JSON textum

    Exemplōrum gratiā (et Python doctest, id est, testum automata):

>>> rem = {"b": 2, "a": ['ت', 'ツ', '😊']}

>>> in_textum_json(rem)
'{"b": 2, "a": ["ت", "ツ", "😊"]}'

# >>> in_textum_json(rem, clavem_sortem=True)
# '{"a": ["ت", "ツ", "😊"], "b": 2}'
#
# >>> in_textum_json(rem, imponendum_praejudicium=True)
# '{"b": 2, "a": ["\\\u062a", "\\\u30c4", "\\\ud83d\\\ude0a"]}'
#
# >>> in_textum_json(rem, formosum=True)
# '{\\n    "b": 2,\\n    \
# "a": [\\n        "ت",\\n        "ツ",\\n        "😊"\\n    ]\\n}'

"""

    # print = json.dumps()

    if formosum is True:
        formosum = 4

    json_textum = json.dumps(
        rem,
        indent=formosum,
        sort_keys=clavem_sortem,
        ensure_ascii=imponendum_praejudicium
    )

    return json_textum


if __name__ == '__main__':

    args_ = parser.parse_args()

    if len(sys.argv) > 1:
        # run_cli(args)
        print(LinguaCodexCli(args_).resultatum_in_textum())
    else:
        parser.print_help()
        sys.exit(1)
