# R5 / EC48J — An exact third supporting normal for the reversed-collision BRC tree

**2026-10-27. Author-side portable mathematical research. Status: UNREVIEWED / NOT_ADMITTED.** No native task CLAIM, Result, independent Driver review, Working Truth, or Foundation promotion is asserted. This is an auxiliary finite positive-weighted two-source BRC observation model, not native X6/Heartbeat dynamics.

## Sources, authority, and carry-forward

GLOBAL_KNOWLEDGE_V1 fixed read snapshot: awdawmip/chatgpt-global-knowledge main@df354899f3e5831d052e05de65d9ec10f4b207d2, including canonical bootstrap/manual, P000, ACTIVE worldview, TASK_RESEARCH route, mathematics and BRC policies. Project main read snapshot: awdawmip/enterprise-math@f8fcea6dd1783b578aaf434aac68b7a1388e49d6. Current portable protocol: docs/PORTABLE_RESEARCH_PROTOCOL.md and docs/AUTONOMOUS_RESEARCH_OPERATIONS.zh-CN.md. Locked P000 is six native spatial axes plus separately typed time, with a three-axis X6 restriction (not an independent native plane); no P000/worldview claim is changed here.

Parent immutable frontier: 3d3002c811f4c23ed3a58db41ee42cd631583c18, research_notes/r5_reversed_collision_second_normal_20261027_r4/PROOF.md and NEXT_TASK.md. It excluded (s_a,s_b)=(1/10,2/5) by the second normal (298,376,37,-17) but left (1/5,1/4) for an exact hull test. This work resolves that nominated pair without repeating its earlier proof. Recent compulsory-arrival and ten-leaf optional-stop results have different scopes.

## Exact finite BRC model and observation

The full (source Q mass, likelihood ratio L=P/Q, stopping time) information at nonterminal histories is:

| h | Q mass | L | time |
| --- | ---: | ---: | ---: |
| root | 1 | 1 | 0 |
| a | 1/2 | 3/2 | 1 |
| b | 1/2 | 1/2 | 1 |
| ax | 1/4 | 1 | 2 |
| ay | 1/4 | 2 | 2 |
| bu | 1/8 | 1 | 2 |
| bv | 3/8 | 1/3 | 2 |

The branches are root→(a,b), a→(ax,ay), b→(bu,bv). At ax, the three time-3 leaves have conditional Q weights (s_a,1−2s_a,s_a) and likelihood ratios (1/2,1,3/2). At bu, they have conditional Q weights (s_b,1−2s_b,s_b) with the same leaf ratios. ay and bv have one time-3 child each, of ratio 2 and 1/3. For 0<s_a,s_b<1/2 the Q and P weights of every leaf are strictly positive and the tree conserves both source masses exactly.

At each nonterminal the action is P (stop and decide P), Q (stop and decide Q), or C (continue). A full observer knows the physical history. A seedless observer sees only (time,L) and must assign the **same local action rule** to ax and bu; it has fresh local private randomization but no persistent shared seed. The declared four-observer vector, for time horizon at most 3, is

\[
O=\big(P[\operatorname{decide}Q],\ Q[\operatorname{decide}P],\ \mathbb E_P[\tau],\ \mathbb E_Q[\tau]\big).
\]

The positive weighted branch carrier retains P/Q mass, likelihood ratios, the two different future kernels, and labeled provenance until the compression test. The signed objective below is a linear *readout*, not a signed BRC mass or amplitude.

## Theorem: new separating normal and an open neighborhood

Consider the rational signed linear functional

\[
J(O)=304 O_1+212 O_2-20 O_3+33 O_4.
\]

Let \(V_{\rm full}\) and \(V_{\rm seedless}\) be its minima over full-history and seedless policies.

**For every real pair in the strictly positive closed rectangle**

\[
\frac{19}{100}\le s_a\le\frac{21}{100},
\qquad
\frac{6}{25}\le s_b\le\frac{13}{50},
\]

we prove exactly

\[
V_{\rm full}(s_a,s_b)=\frac{1571}{8}-\frac{15}{2}s_b
\quad\text{and}\quad
V_{\rm seedless}(s_a,s_b)-V_{\rm full}(s_a,s_b)\ge\frac{1}{10}>0.
\]

At the previously unresolved pair \((s_a,s_b)=(1/5,1/4)\) the **exact** minima are

\[
\boxed{V_{\rm full}=\frac{389}{2},\quad
V_{\rm seedless}=\frac{779}{4},\quad
V_{\rm seedless}-V_{\rm full}=\frac14}.
\]

Thus the attainable four-observer convex hulls differ at every parameter pair in this rectangle. A strict linear support gap also precludes equality of the original images, but makes **no** assertion about the detailed shape or membership of those original possibly nonconvex images.

## Load-bearing proof

At a node with Q mass q, ratio r and time t, the cost of stopping with decision Q is

\[
q[304r+t(-20r+33)],
\]

while decision P costs

\[
q[212+t(-20r+33)].
\]

At terminal time 3, the optimal decision depends only on r, not predecessor: choose Q for r=1/3 or 1/2 and choose P for r=1, 3/2 or 2. Therefore the same terminal Bayes labels are optimal for *both* policy spaces for this linear support; full-history terminal decision flexibility cannot lower the cost further.

Each deterministic nonterminal policy assigns one of P,Q,C to the seven histories (root,a,b,ax,ay,bu,bv), yielding exactly \(3^7=2187\) full policies. The seedless subset, constrained by action(ax)=action(bu), contains \(3^6=729\) policies. For a fixed policy its total signed cost is affine in (s_a,s_b), since no root-to-terminal path visits both parameterized kernels, and all stopping/source costs are rational-affine.

The full-history table

\[
(C,C,C,P,C,C,Q)
\]

has the cost \(F=1571/8-(15/2)s_b\). The attached exact standard-library Python program calculates all 2187 full affine costs and verifies at the four rectangle corners

\[
v-F\ge0
\]

for every full policy v: precisely 8748 rational inequalities. Because each difference is affine, satisfaction at all corners proves the inequality for **all real parameters throughout the rectangle**, not merely the test vertices. The exhibited table attains F, hence F is the full optimum everywhere in the rectangle.

The same program checks for every one of the 729 seedless deterministic policies w, at every corner,

\[
w-F\ge 1/10,
\]

precisely 2916 further exact rational inequalities. The affine-corner argument again applies on the entire rectangle. For a finite-horizon linear objective, local fresh behavioral randomization cannot reduce the minimum below the deterministic tables: expected costs are multilinear in the independently used class-action probabilities, and the minimum of such a function over each action simplex is attained at a vertex. Each (time,L) class occurs at most once on a path, so the shared collision rule is represented by a common policy-table action. Hence the stated uniform lower separation bound holds for the claimed seedless policy class.

All \(8748+2916=11664\) comparisons are exact Fraction operations. The checker also verifies exact P and Q conservation symbolically and obtains the same pointwise minima from independent backward Bellman recursion; it uses no floating-point tolerances. The verified source is VERIFY.py and its captured run output is EXACT_OUTPUT.txt in this directory.

## Exact four-coordinate witnesses and information-loss mechanism

At (s_a,s_b)=(1/5,1/4), the full policy above produces

\[
O_{\rm full}=(9/64,\ 19/32,\ 21/8,\ 19/8),\qquad J(O_{\rm full})=389/2.
\]

The legal seedless policy (C,P,C,C,P,C,Q), with ax and bu both assigned C, produces

\[
O_{\rm seedless}=(9/64,\ 19/32,\ 11/8,\ 13/8),\qquad J(O_{\rm seedless})=779/4.
\]

The minima are certified over *all* policies (the independent Bellman seedless conditional values for collision action P,Q,C are respectively 779/4,195,779/4). These two optimal witnesses agree exactly in both error probabilities but disagree in the two expected stopping times. Therefore preserving current errors alone is not an exact observer/future-operation factorization certificate for discarding the ax/bu history distinction. The full supporting-normal gap, not just the comparison of these two witnesses, establishes the loss.

## Boundaries and next unit

The result is a new **author-side exact positive BRC support-separation theorem**, with complete finite-policy and all-real rectangle certificate. It does not solve the full two-parameter support-hull classification, the nonlinear raw seedless-image membership question, or the general \(K_{\rm seed}=K_{\rm hull}\) problem. It grants no native X6 / three-dimensional slice / heartbeat physical correspondence without an explicit typed embedding, third-coordinate semantics, readout and relation-preservation theorem. It is not Source-native Result admission or independent mathematical review.

Next: compute the exact global lower-envelope chambers of the 2187 full and 729 seedless affine policy values for this **third normal**, classify its entire strict-gap locus and boundaries in 0<s_a,s_b<1/2, then test rational candidates outside the union of already certified normal regions. Use further normals or complete facet/Bellman inclusion rather than interpreting a zero gap for one normal as hull equality.
