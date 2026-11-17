# R260 — Lossless finite-field labelled-observer quotient (R259C continuation)

Date: 2026-11-18, Asia/Shanghai. Status: **AUTHOR_PROVED / EXACT_COMPUTATION / NOT_REVIEWED**. Scientific freeze `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. This note treats the *auxiliary positive rational seven-source scalar observer*, **not** native signed-BRC dynamics, the native six-dimensional world, or a three-dimensional slice.

## Immutable input and scope

R259C scientific note, program and exact four-case orbit results: `awdawmip/enterprise-math@ef9619d3ed267d595415c47e4cc167e1754243ad`, files under `research_notes/portable_direct/R259_*`. For masks m=0,...,62, with `d_m=1+popcount(m)`, `q_(m,k)=J T^k h_(m,k)/K` is an **integer** for k>=3 and obeys the original monic order-d_m recurrence `C_m(x)`. R256/R257/R258 give their own exact values of rational s and J,T,K. Reduce **only** these integer outputs modulo one specified prime p.

## Theorem A: minimal common recurrence for all labelled channels

Over F_p, set `Q_m(z)=z^d C_m(1/z)` with Q_m(0)=1 and `N_m(z)=[Q_m(z) sum_(j=0)^(d-1) q_(m,3+j) z^j]_(<d)`. Reduce the rational function N_m/Q_m to a coprime numerator and denominator `B_m(z)` with B_m(0)=1, and set `f_m(x)=x^deg(B_m) B_m(1/x)`. For an identically zero sequence, f_m=1. The monic lcm `F=lcm_m f_m` is the unique minimal-degree scalar-coefficient recurrence shared by all 63 separate labelled modular sequences.

**Proof.** The recurrence and initial window determine the exact formal generating function N_m/Q_m. In reduced form its denominator B_m divides the reversal of every polynomial annihilating that infinite sequence, and B_m itself gives a recurrence. Hence f_m is its minimal annihilator. Annihilating all channels is equivalent to being a multiple of every f_m. The monic lcm is necessary and sufficient. This is an infinite-horizon algebraic result, not an inference from finite observation.

## Theorem B: a minimal constant-linear labelled observation basis

Let r=deg F, and form the 63-by-r matrix `M_(m,j)=q_(m,3+j) mod p`. Select original mask rows S forming an F_p row basis. For each mask m there are fixed coefficients a_(m,b) such that the initial r residues of m equal the corresponding combination of selected masks. Both sides obey F, so the equality holds for **every k>=3**. Thus all 63 residues vanish together exactly when the selected |S| residues vanish together, for every future event. The row rank |S| is minimal for **constant-coefficient reconstruction of all labelled modular outputs from a subset of mask channels**. It is not asserted minimal for nonlinear or Boolean zero-only tests, nor for native/provenance-sensitive observers.

## Verified exact four-case numerical algebra

| Case (frozen rational s) | p | Original joint-window size | deg F | Nonzero channels | rank M | Original mask basis S | Joint output period | Simultaneous zeros in one period |
|---|---:|---:|---:|---:|---:|---|---:|---|
| R256, 67/169 | 13 | 249 | **16** | 24 | **8** | 9,10,12,13,15,24,26,27 | 2184 | k=1093,2185 |
| R257, 770/1973 | 23 | 249 | **39** | 29 | **20** | 32,33,34,35,36,37,39,40,41,42,43,45,47,48,49,50,51,55,56,61 | 528 | none |
| R258, 866/2197 | 23 | 249 | **39** | 29 | **20** | same 20 mask indices | 12144 | none |
| R258, 866/2197 | 13 | 249 | **1** | 24 | **1** | 9 | 12 | none |

Notably in R258 mod 13, `F(x)=x+6`: every channel is a fixed scalar multiple of mask 9's sequence over the entire future. Mask 9 has no zero in its full 12-step period. This gives a one-mask first-layer 13-adic non-dip certificate. **No higher 13-adic valuation or exact rational compression is claimed.**

The minimal common recurrence degrees 16/39/39/1 and selected mask-basis sizes 8/20/20/1 measure different kinds of compression: one is temporal recurrence order, the other cross-label constant-linear reconstruction. The 249-coordinate raw labelled recurrence is therefore redundant for these declared modulo-p outputs. In the P000 residual-fidelity vocabulary the quotient is observation-relative: no information about excluded source carriers or native BRC paths is declared nonexistent.

## Reproduction and evidence

Reconstruct exact R259 coefficients from fractions `s,J,T,K` and 63 masks; use integer modular arithmetic and exact `sympy.Poly(modulus=p)` gcd/lcm to reduce each generating denominator. Verify each reduced scalar annihilator divides the original mask characteristic polynomial. Construct the F_p row basis and all **63 reconstruction coefficient vectors** by modular Gaussian elimination, then check every channel for two whole periods. The separate local code and full structured JSON certificate include all 63 coefficient vectors for every case, the per-mask degrees, and the 4 monic common polynomials; the digest/summary can be independently reproduced. The proof's all-horizon validity comes from the formal-series identities and recurrence induction, not from a bare finite search.

Executed: Python 3.13.5, SymPy 1.14.0; `Fraction`/finite-field exact computation; four original periods 2184,528,12144,12 and 2P modular reconstruction each. No independent review or native BRC EffectHistogram run. Activity bookkeeping is separate from scientific saving, and no formal TASK CLAIM/owner transfer or P000 change is asserted.

## Next unresolved units

(1) Extend the observer quotient from F_p to rings Z/p^a Z; row-rank over a field is insufficient and Smith/module invariants may govern. (2) Seek an arithmetic parameter locus supporting an actual first-layer 23-adic denominator dip, using these reduced mask observations. (3) Quantify storage/bit cost of 63 output taps, selected labels and recovery compared with a raw 249-coordinate observer; retain all source provenance outside the declared modular quotient.
