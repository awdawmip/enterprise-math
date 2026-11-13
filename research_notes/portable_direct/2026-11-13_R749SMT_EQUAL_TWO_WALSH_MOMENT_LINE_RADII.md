# R749SMT — Exact equal-two-coordinate moment fibers: circuit phase transition and complementary adjacent-edge rigidity

Date: 2026-11-13 (Asia/Shanghai). Source chain R749SMQ → R749SMR → R749SMS, Draft PR #2233. Immutable scientific input pin `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`, unchanged. **Status:** author-side exact proof with exhaustive rational checker; no independent review, native V29/V39 event or shared task CLAIM claimed. This 4-bit auxiliary observer is not an X6 native spatial slice.

## 1. Objects and complete theorems

Let `G=F_2^4`, `chi_a(x)=(-1)^(a·x)`, `C={1,2,4,8,15}`, `B={3,5,6,7,9,10,11,12,13,14}`. For a retained character set U and feasible moment vector m put `F_U(m)={mu∈Delta(G):E_mu chi_a=m_a (a∈U)}` and `rho_U(m)=min_{q∈Delta(G)}max_{mu∈F_U(m)}TV(q,mu)`.

**Theorem A (two equal circuit coordinates; exact phase transition).** Set `m_1=m_2=t` and `m_4=m_8=m_15=0`. For *every real* `-1<=t<=1`, the fiber is nonempty, and

`rho_C(m)= (3/4) min{1, 2-2|t|}`.

The explicit minimax decoder is

`q_t(x)=[1+t chi_1(x)+t chi_2(x)+z(t)chi_3(x)]/16,quad z(t)=max{0,2|t|-1}`.

Thus the exact radius remains 3/4 for `|t|<=1/2`, decreases linearly to zero for `1/2<|t|<=1`, and does **not** immediately decrease when two retained moments become nonzero.

**Theorem B (two equal adjacent complementary coordinates).** Set `m_3=m_5=t` and all other B-moments zero, including `m_6=0`. This fiber is nonempty **if and only if** `-1/2<=t<=1/2`, and throughout its entire feasible range

`rho_B(m)=1/2`.

The explicit optimal decoder is `q_t(x)=[1+t chi_3(x)+t chi_5(x)]/16`.

Every unordered pair of two distinct circuit characters is equivalent to `{1,2}` under the GL(4,2) action permuting the five circuit vectors. Every adjacent pair of complementary characters (viewed as two intersecting edges of K5, e.g. `3=1⊕2`, `5=1⊕4`) is equivalent to `{3,5}`. Thus Theorems A and B apply to their respective complete symmetry orbits, with the same equal-moment input and remaining moments zero. The disjoint-edge complement orbit (XOR in C) is **not** covered.

## 2. Constructive sharp lower bounds: C

Let H be the two-dimensional subgroup annihilated by dual masks 7 and 11: `H^perp={0,7,11,12}`. On H the three characters `chi_4,chi_8,chi_15` restrict to `chi_1 chi_2`, while `chi_1,chi_2` are independent.

For any `|t|<=1/2` and each of the four disjoint cosets `g+H`, define

`nu_g(x)= [1+t chi_1(x)+t chi_2(x)]/4` on `g+H`, and zero elsewhere.

Each is a normalized nonnegative source law, has `m_1=m_2=t`, and has all three other C moments zero. Four pairwise disjoint compatible sources force every estimator q to have maximum TV loss at least `1-1/4=3/4`.

For `t>1/2`, put `tau=2t-1` and let `u_{++}` be the uniform law on the four source states satisfying `chi_1=chi_2=+1`. A pointwise nonnegative character certificate gives **for every compatible mu**

`mu(x)>=tau/4` for each x in that four-state ++ class.

For completeness, fix such x0; denote the signs at x0 of `chi_4,chi_8,chi_15` by `s_4,s_8,s_15`. Since the product of the five circuit signs is +1, for every source state x,

`4 1_{x=x0}+1-chi_1(x)-chi_2(x)-s_4 chi_4(x)-s_8 chi_8(x)-s_15 chi_15(x)>=0`.

Check it directly: within the ++ class the latter three signed signs have product +1, giving sum 3 at x0 and -1 at the other three states; outside the ++ class their allowed sum is at most 1 for a mixed 1/−1 first pair and at most 3 for the −− pair. Averaging and applying the three prescribed zero moments yields the bound.

Therefore every compatible `mu` decomposes as `mu=tau u_{++}+(1-tau)nu`, where `nu` has the boundary circuit moments `m_1=m_2=1/2` and the other C moments zero. The explicit `q_t` decomposes identically with the boundary optimal center `q_{1/2}`. The certified boundary loss 3/4 then gives the exact upper bound `(1-tau)3/4`. Conversely choose the four boundary source laws `nu_g` above; `mu_g=tau u_{++}+(1-tau)nu_g` are compatible. Their disjoint support sets `S_g=g+H` partition G, so for any q:

`sum_g TV(q,mu_g) >= sum_g (mu_g(S_g)-q(S_g)) >=4(1-tau)+tau-1=3(1-tau)`.

Hence maximum loss at least `3(1-tau)/4`, matching the upper bound. Translation by a source g with `chi_1(g)=chi_2(g)=-1` transfers the result to negative t.

## 3. Constructive sharp lower bounds: B

Since `chi_6=chi_3 chi_5`, the two binary signs with expectations t,t and product expectation 0 have joint probabilities `(1+2t)/4,1/4,1/4,(1-2t)/4`. Thus `|t|<=1/2` is necessary.

Let `H={x:chi_1(x)=+1}`, a subgroup with eight elements and `H^perp={0,1}`. For each disjoint coset `g+H`, g=0 or 1, define

`nu_g(x)=[1+t chi_3(x)+t chi_5(x)]/8` on `g+H`, zero otherwise.

This is a valid law exactly for `|t|<=1/2`. In B, the only elements congruent to mask 3 or 5 mod `H^perp` are 3 and 5 themselves: 2 and 4 lie in C. Character orthogonality therefore gives `E chi_3=E chi_5=t` and every other B moment zero for **both** disjoint laws. Hence the minimax radius is at least 1/2, and the same construction proves feasibility.

## 4. Exact upper-bound certificate for the full parameter continuum

The companion `R749SMT_EQUAL_TWO_WALSH_MOMENT_CHECK.py` is a self-contained Python standard-library `fractions.Fraction` checker. No floating point arithmetic is used.

For C, the 6×16 probability/moment matrix has full row rank 6. Every fiber extreme point is a basic feasible solution on at most 6 columns. Enumerate all `binom(16,6)=8008` column sets. For every nonsingular 6×6 basis, the candidate source distribution has entries affine in t. The finite positivity constraints cut out a rational t interval. Intersect that interval with each of `[-1,-1/2],[-1/2,1/2],[1/2,1]`, where `q_t` is affine. The TV loss of affine source and decoder is convex in t; its maximum on any interval is attained at an endpoint. Exactly test both interval endpoints against the claimed radius, whose formula is affine within the same region. This last difference is convex, so the endpoint checks prove every real t in the interval.

For B, Fourier inversion gives `mu_{t,z}(x)=[1+t chi_3(x)+t chi_5(x)+sum_{a in C}z_a chi_a(x)]/16`. The residual five-variable positivity polytope has vertices at 5 independent active inequalities, including degeneracies. Enumerate all `binom(16,5)=4368` active sets and repeat the rational affine-interval check over `[-1/2,1/2]`. The candidate `q_t` is affine and the target upper bound is 1/2, so endpoints suffice.

Local exact run returned PASS, with C: 8008 bases, 4048 nonsingular, 5056 feasible basis-region intervals, 6768 checked endpoints; B: 4368 bases, 3008 nonsingular, 1080 feasible intervals, 1504 checked endpoints. The checker validates the full moment equations, probability simplex, decoder nonnegativity and all endpoint TV inequalities.

**Scope:** exhaustive finite rational verification supplies the universal real-parameter upper inequalities via basic feasible solutions plus convexity; lower bounds are explicit analytic probability constructions. No numerical sampling, external native event operation or independent reviewer acceptance is asserted.

## 5. Frontier

This closes the equal-two-coordinate moment lines with a *new threshold at |t|=1/2* for the five-circuit, and rigidity at 1/2 for adjacent complement pairs. The full nonlinear minimax over **arbitrary** joint moment vectors remains open: especially unequal two-coordinate vectors, complement disjoint-edge pairs, three-or-more-coordinate slices, and whether a nonzero fiber produces risk strictly above the centered values 3/4 or 1/2.

Next test unequal signed pairs `(t,s)`, using the same piecewise-affine candidate `q(x)=[1+t chi_a+s chi_b+clip(0,-1+|t+s|,1-|t-s|) chi_{a⊕b}]/16` and a two-parameter exact chamber/active-set certificate. Preserve the scope of P000, the observed source masks and eventual native V29/V39 licensing as separate proof obligations.
