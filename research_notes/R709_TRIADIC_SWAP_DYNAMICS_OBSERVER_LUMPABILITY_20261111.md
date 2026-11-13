# R709 — Complete-triad swap dynamics and future-safe two-force observer

Date: 2026-11-11 (Asia/Shanghai). Researcher EM-X6-640177; RA-BC55A6E8FF1DD5106A03841E.
Task RS-X6-TRIADIC-CLOSURE-DYNAMICS, TP2-8B7E13C5904A2D6F1142.
Frozen science: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.
Predecessor R708 in the same research branch, R707 PR #2033.

## State and atomic candidate update

Work in R708's four-axis equal-positive-quantum Cell-local family, m>=2. Give the two saturated axes separately identified token sets A={a_1,...,a_m} and B={b_1,...,b_m}. Let C={c_1,...,c_m} be the third-token pool from one or two other native axes; each c retains its axis, sign and original source identity. A full legal complete triadic partition is a pair of bijections f:A->B and g:A->C, represented by m complete three-token candidate triads {a,f(a),g(a)}. The source-state set is Ω=S_m × S_m with exactly (m!)^2 individually labeled full-decomposition states.

A step is chosen as follows, with its operation choice preserved as BRC provenance. With probability 1/2 hold the entire state unchanged. Otherwise choose one of the f- or g-channels with probability 1/4 each, then choose an unordered pair {a_r,a_s} of different A-tokens uniformly among C(m,2) possibilities; swap the two partners IN THE SELECTED CHANNEL SIMULTANEOUSLY, leaving the other channel unchanged. Every output consists of m complete equal-quantum three-distinct-axis candidate triads; no primitive two-force intermediate stable state is asserted. Each nonhold branch has mass 1/[4*C(m,2)] with explicit branch (channel,r,s); a hold has mass 1/2.

This typed update defines event order, not measured heartbeat time. All role selections are carried as part of the state under S6 relabeling; no canonical choice of two special axes from an unmarked triple is assumed.

## Theorem R709-A: connectedness, reversibility and unique stationary distribution

For every m>=2, this finite-state transition graph is connected and aperiodic, with unique stationary probability 1/(m!)^2 on each complete labeled decomposition.

Proof. In each of the two permutation coordinates f and g, elementary transpositions of two images generate all of S_m. Allowed moves can change either coordinate, holding the other unchanged, hence generate the full Cartesian product S_m × S_m and connect every pair of source states. Each elementary swap is its own inverse and has the identical transition probability in both directions; therefore the full stochastic transition matrix is symmetric and satisfies detailed balance under the uniform law. Every state has holding probability 1/2, implying aperiodicity. Finite irreducibility gives uniqueness of the stationary law. QED.

The exact probability of returning to the IDENTICAL complete source state after two events is

P(X_2=X_0) = 1/4 + 1/[8*C(m,2)].

Proof. Two holds contribute 1/4. For two nonholding moves to return, their selected channel and pair must agree exactly, because any distinct pair/channel product moves at least one coordinate. There are 2*C(m,2) choices, each with joint mass 1/[16*C(m,2)^2], summing to 1/[8*C(m,2)]. QED.

Values: m=2:3/8, m=3:7/24, m=4:13/48.

## Theorem R709-B: exact Markov lumpability of a named pair observer

Fix individual tokens a* in A and b* in B. Let E(f,g) be 1 exactly if f(a*)=b*, meaning the visible named two tokens occupy the SAME hidden-third complete triad; otherwise E=0. For every m>=2, E is an exact strong Markov quotient for ALL finite future event horizons with transition probabilities

P(E_next=1|E_now=1)=1-1/(2m)
P(E_next=1|E_now=0)=1/[2m(m-1)].

Proof. Only f-channel swaps affect E; they have total mass 1/4. If E=1, swapping a* with any of the m-1 other A tokens destroys E. The relevant unordered-pair fraction is (m-1)/C(m,2)=2/m, giving 1->0 mass 1/(2m). If E=0, there is one unique other A token mapped by f to b*. Swapping its partner with a* creates E, with mass (1/4)/C(m,2)=1/[2m(m-1)]. In either case the aggregated transition masses depend only on E, not on any other f or g details. Therefore each observer fiber has the same outgoing mass to each observer fiber, the defining strong-lumpability criterion, hence all finite future E observations are exactly preserved. QED.

This two-state kernel has stationary P(E=1)=1/m and nontrivial eigenvalue λ=1-1/[2(m-1)]. The exact n-step probabilities are

P(E_n=1|E_0=1)=1/m+(1-1/m)*λ^n
P(E_n=1|E_0=0)=(1/m)*(1-λ^n)

for every integer n>=0.

The BRC source state Ω retains the hidden C-token identity, f/g full mappings, signs and operation provenance. The binary quotient is certified for E under this exact swap kernel, not for a query of the third token, a future specifically addressed port, or a different native update rule.

## Exact verification

The independent Python Fraction checker in experiments/R709_TRIADIC_SWAP_BRC_DYNAMICS_VERIFY_20261111.py enumerates the complete (f,g) source states for m=2 (4 states), m=3 (36 states), and m=4 (576 states). For every state it explicitly constructs the transition kernel and checks normalization, exact source membership, detailed balance on all positive transitions, and equality of next-E mass for every observer fiber. From one state it computes the two-step full-state return through a second transition enumeration. Marker R709_TRIADIC_SWAP_BRC_KERNEL_LUMPABILITY_PASS. The emitted JSON includes source sizes, E fiber sizes, p_11, p_01 and two-step values; integers and Fraction exact rational arithmetic are used within a typed positive source-counting BRC model.

## Scope and next native obligation

The update is a constructive Cell-local legal triad rewrite candidate obeying the R707 distinct-axis and P000 three-nonzero arity types, and covariant under jointly relabeled S6 axis/token identities. A native physical update requires checking actual X6 Link/Port permission/occupancy, V29 PASS/TRANSFER accounting, V39 loop-flow j and separately typed native rotation-generator updates against the frozen scientific input. Next select a minimal m=2 four-axis example, execute one complete f-channel swap and one g-channel swap against the native event contract, compare their port and loop consequences, then verify whether E remains a future-sufficient observer under that enriched operation set.
