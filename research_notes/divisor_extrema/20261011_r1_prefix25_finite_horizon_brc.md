# Research1: divisor-extrema prefix through 25 nonzero layers; finite-horizon BRC quotient

Progress-Event-ID: `em-r1-divisor-prefix25-brc-finite-horizon-20261011`
Date: 2026-10-11
Status: `AUTHOR_LOCAL_VERIFIED / COMPUTATION_ASSISTED / UNREVIEWED / NOT_ADMITTED`
Project: Enterprise Math — external classical integer-arithmetic example, NOT P000 native dynamics.
Source pins: Global `2415716de586c52eb2615cc10604432998460ece` / `GLOBAL_KNOWLEDGE_V1`; Enterprise Math `3d174bc233263dd45efebc34e5704e7506991ba5`.
Prior activity (metadata only, no CLAIM): `research_activity_records/RA-R1A11-20261011-DIVISOR23.json`.
Real native gateway inventory: `execution_authorized=false`; no formal owner CLAIM/Result/Driver review issued for this note. Independent research under existing user direction; no ownership change.

## Theorem A (author-computation-assisted; exact full-range proof certificate)

For `D_k(N)=max{tau(n):1<=n<=N,omega(n)=k}`, `D_0(N)=1`, and `K(N)=max_{n<=N}omega(n)`, the sequence `D_0(N),...,D_{min(25,K(N))}(N)` is unimodal for EVERY positive integer N. The claim covers the first 25 nonzero layers, not all unbounded k.

Normalization proof: mapping exponents of any `k`-prime integer in descending order to the first k primes never increases n and preserves tau and omega; enumerate ALL normalized exponent vectors for finite bound to determine every D_k(N), including thresholds between events.

Analytic tail: put `q=p_{k+1}`, `b_i=min{b>=2:p_i^b>=q}`, `j0=#{i<=k:2p_i<q}`.
If `a_i>=2b_i-1`, replace `n` by `n*q/p_i^b_i` without increasing n and with tau ratio `2(a_i-b_i+1)/(a_i+1)>=1`.
If `p_i*p_j>=q`, `a_i,a_j>=2` and `(a_i-1)(a_j-1)>=2`, replace n by `n*q/(p_i*p_j)`, with tau ratio `2a_i*a_j/((a_i+1)*(a_j+1))>=1`.
If neither applies for normalized n, either every a_i<=2, or every `j>j0` has `a_j=1` (else a tail exponent >=2 can pair with an exponent >=3, as `2*p_j>=q`). Hence all exchange-free n obey
`tau(n) <= B_k=max(3^k,2^(k-j0)*prod_{i<=j0}(2b_i-1))`.
If the first normalized k-layer integer `t_k` with tau>B_k is found, `N>=t_k => D_k(N)<=D_{k+1}(N)`.
For k=1, N>=8 suffices; k=2..24 witnesses were separately extracted by two full scans and checked strictly increasing.

NEW k=24, q=97:
`B24=max(282429536481,265295347200)=282429536481`.
Earliest normalized first-crossing `T24=15639824539936614813711403299961976428552041022592242982400000`,
`tau(T24)=282981703680>B24`.
Exponents on first 24 primes (2,...,89):
`[12,8,5,4,3,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1]`.
Previously conservative single-donor bound `V24=1129906182670184577950464891711508798496122706607156846913514012112200`; floor(V24/T24)=72,245,451. First-crossing minimality is for tau>B24, NOT for the earliest globally permanent nondecrease.

Finite complete enumeration cutoff `M=16943143251597999381520686908292141130931377774474929897600000 > T24`.
Two independently implemented C++ exact integer scans (direct sorted inverse thresholds vs per-layer min-heap merger) agree in EVERY pair-failure interval/count, first crossings, D values, and critical threshold: 204,426,817 normalized candidates including 1; 3,342,072 inverse-threshold records; 24,324 strict refresh events; max observed prime count 36; zero unimodality valleys for prefix through layer25.
Independent Python enumeration of all 13,836,456 normalized candidates <= critical boundary validates:
`W24=552185371819322819143107766767673444169856000`,
`(D24,D25)(W24-1)=(2906652672,2831155200)`,
`(D24,D25)(W24)=(2906652672,2906652672)`.
25-prime witness at W24 exponents: `[10,6,3,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]`.
All 24,324 strict refresh events independently re-factored/checked. Full integer enumeration covers N<=M, and exchange theorem covers N>=T24; the overlap is nonempty and full. W24 is consequently the earliest integer above which the entire prefix D0..D25 remains nondecreasing.

Machine artifacts in local handoff package: `k24_inverse_scan.cpp`, `k24_independent_heap_cross.cpp`, `k24_boundary_check.py`, `k24_event_verify.py`, `k24_crosscheck.py`, `k24_sharp_certificate.json`, `k24_frontier_events.tsv`, run logs and SHA256 manifest. These are NOT implied to be present in this repository by this note's publication; SOURCE_CODE_SYNC_DEBT if not separately published.

## Theorem B (exact algebra; finite-horizon BRC observer)

Let S be a fixed finite set of prime operations, H a positive integer, and future operations be at most L successive multiplications by primes in S or their legal exact divisions. Every word prefix observes (tau,omega, indicator(n<=H)) and legal/illegal status. Write n=r*prod_{p in S}p^{a_p}, with r coprime to S.
Within one FIXED base fiber (a, tau(r), omega(r)), the most economical further threshold coordinate is the single integer
`F^(L)_{H,S}(r;a)=max({0} union {prod_{p in S}p^{b_p}: b>=0, sum|b_p-a_p|<=L, r*prod p^{b_p}<=H})`.
It is both sufficient and **relatively coarsest** for all words of length <=L.
Proof: reachable b are exactly the nonnegative Manhattan L-ball around a. Every reachable threshold bit equals `[prod(p^b)<=F^(L)]`; all other observations and legalities are determined by the common fixed base fiber. If F differs, the larger F itself is a reachable witness distinguishing the two states.

This is NOT asserted as an unconditional global coarsest state when a, tau(r) or omega(r) vary.

Strict horizon hierarchy for every L>=1: S={2}, a=0, r=5, r'=7, H=5*2^L:
`F^(L-1)(5)=F^(L-1)(7)=2^(L-1)`; `F^(L)(5)=2^L` while `F^(L)(7)=2^(L-1)`.
Thus every L can carry new future information inaccessible at length L-1.

Mixed-operation witness already at length 2: H=1530, r1=101,r2=103, original operation prime2. Enlarging operations separately by prime3 or by prime5 gives identical word-<=2 observations, but simultaneous primes3&5 distinguish via 101*15=1515<=1530<1545=103*15.

Independent exact finite exhaustive checker: S∈{{2},{2,3},{2,3,5}}, thresholds 7,20,60,121,340,1000, n=1..120, horizon L up to 4,3,2 respectively; 8,640 parameter/state instances, 2,694 base fibers and 48,348 pair comparisons pass equality-of-future-tree iff equality-of-F. Tested strict L=1..12 and joint length2 witness. The implementation checks the theorem, not substitutes for its algebraic proof.
BRC exact positive-branch tensor counting `tau(n)=tau(r)*prod(a_p+1)` was actually applied (`REUSE_APPLIED`), not executed as a native BRC engine. P000 native X6 transfer remains unproved and unclaimed.

## Validation bounds / next work

Numerical theorem uses exact integer arithmetic, two full normalized scans, independent direct boundary, strict event factorization, and analytic exchange tail; it remains author-validated and requires independent review/formalization. The BRC horizon statement is an algebraic theorem for the declared observer, fixed base fiber and operation budget, not a universal P000 dynamics theorem.

NEXT: k=25/q=101; compute B25, a bounded first-crossing and D25/D26 boundary (or a precisely bounded partial theorem if a full scan becomes prohibitive). BRC: characterize absolute minimal length-L observer quotient when initial valuations a and cofactor tau/omega vary; obtain a compact jet/valuation representation with proven state-cost bounds. Publish/source-readback check of the full programs and proper research checkpoint remain separate tasks. Do not replay prior validated k<=24 work without an integrity reason.
