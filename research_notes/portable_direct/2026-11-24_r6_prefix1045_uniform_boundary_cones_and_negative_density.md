# PREFIX-1045 — Uniform boundary cones and the asymptotic density of negative Hausdorff differences

Date: 2026-11-24 (Asia/Shanghai). Parent: PREFIX-1044. Status: AUTHOR_CONDITIONAL_ANALYTIC_PROOF / HUMAN_RECHECKABLE / NOT_REVIEWED.

## Scope and fixed sources

P000 V5 remains pinned to enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json. Retain Stage46 signed BRC W=J12−6I12, initial incoming −e1, both exclusions of Link {0,e1}, exactly one outgoing negative step, and the full X6 Cell–terminal-port–grade observer with signs, provenance, multiplicity and residual. This is a theorem about the existing derived scalar spectral observer only; NATIVE_ATTRIBUTION_PENDING_BRC_REVALIDATION. No new classical reference run, phase evaluation, native propagation or numerical spectral evaluation was performed.

Sources actually read at immutable commits:
- PREFIX-1035, ebccbb436685bafe6d697ace256ad93b39c0c50f:research_notes/portable_direct/2026-11-23_r6_prefix1035_six_phase_picard_fuchs_frobenius.md (blob c44fdf1731a40aa7a81886020d69f23f4fa8c227): rational fifth-order ODE for rho, top coefficient −y^5(y−4)(y−16)(y−36), and the formula for g with F'=(y−6)rho.
- PREFIX-1037, 928461a6f8c675b9a7bd38586cf47db9d25835e9:research_notes/portable_direct/2026-11-23_r6_prefix1037_certified_critical_density_positivity.md (blob d82908705601e96ff4966fc8299ab53ca817addc): g(4)>0 and g(16)>0.
- PREFIX-1044, 8d29f3214a82ed34830beb11b8f64478bfccfa2c:research_notes/portable_direct/2026-11-24_r6_prefix1044_exact_edge_density_and_beta_rays.md (blob 30cf85284ac7136494b9dd930e89c62b7a5b4bdd): continuous g, positive edge asymptotics and normalized Beta identity.

For m,k nonnegative integers put n=m+k+1, j=m+1, T~Beta(m+1,k+1), Y=36T. Define E_{m,k}=integral_0^36 y^m(36−y)^k g(y)dy and D_{m,k}=n binom(n−1,m) E_{m,k}/36^n=E[g(Y)]. They have the same sign. Let a>0,b>0 denote the exact leading constants from PREFIX-1044, namely a=35/(12 pi^3) and b=3024 rho(0)/5, carried symbolically without evaluating pi or rho. The source proves g(36−u)=a u^(5/2)+O(u^(7/2)) and g(y)=b y+O(y^(3/2)). Global continuity extends these to finite uniform bounds on [0,36]:
|g(y)−a(36−y)^(5/2)| <= C_R(36−y)^(7/2),
|g(y)−b y| <= C_L y^(3/2).
The two nonnegative constants C_R,C_L need not be known numerically for the following theorem. Explicit choices remain an open certification problem.

## Theorem 1 — uniform relative error, including growing minority indices

For ALL nonnegative m,k,
|D_{m,k}/(a 36^(5/2) E[(1−T)^(5/2)])−1|
 <= (36 C_R/a)(k+7/2)/(m+k+9/2);
|D_{m,k}/(36 b E[T])−1|
 <= (6 C_L/b) sqrt((m+2)/(m+k+3)).

Proof. Divide the right-edge uniform remainder estimate by its positive leading Beta moment. The ratio of consecutive fractional moments is exact:
E[(1−T)^(7/2)]/E[(1−T)^(5/2)]
 = (k+1+5/2)/(m+k+2+5/2).
The extra scale is 36. On the left, tilt the original Beta law by T/E[T]. This is exactly Beta(m+2,k+1), with mean (m+2)/(m+k+3). Hence
E[T^(3/2)]/E[T]=E_tilt[sqrt(T)] <= sqrt((m+2)/(m+k+3))
by concavity, and the extra scale is sqrt(36)=6. Divide by the positive leading term. QED.

In particular, for any sequence with n→infinity and k/n→0 the right-edge relative error tends to zero, with NO fixed-k hypothesis. For any sequence with m/n→0 the left-edge relative error tends to zero, with NO fixed-m hypothesis. These include both minority indices tending to infinity, e.g. k=floor(sqrt(m)) or m=floor(sqrt(k)), and even minority fraction decaying arbitrarily slowly. Moreover there exist fixed-width endpoint cones: for any 0<eta_R,eta_L<1 chosen to satisfy (36 C_R/a) eta_R<1 and (6 C_L/b)sqrt(eta_L)<1, the exact inequalities
(k+7/2)/(n+7/2) <= eta_R
or (m+2)/(n+2) <= eta_L
imply D_{m,k}>0. If the corresponding C is zero, any eta in (0,1) works. This replaces PREFIX-1044's countably many fixed-index existence thresholds by a single uniform two-parameter criterion. Its width is existence-level until C_R,C_L are certified. For fixed small positive thresholds, sufficiently large n yields positivity uniformly for all lattice mean coordinates in a neighborhood of either endpoint (the ratios above differ from the corresponding mean fractions by O(1/n)).

## Theorem 2 — finite zero set of the inherited scalar g

The set Z={y in (0,36): g(y)=0} is finite, with each zero of finite order. All zeros lie a positive distance from {0,4,16,36}.

Proof. The regular fifth-order linear ODE of PREFIX-1035, with analytic rational coefficients wherever its top coefficient is nonzero, makes rho analytic on each of (0,4),(4,16),(16,36). Equivalently the associated first-order system has analytic coefficients there; F'=(y−6)rho gives analytic F. The inherited g formula is a linear combination with polynomial coefficients of rho,rho',F, hence analytic on each band. The positive edge asymptotics give open positive one-sided endpoint neighborhoods, and the positive values at 4,16 with continuity give open positive two-sided neighborhoods. Each band therefore contains nonzero values, and all its zeros are confined to a compact subset of that band. A nonzero real analytic function has isolated finite-order zeros, and an infinite set in such a compact subset would have an interior accumulation point. QED.

Consequently the negative set G_-={y:g(y)<0} is a finite union of disjoint open intervals strictly inside the three regular bands (possibly empty). The endpoints are zeros. This conclusion uses inherited point and edge positivity, not a numerical scan.

## Theorem 3 — negative coefficient density and localization

On degree n−1 define N_n=#{j=1,...,n: D_{j−1,n−j}<0}, and let L be the total ordinary length of G_-. Then
lim_{n→infinity} N_n/n = L/36.
More sharply, if Z is nonempty and r_* is the maximum finite zero multiplicity, then
N_n = n L/36 + O(1+n^(1−1/r_*)).
If all zeros are simple, the count error is O(1). The same asymptotic holds with <=0 in place of <0. If Z is empty then N_n=0 for every n. No actual zeros or negative interval are asserted here.

Proof. Write x_j=E[Y]=36 j/(n+1). The variance is 36^2 j(n−j+1)/((n+1)^2(n+2)) <= 324/(n+2). Since g is continuous on a compact interval, D_{j−1,n−j}−g(x_j)→0 uniformly: for each delta>0 its absolute value is at most omega_g(delta)+2||g||_infty 324/((n+2)delta^2). This controls signs on any compact region separated from zeros and endpoints, including neighborhoods of 4 and 16. Theorem 1 handles endpoint neighborhoods uniformly for sufficiently large n, even where g vanishes at the endpoint itself. Thus all possible sign mismatches for large n are restricted to fixed compact regular neighborhoods of Z.

For the quantitative claim choose small closed neighborhoods of the finitely many zeros lying strictly inside regular bands. For x in their union and any y in [0,36], a single finite constant C satisfies
|g(y)−g(x)−g'(x)(y−x)| <= C |y−x|^2.
Indeed for |y−x|<delta where a slightly enlarged regular neighborhood is valid, Taylor's theorem uses a uniform bound on |g''|. Otherwise continuity and bounded g,g' give a bound on the ratio by (2||g||_infty+36 sup|g'|)/delta^2. Taking expectation at x=x_j cancels the linear term exactly. Therefore |D−g(x_j)| <= 324 C/(n+2) in those neighborhoods. At zero z of order r, the local analytic expansion gives |g(x)| >= c_z |x−z|^r for some c_z>0 in a sufficiently small neighborhood. A mismatch, including a zero coefficient, is possible only within distance (324 C/((n+2)c_z))^(1/r) of z. The lattice spacing is 36/(n+1); the number of such lattice points is O(1+n^(1−1/r)). Sum over finitely many roots. Since the count of lattice means in each open negative interval differs from (n+1) times its length divided by 36 by at most 2, replacing n+1 with n costs O(1). This proves the formula. When Z is empty, each band and the endpoint neighborhoods are positive, so the integral against any positive Beta weight is strictly positive. QED.

## Corollary — exact global alternative

The following are equivalent under the inherited scalar assumptions:
(i) g(y)>=0 throughout [0,36];
(ii) every E_{m,k}>0;
(iii) N_n/n→0;
(iv) all sufficiently high degrees have no negative coefficient.

(i) implies (ii) because g is strictly positive on an open subinterval and each Beta density is positive in the interior. (ii) implies (iv) implies (iii). (iii) implies (i) by Theorem 3 and continuity (a strict negative value would have an open negative interval of positive length).

In particular, ANY single nonpositive E_{m,k} forces a genuine negative interval and a positive asymptotic density of strictly negative coefficients on every sufficiently large degree. Conversely a single certified negative spectral interval of length ell forces liminf N_n/n >= ell/36. A counterexample cannot remain isolated at a high index or be hidden permanently in a sparse exceptional ray. This is a structural discrimination result, not a claim that a counterexample exists.

## Validation and next action

Proof consists of exact Beta identities, a concavity estimate, analytic ODE regularity, and compactness plus Taylor's theorem. All quantifiers and exponents have been rechecked in the argument above. No computational proof or external comparison was run; no formal Result or independent review is claimed. The source formulas were read back as listed. Theorem 2 uses the inherited analytic ODE and point/edge signs; Theorem 1 uses only the inherited edge expansions and continuity. Theorem 3 uses both plus the Beta identity.

The central decision has changed from isolated giant integer thresholds to determining the finite regular-band negative intervals or proving their absence. Next: use the six-component rational ODE from PREFIX-1035 to obtain rigorous local bounds or analytic sign certificates on the remaining regular bands; any zero must be inside them. Effective C_R,C_L would convert the endpoint cones to numerical widths but are not needed for the qualitative finite-zero and density results. Continue separate native X6–signed BRC observer equivalence; the mother question B_fix,odd(32) in {19,20} stays open.

Historical source attribution EM-DIRECT-780BBE / RA-0ABD84561C86E53067DB0322. Current account recovery returned the same own SID pointer with no runs or execution authority. The previous scoped LEASED read r6-20261124-0257-current-leased-owner-read-v1 completed SUCCEEDED, empty LEASED selection as of 2026-11-23T19:05:03Z. A fresh scoped read r6-20261124-0346-leased-observe-v1 was submitted; at last observation it was RUNNING. Independent portable note; no CLAIM, PROGRESS or protected record change.
