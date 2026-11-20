# X6 R59 — Matching collision networks: positive-BRC cycle-trace tomography

Date: 2026-11-20 (Asia/Shanghai). Research line: RS-X6-NATIVE-TIME-DYNAMICS. Status: CONDITIONAL_AUTHOR_PROOF / EXACT_FINITE_AUTHOR_CHECK / NOT_INDEPENDENTLY_REVIEWED.

## Scientific provenance and scope

Continue R58 (source `research_notes/portable_direct/2026-11-20_x6_r58_joint_port_equality_tomography.md`, immutable commit `e2a762d7e251e666a0f840a65e08b652c034a883`) and its R57 collision-geometry definitions. Frozen scientific base: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`, P000 V5; current behavioural rules are separate. This is a conditional *multi-collision positive-BRC observer model*, not a proof of a native TRIADIC_CLOSURE_E evolution/rotation, physical heartbeat, permitted R/T operations or real cross-run reset. No spatial axis or independent research review is added.

Fix p>=1; common stable Port set J={0,...,p-1}; two named sources A,B; each experiment transfers one whole, already balanced three-force carrier of A through Port i, followed by B through Port j. A transfer is either successful or blocked as an indivisible source event; there is no signed cancellation. Exactly p ordered pairs are blocked and form the graph of a permutation `pi:J->J`: `C={(i,pi(i)):i in J}`. This is an extension of R58's one blocked pair, **not** the same hypothesis. A and B have positive Port-independent weights u and v. A successful AB pair contributes the explicit BRC branch weight uv. Reset produces an independent replicate of the same geometry; identities of Port labels across replicates are externally stable, and a cross-replicate equality predicate is observable. Such a reset/equality interface is an extra conditional hypothesis, not established by P000.

Put S_ij=1 if j!=pi(i), else 0, and P_ij=1 if j=pi(i), else 0, so S=J_p-P with J_p the all-ones array. This notation is finite BRC branch-count bookkeeping: every entry is a count of permitted named positive branches. It is not a physical propagator or an amplitude operator.

## R59.1: exact root and closed-chain branch masses

Define U=Z(A), V=Z(B), T=Z(AB) for one fresh experiment. Direct enumeration gives
```
U = p u,        V = p v,
T = p(p-1)uv,   UV-T = p uv,
p = UV/(UV-T),  uv = UV/p^2.
```
The last two formulas identify unknown positive weights' product and p from U,V,T, including p=1 (T=0).

For k>=1 take k **independent, reset** AB experiments with chosen Port pairs (i_t,j_t). In addition to their successful AB branches, retain the joint observer `j_t=i_(t+1)` for all t cyclically, including `j_k=i_1`. Let M_k be the total positive-BRC branch mass satisfying the predicates, and L_k=M_k/(uv)^k. Directly summing permitted named branch histories proves
```
L_k = sum_(i_1,...,i_k in J) S_(i_1,i_2) S_(i_2,i_3)... S_(i_k,i_1)
    = trace(S^k).
```
Every product is a product of indicator counts (0 or 1), not a phase, signed cancellation, native heartbeat transition or ordinary analytic propagation. The k-fold composition refers to the declared *observer of k reset trials*, not to k consecutive native time ticks.

## R59.2: reconstruct every permutation cycle, hence the simultaneous-renaming orbit

Let f_k be the number of fixed labels of pi^k and let c_d be the number of permutation cycles of length d. On the all-ones direction, S acts as p-1; on its zero-sum complement, S acts as -P. The two invariant subspaces give the exact finite counting identity
```
L_k = (p-1)^k + (-1)^k (f_k-1),
f_k = 1 + (-1)^k [L_k-(p-1)^k].
```
Equivalently, this follows by expanding the finite products (J_p-P)^k using J_p^2=p J_p and J_p P=P J_p=J_p, with no analytic spectral assumption. Because a cycle of length d contributes d fixed labels to pi^k precisely when d divides k,
```
f_k = sum_(d | k) d c_d,
c_n = [ f_n - sum_(d | n, d<n) d c_d ]/n, n=1,...,p.
```
Thus U,V,T and M_1,...,M_p determine p, uv and the entire integer cycle profile (c_1,...,c_p). Two permutations yield identical data exactly when they have the same cycle type, which is equivalent to their blocked incidence networks being related by a **single simultaneous Port relabelling**. For p=1, all M_k are zero and c_1=1; the theorem includes this boundary.

Important scope: different labelling groups change the equivalence question. Under independent A/B relabellings every permutation matching belongs to one orbit; the extra cyclic equality predicate is meaningful only under a common stable Port naming convention.

## R59.3: concrete two-step witness not contained in R58's totals or degree moments

At p=4 compare pi_4=(0 1 2 3) and pi_22=(0 1)(2 3), in cycle notation. Both have one forbidden pair in every A row and every B column, zero diagonal forbidden pairs, U=4u, V=4v, T=12uv, and W=4uv (R58's same-Port success mass). All row/column degree-moment observations agree. Yet the two-replicate cyclic-equality observer distinguishes them:
```
                 f_1  f_2    L_1   L_2           M_2
one 4-cycle        0    0      4     8     8(uv)^2
two 2-cycles       0    4      4    12    12(uv)^2
```
This is a strict BRC-positive, joint-provenance information-loss witness: the one-trial totals and all separate-side degree moments do not factor the two-trial cyclic observer. Its 4(uv)^2 mass gap is an *observer residual*, not physical energy or a new dimension.

## Verification

Companion verifier: `research_notes/portable_direct/x6_r59_matching_cycle_trace_verify.py`. Exact full enumeration of all 1!+...+7!=5913 labelled permutation matchings p=1,...,7; for each: construct 0/1 BRC success table, independently enumerate closed positive branch chains through integer array multiplication for k=1,...,p, verify the exact L_k/f_k identity, invert the divisor recurrence and compare with directly counted permutation cycles. Check U,V,T,p recovery with u=2,v=3 and the explicit p=4 witness. All assertions passed in local author computation. The general p result is the finite counting proof above; exhaustive p<=7 tests are not an infinite proof. No independent review, native port/Cell lift, empirical validation or formal Result is asserted.

## Frontier

The next discriminating problem is whether the frozen P000 X6 native rotation/event interface admits a repeatable *same-incidence* reset and a cross-source/replicate Port-equality observer. Without that proof, the R59 moments are conditional tomography only. For an arbitrary blocked relation C (not necessarily a perfect matching), its success table S=J_p-1_C retains positive path moments, but closed-chain trace data need not determine the directed graph under simultaneous relabelling. Identify a minimal stronger observer (typed mixed-word trace family or a finite counterexample) before any claimed general graph classification. Preserve source names, Cell incidence, relation orientation, branch multiplicities and reset provenance.
