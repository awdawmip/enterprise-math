# JT2 UR norm-jet: finite exact p-adic audit on 45 admissible primes

Date: 2026-11-16 (Asia/Taipei). Author-side bounded computational research by the genuine existing JT2 RESEARCH_DRIVER `EM-DVR-DEBB5E`. Existing Sun/ordinary-Legendre elimination and exact norm-jet reduction belong to the original authors and earlier independently reviewed stage (not to this finite audit).

## Input, quantifiers and legitimate inference

Use the exact previously frozen task `RS-EMW59A-JT2-UR-SUN-PARITY-DEFECT` and source `research_returns/EMW59A_JT2_UR_SUN_PARITY_DEFECT_RETURN_EF9380_20260910.md` (immutable GitHub commit `969846f1d451b3e086f34a19b217e333c8a90c8d`, source blob `b400bf432162cc5d67f51a1d2963de533c786afb`). The prior official Driver review `driver_reviews/JT2_UR_NORM_JET_STAGE_REVIEW_57CCCE_20260920.md`, source blob `702f7ddf2816f7515d197f440c30d34f7c3cd244`, accepted the *reduction*, not the uniform value.

For every **tested** prime `p <= 997` with `p > 3` and `p mod 24 in {13,19}`, set `n=(p-1)/3`; let `P_n` be the actual ordinary Legendre polynomial (`P_0=1`, `P_1=x`, `(m+1)P_(m+1)=(2m+1)x P_m-m P_(m-1)`), and the exact polynomial primitive `I_n(x)=int_0^x P_n(v)^2 dv`. In the p-integral CM ring `A=Z_(p)[t]/(2t^2-1)`, the evenness of `n` and parity of the polynomial terms reduce the original scalar exactly to base-field residues:

```text
u_p = (P_n(t)/p) mod p, with P_n(t) evaluated mod p^2
d_p = (P_n'(t)/t) mod p
N_p = (I_n(t)/t) mod p
epsilon_p = 9*u_p*d_p - 2*N_p - 3 mod p.
```

The only reductions in these computations are coefficientwise rational modular arithmetic with denominators prime to `p`; `2n+1 < p`, so every primitive denominator `j+1` is a unit. `P_n(t)` was checked divisible by `p` before dividing. The computation retained `p^2` data for `P_n(t)/p` and used `p` data where justified for `d_p,N_p`. The normalization `t^2=1/2` makes each displayed scalar a well-defined element of `F_p`.

## Actual reproducible result

The archived executable is:

`experiments/jt2_ur_legendre_norm_jet_exact_45_primes_20261116.py`, commit `4859bfc271ec1549234956ea5aca7ab3838cbd1f`, Git blob `4ba9b4c9d7332e96776fe7dec328a9786fe88171`.

It enumerates primality by exact integer trial division; all Legendre recurrences, polynomial products and integration use integer modular arithmetic, never floating-point. The executable was run locally (also `python -m py_compile` passed) before publication and source-byte readback:

```text
admissible primes p<=997       : 45
CM0 violations                 : 0
nonzero norm-jet epsilon_p     : 0
first check (p,n,u,d,N,eps)    : (13,4,2,11,0,0)
last  check (p,n,u,d,N,eps)    : (997,332,473,920,609,0)
```

The tested prime list is

```text
13,19,37,43,61,67,109,139,157,163,181,211,229,277,283,
307,331,349,373,379,397,421,499,523,541,547,571,613,
619,643,661,691,709,733,739,757,787,811,829,853,859,
877,883,907,997
```

An independent symbolic-rational direct calculation of standard Legendre polynomials (using SymPy rather than the modular recurrence) matched `u,d,N,epsilon` at `p=13,19,37,43`. This is a second computation path for those cases, not a checker of a general theorem.

## Scientific evaluation / next discriminating move

This evidence supports the existing uniform conjectural target on the bounded domain of **45 primes**. It does **not** solve the hard target `epsilon_p=0` for all admissible primes, produce a new Native Result admission, or establish formal Task / JT2 mother-objective completion. Any substantive successor should derive an identity controlling `P_n(t)/p` and `I_n(t)/t` across *all* `p=13,19 (mod 24)` within the frozen exact Legendre coefficient and CM hypotheses. A new scan alone is not a substitute for this arithmetic argument.

Contribution provenance: original exact norm-jet reduction and prior accepted stage belong to `EM-JT2-EF9380` and the originally named reviewers; `EM-DVR-DEBB5E` conducted the bounded finite exact audit and authored this note. Existing QTF3 p^3 stage admission is unaffected. A new independent native review must distinguish finite support from uniform proof.
