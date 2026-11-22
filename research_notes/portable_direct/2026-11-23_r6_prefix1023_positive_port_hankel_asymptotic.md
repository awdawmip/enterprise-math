# PREFIX-1023 — Positive-port Hankel obstruction: exact non-C-finiteness, common asymptotic and a finite Gram counterexample

2026-11-23 (Asia/Shanghai). Status: AUTHOR_EXACT_ASYMPTOTIC_PROOF / EXACT_LAURENT_CHECKED / NOT_REVIEWED.

## Frozen mathematical object and provenance

Continue PREFIX-1022's negative-port strict-Hankel result and PREFIX-1014's four-port formula. The immutable scientific input remains enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json (P000 V5); no repinning. The candidate signed X6 Stage46 BRC is W(h,d)=1-6[h=d], seed (chosen Cell 0, incoming -e1), double-direction absorption of the Link {0,e1}, grade k=1 meaning exactly one negative outgoing direction. Amplitudes combine within a joint Cell–terminal-port–grade fibre before squared mass is computed. Results are terminal squared-numerator statements; probability mass divides by 36^n.

Notation in R=Z[z_1^(±1),...,z_6^(±1)]:
S=sum_i z_i, S*=sum_i z_i^-1, L=SS*, m=n-4>=1.
For a fixed positive terminal direction j=1,...,6, PREFIX-1014's exact Laurent packet is
A_(m,j)=(m+3)(L-36)+E_j,   E_j=72-6S(z_1^-1+z_j^-1),
B_(m,j)=z_j[(S-z_1)A_(m,j)+z_1(L-36)+25z_1],
F_(n,j)=S^m B_(m,j),   Q^+_(n,j)=CT(F_(n,j)F_(n,j)*).
The displayed B is an exact rearrangement of PREFIX-1014's S A_n-z_1 A_(n-1)+25z_1 formula, valid including j=1, where duplicate Laurent terms must be retained with coefficient two.

## Theorem 1 — exact leading mass asymptotic for every positive terminal port

For each j=1,...,6 (independently of j), as integer m -> infinity,
Q^+_(m+4,j) = [7063875/(4 pi^(5/2))] 36^m m^(-5/2) (1+o(1)).

Consequently all six positive terminal mass sequences have the same leading asymptotic, their growth-rate root tends to 36, and each Q^+_(m+4,j)/36^m tends to zero.

Proof. Parseval in the six-variable Laurent ring gives the exact torus integral
Q^+_(m+4,j)=(2pi)^(-6) int_[0,2pi]^6 |S(z)|^(2m)|B_(m,j)(z)|^2 dtheta.
B is homogeneous of total Laurent degree 2, and |S| depends only on relative phases, so gauge theta_1=0 and integrate the five relative angles u_i=theta_i-theta_1 (i=2,...,6) with normalized factor (2pi)^(-5). Write q(u)=sum_(i=2)^6 u_i^2-(sum_(i=2)^6 u_i)^2/6. It is positive definite with matrix M=I_5-11^T/6 and det M=1/6. The unique torus maximizer of L=|S|^2 is u=0, where
L(u)=36-6q(u)+O(|u|^4),   E_j(u)=O(|u|),   S(u)-z_1=5+O(|u|).
In the scaling u=y/sqrt(m), one obtains
[L(y/sqrt(m))/36]^m -> exp(-q(y)/6),
B_(m,j)(y/sqrt(m)) -> 25-30q(y),
uniformly on compact y-sets, irrespective of j. In a fixed small neighborhood, L/36 <= exp(-c|u|^2) and |B_(m,j)| <= C(1+m|u|^2); outside that neighborhood L/36 <= rho<1 and |B| <= C(1+m). Gaussian domination and exponential negligibility justify dominated convergence after the rescaling:
lim_(m->infty) m^(5/2) Q^+_(m+4,j)/36^m
= (2pi)^(-5) int_R5 (25-30q(y))^2 exp(-q(y)/6)dy.
Set w=M^(1/2)y. Then det(M)^(-1/2)=sqrt(6). Under the normalized Gaussian proportional to exp(-|w|^2/6), the variable q=|w|^2 has E[q]=15, E[q^2]=315. Hence E[(25-30q)^2]=625-1500*15+900*315=261625, and the integral is
261625*sqrt(6)*(6pi)^(5/2)/(2pi)^5 = 7063875/(4 pi^(5/2)).
This positive constant completes the proof.

## Theorem 2 — infinite Hankel rank for positive ports, despite failure of moment positivity

Each sequence (Q^+_(n,j))_(n>=5), j=1,...,6, has no nontrivial eventual constant-coefficient linear recurrence. Therefore its infinite Hankel matrix has unbounded rank and it admits no fixed-finite-dimensional autonomous linear state update with linear output reproducing the whole sequence.

Proof. If an eventual scalar linear recurrence existed, its sequence would be an exponential polynomial sum P_l(m)lambda_l^m, apart from a finite prefix. Theorem 1 gives lim_m (Q_m)^(1/m)=36 and Q_m/36^m ->0. For an exponential polynomial whose largest effective root modulus is 36, after dividing by 36^m and by the largest polynomial degree m^d, the leading term is a finite nonzero sum c_l exp(i m theta_l), which cannot tend to zero: its Cesaro mean square tends to sum |c_l|^2>0 after combining equal phases. Iterating down degrees rules out the required decay, a contradiction. This is an observation-specific linear no-go; it does not exclude time-indexed or nonlinear closure.

Moreover the PREFIX-1022 strict-positive-Hankel property for negative ports does NOT transfer to positive ports. The exact integer positive-port values for any j>=2 at n=5,...,9 are
109490, 2532792, 59610948, 1458235054, 37154147448.
They give the 3x3 Hankel minor
det [[109490,2532792,59610948],
     [2532792,59610948,1458235054],
     [59610948,1458235054,37154147448]]
= -162880156241080473416 < 0.
Thus this particular positive-port Hankel matrix is indefinite (its 1x1 first principal minor is positive), even though its infinite rank is unbounded. This exact counterexample prevents copying the negative-port moment-Gram positivity argument across port sign.

## Corollary (using PREFIX-1017's proven three-A6-shift asymptotic)

The already established result Delta^+_(m+4)/A6(m+3)=175/(36m)+O(m^-2), with Delta^+ = Q^+_(axis1)-Q^+_(each-other-axis), and the same five-relative-phase Gaussian calculation for A6(r)=CT L^r yield
A6(r) ~ [27/(4 pi^(5/2))]36^r r^(-5/2),
Delta^+_(m+4) ~ [1530900/pi^(5/2)]36^m m^(-7/2).
Therefore Delta^+ also has infinite Hankel rank and no eventual constant-coefficient linear recurrence. The distinguished-to-other leading contrast is
Delta^+_(m+4)/Q^+_(m+4,1) ~ 1296/(1495m).
These consequences reuse the exact PREFIX-1017/1016 expansion with its original author-verified, NOT_REVIEWED evidence status.

## Exact calculation and verification scope

A separately implemented integer Laurent multiplication verifier was run for all twelve positive terminal ports (six per step with the symmetry verified) at n=5,...,11. Its values agree with the PREFIX-1014 published per-port results at n=5,6,7,8,10. Bareiss exact determinants were checked at starting index n0=5 for orders 2,3,4:

- First-axis positive port: det_2=497128617000; det_3=59581568378641261000; det_4=480224313296628175018185990000.
- Each other positive port: det_2=111767381256; det_3=-162880156241080473416; det_4=-3907255130288416178191654446288.

The exact finite computation validates the declared integers and the strict-Hankel counterexample. It does not replace the all-length asymptotic proof. The polynomial-Gaussian asymptotic and non-C-finite implication are author-proved and have not undergone independent mathematical review.

Code: PREFIX1023_R6_POSITIVE_HANKEL_ASYMPTOTIC_CHECK.py. Certificate: PREFIX1023_R6_POSITIVE_HANKEL_EXACT_RESULTS.json.

## Research continuation and authority

This upgrades PREFIX-1022's negative-port infinite Hankel obstruction to positive ports by a different method, while showing a precise sign-sensitive defect of the proposed positivity transfer. For the grade-one fixed seed, the four-class squared masses are now all non-C-finite in n; no finite time-invariant linear scalar observer closes the complete trajectory.

Next discriminating question: can the n-dependent positive-packet polynomial be represented by a minimal time-varying Gram/jet carrier that reproduces all four terminal masses while retaining the Cell–port interference needed for subsequent updates? In particular, compare a finite moment/derivative jet against the native A/B grade-one two-block recurrence and certify the exact future-operation horizon. The mother objective B_fix,odd(32) in {19,20} remains open.

Earlier provenance: PREFIX-1014/1017/1022; historical contributor EM-DIRECT-FBEA5D / Activity RA-3FB2D033BE6048D8712FF056 / SID MCP-45ad6d29cd534c1aad25595a72e3c532. These historical IDs are not present-session CLAIM or execution authority. This work is published as standalone portable research, not an accepted Result, independent Review, or P000 modification.
