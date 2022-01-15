#!/usr/bin/env python3
# ==============================================================================
#
#          FILE:  2600.py
#
#         USAGE:  ./999999999/0/2600.py
#                 ./999999999/0/2600.py --help
#                 NUMERORDINATIO_BASIM="/dir/ndata" ./999999999/0/2600.py
#
#   DESCRIPTION:  ---
#
#       OPTIONS:  ---
#
#  REQUIREMENTS:  - python3
#          BUGS:  ---
#         NOTES:  ---
#       AUTHORS:  Emerson Rocha <rocha[at]ieee.org>
# COLLABORATORS:
#                 <@TODO: put additional non-anonymous names here>
#
#       COMPANY:  EticaAI
#       LICENSE:  Public Domain dedication or Zero-Clause BSD
#                 SPDX-License-Identifier: Unlicense OR 0BSD
#       VERSION:  v0.5.0
#       CREATED:  2022-01-08 04:37 UTC
#      REVISION:  ---
# ==============================================================================

# pytest
#    python3 -m doctest ./999999999/0/2600.py

# TL;DR:
#   ./999999999/0/2600.py
#   NUMERORDINATIO_BASIM="/external/ndata" ./999999999/0/2600.py
#   ./999999999/0/2600.py --verbum-limiti=4 --codex-verbum-tabulae=',0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z' --actionem=fontem-verbum-tabulae
#   ./999999999/0/2600.py --verbum-limiti=4 --codex-verbum-tabulae=',0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z' --actionem=codex

# Generate a list of hex
# a_list = range(60)
# print (',' + '{}'.format(','.join(hex(x) for x in a_list)) + ',')
#    ./999999999/0/2600.py --actionem-neo-scripturam --neo-scripturam-tabulae-hxl-nomini="#item+rem+i_mul+is_zsym+ix_ndt60+ix_hex" --neo-scripturam-tabulae-symbola=',0x0,0x1,0x2,0x3,0x4,0x5,0x6,0x7,0x8,0x9,0xa,0xb,0xc,0xd,0xe,0xf,0x10,0x11,0x12,0x13,0x14,0x15,0x16,0x17,0x18,0x19,0x1a,0x1b,0x1c,0x1d,0x1e,0x1f,0x20,0x21,0x22,0x23,0x24,0x25,0x26,0x27,0x28,0x29,0x2a,0x2b,0x2c,0x2d,0x2e,0x2f,0x30,0x31,0x32,0x33,0x34,0x35,0x36,0x37,0x38,0x39,0x3a,0x3b,'
#
#    ./999999999/0/2600.py --actionem-neo-scripturam --neo-scripturam-tabulae-hxl-nomini="#item+rem+i_mul+is_zsym+ix_ndt60+ix_hex" --neo-scripturam-tabulae-symbola=',�,�,�,�,�,�,�,�,�,�,�,�,�,�,�,�,�,�,�,�,0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,�,�,�,�,' --neo-scripturam-tabulae-hxl-selectum='ix_hex'
#    ./999999999/0/2600.py --actionem-neo-scripturam --neo-scripturam-tabulae-hxl-nomini="#item+rem+i_mul+is_zsym+ix_ndt60+ix_hex" --neo-scripturam-tabulae-symbola=',�,�,�,�,�,�,�,�,�,�,�,�,�,�,�,�,�,�,�,�,0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,�,�,�,�,' --neo-scripturam-tabulae-hxl-selectum='ix_hex' > 1613/1603.2.60.TEST.no1.tm.hxl.tsv


import os
import sys
import argparse
# from pathlib import Path
from typing import (
    # Type,
    Union
)

# from itertools import permutations
from itertools import product
# valueee = list(itertools.permutations([1, 2, 3]))
import csv

NUMERORDINATIO_BASIM = os.getenv('NUMERORDINATIO_BASIM', os.getcwd())
NUMERORDINATIO_DEFALLO = int(os.getenv('NUMERORDINATIO_DEFALLO', '60'))  # �
NUMERORDINATIO_MISSING = "�"
DESCRIPTION = """
2600.60 is (...)
"""

# In Python2, sys.stdin is a byte stream; in Python3, it's a text stream
STDIN = sys.stdin.buffer

# print('getcwd:      ', os.getcwd())
# print('oi', NUMERORDINATIO_BASIM)


# def quod_1613_2_60_datum():
#     datum = {}
#     with open(NUMERORDINATIO_BASIM + "/1613/1603.2.60.no1.tm.hxl.tsv") as file:
#         tsv_file = csv.DictReader(file, delimiter="\t")
#         return list(tsv_file)

# a b aa bb
# printf "30160\n31161\n1830260\n1891267\n" | ./999999999/0/2600.py --actionem-decifram

# a aa aaa
# printf "30160\n1830260\n109830360\n" | ./999999999/0/2600.py --actionem-decifram


# https://www.unicode.org/Public/UCD/latest/ucd/extracted/DerivedNumericType.txt
numerum_decimalem = {
    # 0030..0039    ; Decimal # Nd  [10] DIGIT ZERO..DIGIT NINE
    'DIGIT': [0x0030, 0x0039],
    # 0660..0669    ; Decimal # Nd  [10] ARABIC-INDIC DIGIT ZERO..ARABIC-INDIC DIGIT NINE
    'ARABIC-INDIC': [0x0660, 0x0669],

}

class RadicemNumerali:
    """rādīcem numerālī

    Trivia:
        - rādīcem, https://en.wiktionary.org/wiki/radix#Latin
        - numerālī, https://en.wiktionary.org/wiki/numeralis#Latin

    See:
        - https://cs.stackexchange.com/questions/10318

    Exemplōrum gratiā (et Python doctest, id est, testum automata):

        >>> RadicemNumerali.convertBase([1,1,2,0], 3, 2)
        [1, 0, 1, 0, 1, 0]

        # 30 = a {30} (b60)
        >>> RadicemNumerali.toDigits(30, 60)
        [30]

        # 1830 = aa{30 30} (b60)
        >>> RadicemNumerali.toDigits(1830, 60)
        [30, 30]

        # 109830 = aaa<30 30 30> (b60)
        >>> RadicemNumerali.toDigits(109830, 60)
        [30, 30, 30]

        # [30, 30, 30] -> 109830
        >>> RadicemNumerali.fromDigits([30, 30, 30], 60)
        109830
    """

    @staticmethod
    def toDigits(n, b):
        """Convert a positive number n to its digit representation in base b."""
        digits = []
        while n > 0:
            digits.insert(0, n % b)
            n = n // b
        return digits

    @staticmethod
    def fromDigits(digits, b):
        """Compute the number given by digits in base b."""
        n = 0
        for d in digits:
            n = b * n + d
        return n

    @staticmethod
    def convertBase(digits, b, c):
        """Convert the digits representation of
        a number from base b to base c."""
        return RadicemNumerali.toDigits(
            RadicemNumerali.fromDigits(digits, b), c)


class SystemaNumerali:
    """Systēma numerālī

    Trivia:
        - systēma, n, https://en.wiktionary.org/wiki/systema#Latin
        - numerālī, https://en.wiktionary.org/wiki/numeralis#Latin

    See:
        - unicode.org/Public/UCD/latest/ucd/extracted/DerivedNumericType.txt

    Exemplōrum gratiā (et Python doctest, id est, testum automata):

        # 0030..0039
        >>> digitae = SystemaNumerali('DIGIT', 0x0030, 0x0039)
        >>> digitae.de(1)
        '1'
        >>> digitae.tabulam()
        ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        >>> arabic_indic = SystemaNumerali('ARABIC-INDIC', 0x0660, 0x0669)
        >>> arabic_indic.de(1)
        '1'
        >>> arabic_indic.tabulam()
        ['٠', '١', '٢', '٣', '٤', '٥', '٦', '٧', '٨', '٩']

    """

    def __init__(
            self,
            nomen: str = '',
            unicode_initiale: str = None,
            unicode_finale: str = None
    ):
        # TODO: implement non-decimal systems
        self.nomen = nomen
        self.unicode_initiale = unicode_initiale
        self.unicode_finale = unicode_finale

    def de(self, digitum: int) -> str:
        return str(digitum)
        # pass

    def tabulam(self):
        resultatum = []
        for rem in range(self.unicode_initiale, self.unicode_finale + 1, 1):
            resultatum.append(chr(rem))

        return resultatum


class NDT2600:
    def __init__(self):
        self.D1613_2_60 = self._init_1613_2_60_datum()
        # self.scientia_de_scriptura = {}
        self.scientia_de_scriptura = self.D1613_2_60
        self.cifram_signaturae = 6  # TODO: make it flexible
        self.codex_verbum_tabulae = []
        self.verbum_limiti = 2
        self.resultatum_separato = "\t"

    def _init_1613_2_60_datum(self):
        archivum = NUMERORDINATIO_BASIM + "/1613/1603_2_60.no1.tm.hxl.tsv"
        datum = {}
        with open(archivum) as file:
            tsv_file = csv.DictReader(file, delimiter="\t")
            # return list(tsv_file)
            for conceptum in tsv_file:
                int_clavem = int(conceptum['#item+conceptum+numerordinatio'])
                datum[int_clavem] = {}
                for clavem, rem in conceptum.items():
                    if not clavem.startswith('#item+conceptum+numerordinatio'):
                        datum[int_clavem][clavem] = rem

        return datum

    def est_codex_verbum_tabulae(self, tabulae: Union[str, list]):
        if isinstance(tabulae, list):
            self.codex_verbum_tabulae = tabulae
        else:
            separator = tabulae[0]
            # print('tabulae', tabulae)
            if tabulae.count(separator) < 2:
                raise ValueError(
                    "Separator [" + separator + "] of [" +
                    str(tabulae) + "]? --help")
            crudum_tabulae = tabulae.split(separator)
            self.codex_verbum_tabulae = list(filter(None, crudum_tabulae))

    def est_neo_scripturam_tabulae(self, tabulae: str, nomini: str):
        separator = tabulae[0]
        # print('tabulae22222222', tabulae)
        if tabulae.count(separator) < 2:
            raise ValueError(
                "Separator [" + separator + "] of [" +
                str(tabulae) + "]? --help")

        crudum_tabulae = tabulae.split(separator)
        tabula_array = list(filter(None, crudum_tabulae))

        scientia_de_scriptura_len = len(self.scientia_de_scriptura.keys())
        neo_scripturam_tabulae_len = len(tabula_array)

        if scientia_de_scriptura_len != neo_scripturam_tabulae_len:
            raise ValueError(
                "scientia_de_scriptura_len [{0}] " +
                "neo_scripturam_tabulae != [{1}]".format(
                    str(scientia_de_scriptura_len),
                    str(neo_scripturam_tabulae_len))
            )

        for index in range(scientia_de_scriptura_len):
            # print('index', index)
            # self.scientia_de_scriptura[index][nomini] = tabula_array[index]
            self.scientia_de_scriptura[index][nomini] = tabula_array.pop(0)

    def est_verbum_limiti(self, verbum_limiti: int):
        self.verbum_limiti = int(verbum_limiti)
        return self

    def est_resultatum_separato(self, resultatum_separato: str):
        self.resultatum_separato = resultatum_separato
        return self

    def cifram_lineam(self, datum_lineam: str, index: int = 0):
        # self.resultatum_separato = resultatum_separato
        fontem_separato = "\t"
        resultatum = []

        lineam_arr = datum_lineam.split(fontem_separato)

        codicem_numerae = self.quod_numerordinatio_digitalem(lineam_arr[index])
        resultatum.append(codicem_numerae)

        for rem in lineam_arr:
            resultatum.append(rem)

        # print('...', resultatum, fontem_separato.join(resultatum))
        # print('...', fontem_separato.join(resultatum))

        return fontem_separato.join(resultatum)

    def decifram_codicem_numerae(self, codicem):
        # self.resultatum_separato = resultatum_separato
        fontem = ''

        # TODO: check vality of number before make the tests

        codicem_textum = str(codicem)[:-4]

        # print('TODOcodicem')
        # fontem = "@todo[" + codicem_textum + ']'

        # fontem += str(RadicemNumerali.toDigits(int(codicem_textum), 60))

        codicem_numerum_collectionem = RadicemNumerali.toDigits(
            int(codicem_textum), 60)

        for rem in codicem_numerum_collectionem:
            fontem += self.quod_punctum(rem)

        return fontem

    def exportatum_scientia_de_scriptura(
            self, hxl_selectum: str = None):
        # self.resultatum_separato = resultatum_separato
        tabula = []

        caput = self.scientia_de_scriptura[0].keys()

        # print('clavem', caput)
        # print('neo_scripturam_hxl_selectum', hxl_selectum)
        tabula_caput = []
        tabula_caput.append('#item+conceptum+numerordinatio')
        tabula_non = []
        index = 1
        for clavem in caput:
            tabula_caput.append(clavem)
            if hxl_selectum is not None:
                if clavem.find(hxl_selectum) == -1:
                    tabula_non.append(index)
                    # print('exclude this')
            index += 1

        tabula.append(tabula_caput)
        for clavem_numerum, rem in self.scientia_de_scriptura.items():
            lineam = [str(clavem_numerum)]
            lineam.extend(rem.values())
            tabula.append(lineam)

        if len(tabula_non):
            tabula_selectum = []
            for lineam in tabula:
                neo_lineam = []
                for idx, rem in enumerate(lineam):
                    if idx not in tabula_non:
                        neo_lineam.append(rem)
                    # print(idx, val)
                tabula_selectum.append(neo_lineam)
            # print('oi')
            return tabula_selectum

        # print(tabula)
        # print(self.D1613_2_60)
        return tabula

    def _quod_crc_check(self, numerum):
        numerum_textum = str(numerum)
        crc = 0
        for pumctum in numerum_textum:
            crc = crc + int(pumctum)
        return str(crc)[-1]

    def _quod_numerordinatio_digitalem_punctum(self, punctum: str):
        # for conceptum in self.D1613_2_60:
        #     print('TODO')
        # for clavem, rem in self.D1613_2_60.items():
        for clavem, rem in self.scientia_de_scriptura.items():
            if punctum in rem.values():
                return clavem

        return NUMERORDINATIO_DEFALLO

    def quod_punctum(self, digitalem: int, hxl_selectum: str = None) -> str:
        """quod_punctum Quod Puntum?

        Return a unicode code point based on numeric key

        Args:
            digitalem (int): [description]
            hxl_selectum (str, optional): [description]. Defaults to None.

        Returns:
            str: [description]
        """

        # TODO: deal with overflows for number (not just concept)
        conceptum = self.scientia_de_scriptura[digitalem]

        for _clavem, punctum in conceptum.items():
            # _clavem...
            if hxl_selectum is not None:
                raise NotImplemented(
                    " TODO: implement hxl_selectum")
            if punctum != NUMERORDINATIO_MISSING:
                return punctum

        return NUMERORDINATIO_MISSING

    def quod_numerordinatio_digitalem(
            self, codicem: str = '', verbose: bool = False) -> str:
        # Some unicode code poits may have upper case, but most do not.
        codicem_minor = codicem.lower()
        digitalem_verus = 0
        ordo = 0
        for pumctum in reversed(codicem_minor):
            digitalem_punctum = self._quod_numerordinatio_digitalem_punctum(
                pumctum)
            digitalem_punctum_ordo = digitalem_punctum * \
                pow(NUMERORDINATIO_DEFALLO, ordo)
            digitalem_verus = digitalem_verus + digitalem_punctum_ordo

            # print('pumctum', pumctum, digitalem_punctum,
            #       digitalem_punctum_ordo, digitalem_verus)

            ordo = ordo + 1

        # signātūrum, https://en.wiktionary.org/wiki/signaturus#Latin
        # decimālī, https://en.wiktionary.org/wiki/decimalis#Latin

        signaturum_in_decimali = self._quod_crc_check(
            digitalem_verus + ordo + int(self.cifram_signaturae)
        )

        resultatum = [
            str(digitalem_verus),
            str(ordo),
            str(self.cifram_signaturae),
            # str(self._quod_crc_check(digitalem_verus))
            str(signaturum_in_decimali)
        ]

        if verbose:
            return resultatum

        # print('todo')
        return ''.join(resultatum)

    def quod_tabulam_multiplicatio(self):
        resultatum = []

        # collectionem = permutations(
        collectionem = product(
            self.codex_verbum_tabulae, repeat=self.verbum_limiti)
        for item in collectionem:
            # print('item', item)
            resultatum.append(''.join(item))
        return resultatum

    def quod_codex(self):
        fontem_verbum = self.quod_tabulam_multiplicatio()
        resultatum = []

        for item in fontem_verbum:
            # print('item', item)
            codex_digitum = self.quod_numerordinatio_digitalem(item)
            resultatum.append([
                codex_digitum,
                item
            ])

        # resultatum = list(permutations(self.codex_verbum_tabulae, self.verbum_limiti))

        return resultatum


class CLI_2600:
    def __init__(self):
        """
        Constructs all the necessary attributes for the Cli object.
        """
        self.pyargs = None
        # self.args = self.make_args()
        # Posix exit codes
        self.EXIT_OK = 0
        self.EXIT_ERROR = 1
        self.EXIT_SYNTAX = 2

    def make_args(self, hxl_output=True):
        parser = argparse.ArgumentParser(description=DESCRIPTION)

        # https://en.wikipedia.org/wiki/Code_word
        # https://en.wikipedia.org/wiki/Coded_set

        # cōdex verbum tabulae
        # parser.add_argument(
        #     '--actionem',
        #     help='Action to execute. Defaults to codex.',
        #     # choices=['rock', 'paper', 'scissors'],
        #     choices=[
        #         'codex',
        #         'fontem-verbum-tabulae',
        #         'neo-scripturam',
        #     ],
        #     dest='actionem',
        #     required=True,
        #     default='codex',
        #     const='codex',
        #     type=str,
        #     nargs='?'
        # )

        parser.add_argument(
            '--punctum-separato-de-resultatum',
            help='Character(s) used as separator for generate output.' +
            'Defaults to tab "\t"',
            dest='resultatum_separato',
            default="\t",
            nargs='?'
        )

        neo_codex = parser.add_argument_group(
            "neo-codex-tabulae",
            "(DEFAULT USE) Operations to pre-build codes with their meanings")

        neo_codex.add_argument(
            '--actionem-codex-tabulae-completum',
            help='Define mode to operate with new code ' +
            'tables with their meanings',
            metavar='',
            dest='codex_completum',
            const=True,
            nargs='?'
        )

        neo_codex.add_argument(
            '--actionem-verbum-simplex',
            help='Do not generate the codes. Just calculate the full matrix ' +
            'of possible codes using the rules',
            metavar='',
            dest='verbum_simplex',
            nargs='?'
        )

        neo_codex.add_argument(
            '--verbum-limiti',
            help='Codeword limit when when creating multiplication tables' +
            'Most western codetables are between 2 and 4. ' +
            'Defaults to 2',
            metavar='verbum_limiti',
            default="2",
            nargs='?'
        )

        neo_codex.add_argument(
            '--codex-verbum-tabulae',
            help='Multiplication table of the code words. ' +
            'First character determine the spliter. ' +
            'Example 1: " 0 1 2 3 4 5 6 7 8 9 a b c d e f ". '
            'Example 2: ",a,e,i,o,u,"',
            nargs='?'
        )

        neo_codex.add_argument(
            '--resultatum-limiti',
            help='Codeword limit when when creating multiplication tables' +
            'Most western codetables are between 2 and 4. ' +
            'Defaults to 2',
            metavar='verbum_limiti',
            default="2",
            nargs='?'
        )

        neo_tabulam_numerae = parser.add_argument_group(
            "neo-tabulam-numerae",
            "Automated generation of numerical tables")

        neo_tabulam_numerae.add_argument(
            '--actionem-tabulam-numerae',
            help='Define mode to numetical tables',
            metavar='',
            dest='neo_tabulam_numerae',
            const=True,
            nargs='?'
        )

        neo_scripturam = parser.add_argument_group(
            "neo-scripturam",
            "(internal use) Operations related to associate new symbols " +
            "to entire new writing systems without users needing to " +
            "pre-translate to existing tables.")

        neo_scripturam.add_argument(
            '--actionem-neo-scripturam',
            help='(required) Define mode actionem-neo-scripturam',
            metavar='',
            dest='neo_scripturam',
            const=True,
            nargs='?'
        )

        # cifram, https://translate.google.com/?sl=la&tl=en&text=cifram&op=translate
        decifram = parser.add_argument_group(
            "decifram",
            "Decipher (e.g. the act of decode numeric codes)")

        decifram.add_argument(
            '--actionem-decifram',
            help='(required) Define mode decifram',
            metavar='',
            dest='actionem_decifram',
            const=True,
            nargs='?'
        )
        decifram = parser.add_argument_group(
            "cifram",
            "Cifram (e.g. the act of encode first column of data on B60)")

        decifram.add_argument(
            '--actionem-cifram',
            help='(required) Define mode decifram',
            metavar='',
            dest='actionem_cifram',
            const=True,
            nargs='?'
        )

        # https://stackoverflow.com/questions/59661738/argument-dependency-in-argparse
        # Scriptura cuneiformis
        # https://en.wikipedia.org/wiki/Cuneiform#Decipherment
        # https://la.wikipedia.org/wiki/Scriptura_cuneiformis
        neo_scripturam.add_argument(
            '--neo-scripturam-tabulae-symbola',
            help='(internal use) Inject reference table. ' +
            'This requires entire list of the used base system ' +
            ' (e.g. 60 items for base64 items.' +
            'First character determine the spliter. ' +
            'Example 1: ",0,1,(.....),8,9,"',
            metavar='neo_scripturam_tabulae',
            dest='neo_scripturam_tabulae',
            # default="2",
            nargs='?'
        )

        neo_scripturam.add_argument(
            '--neo-scripturam-tabulae-hxl-nomini',
            help='(internal use) Inject reference table. ' +
            'An HXL Standard tag name.' +
            'Default: #item+rem+i_mul+is_zsym+ix_ndt60+ix_neo',
            dest='neo_scripturam_nomini',
            default="#item+rem+i_mul+is_zsym+ix_ndt60+ix_neo",
            nargs='?'
        )

        neo_scripturam.add_argument(
            '--neo-scripturam-tabulae-hxl-selectum',
            help='(internal use) Inject reference table. ' +
            'When exporting, define some pattern tags must have' +
            'Example: ix_neo',
            dest='neo_scripturam_hxl_selectum',
            default=None,
            nargs='?'
        )

        parser.add_argument(
            '--verbose',
            help='Verbose output',
            metavar='verbose',
            nargs='?'
        )
        if hxl_output:
            parser.add_argument(
                'outfile',
                help='File to write (if omitted, use standard output).',
                nargs='?'
            )

        # print('oioioi', parser)
        return parser.parse_args()

    # def execute_cli(self, args, stdin=STDIN, stdout=sys.stdout,
    #                 stderr=sys.stderr):
    def execute_cli(self, pyargs, stdin=STDIN, stdout=sys.stdout,
                    stderr=sys.stderr):
        # print('TODO')

        self.pyargs = pyargs

        ndt2600 = NDT2600()

        # ndt2600 = NDT2600()

        # print('self.pyargs', self.pyargs)

        ndt2600.est_verbum_limiti(args.verbum_limiti)
        ndt2600.est_resultatum_separato(args.resultatum_separato)

        if args.codex_verbum_tabulae:
            ndt2600.est_codex_verbum_tabulae(args.codex_verbum_tabulae)

        if args.neo_scripturam_tabulae:
            ndt2600.est_neo_scripturam_tabulae(
                args.neo_scripturam_tabulae, args.neo_scripturam_nomini)

# printf "abc\tABC\nefg\tEFG\n" | ./999999999/0/2600.py --actionem-cifram
# cat 999999/1603/47/639/3/1603.47.639.3.tab | head | tail -n 4 | ./999999999/0/2600.py --actionem-cifram
        if self.pyargs.actionem_cifram:

            if stdin.isatty():
                print("ERROR. Please pipe data in. \nExample:\n"
                      "  cat data.tsv | {0} --actionem-cifram\n"
                      "  printf \"abc\\nefg\\n\" | {0} --actionem-cifram"
                      "".format(__file__))
                return self.EXIT_ERROR

            for line in sys.stdin:
                codicem = line.replace('\n', ' ').replace('\r', '')
                neo_lineam = ndt2600.cifram_lineam(codicem)
                sys.stdout.writelines("{0}\n".format(neo_lineam))
            return self.EXIT_OK

        if self.pyargs.actionem_decifram:

            if stdin.isatty():
                print("ERROR. Please pipe data in. \nExample:\n"
                      "  cat data.txt | {0} --actionem-decifram\n"
                      "  printf \"1234\\n5678\\n\" | {0} --actionem-decifram"
                      "".format(__file__))
                return self.EXIT_ERROR

            for line in sys.stdin:
                codicem = line.replace('\n', ' ').replace('\r', '')
                fontem = ndt2600.decifram_codicem_numerae(codicem)
                sys.stdout.writelines(
                    "{0}{1}{2}\n".format(
                        codicem, args.resultatum_separato, fontem)
                )
            return self.EXIT_OK

        if self.pyargs.neo_tabulam_numerae:
            # tabulam_multiplicatio = ndt2600.quod_tabulam_multiplicatio()
            tabulam_numerae = ['TODO']
            return self.output(tabulam_numerae)

        if self.pyargs.verbum_simplex:
            tabulam_multiplicatio = ndt2600.quod_tabulam_multiplicatio()
            return self.output(tabulam_multiplicatio)

        if self.pyargs.codex_completum:
            tabulam_multiplicatio = ndt2600.quod_codex()
            return self.output(tabulam_multiplicatio)

        if self.pyargs.neo_scripturam:
            scientia = ndt2600.exportatum_scientia_de_scriptura(
                args.neo_scripturam_hxl_selectum)
            return self.output(scientia)

        # Let's default to full table
        tabulam_multiplicatio = ndt2600.quod_codex()
        return self.output(tabulam_multiplicatio)
        # print('unknow option.')
        # return self.EXIT_ERROR

    def output(self, output_collectiom):
        for item in output_collectiom:
            # TODO: check if result is a file instead of print

            # print(type(item))
            if isinstance(item, int) or isinstance(item, str):
                print(item)
            else:
                print(self.pyargs.resultatum_separato.join(item))

        return self.EXIT_OK

# if not sys.stdin.isatty():
#     print ("not sys.stdin.isatty")
# else:
#     print ("is  sys.stdin.isatty")

# import fcntl
# import os
# import sys

# # make stdin a non-blocking file
# fd = sys.stdin.fileno()
# fl = fcntl.fcntl(fd, fcntl.F_GETFL)
# fcntl.fcntl(fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)

# try:
#     print(sys.stdin.read())
# except:
#     print('No input')

# from sys import stdin
# from os import isatty

# is_pipe = not isatty(stdin.fileno())

# print('is_pipe', is_pipe)


if __name__ == "__main__":

    cli_2600 = CLI_2600()
    args = cli_2600.make_args()
    # pyargs.print_help()

    # args.execute_cli(args)
    cli_2600.execute_cli(args)


# import itertools
# valueee = list(permutations([1, 2, 3]))
# valueee = list(permutations([1, 2, 3]))

# print(valueee)

# ndt2600 = NDT2600()

# # print(quod_1613_2_60_datum())
# # print(ndt2600)

# print('0')
# print(ndt2600.quod_numerordinatio_digitalem('0', True))
# print('05')
# print(ndt2600.quod_numerordinatio_digitalem('05', True))
# print('zz')
# print(ndt2600.quod_numerordinatio_digitalem('zz', True))
