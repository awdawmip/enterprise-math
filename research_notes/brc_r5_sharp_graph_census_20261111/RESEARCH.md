# R5 — Sharp four-atom edge circuits: graph rigidity and exact census

Date: 2026-11-11 (Asia/Shanghai). Status: author-side exact theorem + exhaustive integer test. Researcher-ID: EM-DIRECT-89C232 (TASK_RESEARCH); activity RA-28509062FAC81AFD31BC1F94.

Frozen scientific pins: GLOBAL `a01383f825ef9d43b4b754254303298c64041568`, EM `86149263e38c22292c9def1e0f69092efa1be77e`. Prior science: [PR #2017](https://github.com/awdawmip/enterprise-math/pull/2017) classifies 210 K2,3 residuals; [PR #2021](https://github.com/awdawmip/enterprise-math/pull/2021) proves rank/adjacency; [PR #2038](https://github.com/awdawmip/enterprise-math/pull/2038) constructs a physically lawful length-four adjacent ray; [PR #2043](https://github.com/awdawmip/enterprise-math/pull/2043) proves the sharp global length-four upper bound and necessary degree geometry. This continuation strengthens the necessary structure to an exact iff and counts the circuits.

## Exact model

The seven target likelihood ratios are (r_i=(2,10,15,20,25,30,38)_i/20), with distinct values. The four variable source ports are (J=\{1,2,3,5\}); singleton arcs at (0,0), (6,6) have zero residual. The 21-by-30 observer (C) records target marginal masses, source marginal masses, and first target-ratio moments at each source. Let (F_b=\{E\ge0:CE=b\}). A signed six-arc (K_{2,3}) atom places opposite zero-mass/zero-first-moment three-target vectors at two source ports. Define (L(d)) as the least number of arbitrarily real-scaled such atoms summing to (d\in\ker C).

## Theorem 1 — iff criterion for sharp adjacent rays

For any nonempty observer fiber (F_b) and distinct adjacent vertices (V,W), (d=W-V) has (L(d)=4) **if and only if** its 14 nonzero source-target arcs form the target-labeled multigraph (K_4) on the four source ports plus one extra edge between the two degree-four ports. Each target label represents the unique unordered source pair carrying opposite nonzero residual masses.

### Proof

By the global sharp bound and necessary geometry proved in PR #2043, any (L(d)=4) adjacent ray has four active source ports, 14 signed nonzero arcs, source degrees (3,3,4,4) and exactly two nonzeros at each of seven targets. Adjacent edge support (S) is a linear-matroid circuit: (dim\ker C_S=1) and its unique nonzero direction has full support. Conversely, throughout the proof start with any adjacent ray having this degree pattern.

Write (p,q) for degree-three ports and (h,k) for degree-four ports; let (m_{uv}) count target labels linking (u,v). Degree equations imply
[
m_{hk}=m_{pq}+1,quad m_{ph}=m_{qk}=x,quad
m_{pk}=m_{qh}=3-m_{pq}-x.
]
If any source pair shared three distinct target labels, those six arcs would themselves contain a nonzero (K_{2,3}) kernel vector, contradicting circuit minimality of the 14-arc support. Thus (a=m_{pq}\in\{0,1\}).

**Three-atom criterion.** Every source row with three nonzero targets needs at least one atom appearance; a row with four needs at least two. Three atoms provide exactly six source appearances, exhausting the minimum (1+1+2+2=6). If (p,q) are paired to each other in one atom, their entire three-target supports must coincide and be negatives. The other four target labels would all join (h,k), which contains a proper six-arc kernel circuit. Hence a three-atom representation must pair (p) with one high port, (q) with the other high port, and have a final atom between (h,k).

For the matching (p\leftrightarrow h, q\leftrightarrow k), the first two atoms are uniquely fixed by the complete three-target rows of (p,q). Their subtraction leaves opposite residual high rows with zero mass and first moment, supported exactly on target labels **not** linking (p-h) or (q-k). The residual support therefore has size (7-m_{ph}-m_{qk}). A nonzero zero-mass/zero-moment row on distinct ratios must use at least three labels; it is one atom if and only if this size is at most three. Therefore a three-atom representation exists iff one of the two matchings has at least four target labels:
[
L(d)=3 \iff \max\{m_{ph}+m_{qk},m_{pk}+m_{qh}\}\ge4.
]
Two atoms are impossible by the six required source appearances.

When (a=0), the matching sizes are (2x) and (2(3-x)), so one is at least four: (L=3). When (a=1), they are (2x) and (2(2-x)): (x=0,2) give (L=3), while (x=1) gives neither matching four labels, hence (L\ge4), and PR #2043 supplies (L\le4). The (a=x=1) case is precisely one label on every source pair, and a second label on the (h-k) pair. This proves the criterion.

## Theorem 2 — complete finite census of possible sharp circuit supports

For these seven *frozen* target ratios, there are exactly **14,832** distinct full 14-arc support circuits of length four. There are **15,120** seven-target-label assignments to the six pairs of (K_4) plus the doubled high-high pair; precisely **288** assignments degenerate by having one zero edge. For each of six choices of the low-degree source pair: 2520 assignments, 2472 nondegenerate circuits, 48 degeneracies.

### Exact derivation and integer certificate

Choose low ports (p,q), high ports (h,k). Denote seven target labels by (A=pq,B=ph,C=pk,D=qh,E=qk,F=hk,G=hk), with (F<G). The (7!/2=2520) assignments for each low-pair choice exhaust the possible labeled support graphs. Let (a,b,c,d,e,f,g) be the corresponding **integer** ratio numerators (divide by 20 only when interpreting their physical ratio).

Define
[
\begin{aligned}
u_A&=(b-c)(d-e),&u_B&=(c-a)(d-e),&u_C&=(a-b)(d-e),\\
u_D&=-(b-c)(e-a),&u_E&=-(b-c)(a-d).
\end{aligned}
]
On the low rows place (p:(u_A,u_B,u_C)), (q:(-u_A,u_D,u_E)) at their incident labels. Set (\Delta=g-f). Multiply all five values by (\Delta). The remaining flows on high source (h) at (F,G) are
[
v_F=(-u_B)(b-g)+(-u_D)(d-g),qquad
v_G=(-u_B)(f-b)+(-u_D)(f-d),
]
and the high source (k) takes their negatives. The high source (h) also has (-\Delta u_B,-\Delta u_D), while (k) has (-\Delta u_C,-\Delta u_E).

All four row mass and first-moment sums vanish exactly; each target has equal/opposite masses. Because the ratios are distinct, the five (u)'s and (\Delta) are nonzero. The two low-row equations and their common (A) edge fix the first five flows up to scalar; the two-by-two system at (F,G) has determinant (g-f\ne0) and uniquely fixes the last two. Hence the restricted seven-target-edge kernel has dimension one for every assignment. Its 14-arc support is a circuit precisely when (v_F v_G\ne0).

The accompanying Python standard-library verifier independently computes all these **integer** quantities, checks all eight row conservation equalities for each of the 15,120 cases, and records the zeros. Exactly 288 cases lose one edge, always at target index 3 (ratio (20/20)); the other 14,832 have full support. The exact terminal output is retained in `EXACT_OUTPUT.txt`.

Each full-support kernel circuit is an actual adjacent ray in some nonnegative observer fiber: write its signed vector (z=z_+-z_-), set (b=Cz_+=Cz_-). Both (z_+) and (z_-) are vertices, and the face supported on (S=\mathrm{supp}(z)) is 1-dimensional. They are adjacent and the difference has word length four by Theorem 1. Distinct target-labeled supports give distinct rays up to scaling.

**Explicit certificates:** With low ports (1,2), high (3,5), assignment ((A,B,C,D,E,F,G)=(0,1,2,3,4,5,6)) gives integer flows ((200,-520,320,920,-720,250,150)), all nonzero. Assignment ((0,1,2,4,5,3,6)) gives ((450,-1170,720,2520,-2070,0,1350)): one edge vanishes.

## Evidence, BRC semantics, and next frontier

Carrier: labeled signed transfer branch masses. Observer: marginals and first likelihood-ratio moments. Future operation in scope: exact linear residual recovery, signed K2,3 dictionary decomposition, and adjacency of nonnegative transport fibers. The seven source-pair/target-label incidences retain joint relation information erased by the observer; the explicit kernel is the repair carrier. Reuse resolution: `REUSE_APPLIED` from PRs #2017, #2021, #2038 and #2043.

Verification: `python VERIFY_SHARP_SUPPORT_CLASSIFICATION.py` (Python 3 standard library; no floats, random sampling or external solvers). Observed terminal marker: `PASS_EXACT_SHARP_SUPPORT_CLASSIFICATION_14832_OF_15120`. This is a complete, precisely enumerated **observer-fiber** census. The physically legal pinned fiber has a known sharp witness (#2038), but the number of its sharp adjacent edges is a separate outstanding problem.

**Next:** Test which of the 14,832 potential circuit supports are actually incident to edges of the frozen physically lawful fiber using the exact (C), its fixed right-hand side and nonnegative feasibility. Extract the physical-fiber count and an efficient exact incidence certificate. Separate question: how the 288 exceptional assignments move under perturbations of the likelihood ratios (do not rebase the frozen science inputs).
