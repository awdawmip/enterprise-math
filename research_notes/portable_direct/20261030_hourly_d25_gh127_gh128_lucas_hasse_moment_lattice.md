# D25/LIFT GH-127–GH-128 — Lucas–Hasse two-digit character-moment lattice and retained mixed residual

2026-10-30 Asia/Hong_Kong. Research lane: chatgpt-research-hourly-enterprise-math-20260923; parent Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3 (unchanged). Scope: author-side portable proof and exact direct finite-field checks. Status: AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. No native claim, authorized open, Source checkpoint, Result or independent review is asserted.

## Exact setup

Let p>=5 be an odd prime, q=p², N=(p-1)/2, e=(q-1)/2=N(1+p), d=floor(N/2), and k=F_q. Set f_B(X)=X³+X²+BX, with B in k, and

H_p(B)=[X^(p-1)]f_B(X)^N = sum_(u=0)^d N!/(u!²(N-2u)!) B^u.

For r>=0 define the punctured, signed character moment

S_r(B) = sum_(x in k, f_B(x)!=0) chi_q(f_B(x)) (x/f_B(x))^r,

where chi_q(0)=0. Write H_p(B+t)=sum_i H_p^[i](B)t^i, using Hasse/divided-power derivatives. GH-124/GH-126 established the single-digit moment theorem. The following two-digit and boundary results are new extensions for this research lane, not a claim of historical priority.

## GH-127 — Lucas–Hasse two-digit formula and rank-one window

**Theorem (for all odd primes p>=5).** For 0<=i,j<=N, excluding (i,j)=(N,N), the exact identity in F_q is

S_(i+p*j)(B) = - H_p^[i](B) (H_p^[j](B))^p / (binom(N,i) binom(N,j)).

Both denominators are invertible modulo p. In particular, S_(i+p*j)=0 whenever i>d or j>d. Assign the artificial correction M_(N,N)=0, and let M_(i,j)=S_(i+p*j) for the other entries. Then M is the Frobenius outer product

M_(i,j)=-U_i U_j^p,   U_i=H_p^[i](B)/binom(N,i),

so rank(M)<=1. The artificial corner is essential: it need not equal the actual punctured moment S_e.

**Proof.** The exact polynomial identity Phi_q(B):=-sum_(x in F_q) f_B(x)^e=H_p(B)H_p(B)^p follows from f_B^e=f_B^N (f_B^N)^p. In the resulting polynomial in X, 1<=degree<=3e<2(q-1). The only contribution to the nonzero finite-field power sum is coefficient X^(q-1). Since deg f_B^N=3N<2p-1, the only exponents u,v in [0,3N] with u+pv=q-1 are u=v=p-1, giving the product of the two Hasse coefficients. This holds identically in F_p[B], so substitute B+t.

For 0<=r<e, coefficient extraction in Phi_q(B+t)=-sum_x(f_B(x)+xt)^e gives [t^r]Phi_q(B+t)=-binom(e,r)S_r(B). Terms with f_B(x)=0 contribute zero because e-r>=1. For r=i+pj with 0<=i,j<=N and r<e, Lucas's congruence yields binom(e,r)=binom(N,i)binom(N,j) mod p, and neither factor vanishes. Independently, the coefficient of t^(i+pj) in H_p(B+t)H_p(B+t)^p is H_p^[i](B)(H_p^[j](B))^p because deg H_p=d<p. Equating the coefficients proves the formula. Since deg H_p=d, all Hasse derivatives of order>d vanish; the outer-product representation and zero indices follow. QED.

For p=3347, N=1673 and d=836. There are (1674)²-1=2,802,275 Lucas-visible moment indices 0<=r<e; (1674)²-(837)²-1=2,101,706 of these are necessarily zero for every B in F_(3347²). This extends the prior 837 consecutive single-digit zeros to a sparse two-digit zero lattice. It does not imply that the individual signed summands are zero.

## GH-128 — blind digit boundary, mixed observable and root correction

**Blind boundary.** At r=N+1, the units base-p digit exceeds N, and binom(e,r)=0 in F_p. Thus the derivative/coefficient identity is not invertible and does not force S_(N+1)=0. Direct exact enumeration at p=11, B=3+sqrt(2) in F_121 gives S_6=2+sqrt(2), nonzero. The GH-126 single-digit zero band cannot be extended to this next index as a general theorem.

**Mixed observer theorem.** If H_p(B)=0 but H'_p(B)!=0, then all single-digit S_i for 0<=i<=N and all pure Frobenius S_(pj) for 0<=j<=N vanish, whereas

S_(p+1)(B)=-4 H'_p(B)^(p+1) != 0.

The proof uses GH-127 at (i,j)=(1,1), the congruence N=-1/2 in F_p, and the nonzero field norm H'(B)^(p+1). Thus the zero total and zero single-direction moment summaries erase a genuinely observable mixed-Frobenius residual.

At p=11, H_11(B)=1+9B+8B². The value B=4 satisfies H_11(4)=0 and H'_11(4)=7. Hence S_0=S_1=S_11=0 while S_12=-4*7^12=2 mod 11. The independently enumerated direct character sums agree.

**Excluded-corner defect.** At r=e, f_B(x)^(e-r)=f_B(x)^0 is nonzero even at roots, so the punctured definition differs from the polynomial coefficient formula. Exactly,

S_e(B)=-sum_(x in F_q: f_B(x)=0) chi_q(x).

At p=11, B=4, the two nonzero roots of X²+X+4 have norm 4, each has quadratic character +1 in F_121, and S_60=-2=9 mod 11. Consequently the true punctured corner can be nonzero although the corrected rank-one matrix corner is 0.

## Executed exact finite-field certificates

The companion script d25_gh127_gh128_lucas_hasse_moment_check.py enumerates all p² elements in F_p[sqrt(2)] for p=11,19,43,59 (2 is a quadratic nonresidue for these p), directly accumulates chi(f)(x/f)^r for **every** r=0,...,e-1, and separately calculates Hasse derivatives via integer multinomial coefficients. It compares every Lucas-visible index and checks the excluded corner by enumerating actual polynomial roots.

Cases B=(3,1),(4,2),(5,1),(7,3) for p=11,19,43,59 respectively, plus the p=11 supersingular witness B=(4,0). Exactly 35+99+483+899+35=1,551 visible indices and 26+74+362+674+26=1,162 forced zero indices passed. All four blind S_(N+1) examples are nonzero; p=11 B=4 verifies S_12=2, S_60=9. Actual terminal marker: PASS_GH127_LUCAS_HASSE_TWO_DIGIT_AND_BLIND_SPOT. No floating point, random sampling or native Enterprise Math experiment was involved.

## BRC, provenance and continuation

BRC COMPOSE_APPLIED: retain finite-field x branch, signed chi(f_B(x)) weight, exact pair (i,j), Frobenius and root-support provenance until the declared moment readout. The rank-one compression is adequate **only** for this Lucas-visible corrected matrix, not for blind r=N+1, the actual r=e punctured corner, arbitrary future operations or native X6 dynamics. B is an external chart; no physical/native-transfer statement is claimed.

Original mathematical inputs: GH-124/126 author-side notes in Enterprise Math (GH-126: research_notes/portable_direct/20261030_hourly_d25_gh126_character_higher_moments.md). P000 ACTIVE and frozen scientific pin remain unchanged. No independent CM/Jacobi/Gauss special-value evaluation for marked S_1(T²=8/9), GH-83, R_3347(9), original GH-3 congruence, or native p=373 experiment is claimed. No prior-art novelty priority is asserted.

**Next exact scientific action:** find and prove an independent CM/Jacobi/Gauss or p-adic-period evaluation of original marked S_1 at T²=8/9 without assuming GH-83, preserving original two-torsion mark and differential normalization. Studying the blind r=N+1 sector is a separate optional mathematical path; it must not be presented as that missing CM evaluation. Native D25 session/claim/run and checkpoint recovery remains with existing support issue #1558; old requests and protected staging are not changed by this GitHub portable note.
