# Addendum: an exact six-dimensional legal 13-arc stratum, with a four-dimensional twelve-vertex fiber

Date: 2026-11-10 Asia/Shanghai. Pinned sources and original model remain those of the accompanying `RESEARCH.md`. Status: author-side exact rational derivation, independently computed and not yet admitted by an independent review.

## Local classification theorem

Let `z_13` be the new explicit lawful thirteen-positive-arc physical point in `RESEARCH.md`. Let

[
m=(0,0,0,1/80,-1,0,0,13/4),
]
[
n=(34101,-293725,-85599,42525,937899,293725,85599,-3287440).
]

Write the codimension-two physical affine plane

[
\Sigma_{13}=\{z:\;m\cdot(z-z_{13})=0,\;n\cdot(z-z_{13})=0\}.
]

There exists an open eight-dimensional neighborhood `W` of `z_13` such that:

1. Every `z in W intersect Sigma_13` is lawful under the original five physical equalities and all 26 nonnegative capacities, is Blackwell-feasible and has exactly **13** as its minimum positive-arc support size.
2. For any lawful, Blackwell-feasible `z in W` outside `Sigma_13`, **no** transfer with 13 or fewer positive arcs exists.

Thus the local **13-edge locus is precisely a six-dimensional relative-open physical stratum**. It is the transverse intersection of the physical target zero-mass face `mu_1=0` and the preceding internal fourteen-arc Blackwell wall `H: n·(z-z_c)=0`. It is not an isolated example.

### Exact linear-algebra proof

The 15×13 reduced column matrix `M13` for the explicit positive solution has rank 13; its two-dimensional left nullspace annihilator `N` gives the following **exact** 2×8 pullback matrix:

```text
N*T =
[[0,0,0,1/80,-1,0,0,13/4],
 [421/800,-11749/2592,-9511/7200,21/32,
    11579/800,11749/2592,9511/7200,-41093/810]]
```

The first row is `m`; the second is `n/64800`. They have rank 2. Thus `b(z)` belongs to the span of the fixed positive 13 columns precisely for `z in Sigma_13`. The unique thirteen-column coefficient vector is affine in `z` and strictly positive at `z_13`; by continuity it remains positive in a common open relative neighborhood on that six-dimensional plane. The four nonmoving capacity zeros at the point are at indices `4,15,19,23`; the first, second and fourth are structurally zero for all nearby parameters, and `mu_1` (index 19) is identically zero on `Sigma_13`. Every other capacity slack is strictly positive at the base point. Hence the real physical conditions remain legal in a small relative neighborhood.

The ten mandatory-arc dual margins are strictly positive at `z_13` and therefore remain so locally. Exhaustive exact quotient enumeration of `binom(20,2)=190` pair candidates excludes every 12-or-fewer-arc realization at `z_13` and throughout some common neighborhood (finite family of closed column spans).

In addition, independently check all `binom(20,3)=1140` possible triples beyond the ten forced arcs. **Exactly 28** three-column spans contain the quotient target at `z_13`; each has a full 15×13 rank-13 column matrix and its two-dimensional annihilator pulls back to the very same two-dimensional normal row space `span(m,n)`. The other **1,112** possible spans exclude the contact and, being a finite family of closed linear spans, remain excluded in a sufficiently small common neighborhood. Therefore no alternative thirteen-arc support can appear off `Sigma_13` sufficiently near the contact. Among the 28 matching spans, **12** have strictly positive coefficients and **16** have at least one negative coefficient, all checked by exact rational linear solves.

### Preserved BRC transport-branch fiber

The twelve positive thirteen-arc supports are all precisely

```text
ten mandatory arcs
+ one choice from ((2,1),(3,1),(4,1))
+ one choice from ((3,2),(4,2))
+ one choice from ((0,3),(2,3))
```

At `z_13`, the union of these branch supports has **17** distinct arcs and matrix rank **13**. Strictly mixing all twelve positive extreme solutions gives an 18? No: a **17-positive-arc** transport at the same physical marginal. The resulting coordinate-support transfer face has dimension `17-13=4`, twelve vertices and seven coordinate facets, combinatorially the product `Delta_2×I×I`, inherited from the parent 14-edge wall but with its common arc `(1,5)` deleted. At sufficiently nearby points on `Sigma_13`, all twelve bases remain positive and preserve this combinatorial face structure.

The four-dimensional face is a set of distinct **transport-branch configurations** sharing exactly the same complete seven-statistic observed marginals; its dimension is an observer-fiber property, not a new native X6 axis.

## Verification and next step

The independent local script `r5_13_triples.py` tested all 1,140 triples, obtained 28 matched, 12 strictly positive, and checked that all 28 pullback normal spans equal the same `m,n`. The independent script `r5_exact13_sheet.py` computed the 2×8 left-annihilator pullback, rank 2, six tangent directions, six distinct infinitesimal exact physical witnesses and all relevant positive margins. `VERIFY_13_STRATUM.py` is the repository-native reproducible wrapper using the source-pinned `VERIFY_13.py`; the actual independent reconstruction output is saved separately as `STRATUM_OUTPUT.txt`. Its wrapper has not yet been run byte-identically against a full source checkout.

Next find a rational 12-arc legal contact on a further capacity or branch boundary, or prove local/nonlocal restrictions on 12-arc possibilities in the frozen physical family. Resolve any actual discrepancies during independent audit without modifying frozen inputs.
