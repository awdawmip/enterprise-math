# Independent review of the original-coordinate CM24 open-disc estimate

Disposition: PAPER_PASS for the fixed connection and the exact all-degree estimates in the 9897-byte frozen paper. No must-fix was found. This is a genuine nonauthor, directed NONBLIND paper review, not a Native scientific review record, Task acceptance, execution authorization, geometric Frobenius construction, or parent closure.

Reviewer: EM-DVR-BFF6DC, own session MCP-47562f9f432d4978a7bea0dd60ecc4aa, own authority DA-144D0C4639CACEEE75DC. The author is EM-DIRECT-88303D. The principal input is CM24_ORIGINAL_OPEN_UNIT_DISC_LOG_COEFFICIENT_BOUND.md, 9897 bytes, SHA256 cfa8974bd1b9c077cdf7210428276b6bb2af707d1de853b91d8180a9387ba26b, Git blob f76cb368f9debdbe217c7027e270d60eb17b9bd3. Its THEOREM_INTERFACE and AUTHOR_FREEZE were read. This new author paper is a local frozen input at review time; I do not invent a Source commit for it.

I had no CM24 author, construction, or support contribution before this intake and supplied none during the audit. Root supplied the frozen object, candidate bounds, dependency locators and an adversarial checklist. EM-PERFECT-9821E2's conditional triangular-transfer support is author-side contribution, explicitly disclosed by the paper, and supplies no independent vote. I read the exact prior papers and their existing reviews, so this is not a blind audit. Prior unrelated P11 and Parity reviews by this Driver are separate. No paper repair, scientific program, numerical experiment, symbolic expansion, coefficient search, new scientific helper, literature search or Native scientific ticket was used. Text extraction and custody hashing are administrative operations only.

## Exact dependency consumption

I personally made fresh managed GitHub full-file calls, preserved their complete responses, checked their UTF-8 bytes and Git blob identities, and decoded each bundle member with its declared byte count, SHA256 and Git blob. The consumed immutable bundles are:

- Source 86b44cfcfe0d448599c3dbb6490bd3df8cd73c58, research_notes/owner_goal_20261015/CM24_LOCAL_ANALYTIC_REVIEWED_BUNDLE.json, SHA256 52939d269f9a60ddbd3494133da96577879308de5de854eb27d04a7ae3864d2a, blob 685d000cc3451e56e65b84bd09ae6ff665680376. All six members were read, including the complete 13899-byte analytic proof, its review, interface and required applicability addendum.
- Source 3981c60496c24a3c1567677726c136966522d8bf, research_notes/CM24_LOG_RESIDUE_GRADES_REVIEWED_20261015.json, SHA256 344261810f30a898fe12e664acce79142973d998b48400ee7823c13f05b6c4cc, blob 02a2cd1ad6228d98e7275babdd289fcf445663d8. All seven members have custody verification. I read the full 13743-byte formal proof, next lemma, direction freeze, proposed patch and the prior full review; its manifest/full-pin metadata were retained for provenance.
- The same Source, research_notes/CM24_RELATIVE_EXTENSION_REVIEWED_20261015_FBF223.json, blob c8c13a14239308110e171eb063772ac184018b7f. All four members have custody verification. I read the full corrected 17493-byte V2 primary, especially its actual proper matrix, exact source polynomial, whole triangular carrier, solution-transport convention and limitations. The previous review is prior evidence, not a substitute for this audit.
- The same Source, research_notes/CM24_KUMMER_KERNEL_REVIEWED_20261015.json, blob 377f659890b7efd9876fa4d5c00cf1665cf2caeb. This exact additional dependency was opened to resolve the selected integral H_b lift. Its full 14956-byte primary was read; the other members are retained as provenance, without reopening their old verdicts.

The formal proof member has SHA256 e17688c59f6d59f4611cbcd0bb518483fa381b2526d3ee82bec3dd61eb75cf5c. The V2 primary has SHA256 a7d92b1f1af9defd1674e379dadab796ee82a40a808ca1cdb63187e35f27d780. These are the actual original systems, not merely a new proposal's description of them. No old accepted Hesse-P3, formal-classification, ad_R^4 or smaller-disc unit is reopened or rerun.

## 1. Allowed primes, source lift and complete carrier

The actual primes are all primes congruent to 13 or 19 modulo 24, hence p>=13. Consequently 2, 3, 5, 6, 9 and 12 are p-units. The chosen coefficient ring is the fixed unramified complete DVR O, with K=O[1/p] and v(p)=1. The minimum-entry valuation and isometric coefficient Witt map are the same as in the old analytic theorem.

The Kummer primary fixes N=(p-1)/2, an integral lift g, sigma0=1-2g exactly, and H_b(x)=g(1+x^N)+(4sigma0/5)x+(sigma0/5)x^(N-1). Thus H_b is genuinely an O-polynomial, H_b(1)=1 exactly, and no inverse of N, of a source value, or of sigma0 is required. The exponent N-1 is nonnegative throughout the actual prime range. This includes sigma0=0. Nothing in the new proof replaces this polynomial by a fitted forcing term or a mod-p-only horizontal source section.

At t=r-1 the proper residue is Rp=(1/12)[[-1,-1],[1,1]], while w has residue -2, rho_-1=(-2,0), and beta_-1=2. The regular coefficients are integral: the only other proper denominators at this centre have p-unit constant terms, and the remaining w denominator is t+2 after removal of its simple pole. Multiplication by the integral polynomial H_b preserves this fact. The correct constant proper change P=[[12,-1],[0,1]] and its inverse are integral; T=diag(P,1,1) sends the original residue to the old hatted residue. Both the proper coupling and the baseline survive. This verifies the exact input, rather than assuming that an arbitrary integral regular-singular system has unit-disc convergence.

## 2. Scalar equation and the logarithmic companion

The elimination is reversible: y2=-6(s^2-1)y1'-(2s-1)y1, with the prime here meaning d/ds. For the original proper matrix, beta'/beta=-2s/(s^2-1) and alpha'-(beta'/beta)alpha+alpha^2+beta gamma=-2/[9(s^2-1)]. These give precisely (1-s^2)y1''-2s y1'-(2/9)y1=0, including the sign of the last term. The substitution z=(1-s)/2 yields z(1-z)h''+(1-2z)h'-(2/9)h=0.

The claimed balanced coefficients obey (n+1)^2 f_(n+1)=(n+1/3)(n+2/3)f_n and f0=1. For h_n equal to the paper's harmonic difference, its increment is 1/(n+1/3)+1/(n+2/3)-2/(n+1). Multiplying this increment by (n+1/3)(n+2/3)f_n gives exactly (2n+1)f_n-2(n+1)f_(n+1). This verifies the inhomogeneous recurrence for g_n=f_n h_n at every n, including n=0. In particular g0=0 and g1=5/9; the companion has the stated positive sign. Direct differentiation also gives L(f log z)=2(1-z)f'-f, so f log z+g is a solution. No named hypergeometric theorem replaces this recurrence check.

For a,b in Z_p, the continuous integer-valued binomial polynomial proves (a)_n/n! and (b)_n/n! integral. Here a=1/3,b=2/3, so f_n is integral for every n. Each reciprocal in h_n has denominator, up to a p-unit, among 3j+1, 3j+2, j+1, all positive integers at most 3n. The nonarchimedean sum inequality therefore gives v(g_n)>=-floor(log_p(3n)) for n>=1 without any cancellation assumption. This is an all-n estimate at every allowed prime; no sample or finite truncation enters.

## 3. Original proper frame, formal logarithm and normalization

The column J(h)=(h,-12z(1-z)h'-(1-4z)h)^T is exactly the original second-coordinate reconstruction after the z substitution. For the companion, J(f log z+g)=J(f)log z+E with E=J(g)-(0,12(1-z)f)^T. This keeps the derivative-of-log term and its sign.

The exact original-coordinate identity is z(t)=-(1/2)t(3+2t)^2=kappa t u(t), kappa=-9/2, u=(1+2t/3)^2. The formal series lambda=log u has constant zero and the paper's coefficients. Choosing the formal symbol log z to be log t+lambda is legitimate because its derivative is z'/z. There is no need to assign a p-adic value to log(kappa). A different constant would only change a companion by a constant multiple of the first solution; the chosen normalized matrix fixes that freedom.

With B=[E+lambda J(f),J(f)], its constant is C=[[0,1],[-12,-1]], det C=12, and direct multiplication gives Rp C=C E21. The first column of B t^(E21) is exactly the companion and its second column is the regular solution. Hence G=B C^-1 satisfies G0=I and G'=A_t G-G Rp/t in the ORIGINAL proper basis. Formal uniqueness from the fixed nilpotent-residue recursion identifies it with the required proper gauge; this is not merely some fundamental matrix in another basis.

Trace A_t=trace Rp=0 implies (det G)'=0 and det G=1. Because this is a two-by-two matrix, G^-1=adj(G), whose entries are signed entries of G. No reciprocal of f or unproved reciprocal-series convergence is used.

All coefficients of z(t) are integral and z(0)=0, so a degree-n composition uses only indices j<=n. The factor z in z(1-z)g' cancels the degree shift and leaves j g_j times integral polynomials; no new denominator appears. J(f) and (1-z)f are integral. Also v(lambda_n)>=-log_p n, and the finite convolution with J(f) retains that lower bound at degree n. Since C and C^-1 are integral, both G_n and (G^-1)_n have valuation at least -log_p(3(n+1)), also at n=0. This verifies output PROPER-002, including the inverse and normalization.

## 4. Full row recurrence and all-degree bounds

In the original 2+1+1 basis, H=[[G,0,0],[0,1,0],[u,v,1]] has u0=v0=0. Multiplication of the full matrices gives u'+u Rp/t=rho G-rho_-1/t and v'=beta-beta_-1/t. The pole cancels because G0=I. At every n>=1 the regular coefficient is exactly

    Q_(n-1)=rho_-1 G_n+sum_(j=0)^(n-1)rho_j G_(n-1-j).

The leading rho_-1 G_n term cannot be omitted. Coefficient comparison gives the ROW equation u_n(nI+Rp)=Q_(n-1). Since Rp^2=0, u_n=Q_(n-1)(I/n-Rp/n^2), with multiplication on the right. The beta equation gives v_n=beta_(n-1)/n. These equations also construct the complete normalized gauge and agree with formal uniqueness. The author-side conditional support does not substitute for these checks.

Integrality and the proper estimate give v(Q_(n-1))>=-log_p 3-log_p(n+1). The finite row inverse loses at most 2v_p(n)<=2log_p(n+1). Thus v(u_n)>=-log_p 3-3log_p(n+1), while v(v_n)>=-log_p(n+1). The proper block and constant diagonals satisfy the same H bound, including n=0.

The full inverse is [[G^-1,0,0],[0,1,0],[-uG^-1,-v,1]]. In each degree-n convolution, i+1<=n+1 and n-i+1<=n+1. The sum inequality therefore gives v((uG^-1)_n)>=-2log_p 3-4log_p(n+1). This covers the other blocks as well. Consequently both stated H and U estimates hold for every n>=0. The integral constant change T and its integral inverse preserve these lower bounds in the hatted frame; its normalized gauge is the conjugate, so no original P-frame information is lost.

## 5. Analytic conclusion, comparison, and exact limits

For |t|=p^(-epsilon)<1, the valuation of each coefficient times t^n is bounded below by epsilon n-C-D log_p(n+1), tending to infinity. Completeness yields convergence at every point of the original open unit disc, without any change to t=r-1. Formal inverse identities become analytic inverse identities there. The possible other poles t=-2,-1/2,-3/2 have absolute value one at the allowed primes and do not lie in this domain. This is a substantive improvement over the old factorial majorant and the rescaled smaller disc.

For each fixed permitted constant F0, the coefficient formula is F_n=sum_(a+pb=n) H_a F0 sigma(U_b). The isometry of sigma and a,b<=n give the stronger immediate lower bound v(F0)-3log_p 3-7log_p(n+1). The displayed paper bound v(F0)-4log_p 3-8log_p(n+1) is a valid conservative weakening, including n=0. Thus its comparison also converges throughout the original open unit disc. RF0=pF0R, the selected theta(t)=t^p and the original solution-transport convention remain the relevant comparison hypotheses. No parameter is selected by this estimate.

The accepted outputs are exactly the four THEOREM_INTERFACE claims: matched proper scalar and companion recurrences; normalized proper gauge and adjugate inverse bound; complete H/U logarithmic coefficient bounds; and original open-disc convergence for those gauges and each fixed permitted comparison. A common C_p=2log_p 3,D_p=4 works for H and U. No optimality of these constants is asserted.

Boundary convergence at |t|=1, original-coordinate dagger membership, good-locus gluing, actual proper log-geometric comparison or sign, source-independent xi/eta or other initial-data selection, singular-boundary change of lift, actual full relative realization, source functional, Y/Z/kappa and mathematical parent completion remain unproved. The old obstruction to generic unit-disc inference is respected: the new argument uses this exact scalar equation, not integrality plus nilpotent residue alone. No whole geometric or fixed-P11 certificate conclusion follows.

Method classification is COMPOSE_APPLIED for this bounded domain lemma: exact proper scalar system plus balanced/logarithmic coefficients, normalized gauge, and retained triangular transfer. No new general tool or literature-novelty claim is accepted. The Heartbeat native X6 basis and external arithmetic/module typing are retained; these formal variables are neither native spatial axes nor physical time, and the complete source carrier is preserved.

This bounded independent audit is complete at paper strength. Source publication of the new author and this report, and any subsequent Native scientific operation, are separate actions. Root retains main-write scheduling. All mathematical parents remain OPEN.

Driver-ID: EM-DVR-BFF6DC / CONTROL_PLANE
