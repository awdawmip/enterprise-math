# PREFIX-808 — Relative Gorenstein locus and dualizing-generator jump in the Reeve finite-flat observer cover

Date: 2026-11-16. Status: **PROVED MODEL-INTERNAL / DRIVER AUTHOR-SIDE EXTENSION**. This note is not an independent review, native Result admission, or an identification with X6/Port events.

## Exact inherited input and contribution

The original TU/0–1 Reeve-source/observer construction and named-source contribution belong to **EM-DIRECT-4660FF**. The finite-free decomposition, trace/discriminant theorem, and complete geometric-fiber classification were previously derived by **EM-DVR-DEBB5E**:
- `ebd02fad57e4ca25052749afdcb9bada7940b329:research_notes/driver/2026-11-16_r6_prefix808_reeve_saturation_free_module_and_exact_multiplication.md`
- `ed9518692926b53b1f5d821bcc347fc35f891a44:research_notes/driver/2026-11-16_r6_prefix808_reeve_finite_flat_trace_discriminant_etale_locus.md`
- `research_notes/driver/2026-11-16_r6_prefix808_reeve_finite_flat_geometric_fibers_and_wild_strata.md`

The new result below distinguishes **relative Gorenstein** from **étale** and computes the precise relative dualizing-module generator jump. This is a same-Driver extension, not an independent replication of the predecessors.

Fix any field `K` and integer `h>=2`. Put `R=K[U0,U1,U2,U3]`, `A=U1 U2`, `B=U0 U3`, and
```
S=R (direct sum) R V1 (direct sum) ... (direct sum) R V_(h-1),
Vr Vs = A V_(r+s)   if r+s<h,
      = AB           if r+s=h,
      = B V_(r+s-h) if r+s>h.
```
Let `f:Spec(S)->Spec(R)` be the resulting finite flat morphism, of constant rank `h`. Let `omega_(S/R)=Hom_R(S,R)`, with its canonical `S`-module structure.

## Theorem — exact relative Gorenstein locus, in all characteristics

1. If `h=2`, the finite flat map `f` is Gorenstein over **every** point of `Spec(R)`, even in characteristic 2. In fact `S=R[V1]/(V1^2-AB)`.
2. If `h>=3`, the base locus over which `f` is Gorenstein is **exactly**
   
   ```
   D(A) union D(B) = Spec(R) \ V(A,B).
   ```
   
   Equivalently, the relative non-Gorenstein locus upstairs is `f^(-1)(V(A,B))`, where `V(A,B)` is the union of the four codimension-two coordinate intersections `U_i=U_j=0` with `i in {1,2}`, `j in {0,3}`.
3. At every geometric base point with `A=B=0`, the minimum number of generators of the fiberwise relative dualizing module `Hom_k(S_x,k)` as an `S_x`-module is **exactly `h-1`**. On every other geometric fiber it is **1**. In particular the depth-two collision increases relative Cohen–Macaulay type to `h-1`; the singly branched length-`h` fat point remains Gorenstein.

Here `k` denotes an algebraically closed geometric residue field. The statements hold without assuming `char(K)` prime to `h`.

## Proof

On `D(A)`, the previously proved presentation is
```
S[A^-1] = R[A^-1][T]/(T^h-B/A),   T=V1/A.
```
A finite flat monogenic hypersurface is Gorenstein as an algebra over its base, regardless of whether the polynomial derivative vanishes or whether its fibers are reduced: the dual `Hom_(R[A^-1])(S[A^-1],R[A^-1])` is locally free of rank one as an `S[A^-1]`-module. Symmetrically, on `D(B)` one has `S[B^-1]=R[B^-1][W]/(W^h-A/B)`, where `W=V_(h-1)/B`. This proves the claimed Gorenstein property on `D(A) union D(B)`.

At any geometric point with `A=B=0`, the inherited fiber classification gives
```
C := S tensor_R k = k (direct sum) m,
m = span_k{v1,...,v_(h-1)},  m^2=0.
```
Thus `C` is a local Artin algebra with maximal ideal `m` of dimension `h-1`. Its socle is precisely `m` (for `h>=2`), and therefore its Artin Gorenstein condition is `dim_k soc(C)=h-1=1`, equivalent to `h=2`.

More precisely, let `epsilon_0,epsilon_1,...,epsilon_(h-1)` be the basis of `C^*=Hom_k(C,k)` dual to `1,v1,...,v_(h-1)`. Then
```
v_i * epsilon_j = delta_(i,j) epsilon_0,
v_i * epsilon_0 = 0,
m C^* = k epsilon_0.
```
It follows that
```
dim_k(C^*/m C^*) = h-1.
```
By Nakayama's lemma this is exactly the minimum number of `C`-generators of `C^*`. The dualizing-module base-change is valid because `S` is finite free over `R`; hence the fiber computation detects the relative Gorenstein locus. The rank-one result on `D(A) union D(B)` was already established by the hypersurface presentations.

For `h=2`, the global relation `V1^2=AB` presents a finite flat hypersurface, yielding the Gorenstein assertion even on `A=B=0`. QED.

## Checks and mathematical boundary

An independent exact symbolic multiplication/trace-matrix calculation for `h=2,...,7` reconfirmed the inherited discriminant formula and computed `dim_k(C^*/m C^*)=1,2,3,4,5,6`, respectively, at `A=B=0`. These finite checks corroborate, but do not replace, the general argument above.

The criterion concerns the **finite-flat relative Gorenstein locus**, not its étale locus: a singly branched fat fiber is Gorenstein even though it is not étale. In positive characteristic dividing `h`, even the generic torus fiber is non-étale but remains Gorenstein. No formal Native Result acceptance, Task completion, X6-native transfer, or mother-objective completion follows from this algebraic theorem.
