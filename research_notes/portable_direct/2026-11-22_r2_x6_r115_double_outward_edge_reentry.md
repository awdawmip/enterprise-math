# X6 R115 — Two double-outward sharp-edge crossings re-enter seven strict near directions

Date: 2026-11-22 (Asia/Shanghai). Status: **AUTHOR_PROOF / EXACT_RATIONAL_REPLAY_PASS / NOT_INDEPENDENTLY_REVIEWED**.

## Scientific scope and antecedents

This is the **conditional four-positive-weight, six-pair BRC observation model** of R90–R114, not an assertion about physical heartbeat time dynamics. In the original signed integer difference chart (a=(x,y,z)), define

\[
q(a)=\max\left(\sum_i\max(a_i,0),\sum_i\max(-a_i,0)\right),
\quad u=x+3y+6z,\quad v=3x+12y+30z,\quad h=7x+39y+126z.
\]

For (w=(A,B,C,D)>0), set (t=(0,u,v,h)) and

\[
F_w(a)=\max_{0\le i<j\le3}\frac{|t_i-t_j|}{w_i+w_j},\qquad
\eta_p(w)=\min_{a\ne0,\,q(a)\le p}F_w(a),
\quad N_p(w)=\{\{\pm a\}:q(a)\le p,\,F_w(a)<3\eta_p(w)/2\}.
\]

All six pair observers are retained. Integer inversion identifies every nonzero direction modulo sign with the relative-height coordinates

\[
t=(0,\tau,3m,\tau+6n),\qquad
a=(10\tau-12m+3n,-5\tau+7m-2n,\tau+(n-3m)/2),
\]

where $\tau,m,n\in\mathbb Z$, $m\equiv n\pmod2$. The project R90 weight cone and R114 boundary/one-facet continuation are upstream conditional inputs. Physical placement here is the ordered lower-odd/lower-even pair (channels 1,2). Its Type-I first full-list Port is 28, and Type-II is 38. Sources: R90 exact cone journal, R114 author's research note, and R114 no-transverse-replacements continuation, all pinned in §Evidence.

## Theorem: simultaneous outward movement can restore seven directions

Fix a real (r>0). There exists (\varepsilon_0(r)>0) such that, for **every** (0<\varepsilon<\varepsilon_0(r)), the following exact classifications hold.

**Type I — intersection of facets (1-2s=0) and (18-Y=0).** Put

\[
s=\frac12+\frac\varepsilon2,\quad X=\frac{17}{4},\quad Y=18+r\varepsilon,\quad
w_I=(s,1-s,X-s,Y-s).
\]

Both facet functions are negative: $1-2s=-\varepsilon$ and $18-Y=-r\varepsilon$. For every integer $p\ge28$,

\[
\boxed{\eta_p(w_I)=\frac{12}{18+(r-1)\varepsilon}},\qquad
\boxed{|N_p(w_I)|=\begin{cases}10,&0<r<1,\\3,&r\ge1.\end{cases}}
\]

At (0<r<1) the complete ten representatives in relative-height coordinates ($\tau,m,n$) are

\[
(0,0,2),(0,1,-1),(0,1,1);
\quad(1,-1,-1),(1,-1,1),(1,1,-1),(1,1,1),
(1,0,-2),(1,0,0),(1,0,2).
\]

At $r\ge1$ only the first three (with $\tau=0$) survive.

**Type II — intersection of facets (1-2s=0) and (9-X=0).** Put

\[
s=\frac12+\frac\varepsilon2,\quad X=9+r\varepsilon,\quad Y=8,\quad
w_{II}=(1-s,s,X-s,Y-s).
\]

Again both facet functions are negative: $1-2s=-\varepsilon$, $9-X=-r\varepsilon$. For all integer $p\ge38$,

\[
\boxed{\eta_p(w_{II})=\frac6{9+(r-1)\varepsilon}},\qquad
\boxed{|N_p(w_{II})|=\begin{cases}10,&0<r<1,\\3,&r\ge1.\end{cases}}
\]

At (0<r<1) the ten representatives are

\[
(0,1,-1),(0,1,1),(0,2,0);
\quad(1,-2,0),(1,0,0),(1,2,0),
(1,-1,-1),(1,-1,1),(1,1,-1),(1,1,1).
\]

At $r\ge1$ precisely the first three survive.

Thus **the very same two outward facet signs do not determine the local direction count at a positive edge**. The ratio (r) of outward facet speeds is decisive: the two-edge path admits a seven-direction jump at (r=1). All ten directions belong to the corresponding original R90 twelve-template bank; this is **re-entry of previously excluded templates, not introduction of new outsiders**.

## Proof

### 1. Unrestricted minimum and Port stability

Write (L=A+B), (s_* = \min(A,B)), (X_*=C+s_*), (Y_*=D+s_*). In the ordered region (C>\max(A,B)), (D>\max(A,B)), the exact unrestricted minimum (R90, also derived by the parity cases of ($\tau,m,n$)) is

\[
\eta_\infty=\frac1T,\qquad
T=\max\left(L,\frac{X_*}{6},\frac{Y_*}{12},
\min\left(\frac{X_*}{3},\frac{Y_*}{6}\right)\right).
\]

Indeed $\tau\ne0$ costs at least (1/L) and its Port-11 witness realizes that value; when $\tau=0$, even (m,n) are bounded by the two pure witnesses (6/X_*,12/Y_*), and odd (m,n) by (\max(3/X_*,6/Y_*)), attained at ((m,n)=(1,1)). The additional CD gap is dominated by these pair bounds in this ordered region.

In Type I, once (s>1/2), (s_*=1-s), so
$X_*=17/4-\varepsilon$, (Y_*=18+(r-1)\varepsilon). At $\varepsilon=0$, (Y_*/12=3/2) strictly exceeds the other three comparison scales. Hence for all sufficiently small positive $\varepsilon$, (T=Y_*/12). The realizing pure direction is ($\tau,m,n$=(0,0,2)) with (q=7), so $\eta_p=\eta_\infty=12/Y_*$ for every $p\ge28$.

In Type II the same swap gives (X_*=9+(r-1)\varepsilon), $Y_*=8-\varepsilon$. At $\varepsilon=0$, (X_*/6=3/2) strictly exceeds the other three scales. Thus (T=X_*/6); the pure direction ((0,2,0)) has (q=27) and realizes (6/X_*) for every $p\ge38$.

### 2. Type-I finite, complete candidate bank

The strict cutoff equals (H_I=18/Y_*). For sufficiently small $\varepsilon>0$, (0<H_I<2). The AB pair forces $|\tau|<H_I<2$, so, modulo sign, $\tau=0$ or (1). The AC and BD observations give

\[
|3m|<XH_I \quad(X=17/4),\q\quad |6n|<Y_*H_I=18.
\]

For small $\varepsilon$ the first inequality gives $|m|\le1$; the second gives $|n|\le2$, with $m\equiv n\pmod2$.

For $\tau=0$, the nonzero possibilities modulo simultaneous sign are exactly the three displayed Type-I pure/odd templates. Their six-pair scores at $\varepsilon=0$ are strictly below the cutoff (1), so they remain included for sufficiently small $\varepsilon$.

For $\tau=1$, parity gives **exactly seven** candidates: $m=\pm1,n=\pm1$ (four) and (m=0,n=-2,0,2) (three). At $\varepsilon=0$ each has AB score exactly (1), while its other five pair scores are strictly below (1); this is checked directly by the displayed (t)-coordinates. Since the AB denominator is always (L=1), each candidate enters **iff** the strict cutoff exceeds (1):

\[
H_I>1 \Longleftrightarrow Y_*<18 \Longleftrightarrow (r-1)\varepsilon<0
\Longleftrightarrow r<1.
\]

The parity and pair bounds exhaust the entire infinite integer lattice, regardless of Port. All ten displayed directions have $q\le28$. This proves Type I for every $p\ge28$.

### 3. Type-II finite, complete candidate bank

The strict cutoff is (H_{II}=9/X_*). As above, (0<H_{II}<2) for small $\varepsilon$, so $\tau\in\{0,1\}$ modulo sign. The AC pair gives (|3m|<X_*H_{II}=9), hence $|m|\le2$. The BD pair gives (|6n|<8H_{II}), hence $|n|\le1$ when $\varepsilon$ is sufficiently small. Parity leaves, modulo sign, exactly three nonzero $\tau=0$ candidates, namely ((0,1,-1),(0,1,1),(0,2,0)), and exactly seven $\tau=1$ candidates, namely (m=-2,0,2) with (n=0), or $m=\pm1$ with $n=\pm1$.

All three $\tau=0$ scores are strictly below (1) at $\varepsilon=0$. For each of the seven $\tau=1$ candidates, the AB score equals (1) and every other pair score is strictly below (1) there. Hence, by continuity and the exact AB comparison,

\[
H_{II}>1 \Longleftrightarrow X_*<9 \Longleftrightarrow r<1.
\]

Their maximum Port is 38, proving the classification for all $p\ge38$. □

## Exact replay

A standalone pure-Python `fractions.Fraction` replay is preserved alongside this note. At $\varepsilon=1/100$, it checks (r=1/2,1,2) for both Types; for each it computes all six exact pair scores and the R90 unrestricted optimum, and **independently enumerates every integer triple with $q\le28$ or $q\le38$** (including both signs). It tests no triple improves the claimed optimum and compares the complete strictly-near set, not just its count, against the ten/three relative-height representatives.

Numerical results: Type I ((r=1/2,1,2)) has ($\eta,|N|$=(2400/3599,10),(2/3,3),(1200/1801,3)). Type II has ((1200/1799,10),(2/3,3),(600/901,3)). The independent raw enumeration visits respectively 77,196 and 190,266 nonzero oriented (q)-bounded triples per sample. The exact open-$\varepsilon$ result rests on the finite analytic candidate bound, not finite sampling.

## Evidence, limits and next scientific question

- Source model and exact cone/optimum: `awdawmip/enterprise-math`, R90 continuation `awdawmip/chatgpt-global-knowledge@6395fb2c:journal/enterprise-math/2026-11-22/x6-r90-exact-sharp-weight-regions.md`.
- Earlier geometric strata: `awdawmip/enterprise-math@77f99f46efd9273abff051558b932bc5a2e40a67:research_notes/portable_direct/2026-11-22_r2_x6_r114_positive_facet_edge_vertex_strata.md`.
- Earlier **one-facet** transverse theorem: `awdawmip/chatgpt-global-knowledge@05e4affa:journal/enterprise-math/2026-11-22/x6-r114-no-transverse-replacements.md`; current actual blob was read from canonical main on 2026-11-22.
- Current P000 V5, ACTIVE worldview and joint-relation preservation were read; this result preserves all six observer pairs and is typed as a conditional auxiliary BRC model, not a native Cell/Link/time-evolution transfer.
- New files: `x6_r115_double_outward_verify.py` and `x6_r115_double_outward_results.json` in the same directory. The proof is author-side and has **not** been independently reviewed or canonically admitted.
- Next: find and classify the remaining edge-corner path-dependent secondary rays, especially the Type-I `(1-2s,\,9+9X-2Y-18s)` and Type-II `(1-2s,\,9-18s-7X+9Y)` edge combinations. At a larger distance, classify the first genuinely new outsider beyond the original R90 twelve-direction banks; preserve Port-specific thresholds.
