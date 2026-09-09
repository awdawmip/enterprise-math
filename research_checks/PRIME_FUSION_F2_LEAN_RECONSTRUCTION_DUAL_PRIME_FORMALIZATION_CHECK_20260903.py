#!/usr/bin/env python3
"""Revision guard for Prime Fusion F2-L04 structural field characterization.

The Driver-requested repair is semantic: the fixed-channel field predicate must
assert fieldness of the existing ZMod quotient operations independently of
modulus primality, and the converse theorem must prove primality from that
fieldness.  The authoritative proof gate remains the pinned warnings-fatal Lean
build; this checker prevents the rejected circular encoding from reappearing.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECON = ROOT / "EnterpriseMath/PrimeFusion/Reconstruction.lean"
DUAL = ROOT / "EnterpriseMath/PrimeFusion/DualPrime.lean"
FACADE = ROOT / "EnterpriseMath/PrimeFusion.lean"


def strip_comments(text: str) -> str:
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


def assert_structural_field_predicate(dual: str) -> None:
    code = strip_comments(dual)
    match = re.search(
        r"def\s+FixedChannelPrimeFieldPair\s*\(a b : ℤ\)\s*:\s*Prop\s*:=\s*(.*?)\n\n",
        code,
        flags=re.S,
    )
    if not match:
        raise AssertionError("F2-L04: cannot locate FixedChannelPrimeFieldPair definition")
    body = match.group(1)
    require(
        body,
        [
            "IsField (ZMod (Nmodulus a b))",
            "IsField (ZMod (Cmodulus a b))",
            "Nmodulus a b ≠ Cmodulus a b",
        ],
        "F2-L04 structural predicate",
    )
    if ".Prime" in body or "Nat.Prime" in body:
        raise AssertionError(
            "F2-L04 structural predicate must not store modulus primality"
        )


def main() -> None:
    recon = RECON.read_text(encoding="utf-8")
    dual = DUAL.read_text(encoding="utf-8")
    facade = FACADE.read_text(encoding="utf-8")

    reject_proof_escapes(recon, RECON.as_posix())
    reject_proof_escapes(dual, DUAL.as_posix())
    assert_structural_field_predicate(dual)

    # Preserve the already-accepted T7/T8 surface while certifying the exact
    # Driver-requested noncircular converse.
    require(
        recon,
        [
            "theorem idempotent_universal_channel_split",
            "theorem reconstruct_positive_cell_of_diagonal_roots",
            "theorem reconstruct_positive_primitive_cell_of_diagonal_roots",
            "theorem reconstructed_strict_interior_gate",
        ],
        "F2 T7 preservation",
    )
    require(
        dual,
        [
            "theorem dualPrime_iff_squarefreeSemiprime_mul",
            "theorem zmod_isField_of_prime",
            "theorem zmod_prime_of_isField",
            "hfield : IsField (ZMod n)",
            "hfield.isDomain",
            "CharP.char_is_prime (ZMod n) n",
            "theorem fixed_channel_prime_fields_and_orders",
            "theorem fixed_channel_prime_field_product",
            "theorem fixedChannelPrimeFieldPair_dualPrime",
            "zmod_prime_of_isField hN1 h.1",
            "zmod_prime_of_isField hC1 h.2.1",
            "theorem fixedChannelPrimeFieldPair_iff_dualPrime",
            "zmod_isField_of_prime hN",
            "zmod_isField_of_prime hC",
        ],
        "F2-L04 field/prime bridge",
    )
    require(
        facade,
        [
            "#print axioms EnterpriseMath.PrimeFusion.zmod_prime_of_isField",
            "#print axioms EnterpriseMath.PrimeFusion.fixedChannelPrimeFieldPair_dualPrime",
            "#print axioms EnterpriseMath.PrimeFusion.fixedChannelPrimeFieldPair_iff_dualPrime",
        ],
        "F2-L04 axiom audit surface",
    )

    print("Prime Fusion F2-L04 structural-field revision guard: PASS")


if __name__ == "__main__":
    main()
