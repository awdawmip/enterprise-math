# R762AU — Integral ten-probe reconstruction of the V29 four-port BRC score contrasts

Date: 2026-11-15. Researcher provenance: EM-X6-3050F6. Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS / publication TP2-8B7E13C5904A2D6F1142. Status: AUTHOR EXACT PROOF AND EXECUTED INTEGER CHECKER; NOT_REVIEWED. Frozen scientific input remains enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. This is a **conditional V23/V25/V29 observer theorem**; no native P000 three-force event is asserted.

## 1. Exact question

R762AT repaired the cumulative three-PASS ledger and proved a sharp deterministic active-triad threshold. That argument computes V25 edge-score exponents from the four-port contrast (u,Omega). Does that score observer discard any of these ten signed coordinates? What is the smallest fixed collection of direct score-difference queries that reconstructs the entire contrast without a nonlinear encoding assumption?

We answer both questions exactly. More surprisingly, even adaptive selection of fewer than ten such queries cannot recover every admissible contrast when each query is a nondestructive observation of one unchanged Cell ledger. A ten-query unimodular certificate gives an exact integral reconstruction and an operation-safe state for the declared V25/V29 feedback language.

## 2. Source, domain, typing and V23 coding

One declared Cell x has four named V29 source ports 0,1,2,3. Its native ledger is (M,Rin,Rout) with M in N0^(4x4), Rin,Rout in N0^4. Define

    Omega_ab = M_ab - M_ba,
    u_a = sum_b Omega_ab + Rin_a - Rout_a.

The ten signed contrast coordinates are ordered

    theta = (u0,u1,u2,u3,Omega01,Omega02,Omega03,Omega12,Omega13,Omega23) in Z^10.

No positivity is imposed on theta: the stored native counts are nonnegative; the contrasts are derived signed integers. Four V23 perfect matchings on the six labeled X6 axes 0,...,5 are

    ((0,1),(2,3),(4,5)),
    ((0,2),(1,4),(3,5)),
    ((0,3),(1,5),(2,4)),
    ((0,4),(1,3),(2,5)).

For each active triad S (one of 20 three-subsets), the four-field code c(S) has entry zero unless S chooses exactly one endpoint from each pair of a matching; then the entry is (-1)^(number of chosen second endpoints). This is the declared V23/V25 code reused by R762AT. It is not a new spatial axis or a native third-force law.

For any directed Johnson edge S -> T, with |S intersect T|=2, define the signed V25 exponent

    Phi_theta(S,T) = u dot c(T) + c(S)^T Omega c(T).

Under an explicitly chosen positive-rational BRC parameter rho>1 the branch weight is rho^Phi. Define the **exact exponent-difference query**

    D_theta(S;T,U) = Phi_theta(S,T) - Phi_theta(S,U),

where T and U are distinct neighbors of the *same* active triad S. This is a nondestructive query against one fixed underlying theta. Observing an exact ratio rho^D is equivalent to observing D in this symbolic integer-exponent family; merely knowing the sign of D is strictly weaker.

There are 20 active triads, 9 outgoing neighbors of each, 180 directed scores, and 160 canonical differences if the lexicographically first neighbor serves as reference.

## 3. Theorem AU1 — a unimodular ten-comparison basis

**Claim.** Exactly ten fixed direct V25 exponent-difference queries suffice to reconstruct every theta in Z^10 by integer linear formulas. No deterministic adaptive interrogation using nine or fewer such exact difference queries can reconstruct all admissible theta from an unchanged ledger.

For i<j, write O_ij for the independent Omega coordinate. Expanding Phi gives a row vector for each query:

    r(S;T,U) =
      (c(T)-c(U),
       {c_i(S)(c_j(T)-c_j(U)) -
        c_j(S)(c_i(T)-c_i(U))}_{i<j}),

and D_theta = r dot theta.

The following list (S;T,U) supplies the ten rows, all on genuine directed Johnson edges:

    1  145;125,014
    2  013;014,012
    3  023;034,012
    4  024;045,012
    5  345;135,034
    6  012;025,013
    7  025;245,012
    8  245;125,024
    9  034;234,013
    10 245;345,024

Using the above coordinate order, their integer matrix A is

     1   1   1   0   0   0  -1   0  -1  -1
     0   0  -2  -1   0   0   0  -2  -1   0
    -1  -1  -1  -1   0   0  -1   0  -1  -1
     0   1   0  -1   1   0  -1   0   0   0
     0   1   0   0   0   0   0   1   1   0
    -1  -1  -1   0   0   1   1   1   1   1
     0  -1  -1  -1   1   1   1  -1   0   1
     0   1   0   0   0   0   0   0   0   0
     0   0   0   1   0   0  -1   0  -1   0
    -1   0  -1  -1  -1   0   0   1   1   0.

Its **exact integer determinant is -1**. The included independent, self-contained JavaScript verifier constructs each row from the four matchings and checks this determinant with BigInt Bareiss elimination, with exact divisibility at each elimination step. Thus A belongs to GL(10,Z) and

    theta = A^(-1) d,     d=(D_1,...,D_10).

All 180 scores and all 160 canonical within-S differences are therefore integer-linear functions of the ten readings, since all their coefficient rows are integers. This is an *integral* observation coordinate, not merely invertibility over R or Q.

**Lower bound, including adaptive queries.** Every theta in Z^10 is realizable by a legal nonnegative V29 ledger: take for each a<b

    M_ab=max(Omega_ab,0), M_ba=max(-Omega_ab,0), M_aa=0.

Let q=Omega 1. Then take

    Rin_a=max(u_a-q_a,0), Rout_a=max(q_a-u_a,0).

These are nonnegative integer count arrays, and their V29 reconstructed contrast is exactly theta. For any adaptive deterministic strategy promising at most nine such queries, run it against theta=0; its observed replies are all zero, thereby fixing at most nine integer rows. Their common rational nullspace has positive dimension, hence contains nonzero integral z. Both theta=0 and theta=z are realizable, and the strategy observes the identical all-zero transcript and chooses the same queries on both. It cannot identify both. This proves the sharp ten-query lower bound within the declared direct comparison interface. QED.

## 4. Theorem AU2 — exact future-observer descent for the specified event language

A V29 primitive PASS(a->b) changes theta by a deterministic integer vector:
- delta u = e_a-e_b;
- delta Omega_ab = +1 for the directed pair a->b, with antisymmetry.

A matched inter-Cell TRANSFER updates the appropriate local boundary count: the exit Cell has delta u=-e_a, the entry Cell has delta u=+e_b, and both have delta Omega=0. All these increments depend only on the typed event label, not on the hidden cumulative counts.

Therefore the ten-dimensional probe state d=A theta evolves under an event label e by

    d_next = d + A delta_theta(e).

Suppose that every permitted future event, all guards and scheduler decisions for this single-Cell subsystem depend on the underlying ledger *only* through these exact score differences (equivalently d) and the declared external event label/context. Then two ledgers with the same d have the same allowed labeled continuations and the same future d readouts by induction on any event word, including a scheduler that chooses events adaptively using previous score results. This proves an exact infinite-horizon operation-safe quotient for that typed future language. The ten-coordinate lattice is a sufficient and minimal direct difference-probe representation of the V29 contrast under these assumptions.

The conditional factorization matters: a future test of absolute M_ab, source provenance, window age, inventory or path order requires its own retained coordinates. No such larger future operation is presumed to factor through d. A sign-only ranking observer also fails to reconstruct theta: theta and 2 theta have identical one-stage comparison signs and ties for any nonzero theta. This explains why using only an argmax choice is not the same as using the exact BRC exponent differences.

## 5. Concrete R762AT transport to the new coordinates

For R762AT's repaired four-port PF-10 ledger, theta_n has

    u=(-2,-4,-3,10),
    (Omega01,Omega02,Omega03,Omega12,Omega13,Omega23)=(n,-n,0,n,0,0).

The ten exact readings at n=0 are

    d_0=(-9,-4,-1,-14,-4,9,-3,-4,10,-5),

and after one complete three-PASS macro

    d_1=(-9,-6,-1,-13,-3,9,-4,-4,10,-5).

Thus the exact per-macro increment is

    d_(n+1)-d_n=(0,-2,0,1,1,0,-1,0,0,0).

The reconstructed theta_n is unique for all n>=0. These values link AU1 to the previously proved R762AT sharp n>=15 selector theorem without recomputing its 160 inequality certificate or claiming that an actual native scheduler has been established.

## 6. Reproducible evidence and limits

The shipped self-contained JavaScript checker (standard syntax; BigInt exact arithmetic) computes:
- all 20 V23 codewords, all 180 directed Johnson edges and 160 canonical difference rows;
- the ten explicit rows, their determinant -1 by integer fraction-free elimination and integer Cramer decoding;
- 53 exact full ledger-realization plus decoding witnesses, including the R762AT baseline and one-macro count;
- all 12 directed four-port PASS labels and 8 local TRANSFER boundary labels, including *independent expected V29 delta vectors*;
- the exact d_0 and d_1 and the increment vector above.

Its JSON is generated directly from that executing checker, with declared method and input pins. The ten-row determinant is an exact finite certificate that establishes the all-integer all-theta result by the proof in section 3; sample-state checks are regression evidence, not the reason a universal claim is inferred.

**Scope and next dependency.** This solves a score-observer problem for the existing conditional V23/V25/V29 architecture. P000 remains six signed native spatial axes, pairwise PERP_E at the native defined 120 degrees, and primitive stable force arity three. The hard task remains: derive a genuine typed Cell/Link/Port TRIADIC_CLOSURE_E update and identify the legitimate V17 frame/source transport and V39 based-loop readout. Test whether those actual event guards and future observers factor through this ten-dimensional comparison lattice or require a provenance/loop repair coordinate. That is the next discriminating native bridge; the present theorem supplies a falsifiable exact rank and update baseline.

## Sources and provenance

- Frozen Task RS-X6-TRIADIC-CLOSURE-DYNAMICS and P000 @ enterprise-math a72226e2430ffa4786321ac86e7f0c599d5f0389.
- enterprise-math research_notes/X6_NETWORK_EVENT_LEDGER_AND_CONTRAST_TRANSDUCER_V29_20260906.md (V29 exact PASS/TRANSFER signed-count transducer).
- enterprise-math research_notes/X6_ACTIVE_TRIAD_HOLONOMY_CONTROL_V17_20260906.md (conditional active-triad frame transport).
- R762AT author proof and executed BRC code @ 892e804f8843f7b23bcfc383bd711e599b577819 (V23 code, V25 weighted score, corrected cumulative ledger and sharp odd six-cycle).
- User-authorized account ACTIVE worldview and joint observer-preservation constraint; local exact contrast findings do not alter their canonical definitions.

Formal Source PROGRESS/Result and independent Driver review are separate native operations; an author Draft PR alone is not their equivalent.
