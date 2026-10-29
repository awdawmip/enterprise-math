# D25 / SECOND-DIGIT-LIFT — exact CM(-24) Hasse p² rank-line certificate

**2026-10-29 · AUTHOR-SIDE / EXECUTED FINITE CERTIFICATE / UNREVIEWED / NOT_ADMITTED / NATIVE_H0_B0_NOT_EXECUTED.**

Mother: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT. Publication: TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin: c47e13e4aba0e006366f989d6334d443f6333ae3 (unchanged). Research conversation: chatgpt-research-onhour-enterprise-math-20260923 (never the maintenance conversation). This note is an author-side continuation of the exact 3-port p² / Hasse falsifier at 919f879a4b29e686117930e148bbd19b722317f5, not a formal Source Result or native experiment.

## Exact model and new finite finding

For an odd prime p>3 let k=(p−1)/2, e=floor(k/2). Work in the **two-component** ring

\[
R_{p^2}=(\mathbf Z/p^2\mathbf Z)[t]/(36t^2-36t+1),\qquad s=(1-t)/4.
\]

Use the genuine but **external** elliptic Hasse coefficient

\[
H_p(t)=\sum_{j=0}^{e}\binom{k}{2j}\binom{2j}{j}s^j=A_p+B_pt.
\]

For CM-inert classes p≡13,17,19,23 mod24, the already established first-digit Hasse criterion gives p|A_p and p|B_p. Hence define α_p=(A_p/p) mod p, β_p=(B_p/p) mod p from canonical representatives A_p,B_p∈[0,p²).

**Observed finite rank-line phenomenon:** among all 616 primes p<10000 in these four classes, *each of the 157 primes p≡13 mod24* satisfies

\[
\boxed{\beta_p\equiv2\alpha_p\pmod p,\quad
H_p(t)\in p\,\mathbf F_p(1+2t)\subset R_{p^2}.}
\]

In the other inert classes there were **zero** instances of this line condition. The statement for all p≡13 mod24 is a **new conjectural proof target**; the assertions above cover only the stated finite domain. In particular the prior individual examples p=13 and 373 are not recycled as a universal proof.

## Proven integer/Lucas reduction (all p>3)

For the linear observer ℓ(A+Bt)=B−2A, the defining ring identity implies s²=s/4−1/576. Put v_j=576^j ℓ(s^j). Then, as exact integers,

\[
\boxed{v_0=-2,\quad v_1=-432,\quad v_{j+2}=144v_{j+1}-576v_j.}
\]

Consequently, **without any conjectural step**, for every prime p>3,

\[
\boxed{\ell(H_p)=
 \sum_{j=0}^{e}\binom{k}{2j}\binom{2j}{j}v_j\,576^{-j}
 \pmod{p^2}.}
\]

All denominators are p-units. For CM-inert p, β_p−2α_p=0 modp is equivalent to this **single integer-first Lucas/binomial sum vanishing mod p²**. This is an exact algebraic reduction of the candidate to one finite character-sum problem; it does not assert that the sum vanishes for all primes.

## Independently executed finite evidence

Checker: research_notes/portable_direct/d25_cm24_hasse_defect_rankline_guard_20261029.py. Standard-library Python; deterministic complete sieve for primes p<10000; direct integral Hasse coefficient evaluated modulo p² in the unreduced two-component ring; separately computes original companion K_b(1/9) and jet D=θK_b via the original (1/8,3/8) coefficient recurrence, with b the **actual second numerator-hit index**. Representative cases are cross-checked by independent factorial/binomial sums and the integer Lucas formula. No floating point, no native H0/B0 surrogate.

| p mod24 | exact count | β−2α=0 modp | original K_b=0 modp² |
|---|---:|---:|---:|
| 13 | 157 | 157 | 157 |
| 17 | 152 | 0 | 0 |
| 19 | 155 | 0 | 0 |
| 23 | 152 | 0 | 152 |

The p≡23 mod24 branch is the **crucial signed/branch negative control**: its original companion has the same observed p² zero, but the external Hasse rank-line is absent. The line condition is not equivalent to Root2 across all inert primes.

Examples: p=13 gives (α,β,D modp)=(2,4,11); p=373 gives (14,28,5) and H_373=373(14+28t) mod 139129; p=23 gives (21,9,8) with β−2α=13 mod23 despite K_b≡0 mod529. A strict **composite counterexample** eliminates a fake residue-only extension: for N=85≡13 mod24 and modulus N²=7225, the same integral Hasse extraction gives (A,B)=(3451,3281) and B−2A=3604≠0 mod7225.

Executed output terminates with PASS_FINITE_CM24_HASSE_P2_LINE_616_PRIMES_P_LT_10000. No all-prime statement follows from the finite run. The new research task is to prove or falsify the Lucas congruence for all p≡13 mod24 using prime-specific arithmetic, then obtain a **genuine finite p² quadratic transport** relating the external Hasse defect to the original K_b source ports. Neither the line condition nor the external Hasse coefficient alone proves Root2.

## BRC / native / recovery frontier

BRC COMPOSE_APPLIED: preserve (p,k,e,A,B,α,β,s,ℓ,companion K_b,derivative D,valuation,source,operation order). Applying ℓ is a declared *derived observer*, not safe collapse of the original t-branches for later Frobenius/differentiation. P000, ACTIVE Heartbeat World X6 plus separately typed time and the frozen scientific Source pin remain intact.

The unchanged **highest-priority native experiment** is Issue #1559: same-original-class p=373 H0/B0 divided-power [X]U mod139129, genuine module rank, semilinear Frobenius direction/η, full odd signed Green/Hesse, κ and Δ_p−R_p, reproducible native input/outputs and independent validation. This author-side external-Hasse computation did not execute the native object.

2026-10-29 Site read: research_authority_granted=false, write_relay_enabled=false, executor_binding_configured=false, active quota 5/5; client checkpoint_list returns ACCESS_DENIED and no callable recovery_status was exposed. Exact own Source session, winning claim/run and original target_request_id remain unverified. Do not assume an authority or send a new mutation to substitute for an unknown old request. Author-side repository artifacts remain UNREVIEWED / NOT_ADMITTED; formal Source registration/checkpoint is pending a genuine authorized path.

**Do not repeat:** earlier Clausen p³ proofs, complete three-port p² identity, 373 scalar certificates or first-digit CM proof. **Next executable mathematical unit:** attack the one-scalar Lucas congruence for the 13 branch and its source-preserving p² CM transform. **Next native action:** actual owner of #1559 runs the unchanged fixed H0/B0 benchmark; no owner is claimed here.

External references: project previous three-port exact proof at 919f879a4b29e686117930e148bbd19b722317f5; existing support Issue https://github.com/awdawmip/enterprise-math/issues/1559. Source pin above is a scientific input pin, not the mutable control head.
