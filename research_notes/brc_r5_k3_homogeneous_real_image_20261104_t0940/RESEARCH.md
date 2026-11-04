# R5 K3 — Homogeneous-source observation: equality of the actual real images

Date: 2026-11-04 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

Frozen scientific inputs retained (not refreshed): GLOBAL_KNOWLEDGE_V1 `a01383f825ef9d43b4b754254303298c64041568`; Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`.

Exact predecessor: `research_notes/brc_r5_k3_uniform_superdiagonal_error_fiber_20261104_t0844/RESEARCH.md` at `5e0ff53bd6b9f573258ce2ad7553721176cf6f0c` and its executed `VERIFY.py` observer. The present result is for the same four-source BRC observation model; it is not a theorem about native X6 physics. P000 and ACTIVE worldview are unchanged.

## Exact real strategy model and observer

Let source capacities be `c=(1/8,1/6,1/16,3/32)`, indexed by `S=(C,I,BJ,IJ)`. Fix arbitrary real `0<r,v,p,q<1`, each identical across sources; in particular there is no requirement `v>r`. A FULL policy chooses `x,y in [0,1]`, `i in [0,1-x]` and for every source `z_s,t_s,u_s in [0,1]`. Define

```
w=(c_C, c_I*(1-x), c_BJ*y, c_IJ*i),
d=w_BJ+w_IJ,       W=sum_s w_s,
M_s=w_s*z_s,       Z_s=(2/3)*M_s*t_s,       U_s=Z_s*u_s,
M=sum_s M_s,       Z=sum_s Z_s,            U=sum_s U_s.
```

The observer coordinates `(eP,eQ,TP,TQ)` are

```
eP=107/128-21*x/128+d/4-(1/2-p/8)*Z,
eQ=13/64+3*x/64-d/2+(1/8+q/32)*Z,
TP=3+M+(3/2)*Z+r*U,
TQ=3+M/2+(3/8)*Z+(v/4)*U.
```

A seedless LR policy has `i=(1-x)*y` and the three stage probabilities shared by every source (`z_s=z,t_s=t,u_s=u`). Denote the actual, nonconvex real observation images by `O(FULL)` and `O(seedless LR)`.

## New theorem (all-real constructive equivalence)

For every real `r,v,p,q in (0,1)` and every FULL behavioral strategy under the foregoing constraints, a seedless LR behavioral strategy has **the identical four observation coordinates**. Consequently

```
O(FULL) = O(seedless LR)
conv O(FULL) = conv O(seedless LR).
```

This conclusion holds uniformly for `v>r`, `v=r`, and `v<r`; it settles the source-homogeneous subfamily at the real-image level, stronger than convex-hull equality.

### Complete proof: explicit FULL -> LR reconstruction

For a FULL policy, its source masses imply

```
0 <= d <= c_BJ+c_IJ*(1-x).
```

Define the LR upstream variables as

```
y' = d/(c_BJ+c_IJ*(1-x)),     i'=(1-x)*y'.           (1)
```

The denominator is at least `c_BJ=1/16>0`, so `y' in [0,1]`. The resulting LR mass vector has

```
d'=c_BJ*y'+c_IJ*i'=d,
W'=c_C+c_I*(1-x)+d'=W.                               (2)
```

The original masses satisfy `W>=c_C=1/8>0` and

```
0<=M<=W,     0<=Z<=(2/3)*M,     0<=U<=Z.             (3)
```

Define the three shared LR continuation probabilities

```
z'=M/W,
t'=(3*Z)/(2*M) if M>0, else 0,
u'=U/Z if Z>0, else 0.                                (4)
```

They lie in `[0,1]` by (3). Their LR aggregate stage masses are

```
M'=W'*z'=M,
Z'=(2/3)*M'*t'=Z,
U'=Z'*u'=U.                                            (5)
```

If `M=0`, then `Z=U=0`; if `Z=0`, then `U=0`, so (5) also holds in both zero-denominator branches. The four displayed observer equations depend on the policy only through `(x,d,M,Z,U)` for source-uniform `r,v,p,q`. Equations (2) and (5) therefore prove all four coordinates match exactly. This proves `O(FULL) subset O(LR)`. Every seedless LR policy is a valid FULL policy by selecting the same stage parameters at all sources and `i=(1-x)*y`. Hence equality. QED.

### Explicit finite convex certificate for every FULL deterministic policy

Take a FULL deterministic upstream vertex (`x=0 or 1`, `y=0 or 1`, `i=0 or 1-x`) and source stage choices `j_s in {0,1,2,3}`. With the original mass vector, set

```
pi_j = (sum_{s:j_s=j} w_s)/W  for j=0,1,2,3.
```

Then `pi_j>=0` and `sum_j pi_j=1`. Let `L(x,Y,j)` be the deterministic seedless LR observation for upstream `x`, upstream `Y in {0,1}` and common stage `j`. For fixed `x,j`, all observer coordinates are affine in the LR parameter `y'`. As an exact identity,

```
O_FULL(x,y,i,(j_s)_s)
= sum_{j=0}^3 pi_j * ((1-y')*L(x,0,j)+y'*L(x,1,j)).    (6)
```

This is an explicit nonnegative convex combination of at most eight seedless LR deterministic observation vectors, with coefficients summing to one. Since the observation space is four-dimensional, Caratheodory's theorem further gives an at-most-five-vertex representation, though equation (6) already certifies containment without an LP solver.

## Executed exact-rational evidence

Sibling `VERIFY.py` checks each of the 1,536 FULL deterministic choices against both the direct real LR reconstruction (1)–(5) and the at-most-eight-vertex LR rational certificate (6), including nonnegativity and coefficient sum. Six different rational parameter tuples yield 9,216 verified deterministic certificates. Additionally, 30 non-vertex rational FULL policies (five per tuple) are reconstructed exactly. Inputs cover `v>r`, `v=r`, `v<r`, stage corner cases and zero denominators. Only Python standard-library `Fraction` is used; see the actual saved execution transcript `EXACT_OUTPUT.txt` with marker `PASS_EXACT_R5_K3_HOMOGENEOUS_REAL_IMAGE_EQUALITY`. Finite validation checks the implementation and rational instances; the real-universal assertion follows from the displayed algebra.

## Information retained, interpretation and next dependency

The four-coordinate observer factors through `(x,d,M,Z,U)` for source-homogeneous parameters. Source-specific stage provenance can differ between the reconstructed policies, but is invisible to this declared observer; equivalence is limited to these four outputs, not future source-resolving operations. Previous author-side evidence shows how heterogeneous answer coefficients expose nonzero error-fiber residuals in the `v>r` region. The next discriminating boundary is homogeneous clocks with **heterogeneous terminal probabilities** when `0<v<=r<1`. Before claiming a complete K3 sixteen-parameter classification, independently reconcile the previous necessary results and their exact boundary hypotheses. R5's original mother objective remains open outside this subfamily.

Validation: AUTHOR_PROVED and EXACT_FRACTION_CHECKED; independent review/admission absent. Publication/readback is a provenance event, not theorem acceptance.
