# R762HC — S6 triadic completion gate, integer image lattice and positive BRC witness

Status: **AUTHOR-PROVED CANDIDATE / EXACT FINITE CHECK PASS / NOT_REVIEWED**
Task: `RS-X6-TRIADIC-CLOSURE-DYNAMICS`
Current continuation: R762HB, Draft PR #2859 @ `dcd47f990fc21fd25688b750b6de55d8f41d3c4d`.
Frozen science: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`, notably `p000_reality_foundation.json`, `definitions/P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md`, `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md`, and `definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json`.
Current rules are read separately from frozen science; no P000 promotion or amendment.

## Defined object and exact scientific scope

Let `I={0,1,2,3,4,5}` label the six native signed spatial axes. P000 fixes distinct axes to be pairwise `PERP_E` and the native angle to be 120 degrees. The X6 Cell torsor has signed displacement group `Z^6`, and all coordinate permutations `S6` are a verified **axis-label rotation skeleton**. Define `T = { S subset I : |S|=3 }` (20 unsigned/unoriented axis triples), and `h_S=sum_{i in S}e_i`.

An `h_S` displacement is a **composite three-primitive-axis path**: it is not a new primitive straight segment; P000's separate `TRIADIC_CLOSURE_E` relation is not defined by the condition `|S|=3` alone. Thus this note studies the **maximal three-axis incidence candidate**. Its optional signed BRC extension has exactly 40 named branches `(S,epsilon)`, `epsilon=+1,-1`, with spatial endpoint increment `epsilon*h_S`; each branch is distinct and positively counted. Nothing in this construction declares that all 20 triples, either sign, or any ordering is permitted by an actual primitive force/Cell/Link/Port/time event.

This addresses a precise obstruction to promoting the prior four K4-STAR columns into an axis-label equivariant native closure rule.

## Theorem 1 — sharp S6-equivariant completion obstruction

For each ordered pair of distinct named axes `(i,j)`, let `U_ij=I\\{i,j}`. The stabilizer of `(i,j)` in `S6` is `S4`, acting transitively on the four elements of `U_ij`.

**(1a)** There is no function `f(i,j) in U_ij` with `f(pi*i,pi*j)=pi*f(i,j)` for every `pi in S6`. Indeed, a permutation fixing `i,j` and moving the chosen third label fixes the input but changes the output.

**(1b)** A deterministic equivariant completion with extra state `r in U_ij` exists: `f(i,j,r)=r`, and `pi*(i,j,r)=(pi*i,pi*j,pi*r)`. Any *surjective* equivariant state repair on a fixed pair must carry at least four distinguishable states (at least two binary bits). The alternative is a positive BRC with four distinct completion branches, `(i,j)->(i,j,r)`, one for each `r in U_ij`, without choosing one branch by hidden fiat.

**(1c)** `S6` acts transitively on the 20 unoriented triples. Consequently an `S6`-invariant legal-triple subset `L subset T` depending only on the three axis labels is either empty or all of `T`. In particular, **only the four FCC/K4 STAR triples cannot form an S6-invariant label-only primitive closure language**. A Port/Link/rotation gate may legitimately restrict those triples provided its additional state transforms as part of the operation; its law must be stated, not silently omitted.

The pair `(i,j)` is a **two-axis observation awaiting a third candidate**. It is not a stable two-force equilibrium; no force-balance predicate has been inferred from the combinatorial completion.

## Theorem 2 — full integer image and minimal additive Link rank

Let `A` be the `6 x 20` incidence matrix, with column `h_S` for each `S in T`. Then

```
A Z^20 = { y in Z^6 : y_0+...+y_5 is divisible by 3 }.
rank_Q(A)=6,  [Z^6 : A Z^20]=3,
Smith invariant factors: (1,1,1,1,1,3).
```

**Proof.** Each column has coordinate sum 3, proving necessity. For any `i != j`, choose distinct `a,b` outside `{i,j}`. Then `h_{i,a,b}-h_{j,a,b}=e_i-e_j`. Thus the integer column span contains all coordinate differences and hence the complete zero-sum root lattice `{y:sum(y)=0}`. One column (e.g. `h_{0,1,2}`) has sum 3. For any integer vector with sum `3q`, subtract `q*h_{0,1,2}`, then express the zero-sum remainder in the differences. This establishes equality and index 3. The full-rank submatrix with columns indexed `[0,1,2,3,4,10]` in lexicographic triple order has determinant `-3`; the index-three description therefore yields Smith form `(1,1,1,1,1,3)`.

If all 20 signed composite increments are to be represented via a free-abelian additive relational Link group `Z^r` and an integer linear decoder `D:Z^r -> Z^6`, with every `h_S` in `im(D)`, necessarily `r>=6`. This is sharp: choose `r=6`, `ell in Z^6`, and `D=identity`; define `C'=C+epsilon*h_S`, `ell'=ell-epsilon*h_S`. Then `K=C+ell` is conserved on every candidate branch. This Link is *relational state over Cells*, not six extra spatial axes.

Contrast: the four FCC/K4 STAR columns have rank 4 (witness minor determinant 2), as in R762HB. Their rank-four Link lower bound is exact **only for that restricted family**. The rank-six lower bound is exact under the all-20 incidence interface, not a declaration that all-20 are native closure events.

## Theorem 3 — finite positive-BRC source count

On the declared 40 equiprobable named signed composite branches, the number of ordered histories of length `m` is `40^m`. Every zero-full-Cell return requires even `m`, since each branch changes the coordinate sum by `+3` or `-3`; equal positive and negative counts are necessary.

Exact enumeration:
- length 2: 1,600 total histories, 423 distinct full endpoints, and **40** zero returns;
- length 4: **11,160** zero returns.

Proof of the four-step count: let `D_2(y)` be the positive multiplicity of two-step histories ending at `y`. Symmetry gives `D_2(y)=D_2(-y)`, hence `Z_4=sum_y D_2(y)^2`. Complete enumeration of all 1,600 ordered two-step histories yields this exact multiplicity histogram:

| Two-step endpoint multiplicity | Number of endpoints |
|---:|---:|
|1|40|
|2|200|
|4|90|
|6|60|
|12|30|
|20|2|
|40|1|

It has `423` endpoints, mass `1600`, and squared mass `11160`. `R762HC_CHECK.js` recomputes it using named positive branches. These are *source multiplicities*, not signed-amplitude cancellations, stable-force counts or original primitive BRC steps.

## Theorem 4 — common-depth repair remains necessary

Let `D=(1,1,1,1,1,1)` and let `can6(y)=y-min(y)D`. For any triple `S` and its complement `S^c`,
`h_S+h_{S^c}=D`. Compare two distinct length-two signed candidate histories:

```
(+S,+S^c) -> full endpoint D,  relative endpoint can6(D)=0
(+S,-S)   -> full endpoint 0,  relative endpoint can6(0)=0.
```

Same length and same full family of positive-min-zero three-axis relative readouts, different native full-Cell endpoint. Thus relative endpoint plus event length cannot support all future full-Cell equality/return observations on signed-triad histories. Keep integer common depth (or another proven lossless repair); for ordered BRC source reconstruction, retain branch provenance as well.

## Author verification, reuse and open native obligations

Source: exact frozen P000/X6 foundations above, previous R762HB restricted STAR rank result, and this note's independent six-axis incidence/positive BRC derivation. `R762HC_CHECK.js` is standard JavaScript, with 720 `S6` permutations, 30 ordered pair inputs, 720 fixed-pair stabilizer enumerations, all 20 triples, constructive difference generators, exact 6x6 determinant and 4x4 STAR minor, 1,600 two-step histories, two-step histogram and derived length-four return. A separate author-side SymPy Smith normal form calculation produced `(1,1,1,1,1,3)`; direct integer DP checked `Z_2=40, Z_4=11160`. Executable assertions and evidence are provided; independent review: `NOT_REVIEWED`.

**Next concrete task.** Retrieve a *fully typed* frozen-P000 `TRIADIC_CLOSURE_E` event predicate with force count, per-Cell attachment, Link/Port state, sign and time transition, together with the interlocking genuine rotation update. Test whether its admissible label-only projection is `S6`-invariant, or state precisely which gate coordinate breaks the full-label orbit. Recompute the incidence image and minimal Link decoder rank on that **actually admitted** event set. Retain the original q9 full-vector period/lift obligation independently. The current frozen Foundation names native closure as open; no native admissible event or stable equilibrium has been certified here.
