# D25 on-hour: resolve the 2304 high-tail zero by published full/half theorem

Date: 2026-11-03. Lane: TASK_RESEARCH; logical conversation chatgpt-research-onhour-enterprise-math-20260923. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; unchanged frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3. Author-side source-verification plus exact mathematical corollary, UNREVIEWED/NOT_ADMITTED/REGISTER_PENDING; **not** native Source checkpoint or claim.

## Highest consumed frontier

Prior immutable D25 two-tail note: enterprise-math@6b7130b6b600cc9bcfe96a7a95d527733fc9199b, path research_notes/portable_direct/20261103_onhour_d25_216_2304_two_tail_hypergeometric_bridge.md. It proves for every prime p>=5, writing h=(p-1)/2, v=floor(3p/4)-h and

- c_k=(4k)!/((k!)^4 2304^k);
- S_N=sum_{k=0}^N (8k+1)c_k;
- Q4_p(x)=sum_{t=0}^{v-1} [(1)_t(3/4)_t(5/4)_t]/[(3/2)_t^3 9^t] x^t in F_p[x];
- theta=x d/dx,

the congruence S_(p-1)-S_h = (p^2/36)[(5+8theta)Q4_p](1) (mod p^3). This was previously an **all-prime proven bridge plus finite-only zero conjecture**.

## External primary-source theorem and exact source match

Victor J. W. Guo and Wadim Zudilin, *A q-microscope for supercongruences*, Advances in Mathematics 346 (2019), 329-358, DOI 10.1016/j.aim.2019.02.008, arXiv:1803.01830v6, https://math.ecnu.edu.cn/~jwguo/maths/q-congruence03q.pdf.

In the published author's manuscript, page 1 formula (2) and page 2 formula (3), explicitly proved as q->1 specializations of Theorem 1.1 formulas (5),(6) on page 3, give **both** congruences for *every* prime p>3:

S_(p-1) = p (-3/p) (mod p^3), AND S_((p-1)/2) = p (-3/p) (mod p^3),

where their summand is (8k+1) binom(4k,2k) binom(2k,k)^2 / (2^(8k)3^(2k)). The denominator equals 2304^k, and binom(4k,2k) binom(2k,k)^2=(4k)!/(k!)^4. Both the weight and the **inclusive endpoints** exactly match the prior D25 c_k/S_N. Thus the prior prospective 2304 half/full congruence is already a **proved external result**, and should be consumed as such. This is source reconciliation, not a claim of original proof of the Guo-Zudilin theorem.

## Exact all-prime finite-Q4 corollary (proof)

For all primes p>=5, subtract the two cited published congruences to obtain S_(p-1)-S_h=0 (mod p^3). Substitute the already-proved D25 high-tail identity. Since 36 is a unit in Z_(p), multiplication by its inverse followed by cancellation of p^2 yields the **proved** finite-field identity

**[(5+8theta)Q4_p](1)=0 in F_p, for every prime p>=5.**

Equivalently, Q4_p'(1)=-(5/8)Q4_p(1) in F_p. For every affine observer a+b theta (a,b in F_p), [(a+b theta)Q4_p](1)=(a-5b/8)Q4_p(1). This is a two-observer linear collapse using the retained signed derivative: a condition on a specific observer space, not termwise zero.

The p=5 endpoint is included: v=1, Q4=1 and weighted value 5=0 in F_5. For p=373, exact integer modular computation gives Q4(1)=30 and theta Q4(1)=261 in F_373; 5*30+8*261=2238=6*373. Both constituents are nonzero, so the zero is from signed cancellation.

## Strict simplification of the original 216–2304 bridge

Keep the already-proved other D25 high-tail formula, with u=floor(2p/3)-h,
Q3_p(x)=sum_{t=0}^{u-1} [(1)_t(5/6)_t(7/6)_t]/[(3/2)_t^3 2^t] x^t,
chi6=(6/p), and b_k=binom(2k,k)^2 binom(3k,k)/216^k, W_N=sum_{k=0}^N(6k+1)b_k.

The prior signed two-tail bridge and the newly discharged 2304 identity combine to the exact all-prime congruence:

**W_(p-1)-S_(p-1) = W_h-S_h + p^2*(chi6/9)*[(4+6theta)Q3_p](1) (mod p^3).**

For p=13 or 19 (mod 24), Guo-Zudilin give S_(p-1)=S_h=p (mod p^3), so D25's auxiliary original-216 target W_(p-1)=p (mod p^3) is strictly equivalent to the **single unresolved** low/high 216 certificate

**(W_h-p)/p^2 + (chi6/9)*[(4+6theta)Q3_p](1) = 0 (mod p).**

The integer division is valid using already accepted first-digit W_(p-1)=p (mod p^2), plus the proven 216 high-tail order >=p^2, hence W_h=p (mod p^2). This is a precise equivalence for the 216 auxiliary target, not automatically an admitted proof of the frozen D24 Delta_p-R_p interface; that interface still requires exact scalar-observer binding.

The 2304 high-tail zero is **not** an open WZ proof task any longer. Do not spend research cycles re-proving it; the paper's proof and the exact source match are sufficient. Continue from the 216 half-carry/Q3 signed cancellation and map to Delta_p-R_p with frozen G_p,h,Phi_xx observer.

## Exact execution and source interpretation

A separate standard-library Python checker was actually run for all 76 primes 5<=p<=400, computing original full/half 2304 binomial sums modulo p^3 and independent finite hypergeometric Q4 and thetaQ4 modulo p. It verified the two published predictions, the previous D25 tail formula and zero observer; all assertions passed. This finite check is a regression, not the theorem proof. Some records: p=13 (Q,thetaQ)=(5,5), p=19 (10,8), p=373 (30,261), with all weighted observers zero.

BRC source-preserving operation: COMPOSE_APPLIED, external Guo-Zudilin double truncation theorem + prior original-integer D25 strip theorem -> signed two-observer elimination. Source origin and coefficient weights retained. No change to P000, no native X6 transfer or H0/B0 Frobenius execution.

## Exact continuation / native status

Mother task: D24 second digit LIFT, Delta_p=(G_p*h-1)/p = R_p mod p for p=13,19 (mod24), after accepted first digit. Unfinished: prove the above 216 low/high certificate *and* verify its precise identification with frozen Delta_p-R_p; alternatively direct proof/counterexample of LIFT. Do not redo D24 UR, 216 Q3 high strip, 2304 two-tail zero or finite tests. Highest author-side frontier: this note and prior commit 6b7130b. Next exact action: consume source-pinned accepted scalar interface and construct an explicit map from the 216 low/high observer to Delta_p-R_p preserving Phi_xx, derivative and p-adic second digit; test p=13,19,373 before claiming equivalence. Then seek a terminating parameter/WZ certificate for the single remaining 216 cancellation.

Native 373 H0/B0 divided-power [X]U mod 139129 benchmark remains NOT_EXECUTED and tracked in issue #1559, no owner assigned at read time. Sites gateway 2026-11-03T07:03Z reported research_authority_granted=false, write_relay_enabled=false. Original dispatch request research-onhour-20261031-0205-dispatch-r15 on kimi-query-bridge issue #6633 has COMPLETE outer receipt but inner FAILED/UPSTREAM_CODE_REVIEW_REQUIRED; no re-dispatch. No own native session, claim, run, Source checkpoint, Result/admission. Source-authority configuration needs a separate approved Site-bound backend client and user-entered credentials; control support #1558 is already open. Research activity remains REGISTER_PENDING/SYNC_DEBT.
