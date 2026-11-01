# D25: exact Hadamard intertwiner, sharp 13/19 precision, and differential-module obstruction

Date 2026-11-01. TASK_RESEARCH portable author-side result, lane `chatgpt-research-hourly-enterprise-math-20260923`. Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`. Frozen scientific source `c47e13e4aba0e006366f989d6334d443f6333ae3` is not modified. `AUTHOR-DERIVED / EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING`; native H0/B0 unrun. Consume, without recrediting, `20261101_hourly_d25_clausen_symmetric_square_cutoff_transfer.md` and `20261101_hourly_d25_clausen_threelevel_pullback_obstruction.md`.

## 1. Exact nonlocal source operator (proved)

Let theta=z d/dz and

`L_A=theta²-z(theta+1/6)(theta+1/3)`, `L_B=theta²-z(theta+1/8)(theta+3/8)`.

Set `u_n=(1/6)_n(1/3)_n/(n!)²`, `b_n=(1/8)_n(3/8)_n/(n!)²`, `h_n=b_n/u_n`, and `T_H(sum f_n z^n)=sum h_n f_n z^n` over Q[[z]]. The Hadamard kernel is `H=_3F_2(1/8,3/8,1;1/6,1/3;z)`. **For all formal series**,

`L_B ◦ T_H = T_H ◦ L_A` (exact over Q).

Indeed `h_n/h_(n-1)=(n-1+1/8)(n-1+3/8)/[(n-1+1/6)(n-1+1/3)]` for n≥1. Comparing the n-th coefficients of the two operators, the `n² h_n f_n` terms match and the `f_(n-1)` terms match by this ratio; constants match.

An unexpectedly simple equivalent kernel recurrence is

`h_(n+1)/h_n=9(8n+1)(8n+3)/[32(6n+1)(3n+1)]=1-5/[32(6n+1)(3n+1)]`.

Thus h_n is positive, strictly decreasing and tends to a nonzero real limit (summable O(n^-2) ratio defects), but this real smallness does not control its p-adic denominators.

For p≥13 in either target class, put `Y_p=sum_(n<p)u_n z^n`, `B_p=sum_(n<p)b_n z^n`. Then `B_p=T_H Y_p`, `L_A Y_p=e_A z^p`, `L_B B_p=e_B z^p`, and **e_B=e_A h_p exactly**, with

`e_A=-(p-5/6)(p-2/3)u_(p-1)`,
`e_B=-(p-7/8)(p-5/8)b_(p-1)`.

This transfers the full *omitted-index source*, without equating the normalized terminal coefficients and without claiming a pointwise variable substitution.

## 2. Sharp p-adic coefficient-precision law (proved)

Write `r=(p-1)/6`, `s=(p-1)/3`, and let n range over 0,...,p-1. In these classes the (1/6) and (1/3) rising factorials first encounter a p-factor at indices r and s; the two (1/8),(3/8) thresholds depend on p modulo 8.

If `p≡13 mod24`, let `a=(5p-1)/8`, `b=(7p-3)/8`; `r<s<a<b`. The five ranges `[0,r],(r,s],(s,a],(a,b],(b,p-1]` have respective `v_p(h_n) = 0,-1,-2,-1,0`.

If `p≡19 mod24`, let `a=(p-3)/8`, `b=(3p-1)/8`; `a<r<s<b`. The five ranges `[0,a],(a,r],(r,s],(s,b],(b,p-1]` have `v_p(h_n)=0,+1,0,-1,0`.

Proof: every affine progression (6j+1),(3j+1),(8j+1),(8j+3) has one p-divisible factor for 0≤j<p, each at the indicated threshold; all factors are <8p, hence have p-valuation exactly 1. Subtract denominator valuations from numerator valuations, **before** mod p reduction. In particular `min v_p(h_n)=-2` for class13 and `-1` for class19; both are attained.

For arbitrary degree <p p-integral input polynomials, computing `T_H f modulo p^m` uniformly requires input modulo `p^(m+2)` in class13, or `p^(m+1)` in class19. This is sharp: an input perturbation `p^(m+d-1)z^j` at a `v_p(h_j)=-d` coefficient is invisible modulo `p^(m+d-1)` but changes the output by a nonzero term modulo p^m. This precision lower bound is for the arbitrary-input observer, not for one exactly specified hypergeometric sequence.

Reusing *previously proved* independent terminal-source normalizations `e_A/p²≡-1/18` and `e_B/p²≡-alpha beta/64` for `alpha p≡1 mod8`, `beta p≡3 mod8`, gives `h_p≡9 alpha beta/32 mod p`, a p-adic unit. Class13: `alpha,beta=5,7`, `h_p≡315/32`. Class19: `3,1`, `h_p≡27/32`. Negative-valuation interior bands and a unit terminal source coexist.

## 3. Strengthened precise differential obstruction (proved)

The two full rank-two Gauss equations have local exponent differences `(0,1/2,1/6)` and `(0,1/2,1/4)` at 0,1,infinity. Consequently their projective local monodromy eigenvalue-ratio orders divide, respectively, 6 and 4. A nonconstant rational pullback raises each ratio to an integer ramification power; an ordinary/apparent preimage contributes only trivial monodromy. A rational 2×2 gauge isomorphism or a finite-order rational-coefficient differential operator *invertible on the two-dimensional solution spaces* intertwines analytic continuation and preserves these eigenvalue-ratio orders. Therefore no single rational pullback of either entire rank-two equation is equivalent to the other by such a full-rank matrix/differential map: source A cannot create target B's order 4, and source B cannot create A's order 6.

This strengthens the previous **scalar** no-pullback result. It does not exclude nonlocal Hadamard maps, higher-rank/tensor constructions, common algebraic correspondences with two independent maps, or finite-p congruences.

The displayed `T_H` itself cannot be a finite-order rational-coefficient differential operator acting diagonally on all monomials: any such operator must be polynomial in theta (compare falling-factorial polynomials in n), hence have polynomial-in-n diagonal eigenvalues; h_n is nonconstant but tends to a finite positive limit, so cannot be a polynomial.

## 4. Original 216 source and BRC preservation

Reusing the exact finite Clausen identity, `U_p=sum_(n<p)(1/2)_n(1/3)_n(2/3)_n/(n!)³ z^n`, `K_p=Y_p²-U_p`, `W_p=(6theta+1)U_p`. The **exact source-preserving two-port diagram** is

`Y_p --T_H--> B_p`, `(Y_p,K_p) --[square, subtract, 6theta+1]--> W_p`,

equivalently `W_p=(6theta+1)[(T_H^(-1)B_p)²-K_p]` over Q. The cutoff K_p remains an independent signed high-index port. Nothing here identifies original `W_p(1/2)` with a single auxiliary value `B_p(1/9)` or proves the original p³ conjecture.

BRC: `COMPOSE_APPLIED`. Carrier is the labeled rational coefficients `(u_n,b_n,h_n,k_n)`, the index/prime-class tags, valuations, low-band resonant seam and terminal sources; observer is the precise future operator, Hadamard map and mod p^m output. A total-only or insufficient-precision quotient loses exact data; there is a quantified two-digit versus one-digit repair requirement. No native X6 embedding is claimed.

**Next unit:** derive a *special-value* 216-at-1/2 versus 2304-at-1/9 trace/moment transfer, retaining K, the class-dependent Hadamard precision and the original Delta_p-R_p / Frobenius source ports. A coefficientwise bridge is not a pointwise special-value theorem.

Checks: independently recurred u,b,h unit/valuation data for 107/107 primes p≤3000 in classes13 (53) and19 (54), all threshold bands and h_p formula PASS; exact Fraction spot checks p=13,19,37,61. Script and full local proof available in the accompanying run bundle. Author-side proof is not independently reviewed.

Control: Gateway 0.6.11 current status had `research_authority_granted=false`, `executor_binding_configured=false`, `UPSTREAM_CODE_REVIEW_REQUIRED`. Own historical recovery #6637 and rejected continuation #6638 preserve exact receipts. Support #1558 controls recovery; native H0/B0 #1559 remains pending. No native CLAIM, OPEN, Source checkpoint or independent mathematical admission is asserted.