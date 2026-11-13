# R749SNH — Exact off-diagonal Walsh minimax at (1/2,1/3)

**Date:** 2026-11-14. **Scientific input:** frozen `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`. **Frontier:** R749SNG at PR #2309, scientific commit `74abff6fff03fb6defec95c6c505c69ea5b0832c`. **Status:** author-side exact proof and reproducible rational certificate; independent scientific review NOT_REVIEWED. **Activity:** pending native registration request `r749sn-offdiag-20261114-session` (no claimed Researcher-ID or Task CLAIM at drafting time).

## Mathematical statement

Let $G=\mathbb F_2^4$, $\chi_m(x)=(-1)^{\operatorname{popcount}(m\mathbin{\&}x)}$, and retained indices $B=\{3,5,6,7,9,10,11,12,13,14\}$. Let $F_{t,s}$ be the set of all probability laws on $G$ with $m_3=t,m_{12}=s$ and their other eight $B$-moments zero. With total variation $\operatorname{TV}(q,\mu)=\frac12\sum_x|q(x)-\mu(x)|$, define
$$
\rho(t,s)=\min_{q\in\Delta(G)}\max_{\mu\in F_{t,s}}\operatorname{TV}(q,\mu),\qquad
\rho^{\mathrm{cal}}(t,s)=\min_{q\in F_{t,s}}\max_{\mu\in F_{t,s}}\operatorname{TV}(q,\mu).
$$
For the genuinely off-diagonal point $t=1/2,s=1/3$, both fibers are nonempty and
$$
\boxed{\rho(1/2,1/3)=19/48,\quad \rho^{\mathrm{cal}}(1/2,1/3)=2/5,\quad \rho^{\mathrm{cal}}-\rho=1/240.}
$$
These values hold for the **whole** compatible source fiber at this fixed parameter point, not for sampled source laws.

## Exact parametrization and reduction of all decoders

Use characters $A=\chi_3,D=\chi_{12},AD=\chi_{15},P=\chi_1,AP=\chi_2,Q=\chi_4,DQ=\chi_8$. The entire fiber is
$$
\mu_{h,u,v,w,z}(x)=\frac{1+\tfrac12 A(x)+\tfrac13D(x)+hAD(x)+uP(x)+vAP(x)+wQ(x)+zDQ(x)}{16}\ge0.
$$
The characters $(A,D,P,Q)$ form a basis; translations that flip $P$ and/or $Q$ while fixing $(A,D)$ preserve the source fiber and total variation. Average any decoder over this finite translation subgroup. Convexity of TV and invariance of the maximization imply no increase in worst-case loss. Therefore a free optimal decoder exists in the invariant form
$$
q_{\tau,\sigma,\eta}(x)=\frac{1+\tau A(x)+\sigma D(x)+\eta AD(x)}{16}.
$$
For a calibrated decoder, the same averaging preserves $F_{1/2,1/3}$ and forces $\tau=1/2,\sigma=1/3$.

## Explicit universal upper-bound decoders

For the free problem use
$$
(\tau,\sigma,\eta)=(7/12,7/24,1/24).
$$
For the calibrated problem use
$$
(\tau,\sigma,\eta)=(1/2,1/3,1/30).
$$
Each has 16 nonnegative atom masses summing to one; the second belongs to the retained-moment fiber. The exact polytope certificate below proves
$$
\forall\mu\in F_{1/2,1/3}:\quad
\operatorname{TV}(q_{7/12,7/24,1/24},\mu)\le19/48,\quad
\operatorname{TV}(q_{1/2,1/3,1/30},\mu)\le2/5.
$$

## Universal lower-bound witnesses

Coefficients are listed in order $(h,u,v,w,z)$, defining **actual compatible** source laws by the formula above. For the free problem take
$$
W_f=(0,-2/3,-1/2,-1/3,-1/3),\quad
E_f=\{3,5,7,9,11,13,14,15\}.
$$
For every invariant decoder $q_{\tau,\sigma,\eta}$, $q(E_f)=1/2$, while $\mu_{W_f}(E_f)=43/48$. Thus $\operatorname{TV}(q,\mu_{W_f})\ge19/48$ for every invariant decoder, hence for the original unrestricted minimax problem by symmetry averaging.

For calibrated decoders take
$$
W_1=(-1/6,-2/3,-2/3,-1/6,-1/6),\quad E_1=\{3,7,11,13,14,15\},
$$
$$
W_2=(5/6,-1/6,-1/6,0,0),\quad E_2=\{0,3,5,6,9,10,12,15\}.
$$
For every calibrated symmetric decoder $q_{1/2,1/3,\eta}$, the event inequalities are
$$
L_1=\mu_{W_1}(E_1)-q(E_1)=19/48+\eta/8,\qquad
L_2=\mu_{W_2}(E_2)-q(E_2)=5/12-\eta/2.
$$
Their nonnegative convex combination eliminates the sole free decoder coordinate:
$$
\frac45L_1+\frac15L_2=\frac25.
$$
Since TV dominates every event difference, the calibrated minimax radius is at least $2/5$. Witness normalization and positivity are checked exactly in the accompanying code.

## Complete exact upper-bound certificate

At $t=1/2,s=1/3$ the feasible $(h,u,v,w,z)$ form a **bounded, full-dimensional** rational five-polytope: the law with $h=u=v=w=z=0$ has strictly positive masses (minimum $1/96$). Sixteen atom inequalities describe it exactly. A vertex must contain five independent tight atom inequalities; every five-facet subset is checked by exact integer Bareiss elimination after rescaling $H=6h,U=6u,V=6v,W=6w,Z=6z$.

The reproducible `R749SNH_OFFDIAGONAL_POINT_EXACT_CHECK.py` enumerates all $\binom{16}{5}=4368$ subsets: 3008 nonsingular bases, 216 feasible bases and **44 distinct vertices**. At all 44, both candidate TV inequalities hold in Python `Fraction` arithmetic; equality occurs at 16 free-radius vertices and 8 calibrated-radius vertices. For a fixed decoder, TV is convex in the source law; its maximum over a compact polytope is attained at a vertex. Thus the vertex test proves the universal upper bound for the entire real source fiber. The explicit event bounds complete both minimax equalities.

## Scope, provenance, continuation

This is a strictly auxiliary finite Walsh-source observation model. No native signed-Port, X6 three-dimensional slice or V29/V39 event correspondence has been proved; the frozen P000 and existing source firewall remain unchanged. A scientific file/PR is not itself a Task CLAIM, Result, independent review, Working Truth or Foundation promotion.

The mathematical frontier now includes the first fully certified strictly non-diagonal point $(t,s)=(1/2,1/3)$. The next high-value question is to determine an exact off-diagonal **region** containing this point and its calibrated/free transition curves; use a six- or seven-dimensional rational joint-polytope certificate plus parameterized event duals, checking existing small-square and diagonal formulas at intersections. A separate native-observer mapping remains an independent question.

**Reproduction:** Python 3 standard library, run `python research_notes/portable_direct/R749SNH_OFFDIAGONAL_POINT_EXACT_CHECK.py` and compare its stdout JSON with `R749SNH_OFFDIAGONAL_POINT_RESULTS.json`. The certificate uses integer/Fraction arithmetic throughout and no floating-point optimization.
