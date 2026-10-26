# D25/LIFT — Diagonal one-digit Green resonance and oriented source Ward identity

Date: 2026-10-26. Parent Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged.

**AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.** This is an external exact corrected-Clausen finite-hypergeometric result, not original-class native CM evidence, a Source checkpoint, formal mathematical admission, or a D25/LIFT/JT2 proof.

## Consumed exact source and new problem

Consume (not recredit) the exact diagonal moment recurrence with the two genuine oriented cutoff ports in research_notes/portable_direct/20261026_hourly_d25_diagonal_rank_moment_closed_recurrence_r11.md. It states for p=6m+1, n_*=1-2m <= n <= 2m-1, and each Hasse channel (a,b) in {(0,2),(1,2),(0,3)}:

\[
(p-2n)M_n^{ab,1}-C_nM_n^{ab,0}
=A_nM_{n+1}^{ab,1}+B_nM_{n+1}^{ab,0}+S_n^{ab}, \tag{1}
\]
where S=J+E retains all nonhomogeneous Hasse and finite-cutoff sources, C_n=(p-n)(p/2-n), A_n=p-1-2n=6m-2n, B_n=-18m^2+9mn-n^2. The oriented moments are defined on the actual labelled pairs 1<=j,ell<=2m, n=ell-j, via M_n^{ab,s}=sum j^s u_{a,j}u_{b,p-ell}, where u are coefficients of the corrected Pochhammer parameter family from the predecessor. Empty moments are zero. The earlier paper already established a forward p-local unit reconstruction for M^1/M^2. NEW problem: obtain an exact first-order contracted Green law, identify the valuation-one n=0 seam, and derive its oriented all-channel source compatibility, without deleting any source face.

## Theorem A: source-faithful scalar contraction

Define the centred labelled-rank observation
\[
Y_n^{ab}=M_n^{ab,1}-\frac{p-n}{2}M_n^{ab,0}. \tag{2}
\]
Then the original quadratic-rank recurrence contracts EXACTLY over the rational coefficient ring to
\[
\boxed{(p-2n)Y_n^{ab}-(p-2n-1)Y_{n+1}^{ab}=S_n^{ab}.} \tag{3}
\]
Proof: C_n=(p-2n)(p-n)/2 cancels the left mass, and
\[
A_n(p-n-1)/2+B_n=(3m-n)(6m-n)-18m^2+9mn-n^2=0
\]
cancels the right mass. All actual J and E terms remain untouched.

Let rho_n=(p-2n)/(p-2n-1), sigma_n=1/(p-2n-1). By induction, for n_*<=v<=2m,
\[
\boxed{Y_v=\left(\prod_{k=n_*}^{v-1}\rho_k\right)Y_{n_*}
-\sum_{h=n_*}^{v-1}\sigma_h
\left(\prod_{k=h+1}^{v-1}\rho_k\right)S_h.} \tag{4}
\]
For every target prime p=6m+1 all denominators are p-units in this entire finite interval: p-2n-1 cannot be zero mod p for n in [1-2m,2m-1]. This is the exact finite-domain Green propagator, valid modulo any p^r without dividing by p.

## Theorem B: precisely one retained p-adic digit across n=0

The diagonal edge obeys
\[
\boxed{Y_1=(pY_0-S_0)/(p-1),\quad
Y_1\equiv S_0\pmod p,\quad
Y_1\equiv S_0+p(S_0-Y_0)\pmod{p^2}.} \tag{5}
\]
In (4) for v>=1 the coefficients of the initial negative left trace and all sources h<0 contain exactly one factor p; every positive/diagonal source coefficient 0<=h<v is a p-unit. Proof: among the forward rho factors, the UNIQUE nonunit is rho_0=p/(p-1); all sigma and all other rho factors are units. Therefore the negative-orientation influence on positive-oriented Y loses exactly one p-adic digit, not all p-adic information. This is a statement about sensitivity with source streams formally held fixed: the actual constrained hypergeometric streams have algebraic correlations.

## Theorem C: oriented endpoint Ward identity and sharpness

The right endpoint has no cell at n=2m, hence Y_{2m}=0. Put
\[
D_h=\frac1{p-2h-1}\prod_{k=h+1}^{2m-1}\frac{p-2k}{p-2k-1},
\quad
P=\prod_{k=n_*}^{2m-1}\frac{p-2k}{p-2k-1}. \tag{6}
\]
Then the following identity holds EXACTLY:
\[
\boxed{\sum_{h=0}^{2m-1}D_h S_h
=P Y_{n_*}-\sum_{h=n_*}^{-1}D_h S_h.} \tag{7}
\]
At target primes, v_p(P)=1; v_p(D_h)=1 for h<0 and v_p(D_h)=0 for h>=0. Therefore the positive oriented source flux vanishes mod p, equivalently
\[
\boxed{\sum_{h=0}^{2m-1}\frac{S_h}{2h+1}
\prod_{k=h+1}^{2m-1}\frac{2k}{2k+1}\equiv0\pmod p.} \tag{8}
\]
All denominators here are units. Furthermore, after proving integrality first, the exact next-digit identity is
\[
\boxed{\frac1p\sum_{h=0}^{2m-1}D_hS_h
=\frac PpY_{n_*}-\sum_{h=n_*}^{-1}\frac{D_h}p S_h.} \tag{9}
\]
This keeps **both oriented cutoff faces, the n=0 injection and all actual three Hasse source channels**. It is a one-digit signed orientation bridge, not the separate original scalar signed reflection Q_p/p²; the latter has 2^n(1-6n) weights and its own infinity port, so the two observers may not be silently identified.

## Precise author verification / nonzero source residue

Companion standard-library checker generates exact corrected Hasse jets from the finite rank recurrence, independently reproduces them from truncated Pochhammer products for m<=5, computes real J+E with finite endpoints, proves arithmetic equalities (3),(4),(7) by exact Fraction evaluation and checks (5),(8),(9) in the p-local ring. Actual run: **1,953 counted exact assertions across m=1,...,12, all PASS** (the composite p=25,49,55 appear only in rational checks). Jet-generator cross-equalities are additional checks not included in this count. These are AUTHOR checks, not independent peer review.

At p=13 (m=2), (Y_0,S_0,Y_1) modulo 169 is (41,125,34) for (0,2), (6,70,57) for (1,2), and (20,136,123) for (0,3); each checks (5). Most importantly the exact positive source flux in (7) divided by 13 is **8, 11, 2 modulo 13**, in those channels. Thus the first-digit vanishing is sharp within the genuine constrained corrected-Clausen family; there is no unwarranted p² cancellation.

## BRC, source separation, recovery

BRC **COMPOSE_APPLIED**: the carrier keeps ordered labels (j,ell), orientation n=ell-j, signed coefficients, Hasse channel, p-local valuation and two finite source ports. The Y observer is adequate for this specific first-order transfer, not for unrestricted future quadratic-rank operations; the predecessor's second-rank moments and full binomial-fibre recovery still matter. Auxiliary Laurent and Hasse variables are external algebra, **not a native P000 X6 two-dimensional plane or physical Frobenius derivation**. P000 unchanged.

**Next smallest exact unit:** compare the nonzero second-digit oriented source Green term against the original separately tagged T02, U02, T12, T03 and infinity ports with the complete corrected coupled Hasse operator; derive a genuine WZ/adjoint cancellation or a certified nonzero obstructing residue. Independently obtain real original-class CM H0/B0, divided power [X]U mod p², semilinear Frobenius direction/eta, kappa and Delta_p-R_p bridge and independent review. Native CM NOT_RUN. D25/LIFT/JT2 parent remains OPEN.

Own ordinary Research logical conversation: chatgpt-research-hourly-enterprise-math-20260923; distinct from maintenance chatgpt-hourly-enterprise-math-20260921. No new winning CLAIM/OPEN/native publish_checkpoint/Result/review is asserted here. Historical neutral staging is not predecessor completed research. Existing actual controller support path: awdawmip/enterprise-math Issue #1558. Frozen science Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 remains unchanged.
