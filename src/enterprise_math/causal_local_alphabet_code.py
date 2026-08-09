"""Local LEGO alphabet + residue code as a common primitive-event generator.

A code alone does not determine the integer/Euclidean primitive geometry.  Each
coordinate slot also has a local residue alphabet with an integer-normalized
minimum grade and multiplicity for each residue symbol, plus a zero-sector local
primitive event family.

For a codeword c=(c_i), its minimum joint representative grade and multiplicity
factor by slots:

    G(c) = sum_i g(c_i),
    M(c) = product_i mu(c_i).

The global primitive grade is the minimum of the zero-sector local primitive
grade and all nonzero codeword lift grades.  Primitive event multiplicity is the
sum of all families attaining that grade.

Two classical specializations are used as executable shadows:

* binary integer cell: zero-sector +/-2 events have normalized square grade 4
  and multiplicity 2 per slot; nonzero residue has grade 1 and multiplicity 2;
  [7,3,4] simplex and [8,4,4] extended Hamming codes give 126 and 240.
* ternary hexagonal/A2 cell: after multiplying the natural shell grading by 3,
  local A2 roots have grade 3 and multiplicity 6, while each of the two nonzero
  deep-hole residue sectors has grade 1 and multiplicity 3; the [3,1,3]_3
  repetition code gives 3*6 + 2*3^3 = 72, the E6 root count.

The code-lattice constructions are classical prior mathematics.  The project
uses this factorization as a causal ordering: local unit alphabet and residue
conservation are primitive, exceptional lattice data are shadows.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import prod
from typing import Hashable, Mapping

Symbol = Hashable
Codeword = tuple[Symbol, ...]


@dataclass(frozen=True)
class LocalResidueAlphabet:
    zero_symbol: Symbol
    zero_sector_primitive_grade: int
    zero_sector_primitive_multiplicity: int
    residue_grade: Mapping[Symbol, int]
    residue_multiplicity: Mapping[Symbol, int]

    def validate(self) -> None:
        symbols = set(self.residue_grade)
        if symbols != set(self.residue_multiplicity) or self.zero_symbol not in symbols:
            raise ValueError("grade and multiplicity maps must cover the same symbols including zero")
        if (
            isinstance(self.zero_sector_primitive_grade, bool)
            or not isinstance(self.zero_sector_primitive_grade, int)
            or self.zero_sector_primitive_grade <= 0
        ):
            raise ValueError("zero-sector primitive grade must be a positive integer")
        if (
            isinstance(self.zero_sector_primitive_multiplicity, bool)
            or not isinstance(self.zero_sector_primitive_multiplicity, int)
            or self.zero_sector_primitive_multiplicity < 0
        ):
            raise ValueError("zero-sector primitive multiplicity must be non-negative")
        if any(
            isinstance(value, bool) or not isinstance(value, int) or value < 0
            for value in self.residue_grade.values()
        ):
            raise ValueError("residue grades must be non-negative integers")
        if any(
            isinstance(value, bool) or not isinstance(value, int) or value <= 0
            for value in self.residue_multiplicity.values()
        ):
            raise ValueError("residue multiplicities must be positive integers")
        if self.residue_grade[self.zero_symbol] != 0 or self.residue_multiplicity[self.zero_symbol] != 1:
            raise ValueError("zero residue representative must have grade zero and multiplicity one")


def codeword_grade(word: Codeword, alphabet: LocalResidueAlphabet) -> int:
    alphabet.validate()
    try:
        return sum(alphabet.residue_grade[symbol] for symbol in word)
    except KeyError as error:
        raise ValueError("codeword uses a symbol outside the local residue alphabet") from error


def codeword_minimum_lift_multiplicity(word: Codeword, alphabet: LocalResidueAlphabet) -> int:
    alphabet.validate()
    try:
        return prod(alphabet.residue_multiplicity[symbol] for symbol in word)
    except KeyError as error:
        raise ValueError("codeword uses a symbol outside the local residue alphabet") from error


def primitive_grade_and_multiplicity(
    codewords: tuple[Codeword, ...],
    alphabet: LocalResidueAlphabet,
) -> tuple[int, int]:
    alphabet.validate()
    if not codewords:
        raise ValueError("codeword family must be non-empty")
    length = len(codewords[0])
    if length == 0 or any(len(word) != length for word in codewords):
        raise ValueError("codewords must have equal positive length")

    base_grade = alphabet.zero_sector_primitive_grade
    base_count = length * alphabet.zero_sector_primitive_multiplicity
    nonzero = [word for word in codewords if any(symbol != alphabet.zero_symbol for symbol in word)]
    code_grades = [codeword_grade(word, alphabet) for word in nonzero]
    primitive_grade = min([base_grade] + code_grades) if code_grades else base_grade

    multiplicity = base_count if base_grade == primitive_grade else 0
    for word, grade in zip(nonzero, code_grades):
        if grade == primitive_grade:
            multiplicity += codeword_minimum_lift_multiplicity(word, alphabet)
    return primitive_grade, multiplicity


def binary_integer_alphabet() -> LocalResidueAlphabet:
    return LocalResidueAlphabet(
        zero_symbol=0,
        zero_sector_primitive_grade=4,
        zero_sector_primitive_multiplicity=2,
        residue_grade={0: 0, 1: 1},
        residue_multiplicity={0: 1, 1: 2},
    )


def ternary_hexagonal_alphabet() -> LocalResidueAlphabet:
    return LocalResidueAlphabet(
        zero_symbol=0,
        zero_sector_primitive_grade=3,
        zero_sector_primitive_multiplicity=6,
        residue_grade={0: 0, 1: 1, 2: 1},
        residue_multiplicity={0: 1, 1: 3, 2: 3},
    )


def ternary_repetition_3_code() -> tuple[Codeword, ...]:
    return (
        (0, 0, 0),
        (1, 1, 1),
        (2, 2, 2),
    )


def e6_primitive_shadow() -> tuple[int, int]:
    return primitive_grade_and_multiplicity(
        ternary_repetition_3_code(),
        ternary_hexagonal_alphabet(),
    )
