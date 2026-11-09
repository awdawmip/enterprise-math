# R5 — Generic exact 15-edge necessity in the physical 8D chamber and an explicit rational counterexample

Date: 2026-11-10 (Asia/Shanghai). Scope: **author-side mathematical result / exact rational computation**, independent review and canonical admission pending.

## Frozen source/model

Reuse the seven likelihood-ratio P/Q-BRC auxiliary Blackwell model, mass map, two stopping-time functionals, allowed capacities, and the physical (g=b) / seedless-F restrictions **without changing any frozen scientific input**. Exact predecessors: PR #1894 (positive 30-edge lawful matched-time physical pair), PR #1902 (separately proved specific 15-edge physical counterexample and a 1D interval), PR #1913 (exact 8D physical marginal affine hull). Frozen science pointers recorded in #1913: account `a01383f825ef9d43b4b754254303298c64041568`; enterprise-math `86149263e38c22292c9def1e0f69092efa1be77e`. Current behavior/control rules are not scientific input pins. Seven LR labels are statistical outcomes, not P000 native spatial axes.

Ratios: `r=(1/10,1/2,3/4,1,5/4,3/2,19/10)`.
Source `X=(g,a,b,u,v,w,z)`, target `Y`; `nu=M(X)`, `mu=M(Y)`. Frozen equalities are `X_g=X_b; Y_g=1; Y_z=Y_a/10; T1(X)=T1(Y); T2(X)=T2(Y)`. Every physical capacity slack is as in the reproduced verifier. Transport columns are
`C_(i,j)=(unit_i[7],unit_j[7],r_i unit_j[7])`, with 30 allowed edges: columns `j=0,6` only their diagonals, columns `j=1,2,3,5` all seven rows. Nonnegative weights must satisfy all 21 Blackwell equations. This is the **exact frozen finite Blackwell carrier**, not a claim about unrestricted transports or other physical models.

## Main theorem — full-dimensional physical generic 15-edge necessity

Let `P` be the 8D affine image of the lawful matched-time physical parameter family in `(mu,nu)`, as computed in #1913. Let `U` be its nonempty relatively open Blackwell-feasible chamber containing a strictly positive 30-edge rational transport and with `nu_j>mu_j` for each `j=1,2,3,5`, and `nu_0,nu_6>0`.

**Theorem.** The union of physically feasible marginal pairs in `U` admitting a coupling with at most 14 positive edges has 8D Lebesgue measure zero. Consequently, **almost every** physical marginal pair in `U` has exactly 15 as its minimum positive Blackwell edge count. The generic assertion is about the stated **physical 8D affine chamber** and actual nonnegative Blackwell couplings.

### Proof of the 14-edge support obstruction

The ambient feasible normalized 30-edge marginal space has affine dimension **10**: two normalization equations, LR-moment conservation, and `nu_4=0` in 14 marginal coordinates. The exact 21x30 transport-column matrix has rank **15**, hence every feasible transport polytope has a vertex using at most 15 positive edges.

Inside the ambient 10D affine space, the physical affine hull has dimension **8** and exactly two further independent affine equations
[
 A(mu)=36mu_0+28mu_1+23mu_2+18mu_3+13mu_4+8mu_5-18=0,
]
[
 B(mu,
u)=-36mu_0-36mu_1-31mu_2-18mu_3-5mu_4
 +36
u_0+36
u_1+31
u_2+18
u_3=0.
]
The verifier checks the independent rank-six family and the exact nonzero physical eight-minor `-19799371/47239200`.

Consider any support `S` admitting a **strictly positive** coupling for a marginal in `U`. Because source columns 0 and 6 have the two extreme LR values, their positive masses force `(0,0),(6,6)` into `S`. In each of the four internal columns `j=1,2,3,5`, the strict deficit `nu_j>mu_j` implies an off-diagonal positive edge. Martingale balance then forces edges strictly below and strictly above `r_j`, so the four column-wise martingale-defect linear forms are nonzero and have disjoint supports. Together with normalization, they have rank 5 on any such `S`. In particular `dim Aff(image(S))<=|S|-5<=9`.

We next show that **no nonzero combination `aA+bB` is an identity on all normalized martingale couplings supported by `S`**. Let `A_e` and `B_e` be its homogeneous coefficients on edge `e=(i,j)`, after replacing the constant -18 by -18 times total mass. If `aA+bB=0` on the entire normalized support solution space, elementary row-space duality yields, for all `e in S`,
[
a A_e+b B_e=kappa+lambda_j(r_i-r_j).
]
At `(0,0)` and `(6,6)` the defect is zero and `B_e=0`, while `A_{00}=18` and `A_{66}=-18`; hence `a=kappa=0`. Since `nu_1>mu_1`, positive non-diagonal mass in column 1 demands both `(0,1)` and some `(i,1)`, `i\ge2`. At `(0,1)`, `B_{01}=0` and `r_0-r_1\ne0`, forcing `lambda_1=0`. For each `i=2,...,6`, `B_{i1}` is respectively `5,18,31,36,36`, all positive; the upper edge therefore forces `b=0`.

If the physical affine hull `P` were contained in the normalized marginal image affine hull of `S`, some nonzero normal to the at-most-9D image in the 10D ambient space would have to be a nonzero combination of `A,B`. The preceding calculation excludes this. Thus for every such `S`, `P ∩ Aff(image(S))` is a **proper affine subspace** of the physical 8D space, of dimension at most 7. There are finitely many supports of size at most 14; their union has 8D measure zero. The universal 15-edge vertex bound gives the stated generic exact minimum. QED.

## New constructive theorem — a completely explicit rational physical pair requiring exactly 15 edges

The preceding generic theorem is strengthened by a **fully rational, finite-form witness**, which does **not** enumerate supports.

Write `p_0=(X,Y) in Q^14` for the exact legal positive 30-edge base point in #1913, reproduced in `VERIFY.py`. Let `v_1,...,v_8 in Q^14` be the exact tangent vectors from the free-variable nullspace basis of the five frozen physical equalities, with free-variable indices `(0,1,2,4,5,6,7,8)` in the order
`(Xu,Xv,Xw,Xz,Yb,Yu,Yv,Yw,Yz)`. The verifier prints all 8 vectors and checks their observable images have rank 8.

The affine physical candidate is
[
p(t)=p_0+sum_{k=1}^{8}t^k v_k.
]
Let `h(t) in Q[t]^21` be the corresponding Blackwell equation right-hand side `(mu(t),nu(t),(r_j nu_j(t))_{0<=j<=6})`. For each allowed edge let `C_e in Q^21` be the frozen transport column. Define the **explicit integers**
[
Q=operatorname{lcm}\{\operatorname{denom}(x):x 	ext{ is an entry of } C_e
  	ext{ or of any coefficient of } h(t)\},
quad
B_*=max(1,\max|Qx|),
]
[
H_*=15!\,B_*^{15},qquad
oxed{t_*=(4H_*)^{-1}}.
]
Exact execution gives
[
oxed{Q=1148267016000000,qquad B_*=5741335080000000}
]
so `H_*` has 249 decimal digits, and `t_*` has a 250-digit denominator. The expression defines **one specific rational number**, not an existential or transcendental choice.

**Rational separation lemma.** Fix any support `S` with `|S|<=14`, and let `r=rank(C_S)<=14`. If `h(t)` is not identically in `span_Q(C_S)`, there exists a nonzero `(r+1)x(r+1)` minor polynomial `P_S(t)` of `[C_S|h(t)]` after taking a rank-`r` column basis and suitable rows. Since only the final column depends on `t`, `deg P_S<=8`. Multiply each entry by `Q` to make the polynomial's coefficients integers. By the Leibniz determinant bound, each coefficient has modulus at most `(r+1)! B_*^{r+1}<=H_*`.

For a nonzero integer polynomial `P(t)=sum_{k=m}^8 a_k t^k` with lowest nonzero coefficient `|a_m|>=1` and all `|a_k|<=H_*`, at `t=t_*` its higher terms divided by `t_*^m` have total modulus at most `H_* t_*/(1-t_*)<1`. Hence `P(t_*)!=0`. This statement is **uniform over all supports**; no enumeration and no unproved numerical solver result is used.

For any support `S` that could realize `p(t_*)` with at most 14 positive edges, the strict margins at `p(t_*)` enforce the same forced edges and defects as in the main theorem. Its marginal image does not contain `P`. Since the 9 coefficients `h(0), [t]h(t),...,[t^8]h(t)` span the affine 8D physical hull, `h(t)` is not identically in `span(C_S)`. The separation lemma therefore gives `h(t_*)\notin span(C_S)`, a contradiction.

Finally, **positive feasibility** is certified directly by rational computation. The 30-positive coupling `E_0` at `p_0` has minimum edge weight `1/10^7`. Exact 15-pivot right inverses lift all eight physical directions to rational coupling directions `W_k`, preserving all 21 equations, so
[
E(t)=E_0+sum_{k=1}^8t^k W_k.
]
The exact verifier establishes `max_e sum_k |(W_k)_e|=535/52`, `min` nonmandatory capacity slack `=7/2000000`, maximum capacity-slope absolute sum `=27`, minimum of four strict deficits `=654982477/81785400000`, and maximum deficit-slope absolute sum `=17/2`. Since `0<t_*<2/10^20` and `t_*^k<=t_*`, all 30 coupling entries, physical capacities and four deficits remain strictly positive wherever required. The verifier **also substitutes the exact rational `t_*` itself** and checks all 21 identities and nonnegative slacks.

Therefore the fully specified **rational** physical pair `p(t_*)` satisfies the frozen `g=b`, seedless-F, capacity and matched stopping-time constraints, is Blackwell feasible, and has
[
oxed{\min_E |\operatorname{supp}(E)|=15}.
]
This independently settles the proposed universal 14-edge bound in the negative within the frozen seven-LR physical model, while #1902 already supplied an earlier exact single-point counterexample.

## BRC interface and provenance

The carrier is the 30 labeled source-to-target LR branch transports; the observer `(X,Y) -> (mu,nu)` discards one physical-flow kernel and retains an 8D observable image. The proof uses exact branch identities, column-wise martingale defects, a finite support family, rational determinant heights and an observer-fiber argument. Branch labels, source columns, target rows and positive masses are never collapsed without an explicit invariant. Reuse class: `REUSE_APPLIED` to the pinned physical mass map and BRC labeled transport; theorem strength: author-side exact derivation backed by `Fraction` execution.

## Reproduction and next research

Run `python3 VERIFY.py` using Python standard library only. It verifies all model equations, exact 8D rank certificate, all transport equalities, 30-edge base and constructed rational positivity, uniform height separation parameters, and the key forced-edge score identities. `EXACT_OUTPUT.txt` is the actual output of that execution.

New question: classify **the full dimensional regions where the exact minimum is 13, 14 or 15** within the frozen 8D physical marginal hull; find small-denominator rational 15-edge witnesses by optimizing certificate height and chart adjacency. Independent proof review, native activity checkpoint and formal Result require their separately authorized control routes.