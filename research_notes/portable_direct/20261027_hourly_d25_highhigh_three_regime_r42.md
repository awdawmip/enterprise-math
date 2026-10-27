# D25/LIFT R42 — Exact W3/S3 high-high transport and all upper-rank source regimes

2026-10-27 Asia/Hong_Kong. Portable TASK_RESEARCH author continuation, declared Research lane chatgpt-research-hourly-enterprise-math-20260923 (not a service-issued current session assertion). Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; D25/LIFT/JT2 OPEN. Frozen scientific Source c47e13e4aba0e006366f989d6334d443f6333ae3. AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Unchanged original terms and remaining source range

Reuse R39's W2/S2 exact unit transport and R41's exact singular W3/S2 transport. R38 already isolated separately the W3 and S3 high-high sources, and R40 proved the unique S-weight-zero valuation. The next range for a new all-order original-source relation is H+1<=k<p, where H=floor((3p-1)/4), p=6m+1>=7 prime.

~~~
w_k=(6k+1)(2k)!(3k)!/((k!)^5*216^k);
s_k=(8k+1)(4k)!/((k!)^4*2304^k);
tau_k=k!(4k)!/((2k)!(3k)!)*(3/32)^k;
a=2k-p, b=3k-2p, r=4k-3p (all in [0,p-1]).
~~~

## Theorem R42-A: Wilson-free high-high transfer and its first jet

Define

~~~
C33_(p,k)=3*k!*r!/(a!*b!)*(3/32)^k,
P33_(p,k)=
 prod(i=1..p-1)(1+2p/i) * prod(i=1..r)(1+3p/i)
 / [prod(i=1..a)(1+p/i) * prod(i=1..b)(1+2p/i)].
~~~

Then exactly as rational numbers,

~~~
tau_k = C33_(p,k)*P33_(p,k) in Z_(p)^x,                 (A1)
s_k/w_k = (8k+1)/(6k+1)*tau_k.                         (A2)
tau_k = C33_(p,k)*[1+p*(3H_r-H_a-2H_b)] (mod p^2).    (A3)
~~~

Proof: Write F=(p-1)!. The three exact p-free numerator factorial blocks are

~~~
(2k)!/p   = F*a!*prod_a(1+p/i);
(3k)!/p^2 = 2 F^2*b!*prod_(p-1)(1+p/i)*prod_b(1+2p/i);
(4k)!/p^3 = 6 F^3*r!*prod_(p-1)(1+p/i)*
                    prod_(p-1)(1+2p/i)*prod_r(1+3p/i).
~~~

All powers of F and the first full-block product cancel in tau, producing the factor 3 and A1; all its factors are p-units. A2 is exact unchanged-summand cancellation. First-order expansion of A1 gives 2H_(p-1)+3H_r-H_a-2H_b in the bracket; H_(p-1)=0 mod p for odd prime p, yielding A3. This is all-prime algebra, not finite interpolation. QED.

## Theorem R42-B: non-erasure of the p=7 special original S source

In the high-high band v_p(w_k)=3, and normally v_p(s_k)=3. Only for p=7 mod24 does k*=(7p-1)/8 fall in this band and make the S weight divisible by p. Let e=v_p(7) (e=1 exactly when p=7), ell0=7/p^e. The *original* normalizations satisfy the exact unit identity

~~~
  [s_(k*)/p^(4+e)] / [w_(k*)/p^3]
          = ell0*tau_(k*)/(6k*+1) in Z_(p)^x.          (B1)
~~~

Indeed 8k*+1=7p=p^(1+e)*ell0, so apply A2; there is no singular tau. The p=7 case has v_p(s_6)=5, rather than the generic class-7 valuation 4, and is NOT discarded.

For j=p-1-k, 0<=j<J=floor(3m/2), R38 gave distinct reflected original third-digit ports
C_j=2(6j+5)216^j(j!)^5/[(2j+1)!(3j+2)!] (W3),
D_j=6(8j+7)2304^j(j!)^4/(4j+3)! (S3).
Away from the exceptional weight A2 gives the p-unit relation

~~~
D_j=[(8k+1)/(6k+1)*tau_k] C_j (mod p).               (B2)
~~~

At k*, D_j=0 but B1 recovers its next nonzero digit. At p=31,k*=27: (w/p^3,s/p^4,tau)=(7,1,28) mod31. At p=7,k*=6: (w/p^3,s/p^5,tau)=(5,6,1) mod7. Both meet B1.

## Theorem R42-C: complete upper-half typed transport

Consume R39 + R41 + R42. For every 3m+1<=k<p define delta_k=1 for 4m+1<=k<=H, and delta_k=0 otherwise, with u_k=p^(delta_k)*tau_k. Every u_k is a p-unit and

~~~
s_k = p^(-delta_k)*(8k+1)/(6k+1)*u_k*w_k         (exact).
~~~

Regimes: 3m+1..4m is (W2,S2,delta=0,R39); 4m+1..H is (W3,S2,delta=1,R41); H+1..p-1 is (W3,S3,delta=0,R42). The S-weight-zero ranks p=13 mod24 in the first band and p=7 mod24 in the third band remain distinct and explicitly weighted. An all-band *unit-diagonal* W/S transfer is impossible because delta=1 in the middle band. The three-regime map changes neither original summand and retains both labels and every p-adic digit. It is NOT the missing W_p=S_p modulo p^3, because weights are not one and the low-half sources are not compensated.

The executed standard-library file 20261027_hourly_d25_mixed_filtration_upper_transport_r41_r42_check.py checks all 80 primes 7<=p<=997, p=1 mod6: 9,125 W3/S3 positions, 21 p=7 mod24 special indices, exact unit products modulo p^3, first jets modulo p^2, plus R41's 3,071 W3/S2 positions and finite S2 aggregate. All PASS. The general proof is factorial algebra; author-side finite checks are NOT the original-class native CM/H0/B0 or independent mathematical review.

BRC COMPOSE_APPLIED: carry (actual W/S provenance, integer rank, valuation, p-unit or one-power pole, original linear weights, modulus, observer, Green finite/infinite endpoint). No P000 or ACTIVE-worldview change; ranks are not X6 axes. No role-bound claim/open/Source checkpoint/Result/review asserted.

**Next smallest open scientific question:** construct or obstruct a *genuine nonlocal unchanged-input WZ compensator* for R23's sum_(k<=3m)(w_k-s_k) = -p^2 U_p (mod p^3) using the three upper transfer types with R36's exact endpoint Green adjoint. Preserve p=181's exceptional S tail, p=19 mod24 low-half S weight, original fixed z=2 six-channel Hasse J/E 3+2+1, both finite boundaries, positive infinity/high-high sources, original H0/B0, [X]U mod p^2, eta/kappa, p373 native experiment and independent Driver review. Mother D25/LIFT/JT2 remains OPEN; existing control support #1558 owns the predecessor CLAIM recovery.
