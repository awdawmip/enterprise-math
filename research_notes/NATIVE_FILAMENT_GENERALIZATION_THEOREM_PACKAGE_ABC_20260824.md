# Native filament generalization theorem package A/B/C

Status: `FREE_RESEARCH_GENERALIZATION_PACKAGE / EXACT_THEOREMS + PRIOR_ART_BOUNDARY_PENDING_INDEPENDENT_AUDIT / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-24`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Parent branch: `research/native-enterprise-prime-trisector-spiral-20260823`

This package extracts three parameterized theorem families from the native Enterprise filament experiments. Classical hyperplane-arrangement, Reed-Solomon/MDS, CRT and quadratic-character tools are used explicitly; no novelty claim is made for those tools themselves.

---

## A. Simple integral affine-arrangement arithmetic-lift theorem

### A.1 Setup

Let

`L_i : x + t_i y + c_i = 0`, `i=1,...,k`,

with `t_i,c_i in Z` and pairwise distinct integer slopes `t_i`.

Assume the arrangement is simple over Q:

`Delta_ijl != 0`

for every triple `i<j<l`, where

`Delta_ijl = det [[1,t_i,c_i],[1,t_j,c_j],[1,t_l,c_l]]`.

Fix a prime p such that

`p does not divide product_(i<j) (t_i-t_j)`.

Hence all slope differences remain units modulo every `p^a`.

For `R_a=Z/p^a Z`, let `m_a(P)` be the number of reduced lines passing through a parameter point P. Let

`n_a(m) = #{P : m_a(P)=m}`

for `m>=2`, and define the concurrence defect

`delta_a = sum_(m>=3) n_a(m) * C(m-1,2)`.

### A.2 Pair budget

Every pair of lines has one unique intersection in `R_a^2`, so

`sum_(m>=2) n_a(m) C(m,2) = C(k,2)`.

### A.3 Exact complement count

The union of the k lines has cardinality

`k p^a - sum_(m>=2) n_a(m)(m-1)`.

Therefore the complement count is

`N_a = p^(2a) - k p^a + C(k,2) - delta_a`.

Equivalently, if

`b_a = sum_(m>=2) n_a(m)(m-1)`,

then

`N_a = p^(2a)-k p^a+b_a`

and

`delta_a=C(k,2)-b_a`.

### A.4 Unramified persistence

Reduce first modulo p and extend scalars to `F_(p^s)`.

Because every pair intersection is uniquely solved from coefficients already in `F_p`, every pair intersection is `F_p`-rational. Thus extending to `F_(p^s)` creates no new pair or higher concurrence points and destroys none.

Hence for every `s>=1`,

`#(F_(p^s)^2 minus union L_i) = p^(2s)-k p^s + C(k,2)-delta_1`.

Thus the mod-p concurrence defect is invariant under finite-field extension.

### A.5 Ramified monotone healing

Reduction `R_(a+1) -> R_a` can only merge higher-precision intersection points, never split a higher-precision concurrence into a lower-precision nonconcurrence.

Inside one m-line concurrence block modulo `p^a`, the pair intersections at precision `a+1` form a linear-space refinement of the `C(m,2)` line pairs. The blocks containing any fixed line already contribute total `m-1` to `sum(|B|-1)`, and all other refined blocks contribute nonnegatively. Therefore

`b_(a+1) >= b_a`,

so

`delta_(a+1) <= delta_a`.

### A.6 Determinant-controlled healing depth

For any triple `i,j,l`, solve the pair `L_i,L_j`. The third line passes through that point modulo `p^a` iff

`p^a | Delta_ijl`.

Set

`nu_p = max_(i<j<l) v_p(Delta_ijl)`.

Since the arrangement is simple over Q, every determinant is nonzero and `nu_p` is finite. For every

`a > nu_p`,

no triple concurrence survives; hence all intersection points are double and

`delta_a=0`.

Thus the complete arithmetic-lift dichotomy is

`finite-field extension -> defect persists`,

`p-adic precision -> defect decreases and vanishes after explicit determinant depth`.

### A.7 Boundary

The complement-count/quasi-polynomial viewpoint for integral arrangements is classical. The theorem above is retained as an explicit determinant-depth specialization useful for the native filament arrangement, not as a claim to have invented characteristic quasi-polynomials.

---

## B. Parity-curvature locked-slope finite-quotient theorem

### B.1 Integer trajectory family

For `k>=3`, define

`epsilon_j = j mod 2`,

`eta_j^chi = (3 j^2 + chi epsilon_j)/2`, `chi in {+1,-1}`,

and native integer trajectories

`V_j(c,R) = c + 3 R j + eta_j^((-1)^R)`,

for `j=0,...,k-1`.

Let `C_k(M)` be the set of all residue words modulo M obtained from all integer parameters `(c,R)`.

### B.2 Effective shell period

A residue word depends on R only through

`chi=(-1)^R`

and

`b=3R mod M`.

Two shell parameters R,R' have the same effective pair iff

`R'-R = 0 mod 2`

and

`3(R'-R)=0 mod M`.

Let `g=gcd(3,M)`. The exact effective period is

`L_M = lcm(2,M/g)`.

### B.3 Three-coordinate injectivity

For `M>2`, the first three coordinates determine `(c,chi,b)`.

Indeed `V_0=c`. If two effective states agree at positions 1 and 2, then with `Delta e in {-1,0,1}` the difference equations are

`Delta b + Delta e = 0 mod M`,

`2 Delta b = 0 mod M`.

Hence `2 Delta e=0 mod M`. Since `M>2`, this forces `Delta e=0`, so chirality agrees, and then `Delta b=0`.

Thus the evaluation map is injective on effective parameters for every `k>=3`, `M>2`.

At `M=2`, every native trajectory collapses to a constant word.

### B.4 Exact cardinality

Therefore

`|C_k(2)|=2`,

and for every `M>2`,

`|C_k(M)| = M * lcm(2,M/gcd(3,M))`.

Equivalently

`|C_k(M)| = 2 M^2 / (2^[2|M] 3^[3|M])`.

In particular, if `6|M`,

`|C_k(M)|=M^2/3`.

The count is independent of k once `k>=3`: additional Cell coordinates increase redundancy, not trajectory dimension.

### B.5 Reduction fibers

If `M|N` and both are above the `M=2` collapse, reduction

`C_k(N) -> C_k(M)`

is surjective with uniform fibers, identified on the parameter quotient

`(c mod N, R mod L_N) -> (c mod M, R mod L_M)`.

For a new generic prime `q>3` not dividing M, the fiber size multiplies by `q^2`.

### B.6 Fixed-chirality finite-field sheet

Let q be prime with

`q>max(3,k-1)`.

For fixed chi, parity and `R mod q` are independent by CRT, and `3R` runs over all of `F_q`. After subtracting the fixed curvature offset `eta^chi`, the residue packets are exactly

`(a+bj)_(j=0,...,k-1)`.

Hence each chirality sheet is an affine translate of the `[k,2,k-1]` Reed-Solomon code. Any two coordinates are an information set; the dual minimum support is three.

### B.7 Boundary

Reed-Solomon/MDS theory and periodicity of codes generated by integral data are classical. The research-specific statement is the exact parity/slope locking selected by the native filament and its exceptional channel-2/channel-3 quotient factors.

---

## C. Two-branch quadratic transparency and CRT breaker theorem

### C.1 Abstract transparency model

Let q be an odd prime. Fix nonzero `alpha,beta in F_q` and distinct `a,b in F_q`.

For a transverse parameter h, define

`f(h)=alpha(h-a)`,

`g(h)=beta(h-b)`.

Call h transparent when both values are nonzero quadratic nonresidues:

`chi(f(h))=chi(g(h))=-1`,

where chi is the quadratic character.

Let `T_q(alpha,beta;a,b)` be the number of transparent h classes.

### C.2 Exact character-sum count

Expanding the two nonresidue indicators over `h != a,b` gives

`T_q(alpha,beta;a,b)`

`= 1/4 * [q-2 + chi(alpha(b-a)) + chi(beta(a-b)) - chi(alpha beta)]`.

Proof uses

`sum_h chi(h-a)=0`

and the standard distinct-root quadratic sum

`sum_h chi((h-a)(h-b))=-1`.

### C.3 Universal large-prime transparency

Each character term is `+-1`, so

`T_q >= (q-5)/4`.

Therefore for every prime

`q>=7`,

`T_q>0`.

Thus no single prime `q>=7` can kill every transverse class in any two-branch model satisfying the setup.

At `q=5`, since `chi(-1)=1`, the breaker condition `T_5=0` is equivalent to

`chi(alpha(b-a))=-1`

and

`chi(beta(a-b))=-1`.

Hence q=5 is the only possible universal breaker above 3 in this model.

### C.4 CRT finite-wheel principle

Let S be any finite set of pairwise distinct primes, and suppose each `q in S` has at least one transparent residue class `h_q mod q`.

By CRT there exists h satisfying all selected congruences simultaneously. The corresponding filament is transparent to every channel in S.

Therefore a finite collection of individually nonbreaking prime channels cannot collectively destroy all filaments.

Conversely, if a single channel q0 has no transparent class, every wheel containing q0 cuts every filament.

So in the independent-transverse CRT setting:

`all long filaments are cut by a finite wheel`

iff

`the wheel contains at least one universal breaker channel`.

### C.5 Enterprise corollary

For the native long filament, completing squares yields the two linear discriminant classes used in the frozen formula

`T(q)=(q-3 + Legendre(3/q)+Legendre(-3/q))/4`.

It satisfies

`T(5)=0`,

`T(q)>0 for every q>=7`.

Thus channel 5 is the unique single-prime connectivity breaker, and by CRT no finite set of later prime channels can substitute for it.

### C.6 Boundary

The quadratic-character identities are elementary classical number theory. The research-specific part is their exact coupling to native incidence connectivity and the resulting deterministic breaker classification.

---

## D. Unified mechanism

The three theorem families fit one pipeline:

`native incidence geometry`

`-> periodic curvature integer trajectories`

`-> finite quotient / affine-code carrier`

`-> divisibility zero-line arrangement`

`-> determinant-controlled exceptional channels`

`-> transparent-channel connectivity classification`.

The current strongest exact reusable statements are therefore:

1. **determinant-depth lift law** for simple integral affine arrangements;
2. **locked-mode finite-quotient cardinality law** for periodic-curvature filaments;
3. **two-branch transparency / CRT breaker law** for long-range connectivity.

## E. Novelty classification to freeze before promotion

- A general integral-arrangement complement counting theory: classical; do not claim novelty.
- B Reed-Solomon/MDS conclusion after flattening: classical once the flattening formula is known; novelty, if any, is only in the geometry-selected integer locks.
- C character-sum formula: elementary classical; novelty, if any, is only in the native connectivity coupling.
- The combined A/B/C pipeline is a research-specific synthesis and requires an independent literature audit before any external novelty claim.
