# PREFIX-571 — Exact gate-count Newton calculus and unbounded diagonal e-positivity

Date: 2026-11-08 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED.
Frozen scientific pin: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Direct predecessor: PREFIX-570, commit 84aff72cfcdfe49d454372c69a8ce3c9978d2743.
Reusable original BRC source: PREFIX565_positive_marginal_certificate.py (Git blob 7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41) and PREFIX566_gate_quotient_certificate.py (blob 7b6613193847e4123cd0ac11107eb9b9c70290c8). Full extended executable test and earlier positive-factor scan are in the accompanying PREFIX571 evidence package.

## Model and exact scope

Keep the frozen four-STAR six-axis X6 native ordered positive-BRC branches, 96 ports, six actions per port. Declare the observation q1=q2=q3=q4=1, x=q5, y=q6, gate z, and the nine allowed roots with r5=r6=0. The 37-class weighted observer quotient preserves all future iterated transitions and terminal joint (x,y,z) path counts in that declared scope. The original native paths and 6-axis state remain the source, not an erased ontology. At the 32 ports fixed by axis-5/6 exchange (11 quotient classes I={0,2,5,7,14,15,18,25,27,31,33}), the observed count is symmetric in x,y. Set u=x+y and v=xy.

Let δ_i be the shortest depth with a gate, with i:δ_i given by
0:4, 2:5, 5:4, 7:3, 14:5, 15:1, 18:4, 25:3, 27:4, 31:3, 33:2.
For k≥1 and excess s≥0 define

H_(i,k,s)(u,v) = [z^k] F_(i, δ_i+4(k−1)+s)(x,y,z).

The depth changes by exactly four original native actions when k increments at fixed excess s. Define ρ=4+8u and the weighted gate-count difference

Δ_ρ H_(i,k,s) = H_(i,k+1,s) − ρ H_(i,k,s).

## Theorem A — all-excess exact finite order

For each specified port, EVERY excess s≥0, gate count k≥1, and integer m≥0,

Δ_ρ^m H_(i,k,s) = 0 whenever 2m > s.

Thus for fixed excess s, the gate-count sequence satisfies the exact recurrence

sum_(j=0)^r (−1)^(r−j) binom(r,j) ρ^(r−j) H_(i,k+j,s) = 0,
r=floor(s/2)+1, for every k≥1.

There is an exact finite Newton representation

H_(i,k,s) = sum_(j=0)^min(k−1,floor(s/2))
  binom(k−1,j) ρ^(k−1−j) G_(i,j,s),

G_(i,j,s) = [t^(s−2j)] a_i(t)b(t)γ(t)^j.

Only floor(s/2)+1 independent Newton coefficients are needed at each fixed excess to reconstruct arbitrarily large gate counts. This is an algebraic representation, with performance and coefficient bit-cost still to measure.

## Theorem B — positive diagonal finite differences for unbounded excess

For EVERY k≥1, EVERY m≥0, and every integer 0≤q≤254,

Δ_ρ^m H_(i,k,2m+q) belongs to Z_≥0[u,v].

Because m is unbounded, this yields explicit positive difference families at arbitrarily large excess 2m+q. This statement concerns the m-th weighted difference; the general e-positivity of each H for arbitrary excess is still the mother question.

For the sharp diagonal q=0, for all m,k without reliance on any finite coefficient-sign scan:

Δ_ρ^m H_(i,k,2m)
 = a_i(0) (4+8u)^(k−1) (80u²+128v)^m,

where a_i(0) is the exact positive first-gate polynomial determined by the frozen native action counts.

## Proof

Write the 37-class weighted transition as N+z U e_5^T. There are precisely three gated source classes 4, 15 and 17 with unit coefficients, every gate points to class 5, and gated edges carry no x or y factor. Put R(t)=(I−tN)^(-1), A_i(t)=[R(t)U]_i, K(t)=[R(t)U]_5, B(t)=[R(t)1]_5. Exact unique gate-cutting of the ordered native paths yields, for every k≥1,

[z^k]sum_(d≥0)F_(i,d) t^d = t^k A_i(t) K(t)^(k−1) B(t).

The orders are ord(A_i)=δ_i−1, ord(K)=3, ord(B)=0. Define a_i=t^(−δ_i+1)A_i, c=t^(−3)K and b=B. Then

sum_(s≥0)H_(i,k,s)t^s = a_i(t)b(t)c(t)^(k−1).  (1)

The complete undirected graph obtained from all ungated edges of N admits a bipartite 2-coloring; all such edges change color. The target state 5 is opposite to all U-source states 4,15,17. Hence every N-path from 5 to a U-source has odd length. K(t) has only odd t powers. Its first exact BRC native coefficients are K_0=K_1=K_2=0, K_3=4+8u, K_4=0, K_5=80u²+128v, K_6=0. Thus

c(t)=ρ+t²γ(t), with γ(t) in Z[u,v][[t]] and γ(0)=80u²+128v.  (2)

Applying Δ_ρ to (1) multiplies the right side by c(t)−ρ=t²γ(t). For every m≥0,

Δ_ρ^m H_(i,k,s) = [t^(s−2m)] a_i(t)b(t)c(t)^(k−1)γ(t)^m.  (3)

The coefficient is zero when its index is negative; this proves Theorem A and the r-order recurrence. Expanding (ρ+t²γ)^(k−1) proves the Newton formula above, for all s,k.

PREFIX-570 has an independently published exhaustive exact INTEGER certificate for nonnegative Z[u,v] coefficients of a_i(t), b(t), and c(t) in all degrees 0..256 for all 11 fixed observation classes. The original compact certificate was re-executed in this run, yielding ALL_CHECKS_PASS, 1,817,330 nonzero coefficient positions, factor scan 0..260. Since γ_j=c_(j+2), this certifies γ_j≥0 for j=0..254. Taking t^q in (3), for 0≤q≤254, is a product of only these verified nonnegative factors, regardless of k or m, proving Theorem B. At q=0 only their constant coefficients are used, giving the sharp formula without the finite sign lemma. For s≤256 the Newton coefficients G_(i,j,s) are likewise nonnegative: j=0 uses the a_i,b factors to s, while j≥1 uses γ through s−2j≤254. Hence the initial 257 excess layers possess a finite *positive Newton basis* for gate-count continuation.

No analytical convergence, floating point, approximation, classical π/trigonometry/propagator, or change to the frozen native BRC input enters this argument.

## Actual reproducibility evidence

An extended executed Python certificate using exactly the pinned native BRC action implementation rebuilt the 37-state quotient, verified the entire ungated transition graph bipartition and the source/target parity, verified the six leading K coefficients exactly, and compared independent gate-aware direct propagation against renewal convolution on three fixed classes (0,15,33), gates 1..4 and excess 0..6: 84 exact full-integer polynomial comparisons covering 523 nonzero coefficient positions, action length 0..23; 60 additional exact finite-difference vanishing checks. All returned ALL_CHECKS_PASS. The separate re-execution of the prior complete factor scan again returned ALL_CHECKS_PASS. Attached source code/result data are contained in PREFIX571_FULL_RESEARCH_EVIDENCE.zip.

The mathematical quantifiers for Theorem A come from the formal path identity and bipartite graph proof, not from finite tests. Theorem B combines that identity with the precisely bounded 256-degree factor sign certificate.

## Next question / discrimination

The open mother question is H_(i,k,s)∈Z_≥0[u,v] for all k≥1 and *all* s≥0, rather than only the previously checked finite band. Search an exact positive cone / nonnegative rational generating-function presentation for a_i,b,γ across all degrees. If any factor first becomes negative in the elementary basis, test the full gate-cut product before inferring any sign failure of H. As a separate engineering experiment, compare the finite Newton basis with direct 37-state gate-truncated propagation for batch multi-k queries, including input mapping, full observer recovery, integer bit lengths, RSS and serialization.

## Control

GitHub authenticated login awdawmip has repo push permission. An attempted native EM session_start reported FAILED/OSError and task list read reported WAITING_RESOURCE/EVENT_COLLECTION_IO. No live native Researcher-ID, Owner, CLAIM, formal Result or independent Review was established. This is independent author research stored under the established portable_direct notes, not scientific admission.
