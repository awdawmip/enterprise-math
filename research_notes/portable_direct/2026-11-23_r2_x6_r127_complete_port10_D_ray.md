# X6 R127 — Complete Port-10 D-ray: five optimizer regimes and six strict-near chambers

**2026-11-23 (Asia/Shanghai).** Status: `AUTHOR_ANALYTIC_PROOF / EXACT_FRACTION_REPLAY_PASS / NOT_INDEPENDENTLY_REVIEWED`. This is an exact continuation of [R126](https://github.com/awdawmip/enterprise-math/blob/6b08a576137fe2b34c44d0fe8e89d26711479e6f/research_notes/portable_direct/2026-11-23_r2_x6_r126_other_maximizer_D_fan.md), extending its Port-10 result from `900<=D<=1300` to the **entire real half-ray `D>=900`**. The existing independent [R126 later-Port ray](https://github.com/awdawmip/chatgpt-global-knowledge/blob/e8b1a5cb721a85514d21cb6c25d72f69dc4fca4c/journal/enterprise-math/2026-11-23/x6-r126-full-later-port-D-ray.md) instead addresses integer Port `p>=11`; it is not duplicated here.

## Exact observer and claim

For an integer triple `a=(x,y,z)!=0`, identify `a` with `-a` only (positive multiples are distinct), let

\[
q(a)=\max\big(\sum_i\max(a_i,0),\sum_i\max(-a_i,0)\big),\quad
h(a)=(0,x+3y+6z,3x+12y+30z,7x+39y+126z).
\]

For four positive weights `w=(A,B,C,D)`, use **all six pair observations**

\[
F_w(a)=\max_{0\le i<j\le3}\frac{|h_i(a)-h_j(a)|}{w_i+w_j},\quad
\eta_p(w)=\min_{0<q(a)\le p}F_w(a),\quad
N_p(w)=\{\{\pm a\}:0<q(a)\le p,\ 2F_w(a)<3\eta_p(w)\}.
\]

Fix `p=10`, `w_D=(48,577,240,D)` and **every real `D>=900`**. The six denominators, in pair order `01,02,03,12,13,23`, are `625,288,D+48,817,D+577,D+240`.

**R127 optimizer theorem.** The exact optimal value is

\[
\boxed{
\eta_{10}(D)=
\begin{cases}
1/96,&900\le D\le1008,\\
11/(D+48),&1008\le D\le5771,\\
12/(D+577),&5771\le D\le6923,\\
1/625,&6923\le D\le7452,\\
12/(D+48),&D\ge7452.
\end{cases}}
\]

All formulas agree on overlaps. There are optimizer changes of *functional form* at `1008,5771,6923,7452`. The `5771` switch is caused by a **13-pair** constraint taking over from 03 on the same optimizer `v`; thus a projection that retains only the 03 denominator would give the wrong middle segment. For `1008<D<7452`, `v=(4,-1,0)` is the unique minimizing direction. At `D=7452`, `v` and `b=(6,-4,1)` tie; for `D>7452`, `b` is the unique minimizer. At `D=1008`, the R126 five-row tie applies.

Define the initial six-row set

\[
S_0=\{(1,0,0),(4,-1,0),(5,-4,1),(5,-1,0),(6,-4,1),(9,-5,1)\}/\pm
\]

and `r=(9,-2,0)`, `t=(1,-3,1)`, `v=(4,-1,0)`, `b=(6,-4,1)`.

**R127 complete strict `3/2`-near fan.**

| Exact real D interval | Full Port-10 strict-near set | Count |
|---|---|---:|
| `900<=D<=912` | `S0` | 6 |
| `912<D<=976` | `S0 + r` | 7 |
| `976<D<6096/5` | `S0 + r + t` | 8 |
| `6096/5<=D<1536` | `S0 + r` | 7 |
| `1536<=D<11202` | `{v,b}` | 2 |
| `D>=11202` | `{b}` | 1 |

Here `+` means set union, and all displayed triples are unoriented. At the critical equalities `6096/5`, `1536`, and `11202`, a strict inequality becomes equality and the outgoing direction(s) are excluded. **At D=1536 exactly five directions leave simultaneously**, leaving only `v,b`; at `D=7452` the optimizer changes with no near-set jump.

## Infinite-half-ray analytic proof

**1. Integer reduction and the exact optimum.** Write `H1=x+3y+6z=k`, `H2=3(x+4y+10z)`. When `H2=0`:

\[
x=4k+6z,\quad y=-k-4z,\quad H3=12z-11k=k+12t,\quad t=z-k,
\]
\[
a=(10k+6t,-5k-4t,k+t),\qquad H3-H1=12t.
\]

**Integral isolation lemma (reused from R126, proof reproduced).** For `q(a)<=10`, `H2=0`, `|k|<=6` and `a!=0`, necessarily `|H3|>=11`. Otherwise `|k+12t|<=10` implies `t in {-1,0,1}`. If `t=0`, `a=k(10,-5,1)`, with Port `11|k|>10` unless zero. If `t=1`, `k+12<=10` forces `k<=-2`; already at `k=-2`, `a=(-14,6,-1)` has Port 15, and decreasing `k` increases the Port. If `t=-1`, the symmetric case `k>=2` has Port at least 15. Contradiction.

The two available short witnesses are

\[
v=(4,-1,0),\quad h(v)=(0,1,0,-11),\quad
F_D(v)=\max\{1/625,11/(D+48),12/(D+577)\},
\]
\[
b=(6,-4,1),\quad h(b)=(0,0,0,12),\quad F_D(b)=12/(D+48).
\]

For `D>=1008`, `F_D(v)<=1/96`. Every other Port-10 direction has one of four cases:

- `H2!=0`: its 02 score is at least `3/288=1/96`.
- `H2=0`, `|k|>=7`: its 01 score is at least `7/625>1/96`.
- `H2=0`, `k=0`: it is an integer multiple of `b`, and `q<=10` leaves just `±b`.
- `H2=0`, `1<=|k|<=6`: the lemma gives `|H3|>=11`. Moreover `t!=0` (otherwise Port is at least 11), so the 13 gap is `12|t|>=12). Consequently its score is at least `max(1/625,11/(D+48),12/(D+577))=F_D(v)`.

Hence **globally across all Port-10 integer triples**,
\[
\eta_{10}(D)=\min\{F_D(v),F_D(b)\}\qquad (D\ge1008).
\]
Exact comparison yields the four later formula branches above. The first branch `900<=D<=1008` is the already proved R126 optimizer `1/96`.

**2. R126 range and reduction to seven rows.** For `900<=D<=1300`, the R126 complete Port-10 eight-row certificate and monotonicity proof give the first four near-set phases, including `6096/5`. At `D=1300`, the seven active rows are `S0+r`.

For `1300<=D<=5771`, `eta=11/(D+48)`. For each fixed integer direction, all six ratios `F_D(a)/eta(D)` are nondecreasing in `D`: the three fixed-denominator terms grow linearly; 03 stays constant; 13 and 23 contain increasing ratios `(D+48)/(D+577)` and `(D+48)/(D+240)`. Thus no new row enters, and all near rows remain among the same seven. Substituting the exact six-gap integer vectors of these seven rows shows that five of them have `|H2|=3` and stay strict only while

\[
3/288<\tfrac32\,11/(D+48)
\iff D<1536.
\]

All their other constraints hold through that point; the other two rows `v,b` are strict throughout. Consequently `S0+r` remains intact for `1300<=D<1536`, and `N_{10}(D)=\{v,b\}` for `1536<=D<=5771`.

**3. Exhaustiveness beyond D=5771.** For every `D>=5771`, the optimum is nonincreasing and at most `1/529`. Thus its strict near cutoff is at most `3/1058<2/625` and also below `3/288`. Every strict-near direction must satisfy `H2=0` and `k=H1 in {-1,0,1}`. Since `eta<=F_D(b)=12/(D+48)`, its 03 gap satisfies `|H3|<18`. But `H3=k+12t`, hence `t in {-1,0,1}`. Up to global sign, these choices yield only `b`, `v`, `u=(10,-5,1)`, or `e=(16,-9,2)`; the last two have Ports 11 and 18, respectively, and are infeasible at Port 10. **Therefore only `v,b` can ever be near for any later real D.** The vector `b` is always strict near. The vector `v` is optimal through `D=7452`; beyond that, its constant 01 gap is the limiting inequality:

\[
F_D(v)<\frac32\eta(D)
\iff\frac1{625}<\frac{18}{D+48}
\iff D<11202.
\]

This proves all intervals and endpoint conventions, with no sampling-to-infinity inference.

## Exact replay and provenance

The standalone [Python Fraction checker](x6_r127_complete_port10_D_ray_verify.py) independently enumerates **all 1,935** sign-unoriented integer triples of Port at most 10 and evaluates **all six pair gaps**, using 27 rational D values around all critical boundaries (52,245 direction–parameter comparisons). It asserts both the exact optimal value and the **complete membership set**, not merely a count. Locally executed: `PASS` on all 27 snapshots; the checker prints a JSON report with minimizers and exact rational values. Analytic proof establishes the continuous D-ray theorem.

Frozen scientific provenance: P000 V5 and the all-six-pair conditional observer as in R121–R126. All prior results and formal/native X6 Task status are preserved. Independent review and strict Activity observation audit remain separate. This result newly closes the **Port-10** full D-ray, not the previously completed **Port>=11** R126 continuation.

**Next unit:** seek the exact full ray of a third Port-10 maximizing weight chamber, or classify which optimizer-switch faces preserve strict near-set cardinality under transverse perturbation.
