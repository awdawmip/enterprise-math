# R762KO — Odd uniform Port–Euler fiber maxima by exact Bernstein certificates

**Scope:** author-derived exact finite/symbolic theorem in the **unsigned auxiliary three-inactive-Port composite Port–Euler observer**, not a signed native `TRIADIC_CLOSURE_E` theorem. **Status:** AUTHOR_EXACT_CERTIFICATE_CHECKED / NOT_REVIEWED. This is a continuation of R762KN (not an independent new model).

## Fixed input and provenance

- Frozen predecessor: `awdawmip/enterprise-math@2ca3fe1ff671a44a1ec4ed4cb90653870a7ddaf7:research_notes/portable_direct/R762KN_M3_ARBITRARY_MULTIPLICITY_FIBER_THEOREM.md`. Reuses KN.1's local multiset weights and KN.4's even-m proof, without repinning the scientific model.
- Global P000 and current ACTIVE worldview were consulted as research premises. This statement is about a declared auxiliary unsigned observation map only. Its boundary characters are **not** signed physical forces or positive BRC branch masses.
- Three inactive Ports: `01,23,45`. Twelve active Ports `G=(F_2)^12`, with basis vectors `[ab]` for active unordered pairs. Eight flexible supports are `(i,2+j,4+k)` for `i,j,k ∈ {0,1}`; their three legal edge boundaries are `e_(ijk,1)=[i,2+j] + [i,4+k]`, `e_(ijk,2)=[i,2+j]+[2+j,4+k]`, `e_(ijk,3)=[i,4+k]+[2+j,4+k]`. Every triple XOR is zero.
- Twelve forced supports each have a fixed 2-edge boundary. Their GF(2) span `F` has exactly `2^9=512` elements. Event choices at each flexible support are counted as **unordered edge multisets**, not time-ordered words.

## Theorem KO.1 — the odd uniform-multiplicity question is closed

Let each of the eight flexible supports have the same positive integer multiplicity `m`. Let `Q_m(b)` count connected legal flexible edge-multiset assignments with the forced support boundary `b ∈ F`, as in R762KN. Then, for every integer `m ≥ 2`, the **unique** maximizer is the zero boundary:

```text
Q_m(0) > Q_m(b)       for every nonzero b ∈ F.
```

The even case is KN.4. For each odd `m=2r+1 ≥3` (`r≥1`) the new, explicit (not claimed sharp) bound is

```text
Q_m(0)-Q_m(b) >= ((r+1)^8 * (r+2)^6)/64 - 3 > 0.       (1)
```

The `m=1` exclusion is necessary: `Q_1(0)=6` while the maximum is `8`, attained at nonzero boundaries.

### Proof

At one flexible support, exactly `A_m` unordered multisets have zero GF(2) boundary and exactly `B_m` have each of its three nonzero triangle-edge boundaries (KN.1). At odd `m=2r+1`, `A_m=r(r+1)/2`, `B_m=(r+1)(r+2)/2`, so

```text
t=A_m/B_m = r/(r+2),     1/3 <= t < 1.
```

In the integral group algebra `Z[t][G]`, set

```text
P(t) = product_(i,j,k in {0,1}) [t + X^(e_ijk,1) + X^(e_ijk,2) + X^(e_ijk,3)],
p_b(t)=[X^b]P(t).
```

The exact computational lemma below certifies, **for all 511** nonzero `b∈F`,

```text
p_0(t)-p_b(t) = (1-t)^2 R_b(t),
R_b(t)=sum_(j=0)^6 beta_(b,j) * binom(6,j)*t^j*(1-t)^(6-j),
beta_(b,j) >= 1.                                         (2)
```

The basis weights are nonnegative and sum to 1 for `0<=t<=1`, so `R_b(t)>=1`. This is a finite integer-polynomial identity, **not** numerical sampling in the free parameter `t` and not extrapolation in `m`.

For a uniform `m`, all three monochromatic disconnected choices have XOR boundary zero: in each edge type each active Port appears an even number of times across the eight cube vertices. They are the only disconnected choices in the predecessor's three-component observer. Thus

```text
Q_m(0)-Q_m(b) = B_m^8 * (p_0(t)-p_b(t)) - 3
              >= B_m^8*(1-t)^2 -3
              = (r+1)^8*(r+2)^6/64 -3.
```

This is positive for `r>=1` (already `2913` at `r=1`, then increasing). The prior KN.4 covers even `m>=2`. QED, within the declared model.

### Exact finite polynomial lemma and replay

The companion pure-Python verifier constructs `G`, all forced boundaries and `P(t)` directly from the six axis labels, without importing a table of expected boundary outputs. It runs the exact `Z[t][G]` convolution for eight supports, subtracts coefficient vectors for `b=0` and all `511` nonzero `b∈F`, divides by `(1-t)^2` by exact coefficient recurrence, and checks full reconstruction of degree-eight polynomials.

The `511` coefficients reduce to **18 distinct degree-at-most-six `R_b` polynomials**. For each, the checker converts to the exact degree-six Bernstein basis by

```text
beta_j = sum_(i=0)^j a_i * binom(j,i)/binom(6,i),   R(t)=sum_i a_i*t^i.
```

All 18×7 Bernstein coefficients are at least 1 (minimum is **1**). The evidence JSON supplies every representative, multiplicity, monomial coefficients and exact Bernstein coefficients; the checker recomputes the classes and positivity rather than trusting their printed values. The code then independently computes numerical integer fibers for `m=3,5,7,9,11`, checking the stated bound. All assertions were locally executed and passed.

| Odd m | Q_m(0) | largest Q_m(b≠0) | exact gap | bound (1) |
|---:|---:|---:|---:|---:|
| 3 | 71,197 | 64,800 | 6,397 | 2,913 |
| 5 | 22,471,422 | 21,257,640 | 1,213,782 | 419,901 |
| 7 | 1,555,439,613 | 1,504,051,200 | 51,388,413 | 15,999,997 |
| 9 | 44,428,515,622 | 43,417,968,750 | 1,010,546,872 | 284,765,622 |
| 11 | 710,800,264,221 | 698,860,503,936 | 11,939,760,285 | 3,087,580,353 |

These five rows are secondary regression checks; the parameter-uniform proof is (2), not finite data.

## Limits, significance, next discriminating unit

This closes the **odd-m uniform maximum** question stated at the end of KN, and consequently all integer uniform `m>=2`, while preserving the `m=1` counterexample. It establishes an exact necessary residual-bits reference for the largest auxiliary provenance fiber. It does **not** determine exact maximal fiber formula for every `m`, temporal composition of residual states, a native signed Cell/Link/Port dynamics lift, or any independent review.

Next useful questions: derive a structural nonenumerative proof of the 18 Bernstein-positive types, or construct an explicit minimal lossless composable provenance coordinate whose decoding respects ordered BRC inputs; identify a concrete native signed typed observation and test whether this unsigned fiber distinction survives. Preserve the parent P000 and task pins; do not promote to native theorem or formally accepted Result on this evidence alone.
