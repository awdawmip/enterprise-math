# Native filament coupled-selection V2 — direct nonblind literature audit

Status: `FROZEN_DIRECT_NONBLIND_LITERATURE_AUDIT / NOT_INDEPENDENCE_ATTESTED`

Date: `2026-08-25`

Auditor: `EM-FREE-NEPS-239A6D`

Target packet:
`research_inputs/NATIVE_FILAMENT_COUPLED_SELECTION_V2_LITERATURE_AUDIT_PACKET_20260825.md`

## 0. Independence disclosure

This is **not** the independent blind return required by the original #632 taskbook. The auditor had already participated in the source/generalization work on PR #627 before the user explicitly requested a direct literature audit.

Accordingly:

- no independence attestation is made;
- this file does not occupy the reserved independent-return path;
- the required blind return may still be produced by an auditor who has not read #627;
- the evidence standard below is nevertheless theorem-level: exact statement mapping, not keyword resemblance.

Freeze label:

`DIRECT_NONBLIND_THEOREM_LEVEL_LITERATURE_AUDIT`.

## 1. Executive verdict matrix

| Row | Direct-audit verdict | Reason |
|---|---|---|
| S1 sector-count provenance | `KNOWN_COMPONENTS_ONLY` | Centered polygonal shell counts and centered-polygonal primes are classical; no direct theorem match found for the half-open cyclic blocks + unique odd central block + zigzag simplification + even-sector seam obstruction as one statement. |
| S2 odd-curvature / finite quotient | `KNOWN_COMPONENTS_ONLY` | Periodic/quasi-polynomial modular code behavior and RS/MDS classification are known; no direct theorem found giving this exact parity-locked minimal period `lcm(2,M/gcd(B,M))` and cardinality `M L_(B,M)` for the family. |
| S3 dual-parabola tangent arrangement | `KNOWN_COMPONENTS_ONLY` | Conic duality, tangent-line conics and arithmetic line arrangements are classical; no direct source found for the parity-sampled pair `Q_e^(chi)` with obstruction `B(w-u)(w-v)+chi(1-2e)` and its exact sampled discriminant/depth package. |
| S4 transparency / breaker phase | `KNOWN_IMMEDIATE_COROLLARY` | The local factor is a direct order-2 cyclotomic/quadratic-residue translate count; the `{2,3,5}` breaker classification and mod-60 table follow by routine substitution plus direct small-prime checks. |
| S5 breaker-coprime capacities | `KNOWN_IMMEDIATE_COROLLARY` | Once S4 supplies a breaker, the `2q` parity/residue period and a single double-root zero in the extremal class immediately give `2q-1`; for q=2,3,5 this is 1,5,9. Literature on runs of quadratic residues/nonresidues is much broader, but no separate novelty should be assigned to this elementary cap. |
| S6 Legendre-dual unification | `KNOWN_COMPONENTS_ONLY` | Legendre/conic duality and the value-set intersection formula are classical; no direct theorem located that identifies the same sampled quadratic pair as simultaneously controlling tangent-concurrence exceptions and global covering/breaking in this indexed family. |
| S7 native tri-sector selection | `KNOWN_COMPONENTS_ONLY` | Centered polygonal geometry, local discrete Laplacians, Legendre symbols and prime-connectivity models all have precedents, but no equivalent theorem was found in which the locally forced scalar 3 from this tri-sector allocation determines the first arithmetic breaker and is coupled to the separate native incidence cap. |
| S8 high-dimensional transparent basin | `KNOWN_COMPONENTS_ONLY` | CRT-factorized/squarefree compact sets, profinite Haar models for polynomial divisibility, Euler products and standard dimension arguments are established; the exact local factors and extinction/no-break specialization are family-specific but obtained by inserting S4 into those frameworks. |

Package-level verdict:

`KNOWN_COMPONENTS_ONLY`.

Meaning:

> No direct theorem-statement match for the full coupled chain was found in the audited literature set, but nearly all ambient mathematical technologies and two substantial rows (S4/S5) are classical immediate consequences. This verdict is **not** proof of novelty.

## 2. S1 — sector-count provenance

### Closest known components

Centered polygonal numbers have the classical form

`C_(s,n)=1+s*n*(n-1)/2`

(up to the usual indexing shift). This is exactly the shell-start count appearing in S1. Centered polygonal prime sequences, including searches for record consecutive prime centered k-gonal values, are also tabulated in OEIS.

Closest sources checked:

1. standard centered polygonal number references, formula `1+s n(n-1)/2`;
2. OEIS A298760, “Numbers k such that there is a record number of consecutive prime centered k-gonal numbers after 1”;
3. OEIS centered k-gonal prime sequences such as A276263/A276264;
4. literature on polygonal Sierpiński/Riesel numbers using covering congruences.

### Mapping

Known literature directly covers the centered-shell start and the fact that centered polygonal quadratic sequences can be studied for prime runs and covering congruences.

What I did **not** find is a source whose theorem starts from:

- `s` cyclic half-open blocks of length r,
- selects the unique block `(s-1)/2` only when s is odd,
- uses `t=h+ceil(r/2)`,
- derives `h+1+(s r^2+eps(r))/2`,
- and pairs this with the even-s central-seam odd-gap obstruction.

Verdict: `KNOWN_COMPONENTS_ONLY`.

## 3. S2 — odd-curvature dynamics / finite quotient

### Closest known components

1. Koji Imamura, Norihiro Nakashima, Takuya Saito, **Periodicity of weight enumerators for codes generated by an integral matrix**, arXiv:2601.21121 (2026). The paper studies modular codes from integral matrices, weight-enumerator quasi-polynomiality and links with Tutte quasi-polynomials/hyperplane arrangements.
2. Reed–Solomon / MDS evaluation-code theory: the flattened fixed-chirality family `(a+bj)` is standard `[k,2,k-1]` RS/MDS.
3. characteristic quasi-polynomial / arithmetic arrangement literature gives broad periodicity over moduli.

### Mapping

These sources cover the general modular-periodic/code language and the post-flattening classification. They do not, in the material located, directly give the family-specific arithmetic lock

`chi=(-1)^R`, `slope=B R`,

nor the exact minimal effective period

`lcm(2,M/gcd(B,M))`

with the special `M=2` collapse and the exact word count `M L_(B,M)` independent of k>=3.

That formula is elementary once the family is specified, so it should be presented as an exact special-family theorem, not as a new general theory of modular codes.

Verdict: `KNOWN_COMPONENTS_ONLY`.

## 4. S3 — chirality-dependent dual-parabola tangent arrangement

### Closest known components

Classical projective geometry states that the tangent lines to a nondegenerate conic form a conic in the dual plane. A modern survey source is:

- **Harmonic ovals**, Journal of Geometry (2024), which recalls the Veblen–Young theorem: tangent lines to a conic in a Pappian projective plane (outside the Fano exception) form a conic in the dual plane, and analogous finite-plane facts.

Finite-geometry literature on dual conics treats tangent lines and internal/external points. Arithmetic-arrangement literature treats determinant-controlled reductions of line arrangements.

### Mapping

The standard theory explains why the zero-line family is naturally dual-conic data. What was not located as a direct theorem is the specific parity-sampled union of two vertically shifted parabolas

`Q_e^(chi)(x)=x^2/(2B)-chi e/2`

sampled at `x=-Bj`, together with the exact mixed-parity triple obstruction

`B(w-u)(w-v)+chi(1-2e)`

and its finite-window two-chirality product discriminant / q-adic persistence interpretation.

Verdict: `KNOWN_COMPONENTS_ONLY`.

## 5. S4 — transparency / universal-breaker phase

### Strong prior art

Order-2 cyclotomic numbers are classical. With quadratic-residue classes `D_0,D_1`, one standard formulation gives, for an odd prime p:

- if `p=1 mod4`, `(0,0)=(p-5)/4` and the other order-2 cyclotomic numbers are `(p-1)/4`;
- if `p=3 mod4`, the corresponding values are `(p-3)/4` and `(p+1)/4` in the standard positions.

Modern expositions explicitly cite these as classical (e.g. Cusick–Ding–Renvall-style sequence literature; surveys of Jacobi sums/cyclotomic numbers).

### Mapping

After scaling, the two hit sets in S4 are translates of the quadratic-residue set with zero included. Therefore

`tau_B(q)=[q-3+(B/q)+(-B/q)]/4`

is a routine order-2 cyclotomic-number calculation for `q∤B`; `q|B` is the degenerate singleton case. The statements

- q>=7 cannot break,
- q=3 breaks iff `3∤B`,
- q=5 breaks iff `(B/5)=-1`,
- the mod-60 first-breaker table,

then follow by elementary substitution plus the separate q=2 calculation.

Verdict: `KNOWN_IMMEDIATE_COROLLARY`.

Required wording consequence: do **not** present the transparency formula or the `{2,3,5}` classification as a new character-sum/cyclotomy theorem. Its research relevance is the way the sector-selected B feeds into this classical local calculation.

## 6. S5 — breaker-coprime capacities

### Closest literature

There is a large classical literature on runs/patterns of quadratic residues and nonresidues, e.g.

- Richard H. Hudson, **On sequences of consecutive quadratic nonresidues**, Journal of Number Theory 3 (1971), 178–181, DOI `10.1016/0022-314X(71)90034-5`.

This literature studies generic longest runs; it is not the exact same indexed alternating quadratic family.

### Mapping

For the S5 statement, no deep run theorem is needed. In a breaker phase modulo odd q, the shell state has period `2q`. In the extremal tangency class the relevant quadratic has exactly one double root in that `2q` period and the opposite parity branch has no root. Hence there is exactly one zero per period and the longest nonzero run is immediately `2q-1`.

For q=2,3,5 this gives 1,5,9. Thus S5 should not carry a novelty claim independently of the family setup.

Verdict: `KNOWN_IMMEDIATE_COROLLARY`.

## 7. S6 — Legendre-dual unification

### Closest known components

1. Legendre/projective duality for conics and parabolas is classical.
2. The order-2 cyclotomic intersection numbers giving `|I_0∩I_1|` are classical.
3. Finite conic literature studies tangent line families as dual conics.

### Mapping

The algebraic facts

`I_e=-Q_e^*(F_q)`

and

`tau=|I_0∩I_1|-1`

are straightforward once the quadratic pair is written. I found no theorem-level source in the audited set that takes one parity-sampled pair of quadratics and states simultaneously:

- sampled tangents determine exceptional characteristics through triple concurrence;
- the negative dual value images determine global covering/breaking;
- both are controlled by the same B chosen by an external shell geometry.

This is the strongest not-directly-matched **coupling** inside the package, but it is composed of classical pieces.

Verdict: `KNOWN_COMPONENTS_ONLY`.

## 8. S7 — native tri-sector selection corollary

### Closest literature

1. centered polygonal/number-spiral prime patterns are classical and computationally studied;
2. Vardi, **Prime Percolation**, Experimental Mathematics 7 (1998), 275–289, DOI `10.1080/10586458.1998.10504373`, studies connectivity questions for Gaussian primes via percolation models;
3. Friedlander–Fuchs–Harris–Hsu–Rickards–Sanden–Schindler–Stange, **Prime and thickened prime components in Apollonian circle packings**, arXiv:2410.00177, introduces tangency-connected prime components in a geometric packing and studies residue classes/component sizes;
4. subsequent shifted-quadratic-form work studies local congruence restrictions motivated by those prime components.

### Mapping

These sources show that geometry-selected prime connectivity, curvature-labelled structures and local congruence obstructions are not new themes. However, none of the located sources directly matches the statement

`sector count = mean filament curvature = normalized local Poisson source = 3`

followed by

`B=3 -> first universal breaker 5 -> breaker-coprime capacity 9`,

with the actual native prime-incidence cap 9 kept as a separate incidence theorem.

Verdict: `KNOWN_COMPONENTS_ONLY`.

Recommended claim strength: model-specific exact selection corollary, not a general theorem about primes or curvature.

## 9. S8 — high-dimensional transparent basin

### Strong prior art / frameworks

1. Olivier Ramaré, **On long kappa-tuples with few prime factors**, Proc. London Math. Soc. 104 (2012), 158–196, DOI `10.1112/plms/pdr026`, explicitly defines a **multiplicatively split compact set** `(K_d)` by CRT factorization `K_(d1 d2) ≅ K_d1 × K_d2` for coprime moduli and a square-free lifting condition.
2. Zakhar Kabluchko, Alexander Marynych, **Divisibility properties of polynomial expressions of random integers**, Journal of Number Theory 259 (2024), 357–377, DOI `10.1016/j.jnt.2024.01.017` (arXiv:2311.05369), uses profinite integers/Haar measure to study divisibility of polynomial values.
3. General sieve and local-solubility literature routinely represents global densities as Euler products of local factors.

### Mapping

Thus the architecture

`local allowed sets -> CRT product -> profinite compact set -> Haar product measure`

is established. The exact factors `tau_B(q)`, the finite-d extinction/no-break split and the specific `4^{-d}(log p_d)^{-3}` specialization come from this family, but once those local factors are known, the CRT product, Euler-product asymptotic, Haar-null conclusion and full-dimension mass-distribution calculation use standard machinery.

Verdict: `KNOWN_COMPONENTS_ONLY`.

Required wording consequence: present S8 as an exact specialization of established CRT/profinite/sieve architecture, not as a new theory of profinite survivor fractals.

## 10. Search domains and closest false positives

The direct audit searched theorem statements / abstracts / bibliographies across:

- integral affine/hyperplane arrangements modulo q;
- characteristic quasi-polynomials, arithmetic/G-Tutte arrangements;
- modular codes from integral matrices;
- RS/MDS codes with affine/periodic offsets;
- centered polygonal numbers and centered-polygonal prime runs;
- finite conics, dual conics and tangent-line arrangements;
- order-2 cyclotomic numbers and quadratic-residue translate intersections;
- consecutive quadratic residues/nonresidues;
- covering systems and prime covers;
- polynomial divisibility / intersective-polynomial literature;
- arithmetic dynamics / prime divisors of quadratic polynomial orbits;
- deterministic/prime percolation;
- prime components in Apollonian circle packings;
- CRT-split compact sets, sieve local conditions and profinite polynomial divisibility.

Representative search phrases included:

- `centered polygonal number consecutive prime centered k-gonal`
- `alternating quadratic sequence Legendre breaker`
- `periodicity weight enumerators integral matrix code`
- `two parabolas tangent arrangement finite field`
- `dual conic tangent lines finite projective plane`
- `cyclotomic numbers order 2 quadratic residues intersection`
- `consecutive quadratic nonresidues`
- `prime covers periodic patterns`
- `polynomial divisibility local conditions profinite integers`
- `multiplicatively split compact set CRT`
- `prime percolation`
- `prime components Apollonian circle packings`
- `curvature prime connectivity local congruence`

Closest false positives / non-subsuming neighbors:

- centered polygonal prime records: same quadratic shell count, no central-block/breaker coupling;
- Sierpinski/Riesel polygonal-number covering work: uses covering congruences, but not this transverse all-shell transparency problem;
- covering-system literature: covers integers by residue classes, not the same quadratic-image cover of `F_q` indexed by shell parity;
- quadratic-nonresidue run literature: generic run bounds/patterns, not the exact tangency-selected `2q-1` family mechanism;
- Vardi prime percolation: Gaussian-prime random/percolation connectivity, not a deterministic finite-wheel phase selected by B;
- Apollonian prime components: very close thematically (geometry + tangency + prime components + local residues), but the geometry and arithmetic forms are different and no theorem maps to S1–S8 directly;
- integral-arrangement and G-Tutte theory: strongly subsumes generic point-counting machinery, but not the preceding sector geometry or subsequent breaker interpretation;
- integral-matrix code periodicity: subsumes broad modular periodicity, not the exact parity/slope locked period/cardinality statement located here.

## 11. Package-level novelty verdict

`KNOWN_COMPONENTS_ONLY`.

The full audited chain is

`sector allocation`
`-> curvature coefficient B`
`-> locked finite quotient / affine code`
`-> parity-sampled dual-parabola tangent arrangement`
`-> sampled-tangent exception discriminant`
`-> dual-value-set breaker classification`
`-> extinction/no-break CRT-profinite phase`.

No source in the audited literature set was found whose theorem directly subsumes essentially this full chain.

However:

- S4 is a classical cyclotomic-number corollary;
- S5 is an elementary periodic/tangency corollary;
- S8 uses established multiplicatively-split/profinite/sieve machinery;
- S2/S3/S6 each rest heavily on classical code/conic/arrangement theory;
- S1/S7 are model-selection statements rather than new ambient number theory.

Therefore the publication-safe statement is **not** “a new general theory” and is **not** “proven novel.”

Allowed wording:

> In the audited literature set, no direct theorem-statement match was found for the complete geometry-selected coupled family. Its component mathematics is largely classical; the potentially distinctive contribution is the exact solvable coupling and the extremal role of the tri-sector specialization.

## 12. Recommended PR #627 relabeling

1. S4 / transparency formula: label `CLASSICAL_ORDER_2_CYCLOTOMY_COROLLARY`.
2. S5 / 1,5,9: label `ELEMENTARY_BREAKER_PERIOD_COROLLARY`; preserve the breaker-coprime scope.
3. S8: label `EXACT_FAMILY_SPECIALIZATION_OF_CRT_PROFINITE_SIEVE_FRAMEWORK`.
4. S2 RS/MDS language: supporting classification only; retain the family-specific period/cardinality formula.
5. S3/S6: retain as the strongest coupled geometric bridge, but write `NO_DIRECT_MATCH_FOUND_IN_AUDITED_SET`, never `NEW`.
6. S7: retain as `NATIVE_MODEL_SELECTION_COROLLARY`, not as a coordinate-independent theorem about primes.
7. Package: label `EXACT_STRUCTURED_SYNTHESIS / EXTERNAL_NOVELTY_UNRESOLVED`.

Suggested paper-level framing if broader expert/MathSciNet/zbMATH review later remains negative:

> An exactly solvable sector-selected quadratic filament model with arithmetic connectivity phase transitions.

This framing foregrounds the coupled model rather than rebranding the classical tools.

## 13. Direct-audit hard-target line

`NATIVE_FILAMENT_COUPLED_SELECTION_DIRECT_NONBLIND_EXTERNAL_NOVELTY_AUDIT = KNOWN_COMPONENTS_ONLY`.

`NO_DIRECT_THEOREM_STATEMENT_MATCH_FOR_THE_FULL_COUPLED_CHAIN_FOUND_IN_THIS_DIRECT_AUDITED_LITERATURE_SET != PROVEN_NOVELTY`.
