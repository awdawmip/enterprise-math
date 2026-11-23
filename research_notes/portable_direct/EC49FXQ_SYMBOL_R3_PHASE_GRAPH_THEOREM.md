# EC49FXQ — Exact r=3 phase-pair obstruction law for whole-activation sensing

Date: 2026-11-23 (Asia/Shanghai). Frozen scientific input: BRC16943. Parent: EC49FXP, immutable source ce4d9738218b181cd3946f5907146537a5d12558, PR #2994. Status: AUTHOR_PROVED / EXACT_INTEGER_CROSSCHECK / PARENT_DEPENDENT / NOT_REVIEWED.

## Proposition

Continue precisely the EC49FXP Farey–CRT auxiliary two-channel whole-activation model. Physical activation positions belong to Z/110. Let D be an arbitrary nonempty phase set and A its image modulo 55; let S be a physical activation set. For each phase d, support color i modulo 5 and missing column j modulo 11, the number of distinguishing activation symbols is

\[
G_S(d,i,j)=\sum_{t\in S}{\bf1}\{(t\bmod5=i\land t\bmod11\ne j)\ \lor\ ((d-t)\bmod5=i\land(d-t)\bmod11\ne j)\}.
\]

The OR belongs INSIDE the activation sum: a double-channel activation can contribute only one symbol-distance unit. Minimize |S| subject to G_S(d,i,j)≥3 for all d∈A, i∈Z/5, j∈Z/11. Assume that A has at least one phase of each modulo-5 color. Define the histogram h_a=|{d∈A:d≡a (mod5)}| and the physical-color safe groups

\[
T_i=\{x\in\mathbb Z/55:x\equiv i\pmod5,\; 2x\notin A\},\qquad s_i=|T_i|=11-h_{2i}.
\]

Put F={i:s_i≤1}, H={i:s_i=2}, and B=15+|F|. A subset U⊆H is repair-admissible if it permits a choice x_i∈T_i for each i∈H\U satisfying x_i+x_j∉A modulo 55 for all distinct i,j∈H\U. Define

\[
\tau(A)=\min\bigl\{|U|:U\subseteq H,\ \exists(x_i)_{i\in H\setminus U}\ \forall i\ne j,\ x_i+x_j\notin A\bigr\}.
\]

**Theorem (exact universal r=3 law, in the frozen auxiliary model).**

\[
\boxed{N^{\rm symbol}_3(D)=15+\#\{a:h_a\ge10\}+\tau(A).}
\]

The first two terms are functions of the five phase counts. The repair term depends on the actual phase residues. There are at most five binary upgrade choices and at most five binary safe-group choices, so an exhaustive exact search uses at most 1024 raw candidate combinations, independently of the size of D.

## Proof

**Self-color rows.** Write m_i for the number of selected physical sites of color i and n_x∈{0,1,2} for the selected lifts of a group x modulo 55. In a phase with d mod5=2i, only sites of physical color i can contribute; an unsafe group x with 2x∈A is deleted in the row with missing column x mod11. Thus the self-color constraints are exactly m_i−max_{x∉T_i}n_x≥3. Every phase color occurs, so every m_i≥3. If s_i≥2, three safe sites can suffice; when s_i=2 they must occupy the two groups in pattern (2,1). If s_i≥3, take three distinct safe groups. If s_i≤1, three safe sites are impossible, so m_i≥4. Four sites from four distinct groups always satisfy the self-color requirement, giving the local lower bound B.

**Normalization.** A class with at least four selected sites can be replaced by four sites at distinct modulo-55 groups. This retains self-color distance at least three; against any other class of at least three selected sites, cross-color distance is at least (4−1)+(3−2)=4, since a missing column deletes at most one site from the four-group class and at most two from any class. If s_i≥3, a three-site class can be replaced by three distinct safe groups without changing its cardinality; against an arbitrary other three-site class the cross-color distance is at least (3−1)+(3−2)=3. Therefore there is an optimum where classes with s_i≤1 use four distinct groups; those with s_i≥3 use three distinct safe groups; classes with s_i=2 use either four distinct groups or three safe sites with exactly one doubled group x_i∈T_i. Let U be the latter classes upgraded to four. Its site count is B+|U|.

**Pair obstruction.** Distinct classes i,j each having three sites with doubled groups x_i and x_j can both lose two sites in a single cross-color row precisely when d=x_i+x_j modulo 55 is an allowed phase: the missing column is x_i mod11 and the right-channel missing column is x_j mod11. That row has distance (3−2)+(3−2)=2. If the sum is absent, no row can delete two in both classes simultaneously, so every such cross row has distance at least (3−2)+(3−1)=3. Any pair involving a non-doubled class also meets distance three.

Consequently the normalized layout satisfies all rows iff its doubled safe groups obey the pair condition. Every admissible layout costs at least B+τ(A); selecting a minimizing U and placing three or four sites as just described constructs a layout of exactly that cost. This proves the theorem.

## Exact equal-histogram counterexample

Represent each phase set by taking all 11 residues of each phase color a=0,1,2 and removing the two indicated holes. In colors a=3,4 take only the listed singleton.

| Set | holes a=0 | holes a=1 | holes a=2 | a=3 | a=4 | histogram | exact N3 |
|---|---|---|---|---|---|---|---|
| Good | 15,45 | 1,36 | 2,32 | 8 | 9 | (9,9,9,1,1) | **15** |
| Bad | 25,45 | 11,26 | 22,37 | 53 | 29 | (9,9,9,1,1) | **16** |

For Good the critical physical colors are H={0,1,3}. Choose doubled safe groups x_0=35, x_1=1, x_3=18. Their pairwise sums are 36,53,19, all absent from Good, so τ=0.

For Bad, T_0={40,50} and T_1={11,46}. All four possible sums 51,31,6,41 belong to Bad. Hence at least one upgrade is unavoidable. Upgrading class 0 and choosing x_1=11, x_3=13 meets the remaining condition, so τ=1. The same five counts give distinct optimum costs: five-count compression is sufficient for EC49FXP at 4≤r≤20 but **fails to retain r=3 optimal cost**.

A dense further witness has all five phase colors occupied 9 times each; remove the hole pairs ([0,45],[16,51],[22,37],[18,53],[19,54]) from the respective full modulo-5 classes. Direct enumeration yields B=15 and τ=3, hence N3=18. The missing phase-pair interaction can cost multiple additional activations.

## Exact verification

The accompanying dependency-free JavaScript program computes the finite repair search, constructs achieving layouts, and directly evaluates all d/i/j rows. Author execution on Node.js 22.16.0 passed 3,190 rows for the Good/Bad witnesses, 2,475 rows for the dense witness, 582,835 rows on 350 deterministically generated arbitrary full-color phase sets, and 618,750 rows on 250 high-density 9-per-color sets. Total: **1,207,250 exact integer row checks**, all passed. The accompanying output includes physical layouts, the worst row, the safe-group choices, repair counts and pair compatibility. The universal statement rests on the proof above; finite tests cross-check its implementation and the examples.

## Meaning and next scientific question

The term τ(A) is a quantified structural residual for the declared static cost observer, not an extra spatial coordinate. Retain full phase-residue provenance for actual layout selection and future operations. The frozen auxiliary observer retains universal independent support-color/missing-column quantifiers; native same-anchor Farey dynamics may correlate phase, support, column, anchor, branch and height. Next: derive these native reachable joint states and check which cost-optimality results transfer under that exact observer bridge. Also examine arbitrary phases at r=1,2. P000, ACTIVE Heartbeat X6 and the scientific pin are unchanged. No formal CLAIM, Result, Review or Foundation admission is asserted.
