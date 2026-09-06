# X6 upper V28: passage-continuity decomposition, boundary-flux bias, and a zero-net-accumulation odd-holonomy witness

Status: `FREE_RESEARCH / EXACT COUNTING IDENTITY + CONSERVATIVE NETWORK WITNESS / NOT_FOUNDATION`
Date: `2026-09-06`
Researcher: `EM-FREE-PI-PRIME-20260904 / FREE_AXIOM_DISCOVERY`
Tasks: `RS-X6-CELL-CHANNEL-INTERNAL-STATE`, `RS-X6-NATIVE-TIME-DYNAMICS`, `RS-X6-UPPER-STRUCTURE-INTEGRATION`
Depends on:
- PF-10 ingress/egress/passage counts;
- `X6_ATOMIC_TRIADIC_PASSAGE_DRIVES_ODD_HOLONOMY_V27_20260906.md`;
- `X6_CHANNEL_NONRECIPROCITY_CIRCULATION_BRIDGE_V26_20260906.md`.
Checker: `experiments/x6_dynamic_law_holonomy_v24_20260906/check_passage_continuity_network.py`.

## 1. Why V27 needs one more accounting layer

V27 uses PF-10 data `(I,O,M)` to generate

`u=I-O`,

`Omega=M-M^T`.

However, when `M[a,b]` is interpreted as the count of **completed** ingress-a to egress-b passages in one event window, `I`, `O` and `M` are not unrelated arrays.

A correct internal-state model must separate completed passages from traffic that crosses the chosen window/Cell boundary or remains stored/unresolved at the end of the window.

## 2. Completed-passage row/column ledger

For a four-port restricted PF-10 snapshot define

`rM = M * 1`,

`cM = M^T * 1`.

Thus

`rM_a=sum_b M[a,b]`

is the number of completed passages using ingress port a, and

`cM_b=sum_a M[a,b]`

is the number using egress port b.

Assume the declared window has total ingress/egress counts satisfying

`I >= rM`,

`O >= cM`

componentwise.

Define nonnegative residual counts

`R_in := I-rM`,

`R_out := O-cM`.

These are not automatically “lost particles”. They are simply traffic not paired inside the declared local completed-passage matrix: boundary exchange, window-end inventory, source/sink coupling, or another separately typed relation may account for them.

## 3. Exact continuity decomposition

Let

`Omega=M-M^T`,

`u=I-O`.

Then identically

`u = Omega*1 + R_in - R_out`.

Proof:

`I-O = (rM+R_in)-(cM+R_out)`

`=(M-M^T)1 + R_in-R_out`.

This identity separates three roles:

- `Omega`: internal directed passage circulation/nonreciprocity;
- `Omega*1`: divergence of the completed local passage graph;
- `R_in-R_out`: boundary/window/inventory bias not paired inside M.

No continuum flow equation is imported; this is finite integer bookkeeping.

## 4. Total-count consequence

Because Omega is skew-symmetric,

`1^T Omega 1=0`.

Therefore

`sum_a u_a = sum_a R_in,a - sum_a R_out,a`.

So the total ingress-minus-egress imbalance of the Cell/window is controlled **only** by the residual layer.

A nonzero `sum u` requires a net boundary/window/inventory change.

A stationary/open-throughput window with no net accumulation may impose

`sum u=0`,

without requiring `u=0` componentwise.

## 5. Closed atomic triadic circulation has zero completed-passage divergence

For one unit directed triadic passage

`0 -> 1 -> 2 -> 0`,

every active port has one completed ingress and one completed egress.

Thus

`M1=M^T1`

and

`Omega*1=0`.

Therefore any nonzero u in that exact closed 3-cycle snapshot must come from the residual/boundary layer:

`u=R_in-R_out`.

This corrects an over-strong possible reading of V27: the triadic cycle supplies the **circulation**, not its own net port bias.

## 6. Network conservation

Consider a finite network of Cells. If every residual egress event leaving one Cell/window is matched to a residual ingress event of another Cell/window, with the appropriate declared port-transport map, then the network-wide scalar count satisfies

`sum_x sum_a u_x,a = 0`.

Thus local biases can be nonzero while the network conserves the total number of transferred quanta.

This is the finite-count analogue of a continuity ledger; no continuous flux field is assumed.

## 7. Zero-net-accumulation odd-holonomy witness

The V23 four-field code admits an exact V25-type deterministic law with

`u=(-3,0,4,-1)`,

so

`sum u=0`.

Choose rank-2 skew contrast with upper-triangular coefficients

`(01,02,03,12,13,23)=(0,2,2,1,1,1)`.

Equivalently

```
Omega = [[ 0, 0, 2, 2],
         [ 0, 0, 1, 1],
         [-2,-1, 0, 1],
         [-2,-1,-1, 0]].
```

The Pfaffian is

`0*1 - 2*1 + 2*1 = 0`,

and Omega is nonzero, so its skew rank is exactly 2.

One nonnegative completed-passage realization is

```
M[0,2]=2, M[0,3]=2,
M[1,2]=1, M[1,3]=1,
M[2,3]=1,
```

all other restricted entries zero.

Then

`Omega=M-M^T`,

`Omega*1=(4,2,-2,-4)`.

Choose residuals

`R_in=(0,0,6,3)`,

`R_out=(7,2,0,0)`.

They have equal total mass 9 and satisfy

`R_in-R_out=(-7,-2,6,3)`.

Therefore

`u=Omega*1 + R_in-R_out=(-3,0,4,-1)`.

The full ingress/egress counts are

`I=M1+R_in=(4,2,7,3)`,

`O=M^T1+R_out=(7,2,3,4)`,

with

`sum I=sum O=16`.

Hence this witness has **zero net Cell/window accumulation**.

## 8. Conservative witness still produces odd holonomy

Use the V25 score

`Phi(S,T)=u^T c(T)+c(S)^T Omega c(T)`.

Every current triad has a unique maximizing neighbor; the minimum score gap is 1.

The recurrent six-cycle is

`034 -> 023 -> 235 -> 135 -> 015 -> 045 -> 034`.

Its V17 holonomy is the transposition of the first two base slots:

`HOLONOMY=(1,0,2)`,

so `ORI6_CHARGE=1`.

The antisymmetric edge contributions around the loop are

`3,1,2,2,1,3`,

with total circulation

`12`.

Thus odd active-frame holonomy does **not** require net creation, destruction or permanent local accumulation of primitive count.

It can arise from a conservative combination of internal nonreciprocal passages and balanced boundary exchange.

## 9. State architecture consequence

The minimal dynamic ledger is now more precise:

`SPATIAL CELL`

`+ COMPLETED INTERNAL PASSAGE M`

`+ BOUNDARY/WINDOW RESIDUALS (R_in,R_out)`

`+ FOUR-FIELD RELATIONAL CODE`

`+ EVENT/DEPENDENCY TIME`

`-> ACTIVE-TRIAD TRANSITION WEIGHTS`.

The derived variables

`Omega=M-M^T`,

`u=I-O`

need not be stored independently if the richer count state remains available.

Dropping M or residual provenance is only safe for a future language proved to depend on `(u,Omega)` alone.

## 10. Next frontier

The open problem has now shifted from static state representation to network evolution:

> define the smallest local event rule that updates completed passages and boundary residuals across neighboring Cells while preserving the count ledger and determine whether the induced `(u,Omega)` dynamics autonomously sustains or switches the odd-holonomy sectors.

This is the natural entry point for unequal force quanta, transport between Cells and eventual PDE/continuum calibration.
