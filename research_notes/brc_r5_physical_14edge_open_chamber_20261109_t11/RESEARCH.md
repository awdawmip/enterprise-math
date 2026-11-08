# R5 — an exact 14-edge affine transport chart on a nontrivial physical open chamber

**Date:** 2026-11-09 (Asia/Shanghai). **Status:** author-side theorem, exact rational/Fraction validation; no independent review or formal Result. **Frozen scientific inputs retained:** GK `a01383f825ef9d43b4b754254303298c64041568`, EM `86149263e38c22292c9def1e0f69092efa1be77e`. Applicable behavioral rules separately resolved at GK main `402fa789b9a0b00f3a2341aca44ced8c46f94a02` and EM main `b16f4211a17218df38ca647fa8d15fc02aeda6dd`. Direct predecessor: PR #1839, immutable commit `bede5ad6f9624b476bae9df16578509f598afe22`, `RESEARCH.md` and `VERIFY_PHYSICAL_SHARPNESS.py` read by the author of this note.

## Question and model

The open question from PR #1839 is whether `g=b` physically lawful FULL_HIST sources admit a uniform 14-edge seedless Blackwell coupling, or whether some pair needs 15. This note establishes a **positive-dimensional, explicit 14-edge region** and an exact support chart; it makes neither global alternative claim.

Fix the seven LR nodes
[
r=(1/10,1/2,3/4,1,5/4,3/2,19/10).
]
For a seven-flow vector (f=(g,a,b,u,v,w,z)), use exactly the Q-mass map (M_i(f)) and the stop-time maps (T_P,T_Q) in predecessor #1839; these formulas are reproduced verbatim in `VERIFY_14_CHAMBER.py`. Write (
u=M(x)) for source, (mu=M(y)) for target. The Blackwell equations are
[
sum_j E_{ij}=mu_i,quad
sum_i E_{ij}=
u_j,quad
sum_i r_i E_{ij}=r_j
u_j,quad E_{ij}ge0.
	ag{1}
]
The matrix is Q-weighted, and the last equations make the conditional LR mean equal to the source LR node.

Restrict to source (b=g) and target on the seedless F face:
[
x=(g,a,g,u,v,w,z),quad
y=(G,A,B,U,A/10+9B/40,W,A/10),
]
where the two exact stop-time equalities determine
[
U=-17A/40-19B/80-G/2-T_P(x)+3T_Q(x)/2-1/2,
]
[
W=-7A/40-39B/80-G/2+T_P(x)-T_Q(x)/2-1/2.
	ag{2}
]
The independent parameter vector is (p=(g,a,u,v,w,z,G,A,B)inmathbb R^9).

## Theorem A — a universal exact affine 14-edge chart for this restricted affine family

Set
[
d_1=
u_1-mu_1,quad d_2=
u_2-mu_2,quad
d_3=mu_3-
u_3,quad d_5=
u_5-mu_5.
]
Define
[
alpha=(10d_2-5d_3)/23,quad
eta=(13d_2-18d_3)/23,quad
gamma=mu_6-
u_6-2d_1/9,quad
delta=mu_4-eta,quad
eta=d_5-delta-gamma.
	ag{3}
]
For **every real** (p), with (x,y) as in (2), the following signed 14-entry array satisfies *all 21 equalities* (1):
[
egin{array}{c|rrrrrrrrrrrrrr}
(i,j)&(0,0)&(0,1)&(1,1)&(6,1)&(0,2)&(2,2)&(3,2)&(4,2)&(3,3)&(0,5)&(4,5)&(5,5)&(6,5)&(6,6)\
hline
E_{ij}&
u_0&7d_1/9&mu_1&2d_1/9&alpha&mu_2&d_3&eta&
u_3&eta&delta&mu_5&gamma&
u_6
end{array}.
	ag{4}
]
All other entries vanish, in particular column 4 because (
u_4=(g-b)/2=0).

**Proof:** Equations (2), the predecessor's exact affine (M,T_P,T_Q), and (3) show that each residual in (1) is affine in the nine entries of (p). The attached Fraction checker evaluates all 21 residuals at (p_0) and the nine independent (p_0+e_k). All 210 residual values are **exactly zero**; affine linearity proves (1) for every real (p), including irrational parameters. Algebraically, the column-1 split follows from ((r_1-r_0)/(r_6-r_0)=2/9); the column-2 split follows from its mass and LR moment equations, and the remaining row/column balances fix (gamma,delta,eta). The 14 restricted columns are linearly independent (direct elimination), making the solution on this support unique.

Consequently, when both flows are physically lawful, the 14 quantities in (4) are all nonnegative **if and only if this specific 14-edge support gives a valid Blackwell transport**. Strict positivity defines an explicit open polyhedral chamber in the nine-parameter affine family; these conditions concern the fixed chart, not other possible supports.

## Theorem B — a fully explicit nine-parameter real box with 14 positive edges

Let
[
p_0=(999/1000,1/6,1/20,29/240,11/160,1/120,871/1000,9/40,5/6).
]
For every real (p) satisfying
[
oxed{|p-p_0|_inftyle 1/10000,}
	ag{5}
]
the source and target (2) are lawful, target is seedless, both times match, and **all 14 entries** in (4) are strictly positive. Thus the entire real nine-parameter box has a declaration-independent 14-edge Blackwell kernel.

**Exact proof of uniform nonnegativity:** List each nontrivial physical-capacity inequality, each source/target nonzero Q mass and all 14 entries as an affine slack (s(p)); the checker constructs this finite set explicitly. For each (s), compute (s_0=s(p_0)) and (L_s=sum_{k=1}^9|s(p_0+e_k)-s(p_0)|) with `Fraction`. Then
[
s(p)ge s_0-10^{-4}L_s>0
]
for every (p) in (5). In fact the smallest exact (s_0/L_s) among all tested inequalities is
[
oxed{585/3227428>1/10000},
]
attained at (E_{4,2}), where (s_0=13/18400) and (L_s=806857/207000). The fixed equalities (b=g, z'=A/10, v'-z'=9B/40) remain equalities by construction. At the center (min E_{ij}=109/360000). Every numerical comparison in this certificate is rational and exact.

**Geometry:** Fixing (z=1/120) and varying the other eight parameters, the affine map
[
plongmapsto(mu_0,ldots,mu_4,
u_0,
u_1,
u_2)
]
has the exact nonzero (8	imes8) determinant
[
-1111424393/139968000000.
]
Therefore the physically realized pair-observer image contains an eight-dimensional open patch (relative to its affine hull) where the *same fixed 14-edge pattern* is valid. This is stronger than an isolated 14-edge example.

## Verification and evidence

Run `python -S VERIFY_14_CHAMBER.py` using Python's standard-library `fractions.Fraction`. The script reproduces the frozen source mass/time maps, constructs the transport, checks 21 identities at 10 affine basis points, verifies all physical inequalities over the explicit nine-dimensional box by exact (L^1)-slope bounds, and repeats the predecessor's eight-dimensional determinant calculation. `EXACT_OUTPUT.txt` contains the actual executed local output.

No MIP/float solution is used in this proof. The typed BRC carrier is the Q-edge mass table, seven labeled LR nodes, source/target Q histograms and exact column-weighted LR moments. Preservation is relative to the declared terminal-declaration/stop-time observer; no native-X6 dynamic or Foundation claim is made. The existing exact transport method is **REUSE_APPLIED**; this work specializes its support geometry instead of creating another top-level tool.

## Next discriminating unit

Extend this exact-chart method to other 14-edge supports and determine whether their **nonnegative chambers cover every lawful feasible (g=b) marginal pair**. An explicit lawful pair outside *all* such chambers, with exact infeasibility certificates for every at-most-14 support, would prove a physical 15-edge requirement. A full chamber cover would prove a uniform 14-edge theorem. Independently, the author-side all-flow feasibility stitch in PR #1831 still requires external independent mathematical replication.

**Control status:** portable author-side research evidence, not a Task CLAIM, formal Result, Driver review, Working Truth or Foundation promotion. No protected worldview change.
