# PREFIX-547 — Exact Krylov rank 23 and a minimal linear BRC–gate observer

Date: 2026-11-07 (Asia/Shanghai). Independent-author research; task `RS-X6-NATIVE-ROTATION-DYNAMICS`.
Frozen science: `enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Previous frontier: PREFIX-546 at `b72eaa9e7a9436972d0602e88611e33ffb58f1f1`.
Scientific status: AUTHOR_PROVED / EXACT_FINITE_RELATION_CERTIFICATE / NONZERO_MODULAR_MINOR / INTEGER_CHECKED / BENCHMARKED / UNREVIEWED / NOT_ADMITTED.

## Model and question

The frozen four-STAR incidence family is A=(1,3,6), B=(1,4,5), C=(2,3,5), D=(2,4,6): 48 directed phase states, 144 phase edges, 96 phase–previous-branch-bit ports, and six (three successors × INNER/OUTER) continuation actions per port. Target phase T=(A,+L1,-L3). The gate increments on prior/new INNER labels and arrival at T. For original root sign r in {-1,0,1}, the typed first-axis BRC increment on a phase edge i→j is

`τ_r(i,j)=(|σ(i)|+|σ(j)|−|σ(j)−r|+|σ(i)−r|)/2 ∈ {0,1}`.

The finite 96-port transfer `M_r` has weights `q^τ z^gate`. The 28-class full-length scalar weighted-row-congruent quotient `Q_r` was proved in PREFIX-545; PREFIX-546 establishes that the same 28 classes work for all root signs. The question here is the least field-linear dimension needed to produce every scalar future histogram `F_c^r(d;q,z)=e_c^T Q_r^d 1`, for all 28 classes and all integer depths d≥0, over `K=Q(q,z)`.

## Theorem: exact symbolic Krylov rank is 23

For each r in {-1,0,1}, let `K_r=[1,Q_r1,Q_r²1,…]` (28 rows, all future depths). Then

`rank_K(K_r)=23`.

This is the **minimal dimension of a linear realization** simultaneously recovering all 28 scalar BRC–gate future readouts for this root-sign model.

### Upper bound: five all-depth polynomial identities

With the canonical class ordering from the PREFIX-545 depth-0..5 fingerprints, put `F_j=F_j^r(d;q,z)`. The following full-polynomial relations hold for every r and every d≥0:

1. `F14 + F3 − F4 − F13 = 0`.
2. `F24 + F6 − F10 + F18 − F19 − F22 = 0`.
3. `F25 + F8 − F12 + F20 − F21 − F23 = 0`.
4. `F26 + F12 − F17 − F20 = 0`.
5. `F27 + F6 − F16 − F22 = 0`.

Let `R` be their 5×28 coefficient matrix. The complete exact-weight enumeration of all 96 ports and 6 continuation actions gives the 28-class weighted-row congruence. For all three signs, an additional **420 exact coefficient comparisons** establish

`R 1_28=0;  R Q_r = A R`,

with the same integer 5×5 matrix

```
A = [[0,0,0,0, 0],
     [0,0,2,0, 0],
     [0,2,0,0, 0],
     [0,0,0,0,-2],
     [0,0,0,-2,0]].
```

The submatrix `R[:,(14,24,25,26,27)]` is the 5×5 identity, hence the rows are independent. Induction gives `R Q_r^d 1=A^d R1=0` for all d. Thus the Krylov columns lie in the 23-dimensional `ker R` and rank≤23. This is a universal-depth exact polynomial proof, not an extrapolation of a finite test window.

### Sharpness: three explicit nonzero minors

Specialize `q=2,z=3` over the exact prime field `F_1000000007`. Select the 23 row indices

`I=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,19,20,21,22,23)`

and columns `d=0,...,22` of the Krylov matrix. The three 23×23 determinants modulo 1000000007, computed by the included exact modular elimination certificate, are:

| root sign | nonzero determinant |
|---:|---:|
| −1 | 432740053 |
| 0 | 802959647 |
| +1 | 609260682 |

Each determinant is the evaluation of a polynomial with integer coefficients. Since its residue is nonzero, the corresponding polynomial determinant is nonzero over `Q(q,z)`. Consequently rank≥23 for each r; together with the upper bound, **rank=23 exactly**. This also proves no field-linear realization producing all 28 class outputs can have dimension below 23.

## Constructive 23-dimensional realization

Write `J=(14,24,25,26,27)`. Define the 28×23 integer matrix `E`: on retained rows I it is the identity, and on each row J_a it uses `−Σ_{i∈I}R[a,i] x_i`. Then `R E=0`, `E 1_23=1_28`, and `E` identifies the 23-vector with `ker R`. Construct

`T_r = (Q_r E)[I,:]`, a 23×23 matrix over `Z[q,z]`.

Because `RQ_r=AR`, the subspace `ker R` is invariant, so `Q_r E=E T_r`. For all d≥0,

`Q_r^d 1_28 = E T_r^d 1_23`.

Reading row c(v) recovers the exact joint BRC–gate histogram from any native phase–bit port v. The 23-state transition has 75 nonzero monomial terms, including 11 negative coefficients, for each sign. It is a **signed virtual linear observer**, while native BRC path multiplicities remain nonnegative in the 96-port combinatorial substrate. The existing 28-state quotient remains the smaller proved nonnegative state-merging realization. Neither representation discards native Cell/branch relations for future chosen-action operations.

## Exact reproducible evidence

Run `python PREFIX547_compact_23state_certificate.py 24` alongside the previously published `PREFIX545_compact_exact_certificate.py` and `PREFIX546_shared_gauge_certificate.py`, at their recorded historical commits. A second fully self-contained Python certificate and a batch benchmark are included in the local evidence bundle.

The published compact certificate returned `ALL_CHECKS_PASS`: 420 exact symbolic relation coefficient comparisons, three nonzero 23×23 minors, 7,200 complete polynomial port-output comparisons (3 root signs × 96 ports × depths 0..24), and 528 independent original native endpoint BRC checks (48 roots × initial OUTER × depths 0..10). A separate self-contained certificate additionally checked both starting bits, 1,056 native comparisons. The unbounded mathematical claims derive from exact finite intertwining identities plus determinant nonvanishing.

Full-batch benchmark of 48 rooted polynomials at every length 0..N, five repeated CPython/tracemalloc median runs, with all algorithm outputs compared by exact equality:

| max N | 23-core s | 28-core s | 49-core s | 23 peak bytes | 28 peak bytes |
|---:|---:|---:|---:|---:|---:|
| 8 | .014551 | .010650 | .027570 | 217968 | 171024 |
| 16 | .057184 | .042633 | .084703 | 792476 | 608424 |
| 24 | .134152 | .107080 | .222457 | 2010252 | 1518476 |
| 32 | .285531 | .244443 | .478184 | 4187476 | 3118800 |

Shared quotient discovery and all 23-transfer setup: median .018479 s, 229144 bytes peak. At N=24, 23-dimensional implementation including setup ~0.153s vs 28-dimensional ~0.126s. Thus **minimal linear dimension does not by itself reduce runtime or memory** in this signed implementation; negative intermediate coefficients and readout reconstruction motivate another integral or positive realization.

## Prior art, precise scope and next unit

Classical weighted-automata Hankel-rank minimization is established mathematics; see Borja Balle, Prakash Panangaden and Doina Precup, *A Canonical Form for Weighted Automata and Applications to Approximate Minimization* (2015), arXiv:1501.06841, DOI 10.48550/arXiv.1501.06841. The five relations, exact rank certificate, BRC-specific readouts and measured costs are derived for this frozen candidate here.

Next PREFIX-548: search for an alternative 23-coordinate basis with nonnegative polynomial transitions or materially lower signed-cancellation cost; verify all 48-root outputs including setup/recovery. Then test which of the five polynomial relations survive two-axis and six-axis BRC joint observations, producing specific witness paths where a relation fails.

Native control status/continuation requests returned `BACKEND_IDENTITY_OR_VERSION_MISMATCH`, `operation_sent=false`. No new native Researcher-ID, owner confirmation, CLAIM, Result, Review or admission is claimed. This is an independent-author Source artifact.
