# EC49FXS — Exact r=1 symbol observation for arbitrary phases

Date: 2026-11-23 (Asia/Shanghai). Scientific pin: **BRC16943**, unchanged. Direct predecessors: EC49FXR at 831aa3f0783f73d82a8ec79a9c47cb33ae9c2e30 (PR #3000) and EC49FXQ at 3a0a82721217b681477d3b365714e8b78ce1a4fe (PR #2998).
Status: AUTHOR_PROVED / EXACT_INTEGER_CROSSCHECK / PARENT_DEPENDENT / NOT_REVIEWED.

## Exact model

This is the frozen auxiliary Farey–CRT *whole physical activation symbol* observer, not a claimed native same-anchor trajectory theorem. Let A be the nonempty phase set modulo 55, with each of the five modulo-5 phase colors present. A physical activation t belongs to Z/110. For selected activation sites S, phase d∈A, support color i∈Z/5 and missing column j∈Z/11, the distinguishing symbol distance is

\[
G_S(d,i,j)=\sum_{t\in S}\mathbf{1}\{(t\bmod5=i\land t\bmod11\ne j)\lor((d-t)\bmod5=i\land(d-t)\bmod11\ne j)\}.
\]

The OR is inside the sum: a physical activation contributes at most one symbol. Require G≥1 for all d,i,j and minimize |S|, writing the optimum as N₁(A).

Let Cᵢ={x∈Z/55:x≡i (mod 5)} and Tᵢ={x∈Cᵢ:2x∉A (mod 55)}. A set E of physical colors is **singleton-compatible** if there exist xᵢ∈Tᵢ for i∈E such that xᵢ+xₗ∉A (mod55) for every distinct i,l∈E. Define α(A) as the maximum cardinality of a singleton-compatible E; E=∅ is allowed.

**Theorem:** For every full-color A⊆Z/55,

\[
\boxed{N_1(A)=10-\alpha(A),\qquad 5\le N_1(A)\le10.}
\]

Checking the five singleton/upgrade choices needs at most ∏ᵢ(1+|Tᵢ|)≤12⁵=248832 raw assignments. The construction is exact integer arithmetic.

## Complete proof

1. In a self-color row, d≡2i (mod5), only activations in physical color i can contribute. Since A includes every phase color, all five physical colors must occur in S. A color-i singleton t is hidden in a self row exactly when the permitted phase is d≡2(t mod55) (mod55), taking the missing column j=t mod11. Thus singleton t is self-safe iff x=t mod55 lies in Tᵢ. Two sites in distinct mod-55 groups of the same physical color are always self-safe: one missing column/phase pair can hide at most one such group.

2. Normalize any feasible color class of size ≥2 to two distinct-group sites. In a mixed-color row d mod5≠2i, precisely two distinct physical colors are relevant, i and (d−i) mod5. From two distinct groups at most one activation can be hidden, hence the two-site class always contributes ≥1 regardless of the other class. Normalization therefore preserves all rows without increasing cost. An optimum has one or two sites in each physical color.

3. For two distinct singleton colors i,l with safe groups xᵢ,xₗ, both physical contributions disappear in a mixed row exactly when an allowed d satisfies d≡xᵢ+xₗ (mod55). Indeed the same missing column j=xᵢ mod11 makes the left singleton and right singleton disappear precisely under this congruence; the mod5 condition is d≡i+l. Therefore singleton compatibility is necessary and sufficient for every mixed row between singleton colors. If either color has two distinct groups, that class leaves ≥1 symbol.

4. An optimal normalized layout with singleton set E must use a compatible assignment, |E|≤α(A). Its size is |E|+2(5−|E|)=10−|E|≥10−α(A). Conversely pick a maximal compatible assignment, activate its one safe site per color, and activate arbitrary two distinct mod55 groups in each remaining color. Steps 1–3 verify every row. The size is 10−α(A), giving equality.

## Exact equal-histogram counterexample

Consider two 22-phase sets:

A_loss = {0,1,2,5,7,10,12,15,20,22,25,27,28,30,32,35,39,40,42,45,47,52}.

A_good = {0,2,5,10,12,13,17,19,20,22,25,27,30,32,35,36,40,42,45,47,50,52}.

Both have the exact modulo-5 phase occupancy histogram (10,1,9,1,1). However **N₁(A_good)=5** and **N₁(A_loss)=6**.

For A_good, the five safe singleton physical positions S_good={2,13,24,35,46} have all pairwise sums modulo55 outside A_good, so all self/mixed rows are covered. Five activations is the universal lower bound.

For A_loss, six positions S_loss={4,9,12,25,36,38} attain G≥1. To exclude five, every physical color would have to be singleton. T₀={25}, forcing x₀=25. Compatibility then forces x₂=12. The remaining x₁ is 36 or 46. If x₁=36, no compatible color-4 singleton exists. If x₁=46, compatibility forces x₃=38 and x₄=4; their sum 42 belongs to A_loss, an exact pair conflict. Hence α(A_loss)=4, N₁=6.

**Observer conclusion:** Phase occupancy counts lose a cost-relevant phase-pair residual even for error-free recovery (symbol distance r=1). This complements EC49FXQ's r=3 and EC49FXR's r=2 witnesses. EC49FXP's five-histogram sufficiency remains restricted to its proved 4≤r≤20 scope. A statement about native same-anchor Farey dynamics requires its separate exact reachability bridge.

## Exact computation

The companion Python standard-library verifier exhaustively optimizes singleton-compatible assignments, constructs achieving physical layouts, and directly evaluates all phase/support/column CRT rows. It was executed on four explicit sets plus 600 deterministic full-color sets (seed 20261123). **997370 exact integer rows** were checked; every constructed layout achieved G≥1. The program also independently asserts the explicit A_loss five-singleton contradiction. Exact coverage and witness data are recorded in the companion JSON. Finite tests cross-check the theorem and examples; the full universal claim follows from the proof above.

## Frontier and non-transfer

The useful native frontier is the jointly reachable relation among (phase, support color, missing column, anchor, branch, height, time) from the original pinned same-anchor Farey evolution. Restrict G to that relation only after extracting its authentic source. Before any compression, require exact observer/future-operation fiber constancy; preserve phase, branch, height, X6 spatial provenance and time. No new Task/CLAIM/Result/Review, native heartbeat arithmetic claim, or Foundation admission is asserted. P000/ACTIVE and the frozen science input remain unchanged.
