"""Static square-class transport table for BRC multiplier sieve roots.

For the 75 admissible odd-N multipliers m<=100 there are 46 squarefree kernels
d in m=a^2*d.  For every odd prime p<=10000 this table stores:

* one fixed quadratic nonresidue z_p;
* for every kernel d, a 16-bit word encoding its square class modulo p and a
  transport coefficient c such that
    d = c^2              (QR class), or
    d = c^2 * z_p        (nonresidue class),
  with a dedicated zero/divisible code when p|d.

The bytes are derived classical finite-field data.  They are not theorem
content.  The table exists so one factorization target N needs only one
N-dependent modular square root per factor-base prime before all 75 multiplier
sieve-root pairs are obtained by table lookup and multiplication.
"""

from __future__ import annotations

from functools import lru_cache
from hashlib import sha256

from .brc_multiplier_sieve_root_table_shard0 import PAYLOAD as _S0
from .brc_multiplier_sieve_root_table_shard1 import PAYLOAD as _S1
from .brc_multiplier_sieve_root_table_shard2 import PAYLOAD as _S2
from .brc_multiplier_sieve_root_table_shard3 import PAYLOAD as _S3
from .brc_multiplier_sieve_root_table_shard4 import PAYLOAD as _S4
from .brc_multiplier_sieve_root_table_shard5 import PAYLOAD as _S5
from .brc_multiplier_sieve_root_table_shard6 import PAYLOAD as _S6
from .brc_multiplier_sieve_root_table_shard7 import PAYLOAD as _S7
from .legendre import primes_up_to

MAX_STATIC_PRIME = 10_000
KERNELS = (
    1, 2, 3, 5, 6, 7, 10, 11, 13, 14, 15, 17, 19, 21, 22, 23,
    29, 31, 33, 35, 37, 39, 41, 43, 47, 51, 53, 55, 57, 59, 61,
    65, 67, 69, 71, 73, 77, 79, 83, 85, 87, 89, 91, 93, 95, 97,
)
CLASS_DIVISIBLE = 0
CLASS_QUADRATIC_RESIDUE = 1
CLASS_NONRESIDUE = 2
ENTRY_BYTES = 2
ROW_BYTES = 2 + ENTRY_BYTES * len(KERNELS)
ODD_PRIME_COUNT = 1228
RAW_PAYLOAD_BYTES = 115_432
TABLE_SHA256 = "e2bf32a2ce0af1e7032466edf6eb84530253b0ad4a3b00e3d2202a2d8c31356d"

_PAYLOAD = _S0 + _S1 + _S2 + _S3 + _S4 + _S5 + _S6 + _S7
if len(_PAYLOAD) != RAW_PAYLOAD_BYTES:
    raise AssertionError("BRC sieve-root table payload length mismatch")
if sha256(_PAYLOAD).hexdigest() != TABLE_SHA256:
    raise AssertionError("BRC sieve-root table SHA-256 mismatch")

ODD_PRIMES = tuple(prime for prime in primes_up_to(MAX_STATIC_PRIME) if prime > 2)
if len(ODD_PRIMES) != ODD_PRIME_COUNT:
    raise AssertionError("unexpected odd-prime count for sieve-root table")
_PRIME_INDEX = {prime: index for index, prime in enumerate(ODD_PRIMES)}
_KERNEL_INDEX = {kernel: index for index, kernel in enumerate(KERNELS)}


@lru_cache(maxsize=None)
def static_squareclass_row(prime: int) -> tuple[int, tuple[int, ...]]:
    """Return ``(z_p, packed_kernel_words)`` for one checked-in prime."""
    index = _PRIME_INDEX.get(prime)
    if index is None:
        raise KeyError(f"prime {prime} is outside the static sieve-root table")
    start = index * ROW_BYTES
    row = _PAYLOAD[start : start + ROW_BYTES]
    nonresidue = int.from_bytes(row[:2], "big")
    words = tuple(
        int.from_bytes(
            row[2 + ENTRY_BYTES * i : 2 + ENTRY_BYTES * (i + 1)],
            "big",
        )
        for i in range(len(KERNELS))
    )
    return nonresidue, words


def unpack_kernel_word(word: int) -> tuple[int, int]:
    """Return ``(class_code, coefficient)`` from one 16-bit table word."""
    if isinstance(word, bool) or not isinstance(word, int) or not 0 <= word < 1 << 16:
        raise ValueError("word must be a 16-bit integer")
    return word >> 14, word & 0x3FFF


def static_kernel_transport(prime: int, kernel: int) -> tuple[int, int, int]:
    """Return ``(z_p,class_code,c)`` for a static prime/kernel pair."""
    kernel_index = _KERNEL_INDEX.get(kernel)
    if kernel_index is None:
        raise KeyError(f"kernel {kernel} is absent from the <=100 multiplier table")
    nonresidue, words = static_squareclass_row(prime)
    class_code, coefficient = unpack_kernel_word(words[kernel_index])
    return nonresidue, class_code, coefficient


def raw_payload() -> bytes:
    """Return the exact checked-in bytes for integrity/regeneration tests."""
    return _PAYLOAD


__all__ = [
    "MAX_STATIC_PRIME",
    "KERNELS",
    "CLASS_DIVISIBLE",
    "CLASS_QUADRATIC_RESIDUE",
    "CLASS_NONRESIDUE",
    "ENTRY_BYTES",
    "ROW_BYTES",
    "ODD_PRIME_COUNT",
    "RAW_PAYLOAD_BYTES",
    "TABLE_SHA256",
    "ODD_PRIMES",
    "static_squareclass_row",
    "unpack_kernel_word",
    "static_kernel_transport",
    "raw_payload",
]
