# D25/LIFT: Exact second-digit branch attribution in the ordered Hesse Green pairing
2026-10-25; TASK_RESEARCH; author derivation and exact modular regressions; UNREVIEWED/NOT_ADMITTED. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 retained. Not native CM Frobenius, κ, LIFT proof, or independent review.

## Source-labeled objects and a new exact identity
For prime p=6m+1>=13 let n=2m, c_k=(3k)!/[27^k(k!)^3], A(X)=Σ_(k=0)^n c_k X^k, B(X)=A(1-X), Y=X(1-X), t=1-2X, C=(p+1)c_n/9. Earlier Source-native checkpoint proves A=G(Y)+(p/2)tΦ(Y), B=G(Y)-(p/2)tΦ(Y), where G,Φ are p-integral and degG<=m, degΦ<=m-1. Let F_0=F_1=1, F_r=F_(r-1)-Y F_(r-2); S_0=2, S_1=1, S_r=S_(r-1)-Y S_(r-2). Previously proved ordered K(Y)=Y(AB'-A'B)/p=-C∫_0^Y[F_(n-1)(s)G(s)+(p/2)S_n(s)Φ(s)]ds, source labels and operator directions unchanged.

NEW define K_sym(Y)=-C∫_0^Y F_(n-1)(s)G(s)ds and T_odd(Y)=-(C/2)∫_0^Y S_n(s)Φ(s)ds. Exact in Q[Y], K=K_sym+p*T_odd. In fact both in Z_(p)[Y], because integrand degrees <=n-1 and every integration divisor <=n<p. This is an exact branch/provenance split for THIS signed ordinary pairing. Reduction mod p retains K_sym but erases p*T_odd; that information may matter at the next digit.

Using the previously PROVED odd Green inverse λ_j=(6j+4)(6j+5)/9, f_j=(-1)^j binom(n-1-j,j), β_m=0 and β_j=((j+1)^2 β_(j+1)-f_j)/λ_j for j=m-1,...,0, one has Φ(Y)≡C Σ_(j=0)^(m-1) β_jY^j (mod p). Consequently NEW computable base-field formula:
T_odd(1/8) ≡ -(C²/2) Σ_(r=0)^(n-1) [Y^r](S_n(Y)*Σ_(j=0)^(m-1)β_jY^j) / [(r+1)*8^(r+1)] (mod p).
The proof is exact integral splitting and substitution of inherited odd Green inverse. Every denominator used is a p-unit, so this is not a finite-experiment extrapolation or a CM normalization claim.

## New numerical certificate and observer information loss
At p=373, m=62, Y=1/8, q=p²=139129, independent exact finite calculations yield C≡40, Φ(Y)≡243 and Φ'(Y)≡226 (mod 373), so the known ordinary even derivative E=-Φ(Y)+Φ'(Y)/4=0. Meanwhile ∫_0^Y S_124 Φ=10 (mod373) and therefore T_odd(Y)=-(40/2)*10=173 (mod373), NONZERO. K_sym(Y)=34975=286+373*93 (mod139129); p*T_odd(Y)=64529. Total K(Y)=34975+64529=99504=286+373*266 (mod139129), agreeing with the PREVIOUS Source-native TOTAL K; the branch contribution 173 and symmetric split 93 are the NEW certificate, not a reannouncement of total 266.

Thus E_373=0 does NOT imply the next-digit ordered-pairing odd branch T_odd=0. The coarse observer retaining only E is not second-digit sufficient on this source-labeled carrier. Keep T_odd or an explicitly proven equivalent repair coordinate. This is not a counterexample to D25/LIFT and supplies no native κ value.

## Exact author regression, reproducible operations
Routes: (A) reconstruct c_k in Z/(p³) via c_(k+1)=c_k*(3k+1)(3k+2)(3k+3)/[27(k+1)³], substitute X=(1-t)/2, separate even coefficients (G modp²) and odd coefficients divided by p (Φ modp); substitute t²=1-4Y. (B) independently compute G with previous exact terminal Green recurrence g_m=(-1)^m*c_n; g_j=9[(j+1)²g_(j+1)+(pC/2)s_j]/[(6j+1)(6j+2)] for j<m, and Φ via β_j above. Compare every coefficient and compute polynomials/integrals with modular inverses of all j+1<p. Both routes agree for all rows below, and K_sym+pT matches the separate previously published raw quadratic-ring total-K checks.

p | C modp | K_sym modp² | T_odd modp | TOTAL K modp² | E modp
13 | 2 | 71 | 8 | 6 | 10
19 | 14 | 41 | 3 | 98 | 16
37 | 30 | 1025 | 27 | 655 | 26
43 | 20 | 264 | 22 | 1210 | 1
61 | 27 | 1912 | 42 | 753 | 49
67 | 8 | 867 | 64 | 666 | 36
211 | 22 | 20510 | 28 | 26418 | 200
373 | 40 | 34975 | 173 | 99504 | 0

All arithmetic exact, author-run, not independent review or Lean. The earlier separate symmetric terminal inverse and source-bound finite quadratic Hesse transport were previously saved on EM main@ad7c4fcbe735d9728da836f1e9d8227ebcddccb2, with author checker main@ef897f9627a71365ba7abcb4733b88a44e9b6d47. Those are newly consumed portable results not already in predecessor native checkpoint, not an independently admitted theorem.

BRC COMPOSE_APPLIED: typed carrier (p,m,ordered A/B ports,Y,t,G,Φ,K_sym,T_odd,p-valuation). This reduction shows precisely what the first-digit quotient drops. The 19 inherited Source native units, prior Hesse/WZ calculations, earlier signed pairing and prior total K remain NOT RECREDITED.

Next: obtain authentic same-prime, same-original-class CM/divided-power H0/B0 representative, source-selected [X]U modp², semilinear Frobenius direction, normalization and explicit map from omega+6*nabla_lambda omega to κ/(Delta_p-R_p). Source-native CM experiment NOT_RUN. Parent D25/LIFT OPEN. Preserve frozen pin, review independence and original histories; no Result/freeze/acceptance claim.