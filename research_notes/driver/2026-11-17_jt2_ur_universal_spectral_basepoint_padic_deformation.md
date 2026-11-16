# JT2 UR — Universal spectral basepoint and first p-adic deformation

Date: 2026-11-17. Status: **EXACT COEFFICIENTWISE MOD-p² THEOREM; CM-PORT RESIDUE REFORMULATION; FINITE VERIFICATION**.

## Scope and provenance

This is an author-side RESEARCH_DRIVER extension by `EM-DVR-DEBB5E` of the JT2 UR algebraic frontier, retaining original researchers including `EM-JT2-EF9380`, prior Source proofs and the open all-prime target. This note does not declare an independent Native review, Result acceptance, Task completion, or a proof that all residuals vanish.

Let p>3 be a prime with p=6m+1, m>=1, and let R=Z_(p). The normalized Legendre polynomial satisfies
[
Q_m(Y)=P_{2m}(sqrt Y)=c_0H_m(C_*,Y),qquad
c_0=(-1)^m {2mchoose m}4^{-m},qquad C_*=m(2m+1).
]
Define the **degree-m truncated** spectral polynomial (no infinite-series interpretation)
[
H_m(C,Y)=sum_{j=0}^m a_j(C)Y^j,quad
a_0=1,quad
a_{j+1}(C)=rac{j(2j+1)-C}{(j+1)(2j+1)}a_j(C)quad(0le j<m).
]
Define the spectral derivative (Z_m(Y)=c_0partial_C H_m(C,Y)|_{C=C_*}), already evaluated in the preceding spectral/harmonic companion.

Put the **universal rational basepoint** (C_0=-1/9) and
[
F_m(Y)=H_m(C_0,Y)=
sum_{j=0}^{m}rac{(1/6)_j(1/3)_j}{(1/2)_j,j!}Y^j
quad	ext{(truncated at precisely }m	ext{)}.
]
All coefficients are in R: (j+1), (2j+1), 2, 3, 6, 9 and 18 in the required recurrences are p-units for (j<m).

## Theorem 1 — Universal spectral p-adic deformation (polynomial identity)

For every such prime p, coefficientwise in (R[Y]/p^2R[Y]),
[
oxed{Q_m(Y)equiv c_0F_m(Y)+rac{p}{18}Z_m(Y)pmod {p^2}.}	ag{D}
]
The congruence holds at **every** Y, before CM0 or any port evaluation. Its statement depends only on the fixed degree-m polynomial realization and p=6m+1.

**Proof.** The key exact identity is
[
C_*=m(2m+1)=rac{p^2+p-2}{18}
=-rac19+rac{p(p+1)}{18}=C_0+delta.
]
The coefficients of (H_m(C,Y)) lie in (R[C]), because all recurrence denominators are units in R. Taylor expansion in the spectral parameter thus gives
[
H_m(C_* ,Y)equiv H_m(C_0,Y)+delta,partial_C H_m(C_0,Y)pmod{p^2}.
]
Since (deltaequiv p/18pmod {p^2}) and (C_*-C_0in pR), the two polynomial derivatives (partial_C H_m(C_0,Y)) and (partial_C H_m(C_*,Y)) agree modulo p. Multiply by (c_0), a p-unit, to obtain (D). Finally
(j(2j+1)+1/9=2(j+1/6)(j+1/3)) identifies the coefficients of (F_m) as displayed. QED.

An equivalent **coefficient-level** identity, useful for reproduction, is
[
c_jequiv c_0 f_j+(p/18)c_jT_jpmod {p^2},quad
f_j=rac{(1/6)_j(1/3)_j}{(1/2)_j j!},quad
T_j=sum_{i<j}rac1{(m-i)(2m+2i+1)}.
]
The (T_j) are p-integral. This identity provides a second direct proof via finite product expansions:
[
(i-m)(i+m+	frac12)
=(i+	frac16)(i+	frac13)-rac{p(p+1)}{36}.
]
Modulo p, (T_j=-rac12sum_{i<j}[(i+1/6)(i+1/3)]^{-1}). Multiplying the product perturbations yields exactly (pT_j/18) modulo p².

## Corollary 2 — Divided CM half-value without spectral differentiation

Specialize further to p mod 24 in {13,19} and the inherited verified CM0 assertion (Q_m(1/2)equiv0pmod p). Theorem 1 implies (F_m(1/2)equiv0pmod p). The two p-divisions are now legal. Set
[
u_m=Q_m(1/2)/ppmod p,quad
v_m=F_m(1/2)/ppmod p,quad
d_m=Q'_m(1/2)pmod p.
]
Then
[
oxed{u_mequiv c_0v_m+rac1{18}Z_m(1/2)pmod p.}	ag{H}
]
In particular (v_m) is a well-defined, new finite hypergeometric quotient at the universal basepoint.

## Corollary 3 — Remove both spectral derivative and quadratic norm convolution from the UR residue

Retain the preceding proven finite Lagrange identity
[
2J_m(1/2)equiv d_m Z_m(1/2)+2c_mS_ppmod p,
]
where
[
J_m(Y)=sum_{r=0}^{2m}rac{[Y^r]Q_m(Y)^2}{2r+1}Y^r,quad
S_p=sum_{j=0}^{m}rac{c_j2^{-(m+j)}}{2m+2j+1}.
]
The original obstruction, in the established half-coordinate notation, is
[
arepsilon_pequiv18u_md_m-2J_m(1/2)-3pmod p.
]
Substituting (H) and the Lagrange identity produces the **exact equivalent residue**:
[
oxed{arepsilon_pequiv
18c_0d_mv_m-2c_m S_p-3pmod p.}	ag{U}
]
The spectral-derivative term cancels identically. (U) requires only a p²-level evaluation of one degree-m basepoint hypergeometric partial sum and p-level, O(m)-term coefficient/weighted sums; it eliminates the degree-2m quadratic convolution and spectral parameter differentiation. To prove the full UR target one must still prove the vanishing of (U) uniformly over the specified primes. The equality (U) itself is proved without that assumption.

A second use is methodological: any proposed p-adic evaluation of (F_m(1/2)) can be checked against the inherited UR scalar without re-proving the Legendre spectral identities. This is a **new representation of the same mathematical obstruction**, not a new axiom.

## Verification

Exact finite arithmetic was independently performed for all 148 primes p<=2000 with p mod6=1: every coefficient of (D) agreed modulo p². For the 77 primes among them with p mod24 in {13,19}, (H) was checked using actual p² division. For the 15 such primes p<=300, independent quadratic-convolution calculation of J also confirmed (U) against the original residual; all those checked residuals were zero. All operations used modular exact arithmetic and p-unit inverses, no floats.

Suggested verifier path: `experiments/jt2_ur_spectral_basepoint_padic_deformation_20261117.py`. These finite tests corroborate but are not the general proof.

### Sources and contribution boundaries

- Original frozen task and return: `research_returns/EMW59A_JT2_UR_SUN_PARITY_DEFECT_RETURN_EF9380_20260910.md`, result `RR-60983E048B55C2AC7F66` (original author `EM-JT2-EF9380`).
- Previous Driver extension: `research_notes/driver/2026-11-17_jt2_ur_spectral_logarithmic_harmonic_companion.md` (author `EM-DVR-DEBB5E`).
- New derivation, proof and computational crosscheck: `EM-DVR-DEBB5E`, this note. Shared mathematical/control context disclosed; **not** an independent Native review.
- Research objective: uniform (arepsilon_p=0) remains open; no formal Task/parent closure inferred.
