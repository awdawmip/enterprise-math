# C90 — author-only research note (not admitted)
Date: 2026-10-16. Model: classical positive-weight BRC auxiliary on the fixed 156-edge / 142-face integer multiplication graph, using C37's 48-bit core observer. This is not a native X6/Cell theorem.

Free ports 86 and 111, strong faces 8/11/44/61 (coupling 1/2), anchors 89 and 118 (couplings a,b in [1/2,1)), and 68 other independently perturbed weak faces (couplings r_f).

Exact new structural result: all coefficients of the four-variable port partition polynomial have ZERO first derivative with respect to each r_f at the 68-fold zero-perturbation point. This was established by an exhaustive GF(2) character test, then a separate raw 156-bit XOR quotient check.

Surviving term counts at transverse weak degree k=2,3,4,5 respectively:
A/D: 4,18,56,188. B/C: 8,6,38,192.
Maximal absolute weighted coefficients (upper bounding anchors by 1):
A/D: 5/4,111/16,373/16,1033/16.
B/C: 9/4,51/16,211/16,1053/16.

Define T(e) = max_X sum_{k=2}^5 W_{k,X} e^k + (81/4)sum_{k=6}^{68} binom(68,k)e^k. Exact rational evaluation gives T(1/50)=0.17231760274825975...<3/16. Hence sigma*(AD-BC)/kappa^2 >= (75/64)*(3/16-T)>1/60, sigma=(-1)^(c18+c19), for all 2^48 cores, 1/2<=a,b<1 and 0<=r_f<=1/50 independently. This extends C89's 1/7400 bound by factor 148. No true sign-flip witness is claimed.

Validated independently by two Python enumerators and exact integer margin check. Complete portable proof and executable archive are attached in the current research conversation (C90_WORK). Certificate SHA256: b1a90dd8851a1e7603f376dd71a4fda2940b7e4c5a360b4c25e466216ddba63d. This is unclaimed and has no independent Driver acceptance. Next: exact sixth-order spectrum / stronger tail and true zero testing.
