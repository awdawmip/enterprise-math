# Orthogonal response budgets and a dictionary-independent limit of an NS certificate

Record-ID: FINDING-EM-PDE-ORTHOGONAL-RESPONSE-BARRIER-20260910
Status: TESTING / ORDINARY_PROOFS_AND_EXACT_RATIONAL_CHECKS / NOT_INDEPENDENTLY_REVIEWED
Researcher-ID: EM-DIRECT-F00A51
Research-Activity-ID: RA-076944AE1950A916ACC95399
Session: local-ns-jitter-901c9f34161ce0f1 (locally assigned continuation key, not a platform-authenticated identity)
Date: 2026-09-10
Read pins: global 2b27c41bbc488ceb1a0b0f7c53afad9df12abe16; enterprise-math a12be839318bded31998207ee18ef76762b7a856.

## 0. Scope, recovery, and mathematical status

Continue the user-selected NS/BRC problem. P000 and native 120-degree orthogonality are unchanged. The calculations concern the classical normalized torus T3=(R/2pi Z)^3, mean-zero real solenoidal fields, viscosity nu=1. The A3/FCC carrier is not a derivation of complete native X6 dynamics. No arbitrary-data regularity, independent review, or historical priority is claimed.

The current parent is research_notes/ns-goal-primal-dual-certificate-20260910.md, Git blob 37d9f40be276dccca96f75c1afa1a2c6694225af, SHA256 dcc9a7e8459593cde11cb5f777c9aa44561f37d9f63758e6c26705f1d89ee22c. Its fixed finite dictionary at amplitude 0.16 was certified insufficient with the split norm majorant. That is consumed as a proved parent result, not rerun as a new discovery.

This note replaces a triangle bound by a proved causal-layer orthogonality law. It certifies the specified amplitude 0.157, and proves a stronger limitation at 0.16: the same fixed scalar contraction majorant cannot work even with an unlimited trial dictionary and an exact norm oracle. The limitation is of a sufficient certificate, not of the PDE solution.

General Hilbert orthogonality, reverse triangle inequalities, infimal convolution, and approximate-solution validation are established methods. The result-specific content is their phase/causal support realization for this A3 family, explicit all-time bounds, and certified consequences. Primary method context: Morosi-Pizzocchero, arXiv:1104.3832; Lobo-Vandenberghe-Boyd-Lebret, Applications of Second-Order Cone Programming, Linear Algebra Appl. 284 (1998). These are context, not independent validation of this note.

## 1. Inherited all-mode interface

Let Lambda=(-Delta)^(1/2), B(f,g)=P((f.grad)g), N(f,g)=-B(f,g), D0=partial_t+Lambda^2. Fix a prescribed heat reference v and put

D_v = D0+B(v,.)+B(.,v), g=N(v,v).

The exact zero-initial causal response is h0=G_v g, with G_v=D_v^-1. The parent all-mode inverse and bilinear trajectory bounds are

Y=L2(0,infinity;Hdot^-1/2),
||h||_X^2=sup_t [||h(t)||_Hdot^1/2^2+(3/4)int_0^t ||h(s)||_Hdot^3/2^2 ds],
||G_v||_(Y->X)<=L,
||G_v B(f,g)||_X<=alpha||f||_X||g||_X,
alpha>= L C*/sqrt(3/2), C*=9503/1000.

The parent proves existence and uniqueness of this full causal inverse using uniform Galerkin estimates and a limit. No finite matrix is identified with the infinite-dimensional inverse.

For any legal zero-initial finite trial d, e=D_vd-g gives

||h0-d||_X <= L||e||_Y.                                    (1)

An upper bound eta>=||h0||_X proves a full NS solution in a radius-r ball when

eta+alpha r^2 <= r, 2alpha r<1.                              (2)

The full nonlinear error equation is w=h0-G_v B(w,w). No generated frequency or helicity is discarded.

## 2. Joint running-energy Gram, before applying a triangle bound

For legal trial trajectories psi_i define

K_ij(t)=Re<Lambda^(1/2)psi_i(t),Lambda^(1/2)psi_j(t)>
        +(3/4)int_0^t Re<Lambda^(3/2)psi_i(s),Lambda^(3/2)psi_j(s)>ds.

K(t) is positive semidefinite for each t and

||sum_i c_i psi_i||_X^2=sup_t c^T K(t)c.                      (3)

Thus the exact norm term in a fixed-reference complete certificate is a convex function of c. Evaluating (3) only at sampled times supplies a LOWER bound, never an all-time upper bound. A full upper bound requires temporal interval/tail control or another proved structural estimate.

In particular, if two trajectories have disjoint Fourier support at every time, then the cross terms vanish in every Sobolev inner product and

||d1+d2||_X^2
 =sup_t [E1(t)+E2(t)]
 <=||d1||_X^2+||d2||_X^2.                                  (4)

This is stronger than squaring ||d1||_X+||d2||_X. Different formal generation labels alone do NOT imply (4); support or the exact cross Gram must be checked. If supports overlap, signed complex cross terms must be retained.

## 3. An A3 causal-support separation law, valid beyond one coefficient choice

Let

k1=(1,1,0), k2=(1,0,1), k3=(0,1,1), k4=(2,-2,0),
Lset={+-k1,+-k2,+-k3}, Hset={+-k4}.

Their integer relation module is

ker_Z[k1 k2 k3 k4] = Z*(0,-2,2,1).                          (5)

Suppose the low-shell component and high-shell component are each separately curl eigenfields on these supports. Their amplitudes and phases may vary subject to reality and these eigenfield conditions; the eigenvalue signs need not be identified across the two shells. Their self nonlinearities vanish because P(a cross curl a)=0.

For the heat reference v, let psi2=D0^-1 N(v,v) be the quadratic response and

psi3=D0^-1 [N(v,psi2)+N(psi2,v)]

the cubic response. A heat inverse preserves output frequency and zero initial trace. Therefore

supp psi2 subset S2=Lset+Hset,
supp psi3 subset S3=(Lset+Lset+Hset) union (Lset+Hset+Hset).

Claim: S2 and S3 are disjoint. For a collision, subtract the leaf multiplicity vectors in Z4. The result has l1 norm at most five and is m*(0,-2,2,1). For the first part of S3, its fourth coordinate is even, so m is even. The l1 bound gives |m|<=1, hence m=0. But the parity of the sum of the four coordinates is the difference between two and three leaves, hence odd; zero is impossible. For the second part of S3, the first three coordinates have l1 norm at most two, whereas any nonzero relation in (5) has low-coordinate l1 norm at least four. Thus m=0, also impossible because the fourth coordinate difference is odd. This proves the claim.

Finite exact set enumeration separately checks |S2|=12, |S3|=56, S2 intersection S3 empty. The proof does not require a floating-point coincidence or one phase choice.

Consequently the first two causal responses satisfy (4) at ALL times. This is the BRC structural step: keep leaf multiplicities, support, shell self-cancellation, and causal trace before deciding that the cross term can be removed. It is not a claim that all successive NS response generations are orthogonal.

## 4. Executed specific initial data and exact defects

For numerical consequences take both initial shells with positive helicity. At each positive k choose e at its zero coordinate and

h_+(k)=[e+i(k cross e)/|k|]/sqrt(2),

use coefficient amplitude a, and impose conjugates at -k. The initial rank is three. Set v=a v_unit. Write the unit first and second causal responses as p2,p3. Then

d=a^2 p2+a^3 p3,
e=D_v d-g=-a^4 [N(v_unit,p3)+N(p3,v_unit)].                  (6)

These equalities are checked with the unchanged exact Fourier/Leray/heat backend. The trial has 216 packets. Its COMPLETE linear defect has 772 packets and 144 output frequencies. These counts are for unit coefficients of both whole responses, not the parent's optimized coefficients; exact cancellation can change the counts.

The inherited analytic temporal certificate gives ||p2||_X<3271/10000. For p3, pure heat energy yields

||p3||_X <=||D0p3||_Y <16/125.

The exact squared source norm is 0.01623924550025455... and its full radical expression is stored in output/verification.json. Therefore (4) proves the all-time upper bound

U_orth(a)=sqrt([(3271/10000)a^2]^2+[(16/125)a^3]^2).           (7)

This bound requires no time sampling. Its source is orthogonality and two established analytic response bounds.

### Amplitude 157/1000: full NS certificate

At a=0.157, rigorous rational bounds give

L=389796863/100000000=3.89796863,
alpha=37806237/1250000=30.2449896,
||e||_Y<0.000023062335301,
U_orth<0.008077889831738,
eta=81677861/10000000000=0.0081677861.

The previous triangle expression with the same component bounds is 0.008558034204, before paying any residual cost. The improvement is not from concealing residuals.

Take r=3/200=0.015. Exact arithmetic verifies

r-eta-alpha r^2=677281/25000000000>0,
2alpha r=113418711/125000000=0.907349688<1,
4alpha eta=3087932570619057/3125000000000000<1.

Thus the inherited all-mode theorem gives a global smooth full NS solution of this specified initial value problem and ||u-v||_X<=0.015. This is one certified parameter point, not a theorem about every amplitude up to it, an optimal threshold, or arbitrary data.

For an apples-to-apples estimator comparison, the UNCHANGED previous goal optimizer was also run with all 12 directions at 0.157. Its rational primal-dual certificate encloses the old split-majorant optimum near 0.00862849333; its lower bound is strictly above 1/(4alpha). Hence coefficient tuning of that old fixed norm model cannot reproduce this result. The new success changes the norm model, not the truth of the old dual bound.

## 5. Two-sided certification and the exact all-dictionary envelope

For t0 finite define

||d||_(X,t0)^2=||d(t0)||_Hdot^1/2^2+(3/4)int_0^t0 ||d(s)||_Hdot^3/2^2 ds.

It is a norm on the appropriate restriction modulo trajectories vanishing through t0, and is bounded by ||d||_X. Equation (1) and the reverse triangle inequality prove

max(0,||d||_(X,t0)-L||D_vd-g||_Y)
 <=||h0||_X
 <=U(d)+L||D_vd-g||_Y.                                    (8)

A single exact time is sufficient for the lower side of (8), not for an all-time upper side. This is the distinction respected by the verifier.

More strongly, over the FULL legal domain of D_v,

inf_d [||d||_X+L||D_vd-g||_Y] = ||G_vg||_X.                 (9)

The inequality >= follows from (1), and equality follows by choosing d=h0. For a graph-dense finite dictionary union, the same infimum follows by approximating h0 in the graph norm using the inherited density theorem. No uniform algorithmic complexity follows from (9).

Thus even an unlimited dictionary and exact coefficient/norm optimization cannot make this certificate smaller than the true first linear response. This identifies a stopping floor without knowing the true nonlinear NS solution.

## 6. A dictionary-independent fixed-majorant obstruction at amplitude 0.16

Keep the SAME heat reference, X norm, and scalar bounds as the parent's 0.16 obstruction:

L0=200630557/50000000=4.01261114,
alpha0=1556725999/50000000=31.13451998.

Use the explicit d in (6). Evaluate its running energy at the RATIONAL time t0=17/100. Every scalar coefficient is in a finite radical field. Products and partial integrals are finite exponential-polynomial expressions; exponentials are enclosed by rational Taylor bounds. The checker verifies all derivative and zero-initial integral identities and the total integrated dissipation against the canonical Fourier Gram.

A certified evaluation gives, by (8),

||h0||_X > ell=41340889/5000000000=0.0082681778.              (10)

Here ||e||_Y<0.000024876232260; its complete outputs are retained. The finite-time running norm of d is used only to prove the lower bound.

Rational arithmetic yields

4alpha0 ell=64356436728073111/62500000000000000>1.            (11)

For any eta>=||h0||_X and any radius r, the scalar quadratic condition eta+alpha0 r^2<=r is impossible because the maximum of r-alpha0 r^2 is 1/(4alpha0). Therefore NO trial dictionary, and no refinement of U down to the exact norm, can make THIS fixed-reference, fixed-alpha majorant test pass at 0.16. This is stronger than the parent's finite-dictionary obstruction.

It is NOT a blow-up result or a lower bound on the best possible bilinear operator norm. A new reference, sharper directional feedback bounds, a different norm, or a smaller valid alpha could change the result.

As a diagnostic, while retaining this reference and this X norm, success requires alpha<1/(4ell)=30.2364083172..., at least a 2.884617% decrease relative to alpha0. This is necessary from the available lower bound, not sufficient for success. It gives a quantitative next target instead of repeatedly refining an exhausted dictionary.

## 7. Reuse, verification, and next unfinished unit

REUSE_EXECUTED unchanged:
- exact_packets.py SHA256 0ffab938427c4827700876fbd9f9c371a59d07aa89edefd5a6447071ec48d25d;
- certify_greedy.py SHA256 b2c662832fccd5749d6f531c17b9bbb7ed9f512c42158271076cd1c2fdfba536;
- certify_goal.py SHA256 954caee644e7a251e7a4631bf94cdca32dd19cd14d7d9577506235b2f59c9a81, for the old norm-model comparison.

REUSE_APPLIED: T0_BRC and T6 operation-safe quotient; parent all-mode inverse, critical trajectory product, temporal first-response certificate, and C*=9.503. EXTEND_EXISTING_TOOL: two-layer orthogonal norm budget and two-sided all-dictionary obstruction. No new accepted top-level toolbox family or Foundation promotion.

Executed checks: exact integer kernel and support separation; shell self-nonlinearity zeros; reality, divergence and initial traces; complete linear defects; exact cross-Gram zero; exact exponential integral/derivative identities; rational inverse and norm enclosures; .157 nonlinear ball; .16 dictionary-independent obstruction; old .157 full-dictionary dual comparison. No PDE simulation or time-grid extrapolation. The code reads no external pickle.

Next smallest mathematical unit: reduce the directional feedback/inverse majorant at .16 or replace the reference, with all Fourier tails certified. Merely adding more vectors to the old linear solve is now ruled out as a remedy under its fixed scalar alpha. The arbitrary-data NS problem remains unclosed.
