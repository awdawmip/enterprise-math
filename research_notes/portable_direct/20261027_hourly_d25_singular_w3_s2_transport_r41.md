# D25/LIFT R41 — Wilson-free singular W3/S2 transfer

2026-10-27, Asia/Hong_Kong. TASK_RESEARCH portable author research. User-declared Research lane: chatgpt-research-hourly-enterprise-math-20260923; no native session ownership inferred. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Parent D25/LIFT/JT2 OPEN. Frozen scientific Source c47e13e4aba0e006366f989d6334d443f6333ae3, not the mutable control HEAD. AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Previously verified frontier and fresh question

R23 established the S upper-half second-valuation aggregate cancellation using Guo–Zudilin, *A q-microscope for supercongruences*, Adv. Math. 346 (2019); this external proved S result does not imply W=S. R38 identified four genuinely different W2/W3/S2/S3 ports at precision p^4. R39 proved unit W2/S2 transfer only for 3m+1<=k<=4m. R40 classified the S linear-weight singularity. The still-unpaired interval 4m+1<=k<=H=floor((3p-1)/4) has W3 but S2 source valuation. We retain ORIGINAL, UNCHANGED rational terms:

~~~
p=6m+1 prime, p>=7;
w_k=(6k+1)(2k)!(3k)! / ((k!)^5*216^k);
s_k=(8k+1)(4k)! / ((k!)^4*2304^k);
tau_k=k!(4k)! / ((2k)!(3k)!) * (3/32)^k.
~~~

For each k in the stated band, put a=2k-p, b=3k-2p, r=4k-2p, c=3p-1-4k; these lie in [0,p-1]. v_p(w_k)=3, v_p(s_k)=2, and 6k+1,8k+1 are p-units. A same-index unit transfer s_k=u_k w_k is therefore IMPOSSIBLE on this band. The correct transfer has a sharp one-power pole.

## Theorem R41-A: exact Wilson-free singular transport

Define sigma_(p,k)=p*tau_k and

~~~
C_(p,k)=(-1)^c * k!/(a!*b!*c!) * (3/32)^k,
P_(p,k)=prod(i=1..r)(1+2p/i) /
 [prod(i=1..a)(1+p/i) * prod(i=1..b)(1+2p/i)
  *prod(i=1..c)(1-p/i)].
~~~

**Exact rational identities**, with sigma a p-unit:

~~~
sigma_(p,k)=C_(p,k)*P_(p,k),                             (A1)
s_k/p^2=(8k+1)/(6k+1) * sigma_(p,k) * (w_k/p^3).        (A2)
~~~

Proof: F=(p-1)!. Exact factorial block splitting gives
(2k)!/p=F*a!*prod_a(1+p/i);
(3k)!/p^2=2F^2*b!*prod_(p-1)(1+p/i)*prod_b(1+2p/i);
(4k)!/p^2=2F^2*r!*prod_(p-1)(1+p/i)*prod_r(1+2p/i).
Insert into p*tau to obtain k!r!/(F a!b!)*(3/32)^k times the stated three product factors. The exact factorial reflection F=(-1)^c r!c! prod_c(1-p/i), since r+c=p-1, cancels F without a Wilson quotient and proves A1. All remaining factors are p-units, proving sharp v_p(tau)=-1. Direct unchanged rational summand cancellation yields s_k/w_k=(8k+1)/(6k+1)*tau_k, hence A2. QED.

## Theorem R41-B: next digit and source-labelled mixed port

Let H_n=sum_(i=1..n)1/i in Z_(p), H_0=0. A1 immediately gives

~~~
sigma_(p,k) = C_(p,k)*[1+p*(2H_r-H_a-2H_b+H_c)] (mod p^2). (B1)
~~~

Reflect j=p-1-k, J=floor(3m/2)<=j<=2m-1. The R38 genuine W3 and S2 source residues are

~~~
C_j=2(6j+5)216^j(j!)^5 / [(2j+1)!(3j+2)!] (mod p), W3;
B_j=2(8j+7)2304^j(j!)^4 / (4j-6m+2)! (mod p), S2.
~~~

Then, with k=p-1-j,

~~~
B_j=[(8k+1)/(6k+1)*sigma_(p,k)]*C_j (mod p).       (B2)
~~~

Thus an actual S2 contribution is a **p-unit multiple of the normalized W3 third-valuation source**, not a unit multiple of the raw W3 source. Combining B2 with previously proved R39 W2/S2 transfer and CONSUMING, not recrediting, R23's external-theorem-supported S2 aggregate cancellation gives the mixed-filtration identity

~~~
0 = sum_(j=J..2m-1) [(8k+1)/(6k+1)*sigma_(p,k)] C_j
  + sum_(j=2m..3m-1) [(8k+1)/(6k+1)*tau_k] A_j  (mod p),
k=p-1-j,
A_j=(6j+5)216^j(j!)^5 / [(2j+1)!(3j-6m+1)!] (mod p), W2.
~~~

This is a source-labelled representation of KNOWN S2 cancellation, not a W/S supercongruence proof or permission to erase provenance.

At p=181,k=121,j=59, independently calculated residues mod181 are w_k/p^3=146, s_k/p^2=129, sigma=162, and (8k+1)/(6k+1)*sigma=17; 146*17=129. At p=7,k=5 corresponding residues are 1,2,1 with weighted sigma=2.

The shared, actually executed Python checker 20261027_hourly_d25_mixed_filtration_upper_transport_r41_r42_check.py passed 80 primes 7<=p<=997, p=1 mod6, including 3,071 R41 interval terms, exact p-free factorial product tests mod p^3 and jets mod p^2; a fuller author-local checker also checked R38 reflected port formulas and 12 exact Fraction equalities at p=7,13,19. These finite checks corroborate the displayed all-prime factorial proof. Not a native H0/B0 / p373 CM experiment, formal Source checkpoint, review or Result.

BRC COMPOSE_APPLIED: (original W/S label, rank, valuation, regularized unit sigma, future modulus/observer and boundary) is retained. The rank is an arithmetic index, not an Enterprise native six-axis Cell coordinate. P000, ACTIVE worldview and frozen scientific Source pin are unchanged.

**Next unit:** derive the exact W3/S3 high-high p-unit transport on H+1<=k<p, with p=7 double S-weight case, then assemble the source-preserving three-regime upper transport. Neither that nor this note resolves the original low-half WZ compensation or the fixed z=2 six Hasse J/E and finite/infinite boundaries.
