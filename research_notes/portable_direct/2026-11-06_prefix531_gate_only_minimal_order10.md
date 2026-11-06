# PREFIX-531 — A minimal 10th-order gate-only BRC-path observer

**Date:** 2026-11-06 Asia/Shanghai. **Task:** `RS-X6-NATIVE-ROTATION-DYNAMICS`. **Frozen science:** `enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`. **Evidence:** AUTHOR_PROVED / EXACT_BIGINT_AND_SYMBOLIC_CHECKED / UNREVIEWED / NOT_ADMITTED.

## Question and scope

Starting from PREFIX-530's generically minimal 49-dimensional **all-origin/all-terminal and all-six-axis weighted** linear realization, determine the least eventual linear recurrence needed when the observer retains **only** the total count of occurrences of the reachable KMP word `aAc`. We sum over the 48 starting phases, 48 final phases and six macro labels (three next-phase options, two INNER/OUTER words) at each step. Distinct histories are counted with multiplicity. The underlying P000 six-axis path and signed BRC semantics remain unchanged; the specialization merely changes the declared observer.

Let `a_d(z)=Σ_{|w|=d}z^{H(w)}` and `P(t,z)=Σ_{d≥0}a_d(z)t^d`. Work over `Q(z)`. The frozen STARs are A={L1,L3,L6}, B={L1,L4,L5}, C={L2,L3,L5}, D={L2,L4,L6}, with phase/transition/branch rules as in PREFIX-530; target phase T=(A,+L1,−L3), and a gate fires precisely when two successive branches are INNER and the ending phase is T.

## Theorem — minimal scalar recurrence

For the all-start, all-terminal, gate-only observer, the reduced rational function `P(t,z)=N(t,z)/D(t,z)` has denominator

```text
D(t,z) = 1 - 20t² - (396+20z)t⁴ - (4944+48z)t⁶ - (32832+1728z)t⁸ + (186624+62208z)t¹⁰
```

and numerator

```text
N(t,z) = 3[16 + 96t + (253+3z)t² + (1500+36z)t³
           + (2616−56z)t⁴ + (15408−48z)t⁵ + (12864−576z)t⁶
           + (74304−576z)t⁷ − (81792+28800z)t⁸
           − (504576+158976z)t⁹ + (20736z−20736)t¹⁰].
```

The **minimal eventual constant-coefficient recurrence order over Q(z) is exactly 10**. Indeed, for d≥11,

```text
a_d(z) = 20a_(d−2)(z) + (396+20z)a_(d−4)(z)
       + (4944+48z)a_(d−6)(z) + (32832+1728z)a_(d−8)(z)
       − (186624+62208z)a_(d−10)(z).
```

The even and odd subsequences, indexed by m in `a_(2m)(z)` and `a_(2m+1)(z)`, each have **minimal eventual order 5** over Q(z). At z=0 this gives the number of histories avoiding `aAc`; its minimal eventual order is 10, with first values

```text
48, 288, 1719, 10260, 61236, 365472, 2181348,
13019184, 77705712, 463777920, 2768096880, 16521157440, ...
```

## Proof

PREFIX-524 established the event-renewal identity (on the same frozen graph)

```text
P(t,z) = 48/(1−6t) + 9t²(z−1)/[(1−6t)²(1−(z−1)R(t))],
R(t) = [A(4t²)−1]/4,
A(u) = [1−5u−21u²−75u³−108u⁴]
       /[1−5u−26u²−78u³−135u⁴+243u⁵].
```

Substitute A and clear the scalar denominators in Q[z,t]. Exact polynomial arithmetic reduces this identity to N/D displayed above. Observe that D has even powers only, degree 10 in t and leading coefficient `186624+62208z`, while N has both parities. The two coefficients of D and N are polynomials over Z[z]. The primitive t-polynomial D has constant term 1, so any positive-t-degree common factor over Q(z) may be taken in Q[z,t]. Specialize z=0; the t-degree of D remains 10. Direct Euclidean calculation gives

```text
gcd_Q[t](N(t,0),D(t,0)) = 1.
```

A short independently executable finite-field witness is `gcd_F101[t](N(t,0),D(t,0)) = 1`, with degree-10 D retained modulo 101. Therefore D is the reduced denominator over Q(z), and the minimal eventual linear-recurrence order is 10 (rational generating function/linear recurrence equivalence).

Set v=t², and split N(t,z)=N_even(v,z)+t N_odd(v,z); D(t,z)=D_even(v,z). The sequences indexed by m have generating functions `N_even/D_even` and `N_odd/D_even`. Since D_even has degree 5 and each numerator is coprime to it (verified already at z=0 by polynomial Euclid, also modulo 101), both minimal orders are 5. The z=0 specialization retains degree-10 D and coprime numerator, establishing the avoidance order. QED.

## Exact certificate and observed coefficients

The attached independent JavaScript BigInt certificate reconstructs the 48 frozen phases, all legal transitions, two labeled primitive-step branches, and KMP gate increments; it aggregates all histories by (phase,last-inner,H) at lengths d=0..17 and verifies **every coefficient** of the polynomial identity D(t,z)P(t,z)=N(t,z) in that range. It also checks total histories `48·6^d`, first gate moment `9(d−1)6^(d−2)` (d≥2), and modular-101 polynomial Euclidean gcd for all three reductions.

At d=6 the direct histogram H=0,1,2 is `[2181348,57960,180]`; at d=10 the histogram H=0,1,2,3 is `[2768096880,132513840,1762128,3600]`, agreeing with PREFIX-524. The finite program checks the implementation; the rational identity and coprime argument yield the infinite-length minimality statements.

## Resource/observer result

The full BRC/H path-fiber histogram in PREFIX-528 needs a generic order-22 scalar observer; after *explicitly discarding the six-axis BRC coordinate readout*, the gate-only aggregated observer has exact order 10. For a single fixed numeric z, advancing the sequence uses five delayed coefficients and O(1) scalar-arithmetic work per macro-depth once the first 11 coefficients are known. Recovering all H coefficients at each depth still requires growing polynomial storage/bit arithmetic. The 49-dimensional phase-resolved controller and 51-state online deterministic controller remain appropriate for their richer specified future/phase/path observers.

## Next research unit

Test fixed-origin gate-only and fixed-origin/single-axis BRC observers for exact lower-order quotients. A distinguishing computation is the reachable/observable rank of the symbolic 49-realization, proved via an explicit full-rank finite-field specialization or an exact symmetry quotient. Compare bit-level runtime against the 49 linear and 51 deterministic alternatives; retain branch and Cell provenance when the observer requests it. The larger arbitrary-three-axis C6 and native X6 rotation dynamics objectives remain active.

**Sources:** PREFIX-524 [full event distribution](research_notes/portable_direct/2026-11-06_prefix524_complete_aAc_event_distribution_r6.md), PREFIX-528 [joint BRC-gate denominator](research_notes/portable_direct/2026-11-06_prefix528_generic_joint_brc_gate_minimal_denominator.md), PREFIX-530 [49-dimensional realization](research_notes/portable_direct/2026-11-06_prefix530_49_coordinate_rank_one_linear_lift.md). P000 and ACTIVE worldview govern this candidate subproblem; all scientific graph inputs stay at the frozen pin.
