# C301 — Exact primitive coefficient 1-norm and short-strip adaptive denominator height

**2026-10-25 | AUTHOR_EXACT | SOURCE-EXPOSED | NO NATIVE CLAIM | NOT ADMITTED**

## Frozen basis and control

Verified account GLOBAL_KNOWLEDGE_V1 canonical main `d2c4b5e66fcabee0cebf65b18bb46ac17dfa5d70` and Enterprise Math main `d34d39e9e13b28ea5a509ad180a012cbf17102b8`, including bootstrap/manual, P000, ACTIVE worldview, code/math/BRC policy, native X6, observer-preservation contract, AGENTS and current portable research protocol. Predecessor C300 author frontier is the immutable commit `5f03468054ef8cfa14b19eea69ca044d0f5a53dc`. Reuse exactly the 125 frozen C293 affine paths and dyadic short strips with C275/C284/C288/C293/C298/C300 evidence in the portable research package.

GitHub login actually read: `awdawmip`; repository push permission true. Native EM `em_control_tasks` returned `CONTROL_QUOTA`; `em_session_start` returned `STATIC_READONLY_SCOPE_DENIED`, `operation_sent=false`. Thus owner/claim authority is **not established**. This author-branch artifact is not a canonical Source CLAIM, Result, Driver review or mathematical admission.

Scope: ONLY the C195/H168 positive-rational 79-branch scalar auxiliary function `f_i(t)=F(w_i+t d_i)/2^128`. No native signed/phase GF(2)-BRC or P000 six-dimensional Cell theorem follows.

## Definitions

For every path i, let `f_i=A_i/D_i` be C298's integral shared-denominator representation. Its least-common-multiple positive scalar is `s_i` and its denominator primitive `Z[t]` factor multiset is `(G_i,e_i(q))`. The two linear factors `C_i={q_02,q_13}` canceled by an **exact** C299/C300 proof are removed **once**. The resulting integer denominator is

```
D_i^red(t) = s_i * PRODUCT[q(t)^e_i(q), q in G_i \ C_i].
```

Its numerator `A_i^red` is an integer polynomial by the inherited exact cancellation. C300 proves no additional nonconstant polynomial gcd over Q[t]; C301 does **not** assert that the numerator and denominator share no *scalar* integer gcd.

## Theorem I — actual coefficient content and L1 norm

Let `P_i(t)=D_i^red(t)/s_i`. Every q is primitive in Z[t]; Gauss's lemma gives `content(P_i)=1`, hence `content(D_i^red)=s_i` exactly. The independent direct integer coefficient gcd calculation verified content 1 for **125/125** P_i.

Define `L_i=s_i*sum_j |[t^j]P_i|` and let `H_i^coef` be the least nonnegative integer with `L_i<2^H_i^coef`. For `0<=t<=1`,

```
0 < D_i^red(t) <= L_i < 2^H_i^coef.
```

Exact full 125-path polynomial expansion gives `max_i H_i^coef=13704` (path index 63), improving C300's conservative product-of-norms height 13713. Reduced degrees remain 352 for 124 paths and 265 for special path 28, as proved in C300. Integer scalar content bit-width across paths is 4758..5623. These are exact calculations of coefficient norms; no floating point decision.

## Theorem II — sharper local denominator bound for continuous t

Write the frozen C293 strip `I_i=[a_i,b_i]=[k_i/2^24,(k_i+1)/2^24]`. Every primitive factor has a positive orientation throughout I_i. Affine linear q is monotone; constant q is trivial. Each nonlinear degree-12 q is a positive scalar multiple of `[(2-x(t)^2)(3-x(t)^2)]^3` where `x(t)=w+dt`, `d!=0`, and `0<x(t)<1` on I_i. For `h(x)=[(2-x^2)(3-x^2)]^3`,

```
h'(x) = -6*x*(5-2*x^2)*[(2-x^2)(3-x^2)]^2 < 0     (0<x<1).
```

Thus every primitive q has strip maximum at one endpoint. Define an **exact rational**

```
U_i = s_i * PRODUCT[max(q(a_i),q(b_i))^e_i(q), q in G_i \ C_i],
H_i^strip = min{h>=0: U_i<2^h}.
```

For **every real t in I_i**, `0<D_i^red(t)<=U_i<2^H_i^strip`. All 125 exact rational evaluations yield `max_i H_i^strip=13702`, attained at index 63. Every path improves its own C300 product norm height by 10..17 bits. The local bound is 1 or 2 bits below the exact coefficient L1 height on every path. Special path 28: `d_28=265`, `H_28^strip=10767`.

## Theorem III — sufficient dyadic sign precision (conditional on C297)

For `t=k/2^b` within its strip, `A_i^red-D_i^red` is an integer polynomial of degree at most `d_i=deg(D_i^red)`. If `f_i(t)!=1`, multiplying by `2^(b*d_i)` gives a nonzero integer and hence

```
|f_i(k/2^b)-1| > 2^(-d_i*b-H_i^strip).
```

Assuming the **inherited** C297 continuous-strip fixed-point interval evaluator has actual normalized enclosure width `<2^(134-P)`, strict sign is provably decided when

```
P >= d_i*b + H_i^strip + 134.
```

Uniformly `P=352*b+13702+134` is sufficient. For b=512: uniform old C300 bound `194071`, new `194060`; path 28 using its actual degree and local height: `265*512+10767+134=146581`. These are conservative *sufficient precision bounds*, not measured runtime, nor optimality. If the dyadic point is an exact root, strict sign is not certifiable at any finite precision.

## Actual checks, evidence and limits

The attached portable C301 zip contains all 125 per-path coefficient SHA256 records and exact height audit, frozen predecessor inputs, expanded English proof, scripts and execution logs. Three actual programs:

1. `C301_PRIMITIVE_COEFF_EXACT.py`: 125/125 exact integer convolutions, coefficient gcd=1, exact coefficient L1 and degree assertions. Output `C301_PRIMITIVE_COEFFICIENT_EXACT_PASS`.
2. `C301_STRIP_ADAPTIVE_HEIGHT_EXACT.py`: 125/125 strictly positive short strips, exact rational factor maxima and height proofs. Output `C301_STRIP_ADAPTIVE_HEIGHT_EXACT_PASS`.
3. `C301_INDEPENDENT_POLYNOMIAL_CROSSCHECK.py`: nine selected paths `{0,8,24,28,40,63,64,96,124}` recomputed via `sympy.Poly(...,domain=ZZ)` and full coefficient vectors compared; output `C301_INDEPENDENT_SYMPY_COEFFS_9_OF_125_PASS`. Nine is **not** 125 independent crosschecks.

The C300 two-zero-residue and all remaining poles are inherited author-level algebraic evidence; C297 outward-width theorem was **not independently replayed** here. C301 itself is not a Lean/formal checker result. No native GF(2)-BRC execution was done. The canceled scalar residues `(r,-r)` remain distinct branch/provenance data for observers and future operations.

## Next smallest research unit (C302)

Compute the primitive *integer numerator-denominator pair* by determining `gcd(content(A_i^red),s_i)` exactly (or a certified p-adic factor analysis). Quantify the further denominator-height saving while retaining independent branch provenance. Separately construct a typed native BRC/X6 observer/future-operation bridge; until this is proved, auxiliary scalar cancellations cannot be elevated to native equivalence.

## Portable archive

Filename: `EM_C301_PRIMITIVE_AND_STRIP_HEIGHTS_EXACT_PORTABLE.zip`.
SHA256: `6b73d69cf5da7f1f00141e12f104c6c98007f447afa310c3410ad0392028a7fd`.
Archive integrity: 26 file SHA256 records verified, 125 paths, successful local isolated exact runs. The archive was delivered in the chat artifact surface; not claimed to be stored as a Git blob in this repository.
