# EC49FAM — Exact key lifespans and native-prefix decoder for the frozen H9 X6 BRC model

**Date:** 2026-11-04. **Status:** AUTHOR_ANALYTIC_THEOREM / EXACT_FINITE_CHECK / PORTABLE_DRAFT / NOT_ADMITTED.

## Source and exact claim scope

Continue EC49FAL at immutable author checkpoint `42aa297b47b7742f99b3ae1b35371b786832f7e5`; scientific input remains frozen at `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Applicable behavioral rules are read from current normative context; P000 and ACTIVE worldview are unchanged. The mother target is the H2–H9 signed-six-axis seven-operation BRC optimization with one full positive cache key per horizon, at most six nine-history observation signatures, rational rank nine, and five cache keys. Its author-side bounds remain `80 <= E_H9* <= 94`.

The **full signed native primitive operation code** is `a=(-1,-1), b=(-2,-2), c=(1,2,-1,-2), d=(2,1,-2,-1), e=(3,1,1,-3), f=(1,-1), g=(2,-2)`; signed integers mean signed axis labels, not coordinates in a lower-dimensional ambient space. A word is displacement-valid when the sum of its signed X6 primitives is `(2,0,0,0,0,0)`. Its **full positive BRC key** is the vector of positive occurrences of each of the six axes, with operation order and signed steps preserved separately as native path data.

## Theorem 1 — exact feasible key set and interval lifespan

For any displacement-valid operation word of length `h`, define `z=n_e`, `r=n_c+n_d`, `f=n_f`, `g=n_g`. Then `n_b=0` and `n_a=z-1`; hence `z>=1` and

```text
h = 2*z - 1 + r + f + g
K = (x,y,z,0,0,0)
x = 2*z + r + f
y = r + g.
```

Conversely every quadruple of integers `z>=1`, `r,f,g>=0` satisfying the length equation has a displacement-valid ordered realization (choose `z` e's, `z-1` a's, `r` c's, `f` f's and `g` g's). No condition on the **nine-history observer** or rank is used in this algebraic key census; these must be checked when forming an actual optimization witness.

For an integer triple `(x,y,z)` with `z>=1`, its key is feasible at **exactly** the integer horizons in the interval

```text
max(x-1, y+2*z-1) <= h <= x+y-1.
```

Proof: the inverse operation counts are `r=x+y-h-1`, `f=h+1-y-2z`, `g=h+1-x`; these are all nonnegative exactly on that interval. In particular a key feasible at `h` remains algebraically feasible at `h+t` precisely when `r_h>=t` (for integer `t>=0`). This statement keeps the full positive X6 key, rather than substituting a shorter cache hash.

Writing `K_h` for the set of feasible full keys at horizon `h`, put `n=h+1-2z` and `C(q,2)=q(q-1)/2` for `q>=2` (zero otherwise). The exact counts are

```text
|K_h| = sum_(z=1)^floor((h+1)/2) C(h+3-2*z,2).
|K_h ∩ K_(h+t)| =
    sum_(z=1)^floor((h+1-t)/2) C(h+3-2*z-t,2), t>=0.
|K_(2m)| = m(m+1)(4m+5)/6.
|K_(2m+1)| = (m+1)(m+2)(4m+3)/6.
```

Proof: for fixed `z`, `r+f+g=n` has `C(n+2,2)` solutions, with an injective map to `K_h` through the inverse formulas. Joint feasibility at `h` and `h+t` requires `r>=t`; replacing `r` by `r-t` counts `C(n-t+2,2)` choices. The parity formulas are elementary sums of quadratic polynomials.

**Exact H9 search consequences:** `|K_8|=70`, `|K_9|=95`, `|K_8∩K_9|=50`, `|K_8∩K_10|=34`. This extends the EC49FAJ one-step key census to arbitrary horizon gaps, with an interval/lifespan predicate for pruning future native-path search.

## Theorem 2 — native signed-prefix decoder and local equal-key replacement

All seven operation codes are distinguished by their first **two** signed native primitive directions. The only distinct operation pairs with one identical leading native primitive are `{c,f}` and `{d,g}`. If two operation words `u,v` have maximal shared operation-word prefix `p`, and neither ends after `p`, then their exact native **primitive-step longest common-prefix length** is

```text
LCP_native(u,v) = primitive_length(p) + delta,
delta = 1 if their first different operations form {c,f} or {d,g},
        0 otherwise.
```

If one operation-word is a prefix of the other, the native longest common prefix is the full primitive length of the shorter word. Proof: the seven first-two-direction pairs are distinct; all operation codes have at least two primitive directions. Thus after the first differing operations native agreement lasts at most one step. The decoder does not erase branch order or signed six-axis steps.

Furthermore, **two distinct displacement-valid words with the same full positive BRC key cannot be related by strict operation-word prefix.** Any nonempty appended suffix preserving the positive key could use only `a,b`, the sole operations having no positive primitive occurrence. Their signed net displacement is strictly negative on at least one native axis, contradicting equal target displacement.

Finally, suppose `u=pU`, `v=pVW` have lengths `h`, `h+1`, share `h-1` initial operations, both have target displacement and equal full key. Then precisely the following suffix replacements are possible:

```text
c -> fg,  c -> gf,  d -> fg,  d -> gf.
```

Proof: eliminate the common operation prefix and compare complete six-coordinate positive counts and signed net displacement of the one-letter and two-letter suffixes. The seven-versus-49 finite table gives exactly these four equalities (verified independently by the checker). The matching native suffix LCP equals one step for `c/fg` or `d/gf`, zero for `c/gf` or `d/fg`. Hence a single final-operation replacement can share at most one extra native primitive edge beyond the complete shared operation prefix.

## Executed verification and reproducibility

`node VERIFY_EC49FAM.js > EXACT_REPORT_EC49FAM.json` executes the full independent signed-X6 ordered-word census for horizons 2–7 (all `7^h` input words per `h`), checking displacement validity and every full positive key against the analytic construction. It checks 133 horizon-gap intersections for `2<=h<=20`, `0<=t<=6`; it directly compares native primitive-step LCP against the operation decoder on **160,000 ordered word pairs** (all operation words of length 0–3), and enumerates all 343 ordered one-to-two operation suffix comparisons.

**Actual execution result:** `PASS`. Direct key counts for horizons 2–7 are 3, 7, 13, 22, 34, 50; valid ordered-word counts are 8, 51, 304, 1770, 10224, 58947. Intersections at `h=8,t=0..6` are 70, 50, 34, 22, 13, 7, 3. The four one-to-two replacements are `c->fg, c->gf, d->fg, d->gf`. JSON in this directory records the exact executed counts and parameters.

**Inference:** theorems 1–2 hold for arbitrary finite operation-word lengths by the analytic proofs, and the finite tests audit the implemented formulas and parser. No claim is made about H9 rank-nine optimality from key feasibility alone. Native signed path order, full cache key, six-axis geometry and nine-history observer remain separately typed.

## Next unit EC49FAN — unrooted H8/H9 93-edge discrimination

For each of the four EC49FAL fixed H2–H7 schedules, remove the H6-root condition and permit independent H8/H9 native paths that branch at H5 or earlier. Apply Theorem 1 to narrow common fifth-key candidates and Theorem 2 to compute exact shared **signed primitive** prefix lengths without changing the observer or 9×5t rank test. Test whether a compatible pair of H8/H9 rank-nine word sets has total native-prefix cost <=93; either furnish a complete certificate (words, signed step key, observation signatures, rank, prefix set) or establish a rigorous lower bound for the specifically enumerated family. The global nine-window optimum remains open within `80 <= E* <= 94`.

**Role and authority:** author-side scientific draft on the existing GitHub PR, not a native CLAIM, Result or independent Driver review. Control authority must be verified separately and is not conferred by this Source commit.
