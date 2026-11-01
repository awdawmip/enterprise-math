# D25/LIFT — fixed-216 conditional curvature and cubic skew of the ORIGINAL weighted observer

2026-10-31; two consecutive author-side portable TASK_RESEARCH units. Real logical lane: chatgpt-research-hourly-enterprise-math-20260923 (NOT maintenance). Formal Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source c47e13e4aba0e006366f989d6334d443f6333ae3. Status: AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / CONDITIONAL / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. P000 and ACTIVE worldview unchanged; external p-adic finite-field mathematics only, not native X6/H0/B0 execution.

## Inherited premise, original observer

Let p=6l+1>=7 be prime. Retain ORIGINAL coefficients, signed weight, and exact denominator:

\[
a_n=\binom{2n}{n}^2\binom{3n}{n}/216^n,\qquad A_p(X)=\sum_{n=0}^{p-1}(6n+1)a_n X^n.
\]

Let theta=X d/dX=z d/dz, z=X/2, and G(z)=sum_{k=0}^l binom(l,k)binom(2l,k) z^k. The specific *inherited, not independently proven here* CM premise is G(1/2)=0 mod p. Previously proved classical finite Clausen reduction: F_p(X)=sum a_nX^n = G(X/2)^2 mod p coefficientwise. The earlier fixed-216 sensitivity paper proves under CM that G'(1/2) is nonzero mod p; this is consumed, not recredited. All rational denominators appearing here are p-local units.

## Unit 1: first three original source moments and sharp even curvature

Set M_r=sum_{n=0}^{p-1}n^r(6n+1)a_n, r=1,2,3. **Conditional theorem:**

\[
\boxed{(M_1,M_2,M_3)\equiv (3,5,56/3)\,G'(1/2)^2\pmod p.}\tag{1}
\]

**Complete algebraic proof.** Apply theta^r(1+6theta) to F_p=G(z)^2 mod p before evaluating z=1/2. The Gauss polynomial satisfies exactly

\[
z(1-z)G''+[1+(3l-1)z]G'-2l^2G=0.
\]

At z0=1/2, using l=-1/6 mod p and CM: G''(z0)=-G'(z0) mod p. Differentiate the ODE once: z(1-z)G'''+[1-2z+1+(3l-1)z]G''+(3l-1-2l^2)G'=0; at z0 its coefficients become (1/4,1/4,-14/9), hence G'''(z0)=(65/9)G'(z0) mod p. For F=G^2 and G(z0)=0,

\[
\begin{aligned}
\theta F&=0,\\
\theta^2F&=2z_0^2G'^2,\\
\theta^3F&=6z_0^2G'^2+6z_0^3G'G'',\\
\theta^4F&=14z_0^2G'^2+36z_0^3G'G''+6z_0^4(G'')^2+8z_0^4G'G'''.
\end{aligned}
\]

Substitute z0=1/2, G''=-G', G'''=65G'/9, and M_r=[theta^rF+6theta^{r+1}F] at z0. Results are exactly 3, 5, and 56/3. QED.

Write X_t=(1+pt)^(-1), t in Z_(p). Finite expansion for each original index 0<=n<p gives
(1+pt)^(-n)+(1-pt)^(-n)-2=n(n+1)p^2t^2 mod p^3.
Thus

\[
\boxed{\Delta_{2,p}(t):=A_p(X_t)+A_p(X_{-t})-2A_p(1)
\equiv8p^2t^2G'(1/2)^2\pmod{p^3}.}\tag{2}
\]

The first moment's unknown p-adic carry cancels **because of this exact symmetric observer**. As 8 and the inherited G' are p-units, v_p(Delta2)=2 whenever t is a p-unit. This does not change the frozen original denominator.

## Unit 2: sharp third-order odd stencil

Define the four-point signed observable

\[
\Delta_{3,p}(t)=A_p(X_{2t})-2A_p(X_t)+2A_p(X_{-t})-A_p(X_{-2t}).
\]

The finite rising-factorial expansion of the ORIGINAL full sum reads

\[
A_p(X_t)\equiv A_p(1)-ptM_1+\frac{p^2t^2}{2}(M_2+M_1)
-\frac{p^3t^3}{6}(M_3+3M_2+2M_1)\pmod{p^4}.
\]

The displayed four-point operator cancels the constant, linear and quadratic terms and multiplies the cubic term by 12. From (1),

\[
M_3+3M_2+2M_1\equiv(56/3+15+6)G'^2=119G'^2/3\pmod p.
\]

Therefore the **conditional theorem** is

\[
\boxed{\Delta_{3,p}(t)\equiv-\frac{238}{3}p^3t^3G'(1/2)^2\pmod{p^4}.}\tag{3}
\]

For the frozen classes p mod 24 in {13,19}, neither p=7 nor p=17 is possible, so 238=2*7*17 is a p-unit. Together with inherited CM simple-root property, v_p(Delta3)=3 for p-unit t. This is a source-faithful third-order skew certificate, NOT a proof that A_p(1)=p mod p^3.

## Actually executed exact checks and precise status

The self-contained standard-library program d25_fixed216_normalization_curvature_stencil_20261031.py computes all original coefficients using the exact recurrence
a_n/a_{n-1}=(2n-1)(3n-1)(3n-2)/(36 n^3), evaluates full original A_p(X_t) modulo p^4 independently from integer-binomial G'(1/2), and checks all three moments. All **166** primes p<=5000 with p mod 24 in {13,19} passed, including **332** even-curvature pairs t=1,2 and **166** odd stencils. Program marker PASS_D25_FIXED216_CURVATURE_AND_CUBIC_STENCIL_EXACT.

| p | G' mod p | M1 mod p | M2 mod p | M3 mod p | Delta2(1)/p^2 mod p | Delta3(1)/p^3 mod p |
|---:|---:|---:|---:|---:|---:|---:|
| 13 | 1 | 3 | 5 | 10 | 8 | 3 |
| 19 | 2 | 12 | 1 | 5 | 13 | 12 |
| 37 | 11 | 30 | 13 | 14 | 6 | 33 |
| 157 | 118 | 10 | 69 | 132 | 79 | 67 |
| 373 | 215 | 292 | 238 | 242 | 157 | 277 |

Scope: mathematical formulas are conditional on the existing CM root; finite computation corroborates instances only. No independent review, native Source checkpoint, formal Result or Lean checking. BRC COMPOSE_APPLIED: carrier retains p,n,original a_n,weight 6n+1,216,valuation,perturbation t, moments and signed operators; the even/odd stencils discard specified jet orders by explicit operators, not by a total-only unlabeled quotient. No automatic P000 X6 native transfer.

Mother D25/LIFT/JT2 remains OPEN: A_p(1) ?= p mod p^3 for p mod 24 in {13,19}; the original-source four-port obstruction C+L-J+I=0 mod p remains unproved. Next: build an exactly finite source-preserving WZ/adjoint that transports fixed-216 low-band p-adic carry to middle/high signed valuation walls and the endpoint Fermat quotient. The distinct on-hour Green terminal/carry is not reattributed or identified with the current stencils.

Current native read boundary: Gateway 0.6.11, research_authority_granted=false, executor_binding_configured=false, active jobs 5/5, CODE_REVIEW_REQUIRED / UPSTREAM_CODE_REVIEW_REQUIRED; one exact read-only continuation request returned CONTROL_QUOTA. Available connected native action list does not expose recovery_status. Historical own #6424/#6425 receipts are not current authorization. Support enterprise-math#1558 owns control repair. No new claim/open/source checkpoint/Result, no session/staging transition, no maintenance identity, no scheduler changes.
