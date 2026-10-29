# EC49AQ — exact global causal optimum by a truncated-polytope certificate

Date: 2026-10-30 (Asia/Shanghai). Author-side portable continuation of EC49AP PR #1724, commit `5a4067ce27d95685f21087aebe0b468660eeb891`. Status: `AUTHOR_ANALYTIC_PROOF / TWO_EXACT_FRACTION_CHECKS_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED`.

## Theorem (exact scope)

In the fixed **auxiliary strictly positive 18+18-leaf BRC** model, let hidden `w∈{0,1,2}`, initially observed `u∈{0,1}`, and optional sensor observation `z∈{0,1,2}`, with `η=1/25`. Put
[
t(w,u)=	frac12+(2u-1)(1-w)eta,qquad
P(w,u,z)=t(w,u)egin{cases}1/6&z=w,\\1/12&z
e w,end{cases}
qquad Q(w,u,z)=t(w,u)/9.
]
At `w` choose action `c∈{A0,A1,B0,B1,STOP}` with conditional probabilities `x[w,c]`, costs `(1,1,2,2,0)`, row sums 1 and expected first cost `43/48` (so `Σ cost(c)x[w,c]=43/16`). Then `w` is **erased**. After observing only `(c,u)`, use an independent behavioral purchase coin `r(c,u)∈[0,1]` to reveal `z`, with exact expected sensor cost `C2=13/16`. Terminal acceptance may use only the realized observations and independent behavioral coins. Set `α=P(accept)`, `β=Q(accept)`, and `H=α−(177/172)β`.

**For every such legal real-valued causal policy,**
[
oxed{Hle rac{77}{688},qquad H_{max}=rac{77}{688}.}
]
An explicit rational legal policy below attains equality. Thus EC49AP's fixed-cost interval `77/688≤Hmax≤1875833/16649600` is closed **inside this auxiliary probability model**.

## Proof I — exact observation and BRC support

For a paid action `c<4` and observed `u`, define
[
q_z(c,u)=x[z,c]t(z,u)/3,quad T(c,u)=sum_{z=0}^2q_z(c,u),quad
V(c,u)=rac1{172}sum_{z=0}^2[43q_z(c,u)-16T(c,u)]_+.
]
The purchased observation `(c,u,z)` has masses `P=(T+q_z)/4` and `Q=T/3`, so its positive support contribution to `α−(177/172)β` is `[43q_z−16T]_+/172`. Without purchasing, the observable `(c,u,no_sensor)` has equal P and Q masses, so its optimal acceptance is zero. STOP likewise carries no positive unpurchased discrimination.

The paid mass is
[
c(x)=sum_{c<4,u}T(c,u)=rac13sum_{w,c<4}x[w,c].
]
The **full-purchase support envelope**
[
F(x)=sum_{c<4,u}V(c,u)
]
is convex in `x`: each summand is the positive part of a linear form. For any legal purchase fractions and terminal decisions,
[
Hlesum_{c<4,u}r(c,u)V(c,u)le F(x),qquad
C_2=sum_{c<4,u}r(c,u)T(c,u)le c(x).
]
Consequently, all legal real causal strategies are bounded by `max_{x∈P_cut}F(x)`, where
[
P_{mathrm{cut}}={xge0: sum_cx[w,c]=1 (w=0,1,2),sum_{w,c}operatorname{cost}(c)x[w,c]=43/16,sum_{w,c<4}x[w,c]ge39/16}.
]
No hidden-state access, shared persistent random seed, or sensor-purchase dependence on erased `w` appears in this reduction.

## Proof II — complete finite exact vertex certificate

A continuous convex function on the compact polytope `P_cut` attains its maximum at a vertex. Every original first-cost polytope vertex has **exactly four** positive coordinates: three row-sum equalities plus one cost equality have rank four; a support of three would force an integer cost, contradicting `43/16`. Thus its support has one mixed row and two deterministic rows. Exhaustive rational enumeration yields **168 distinct original vertices**, of which **24** satisfy `c(x)>13/16`, all with `c(x)=43/48`. None lies on `c(x)=13/16`.

At the new paid-mass boundary `Σ_{w,c<4}x[w,c]=39/16` there are five linear equalities (three row sums, first cost, paid mass). A new vertex therefore has at most five positive entries; support of four would already be an original first-cost vertex on the cutoff, which does not exist. Enumerate **all** (inom{15}{5}=3003) five-coordinate supports, solve the corresponding five-by-five rational system, and retain only unique strictly positive solutions. This produces **144** boundary vertices. Independently, all (inom{15}{4}=1365) four-coordinate systems reproduce the 168 originals.

A direct exact rational evaluation of purchased leaf masses `P(c,u,z),Q(c,u,z)` at the **168 vertices of `P_cut`** gives
[
max_{	ext{24 high originals}} F=rac{12177}{137600}
<rac{77}{688},quad
max_{	ext{144 cutoff vertices}}F=rac{77}{688},
]
with **24 cutoff vertices** attaining the latter maximum. All enumeration, Gaussian elimination, P/Q computations, and comparisons use Python standard-library `Fraction`, not floats, sampling or tolerances. The separately executed edge-intersection checker regenerates 168 original vertices, 924 original edges, 144 boundary crossings and the same two maxima. Hence `F(x)≤77/688` for every real `x∈P_cut`; the theorem follows from Proof I.

## Attaining policy and exact source check

Take
[
x[0]=(0,3/16,1/4,0,9/16),qquad
x[1]=(1,0,0,0,0),qquad
x[2]=(0,1,0,0,0).
]
Buy the sensor for every positive-mass paid `(c,u)`; accept precisely when `(c,z)∈{(A0,1),(A1,2),(B0,0)}`, independently of `u`. Row sums, `C_1=43/48`, `C_2=13/16`, causal erasure and independent behavioral randomness are satisfied. Exact source-leaf summation gives
[
alpha=rac{25}{64},qquad eta=rac{13}{48},qquad
alpha-rac{177}{172}eta=oxed{rac{77}{688}}.
]
Both source populations have 18 strictly positive normalized leaves.

## Validation, evidence and interpretation boundary

`VERIFY.py` and `VERIFY_EDGE.py` are two **author-side**, differently structured exact implementations (support-matrix elimination with direct P/Q leaves; edge traversal with BRC q/T support). Both were actually executed; their captured reports are `EXACT_REPORT.json` and `EDGE_REPORT.json`. The edge checker also exports a full list of 168 rational vertex-support evaluations. Finite completeness relies on the stated rank/support polytope argument, not on a numerical grid. This is **not** independent mathematical peer review or Lean proof assistant certification.

The carrier is a positive probability BRC observer with declared `(c,u,z)` readout and one-step future-operation horizon. No theorem is asserted for native signed/phase BRC, six-dimensional native X6, a three-dimensional native slice, or heartbeat dynamics. A transfer would require a typed state/observer/operation-preserving bridge respecting P000 and ACTIVE residual-fidelity premises; no protected file was modified.

**Next scientific problem EC49AR:** determine the maximal open `η` interval around `1/25`, with `C1=43/48,C2=13/16,k=177/172` fixed, on which the same rational prefix and terminal decision rule remain globally optimal, using parameter-aware support polytopes and exact sign-breakpoint certificates. Alternatively compute the first rational counterexample to persistence of the optimizer. The model's native-transfer obligation remains separate.
