# D25 — terminating 4F3 form and signed monotonicity of the exact single-carry shell

Date: 2026-11-06. Author-side PORTABLE / EXACT ALGEBRA / 428-PRIME FINITE CHECK / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CHECKPOINT. Continues the separately published single-carry support lemma at main@962871a342fb7148bdf09ccf21e50c811b649898; does not recredit it.

Mother task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7, frozen input c47e13e4aba0e006366f989d6334d443f6333ae3.

## A finite 4F3 identity for every prime q>=5

Set eps_q=1 for q=1 mod6, eps_q=-1 for q=5 mod6, m=(q-eps_q)/6, delta=(1-eps_q)/2 and a=2m-delta, b=3m-delta, c=4m-delta. Work in F_q; all displayed denominator parameters below are units throughout the terminating range.

Define
  F_m(z) = _4F_3(1-m,1-2m,1,1; a+2,a+2,a+2; z),
a polynomial of degree m-1, and
  E0 = (-1)^(a+1) * 2^(-(a+1))/(a+1) * binom(b,a+1) * binom(c,a+1).

For the source-labelled D25 directional jet M_j(t)=(-1/2)^j prod_{s=a,b,c}binom(s+t,j) j!/(1-3t)_j and S_shell=sum_{j=a+1}^b (6j+1) M_j'(0), the exact finite-field identity is

  S_shell = E0 * [ (6a+7)*F_m(1/2) + 6*(1/2)*F_m'(1/2) ]  (mod q).

The derivative here is an ordinary polynomial derivative in its argument z, not the original parameter derivative t. Their roles are explicitly distinguished. In particular 6a+7 is a nonzero q-unit: it reduces to 5 for q=6m+1 and to 3 for q=6m-1.

Proof: put j=a+1+t, 0<=t<=m-1. The previous single-zero binomial derivative gives

  M_(a+1+t)'(0) = (-1)^(a+1) 2^(-(a+1+t))
                  * a! t!/(a+1+t)! * binom(b,a+1+t)binom(c,a+1+t).

Thus the first term is E0, while the ratio of successive shell terms is

  M_(j+1)'(0)/M_j'(0) =
  (j-a)(b-j)(c-j) / [2(j+1)^3]
  = (t+1)(m-1-t)(2m-1-t)/[2(a+2+t)^3].

All shell terms are q-units, so this quotient is legitimate. Exactly the same quotient occurs between successive terms of F_m(1/2), since its coefficient is
  (1-m)_t (1-2m)_t (1)_t / (a+2)_t^3 * (1/2)^t.
Multiplication by 6(a+1+t)+1 is exactly the differential operator (6a+7)+6z*d/dz at z=1/2, proving the formula.

## A sign-sensitive observation in ordinary rational representatives

Before reducing modulo q, every shell term has the fixed sign (-1)^(a+1), including the positive weight (6j+1). Its unsigned successive ratio is strictly between 0 and 1/2, because for a<j<b each of j-a, b-j, c-j is positive and strictly below j+1. After the linear weight, the ratio is still <1 as (6j+7)/(6j+1)<2. Hence the rational shell is sign-coherent with strictly decreasing magnitudes; the net mod-q shell sum can nevertheless be zero because reduction is not order preserving (example q=17).

This cleanly separates a signed rational shell from finite-field cancellation and keeps the original binomial labels available to BRC.

## Independent exact checks and next certificate target

A standalone Python implementation evaluates the terminating 4F3 term ratio and its weighted derivative, then compares it with the separate factorial/harmonic single-carry implementation over every prime 5<=q<=3000. Result 428/428 PASS. Values S_shell for q=5,7,11,13,17,19,373,1009,2003 respectively: 3,5,8,8,0,17,292,863,300.

The earlier conditional Theta criterion, where L=0 and q divides W_q, is now the explicit hypergeometric matching problem

  E0[(6a+7)F_m(1/2)+3F_m'(1/2)]
    ?= 6Z-6(W_q/q)-S_regular    (mod q).

This is the next precise WZ/contiguity target, not a theorem proved here. The native original-class H0/B0, [X]U mod373^2, semilinear Frobenius eta/kappa and frozen Delta_p-R_p remain separate required obligations. No service Researcher session, new claim/open/run or canonical native checkpoint is asserted.

## Source provenance

Previous author-side note and verified executable: commit 962871a342fb7148bdf09ccf21e50c811b649898. Current project ACTIVE P000 and Heartbeat World rules read separately; frozen scientific pin unchanged.