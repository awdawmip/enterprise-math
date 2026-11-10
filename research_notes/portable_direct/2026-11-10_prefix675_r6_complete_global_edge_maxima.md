# PREFIX-675-R6 — Exact global classification of frozen BRC boundary maxima

Date: 2026-11-10 (Asia/Shanghai). Mode: independent portable TASK_RESEARCH. Researcher-ID EM-DIRECT-9F3462; Research-Activity-ID RA-59D34738FA9229BDC58D7E47.

Scientific input frozen at f42f2906d77f24085c123f3ccfe9667d41caa96d. Status: AUTHOR_DERIVED / EXACT_INTEGER_BERNSTEIN_CHECKED / UNREVIEWED / NOT_ADMITTED.

## Question and statement

The mother problem asks for the full [0,1]^2 global maximum of the frozen BRC 189-survivor-layer, two-informative-direction, first-stop statistical observer variance. Its p,z are observer probabilities within Heartbeat World X6, not new spatial axes or a native plane. The signed-path multiplicities and Gamma-clock observation remain unchanged.

For independent Poissonized clocks Y_p,Y_z define Y(p,z)=max(Y_p,Y_z), mu=E[Y], H=E[Y^2]/2, W=2H-mu^2 and V_q=q^2 W-q mu.

**Theorem 675.1 (full boundary).** For every real q in [12,24], a unique z_*(q) in the open interval I=(607/4096,609/4096) maximizes z↦V_q(0,z) over [0,1/2]. The function is strictly increasing on [0,z_*(q)], strictly decreasing on [z_*(q),1/2], and symmetric about z=1/2 on [0,1]. Its exact maximizer set on the entire edge p=0 is precisely {z_*(q),1-z_*(q)}. In particular, there are no other boundary maximizers for either practical scheme q=12 or q=24.

**Theorem 675.2 (exact executable certificate).** Let S=2^216 and P_q(z)=S^2 V_q(0,z). At q=12 and q=24, the integer polynomial P_q' has degree 375 and admits exact division
P_q'(z)=(1-2z)D_q(z), deg(D_q)=374,
with zero remainder. The Bernstein coefficients of D_q on the seven dyadic cells covering [0,607/4096] are all strictly positive, and on the eight dyadic cells covering [609/4096,1/2] are all strictly negative. The Bernstein coefficients of P_q'' on both cells [607/4096,608/4096] and [608/4096,609/4096] are all strictly negative. Further exact integer evaluations show P_q'(607/4096)>0 and P_q'(609/4096)<0.

The complete 15-cell sign cover for each q is listed in the machine output of PREFIX675_R6_COMPACT_CERTIFICATE.py and summarized in PREFIX675_R6_RESULTS.json. The two central cells form exactly the interval I. No finite floating-point sampling is used as a universal sign inference.

## Frozen model and proof

For original signed-path survivor counts A_m(k), put s_m(z)=Σ_{k=0}^m A_m(k)z^k(1-z)^(m-k). The frozen original recurrence has all paths surviving through level 24, loses both same-sign paths at level 25, and is extinct at level 189. Hence at p=0, Y_0 is Gamma(shape 25,rate 1).

Set w(n,m)=binom(n+m,n)/2^(n+m+1),
a_m=1−Σ_{n=0}^{24}w(n,m),
b_m=(m+1)−(1/2)Σ_{n=0}^{24}(n+m+1)w(n,m).
The exact independent-clock maximum moment kernel gives
mu(0,z)=25+Σ_{m=0}^{188} a_m s_m(z),
H(0,z)=325+Σ_{m=0}^{188} b_m s_m(z).
All S a_m and S b_m are integers. With integer polynomial M=S mu, K=S H,
P_q=2q² S K−q S M−q² M².
The companion script rebuilds the frozen rows and constructs these integer polynomials directly; no predecessor numerical table is used.

The count symmetry A_m(k)=A_m(m−k) is verified for all m,k, so s_m(z)=s_m(1−z), P_q(z)=P_q(1−z), and P_q'(1/2)=0. Integer polynomial division gives P_q'(z)=(1−2z)D_q(z) exactly. Factoring is essential: P_q'(1/2)=0, whereas D_q(1/2)<0. Repeated strict-sign subdivision of P_q' alone would retain a zero endpoint and fail to terminate.

For an integer polynomial f(z)=Σ_{k=0}^d c_k z^k, let its degree-d Bernstein coefficients on [0,1] be B_j. Then the identity
d! B_j=Σ_{k=0}^j c_k j!/(j−k)! (d−k)!
makes every coefficient comparison exact in integers. The dyadic de Casteljau restrictions use only additions and positive integer powers of two to clear denominators. The Bernstein basis is nonnegative and sums to one, so uniformly strictly positive or negative coefficients certify the polynomial's strict sign throughout the closed interval. The program checks a gapless cover of seven positive and eight negative dyadic cells for each q, plus strict negative curvature on the central two cells and strict boundary derivative signs.

For z in [0,1/2), (1−2z)>0, and therefore P_q' and D_q have the same sign. Exact curvature in I and opposite endpoint signs yield a unique stationary maximum z_*(q) for q=12,24; the outside cells rule out all other stationary maxima in [0,1/2).

For arbitrary real q in [12,24], V_q'(0,z)/q=q W_z(0,z)−mu_z(0,z) is affine in q. Its strict signs at q=12 and q=24 propagate to every q between them at each real z outside I. The same affine argument for V_q''(0,z)/q=q W_zz−mu_zz propagates strict negative curvature throughout I, and the endpoint signs also persist. Thus every real q has the exact same monotonicity structure and a unique z_*(q). Reflection gives precisely the two full-edge maximizers. QED.

## Execution, evidence and scope

Executable Python: PREFIX675_R6_COMPACT_CERTIFICATE.py. Outputs: PREFIX675_R6_RESULTS.json. The program uses only Python standard-library arbitrary-precision integers, Fraction and factorial/binomial coefficients. Local run returned ALL_CHECKS_PASS 12, additionally covering 30 strict Bernstein-sign cells, four strict-concavity cells, zero reflection remainder, exact path-count symmetry, survivor extinction and gapless interval coverage. The analysis uses the exact statistical observer specified by frozen pin, not an original physical X6 dynamics rerun.

The prior PREFIX-660 rational brackets for max V_12(0,z)≈86048.10654843 and max V_24(0,z)≈346340.56783942 can now be read as complete-edge (p=0) maxima rather than merely maxima on the small band I. This is an author derivation and exact computational certificate pending independent mathematical review, not an accepted Foundation theorem and not yet the full two-dimensional maximum.

## Next frontier

Use the now-global exact edge maxima as strict competitors in a bivariate signed Bernstein interval search on the symmetry-reduced chamber 0<=p<=z<=1/2. Start from cells with p>=1/64 or z outside I, certify exclusions or retain any interior candidate that dominates the edge. Preserve the original frozen model, observer/map, current P000 and active-source authority. This independent portable research artifact does not claim shared Task ownership or create Result/Review records.
