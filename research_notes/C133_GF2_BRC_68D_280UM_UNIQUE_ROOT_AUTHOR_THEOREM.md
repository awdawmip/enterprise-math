# C133: Exact rational unique transverse root at 280 microunits — finite GF(2)-BRC auxiliary

Research status: AUTHOR_EXACT_RATIONAL / NOT_DRIVER_REVIEWED / NO_NATIVE_CLAIM / NOT_ADMITTED.
Date: 2026-10-18 Asia/Shanghai.
Verified global rule snapshot: awdawmip/chatgpt-global-knowledge at e2c99e7eeea5f67b9014b350fff8f8b35fe38d4c.
Verified EM control snapshot: awdawmip/enterprise-math at 341ea3fb3b06d32b16208d523dd5b7fdf6037f39.
Scientific inputs: frozen C102 original finite positive-weight GF(2) ensemble; C125 complete hidden-charge enumerator; C127 17-visible-face port tensor; C132 face-deleted positive-mass derivative technique. The historical original source pins are retained and are not overridden by the current control snapshot.

## Theorem: precise scope and quantifiers

Fix any of C102's 11 arcs (shared C104 and first/second stages for pairs (1,9), (3,8), (5,9), (6,8), (8,9)). For every t in [0,1] and all 68 independent fixed perturbations z_f, each |z_f| <= delta, consider u in [2/5,99/100] and

\[
\delta=\frac{7}{25000}=0.00028,\qquad
\varepsilon=\frac{28001}{10^8}=0.00028001,\qquad
r_f=\varepsilon+(1-\varepsilon)r^0_f(t,u)+z_f,\quad F=AD-BC.
\]

The z_f are independent parameters, NOT assumed independent GF(2) random characters; they are fixed with respect to both t and u. The A/B/C/D labels and original signed port projections are retained. The original C102 positive branch weights, 48-bit core, and couplings define a polynomial F. All permitted actual couplings belong to (0,1), since epsilon minus delta is exactly 10^(-8) and the max high-u baseline is 99/100.

For every arc, t, z and u, the exact rational certificate proves

\[
\boxed{\partial_u F<-1,\qquad F(t,2/5,z)>30,\qquad F(t,99/100,z)<-15.}
\]

Thus for every fixed arc, t and z, there exists exactly one zero u* in (2/5,99/100), and it is simple/transverse (\partial_uF<-1). This expands the previously author-verified finite-model radius from 0.00027 (C132) by 3.7037037%. There is no implied statement for Enterprise Math's native six-dimensional Cell, its three-dimensional slice, its 120-degree native orthogonality, physical experiments or RH.

## Exact method and new mathematics

The hidden GF(2) charge structure partitions the 68 faces into 17 first-order visible and 51 hidden. The C125 closed-charge kernel is 19-dimensional with 524288 charge-closed subsets. The complete (not cutoff) weight enumerator W(x) gives S=W(rho)-1 at rho=epsilon+delta=56001/10^8. For true unsigned positive source mass Z and direct factor-derivative positive mass L, the all-order 51-hidden determinant derivative error obeys

\[
|\partial_u F-\partial_u F_V|\le 8 L Z S+4 L Z S^2.
\]

Here F_V keeps the 17 visible perturbations, and the hidden variables are zeroed only in the comparison model. No probabilistic independence or information-loss-free identification is assumed. Unsigned source-state mass, labeled signed Fourier port coefficients and determinant must remain distinct; the signed port absolute-coefficient sum can underestimate the required unsigned source mass.

A fresh exact C102 diagnostic at radius 0.00028 constructs 365 derivative rectangles over all 11 arcs, 89 left endpoint slabs and 110 right endpoint slabs with exact closed-domain coverage. Its older sufficient derivative estimate is negative on 353 rectangles; twelve fail that estimate (ten Stage I and two Stage II). These are failures to certify, not derivative sign counterexamples.

For the ten Stage-I rectangles, build all 2^17 visible Fourier masks; recenter their polynomial factors exactly at the appropriate C102 baseline; compute the exact rational 2D Bernstein upper bounds of the baseline derivative and 17 first-order derivatives, including the derivative of epsilon*(1-b_f) for each of the three u-active faces. Bound every order 2 through 17 from the original complete tensor. Improve the 51-hidden derivative bound using the C132 FACE-DELETED-POSITIVE-MASS lemma: differentiate the three u-dependent positive factors before bounding the residual positive mass, to avoid an unnecessary 1/(1-r_max) blow-up. If B0 bounds exact zero-high positive mass by a rational Bernstein inequality and Rrest bounds the remaining statewise positive mass ratios, then

\[
L_{\rm deleted}\le 3(1-\varepsilon)(1+r_{\rm high,max})^2B_0R_{\rm rest}.
\]

All ten resulting full-68-face derivative upper bounds are strictly negative. The weakest repaired upper is approximately -382.043090357 at (8,9) Stage I, t in [31/32,1] and u in [733/800,99/100]. The alternative author-side implementation recomputes all ten source unsigned masses and 1D Bernstein extrema directly from original C102 terms.

**New C133-specific Stage-II repair:** (1,9) Stage II t in [0,1/8], u in [337/400,99/100]. Recenter the complete 17-dimensional visible Fourier tensor at its own Stage-II baseline: six medium faces at 9/10, high faces 4 and 42 at u(1-t), high face 90 at u, other visible baselines at zero. For each high-face monomial, expand u^m(1-t)^h exactly by binomial coefficients; this produces four integer port tensors with common denominator 10^6. Their zero-perturbation four-port polynomials are proved identical to the original C102/C115 baseline moments. Exact bivariate Bernstein calculation bounds the derivative of A0D0-B0C0. The visible 17-variable Taylor remainder includes **every order from 2 through 17**, and the C125 complete 51-hidden charge spectrum controls the remaining derivative.

The exact rational upper bound components (decimals for display only) are:

| Component | Upper-bound contribution |
| --- | ---: |
| Baseline Bernstein maximum | -1770.681779862... |
| All first-order visible faces | < 19.835523 |
| Visible regularization derivative | < 0.737183 |
| All orders 2..17 visible remainder | < 26.743227 |
| Full 51-hidden derivative transfer | < 9.032643 |
| **Final full-68-face derivative bound** | **-1714.333206176... < -1714** |

A separate source implementation reconstructs the four baseline moments directly from original C102 GF(2) terms, computes their bivariate Bernstein bounds by a different rational algorithm, checks unsigned source mass and the final exact fraction. This is author-side cross-reproduction, NOT independent mathematical Driver review. The remaining (5,9) Stage-II difficult derivative rectangle obtains approximately -2113.71099 by the inherited exact full-order 17-visible and 51-hidden control.

The 89 original left endpoint intervals remain strictly positive. At the right endpoint, 93 original intervals remain strictly negative; the remaining 17, all on (5,9) Stage II upper t-quarter, are replaced by 64 consecutive exact rational Bernstein subslabs over t in [3/4,1], all with F upper <-56. The source checker verifies all 365 derivative rectangles cover the full t-u domain, as do all endpoint slabs, including joining boundaries. The exact all-stage smallest margins are approximately:

- derivative negative margin > 1.842479784;
- left endpoint positive margin > 30.415375245;
- right endpoint negative margin > 15.237283095.

All logical decisions are made by exact rational fractions, not decimals. Continuity and IVT give a root, the strict derivative bound yields uniqueness and transverse simplicity.

## Evidence and bounded conclusions

The author proof is reproduced by scripts c133_diagnostic_280um.py, c133_stageI_280um.py, c133_stageII_280um.py, c133_stageII_visible_pair19.py, c133_endpoint_280um.py, c133_independent_source_verify.py, c133_face_deleted_mass_independent.py, c133_pair19_independent_source_check.py, c133_integrate_full.py. Corresponding JSON certificates are C133_DIAGNOSTIC_280UM_EXACT_CERTIFICATE.json, C133_STAGE_I_280UM_EXACT_CERTIFICATE.json, C133_STAGE_II_280UM_EXACT_CERTIFICATE.json, C133_PAIR19_STAGEII_280UM_EXACT_CERTIFICATE.json, C133_RIGHT_FULL_QUARTER_FIRSTORDER_CERTIFICATE.json, C133_INDEPENDENT_SOURCE_CROSSCHECK.json, C133_FACE_DELETED_MASS_INDEPENDENT_CERTIFICATE.json, C133_PAIR19_STAGEII_INDEPENDENT_RECHECK.json, C133_INTEGRATED_EXACT_CERTIFICATE.json, plus diagnostic summary. These witnesses form a portable ZIP that also embeds the unchanged C132/C131/C130 prior scientific input chain and its SHA256 manifest. A separate clean directory ran all nine C133 scripts and reproduced ten JSON outputs byte-for-byte, with result C133_CLEAN_SOURCE_REPLAY_11_ARCS_68D_280UM_EXACT_RATIONAL_PASS.

The author proof does not assert independent Driver verification, Lean checking, formal Result acceptance, canonical Source task ownership, truth in the native X6 Cell, or all-scale uniformity. The unresolved foundational bridge is a typed six-dimensional-to-GF(2)-BRC observer and update correspondence preserving all labeled four ports and the future-relevant residual fiber.

**Next scientific unit C134:** test delta=29/100000 with epsilon=29001/10^8, diagnose all original exact derivative and endpoint margins, repair only first-failing local boxes and do not mislabel a sufficient-bound failure as a counterexample.

GitHub storage on an unmerged author branch does NOT itself confer CLA​​IM, an operational Result record, independent review, or theorem admission; those remain under the project control protocol.