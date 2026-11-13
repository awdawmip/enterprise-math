# R749SMV — Exact nonlinear Chebyshev radii of the full two-moment Walsh five-circuit slice

Date: 2026-11-13 (Asia/Shanghai). Continuation of R749SMQ → R749SMR → R749SMS → R749SMT, Draft PR #2233. **Frozen scientific input:** \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\` (unchanged). This is an auxiliary four-bit signed-source observer model, **not** the native six-dimensional spatial geometry of P000. Author-side exact proof and reproducible exact rational finite certificate; no formal native V29/V39 event license, independent review, shared task CLAIM or canonical theorem acceptance claimed.

## 1. Exact mathematical statement

Take \`G=F_2^4\`, \`chi_a(x)=(-1)^{a·x}\`, and retain Walsh characters \`C={1,2,4,8,15}\`. For real \`t,s∈[-1,1]\`, let

\`F_C(t,s)={mu∈Delta(G): E_mu chi_1=t, E_mu chi_2=s, E_mu chi_4=E_mu chi_8=E_mu chi_15=0}\`.

Define the minimax full-source-law prediction radius in total variation

\`rho_C(t,s)=min_{q∈Delta(G)} max_{mu∈F_C(t,s)} TV(q,mu)\`.

**Theorem 1 (full signed two-coordinate exact nonlinear radius).** Every \`F_C(t,s)\` is nonempty and for **all real** \`(t,s)∈[-1,1]^2\`,

\`\`\`
rho_C(t,s) = (3/4)*min(1,2-|t|-|s|).
\`\`\`

A minimax optimal, genuinely moment-dependent probability decoder is

\`\`\`
q_{t,s}(x)=[1+t chi_1(x)+s chi_2(x)+z(t,s)chi_3(x)]/16,
z(t,s)=clip(0, -1+|t+s|, 1-|t-s|),
clip(v,L,H)=min(max(v,L),H).
\`\`\`

On the inner diamond \`|t|+|s|<=1\`, \`z=0\` and \`rho=3/4\` exactly; on the outer region, \`z=sgn(ts)(|t|+|s|-1)\` and \`rho=(3/4)(2-|t|-|s|)\`. At \`|t|=|s|=1\`, the compatible source law is unique and the radius is zero. Theorem 1 strengthens the earlier equal-coordinate line \`t=s\` (R749SMT) to **all signed unequal pairs**, including the deterministic boundary.

By symmetry, any ordered pair of distinct members of C can replace 1 and 2, with the same formula and an appropriate relabeling of the product character \`chi_{a⊕b}\`; every permutation of the five circuit vectors is induced by an invertible linear automorphism of the four-bit source dual (any four circuit members are independent).

## 2. Constructive lower bound in the inner diamond

Let the two-dimensional source subgroup \`H\` be the common annihilator of the binary masks 7 and 11. Then \`H^\perp={0,7,11,12}\` and the signs \`chi_1,chi_2\` are independent on H. Furthermore \`4⊕1⊕2=7\`, \`8⊕1⊕2=11\`, and \`15⊕1⊕2=12\`. Hence the restrictions of \`chi_4,chi_8,chi_15\` to any coset \`g+H\` are constant signs times \`chi_1 chi_2\`.

For \`|t|+|s|<=1\`, and each of the four disjoint cosets \`g+H\`, put

\`nu_g(x)=[1+t chi_1(x)+s chi_2(x)]/4\` for \`x∈g+H\`, and zero elsewhere.

All four are probability measures (pointwise nonnegativity follows from \`1-|t|-|s|>=0\`). Orthogonality on the four-state coset gives \`E chi_1=t\`, \`E chi_2=s\`, and all three other C-moments zero, for every coset. Thus all four compatible laws have **pairwise disjoint support**. For any decoder distribution q, one of the four support sets has q-mass at most 1/4; the corresponding TV distance is at least 3/4. Therefore \`rho_C(t,s)>=3/4\` throughout the inner diamond, including its boundary.

## 3. A forced common component gives the sharp outer lower bound

First suppose \`t>=0,s>=0,t+s>1\`, and set \`tau=t+s-1\`. Let \`S_{++}\` be the four source states where \`chi_1=chi_2=+1\`, and let \`u_{++}\` be uniform on these four states.

**Pointwise forcing lemma.** For any compatible mu and each \`x0∈S_{++}\`, one has \`mu(x0)>=tau/4\`.

Proof: put \`c_a=chi_a(x0)\` for \`a∈{4,8,15}\`. For every source x, the integer-valued Walsh witness

\`4*1_{x=x0}+1-chi_1(x)-chi_2(x)-c_4 chi_4(x)-c_8 chi_8(x)-c_15 chi_15(x)\`

is nonnegative. At x0 it vanishes; at each of the three other ++ source states, the three last signed characters have product +1 and sum -1, so it also vanishes. At mixed +−/−+ points the last three signed characters have product -1 and sum at most 1; at −− points their sum is at most 3. Thus the expression is nonnegative everywhere. Expectation under mu and the three zero character moments give \`4mu(x0)+1-t-s>=0\`. QED.

It follows that every mu decomposes into \`mu=tau*u_{++}+(1-tau)nu\`. When \`tau<1\`, the residual nu has zero moments on characters 4,8,15 and moment pair

\`t'=(t-tau)/(1-tau)=(1-s)/(2-t-s)\`,
\`s'=(s-tau)/(1-tau)=(1-t)/(2-t-s)\`.

Consequently \`t',s'>=0\` and \`t'+s'=1\`; the residual is in the **inner-diamond boundary fiber**. Conversely, every such nu yields a compatible mu by this affine decomposition.

For all four disjoint boundary witnesses \`nu_g\` of Section 2, define \`mu_g=tau*u_{++}+(1-tau)*nu_g\`. Their original four source cosets \`S_g=g+H\` partition G, and for any q,

\`\`\`
sum_g TV(q,mu_g)
  >= sum_g(mu_g(S_g)-q(S_g))
  >= 4(1-tau)+tau-1 = 3(1-tau).
\`\`\`

The middle bound uses \`mu_g(S_g)>=1-tau+tau*u_{++}(S_g)\` and the fact that the four S_g partition G. Hence \`max_g TV(q,mu_g)>=3(1-tau)/4\`, exactly the claimed outer lower bound.

If \`tau=1\` then \`t=s=1\` and the forcing lemma makes the source law uniquely \`u_{++}\`; the lower/upper radius is zero. If one or both moments are negative, translation by a source vector with prescribed independent signs for chi_1 and chi_2 sends the signed pair to \`(|t|,|s|)\` while keeping the other specified moments zero. Since translation is an isometry for total variation and source fibers, the same lower bound holds in every signed quadrant.

## 4. Explicit minimax decoder and the complete rational upper certificate

The candidate q in Theorem 1 is always a probability distribution. For two binary signs with expectations t and s and product moment z, their joint class masses are \`(1±t±s±z)/4\`, with the cross term signed by the product. Nonnegativity is equivalent to

\`-1+|t+s|<=z<=1-|t-s|\`.

This interval is nonempty for all \`(t,s)∈[-1,1]^2\`. Its closest point to 0 is the displayed \`z(t,s)\`. On the inner diamond q is the source-uniform-within-sign-classes law \`[1+t chi_1+s chi_2]/16\`; in the outer quadrant q decomposes with the same \`tau*u_{++}+(1-tau)*q_{t',s'}\` as the source law.

The companion **self-contained exact Fraction checker**, \`R749SMV_FULL_TWO_COORDINATE_EXACT_CHECK.py\`, establishes the matching upper bound on every fiber simultaneously, for the whole real square and not only sampled t,s. The rational certificate is finite and complete for these reasons:

1. The probability normalization and the five C moments form a full-row-rank 6×16 real system. Every extreme compatible source law is a basic feasible solution supported on at most six source states. Enumerate all \`binom(16,6)=8008\` subsets of six possible support columns. If the 6×6 basis is nonsingular, the candidate source law is an affine vector \`p(t,s)=a+b*t+c*s\` with **exact rational** coefficients; degeneracies of smaller support appear among these extended bases.
2. Split the parameter square into the eight closed rational triangles given by the four signed quadrants, each cut along \`|t|+|s|=1\`. On each triangle both the explicit q and the target formula \`(3/4)min(1,2-|t|-|s|)\` are affine.
3. Intersect each parameter triangle with all 16 rational linear halfspaces \`p_x(t,s)>=0\`. The resulting (possibly degenerate) rational polygon is exactly the set of parameters on which that basic feasible law is admissible within that chamber. A Sutherland-Hodgman rational polygon-clipper computes **all** polygon vertices.
4. Since p and q are affine within the chamber, \`TV(p(t,s),q(t,s))\` is convex there. Its difference from the affine claimed target is convex as well. A convex function on a compact polygon is bounded by its maximum over the vertices. Therefore checking the desired inequality at **every** such vertex proves it everywhere in the polygon and hence for every feasible law in every fiber in the whole real parameter square.

The executable returned \`PASS\` using solely \`fractions.Fraction\`: 8008 six-column candidates; 4048 nonsingular bases; 25,280 nonempty basic-feasible chamber polygons; 42,464 verified polygon vertices; 17 distinct rational parameter vertices. Each vertex independently checks source nonnegativity, total mass one, every specified moment, candidate decoder nonnegativity/normalization and the upper TV inequality. No float, sampling extrapolation, numerical tolerance or external solver is involved.

Thus for any compatible mu, \`TV(q_{t,s},mu)<= (3/4)min(1,2-|t|-|s|)\`. The witnesses from Sections 2–3 give the opposite bound; Theorem 1 is proved.

## 5. Scope and next frontier

The result is a **full two-coordinate slice**, not the global minimax over all five simultaneously nonzero retained circuit moments. It does not yet resolve whether the unrestricted nonlinear minimax is strictly below the proven affine minimax 5/6 (R749SMU), or whether a fiber with three-or-more nonzero moments has minimax radius greater than 3/4. The complementary ten-character family B still has a distinct disjoint-edge two-moment orbit not covered by R749SMT, and higher joint moments remain open.

Next discriminating work: (a) classify the B disjoint-edge two-moment fibers (the pair masks have xor belonging to C), (b) search exact multivariate C fibers with three nonzero moments for a strict radius above 3/4, and (c) establish a global nonlinear decoder bound, or a matching bad-fiber obstruction. If mapping into native Heartbeat World is attempted, require a real licensed V29/V39 Cell/Link/Port correspondence and explicit observer/future-operation preservation. P000 native geometry and source-provenance rules remain unchanged.

**Evidence:** \`R749SMV_FULL_TWO_COORDINATE_EXACT_CHECK.py\` (full rational finite certificate) and \`R749SMV_FULL_TWO_COORDINATE_RESULTS.json\` (actual executed PASS record). This is author-side mathematical work; independent review and native formal acceptance are pending.
