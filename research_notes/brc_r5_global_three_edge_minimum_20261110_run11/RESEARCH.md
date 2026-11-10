# R5: an exact global three-edge minimum in the frozen P/Q–BRC Blackwell model

Date: 2026-11-10 (Asia/Shanghai)  
Evidence status: author-side mathematical proof with executed exact-rational SymPy checks; no independent mathematical review or official Source Result yet.

## 1. Model, fixed provenance, statement

This is a new research unit **within the same seven-likelihood-ratio statistical Blackwell model** as PR #1939, immutable predecessor commit `9f39dc7f2145548c2a9a04e387d9f33fdec1ce4e`. Frozen scientific input pins remain account `a01383f825ef9d43b4b754254303298c64041568` and Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`. P000 and its six native spatial axes remain unchanged; the seven ratios below are auxiliary statistical observations.

The likelihood ratios, in index order 0 through 6, are

$$
r=(1/10,\ 1/2,\ 3/4,\ 1,\ 5/4,\ 3/2,\ 19/10).
$$

A nonnegative Blackwell coupling $E=(E_{ij})$ obeys all 21 equations

$$
\sum_j E_{ij}=\mu_i,\quad
\sum_i E_{ij}=\nu_j,\quad
\sum_i r_iE_{ij}=r_j\nu_j.
$$

The 30 allowed directed edges are exactly those from the PR #1939 checker: source columns $j=0,1,2,3,5,6$; columns $0,6$ have only the diagonal edges $(0,0),(6,6)$; each of columns $1,2,3,5$ may target any of seven rows. Source physical parameters are $x=(g,a,b,u,v,w,z)$; target physical parameters are $y=(G,A,B,U,V,W,Z)$. We retain all 13 physical capacity inequalities per strategy, the source condition $g=b$, target conditions $G=1$ and $Z=A/10$, the two matched stopping-time equations, and the *same* affine mass and time maps in `VERIFY.py`.

### Theorem: global minimum, including all equality cases

Among all physically lawful source–target pairs that admit a Blackwell coupling, the **least possible number of positive coupling edges is 3**. The physically lawful pairs admitting a coupling with exactly 3 positive edges are precisely

$$
\boxed{x=y=(1,1,1,27/80,v,27/80,1/10),\quad 1/10\le v\le13/40.}
$$

For every such pair, the **unique** coupling with only 3 positive edges is the diagonal support

$$
\boxed{\{(0,0),(3,3),(6,6)\}},
$$

with masses

$$
E_{00}=E_{66}=s(v),\quad E_{33}=1-2s(v),\qquad
s(v)=\frac{7933}{36000}+\frac{67}{162}\left(v-\frac1{10}\right).
$$

All three masses are strictly positive for the **whole closed interval** (including both endpoints). At $v=1/10$ they are $(7933/36000,\ 10067/18000,\ 7933/36000)$. This theorem describes the **global sparsest realization**; the independent local classification of **14/15-edge necessary regions** in PR #1939 remains intact.

## 2. Universal lower bound: every lawful source uses at least three columns

Write $d=v-z$. The source's original capacity inequalities plus $g=b$ imply

$$
0\le a\le b\le1,\quad
0\le u\le\frac{13a}{40}+\frac b{80},\quad
0\le w\le\frac{3a}{40}+\frac{21b}{80},\quad
0\le z\le a/10,\quad
0\le d\le9b/40.
$$

Necessarily $b>0$: at $b=0$, nonnegative slacks enforce $a=u=v=w=z=0$ and the source's second stopping time equals 1, whereas every lawful target has $G=1$ and second stopping time at least 2. The two stopping times must match.

The source column-3 mass is *exactly*

$$
\nu_3=(1-b)+(a/10-z)+(9b/40-d)
       +(191/450)(u+w)+(43/90)z+(14/81)d.
$$

Every summand is nonnegative. The last two terms involving $d$ yield the uniform bound

$$
\nu_3\ge 1-b+\frac7{180}b>0.
$$

The extreme column masses are

$$
\begin{aligned}
\nu_0&=(509/900)u+(47/180)z+(67/162)d+w/100,\\
\nu_6&=u/100+(47/180)z+(67/162)d+(509/900)w.
\end{aligned}
$$

If at least one of $u,w,z,d$ is positive, both $\nu_0$ and $\nu_6$ are strictly positive. Then columns $0,3,6$ all have positive mass. In the complementary case $u=w=z=d=0$, we have $\nu_1=13a/40+b/80>0$ and $\nu_5=3a/40+21b/80>0$, together with $\nu_3>0$. Therefore **at least three distinct source columns always carry strictly positive mass**. Every coupling with those source margins requires at least one positive edge per positive source column; hence it has at least three positive edges.

## 3. Three edges force a diagonal coupling and equal statistical margins

Suppose a lawful coupling has exactly three positive edges. By the preceding proof there are exactly three positive source columns, each with **one** positive edge. If the sole edge from column $j$ is $(i,j)$ of weight $\nu_j>0$, the exact column moment equation is

$$
r_i\nu_j=r_j\nu_j.
$$

Since the seven likelihood ratios are pairwise distinct, $i=j$. All three edges are diagonal and consequently $\mu=\nu$.

## 4. Physical capacity inequalities force x=y

The system comprising the five independent physical equations (source $g=b$, target $G=1$, target $Z=A/10$, two matched times) and the seven equal-margin equations $\mu_i-\nu_i=0$ has **exact rational coefficient rank 9** in fourteen physical variables. Its **complete five-parameter affine solution** is

$$
\begin{aligned}
y&=(1,10Z,1,U,V,W,Z),\\
x&=(1+\kappa\Delta,\ 10Z+\kappa\Delta,\ 1+\kappa\Delta,\
       U+\lambda\Delta,\ V-\gamma\Delta,\ W+\lambda\Delta,\ z),\\
\Delta&=Z-z,\\
\kappa&=49400/295513,\quad
\lambda=33345/591026,\quad
\gamma=132145/295513.
\end{aligned}
$$

Substitution into all twelve equations is exact, and the five parameters are independent; rank 9 therefore establishes completeness. The two *existing* source capacity slacks give

$$
1-x_g=-\kappa\Delta\ge0,\qquad
x_a/10-x_z=\frac{300453}{295513}\Delta\ge0.
$$

Both coefficients are positive, hence $\Delta=0$ and **$x=y$**. In particular this is an explicit observation-fiber phenomenon: equal statistical margins alone leave an affine one-dimensional difference direction, but the lawful physical capacity cone cuts that direction to zero.

It follows that every lawful equal-margin pair is of the form

$$
x=y=(1,a,1,u,v,w,a/10)
$$

with

$$
0\le a\le1,\quad
0\le u\le13a/40+1/80,\quad
0\le w\le3a/40+21/80,\quad
a/10\le v\le a/10+9/40.
$$

The remaining original capacities and two matched stopping times hold throughout this family. It is a four-dimensional relative physical family.

## 5. Classify the minimum-support equality cases

On the above equality locus, $\nu_3>0$ and $\nu_0,\nu_6$ are either both positive or both zero.

If both extreme masses vanish, their strictly positive coefficient formulas require $u=w=z=v-z=0$. Since $z=a/10$, this forces $a=0$. Columns $1,2,3,5$ are then all positive, yielding **four** positive source columns (not three).

If $\nu_0,\nu_6>0$, three positive columns are possible **only if** $\nu_1=\nu_2=\nu_5=0$. But exactly

$$
\nu_1=13a/40+1/80-u,\qquad
\nu_2=(1-a)/2,\qquad
\nu_5=3a/40+21/80-w.
$$

These equalities force $a=1,\ u=27/80,\ w=27/80$ and hence $z=1/10$. The original remaining capacity bounds give $1/10\le v\le13/40$.

For every $v$ in that interval, direct substitution gives the three positive masses specified in the theorem, normalization to one, all capacities, both stopping-time equations, and the 21 exact Blackwell equations for the diagonal coupling. Thus the necessary conditions are sufficient, proving the **if-and-only-if classification**.

## 6. Further exact low-support interior family

At any interior point satisfying

$$
0<a<1,\quad
0<u<13a/40+1/80,\quad
0<w<3a/40+21/80,\quad
a/10<v<a/10+9/40,
$$

all six source columns $0,1,2,3,5,6$ are strictly positive. The diagonal coupling uses exactly six edges and is minimal, by the lower bound of one edge per active source column.

For example the rational pair

$$
x=y=(1,1/2,1,1/20,1/10,1/16,1/20)
$$

has source masses in column order $(0,1,2,3,5,6)$:

$$
(40589/648000,\ 1/8,\ 1/4,\ 82711/324000,\ 19/80,\ 45089/648000).
$$

This is a nonempty four-dimensional relative-open physical family of exact six-edge realizations.

## 7. Reproduction, BRC scope, and next question

`VERIFY.py` is the locally executed exact-rational SymPy source: it checks the rank-9 physical/equal-margin linear system, the complete five-parameter affine parameterization, both sign-forcing slacks, the whole minimizer's symbolic mass formulas, exact 21-row Blackwell equalities at both endpoints and one interior point, and the six-edge interior example. `EXACT_OUTPUT.txt` contains the actual local stdout and an explanatory provenance header. The **universal claim** is proved by Sections 2–5, rather than extrapolated from three numerical samples. No Lean or independent project review is asserted.

The methodological BRC content is an explicit, typed distinction between the auxiliary statistical observer and physical flow states. The physical observation fiber is resolved by **capacity signs** instead of discarding its unobserved residual. These statistical dimensions are not P000 spatial dimensions.

**Next research unit:** derive exact tangent-cone inequalities at the three-edge minimizer segment, test whether any non-diagonal Blackwell realization can leave the segment with 4–9 positive edges, and map the resulting legal lower-support strata to the already certified 14/15 boundary. Preserve the original frozen physical input and all provenance.

Source identity: `EM-DIRECT-C534A2 / TASK_RESEARCH`; research activity `RA-A797EAA416A7AF97A8A79E39`. Formal R5 Owner/CLAIM remains unconfirmed; this author-side evidence is not a Source Result or an independent review.


## 8. Stronger result: complete 3/4/5/6 support stratification of the physical equality locus

The four-dimensional lawful family from Section 4 admits a **complete exact minimum-support classification**. It is stronger than isolated rational witnesses. Write the same equality-family coordinates as

$$
x=y=(1,a,1,u,v,w,a/10),\quad
0\le a\le1,\quad
0\le u\le13a/40+1/80,\quad
0\le w\le3a/40+21/80,\quad
a/10\le v\le a/10+9/40.
$$

At every point of this family, equality of source and target margins makes the diagonal coupling feasible. The minimum number of positive edges equals **exactly the number of positive source columns**: each column needs an outgoing edge, while the diagonal coupling attains that bound. Moreover any coupling *attaining this minimum* is diagonal, because each source column then has a single edge, and distinct likelihood ratios force that edge to be $(j,j)$.

Define $c_1=13a/40+1/80-u$, $c_2=(1-a)/2$, $c_5=3a/40+21/80-w$. All three are nonnegative physical masses. There are exactly two cases.

**Case A (ordinary locus).** If at least one of $u,w,a/10,v-a/10$ is strictly positive, both $\nu_0$ and $\nu_6$ are strictly positive. The column-3 mass is always positive. Consequently the *exact global (over couplings for this pair) support count* is

$$
\boxed{m(x,x)=3+\mathbf1_{c_1>0}+\mathbf1_{c_2>0}+\mathbf1_{c_5>0}.}
$$

Each of the eight possible strict/zero patterns of $(c_1,c_2,c_5)$ is attainable in the lawful four-dimensional physical equality family. Thus the strata are nonempty and have the following **relative** dimensions inside the equality family: minimum-3 has dimension 1 (all three zero); minimum-4 has dimension 2 (exactly two zero); minimum-5 has dimension 3 (exactly one zero); minimum-6 has dimension 4 (none zero). Their indicated relative interiors give genuine nonempty cells/chambers of the equality-locus stratification.

**Case B (exceptional corner).** If $u=w=a/10=v-a/10=0$, then $a=u=v=w=0$ and the exact physical point is $x=y=(1,0,1,0,0,0,0)$. Here $\nu_0=\nu_6=0$ and precisely the four columns $(1,2,3,5)$ are positive, so $m(x,x)=4$. This is an *additional isolated zero-dimensional minimum-4 stratum*, not included in Case A.

Exact rational witnesses checked with the original 13 physical capacities, source normalization and all 21 Blackwell conditions include:

| Support minimum | Physical parameter tuple $x=y$ | Positive source columns |
|---|---|---|
| 3 | $(1,1,1,27/80,1/10,27/80,1/10)$ | $0,3,6$ |
| 4 (ordinary) | $(1,1,1,27/80,1/5,1/8,1/10)$ | $0,3,5,6$ |
| 4 (isolated) | $(1,0,1,0,0,0,0)$ | $1,2,3,5$ |
| 5 | $(1,1,1,1/5,1/5,1/8,1/10)$ | $0,1,3,5,6$ |
| 6 | $(1,1/2,1,1/20,1/10,1/16,1/20)$ | $0,1,2,3,5,6$ |

The finite checker STRATA.py and local execution output STRATA_OUTPUT.txt accompany the original global minimum proof and initial VERIFY.py. The universal classification is the source-column/diagonal martingale argument together with the complete sign partition above; the five explicit samples are exact witnesses of nonemptiness.

This establishes a **nested 1D–2D–3D–4D diagonal-support hierarchy**, plus an exceptional isolated 4-edge corner, using only the original frozen P/Q–BRC model and no new coordinate or observer assumptions. The next question is whether non-diagonal *nearby* physical pairs admit 4–9-edge couplings, and what tangent-cone crossings attach to these diagonal strata.
