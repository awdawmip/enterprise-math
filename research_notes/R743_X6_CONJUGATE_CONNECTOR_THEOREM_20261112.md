# R743 — factorial hidden connector histories and conjugacy-limited V39 frame observability

**Date:** 2026-11-12 Asia/Shanghai. **Class:** author-side exact X6/BRC combinatorial theorem, not a native TRIADIC_CLOSURE_E realization.  
**Parent:** RS-X6-TRIADIC-CLOSURE-DYNAMICS / publication TP2-8B7E13C5904A2D6F1142. **Frozen scientific inputs:** `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`. **Predecessor:** R741 PR #2145, commit `82d53d29e6c130b8381c7168bf6632c58ee9f148`. Comparison method: V39 current-plus-holonomy note (contemporary main, not silently repinned frozen science).

## 1. The 24-history native-X6 construction

Work in a *chosen* native X6 affine Cell chart, with six signed unit primitive steps. These are composite **coordinate paths**; no Euclidean force-vector sum or native triadic physical closure is asserted.

Choose connector axes 0,1,2,3 and square axes 4,5. For each permutation σ of (0,1,2,3), let
$$
c_\sigma=(+\sigma_1,+\sigma_2,+\sigma_3,+\sigma_4),\qquad
L=(+4,+5,-4,-5),\qquad
w_\sigma=c_\sigma Lc_\sigma^{-1},
$$
where the inverse connector is the geometrical reverse of the four original unit steps, in opposite order. Hence every word has 12 steps, one positive and one negative occurrence of each native axis. Each word returns to the chosen starting Cell, and no adjacent pair of steps is mutually inverse. Distinct σ give 4!=24 distinct rooted BRC path branches.

Define the integer oriented coordinate current for the positive reference edge (u,i):
$$
j_w(u,i)=N_w(u\xrightarrow{+i}u+e_i)-N_w(u+e_i\xrightarrow{-i}u).
$$
Every connector contributes one positive and one negative traversal of the *same edge*, hence `j(c_sigma)+j(c_sigma^-1)=0`. The square L always lies at the same Cell offset (1,1,1,1,0,0), independent of σ. Consequently
$$
\boxed{j(w_\sigma)=j(L\text{ at }(1,1,1,1,0,0))\quad\text{for all 24 }\sigma.}
$$
The common current has exactly four nonzero edges. All first-occurrence signs Q are +, so (j,Q) has a 24-element fiber. The parity ε of the six-axis first-occurrence permutation equals sign(σ), hence 12 paths have ε=+ and 12 have ε=−. This is an **exact information-loss witness on nonbacktracking paths**, extending R741's six-way order and two-way connector constructions.

More generally, on any fixed n-axis signed lattice carrier with r connector axes and two distinct square axes, 0≤r≤n−2, the r! paths cσ L cσ^-1 share nonzero j and Q. In P000's native X6, r≤4 and the maximum constructed fiber is 24.

## 2. A group-theoretic holonomy bottleneck

Let a fixed based network have invertible transport in an arbitrary group G, and let g=h(L) be the square transport. With V39's chronological composition `h(gamma;r)=h(r)∘h(gamma)`, the complete path transport is
$$
\boxed{h(w_\sigma)=H_\sigma^{-1}gH_\sigma,\qquad H_\sigma=h(c_\sigma).}
$$
Thus all r! conjugate-connector histories have holonomy in the *one conjugacy class* `Cl_G(g)`. For a finite group G, at most |Cl_G(g)| distinct (j,h) values can occur. By the pigeonhole principle, **some** fiber must have cardinality at least
$$
\boxed{\left\lceil\frac{r!}{|\operatorname{Cl}_G(g)|}\right\rceil.}
$$
If the additional first-axis orientation parity ε is retained, at most `2|Cl_G(g)|` joint values can occur, giving the corresponding bound
$$
\boxed{\max_{j,Q,h,\varepsilon}|\text{fiber}|\ \ge\
\left\lceil\frac{r!}{2|\operatorname{Cl}_G(g)|}\right\rceil.}
$$
These bounds are combinatorial and do not suppose every permutation has the same frame transport.

For a genuine `S3` transport, its conjugacy classes have sizes 1 (identity), 2 (three-cycles), or 3 (transpositions). For r=4, therefore, some `(j,Q,h)` fiber has at least 8 paths and some `(j,Q,h,epsilon)` fiber at least 4 paths. If the later observation asks for the *full original word*, this requires at least 3 and 2 additional bits, respectively, in the worst case. The current alone requires at least `ceil(log2 24)=5` bits.

For V39's declared future language `L_JH`, the exact (j,h) quotient remains operation-safe: it does not query raw event order. Our new lower bounds quantify the extra provenance needed for the expanded language that does.

## 3. Sharp finite S3 realization on the six-axis example

Write a permutation as its ordered image tuple. Put forward connector-axis transports
$$
H_0=(0,1,2),\quad H_1=(0,2,1),\quad H_2=(1,0,2),\quad H_3=(2,1,0)
$$
and the square generator transport `g=(1,0,2)`. Reverse oriented edges receive the inverse transport; assign g to one square edge and identity to its remaining three edges. This defines an invertible edge-transport model on the selected based graph.

For every σ, compute `H_sigma` from the four connector transports, then `H_sigma^-1 g H_sigma`. Exact permutation enumeration shows: all 24 paths share one current; ε partitions 12/12; the three possible transpositions each occur exactly 8 times; the six joint (ε,h) cells each occur exactly 4 times. Hence the two-bit final residual bound is **sharp in this explicit S3 connection**, and the three-bit bound without ε is sharp there as well.

The accompanying checker enumerates *all* 24 connector orders; asserts token identity, nonbacktracking, full Cell return, common four-edge integer current, first signs, parity and every S3 fiber. All arithmetic and group operations are exact.

## 4. BRC observer/future operation and X6 symmetry

Population: 24 individually labeled ordered source branches wσ, with positive count 1 per branch. Coordinate-current j is a signed integer observer, not positive BRC mass. S3 holonomy h is a separate noncommutative frame observer. The target expanded future operation is recovery or querying of the full ordered primitive-step history. The least additional binary code **for the six-class sharp example** has exactly 2 bits after (j,Q,h,epsilon), because each joint fiber has size 4.

Relabeling the six native axes transports the path family, currents, and its first-occurrence orientation relative to a correspondingly relabeled frame. The theorem concerns a declared six-axis restriction of X6 and does not introduce an independent lower-dimensional native world. The action of an odd axis relabeling changes the orientation sign in the expected way.

## 5. Status and next experiment

**Proved:** factorial source collapse under signed current; conjugacy-class bounds; sharp S3 six-axis construction. **Exact tested domain:** all 24 four-connector permutations; a separate Python standard-library check independently agreed. **Not yet established:** whether the real frozen `TRIADIC_CLOSURE_E` event semantics admits this connector-square packet, its inverse edge law, a root-preserving S3 transport and the selected V29 PASS/V39 mapping. These are explicit native-model correspondence questions.

**Smallest follow-up:** read the frozen triadic-balance and Cell/Link/Port definitions and instantiate one *actual legal* closure event with a specified native update. Compare two event orders with equal projected current; check whether their true V17/V39 transport is a path-groupoid homomorphism and whether their V29 status changes. Preserve the P000 frozen pin and require a real publication/CLAIM for any shared task ownership mutation.
