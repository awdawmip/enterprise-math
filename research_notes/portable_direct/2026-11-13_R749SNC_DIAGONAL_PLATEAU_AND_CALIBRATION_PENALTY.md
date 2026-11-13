# R749SNC — Exact diagonal Walsh minimax plateau and calibration penalty

Date: 2026-11-13 (Asia/Shanghai).
Lineage: R749SMX–R749SNB, extending the exact R749SNB small-square theorem.
Scientific source remains frozen at `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`; current behavioral rules read separately.
Status: author-side exact proof plus reproducible integer/Fraction vertex certificate. Independent review pending.
This is an auxiliary signed-source observation model, not a native X6/V29/V39 event correspondence.

## Setup and theorem

Let (G=\mathbb F_2^4), (\chi_m(x)=(-1)^{m\cdot x}),
(C=\{1,2,4,8,15\}) and (B=\{3,5,6,7,9,10,11,12,13,14\}).
The compatible fiber (F_p) consists of all source probability measures with
(m_3=m_{12}=p) and the other eight B moments zero.
Write (A=\chi_3,D=\chi_{12},P=\chi_1,Q=\chi_4).
These are independent binary sign coordinates. Every compatible law is uniquely

[
\mu_{p,h,u,v,w,z}(A,D,P,Q)
=\frac{1+p(A+D)+hAD+uP+vAP+wQ+zDQ}{16},
]

subject to all sixteen numerator nonnegativity conditions.
For any compatible source law (\mu), the loss is total variation
(TV(q,\mu)=\frac12\sum_x|q(x)-\mu(x)|).
Define

[
\rho(p)=\min_{q\in\Delta(G)}\max_{\mu\in F_p}TV(q,\mu),\qquad
\rho^{cal}(p)=\min_{q\in F_p}\max_{\mu\in F_p}TV(q,\mu).
]

**Theorem (exact plateau).** For every REAL (p\in[1/5,3/10]),

[
\boxed{\rho(p)=\frac25,\quad
\rho^{cal}(p)=\frac{1+p}{3},\quad
\rho^{cal}(p)-\rho(p)=\frac{5p-1}{15}.}
]

Two explicit optimal prediction distributions are

[
q_p^{free}=\frac{1+(p+\frac15)(A+D)+\frac15 AD}{16},
\qquad
q_p^{cal}=\frac{1+p(A+D)+\frac{1-2p}{3}AD}{16}.
]

The calibrated one has exactly the prescribed ten retained B moments.
Both are nonnegative throughout the stated interval. The latter is a genuine
source law. The free predictor deliberately shifts both known moments from p
to p+1/5, and its optimal risk is lower whenever p>1/5.

Combining with the previous R749SNB theorem gives the COMPLETE diagonal
formula up to 3/10:

[
\rho(p)=\rho^{cal}(p)=\frac{1-p}{2}\quad(0\le p\le1/5);
\qquad
\rho(p)=\frac25,\quad\rho^{cal}(p)=\frac{1+p}{3}
\quad(1/5\le p\le3/10).
]

Independent signed translations extend these formulas to the four sign
diagonals (|t|=|s|=p\le3/10).

## Reduction of the minimax lower bounds to two source laws

The fiber (F_p) is invariant under (P\mapsto-P) and (Q\mapsto-Q).
At equal moments it is also invariant under exchanging
((A,P)\leftrightarrow(D,Q)). Averaging a candidate q over these exact
source-label symmetries cannot increase its worst-case TV radius. Thus a
free minimax center can be taken in the two-parameter form

[
q_{\tau,\eta}=\frac{1+\tau(A+D)+\eta AD}{16},
]

and a calibrated center has (\tau=p). All probabilities here are grouped
by four ((A,D)) classes and uniform in ((P,Q)).

**Witness 1 (deterministic AD).** The compatible law

[
\mu_{AD}=\frac{1+p(A+D)+AD}{16}
]

is nonnegative for (0\le p\le1) and has (AD=+1) with probability one.
The event ({AD=1}) gives

[
TV(q_{\tau,\eta},\mu_{AD})\ge\frac{1-\eta}{2}.
\tag{L1}
]

**Witness 2 (a source-supported event).** Define

[
\mu_E=\frac{1+p(A+D)-pAD-2pQ+(p-1)DQ}{16}.
]

For (0\le p\le1/3), each numerator is one of
(0,4p,2-2p,2-6p,2+2p), hence nonnegative. Its Walsh spectrum has precisely
the allowed coefficients: (h=-p,u=v=0,w=-2p,z=p-1).
Let

[
E=\{DQ=-1\}\cup\{A=1,D=-1\}.
]

Then (\mu_E(E)=1) and (q_{\tau,\eta}(E)=(5-\eta)/8), independently of τ.
Thus

[
TV(q_{\tau,\eta},\mu_E)\ge\frac{3+\eta}{8}.\tag{L2}
]

The maximum of (L1) and (L2) is at least (2/5) for every η,
with equality of these two linear lower bounds when η=1/5.
This proves (\rho(p)\ge2/5) for the whole stated interval.

For a calibrated q, use the fixed event

[
H=\{D=1,Q=-1\}\cup\{A=1,D=-1\}.
]

A direct marginal computation gives
(\mu_E(H)=3(1+p)/4) and
(q_{p,\eta}(H)=(2+p-\eta)/4). Hence

[
TV(q_{p,\eta},\mu_E)\ge\frac{1+2p+\eta}{4}.\tag{L3}
]

Minimizing the maximum of (L1) and (L3) over η yields
(\eta=(1-2p)/3) and value ((1+p)/3).
Consequently (\rho^{cal}(p)\ge(1+p)/3).

## Upper bounds: one finite certificate covers every real p in the interval

Both displayed candidate decoders are affine functions of p. The joint
polytope in six variables ((p,h,u,v,w,z)) is specified by the sixteen
source-positivity inequalities together with (5p\ge1), (10p\le3).
It is full-dimensional and bounded: p has an interior interval and the five
free coordinates are Walsh moments of genuine source probability measures.

The attached `R749SNC_DIAGONAL_PLATEAU_EXACT_CHECK.py` enumerates EVERY
six-facet basis among the 18 inequalities using exact integer Bareiss
elimination and rational back substitution. It tests each solution against all
18 inequalities, deduplicating the resulting vertices. The exact execution
finds:

- 18,564 six-facet subsets;
- 10,848 nonsingular bases;
- 384 feasible bases;
- **106 distinct vertices**, all at p=1/5 (53) or p=3/10 (53).

At each vertex the checker evaluates both explicit decoders by exact
`Fraction` arithmetic, confirming

[
TV(\mu,q_p^{free})\le2/5,\qquad
TV(\mu,q_p^{cal})\le(1+p)/3.
]

Respectively 58 and 66 of the 106 vertices attain equality. For a variable
law in the joint polytope, each distance minus its proposed affine bound is
convex because the law and both candidate decoders are affine in the six
variables. Its maximum is therefore attained at a vertex of this bounded
polytope. Exact nonnegative slacks at all vertices establish BOTH upper
bounds for ALL real p in the interval. Together with (L1)–(L3), this
completes the proof.

The companion JSON records the precise counts and all slack multiplicities.
The script uses Python standard library only. Finite computations are a
complete certificate specifically because the polytope is bounded,
full-dimensional, and all possible vertices are enumerated exactly.

## Interpretation, scope, and continuation

This identifies a nontrivial interval in which deleting the same five
omitted Walsh moments incurs a constant optimal unconstrained prediction
radius, while requiring a calibrated decoder incurs an increasing penalty.
In particular at p=1/4,
(ho=2/5,ho^{cal}=5/12), and at p=3/10,
(ho=2/5,ho^{cal}=13/30).
It extends SNB's one-fifth exact phase rather than repeating it.

Next scientific unit: determine the next diagonal transition immediately
above p=3/10, where the exact optimum begins to exceed 2/5, and derive
piecewise formulas and explicit dual witnesses. Separately inspect
non-diagonal t≠s fibers and observer-composition rules.
Native V29/V39 correspondence, formal Result promotion and independent
review remain outstanding; no shared Task CLAIM is implied.
