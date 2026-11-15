# R169 — Unbounded first-collision delay with nonconstant suffix and unbounded subsequent lifespan

Date: 2026-11-15 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_CHECKED / NOT_REVIEWED.
Scientific frozen input: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Scope: finite binary Sturmian *external scalar phase observer* as defined in R167–R168. This is not a native BRC or X6 identity assertion. Native branches, signed ports, path order, multiplicity and provenance remain distinct.
Dependencies: R162, R164 and particularly R167 final-horizon non-remergence @ `d700f5c6ad0141a1fb6e8636119182b677e36f31`; R168 singleton-family source @ `fa956be5d33160ee8db4d62e64538c5d9d2b58f6`. Both are author proofs awaiting independent mathematical review.

## Definition of the observer

For an admitted binary word `w=w_1...w_n`, let `p_0=0` and `p_i=sum_{t=1}^i w_t`. Its feasible intercept interval at slope `theta in [0,1]` is `I_w(theta)=intersection_{i=0}^n [p_i-i theta,p_i+1-i theta]`. Its positive-width slope support is `(alpha,beta)`. Write the **unscaled exact signature** as
`S(w)=(alpha,beta,A,B)`, `A=min_i(p_i+1-i alpha)`, `B=max_i(p_i-i beta)`.
These unscaled endpoint intercepts are equivalent to denominator-scaled `U,V` in R164. Only *admitted* words possess the signature; two inadmissible words do not constitute an alias.

The complete slope-pair oracle used below is
`alpha=max(0,max_{0<=i<l<=n}(p_l-p_i-1)/(l-i))`,
`beta=min(1,min_{0<=i<l<=n}(p_l-p_i+1)/(l-i))`,
followed by the exact endpoint extrema `A,B`.

## R169A. A multi-one nonconstant-suffix infinite collision family

**Theorem.** For every integer `k>=2`, set
`u_k=01 0^k 1 0^(k-1) 1` and
`v_k=01 0^(k-1) 1 0^k 1`.
Both words have length `m=2k+3` and exactly three ones, and differ only by an adjacent `01 <-> 10` exchange at positions `j=k+2,j+1=k+3`. Their suffix after this exchange is the same nonconstant word `0^(k-1)1`.

They have **identical valid signatures**, explicitly
`S(u_k)=S(v_k)=(1/(k+1),1/k,k/(k+1),(k-2)/k)`.

**Proof.** The one-positions are `(2,k+3,2k+3)` for `u_k` and `(2,k+2,2k+3)` for `v_k`. Apply the exact strip-pair inequalities given above. If the interval `(i,l]` contains `d` ones, then its constraints are `(d-1)/(l-i)<=theta<=(d+1)/(l-i)`.

For the lower endpoint, `d=0,1` contribute no positive lower bound. Every interval containing two ones has length at least `k+1`, and a pair of neighboring ones with gap `k` attains this value. Every interval containing all three ones has length at least `2k+2=2(k+1)`, attained from index `1` to `2k+3`. Hence `alpha=1/(k+1)`.

For the upper endpoint, `d=0` intervals have length at most `k` (the longest zero run); `d=1` intervals have length at most `2k`; `d=2` intervals have length at most `2k+2<=3k`; `d=3` intervals have length at most `2k+3<=4k`. These inequalities all hold for `k>=2` and yield `beta>=1/k`. A zero run of exactly `k` supplies `beta<=1/k`. Thus `beta=1/k>alpha`, and both words are admitted.

At `alpha=1/(k+1)`, `p_i+1-i alpha` decreases between consecutive ones, so its minimum is among `i=1`, just before the second/third one, and the terminal index. Direct substitution shows its global minimum is `A=k/(k+1)`, attained at `i=1` in both words. At `beta=1/k`, `p_i-i beta` decreases between ones, so the maximum is among indices `0,2,` the second-one index, and `m`. These values are at most `(k-2)/k`, with equality at `i=2`. Thus `B=(k-2)/k`, completing the identical signature formula. QED.

## R169B. Exact first birth after an arbitrarily long nonconstant suffix

**Theorem.** Consider the prefixes of `u_k,v_k` starting at length `k+3`, immediately after the adjacent exchange is complete. They are *distinctly signed* at every length `n=k+3,...,2k+2`; they first become equal at `n=2k+3`, after exactly `k` common appended symbols `0^(k-1)1`.

**Proof.** At each such earlier length there are exactly two ones. For any two-one word whose one-positions are `a<b`, the exact positive lower support endpoint is `1/(b-a+1)`: the only positive pair constraint has `d=2`, and the shortest interval containing both ones has length `b-a+1`. Consequently the earlier prefixes of `u_k` have `alpha=1/(k+2)`, while those of `v_k` have `alpha=1/(k+1)`. Both are admitted because each is a prefix of an admitted final word and shortening cannot shrink slope support. Their signatures therefore differ. R169A establishes equality exactly when the common final one arrives. QED.

In particular, the **first-collision delay is unbounded even when the common appended suffix is required to be nonconstant and the final words contain three ones.** This goes beyond the all-zero singleton suffix in R168.

## R169C. Exact maximal post-birth survival under *any* common suffix

**Theorem.** After the first collision at `m=2k+3`, there is precisely one preserving common suffix of every length `0<=h<=k-1`, namely `0^h`. There is no preserving suffix of length `h>=k`. Thus the first collision can persist for an additional `k-1` steps, also unbounded in `k`.

**Proof.** At collision, the unique differing prefix is `j=k+2`, the larger prefix count is `q=2`, the common total count is `N=3`, and `alpha=1/(k+1), beta=1/k`. The R167 exact final-horizon certificate for a common suffix is
`q+t_h beta-1<=N_h<=q+t_h alpha`, where `t_h=m+h-j=k+1+h`, and `N_h` is the total ones count after `h` extra symbols.

For `0<=h<=k-1`, these bounds become `2+(h+1)/k<=N_h<=3+h/(k+1)`. The **only integer** in this interval is `N_h=3`. Hence each symbol must be zero; this unique suffix indeed satisfies the certificate. At `h=k`, the allowed interval is `[3+1/k,4-1/(k+1)]`, containing no integer. R167 final-horizon non-remergence rules out equality at any later `h`, whether or not intermediate words remain admitted. QED.

## Examples and exact evidence

- `k=2`: `0100101` and `0101001` first coincide at length 7 with `(1/3,1/2,2/3,0)`; their signatures remain equal after one additional zero, then split.
- `k=3`: `010001001` and `010010001` first coincide at length 9 with `(1/4,1/3,3/4,1/3)`; two additional zeros preserve equality.
- `k=4`: length 11, shared signature `(1/5,1/4,4/5,1/2)`, three additional zeros preserve equality.

Independent exact-`Fraction` pair-strip oracle: `R169_nonconstant_collision_check.py`; data: `R169_verification.json`, marker `R169_NONCONSTANT_BIRTH_LIFESPAN_EXACT_PASS`. Executed checks: 54 family words for `k=2..28`, 405 pre-birth prefixes, 306 zero-extension cases, and exhaustive 1,016 common binary continuations of lengths `0..6` for `k=2..9`. All comparisons require *both* signatures to be valid, preventing `None==None` false positives. The entire infinite claim rests on the symbolic argument above; the finite checks probe arithmetic and boundary cases. Independent reviewer/Lean: not performed.

## Connection and next scientific question

This family exhibits simultaneously `arbitrarily late birth`, `nonconstant common suffix`, and `arbitrarily long but finite post-birth lifespan` under one precise external observer. Its ordered symbolic paths, middle one-position and branch label carry an identity residual that survives when scalar signatures coincide. Investigate the precise distribution of maximal collision lifespan over fixed length/weight and whether a minimum typed *signed-port/path* enrichment distinguishes these pairs while preserving legitimate future operations. Native BRC transfer needs an explicit observer map and verified fiber-safety certificate under P000.

Preservation provenance: new independent portable research; no formal task CLAIM/Result/Review represented. Current native S23 publication/owner read is separately reconciled by original request `em-r1-20261115-1103-r169-s23-continuation-01` and not a prerequisite for research file preservation.
