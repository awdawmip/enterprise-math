# D25/LIFT: exact harmonic/factorial block formulas for the terminating Gauss two-jet

Date: 2026-10-31 (Asia/Hong_Kong). Portable author-side research unit D25-HOURLY-20261031-0220-HARMONIC-JET-BLOCKS, logical Research lane chatgpt-research-hourly-enterprise-math-20260923, never the maintenance conversation. Classification: AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. No native CLAIM/OPEN/checkpoint/Result/review is asserted.

Mother ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION; exact Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT at publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3. P000 ACTIVE_LOCKED; this is auxiliary rational arithmetic, not an X6 theorem.

## Exact new lemma (all primes p=6m+1 >=7)

In Z_(p)[t,X]/(t^3) define

\[
J_p(t,X)=\sum_{k=0}^{p-1}\frac{(-m+t/6)_k(-2m+t/3)_k}{2^k(k!)^2}X^k
=P_0+tP_1+t^2P_2\pmod{t^3}.
\]

Write c_{k,r}=[X^k]P_r, and H_n^{(s)}=\sum_{j=1}^n j^{-s}, H_n=H_n^{(1)}. Then the following are *exact rational identities*, not finite sample fits.

**Block I: 0<=k<=m.** Let

\[
B_k=2^{-k}{m\choose k}{2m\choose k},\quad
L_k=-\frac{H_m-H_{m-k}}6-\frac{H_{2m}-H_{2m-k}}3,
\]
\[
V_k=\frac{H_m^{(2)}-H_{m-k}^{(2)}}{36}
+\frac{H_{2m}^{(2)}-H_{2m-k}^{(2)}}9.
\]

Then c_{k,0}=B_k, c_{k,1}=B_k L_k and c_{k,2}=B_k(L_k^2-V_k)/2.

**Block II: m<k<=2m.** Let

\[
D_k=\frac{(-1)^{m+k}m!(2m)!(k-m-1)!}{6\,2^k(k!)^2(2m-k)!},
\quad
M_k=\frac{H_{k-m-1}-H_m}{6}-\frac{H_{2m}-H_{2m-k}}3.
\]

Then c_{k,0}=0, c_{k,1}=D_k and c_{k,2}=D_kM_k.

**Block III: 2m<k<p.** Let

\[
F_k=\frac{(-1)^m m!(2m)!(k-m-1)!(k-2m-1)!}{18\,2^k(k!)^2}.
\]

Then c_{k,0}=c_{k,1}=0 and c_{k,2}=F_k.

**New unit-support refinement.** For *every index* in each block, its first nonzero coefficient (respectively c_{k,0}, c_{k,1}, c_{k,2}) is a p-adic unit. Thus the order in the deformation parameter t is *exactly* 0/1/2, not only bounded below by 0/1/2. Block III's leading jet is **harmonic-free**; harmonic corrections occur only in the first two blocks. This strengthens GH-178's previously known upper support bounds without recrediting that prior result.

### Proof

For k<=m, neither rising factorial vanishes at t=0. Its logarithmic first derivative is L_k and its logarithmic second derivative is -V_k, giving (1,L,(L^2-V)/2) times B_k. For m<k<=2m, only the j=m factor in (-m+t/6)_k vanishes. Removing it produces (-1)^m m!(k-m-1)!/6; multiplying by (-2m)_k=(-1)^k(2m)!/(2m-k)! produces D_k, while the remaining logarithmic derivative is M_k. For 2m<k<p the two factors at j=m and j=2m both vanish. Their product contributes t^2 times (-1)^m m!(k-m-1)!(2m)!(k-2m-1)!/18, yielding F_k with no harmonic factor. All factorial arguments and harmonic denominators are <p, and 2,6,18 are units for p>=7. The first nonzero coefficient in each block is therefore a p-adic unit. QED.

## Source-bound observer and exact anchors

The original hard target is **still open**:

\[
\mathcal A_p(1)=\sum_{k=0}^{p-1}(6k+1)\frac{{2k\choose k}^2{3k\choose k}}{216^k}
\stackrel{?}{\equiv}p\pmod{p^3},\qquad p\bmod24\in\{13,19\}.
\]

The current lemma supplies closed harmonic/factorial forms for the existing GH-178 parameter-jet reconstruction, not a new proof of LIFT. At t=p the deformation is exactly the original Gauss polynomial G_p. At the fixed original X=1, preserve GH-178's *previously established* relation

\[
(\mathcal A_p(1)-p)/p^2\equiv (UQ_0-1)/p+S_2Q_0+UQ_1-E_p\pmod p
\]

with S_r=P_r(1), U=S_0/p+S_1, Q_r=[(1+12\theta)P_r](1); E_p is the original signed high-degree projection, not the different reflected 3347 polynomial. No port is set to zero by assumption.

Actually executed an **independent factorial/harmonic formula** checker, separately computing all coefficients by GH-178's *recurrence without harmonic inputs*, plus original rational Gauss and original 216-weighted series. For all 330 primes 7<=p<5000 with p=1 mod6, all 772620 coefficient positions passed (each checked in all three jets modulo p^3, and checked for nonzero leading-unit support). All 166 original target-class primes passed independent raw-216 scalar regression (not an extended prime census or a universal proof).

Actual values: p=19 gives Block-I/II/III contributions to S2 mod p (3,18,10), original carry/jets/signed E=(16,15,12) mod19. At p=157, S2 blocks=(112,135,0) but signed E=82, reproducing GH-167's *previously known* distinction via a separate coefficient route. At p=373, S2 blocks=(197,212,252), S2=288, Q0=171, Q1=82, carry/jets/E=(81,115,196), so 81+115-196=0 mod373. The three contributions to S2*Q0 are 117,71,197 mod373: individually nonzero. The checker returned PASS_D25_EXACT_HARMONIC_BLOCKS_INDEPENDENT_RAW_216.

The arithmetic BRC carrier is Z_(p)[t,X]/(t^3). Preserved ports include k-block, t-order, p-valuation, sign, coefficient provenance and X-degree, with future operations t=p, X=1, theta, degree >=p projection, mod p^3 and division by p^2. The formulas preserve these data; a total-only S2 compression does not preserve the signed projection. This is **not** native X6 geometry, a native H0/B0 divided-power run, or an authenticated Frobenius/373 experiment.

## Next smallest unfinished step and control

Use the displayed harmonic Block-I/II and harmonic-free Block-III kernels to seek a *genuinely new, joint* finite WZ/CM/Gauss-Manin certificate for carry+jets-E, in **both** residue classes. This lemma does not by itself reduce the number of unknown global connection constants, and finite checks do not close LIFT/JT2. The D25 divided-power, [X]U mod p^2, semilinear Frobenius, eta and native p373 obligations remain open.

Gateway 0.6.11 current observation: research_authority_granted=false, executor_binding_configured=false, quota 5/5 active, Source CODE_REVIEW_REQUIRED / UPSTREAM_CODE_REVIEW_REQUIRED. Recovery_status is advertised but not callable through this current client; no invented request is issued. Existing historical session/claim/staging is not borrowed or modified. Control support: enterprise-math #1558; native benchmark support: #1559. The file is author-side portable evidence, **not** Source checkpoint or Task/Result/review admission. Activity registration remains pending until genuine authorization.
