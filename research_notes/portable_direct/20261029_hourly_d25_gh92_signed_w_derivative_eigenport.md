# D25/LIFT GH-92 — exact finite-source derivative and signed target eigenport

2026-10-29 / Research logical lane chatgpt-research-hourly-enterprise-math-20260923. AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. Mother ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION and D25/LIFT/JT2 OPEN; Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT / publication TP2-B6F4FC938FF94941C1B7. Frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged; current portable note grants no native CLAIM, checkpoint or mathematical acceptance.

## GH-92A — complete global differential-source identity

Let p=4d+3>=7 be prime, work in F_p[z] with theta=z*d/dz. Keep original S=sum c_i z^i and reflected U=sum h_j z^j as distinct GH-84/GH-90 input sources. Define original target T=(8theta+1)S, reflected obstruction H=(8theta+5)U, J=theta H, signed ordered concomitant B=B(S,U), its new derived observer V=B(S,theta U) and W=64V+40B (GH-91).

GH-84 proves theta B=(c_d/8) z^(d+1)U. GH-90 proves theta V=(c_d/8) z^(d+1)theta U+zS(theta+3/4)^3U. The exact linear combination 64theta V+40theta B gives the **complete polynomial identity**:

    theta W=c_d z^(d+1)H+64zS(theta+3/4)^3U.               (92.1)

This retains both the genuine finite terminal forcing and the separately labeled reflected source term; the derivation uses neither CM nor the still-open original special-value claim.

## GH-92B — pointwise reflected-root differential/eigenvalue certificate

At the ordinary target z=9 suppose H(9)=0 (GH-83's separately author-derived, currently unreviewed CM-dependent assertion). Then theta U(9)=-5U(9)/8 and theta²U(9)=J(9)/8+25U(9)/64. The exact reflected equation

    L_+ U=(1-z)theta³U+(3-9z)theta²U/4
          +(2-27z)theta U/16-27zU/64=0

gives, by substitution with no division by U,

    [(theta+3/4)^3U](9)=-(6J(9)+U(9))/256.                  (92.2)

Equation (92.1) now becomes

    (theta W)(9)=-(9/4)S(9)[6J(9)+U(9)].                    (92.3)

The complete GH-91 signed target identity at the same fiber is

    W(9)=8J(9)T(9)+3[8J(9)+U(9)]S(9).

Multiply (92.3) by 8J+U, multiply this last identity by 3(6J+U)/4, and add to cancel S without dividing by ANY source or jet. This yields the exact **signed target eigenport**:

    [8J(9)+U(9)](theta W)(9)
      +(3/4)[6J(9)+U(9)]W(9)
       =6J(9)[6J(9)+U(9)]T(9).                            (92.4)

GH-91 established J(9)!=0 on every H(9)=0 fiber. Also 6J+U is a unit: if U=0 then 6J!=0; otherwise GH-87 gives J=-U/32, so 6J+U=13U/16!=0, since p=4d+3 cannot equal 13. Hence

    T(9)=0 <==> (8J+U)theta W+(3/4)(6J+U)W=0 at z=9.  (92.5)

On the nonzero-U fiber (J=-U/32), this specializes to

    [(theta+13/16)W](9)=-(13/64)U(9)T(9).                 (92.6)

On the U-double-root fiber (J=8theta²U), it specializes to

    [(theta+9/16)W](9)=(9/2)J(9)T(9).                    (92.7)

The two weights 13/16 and 9/16 are *pointwise target-fiber derivative multipliers*, not asserted global eigenvalues or completed CM/Frobenius arithmetic. In particular the left side of (92.5) still needs an independent all-prime CM, Jacobi or finite WZ vanishing argument before GH-3 can close.

## Author evidence, BRC, continuation

Actually executed Python standard-library integer modular checker verified the FULL polynomial source derivative (92.1) for all 70 primes p<800 with p=3 mod4. The same checker independently evaluated B,V via original/reflected signed jets, source (theta+3/4)^3U and all target equations (92.2)-(92.7) for 618 primes p<10000, split 311 U(9)!=0 / 307 U(9)=0. All PASS. A separate executed SymPy symbolic substitution checked the exact algebra of (92.1), (92.2), (92.4). These are author checks, not independent review, Source admission, a formal GH-3 theorem or native p=373 H0/B0 experiment. Reproducibility package includes full finite modular program, logs and SHA256 manifest.

BRC COMPOSE_APPLIED: typed ordered population (p,z,i,j,original/reflected source labels), signed first derivatives of W and downstream target T; both terminal forcing and observer scale retained. Finite-field algebra is an auxiliary external chart and claims no native Heartbeat X6 or three-dimensional-slice transfer. P000 ACTIVE, source pins and proof status remain unchanged.

Next precise scientific action: obtain independent CM/Jacobi/WZ evidence that the left side of (92.5) vanishes at z=9 (or evaluate W(9) directly from GH-91's two finite-source sums). Preserve GH-83 first Laurent pole B_0L, GH-20/21, W/S, Hasse ports, R23/R36 and native p=373. The existing session, pending requests, claim and staging remain protected by control support issue #1558; no native successor CLAIM/OPEN/Source checkpoint is claimed for this research turn.