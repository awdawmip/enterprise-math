# D25/LIFT GH-60 — full rational torsion from signed CM Frobenius

2026-10-28 Asia/Hong_Kong. Author proof / exact checked / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. Derived directly from GH-58/GH-59 (separate author proofs, not native admitted Results). Mother objective ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION remains OPEN; task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged. This research lane chatgpt-research-hourly-enterprise-math-20260923 is NOT the maintenance lane.

## New structural theorem GH-60

Fix **any** prime p≡19(mod24), p>=19, set k=F_(p²), t=2sqrt(2)/3 in k, with sqrt(2)^p=−sqrt(2). Define the GH-58/59 CM curve (translate X→x=X+2)

\[
E_t:y^2=x(x^2-6x+\tfrac92(1-t)).
\]

Let \(\pi=F_{p²,E_t}\) denote its geometric q-Frobenius endomorphism. GH-58 proved a **signed** degree-2p endomorphism \(\Phi=\psi_{-t}\circ F_p\) with

\[
\Phi^2=[-2]\circ\pi,\qquad \deg\Phi=2p.
\]

GH-59 proved \(\operatorname{Tr}(\Phi)=0\) for every p≡19(mod24), using the GH-32 inert CM/Hasse input, the p-divisibility trace congruence and the endomorphism trace bound. The general integral elliptic characteristic relation

\[
\Phi^2-[\operatorname{Tr}\Phi]\Phi+[\deg\Phi]=0
\]

therefore gives \(\Phi^2=[-2p]\). Comparing with the **signed** GH-58 equality, \([-2]\pi=[-2p]\), and using the torsion-freeness of the elliptic endomorphism ring, yields the stronger, exact identity

\[
\boxed{F_{p²,E_t}=[p]\quad\text{in }\operatorname{End}_{\overline k}(E_t).}\tag{60.1}
\]

The endomorphism identity is more informative than the point-count equality \(\#E_t(k)=(p-1)^2\) already obtained in GH-59. A curve with that order need not have the particular group structure below without further evidence.

For any E over k, \(E(k)=\ker(\pi-[1])\) as a group of geometric points. Apply (60.1):

\[
E_t(k)=\ker([p-1])=E_t[p-1](\overline k).
\]

Since gcd(p,p−1)=1, the full prime-to-characteristic torsion group has its usual two-generator structure. Therefore

\[
\boxed{E_t(\mathbb F_{p²})\ \cong\
(\mathbb Z/(p-1)\mathbb Z)^2,\qquad
E_t[p-1]\subset E_t(\mathbb F_{p²}).}\tag{60.2}
\]

This is **valid for every prime p≡19(mod24)** under the inherited GH-32 and GH-58/59 hypotheses; it is not merely a finite numerical observation. Equivalently, all \((p-1)\)-division points are rational in exactly the field specified (not necessarily of minimal field of definition). The sign [+p], not [−p], is essential. No claim about the distinct non-CM GH-31 elliptic curve, original G weighted moment, W/S or native X6 Hasse ports follows.

## Independent arithmetic certification

The companion standard-library Python checker imports the already published, byte-matched GH-58/59 finite-field primitives, enumerates **every** affine point of E_t over F_(p²) (two square roots when nonzero), and verifies \([p-1]P=O\) by a separate elliptic group law and binary multiplication. It checks all inert primes p<200:

- p=19: all 324 points including O;
- p=43: all 1,764 points;
- p=67: all 4,356 points;
- p=139: all 19,044 points;
- p=163: all 26,244 points.

All checks PASSED; this exhaustive finite confirmation supplements the above general algebraic theorem. It is not an independent proof of the GH-32 CM premises.

## Typed source and continuation

BRC COMPOSE_APPLIED: keep distinguished point label P, full group addition/scalar operation, isogeny kernel and sign, p²-Frobenius endomorphism and group-coordinate observer. The group structure would be erased by replacing the endomorphism with its trace/point count alone; (60.1) certifies the stronger observer. Preserve original GH-22 F/G ports and GH-29 square-fiber signed residual, W/S, six native Hasse ports, P000's 6D space + 1 time, all separate from this auxiliary finite-field curve.

Next exact mathematical action: class p≡11(mod24) remains an **ordinary** CM class, not covered by (60.1); attempt a genuinely sourced horizontal Gauss–Manin/Katz or weighted-character identity for \(tP'_{(p-3)/4}(t)-P_{(p-3)/4}(t)=0\), avoiding derivative-from-point-count inference. Independently original GH-3 T_d(9) all-prime theorem, GH-20/21 next precision, R23/R36, native p=373, six Hasse ports, and Driver review remain open.

Native gateway 0.6.11 shows research_authority_granted=false and source_sync.control.state=CODE_REVIEW_REQUIRED. These are **portable author proofs only**, not native CLAIM, authorized OPEN, Source checkpoint, Result or independent acceptance. Historical service session, staging, contribution and pending requests are preserved; control issue awdawmip/enterprise-math#1558 is the owner recovery path. No modification to task schedule or frozen Source pin.
