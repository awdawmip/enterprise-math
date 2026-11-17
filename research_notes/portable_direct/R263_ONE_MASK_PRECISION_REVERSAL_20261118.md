# R263 — precision reversal for the minimal zero-only observer

Date: 2026-11-18 (Asia/Shanghai). Status: **AUTHOR_PROVED / EXACT_FINITE_CERTIFICATE / NOT_REVIEWED**.
Parent sources: R260, R262. Frozen scientific input pin: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.

## Exact theorem

For the R256 auxiliary 63-mask positive rational scalar model with
`s=67/169`, `J=1184397599`, `T=989553240`,
`K=3805974000`, define the normalized integer sequences
`q_(m,k)=JT^k h_(m,k)/K` for `k>=3`.

The minimum number of original labels needed to decide the all-63-source
**simultaneous-zero predicate** by the conjunction of those labels' zero
tests is **four modulo 13** (R262, masks [9,10,13,26]) but is **one
modulo 169**, with the explicit singleton mask `[57]`.

Thus an additional p-adic precision layer can strictly **decrease**
the Boolean observer's minimal labelled input count, even though
value-preserving constant-linear reconstruction may demand more inputs.

## Self-contained mod-169 proof

Mask 57 has order `d=5`, characteristic polynomial (ascending
coefficients modulo 169)

`C_57(x) = x^5+2x^4+166x^3+104x^2`.

The first five exact normalized outputs at k=3,4,5,6,7 are
`[54,58,150,4,156]` modulo 169.

The accompanying integer checker generates the next 78 shifts and
verifies **all five** equations `q_(57,3+j+78)=q_(57,3+j)`
for `j=0,1,2,3,4`. Since `C_57` is monic, induction proves that
the *entire infinite sequence* has period 78. The full 78-term list
is stored in `R263_verification.json`, and every term is nonzero
modulo 169. The check also establishes that no proper divisor
of 78 is a period.

Consequently `q_(57,k) != 0 mod 169` for every k>=3;
the all-63-mask simultaneous-zero predicate is false at every event.
The singleton `[57]` has the identical predicate, while the empty
observer's all-zero conjunction is vacuously true. Hence its exact
minimal cardinality is **one**.

At the two mod-13 simultaneous-zero events of R256, k=1093 and
k=2185 (in the declared full 2184 period), the extra information
is explicit:

`q_(57,1093) = q_(57,2185) = 156 = 12*13 mod 169`.

These sources vanish modulo 13 at those events but are detectable
at the next precision layer.

## Reproducibility and scope

Run `python R263_precision_reversal_zero_observer.py` alongside
the frozen R260 helper `R260_labelled_modular_quotient.py`.
The script recomputes the exact initial normalized coefficients,
checks all five shifted taps, all 78 entries and the two event
witnesses. It passed with integer modular arithmetic; no analytic
approximation is involved. The 78-term period certificate is separately
saved as JSON. Mathematical acceptance remains NOT_REVIEWED.

The statement concerns the declared auxiliary scalar mask observer
and one Boolean predicate. It is not a native signed BRC port or an
X6 physical dynamics result.

## Next

Study mod `13^a` for `a>=3` at the same R256 input, and
distinguish existence of one eternally nonzero source, a minimal
zero-only cover, and full value reconstruction. Transfer only
through a typed, provenance-preserving BRC interface.
