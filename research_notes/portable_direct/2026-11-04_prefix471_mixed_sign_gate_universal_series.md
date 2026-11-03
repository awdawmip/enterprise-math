# PREFIX-471 — Mixed-sign gate support universality and constructive normalized BRC state bijection

Date: 2026-11-04 (Asia/Shanghai). **Status: AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED.**
Source: continuation of PREFIX-470, \`research_notes/portable_direct/2026-11-03_prefix470_monotone_gate_universal_brc_series_and_aba_horizon.md\`, immutable continuation commit \`1e6534a6deccf270a42c4f5d6c2944c2a87499fc\`; scientific pin remains \`f42f2906d77f24085c123f3ccfe9667d41caa96d\`. Current normative rules read independently from global main and Enterprise Math main. This note makes no P000/worldview amendment.

## Scientific question and exact population

PREFIX-470 proved the closed base-state count for a *sign-consistent* ordinary-letter gate \`w\`, and proposed checking whether a mixed-sign gate of the same length changes the counts. The outcome here is stronger: **for the declared base observer, gate length alone controls the complete count even with arbitrary mixtures of positive and negative letters on the same native axis.**

Work entirely in the same chart-relative native X6 ordered-path model: directions \`x=+E_1\` and five ordinary signed native pairs \`±E_2,...,±E_6\`. Every ordinary direction is allowed. The special \`x\` is allowed at the initial empty history, and after that exactly when the last \`k\` letters are the fixed ordinary gate word \`w\` (of length \`k>=1\`; \`x\` does not occur in \`w\`). All steps have nonnegative integer multiplicity. The fixed-length base BRC observation is

\[
f=(s,y_1,\ldots,y_5,A,C),\quad
s=\#x,\quad y_i=c_i^+-c_i^-,\quad
p_i=\min(c_i^+,c_i^-),\quad
A=p_2+2p_4+p_5,\quad C=p_3+p_5 .
\]

Here \`c_i^\pm\` are ordinary-letter counts, \`i=1,...,5\` denotes axes \`E_2,...,E_6\`, and the ordered paths contribute integer multiplicities. This is an explicitly declared positive-weight/valuation observer; full order, suffix state and further joint provenance are retained separately when needed.

## Theorem 1 — full Parikh feasibility (reuse, arbitrary gates)

Write \`h_i^+,h_i^-\` for the number of occurrences of the signed directions on the \`i\`th ordinary axis in \`w\`; \`sum_i(h_i^++h_i^-)=k\`. For an occupancy vector with \`s>=1\`, set \`r=s-1\`. It is realizable by a legal ordered path iff

\[
c_i^+\ge r h_i^+,\qquad c_i^-\ge r h_i^-\quad (i=1,\ldots,5).
\]

For \`s=0\` all ordinary-count vectors are realizable. Necessity follows because the \`r\` gated occurrences of \`x\` have disjoint, immediately preceding \`w\` blocks (since \`w\` uses no \`x\`). Sufficiency is the actual path \`x (w x)^r R\`, where \`R\` is any ordering of the residual ordinary letters. This uses PREFIX-470's feasibility result without repeating its previous verification.

## Lemma 2 — exact two-sign minimum and shifted displacement

Fix \`r>=0\` and one ordinary axis, with required counts \`a=r h_i^+\`, \`b=r h_i^-\`. For a chosen signed displacement \`y\`, the least possible paired cancellation count is

\[
L_{a,b}(y)=\max\{0,\ a-\max(y,0),\ b-\max(-y,0)\}.
\]

**Exact identity, all integers \`y\` and nonnegative \`a,b\`:**

\[
\boxed{|y|+2 L_{a,b}(y)=a+b+|y-(a-b)|.}\tag{1}
\]

Proof: any counts with the prescribed displacement have the form
\`c^+=max(y,0)+p\`, \`c^-=max(-y,0)+p\`. Feasible means \`p>=L\`. Conversely the unique minimal total step count with lower bounds \`c^+>=a,c^->=b\` and difference \`y\` is attained by \`c^+=a+max(d,0),c^-=b+max(-d,0)\`, where \`d=y-(a-b)\`; the total is \`a+b+|d|\`. These are exactly the two expressions on the left and right of (1).

Summing (1) over all signed displacements gives the **two-sided axis series**:

\[
\boxed{\sum_{y\in\mathbf Z} z^{|y|+2L_{a,b}(y)}
=z^{a+b}\frac{1+z}{1-z}.}\tag{2}
\]

Thus the shifted axis series depends on the *total required number of signed steps*, not their division between positive and negative directions. In particular, this calculation removes the sign-consistency premise from PREFIX-470's generating-function argument.

## Theorem 3 — all-gate closed base-state series

For every ordinary gate word \`w\` of length \`k>=1\` and every integer \`n>=0\`, the number \`B_n(w)\` of distinct observations \`f\` reached by legal ordered paths of length \`n\` has generating function

\[
\boxed{
\sum_{n\ge0}B_n(w)z^n
=\frac{(1+2z^2)(1+z)^2(1+z-z^{k+1})}
{(1-z)^8(1-z^{k+1})}.}\tag{3}
\]

**Proof.** For \`s>=1\` and fixed signed \`y=(y_i)\`, use Lemma 2 to write \`p_i=L_i(y_i)+v_i\` with \`v_i>=0\`. Then \`T=sum v_i\`, and \`(A,C)\` is the fixed known translation by \`(L_2+2L_4+L_5,L_3+L_5)\` of the set

\[
\mathcal S_T=\{(A',C'):\ 0\le C'\le T,\ 0\le A'\le 2T-C'\}.
\]

Every lattice point in this triangle occurs: choose \`v_5\` between \`0\` and \`C'\`, then \`v_3=C'-v_5\`, and use the remaining \`T-C'\` units among \`v_1,v_2,v_4\` to sweep \`A'\` through its full interval. Its size is \`R(T)=(T+1)(3T+2)/2\`, with series \`sum_T R(T)z^{2T}=(1+2z^2)/(1-z^2)^3\`, as already used in PREFIX-465/470.

By (2), summing over the five displacements contributes
\`z^{rk}((1+z)/(1-z))^5\`. The \`s=0\` term uses \`r=0\`; the \`s>=1\` terms contribute \`sum_{r>=0} z^{1+r(k+1)}=z/(1-z^{k+1})\`. Multiplication and \`(1-z^2)^3=(1-z)^3(1+z)^3\` give (3). This is an identity of formal integer power series; it holds for all \`n\`, including \`n=0\`.

As in the previous paper, the order-nine pole at \`z=1\` gives \`B_n(w)=n^8/[3360(k+1)]+O_k(n^7)\`. The formula is a counting theorem for the stated observer and is **not** a weight-mass or signed-phase equality claim.

## Theorem 4 — explicit, invertible cross-gate normalized state map

For a reachable \`f\`, let \`r=max(s-1,0)\`, \`d_i=y_i-r(h_i^+-h_i^-)\` and \`L_i=L_{rh_i^+,rh_i^-}(y_i)\`. Define

\[
\mathcal N_w(f)=(s,d_1,\ldots,d_5,A',C'),\
A'=A-L_2-2L_4-L_5,\quad C'=C-L_3-L_5.
\]

For a fixed path length \`n\` and gate \`w\` of length \`k\`, its image is **exactly**

\[
\mathcal U_{n,k}=\left\{(s,d,A',C'):
\begin{array}{l}
s\ge0,\quad T=(n-s-k\max(s-1,0)-\sum_i|d_i|)/2\in\mathbf Z_{\ge0},\\
0\le C'\le T,\quad 0\le A'\le 2T-C'
\end{array}\right\}.\tag{4}
\]

It is injective: from \`(s,d)\` recover \`y_i=d_i+r(h_i^+-h_i^-)\`; then compute \`L_i\`, and recover \`(A,C)\` by the displayed translations. For surjectivity choose any \`v_i>=0\` with \`sum v_i=T\` realizing \`(A',C')\` (the triangle construction above), set \`p_i=L_i+v_i\`, and reconstruct feasible signed counts. Theorem 1 supplies a legal ordered word. Hence \`\mathcal N_w\` is a constructive bijection.

**Corollary.** If \`w\` and \`w'\` are any ordinary gate words with equal length \`k\`, then \`\mathcal N_{w'}^{-1}\mathcal N_w\` gives an explicit bijection between their **base observer support sets**, for every length \`n\`. It generally changes the actual observed \`y,A,C\`, and it is not asserted to preserve multiplicities or future gate-language semantics.

For example, at \`n=4\`, gate \`aa\` reaches \`f=(2,2,0,0,0,0,0,0)\` through \`x a a x\`. Gate \`aA\` (where \`A\` is the opposite signed direction on that same axis) cannot reach that \`f\`, because its second \`x\` requires both signs. Yet both gates have exactly **933** distinct base observations at \`n=4\`. Thus equality of the support **cardinalities** coexists with different raw support sets. Distinguishing the two words as dynamical systems may require retaining the gate, suffix automaton, full path counts and provenance.

## Exact computation and reproducibility

The companion Python 3 standard-library certificate at \`research_notes/portable_direct/prefix471_mixed_sign_gate_certificate.py\` independently generates reachable (11-letter occupancy, KMP suffix) pairs; exhausts every weak composition of \`n\` into 11 counts and tests Theorem 1; maps every occupancy to \`f\` and to \`\mathcal N_w(f)\`; compares these sets to (3); and directly enumerates ordered words for \`n<=4\`. Gate families:
- \`k=2\`: \`aa, aA, ab, AB\`;
- \`k=3\`: \`aba, aAa, aaa\`.

Executed reference certificate (the full Python local version) tested \`n=0..7\` for all seven words, and direct word enumeration through \`n=4\`. All assertions passed. At \`n=7\`, the four k=2 gates each have 16,666 feasible occupancy vectors and 15,863 distinct base states; three k=3 gates each have 16,500 occupancy vectors and 15,697 base states. The source contains every formula and test domain. The GitHub source is the compacted equivalent implementation of the same checker; it is published as reproducible code and has not been independently executed in the remote GitHub environment.

Recorded local execution:

\`\`\`text
GATE aa k 2 n7(Parikh,B,normal) (16666, 15863, 15863)
GATE aA k 2 n7(Parikh,B,normal) (16666, 15863, 15863)
GATE ab k 2 n7(Parikh,B,normal) (16666, 15863, 15863)
GATE AB k 2 n7(Parikh,B,normal) (16666, 15863, 15863)
GATE aba k 3 n7(Parikh,B,normal) (16500, 15697, 15697)
GATE aAa k 3 n7(Parikh,B,normal) (16500, 15697, 15697)
GATE aaa k 3 n7(Parikh,B,normal) (16500, 15697, 15697)
LENGTH_INVARIANCE 2 all n=0.. 7 cases= aa,aA,ab,AB PASS
LENGTH_INVARIANCE 3 all n=0.. 7 cases= aba,aAa,aaa PASS
SUPPORT_NONIDENTITY n=4 w=aa contains (2, 2, 0, 0, 0, 0, 0, 0) w=aA excludes it; cardinalities= 933 933
CLOSED_SERIES k 2 B(n)= 1,11,65,275,933,2694,6869,15863,33797,67356,126910
CLOSED_SERIES k 3 B(n)= 1,11,65,275,932,2685,6824,15697,33295,66042,123829
ALL_CHECKS_PASS
\`\`\`

No phase, BRC–Shor or physical-heartbeat clock arithmetic was performed. Relative native X6 observations are retained as typed readouts and are not serialized as final nonnegative Cell addresses. This supports exact positive-integer BRC support reasoning; a different observer, e.g. suffix-state counts or exact weight histograms, requires its own sufficiency test.

## Next unit: codebook-free rank and unrank

Use (4) to rank/unrank \`(s,d,A',C')\` at fixed \`n,k\` without storing a complete list of reachable base keys. For each \`s\`, enumerate the admissible \`L^1\` shells of five signed integers \`d\` weighted by \`R(T)\` and derive exact prefix sums and a provably reversible integer codec. Verify its bit complexity, and test how retaining KMP suffix state alters its sufficient future-operation horizon. Separately, the arbitrary-order X6 moment-rank problem remains an independent research route.

## Control and provenance

Authenticated GitHub login: \`awdawmip\` (GitHub repo admin/push). Native gateway \`0.6.11\` status reports \`research_authority_granted=false\`, active native jobs \`5/5\`; \`em_control_tasks\` returned \`CONTROL_QUOTA\`. \`em_session_start\` returned \`STATIC_READONLY_SCOPE_DENIED\` with \`operation_sent=false\`. Accordingly active Owner, Researcher-ID and official Task CLAIM are unverified; report is unreviewed author-side Source research, not a native Result, Driver review or Foundation admission. A subsequent authorized controller can consume this immutable Source note and pursue the remaining unit under the frozen scientific pin.