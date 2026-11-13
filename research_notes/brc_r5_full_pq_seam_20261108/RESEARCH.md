# R5: Extended all-real five-parameter full physical capacity prism to t <= 1/40

Date: 2026-11-08. Status: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

Source scientific pins retained from preceding R5 research: global `a01383f825ef9d43b4b754254303298c64041568`, Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`. Normative snapshot separately read: global main `a8d14be2e722c5a25314d242439567ba60ca5639`, EM main `b62110008321d9147212cb89f2627ff613c2550d`. This is an internal result in the fixed seven-node P/Q-BRC terminal-observer model; P000 and the ACTIVE worldview are unchanged. Source predecessor: Draft PRs #1817 and #1819. The initial version of this branch covered t <= 1/50; the present exact certificate strengthens the same theorem to t <= 1/40, preserving the earlier proof in Git history.

## New theorem (complete five-parameter real box)

Let $t,p,q,\theta,\kappa$ be arbitrary real numbers in

$$
0\le t\le 1/40,\qquad 0\le p,q,\theta,\kappa\le1.
$$

For the lawful FULL_HIST source

$$
x=(1,t,1,(13t/40+1/80)p,9\kappa/40+t\theta/10,
(3t/40+21/80)q,t\theta/10),
$$

there exist a lawful seedless target $y=(g',a',b',u',v',w',z')$ and a nonnegative 7-by-7 Blackwell matrix $E$, independent of the terminal declaration, satisfying

$$
\sum_j E_{ij}=M_i(y),\qquad
\sum_i E_{ij}=M_j(x),\qquad
\sum_i r_i E_{ij}=r_j M_j(x),
$$

for all $i,j=0,\ldots,6$, with

$$
r=(1/10,1/2,3/4,1,5/4,3/2,19/10),\quad
T_P(x)=T_P(y),\quad T_Q(x)=T_Q(y).
$$

Therefore every randomized seven-node terminal declaration is transported to a declaration with exactly the same $(e_P,e_Q,T_P,T_Q)$. All real endpoints and irrational parameters are included.

## Exact finite-law Blackwell/convex-order bridge

Write (\mu_f=\sum_i M_i(f)\delta_{r_i}) for the (Q) LR law. The seven masses obey (\sum_i M_i(f)=\sum_i r_iM_i(f)=1) for each lawful flow.

For any two lawful flows (x,y), a nonnegative (E) with the three sets of row/column/moment identities above exists **if and only if** the following five scalar inequalities hold:

$$
H_k(y)\ge H_k(x),\quad
H_k(f)=\sum_{i=0}^6(r_i-r_k)_+M_i(f),\quad k=1,2,3,4,5.
$$

Necessity follows from conditional Jensen, since (E) couples a target LR (Y) with a source LR (X) and $\mathbb E[Y\mid X]=X$. Conversely, linear interpolation on the ordered finite support expresses every convex function (modulo an affine function) as a nonnegative combination of the five interior hinge functions. The inequalities plus the equal masses/means give $\mu_x\preceq_{cx}\mu_y$. The finite-support martingale coupling theorem (Strassen) supplies (E) with precisely these marginals and conditional mean. Source: L. Leskelä and M. Vihola, *Conditional convex orders and measurable martingale couplings* (*Bernoulli*, 2017), arXiv:1404.0999, and the finite-support formulation in Econlib Probability Order Strassen DiscreteGeneral, https://lean4.party/docs/Econlib/Probability/Order/Strassen/DiscreteGeneral.html . This is an application of an established theorem, not a claim of new Strassen theory.

Every hinge is affine in the seven flow coordinates. Consequently, the existence condition is a **five-linear-inequality certificate** for this model, instead of carrying 49 nonnegative transport entries for each point. The full verifier `VERIFY.py` independently checks all five hinges, legal capacities, normalizations, seedless relation, and both stop times using Python `Fraction`.

## New exact G/F seam

For $p,q\in[0,1]$ let

$$
s_{00}=s_{11}=3/4,\quad s_{01}=9/10,\quad s_{10}=1/2,
$$
$
S(p,q)=\sum_{i,j\in\{0,1\}}s_{ij}p^i(1-p)^{1-i}q^j(1-q)^{1-j},
\qquad h(t,p,q)=1-40t\bigl(1-S(p,q)\bigr).
$$

Thus $1/2\le h\le1$.

* For $0\le\kappa\le h$, set $\lambda=\kappa/h\in[0,1]$. Construct the target by multiaffine interpolation of the rational `G` vertices in `VERIFY.py`. The common linear seedless face is (a'=z'=0).
* For $h\le\kappa\le1$, set (\lambda=$\kappa-h$/(1-h)\in[0,1]) when (t>0). Construct the target from the rational `F` vertices, on the common face $z'=a'/10,\ v'-z'=9b'/40$. At (t=0), (h=1), the source is already seedless and its identity target lies on the F face.

For each chart use the independent parameter cube ($t,p,q,\theta,\lambda$\in[0,1/40]\times[0,1]^4), with $\kappa_G=\lambda h$ or (\kappa_F=h+\lambda(1-h)). **The source is separately affine in all five chart variables**: products such as $tp,tq,t\theta,t p q\lambda$ remain separately affine. At (t=0) exact identity targets suffice. At (t=1/40), `VERIFY.py` records 16 exact G targets and 16 exact F targets, for all ($p,q,\theta,\lambda$\in\{0,1\}^4).

The program checks each vertex precisely, including all five hinge inequalities. Given chart coordinates $z_1,\ldots,z_5$ normalized to ([0,1]), take (W_v=\prod_i$z_i\text{ if }v_i=1\text{ else }1-z_i$). Define $y=\sum_vW_v y_v$. Since all y vertices of one chart belong to the same linear seedless face, their nonnegative mixture is lawful and seedless. Every mass, hinge and stopping-time functional is affine in the seven flow coordinates, so the equalities/inequalities also interpolate. Finite Strassen then provides a Blackwell matrix at every real point.

The two charts jointly cover the complete physical ($p,q,\theta,\kappa$) cube at $0\le t\le1/40$. On the seam either chart gives an admissible, potentially different, target. This gives the exact all-real statement.

## Exact verification

`VERIFY.py` is standalone stdlib-only and reconstructs the Q masses from the fixed calibration. It includes the exact 32 rational (t=1/40) targets plus the (t=0) identity vertices. It checks 64/64 chart vertices and 151 deterministic rational interior tests. Output captured in `EXACT_OUTPUT.txt`. An additional independent local SymPy/SciPy exploratory/exactification pass actually reconstructed explicit nonnegative rational 7-by-7 transports for all 32 nontrivial vertices (301 positive edges total); this transport experiment is a cross-check. The published full-real proof uses the exact finite hinge certificate and Strassen theorem; it does not rely on the floating LP search.

## Next local unit

1. Test (t=1/30) and the four ((p,q)) physical corners across candidate seams; derive an exact new seam or sharply state a particular chart's failure.
2. Check whether the present 32 target families yield a sparse constructive analytic martingale-transfer formula, and compare cost versus the existing 32-corner transport reconstructions.
3. Obtain independent mathematical review of the full-box theorem and reconcile its scope with upstream R5 mother-question admission. The R5 FULL_HIST model outside $t\le1/40$ remains the larger objective.

Scientific status is author-side proof and exact computation. GitHub persistence and PR review are distinct from formal Task CLAIM, Result and independent mathematical admission.