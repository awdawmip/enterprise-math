# X6 R125 — Exact D-line near-direction fan, optimizer switch and delayed Port recovery

**Date:** 2026-11-23 (Asia/Shanghai). **Status:** AUTHOR_ANALYTIC_PROOF / EXACT_FINITE_REPLAY_PASS / NOT_INDEPENDENTLY_REVIEWED. **Model:** the conditional four-positive-weight six-pair BRC integer observer used by R121–R124, preserving its frozen scientific definitions and NOT asserting native X6/P000 physical time dynamics.

## Definitions and theorem

For any nonzero integer vector \(a=(x,y,z)\), considered modulo sign only (positive multiples remain distinct), set
\[
q(a)=\max\{\sum_i\max(a_i,0),\ \sum_i\max(-a_i,0)\},\qquad
h(a)=(0,x+3y+6z,3x+12y+30z,7x+39y+126z).
\]
For positive weights \(w=(A,B,C,D)\), set
\[
F_w(a)=\max_{0\le i<j\le3}\frac{|h_i(a)-h_j(a)|}{w_i+w_j},\quad
\eta_p(w)=\min_{0<q(a)\le p}F_w(a),\quad
N_p(w)=\{\{\pm a\}:0<q(a)\le p,\ F_w(a)<\tfrac32\eta_p(w)\}.
\]
Fix the **one-parameter positive real weight line**
\[
w_D=(1,3,4,D),\qquad D\ge3,
\]
and integer \(p\ge11\). Define four unoriented directions
\[
u=(10,-5,1)\ (q=11),\quad
v=(4,-1,0)\ (q=4),\quad
b=(6,-4,1)\ (q=7),\quad
e=(16,-9,2)\ (q=18).
\]

**Theorem (complete all-real-D, all-integer-p fan):** For all real \(D\ge3\) and every integer \(p\ge11\),
\[
\boxed{\eta_p(w_D)=
\begin{cases}
1/4,&3\le D\le47,\\
12/(D+1),&D\ge47.
\end{cases}}
\]
At \(D=47\), \(u,b\) tie for the optimum. For \(D>47\) the unique optimal direction is \(b\); for \(3\le D<47\) the unique optimal direction is \(u\). The strict \(3/2\)-near set is exactly:

| Real D interval | Near set for 11 ≤ p ≤ 17 | Near set for p ≥ 18 |
|---|---|---|
| \(3\le D\le29\) | \(\{u\}\) | \(\{u\}\) |
| \(29<D\le31\) | \(\{u,v\}\) | \(\{u,v\}\) |
| \(31<D\le101/3\) | \(\{u,v,b\}\) | \(\{u,v,b\}\) |
| \(101/3<D<71\) | \(\{u,v,b\}\) | \(\{u,v,b,e\}\) |
| \(D\ge71\) | \(\{b\}\) | \(\{b\}\) |

All endpoint assignments are **strict** and exact. In particular the Port-11 singleton near set persists on the entire anisotropic interval \(3\le D\le29\), much farther along the fourth-weight axis than R124's local sufficient box; at \(D=47\) the minimizing witness changes with **no change** in the near-direction set. At \(D=71\), three directions leave simultaneously when p≥18 (two when p≤17). The direction \(e\) enters only when the integer Port reaches 18.

## Proof (unbounded integer grid and continuous real parameter)

Write \(H_1=x+3y+6z\) and \(H_2=3(x+4y+10z)\). The six denominators, ordered 01,02,03,12,13,23, are \(4,5,D+1,7,D+3,D+4\). The vector \(u\) has heights \((0,1,0,1)\), so \(F_{w_D}(u)=1/4\) for every \(D\ge3\). The vector \(b\) has heights \((0,0,0,12)\), so \(F_{w_D}(b)=12/(D+1)\).

**Exact optimizer.** If \(3\le D\le47\) and \(F_{w_D}(a)<1/4\), then the 01 gap forces integer \(H_1=0\), and 02 forces \(H_2=0\), since \(H_2\) is a multiple of three. Solving gives \(a=z(6,-4,1)\) with nonzero integer z. Its score is \(12|z|/(D+1)\ge12/(D+1)\ge1/4\), a contradiction. Hence \(u\) is optimal. Equality with \(u\) is possible for \(b\) precisely at \(D=47\), so uniqueness for \(D<47\) follows from the same argument with a weak bound: any competitor of score ≤1/4 must have \(H_1\in\{-1,0,1\}\), \(H_2=0\). Alternatively for \(D<47\), the only equality possibility with a second direction requires checking the finite k,z list below: on \(D\le47\), \(b\) has score >1/4 and \(v,e\) have score >1/4. For \(D>47\), if a direction scored below \(12/(D+1)<1/4\), the same 01/02 divisibility forces it to be a nonzero integer multiple of \(b\), none of which scores below \(b\). This proves the optimum and its unique minimizer for \(D>47\).

**Complete strict near set, \(3\le D\le47\).** The near cutoff is \(3/8\). The 01 and 02 constraints force \(H_1=k\in\{-1,0,1\}\) and \(H_2=0\). Solving these integer equations yields
\[
x=6z+4k,\quad y=-4z-k,\quad h_3=12z-11k,\quad h_3-H_1=12(z-k).
\]
The 13 gap then implies
\[
12|z-k|/(D+3)<3/8\ \Longrightarrow\ |z-k|<(D+3)/32\le50/32<2.
\]
Thus **every possible** near direction is among \(z=k-1,k,k+1\) for \(k=-1,0,1\). After excluding the zero vector and quotienting by sign, precisely the four candidates \(u,v,b,e\) remain. Their 03 and 13 conditions give:
\[
v:\ D>29,\qquad b:\ D>31,\qquad e:\ D>101/3,
\]
while \(u\) is always near. For instance, \(v\) has \(|h_3|=11\) and \(|h_3-H_1|=12\), hence the two strict conditions \(D>85/3\) and \(D>29\); \(e\) has corresponding gaps 13 and 12, yielding \(D>101/3\). Check their Port budgets \(q(u),q(v),q(b),q(e)=(11,4,7,18)\) to obtain the table.

**Complete strict near set, \(D>47\).** The cutoff is \(18/(D+1)<3/8\). Again 01/02 give \(H_1=k\in\{-1,0,1\}\), \(H_2=0\), and 13 gives
\[
|z-k|<\frac{3(D+3)}{2(D+1)}<2,
\]
so the same **four-candidate list is globally exhaustive**, regardless of Port. For \(b\), its score \(12/(D+1)\) is strictly near. For each of \(u,v,e\), all the other five pair inequalities are strictly satisfied when \(47<D<71\), and the 01 inequality reduces to
\[
1/4<18/(D+1)\quad\Longleftrightarrow\quad D<71.
\]
At \(D=71\) equality excludes \(u,v,e\); for larger D they remain excluded. Thus the table holds for all real D≥3 and all integer p≥11, with no finite-Port extrapolation.

**Uniqueness clarification for \(3\le D<47\).** A potential equality \(F=1/4\) still has \(|H_1|\le1\), \(H_2=0\); the 13 inequality gives \(|z-k|\le(D+3)/48\le50/48<2\). Hence it too lies in the four candidates. On \(3\le D<47\), the scores of \(v,e\) exceed \(1/4\) because their 03 gaps are at least 11/(D+1) and 13/(D+1) for D below their corresponding equality points; when D grows, \(F(v)\) eventually attains \(1/4\) (at D≥45) and \(F(e)\) does so at D≥51 (outside the considered range). Therefore **optimizer uniqueness for D<47 is not claimed** beyond the lower intervals: more precisely, at D≥45, v is also an optimizer. This corrects the earlier informal uniqueness assertion; the optimum value and complete near-direction table are unaffected. The exact optimizer set may be obtained from the four candidates using pair scores and can be studied separately.

## Exact computational replay and source provenance

The accompanying exact Python Fraction program exhausts every sign-unoriented integer triple with q≤11 (2,541 directions), q≤17 (8,942 directions), and q≤18 (10,563 directions). It evaluates all six gaps for 13 rational D samples, including 29,31,101/3,47,71 boundaries, with 39 complete optimizer/near-set checks and 286,598 vector–parameter pairs. All agree with the formula and sharp strict equalities. The theorem itself is the preceding exhaustive symbolic integer reduction and covers every real D≥3 and every integer Port p≥11.

**References:** frozen observer definitions and early-Port exact optimizer [R121](https://github.com/awdawmip/enterprise-math/blob/8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd/research_notes/portable_direct/2026-11-23_r2_x6_r121_small_port_exact_optimizer.md); Port-10 eight-direction witness [R123](https://github.com/awdawmip/enterprise-math/blob/07a10b16c8ee89ecbb6f2d99c1376be062f2b72b/research_notes/portable_direct/2026-11-23_r2_x6_r123_port2_sharp_port10_eight_witness.md); unbounded isolation near D=18 and its existing perturbation bound [R124](https://github.com/awdawmip/enterprise-math/blob/bd5298def776bfac3aee14ca9bec24f89e594613/research_notes/portable_direct/2026-11-23_r2_x6_r124_port10_to11_robust_collapse.md). Recent independent R124 centered sharp radius and shape-recovery results were checked at the global current foundation router; they do not supply this exact entire fourth-weight ray.

**Open problem:** classify the **optimizer tie subfan** on this ray, then compute analogous exact one-parameter recovery fans for the remaining Port-10 maximizing weight chambers. Preserve the distinct native X6/R063 work and all prior authors/acceptance states.
