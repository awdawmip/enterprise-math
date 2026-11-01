# D25 — Exact weighted 2304 resonance and the 216/2304 carry mismatch

2026-11-02 (+08:00). TASK_RESEARCH portable author-side mathematics; AUTHOR-DERIVED / EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING.
Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7; frozen scientific source pin c47e13e4aba0e006366f989d6334d443f6333ae3.
Research logical lane chatgpt-research-hourly-enterprise-math-20260923; maintenance lane chatgpt-hourly-enterprise-math-20260921 is separate.

## Theorem: exact p-adic resonance and normalized unit

Let p>=5 be prime and T_p = sum_{k=0}^{p-1} R_{p,k} with
    R_{p,k} = (8k+1)(4k)! / ((k!)^4 * 2304^k).
Let m be the unique element in {1,3,5,7} with m*p ≡ 1 (mod 8), let
    k_*=(m*p-1)/8, r=(m-1)/2, H=(p-1)/2, e=v_p(m).
Then 8k_*+1=m*p, 4k_*=r*p+H, 0<=k_*<p. Consequently
    v_p(R_{p,k_*}) = r+1+e,                                           (1)
    R_{p,k_*}/p^(r+1+e)
       ≡ (m/p^e)*(-1)^r*r!*H! / ((k_*!)^4 * 2304^k_*) (mod p) !=0.    (2)
All denominators in (2) are units modulo p.

Proof. Since 4k_*=rp+H with 0<=r<=3<p and H<p, its factorial has exactly r p-factors, while k_*! and 2304^k_* are p-units. The weight m*p has valuation 1+e. For the normalized factorial, the r complete nonmultiple residue blocks give (-1)^r by Wilson, the r multiples of p give r!, and the final incomplete block gives H!. Thus (rp+H)!/p^r ≡ (-1)^r*r!*H! (mod p). The displayed residue is nonzero. QED.

For p>=11, e=0: the class p (mod 8) =1,3,5,7 gives resonance valuation 1,2,3,4 respectively. Small boundary cases are p=5: m=5, e=1, valuation 4 and p=7: m=7, e=1, valuation 5.

## Target-class corollary and exact source port

Guo and Zudilin, A q-microscope for supercongruences, Adv. Math. 346 (2019) 329-358, arXiv:1803.01830, proved T_p ≡ ((-3)/p)*p (mod p^3) for all p>3. For the frozen target classes p≡13,19 (mod24), (-3/p)=+1. Let R_p=R_{p,k_*}. Then
    p≡13 (mod24): k_*=(5p-1)/8, v_p(R_p)=3;
                    T_p-R_p ≡ p (mod p^3).
    p≡19 (mod24): k_*=(3p-1)/8, v_p(R_p)=2;
                    T_p-R_p ≡ p-p^2*rho_p (mod p^3),
       rho_p = -3 * ((p-1)/2)! / (((3p-1)/8)!^4 * 2304^((3p-1)/8))
               (mod p) != 0.
The nonzero second-digit source rho_p arises from removing exactly this labeled resonant term in the p19 class. It is distinct from the earlier Clausen high-degree cutoff K_p=F_<p^2-V_<p, which is a different source object.

## Comparison to original 216 weighted resonance

Define S_p=sum_{k=0}^{p-1}(6k+1)*binom(2k,k)^2*binom(3k,k)/216^k.
For p=6q+1, at k=q=(p-1)/6, the weight equals p and every factorial argument in the unweighted binomials is below p. Thus the 216 weighted resonant term has valuation exactly 1 for both target classes. Its counterpart labeled by 8k+1≡0 (mod p) in T_p has valuation 3 (p13) or 2 (p19). Any proposed **termwise resonance-label- and valuation-preserving** transfer is obstructed; a full p^3 relation can instead involve other terms and nontrivial signed cancellation. This is a scoped obstruction, not an impossibility claim about the original 216/2304 congruence.

BRC COMPOSE_APPLIED: input population is the complete labeled rational summand sequence (source-series tag, k, coefficient, denominator, weight, p-valuation, unit), observer T_p modulo p^3, future operation deletion of the identified weight-resonance port. The p13/p19 fiber contrast shows total-value-only compression is insufficient to reconstruct that operation. These classical auxiliary calculations make no native X6 dynamical assertion.

## Exact execution and frontier

Script d25_weighted_resonance_20261102.py uses independent (a) Wilson factorial-unit reduction and (b) finite-ring binomial coefficient recurrence mod p^7. All 166 primes 5<=p<=997 passed exact valuation, nonzero unit and published T_p residue, with 13/19 resonance-deletion checks. Counts by m: {1:37,3:43,5:43,7:43}. Selected tuples (p,m,k_*,valuation,unit mod p):
(13,5,8,3,8); (19,3,7,2,10); (37,5,23,3,15); (43,3,16,2,28); (61,5,38,3,4); (67,3,25,2,44); (163,3,61,2,107); (373,5,233,3,331).
The universal result is proved by the factorial argument; finite checks corroborate implementation. The general bridge S_p-T_p≡0 mod p^3 for p≡13,19 mod24 remains OPEN, despite finite numerical checks in prior notes.

Next mathematical unit: seek an actual mod p^3 trace/summation identity for the full signed 216/2304 term ensembles retaining the p19 p^2*rho_p term, and independently retain earlier p13/p19 Clausen cutoff. Check proposed source maps on p13 and p19 before generalization. Prior CM selector/Green/Hadamard/Clausen proof units need not be rerun. Native p373 H0/B0 remains separately pending.

2026-11-02 control: authenticated gateway 0.6.11 research_authority_granted=false, executor_binding_configured=false, CODE_REVIEW_REQUIRED / UPSTREAM_CODE_REVIEW_REQUIRED. Own historical recovery bridge #6637 request hourly-recovery-20261101T1518p0800-r11 succeeded read-only, earlier own service session MCP-06f7ad61a8d841d9ba1ba1ef4d088d94 with no pending/run/claim/unpublished upload in that dated snapshot; source_authority_verified=false. Own exact continuation bridge #6638 request hourly-d25-continuation-20261101T1530p0800-r11 definitively FAILED, code-review gate (five Python paths listed in original receipt), do not replay. Support owner issue #1558. Neutral preserved staging archives are not source research checkpoint. No current CLAIM, authorized OPEN, native checkpoint, Result or independent admission is claimed. P000, ACTIVE Heartbeat World X6, input source pin and scheduler/notification settings unchanged.

This project-repository artifact is **portable evidence preservation only**, awaiting formal Research activity/source checkpoint and independent review.