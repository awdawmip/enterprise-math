# D25 — Cauchy C1 reflection carrier and exact binomial/harmonic p² lift
Date: 2026-11-02. Research lane: chatgpt-research-hourly-enterprise-math-20260923.
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen scientific input c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged.
Status: AUTHOR-DERIVED / ALGEBRAICALLY PROVED (U3,U4) / FINITE EXACT CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.
Previous local frontier: research_notes/portable_direct/20261102_hourly_r11_d25_cauchy_gauss_pf_endpoint.md (U1/U2 and C1).

## U3. Elementary generating function of the exact reflection source
Set b_s=binom(2s,s)/8^s, u_s=-1/(4s b_s), U_m=sum_{s=1}^m u_s, U_0=0.
The unique series W(x)=sum_{s>=1} u_s x^s in Q[[x]] satisfies
  2x(1-2x)W'(x)-W(x)=-x,
  W(x)=-(1/2)*sqrt(2x/(1-2x))*arcsin(sqrt(2x)).
Here the latter expression means its rational formal Taylor expansion.
Proof: b_{s+1}/b_s=(2s+1)/(4(s+1)); hence u_1=-1,
(2s+1)u_{s+1}=4s u_s. Coefficient comparison gives the ODE; the
specified zero constant term selects its unique formal solution. Direct
differentiation of the arcsine expression proves the claimed series.
The cumulative-source generating series is exactly W(x)/(1-x).
Its first terms are -x-4x²/3-32x³/15-128x⁴/35.
For a_m=(1/2)_m(1/3)_m(2/3)_m/(m!)³, the prior ordered Cauchy
carry K0(z)=sum a_m U_m z^m is the coefficientwise Hadamard product
of sum a_m z^m and W(z)/(1-z). This is a precise generating-series
candidate for creative telescoping of the endpoint character C1,
with original (m,s) provenance intact.

## U4. Source-faithful p² lift for any prime p=6r+1>=7
All rational denominators below are p-adic units. For 1<=m<=2r and
1<=s<=m set J(n,m)=sum_{j=0}^{m-1} 1/(n-j), J(n,0)=0, and
  T_m=(-1)^m 2^(-m) C(3r,m) C(2r,m) C(4r,m),
  v_s=(-1)^(s+1) 2^s/(4s C(3r,s)),
  alpha_m=J(3r,m)/2+J(2r,m)/3+2J(4r,m)/3,
  beta_s=J(3r,s)/2,
  V_m=sum_{s=1}^m v_s, E_m=sum_{s=1}^m v_s beta_s.
For the original weighted Cauchy observer H_p=[(1+6theta)K0,p](1/2),
theta=z*d/dz, K0,p truncated at m=2r, the following congruence holds:
  H_p = Hbin_p + p Hharm_p  (mod p²),
where
  Hbin_p = sum_{m=1}^{2r} (6m+1) T_m V_m       (mod p²),
  Hharm_p= sum_{m=1}^{2r} (6m+1) T_m
                  (E_m-alpha_m V_m)          (mod p).
Proof. The exact parameter shifts
  1/2=-3r+p/2; 1/3=-2r+p/3; 2/3=-4r+2p/3
and the first-order product expansion in Z_(p) yield
  a_m 2^(-m) = T_m(1-p alpha_m) (mod p²).
Similarly b_s=(1/2)_s/(2^s s!) satisfies
  b_s=(-1)^s 2^(-s) C(3r,s)(1-p beta_s) (mod p²),
so u_s=v_s(1+p beta_s) (mod p²).
Multiplying these expressions and summing the original ordered pairs
1<=s<=m<=2r proves U4. No CM hypothesis is used.

## Narrow exact reduction and precision witness
The earlier first-digit finite conjecture C1 is exactly equivalent to
  Hbin_p ?= 3*((2/p)-1) (mod p)
for all primes p=6r+1. The binomial kernel is a terminating
integer-combinatorial WZ target; additionally 6m+1=6(m-r) (mod p).
This equivalence follows from U4; the universal character evaluation
remains open.

Conditionally on C1, the second digit has the exact decomposition
 [(H_p-3*((2/p)-1))/p]
  = [(Hbin_p-3*((2/p)-1))/p] + Hharm_p (mod p).
For p=373: p²=139129, (2/p)=-1,
Hbin=64523 (mod p²), Hharm=59 (mod p), H=86530 (mod p²).
The binomial second digit is (64523+6)/373=173, while
the original observer's digit is (86530+6)/373=232,
and 173+59=232 (mod 373).
This is a concrete BRC observer-specific information-loss certificate
if the harmonic provenance carrier is discarded at p² precision.

The companion exact integer program tests pointwise coefficient expansions
and the final observer using independently calculated hypergeometric and
binomial recurrences. At 611/611 primes 7<=p<=10000 with p%6=1 it passes
the U4 formula and the finite C1 check. This numerical window is not
used as a general proof of C1. Additional second-digit examples:
p=13:2 (harm=7), p=19:15 (harm=11), p=37:21 (harm=17),
p=43:41 (harm=27), p=1171:917 (harm=1017).

## Continuation
Mother target remains signed Delta_p-R_p=0 (mod p) for p=13,19 (mod24).
Next exact action: creative-telescoping/contiguous search on the
terminating binomial core Hbin mod p with centred 6(m-r) weight,
and proof or genuine prime counterexample to C1. Use the U4 harmonic
port to extend any successful signed identity to p² and compare
existing second-carry observations; do not duplicate U1/U2 or
known CM0/R_p provenance. Raw p373 H0/B0 remains a distinct native
experiment. Treat U3/U4 as author-side portable evidence, not
native completed_units or accepted Result.
Observed service 2026-11-02: Gateway 0.6.11,
UPSTREAM_CODE_REVIEW_REQUIRED, research_authority_granted=false,
executor_binding_configured=false. Issue #6637 read-only recovery:
old service session MCP-06f7ad61a8d841d9ba1ba1ef4d088d94,
no claim/run, no pending operation; #6638 continuation FAILED.
Preserved staging disposition references remain protected. No new
native session/CLAIM/OPEN/checkpoint/freeze/review created.
Activity registration and independent mathematical admission pending.
P000/ACTIVE worldview, source pin and separate Research lane unchanged.