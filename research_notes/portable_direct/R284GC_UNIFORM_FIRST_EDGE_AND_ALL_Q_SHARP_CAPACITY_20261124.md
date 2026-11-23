# R284GC — Uniform first-edge obstruction; sharp four-phase noisy cycle for every q>=2

Date: 2026-11-24 (Asia/Shanghai). Mode: informed portable TASK_RESEARCH. Status: AUTHOR_COMPUTER_ASSISTED_PROOF / EXACT_INTEGER_HALL_BARRIER_VERIFIED / NOT_INDEPENDENTLY_REVIEWED. This is an auxiliary, frozen R284CO–R284FM four-phase binary observer theorem, not a P000 or native-X6 change.

## Main theorem

Retain the exact four-phase binary cycle model of R284FM/R284FT: four fixed distinct phase labels; any number of past generation updates may leave residuals, with at most q omitted bit writes on **each** update; each read may independently flip at most u=1 bit; stable reads must decode the true phase; and a non-atomic publication must neither produce a third-phase read nor permit a successful new-phase read followed by an old-phase read while the prefix is paused.

**Theorem R284GC (author-level exact computational proof).** For every integer q>=2, the minimum length of a fixed binary tag satisfying those requirements is

    n_min(q,1) = 4q+10.

The new universal step proves the lower bound for every integer q>=5; q=2,3,4 were previously covered by the exact finite calculations R284FS, R284FT, R284FU. The repeated two-Gray-group construction R284FE supplies the upper bound 4q+10 at every q>=2. This theorem's proof status is *author-proved with exactly checked finite arithmetic certificates*, not independent mathematical Review, a formal Result, project Foundation or a native-X6 theorem.

## Proof of the new universal first-edge lemma

**Step 1 — Full stable histogram classification.** R284GB proves, using all six nominal codeword distances and only the three (01),(02),(03) exact stable-source residual cuts, that each seven-pattern histogram satisfying all six stable cuts at n=4q+8 or 4q+9 and q>=5 has a unique heavy pair G among {3,5,6}, with both counts at least 2q+2. R284GA then gives all configurations exactly, in q-independent form

    x_p(q) = 2q * 1_{p in G} + z_p,      sum_p z_p = k,

for k=8 or 9. The respective complete stable necessary-condition candidate sets have 7 and 66 members. This does **not** by itself establish a viable non-atomic writing order.

**Step 2 — Exact weighted Hall formula for a partial write.** Fix an attempted prefix in edge 0->1, its subset of omitted attempts (total<=q), and the resulting counts s_p of successfully overwritten coordinates. Fix another phase j. For every coordinate type p, the R284FT flow-distance demand consists of:
- x_p(q)-s_p units when phase 0 and phase j differ, each assignable to either the independent source last-write group L_(ell_0(p)) or the target stable-state last-write group R_(ell_j(p));
- s_p units when phase 1 and phase j differ, each assignable **only** to the target group R_(ell_j(p)).

All eight omission-group vertices have capacity q. The maximum uncorrected Hamming distance deficit, equal to the minimum physical prefix-to-stable-j distance, obeys the exact capacitated Hall formula

    d_min(q,s,j) = max(0, max_{U subset V}
              [sum_{demand classes E subset U} weight_E(q) - q |U|]),

where V comprises the four source and four target group vertices. This is the max-flow/min-cut theorem applied to the exact R284FT demand network; it preserves all original omission-source identities. At the fixed prefix, every demand weight is affine in q because x_p(q)=2q*[p in G]+z_p. Hence each of the 256 Hall-cut expressions is alpha_U*q+beta_U with integer coefficients.

An exact **uniform forbidden-prefix witness** consists of a legal fixed missed-attempt vector at q0=5 and either (a) a third phase j in {2,3} with d_min<=2, or (b) phase j=1 with d_min<=2 and at most two successful overwrites, so the same physical prefix permits new-then-old decoding. To certify the witness for every q>=5, it is enough to check for **all 256 U** that

    alpha_U <= 0,       5*alpha_U+beta_U <= 2.

These inequalities prove d_min(q,s,j)<=2 uniformly for q>=5. The missed-attempt vector remains legal because its total is <=5<=q; the fixed prefix remains physically available because extra heavy-type columns remain unattempted. The radius-one balls around the two physical states intersect whenever distance<=2, so the prescribed stable decoder cannot eliminate the forbidden observation. The checker verifies all conditions with exact integers; no floating-point or extrapolation appears in this universal step.

**Step 3 — Complete finite prefix barriers.** For each of the 7+66 fixed offset families, construct a finite count lattice whose coordinates are attempted writes by changed column type on edge 0->1, bounded by their counts at q0=5. Start at the zero prefix. On every candidate next node, independently search all legal missed-attempt vectors for one of the uniform Hall witnesses above; if a witness is found, mark that node forbidden. Explore only nodes for which no such witness was found (an over-approximation of true safe paths).

For every uniformly excluded family, this over-approximation cannot reach a node where any *growing* changed type first reaches its q0=5 maximum, nor can it reach the complete q0=5 endpoint. Any update ordering at q>5 must also cross one of these same old maxima before it can finish, since the count increases by one per attempted write. Non-growing types have the same maximum at all q. Thus the finite-box barrier proves no complete safe write order exists for any q>=5, not merely for q=5.

The exact checker produces:

| Width | Complete stable candidates | Families uniformly excluded already on 0->1 | Families not excluded by this first-edge certificate | Certified forbidden nodes |
|---|---:|---:|---:|---:|
| 4q+8 | 7 | 6 | 1 | 17 |
| 4q+9 | 66 | 56 | 10 | 240 |
| **Total** | **73** | **62** | **11** | **257** |

The largest over-approximate safe-reachable search region in an excluded family had 9 nodes at width 4q+9 (4 at width 4q+8). The 11 remaining template families are **exactly the parameterized F0–F10 list in R284FW**, checked as full seven-type histograms at q0=5; they are *not* asserted to possess a successful first-edge protocol at every q.

**Step 4 — Second edge, lower bound and construction.** R284FW had already proved that each F0–F10 fails the 1->2 publication edge for every q>=2, using a 59-node barrier, exact q=2 flow witnesses and an omission-provenance-preserving lift. Combining with Step 3 excludes every n=4q+8 or 4q+9 candidate for all q>=5. R284FP had already established the baseline bound n>=4q+8 when q>=3,u=1, eliminating all smaller n. Therefore n>=4q+10 for q>=5. R284FE constructs a valid 4q+10-bit Gray two-group cycle; equality follows. The previously published exact certificates establish q=2 (18 bits), q=3 (22 bits), and q=4 (26 bits), giving the displayed formula for all q>=2.

## Exact execution and evidence

Source: `research_notes/portable_direct/R284GC_uniform_first_edge_barrier.py`. Run `python R284GC_uniform_first_edge_barrier.py`; it uses only the Python 3 standard library. It reconstructs the eight-vertex incidence masks, enumerates the full 2016 q-independent two-heavy offsets, checks R284GA's symbolic stable predicate to obtain exactly 7 and 66 families, constructs and verifies all 256 Hall inequalities for each selected unsafe-prefix witness, exhausts the finite bounded prefix lattices, and compares all eleven leftover histograms against the exact R284FW list.

Actual local execution:

    k=8 stable=7 uniformly_excluded=6 residual=1 witness_nodes=17 max_safe_nodes=4
    k=9 stable=66 uniformly_excluded=56 residual=10 witness_nodes=240 max_safe_nodes=9
    PASS: for every integer q>=5 first-edge survivors are contained in exactly R284FW F0-F10 (11 parameterized families)
    With R284GB, R284GA, R284FW, R284FP and R284FE: n_min(q,1)=4q+10 for all integers q>=5
    Existing R284FS/FT/FU cover q=2,3,4 separately

As an additional non-load-bearing implementation cross-check, an independently written exact integral max-flow routine (the previously verified R284FV prefix-distance implementation) evaluated each of the 257 selected witness prefixes at q=5,6,17,53: **1,028 integer max-flow comparisons; all distances <=2**, maximum observed distance 2. That regression is finite and is not used for the all-q quantifier, which follows from the integer Hall slopes and fixed-box barrier.

## Evidence limitations and next work

The proof is a finite, reproducible computer-assisted mathematical argument with a genuinely universal q parameter: R284GB uses exact rational Farkas identities over q as a real variable; R284GC uses exact integer Hall slopes and explicit finite monotone barriers. Its soundness depends on the frozen R284FM all-history residual-source product, R284FT flow-prefix characterization and R284FW q=2 witness-lift semantics. It has not undergone independent mathematical audit or formal Result/Review admission.

**Highest-value next unit:** independent audit of the two new load-bearing certificates and of R284FM/R284FT/FW model assumptions, especially omission group independence, the exact Hall demand-to-physical-state correspondence, and the no-rollback interpretation. Then investigate whether the same source-aware residual flow method gives a sharp general u>=2 bound; also distinguish data-bank write omissions and finite reader caching span H. No P000/ACTIVE worldview, BRC theorem, author attribution or Task frozen input has been changed.

## Frozen source lineage

- R284FM residual cut and state reachability: enterprise-math@1d1c5dd412719c7aaf016187b6493b77253cd9f9.
- R284FP analytic baseline lower bound: enterprise-math@de49ae0239abee14619a730fe6ea60614a2cde5b.
- R284FE repeated Gray upper construction: enterprise-math@9974b3b5a1031bb5c841ab5a4950a9c55baed9e0.
- R284FW uniform eleven-family second-edge obstruction: enterprise-math@bfbeefc839da0fb1b9d6d87db10c531b1f0f5cbc.
- R284GA two-heavy sector exact classification: enterprise-math@0c3284aec3e378b384beb43f232018d7978455da.
- R284GB global two-heavy star-cut theorem: `research_notes/portable_direct/R284GB_GLOBAL_STAR_CUT_TWO_HEAVY_CONVERSE_20261124.md` (prior verified main commit 5b273167).
- Prior finite q2/3/4: R284FS, R284FT, R284FU; keep original distinct authors/results/verification levels.
