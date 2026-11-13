# R5 — exact C_(4/5) positive-residual extension across the full physical side-capacity square

Date: 2026-11-08. Status: **AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY**.

## Provenance and scope

This is a continuation of the seven-likelihood-ratio P/Q-BRC statistical observer from R5 PR #1803 (research SHA `8613b2b8d6721938dfd310a4a1fafb25b6c5c785`), with **scientific inputs frozen** at global `a01383f825ef9d43b4b754254303298c64041568` and Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`. Applicable current norms were read independently. P000 and the protected ACTIVE worldview were not modified. The only declared preserved observer is `(e_P,e_Q,T_P,T_Q)` for seven terminal likelihood-ratio decisions; this is **not** a native Heartbeat X6 dynamics theorem or a claim that every future branch observer is preserved.

Real current native Researcher-ID: `EM-DIRECT-731910 / TASK_RESEARCH`, activity `RA-B1E6CFA9F7A4EC4A6E09515B`, as issued by the Source MCP service. It grants no CLAIM, shared result publication, or independent review. This author-side artifact is placed on an ordinary GitHub research branch.

## New theorem

Let every parameter be a real number with

[
\frac1{100}\le t\le\frac15,\quad 0\le p,q\le1,\quad\frac34\le\theta\le1.
]

Fix \(\kappa=3/4\) and define the lawful FULL_HIST flow

[
x(t,p,q,\theta)=
\left(1,t,1,
\left(\frac{13t}{40}+\frac1{80}\right)p,
\frac{t\theta}{10}+\frac{27}{160},
\left(\frac{3t}{40}+\frac{21}{80}\right)q,
\frac{t\theta}{10}\right).
]

For **each** such real source, there is a lawful seedless LR target \(y\) on the *same fixed chart*

[
C_{4/5}=\left\{z'=\frac{2a'}{25},\quad v'-z'=\frac{9b'}{50}\right\},
]

and a nonnegative \(7\times7\) declaration-independent Blackwell matrix \(Q\) that exactly matches both P/Q terminal decision errors and P/Q expected stopping times. The four observables are \((e_P,e_Q,T_P,T_Q)\); the result holds for any seven-node randomized terminal declaration and for the entire source-to-target convex interpolant \((1-h)x+hy\), \(0\le h\le1\).

The signed historical residual in this source is

[
R_{history}=\frac{9t}{10}(\theta-\tfrac34)\ge0,
]

strictly positive when \(\theta>3/4\). Thus this result crosses into the **positive-residual** side of the prior \(\theta\le3/4\) prism while keeping **both** physical side capacities \(p,q\in[0,1]\) unrestricted.

## Exact finite certificate and proof for all real parameters

The relevant seven likelihood ratios in increasing order are

[
r=(1/10,1/2,3/4,1,5/4,3/2,19/10).
]

Write \(M(f)\) for the seven Q-probability masses, and \(T_P(f),T_Q(f)\) for the two stopping-time expressions defined **explicitly** in the self-contained `VERIFY_SUPPORT.py`; these are the unchanged frozen R5 affine functions.

The entire rectangle is the nonnegative multi-affine combination of the 16 vertices

[
t\in\{1/100,1/5\},\quad
p,q\in\{0,1\},\quad
\theta\in\{3/4,1\}.
]

For **each** of the 16 vertices, `EXACT_SUPPORT_CERTS.json` gives: (a) the sparse matrix support `s`, encoding an edge \((i,j)\) by \(7i+j\); (b) the exact rational values `f` for the free columns in an exact left-to-right Gaussian elimination of the seven row-mass, seven source-column mass, seven likelihood-ratio-weighted column, and two time equations.

The standalone Fraction-only checker reconstructs all five target flow coordinates \((g',a',b',u',w')\) and all nonzero matrix entries by exact Gaussian elimination. It then verifies:

[
\sum_jQ_{ij}=M_i(y),\qquad
\sum_iQ_{ij}=M_j(x),\qquad
\sum_ir_iQ_{ij}=r_jM_j(x)
]

for every \(i,j\), and \(T_P(y)=T_P(x)\), \(T_Q(y)=T_Q(x)\). It also tests positivity, both normalizations under P and Q, the target physical side capacities and seedless relation

[
9b'z'=4a'(v'-z').
]

The exact 16 certificates contain **164 strictly positive transfer entries** in total. They were found by floating-point LP support exploration followed by exact rational reconstruction. **The LP numerical output is not the mathematical evidence:** the stored rational support/free-value data plus the independent Fraction-only verifier are sufficient to reconstruct and test every identity without optimization packages.

For any real interior point, use the product weights

[
W_{ijkl}=(s\text{ if }i\text{ else }1-s)
(p\text{ if }j\text{ else }1-p)
(q\text{ if }k\text{ else }1-q)
(d\text{ if }l\text{ else }1-d),
]
where \(s=(t-1/100)/(1/5-1/100)\) and \(d=4(\theta-3/4)\). All weights are nonnegative and sum to 1. The source is separately affine in \(t,p,q,\theta\), so \(x=\sum W_e x_e\). Define \(y=\sum W_e y_e\), \(Q=\sum W_e Q_e\); every target belongs to the **common affine seedless chart** \(C_{4/5}\). Source/target mass laws, physical capacities, transport equations, and stopping time laws are affine, so all equalities and inequalities are preserved by this convex mixture. This completes the proof for **all real parameters** (including irrational interior values), independent of the finite regression grid.

For an arbitrary real \(h\in[0,1]\), the kernel \(Q_h=(1-h)Q+h\operatorname{diag}(M(y))\) implements the same declared four-observable equivalence for \((1-h)x+hy\).

## Executed verification

Local command run: `python3 VERIFY_SUPPORT.py` with Python standard-library `fractions.Fraction` only. Observed stdout:

```text
EXACT_16_CORNER_CERTIFICATES_PASS 164
EXACT_257_INTERIOR_REGRESSION_PASS
PROVED_ALL_REAL_T_1_100_TO_1_5_P_Q_0_TO_1_THETA_3_4_TO_1_KAPPA_3_4_SEEDLESS_C_4_5
```

The 257 regressions are an implementation check; the all-real conclusion follows from the 16 exact certificate checks and multi-affine algebraic argument above, **not** finite numerical interpolation alone.

## Connection to prior verified author frontier

The prior R5 PR #1803 author-side proof shows \(t\in[0,1/5]\), \(p,q\in[0,1]\), \(\theta\in[0,3/4]\), \(\kappa=3/4\) on chart \(C_{3/4}\). The present theorem handles \(t\in[1/100,1/5]\), \(\theta\in[3/4,1]\) on chart \(C_{4/5}\). Consequently **their union covers the full real \(\theta\in[0,1]\) interval for every \(t\in[1/100,1/5]\), \(p,q\in[0,1]\) at fixed \(\kappa=3/4\)**. At the shared \(\theta=3/4\) boundary, each chart separately has an exact lift. No cross-chart convex mixture is needed; the proof chooses the chart by region.

This does not settle \(0<t<1/100,\theta>3/4\), varying \(\kappa\), or all FULL_HIST strategies, and is not mathematical admission.

## Smallest unresolved research unit

Inspect \(0<t<1/100\), \(\theta>3/4\) especially the \(p=0,q=1\) source corner, where a fixed \(C_{4/5}\) chart already becomes infeasible at \(t=0\). Test a **moving seedless chart** \(C_{c(t)}\) with \(c(t)\to3/4\) as \(t\to0\), seeking an analytic nonnegative Blackwell kernel and a uniform patch argument. Distinguish chart-specific no-go from global nonrealizability. An independent route is to allow \(\kappa\) to vary and locate adjacent full physical-capacity regions. Keep the original R5 mother question open and preserve all activity/claim/admission boundaries.
