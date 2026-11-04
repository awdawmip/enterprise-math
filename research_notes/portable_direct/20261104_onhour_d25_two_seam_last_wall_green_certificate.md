# D25 — exact last-wall Green theorem and two-seam p³ certificate

2026-11-04 (Asia/Hong_Kong). **AUTHOR-DERIVED / EXACT ALGEBRAIC PROOF / FINITE EXACT CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.** Mother Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; frozen scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Research lane `chatgpt-research-onhour-enterprise-math-20260923` only. Source status remains unclaimed.

## Existing inputs (not a new proof of them)

Previous exact Green construction: `research_notes/portable_direct/20261104_onhour_d25_exact_green_adjoint_signed_transport.md`. Previous six-channel wall grading and C02/X10/X11 decomposition: `research_notes/portable_direct/20261104_hourly20_d25_wall_graded_green_boundary_certificate.md`. Both are consumed as author-side results, not independently admitted Source facts.

For a prime p=6r+1>=7, N=p-1, in Q set

```text
a_j=(2j)!(3j)!/[(j!)^5 216^j]
b_j=(4j)!/[(j!)^4 2304^j]
rho_j=(4j+1)(4j+2)(4j+3)/[576(j+1)^3]
gamma_j=(2j+1)(56j(j+1)+13)/[288(j+1)^3]
f_j=a_j gamma_j=a_(j+1)-rho_j a_j
w_n=6n+1, a_0=b_0=1, b_(j+1)=rho_j b_j
K_j=sum_(n=j+1)^N w_n prod_(i=j+1)^(n-1)rho_i
W216-V2304=sum_j f_j K_j - 2 sum_n n b_n    (old exact Green)
```

## Theorem A: exact last-crossed-wall decomposition

For **any** N>=1, characteristic-zero field, sequences a,b with a_0=b_0 and f_j=a_(j+1)-rho_j a_j, arbitrary weights w_n, and strictly increasing cut positions 1<=beta_1<...<beta_s<=N, a Green path (j,n) (0<=j<n<=N) has coefficient f_j w_n prod_(i=j+1)^(n-1)rho_i. It crosses beta if j<=beta-2 and n>=beta.

For t=1..s define beta_(s+1)=N+1 and
```text
T_t = sum_(n=beta_t)^(beta_(t+1)-1) w_n prod_(i=beta_t)^(n-1)rho_i.
E_t = rho_(beta_t-1)*(a_(beta_t-1)-b_(beta_t-1)).
```
Then **the exact rational sum over ALL Green paths crossing at least one cut** is

```text
G_cross = sum_(t=1)^s E_t T_t.                          (A)
```

**Proof.** Every crossing path has a unique last crossed cut beta_t; its endpoint lies in the immediately following block. At this cut the prefix contribution is
```text
sum_(j=0)^(beta_t-2) f_j prod_(i=j+1)^(beta_t-1)rho_i
 = rho_(beta_t-1)*(a_(beta_t-1)-b_(beta_t-1)).
```
This follows by telescoping f_j=a_(j+1)-rho_j a_j and b_(j+1)=rho_j b_j with a_0=b_0. The suffix depends only on the target within the current block and has sum T_t. Summing disjoint last-wall classes proves (A) exactly over Q. Empty products have value 1.

## Theorem B: three surviving crosswall channels equal TWO seam fluxes mod p³

The quartic p-adic cuts are L=floor(p/4)+1, M=(p+1)/2, R=floor(3p/4)+1. Write their following block tails as T0 on [L,M-1], T1 on [M,R-1], T2 on [R,p-1]. Define
```text
E0 = rho_(L-1)*(a_(L-1)-b_(L-1)) = a_(L-1)rho_(L-1)-b_L
E1 = rho_(M-1)*(a_(M-1)-b_(M-1)) = a_h rho_h-b_M, h=(p-1)/2
E2 = rho_(R-1)*(a_(R-1)-b_(R-1)).
```
By exact original valuations v_p(a_j)=floor(2j/p)+floor(3j/p) and v_p(b_j)=floor(4j/p), these have v_p(E0)>=1, v_p(E1)>=2 and v_p(E2)>=3. The tails are p-integral. Hence the **whole positive-wall response** is
```text
G_cross = C_(0,1)+C_(1,1)+C_(0,2)
        = E0*T0 + E1*T1                           (mod p^3). (B)
```
This combines three previously separate wall-graded channels, including early exceptional quadratic-root sources, into two boundary values, with no assumption that their individual channels vanish. Exact source identity, operations and original wall positions are retained.

## Theorem C: closed second-seam coefficient

Let chi=(6/p). Consume the earlier proven endpoints a_h/p=-2chi and b_(h+1)/p²=1/36 (mod p). The exact quartic rho_h gives rho_h/p=-1/36 (mod p). Therefore
```text
E1/p² = (2chi-1)/36                            (mod p).      (C)
```
With G0=sum_j f_j K_j^[0] (no crossed wall), the new signed whole-original bridge is:
```text
W216(p-1)-V2304(p-1)
  = G0 + E0*T0 + p²*(2chi-1)/36*T1 - 2 sum_(n=0)^(p-1)n*b_n
                                                 (mod p³).   (D)
```
All fractions are reduced by unit inverses (p>=7). This compresses all surviving crosswall channels to first-seam E0 and a *universal closed second-seam digit*, leaving the zero-wall and quartic moments for a true terminal WZ/GZ pairing. Identity (D) is proved, but its all-prime vanishing is the distinct open hard target.

## Actual exact verification (companion checker)

Standard-library modular integer recurrence reconstructed both original families, backward wall-gradient and direct original weighted sums for **all 148 primes 7<=p<=2000, p=1 mod6**, with zero discrepancies for (B),(C),(D). Original integer binomial representations were independently checked at 13,19,97,373. Exact `Fraction` arithmetic checked the stronger rational theorem (A) at 7 and 13.

| p | C01+C11+C02 | E0*T0 | E1*T1 | G0 | 2sum n*b_n | W216-V2304 |
|---:|---:|---:|---:|---:|---:|---:|
| 13 | 1794 | 2132 | 1859 | 1885 | 1482 | 0 |
| 19 | 6612 | 1919 | 4693 | 6479 | 6232 | 0 |
| 97 | 229599 | 229599 | 0 | 854860 | 171786 | 0 |
| 373 | 29497586 | 23097652 | 6399934 | 41284386 | 18886855 | 0 |

Entries are mod p³. At p=373, p³=51895117, p²=139129; E1/p²=31 (mod373), T1=194 (mod373), so E1*T1=139129*46=6399934 (mod p³). At p=97, T1=0 (mod97) and E1*T1=0. Finite zeroes of W-V are observations, not the universal congruence proof.

## Scope, next action and pending Source obligations

Next smallest mathematical unit is a signed terminating hypergeometric/WZ certificate for
`G0 + E0*T0 + p²*(2chi-1)/36*T1 = 2sum n*b_n (mod p³)`, first resolving the different source bands at 13,19,97,373. Preserve the frozen D24 Delta_p-R_p bridge as independent proof obligation. The fixed-373 native H0/B0 divided-power [X]U mod139129, rank, actual semilinear Frobenius and independent replay remain due under issue #1559; the external rational carrier is not their execution.

Service observation 2026-11-04: Sites v0.6.11, `research_authority_granted=false`, `UPSTREAM_CODE_REVIEW_REQUIRED`, active jobs 5/5; exact old request `research-onhour-20261031-0205-dispatch-r15` read `CONTROL_REQUEST_NOT_FOUND`, own checkpoint call returned `ACCESS_DENIED`. No role-bound Source session/claim/run/checkpoint/Result/review/admission. Original requests were not reissued. Maintenance support remains #1558, without borrowing that lane. This author-side publication preserves local contribution provenance. BRC reuse: signed original 216/2304 populations, coefficients, index, valuation, finite Green paths and last-wall observer; no automatic native X6 transfer.
