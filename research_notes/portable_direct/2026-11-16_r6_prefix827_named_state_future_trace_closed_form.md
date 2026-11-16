# PREFIX-827 — Exact named-source future count traces, sharp local recurrences, and observable profile classification

**Research status:** AUTHOR_PROVED / EXACT_BIGINT_REGRESSION / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.  
**Scope:** Independent portable positive-count BRC auxiliary research; no shared native Task CLAIM, native time law, X6 event admission or phase/amplitude completeness asserted.  
**Scientific input:** Frozen Source pin \`f42f2906d77f24085c123f3ccfe9667d41caa96d\`. Continues PREFIX-825/826 and their explicit Q-only observer; no P000 rebase.

## 1. Model, notation, and explicit closed formula

Let \`q≥1\` be the allowed occupied-source capacity. A named state is \`(m,S)\`, where \`m∈{0,1}\` indicates whether the distinguished source is present, \`S\` is a finite set of **distinct named unmarked sources**, \`p=|S|\`, and \`p+m≤q\`. Each \`i∈S\` has nonnegative integer removal weight \`β_i\`. The distinguished source has insertion weight \`a≥0\` and removal weight \`b≥0\`. In an unnormalized \`Q=R+A\` step, remove any present unmarked source \`i\` with branch coefficient \`β_i\`; remove a present mark with coefficient \`b\`; or insert an absent mark with coefficient \`a\` only when current occupancy is below \`q\`. Branches retain named identity. The declared output \`Y_\ell(t;m,S)\` is the sum of all path weights terminating with total occupancy \`ℓ\`, after exactly \`t\` sequential Q applications. This \`t\` is an **operator-step index**, not elapsed physical or native heartbeat time.

Set \`e_d(S)=∑_{T⊆S, |T|=d}∏_{i∈T}β_i\`, with \`e_0=1\`. For \`s≥0\` put
\[
w_{0,s}=a^{\lceil s/2\rceil}b^{\lfloor s/2\rfloor},\quad
w_{1,s}=a^{\lfloor s/2\rfloor}b^{\lceil s/2\rceil},
\quad m_s=(m+s)\bmod2 .
\]
Here \`0^0=1\`, as appropriate for a missing operation. For \`0≤d≤min(p,t)\` define the legal shuffle factor
\[
I_{q,p,m}(t,d)=
\begin{cases}
1& m=0,\ p=q,\ t=d=0,\\
0& m=0,\ p=q,\ t>0,\ d=0,\\
\binom{t-1}{d-1}&m=0,\ p=q,\ 1≤d≤t,\\
\binom{t}{d}&\text{otherwise}.
\end{cases}
\]

**Theorem 827.1 (all-capacity exact named-state trace).** For every integer \`q≥1\`, valid named state, nonnegative integer weights, \`t≥0\` and output bin \`0≤ℓ≤q\`,
\[
\boxed{Y_\ell(t;m,S)=
\sum_{d=0}^{\min(p,t)}
\mathbf1_{\ell=p-d+m_{t-d}}
d!\,e_d(S)\,I_{q,p,m}(t,d)\,w_{m,t-d}.}
\]
Every term is an actual positive-count BRC branch contribution. In particular this is a division-free *final sum* of nonnegative integers, not a cancellation or a claim of signed/phase completeness.

**Proof.** Exactly \`d\` unmarked sources are removed, each at most once. For any size-\`d\` subset there are \`d!\` orders, all with the same product of removal weights; summing over such subsets gives \`d!e_d(S)\`. There remain \`s=t-d\` distinguished-source steps. They must alternate insertion and removal, starting with insertion if \`m=0\` and removal if \`m=1\`; hence their order, product \`w_{m,s}\`, and final flag \`m_s\` are forced. If the initial state is not saturated with an absent mark, any shuffle of the \`d\` unmarked-removal steps with the \`s\` mark steps is legal: total unmarked occupancy can only decrease, and an insertion never exceeds capacity. There are \`\binom{t}{d}\` shuffles. If instead \`m=0,p=q\`, a mark insertion is initially blocked and the **first step must remove an unmarked source**. Exactly \`\binom{t-1}{d-1}\` shuffles then remain when \`d≥1\`; the only \`d=0\` legal trace is the empty \`t=0\` path. Final occupancy is \`p-d+m_s\`. Counting these disjoint paths proves the formula. □

## 2. Complete basis-state future equivalence certificate

**Theorem 827.2 (fixed-cardinality, fixed-mark future equivalence).** Fix \`q,p,m,a,b\` and compare two legal named basis states \`(m,S)\` and \`(m,S')\` with \`|S|=|S'|=p\`. Their entire Q-only occupancy-histogram traces agree for all \`t≥0\` **if and only if** \`e_d(S)=e_d(S')\` for every \`0≤d≤p\`. With positive integer removal weights this is equivalent to equality of the multisets of \`β_i\` (not equality of source names). With globally pairwise-distinct positive weights, two such basis states are trace-equivalent only when their unmarked named subsets coincide.

**Proof.** Sufficiency is Theorem 827.1. For necessity, inspect time \`t=d\`, and use induction on \`d\`. When \`m=0\`, only \`d\` unmarked removals can reach bin \`p-d\` in exactly \`d\` steps, so
\[
Y_{p-d}(d;0,S)=d!\,e_d(S).
\]
For \`m=1\`, the bin \`p-d+1\` receives precisely the paths with \`d\` unmarked removals and no marked step, plus the paths with \`d-1\` unmarked removals and one marked removal. Thus for \`d≥1\`
\[
Y_{p-d+1}(d;1,S)=d!\bigl(e_d(S)+b\,e_{d-1}(S)\bigr).
\]
The base case \`e_0=1\` and these triangular identities recover all \`e_d\` successively from the trace. Finally \`∏_{i∈S}(1+β_i z)=∑_d e_d(S)z^d\`; equality of this polynomial for positive weights entails equality of its factor multiset. □

**Important scope:** the equivalence statement is for **individual named basis states with fixed \`p,m\`**. Linear compression of arbitrary mixtures, nondeterministic or signed/phase observers, and additional individually-addressable source operations have different equivalence relations. Consequently distinct basis states may be nonmergeable even though PREFIX-823/825 construct a much smaller *linear* carrier for their mass distributions.

## 3. State-sensitive temporal recurrence and sharpness

Write \`E Y(t)=Y(t+1)\` and \`λ=ab\`. Assume \`a,b>0\` and every initially present \`β_i>0\`.

**Theorem 827.3.** If \`m=1\` or \`p<q\`, then
\[
\boxed{(E^2-\lambda)^{p+1}\,Y(t;m,S)=0\qquad(t\ge0).}
\]
If \`m=0,p=q\`, then
\[
\boxed{(E^2-\lambda)^q\,Y(t;0,S)=0\qquad(t\ge1).}
\]
These powers are **sharp for the corresponding individual positive named basis state** as identities in the even-step shift \`E²\` on the indicated full-tail observation sequence.

**Proof.** Fix a time parity. In every legal summand of Theorem 827.1, \`w_{m,t-d}\` is \`λ^{t/2}\` multiplied by a \`t\`-independent nonzero constant depending on \`m,d\` and parity (the exponent \`t/2\` may be half-integral in this proof only; no such expression is used in the exact implementation). In a non-saturated-absent start, the shuffle coefficient is \`\binom td\`, a polynomial in \`t\` of degree \`d≤p\`. In the initially saturated-absent case, \`t≥1\`, the coefficient is \`\binom{t-1}{d-1}\` of degree \`d-1≤q-1\`. Advancing two steps multiplies the common exponential part by \`λ\`; the \`p+1\`st or \`q\`th twisted finite difference therefore vanishes. For sharpness, the \`d=p\` term is nonzero at every sufficiently large admissible time of each parity. In an output bin receiving that term, all contributions from \`d<p\` have strictly smaller polynomial degree, so the leading polynomial coefficient cannot cancel. The maximal degree is exactly \`p\`, respectively \`q-1\`. □

The universal \`E(E²-\lambda)^q\` annihilator of PREFIX-826 follows again by taking the worst supported state. The present local statement is stronger for sparse initial subsets. No claim is made that these are minimal polynomials in the **one-step** operator \`E\` over arbitrary mixed states.

## 4. Exact algorithm, evidence and performance scope

Compute \`e_0,\ldots,e_p\` by the usual descending one-pass elementary-symmetric update in \`O(p²)\` exact integer operations, then evaluate at any chosen \`t\` using the \`p+1\` summands and integer binomial coefficients; powers use binary exponentiation. A single named basis source therefore needs only \`p+1\` profile coordinates to recover any declared \`Q^t\` occupancy histogram without producing the first \`2q\` snapshots required by the generic PREFIX-826 interpolation route. This is a source-conditioned formula, not a globally dimension-minimal state-space realization. Arithmetic work excludes the potentially dominant bit-length of powers/output integers, and converting a general mass distribution still requires aggregation of its named input states and weights.

The reproducible program \`PREFIX827_R6_NAMED_TRACE_CHECK.js\` uses JavaScript BigInt only. Its independent comparator enumerates the actual **named subset transition graph and each weighted legal branch**, rather than using the closed formula as the simulator. Configurations cover \`q=1..7\`, two weight families (distinct and duplicate where indicated), positive and boundary-zero \`a,b\`, and \`t=0..3q+9\`. It also checks the two exact profile-recovery identities, the state-sensitive temporal annihilators in the positive cases, identical-profile trace equivalence and a high-time \`t=1000\` exact calculation. See \`PREFIX827_R6_NAMED_TRACE_RESULTS.json\` for counted finite checks. These tests do not establish the all-\`q\` theorems; the path bijection and polynomial-degree arguments do.

## 5. Provenance, boundaries, remaining research

Frozen scientific Source: \`awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d\`, with P000 V5 and joint observer preservation. Reuses PREFIX-823/824/825/826, especially the declared unnormalized positive named-source Q action and final count observer; scientific definitions are not re-pinned to current \`main\`. Current norms are read separately from \`docs/RESEARCH_CONTINUATION_PROTOCOL.md#current-normative-context\`, \`docs/PORTABLE_RESEARCH_PROTOCOL.md\`, and \`research_priorities/research_method.json\`.

**Do not infer** that equal future cardinality traces imply equality of named provenance, phase, signed amplitudes, arbitrary R/A words, native X6 Cell/Link/Port events or physical-time traces. Keep \`S\` and the mark flag until the exact Q-only quotient is the declared target.

**Remaining:** Determine a universal minimally sized **nonnegative integer carrier** for Q-only \`q≥5,b>0\` (PREFIX-825 frontier); investigate source-condition-specific accelerated updates for **mass mixtures**, and exact distinctions when single-source removal/insertion is individually addressable. Native X6 event permissions require separate certificates and are still unresolved.

**Activity:** Existing historical \`EM-DIRECT-AB379B\` / \`RA-9B596EB6873BC7BAF237BC3A\` is provenance only. No fresh current-session authentication, shared TASK CLAIM, formal Result/review or authenticated Activity checkpoint is asserted by this standalone paper.
