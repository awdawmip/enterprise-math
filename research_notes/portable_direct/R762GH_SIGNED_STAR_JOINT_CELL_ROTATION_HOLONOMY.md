# R762GH — Exact minimal joint Cell-depth and signed triadic orientation return

Date: 2026-11-20 (Asia/Shanghai). Task `RS-X6-TRIADIC-CLOSURE-DYNAMICS`, immutable publication `TP2-8B7E13C5904A2D6F1142`. Status: **AUTHOR-PROVED in the candidate model below; NOT_REVIEWED**. Continuation of R762GG at `awdawmip/enterprise-math@445625797db772940f17487283afa04aeed02571:research_notes/portable_direct/R762GG_STAR_TRIAD_EVENT_LATTICE_AND_DEPTH_HOLONOMY.md`. The taskbook and P000 science inputs remain pinned respectively to `857280d1012943290d141d1317179c40ec3cbdf8` and `a72226e2430ffa4786321ac86e7f0c599d5f0389`.

## Typed candidate and BRC provenance

Let the X6 native signed Cell displacement live in `Z^6`, with one chosen coordinate anchor and original native axes. The fixed four K4 STAR triples are
`S0=(0,1,2)`, `S1=(0,3,4)`, `S2=(1,3,5)`, `S3=(2,4,5)`.
Put `Hj=sum(e_i for i in Sj)`. Define `gj` to be the positive 3-cycle on the ordered triple `Sj` (fixing the other native labels). For each sign `s∈{+1,-1}`, declare the competing signed composite event `(j,s)` to update two **separately typed** registers:

```
(x,pi) -> (x+s*Hj, gj^s ∘ pi),    x∈Z^6, pi∈A6.
```

The permutation `pi` is an accumulated axis-label **orientation register**. It does **not** act on the previously accumulated Cell displacement: this is a direct-product candidate, not a semidirect affine rotation acting on `x`. Each composite event still expands into three ordered primitive ±axis steps and carries named 3-ports, their Link cycle, source, branch and multiplicity. A negative transport sign is not a negative BRC weight. Actual native `TRIADIC_CLOSURE_E` legality has **not** been assigned to these candidate branches.

For an ordered event word `w`, let `n_j=#(j,+)-#(j,-)` and let `B` be the six-by-four K4-STAR incidence matrix of R762GG. Its Cell displacement is `Bn`. Write `D=(1,1,1,1,1,1)`. A **joint relative/rotation return** has `Bn=kD` and total permutation product equal to identity. R762GG's exact incidence inverse implies that necessarily `n=(a,a,a,a)` and `k=2a`.

## Theorem 1 — exact shortest nonzero joint return at every depth

For every integer `a≠0`, the minimum number of signed composite events in a joint return with displacement `2aD` is

```
L(a) = 8       if |a|=1,
L(a) = 4|a|    if |a|>=2.
```

The joint depth-holonomy group is **exactly** `2Z`, as in the relative-only transport model, but the first nonzero **joint** return occurs at eight events (24 primitive signed coordinate steps) instead of four.

**Proof (all integer a).** Each event changes exactly one `n_j` by ±1. Hence a relative return with `n=(a,a,a,a)` needs at least `4|a|` letters and has length congruent to `4a` modulo 2. For `a=+1`, length four consists of each of `0+,1+,2+,3+` once. Its 24 possible time orders produce nonidentity permutation cycle types: precisely 16 of type `(4,2)`, 4 of type `(3,3)`, and 4 of type `(5,1)`. Thus length four cannot return both registers.

At length six, exactly one STAR `j` contributes an extra `j+,j-` pair in addition to the four distinct positive types. For each `j` there are `6!/2!=360` different ordered words; the resulting complete finite set has `4*360=1440` words. Exact integer permutation-state enumeration in `R762GH_VERIFY.py` verifies **zero identity products** among these 1440 possibilities; thus length six also fails. The inverse-word map proves the same for `a=-1`.

There is an eight-event witness for `a=+1`:
```
0+ 1+ 2+ 0- 2+ 3+ 0+ 2-
```
It has `n=(1,1,1,1)` and total permutation identity. An eight-event **positive-only** witness for `a=+2` is
```
0+ 1+ 3+ 0+ 2+ 3+ 1+ 2+
```
with `n=(2,2,2,2)` and permutation identity. A 12-event positive-only witness for `a=+3` is
```
0+0+0+ 1+1+1+ 2+2+2+ 3+3+3+
```
since each `g_j^3=id`. Every positive integer `a≥2` is `2u+3v` for nonnegative integers `u,v`; concatenating `u` depth-2 witnesses and `v` depth-3 witnesses yields length `8u+12v=4a`, the lower bound. Inverting every event and reversing word order treats negative `a`. The displayed witnesses and all exact exclusions are checked separately by executable integer verification. ∎

## Theorem 2 — positive BRC counts through event depth eight

Let each of the eight signed composite events have positive BRC probability `1/8`, sampled independently per step, retaining **each individual ordered word** as a distinct source history. Let `J_m(a)` count joint relative/rotation return words of length `m` and common-depth change `2a`. Exact full-distribution DP gives:

| Event steps m | J_m(0) | J_m(+1)=J_m(-1) | J_m(+2)=J_m(-2) | Joint return total |
|---:|---:|---:|---:|---:|
| 0 | 1 | 0 | 0 | 1 |
| 2 | 8 | 0 | 0 | 8 |
| 4 | 120 | 0 | 0 | 120 |
| 6 | 2,192 | 0 | 0 | 2,192 |
| 8 | 44,632 | 16 | 8 | 44,680 |

All odd lengths have no relative return by event-count parity. For comparison, R762GG relative-only return counts at four and eight events are 216 and 343,000 respectively. At event depth eight, the exact unconditional positive-BRC mass of **nonzero-depth joint return** is
```
(2*16+2*8)/8^8 = 3/1048576.
```
No signed-force cancellation or information-erasing quotient was used.

## Independent exact finite validation

`R762GH_VERIFY.py` uses standard-library integer state DP over the **full** tuple `(n0,n1,n2,n3,permutation)` for `m=0,...,8`. It checks total `8^m` weighted paths at each depth, 24 four-event permutation products and their cycle classes, the 1440 six-event exact no-return certificate, 8-event coefficients, monotone positive-only returns at `a=1,2,3`, and independently finds depth-1 and depth-2 witnesses by splitting 8-event words 4+4. `R762GH_EVIDENCE.json` records exact counts and witnesses. The finite computation supports Theorem 2 and the two finite exclusions used in the all-depth constructive proof of Theorem 1. Author-side PASS; independent mathematical review NOT_REVIEWED.

## Research significance and next falsifiable step

The signed triadic orientation register **delays** the first joint nonzero depth loop while preserving the complete even-depth holonomy set. This differs from merely using the A6 generator reachability of R762FY or the displacement lattice of R762GG. Both typed registers and the source-preserving ordered Port/Link event word may affect future legal operations. This candidate must next be tested against the **actual frozen native** `TRIADIC_CLOSURE_E` signed Cell/Link/Port transition and permission definitions. If those native rules do not specify a legal gate, construct and compare explicit typed finite-state Port/Link gates, augmenting the same DP key with that state; do not promote an unconstrained positive-BRC branch to native legality.
