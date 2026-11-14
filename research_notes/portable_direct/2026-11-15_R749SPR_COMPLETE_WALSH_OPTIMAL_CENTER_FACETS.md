# R749SPR — Complete irredundant rational facets of a calibrated Walsh minimax-center polytope

**Status:** AUTHOR_EXACT_NOT_REVIEWED. **Date:** 2026-11-15. **Frozen scientific pin:** `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`. **Direct predecessor:** R749SPP–SPQ, Draft PR #2456 at `bbcbdf7c814590e3210e3f116a754b89cb4a6fc5`. **Scope:** the auxiliary 16-atom Walsh source fiber; no identification with native X6/V29/V39 events is assumed.

## 1. Model and exact theorem

For `k=0,...,15`, write `chi_m(k)=(-1)^popcount(k&m)`, with `m=3,12,15,1,2,4,8`. The 16-atom probability laws in the frozen model are

```text
p(t,s,h,u,v,w,z)[k] =
 (1 + t chi_3(k) + s chi_12(k) + h chi_15(k)
    + u chi_1(k) + v chi_2(k) + w chi_4(k) + z chi_8(k)) / 16.
```

Fix `(t,s)=(1/10,1/2)`. Let `F` be the nonnegative laws of this form. Define the calibrated minimax-center set

```text
C = {q in F : max_{P in F} TV(P,q) = 9/20}.
```

R749SPP–SPQ established the common free/calibrated minimax radius `rho=rho_cal=9/20`, proved every `q in C` satisfies `w=z=0`, and gave a strict inner octahedron. The new result completely determines `C`.

**Theorem (complete irredundant H-representation).** Put `H=10h, U=10u, V=10v`. The full set `C`, including every feasible calibrated center in the original five-free-coefficient fiber, is exactly

```text
q = p(1/10,1/2,H/10,U/10,V/10,0,0),
subject to all eight inequalities:
 -H-U-V >= -2          -H-U+V >= -2
 -H+U-V >= -2          -H+U+V >= -2
  H-U-V >= -2           H-U+V >= -4
  H+U-V >= -4           H+U+V >= -2.
```

Every inequality defines a genuine facet. This is a bounded full-dimensional polytope with exactly **8 facets and 11 vertices** in scaled coordinates:

```text
(-2,-1,1)   (-2,1,-1)   (-1,-2,1)   (-1,-1,2)
(-1,1,-2)   (-1,2,-1)   (0,-2,0)    (0,0,-2)
(0,0,2)     (0,2,0)     (2,0,0).
```

The previously certified octahedron `|H|+|U|+|V|<=2` is a proper subset. For example `(-1,1,-2)` is a vertex of the complete set.

## 2. Necessary conditions: moment witnesses and eight event inequalities

Use scaled source coordinates `Y=10(h_src,u_src,v_src,w_src,z_src)` and row vectors
`a_k=(chi_15(k),chi_1(k),chi_2(k),chi_4(k),chi_8(k))`.
The source polytope is given by all 16 inequalities

```text
a_k dot Y >= -10-chi_3(k)-5 chi_12(k).
```

The four compatible sources `Y=(1,0,0,9,4)`, `(1,0,0,-9,-4)`, `(1,0,0,4,9)`, `(1,0,0,-4,-9)` prove `w=z=0`: for any center at radius at most `9/20`, the variational moment bound `|E_P chi_m-E_q chi_m| <= 2TV(P,q) <=9/10` forces its `chi_4` and `chi_8` moments both to zero. All four source laws pass the 16 exact nonnegativity checks.

For an event `A\subseteq {0,...,15}`, let `v_A=sum_{k in A}a_k`. The exact event risk inequality

```text
P_Y(A)-q_Q(A) = (v_A dot (Y-Q))/160 <= 9/20
```

for `Q=(H,U,V,0,0)` becomes `v_A[0:3] dot (H,U,V) >= v_A dot Y -72`.
The following eight explicit pairs (bit-mask specifying event membership, and feasible scaled source Y) give **all eight proposed facets** with equality in their corresponding event inequality:

| Facet normal m | Right side c | Event mask | Feasible source Y | Event vector v_A |
| --- | ---: | --- | --- | --- |
| (-1,-1,-1) | -2 | 0x0F8F | (-1,0,0,9,6) | (-1,-1,-1,7,1) |
| (-1,-1,1) | -2 | 0x00BF | (-1,0,0,6,9) | (-1,-1,1,1,7) |
| (-1,1,-1) | -2 | 0x00DF | (-1,0,0,6,9) | (-1,1,-1,1,7) |
| (-1,1,1) | -2 | 0x01FF | (-1,0,0,6,9) | (-1,1,1,1,7) |
| (1,-1,-1) | -2 | 0x00EF | (0,-1,-1,5,9) | (1,-1,-1,1,7) |
| (1,-1,1) | -4 | 0x02FF | (-1,0,0,6,9) | (1,-1,1,1,7) |
| (1,1,-1) | -4 | 0x04FF | (-1,0,0,6,9) | (1,1,-1,1,7) |
| (1,1,1) | -2 | 0x007F | (0,1,1,5,9) | (1,1,1,1,7) |

For every row the independently checked integer equality `v_A dot Y=72+c` establishes its supporting halfspace. Thus every optimal calibrated center lies in their intersection `K`.

## 3. Sufficiency, exact arithmetic and irredundancy

All eight sign normals are present, so `K` is bounded; the origin is a strict interior point, hence `K` is three-dimensional. Solve every one of the `binom(8,3)=56` triple facet intersection exactly by rational Cramer's rule. The feasible intersections give precisely the 11 distinct vertices listed above. Each proposed vertex passes all 16 atomic nonnegativity inequalities.

For source completeness, solve every `binom(16,5)=4368` possible five-active-inequality system with exact integer Bareiss elimination. There are 3008 nonsingular combinations, 196 feasible bases with repetitions and **50 distinct exact rational source vertices**.

For each of the 11 proposed center vertices `Q` and every one of the 50 source vertices `Y`, the exact TV identity is

```text
TV(P_Y,q_Q) = (sum_{k=0}^{15} |a_k dot (Y-Q)|)/320.
```

The maximum numerator is **144** for every proposed center vertex, so their worst-case risk is exactly `144/320=9/20`. By convexity in the source, checking all 50 source vertices proves the upper bound for every source in `F`. By convexity in the center, it extends from the 11 vertices to every point of `K`. The prior antipodal source pair `Y_+=(0,-1,-1,5,9)`, `Y_-=(0,-1,-1,-5,-9)` is feasible and has distance `288/320=9/10`, giving the universal minimax lower bound `9/20`. Consequently `K=C`.

For each of the eight inequalities, at least three affinely independent polytope vertices achieve equality, verified by exact cross products. Each inequality is therefore a true, nonredundant facet. No numerical tolerance or sampling assumption is used in the proof.

## 4. Reproducible evidence and unresolved problem

Run the accompanying standard-library script `R749SPR_FULL_WALSH_CALIBRATED_CENTER_POLYTOPE_CERT.py`. Its JSON output records the eight source/event witnesses, the 50 source vertices check, 56 triple intersections, 11 center vertices and facet incidence. The computation is an exact finite certificate; the proof of exhaustive sufficiency rests on active-basis enumeration and convexity, as above. Status: **AUTHOR_EXACT_NOT_REVIEWED**.

**Next scientific unit:** classify the parametric deformation of this complete center polytope for a rational neighborhood of `(1/10,1/2)`, determining the first combinatorial wall in `(t,s)` and the moving facet event/source witnesses. Maintain the native X6 signed-source event correspondence as a separate, explicit bridge problem.
