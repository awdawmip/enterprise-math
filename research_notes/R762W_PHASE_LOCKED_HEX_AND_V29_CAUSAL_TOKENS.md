# R762W — Phase-locked hexagonal triadic incidence and sharp causal token overhead

Date: 2026-11-14 Asia/Shanghai.
Research class: **AUTHOR-SIDE EXACT CANDIDATE / FINITE REPRODUCIBLE VERIFICATION / NOT_REVIEWED / NOT_ADMITTED**.
Parent task: \`RS-X6-TRIADIC-CLOSURE-DYNAMICS\`, publication \`TP2-8B7E13C5904A2D6F1142\`.
Researcher: \`EM-X6-F253B2\`; Activity: \`RA-28B178D65597152EEB3BFF6B\`; current native CLAIM is separately checked.
Frozen P000 scientific revision: \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`.

## Question and typed scope

The accepted X6 spatial Cell carrier is an affine torsor for \`Z^6\` with twelve signed primitive coordinate neighbor moves. A P000 stable nonzero atomic balance needs precisely three distinct present force quanta and \`TRIADIC_CLOSURE_E\`; the currently frozen premise fixes the arity and canonical pairwise \`PERP_E\` but leaves the precise force-event scheduler and V39 transport for further construction.

R762H (PR #2288) established six *first-return hexagonal* closed coordinate-path witnesses among 24 shortest three-port-covering loops. R762R (PR #2333) built a three-spoke excursion candidate with cyclic source-order update. R762S (PR #2337) built a candidate V29 oriented three-PASS ledger for ordered sources. R762U (PR #2347) proved that one token can execute an arbitrary balanced directed-PASS multiset when event order may be chosen freely. R762V (PR #2351) further distinguished first-return paths and source-projection fibers.

This note joins these interfaces in a **different explicit candidate event family** and computes a sharp *time-order restriction cost*. The candidate Cell/Link/Port event is fully typed; whether it is adopted as the unique physical \`TRIADIC_CLOSURE_E\` admission/update law is open.

## Definition: the hexagonal macroevent

Fix a native Cell \`c\` and three signed unit directions \`a,b,d \in \{\pm e_1,\ldots,\pm e_6\}\` with distinct underlying axes, each permanently attached to a distinct nonzero equal-quantum force-source identity. Their local incidence ports are \`c+a,c+b,c+d\`. Declare the ordered hexagonal coordinate trace

\[
H(a,b,d)=(a,b,-a,d,-b,-d).
\]

A walker over these six **primitive single-axis** microsteps has relative Cell coordinates

\[
0,\quad a,\quad a+b,\quad b,\quad b+d,\quad d,\quad0.
\]

The first source, second source, third source are encountered at times \`1,3,5\` respectively; no proper return or adjacent immediate backtrack occurs. The packet records the full ordered trace, source names, rooted directed-edge current and the three equal force quanta. The proposed macroevent \`E_H(c;a,b,d)\` is *candidate-accepted* when exactly this typed incidence and all three equal-quantum pairwise \`PERP_E\` sources are present. This is a constructive choice of the undeveloped admission interface, not a theorem deriving physical admission from endpoint return.

Declare \`F(a,b,d)=(b,d,a)\`. A completed macroevent keeps the Cell and all force quanta and moves only this internal source-order state. The phase is internal, not a seventh spatial coordinate.

In a separate declared **V29-compatible ledger lift**, let the macroevent emit three local primitive PASS occurrences, in the fixed order

\[
a\to b,\qquad b\to d,\qquad d\to a,
\]

with zero boundary TRANSFER counts. All three labels are source/port IDs. This sequence is an additional typed contract for the *candidate* force event; a coordinate step is not silently identified with one PASS.

## Theorem W1 — spatial first return with a nontrivial order cycle

For each \`T=\{a,b,d\}\` there are six distinct ordered hexagonal macroevents \`E_H(c;\ell)\`. They are permuted covariantly under the current native axis-permutation rotation skeleton \`S_6\`, have the same Cell endpoint and all visit the three ports, but their **rooted oriented-edge currents are pairwise distinct**.

**Proof.** The explicit seven-point trace above shows return only at phase six. Distinct axes preclude partial cancellations, and all six consecutive edges are distinct. The rooted current has a unique edge leaving \`c\` in direction \`a\`, determining the first source; the edge from \`c+a\` to \`c+a+b\` then determines \`b\` and hence the remaining \`d\`. Therefore rooted current determines the entire order. Relabeling the six native axes preserves all signed single-axis step definitions and transports every term of the expression; no classical Euclidean vector-force equilibrium is invoked. The update \`F\` has two three-element orbits on the six orders, i.e. 320 internal period-three cycles among the 160 signed triads and 960 ordered states. QED.

## Theorem W2 — complete event count loses exactly a threefold phase

Each candidate macroevent contributes the same directed three-cycle PASS matrix for its cyclic orientation:

\[
M_{a,b}=M_{b,d}=M_{d,a}=1,\quad \text{all other entries zero}.
\]

Its V29 local imbalance is exactly

\[
u=(M-M^{\mathsf T})\mathbf 1=0,
\]

while \(\mathrm{rank}_\mathbb Q(M-M^{\mathsf T})=2\). The opposite order orientation reverses the directed cycle. Thus the six ordered states have exactly **two** different complete V29 PASS matrices, with **three** source-order states in each fiber.

Under \`F\`, the three orders of a given cyclic orientation all contribute the same \`M\`, so after any \`k>=1\` complete events the cumulative matrix is \`kM\`, independently of the initial phase within that orbit. Rooted X6 edge current from even one completed hexagonal event identifies its order uniquely by W1. A fixed-width repair of the V29 count observer needs and admits exactly \(\lceil\log_2 3\rceil=2\) phase bits. This conditional BRC information-loss result is for the specific macroevent and observer; the initial quantum identities remain present in the full packet.

## Theorem W3 — phase-locking changes the optimal seed count from 1 to min(k,3)

Add the **conditional causal-token semantics** of R762U: each labeled port holds nonnegative integer tokens, each of the three PASS occurrences requires one token at the source and moves it to its destination, and the prescribed three PASS within one macroevent must execute consecutively in the indicated order. Define a \`k\`-round execution as

\[
E_H(\ell), E_H(F\ell), \ldots,E_H(F^{k-1}\ell).
\]

No extra injection or interleaved reordering is permitted. Then for every initial ordered source triple and every positive integer \`k\`,

\[
\boxed{K_{\min}^{\mathrm{phase\ locked}}(k)=\min\{k,3\}.}
\]

**Proof.** Within an individual macroevent beginning with source \`s\`, the first PASS requires a token already at \`s\`. The following two PASS edges move that token around the three-source cycle and return it to \`s\`. No token distribution changes between completed macroevents, regardless of extra tokens. Under \`F\`, the distinct first sources across \`k\` consecutive events are exactly \(\{a,b,d\}\) truncated to \(\min(k,3)\) initial distinct sources. One initial token at each of those sources is therefore necessary. It is also sufficient: each event routes its first-source token around the three PASS and restores it. QED.

For comparison, if the **same multiset** of \`3k\` directed PASS occurrences is allowed to be arbitrarily reordered, it is one weakly connected balanced directed multigraph, so R762U's theorem gives

\[
\boxed{K_{\min}^{\mathrm{free\ schedule}}(k)=1\qquad(k\ge1).}
\]

For every \`k>=3\`, the temporal phase-locked schedule thus requires **two additional initial tokens**, despite identical final V29 PASS matrix \`kM\` and identical scalar conservation. This is a sharp event-order / inventory residual that survives complete local count conservation. One macroevent can run with a single token, but repeatedly executing the actual rotating phase order without injection needs three tokens.

In particular, the three-phase period is the first horizon where a static V29 event-count observer underestimates the required starting inventory by the full two-token gap. The gap measures the additional **fixed macroblock and phase constraint**, not a limitation on R762U's unrestricted trail theorem.

## Verification and applicability

\`research_notes/R762W_PHASE_LOCKED_HEX_VERIFY.py\` uses only Python standard-library exact integer calculations. It checks all 160 signed distinct-axis triads, six orders each (960 candidate macroevents); all loop prefixes/edges and fixed three-PASS cycles; each seven-round sequence against the sharp \`min(k,3)\` token bound; and 720 native axis permutations over a mixed-sign representative, six orders each (4,320 covariance tests). Its matching deterministic output is \`research_notes/R762W_EVIDENCE.json\`. All assertions passed. W1–W3 above give general mathematical proofs; the finite enumeration is a reproducible check of the declared finite signed-axis carrier.

P000 remains at the frozen scientific pin. The actual \`TRIADIC_CLOSURE_E\` atomic event selection, possible other scheduling, V17 active-frame connection and V39 based-loop \`(j,h)\` transport remain unresolved. The next discriminating scientific task is to locate or define the true admitted force event's source-typed scheduler; if its PASS operations are fixed and phase-coupled, test the W3 resource excess; if schedule ordering is not fixed, retain R762U's one-token theorem. Retain the exact full Cell/Link/Port and source identity before projecting to V29 counts.
