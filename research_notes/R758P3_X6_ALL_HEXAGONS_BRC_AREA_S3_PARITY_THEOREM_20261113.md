# R758P3 — Complete six-step X6 BRC area–frame classification and rooted parity repair

**Status:** proved algebraic/combinatorial theorem and complete finite enumeration in a *declared candidate* spatial-link-to-\(S_3\) transport. Author-side mathematical contribution; no new native \`TRIADIC_CLOSURE_E\` event, formal Source Result, independent review, P000/worldview change or active Task CLAIM is asserted.

**Source lineage:** R758P (PR #2200), R758P2 (PR #2201, immutable evidence commit \`7ab2bdd2c104f80cbf494c2be492001a50e749b0\`), with relevant V39 compositional convention from R757. Frozen scientific input remains \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`. This note extends R758P2 from the **192 simple hexagons** to **all 720 balanced six-step words**, including repeated intermediate Cells.

## 1. Exact domain and group convention

Select three distinct axes in the native X6 discrete Cell space, denoted 0,1,2 only *within this three-dimensional research slice*. Consider the \`6!=720\` words containing each token \`+0,-0,+1,-1,+2,-2\` exactly once. All words return to the chosen Cell. Their projection to axis labels is a double-occurrence word, with \(6!/(2!)^3=90\) possible label arrangements; each has \(2^3\) sign decorations.

Use the **candidate** frame link assignment \(\tau_a=s r^a\) for \(a=0,1,2\), where \(s=(01)\) and \(r=(012)\) in \(S_3\), \(s^2=e\), \(r^3=e\), and \(srs=r^{-1}\). Reverse coordinate steps have the same involutive \(\tau_a^{-1}=\tau_a\). Later steps multiply on the left. For \(w=(a_1,\dots,a_L)\), define \(H(w)=\tau_{a_L}\cdots\tau_{a_1}\). Coordinate signs matter for signed areas but not for these declared axis-involutive increments.

For a closed six-step word, the integer signed projected-area observer is
\[
\mathcal A(w)=(\mathcal A_{01},\mathcal A_{02},\mathcal A_{12}),\quad
\mathcal A_{ab}=\sum_{\ell:\,a_\ell=b} x_a(\ell-1)\Delta x_b(\ell).
\]
Every component belongs to \(\{-1,0,1\}\); the full native slice still has three coordinates. Define \(N(w)=\|\mathcal A(w)\|_0\).

## 2. New exact theorem: all 720 words

**Theorem 1 (all-path area–holonomy criterion).** For every one of the 720 words,
\[
\boxed{H(w)=e\iff N(w)\in\{0,3\}},\qquad
\boxed{H(w)\in\{r,r^{-1}\}\iff N(w)\in\{1,2\}}.
\]
In particular, *simple path* was not necessary for this form of the area–frame criterion. The previous simple-only statement is recovered by restricting \(N\) to 2 or 3.

**Proof.** In the cyclic axis-label word, connect the two positions of each axis with a chord. Two chords cross exactly when their four occurrences interleave. Because each signed axis occurs once positively and once negatively, direct substitution in the signed area sum gives \(\mathcal A_{ab}\ne0\) exactly when chords \(a,b\) cross (then the value is \(+1\) or \(-1\)). Hence \(N\) is the edge count of the three-vertex chord intersection graph \(\Gamma\).

For any axis word (of *arbitrary length*), define
\[
q(w)=\sum_{j=1}^{L}(-1)^{j-1}a_j\bmod3,\qquad p(w)=L\bmod2.
\]
Using \(s r^a s=r^{-a}\), direct induction yields
\[
\boxed{H(w)=s^{p(w)}r^{q(w)}}.
\]
For \(L=6\), let \(n_a\) count occurrences of axis \(a\) at odd positions. Then
\(q=2\sum_{a=0}^2 a n_a\pmod3\), as \(\sum a=3\). Since \(\sum n_a=3\) and each \(n_a\in\{0,1,2\}\), \(q=0\) holds precisely when \((n_0,n_1,n_2)=(1,1,1)\): the other six patterns are the permutations of \((2,1,0)\) and have nonzero residue. Thus \(H=e\) iff the two occurrences of **each** axis have opposite positional parity.

For one chord, its endpoints occupy opposite parity positions iff the number of intervening endpoints is even. Modulo 2 this number equals the degree of that vertex in \(\Gamma\): each other chord with two or zero endpoints inside contributes an even number; a crossing chord contributes one. Hence all axis pairs have opposite positional parity iff every degree in \(\Gamma\) is even. A simple graph with exactly three vertices has all even degrees iff it is empty or a triangle. Equivalently, \(N=0\) or \(N=3\). QED.

## 3. Complete signed-area fibers and minimal repair

**Theorem 2 (exact observer fibers).** The 720 words yield **all 27** possible signed-area vectors. Their frame-fiber distributions are exactly:

| \(N=\#\) nonzero areas | distinct signed-area vectors | words per vector | \(e\) per vector | \(r\) per vector | \(r^{-1}\) per vector | words total |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 1 | 240 | 240 | 0 | 0 | 240 |
| 1 | 6 | 48 | 0 | 24 | 24 | 288 |
| 2 | 12 | 12 | 0 | 6 | 6 | 144 |
| 3 | 8 | 6 | 6 | 0 | 0 | 48 |
| **Total** | **27** | — | **288** | **216** | **216** | **720** |

**Counting proof.** The 90 unsigned double-occurrence axis words split by chord-crossing count as \(30,36,18,6\) for \(N=0,1,2,3\). Here: \(N=0\) is one of the five noncrossing perfect matchings on six cyclic slots, with \(3!\) axis labels; \(N=3\) is the unique fully crossing pairing of six cyclic slots, also with \(3!\) axis labels. R758P2's inclusion–exclusion proves that exactly 24 unsigned words are simple and its chord classification gives \(N=2\) for 18 and \(N=3\) for 6 of these. The remaining number is \(90-30-18-6=36\) for \(N=1\). Each axis word admits eight oriented sign assignments. The precise signed-vector partitions in the table follow from the complete finite enumerator bundled with this note; its loops cover each of the six distinguishable signed tokens exactly once. Cyclic rotation of a closed spatial path preserves every signed area, while the same rotation conjugates \(H\) by one transposition, interchanging the two nontrivial three-cycles. This gives the equal \(r/r^{-1}\) counts in every \(N=1,2\) fiber. QED.

Consequently, the area observer determines the **conjugacy class** of the final frame on all 720 paths. For \(N=1\) or \(2\) it loses exactly one binary frame-orientation choice, while for \(N=0\) or \(3\) it loses none. Under the explicitly declared *uniform distribution on all 720 signed words*,
\[
\boxed{\mathsf H(H\mid\mathcal A)=\frac{288+144}{720}=\frac35\ \text{bit}}.
\]
This conditional entropy is a model-specific source statistic; it is not a universal information bound for native dynamics.

**Theorem 3 (constructive parity-bit repair).** From \(\mathcal A\), form the graph \(\Gamma\) with edge \(ab\) iff \(\mathcal A_{ab}\ne0\). For \(N=1,2\), let \(a<c\) be its two odd-degree vertices and let
\(\beta(w)=1\) if both occurrences of \(a\) lie in odd-numbered positions of the rooted word, and \(\beta(w)=0\) if both lie in even-numbered positions. Then
\[
\boxed{q(w)=\begin{cases}2(a-c)\pmod3,&\beta=1,\\2(c-a)\pmod3,&\beta=0.\end{cases}}
\]
The graph determines the odd-degree pair, and the remaining even-degree chord contributes one occurrence to each positional parity. The odd-degree pair contributes two odd occurrences from one axis and two even occurrences from the other, proving the formula. Thus \((\mathcal A,\beta)\) recovers the based frame **without computing the full group product**. Because both \(r,r^{-1}\) occur in every \(N=1,2\) signed-area fiber, one binary repair bit is also necessary on each of these fibers. For \(N=0,3\), take \(q=0\) with no repair bit.

## 4. A future-composable six-state BRC frame register

**Theorem 4 (exact transport quotient).** For arbitrary finite axis words \(u,v\), including words which do not return spatially,
\[
p(uv)=p(u)+p(v)\pmod2,\quad
\boxed{q(uv)=q(u)+(-1)^{|u|}q(v)\pmod3}.
\]
The register \((p,q)\in\mathbb Z_2\ltimes\mathbb Z_3\) is an exact six-state compositional frame carrier, with group readout \(s^p r^q\). On **even-length loops**, \(p=0\) and the three-state \(q\) register composes additively modulo 3. For frame-only outputs under arbitrary future concatenations, two words with the same \((p,q)\) give identical future frame transport, and words with different \((p,q)\) differ already at their present frame; thus this quotient is minimal among exact deterministic frame observers. For a joint spatial-area/frame observer, retain \(\mathcal A\) and the conditional repair information rather than discarding spatial structure.

**Scope:** This is a theorem about a specified \(S_3\) candidate connection and a three-axis slice within X6. The next native bridge must independently determine the legal force incidence, Cell/Link/Port typing, scheduler, and allowed V39 based-loop increment; a unit spatial step is not asserted to be an admitted V39 frame event.

## 5. Validation and next step

The companion Python stdlib checker exhausts all 720 signed words, all 27 area fibers, all frame outputs, all conditional parity-bit repairs and 1,093 arbitrary axis words of length 0–6 for the \((p,q)\) formula and future-concatenation law. The checker asserts the exact numerical table. Its output is summarized in the matching JSON evidence artifact.

**Next discriminating native question:** Obtain one actual accepted \`TRIADIC_CLOSURE_E\` Cell/Link/Port incidence and an explicitly authorized V39 increment. Test whether that increment admits this three-transposition quotient or provides a different based-loop frame action. If it does, derive the correct retained residual/conditional repair on the admitted event domain. Otherwise retain this exact finite transport result as a separate model comparison. Do not infer primitive spatial movement from a three-force balance event.
