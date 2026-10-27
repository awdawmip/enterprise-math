# D25/LIFT R38 — Exact p^4 four-port decomposition of the unchanged W/S upper halves

Date: 2026-10-27 (Asia/Hong_Kong). TASK_RESEARCH portable author calculation on the Research lane `chatgpt-research-hourly-enterprise-math-20260923` (distinct from maintenance). Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; parent D25/LIFT/JT2 **OPEN**. Scientific source frozen at `c47e13e4aba0e006366f989d6334d443f6333ae3`. **AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY**. No native CLAIM/open/Source checkpoint, original-class H0/B0, CM experiment, independent review, or W=S proof is claimed.

## Exact question and predecessor boundary

Consume R23's mod-p^3 low-half/W-high decomposition, R29's unique p-divisible S weight, R34/R35's p^4 one-index source jets, and R36/R37's separate integral Green and future rank-jet endpoint information laws without recredit. The smallest additional question is: what *genuine unchanged-input, source-labelled upper-half information* is necessary at the next modulus p^4? At p^3 the high-high region vanishes; at p^4 it need not. In particular, the S second-valuation region contains a single index with one additional valuation (p congruent to 13 mod 24); no division by its vanishing linear weight is permitted.

For any prime p=6m+1>=7, in Z_(p) define the *unchanged original terms*

```
w_k = (6k+1)*(2k)!*(3k)!/((k!)^5*216^k);
s_k = (8k+1)*(4k)!/((k!)^4*2304^k),
W_p = sum(k=0..p-1) w_k,  S_p = sum(k=0..p-1) s_k.
```

All inverses below are in the stated p-integral ring. Define J=floor(3m/2) and H=floor((3p-1)/4). The high ranks split into precisely four **tagged sources**:
`W2: k=3m+1..4m`, `W3: k=4m+1..p-1`; `S2: k=3m+1..H`, `S3: k=H+1..p-1`. The digit number on a port is a *factorial valuation lower bound*, not necessarily the actual valuation when a linear weight is divisible by p.

## Theorem 1 — exact rational second-valuation source transfers

Let F=(p-1)!=-1+pQ_p and q_p(b)=(b^(p-1)-1)/p for b=216,2304. For W2 index 2m<=j<=3m-1 set k=p-1-j, a=2k-p, b=3k-p, t=3j-6m+1 and

```
A_j=(6j+5)*216^j*(j!)^5 / ((2j+1)!*t!),
P_j=[prod(i=1..j)(1-p/i)^5 *
     prod(i=1..a)(1+p/i) * prod(i=1..b)(1+p/i)]/
    [prod(i=1..2j+1)(1-p/i) * prod(i=1..t)(1-p/i)].
```

Then **exactly as rational numbers**

```
w_(p-1-j)/p^2 =
 A_j * (1-6p/(6j+5)) * P_j /
 ((1-p*Q_p)*(1+p*q_p(216))).                                  (W2-exact)
```

Here every denominator `6j+5`, factorial and elementary product denominator is a p-unit. Let H_n=sum(i=1..n)1/i in Z_(p), H_0=0. Its next digit is

```
E^W_(p,j) = Q_p-q_p(216)-6/(6j+5)-5H_j+H_a+H_b+H_(2j+1)+H_t mod p,
w_(p-1-j)/p^2 = A_j*(1+p*E^W_(p,j)) mod p^2.                 (W2-jet)
```

For S2 index J<=j<=3m-1 set k=p-1-j, r=4k-2p, d=4j-6m+2 and Btilde_j=2*2304^j*(j!)^4/d!. Define

```
R_j=prod(i=1..p-1)(1+p/i) * prod(i=1..r)(1+2p/i) *
    prod(i=1..j)(1-p/i)^4 / prod(i=1..d)(1-p/i).
```

Then **exactly as rational numbers**

```
s_(p-1-j)/p^2 =
 Btilde_j * ((8j+7)-8p) * R_j /
 ((1-p*Q_p)*(1+p*q_p(2304))).                                 (S2-exact)
```

Crucially S2-exact and its jet contain **no division by 8j+7**. Set

```
E^S_(p,j)=Q_p-q_p(2304)+H_(p-1)+2H_r-4H_j+H_d mod p,
s_(p-1-j)/p^2 =
 Btilde_j*[(8j+7)+p*((8j+7)*E^S_(p,j)-8)] mod p^2.           (S2-jet)
```

**Special rank test:** for p congruent to 13 mod 24, `j*=(3p-7)/8`, `k*=(5p-1)/8`, `8j*+7=3p`, and the original term satisfies

```
s_(k*)/p^3 = -5*Btilde_(j*) (mod p).
```

The right-hand side is a unit, so an apparently missing second-valuation S source is a *nonzero third-digit* source, rather than one to erase. Examples: p=13 has j*=4,k*=8; p=181 has j*=67,k*=113 and s_(k*)/p^3=12 (mod 181). This test independently agrees with the preceding R29 valuation classification, but the regular all-rank jet is new.

**Proof.** Write `k=p-1-j` and split factorials at the completed p-blocks. For W2, `(2k)! = p*(p-1)!*a!*prod(i=1..a)(1+p/i)`, and similarly for 3k with b. Reflect `k!=(p-1-j)!=F/[(-1)^j*j!*prod(i=1..j)(1-p/i)]`. Reflect the unit factorials `a!` and `b!` using `a=p-1-(2j+1)`, `b=p-1-t`. The signs and two numerator F factors against five denominator F factors leave exactly `1/(-F)=1/(1-pQ_p)` with the displayed positive A_j. Fermat's identity `216^(p-1)=1+p q_p(216)` yields W2-exact. For S2, `(4k)!/p^2=2*(p-1)!^2 *r! *prod(i=1..p-1)(1+p/i)*prod(i=1..r)(1+2p/i)`; reflect r! via `r=p-1-d` and k! via the same complement. Three copies of F survive, again yielding exactly `1/(-F)`, and `8k+1=8p-(8j+7)` gives S2-exact with the stated sign. Expand `(1+px)^{-1}` and the products modulo p^2 to obtain both jets; the S formula is regular also at the special rank. All equalities are in the original factorial carrier, with no interpolation or changed polynomial input.

## Theorem 2 — third-valuation high-high ports

The previously absent rank regions contribute at p^3. Their **termwise exact mod-p residues after dividing by p^3** are, for 0<=j<=2m-1 (W3) and 0<=j<J (S3),

```
C_j = 2*(6j+5)*216^j*(j!)^5/((2j+1)!*(3j+2)!)       mod p,
D_j = 6*(8j+7)*2304^j*(j!)^4/(4j+3)!                mod p,
w_(p-1-j)/p^3 = C_j                                  mod p,
s_(p-1-j)/p^3 = D_j                                  mod p.
```

**Proof.** In W3 both numerator factorials cross full p-blocks and `3k` crosses two, so `v_p((2k)!(3k)!)=1+2=3`; their normalized completed-block factors have residues `(-1)*2`. In S3, `4k` crosses three blocks, giving the normalized factor `-6`. Apply Wilson factorial complements, inverse k!, the original linear weights and 216 or 2304 powers. The paired signs reduce to the displayed `+2` and `+6`. Extra weight factors divisible by p automatically contribute zero to the displayed mod-p classes (e.g. p=7 S3). All denominator factorial arguments are <p.

## Corollary — four-source p^4 normal form without changing original input

Let `A'_j=A_j*(1+p*E^W_(p,j)) mod p^2` and `B'_j=Btilde_j*((8j+7)+p*((8j+7)*E^S_(p,j)-8)) mod p^2`. Then **for every prime p=6m+1>=7**,

```
W_p-S_p =
  sum(k=0..3m)(w_k-s_k)
  +p^2*[sum(j=2m..3m-1) A'_j - sum(j=J..3m-1) B'_j]
  +p^3*[sum(j=0..2m-1) C_j - sum(j=0..J-1) D_j]
  (mod p^4).
```

The formula is an *identity in the original W/S source-labelled finite sums*; it does not assert W=S mod p^4 or prove the still-open p^3 cross-index WZ cancellation. Its new mathematical content versus R23 is the **all-rank second-valuation p-adic jet with a regular singular-weight term**, and the two previously omitted **third-valuation high-high families**. It also gives a concrete next-digit WZ target: a genuine WZ certificate for p^4 must compensate the indicated bracket and low-half jet, not only R23's p^3 `U_p`.

## Executed author checks, scope, and forward route

A standalone Python 3 standard-library exact checker was **actually executed** (original factorials via p-free modular products, independently derived harmonic/reflection RHS, and small-prime exact Fraction identities). It passed all 80 primes 7<=p<1000 with p=1 (mod 6), covering **6,098 W2 + 9,169 S2 + 12,196 W3 + 9,125 S3 distinct termwise positions**, plus complete p^4 W/S original finite sum comparisons. The W2-exact/S2-exact rational formulas were also compared symbolically to the original exact factorial fractions at p=7,13,19; special p13/p181 weight-zero S third-digit checks passed. Finite arithmetic corroborates but does not prove the universal result; the factorial arguments above are the proof. The actual script is `20261027_hourly_d25_p4_all_high_ports_r38_check.py` (author-side executable evidence; check publication status separately).

BRC **COMPOSE_APPLIED**: the state is `(original series W/S label, index k/j, prime, floor factorial valuations, linear weight valuation, p-adic unit, modulus, observer, allowed next-digit operations)`. Collapsing a source to zero modulo p^3 is **not safe** when the future observer is modulo p^4. Rank k is an arithmetic index, *not* a native six-axis Cell coordinate. P000/ACTIVE worldview, formal admission, independent native Frobenius and frozen scientific pin are unchanged.

**Next minimal research action:** compare the actual p^4 S half-truncation remainder with the S2/S3 ports; seek an explicit unchanged-input nonlocal WZ source that compensates the original R23 low-half p^2 defect, using R36 full Green adjoint and new R38 port jets. Do not infer an all-prime fourth-digit supercongruence from finite checking. Preserve the six z=2 Hasse J/E channels, both finite boundaries, positive infinity/high-high sources, p181 exceptional source, original native H0/B0, [X]U mod p^2, semilinear eta/kappa and independent Driver review. Source continuation checkpoint still prior to these portable notes; Research lane canonical authority must be recovered through #1558 before native CLAIM/open/publish.