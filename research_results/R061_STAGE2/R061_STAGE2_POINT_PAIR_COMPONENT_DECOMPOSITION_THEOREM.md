# R061 Stage 2 — Point-Pair Component Decomposition Theorem

Task-ID: `RS-R061-STAGE2-ARBITRARY-POINT-NATIVE-LINE-TRANSLATION-CROSS-SECTOR-GLUING`  
Taskbook source: `8b197776249e0b18850cee8375488de9aa57cbb4`  
Researcher-ID: `EM-R061S2-3CE600`

## Status

`ALL_INTEGER_DIRECTED_DISPLACEMENTS_POSITIVE_AXIS_DECOMPOSABLE = true`  
`DISPLACEMENT_DECOMPOSITION_UNIQUE_UP_TO_AXIS_GLUE = true`

## 1. Directed displacement object

Let `P,Q` be arbitrary native coordinate vertices with canonical nonnegative min-zero native addresses.

Do **not** subtract those native triples as though they were a signed native vector space.

Instead, use the implementation carrier map `kappa` only for the incidence calculation:

`delta_I(P,Q)=kappa(Q)-kappa(P)=(r,s) in Z^2`.

Let

`m=min(r,s,0)`

and define the decoded native displacement address

`D(P->Q)=(r-m, s-m, -m)`.

Then every component of `D` is nonnegative and `min(D)=0`.

This is a **decoding map from an I0 carrier difference to the unique canonical native sector address**. It is not the deleted native equivalence `(a,b,c)~(a+k,b+k,c+k)`.

## 2. Uniqueness

Suppose two canonical native triples `D,D'` with `min=0` have the same carrier image. Then their coordinate differences satisfy

`D_1-D_3=D'_1-D'_3`,

`D_2-D_3=D'_2-D'_3`.

Hence `D-D'` is a common diagonal constant. Since both triples have minimum zero, that constant must be zero. Therefore `D=D'`.

So `D(P->Q)` is unique before chart presentation duplication on physical axes.

## 3. Exact sector / axis classification

Write `D=(A,B,C)`.

- `P=Q` iff `D=(0,0,0)`.
- If exactly one component is positive, the displacement lies on that translated positive axis.
- If exactly two components are positive, the unique zero component selects exactly one translated open sector:
  - `C=0`, `A,B>0` -> `S12(P)`, local components `(A,B)`;
  - `A=0`, `B,C>0` -> `S23(P)`, local components `(B,C)`;
  - `B=0`, `C,A>0` -> `S31(P)`, local components `(C,A)`.

A positive-axis displacement has two adjacent chart presentations but one physical axis displacement:

- `E1`: `S12(n,0)` and `S31(0,n)`;
- `E2`: `S12(0,n)` and `S23(n,0)`;
- `E3`: `S23(0,n)` and `S31(n,0)`.

The zero displacement has three local zero presentations, one per sector anchor, but one global zero trace identity.

## 4. Six carrier directions with no native negative axis

The six nearest carrier directions decode as follows:

- `+E1 -> (1,0,0)` : translated axis `E1`;
- `+E2 -> (0,1,0)` : translated axis `E2`;
- `+E3 -> (0,0,1)` : translated axis `E3`;
- carrier direction opposite `E1 -> (0,1,1)` : open `S23`, local `(1,1)`;
- carrier direction opposite `E2 -> (1,0,1)` : open `S31`, local `(1,1)`;
- carrier direction opposite `E3 -> (1,1,0)` : open `S12`, local `(1,1)`.

The last three statements are sector-decoding facts. They do **not** assert native identities such as `-E1=E2+E3`.

## 5. Finite exact census

On the full directed point-pair census of the patch `-4<=p,q<=4`:

- native coordinate vertices: `81`;
- ordered point pairs: `6,561`;
- zero displacements: `81`;
- translated-axis displacements: `852`;
- translated-open-sector displacements: `5,628`;
- one-chart presentations: `5,628`;
- two-chart axis presentations: `852`;
- three-chart zero presentations: `81`;
- unexpected mismatch count: `0`.

## 6. Consequence

Every integer-addressed directed point pair has an exact native displacement typing using only the three positive axis families.

Origin-sector membership of `P` or `Q` is irrelevant to the displacement chart. The chart is selected by `D(P->Q)` relative to the translated atlas based at `P`.
