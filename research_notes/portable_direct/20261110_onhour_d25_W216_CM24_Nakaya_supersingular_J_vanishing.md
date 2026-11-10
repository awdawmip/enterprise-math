# D25 W216: all-prime CM(-24) vanishing of the original Clausen root J_p

Date: 2026-11-10 (+08). Classification: **AUTHOR_SIDE / EXACT_SOURCE_DEPENDENT_PROOF / FINITE_VERIFIED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0_B0**. No claim of originality of Nakaya's or Deuring's theorems.

## Frozen parent and result

Parent: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication: `TP2-B6F4FC938FF94941C1B7`; frozen scientific Source **`c47e13e4aba0e006366f989d6334d443f6333ae3`** (unchanged).

Let `p=6m+1>3` be prime, and, in `Z_(p)`,
[
B_k=rac{(1/6)_k(1/3)_k}{2^k(k!)^2},qquad J_p=sum_{k=0}^{p-1}B_k.
]
Then the source-backed full-class classification is
[
oxed{J_pequiv0pmod pquadLongleftrightarrowquad pequiv13,19pmod{24}}
	ag{A}
]
for **every** prime `p=1 (mod 6)`.

This discharges the preceding author-side continuation's specific missing **CM/J_p mod p vanishing** for the two target classes, using identified published external theorems. It neither proves the signed second-digit LIFT nor runs the original fixed H0/B0 divided-power benchmark.

## Proof with exact representation and field

1. For `k>m`, the factor `(1/6)_k` contains `p/6` and `k! (k<p)` is a p-unit, so `B_k=0 (mod p)`. For `0<=k<=m`, use `1/6=-m`, `1/3=-2m` in `F_p`, yielding
[
J_pequiv sum_{k=0}^{m}inom{m}{k}inom{2m}{k}2^{-k}
={}_2F_1(-m,1/3;1;1/2)pmod p.
	ag{B}
]
The second identity uses the *truncated polynomial*; all factorial denominators have indices below p.

2. In Tomoaki Nakaya (2018), *The number of linear factors of supersingular polynomials and sporadic simple groups*, arXiv:1809.02363v1, Definition 1, for `p=6m+1`, `delta=0`,
[
ss^{(3*)}_p(X)=X^m,{}_2F_1(-m,1/3;1;108/X)pmod p.
]
Consequently
[
ss^{(3*)}_p(216)=216^m J_ppmod p,
	ag{C}
]
and `216` is a p-unit. Nakaya §4, equations (6),(23) and the definition of `S_3^*` identify this polynomial's roots with level-3 Fricke points whose corresponding ordinary elliptic `j`-invariant is supersingular. (This step depends on **published supersingular polynomial identification**, not on a conjectural association.)

3. The level-3 Fricke relation for `X=j_3^*=216` is
[
j_3^2-216(j_3-27)=0,qquad j_3=108pm54sqrt2.
]
The modular relation is
[
j_3(j_3+216)^3=j(j_3-27)^3.
]
Since `Norm(j_3-27)=81^2-2(54)^2=729`, the denominator is a unit for each prime `p>3`. Exact simplification in `Q(sqrt(2))` gives the two possible classical invariants
[
j_pm=2417472pm1707264sqrt2,
	ag{D}
]
and
[
(j-j_+)(j-j_-)
=j^2-4834944j+14670139392=H_{-24}(j).
	ag{E}
]
The polynomial is the **known Hilbert class polynomial of discriminant -24** (class number 2), not newly inferred just from its shape. Independent reference: NumberDB `https://numberdb.org/Hilbert_class_polynomials` and OEIS A305474 `https://oeis.org/A305474`.

4. Both `j_pm` are CM invariants by the maximal order of `K=Q(sqrt(-6))`, whose discriminant is -24. For `p>3`, the CM curve has good reduction at primes over p; by **Deuring's CM reduction criterion**, its reduced j is supersingular precisely when `(-24/p)=(-6/p)=-1`, i.e., inert p. Source: Deuring theorem, e.g. `https://link.springer.com/article/10.1007/s10231-024-01528-x`, §4.1.1. Supersingularity is geometric and therefore identical for both conjugate j values.

5. For `p=6m+1`, `(-3/p)=+1`; hence `(-6/p)=(2/p)`. Quadratic reciprocity for 2 yields `(2/p)=-1` exactly when `p=3 or 5 (mod 8)`. Intersecting with `p=1 (mod6)` gives precisely `p=13 or 19 (mod24)`. Together with (B)–(E), this proves (A). QED.

**Source/representation firewall.** The field `F_p[sqrt2]` and Fricke modular j here are an *external CM validation/representation* for the scalar `J_p` mod p. They do not identify the original H0/B0 `[X]U`, its lattice rank, semilinear Frobenius, normalization `eta`, odd Green/Hesse port, or native signed `kappa`. No native operator transfer is asserted.

## Concrete consequence at the actual LIFT interface

The previous original signed/unsigned Clausen first-jet theorem (author-side, source verified, **not** Source-admitted) supplies `Q_0,Q_w in p² Z_(p)`, `F_{0,p}=J_p²-Q_0`, and
[
W_p=J_p^2+12J_pK_p-Q_w,quad
K_p=sum_{k=0}^{p-1} kB_k,quad
Q_w=sum_{0le i,j<p, i+jge p}(6(i+j)+1)B_iB_j.
]
Under the accepted parent first-digit theorem `W_p=p (mod p²)`, (A) now **unconditionally provides** `j_p=J_p/pin Z_(p)` at every target prime, and reduction mod p² yields
[
12j_pK_p=1pmod p.
	ag{F}
]
Thus `j_p` and `K_p` are units mod p, i.e. `v_p(J_p)=1`, and `F_{0,p}=0 (mod p²)` follows from `J_p²` and `Q_0`. This is an exact dependency elimination using the already accepted first digit, not an independent native result.

The **remaining original second-digit obligation** is the exact signed equality
[
	au_p+j_p^2-R_pequiv0pmod p,qquad
	au_p=(12j_pK_p-1)/p,quad R_p=Q_w/p²pmod p,
]
equivalently `(W_p-p)/p²=0 (mod p)`; preserve the signed ordered cutoff and its p-adic grade provenance. Proof of `J_p=0 (mod p)` itself **does not close LIFT**.

## Actual integer checks (author-only, deterministic)

Independent script `research_notes/portable_direct/d25_w216_cm24_nakaya_20261110.py` uses **exact modular recurrences** (no floating point). For all **611 primes `p=1 (mod6)`, `p<=10000`**, `J_p` vanishes exactly in **312** target-class cases and is nonzero in **299** other cases. Original recurrence and direct binomial truncated expression crosschecked for all `p=1 (mod6),p<=1000`.

A separate elliptic-curve **Hasse invariant** computation of the external CM j, over `F_p[T]/(T²-2)`, independently gives
[
[x^{p-1}](x^3+ax+b)^{(p-1)/2}=0,quad
a=-3j/(j-1728),;b=-2j/(j-1728),
]
for all **45** target primes `p<=1000`. Here `j=2417472-1707264T`; denominators are units on the target classes; standard Hasse criterion applies. In particular `p=373`: `J_{373}=0 (mod373)`, Hasse pair `(0,0)`.

**Scope of testing**: finite checks of the exact arithmetic/program and modular CM consistency; the all-prime result is supported by the five-step source-dependent proof above.

## Current control, incomplete native evidence and handoff

- Logic Research lane: `chatgpt-research-onhour-enterprise-math-20260923` (separate from maintenance). Historical native session `MCP-5378d3819d8947bda9049c9428493e2d`, Researcher `EM-ENTERPRISE-43C218`, RA `RA-C3371503F6CA7F93D8D60568`; private issued capability unavailable. `recovery_status` returned `SESSION_CAPABILITY_REQUIRED`.
- Original continuation request `onhour11-20261110-1658-exact-cont-after-unit` read `SUCCEEDED`; its historic Source as-of read is **not a current claim**. No new native CLAIM, run, checkpoint, freeze or review.
- Benchmark support: Issue #1559 open, unassigned at 2026-11-10 18:56 +08; original `[X]U mod139129`, native rank, semilinear direction and eta, signed kappa/Delta-R and independent replica remain **NOT_RUN / PENDING_OWNER**.
- Next exact math: seek a finite field/WZ or Jacobi identity for `tau_p+j_p²-R_p=0 (modp)`, now without the extra CM vanishing premise. Next exact native step: an authorized original-class H0/B0 owner runs the frozen p373 benchmark and documents operator normalization and independent confirmation. Neither step may replace the other.
- Prior author-side proofs and their contributions preserved; this is **a standalone new source-dependent bridge**. All review/admission stays pending.

External references:
1. T. Nakaya, 2018, `https://arxiv.org/html/1809.02363v1`, Definition 1, formulas (6), (23), §§2,4.
2. Hilbert `H_{-24}`, `https://numberdb.org/Hilbert_class_polynomials`; OEIS `https://oeis.org/A305474`.
3. Deuring CM reduction criterion `https://link.springer.com/article/10.1007/s10231-024-01528-x`, §4.1.1.
4. Prior original signed/unsigned Clausen author-side note `research_notes/portable_direct/20261110_onhour_d25_W216_unsigned_Clausen_square_firstjet_bridge.md`.

**Classification** `AUTHOR_SIDE_EXACT_PROOF_DEPENDS_ON_REFERENCED_PUBLISHED_THEOREMS / FINITE_CHECKED / NOT_INDEPENDENT_REVIEWED / NOT_NATIVE_EXECUTED / NOT_ADMITTED`.
