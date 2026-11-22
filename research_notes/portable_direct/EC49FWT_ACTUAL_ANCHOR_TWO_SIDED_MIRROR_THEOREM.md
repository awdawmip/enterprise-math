# EC49FWT — Actual Farey anchor realizability and two-sided mirror trace

**2026-11-22 · frozen science pin `BRC16943` · continuation of EC49FWS@95507f064ee46910b32e26d1c49e6df4a05b84fc · AUTHOR_PROVED / EXACT_FINITE_CERTIFICATE / PARENT_DEPENDENT / NOT_REVIEWED**

## 1. Exact model and normalization

Retain the inherited certificate
[
C_{11}(h,n)=P_{10}(hmod10,nmod10) land (9h+10n
otequiv0pmod{11}),
]
where `P10` is the same 44-pair predicate from the frozen BRC16943 Bernoulli/projective calculation. Its defining slope/parity formula is reproduced in the companion verifier. In particular, `P10(-h,-n)=P10(h,n)`, and hence `C11(-h,-n)=C11(h,n)`.

For any reduced anchor `0<a<b`, write `y=b-a`. The signed determinant-`s` Farey branch consists of integer pairs `(h,n)` with `y*h-a*n=s` (`s=-1` left, `s=+1` right). Its direction is `(a,y)`; positive sufficiently late points have `h>0,n>0`, denominator `d=h+n`, and satisfy `b*h-a*d=s`.

Use the following **fixed, reproducible coordinate convention** for either sign. Choose the unique `h0 in {0,...,a-1}` solving `y*h0=s (mod a)` (when `a=1`, put `h0=0`), then `n0=(y*h0-s)/a`. Let `(x,z)` be the lexicographically first pair in `{0,...,9}^2` satisfying `y*x-a*z=s (mod 10)`. Exactly one `t0 in {0,...,9}` has `(h0+a*t0,n0+y*t0)=(x,z) (mod 10)`. Put `(H,N)=(h0+a*t0,n0+y*t0)`.

Define
[
U_s(t)=1_{P_{10}}(H+at,N+yt),quad
L_0=9H+10N,quad D=9a+10y=10b-aquad(mod11).
]
Unimodularity implies `(L0,D) != (0,0) mod 11`. When `D=0`, put `V_s=Z/11Z`; otherwise let `z_s=-L0 D^{-1} mod 11` and `V_s=(Z/11Z)\\{z_s}`. The whole indexed trace is exactly
[
oxed{C_{11}(H+at,N+yt)=U_s(tmod10),1_{V_s}(tmod11),quad tinmathbb Z.}
]

An observer's static 110-site coordinate is the **specified normalized affine parameter** `t mod 110`. Anchor/provenance must be retained to transport a reconstructed trace into actual height-dependent Farey neighbors. These are scoped rational certificate observers within the user's native X6 research framework, not independent native spatial axes or a full X6 dynamics claim.

## 2. Finite universal realization theorem

**Theorem (new).** With the above *deterministic* normalization, already among positive coprime anchors with `2<=b<=139`:

* The left (`s=-1`) traces realize **all 600** products `U x V`, where `U` ranges over the *same 50 frozen EC49FWQ masks*, and `V` is full mod 11 or excludes exactly one of eleven positions. The largest denominator of a first witness is 139.
* The right (`s=+1`) traces realize **600** products from a right-hand 50-mask family, with every full/single-hole factor realized for each right-hand mask; the largest first-witness denominator is 125.
* The left/right 50-mask families have exactly **24 common masks** (hence 76 distinct normalized ten-bit masks across the two signs).

**Proof.** Primitive directions modulo 10 yield the original 72 `(a,y)` residue classes, each with a ten-point unimodular affine orbit; the left masks obtained from the lexicographically first orbit point reproduce exactly the 50 source masks. Every reduced positive `a/b` has the unique stated Euclidean seed and ten-phase origin, so its 110-periodic word factorizes by CRT as shown above. The companion exact integer program enumerates *all* `1<=a<b<=139` with `gcd(a,b)=1`; there are 5,951 anchors. It evaluates both sign branches, does 110 direct-`C11` versus factored-word comparisons for each branch, and accumulates the first `(a,b)` for each `(mask, hole_or_full)`. This yields exactly 600 different pairs per sign, 50 masks per sign, complete `{full,0,...,10}` factor coverage for each mask, and the indicated witness denominators and intersection. There are at most `50*(11+1)=600` states in each declared sign family, so the finite complete witness enumeration establishes full realization. The enumeration and exact assertions, not an untested heuristic, are the finite certificate. For the infinite anchor family the finite witnesses remain valid.

The finite certificate does **not** assert all arbitrary `U,V` combinations occur along one *fixed* anchor, nor that a fixed anchor's provenance is unknown to an observer who is actually given it.

## 3. Sharp fixed-site observation on genuine left Farey anchors

**Corollary (new strength relative to EC49FWS).** For the actual **normalized left** Farey anchor population (varying unknown anchor), an observer given the *complete indexed reflection-defect spectrum* but not the anchor and requiring minimum Hamming separation `r` in membership reads, the exact fixed-site optimum and count, for `1<=r<=10`, are
[
oxed{N_{m actual,left}(r)=3(r+1),qquad
#operatorname{Opt}_{m actual,left}(r)=inom{11}{r+1}^{3}16^{r+1}.}
]
In particular, exact identification requires **6 sites**, one known erasure **9**, and one arbitrary erroneous bit **12**.

**Proof.** EC49FWS established these formulas for its enlarged 600-state family. Section 2 proves equality of that entire family with the actual normalized-left-anchor trace population, so both the lower-bound witness pairs and the upper-bound construction transfer with identical quantifiers. More explicitly, its three necessary disjoint ten-position supports
[
A={1,4,6,9},quad B={2,7},quad C={3,8}
]
are achieved by same-spectrum, equal-cardinality pairs of left masks. All eleven missing-column choices for each pair occur at *actual reduced anchors*, so the adversary may remove whichever probed column contains most reads. At least `r+1` reads per group in distinct columns are necessary; one per group in each of `r+1` columns achieves distance `r`. The finite certificate identifies explicit actual-anchor witnesses for each group and every excluded column, and verifies 478 spectral fibers / 122 doubletons, as in FWS. The exact-count formula follows from independent choices of columns and a `4,2,2` site choice in each group's selected columns.

Concrete excluded-column-0 anchor-pair witnesses: `A: U=327,789` from `49/57,23/29`; `B: U=367,491` from `9/32,37/42`; `C: U=701,949` from `9/64,13/14`. All 33 pairs (three groups times eleven excluded columns) are regenerated in the verifier. The other support pairs and optimum-count proof are inherited from the pinned EC49FWS source.

**Knowledge condition matters:** if the *anchor, signed determinant, normalization and frozen predicate* are all known in advance, its trace is directly computable; the 6/9/12 observation cost addresses the declared unknown-anchor compressed observer, not that distinct informational model.

## 4. Paired right/left mirror and future-height bridge

**Theorem (new explicit two-sided relation).** Pick any integer seed `p=(h0,n0)` on the left determinant-minus-one line, direction `v=(a,b-a)`. The reflected seed `-p` lies on the right determinant-plus-one line. For every integer `t`,
[
oxed{C_{11}(-p+t v)=C_{11}(p-t v).}
]
Consequently the entire right-side certification word, indexed from `-p`, is the index-reversal `t -> -t` of the left-side word indexed from `p`, with **no new independent 110-bit certificate**. Each side still needs its signed branch and affine denominator origin. Right/left individually normalized words can differ by a computable integer phase shift (different Euclidean seeds); do not equate them without that coordinate conversion.

**Proof.** The determinant of `-p` has the opposite sign. `-p+t v=-(p-t v)`, and the `P10` slope/parity predicate and the mod-11 nonzero linear condition are both invariant under simultaneous negation of `h,n`. The result holds at every integer `t`, and passes all 654,610 finite mirror comparisons in the companion verifier.

For `H>16b`, invoke the already-proved EC49FVU nearest-certified-neighbor theorem: compute the greatest admissible height-limited indices `t_-(H)`, `t_+(H)` from the left trace `f(t)=C11(p+tv)` respectively at `f(t)` and `f(-t)`, retaining the two denominator maps `d_-(t)=d0+bt`, `d_+(t)=-d0+bt`. Then
[
q_pm(H)=d_pm(t_pm(H)),qquad
x_pm(H)=rac{a q_pm(H)pm1}{bq_pm(H)}.
]
The signs in `x_-(H)` and `x_+(H)` are `-` and `+`, respectively. This is an explicit two-sided observation/readout preservation for the exact rational-height process and the stated retained provenance. It is not an identification of full native X6 states.

## 5. Verification, dependencies and continuation

Reproduce with `python3 EC49FWT_TWO_SIDED_ANCHOR_REALIZATION_VERIFY.py`. The output JSON reports `ALL PASS`, 5,951 anchors, **1,309,220** direct `C11`/CRT checks, **654,610** mirror checks, 600 states per sign, 50/50 masks with intersection 24, and all 33 genuine anchor-pair lower-bound witness checks. All loops use integer arithmetic; the finite domain is exhaustive. Infinite assertions rely on the displayed CRT/unimodular proof and valid finite witness realization.

Frozen upstream references: EC49FVU@ac3bdb073b8ccd821cd23e830bcb9ccaf8d09529; EC49FWQ@d091c8f2757f67c18be8056ae976b1e092a21098; EC49FWS@95507f064ee46910b32e26d1c49e6df4a05b84fc. BRC16943, P000, the native six-axis Heartbeat World, joint observer/provenance requirements and source firewall stay unchanged.

Next: determine the **optimal two-sided jointly observed** robust code when the same unknown anchor couples left and right words, rather than treating each sign as independent. Compare coordinate-aware, anchor-hidden and anchor-given observation models before inferring any saving. Also test whether the retained signed Farey gap readout yields a safe quotient for a specifically declared native-X6 future operation; no such global transfer is asserted here.

**Publication/authority scope:** Independent portable author-side mathematical note; no new Task, active-owner CLAIM, protected PROGRESS, Result, or Review. Activity association requires a verified own native identity; do not infer one from the GitHub actor.