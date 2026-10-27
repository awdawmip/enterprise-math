# D25/LIFT R20 — Original fixed-2 cutoff ports: two distinct exact Smith fingerprints

Date 2026-10-27. Research logical conversation: chatgpt-research-hourly-enterprise-math-20260923 (not maintenance). Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen scientific Source c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged. **AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.**

## Consumed input and question

Consume existing R15 exact original-parameter low/high cutoff and positive complement, R16's different Green flux, R17's mod-p full-rank geometric moment factorization, R19's genuine ramified source, and the authentic signed six-label Hasse transport; do not recredit those results. Unlike the full signed-rank carrier, the actual original Clausen cutoff retains only ordered pairs of difference rank ell-j <= 0; the positive complement uses ell-j > 0. What is the exact p-local information profile introduced by this cutoff itself?

Let p=6m+1 >= 7 be prime and R=Z_(p), N=2m. At original theta=-p/6, set

f_j=(1/6)_j (1/3)_j/(j!)^2, for 1<=j<=N;

beta_(p-ell)=f_(p-ell)/p^2, for 1<=ell<=N.

These are actual original corrected Clausen coefficients from R15 (f_r(theta)=2^r r_r). The exact ratio f_(j+1)/f_j=(6j+1)(3j+1)/(18(j+1)^2) gives v_p(f_j)=0 at 1<=j<=m and v_p(f_j)=1 at m<j<=N; all beta factors are R-units.

At **fixed original geometric weight z=2**, define labelled N-by-N ordered-pair kernels, rows j and columns ell:

K^-_(j,ell) = [ell<=j] (6p+1-6(ell-j)) 2^(ell-j) f_j beta_(p-ell);

K^+_(j,ell) = [ell>j] (6p+1-6(ell-j)) 2^(ell-j) f_j beta_(p-ell).

The exact R15 original low/high cutoff and complementary scalar equal respectively 2^(1-p) times the sum of all K^- entries and of all K^+ entries, after normalizing by p^2. The separately ordered high/high p^2 H_beta term remains outside these two kernels. The matrices are *pair-port extensions* of these genuine scalars, not permission to vary real hypergeometric coefficients independently.

## Theorem — exact Smith forms over R (all target primes)

**SNF(K^-) = diag(1 [m copies], p [m copies]).**

**SNF(K^+) = diag(1 [m copies], p [m-1 copies], 0 [one copy]).**

In particular both ranks modulo p equal m, but ranks over Q equal 2m and 2m-1 respectively. There are m one-digit p-local deficits in the lower port; in the positive-complement port m-1 such deficits coexist with an independent permanent null direction (column ell=1). These are different from the earlier single p-torsion Ward seam, which acts on a different declared module.

**Proof.** Factor K^±=diag(f_j 2^(-j)) W^± diag(beta_(p-ell) 2^ell), where W has coefficient 6p+1-6(ell-j) on its declared triangular support. All right-hand diagonal factors are R-units; the left-hand valuations are exactly 0 (first m) or 1 (last m).

W^- is lower triangular with constant diagonal 6p+1, an R-unit. Hence W^- is unimodular and K^- is equivalent over R to diag(f_1,...,f_N), whose unit parts reduce to m ones and m p's.

For W^+, the first column and last row vanish. Permute columns into (2,3,...,N,1). The (N-1)x(N-1) nonzero block (rows j=1,...,N-1) is upper triangular with constant diagonal 6p-5, an R-unit because p>=7. Thus the full matrix is equivalent to diag(f_1,...,f_(N-1),0). Of those first N-1 factors, m have valuation zero and m-1 have valuation one. This proves both full Smith forms, not just mod-p ranks.

The two independently useful exact determinant identities are

det(K^-)=(6p+1)^N PROD_(j=1)^N f_j PROD_(ell=1)^N beta_(p-ell),  v_p(det)=m;

det(K^+_[rows 1..N-1; columns 2..N])=[2(6p-5)]^(N-1) PROD_(j=1)^(N-1) f_j PROD_(ell=2)^N beta_(p-ell),  v_p(det)=m-1.

Both normalized leading determinants are nonzero mod p. QED.

## Actual finite-source certificates and reproducibility

Companion executable Python standard-library checker: 20261027_hourly_d25_original_cutoff_smith_r20_check.py. Executed PASS: independent Fraction-rational original f, reflected beta, actual pair matrices, modular Gaussian ranks, exact determinants and valuations for p=7,13,19,31,37,43; factorial and product-route beta reduction plus normalized determinant/minor residue checks at 11 targets including 733 and 997. General theorem follows from the triangular proof; for p>43 the rank values below are **theoretically determined**, not reported as executed large Gaussian eliminations.

| p | m | rank(K^- mod p) / rank(K^+ mod p) | det(K^-)/p^m mod p | upper max minor/p^(m-1) mod p |
|---:|---:|---:|---:|---:|
| 7 | 1 | 1 / 1 | 5 | 1 |
| 13 | 2 | 2 / 2 | 11 | 3 |
| 19 | 3 | 3 / 3 | 9 | 15 |
| 37 | 6 | 6 / 6 | 20 | 17 |
| 733 | 122 | 122 / 122 | **663** | **165** |
| 997 | 166 | 166 / 166 | **704** | **936** |

BRC **COMPOSE_APPLIED**: the carrier retains ordered (j,ell) labels, rank sign, actual original cutoff, p-valuation, 2^rank and the operation of passing from labelled ports to a scalar. One scalar contraction may be sufficient for that scalar but does not preserve future pair-port or signed Hasse operations. Over R/p^h, appropriate unimodular coordinates exhibit one digit of precision loss in m lower-port directions, m-1 upper-port directions, and one permanently unobserved upper direction. These are auxiliary arithmetic coordinates, not P000 native X6 axes or a physical model; protected P000 and ACTIVE residual-fidelity worldview are unchanged.

**Next smallest scientific unit:** constrain this two-port matrix result by the actual signed 3+2+1 Hasse coefficient family at fixed z=2 and the authentic bivariate J/E master. Determine whether the constrained sources admit a genuine cross-channel WZ cancellation; failing that, produce an actual six-labelled nonzero source residual. Preserve the two genuine finite origins in each orientation, positive/infinity, the ordered high/high corner, and independent original-class H0/B0, [X]U mod p^2, semilinear eta, kappa, Delta_p-R_p, native experimental and review gaps. A Smith theorem for the freely testable pair-port module alone is **not** a no-go for the constrained real Hasse family.

**Control/recovery:** direct em_status version 0.6.11 reports research_authority_granted=false. Exact continuation request researchhourly-20261027-0325-continuation-r20 failed INVALID_ARGUMENT/CONTROL_QUOTA. Last verified own recovery #6567 found no pending/unopened/run/unpublished upload, two neutral protected staging archives; last successful Source continuation #6568 preserved SOURCE_BYTES_AND_RECORDED_CLAIM_VERIFIED, REGISTER_NEW_SESSION_AND_CLAIM_CURRENT_PUBLICATION, execution_authorized=false. Existing support enterprise-math#1558 owns the predecessor-CAS/session transition. No claim/open/native checkpoint/freeze or mathematical admission is asserted. Mother D25/LIFT/JT2 OPEN.