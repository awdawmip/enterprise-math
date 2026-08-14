# R039 — Native Rough Surface Algebra and Collapse Calculus

Status: `SEMANTIC_CHECKPOINT / L2 RESEARCH / NOT CANONICAL`  
Researcher-ID: `EM-R039-9F3C27`  
Task: `RS-R039-NATIVE-ROUGH-SURFACE-ALGEBRA-COLLAPSE-CALCULUS`  
Taskbook base: `cfbecf969b15d5d8c027c910bdbd6ca74259f0f7`  
Exact exhaustive range: `FCC N<=8`, `HCP N<=8`  
CI: `CI_NOT_REQUIRED_FOR_RESEARCH`

## 1. Checkpoint result

R039 closes a metric-free native surface calculus far enough to answer the taskbook's core questions without defining radius, graph distance, equal-distance shells, Euclidean normals/area, or a sphere.

For a finite connected occupied cluster `C`, the native rough surface is the oriented contact cut

\[
\delta(C)=\{(u,v):u\in C,\ v\notin C,\ u\sim v\},
\]

preferably retaining contact-slot labels. The scalar `S(C)=|delta(C)|` is a collapse/readout, not the surface itself.

The concrete future-relative precision ladder found here is

```text
full native cluster/incidence
 -> full cut + frontier incidence
 -> local surface-type multiset
 -> frontier attachment histogram H
 -> scalar S.
```

A second-order frontier residual then repairs `H` exactly for a two-step terminal-`S` future.

## 2. Exact native models

### FCC

Implementation-only carrier:

\[
L_{FCC}=\{(x,y,z)\in\mathbb Z^3:x+y+z\equiv0\pmod2\}.
\]

The 12 native contact steps are the permutations of `(±1,±1,0)`. Canonicalization quotients translations and 48 signed coordinate permutations. No norm is evaluated.

### HCP

Implementation-only coordinates are `(i,j,k) in Z^3`, with even `k` = A and odd `k` = B. Same-layer contacts use the six triangular steps `(±1,0),(0,±1),(1,-1),(-1,1)`. Interlayer offsets are `(0,0),(-1,0),(0,-1)` from even layers and `(0,0),(1,0),(0,1)` from odd layers, to each adjacent layer.

Canonicalization uses 24 explicit adjacency-preserving space-group representatives modulo Bravais translations `(a,b,2m)`. Their adjacency preservation and closure modulo those translations were checked. Before L4, a conventional crystallographic completeness audit against a full `P6_3/mmc` presentation remains recommended; no abstract graph-isomorphism quotient is used here.

## 3. Exact interface laws

### R039-T1 — set-level cut update

For a frontier cell `x`, define

\[
A_x(C)=\{(u,x):u\in C, u\sim x\},\qquad
B_x(C)=\{(x,y):y\notin C\cup\{x\}, x\sim y\}.
\]

Then

\[
\boxed{\delta(C\cup\{x\})=(\delta(C)\setminus A_x(C))\cup B_x(C).}
\]

### R039-T2 — 12-regular boundary handshake

If `N=|C|` and `E_int(C)` is the number of occupied-occupied contacts,

\[
\boxed{S(C)=12N-2E_{int}(C).}
\]

Thus fixed-volume surface minimization is exactly internal-contact maximization. This is a specialization of the standard regular-graph edge-isoperimetric handshake identity, not a generic Enterprise Math novelty claim.

### R039-T3 — local addition/removal

For `x` in the frontier,

\[
k_C(x)=|\{u\in C:u\sim x\}|,
\]

and

\[
\boxed{S(C\cup\{x\})-S(C)=12-2k_C(x).}
\]

If `D=C\setminus\{x\}` is an allowed connected-cluster deletion,

\[
\boxed{S(D)-S(C)=2k_D(x)-12.}
\]

Deletion legality is not encoded by the scalar contact count: an articulation/connectivity residual is required by the partial-operation future language.

### R039-T4 — frontier handshake

Let

\[
F(C)=\{x\notin C:\exists u\in C, u\sim x\},\qquad
H_C(k)=|\{x\in F(C):k_C(x)=k\}|.
\]

Every boundary dart has exactly one frontier endpoint, so

\[
\boxed{S(C)=\sum_{x\in F(C)}k_C(x)=\sum_k kH_C(k).}
\]

Consequences:

- `H_C` reconstructs current `S` exactly;
- Boolean one-step `Delta S` support needs only the presence set `{k:H_C(k)>0}`;
- multiplicity-sensitive one-step `Delta S` support is exactly equivalent to `H_C`;
- best one-step descent needs only `S` plus `max k`.

## 4. Second-order residual: exact two-step repair

For each `x in F(C)`, define

\[
A_x(j)=|\{y\in F(C)\setminus\{x\}:y\sim x,\ k_C(y)=j\}|,
\]

\[
b_x=|\{y:y\sim x,\ y\notin C\cup F(C)\}|,
\]

and the local record

\[
P_C(x)=(k_C(x),A_x,b_x).
\]

If `H'=H_{C union {x}}`, then exactly

\[
\boxed{H'=H_C-e_{k_x}-A_x+\operatorname{shift}_{+1}(A_x)+b_xe_1.}
\]

Therefore

\[
R_2(C)=\{P_C(x):x\in F(C)\}_{multi}
\]

contains `H_C` through its first-coordinate histogram and computes every successor `H` exactly. It is therefore sufficient for exact two-step terminal-`S` support. No minimality claim is made for `R_2`.

Executable verification over every addition from every exhaustive Python cluster through `N<=5`:

- FCC transitions: `5,121`;
- HCP transitions: `17,487`;
- mismatches: `0`.

## 5. Exact small-cluster atlas

Connected embedded clusters are quotiented by the declared lattice symmetry actions, never by abstract induced-graph isomorphism.

| N | FCC classes | FCC S_min | FCC S_max | FCC minimizers | HCP classes | HCP S_min | HCP S_max | HCP minimizers |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 12 | 12 | 1 | 1 | 12 | 12 | 1 |
| 2 | 1 | 22 | 22 | 1 | 2 | 22 | 22 | 2 |
| 3 | 4 | 30 | 32 | 1 | 9 | 30 | 32 | 3 |
| 4 | 20 | 36 | 42 | 1 | 57 | 36 | 42 | 1 |
| 5 | 131 | 44 | 52 | 2 | 460 | **42** | 52 | 1 |
| 6 | 1,211 | **48** | 62 | 1 | 4,641 | 48 | 62 | 1 |
| 7 | 12,734 | 54 | 72 | 1 | 50,353 | 54 | 72 | 1 |
| 8 | 144,158 | 60 | 82 | 3 | 575,375 | 60 | 82 | 4 |

Hence

```text
FCC S_min: 12, 22, 30, 36, 44, 48, 54, 60
HCP S_min: 12, 22, 30, 36, 42, 48, 54, 60
```

The first scalar minimal-surface distinction is `N=5`.

## 6. Minimal collapse counterexamples

Minimality below means no smaller witness exists in the exact exhaustive atlas under the declared quotient/language.

### CE1 — scalar S is one-step unsafe at N=3

FCC, both `S=32`:

```text
C=((0,0,0),(0,1,-1),(1,-1,0))
H(C)=((1,17),(2,6),(3,1))
DeltaS support={6,8,10}

D=((0,0,0),(0,1,-1),(0,2,-2))
H(D)=((1,16),(2,8))
DeltaS support={8,10}
```

HCP has the analogous `N=3` witness

```text
C=((0,0,0),(0,0,1),(0,1,1))
D=((0,0,0),(0,1,0),(0,2,0)).
```

### CE2 — H is two-step unsafe at N=4

FCC has two `S=42` clusters with the same

```text
H=((1,20),(2,8),(3,2))
```

but terminal two-step supports

```text
{52,54,56,58,60,62}
{54,56,58,60,62}.
```

One exact pair is

```text
C=((0,0,0),(0,1,-3),(1,0,-1),(1,1,-2))
D=((0,0,0),(0,1,-1),(1,-2,1),(1,-1,0)).
```

HCP has the same failure at `N=4`, with same `S=42`, same

```text
H=((1,19),(2,7),(3,3)),
```

and exact pair

```text
C=((0,0,1),(0,1,0),(1,0,2),(1,1,0))
D=((0,0,0),(0,0,1),(0,1,1),(1,1,2)).
```

### CE3 — local type multiset loses correlation at N=4

FCC:

```text
C=((0,0,0),(0,1,-3),(1,0,-1),(1,1,-2))
D=((0,0,0),(0,1,-1),(1,-1,0),(1,1,-2))
N_tau(C)=N_tau(D)
H(C)=((1,20),(2,8),(3,2))
H(D)=((1,20),(2,9),(4,1)).
```

HCP:

```text
C=((0,0,1),(0,1,0),(1,0,2),(1,1,0))
D=((0,0,0),(0,0,1),(0,1,2),(1,1,2))
N_tau(C)=N_tau(D)
H(C)=((1,19),(2,7),(3,3))
H(D)=((1,18),(2,9),(3,2)).
```

Thus a bag of local surface types loses type-to-type/frontier correlation.

### CE4 — premature recoalescence

From the unique FCC `N=2` state, different additions reach `N=3` states with the same `S=32`, including CE1. Recoalescing those branches by scalar `S` makes unequal one-step suffix signatures indistinguishable. Likewise, the CE2 `N=4` states show that recoalescing by `H` is unsafe for a two-step suffix. This is the R023/R023I no-resurrection boundary specialized to native surface growth.

## 7. Native FCC/HCP memory

At `N=2`, HCP already has two non-equivalent native bond/surface orbits:

```text
basal:      ((0,0,0),(0,1,0))
interlayer: ((0,0,0),(0,0,1)).
```

Both have `S=22` and `H=((1,14),(2,4))`, but distinct HCP local mask orbits. FCC has only one two-cell orbit. Excluding the trivial substrate/world tag, the first nontrivial embedded native-surface distinction is therefore `N=2`.

A stronger scalar difference appears at `N=5`: `S_min_HCP(5)=42`, while `S_min_FCC(5)=44`.

## 8. FCC greedy SURFACE_DOWN trap

Retain all ties and always add a frontier cell of maximal `k_C(x)`. Through `N=5`, FCC remains globally optimal. Its unique greedy `N=5` state is

```text
G5=((0,0,0),(0,0,2),(0,1,1),(1,0,1),(1,1,0))
S=44
H=((1,15),(2,10),(3,3)).
```

So `max k=3`, forcing every greedy `N=6` successor to `S=50`. But the exact global optimum is `S_min_FCC(6)=48`, for example

```text
M6=((0,0,0),(1,-1,0),(1,0,-1),(1,0,1),(1,1,0),(2,0,0)).
```

Thus the first true all-tie FCC greedy trap is `N=6`.

Mechanism: FCC has two global `N=5` minimizer classes with equal current `S=44`. The greedy-history minimizer has `max k=3`; the other minimizer has a `k=4` frontier site and extends to the `N=6` optimum, but it is not reachable through a globally minimal `N=4` prefix. Current surface optimality is not a nested-state invariant.

For HCP, all-tie greedy growth contains nonoptimal branches from `N=4`, but at least one greedy branch reaches `S_min(N)` for every tested `N<=8`. No complete HCP greedy trap is claimed in the exact range.

## 9. Native roughness

After defining the metric-free optimum,

\[
\rho(C)=S(C)-S_{min}(|C|).
\]

Both terms are even, so

\[
\boxed{\rho(C)\equiv0\pmod2.}
\]

For an addition,

\[
\boxed{\rho(C\cup\{x\})-\rho(C)=12-2k_C(x)-[S_{min}(N+1)-S_{min}(N)].}
\]

No sphere is referenced. As a collapse coordinate, `rho` inherits scalar `S`'s future insufficiency at fixed `N`.

## 10. Future-safe collapse matrix

| Representation | Current S | one-step DeltaS support | one-step multiplicity | best one-step | two-step terminal S | arbitrary h / deletion legality |
|---|---|---|---|---|---|---|
| Q0 full cluster/incidence | SAFE | SAFE | SAFE | SAFE | SAFE | SAFE |
| Q1 cut + frontier incidence | SAFE | SAFE | SAFE | SAFE | SAFE for additions | deletion needs connectivity residual |
| Q2 local type multiset | SAFE | UNSAFE at N=4 | UNSAFE | UNSAFE | UNSAFE | UNSAFE |
| Q3 H | SAFE | SAFE | SAFE/equivalent | SAFE | **UNSAFE at N=4** | UNSAFE |
| Q4 `(N,E_int,S)` | SAFE | UNSAFE at N=3 | UNSAFE | UNSAFE | UNSAFE | UNSAFE |
| Q5 scalar S | SAFE | **UNSAFE at N=3** | UNSAFE | UNSAFE | UNSAFE | UNSAFE |
| Q6 `(N,rho)` | SAFE for S if `S_min` known | scalar failure class | UNSAFE | UNSAFE | UNSAFE | UNSAFE |
| R2 second-order frontier residual | SAFE | SAFE | SAFE | SAFE | **SAFE** | higher h OPEN |

For `Ubest1`, `(S,max k)` is exact. For Boolean one-step support, `(S,{k:H(k)>0})` is exact.

## 11. Horizon monotonicity

Let `Sigma_<=h(C)` contain every declared observation through horizon `h`. Then

\[
\Sigma_{\le h+1}=(\Sigma_{\le h},\text{new observations}),
\]

so

\[
\boxed{\ker\Sigma_{\le h+1}\subseteq\ker\Sigma_{\le h}.}
\]

Therefore the coarsest exact quotient refines monotonically only for nested future languages. No monotonicity is automatic for unrelated terminal-only languages.

## 12. H1-H13 ledger

| H | checkpoint status |
|---|---|
| H1 native interface exactness | `CONFIRMED` |
| H2 boundary handshake | `CONFIRMED` |
| H3 local attachment law | `CONFIRMED` |
| H4 finite surface alphabet | `CONFIRMED` (`<=2^12` raw masks before quotient) |
| H5 scalar insufficiency | `CONFIRMED / MIN N=3` |
| H6 H one-step sufficient / two-step insufficient | `CONFIRMED / MIN N=4` |
| H7 local-type correlation debt | `CONFIRMED / MIN N=4` |
| H8 native droplet atlas | `CONFIRMED N<=8` |
| H9 greedy DOWN trap | `CONFIRMED FCC / MIN N=6`; HCP open beyond 8 |
| H10 precision ladder | `CONFIRMED FOR NESTED LANGUAGES` |
| H11 small residual repair | `CONFIRMED FOR HORIZON 2 / MINIMALITY OPEN` |
| H12 FCC/HCP native memory | `CONFIRMED` |
| H13 sphere not required | `CONFIRMED FOR CHECKPOINT CALCULUS` |

## 13. Prior-art boundary

Independent derivation preceded the bounded search.

- Barber & Erde, *Isoperimetry in integer lattices*, Discrete Analysis 2018:7, DOI `10.19086/da.3555`: generic lattice edge-isoperimetry is prior mathematics.
- Strachan & Swanepoel, *Edge Isoperimetry of Lattices*, Annals of Combinatorics (2026), DOI `10.1007/s00026-025-00801-x`: regular-graph edge-boundary/internal-edge equivalence is generic prior mathematics.
- Arkus, Manoharan & Brenner, *Deriving Finite Sphere Packings*, SIAM J. Discrete Math. 25 (2011), DOI `10.1137/100784424`, and Holmes-Cerfon, *Sticky-Sphere Clusters*, Annual Review of Condensed Matter Physics 8 (2017), DOI `10.1146/annurev-conmatphys-031016-025357`: finite contact-maximization/sticky-cluster landscapes are established prior areas.

No generic EIP, regular-graph handshake, or quotient/lumpability priority claim is made. The project-local contribution is the concrete composition

```text
native close-packed interface
+ exact local update algebra
+ embedding-sensitive FCC/HCP quotient
+ minimal small-N collapse counterexamples
+ future-safety matrix
+ explicit second-order frontier residual
+ BRC no-resurrection specialization.
```

## 14. Direct answers to the taskbook

1. **Native surface without distance:** the occupied-to-unoccupied contact incidence cut `delta(C)` with slot labels retained when needed.
2. **First nontrivial branching:** HCP embedded classes split at `N=2`; FCC at `N=3`; scalar `S` values split at `N=3` in both.
3. **What S loses:** frontier endpoint multiplicities, local-type arrangement/correlation, and deletion connectivity legality.
4. **Smallest sufficient state:** language-dependent. Boolean one-step needs nonzero-k presence; multiplicity-sensitive one-step is `H`; two-step terminal `S` is repaired by concrete `R2`; generic h is the future-signature kernel.
5. **Collapse lattice:** yes when summaries are treated as quotient kernels ordered by factorization/refinement and indexed by declared future language.
6. **Droplet without radius:** yes, minimize native cut / maximize internal contacts.
7. **FCC/HCP memory:** nontrivially `N=2` in native bond/surface orbit structure; `N=5` in scalar minimal boundary.
8. **First scalar collapse toward smooth readouts:** already `delta(C) -> |delta(C)|=S(C)`; area/normal/curvature/radius/sphere are later optional readouts.

## 15. Validation and next action

Artifacts include a transparent Python reference, 7 exact unit tests, an independent optimized C++ enumerator, and a machine-readable `N<=8` atlas.

- Python/C++ class-count and `S_min/S_max/minimizer_count` agreement through `N<=7`.
- C++ exact exhaustive certificate through `N=8` for both worlds.
- Direct cut count equals `12N-2E_int` on every C++ enumerated state through `N=8`.
- Seven local tests pass.
- No theorem-critical floating point, radius, norm, or pi.
- No CI status query: `CI_NOT_REQUIRED_FOR_RESEARCH`.

Unique continuation point:

```text
formalize finite-horizon frontier behavioral refinement:
H (h=1 exact) -> R2 (h=2 exact) -> search/construct R3,
while preserving embedded FCC/HCP symmetry semantics.
```

Secondary next actions: conventional HCP space-group completeness audit; search HCP beyond `N=8` for a true all-tie greedy trap; extend to periodic Barlow words; consider a narrowly scoped Foundation feedback packet for the `R2` surface specialization only.
