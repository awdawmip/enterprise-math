# R45 — Farey-boundary provenance transfer and risk compiler

**Status:** Author-side proof plus exact finite validation, independent mathematical review pending. **Date:** 2026-11-10. **Scientific freeze:** `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`. **Predecessor:** R44 `e3e19dd3b0b98a7329bf5ccd24b877228a284c52`. Scope: auxiliary irrational circle-rotation S23/AV observer; native X6/P000 is unchanged.

## Exact setting

Take irrational `0<theta<1`, m>=2 historical half-open oriented arcs, labelled by the historical phases `{t theta}` for 0<=t<m. Each current elementary gap has its integer source t (the starting phase) and unique original historical owner. Let `R_n=1-sum_I M_n(I)`, where `M_n(I)` is the longest current elementary gap in original arc I, for n>=m. In one Farey stage `a/i<theta<c/j`, `ic-ja=1`, write `u=i theta-a>0`, `v=c-j theta>0`, `w=u+v`, `s=i+j`. R35/R36's frozen exact stage law says the w-gap source set at n is `[n-i,j)` and

`R_q-R_p = (F(q)-F(p))*min(u,v)`

within this stage, where `F(n)` counts historical arcs with no surviving source from `[n-i,j)`. With `tau_k=max{t in [n0-i,j):owner(t)=k}` (or None), `F(n)=#{k:tau_k is None or tau_k<n-i}`. Hence `F(n+1)-F(n)` is 0 or 1.

## Theorem R45.1: exact boundary source-class transfer

At n=s the old w gaps are extinct. The only gap lengths are u and v; `u!=v` since theta is irrational.

* If **u>v**, theta exceeds the mediant `(a+c)/s`. The new neighbors are `((a+c)/s,c/j)` with denominators `i'=s,j'=j`. Their new long length is `w'=u`, whose sources at s are `[s-i',j')=[0,j)`. These are exactly the **old u-gap sources**.
* If **u<v**, theta lies below the mediant. The new neighbors are `(a/i,(a+c)/s)` with `i'=i,j'=s`. Their new long length is `w'=v`, whose sources at s are `[s-i',j')=[j,s)`. These are exactly the **old v-gap sources**.

**Proof.** The signed difference `s theta-(a+c)=u-v` chooses the Stern–Brocot successor. Its new short lengths are respectively `(u-v,v)` or `(u,v-u)`, and their sum is the stated w'. Substitute the new denominators into the verified gap-source interval `[n-i',j')` at n=s. Since at s only the old u and v length classes remain, the identified new longest length class is precisely the claimed old class. □

This is a **source-labelled mapping**, not the identity `F_new(s)=F_old(s)`. The old longest class is empty so `F_old(s)=m`, but

`F_new(s)=m - # { owner(t): t in W_new(s) }`

must be recomputed from the owner labels of the surviving u/v class. Dropping that class before the transfer destroys later observational information.

## Theorem R45.2: explicit boundary risk and no-full-risk-query compiler

Let `G=max(u,v)`, `g=min(u,v)`, and `f=F_new(s)`. Then

`R_s = 1 - m*g - (m-f)*(G-g).`

**Proof.** Each historical arc contains at least one current elementary gap because it contains its initial historical phase cut. At s every gap length is either G or g. Precisely m-f historical arcs contain a G-gap, so their local maxima equal G; the other f maxima equal g. Sum them in the definition of R. □

At n=m the current cuts are exactly the original historical cuts, so their m single-gap lengths sum to 1; hence `R_m=0`. Starting with R_m, use each Farey stage's exact rank differences to advance R. At each boundary carry the numerical/affine R_s unchanged, switch to the updated Farey pair, and reconstruct the *labelled* new tau vector using R45.1. This inductively computes the exact entire scalar risk prefix **without any per-boundary full-maxima reconstruction**. R45.2 provides an independent algebraic check on every transferred R_s.

The R43/R44 constant-width rolling window `[J-N,J)` differs from the stage window `[n-i,j)`, whose right endpoint is fixed and whose left endpoint advances. Within a stage at most one owner can lose its last source per update. At a Farey boundary the source class, denominators and owner population change together; the explicit bridge above handles the transition.

## Certified finite computations

The extended executed `VERIFY_R45.py` used exact `Fraction`, independent direct phase-sorted gap maxima, the extinction-only risk compiler, and strict S23 enclosure endpoints `262204504569236716045286/10^24` and `262204504569236716045287/10^24`. It checked four angle/size families plus **six** full compiler cases. For frozen m=128, every n=128..389 was cross-checked at midpoint and both enclosure endpoints, obtaining three stages ending at 164, 225 and 389. At s=164 and 225, `F_old(s)=128` in both cases while `F_new(s)=67` and `F_new(s)=0` respectively. `R_389=-7551+28800 theta`. Every one of 261 updates matched the frozen R32 `AFFINE_RUNS_R32.tsv` byte-derived coefficients at the same n. Two other finite rational angles approximate sqrt(2)-1 and sqrt(3)-1 and are treated strictly as finite noncollision test angles.

Standalone `VERIFY_R45_COMPACT.py` independently executes the main geometric/reference comparison and both transition identities at the two S23 intermediate boundaries, testing both rational enclosure endpoints. The local extended evidence JSON has SHA-256 `460605f646a5f234e2d1621e8e45119519b01d9e9b0b32ce7c4109b6f83b1689`; the full compiler certificate JSON has SHA-256 `7d68018c190c556b990d48c283c6387791d35a474fadfd103683ebcdc2e98e8d`. Local regression result: `PASS_R45_FROZEN_R32_261_UPDATE_CHECK`.

## Arithmetic / BRC scope and successor

Historical sorting costs O(m log m) certified comparisons on integer/precision-dependent operands; stage preparation incurs the actual R37/R40 last-source selection cost `P_e`; each sorted-tau rank query uses O(log m) index comparisons; Farey neighbor update is O(1) integer operations of evolving bit width; output K runs consumes at least the bytes of their endpoints and coefficients. This removes whole-boundary maximum-gap reconstruction **from the generation path**, not input conversion, certification, historical preprocessing, source selection, other bit costs or final output. Geometric reconstructions remain the *independent finite validator*.

BRC owner-labelled provenance transfer: `REUSE_APPLIED` for the auxiliary observer and declared future scalar risk operations. No accepted native-X6 theorem, new CLAIM or independent proof review is asserted. Next R46: integrate into R32's long-horizon jump/compiler with large-denominator boundary rank/select, test a distant frozen stage and measure full integer bit costs.