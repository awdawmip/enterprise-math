# OAI7 r327 — Pairwise-distinct common shifts without extra entropy or loss of second-order scale

Date: 2026-11-18. Source-exposed, author-side mathematical derivation, preserved independently in GitHub; not Native Result admission, independent Driver review, CLAIM, or native X6 implementation. This uses r326's quantitative second-order schedule and preserves the original OAI7 researcher and earlier authors' provenance.

## Theorem: a collision-repaired shared polynomial schedule

Use the external finite-cyclic model and exact parameter definitions of r326: prime `p`, `u=ceil(sqrt(p))`, `b=17/64`, `J=1-b+b log b`, `c_*=1/(4J)`, and `n=ceil(c_* sqrt(p) [log p-2 log log p+w(p)])`, where `w(p)->infinity` and `w(p)=o(log log p)`. Put `rho=u/p`, `mu=n rho`, `a_b=b+1/W_0(e^(-1))`, `t=2 ceil(a_b mu/2)`, `s=k=4096t+1`. Let `v_l=P(l)` for a polynomial `P` with `t` independent uniform coefficients over `F_p`, evaluated at `0<=l<n`; `t<=n<p` for large primes.

There exists a **deterministic, translation-equivariant, seed-preserving repair** `R:F_p^n -> F_p^n` such that the repaired sequence `v'_0,...,v'_(n-1)=R(v_0,...,v_(n-1))` has all entries pairwise distinct, each `v'_l` is individually uniform over `F_p`, and the shared integer lattice vectors `h'_l=([v'_l]_p,...,[v'_l]_p)` have all the same full-lattice terminal law after addition to the independent initial `Y` of r326. Its shared schedule entropy satisfies

```text
H(H') <= t log p = O((log p)^2).
```

The r307 worst-fixed-set small-list probability of **every** signed coordinate satisfies

```text
q'_c <= q_c + p^(1/4) * binom(n,2) * u/p^2
     <= [C_b/sqrt(c_*)+o(1)] exp[-w(p)/4]
        + O(p^(-1/4) (log p)^2)
     -> 0,
```

where `q_c` is the original r326 polynomial schedule tail and `C_b=1/[(1-b)sqrt(pi b)]+2/sqrt(2pi a_b)`. Thus the **pairwise-distinct-shift** class also admits the second-order `-2 c_* sqrt(p) log log p + o(sqrt(p) log log p)` sample saving while retaining all r307 information, marginal-law, and fixed-test-set quantifier conditions.

## Deterministic repair and uniform terminal laws

Given an arbitrary `v=(v_0,...,v_(n-1))` with `n<p`, let `D` be the set of its original distinct values. Keep `v_l` unchanged at the *first occurrence* of each value. At each subsequent occurrence, in increasing order of `l`, assign the next unused element of the cyclic scan

```text
v_0, v_0+1, ..., v_0+(p-1)    (mod p)
```

that lies outside the **entire original set** `D` and has not been assigned to another duplicate position. There are `p-|D| >= n-|D|` candidates, so repair always succeeds. Reserving the original `D` before replacement is essential: it prevents an earlier replacement from displacing a later first occurrence. All outputs are pairwise distinct.

For every `a in F_p`, the construction obeys `R(v+a)=R(v)+a` coordinatewise, because first-occurrence equalities, original-set exclusion, and the cyclic order relative to `v_0` commute with common translation. Conditional on the polynomial's nonconstant coefficients, its constant coefficient `U_0` is uniform, and adding `a` to `U_0` translates all `v_l` by `a`. Equivariance therefore makes every `v'_l` uniform on `F_p`, though the repaired vector is correlated. The deterministic integer representative of each `v'_l` has the same law; independence from `Y` gives identical full-lattice `Y+h'_l` laws for all `l`. As `H'` is a deterministic function of the original `t` coefficients, `H(H')<=t log p`.

## Tail comparison under pairwise-independent original evaluations

Fix one sign coordinate `c`, a deterministic `u`-set `K` chosen independently of the random polynomial, and a start `x in F_p`. Write

```text
X_x  = # {l : x + phi_c(h_l)  in K},
X'_x = # {l : x + phi_c(h'_l) in K}.
```

Only positions with a repeated **original** value are changed. If no repeated original value belongs to the signed preimage `K_(c,x)={v: x +/- v in K}`, all deleted hits were zero; replacement can only add hits, so `X'_x>=X_x`. The exceptional event is contained in the union over `l<m` of

```text
{v_l=v_m and v_l in K_(c,x)}.
```

Because `t>=2`, each pair `(P(l),P(m))` is independent uniform over `F_p^2`. The probability of one such event is exactly `u/p^2`; hence

```text
Pr(X'_x<=b mu)
  <= Pr(X_x<=b mu) + binom(n,2) u/p^2.
```

Sum over the `p` starting residues `x`, apply Markov to the list-cardinality threshold `p^(3/4)`, then maximize over deterministic `K` **outside** the random-schedule probability. This gives the claimed `q'_c` inequality for each of the `2k` signed coordinates. Since `n=O(sqrt(p) log p)` and `u=O(sqrt(p))`, the collision correction is `O(p^(-1/4)(log p)^2)`.

The r307 entropy deficit of the independent initial coordinates and its exact `s=k` base-index sign sampling are unchanged. Replacing `H` by the deterministic image `H'` can only lower its entropy cost. All r307 assumptions hold eventually; no post-sampling choice of `K` is introduced.

## Contribution boundaries and next discriminating question

This note is the first pairwise-distinct-offset repair of the r326 second-order bound. It does not claim that the corrected vector is itself `t`-wise independent, and it does not use any such false premise: its error is controlled by the original `t`-wise polynomial sequence plus a pairwise collision union bound.

Pins: r307 `baaaabaacaf8543f62a45a00cdfcf03e95389075`; r321 lower leading coefficient `3c411d17ca496dfcfcdb91082643597981f6b9d2`; r325 Lambert-W bound `6634ecc793d149a55c88ceb6a9780a2f3ec5eac3`; r326 second-order bound `4d94923811a8b47a01f584f337fd5028bd23b40d`. The next mathematical question is whether the coefficient `2` of `log log p` is also a necessary second-order threshold in the pairwise-distinct class. The formal OAI7 Task/Result and native X6/Port/Link transfer retain their separate scope.
