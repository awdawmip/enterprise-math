"""Current exact P022 low-order identifiability certificate through length 150.

The selected valuation rows below give a 151x151 integer matrix for segment
lengths 1..150 plus one hidden-tail generator.  Its determinant is nonzero
modulo 1,000,003, proving that joint M2/M3 values -- and therefore P011
(J1,J2,J3) -- uniquely determine all bounded segment multiplicities and the
hidden tail throughout this certified class.

Rows are recomputed directly from the central-binomial and Franel definitions;
no factor table is stored.
"""

from __future__ import annotations

from .p022_barlow_low_order_identifiability import (
    CERTIFICATE_MODULUS,
    determinant_mod_prime,
    p_adic_valuation,
    pair_moment_factor,
    triple_moment_factor,
)

MAX_CERTIFIED_SEGMENT_150 = 150
CERTIFICATE_150_DETERMINANT_RESIDUE = 973_381

CERTIFICATE_150_ROWS: tuple[tuple[str, int], ...] = (
    ("A",2),("A",3),("A",5),("A",7),("A",11),("A",13),("A",17),("A",19),("A",23),("A",29),
    ("A",31),("A",37),("A",41),("A",43),("A",47),("A",53),("A",59),("A",61),("A",67),("A",71),
    ("A",73),("A",79),("A",83),("A",89),("A",97),("A",101),("A",103),("A",107),("A",109),("A",113),
    ("A",127),("A",131),
    ("F3",2),("F3",5),("F3",7),("F3",13),("F3",23),("F3",29),("F3",31),("F3",37),("F3",41),
    ("F3",47),("F3",53),("F3",59),("F3",61),("F3",67),("F3",71),("F3",73),("F3",79),("F3",101),
    ("F3",109),("F3",127),("F3",131),("F3",151),("F3",157),("F3",173),("F3",251),("F3",269),
    ("F3",367),("F3",389),("F3",421),("F3",563),("F3",661),("F3",769),("F3",937),("F3",1361),("F3",2141),
    ("F3",337),("F3",281),("A",137),("A",139),("F3",107),("F3",359),("F3",2417),("F3",149),
    ("A",149),("A",151),("F3",179),("F3",2837),("A",157),("F3",227),("F3",457),("A",163),
    ("F3",167),("A",167),("F3",1579),("F3",3019),("A",173),("F3",3853),("F3",941),("A",179),
    ("A",181),("F3",4789),("F3",829),("F3",239),("F3",191),("A",191),("A",193),("F3",197),
    ("A",197),("A",199),("F3",103),("F3",2917),("F3",967),("F3",1123),("F3",2693),("A",211),
    ("F3",659),("F3",2003),("F3",5801),("F3",1013),("F3",223),("A",223),("F3",10331),("A",227),
    ("A",229),("F3",463),("A",233),("F3",1187),("F3",277),("A",239),("A",241),("F3",593),
    ("F3",7411),("F3",16111),("F3",231947),("A",251),("F3",311),("F3",22859),("A",257),("F3",66373),
    ("F3",263),("A",263),("F3",907),("F3",6037),("A",269),("A",271),("F3",3229),("F3",857),
    ("A",277),("F3",8147),("A",281),("A",283),("F3",467),("F3",3331),("F3",257),("F3",293),
    ("A",293),("F3",65699),("F3",20963),("F3",92083),
)


def _tail_row_value(kind: str, prime: int) -> int:
    if prime != 2:
        return 0
    return 2 if kind == "A" else 3


def identifiability_certificate_matrix_150() -> tuple[tuple[int, ...], ...]:
    rows = []
    for kind, prime in CERTIFICATE_150_ROWS:
        row = []
        for segment in range(1, MAX_CERTIFIED_SEGMENT_150 + 1):
            value = (
                pair_moment_factor(segment)
                if kind == "A"
                else triple_moment_factor(segment)
            )
            row.append(p_adic_valuation(value, prime))
        row.append(_tail_row_value(kind, prime))
        rows.append(tuple(row))
    matrix = tuple(rows)
    if len(matrix) != 151 or any(len(row) != 151 for row in matrix):
        raise AssertionError("length-150 certificate matrix must be 151x151")
    return matrix


def certificate_150_determinant_residue() -> int:
    return determinant_mod_prime(
        identifiability_certificate_matrix_150(), CERTIFICATE_MODULUS
    )


def verify_bounded_identifiability_certificate_150() -> bool:
    residue = certificate_150_determinant_residue()
    if residue != CERTIFICATE_150_DETERMINANT_RESIDUE:
        raise AssertionError("length-150 determinant certificate changed")
    return True
