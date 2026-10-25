# D25/LIFT — all-order cutoff-moment closure at the original Clausen source

Date: 2026-10-25. TASK_RESEARCH portable author-side result. Research logical lane: chatgpt-research-hourly-enterprise-math-20260923, distinct from CONTROL_PLANE_MAINTENANCE. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 is unchanged.

Status: AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY. Not a native Source CLAIM, run/checkpoint, independent review, original CM/divided-power experiment, or LIFT/JT2 proof.

## Exact source and new question

Consume, without re-crediting, the original scalar series and the proved second-moment boundary certificate in research_notes/portable_direct/20261025_hourly_d25_jacobi_second_jet_cutoff.md (Git source 1bfe9166160a940e6e30c8ad652175191dd8357e). That result proved 18 M_2 - 9 M_1 - M_0 = -p^2 (mod p^3). The previously unanswered question is whether higher polynomial-in-rank moments give independent source observations at the same original cutoff, evaluation point and precision.

Let p=6m+1>=7 be prime. All rational numbers are considered first in Q and then in Z_(p) where their denominators are p-units. Put

    b_n=(1/6)_n (1/3)_n/(n!)^2,   r_n=b_n/2^n   (0<=n<p),
    f_p(z)=SUM_(n=0)^(p-1) b_n z^n,
    M_s=SUM_(n=0)^(p-1) n^s r_n   (s>=0);
    g=M_0,  d=M_1,  E_p=18 M_2-9 M_1-g.

The population is the original ordered rank set n=0,...,p-1; amplitude r_n is signed/rational and provenance-bound, not replaced by a support set or positive total. The declared observer family consists of polynomial rank moments evaluated at z=1/2, with arithmetic modulo p^3. The allowed future operation here is further polynomial rank weighting and Z_(p)-linear combination; no division by p or nonlinear Frobenius extraction is included.

## Theorem A — exact all-order finite-cutoff moment recurrence over Q

Set

    K_p=(p-5/6)(p-2/3)b_(p-1).

For every nonnegative integer s (with no bound s<p), the actual moments satisfy the exact rational identity

    2 M_(s+2)
      - SUM_(j=0)^s binom(s,j)
          [ M_(j+2) + (1/2) M_(j+1) + (1/18) M_j ]
      = (E_p/18) p^s.                                      (A)

Moreover

    E_p=-36 K_p/2^p
       =-18(p-5/6)(p-2/3)b_(p-1)/2^(p-1).               (B)

The coefficient of M_(s+2) on the left of (A), after moving the j=s summand, is 1. Consequently g,d and the one exact endpoint scalar E_p determine every M_s by a triangular rational recurrence, even before p-adic reduction.

Proof. The exact hypergeometric recurrence is

    (n+1)^2 b_(n+1)=(n+1/6)(n+1/3)b_n.

For the Euler operator theta=z*d/dz, cancelling every coefficient below rank p yields the source-bound differential identity

    [theta^2-z(theta+1/6)(theta+1/3)]f_p(z)
       =-K_p z^p.                                           (C)

The right-hand side is solely the deliberately omitted rank-p coefficient of the fixed degree-(p-1) polynomial; it is NOT an additional series input. Substitute z=e^t/2 and G(t)=f_p(e^t/2)=SUM r_n e^(nt). Then G^(s)(0)=M_s and (C) becomes exactly

    (2-e^t)G''-e^t[(1/2)G'+(1/18)G]
       =-2 K_p 2^(-p)e^(pt).                               (D)

At t=0 the left side is E_p/18, which proves (B). Differentiating (D) s times at t=0 by Leibniz's formula gives (A) with right side E_p p^s/18. This is an identity in Q for every s; although the notation uses exponential generating series, the final recurrence contains only integer binomial coefficients and denominators 2 and 18. QED.

For reference, the first exact higher identities are

    36 M_3=5g+47d+(3+2p)E_p,
    648 M_4=335g+3177d+(209+90p+36p^2)E_p.             (E)

## Theorem B — complete modular closure and a precise no-new-observer result

For every prime p=6m+1 and every s>=0, modulo p^3 all rank moments M_s are determined by the two original coordinates g,d and the known endpoint p^2, with universal coefficients in Z[1/6], independent of p.

Explicitly start U_0=g, U_1=d, and recursively for s>=0 define in Z/p^3:

    U_(s+2) =
       (1/2)U_(s+1)+(1/18)U_s
       + SUM_(j=0)^(s-1) binom(s,j)
           [U_(j+2)+(1/2)U_(j+1)+(1/18)U_j]
       -(p^2/18) 1_(s=0).                               (F)

Then M_s=U_s (mod p^3) for every s. In particular,

    36 M_3 = 5g+47d-3p^2           (mod p^3),
    648 M_4 = 335g+3177d-209p^2  (mod p^3).             (G)

Proof. In the previous source note, the source-extracted endpoint has v_p(K_p)=2 and E_p=-p^2 (mod p^3); that conclusion follows independently from (B), two distinct p factors in b_(p-1), Wilson complements and 2^(p-1)=1 (mod p). Apply (A). For s=0, E_p p^s/18=-p^2/18 modulo p^3. For every s>=1, v_p(E_p p^s)>=3, so the source boundary term vanishes modulo p^3. The denominators 2 and 18 are p-units for p>=7. Solve for the coefficient-one M_(s+2) and induct on s; the resulting recurrence is (F). Substitution in the exact formulas (E) proves (G). No finite-prime interpolation is used. QED.

Corollary (source-observer factorization, with declared scope). For every polynomial P(n) over Z_(p), the moment SUM_(n=0)^(p-1) P(n)r_n modulo p^3 factors through (g,d,p^2) and introduces no additional freely varying source coordinate within this **fixed hypergeometric family, cutoff and evaluation point**. This DOES NOT assert such factorization for parameter x-derivatives, different evaluation points, full branch-resolved states, operations involving 1/p, nonlinear CM/Frobenius normalization or hidden original-class data. In particular this theorem does not prove Delta_p=R_ref,p or reconstruct H_0/B_0. Higher fixed-point rank moments alone cannot supply the missing independent source port.

## Author checks and exact certificates

Companion executable: research_notes/portable_direct/20261025_hourly_d25_original_moment_hierarchy_check.py. It generates r_n directly from the original 2F1 rational ratio, accumulates M_0..M_9 modulo p^3, independently reconstructs them from (F), checks the two new explicit identities (G), and checks E_p=-p^2. All 94 qualifying primes p<=1199 and the two additional primes 1327 and 19963 were checked (96 primes total), including p=373. For p=7,13,19 it separately constructs the exact rational moments and verifies (A)/(E) coefficient-for-coefficient through s=5.

Selected p=373, modulus 51,895,117: (g,d,M_2,M_3,M_4)=(24,495,656;45,882,278;4,112,845;47,435,602;49,769,930) and E_p=51,755,988=-373^2 (mod 373^3). For p=13, modulus 2,197: (g,d,M_2,M_3,M_4)=(988;423;257;2018;28), E_p=2028=-169 (mod 2197).

The computation is integer modular/rational author crosscheck, not original CM or native BRC execution. All-prime validity comes from (C)-(F), not from the finite checks.

## Exact frontier, limits, next unit

Consumed, not re-proved: the initial 2F1-to-Clausen identity, the p^3 cutoff corner, the p^4 reflected corner, and the earlier single second-moment endpoint anomaly. The new unit is **all-order** closure and its strictly scoped no-new-observer corollary.

The parent D25/LIFT/JT2 remains OPEN. Next discriminating mathematical action: search for a source-observer genuinely independent of (g,d) at this cutoff/precision, particularly a parameter jet with its authentic source map to (G_p h-1)/p or a same-original-class divided-power Frobenius normalization. Establish an exact source-preserving map to Delta_p-R_ref,p rather than expanding more rank moments. Exact native H_0/B_0, [X]U modulo p^2, Frobenius direction/rank/normalization and the original kappa correspondence remain missing, and the native CM experiment is NOT_RUN.

Control continuation is separately blocked, last observed: verified old persisted_checkpoint but successor last CLAIM epoch differs from the checkpoint capture CLAIM. The previous definite CHAT_CHECKPOINT_PREDECESSOR_MISMATCH and TYPED_CONTINUATION_REQUIRED_FOR_PREDECESSOR errors are not replayed. An attempted current read through the read-only Gateway returned CONTROL_QUOTA. No native CLAIM/OPEN/checkpoint or new service identity is asserted. Existing authentic requests and the real maintenance support owner remain tracked in enterprise-math issue #1558. Scientific Source pin above and all contributor history are preserved. This portable author-side artifact is NOT_ADMITTED pending legitimate native Source entry and independent review.
