# R749SG — Exact Walsh-lineage rank and minimal observer-safe source coordinates

Date: 2026-11-12 (Asia/Shanghai). Research2 direct independent mathematical continuation, NOT a CLAIM on RS-X6-TRIADIC-CLOSURE-DYNAMICS. Native session registration request `research2-20261112T2239-r749sg-direct-start` initially QUEUED; no unverified Researcher-ID is asserted. Source scientific inputs retain the predecessor pin `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`. Source model: R749SF at `066958c8da10e4d67395f3c9b6942a8d9d26daa7:research_notes/portable_direct/2026-11-12_R749SF_EIGHT_LIFT_HIDDEN_SIGN_FILTER.md`; R749SA 8:1 quotient at `ec7b7eec75e177e9d10c99b5cf943400189416d1`. Author-side exact proof plus independently executed finite-graph rational checker, NOT independent mathematical review.

## A. Typed domain and conditioned path

Six named X6 axes; signed Port=(axis, ±1). A signed directed-edge state (u,v) joins two distinct-axis two-Port vertices with precisely one *identical signed Port* shared and three distinct underlying axes. There are 60 signed vertices, 960 signed directed edges, 120 unsigned directed supports and eight signed lifts per unsigned support (R749SF). This is a restricted X6 observer model, not a replacement ontology or a native Cell/Link/Port event license.

Let `A,B` be initial unsigned two-axis supports with |A∩B|=1. Let `omega=(A,B,C_1,...,C_m)` be a fixed legal unsigned path; every consecutive pair is adjacent. The conditional Markov kernel from an initial distribution over the eight signs on A∪B to the final eight signs is `K_{omega,p}`, where `p∈[0,1]` and only positive-probability unsigned paths are conditioned upon.

Write `q=(1+15p)/16`, `r=(1-p)/16`, `a=(1+7p)/8`, `theta=(q-r)/(q+r)=8p/(1+7p)`. Every step `(A,B)->(B,C)` has two types:

- **Forced unsigned C1:** `C=A△B`. The sign on the A-only axis is transferred with an independent binary symmetric channel of correlation theta; two B-axis signs are retained. Thus the three previous sign lineages move bijectively to three final slots.
- **Nonforced unsigned:** `C≠A△B`. The sign on the A-only axis is discarded, B-axis signs survive, and the sign on the new C-only axis is an independent fair coin, even if this axis name occurred earlier in the path. At p=1 these paths have zero probability and cannot be conditioned upon.

The eight-state filter is exactly the R749SF conditional kernel, including its source-label semantics.

## B. Theorem: Walsh pullback is monomial-or-zero along every observer word

Initialize one source-lineage tag for each of the three named axes in A∪B, with forced-flip count zero. At each nonforced step, delete the tag of the dropped A-only slot, and mark the newly created sign as fresh/fair. At each forced step, transfer the A-only tag and increase its flip count by one; if the tag is already fresh it stays fresh. At p=0, a forced BSC has theta=0, so *also* mark its transferred tag fresh. A fresh tag stays fresh along future transfers. Denote by `h_omega(x)=(ancestor_x,k_x)` the retained original source axis and forced-BSC count for each currently tagged final axis x; otherwise `h_omega(x)=⊥`.

For a subset S of the three final axes, let `chi_S(s)=∏_{x∈S}s_x`, with chi_empty=1. Let `mu0` be an arbitrary initial eight-sign probability distribution. Then

```
E_{K_omega,p(mu0)}[chi_S] =
  0                                          if some x in S has h_omega(x)=⊥;
  theta^(sum_{x in S} k_x) *
    E_mu0[chi_{ {ancestor_x : x in S} }]     otherwise.
```

The ancestors in the second case are distinct. This is an exact algebraic identity for every finite legal omega and all p in [0,1] on positive-probability conditioned paths. In particular, no nontrivial Walsh coefficients mix under a fixed unsigned path. The proof is induction: in each forced BSC, E[s_new|s_old]=theta*s_old with independent noise; an independent fair fresh sign kills every parity containing it; copied signs retain their parity. Conditional path likelihood depends only on unsigned supports, so Bayesian reweighting introduces no source-dependent factor.

## C. Sharp rank/minimal residual theorem

Let `r_p(omega)` be the number (0..3) of currently surviving *original* sign-lineage tags at the final edge under the preceding rule. Then the real linear rank of the 8×8 row-stochastic operator is exactly

```
rank(K_omega,p) = 2^r_p(omega).
```

Equivalently, as the arbitrary initial distribution mu0 varies over the eight-sign simplex, the affine dimension of the family of possible final sign distributions is exactly `2^r_p(omega)-1`.

**Proof:** The 8 Walsh output characters form a basis for functions on the final sign cube. The adjoint K acting on an output character is either zero or a nonzero scalar times a distinct initial Walsh character supported on the r surviving ancestral axes. All `2^r` such characters appear (choose the corresponding final slots). They are linearly independent. Hence the rank is exactly `2^r`, and the image of the affine probability hyperplane has dimension rank−1. For p>0, theta>0 so a forced BSC preserves linear rank; at p=0 its zero correlation is accounted for by deleting that lineage. At p=1, every admissible path is forced and has r=3.

For the declared query language of *all current signed-Port distribution readouts at the final state*, exactly `2^r-1` independent affine source statistics are necessary and sufficient; a convenient sufficient coordinate set is the nonempty Walsh moments of the surviving r initial tags. This is a minimal **affine/expectation-coordinate** claim; it does not claim an absolute bit-information lower bound under arbitrary nonlinear encodings. For a smaller declared family of signed parity queries, retain exactly its distinct nonzero Walsh pullbacks, which may be fewer.

## D. Explicit compression/repair certificate and boundary cases

At any `0<p<1` (e.g., p=1/2, theta=8/9), a purely forced path preserves all three source lineages and has rank 8. One nonforced step erases one lineage, producing rank 4; two consecutive nonforced steps erase two, giving rank 2; the legal unsigned example

```
{0,1} → {1,2} → {2,3} → {3,4} → {4,5}
```

has three nonforced updates, erases all three source lineages and has rank 1: the current three sign bits are independent fair coins, regardless of mu0. At p=0, even forced updates can erase a lineage, and after any two updates from a fixed directed edge exactly one original lineage survives, giving rank 2. At p=1 only forced updates have positive probability and rank remains 8 for every admissible path.

If the future query language includes an **earlier historical source sign** after its lineage was erased, the current eight-state posterior cannot reconstruct that source; two initial point-mass priors that differ only on the erased sign yield the same future current-sign law. A scope-typed repair is to retain that original sign or its posterior moment separately in a historical provenance ledger. For arbitrary historical joint queries of all three original signs, retaining their entire seven nonconstant Walsh moments is sufficient; a past/current joint-distribution query may need additional properly typed branch correlations. This cleanly separates a safe current-state quotient from a loss of provenance under a stronger future language.

## E. Validation

Standalone checker `R749SG_WALSH_LINEAGE_RANK_EXACT_CHECK.py` reconstructs the entire signed graph and checks **all** 120 unsigned initial directed edges and **all** 64 legal length-two unsigned continuations for p=0 and p=1/2, i.e. 15,360 fixed-path matrices. It compares all eight Walsh characters and all eight input source lifts against exact integer-scaled source pullbacks. It also checks all 512 length-three continuations from one fixed initial edge at p=1/2 and 120 p=1 forced steps. Python integer arithmetic, no float approximations.

Exact PASS histogram for the 7,680 length-two paths at p=1/2:
- r=3: 120 paths (rank 8);
- r=2: 1,680 paths (rank 4);
- r=1: 5,880 paths (rank 2);
- r=0: 0.

At p=0, all 7,680 length-two paths have r=1 (rank 2). The finite checker proves these enumerated statements; the all-length rank theorem follows from the preceding algebraic induction, not extrapolation from the tests. The 16-successor signed C1 source and 8:1 observer laws are treated exactly as in R749SF.

## F. Next research problem

For a future query family that can include **historical/current joint Port events**, characterize minimal time-indexed Walsh and BRC branch-association residuals under adaptive unsigned observation words; test whether a native V29/V39 permissioned three-force closure event can instantiate any of these abstract transitions. Do not conflate signed-Port graph compatibility with native event permission.
