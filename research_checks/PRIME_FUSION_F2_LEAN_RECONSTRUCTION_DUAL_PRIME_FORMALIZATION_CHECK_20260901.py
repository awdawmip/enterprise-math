#!/usr/bin/env python3
"""Static acceptance guard for Prime Fusion F2 T7/T8 Lean formalization.

This checker is intentionally narrow. The authoritative elaboration/build gate is
`lake build --wfail -KCI EnterpriseMath`; here we additionally guard the expected
F2 theorem surface and reject proof escapes in the two new source modules.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECON = ROOT / "EnterpriseMath/PrimeFusion/Reconstruction.lean"
DUAL = ROOT / "EnterpriseMath/PrimeFusion/DualPrime.lean"
FACADE = ROOT / "EnterpriseMath/PrimeFusion.lean"


def strip_comments(text: str) -> str:
    """Remove nested Lean block comments and line comments, preserving strings."""
    out: list[str] = []
    i = 0
    depth = 0
    in_string = False
    while i < len(text):
        if depth:
            if text.startswith("/-", i):
                depth += 1
                i += 2
            elif text.startswith("-/", i):
                depth -= 1
                i += 2
            else:
                i += 1
            continue
        if in_string:
            out.append(text[i])
            if text[i] == "\\" and i + 1 < len(text):
                out.append(text[i + 1])
                i += 2
                continue
            if text[i] == '"':
                in_string = False
            i += 1
            continue
        if text.startswith("/-", i):
            depth = 1
            i += 2
            continue
        if text.startswith("--", i):
            end = text.find("\n", i)
            if end == -1:
                break
            out.append("\n")
            i = end + 1
            continue
        if text[i] == '"':
            in_string = True
        out.append(text[i])
        i += 1
    if depth:
        raise AssertionError("unterminated Lean block comment")
    return "".join(out)


def require(text: str, needles: list[str], label: str) -> None:
    missing = [needle for needle in needles if needle not in text]
    if missing:
        raise AssertionError(f"{label}: missing required surface: {missing}")


def reject_proof_escapes(text: str, label: str) -> None:
    code = strip_comments(text)
    forbidden = {
        "sorry": r"\bsorry\b",
        "admit": r"\badmit\b",
        "axiom declaration": r"(^|\n)\s*axiom\s+",
        "unsafe declaration": r"(^|\n)\s*unsafe\s+",
    }
    hits = [name for name, pattern in forbidden.items() if re.search(pattern, code)]
    if hits:
        raise AssertionError(f"{label}: forbidden proof escape(s): {hits}")


def main() -> None:
    recon = RECON.read_text(encoding="utf-8")
    dual = DUAL.read_text(encoding="utf-8")
    facade = FACADE.read_text(encoding="utf-8")

    reject_proof_escapes(recon, RECON.as_posix())
    reject_proof_escapes(dual, DUAL.as_posix())

    require(
        recon,
        [
            "theorem idempotent_universal_channel_split",
            "theorem channels_isCoprime_implies_primitive",
            "theorem positive_cell_channel_orientation",
            "theorem reconstruction_square_gate_necessary",
            "theorem no_reconstruction_if_U_not_square",
            "theorem no_positive_reconstruction_if_not_oriented",
            "theorem reconstruct_positive_cell_of_diagonal_roots",
            "have hrootParity : Even U ↔ Even V",
            "theorem reconstruct_positive_primitive_cell_of_diagonal_roots",
            "theorem reconstructed_strict_interior_gate",
        ],
        "F2 reconstruction",
    )
    require(
        dual,
        [
            "def SquarefreeSemiprime",
            "theorem dualPrime_iff_squarefreeSemiprime_mul",
            "def FixedChannelPrimeFieldPair",
            "theorem fixed_channel_prime_fields_and_orders",
            "theorem fixed_channel_prime_field_product",
            "pointedCRT a b hab",
            "theorem fixed_channels_dualPrime_iff_squarefreeSemiprime",
            "theorem fixedChannelPrimeFieldPair_iff_dualPrime",
        ],
        "F2 dual-prime",
    )
    require(
        facade,
        [
            "import EnterpriseMath.PrimeFusion.Reconstruction",
            "import EnterpriseMath.PrimeFusion.DualPrime",
            "#print axioms EnterpriseMath.PrimeFusion.idempotent_universal_channel_split",
            "#print axioms EnterpriseMath.PrimeFusion.reconstruct_positive_cell_of_diagonal_roots",
            "#print axioms EnterpriseMath.PrimeFusion.reconstruct_positive_primitive_cell_of_diagonal_roots",
            "#print axioms EnterpriseMath.PrimeFusion.dualPrime_iff_squarefreeSemiprime_mul",
            "#print axioms EnterpriseMath.PrimeFusion.fixed_channel_prime_field_product",
        ],
        "PrimeFusion facade/axiom audit",
    )

    print("Prime Fusion F2 static acceptance: PASS")


if __name__ == "__main__":
    main()
