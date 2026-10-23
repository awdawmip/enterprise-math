# C270 Research2 — The final seven four-free C195/H168 hulls

**AUTHOR-LEVEL EXACT MATHEMATICAL EVIDENCE ONLY.** Not a native GF(2)-BRC or six-dimensional X6 theorem; not a Source Result, CLAIM, independent Research Driver review, Working Truth, or Foundation admission.

## Verified input authority and prior frontier

Global canonical GLOBAL_KNOWLEDGE_V1 snapshot: `main@7e4295e316213dd2deafbbcb0043567d5f59ea8c`; Source canonical Enterprise Math `main@620d43b07299193e4c9c10bf46507daa3ae45aca`. P000, ACTIVE worldview, researcher activity/role and portable research protocol were loaded. GitHub connection identifies `awdawmip`.

This result continues the *unmerged* author handoff `research/c269-r2-seven-fourfree-pairs-20261024:research_handoffs/C269_R2_AUTHOR_EXACT_SEVEN_PAIRS_20261024.md` (blob `e29ee24b4bf28dc6cb2da97d5672dab3aaf51666`) without reclassifying its seven already-positive pairs. Previous author-only frontier: 213 strict-negative witnesses, 143 full-region strict-positive certificates, seven not yet classified within 363 historically eligible unordered pairs. The remaining seven were `(4,18),(12,18),(14,18),(18,23),(18,27),(18,33),(21,22)`.

## Exact auxiliary

The 79 strictly increasing rational nodes `u[0:79]` are embedded in `C270_R2_STANDALONE_REPLAY.py`. Put `I=(5,50,55,56)`, `J={0,...,78}\\I`, `Q=2**128`, `H=2**166`, `Z=141421356237309504880/10**20`, `A=6912*50000**2/17**2`. All legal boxes have no poles and retain index ordering. For `j in J`, define the strictly positive integer

`B_j=floor((Q*A/H)/(((2-u_j**2)*(3-u_j**2))**3)*product_(r != j)((Z-u_r)/abs(u_j-u_r)))`.

Write `g_(j,p)(t)=((Z-t)/(Z-u_p))*abs(u_j-u_p)/abs(u_j-t)` and

`M_k(v)=(Q*A/H)/(((2-v_k**2)*(3-v_k**2))**3) * product_(j in J)((Z-u_j)/abs(v_k-u_j)) * product_(p in I,p != k)((Z-v_p)/abs(v_k-v_p))`.

The specified model is `F(v)=sum_(j in J) B_j*product_(p in I) g_(j,p)(v_p)+sum_(k in I) M_k(v)`. These are **positive-rational** branches, not phase-bearing native branches.

## Theorem C270-A (full closed continuous regions)

For every **real** `v=(v5,v50,v55,v56)` in the union of these four-dimensional rational boxes,

| Root | v5 | v50 | v55 | v56 | Exact positive leaves | Exact midpoint splits |
|---|---|---|---|---|---:|---:|
| R18 | [2/271,6/409] | [34/49,28/39] | [60/77,72/91] | [19/24,41/51] | 507 | 506 |
| R21 | [1/105,3/205] | [7/10,18/25] | [53/68,21/26] | [13/16,23/28] | 345 | 344 |

**F(v) >= 2**128 + 1010974601248244513663243410561557 > 2**128.**

The exact integer margins `min_leaf(floor(LB)-Q)` are **3160132858209827601324667317753066** for R18 and **1010974601248244513663243410561557** for R21. Each C254 original pair hull is checked using rational containment: R18 covers six pairs `(4,18),(12,18),(14,18),(18,23),(18,27),(18,33)`; R21 covers `(21,22)`.

## Complete proof method: four nonnegative affine factors, one multiaffine sum

1. For fixed `j,p` the positive factor `g_(j,p)` is convex on the corresponding pole-free order-preserving interval because `g''=2*(abs(u_j-u_p)/(Z-u_p))*(Z-u_j)/abs(t-u_j)**3>0`. Take its exact rational midpoint tangent `h(t)<=g(t)`. If either of its endpoint values is negative, replace it by the positive constant factor evaluated at the monotone minimizing endpoint (`lo` if `j>p`, otherwise `hi`). Therefore on every leaf `0<=h_(j,p)<=g_(j,p)`.
2. Multiply all four **nonnegative** affine minorants within each fixed positive branch, then sum 75 branches with `B_j>0`. The resulting function is **four-variable multiaffine**. Its minimum throughout a rectangular closed leaf is **exactly the minimum of its values at the 16 corners**. The 16 corners evaluate the *minorant*, not the original nonlinear target. Shared coordinate correlations across all 75 branches are preserved.
3. In each moving branch `M_k`, all other coordinates can be replaced by order-preserving endpoint factors which give a lower bound uniform in `v_k`. The resulting positive single-variable branch is log-convex, with `(log M_k)''=6(2+t²)/(2-t²)²+6(3+t²)/(3-t²)²+sum_(j in J)1/(t-u_j)²+sum_(p != k)1/(t-e_p)²>0`. At the rational midpoint form its tangent, evaluate its monotone linear minimum at the appropriate endpoint, and intersect with the trivial zero bound. This gives four exact rational lower contributions.
4. Add these fixed/moving lower contributions; `LB_leaf<=F(v)` holds for **all real points in the entire leaf**. Both full binary trees bisect an actual coordinate at its exact midpoint, with both closed halves covering the parent. The 507+345=852 leaves and 506+344=850 splits cover both four-dimensional roots. Each of the 852 exact rational lower values exceeds `2**128` with the margins above. QED.

### Verification, reproducibility and scope

This branch contains a fully **self-contained Python standard-library** verifier `research_handoffs/C270_R2_STANDALONE_REPLAY.py` with all 79 raw nodes, masses, exact formulae, both complete preorder trees, rational bisection and integer assertions. Its encoded tree counts are checked as 507/506 and 345/344. The same mathematical kernel was separately computed with Python `Fraction` for **852/852** leaves. A second **different author-coded rational dual-number automatic-differentiation implementation** independently reconstructed the 75 masses and every lower bound, matching the **full exact rational value** of all 852 leaves. Nine chunk audits passed; a combined certificate and source code are preserved in the conversation's C270 ZIP handoff. The actual remote code and tree bytes were re-read from GitHub; no unperformed remote execution is claimed.

**Deduplicated C269+C270 author-only classification:** 213 certified negative + 150 complete positive + **0 unresolved** = 363 eligible unordered box pairs. The other **232 historically ineligible combinations are not classified here**. All arithmetic and theorems concern the declared 79-node auxiliary; the passage from positive mass to native signed/phase GF(2)-BRC, branch provenance, ports, future operations, three-dimensional slice or six-axis physical semantics is unproved.

**Control boundary:** Native `em_session_start` returned `STATIC_READONLY_SCOPE_DENIED` and `operation_sent=false`. No genuine native Activity, CLAIM, Source Result, independent Driver acceptance or Foundation promotion. This standalone **author evidence** lives only on a noncanonical GitHub research branch; it is not integrated into `main`. Google Drive was not used to bypass the service permission refusal.

**Next discriminating step:** independent mathematical review of the seven new hull certificates and the 143 prior positive certificates, plus a precise type-preserving native BRC phase/port/provenance bridge or an explicit impossibility witness; separately classify the 232 out-of-method-domain combinations if appropriate.
