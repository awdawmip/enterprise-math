# R155 — Reversal aliases, exact cuts, and an infinite three-one family

Date: 2026-11-15 (Asia/Shanghai). Status: **author-side proof**, finite exact regression, independent review **NOT_REVIEWED**. Scientific pin unchanged: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Scope: **external scalar tied-phase S23 finite mechanical-word observer**. No native X6 identification or new P000 axiom.

Sources: R146 (exact cut/fiber law) at `b02b0c242b274bc6a82111dbd3600126a2867319`, R153 (unequal-denominator increment injection) at `e6e436cb90f6c943b3825a4a2fe26b0500c558f8`, R154/R154B (equal-denominator and one-defect classifications) at `e446e8844513be49f214206e0f16d6d740154260`.

## Definitions

For a binary word `w=w_0...w_{m-1}`, let `s_j=∑_{i<j}w_i`, `n=s_m`. Its admissible open slope support is `(α,β)`, with `α=a/b<β=c/d` in lowest terms (including `0/1,1/1`). Put

- `X_j=s_j-jα`, `Y_j=s_j-jβ` for `0≤j≤m`;
- `U=b(1+min X_j)`, `V=d max Y_j`;
- `C_w(L+1)=ceil((Lc−V)/d)−floor((La−U)/b)−1` for integer `L≥1`.

These are R146's exact integer cuts and count, with each integer phase index counted once.

## R155.1 — Exact reversal-cut equations

Let `w^R` be the word in reverse order. Its support is also `(α,β)`, because reversal preserves every contiguous subword's length and number of ones. Its prefix sums are `s^R_j=n−s_{m-j}`. Direct substitution gives

```text
U(w^R)/b = 1+n−mα−max_j X_j,
V(w^R)/d =   n−mβ−min_j Y_j.
```

Consequently, **for every admissible word**, `(U,V)(w^R)=(U,V)(w)` if and only if

```text
min_j X_j + max_j X_j = n−mα,    (A)
min_j Y_j + max_j Y_j = n−mβ.    (B)
```

This is a direct finite-prefix test using exact rational arithmetic. If (A),(B) hold, R146 gives `C_{w^R}(K)=C_w(K)` for every `K≥2`.

Conversely, if **b≠d**, equality of all the counts forces (A),(B). Indeed, equal counts imply equal complete period increment waveforms. R153.1 proves injection of the two cut residues for distinct *interior* endpoint denominators. The same argument covers endpoint `α=0` or `β=1`: that endpoint has denominator 1 and its genuine cut is fixed, respectively `U=1` or `V=0`; the other nontrivial increment pulse has a distinct waveform for each cut residue. For genuine words, `0<U≤b` and `0≤V<d`, because the strict support inequalities give `0<u_α≤1` and `0≤ℓ_β<1`. Thus each residue identifies its normalized cut uniquely, and equal waves imply exactly equal U,V, proving (A),(B). 

For `b=d`, the actual equal-denominator finite factors are the alternating words classified by R154, and the two phases can have equal complete count sequences with unequal cuts (R153.3). In that case the implication “equal counts ⇒ (A),(B)” is intentionally not asserted.

## R155.2 — Infinite aliases with three 1s

For every integer `h≥2`, define two *distinct* length-`2h+2` words

```text
A_h = 1 0^(h−1) 1 0^h 1,
B_h = 1 0^h 1 0^(h−1) 1 = reverse(A_h).
```

Both are admissible and have exactly the same genuine slope support and absolute cuts:

```text
α = 1/(h+1),   β = 1/h,
U = h+1,       V = h−1.
```

**Support proof.** Any subword with two 1s has length at least h+1, and the full word with three 1s has length 2h+2. All lower-factor ratios `(ones−1)/length` are therefore ≤1/(h+1), while the full word attains equality. For upper bounds, zero runs have length at most h; a subword with exactly one 1 has length at most 2h; any two-one subword has length at most 2h+1; the three-one subword has length 2h+2. Thus all `(ones+1)/length` are ≥1/h for h≥2, and a zero run of length h attains equality. Hence the displayed support.

**Cut proof.** With `α=1/(h+1)`, each prefix satisfies `(h+1)(s_j+1)−j≥h+1`, with equality at `j=0`, so `U=h+1`. At `β=1/h`, `hs_j−j≤h−1` for every prefix and equality holds immediately after the first 1, so `V=h−1`. The position of the middle 1 does not change either extremum.

R146 now yields the identical exact all-coefficient count

```text
C_{A_h}(L+1)=C_{B_h}(L+1)
 = ceil((L−h+1)/h) − floor((L−h−1)/(h+1)) − 1.
```

The two cut denominators are distinct, `b=h+1` and `d=h`. In particular, this gives infinitely many multi-one, distinct-denominator **word identity aliases**. Bitwise complement gives the corresponding family with three 0s.

## R155.3 — Exact permanent-presence threshold for this family

The open integer phase interval from R146 is

```text
I_L = ((L−h−1)/(h+1), (L−h+1)/h).
```

Its length is `|I_L|=(L+h+1)/(h(h+1))`. At `L=h²−1` its endpoints are the consecutive integers `h−2` and `h−1`: there is **no** interior integer, hence `C(h²)=0` (here the count argument is K=L+1).

For every `L≥h²`, `|I_L|>1`, so every such open interval contains an integer and `C(L+1)≥1`. Therefore the **exact permanent-appearance threshold** for both words is

```text
T_{A_h}=T_{B_h}=h²+1.
```

At length `m=2h+2`, the still-unresolved proposed global threshold is `(m−2)floor((m−1)/2)+1=2h²+1`. The present infinite family contributes a strict, explicit `h²+1` subfamily threshold and does not settle the global maximum.

## Exact finite validation

Companion `R155_check.py` uses Python arbitrary-precision integers and `fractions.Fraction` and checks:
- all 860 admissible words at lengths 1..12 for the two reversal-cut equations, exact reversed cuts, and one full affine period of count equality; 846 words have distinct endpoint denominators;
- `h=2..60` (59 pairs) for exact endpoints and cuts, 472 very-large-integer count comparisons, 1,888 post-threshold positive-count checks;
- equal-cut alias groups among all words at lengths 1..12: 72 pair-collisions in that finite range.

All assertions passed. Finite checks corroborate the implementation; the three all-h statements above are proved symbolically. Verification marker: `R155_REVERSAL_AND_THREE_ONE_FAMILY_EXACT_PASS`, record `R155_verification.json`.

## Next question

Classify non-reversal aliases and the maximal fibers of `w→(α,β,U,V)` in the entire finite Sturmian language, or establish a general sharp upper bound on the last zero `C_w(K)=0` from the exact cut coordinates. Reuse R152B's finite-period certificate and compare with the proposed `T(m)` formula. Preserve the frozen S23 pin and existing P000/native observer typing. Formal CLAIM: none; independent review: NOT_REVIEWED.
