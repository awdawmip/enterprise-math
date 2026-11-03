# D25 — CM quartic argument jet and first-lossless reflection precision repair

Date: 2026-11-03 (+08). TASK_RESEARCH author-side research, NOT native claim/checkpoint/review. Intended logical lane: chatgpt-research-hourly-enterprise-math-20260923; maintenance lane excluded: chatgpt-hourly-enterprise-math-20260921. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; unchanged frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3. Status AUTHOR-DERIVED / ALGEBRAICALLY-PROVED / FINITE-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.

## Sources and scope

For primes p>=13, p mod24 in {13,19}, r=(p-1)/6, put b_k=binom(2k,k)^2 binom(3k,k)/216^k, F_p(t)=sum_{0<=k<p} b_k t^k, W_p(t)=(1+6 theta_t)F_p(t), theta_t=t d/dt. Work in Z_(p) and F_p. Existing accepted finite CM0 says ell_r(1/2)=0 mod p, where ell_r(z)=sum_{k=0}^r binom(r,k)binom(2r,k)z^k. Set G(t)=ell_r(t/2), j=G'(1) modp, j!=0. Consume, do not re-credit, the preceding author-side finite Clausen polynomial identity F_p(t)=G(t)^2 modp, first/second argument jets, and three-port reflected valuation theorem (research_notes/portable_direct/20261103_hourly20_d25_cm_parameter_jet_reflection_fiber.md and 20261103_hourly20_d25_reflection_three_port_universal_measure.md). The separate finite Hensel-parameter operator is in research_notes/portable_direct/20261103_onhour_d25_original216_coupled_finite_hensel_ode.md.

## Q1: new third/fourth argument moment theorem (proved)

With x=t-1, in F_p[x]/(x^5),

\[
\boxed{W_p(1+x)=j^2(12x+4x^2+\frac{58}{9}x^3+\frac{95}{27}x^4).}
\]

Consequently the NEW original signed ordinary falling-factorial moments are

\[
\boxed{\sum_{k<p} k(k-1)(k-2)(6k+1)b_k=(116/3)j^2\pmod p,}
\]

\[
\boxed{\sum_{k<p} k(k-1)(k-2)(k-3)(6k+1)b_k=(760/9)j^2\pmod p.}
\]

Proof: Gauss ODE for exact terminating G is t(2-t)G''+[2-(1-3r)t]G'-2r^2 G=0. Mod p (r=-1/6) at t=1+x it becomes (1-x^2)G''+(1/2-3x/2)G'-(1/18)G=0. Normalize G(1+x)=j sum_{n>=0}u_n x^n with u_0=0,u_1=1. Extracting x^n gives

\[
(n+2)(n+1)u_{n+2}+(n+1)u_{n+1}/2
-(n^2+n/2+1/18)u_n=0.
\]

All necessary denominators are p-units. Thus u_2=-1/4, u_3=65/216,u_4=-247/1728. Squaring gives G^2/j^2=x^2-x^3/2+287x^4/432-377x^5/864+O(x^6). Apply original weight 1+6(1+x)d/dx to recover the four claimed coefficients. The original sums are derivatives of the polynomial W_p(t) at t=1. QED. The first two moments are reused results.

## Q2: new reflection precision threshold and repair (proved)

For a p-integral weight w(k), independent of t, define C_p(w;t)=sum_{k<p}w(k)b_k b_{p-1-k}t^{p-1}. This factorizes EXACTLY as t^{p-1}C_p(w;1). The preceding valuation theorem gives v_p(C_p(w;1))>=2, and its three-port unit theorem gives C_p(1;1)=10p^2 mod p^3. For t=1+p lambda, lambda in Z_(p), we obtain

\[
\boxed{(C_p(1;1+p\lambda)-C_p(1;1))/p^3=-10\lambda\pmod p.}
\]

Proof: (1+p lambda)^(p-1)=1+(p-1)p lambda+O(p^2), multiply by 10p^2+O(p^3), reduce modulo p^4. Since -10 is invertible for all target p, ONE relative scalar observation C_p(1;t) modp^4 recovers lambda modp. All reflection observations C_p(w;t) modp^3 remain unchanged under the same perturbation. Thus p^4 is the first sufficient reflected precision for this source family and these p-adic lifts, not a blanket lower bound for unrelated observers.

Combine the new recovered lambda with the *separate oriented* Gauss derivative j^2 to restore the original UNREFLECTED displacement:

\[
\boxed{W_p(1+p\lambda)-W_p(1)
=-\frac65 j^2 [C_p(1;1+p\lambda)-C_p(1;1)]/p^2
\pmod{p^2}.}
\]

The left is 12p lambda j^2 modp^2 (Q1), and the right is -(6/5)j^2(-10p lambda). This repairs the exact earlier BRC reflection-fiber obstruction at its first sensitive precision. Carrier=(relative reflection modp^4, j^2 modp), operation=argument lift, observer=weighted difference modp^2. It does NOT reconstruct the fixed baseline W_p(1) modp^3.

## Executed exact evidence

Script d25_cm_jet_precision_repair_20261103.py (separate repository file) was executed with Python unbounded integers and p-unit modular inverses for all 77 primes 13<=p<=2000 in target residue classes. The checker uses the independent exact coefficient recurrence b_{k+1}=b_k(2k+1)(3k+1)(3k+2)/(36(k+1)^3), all k<p, computes G and j independently, and checks Q1 moments, base C/p^2=10, C first-visible digit, repaired weighted displacement, direct original W_p(1+p lambda) versus cubic Taylor modulo p^4 for each lambda=1,2,3. All PASS. At p13: j=7,D3=1,D4=11 mod13, C(1;1) mod13^4=17069, C first difference/p^3 at lambda=1 =3; at p19: j=1,D3=7,D4=0; at p373: j=294,D3=112,D4=176 and first reflection digit=363, first weighted digit=292. Finite checking supports the stated algebraic proofs, but is not a formal project review or the native p373 H0/B0 experiment.

## Continuation and control

Mother goal remains OPEN: W_p(1)=p modp^3 for p mod24 in {13,19}, equivalently frozen Delta_p-R_p=0 modp. Next precise unit: combine the *argument* jets with the sibling's separate *hypergeometric-parameter* three-strip operator (F0,F1,F2) at fixed t=1 in a terminating WZ/contiguous identity; require correct signed H2 4F3 boundary and p13,p19,p373 divided second carry. A proposed identity that only controls differences across t cannot complete this baseline.

Actual Gateway 0.6.11 read on 2026-11-03: UPSTREAM_CODE_REVIEW_REQUIRED; research_authority_granted=false; executor_binding_configured=false; control_quota active=5/5. No new native CLAIM, authorized OPEN, Source checkpoint, Result, review, or mathematical admission this run. Preserve previous service session MCP-06f7ad61a8d841d9ba1ba1ef4d088d94, bridge Issues #6637/#6638, unpublished staging and Source owner frontier; support #1558 and native experiment #1559 remain. P000, ACTIVE worldview, frozen pin and Research/Maintenance lane identities unchanged.
