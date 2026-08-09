"""ABC specialization of the generic certificate-image saturation defect.

For a primitive abc relation, the arithmetic Wronskian image on the exact
relation-adapted derivative lattice is ``D Z``.  Pasten's residual divisibility
gives a fixed positive integer

    M = m(a)m(b)m(c)

that divides every Wronskian value.  Hence the normalized certificate

    eta_signed = W / M

is an integer-valued group homomorphism on the relation lattice and its image is

    (D/M) Z = eta_min Z.

Therefore ``eta_min`` is exactly the saturation index of the normalized scalar
certificate image in ``Z``.  Its prime factorization is the finite congruence
obstruction spectrum already computed by the P025 local-absorption layer.
"""

from __future__ import annotations

from dataclasses import dataclass

from .abc_absorption_local import absorption_obstruction_spectrum
from .abc_block_value_lattice import block_value_lattice_invariants


@dataclass(frozen=True)
class NormalizedWronskianCertificateIndex:
    abc: tuple[int, int, int]
    raw_wronskian_image_generator: int
    residual_product: int
    normalized_image_generator: int
    normalized_saturation_index: int
    obstruction_spectrum: tuple[tuple[int, int], ...]


def normalized_wronskian_certificate_index(
    a: int, b: int, c: int
) -> NormalizedWronskianCertificateIndex:
    """Return the exact normalized Wronskian certificate saturation defect."""
    invariants = block_value_lattice_invariants(a, b, c)
    D = invariants.wronskian_image_generator
    M = invariants.residual_product
    if D % M:
        raise AssertionError("Pasten residual product must divide Wronskian image generator")
    normalized = D // M
    if normalized != invariants.absorption_floor:
        raise AssertionError("normalized certificate generator must equal eta_min")
    spectrum = absorption_obstruction_spectrum(a, b, c)
    reconstructed = 1
    for prime, exponent in spectrum:
        reconstructed *= prime**exponent
    if reconstructed != normalized:
        raise AssertionError("local obstruction spectrum must factor certificate saturation index")
    return NormalizedWronskianCertificateIndex(
        abc=(a, b, c),
        raw_wronskian_image_generator=D,
        residual_product=M,
        normalized_image_generator=normalized,
        normalized_saturation_index=normalized,
        obstruction_spectrum=spectrum,
    )
