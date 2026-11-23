# EC49FXR — Exact r=2 cost for arbitrary phases in the frozen two-channel symbol model

Date: 2026-11-23 Asia/Shanghai. Scientific input pin: **BRC16943**, unchanged. Direct predecessor: EC49FXQ at 3a0a82721217b681477d3b365714e8b78ce1a4fe (PR #2998); EC49FXP at ce4d9738218b181cd3946f5907146537a5d12558. Status: AUTHOR_PROVED / EXACT_INTEGER_CROSSCHECK / PARENT_DEPENDENT / NOT_REVIEWED.

## Exact observer and statement

Use the inherited Farey–CRT auxiliary observer, not a proven native Farey reachability model. A physical activation site t belongs to Z/110. For a selected set S, permitted phase d, support color i in Z/5, and missing column j in Z/11, the **whole-activation symbol** distance is

\[
G_S(d,i,j)=\sum_{t\in S}\mathbf1\{(t\bmod5=i\land t\bmod11\ne j)\lor ((d-t)\bmod5=i\land(d-t)\bmod11\ne j)\}.
\]

The OR is **inside** the sum: one corrupted physical activation counts as one symbol, even if both channels differ. Require G≥2 for every admissible d,i,j. The observation depends only on A={d mod55: d in D}. Assume each of its five phase colors occurs: h_a=|{d in A:d mod5=a}|≥1 for a=0,...,4.

For physical color i, define C_i={x in Z/55:x mod5=i} and the safe CRT groups

\[
T_i=\{x\in C_i:2x\notin A\pmod {55}\},\qquad |T_i|=11-h_{2i}.
\]

Choose E⊆{i:T_i nonempty}, with one group x_i∈T_i for each i∈E, satisfying x_i+x_j∉A (mod55) for all distinct i,j∈E. For each remaining color j∉E define

\[
P_j(E,x)=\{y\in T_j:\ \forall i\in E,\ x_i+y\notin A\pmod{55}\},
\quad L(E,x)=|E|+\#\{j\notin E:|P_j(E,x)|\ge2\}.
\]

**Theorem (sharp for every eligible arbitrary phase set):**

\[
\boxed{N^{\mathrm{symbol}}_2(D)=15-\max_{E,x}L(E,x),\qquad 10\le N_2(D)\le15.}
\]

The empty choice E is valid. The exhaustive finite optimization considers at most \(\prod_i(1+|T_i|)\le12^5=248832\) raw double-choice assignments. It uses the actual phase residues and modular sums, not just the five h_a.

## Complete proof

**1. Self-color constraint.** Every phase color occurs. For each physical color i some d has d≡2i (mod5), so only sites of color i contribute to its self row and m_i≥2. For m_i=2, any selected group x with 2x∈A can be hidden by choosing the corresponding self-row d=2x and missing j=x mod11, violating G≥2. Consequently both selected sites must lie over safe groups T_i. Conversely two safe sites satisfy every self-row.

**2. Heavy normalization.** Any color with m_i≥3 can be replaced by exactly three sites at distinct modulo-55 groups. At most one of these sites is hidden in any self row, leaving at least two. In any cross-color row involving this normalized class it contributes at least 3−1=2, independently of the other physical class. Thus normalization weakly decreases cost while preserving all constraints. Every cardinality optimum admits a representative in which each physical color is light (two safe sites) or heavy (three distinct groups).

**3. All cross-color obstructions.** A light class either selects both physical lifts x,x+55 of one safe group (a *double*) or one site each from two distinct safe groups. Distinct-group light classes lose at most one site for each missing column; two of them together always retain at least two symbols. Two doubled classes i,j fail exactly when their sum x_i+x_j is an allowed phase mod55 (then all four sites disappear in one cross row). A doubled class i paired with a distinct-group class j fails exactly when one of the chosen groups y of j has x_i+y∈A (then the doubled class loses two and j loses one). These statements follow by imposing both left and right missing-column congruences simultaneously, using CRT mod55. Other cross rows retain at least two symbols.

**4. Necessity and construction.** Given a normalized feasible layout, let E be its doubled light classes. It is pair-compatible. Every other light class j must take two distinct groups in P_j(E,x), so the total number of light colors is at most max L. Since there are five colors, |S|≥2L+3(5−L)=15−L, giving the asserted lower bound. Conversely choose maximizing E,x: activate x_i,x_i+55 for i∈E, two distinct safe group representatives from P_j for each remaining j with |P_j|≥2, and three distinct groups for each remaining heavy color. Steps 1–3 show every row meets G≥2, attaining the lower bound. Thus equality holds universally under the stated assumptions.

## Two sets with the same histogram but different cost

Let C_a={a,a+5,...,a+50}⊆Z/55 and

\[
B=(C_0\setminus\{0\})\cup(C_2\setminus\{2,7\})\cup\{1,3\}.
\]
\[
A_{\rm good}=B\cup\{19\},\qquad A_{\rm bad}=B\cup\{4\}.
\]

Each set contains 22 phases, with identical phase histogram **(10,1,9,1,1)** and physical safe-group counts (1,2,10,10,10).

For Good, the ten-site layout

\[
S_{\rm good}=\{0,2,7,24,31,33,38,55,79,86\}
\]

is feasible. Doubled physical colors 0,1,4 use groups 0,31,24. Their pairwise sums (31,24,0) are absent from A_good. The other light colors use the distinct pairs (2,7) and (33,38); every sum with a chosen double is absent from A_good. The general lower bound is 10, hence N_2(A_good)=10.

For Bad, suppose ten activations were feasible, forcing all five colors light. Since T_0={0}, color 0 must double group 0. Dense phase color 2 has all residues except 2 and 7, so color 2 must use groups 2 or 7 to avoid collision with 0. Group 2 is not safe (2·2=4∈A_bad); therefore color 2 must double group 7. The safe groups for color 1 are {1,31}; 1 collides with doubled 0 because phase 1 is allowed, forcing a double at 31. Dense phase color 0 then forces physical color 4 to double group 24, the sole solution of 31+y∉A_bad in that color. Finally, to coexist with double 7, each group y of a light color 3 must satisfy y=48 (since 7+y must equal the only missing phase 0); to coexist with double 24 it must satisfy y∈{33,38} (since 24+y must equal a missing phase 2 or 7). These requirements are disjoint. Therefore no ten-site layout exists.

The explicit eleven-site set

\[
S_{\rm bad}=\{0,1,3,4,5,7,8,9,10,12,31\}
\]

satisfies every row: color 0 is heavy (0,5,10), and the other colors each use two distinct safe groups. Hence **N_2(A_bad)=11**.

This is an exact **cost-observer information-loss witness**: five phase histogram counts cannot determine optimum cost at r=2, complementing EC49FXQ's r=3 obstruction and EC49FXP's histogram sufficiency at 4≤r≤20.

## Verification and bounded transfer

Companion Node.js script enumerates the double-choice optimization, constructs optimal site layouts, and independently evaluates the distance expression over every (d,i,j) for the tested phase sets. The executed result passed **1,231,835 exact integer row checks**: both 22-phase witnesses, a complete 32-member binary five-phase family, and 600 deterministic generated sets (400 general, 200 dense). The analytic argument proves the quantified theorem; finite calculations crosscheck its implementation and witnesses. No floating point arithmetic enters the distance computation.

Future scientific problem: derive the actual **same-anchor Farey jointly reachable tuples** (relative phase, support color, missing column, anchor, branch, height), restrict the auxiliary observer to the exact reachable row relation and test which optimization laws descend. Retain all phase/branch provenance and P000/ACTIVE native X6 meanings. This result does not claim a formal shared Task CLAIM, Result, or independent Review.