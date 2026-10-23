# Auxiliary BRC: strict all-round threshold monotonicity and finite gain lifespan

**Date:** 2026-10-23. **Status:** Unreviewed author-side mathematical derivation, NOT an admitted Enterprise Math Result, NOT a native X6 theorem. This is a follow-on to the separately unreviewed N31 author proof, immutable commit `b70c8cf71b9557569da66eddf44ebdd4057d082c`, path `research/unreviewed/brc_uniform_pulse_20261023/N31_AUTHOR_THEOREMS.md`.

**Control/source pins:** GLOBAL_KNOWLEDGE_V1 main@`90248aab307c325e45690bb2bc147e483a18734b`; enterprise-math main@`a57e28e541c36c73cbe37cd553caaacfaa7f0185`; P000 startup projection checked against canonical Blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`. Native `em_control_tasks` returned `CONTROL_QUOTA`, and `em_session_start` returned `STATIC_READONLY_SCOPE_DENIED` (`operation_sent=false`). Neither owner nor formal CLAIM was established. This branch is research persistence only, not mathematical admission.

## Exact model and reused all-round single-pulse identity

There are four hidden labels U={0,1,2,3}, with independent per-round outputs of action 0 distributed as `q0/3=(0,1+z,1-z,1)/3` and action 2 as `q2/3=(1,1,0,1)/3`, with z in [0,1]. Good occupied label sets are G={{0,1},{1,2},{1,3},{2,3}}. Define delta_t=P(D_t in G), Delta_t=delta_t-delta_(t-1), M_t=max(delta_0,...,delta_t), R_t=sum_(j=2)^t [Delta_j]_+ - M_t.

For single-pulse protection word `p^(n,k)=0^(k-1) 2 0^(n-k)` with n>k>=4, the N31 author-side computation proved

`R_n - R_(n-1) = [Z_n(z)]_+ / 3^n`,

where `[x]_+=max(x,0)` and

`Z_n(z)=4-2^(n-2)-2(1-z)(2+z)^(n-2)-(1+z)(2-z)^(n-2)+(2-z)(1+z)^(n-2)`.

The same N31 algebraic argument states that for every n>=4, Z_n has exactly one simple positive real zero theta_n in (0,1), and Z_n(z)>0 on [0,1] precisely when z>theta_n. The present research *reuses* this exact lemma; it is not independently Research-Driver accepted.

## NEW THEOREM 1: strict decay in round number

For every integer n>=4 and every real z in [0,1), `Z_(n+1)(z)<Z_n(z)`. For z=1, `Z_n(1)=2` for every n.

**Complete proof.** Let m=n-2. Direct subtraction gives the *polynomial identity*

`Z_n(z)-Z_(n+1)(z) = 2^m + (1-z^2)[2(2+z)^m+(2-z)^m] - z(2-z)(1+z)^m`.

For z in [0,1), we have `0<=z(2-z)=1-(1-z)^2<1` and `1+z<2`; consequently `0<=z(2-z)(1+z)^m<2^m`. The middle term is nonnegative. Thus the right side is strictly positive. Substitution z=1 in the original polynomial yields Z_n(1)=2. QED. No finite search is needed for the general result.

## NEW THEOREM 2: threshold sequence strictly increases to 1

Assuming the algebraic all-n root-uniqueness lemma from N31, the exact critical parameters satisfy

`0<theta_4<theta_5<theta_6<...<1`, with `lim_(n->infinity) theta_n=1`.

**Proof.** At z=theta_n, Theorem 1 gives `Z_(n+1)(theta_n)<Z_n(theta_n)=0`. Since Z_(n+1) has one simple positive root with negative sign to its left, `theta_n<theta_(n+1)`.

For fixed 0<z<1, write m=n-2. The term `-2(1-z)(2+z)^m` dominates the other exponential terms, since `2+z>max(2,2-z,1+z)`; therefore `Z_n(z)->-infinity`. For z=0, directly `Z_n(0)=6-4*2^(n-2)->-infinity`. Thus every z<1 eventually lies below theta_n. The increasing sequence bounded by 1 therefore converges to 1. QED.

**Root-uniqueness lemma algebraic audit (inherited):** For m=n-2>=4, the coefficient of z^0 is `6-4*2^m<0`; that of z^(m+1) is `1+(-1)^(m+1)>=0`. For 1<=j<=m, with r=j/(m+1-j), H=(2+(-1)^j)*2^(m-j), the coefficient A_(m,j) satisfies `A_(m,j)/binom(m,j)=H(2r-1)+2-r`. It is positive when 3j>=m+1. Otherwise r<1/2 and `(2-r)/(1-2r)=1+(m+1)/(m+1-3j)<=m+2<H`, using H>=2^ceil(2m/3)>m+2 for all m>=4 (base m=4,5,6; induction m->m+3). Thus signs have exactly one change; m=2,3 follow from `Z4=9z^2+3z-10`, `Z5=2z^4+4z^3+21z^2+z-26`. Descartes plus `Z_n(0)<0<Z_n(1)=2` establishes existence and uniqueness counting multiplicity.

## NEW COROLLARY: an absorbing finite positive-gain window

For every fixed k>=4 and z in [0,1), the post-pulse residual increments `R_n-R_(n-1)` (n>k) are positive only for a possibly empty *initial contiguous finite block*. Once an increment vanishes, every later increment vanishes: no second revival is possible within this single-pulse family.

Indeed `R_n-R_(n-1)>0 <=> z>theta_n`; increasing theta_n and theta_n->1 give the block and finite termination. If z<=theta_(k+1), the block is empty; if theta_(k+1)<z<1, it starts at n=k+1 and terminates in finite time. For the endpoint z=1, all increments equal `2/3^n>0`, so the finite-lifespan conclusion explicitly excludes z=1.

This is about *increments* only; it does not assert the eventual residual R_n itself is zero. Nor does it classify arbitrary multiple-pulse or adaptive words.

## Verification, boundary, next unit

Independent standard-library `fractions.Fraction` checker and exact 16-state occupancy-mask DP: 963 direct polynomial-difference identities (n=4..110 and nine rational z values), 856 strict positivity cases z<1, 1,539 independent post-pulse occupancy/increment trials, 1,539 residual-increment trials, 17,199 peak-freeze checks, and exact dyadic root intervals for n=4..44 with 40 consecutive-order comparisons. All passed in local author execution. Finite checks support identities but are NOT an all-round proof. The full Chinese draft, source and machine-readable result log are also retained as conversation artifacts.

**Next mathematical unit:** find a uniform non-single-pulse last-increment negativity criterion that respects historical occupancy information, or construct a shortest exact counterexample. This auxiliary positive-mass four-label observer has no proved faithful transfer to native P000 Heartbeat World six-dimensional Cell dynamics. No change to P000/worldview, formal source result, author/Driver roles, CLAIM or promotion is asserted.
