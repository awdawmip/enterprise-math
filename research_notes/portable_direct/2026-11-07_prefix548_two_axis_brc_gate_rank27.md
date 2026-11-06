# PREFIX-548 — Exact two-axis BRC–gate observer rank 27

Date: 2026-11-07 (Asia/Shanghai). Independent-author research, task line `RS-X6-NATIVE-ROTATION-DYNAMICS`. Scientific input frozen at `enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`. Continuation: PREFIX-547 (`aa9672fd3d7b570e323c39bdb3cc25ffd76a774e`). Status: AUTHOR_PROVED / EXACT_FINITE_TRANSITION_CERTIFICATE / NONZERO_MODULAR_MINOR / INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED.

## Model and question

The frozen four STARs are A=(1,3,6), B=(1,4,5), C=(2,3,5), D=(2,4,6). They induce 48 directed phases, 144 allowed phase edges, and 96 phase–previous-branch ports. Each port has three successor phases and two INNER/OUTER options. A gate is registered when prior and new bits are both INNER and the new phase is `(A,+L1,-L3)`.

PREFIX-547 proved a rank-23 field-linear realization for the first-axis BRC cancellation count plus the gate. Here retain the **joint** first-axis and second-axis BRC counts, as well as gate count. For axis `a∈{1,2}`, let `σ_a(i)` be ±1 when the current signed line in phase i lies on axis a, and 0 otherwise. Fix the original root signs `r_a=σ_a(root)`. Define for each phase edge i→j

`τ_(a,r)(i,j)=(|σ_a(i)|+|σ_a(j)|−|σ_a(j)−r_a|+|σ_a(i)−r_a|)/2`.

The 144-edge finite verification for each axis and root sign gives `τ∈{0,1}`. The original BRC endpoint formula telescopes to `p_a=Σ τ_(a,r)` along a legal path (the same typed identity used for axis 1 in PREFIX-539). Assign each labeled step monomial weight `q1^τ1 q2^τ2 z^g`, where `g` is the gate increment. There is no marginalization of either axis.

A true initial phase has one signed current axis, so the **five physically realized two-axis root-sign pairs** are `(0,0),(1,0),(-1,0),(0,1),(0,-1)`. We study all 96 continuation-port readouts relative to each fixed root-sign parameter; this suffices for all 48 actual rooted path outputs.

## Theorem: rank is exactly 27 for each rooted parameter

For each of the five root-sign pairs, the same 28 weighted state-merging classes discovered using first-axis depth-0…5 fingerprints in PREFIX-545 remain an **exact nonnegative all-length quotient** for the joint `(p1,p2,h)` observation. Their 28×28 transfer is `Q_(r1,r2) ∈ Mat_28(Z[q1,q2,z])`. Define the infinite Krylov output array

`K_(r1,r2)=[1,Q1,Q²1,...]`,

with 28 rows, one per class, over `F=Q(q1,q2,z)`. Then

**`rank_F K_(r1,r2)=27` for each of the five pairs.**

This is the minimal dimension of a **field-linear** system simultaneously recovering all 28 class future-histogram readouts, for every `d≥0`.

### Exact quotient and upper-bound certificate

Generate the original canonical class IDs by the complete first-axis r=0 depth-0…5 fingerprint (first-encounter numbering, as in PREFIX-545). For **every** one of the five root-sign pairs, enumerate all 96 ports and their six labeled actions; compare complete counters indexed by `(destination_class,τ1,τ2,gate)`. Each class has exactly one weighted transition row independent of the source port. This is 5×96×6=2,880 checked actions. Weighted row congruence implies, by induction on future length, that each quotient exactly reproduces the underlying 96-port scalar polynomials for **all** lengths.

With the canonical 28 class IDs, exact coefficient comparison yields the row equality

`Q[14,*]+Q[3,*]−Q[4,*]−Q[13,*]=0`

for **all five** root-sign pairs, over `Z[q1,q2,z]`. The corresponding combination of `1_28` is zero. Hence the all-length polynomial identity

`F14(d)+F3(d)−F4(d)−F13(d)=0` for every `d≥0`.

The Krylov rank is therefore at most 27.

### Nonzero 27×27 minor: sharp lower bound

Take row indices `I={0,1,...,27}\{14}`, depth columns `d=0,...,26`, evaluate `q1=2,q2=5,z=3`, and compute the determinant modulo the prime `1000000007`. Exact modular elimination returns:

| Root signs (r1,r2) | 27×27 determinant mod 1000000007 |
|---|---:|
| (0,0) | 537344283 |
| (1,0) | 244920416 |
| (-1,0) | 819338349 |
| (0,1) | 559915505 |
| (0,-1) | 435513067 |

Every residue is nonzero. Each evaluated determinant is the specialization of a polynomial determinant with integer coefficients. Nonzero residue therefore proves that the respective symbolic minor is nonzero over `Q(q1,q2,z)`. Rank is at least 27, establishing the theorem. This is an exact all-length statement derived from a finite symbolic identity and nonzero minor, not a finite-depth extrapolation.

### Constructive minimal 27-coordinate observer

Let E map 27 retained coordinates indexed by I to 28 class coordinates: on I, E is the identity; its row 14 is `E[14]=E[4]+E[13]−E[3]`. Define the 27×27 matrix `T=(Q E)[I,*]`. Because the relation row annihilates Q, `Q E=E T`, and because `E 1_27=1_28`, induction yields

`Q^d 1_28=E T^d 1_27` for all `d≥0`.

The 27-coordinate realization may have signed intermediate coefficients. Nonnegative native path multiplicities are preserved by the original 96-port carrier and the 28-class quotient. The 27-coordinate result is observer-specific; chosen-action continuation, Cell identity, path provenance and other future operations retain their own information requirements.

## Which of the prior five relations survive?

At root-sign pair (0,0), name the five full first-axis polynomial relations of PREFIX-547 `R1,...,R5` in their original order; R1 is the surviving `F14+F3−F4−F13`. Exact joint polynomial evolution gives the **earliest nonzero witness** for each of the four former relations:

| Relation | Earliest nonzero depth | Exact polynomial |
|---|---:|---|
| R2 | 6 | `16 q1 (q2−1)(z−1)(q1+q2−1)` |
| R3 | 3 | `2 q1 (q2−1)(z−1)` |
| R4 | 3 | `−2 q1 (q2−1)(z−1)` |
| R5 | 4 | `4 q1 (q2−1)(z−1)` |

Thus adding the second native BRC count distinguishes four independent directions of future observation that were collapsed by the first-axis-only rank-23 readout. Upon setting `q2=1` these witness polynomials vanish, as required by first-axis marginalization. The exact rank-27 result proves there is precisely one remaining linear relation among the 28 class future readouts over `Q(q1,q2,z)`.

## Executed evidence and costs

The standalone extended Python integer/formal-polynomial certificate was executed with `depth=16, native_depth=8` and reported `ALL_CHECKS_PASS`. It verifies 2,880 labeled quotient transitions, 140 exact 27-state intertwiner rows, **8,160** full joint polynomial comparisons (5 root-sign pairs ×96 ports×17 depths) and **864** independent native visit-count/endpoint-correction checks (48 actual roots ×2 prior-bit states×9 depths). It also asserts the four minimal symbolic counterexamples. The native reference reconstructs both BRC counts via axis-visit totals and final endpoint corrections, instead of using local τ, providing an independent implementation check. Full source and raw output are in the companion local evidence archive.

The published self-contained `PREFIX548_compact_exact_certificate.py` independently rebuilds the 28-class quotient, all five exact upper-bound row identities, and the five nonzero modular 27×27 determinants. It executed successfully on CPython 3.13.5; the matching compact result is `PREFIX548_COMPACT_EXECUTION.json`.

An exploratory CPython 3.13.5 Linux comparison generated both initial bit states for all 48 actual roots at every depth 0…24 (2,400 rooted polynomials). With `tracemalloc` and five repetitions, and including full output readout but excluding one-time quotient setup, the median times were **2.7588 s for the 28-class nonnegative implementation** and **2.7842 s for the 27-coordinate signed implementation**. Median traced peak bytes were 1,962,892 and 1,908,188 respectively. The 27-coordinate basis saves some memory but did not improve runtime in these measurements. Exact program, all raw repetitions and SHA256 manifest are in the companion evidence archive.

## Provenance, scope and next research unit

This theorem concerns the frozen four-STAR **X6 carrier-readout candidate** and the declared joint `(p1,p2,h)` scalar future histogram. It extends the PREFIX-547 scalar observer while preserving the native six-axis world assumptions and the observer/future-operation scope of the project's Joint Relation Preservation contract. It does not alter P000 or the protected ACTIVE worldview.

Next unit PREFIX-549: treat all six signed-axis BRC counts jointly with the gate. Construct the exact positive weighted quotient for each actually realizable root signature and determine the generic field-linear rank by invariant row relations and explicit nonzero minors. Preliminary modular-only exploration found 51 weighted classes and numerical rank 49 for one r3=−1 parameter; this remains a next-step hypothesis pending a complete symbolic certificate. Also evaluate whether any improved integral/nonnegative realization lowers full output cost.

Native Enterprise Math Site gateway returned `BACKEND_IDENTITY_OR_VERSION_MISMATCH` with `operation_sent=false` in this run. Researcher-ID and active owner were not established; no official CLAIM, Result, Review or admission is asserted. This is an independent-author Source research artifact.