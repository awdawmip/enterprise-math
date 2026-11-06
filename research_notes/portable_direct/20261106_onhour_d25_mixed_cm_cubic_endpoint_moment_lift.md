# D25 — Mixed-CM cubic weighted endpoint lift: exact three-branch p-adic moment certificate

Date: 2026-11-06. Origin: TASK_RESEARCH on-hour logical lane `chatgpt-research-onhour-enterprise-math-20260923`. Scientific pin: `c47e13e4aba0e006366f989d6334d443f6333ae3`, publication `TP2-B6F4FC938FF94941C1B7`. Author-side math: PROVED (elementary identity and valuation corollary); finite arithmetic: CHECKED; admission: UNREVIEWED / NOT_ADMITTED. This note is not a Source Result and not native 373 H0/B0 execution.

## Inputs / dependency and preserved observer

Consume the prior **exact** convolution theorem (E1) and valuation partition (E3) from commit `37f417a0fbfad1806b092d0c685d2f3c310e71fe`, `20261106_onhour_d25_mixed_cm_cubic_original216_valuation_bridge.md`. In particular, this note does not re-prove the published preprint supercongruence or claim a transfer from a cubic coefficient to the original evaluation.

Let p=6m+1 be a prime >3. Define
`gamma_k=binom(2k,k)^2 binom(3k,k)`,
`b_0=1; b_n/b_(n-1)=6(6n-5)(3n-2)/n^2`.
For 1<=k<=p-1, `T_k=gamma_k*b_(p-k)`; let `Gamma=gamma_p`, `B=b_p`. These are all p-integral. Distinguish original k, reflected b-index, p-adic valuation, and the signed weight.

The exact Cauchy/derivative identity for every integer n>=0 is
`sum_(k=0)^n (6k-4n)*gamma_k*b_(n-k)=0`.   (1)
This follows coefficientwise from `B(z)^2=sum gamma_k z^k` and `theta(B^2)B=(2/3)theta(B^3)`, where `B(z)=sum b_n z^n`. Equation (1) at n=p is
`2p*(Gamma-2B) + sum_(k=1)^(p-1)(6k-4p)*T_k=0`. (2)

## New theorem — two digits of the endpoint mismatch with separate signed ports

Use the valuation bands already established by E3: `v_p(T_k)=2` for 1<=k<=2m; `v_p(T_k)=3` for 2m+1<=k<=3m and 5m+1<=k<=6m; `v_p(T_k)>=4` for 3m+1<=k<=5m. Set
`L_k=T_k/p^2` on [1,2m], and `V_k=T_k/p^3` on `M=[2m+1,3m]` and `U=[5m+1,6m]`. All are in Z_(p).

**For every prime p=6m+1>3,**
`
(Gamma-2B)/p =
 -3 sum_(k in [1,2m]) k L_k
 +p*(2 sum_(k in [1,2m]) L_k -3 sum_(k in M union U) k V_k)
                    (mod p^2).                       (3)
`
In particular `Gamma=2B (mod p)`. Proof: divide exact (2) by 2p, substitute the valuation-band factors, and reduce modulo p^2. The [3m+1,5m] band vanishes only at this precise precision; the M and U branches remain separate. The formula requires no external preprint or floating-point approximation. The p-adic division by p in (3) is justified by (2) and the valuation bands.

By classical Wolstenholme/Jacobsthal binomial congruence `binom(ap,p)=a (mod p^3)` for fixed a=2,3 and p>=5, `Gamma=12 (mod p^3)`. Thus the new branchwise finite formula also gives
`
B = 6 +(3p/2) sum_L k L_k -p^2 sum_L L_k
    +(3p^2/2) sum_(M union U) k V_k (mod p^3).       (4)
`
All denominators 2,3 and 216 are p-units. Equation (4) is a derived p-adic formula for the mixed-CM terminal coefficient b_p with explicit low, middle and upper signed provenance. It is not the frozen W_p supercongruence.

## Executed, independent arithmetic

The accompanying integer-only checker used the original b-recurrence modulo p^6 (therefore b_(p-1)/p^2 modulo p^4 is determined), integer binomial coefficients for gamma, and independently checked exact (1) in Q for p=7,13,19,31. All **80 primes p<=997, p==1 (mod 6)** passed: valuation intervals, (2) modulo p^4, (3) modulo p^2, and the `Gamma=12 (mod p^3)` / (4) consequence. 45 primes are in the frozen residue classes. `p=19`: `(Gamma-2B)/p=247 (mod 361)`, low term 285, p-times correction 19*17; correction ports (low,middle,upper)=(13,17,6) mod19. `p=373`: endpoint quotient 28721 mod139129, low term 111900, p-times correction 373*150; ports (77,150,296) mod373. Correct checks: 285+323=247 mod361, 111900+55950=28721 mod139129.

The middle and upper ports are individually generally nonzero, including p=19 and p=373. Their cancellations are signed observer effects and cannot be inferred from a single total valuation or the p^4-negligible middle gap. `gamma_p` and `b_p` are terminal coefficients of the mixed-CM coefficient observer, *not* direct copies of original 216 weighted evaluation `W_p`.

## Next exact action and unresolved original objective

The parent target is still `Delta_p-R_p=0 (mod p)` for p=13,19 mod24, equivalently under the frozen scalar interface to `W_p=p (mod p^3)`. Next: test if the branchwise two-digit endpoint formula (3) can pair with the already proved **original-evaluation** signed Green observer `J_p=sum_(t=1)^m h_t P_t` to produce a genuine finite adjoint transfer. In particular construct the missing operator kernel mapping the original **evaluation functional** to the mixed-CM coefficient without discarding M/U or the original J19=6, J373=98. If the operator lacks a source-preserving p-unit lift, record the minimal obstruction and keep the competing original-Gauss-moment path. The former p373 original H0/B0 divided-power [X]U, rank, Frobenius direction/eta, kappa and independent replica remain NOT_EXECUTED/PENDING_OWNER at Issue #1559.

BRC resolution: COMPOSE_APPLIED — exact signed p-adic valuation/branch carrier and two derivative observations, preserving distinct low/M/U ports and the original 216/CM observer separation. No positive-mass approximation or arbitrary branch quotient.
