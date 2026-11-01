# D25 — full finite-field Legendre reduction, Hensel root digits and explicit inverse observer

2026-11-01 UTC+08. Research: portable author-derived, exact-checked, UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443 unchanged. TASK_RESEARCH lane chatgpt-research-hourly-enterprise-math-20260923; CONTROL_PLANE_MAINTENANCE lane not used. No native CLAIM/OPEN/Source checkpoint/Result or original H0/B0 asserted.

## I. New whole-polynomial reduction (all p = 6r+1 >= 7)

Put u_k=(1/6)_k(1/3)_k/(k!)^2, Y_p(z)=sum_{k=0}^{p-1}u_k z^k, theta=z d/dz. Let P_m be the Legendre polynomial with P_m(1)=1. Then, **as polynomials in F_p[z]**, not just at a sample point,

\[
\boxed{Y_p(z)=P_{2r}(\sqrt{1-z})\pmod p.}\tag{L}
\]

The right-hand side is a polynomial because P_{2r} is even; no square-root branch is chosen. Proof: 1/6=-r and 1/3=-2r modulo p, so Y_p modulo p is the degree-r terminating Gauss polynomial with parameters (-r,-2r). The exact rational polynomial identity

\[
P_{2r}(\sqrt{1-z})=\sum_{k=0}^r\frac{(-r)_k(r+1/2)_k}{(k!)^2}z^k
\]

follows directly from the Legendre ODE (substitute x^2=1-z) and normalization at z=0. Since r+1/2=-2r+p/2 and k! is a p-unit for k<=r, coefficients match mod p. This is a classical quadratic-polynomial transformation applied to the actual finite D25 coefficients; it is not claimed as an original transformation theorem.

Define x formally by x^2=1/2 in F_p[x]/(x^2-1/2), and define two scalars S=P_{2r}(x), B=P_{2r-1}(x)/x, both in F_p by parity. At z0=1/2 write s=Y_p(z0), d=(theta Y_p)(z0). The standard Legendre derivative law (1-x^2)P_m'=m(P_{m-1}-xP_m) gives

\[
\boxed{s=S,\qquad d=r(S-B)\pmod p.}\tag{N}
\]

When S=0, B and d are nonzero: a simultaneous zero of P_{2r} and its derivative at x^2=1/2, where 1-x^2 is a unit, would contradict uniqueness for the regular Legendre ODE (degree 2r<p, P_{2r}(1)=1). Thus an actual zero Y_p(1/2) mod p is automatically simple, uniformly for both class-13 and class-19 primes. The assertion that S=0 for **every** prime in those two classes is still an open CM/character-sum obligation.

## II. New explicit Hensel observer through p^3

Assume S=0. Express canonical digits

\[
s/p=a_0+pa_1\pmod{p^2},\qquad d=d_0+pd_1\pmod{p^2},
\quad 0\le a_i,d_i<p,\quad d_0\ne0.
\]

The unique zero z* of Y_p above 1/2 satisfies z*=1/2+p delta_0+p^2 delta_1 (mod p^3), with 0<=delta_i<p and

\[
\boxed{\delta_0=-a_0/(2d_0)\pmod p,}\tag{H1}
\]
\[
\boxed{\delta_1=-(c+a_1+2\delta_0d_1-\delta_0^2d_0)/(2d_0)\pmod p,}\tag{H2}
\]
where c=(a_0+2 delta_0 d_0)/p is an **integer carry**, not a formal quotient in F_p.

Proof: the truncated Gauss ODE has a p^2-divisible terminal source and hence
z(1-z)Y''+(1-3z/2)Y'-(1/18)Y=0 (mod p).
At the zero z=1/2, this yields Y''=-Y'=-2d_0 (mod p). Taylor-expand Y(1/2+p delta_0+p^2 delta_1) using Y'(1/2)=2d exactly, equate the first two p-adic digits and apply Hensel uniqueness. No native experiment is used.

Consume the already-proved *signed* Clausen cutoff identity
W_p(1/2)=s^2+12sd-T_p, with T_p=p^2 C_p (mod p^3).
The original weighted 216 target has the following **equivalent Hensel digit tests**:

\[
\boxed{W_p(1/2)=p\pmod{p^2}
\iff \delta_0=-1/(24d_0^2)=-1/(24r^2B^2)\pmod p.}\tag{H3}
\]

If H3 holds, the mod-p^3 target holds iff

\[
\boxed{
\frac{-24\delta_0d_0^2-1}{p}
-48\delta_0d_0d_1-24\delta_1d_0^2
+16\delta_0^2d_0^2-C_p=0\pmod p.}\tag{H4}
\]

Again the displayed quotient is the actual integer carry for canonical digits. To prove H3 use W/p=12a_0d_0 (mod p). For H4 use the root expansion
s=-2p delta_0 d+p^2(delta_0^2 d_0-2delta_1 d_0) (mod p^3)
inside W=s^2+12sd-p^2C_p. H3/H4 are new coordinate forms of the earlier exact two-digit criterion, **not** a proof that it vanishes for every target prime. This explicitly retains the signed high-index cutoff C_p.

## III. Explicit inversion of the prior triangular coefficient-observer matrix

Reuse the previous arbitrary-coefficient quadratic observer Q(a)=a^T M a, where
M_{ij}=1_{i+j<p}(6(i+j)+1)2^{-i-j}, 0<=i,j<p.
The earlier work proved only det(M) != 0. Put c=6p-5, q=(c+6)/c and

\[
b_0=1/c,\quad b_1=(q-2)/c,\quad
b_d=36q^{d-2}/c^3\quad(d\ge2).
\]

Then the **exact rational inverse** is

\[
\boxed{
(M^{-1})_{ij}=
1_{i+j\ge p-1}\,2^{i+j}b_{i+j-(p-1)}.
}\tag{I}
\]

Proof: factor M=DAD with D_{ii}=2^{-i}; let J reverse columns, U=AJ. Then U is upper-triangular Toeplitz with U_{i,i+d}=c-6d. Its coefficient series is f(t)=[c-(c+6)t]/(1-t)^2 modulo t^p, so the inverse series (1-t)^2/[c-(c+6)t] has precisely coefficients b_d. Since A=UJ and A^{-1}=JU^{-1}, conjugation by D^{-1} proves I. Mod p>=7, c=-5 is a unit, so I also gives a full inverse over F_p. This identifies the exact reversible full-port reconstruction from the p linear polarizations of Q on arbitrary coefficient inputs; the single Hadamard special value is not thereby a sufficient statistic for the actual hypergeometric sequence.

BRC applied: carrier is the signed source-preserving truncated coefficient family; allowed future operators are theta, Clausen convolution, Hadamard, Hensel lift, polarization and mod-p^3 observation. H1/H2 keep the exact zero location, H4 keeps C_p and integer carry, and I describes full-port invertibility. These are external arithmetic auxiliary coordinates, not a proposed native X6 embedding.

## IV. Exact integer verification and open mathematical frontier

The executable Python checker separately computes original (1/6,1/3) Pochhammer coefficients modulo p^3, Legendre polynomials in F_p[x]/(x^2-1/2), derivatives, Hensel roots modulo p^3, the weighted original 3F2 cutoff, and matrix inverses. All 207 primes p=1 mod6 up to 3000 PASS the whole-polynomial coefficient check and neighbor identity. Zero census by p mod24: 1:0/46, 7:0/54, 13:53/53, 19:54/54. For the 107 target primes, finite checks also give W_p(1/2)=p mod p^3. Matrix M M^{-1}=I was checked entrywise for p=7,13,19,37. Exact witnesses (p,B,d0,delta0,delta1,Cp,Wmodp^3): (13,3,7,2,9,0,13); (19,6,1,15,3,12,19); (37,33,24,8,10,11,37); (373,272,294,274,321,196,373). Finite checks are not universal proof or independent review.

Mother objective A_p=p mod p^3 for p mod24 in {13,19} remains open. The next smallest question is a CM/finite-character-sum proof of P_{(p-1)/3}(1/sqrt(2))=0 for precisely those classes, taking care that its index (p-1)/3 differs from the elliptic Hasse index (p-1)/2. Then seek arithmetic source for H3/H4 including C_p and both class ports. Existing continuation request hourly-d25-continuation-20261101T1530p0800-r11 is terminal FAILED with UPSTREAM_CODE_REVIEW_REQUIRED (bridge #6638). Gateway 0.6.11 currently reports research_authority_granted=false and executor_binding_configured=false, active_jobs=5/5. Support issue #1558 is the control lane, #1559 the original p=373 H0/B0. This portable report grants no claim, Source checkpoint, review, P000 change, worldview change, or native experiment.