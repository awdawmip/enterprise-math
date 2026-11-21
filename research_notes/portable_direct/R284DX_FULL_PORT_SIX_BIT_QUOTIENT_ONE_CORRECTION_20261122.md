# R284DX — Frozen full Port universe: six-core-bit quotient stratification with one exceptional threshold

Date: 2026-11-22 (Asia/Shanghai)  
Scientific status: `AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED`  
Scope: frozen auxiliary Port model, **not** a native-X6 dynamics or physical transfer theorem.

## Frozen definitions

The unchanged source is `awdawmip/enterprise-math@acba2d8667903434aaa2a10720f43637fcc2421b:research_notes/portable_direct/R284CO_spectral_witness_checker.py`, blob `b46e0f682b58e47c27094b4bea6fa4e55119a3ee`. Its 65,536 Port codewords have SHA-256 `b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4`. The modulus is `P=17179869143`. The 12 lower inputs in order are `(u1,a,x,y,u2,w,b,z,u3,g,h,r) ∈ {1,2}^12`; the upper mask ranges over `0..15`. Let `T(L,top)` be the **unreduced** integer determinant from R284CO and `z=T mod P` its circular Port coordinate.

Select the six lower bits

`k=(u1−1)+2(a−1)+4(x−1)+8(u2−1)+16(w−1)+32(b−1)`, `0≤k≤63`.

Let `Q[k]` be the following 64 exact integers, in ascending `k` order (rows are `k=0..15`, `16..31`, `32..47`, `48..63`):

```
5640 5152 4385 3898 5495 5007 4240 3752 5413 4925 4196 3708 5230 4742 4014 3526
5494 4969 4240 3714 5242 4716 3987 3461 5267 4742 4051 3525 4977 4451 3760 3234
5139 4689 3992 3542 4994 4543 3847 3396 4912 4462 3803 3352 4729 4279 3620 3170
4993 4505 3846 3358 4740 4252 3593 3105 4766 4278 3657 3169 4476 3988 3367 2879
```

## Theorem — full-universe exact quotient without integer division

For **each** of the 65,536 frozen source states, define

`e(L,top) = 1` if `k=63` and `T < 2879P`, and `0` otherwise. Then

\[
\boxed{\left\lfloor T/P\right\rfloor=Q[k]-e(L,top),\quad z=T-(Q[k]-e(L,top))P\in[0,P).}
\]

In 63 of the 64 six-bit core classes, the entire 1,024-state fiber has **exactly the same integer quotient** `Q[k]`, regardless of the other six lower variables and all four upper bits. The only exceptional class is `k=63` (`u1=a=x=u2=w=b=2`): precisely **446/1,024** states have quotient 2878 and the remaining **578/1,024** have quotient 2879. Thus **one threshold bit is necessary and sufficient** to repair the selected six-core-bit quotient representation. This is a statement about this chosen representation, not an absolute state-encoding optimum. The fourth upper mask bit (weight 8) never changes the quotient, across the entire frozen population.

The formula recovers the exact original Port residue using 64 precomputed integers, a six-bit index, an exceptional-case comparison and integer multiplication/subtraction. It removes general division/remainder from **the quotient/residue reduction stage**, not from the original determinant construction or the independent arc-distance reference checker.

## Finite exhaustive proof and scope

The companion Python program reproduces the original pinned `det` and all 64 labeled arcs. It enumerates all 16 upper masks and all `2^12` lower assignments in the original R284CO order, asserts the pinned SHA-256 of the original residues, computes `T` exactly, and independently compares the claimed `Q[k]-e` against `T//P` and the constructed residue against `T%P` for **every** state. It also obtains, from the same finite exhaustive domain, the exact per-fiber `min(T),max(T)` and quotient counts. For every `k<63`, the verified inequalities are `Q[k]P≤min T≤max T<(Q[k]+1)P`; at `k=63`, they are `2878P≤min T<2879P≤max T<2880P`. The 446/578 split is then checked by a strict integer comparison at the exact threshold `2879P=49,460,843,262,697`. Each fiber has exactly 1,024 configurations; no sampled cases or floating-point tolerances enter the proof.

For an additional independent-observer consistency check, each generated reduced residue is compared with **all 64 original labeled circular arcs**, giving 4,194,304 exact point–arc evaluations. The ordered `(residue,winner-label,max-distance)` checksum is `4d15e6ffb1fa38e92f105fa54e5b7c8061301fadcb761ebc4feeb1c57b2a1cc8`. All 65,536 states have unique farthest-arc labels in this computation. These calculations certify the fixed **finite frozen** statement; they do not imply an asymptotic bound, a faster end-to-end runtime, or an independent reviewer pass.

## Relation to earlier research and next questions

R284DW established a four-case division-free quotient for a 4,096-state subcube. The current theorem extends exact quotient reduction to the **full 65,536-state population** while retaining the original data and operation semantics. For the R284DW restrictions `u1=u2=1,a=b=2`, the present 64-entry table reduces exactly to its four values `3992,3847,3846,3593` for `(X,W)=(0,0),(1,0),(0,1),(1,1)`; no exceptional threshold applies. R284DS already supplies an exact labeled event-envelope observer; integrating that existing observer with the new reduction is a separate implementation/benchmark task.

Next, seek a smaller arithmetic circuit generating the 64 `Q[k]` values, and derive a compact threshold predicate for the 446 exceptional configurations that avoids re-evaluating all determinant terms. Compare full costs of determinant evaluation, table preparation, bit/precision representation, envelope preprocessing, observer queries, and recovery against original `% P` and direct 64-arc baselines. Preserve all state/branch information needed by subsequent operations; a quotient coincidence does not identify full states or license arbitrary future-observer compression.

## Reproducibility

Run `python R284DX_six_bit_full_quotient_checker.py`; it uses only the Python standard library and creates `R284DX_six_bit_full_quotient_certificate.json`. The script was executed locally with exact integers. The project artifact is an author calculation/proof, with independent mathematical review still `NOT_REVIEWED`. Researcher/Activity identity and formal Task/CLAIM/Result association are separate control records and are not asserted by this scientific file.
