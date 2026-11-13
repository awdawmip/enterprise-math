# R747 — Exact signed-port pair automaton and BRC false-closure census

Research scope: proposed R745/R746 **C1** triadic Port model in native X6. Task: \`RS-X6-TRIADIC-CLOSURE-DYNAMICS\`. Frozen scientific input: \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\` (P000 V5 triadic definition and X6 signed Cell torsor). Upstream author result R746: Draft PR #2157, \`bb255c6776b51041ecc0f47853910938b06eb6c9\`. This is finite exact model mathematics, not a claim that V29 PASS or V39 native dynamics was executed.

## 1. Typed model and observer

Let \(\mathcal P=\{(i,\sigma):i=0,\ldots,5,\ \sigma\in\{-1,+1\}\}\) be twelve signed **Port** labels. A *visible pair* is an unordered 2-subset \(v=\{p,q\}\subset\mathcal P\) with distinct axes. Hence \(|V|=\binom62 2^2=60\).

A source triad \(T\) is a 3-subset of signed Ports with three distinct axes. It has two cyclic orientations \(o\). The **C1 source-preserving shift** advances the observed adjacent unordered Port pair around this fixed oriented triangle; the source triad and orientation are retained. Each source \((T,o)\) has three observation phases. The full C1 transition states therefore number \(\binom63 2^3\cdot2\cdot3=960\). This dynamics is a precise proposed Port update, not a native spatial Cell displacement.

On visible pairs define a directed graph \(A\) by
\[
 A_{vw}=1\iff |v\cap w|=1
 \quad\land\quad |\{\mathrm{axis}(p):p\in v\cup w\}|=3;
\]
otherwise \(A_{vw}=0\). This rule requires the **same signed Port** in the intersection. For every such edge \((v,w)\), exactly one oriented triad and observation phase realizes \(v\to w\).

## 2. Theorem: exact observer graph and unique second-order reconstruction

The graph has exactly **60 vertices and 960 directed edges**, with indegree=outdegree=16 at every vertex. In particular, from a fixed pair there are four choices of third axis, two signs, and two cyclic orientations, i.e. exactly 16 outgoing source choices.

For adjacent pairs \(v,w\), let \(v\triangle w\) denote their symmetric difference as sets of **signed Ports**. Then the original fixed-triad dynamics is recovered without carrying a named triad object:
\[
\boxed{(v,w)\longmapsto(w,v\triangle w).}
\]
Every \(v\triangle w\) is a valid visible pair; all 960 directed edges are valid augmented states; and the transition has **exact period 3**, because \((v\triangle w)\triangle w=v\).

Proof. Write \(v=\{a,b\}\), \(w=\{b,c\}\), with three different axes. Their union is the unique signed triad \(\{a,b,c\}\); requiring the ordered edge observation \(v\to w\) selects exactly one of its two cyclic orientations. The next visible pair is \(\{c,a\}=v\triangle w\). This proves existence, uniqueness and the update law. Conversely every C1 source and phase yields one such edge. At a fixed current \(w\), the 16 possible predecessors are inequivalent under future source-preserving shifts; an exact conditional repair needs at least \(\lceil\log_2 16\rceil=4\) bits. The previous visible pair attains this bound. No deterministic function of the *current pair alone* can represent all 16 future choices.

## 3. Theorem: an exact sevenfold three-step closure overcount

Let \(C_3(A)\) count directed 3-cycles modulo cyclic re-rooting, retaining reversal as a distinct direction. A length-three closed walk must use three distinct pair vertices. Three 2-subsets which intersect pairwise in a single Port are exactly one of two configurations:

* **True triangle:** \(\{a,b\},\{b,c\},\{c,a\}\). All three pairs lie in one signed source triad. Count: \(\binom63\,2^3\,2=\boxed{320}\).
* **Spurious star:** \(\{a,b\},\{a,c\},\{a,d\}\), with a common signed Port and four distinct axes. This changes the hidden triad between steps. Count: \(12\binom53 2^3\,2=\boxed{1920}\).

Thus
\[
\boxed{C_3(A)=2240,\qquad \operatorname{tr}(A^3)=6720.}
\]
Exactly 960 of those 6720 rooted closed walks keep one C1 source; the remaining **5760** are compositional artifacts created by independently forgetting the hidden triad before each new edge.

Every visible signed pair has exactly 16 genuine and 96 spurious rooted 3-step returns, total 112. For instance the three observations
\[
\{+0,+1\}\to\{+0,+2\}\to\{+0,+3\}\to\{+0,+1\}
\]
form a graph loop but cannot follow one oriented C1 triad: its union has four axes, not three.

## 4. Sharp observer / BRC consequence

The original C1 transition on the 960 edge states is a disjoint union of 320 oriented 3-cycles. Forgetting the previous observation at each step yields a 16-regular positive multiplicity adjacency operator \(A\), but this *does not commute with serial composition of source-preserving updates*.

If a new source branch is chosen uniformly and independently at every visible step, the ordinary Markov kernel \(P=A/16\) has
\[
\Pr(V_3=V_0\mid V_0=v)=(P^3)_{vv}=\frac{112}{16^3}=\boxed{\frac7{256}}.
\]
If a single hidden oriented source triad is selected first and preserved during all three shifts, return probability is exactly 1. The two constructions use the same 16 one-step choices but implement **different cross-time source coupling**. BRC observer/future-operation scope must therefore retain a signed Port triad or the previous/current pair whenever serial C1 rotation is queried. The minimal repair is 4 bits conditioned on the current visible pair.

All definitions and claims are invariant under the exact \(S_6\) native axis-permutation skeleton: permutations act on axes and preserve signs, set unions, intersections and symmetric differences.

## 5. Proof verification, scope and forward task

Run \`python3 research_notes/R747_X6_SIGNED_PAIR_BRC_AUTOMATON_VERIFY.py\`. The integer/set checker exhausts 60 pair vertices, all 960 edges, all 6720 rooted 3-step loops, verifies the true/star split, period-3 continuation, per-vertex counts, and 720×960=691200 axis-permutation covariance instances. Stored evidence: \`R747_X6_SIGNED_PAIR_BRC_AUTOMATON_EVIDENCE.json\`.

The result supplies an explicit, source-preserving triad **Port shift candidate** satisfying the P000 triad arity and six-axis permutation structure. It does not replace the still-open native \`TRIADIC_CLOSURE_E\` Cell/Link/Port incidence or establish compatibility with actual V29 PASS, V17/V39 holonomy, or full native rotations. Next discriminating test: extract one valid native triad event from the frozen V29/V39 definitions; compare actual port successor pairs and flow after one and three events with the C1 augmented update, and retain a minimal defect coordinate if they differ.
