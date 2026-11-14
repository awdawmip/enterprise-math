# R155 — Infinite multi-one central-defect aliases with exact last-absence certificates

Date: 2026-11-15 (Asia/Shanghai). Scientific input frozen at `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Status: author-side exact proof and exact finite computation; independent mathematical review `NOT_REVIEWED`. Scope: the **external scalar tied-phase S23 mechanical-word observer**, with R146 phase-fiber counts. This is not a native X6 theorem or a Heartbeat/BRC–Shor arithmetic experiment.

Predecessors: R146 at `b02b0c242b274bc6a82111dbd3600126a2867319` (`research_notes/brc_s23_av_r146_fiber_affine_period_20261114/PROOF.md`); R153 at `e6e436cb90f6c943b3825a4a2fe26b0500c558f8`; R154/R154B at `e446e8844513be49f214206e0f16d6d740154260`.

## Exact definitions

For a binary word `w` of length `m`, put `s_0=0`, `s_j=sum_{i<j}w_i` and

- `alpha = max(0, max_{i<j}(s_j-s_i-1)/(j-i))`,
- `beta = min(1, min_{i<j}(s_j-s_i+1)/(j-i))`.

An admissible word has `alpha<beta`. Write reduced endpoints `alpha=a/b`, `beta=c/d`, and define cuts `U=min_j[b(s_j+1)-ja]`, `V=max_j[ds_j-jc]`. The R146 exact tied-phase count at `K=L+1`, `L>=1`, is

`C_w(L+1)=ceil((cL-V)/d)-floor((aL-U)/b)-1`.

These definitions and counts are intentionally kept separate from original word identity.

## R155.1 — Infinite multi-one alias theorem

**Theorem.** For every integer `k>=1`, set `m=4k+4` and

`A_k=(01)^k 0010 (10)^k`,  `B_k=(01)^k 0100 (10)^k`.

These are distinct admissible length-`m` words, each containing `2k+1>=3` ones. Nevertheless, their complete signatures agree:

`(alpha,beta,U,V)=(k/(2k+1),1/2,k+1,0)`.

Consequently, for **every** integer `L>=1`, the entire infinite integer phase-fiber count sequences are identical:

`C_{A_k}(L+1)=C_{B_k}(L+1)=ceil(L/2)-floor((kL-k-1)/(2k+1))-1`.

**Proof of the slope support.** Both words begin with `0`, have no `11`, and contain exactly one adjacent `00`. Deleting one zero in that pair produces a fully alternating word starting and ending in `0`, of length `4k+3`. Thus every contiguous factor has `(#zeros)-(#ones)<=2`. Equivalently `(ones+1)/q>=1/2` for every factor length `q`, while the `00` factor attains equality. Therefore `beta=1/2`.

Put `b=2k+1`. Both words contain a contiguous alternating factor `1(01)^k` of length `b` with `k+1` ones: for `A_k` it is in the suffix `(10)^(k+1)`; for `B_k` it lies in the initial `(01)^(k+1)`. Thus `alpha>=k/b`. To prove the reverse, bound `(ones-1)/q` for every factor of length `q`:

1. If `q=2j+1<=2k+1`, the absence of `11` yields `ones<=j+1`, hence `(ones-1)/q<=j/(2j+1)<=k/b`.
2. If `q=2j+1>=2k+3`, there is no alternating factor of that length starting and ending in `1`: the maximal such odd alternating factor has length `2k+1`. Achieving `j+1` ones in an odd factor with no `11` would require exactly that forbidden alternating factor. Thus `ones<=j` and `(ones-1)/q<=(q-3)/(2q)<=k/b`, since `q<=4k+3<=3b`.
3. If `q` is even and `q<=4k+2`, then `ones<=q/2`, so `(ones-1)/q<=1/2-1/q<=1/2-1/(4k+2)=k/b`.
4. The only factor of length `4k+4` is the whole word, which contains `2k+1` ones. Its lower ratio is `2k/(4k+4)<k/b`.

Therefore `alpha=k/b`.

**Proof of the absolute cuts.** For any prefix, let `s` and `z` be its number of ones and zeros, and let `delta=z-s`. Since the word begins in `0` and is alternating except for the extra central zero, `delta` lies in `{0,1,2}`. Whenever `delta=2`, the prefix has passed the defect and contains at least `k` ones. With `a=k`, `b=2k+1`, the lower-cut expression is

`b(s+1)-k(s+z)=b+s-k*delta >=k+1`.

Indeed, for `delta<=1` the lower bound is `b-k=k+1`; for `delta=2`, it is `b+k-2k=k+1`. At the first prefix (`j=1`, `s=0`, `delta=1`) equality holds. Hence `U=k+1`. At the upper endpoint `1/2`, the upper-cut expression is `2s-j=s-z=-delta<=0`, attaining zero at the empty prefix, so `V=0`. Substitute these four common quantities into R146's integer formula. QED.

## R155.2 — Exact absence set, not merely an asymptotic result

Write `b=2k+1`. Direct integer algebra gives, for `t>=0` and `L>=1`,

- **Odd** `L=2t+1`: `C(L+1)=ceil((t+1)/b)>=1`.
- **Even** `L=2t` with `t>=1`: `C(L+1)=ceil((t+k+1)/b)-1`.

The even case vanishes exactly when `1<=t<=k`. Hence the complete absence set is

`{ L>=1 : C(L+1)=0 } = {2,4,6,...,2k}`.

Equivalently, the words are absent precisely at odd coefficients `K=3,5,...,2k+1`, and their exact permanent-appearance threshold is

`T_{A_k}=T_{B_k}=2k+2`.

For `k=1`, the pair is `01001010` and `01010010`, with common signature `(1/3,1/2,2,0)`, and its only missing coefficient is `K=3`. This provides an explicit full-time alias family together with exact arithmetic holes, beyond R154B's one-1 family. The full-language conjectural threshold `T(m)` is not resolved by this subfamily.

## R155.3 — Exact finite landscape (exploration only)

`R155_check.py` independently constructs the reduced rational endpoints and cuts of **every** binary word of length `1..14`, rejecting words with `alpha>=beta`. Among the resulting admissible words, no signature `(alpha,beta,U,V)` has more than two words in this *finite* domain. For example, at `m=14` there are 346 admissible words, 320 distinct signatures, 26 doubletons and 294 singleton signatures. This is a finite classification check, not a universal multiplicity theorem.

The same script checks the above infinite-family theorem at all `k=1..100` (`m=8..404`), 10,816 exact large-integer count values, and 10,400 additional exact absence-window checks. It writes `R155_verification.json`. The script uses integer cross-products for supports, Python `Fraction` for reduced endpoints, arbitrary-precision integers for counts, and no floating-point calculations. Exact execution result: `R155_MULTI_ONE_ALIAS_EXACT_PASS`. Mathematical generality of R155.1 and R155.2 derives from the preceding proofs, not the finite test.

## Next discriminating question

Classify the complete fibers of `w -> (alpha,beta,U,V)` for arbitrary multiple-one factors: are all actual fiber classes of size at most two, or can a triple alias be constructed? Determine minimal extra word/provenance data needed to distinguish such aliases under the declared future observer. Separately, apply R152B's exact first-period certificate to candidate factors controlling the **global** saturation threshold, retaining each word's absolute cuts. Keep Source owner/CLAIM, author-side publication, independent review and native-X6 correspondence distinct.
