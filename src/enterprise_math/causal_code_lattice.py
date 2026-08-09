"""Binary conservation codes as generators of integer causal lattice shadows.

Let C be a binary code of length N and consider integer slot states whose residue
modulo two lies in C (the unscaled Construction-A preimage).  Two elementary
families of integer events compete under the square-grade sum delta_i^2:

* residue-preserving axis events +/-2e_i have grade 4;
* a nonzero codeword of Hamming weight w lifts to events with +/-1 on its support,
  one for each sign assignment, and has grade w.

Thus the minimum primitive grade is min(4,d_H(C)), with d_H=infinity for the zero
code.  Minimum-grade events are generated accordingly.  For the even-parity
single-check code d_H=2, the primitive family is the D_N root grammar.  For the
extended [8,4,4] Hamming code d_H=4, the grade tie gives 16 axis +/-2 events plus
14*16=224 weight-four sign lifts, totaling 240 primitive events, the E8 root
count after the conventional Construction-A normalization/rotation.

Construction A and code facts are classical prior mathematics.  This module uses
them as a computational shadow of a causal conservation-kernel / minimum-grade
story; it does not claim invention of code lattices.
"""

from __future__ import annotations

from collections import Counter
from itertools import product

BitWord = tuple[int, ...]
Vector = tuple[int, ...]


def hamming_weight(word: BitWord) -> int:
    if any(bit not in (0, 1) for bit in word):
        raise ValueError("binary word entries must be 0/1")
    return sum(word)


def binary_span(generator_rows: tuple[BitWord, ...]) -> tuple[BitWord, ...]:
    if not generator_rows:
        raise ValueError("at least one binary generator row is required")
    width = len(generator_rows[0])
    if width == 0 or any(len(row) != width for row in generator_rows):
        raise ValueError("generator rows must have equal positive width")
    if any(bit not in (0, 1) for row in generator_rows for bit in row):
        raise ValueError("generator rows must be binary")
    code = set()
    for coefficients in product((0, 1), repeat=len(generator_rows)):
        word = tuple(
            sum(coef * row[index] for coef, row in zip(coefficients, generator_rows)) % 2
            for index in range(width)
        )
        code.add(word)
    return tuple(sorted(code))


def minimum_hamming_weight(codewords: tuple[BitWord, ...]) -> int | None:
    nonzero = [hamming_weight(word) for word in codewords if any(word)]
    return min(nonzero) if nonzero else None


def weight_histogram(codewords: tuple[BitWord, ...]) -> dict[int, int]:
    return dict(sorted(Counter(hamming_weight(word) for word in codewords).items()))


def extended_hamming_8_code() -> tuple[BitWord, ...]:
    rows = (
        (1, 0, 0, 0, 1, 1, 0, 1),
        (0, 1, 0, 0, 1, 0, 1, 1),
        (0, 0, 1, 0, 0, 1, 1, 1),
        (0, 0, 0, 1, 1, 1, 1, 0),
    )
    return binary_span(rows)


def even_parity_code(length: int) -> tuple[BitWord, ...]:
    if isinstance(length, bool) or not isinstance(length, int) or length < 2:
        raise ValueError("length must be at least two")
    return tuple(
        tuple(word)
        for word in product((0, 1), repeat=length)
        if sum(word) % 2 == 0
    )


def axis_grade_four_events(length: int) -> set[Vector]:
    if length < 1:
        raise ValueError("length must be positive")
    result = set()
    for index in range(length):
        for sign in (-2, 2):
            vector = [0] * length
            vector[index] = sign
            result.add(tuple(vector))
    return result


def codeword_sign_lifts(word: BitWord) -> set[Vector]:
    support = [index for index, bit in enumerate(word) if bit]
    if not support:
        return set()
    result = set()
    for signs in product((-1, 1), repeat=len(support)):
        vector = [0] * len(word)
        for index, sign in zip(support, signs):
            vector[index] = sign
        result.add(tuple(vector))
    return result


def construction_a_primitive_grade(codewords: tuple[BitWord, ...]) -> int:
    if not codewords:
        raise ValueError("codeword set must be non-empty")
    width = len(codewords[0])
    if width == 0 or any(len(word) != width for word in codewords):
        raise ValueError("codewords must have equal positive length")
    distance = minimum_hamming_weight(codewords)
    return 4 if distance is None else min(4, distance)


def construction_a_primitive_events(codewords: tuple[BitWord, ...]) -> set[Vector]:
    grade = construction_a_primitive_grade(codewords)
    width = len(codewords[0])
    events: set[Vector] = set()
    if grade == 4:
        events |= axis_grade_four_events(width)
    for word in codewords:
        if any(word) and hamming_weight(word) == grade:
            events |= codeword_sign_lifts(word)
    return events


def event_square_grade(event: Vector) -> int:
    return sum(value * value for value in event)


def primitive_event_grade_is_uniform(codewords: tuple[BitWord, ...]) -> bool:
    events = construction_a_primitive_events(codewords)
    expected = construction_a_primitive_grade(codewords)
    return bool(events) and {event_square_grade(event) for event in events} == {expected}
