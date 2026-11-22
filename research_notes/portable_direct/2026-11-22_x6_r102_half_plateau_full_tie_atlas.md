# X6 R102 — Exact half-optimum plateau and explicit complete tie atlas

Date: 2026-11-22 (Asia/Shanghai).
Status: CONDITIONAL_SYMBOLIC_AUTHOR_PROOF / EXACT_FRACTION_AUTHOR_CHECK_PASS / NOT_INDEPENDENTLY_REVIEWED.
Scientific input: frozen `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json`; unchanged. Mathematical dependencies: R98 exact optimum and R99 complete ten-direction carrier, both author-proved and not independently reviewed. R101 supplies the already established strict-sub-half phase.
Scope: conditional positive-count four-channel BRC star-moment observer with common unknown offset. The auxiliary triples here are NOT native six-axis Cell/Link/three-force/time states.

## Model

For nonzero integer `a=(x,y,z)` up to sign, let `q(a)=max(sum_i max(a_i,0),sum_i max(-a_i,0))`. Define
`u=x+3y+6z`, `v=3x+12y+30z`, `h=7x+39y+126z`.
For real `S,T>=1`, write `X=S+1`, `Y=T+1`, `Z=S+T=X+Y-2` and
```
F(a;S,T) = max( |u|/2, |v|/X, |h|/Y,
                |v-u|/X, |h-u|/Y, |h-v|/Z ).
eta_p(S,T) = min {F(a;S,T): a in Z^3\{0} up to sign, q(a)<=p}.
M_p(S,T)   = {unoriented feasible a attaining eta_p}.
```
Throughout `p` is any integer `p>=11`.

## Theorem A — Exact and sharp half-optimum domain

The entire real-parameter plateau `eta_p(S,T)=1/2` is characterized, without optimization or enumeration, by

```
P_p(S,T)  <=>  T<=23  and  (S<=5 or T<=11)
                   and  (p<=26 or S<=11).
```

Equivalently, for `11<=p<=26`, the plateau is the union of two closed rectangles
`[1,5] x [1,23]` and `[1,infinity) x [1,11]`.
For `p>=27`, it is the union
`[1,5] x [1,23]` and `[1,11] x [1,11]`.
Thus allowing Port 27 changes a previously noncompact half-optimum region into a bounded one. Every parameter pair outside this set has `eta_p(S,T)<1/2`.

*Proof.* R98 yields
```
eta_p = min(1/2,12/Y,max(3/X,6/Y), [6/X if p>=27]).
```
It equals `1/2` precisely if each of the other available terms is at least `1/2`. These inequalities are respectively `Y<=24`, `(X<=6 or Y<=12)`, and (for `p>=27`) `X<=12`. Substitute `X=S+1,Y=T+1` to obtain the claimed conditions, with all equality cases included. QED.

## Theorem B — All ties on the half-optimum plateau, with precise Port onsets

Suppose `P_p(S,T)` holds. Begin with `M={s}`, `s=(10,-5,1)`.
The **entire** set `M_p(S,T)` is obtained by adding exactly the named directions for which the following conditions hold:

| Direction | q | Exact condition on the plateau |
|---|---:|---|
| `(1,0,0)` | 1 | `S=5` and `13<=T<=23` |
| `(4,-1,0)` | 4 | `T=23` and `S<=5` |
| `(5,-4,1)` | 6 | `(S=5 and 11<=T<=23) or (T=11 and S>=5)` |
| `(6,-4,1)` | 7 | `T=23` and `S<=5` |
| `(9,-5,1)` | 10 | `(S=5 and 11<=T<=23) or (T=11 and S>=5)` |
| `(10,-5,1)` | 11 | Always |
| `(14,-9,2)` | 16 | `p>=16`, `T<=11`, `S>=11` |
| `(15,-9,2)` | 17 | `p>=17` and `((S=5 and 13<=T<=23) or (T=11 and S>=7))` |
| `(19,-10,2)` | 21 | `p>=21`, `T=11`, `S>=7` |
| `(24,-14,3)` | 27 | `p>=27`, `S=11`, `T<=11` |

All conditions are to be intersected with the stated plateau hypothesis. For example, the apparent unbounded `S>=11,T<=11` rows automatically truncate to `S=11` (or `S<=11`) when `p>=27). For directions of q<=11 no additional Port condition is needed.

*Proof.* R99 provides a complete ten-direction universal carrier, with the following exact `(U,V,H,K)` values where
`U=|u|`, `V=max(|v|,|v-u|)`, `H=max(|h|,|h-u|)`, `K=|h-v|`:

```
(1,0,0)      q=1   : (1,3,7,4)
(4,-1,0)     q=4   : (1,1,12,11)
(5,-4,1)     q=6   : (1,3,6,8)
(6,-4,1)     q=7   : (0,0,12,12)
(9,-5,1)     q=10  : (0,3,6,3)
(10,-5,1)    q=11  : (1,1,1,1)
(14,-9,2)    q=16  : (1,6,1,5)
(15,-9,2)    q=17  : (0,3,6,9)
(19,-10,2)   q=21  : (1,4,6,2)
(24,-14,3)   q=27  : (0,6,0,6)
```

A `U=1` row has `F>=1/2` and equals `1/2` exactly when
`X>=2V, Y>=2H, X+Y>=2K+2`.
A `U=0` row has `F=1/2` exactly when all remaining three ratios are <=`1/2` and at least one attains equality.

Impose the theorem-A plateau inequalities `Y<=24`, `(X<=6 or Y<=12)`, and `(p<=26 or X<=12)`. The necessary and sufficient conditions reduce directly to the table: for instance `(1,0,0)` requires `X>=6,Y>=14`, hence `X=6,14<=Y<=24`; `(4,-1,0)` requires `Y>=24`, hence `Y=24,X<=6`; `(15,-9,2)` requires `X>=6,Y>=12,X+Y>=20`, which on the plateau means `X=6,Y>=14` or `Y=12,X>=8`. The `(14,-9,2)`, `(19,-10,2)`, and `(24,-14,3)` inequalities similarly yield their displayed exact boundaries. Each remaining row is an immediate substitution. R99 excludes every other optimizer in the unbounded integer lattice. QED.

## Consequences

1. Theorems A and B, together with R101 for `eta<1/2`, constitute a complete **inequality-only** atlas of all optimal directions for arbitrary real `S,T>=1` and integer `p>=11`. The R99 ten-carrier score evaluation is no longer required to classify a point.
2. The half-plateau's nontrivial tie skeleton lies on `S=5`, `T=11`, `T=23` and, after Port 27, `S=11`; interior plateau points not satisfying the table's extra conditions have only `s`.
3. At `(S,T)=(5,23)`: exactly six ties for `11<=p<=16`, seven for `p>=17`. At `(11,11)`: seven for `p>=27`. These reproduce, rather than independently re-prove, R100's global maximum multiplicities. No change in optimal set occurs after Port 27, consistently with R99.

## Exact author-side validation

The accompanying `x6_r102_plateau_atlas_verify.py` computes `F` with Python `fractions.Fraction`, without floating point. It passed 1,470 C10 exact rational-parameter / Port cases (147 pairs x 10 Port values), of which 744 are on the half plateau, checking the exact equality conditions and their complement. Separately, for 12 selected rational parameter pairs and seven budgets `p=11,16,17,21,26,27,30`, it enumerated all **47,305** unoriented nonzero integer triples with `q<=30`, directly evaluated the original six-term observer, and matched the exact complete C10 minimizer sets in all 84 cases.

The executable evidence establishes only those finite rational tests and exhaustive finite search bounds. The full real-parameter and unbounded-Port theorem is the exact symbolic reduction above, conditional on R98 and R99. No independent theorem review or Lean formalization has occurred.

## Provenance and next frontier

Scientific model input remains the frozen P000 pin; current behavioral rules are separate. This BRC histogram is an auxiliary observer only; it is not a proof of native P000 Cell/Link/force/time, nor a future-operation-safe quotient. Neither P000 nor the protected worldview was edited.

Next worthwhile direction: classify the **arbitrary four-weight** positive BRC star observer beyond the two-parameter `(1,1,S,T)` section, and seek an explicit observer-fiber counterexample or future-operation-safe repair preserving native Cell identity, path/branch provenance, triadic force and heartbeat order.

Control note: current Task read `r2-20261122-0914-x6-task-read-r102-v1` reached `FAILED / SOURCE_TREE_TRUNCATED`; this independent GitHub proof confers no CLAIM, PROGRESS, Activity or Result authority.
