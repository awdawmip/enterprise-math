# D25 — finite p-local rational Green evaluation and a noncollapse witness

Date: 2026-10-31. Mode: AUTHOR-SIDE / TASK_RESEARCH / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. This is an independently derived portable mathematics artifact, not a Source-native task checkpoint, CLAIM, Result or native H0/B0 experiment.

## Frozen context and exact question

Scientific source pin: c47e13e4aba0e006366f989d6334d443f6333ae3 (unchanged). Parent target: original fixed-216 A_p = p (mod p^3) for primes p=13,19 (mod 24), still **OPEN**. Task publication TP2-B6F4FC938FF94941C1B7; accepted D24/UR is an input, not re-proved. The previous proved Gauss jet differential/Green identity is at project commit 97559d4bd4f3bb330c34b91d8950ab4ec20ffd18. The signed overdegree R is independently sourced at 2cebb4700946f7f3ef5c7b54415573d301f83810.

Previous next obligation was to produce a **finite p-local rational evaluation at z=1/2** instead of substituting z=1/2 into a non-converging formal series. This note discharges exactly that mathematical sub-obligation and records its limit.

## Theorem — finite Green evaluation with all denominator units

Fix a prime p=6l+1>=7, M=3l, and let
\[
K_k(t)=\frac{(-l+t/6)_k(-2l+t/3)_k}{(k!)^2},\quad
J_r(z)=\sum_{0\le k<p}[t^r]K_k(t)z^k,\quad r=0,1,2.
\]
Write u_i=[z^i]J_0, v_i=[z^i]J_1, w_i=[z^i]J_2; thus deg J_0<=l and deg J_1<=2l. Define
\[
D=\tfrac12 z\tfrac{d}{dz}-\tfrac{2l}{3},\quad
\gamma=20l^2w_{p-1},\quad
F(z)=J_0(z)\big(DJ_1(z)+J_0(z)/18-\gamma z^{p-1}\big).
\]
Let f_k=[y^k]F(1-y), 0<=k<=7l. Define the signed rational Green current
\[
\Phi(z)=z(1-z)^{-3l}(J_0J'_2-J_2J'_0).
\]
Then over Q, hence over the p-local ring Z_(p), **all** of the following hold:

(1) **Residue cancellation**: f_{3l}=0 exactly (not merely modulo p).

(2) **Finite rational evaluation**:
\[
\boxed{\displaystyle
\Phi(1/2)=\sum_{\substack{0\le k\le7l\\k\ne3l}}
f_k\,\frac{1-2^{3l-k}}{k-3l}
=2^{3l}\left(J_0(1/2)\,\theta J_2(1/2)
                  -J_2(1/2)\,\theta J_0(1/2)\right),
}
\]
where theta=z d/dz. Every integer denominator k-3l in this formula is nonzero with absolute value <=4l<p, and powers of 2 are p-units. The formula is therefore a p-local finite certificate at any required p-adic precision. The f_k are **finite** binomial transforms of the explicitly retained J_0,J_1 and the distinct terminal gamma:
\[
f_k=(-1)^k\sum_{j=k}^{7l}\binom{j}{k}[z^j]F(z).
\]
No formal infinite-series evaluation or analytic exchange of sums is used.

(3) **Top-jet/terminal source identity**. Put
\[
S_p=\sum_{i=0}^{l}u_i\binom{p-1+i}{3l}.
\]
Residue cancellation is equivalently the exact rational identity
\[
\boxed{\gamma S_p=\frac l3\,u_l v_{2l}}.
\]
Furthermore S_p == (-1)^l (mod p), so S_p is a p-unit. Thus the terminal is reconstructible from first-jet **endpoint coefficients** and an explicit p-unit, within the declared endpoint-observer scope; it does not imply lossless erasure of the original second-jet state for other operations.

### Proof

By the previously proved exact truncated differential equations,
\[
L_0J_0=0,\quad L_0J_1=zDJ_0,\quad
L_0J_2=zDJ_1+zJ_0/18-\gamma z^p,
\]
with L_0=theta^2-z(theta-l)(theta-2l). The exact Green integrating-factor subtraction gives
\[
\Phi'(z)=(1-z)^{-3l-1}F(z).
\]
This is an identity of rational functions; \Phi(0)=0. Substitute y=1-z and expand the **polynomial** F(1-y)=sum f_k y^k. The right side is sum f_k y^{k-3l-1}. A derivative of a rational function has zero (1-z)^{-1} coefficient in its Laurent expansion at z=1; hence f_{3l}=0. All remaining monomials integrate *finitely*, giving
\[
\Phi(z)=\sum_{k\ne3l}f_k\,\frac{1-(1-z)^{k-3l}}{k-3l},
\]
where the constant is fixed by \Phi(0)=0. Substitute z=1/2 and rewrite the Wronskian via theta to obtain (2). Since deg F<=max(3l,(p-1)+l)=7l and 3l<=7l, all denominators meet the bound above.

For (3), [z^{3l}]J_0(DJ_1+J_0/18)=(l/3)u_l v_{2l}: J_0J_1 only reaches degree 3l through the unique pair (l,2l), while J_0^2 has degree <=2l. The z^{p-1}J_0 term contributes -gamma S_p to [y^{3l}]F(1-y), with common factor (-1)^{3l}. Thus f_{3l}=0 gives gamma S_p=(l/3)u_l v_{2l}. Modulo p, for 1<=i<=l each binomial (p-1+i choose 3l) contains exactly one numerator multiple of p and has a p-unit denominator; only i=0 remains, (p-1 choose 3l)=(-1)^{3l}=(-1)^l (mod p). This proves S_p is a unit.

## Executed exact check and BRC port separation

Independent standard-library Python exact modular checker: d25_finite_rational_green_eval_20261031.py; run locally with python, checked every prime p=6l+1 in [7,500], **45 primes**, modulo p^2. Computation independently constructs all three original parameter jets, translates F into the y basis, tests zero residue and top-jet identity, and compares finite source evaluation against the complete antisymmetric Wronskian evaluation. It also computes the earlier signed R as an **independent original double sum** (g_i,c_a,K_i), not as a rename of Phi. All checks passed: PASS_D25_FINITE_RATIONAL_GREEN_EVALUATION_PLOCAL.

Rows (p, gamma mod p, S_p mod p, Phi(1/2) mod p, Phi(1/2) mod p^2, original signed R mod p):
- (7,2,6,3,31,3)
- (13,8,1,4,147,0)
- (19,18,18,12,354,12)
- (37,35,1,18,166,11)
- (67,41,66,19,1091,21)
- (373,228,1,1,36928,196).

**Exact observer-loss counterexample:** the tempting identification Phi(1/2) == R_p (mod p) is false: at target p=67 the two readouts are 19 and 21; at target p=373 they are 1 and 196. Agreement at p=19 is accidental with respect to this proposed global identity. Keep the Green evaluation, gamma, signed Clausen R, and the native H0/B0 signed Green/Hesse as separate typed ports.

BRC: COMPOSE_APPLIED to the already source-derived (index k, jet order r, original coefficient, p-adic valuation, derivative orientation, signed terminal) carrier. Declared operations are finite binomial basis change, p-local integration, evaluation at 1/2, and separate signed R readout. The exact finite transform preserves F and gamma; the single scalar Phi(1/2) is not certified sufficient for future source-class Frobenius/Green observables. No native X6 dynamics is asserted by this auxiliary classical finite algebra.

## Frontier and next exact action

**Proved here:** a pole-safe finite p-local rational evaluation/terminal interface, exact top-jet residue identity, and non-identification of Phi with the frozen signed R. These are full rational/algebraic equalities, with finite machine checks supporting implementation only. **Not proved:** original A_p == p (mod p^3) for every target prime; no finite WZ/CM cancellation certificate linking the full symmetric lower jets to R; no original-class native experiment.

Next mathematically discriminating unit: build the **coupled symmetric/antisymmetric two-port finite adjoint**, i.e. retain both J_0(1/2)J_2(1/2) and Phi(1/2), plus the distinct first-jet terms, and test an actual parameter-shift/boundary relation with signed R for p=19,67,373. Any proposed linear equality collapsing Phi alone onto R is already refuted. Preserve first/second p-carries and source class. In parallel, same-original-class fixed-373 native H0/B0 divided-power [X]U mod 139129, rank, actual semilinear Frobenius/eta, signed Green/Hesse, kappa and independent replay remain **NOT_EXECUTED / PENDING_OWNER** in Enterprise Math #1559; they are not replaced by this evaluation.

Control provenance (read-only, as of this run): original Research logical lane chatgpt-research-onhour-enterprise-math-20260923, recovery request research-onhour-20261031-0202-recovery-r15 (#6632) has no current claim/run and explicitly says source_authority_verified=false. Original dispatch request research-onhour-20261031-0205-dispatch-r15 (#6633) ended FAILED / UPSTREAM_CODE_REVIEW_REQUIRED; do not replay. No new session, claim, open, dispatch, Source checkpoint, Result or admission is claimed. Do not use maintenance conversation chatgpt-hourly-enterprise-math-20260921. The neutral old staging disposition remains separate. Original recurring automation scheduling is untouched.
