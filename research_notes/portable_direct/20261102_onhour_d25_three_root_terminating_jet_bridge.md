# D25 — Three-root finite polynomial jet bridge for original LIFT (2026-11-02)

**Status:** AUTHOR-DERIVED / EXACT ALGEBRA / FINITE REGRESSION / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT. Not formal Source checkpoint, admitted Result or native H0/B0 experiment.

**Task:** RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; **immutable scientific pin** c47e13e4aba0e006366f989d6334d443f6333ae3; Research conversation chatgpt-research-onhour-enterprise-math-20260923. Preserve separate maintenance lane. Inputs: accepted D24 first-digit theorem, frozen Clausen finite-convolution correction, previously established author-side W216 half-cutoff and Wilson-reflected B2 tail.

## Exact theorem: three-root terminating deformation

For every prime p>3 with p=6m+1, let k in [0,p-1] and define the finite rational polynomial

\[
F_{p,k}(t)=\frac{6k+1}{2^k(k!)^3}\prod_{j=0}^{k-1}
(j-3m+t/2)(j-2m+t/3)(j-4m+2t/3).
\]

Every polynomial coefficient belongs to Z_(p), since k<p and p>3. At the genuine integer t=p, the parameters become j+1/2,j+1/3,j+2/3. Using the Pochhammer factorial formula gives the **exact rational identity**

\[
F_{p,k}(p)=w_k=(6k+1)\frac{(2k)!(3k)!}{216^k(k!)^5}.
\]

The three t-roots occur in successive bands as k exceeds 2m,3m,4m. Thus polynomial valuations at t=0 are at least 0 for 0<=k<=2m, at least 1 for 2m<k<=3m, at least 2 for 3m<k<=4m, and at least 3 for 4m<k<p. Define the source-tagged ordinary polynomial-coefficient ports

\[
A_i=\sum_{k=0}^{2m}[t^i]F_{p,k}(t)\ (i=0,1,2),\quad
B_i=\sum_{k=2m+1}^{3m}[t^i]F_{p,k}(t)\ (i=1,2),\quad
C_2=\sum_{k=3m+1}^{4m}[t^2]F_{p,k}(t).
\]

Write W(n)=sum_{k=0}^n w_k and H=3m. Exact finite polynomial substitution t=p and reduction modulo p^3 prove

\[
\boxed{W(p-1)\equiv A_0+p(A_1+B_1)+p^2(A_2+B_2+C_2)\pmod {p^3}}, \tag{1}
\]
\[
\boxed{W(H)\equiv A_0+p(A_1+B_1)+p^2(A_2+B_2)\pmod {p^3}}. \tag{2}
\]

## Original scalar second digit, no loss of signed tail

For p congruent 13 or 19 modulo 24, the accepted D24 first-digit result gives W(p-1)=p modp². Therefore the p-adic integer

\[
D_0=(A_0+p(A_1+B_1)-p)/p^2
\]

is well-defined. The frozen exact Clausen return and the previous half-cutoff theorem say
Delta_p-R_p = [W(p-1)-p]/p² modp. Hence (1) gives the genuinely original observer

\[
\boxed{\Delta_p-R_p\equiv D_0+A_2+B_2+C_2\pmod p}. \tag{3}
\]

For each 3m<k<=4m the polynomial has exactly two forced roots, hence w_k/p²=[t²]F_{p,k}(0) modp. Consequently

\[
\boxed{C_2\equiv B_{2,W}(p)\equiv\sum_{r=1}^{m}(6r-2)U_r\pmod p}, \tag{4}
\]

where the pre-established Wilson-reflected sequence obeys U_1=(6/p)/9 and
U_(r+1)=U_r r(6r-1)(6r+1)/[9(2r+1)^3] modp. The Wilson formula is imported from previously saved author-side research, not newly proven in this note.

The **equivalent still-open all-target finite-jet certificate** is therefore

\[
\boxed{D_0+A_2+B_2\equiv-C_2\pmod p}. \tag{5}
\]

The k-band, original W216 weight, valuation, and observer's p² division remain typed and recoverable. This reduction concerns precisely the specified scalar Delta-R observer, not a native H0/B0 Frobenius or unrestricted future operations.

## Non-singular three-coefficient recurrence

Let x(k)=(x0,x1,x2) be the degree-at-most-two coefficients of the unweighted finite product /[2^k(k!)^3], with x(0)=(1,0,0). For a=k-3m, b=k-2m, c=k-4m set

\[
g_0=abc,\quad g_1=bc/2+ac/3+2ab/3,\quad g_2=c/6+b/3+2a/9.
\]

Then

\[
x(k+1)=\frac1{2(k+1)^3}(x_0g_0,\ x_1g_0+x_0g_1,\ x_2g_0+x_1g_1+x_0g_2)\pmod{p^3}. \tag{6}
\]

All denominators are units for k<p-1; no zero-root inverse is taken. Recover F by multiplying by original signed weight 6k+1. The loop runs in O(p) coefficient transitions; actual bit complexity also includes p-adic modular arithmetic.

## Actually executed verification and explicit new counterexample

A fresh independent jet-coefficient recurrence and the original factorial-ratio W216 recurrence matched for every target p<=3000 (107 primes, 142715 indexed polynomial positions). Independently computed original integer binomial coefficients matched p=13,19,37,43,373. These are finite exact arithmetic checks, not proof of the universal cancellation (5).

| p | D0 | A2 | B2 | C2 | J_H | original B2W |
|---:|---:|---:|---:|---:|---:|---:|
| 13 | 3 | 5 | 8 | 10 | 3 | 10 |
| 19 | 11 | 1 | 17 | 9 | 10 | 9 |
| 373 | 240 | 82 | 158 | 266 | 107 | 266 |
| 1171 | 1121 | 823 | 521 | 1048 | 123 | 1048 |

For p=373: A0=15521276 modp³, A1=3122 modp², B1=44787 modp², so A0+p(A1+B1)=373+240p²=33391333 modp³. Moreover

\[
D_0+A_2+B_2+C_2=240+82+158+266=746=2p.
\]

Thus J_H=107, C2=B2W=266, and the original residual vanishes at 373. The first-order-only deformation yields D0=240 !=0 mod373: **a counterexample to omitting all quadratic jet terms** in the specified p373 divided-second-digit observer. This does not refute the mother target.

## Precise next work, provenance and separate native debt

Seek a terminating contiguous identity or WZ pair connecting D0+A2+B2 to the *same* U_r in (4), preserving both residue classes and p² division. Exact 373 discriminator: 240+82+158=480=107=-266 mod373. The all-prime mother Delta_p=R_p remains OPEN; accepted D24, frozen Clausen return and prior Wilson reflection are to be consumed rather than rederived.

Fixed p373 original-class native H0/B0 divided-power [X]U mod139129, semilinear Frobenius normalization eta, operator rank, signed odd Green/Hesse kappa and independent replication are NOT_EXECUTED / PENDING_OWNER under existing enterprise-math issue #1559. This author-side polynomial scalar proof does not replace that native experiment.

Read-only Sites status observed 2026-11-02 07:11 UTC: backend 0.6.11, research_authority_granted=false and write_relay_enabled=false; no verified native Research session, claim, run or checkpoint. Old original request research-onhour-20261031-0205-dispatch-r15 was not replayed. Historical failed receipt remains distinct.

**Frozen scientific sources:** task publication TP2-B6F4FC938FF94941C1B7 and research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_FINITE_CLAUSEN_DERIVATIVE_BRIDGE_RETURN_20260827.md at c47e13e4aba0e006366f989d6334d443f6333ae3; already published author-side 20261102_onhour_d25_lift_half_cutoff_source_bridge.md. Current behavioral norms are read separately on canonical main; mathematical evidence not admitted by this author-side note.
