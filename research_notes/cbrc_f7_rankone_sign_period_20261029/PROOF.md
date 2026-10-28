# CBRC F7 period branch: self-contained signed-permutation obstruction

Status: **NONBLIND / SUPPLEMENTARY_AUTHOR_SIDE / UNREVIEWED / NOT_ADMITTED / NOT_A_NATIVE_DRIVER_REVIEW**. This note is a candidate for independently verifying *one branch* of the F7 theorem repair; it is not a new task or formal review.

Source: `enterprise-math@943658634314612424dd7b004ed59eff4afe0bbc`. Exact frozen F7 Result: `RR-AA38973D56330E59D315` (Git blob `3366edeae347e76b1f6a50bc45a6c6e4cd2dd472`). P000 frozen global source: `7b33f8066e9993e7c941959a9d738ed405248eb8`, P000 blob `ba8e4c75cdb3663ab3fde07e4286782344b0ed42`.

## Theorem

Let `h:Z -> [0,infinity)` have `h(0)=0` and `h(n)>0` for all `n != 0`. **Evenness is not assumed.** If `B=[[a,b],[c,d]] in GL_2(Z)` satisfies, for all integers `x,y`,

`h(ax+by)+h(cx+dy)=h(x)+h(y)`, (E)

then `B` is a signed permutation matrix. For noneven `h`, a signed permutation with negative entries may still fail (E): this is a necessary condition only.

### Exact mixed-difference sign identity

Write `D_r h(t)=h(t+r)-h(t)`. If nonzero integers `r,s` have `D_r D_s h(t)=K` independently of `t`, exact discrete integration gives

`h(ir+js)-h(ir)-h(js)+h(0)=i*j*K` for every `i,j in Z`.

Put `i=s`, `j=-r`. Since `h(0)=0`:

`h(rs)+h(-rs)=rs*K>0`. (1)

No symmetry, regularity or bounded enumeration is used.

### All four entries nonzero

Take the mixed input difference of (E):

`D_a D_b h(ax+by)+D_c D_d h(cx+dy)=0`.

Since `B` is surjective on `Z^2`, the output arguments vary independently. Thus these two mixed differences are constants `K` and `-K`. Using (1),

`ab*K>0`, while `cd*(-K)>0`.

Therefore `abcd<0`, so `ad` and `bc` have opposite signs. They are nonzero integers and hence

`|det B|=|ad-bc|=|ad|+|bc|>=2`,

contrary to unimodularity. At least one entry is zero.

### Zero entry

If `a=0`, then `|b|=|c|=1`. By (E) with `x=0`, `h(by)+h(dy)=h(y)`. If `b=1`, strict zero separation implies `d=0`. If `b=-1`, apply the identity at `y` and `-y` and add: `h(dy)+h(-dy)=0`. Hence again `d=0`. The resulting matrix is signed anti-diagonal. The two-slot swap `S` preserves `h(x)+h(y)`; applying the same argument to `S B`, `B S`, or `S B S` handles zeros in any other position. Unimodularity forces each remaining nonzero entry to have absolute value one. QED.

## F7 period-branch consequence

In the frozen F7 revision, let `f:Z^2->[0,infinity)` obey `f(0,0)=0`, old-projection positivity `n!=0 => f(n,m)>0`, and exact two-slot conservation under `A in GL_4(Z)`. Suppose `f` has a nonzero period. Every period has zero old coordinate, hence `Per(f)={0} x kZ` for some positive integer `k`.

The period subgroup of the separable two-slot scalar is exactly `Per(f)^2`: a pair period makes independent first differences constant; global lower boundedness forces both constants zero by iterating shifts forward and backward. Since `A` is invertible and scalar-preserving, it preserves this subgroup and induces an automorphism of `(Z x Z/k)^2`. The induced torsion-free old-coordinate map is `B in GL_2(Z)`.

Define `g(n)=min_{m mod k} f(n,m)`. Finite-fiber positivity gives `g(n)>0` for `n!=0`, and `g(0)=0`. The induced automorphism bijects input and output finite fibers; minimization of the two-slot exact conservation identity therefore yields `g(B(n_1,n_2))` in separable sum form equal to `g(n_1)+g(n_2)`. By the theorem, `B` is signed permutation, whose first column has exactly one nonzero old output. The frozen F7 A0 requires *two* nonzero old outputs from that first elementary column. Contradiction.

Thus **the nonzero-period branch is impossible**. This only supplies a self-contained alternative proof for the rank-one signed-permutation dependency. The other F7 block-rank cases and whole Result still await exact-set review.

## Evidence and provenance boundary

**Historical source-pin type correction (verified 2026-10-29):** the frozen F7 return's suffixes `@bc046c8d77910ddb1f42b572a736d9d938ecbb9c` (blind input) and `@f0a0edc9ef5d8e0ea1b21727f5a7c92f681e09a5` (F4 report) are **Git commit SHAs, not blob SHAs**. Authenticated `fetch_commit` resolves the former to the original F7 blind-packet freeze commit, and the latter to the F4 evidence-manifest freeze commit. Authenticated `fetch_file(path, ref=<cited commit>)` successfully reads the exact path at each historical commit: F7 input blob `9f03062f665ff4117463b746ec630f659cc22cbc`, F4 report blob `faff2e589583d8693d1c2f25c76b6b30fec80d8e`. The earlier 404s arose from passing **commit IDs to the blob endpoint**; they do not indicate missing historical evidence. The immutable cited commits and returned file blobs remain distinct provenance fields. This resolves only that source-lookup incident, **not** independent mathematical review, source-author independence or native review admission.

The lemma was derived with full access to the F7 author return and source, so it is **not a clean-blind independent Driver review**. It neither materializes Reference passes nor closes Synthesis, Follow-up, Result acceptance, or a V2 task. The next eligible Driver should inspect the *entire* frozen Result and exact review set, independently verify this period argument if useful, and preserve the now-verified commit-ref/file-blob distinctions. The original controller request `drv-ro-taskscan-20261027-1656-260b` remains for control maintenance.

Companion exact regression program: `CHECK.py`. Finite calculations check algebraic instances and small matrices; they are not the universal proof.
