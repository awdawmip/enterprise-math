# R5 — Exact Blackwell lifting of the entire two-parameter early side-flow rectangle

Author-side research note, 2026-11-07 (Asia/Shanghai). Frozen science inputs: GLOBAL `a01383f825ef9d43b4b754254303298c64041568`, Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`. Current behavioral rules read separately. Scientific predecessor: immutable `8231237c0863b6fb9d4c394f753e3f6480dc156f`, `research_notes/brc_r5_symmetric_high_v_blackwell_slab_20261107_t2042/` (especially `SIDE_FLOW_U_MAX.md`). This note is a proof in the fixed four-stage seven-key P/Q-BRC stopping experiment, not a claim about a native X6 physical dynamics.

## New all-real theorem

Let the seven likelihood-ratio keys be `r=(1/10,1/2,3/4,1,5/4,3/2,19/10)`. For **every** real `(p,q) in [0,1]^2` and **every** real terminal declaration `d in [0,1]^7`, the FULL_HIST flow

`x(p,q)=(g,a,b,u,v,w,z)=(1,1,1,27p/80,9/40,27q/80,0)`

admits one legal **seedless LR** flow `y(p,q)` and one nonnegative row-stochastic seven-key Blackwell kernel `K(p,q)` such that its transformed declaration `d'=K(p,q)d` has exactly the same four observations `(e_P,e_Q,T_P,T_Q)` as `(x,d)`. The matched stopping times are

`T_P=129/40 + 27p/160 + 81q/160`, `T_Q=129/40 + 27p/80 + 27q/80`.

The FULL_HIST historical residual is `9*b*z-4*a*(v-z)=-9/10` throughout this rectangle, except that its history is observed through side flows; it is strictly negative even when `p=q=0`. The theorem covers the entire continuous side-flow rectangle, rather than two isolated maximal-side corners.

## Four exact seedless corner flows

Use corner order `(p,q)=(0,0),(1,0),(0,1),(1,1)`. The corresponding legal seedless flows, in order `(g,a,b,u,v,w,z)`, are:

- `y00=(1,9/10,9/10,13/800,117/400,13/800,9/100)`;
- `y10=(686/705,686/705,659/705,1233/3760,347/1128,0,343/3525)` (previously published exact `u` certificate);
- `y01=(1,4/5,1,7/200,61/200,129/400,2/25)` (new);
- `y11=(1,14/15,1,379/1200,191/600,359/1200,7/75)` (new).

Every corner satisfies `z=a/10` and `v-z=9b/40`, hence satisfies the seedless equation `9bz=4a(v-z)`. These *linear* identities, along with the convex flow inequalities, survive convex combinations.

Each corner has a seven-by-seven **Q-mass transport** `Q^corner` from the seedless experiment (`rows`, key `i`) to the FULL_HIST experiment (`columns`, key `j`). Every entry not listed here is zero. Write `i:j=fraction` for `Q[i,j]`:

```
Q00: 0:0=67/720; 0:1=8477/360000; 1:1=23/80;
     2:1=1523/100000; 2:3=3477/100000;
     3:1=20201/1800000; 3:3=31207/450000; 3:5=20201/1800000;
     4:3=3477/100000; 4:5=1523/100000;
     5:5=23/80; 6:5=8477/360000; 6:6=67/720.
Q10: 0:0=20443/72000; 0:3=9977/1184400; 0:5=16277/2961000;
     3:3=421271/1692000; 4:3=9/470;
     5:3=3677/658000; 5:5=102899/329000;
     6:5=16277/846000; 6:6=6943/72000.
Q01: 0:0=6943/72000; 0:1=76/1875; 1:1=19/80;
     2:1=169/3125; 2:3=287/6250; 3:1=101/18750;
     3:3=67039/300000; 6:3=287/22500; 6:6=20443/72000.
Q11: 0:0=10343/36000; 0:3=22/1875; 2:3=1/30;
     3:3=93019/270000; 5:3=1/30;
     6:3=167/67500; 6:6=10343/36000.
```

## Proof for all real parameters and all declarations

Let `M_i(f)` be the frozen model's affine Q stopping mass at key `r_i`. At each corner `c`, direct Fraction identities (checkable in `VERIFY.py`) establish, for all `i,j`:

`Q^c_ij >= 0; sum_j Q^c_ij = M_i(y_c); sum_i Q^c_ij = M_j(x_c); sum_i r_i Q^c_ij = r_j M_j(x_c)`.

The last two are the calibrated Blackwell transport identities. Also `T_P(y_c)=T_P(x_c)` and `T_Q(y_c)=T_Q(x_c)`, all corner flows are legal, and all stop masses are normalized with first moment one.

For arbitrary real `p,q in [0,1]`, define

`h00=(1-p)(1-q), h10=p(1-q), h01=(1-p)q, h11=pq`.

All `h` are nonnegative and sum to one. Define `y(p,q)=sum_c h_c y_c` and `Q(p,q)=sum_c h_c Q^c`. Since the source corner flows share fixed `(g,a,b,v,z)=(1,1,1,9/40,0)` and differ only in `u,w`, `sum_c h_c x_c = x(p,q)` exactly. Stop masses and stopping times are affine in the seven flow coordinates, so the four equations in the previous paragraph survive the same bilinear convex interpolation. Legal flow bounds are linear and preserved. The seedless equalities `z=a/10` and `v-z=9b/40` likewise survive, proving `9bz=4a(v-z)` without assuming convexity of the full nonlinear seedless family.

For every input row `i` with `M_i(y)>0`, set `K_ij=Q_ij/M_i(y)`; set `K` to the identity row where `M_i(y)=0`. The row identities make `K` stochastic and ensure `d'=Kd` lies in `[0,1]^7` for every real declaration vector. Then

`sum_i M_i(y)d'_i = sum_j M_j(x)d_j = e_Q(x,d)`, and

`sum_i r_i M_i(y)d'_i = sum_j r_j M_j(x)d_j = 1-e_P(x,d)`.

Together with stopping-time equality these give exact four-observer equality for every real `p,q,d`, including all boundary and irrational cases. **QED.**

## Executed exact validation and scope

`VERIFY.py` is standalone, using only Python's `fractions.Fraction` and `itertools`. The run captured in `EXACT_OUTPUT.txt` checked: 4 precise corner certificates; 7 Q row sums, 7 Q columns and 7 weighted-P columns per corner; positivity, legal flow inequalities, bilinear seedless constraint, exact two stop times; all 128 binary declarations at each corner (512 in total); and 25 additional exact bilinear parameter samples. The all-real statement follows from the analytical convex-combination argument above rather than finite sampling.

The proof establishes a full two-parameter subset of the four-observer image of FULL_HIST inside the seedless LR image under arbitrary declarations. It adds the `w>0` and jointly `u,w>0` corners to the prior `u`-only and zero-side results. The full R5 mother problem (all legal FULL_HIST flows and declarations) remains open; independent review and native Source admission remain pending. GitHub author-side publication gives durable proof/evidence but does not grant CLAIM or ownership.
