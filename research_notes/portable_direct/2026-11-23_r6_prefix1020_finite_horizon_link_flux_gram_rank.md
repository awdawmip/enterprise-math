# PREFIX-1020 — Exact finite-horizon Link-flux Gram reconstruction and sharp 2H linear rank

Date: 2026-11-23 (Asia/Shanghai). Scientific status: **AUTHOR_EXACT_ALGEBRAIC_PROOF / INTEGER_BRC_GRAM_CHECK_H1_TO_H5 / NOT_REVIEWED**.

## Frozen scientific input and typed scope

Continue PREFIX-1019 (`bd605a1db6084edcec02b340181c9eebfcaa18c9:research_notes/portable_direct/2026-11-23_r6_prefix1019_brc_link_parseval_finite_horizon_obstruction.md`). Scientific pin: P000 V5 `f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json` and the Stage46 candidate **signed** twelve-direction BRC kernel. This note changes no P000 ontology, candidate admission, task ownership or fixed-input pin.

Native X6 signed chart Cells form the chosen-anchor torsor over ℤ^6; there are twelve signed primitive directions ±e_j, and twelve named incoming-neighbour ports h. The native model step index t denotes ordered BRC updates (not a claim about calibrated physical heartbeat time). A packet v(x,h) is finite-support over ℝ or ℂ; signed integers suffice for the exact checks.

At each Cell, outgoing direction d has numerator f_v(x,d)=∑_h (1-6[h=d])v(x,h); the incoming port at the next Cell x+d is -d. Write W=J_12-6I_12 and let S be this shift-and-port-relabeling permutation. The unrestricted step T_0=SW, with T_0*T_0=36I. Let E select precisely the two outgoing joint fibres (0,+e1) and (e1,-e1), and let T=(I-EE*)T_0 denote absorption on the two-way Link {0,e1}. Define the **oriented coherent boundary-flux map** C=E*T_0:
C(v)=(Φ_+(v),Φ_-(v))=(f_v(0,+e1),f_v(e1,-e1)).
Here * denotes the transpose / Hermitian adjoint on the finite-support carrier; all coherent sums precede squaring.

## Theorem 1020.A — exact finite-horizon Gram repair

For each integer H≥1 define the finite-horizon flux observation
Γ_H v = (Cv, CTv, ..., CT^{H-1}v) ∈ ℂ^{2H}.
For every finite-support packet v and every integer 0≤t≤H,

```text
||T^t v||^2
 = 36^t ||v||^2
   - sum_{s=0}^{t-1} 36^(t-1-s) (|Phi_+(T^s v)|^2+|Phi_-(T^s v)|^2).
```

In operator form, for each t,
```text
(T^t)* T^t
 = 36^t I - sum_{s=0}^{t-1} 36^(t-1-s) (T^s)* C* C T^s.
```

Thus the initial coherent squared norm and the **exact 2H signed/complex channel amplitudes** reconstruct every intermediate all-grade coherent squared norm through time H. The positive-semidefinite boundary-loss Gram operator
K_H = Γ_H* Γ_H = ∑_{s=0}^{H-1}(T^s)*C*C T^s
has finite rank.

**Proof.** From PREFIX-1019 or directly W*W=36I, and the orthogonal mask P=I-EE*, one has
T*T=T_0*PT_0=36I-C*C.
Replace v by T^sv; take squared norms; multiply by 36^(t-1-s) and telescope from s=0 to t-1. Polarization gives the operator equality, and K_H is a sum of 2H rank-one nonnegative outer products. QED.

## Theorem 1020.B — exact rank(K_H)=rank(Γ_H)=2H

The preceding rank upper bound is **sharp for every H≥1**. More strongly, Γ_H restricted to a 2H-dimensional explicitly exhibited integer unit-packet subspace has determinant +1 in the following natural ordering.

For s=0,...,H-1, take two legal unit packets
```text
v_{+,s} = delta_(s e2, -e1)
v_{-,s} = delta_(e1+s e2, +e1).
```

Order their columns by increasing s and + before -, and order the 2H rows of Γ_H by increasing t and + before -. Then:

* At all t<s, C T^t v_{+,s}=C T^t v_{-,s}=0. The closest Link outgoing starting Cell is exactly s native e2-steps away and the opposite Link endpoint requires at least s+1 steps.
* At t=s, `C T^s v_{+,s}=(1,0)` and `C T^s v_{-,s}=(0,1)`. The only path reaching the designated Link starting Cell in s steps is (-e2)^s; its intermediate BRC weights are +1 and its final outgoing prohibited-direction weight is +1. No opposite-channel starting Cell can be reached in s steps.
* Therefore the resulting 2H-by-2H matrix is lower block triangular, with an identity 2-by-2 block on every diagonal: determinant +1.

The 2H flux coordinate functionals are linearly independent. Since Γ_H has precisely 2H rows, rank(Γ_H)=2H. Since rank(A*A)=rank(A) for a finite-rank operator, rank(K_H)=2H. QED.

**Minimality scope.** For the specific future observable `(Φ_+(T^s v),Φ_-(T^s v))_{s=0}^{H-1}`, any exact *linear* intermediate compression through which this oriented flux vector factors needs dimension at least 2H. This proves linear observable-rank minimality, not an unconditional information-bit lower bound or minimal nonlinear state for squared-mass-only readout. The raw Cell--port carrier remains the authoritative state for future operations not included in the declared observer.

**Finite-horizon frontier.** Each increase H→H+1 adds two independent oriented channel directions, even though all squared norms through each finite horizon admit a compact exact finite-horizon Gram repair. No fixed finite-rank linear flux observer suffices for every H on unrestricted finite-support X6 packets. This strengthens PREFIX-1019's delayed distinguishability by computing a sharp rank, without reclassifying its result or changing the fixed-anchor exact-grade k=1 claims of PREFIX-1014–1018.

## Executed exact verification

The standalone Python checker `PREFIX1020_R6_LINK_GRAM_RANK_CHECK.py` implements all 12 named directions, native signed integer weights W(h,d)=1-6[h=d], coherent Cell--port collection, and the two specific deleted channels. For H=1,2,3,4,5 it verifies **every** entry of the lower-block-triangular witness matrix, including the identity diagonal, and tests the full bilinear Gram identity across every pair of the 2H witness unit packets, using exact Python integers. It also verifies one independent three-packet integer superposition through six steps.

| H | Proven exact rank 2H | Largest nonzero Cell-port state count after H updates (test) | Gram pairwise test |
|---:|---:|---:|---|
| 1 | 2 | 11 | PASS |
| 2 | 4 | 143 | PASS |
| 3 | 6 | 864 | PASS |
| 4 | 8 | 3,647 | PASS |
| 5 | 10 | 11,819 | PASS |

For the additional coherent input the initial squared norm is 14; first two flux channels are (2,3); next squared norm is 491=36×14-2²-3². Its next norms are 17,675, 628,024, 22,603,423, 811,655,564 and 29,210,029,100; each step satisfies exact Link-flux dissipation.

The proof establishes every integer H≥1; numerical execution only covers H=1..5 and the explicit six-step test. No independent mathematical review or formal Result admission occurred.

## Provenance and next scientific unit

Historical R6 contributor: `EM-DIRECT-FBEA5D`; Activity `RA-3FB2D033BE6048D8712FF056` (provenance only; requires its own lawful association). Original SID `MCP-45ad6d29cd534c1aad25595a72e3c532`, not an inferred live CLAIM. This scientific note is a portable Source artifact; GitHub publication does not grant research execution, task ownership, Result/Review or Foundation authority.

Next: (1) inspect how much of the sharp 2H boundary rank remains reachable from the frozen fixed-anchor and exactly-one-negative-step input family; (2) investigate the smallest *quadratic* state specifically for end-port coherent squared masses under one or several future updates, distinguishing that target from full oriented flux. The mother question B_fix,odd(32) in {19,20} remains open.
