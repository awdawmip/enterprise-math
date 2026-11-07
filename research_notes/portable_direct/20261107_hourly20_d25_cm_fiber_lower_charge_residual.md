# D25 — Exact lower-source mismatch at the common Fricke CM observation fiber
2026-11-07 · TASK_RESEARCH author-side. **PROVED CONDITIONAL-ON-CURRENT-INPUT-FIBER / EXACT FINITE VERIFIED / UNREVIEWED / NOT_ADMITTED**.

Parent task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7, frozen science c47e13e4aba0e006366f989d6334d443f6333ae3. Consumes, without reproducing, the two-point Gauss-tail differential theorem at 69f820fb2bcd8673f6bff8eb390526783059daab.

## Theorem (exact F_p observation-level mismatch)
For every prime p≡13 or 19 (mod24), write p=6m+1 and p=8k+3 or 8k+5, respectively. Keep the distinctly labeled normalized p² Gauss tails R_A, R_B and operators
L_A=θ²-z(θ+1/6)(θ+1/3),
L_B=θ²-w(θ+a)(θ+b), where (a,b)=(1/8,3/8) for 8k+3 and (5/8,7/8) for 8k+5.
At the common Fricke CM fiber, the observation points are α=1/2 and β=1/9. Then

    36 [L_A R_A](1/2) - 192 [L_B R_B](1/9)
       = (-1)^m/[4^m binom(2m,m)]
         + 1/[9^(3k+1) binom(3k+1,k)]             (mod p).  (*)

In particular the Frobenius terminal charges cancel **exactly** in this normalized difference, and the surviving expression consists solely of two explicit lower-source injections. Equation (*) is a general identity, not a fitted finite-sample formula. Its right side need not vanish; for p=13 it equals 12 in F_13, for p=19 it equals 1 in F_19.

## Proof
The previous exact inhomogeneous ODEs give
18 L_A R_A= c_A z^(2m+1)-z^p with c_A=(-1)^m/binom(2m,m),
(64/3) L_B R_B= c_B w^(3k+2)-w^p with c_B=-1/binom(3k+1,k).
Multiply the first by 2 and the second by 9, and subtract. Since α,β are nonzero elements of F_p, Frobenius gives 2α^p=9β^p=1, so their -1 terminal contributions cancel. The remaining lower terms are
2c_A α^(2m+1)=(-1)^m/[4^m binom(2m,m)] and
-9c_B β^(3k+2)=+1/[9^(3k+1) binom(3k+1,k)].
All denominators are p-units. QED.

## Discriminating significance
The naive shortcut 'the identical normalized -z^p terminal boundary suffices to identify both forced Gauss readouts at their common scalar CM fiber' is false already at p=13 by the exact 12 mod13 witness. This is a **local observer mismatch**, not a counterexample to the parent supercongruence. It identifies the exact algebraic lower-source compensation that any Fricke/gauge/adjoint transfer must supply, while preserving Euler flag, source labels, and the different differential operators. Because the maps t↦z(t),w(t) are nontrivial, this equality of observation coordinates does not assert global pullback operator equality.

## Verification
The companion exact finite-ring checker constructs BOTH R tails independently from original rising-factorial coefficients mod p³ (not from the displayed ODE), evaluates L_A and L_B at α and β, and tests the separate closed-form right side. All 166 primes p<5000 with p≡13,19 mod24 passed. Sample (p,residual): (13,12),(19,1),(37,36),(43,36),(67,34),(109,17),(373,55). None of these 166 residues was zero; **nonvanishing for all primes is not claimed**, only the exact formula and the exhibited counterexamples to the naive shortcut.

## Next executable step
Seek a source-preserving Fricke gauge or adjoint transformation whose inhomogeneous forcing contributes the explicit (*) lower-source residual and whose p² jet removes the earlier (G_A-G_B)/p²+E_A-E_B obstruction. Independently test p=13,19,43,67,373 before asserting a universal bridge. Mother Δ_p-R_p=0 mod p remains OPEN; p373 native H0/B0 and Source result admission remain separate.

Native tool current bound 2026-11-07: em_status BACKEND_IDENTITY_OR_VERSION_MISMATCH, operation_sent=false; Site CONFIGURED_NOT_LIVE_VERIFIED; historical requests/session/staging preserved; support issue #1558. This is portable author-side mathematics, not a live Researcher CLAIM or accepted Source checkpoint.
