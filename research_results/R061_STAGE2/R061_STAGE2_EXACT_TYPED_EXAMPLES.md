# R061 Stage 2 — Exact Typed Examples

Task-ID: `RS-R061-STAGE2-ARBITRARY-POINT-NATIVE-LINE-TRANSLATION-CROSS-SECTOR-GLUING`  
Researcher-ID: `EM-R061S2-3CE600`

Native vertex addresses below are canonical triples `(A,B,C) in N_0^3` with `min=0`. Signed carrier pairs are omitted from the native identities.

## 1. `P=Q`

Take `P=Q=(3,0,1)`.

`D(P->Q)=(0,0,0)`.

Global line identity: `T_P^0`.

Native directed length: `0`.

Three local zero presentations are glued, retaining three distinct incidence-only anchor branches.

## 2. One-step positive-axis displacement

`P=(0,0,0)`, `Q=(1,0,0)`.

Forward: axis `E1`, radial component `1`, squared length `1`.

Two chart presentations: `S12(1,0)` and `S31(0,1)`.

Reverse: `D(Q->P)=(0,1,1)`, translated `S23(1,1)`, squared length `2`.

## 3. Direction geometrically opposite one global positive axis, without native negative axis

`P=(0,0,0)`, `Q=(0,1,1)`.

This is the carrier direction opposite `E1`, but its native displacement is translated `S23` with components `(1,1)`.

No native `-E1` coordinate is introduced.

Squared directed length: `2`.

## 4. Translated `(1,1)`

Take start `P=(3,0,1)` and end `Q=(3,0,0)`.

`D(P->Q)=(1,1,0)`.

Line identity: `T_{P;1,1}^{(12)}`.

Path fiber cardinality: `binom(2,1)=2`.

Squared length: `2`.

Reverse displacement is positive axis `E3` of one tick, squared length `1`.

## 5. Translated non-origin `3-4-5`

`P=(3,0,1)`, `Q=(5,3,0)`.

`D(P->Q)=(3,4,0)`.

Line identity: `T_{P;3,4}^{(12)}`.

Path fiber cardinality: `binom(7,3)=35`.

Forward squared length: `25`.

Reverse displacement: `(1,0,4)` = translated `S31` local `(4,1)`; reverse squared length: `17`.

## 6. Endpoints in different origin sectors, translated displacement `(3,4)`

`P=(1,0,3)` lies in origin `S31`.

`Q=(1,1,0)` lies in origin `S12`.

Yet

`D(P->Q)=(3,4,0)`.

Hence the point-to-point line is exactly translated `S12(P)` with squared length `25` and `35` path representatives.

## 7. Translated axis-boundary double presentation

Take `P=(3,0,2)` and `Q=(1,1,0)`.

`D(P->Q)=(0,3,0)`.

This is translated positive axis `E2`, radial component `3`.

Local presentations:

- `S12(0,3)`;
- `S23(3,0)`.

They glue to one global line identity while retaining two chart-local trajectories.

Forward squared length `9`; reverse displacement `(3,0,3)` has squared length `18`.

## 8. Reversal summary

Every example is reversed by the exact complement rule

`D_rev=M(1,1,1)-D`, `M=max(D)`.

This always gives a nonnegative min-zero native displacement and never a native negative axis. It does not generally preserve native length.

## 9. Several non-integer native lengths

Examples from non-origin starts include:

- displacement `(1,1,0)` -> `ell_E=sqrt(2)`;
- displacement `(1,2,0)` -> `ell_E=sqrt(5)`;
- displacement `(2,2,0)` -> `ell_E=sqrt(8)`.

These lengths are component readouts; their path jump counts are respectively `2`, `3`, and `4` and are not the native lengths.

## 10. Triangle-inequality stress example

Take

`P=(0,0,0)`, `Q=(1,0,0)`, `R=(1,1,0)`.

Then

- `ell_E(P->R)^2=2`;
- `ell_E(P->Q)^2=1`;
- `ell_E(Q->R)^2=1`.

Therefore

`sqrt(2) <= 1+1`.

The checker additionally exhausts all `531,441` ordered triples on the `81`-vertex bounded patch and finds no triangle-inequality counterexample.
