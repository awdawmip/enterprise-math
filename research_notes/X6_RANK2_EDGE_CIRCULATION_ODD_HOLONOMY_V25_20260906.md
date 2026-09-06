# X6 upper V25: a rank-2 source-space circulation is sufficient and minimal for deterministic odd active-triad holonomy in the affine edge-score family

Status: `FREE_RESEARCH / EXACT CONSTRUCTIVE DYNAMICS + MINIMAL-RANK THEOREM / NOT_FOUNDATION`
Date: `2026-09-06`
Researcher: `EM-FREE-PI-PRIME-20260904 / FREE_AXIOM_DISCOVERY`
Tasks: `RS-X6-CELL-CHANNEL-INTERNAL-STATE`, `RS-X6-NATIVE-ROTATION-DYNAMICS`, `RS-X6-NATIVE-TIME-DYNAMICS`, `RS-X6-UPPER-STRUCTURE-INTEGRATION`
Depends on:
- `X6_FOUR_FIELD_LOCAL_SUCCESSOR_AND_STATIC_POTENTIAL_NOGO_V24_20260906.md`;
- `X6_FOUR_FIELD_ACTIVE_TRIAD_CODE_V23_20260906.md`;
- `X6_ACTIVE_TRIAD_HOLONOMY_CONTROL_V17_20260906.md`;
- Weighted-BRC exact positive-rational branch semantics.
Checker: `experiments/x6_dynamic_law_holonomy_v24_20260906/check_dynamic_law_holonomy.py`.

## 1. Why an edge term is the next admissible object

V24 rules out every deterministic update obtained solely by maximizing a fixed destination potential on `J(6,3)`: such a law has no periodic orbit of length at least three and therefore cannot generate V17 nontrivial active-frame holonomy.

The smallest structural extension is to let the transition score depend on both the current and candidate active triad.

Use the explicit four-field identity code H from V23. For a triad S write

`c(S)=Code_H(S) in {-1,0,+1}^4`.

The four source slots remain labeled relation sources; they are not four new spatial axes.

## 2. Affine edge-score family

Let

`u in Z^4`

and let

`Omega in Mat_4(Z)`

be skew-symmetric:

`Omega^T=-Omega`.

For adjacent active triads `S~T`, define

`Phi_{u,Omega}(S,T)=u^T c(T) + c(S)^T Omega c(T)`.

The first term is a static destination preference. The second is an antisymmetric edge coupling:

`A_Omega(T,S)=-A_Omega(S,T)`.

For any rational `rho>1`, the exact positive-rational Weighted-BRC mass

`W_rho(S->T)=rho^(Phi_{u,Omega}(S,T))`

has the same branch ordering as Phi.

Under simultaneous native axis relabeling of the four source fields and both active triads,

`Code_{gH}(gS)=Code_H(S)`

and therefore Phi is S6 covariant for the transported labeled context.

The integer coefficients `(u,Omega)` are dynamical/source-coupling data. They are not supplied by P000 and are not claimed to be physically calibrated here.

## 3. Static rank zero is impossible

If `Omega=0`, the rule

`S -> unique argmax_{T~S} Phi(S,T)`

is exactly a fixed destination-potential update.

By V24, it has no recurrent cycle of length at least three. Every two-cycle is a backtrack with identity V17 connection holonomy.

Hence

`rank(Omega)=0 -> NO ODD RECURRENT ACTIVE-FRAME HOLONOMY`.

## 4. Explicit rank-2 law

Use the V23 positive four-field code determined by the four perfect matchings

`{{0,1},{2,3},{4,5}}`,

`{{0,2},{1,4},{3,5}}`,

`{{0,3},{1,5},{2,4}}`,

`{{0,4},{1,3},{2,5}}`.

Take

`u=(-3,-4,2,1)`.

Write the six independent upper-triangular entries of Omega in the order

`(01,02,03,12,13,23)`.

Choose

`Omega=(-1,-1,0,0,0,0)`.

Equivalently

```
Omega = [[ 0,-1,-1, 0],
         [ 1, 0, 0, 0],
         [ 1, 0, 0, 0],
         [ 0, 0, 0, 0]].
```

This matrix has exact rank 2.

For every one of the twenty current active triads, the nine adjacent candidates have a **unique** maximum Phi score. The minimum gap between the largest and second-largest score over all twenty states is exactly 1.

Thus the score defines a deterministic S6-covariant update on this transported four-field context.

## 5. The deterministic law has an odd-holonomy six-cycle

The functional graph has a recurrent six-cycle

`012 -> 015 -> 135 -> 235 -> 245 -> 124 -> 012`.

Every consecutive pair shares two axes, so the V17 active-frame replacement connection applies at every step.

Transport around the loop returns to the base triad `012` with slot permutation

`(0,2,1)`.

Therefore the returned active frame exchanges axes `1` and `2` while leaving axis `0` fixed.

Hence

`HOLONOMY = transposition(1,2)`,

`ORI6_CHARGE = 1`.

The law also has one flat two-cycle

`034 <-> 045`,

whose holonomy is identity.

Thus one and the same exact local rule exhibits both a flat recurrent sector and a curved/odd recurrent sector.

## 6. The antisymmetric circulation is genuinely nonzero

Along the odd six-cycle, the edge-coupling contributions are

`0,1,1,0,1,1`.

Therefore

`sum_cycle A_Omega = 4 != 0`.

This is a direct discrete circulation witness. It cannot be represented by a global static destination potential.

The corresponding total selected edge scores around the six-cycle are

`3,4,3,4,3,4`.

So the recurrence is not created by one exceptionally high destination state; it is sustained by the edge-sensitive relational circulation.

## 7. Minimal antisymmetric rank inside this declared family

Over characteristic zero, the rank of a skew-symmetric matrix is even.

V24 proves rank 0 cannot generate nontrivial recurrent holonomy in this affine edge-score family.

The explicit construction above uses rank 2 and does generate odd holonomy.

Therefore

`MINIMUM POSSIBLE rank(Omega) FOR ODD RECURRENT HOLONOMY IN THIS AFFINE FOUR-FIELD EDGE-SCORE FAMILY = 2`.

This is a structural-rank minimum, not a claim about minimum coefficient magnitude, minimum number of nonzero matrix entries, or a universal law class outside the declared score family.

## 8. Interpretation: gradient plus circulation

The score separates naturally into

`Phi = STATIC_DESTINATION + ANTISYMMETRIC_EDGE_CIRCULATION`.

The first part can rank states but cannot by itself sustain a nontrivial holonomy loop.

The second part supplies the first exact nonconservative relational degree needed to make the active-triad history curve through `J(6,3)`.

This gives a concrete bridge:

`FOUR-FIELD INTERNAL CONTEXT`

`+ RANK-2 EDGE 2-FORM`

`-> DETERMINISTIC ACTIVE-TRIAD LOOP`

`-> V17 S3 TRANSPOSITION HOLONOMY`

`-> ORI6 CONTROL BIT + POINTED PAIR`.

No external axis-pair selector is used after the field/context and coupling coefficients have been supplied.

## 9. What is still not derived

The example proves **sufficiency** of a very small edge-sensitive relational coupling and proves rank-2 minimality within the declared affine score family.

It does not derive the numerical coefficients `(u,Omega)` from P000, triadic balance, duration, energy, or experiment.

So the next question is not whether edge sensitivity can work. It can.

The remaining high-leverage problem is:

> can `(u,Omega)` or an equivalent rank-2 circulation datum be generated from already-existing channel/frame/time relations, rather than introduced as independent calibration coefficients?

That is the next upper-structure frontier.
