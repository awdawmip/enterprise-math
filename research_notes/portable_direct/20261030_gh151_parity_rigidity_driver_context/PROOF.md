# GH-151 centered reflection rigidity: exact polynomial proof and coefficient certificate

**2026-10-30 — portable author-context mathematical contribution.** Classification: UNREVIEWED / NOT_ADMITTED / NOT_NATIVE / REGISTER_PENDING. This is neither a canonical Source Result nor an independent native Driver Review. Reuse of shared prior GH-151 author sources is disclosed.

## Immutable input

Enterprise Math source main ea390dcadd5d3233200fad2aa0888d427f157db8, GH-151–152 report research_notes/portable_direct/20261030_hourly_d25_gh151_gh152_one_cm_anchor_picard_fuchs.md (Git Blob ae474e4b4af292c318e9dbcb81a504bee13b5085). Current P000 and six-axis worldview continue to apply, but these finite-field statements concern an external auxiliary arithmetic model, not native X6 dynamics.

## Theorem: centered reflection is forced, independently of the separately imported GH-131 lemma

For every prime p=8m+3>=11, put N=(p-1)/2=4m+1 and let

  H(B)=[X^N](X^2+X+B)^N
      = sum_{k=0}^{2m} N! / ((N-2k)! (k!)^2) * B^k  in F_p[B].

All factorial indices are less than p. The integer coefficients h_k satisfy

  (k+1)^2 h_{k+1}=(N-2k)(N-2k-1) h_k.

Reducing N=-1/2 modulo p proves the following identity of *polynomials*, including its leading term, whose residual coefficient vanishes because 8m+3=p:

  B(1-4B)H''+(1-8B)H'-(3/4)H=0.                    (1)

Set z=B-1/8 and T(z)=H(1/8+z)=sum_{j=0}^{2m} c_j z^j. Then (1) becomes

  (1/16-4z^2)T''-8zT'-(3/4)T=0.                   (2)

If the odd part of T were nonzero, let d be its largest odd exponent with coefficient c_d!=0. Necessarily 1<=d<=2m-1. Taking the degree-d coefficient of the *odd part* of (2), the c_(d+2) term vanishes by maximality, leaving

  -((4d+1)(4d+3)/4)*c_d=0 in F_p.

Yet 0<4d+1<4d+3<=8m-1=p-4<p, a contradiction. Therefore T is even, yielding the exact polynomial identity

  H(1/4-B)=H(B).                                  (3)

This derives the reflection used in GH-151 directly from its own Hasse polynomial and Picard–Fuchs ODE: **a separate GH-131 reflection premise is unnecessary for that step**. Neither GH-151's trace-family identity, marked-moment relation, nor source-original CM/Frobenius obligations are thereby independently proved.

The centered even-coefficient recurrence uniquely determines T from c_0, while the leading original h_(2m) is nonzero modulo p. Consequently c_0=H(1/8) is also nonzero for every stated prime. This is a polynomial nonvanishing result; it does not amount to a separate integer CM evaluation.

## Alternative finite-binomial coefficient certificate

Take rho^2=2 in F_(p^2), B=1/8+rho*v, W=v^2, and H(B)=g_0 Phi(W), where Phi(W)=sum_{k=0}^m u_k W^k and u_0=1. The recurrence from (2) is

  (k+1)(2k+1)u_(k+1)=4(8k+1)(8k+3)u_k.

Equivalently in F_p,

  u_k=128^k (1/8)_k (3/8)_k / ((1/2)_k k!).

Since 1/8=-(3m+1), 3/8=-m and 1/2=-(4m+1) modulo p, for every 0<=k<=m,

  u_k * C(4m+1,k) = (-128)^k C(3m+1,k) C(m,k) mod p. (4)

The denominators are p-units. This is a second exact coefficient representation, not an independent elliptic-curve sample or a stronger admitted theorem.

## Finite exact crosscheck, reproducibility and boundaries

The accompanying Python standard-library checker constructs H from its **direct integer binomial coefficients** rather than the recurrence, expands at B=1/8, checks all centered coefficients, parity, the ODE, the normalized recurrence, and (4) at primes 11,19,43,59,67,83,107,3347. A single independent prime-field elliptic-curve point count at p=3347 yields a_p(E_(1/8))=-114. With W_0=1/144=860 in F_3347, direct expansion returns g_0=3233, G(W_0)=783, G'(W_0)=2824, J(W_0)=588, J'(W_0)=997 and the signed rho coefficient 362. Exactly 936 centered coefficients, 837 at p=3347, passed in the recorded run. Finite tests are not the universal proof: the highest-odd-coefficient argument is the proof.

This does not claim native H0/B0, the source-original p=373 benchmark, R_3347(9), independent Reviewer/Driver status, F7 review completion, or a change to P000. The old F7 control request drv-ro-taskscan-20261027-1656-260b was most recently WAITING_RESOURCE/CANONICAL_RUNNER_TOTAL_TIMEOUT. The Sites gateway remains read-only without current Driver DA. No Review, Reference, Synthesis, Follow-up, immutable Task publication, or Source CLAIM is attempted here.

## Exact handoff for an independent successor

Read the current global-knowledge bootstrap and operating manual, project docs/AUTONOMOUS_RESEARCH_OPERATIONS.zh-CN.md, current P000/ACTIVE constraints, and the GH-151 frozen author source above. Verify (1)–(4) against complete coefficient identities and the actual checker. Treat this file as shared-context scientific material only; do not assert CLEAN_INDEPENDENT_CONTEXT merely from a new session. Reconcile the original unfinished Source request without issuing a duplicate ID. Obtain and verify your own active Source Driver authority and contribution independence before an exact-set F7 native review. For GH-151, separately review GH-147 trace/marked-moment dependencies and source-original arithmetic; do not promote auxiliary finite-field results to native X6. Existing authors, accepted review history, task scheduling, and P000 remain untouched.
