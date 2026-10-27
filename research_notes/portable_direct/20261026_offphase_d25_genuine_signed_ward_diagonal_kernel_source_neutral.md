# D25/LIFT — Genuine finite Hasse face defeats diagonal-only observation; exact signed 3+2+1 source transport

Date: 2026-10-26. **SOURCE-NEUTRAL PORTABLE MATHEMATICAL EVIDENCE** only: AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / NATIVE_SYNC_DEBT. No current Source CLAIM, OPEN, Result, reviewer independence or original-class experiment is inferred.

Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Its **frozen mathematical Source** remains c47e13e4aba0e006366f989d6334d443f6333ae3. This proof consumes, without re-crediting, the exact genuine finite-face bivariate Green–Ward master at commit 0929779757189d61ebfa1e815d8c5a31fd95f6df (research_notes/portable_direct/20261026_hourly_d25_bivariate_master_ward_r13.md).

## A. Exact p-local normalization of the authentic reflected source

For a prime p=6m+1>=7, take R=Z_(p), and let f_r(z)=(-m-z)_r(-2m-2z)_r/((1-p/2-3z)_r r!), 0<=r<p. The inherited ordered finite carrier is

M_n^h(t,s) = SUM_{1<=j,ell<=2m; ell-j=n} j^h f_j(t) f_{p-ell}(s), h=0,1,

with L=1-2m<=n<=N=2m-1 and M_{N+1}=0. The inherited exact master equation is

[p-2n-3(t+s)] M_n^1 +[-C_n+3s(p-n)] M_n^0
= [A_n-3(t+s)] M_{n+1}^1
+[B_n+4mt+(14m-3n)s+2(t^2-s^2)] M_{n+1}^0 + E_n,

where C_n=(p-n)(p/2-n), A_n=6m-2n, B_n=-18m^2+9mn-n^2. Crucially E_n denotes the **real two-ended finite shift faces**, not infinity or the separately ordered high-high population:

- n>=0: E_n=2(m+t)^2 f_{p-n-1}(s)-(6m^2-8ms+2s^2)f_{2m-n}(t)f_{4m}(s);
- n<0: E_n=(20m^2-14ms+2s^2)f_{-n}(t)f_{p-1}(s)+(2mt-2t^2)f_{2m}(t)f_{p-(2m+n+1)}(s).

**Lemma (proved).** For every 2m+1<=r<p, exactly the Pochhammer factors at k=m and k=2m vanish at z=0. They have slopes -1 and -2. Since all other numerator factors and the entire denominator are p-units, there is an exact factorisation f_r(s)=s^2 q_r(s) in R[[s]] with q_r(0) in R^x and

q_r(0)=2(-1)^m m!(2m)!(r-m-1)!(r-2m-1)! / [r! (1-p/2)_r].

Every reflected index in all real moments and each true finite face lies in [2m+1,p-1]. Hence define V_n=M_n^0/s^2, U_n=M_n^1/s^2 and F_n=E_n/s^2. This is an exact p-local operation preserving each finite source; it does not discard a boundary. The same displayed master holds with (M^0,M^1,E) replaced by (V,U,F).

## B. Exact 3+2+1 signed observer on the **actual** six Hasse labels

On any normalised total-degree-2 source jet, write

G(t,s)=a+bt+cs+dt^2+ets+fs^2 (mod terms of total degree>=3).

These six coefficients are the original actual bivariate source Hasse labels (0,2), (1,2), (0,3), (2,2), (1,3), (0,4), respectively. Define S(z)=G(z,z), A(z)=(partial_t-partial_s)G(z,z), B=(partial_t-partial_s)^2G(0,0). Their 3+2+1 coefficients are

S=(a,b+c,d+e+f);
A=(b-c,2(d-f));
B=2(d-e+f).

**Theorem (proved).** This change of observables is an isomorphism over R (p>3). Its inverse is

a=S0,
b=(S1+A0)/2, c=(S1-A0)/2,
d=S2/4+B/8+A1/4, e=S2/2-B/4, f=S2/4+B/8-A1/4.

Thus signed first- and second-anti-diagonal data are exactly the three extra source coordinates needed beyond the diagonal three; this is now typed onto authentic reflected Hasse coefficient sources, not only the previous free six-dimensional formal example. The derivative here is a *parameter anti-diagonal*, not automatically a true J/E operator or the original Clausen mass.

A second exact theorem: write X^+=X(z,z), X^-=(partial_t-partial_s)X(z,z), X^{--}(0)=(partial_t-partial_s)^2X(0,0), and alpha=p-2n-6z, beta=-C_n+3(p-n)z, gamma=A_n-6z, delta=B_n+(18m-3n)z. The normalized master yields, without suppressing F,

alpha U_n^+ + beta V_n^+ = gamma U_{n+1}^+ + delta V_{n+1}^+ + F_n^+,

alpha U_n^- + beta V_n^- -3(p-n)V_n^+
= gamma U_{n+1}^- + delta V_{n+1}^-
  +(-10m+3n+8z)V_{n+1}^+ + F_n^-,

and the *sixth-coordinate* equation at z=0,

(p-2n)U_n^{--}(0)-C_n V_n^{--}(0)-6(p-n)V_n^-(0)
=A_n U_{n+1}^{--}(0)+B_n V_{n+1}^{--}(0)
 +2(-10m+3n)V_{n+1}^-(0)+F_n^{--}(0).

The three scalar Taylor coefficients, two first signed coefficients and one second signed coefficient form exactly the six genuine source Ward coefficient equations. The signs -3(p-n), -10m+3n+8z, and -6(p-n) are essential and originate in differentiating **both** finite-source orientations.

## C. Genuine-source counterexample, not a free-vector no-go

Here is a finite **exact** source witness in F_13, using only the bona fide endpoint faces F_n=E_n/s^2 and m=2. Order the six jet coefficients (a,b,c,d,e,f), and reduce exact rational computations modulo 13:

F_{-3}=(0,7,0,8,0,0);
F_0=(8,0,8,10,2,0);
F_1=(9,7,8,11,0,1).

The nonzero weighted authentic source sum

F_{-3}+7F_0+F_1=(0,1,12,11,1,1)

has *all three diagonal coefficients zero*:

S=(0,1+12,11+1+1)=(0,0,0) mod 13,

but its three signed coefficients are

(A0,A1,B)=(1-12,2(11-1),2(11-1+1))=(2,7,9) mod 13.

This proves **diagonal-only loss on the actual finite Hasse face span**, not just on arbitrary six-dimensional test vectors. The actual source face row matrix has rank six over F_13; the n=(-3,-2,-1,0,1,2) minor has determinant 2 mod 13. The diagonal observer has rank three.

A separately exact and **shorter, two-face witness** occurs for p=37, m=6:

F_{-6}=(35,2,0,19,0,0), F_5=(30,11,33,5,14,29),
15F_{-6}+F_5=(0,4,33,31,14,29) mod 37.

Its scalar diagonal is zero, its signed observable (A0,A1,B)=(8,4,18) is nonzero. A six-face minor n=(-11,-10,-6,0,1,2) has determinant 22 mod 37. These are finite counterexamples to claims of general diagonal reconstruction; they **do not** preclude a cancellation by additional J/E, positive-infinity or high-high contributions in the complete original D25 target.

## D. Author exact checks, BRC and limitations

An independent standard-library Python evaluator constructed the f_r coefficients from exact rational product ratios rather than from the claimed Ward equation, then constructed genuine ordered finite moments and four original finite endpoints. It checked m=1,2,3,4,5,6 (p=7,13,19,25,31,37; composite 25 is **rational algebra only**, not a p-local finite-field case):

- 78 exact rankwise normalized bivariate Ward polynomial identities;
- 468 independent scalar/signed six-observer Ward coefficient equations;
- 234 exact six-coordinate inverse/reconstruction tests;
- 84 exact q_r(0) formulas; mod-prime q_r are units;
- authentic source span rank six for p=13,19,31,37 (finite observation), diagonal rank three, and the explicit p=13/p=37 signed-kernel certificates above.

The complete local checker and machine JSON accompany this turn; tests are author-side, not a native CM experiment or an independent review. The universal statements in A/B use the product-zero factor proof, unit denominators and explicit inverse; the finite-source witness statements are *only* for the named finite fields.

BRC **COMPOSE_APPLIED**: ordered (j,ell) population, Hasse label, true left/right finite faces, parameter sign, p-valuation and possible future signed observer are retained. The diagonal is a known non-injective observer on actual faces; the signed 3+2+1 extension repairs precisely that information loss. P000 and the existing frozen Source pin are unchanged.

Current Site gateway: static_machine_readonly; write_relay_enabled=false; research_authority_granted=false. A new read-only native continuation returned CONTROL_QUOTA; there is no verified winning CLAIM, authorized OPEN or native checkpoint. Controller support remains enterprise-math#1558. Neutral GitHub storage **does not** grant any such authority or mathematical admission.

UR V2's original four-file 94,687-byte bundle with SHA256 4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76 remains unavailable/unchecked; existing UR proof was not redone. Actual H0/B0, [X]U mod p^2, normalized Frobenius and signed J/E/infinity/high-high are still open. **Exact next scientific unit:** apply the genuine source J/E, Z^+ and ordered H_p populations to the signed 3+2+1 six-channel observer and prove or refute the required full source-preserving cancellation; do not mistake this auxiliary lemma for D25/LIFT/JT2 completion.