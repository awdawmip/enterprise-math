# Stage467-B — full ternary X6 initial-observer fibers: exact Q-only future classes and positive BRC transfer

Date: 2026-11-06. Author-side research continuation of Stage466-B, independently scoped from formal Task ownership. Frozen scientific pins: GLOBAL `bf84bd7c61a2444b59b1da96be57df0e9ae47e53`, EM `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`, original P000 blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`. Read current rules separately. Stage466-B source commit `6bc9070ed113f2b84b77226de5149ecac2f9477c`. Classification: author-side proved statement + exact integer execution; independent review pending.

## Model and exact observer

Choose the **original** ternary alphabet Σ={A=+E1,B=+E2,C=+E3}, a typed subset of the 12 signed X6 directions. Two distinct original sources P,Q have lengths 2≤m<n and fixed first letter A in each. Initial observer Φ(P,Q) comprises both lengths, two complete signed six-axis displacements, two full **directed 12×12 adjacent-direction matrices**, and K(P,Q)=Σ_{i≤m}[P_i=Q_i]. We fix any nonempty initial observer fiber F=Φ^{-1}(φ). All future APPEND_Q(u) labels u range over the entire signed 12-direction alphabet, even though original letters are ternary. Only Q may POP (budget h, with 0≤h≤n) and APPEND (arbitrary finite positive budget s≥1); P remains unchanged. POP of an appended letter spends the same h budget. Future equivalence means equality of the complete **labeled intermediate-observation tree** for all legal operations.

## Theorem 467.1 — exact full-fiber distinguishing tail

Set t=max(1,n−h) and define the ordered *tail emissions*

Λ_h(P,Q) = ( (Q_t), (P_{t+1},Q_{t+1}) if t+1≤m else (Q_{t+1}), …, (P_m,Q_m) if t<m, (Q_{m+1}), …, (Q_n) ),

with each position i>t and ≤m contributing the ordered pair (P_i,Q_i), and positions i>m a Q singleton. For h=0 the label is the singleton Q_n. Then for every fixed φ and finite s≥1,

**H ≡_{h,s} H′ if and only if Λ_h(H)=Λ_h(H′).**

This statement is an exact sufficient and distinguishing label on F; not every coordinate is independent within F.

**Necessity.** After h Q POPs the remaining original Q has length t (or 1 if h=n). Its final direction Q_t is recoverable from the current initial-A directed-edge imbalance: out(x)−in(x)=[x=A]−[x=last]. For every j>t, the Q POP chain reveals Q_j directly from the six-dimensional endpoint delta (the ternary native direction is injective as a signed vector). For every t<j≤m, execute n−j+1≤h original-Q POPs, so Q has length j−1, and compare APPEND_Q(u) for each of the 12 u. Its K change is exactly [P_j=u]. Therefore the observed labeled future tree identifies every emission in Λ_h. (When h=0, Q_n is already determined by the original observer.)

**Sufficiency.** The original complete observer and Q_t,…,Q_n reconstruct every reachable original-Q prefix observer down to length t: reverse each known removed direction and directed boundary edge. The K value of the Q prefix of length k≥t is K(P,Q) minus the matching terms at indices k<j≤m; all those j satisfy j>t, hence P_j,Q_j are in Λ_h. When APPEND_Q extends any retained original-Q prefix of length k≥t, the appended positions have indices j>k≥t, where the original P letter, if any, is in Λ_h; appended Q letters and Q boundary edges are action-known. Every future state consists of such a prefix and an action-known appended suffix, including paths that POP some appended letters. Thus the entire intermediate-observation tree factors through (φ,Λ_h).

The cut has **one asymmetric boundary column**: Q_t is observable, but P_t need not be. Placing P_t in the visible key would refine some fibers unnecessarily. At h=1, P=AAA with Q=AABA versus ABAA (both original full observers equal) already illustrates why only retaining Q_n is insufficient: after one POP the penultimate Q direction is exposed through the directed-edge change. This repairs the off-by-one issue in a naive common-tail cut.

## Theorem 467.2 — exact positive-branch BRC transfer, support and rank

For Σ={+E1,+E2,+E3}, use the additive observer state

C=(N_P∈ℕ³,N_Q∈ℕ³,E_P∈ℕ^{3×3},E_Q∈ℕ^{3×3},K∈ℕ),

which has 25 nonnegative integer counters. This is exactly Φ on the declared original alphabet: N_P,N_Q reconstruct the signed X6 endpoints, E_P,E_Q embed in 12×12 directed matrices, and lengths are fixed. The transfer retains source identities P and Q; a branch represents one ordered original history with unit positive weight. Alternative composition adds source-distinct population; serial composition propagates the path and its observer increments. The Boolean-support projection [mass>0] is taken **only at the completed class**, never at a hidden branching point. This is the unit-weight positive-branch specialization of the project's weighted-BRC substrate, not phase/sign cancellation.

Build a hidden-prefix positive-integer transfer H through columns 1,…,t−1 (both letters where i≤m, only Q where i>m). At position t, also consume hidden P_t if t≤m, preserving its exact direction and P-last boundary; Q_t remains visible. States retain C and last P/Q letters and P_t. All weights are the exact numbers of hidden source pairs leading to the state.

Now scan visible emissions Λ_h chronologically. Each emitted pair/singleton uniquely advances a *deterministic* additive visible state V: its own counts, internal directed edges and K for matched visible pairs, first visible letters and last letters. At the terminal, for each of at most 3³ hidden bridge assignments, add (i) the P boundary edge from hidden P_t to first visible P if present, (ii) Q boundary edge from hidden Q_{t−1} to visible Q_t if present, and (iii) the match [P_t=Q_t] if t≤m. Let

M(λ) = Σ_{hidden boundary states u} H(u) · [C(u)+V(λ)+bridge(u,λ)=C_target].

Then the positive BRC class mass is exactly M(λ), and the class-support bit is [M(λ)>0]. Because each visible word λ labels exactly one deterministic visible transition path, the suffix dynamic program with terminal values 1_{M>0} and M separately computes q_F and |F| without multiplying support by hidden multiplicity. Recursion S(state)=Σ_{next emitted symbols} S(next state), similarly for total population; lexicographic rank/unrank branches by S of each next-state and class population queries use M. The exact law Σ_λ M(λ)=|F| follows by a partition of the ordered original histories according to Λ_h.

For this fixed ternary alphabet, all counters are bounded by n and there are at most O(n·(n+1)^25) cached transfer states up to constant boundary-letter factors. Terminal bridge lookup costs O(1) fixed-alphabet table queries (plus 25-counter arithmetic). Thus support count and exact class mass/rank/unrank are polynomial in n in arithmetic operations, with a conservative O(n·(n+1)^25) bound and O(n) bits per count. The actual reachable states are much fewer in the tested fibers; no claim of practical efficiency at all n or an arbitrary growing original alphabet is needed for this theorem.

## Executed evidence

`STAGE467B.py` is an independent Python standard-library implementation of the integer transfer, rank/unrank, full native signed-X6 observer, complete original-history enumeration for short configurations, and the 12-direction APPEND_Q witness traces. The exact executed JSON accompanies it. For (m,n)=(2,3),(3,4),(3,5),(4,5),(4,6),(5,6), 200 selected complete initial-observer fibers were fully enumerated. Across h=0..n, 1,259 parameter/fiber cases, 2,246 supported class population and bidirectional rank checks, and 1,151 original-history-pair future trace comparisons passed. A selected full fiber is exhaustively compared; the selection of 200 fibers is bounded, not every fiber at larger lengths.

Larger deterministic example without class/history enumeration: m=81,n=121,h=50, Q/P source population 76,072,914,304,576,841,039,448,060, classes 534,222,840, 2,220 hidden-prefix states and 154,162 cached suffix states. Exact rank/unrank/population spot checks at ranks 0, 267111420 and 534222839 passed. Other cases: (41,49,18) qF=7,636, |F|=22,614,134,400 and (61,81,27) qF=65,532, |F|=537,179,206,441,132,800.

Scope: direct mathematical theorem in the stated Q-only operation algebra; finite tests supplement the proof. Formal Source Result and independent Driver evaluation are pending.

## Next

Stage468-B: permit P POP and P APPEND while retaining the exact full-fiber signed-X6 observer. Identify a minimal *joint* boundary/transducer interface and determine whether the support automaton can remain deterministic and polynomial when both original suffixes can be edited. Subsequently extend to arbitrary signed original alphabets with signed displacement cancellations tracked explicitly.
