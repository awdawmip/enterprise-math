# R762GU — Exact signed STAR readout lattice, BRC fibers and reachable-state growth

Date: 2026-11-20 (Asia/Shanghai). Research task: `RS-X6-TRIADIC-CLOSURE-DYNAMICS` / immutable publication `TP2-8B7E13C5904A2D6F1142`. Frozen scientific taskbook: `enterprise-math@857280d1012943290d141d1317179c40ec3cbdf8`; frozen P000: `enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`. Continuation: R762GT in Draft PR #2843@27e2dcf7ec6bfdb5a3fba527f7845b8609c2df4a. Independent mathematical review: **NOT_REVIEWED**.

## Scope and exact alphabet

Use the *constructed* eight-letter signed K4 STAR candidate alphabet of R762GT, rather than asserting a native event admission. Four vertices `v=0,1,2,3`; six named native-axis labels in order `E=(01,02,03,12,13,23)`. Let `H_v` be the six-entry 0–1 incidence column for the three edges meeting vertex `v`. A candidate letter `T_(v,s)`, `s=+1,-1`, denotes three signed primitive force components carried as a **composite triadic readout** `s H_v` from a chosen Cell anchor. It is not a primitive diagonal spatial step. An ordered word `w` has length `m`, signed net vertex inventory `z_v=#(v,+)-#(v,-)`, and six-axis signed Cell readout `y=Bz=\sum_v z_v H_v`. Each source word has positive integer BRC mass 1. The word remains the source object even when an observer compresses its readout.

This is a finite-alphabet combinatorial extension under P000; no Port/Link legality, physical time step or actual `TRIADIC_CLOSURE_E` transition is assumed. Event count `m` is an ordering index, not the independent P000 time coordinate. The statements below apply to the free candidate language or to a gate that happens to admit *all* eight letters independently of state/history.

## Theorem 1. Exact integral image-lattice and parity obstruction

Writing `y=(a,b,c,d,e,f)=(y01,y02,y03,y12,y13,y23)\in Z^6`, there exists `z\in Z^4` with `y=Bz` **if and only if** all three conditions hold:

\[
\boxed{e=c+d-b,\qquad f=c+d-a,\qquad a+b+d\equiv0\pmod2.}
\]

If they hold, `z` is **unique**, given by

\[
z_0=(a+b-d)/2,\quad z_1=(a+d-b)/2,\quad
z_2=(b+d-a)/2,\quad z_3=c-z_0.
\]

Consequently the integer image of `B` has index **2** in the rank-four sublattice of `Z^6` cut out by the two linear equalities. For example `(1,0,0,0,0,-1)` satisfies both equalities but fails the parity condition; it has no integral signed STAR lift.

**Proof.** Each edge `uv` has entry `y_uv=z_u+z_v`. Solve the 012 triangle for `z0,z1,z2`, use the 03 edge to solve for `z3`, and substitute into edges 13,23. Integrality of the reconstructed triangle is equivalent to `a+b+d` even; if it is even, all four displayed `z` are integral and substitution proves existence. This also establishes uniqueness. Without the parity condition the same two equalities give a rank-four integer lattice on which the indicated parity is surjective, witnessed by the displayed odd example. Thus the image has index 2.

The 12 full-rank four-axis selections from R762GT (triangle plus pendant edge) also recover the signed `z` from their named axis values; fewer than four named axis values cannot recover `z` for all signed integer inventories. This is safe **for the specified additive net-cell observer and its future free-alphabet updates**: six-axis future net readouts are reconstructed via the same `B`. It is not a certificate for forgetting ordered source words, multiplicities, Port gates or future history-dependent observations.

## Theorem 2. Exact length-constrained reachability

Let `y\in Z^6`, `m\in Z_{\ge0}`. Some ordered word of exactly `m` candidate signed STAR letters has net Cell readout `y` **if and only if**:

1. `y` satisfies the three Theorem 1 image-lattice constraints, giving unique `z`;
2. `m\ge\|z\|_1=\sum_v|z_v|`;
3. `m-\|z\|_1` is even.

In particular the shortest candidate word reaching a legal signed readout `y` has exactly `\|z\|_1` letters; later lengths have the same parity and are reached by inserting opposite-sign source pairs.

**Proof.** If `n_v^+` and `n_v^-` are the letter counts, then `z_v=n_v^+-n_v^-` and `m=\sum_v(n_v^++n_v^-)=\|z\|_1+2\sum_v\min(n_v^+,n_v^-)`. This establishes necessity. For sufficiency take `|z_v|` letters of the required sign for each `v` and add `(m-\|z\|_1)/2` opposite-sign pairs, at any vertices.

## Theorem 3. Complete exact positive BRC fiber formula

For any `m,z`, let `N_m(z)` be the number of ordered candidate source words of length `m` with signed vertex inventory `z`. Set `q=(m-\|z\|_1)/2`. If `q\notin Z_{\ge0}`, then `N_m(z)=0`. Otherwise,

\[
\boxed{
N_m(z)=m!\sum_{\substack{r_0+\cdots+r_3=q\\r_v\ge0}}
\prod_{v=0}^{3}
\frac{1}{(r_v+\max(z_v,0))!\,(r_v+\max(-z_v,0))!}.
}
\]

For an integer six-axis readout `y`, the exact fiber cardinality is `N_m(B^{-1}y)` when Theorem 1 applies, and 0 otherwise. In particular, for `m=2j`,

\[
\boxed{
N_{2j}(0)=(2j)!\sum_{r_0+\cdots+r_3=j}\prod_{v=0}^{3}\frac1{(r_v!)^2},\qquad
N_{2j+1}(0)=0.
}
\]

These are **BRC source counts**, not physical signed amplitudes. Under uniform free-choice candidate letters, `Pr(y_m=0)=N_m(0)/8^m`.

**Proof.** For fixed `z`, uniquely express the pair of nonnegative count vectors as `n_v^+=r_v+\max(z_v,0)`, `n_v^-=r_v+\max(-z_v,0)`. The required total count forces `\sum r_v=q`. Every choice of eight letter multiplicities supports exactly the multinomial number `m!/\prod_v(n_v^+!n_v^-!)` of ordered source words. Summing over the disjoint `r` yields the formula; Theorem 1 identifies the six-axis fiber with precisely one signed inventory. For `z=0` the plus/minus multiplicities at each vertex both equal `r_v`.

Equivalently this is the exact positive BRC recurrence `N_0(0)=1`, `N_0(z)=0` for `z\ne0`,
\[
N_{m+1}(z)=\sum_{v=0}^3\big(N_m(z-e_v)+N_m(z+e_v)\big).
\]
It retains all eight named signed branch multiplicities during evaluation. The evaluated `z` is an observer key, not an authorization to erase paths where a later operation reads source history.

## Theorem 4. Polynomial readout support versus exponential ordered sources

Let `R_m=|\{Bz:N_m(z)>0\}|` be the number of distinct six-axis net Cell readouts possible after `m` free candidate letters. For every `m\ge0`,

\[
\boxed{\displaystyle R_m=\frac{(m+1)^2(m^2+2m+3)}3.}
\]

Thus the BRC source population contains `8^m` ordered words but only `R_m=O(m^4)` distinct net readouts. The average source-word fiber size over reachable readouts is exactly `8^m/R_m` (this average is unweighted over the distinct readout keys).

**Proof.** By Theorem 2, each `z\in Z^4` is reachable at length `m` exactly when `m\ge\|z\|_1` and the difference is even. The formal generating function for possible endpoint keys is therefore
\[
\sum_{m\ge0}R_m t^m
=\frac1{1-t^2}\left(\sum_{n\in Z}t^{|n|}\right)^4
=\frac{(1+t)^3}{(1-t)^5}.
\]
Its `t^m` coefficient is the displayed quartic expression. Theorem 1 guarantees different `z` yield different six-axis `Bz`.

## Exact computational evidence

`R762GU_CHECK.py` is a standard-library integer/rational checker. It verifies all 15 four-axis subsets, all `7^4=2,401` inventories in `[-3,3]^4`, all `5^6=15,625` tested candidate readouts in `[-2,2]^6`, the recurrence through length 12, multinomial fibers through length 6, and an independent complete ordered-word enumeration through length 4. The recurrence sums to exactly `8^m` for every tested `0\le m\le12`.

| Length m | Ordered candidate source words | Distinct net readouts R_m | Zero net Cell readout words |
|---:|---:|---:|---:|
| 0 | 1 | 1 | 1 |
| 2 | 64 | 33 | 8 |
| 4 | 4,096 | 225 | 168 |
| 6 | 262,144 | 833 | 5,120 |
| 8 | 16,777,216 | 2,241 | 190,120 |
| 10 | 1,073,741,824 | 4,961 | 7,939,008 |
| 12 | 68,719,476,736 | 9,633 | 357,713,664 |

The general results above are established by exact algebra and counting; finite calculation is an independent implementation check. Author check `PASS`; independent review `NOT_REVIEWED`.

## Preservation and remaining mother problem

P000 fixes six native spatial dimensions, the 120-degree `PERP_E` relation and triadic stable arity. `T_(v,s)` is a constructed admissibility **candidate**, preserving component branch identity, order and multiplicity in the source carrier. The current polynomial observer quotients are safe only for additive net-readout questions with eight available letters; the absence of a native signed Cell/Link/Port/time update law remains a separate task. In particular Theorem 1's parity obstruction is a precise test that any proposed native triadic gate must pass **when its readout is required to factor through this signed STAR incidence**; it is not a new condition on all native events.

**Next scientific test:** Build an explicit typed `TRIADIC_CLOSURE_E` transition that specifies Cell, named Port, Link and independent-time state; determine which signed `T_(v,s)` pass its actual gate. Then test whether the exact lattice condition remains necessary and whether the 4-axis observer still descends through that gated transition. Preserve historical R762GP–R762GS moving-Port results as separate candidate mechanics rather than assuming their gates coincide with this alphabet.

Files: `R762GU_SIGNED_STAR_BRC_LATTICE_AND_FIBRES.md`, `R762GU_CHECK.py`, `R762GU_EVIDENCE.json`.
