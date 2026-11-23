# R284FO — 四代跨代漏写与全局读取噪声的统一容量下界：n ≥ 4q+5u+2

Date: 2026-11-23 (Asia/Shanghai)  
Status: AUTHOR_PROVED / EXACT_FINITE_CROSSCHECKED / NOT_REVIEWED  
Mode: informed TASK_RESEARCH, portable scientific material; no shared CLAIM or formal Result.

## 1. Question, inherited definitions, and scope

Direct continuation of R284FM (the exact capacitated Hall/flow-cut criterion) and R284FN (the prior n ≥ 4q+3u+2 bound), with the exact model and frozen R284CO scientific inputs inherited through R284FL. P000 and the ACTIVE Heartbeat World are unchanged. The four-phase tag is an auxiliary discrete observer code, not an assertion about native X6 geometry.

Four distinct fixed binary tags c0,c1,c2,c3 repeat in a cycle. Each publication writes the changed coordinates in a fixed, arbitrary non-atomic order, with at most q omissions per publication and unlimited carryover of residual omissions. An independent read may flip at most u bits. A stateless decoder must identify all stable phases, produce no third-phase success during publication, and never permit a new-phase success followed by an old-phase success on the same prefix trajectory. Integers q,u are nonnegative. All-constant columns can be removed; take n to be the number of active coordinates.

**Theorem R284FO-1 (global all-parameter necessary bound).** For any such protocol, without assuming a Gray code or independent repeated-bit groups,

    n_min(q,u) ≥ 4q + 5u + 2,       q,u ∈ Z_{≥0}.

The bound strengthens both branches of R284FN's previous combined bound max(4q+3u+2, 3q+5u+2). It is sharp on either coordinate axis: for u=0, R284FL proves n_min(q,0)=4q+2; for q=0, the earlier omission-free four-phase construction gives n_min(0,u)=5u+2. The joint positive-(q,u) global sharp capacity remains open (notably n_min(1,1)=12 from R284FH, exceeding the new bound 11).

## 2. Exact ingredients and the alternating coordinate

Normalize c0=0 by coordinatewise bit complementation, and let x_p be the multiplicity of the active column pattern p=(c1[k],c2[k],c3[k]), p=1,...,7, encoded by the integer p with c1 as its least significant bit. Thus n=Σ_{p=1}^7 x_p. Let b=x_5; p=5 is the alternating phase column (0,1,0,1).

Inherited R284FH's no-rollback prefix argument gives the *four adjacent-phase distance* necessities

    d(c_i,c_{i+1}) ≥ A := 2q+4u+1.

Each nonalternating active column contributes exactly two changes to the four cyclic adjacent distances; the alternating column contributes four. Therefore

    Σ_{i=0}^3 d(c_i,c_{i+1}) = 2n+2b,
    n+b ≥ V := 4q+8u+2.                                  (1)

For either opposite-phase graph G_02 or G_13, the R284FM theorem says disjoint radius-u stable readouts force a vertex subset U with

    |E(U)| > q|U|+2u.                                      (2)

The graph has precisely four relevant vertices and is K_(2,2) on four coordinate-pattern edge types. For G_02 these types are {2,3,6,7}; for G_13 they are {1,3,4,6}. Their common types {3,6} are **disjoint**, not adjacent, in both graphs. Neither opposite graph uses pattern 5. There are only three possible useful witness shapes:

- Two vertices: a *single* type p with x_p ≥ 2q+2u+1.
- Three vertices: two adjacent types with combined multiplicity ≥ B := 3q+2u+1.
- Four vertices: all four edge types with combined multiplicity ≥ C := 4q+2u+1.

This classification is exhaustive: a one-vertex set carries no edge, and any extra isolated vertices only raise the right-hand capacity.

## 3. All-parameter analytic proof

Suppose n≤4q+5u+1. Both opposite-phase graphs must have separation witnesses by (2). We show every possibility impossible.

**Case I: at least one four-vertex witness.** All its edge types are nonalternating, so n-b≥C=4q+2u+1. Adding (1) gives

    2n ≥ (4q+2u+1)+(4q+8u+2) = 8q+10u+3,

but the assumed n gives 2n≤8q+10u+2. Contradiction.

**Case II: at least one two-vertex witness.** Its single pattern p occurs at least 2q+2u+1 times. Every pattern belonging to an opposite-phase graph is nonalternating and changes at exactly two of the four cyclic adjacent publication edges. Choose an adjacent edge at which p does not change. The entire Hamming distance along that edge comes from columns other than p, hence n-x_p≥A. Thus

    n ≥ (2q+2u+1)+(2q+4u+1) = 4q+6u+2,

contradicting n≤4q+5u+1.

**Case III: both graphs use three-vertex witnesses.** Their type supports P and Q are two-element sets, of multiplicity at least B each. They exclude pattern 5. Since the two opposite graphs have shared types only {3,6}, which cannot coexist in a three-vertex witness, P∩Q has either zero or one type.

If P∩Q is empty, n-b≥2B. Adding (1) gives

    2n ≥ 2B+V = 10q+12u+4,
    n ≥ 5q+6u+2 ≥ 4q+5u+2,

contradiction.

If P∩Q={p}, p is type 3 or 6. Put m=x_p. Inclusion-exclusion of the two witness supports gives

    n-b+m ≥ 2B.                                           (3)

Type 3 changes only edges 0→1 and 2→3, while type 6 changes only edges 1→2 and 3→0. Thus at least one adjacent edge does not change type p; its distance bound yields

    n-m ≥ A.                                              (4)

Add (3), (4) and (1):

    3n ≥ 2B+A+V
       = 12q+16u+5.

Under the supposed n≤4q+5u+1, however, 3n≤12q+15u+3, impossible because u+2>0.

All cases are excluded. Hence n≥4q+5u+2 for all integers q,u≥0. No enumeration or machine algebra is needed for the universal proof. QED.

## 4. Near-extremal residual structure

**Corollary R284FO-2 (alternating-column lock).** If a protocol has n=4q+5u+2 and at least one opposite-phase graph uses a four-vertex separation witness, then

    x_5 ∈ {3u,3u+1}.

Indeed (1) gives b≥V-n=3u, while the four-vertex witness gives b≤n-C=3u+1. Moreover, for every u≥2, any hypothetical protocol attaining this global lower bound **must** use such a four-vertex witness: Case II always costs ≥4q+6u+2; disjoint Case III costs ≥5q+6u+2; overlapping Case III gives n≥4q+ceil((16u+5)/3), strictly larger than 4q+5u+2 when u≥2. This is an observer- and model-typed structural restriction, not a conjectural geometric identification.

The positions and last-write provenance of the alternating coordinates still matter for the exact six-pair cuts and all publication prefixes. Replacing them by only total Hamming distance is not a full protocol proof.

## 5. Exact computational crosscheck and additional finite exclusions

Independent standard-library Python implementation: `R284FO_all_noise_cycle_bound_checker.py`. Its inputs are the seven pattern multiplicities x_p, q and u. It obtains each last-update edge from the four phase bits, constructs all six two-sided capacitated-cut families, applies four adjacent prefix-distance necessities and two opposite stable-distance necessities, and tests every weak composition of n=4q+5u+1 into seven classes. This is a complete coordinate-permutation quotient at each declared n.

Actually executed with Python integer arithmetic for 0≤q≤4 and 0≤u≤2: **2,518,909** pattern histograms, **4,878** survived the six distance necessities, **zero** survived all six exact flow-cut tests. The closed-form proof, not this finite check, is the evidence for the universal parameter range.

Separately, with full *six-pair* cuts (beyond the two opposite cuts needed in the analytic proof), the same checker exhaustively excludes these further individual widths:

| (q,u) | Excluded n | Histograms | Consequence |
|---|---:|---:|---|
| (3,1) | 19 | 177,100 | n_min(3,1) ≥20 |
| (4,1) | 23 | 475,020 | n_min(4,1) ≥24 |
| (5,1) | 27 | 1,107,568 | n_min(5,1) ≥28 |

These last three are **finite necessary-condition exclusions**, not all-q sharp formulas and not constructions at the resulting next widths. The combined run enumerated **4,278,597** histograms. The code has explicit assertions and emitted per-parameter counts; source/result agreement was checked in this research turn. Independent author-unrelated mathematical review is still pending.

## 6. Provenance and next executable scientific question

- R284FH, exact 4-edge prefix distance and known n_min(1,1)=12: `research_notes/portable_direct/R284FH_RESET_FREE_SHARP_TWELVE_BIT_CYCLE_20261123.md` at project commit `74b390d267ec130a2da8fb170e10214aeeb7351e`.
- R284FM, exact per-pair all-u residual/observer flow cut: `research_notes/portable_direct/R284FM_NOISY_OBSERVER_FLOW_CUT_AND_ADDITIVE_LOWER_BOUND_20261123.md` at `1d1c5dd412719c7aaf016187b6493b77253cd9f9`.
- R284FN, former combined capacity bound: `research_notes/portable_direct/R284FN_STRONGER_FOUR_EDGE_NOISY_CYCLE_LOWER_BOUND_20261123.md` at `eae73bbb24a6e5b8ee54911dc54a480b83fad453`.
- Frozen scientific task lineage R284CO remains inherited, not re-pinned. P000/ACTIVE worldview untouched. Source publication and Activity/CLAIM/Result/Review have distinct authority.

**Next:** exploit the near-extremal alternating-column lock and all six last-update flow cuts to settle whether the strengthened n=4q+5u+2 line can be attained for positive q,u; separately validate full prefix legality for candidate near-extremal histograms rather than mistaking stable endpoint separation for a complete protocol. The finite q=3,4,5;u=1 exclusions suggest a further parameter-dependent obstruction, but do not establish an infinite-q theorem. Then extend the precise observer to bank-data omission and H-lag reader state without prematurely compressing residual provenance.
