# R5 — Two monotone named Set commands force an eleven-state controller at horizon one

Date: 2026-11-16. Scientific input pin: 435e77af0d180eac32bd1f9c4c464bc4010b7551.
Scope: auxiliary genuine-source-labelled **six-cycle** with redundancy slack 2, not an assertion about the full native X6 dynamics. Source provenance: the inherited common genuine-source-library replacement lemma, the single-control 10-state theorem at 1da48c5497a18405d68b27e92c0ba7cf6426a051, and the two-control 11-state coherent-cube construction at edcceb086854d269acf0f7e288da54ddb7393d25. Author-side evidence: **AUTHOR_PROVED / EXACT_FINITE_EXHAUSTIVE / NOT_REVIEWED**.

## The exact statement

Let X={0,...,63}. The bit u_i represents indexed auxiliary coordinate i (indices modulo 6), and

q(u) = Σ_{i=0}^{5} u_i u_{(i+1) mod 6}.

An output source label r may serve a raw state u precisely when

G(r,u) = [u & ~r = 0] ∧ [0 ≤ q(r)-q(u) ≤ 2].

Let S_i⁺(u)=u | (1<<i) be the **positive-only** named setting command for bit i. A deterministic controller has m output states labelled by genuine source centres r_j; its internal transition for each allowed command is any map on the m states. Every raw u may initialize any nonempty set of compatible controller states, but one selected initial state must produce a compatible output after every command word of length at most H. The transition maps are not assumed idempotent, absorbing, or commuting.

Let N_H(A) be the minimum state count for command alphabet A through horizon H. Then

~~~text
N_H({S_0⁺}) = N_H({S_1⁺}) = 10   for all H >= 0;
N_0({S_0⁺, S_1⁺}) = 10;
N_H({S_0⁺, S_1⁺}) = 11          for all H >= 1.
~~~

Thus a one-step state-count jump already occurs with only **two monotone, idempotent and commuting commands at the raw-state level**. Neither lowering a bit nor alternating opposite assignments is necessary. Each single positive command separately admits ten control states.

## Pairwise obstruction proof: zero transition-table enumeration

The exact static-cover recurrence branches on an uncovered raw state and every undominated source centre that can serve it. The 64 masks reduce to **22 nondominated masks**; complete search of covers of size at most ten yields **zero** covers of size at most nine and **116** distinct ten-centre covers.

Fix one such ten-centre set C. For each r in C, define its mandatory unique raw inputs

F_r={u : G(r,u) and (for every z in C other than r, not G(z,u))}.

All inputs in F_r must initialize the output state r, since no alternative output can serve them. Consequently any command S_i⁺ must map controller state r to a single target source centre z in C satisfying **all** images of F_r.

The 116 covers split into two exactly exhaustive cases:

1. **101 covers: forced-pair incompatibility.** There exist r in C, i in {0,1}, and two inputs x,y in F_r such that no z in C covers both S_i⁺(x) and S_i⁺(y). The transition from r under S_i⁺ is therefore impossible. Every failure has a **two-input certificate**; no larger simultaneous belief is needed.
2. **15 covers: the same raw input 36 defeats every initialization.** For every r in C satisfying G(r,36), there are a command S_i⁺ and a unique mandatory anchor v in F_r such that no centre z in C covers both S_i⁺(36) and S_i⁺(v). If raw state 36 were initialized in state r, the successor would have to serve both images, which is impossible. Every candidate r for initializing 36 is eliminated. Across the 15 covers, the certificate contains **40 one-anchor rows**, all checked exactly.

The second case is a *uniform distinguished-state obstruction*: **36 (binary 100100) suffices for all 15 residual source covers**. For example, when C=(15,27,43,45,53,54,55,61,62,63), the candidate label r=45 has mandatory input v=44; under S_1⁺, the two images are 38 and 46, and no label in C serves both. The other candidate labels for 36 are separately eliminated in the certificate.

Hence every ten-state controller fails the one-step test, regardless of initialization overlap or internal transitions. Since a controller with fewer than ten states cannot cover the initial raw universe, this proves N_1({S_0⁺,S_1⁺}) >= 11, and monotonicity in horizon extends the bound to H>=1.

For the matching bound, reuse the earlier **eleven-state coherent-cube genuine-source witness** for all four assignments to bits 0 and 1; it works under the two positive commands for arbitrarily long words. For a singleton positive command, reuse the verified **ten-state single-bit** genuine-source controller for both assignments to bit 0; cyclic rotation yields bit 1. Both witnesses are reconstructed and checked on all relevant 64 raw states by the accompanying verifier. Their matching lower bound ten is the static-cover lower bound above.

## Reproducibility and scope

VERIFY_R5_TWO_RAISES_PAIRWISE.py is a Python 3 standard-library exhaustive checker. It generates EXACT_R5_TWO_RAISES_PAIRWISE_EVIDENCE.json, including the **116 exact centre sets and their complete pairwise obstruction certificates**. Its actual execution returned PASS_R5_TWO_RAISES_PAIRWISE_HORIZON_ONE: 29,525 static-cover recursion calls, 101 forced-pair covers, 15 distinguished-36 covers, 40 anchor rows, zero static covers below ten, and successful ten-/eleven-state upper checks.

All computations are finite Boolean/integer tests over 64 raw states and 22 undominated centre masks; no floating point, MILP, sampled trajectories or independent review claim is involved. The genuine-source replacement lemma is an inherited, explicitly scoped dependency for upgrading the centre search to arbitrary admissible output libraries. This auxiliary model does not modify P000, the six-dimensional primitive spatial axioms, or the three-dimensional research-slice semantics.

**Next research unit:** seek a human-short structural characterization of which source-cover cores force the two-command jump, then test whether analogous pairwise certificates exist for seven-node and larger rings. Distinguish the finite indexed source observer from any proposed native X6 embedding.
