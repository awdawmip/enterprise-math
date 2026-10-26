# D25/LIFT — Two-digit factorial Green lift with explicit odd-harmonic correction

Date: 2026-10-26. Parent Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged.

**AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.** This extends the preceding factorial-normalized oriented Ward quotient by a second p-adic digit; it is not native original-class CM/Frobenius evidence, original scalar reflection cancellation or formal D25 mathematical admission.

## Exact inherited input and new theorem

For each prime p=6m+1>=7, put N=2m-1. Consume the preceding actual signed oriented corrected-Clausen/Hasse sources S_h^{ab}=J_h^{ab}+E_h^{ab}, left edge Y_{1-2m}^{ab}, and three channels (a,b)=(0,2),(1,2),(0,3). Retain exact finite Green coefficients and factorial p-units:

\[
F_m=\frac{2^{4m-1}(2m-1)!(2m)!}{(4m)!},\quad C_t=\frac{4^t(t!)^2}{(2t)!},
\quad D_h=\frac{1}{p-2h-1}\prod_{k=h+1}^{2m-1}\frac{p-2k}{p-2k-1},
\quad P=\prod_{k=1-2m}^{2m-1}\frac{p-2k}{p-2k-1}.
\]

For 0<=t<N define the new p-integral odd-harmonic correction

\[
\boxed{E_t=\frac1{2N+1}-\frac1{2t+1}
+\sum_{r=t+1}^{N}\left(\frac1{2r-1}-\frac1{2r}\right).} \tag{1}
\]

All denominators here are <p and p-units. The new coefficient formulas, now **modulo p²**, are

\[
\boxed{\frac{D_{-t-1}}p\equiv-\frac{F_mC_t}{2t+1}(1+pE_t)\pmod{p^2}},\qquad
\boxed{\frac Pp\equiv-F_m C_N\left(1+\frac p{2N+1}\right)\pmod{p^2}}. \tag{2}
\]

They yield a two-digit **source-faithful oriented Ward law**

\[
\boxed{\begin{aligned}
\frac1{pF_m}\sum_{h=0}^{2m-1}D_h S_h^{ab}\equiv {}&
\sum_{t=0}^{N-1}\frac{C_t}{2t+1}(1+pE_t)S_{-t-1}^{ab}\\
&-C_N\left(1+\frac p{2N+1}\right)Y_{1-2m}^{ab}
\pmod{p^2}.
\end{aligned}} \tag{3}
\]

All exact J+E sources, two finite boundaries, source labels and Hasse channels are retained; the external infinity-port remains an explicitly different observer.

## Complete proof

At each negative h=-t-1 factor the exact Green coefficient as

\[
\frac{D_{-t-1}}p
=\frac1{p+2t+1}\frac1{p-1}
\prod_{r=1}^{t}\frac{p+2r}{p+2r-1}
\prod_{k=1}^{N}\frac{p-2k}{p-2k-1}.
\]

The unique k=0 numerator was p and has already been extracted. All remaining factors have p-unit numerators/denominators. Over the p-local ring, for p-units x,y,

\[
\frac{p+x}{p+y}=\frac{x}{y}\left(1+p\left(\frac1x-\frac1y\right)\right)\pmod{p^2}.
\]

The zeroth-order product is -F_m C_t/(2t+1), while the first-order relative correction is

\[
-\frac1{2t+1}+1+
\sum_{r=1}^{t}\left(\frac1{2r}-\frac1{2r-1}\right)+
\sum_{k=1}^{N}\left(-\frac1{2k}+\frac1{2k+1}\right).
\]

The identity

\[
1+\sum_{r=1}^{N}\left(\frac1{2r+1}-\frac1{2r-1}\right)=\frac1{2N+1}
\]

telescopes the correction exactly to E_t in (1), proving the first (2). The product P/p lacks the initial 1/(p+2t+1) and includes all negative r=1,...,N; its relative correction is directly 1/(2N+1), proving the second (2). Finally, the inherited **exact** Ward identity

\[
\sum_{h=0}^{2m-1}D_hS_h^{ab}
=P Y_{1-2m}^{ab}-\sum_{h=1-2m}^{-1}D_h S_h^{ab}
\]

is divisible by p in Z_(p). Divide first by pF_m and insert the two coefficient expansions. This proves (3) modulo p² with no invalid division by a zero residue or loss of terminal source tags. QED.

## Numeric source-bound witness and author check

At p=13 (m=2, N=3), the actual corrected Hasse moments produce:

| channel | Zeroth-order RHS B mod 169 | First correction L mod 13 | B+13L = exact normalized flux mod 169 |
| --- | ---: | ---: | ---: |
| (0,2) | 141 | 2 | 167 |
| (1,2) | 111 | 0 | 111 |
| (0,3) | 97 | 8 | 32 |

The (1,2) channel still has the **uniform non-removable endpoint** from the previous theorem; the accidental vanishing of its aggregate first correction at p=13 is not an all-prime zero theorem.

The companion Python stdlib verifier imports the immediately preceding actual Fraction corrected-jet/source checker (not a synthetic arbitrary source) and checks all individual coefficients in (2), each actual three-channel identity (3), and the p=13 reference values. Local run: **142 counted exact assertions PASS** for m<=12 and the nine prime targets p=7,13,19,31,37,43,61,67,73. The general conclusion is the proof above; finite tests are author-only evidence, not independent review or native CM computation.

## BRC, scope and next research unit

BRC **COMPOSE_APPLIED**: exact signed oriented pair provenance (j,ell), three Hasse channels, two-digit p-local valuation, both finite J+E sources, and separately tagged infinity port. The Green quotient is an auxiliary algebraic observer, **not** the original Clausen reflection weighted by 2^n(1-6n); this computation does not convert its external formal coordinates into primitive P000 X6 axes. Existing full binomial-fibre source tomography is preserved for quadratic-rank operations.

Next exact executable portable question: substitute the full corrected-Clausen (k-1,k-2) Hasse coupling and infinity-port correction into (3), compare actual separately weighted T02/U02/T12/T03, and derive an all-prime adjoint/WZ cancellation or certify a nonzero source-tagged remainder. The mother D25/LIFT/JT2 goal still requires original-class H0/B0, [X]U mod p², Frobenius direction and eta, kappa, Delta_p-R_p, real native experiments and independent mathematical review. The Source scientific pin remains c47e13e4aba0e006366f989d6334d443f6333ae3; no Source CLAIM/OPEN/checkpoint is asserted.