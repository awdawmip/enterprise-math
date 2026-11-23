# X6 R131 — explicit four-weight open stability boxes for two Port-10 eight-direction BRC chambers

Date: 2026-11-23. Status: **AUTHOR EXACT RATIONAL LEMMA / REPRODUCIBLE FINITE GAP EVALUATION / NOT INDEPENDENTLY REVIEWED**.
Applies only to the *conditional* four-positive-weight six-pair BRC observer, frozen at R121/R122, with **physical integer Port 10** and strict \(3/2\) nearness. It does not establish native X6 dynamics or modify P000.

## Model-independent positive-denominator lemma

Let a finite positive-denominator observer be
\[
F_w(a)=\max_j\frac{g_j(a)}{w_{i(j)}+w_{k(j)}},\qquad
\eta_w=\min_{b\in B}F_w(b).
\]
Here \(B\) is an **exact** finite optimizer bank and \(E\) is a set containing every candidate that could be strict near; every direction outside \(E\) has a uniform exclusion certificate. Fix \(w_0\in(0,\infty)^4\), \(\eta_0>0\), and let
\(N_0=\{a\in E:2F_{w_0}(a)<3\eta_0\}\).
Assume all \(a\in E\setminus N_0\) satisfy strict \(2F_{w_0}(a)>3\eta_0\).
Define the exact normalized gaps
\[
\rho_{\rm in}=\min_{a\in N_0}
\frac{3\eta_0-2F_{w_0}(a)}{3\eta_0+2F_{w_0}(a)},\quad
\rho_{\rm out}=\min_{a\in E\setminus N_0}
\frac{2F_{w_0}(a)-3\eta_0}{2F_{w_0}(a)+3\eta_0}.
\]
Then **for any** \(0\le\rho<\min(\rho_{\rm in},\rho_{\rm out})\), every positive four-weight \(w\) satisfying
\[
|w_i-w_{0i}|\le\rho w_{0i}\quad(i=1,2,3,4)
\]
has **exactly the same** strict near-direction set \(N_w=N_0\).

**Proof.** Each capacity \(s_j=w_i+w_k\) lies between \((1-\rho)s_j^0\) and \((1+\rho)s_j^0\). Therefore
\(F_0(a)/(1+\rho)\le F_w(a)\le F_0(a)/(1-\rho)\) for every direction; taking the minimum over the same exact bank yields \(\eta_0/(1+\rho)\le\eta_w\le\eta_0/(1-\rho)\).
For a previously near row,
\[
\frac{F_w(a)}{\eta_w}\le
\frac{F_0(a)}{\eta_0}\frac{1+\rho}{1-\rho}<3/2
\]
by the definition of \(\rho_{\rm in}\).
For a previously non-near row in \(E\),
\[
\frac{F_w(a)}{\eta_w}\ge
\frac{F_0(a)}{\eta_0}\frac{1-\rho}{1+\rho}>3/2
\]
by \(\rho_{\rm out}\).
All directions outside \(E\) stay excluded by their preexisting weight-independent domination witness. Thus the entire set, not merely its count, stays fixed. QED.

## Two exact applications to newly completed R129 and R130

The R121 18-row bank and R122 20-row near envelope satisfy the lemma's premises for every positive four-weight. Exact six-gap \`Fraction\` evaluation of **all 20 envelope rows** gives:

| Base weights \(w_0\) | \(\eta_0\) | \(|N_0|\) | Worst inside row / exact ratio \(F/\eta\) | \(\rho_{\rm in}\) | Worst outside row / exact ratio \(F/\eta\) | \(\rho_{\rm out}\) |
|:---|:---|---:|:---|---:|:---|---:|
| (136,8,176,185) | \(1/48\) | 8 | (7,-1,0), \(160/107\) | **\(1/641\)** | (3,-4,1), \(36/23\) | \(1/47\) |
| (722,465,240,48) | \(1/96\) | 8 | (3,3,-1), \(720/481\) (also (7,-8,2)) | **\(1/961\)** | (2,-4,1), \(128/57\) | \(85/427\) |

Consequently the exact sets established in R129 and R130 survive under **simultaneous independent perturbation of all four positive weights**, respectively whenever
\[
\boxed{|w_i-w_{0i}|\le\rho(w_0)_i,\quad
0\le\rho<1/641 \ \text{ for } w_0=(136,8,176,185)}
\]
and
\[
\boxed{|w_i-w_{0i}|\le\rho(w_0)_i,\quad
0\le\rho<1/961 \ \text{ for } w_0=(722,465,240,48).}
\]

This is a **certified sufficient radius**, not a claim of the maximal transverse stability box. The two base sets are different (R129: 184<D<304; R130: 0<D<243/5). Unlike one-dimensional D-line stability, each bound tolerates simultaneous changes in A,B,C,D.

## Checkable exact arithmetic and scope

For any row \(a\) compute \(h(a)\), then six integers \(g_{ij}\) and
\(F_{w_0}(a)=\max_{ij}g_{ij}/((w_0)_i+(w_0)_j)\) using exact rational cross-products. Compute \(\eta_0\) over all R121 bank rows, and classify all R122 envelope rows by \(2F<3\eta_0\). Obtain the two minima above by exact Fraction arithmetic; no interpolation or floating point is involved. In particular, \((3\eta-2F)/(3\eta+2F)\) for \(F/\eta=160/107\) simplifies to \(1/641\), while for \(F/\eta=720/481\) it simplifies to \(1/961\).

Sources: [R121 fixed bank](https://github.com/awdawmip/enterprise-math/blob/8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd/research_notes/portable_direct/2026-11-23_r2_x6_r121_small_port_exact_optimizer.md); [R122 exact exclusion envelope](https://github.com/awdawmip/enterprise-math/blob/0687aa24f5402da3b35f914dd6907967a9805b94/research_notes/portable_direct/x6_r122_small_port_near_exclusion_certificate.json); [R129](2026-11-23_r2_x6_r129_class_iii_port10_D_ray.md); [R130](2026-11-23_r2_x6_r130_class_iv_port10_D_ray.md).

Unresolved: find **sharp** correlated four-weight stability boundary by solving the exact ratio inequalities rather than only the common relative perturbation bound. Mathematical independent review and any native Source Result remain separate.