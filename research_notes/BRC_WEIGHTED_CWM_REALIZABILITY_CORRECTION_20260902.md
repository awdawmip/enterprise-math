# BRC Weighted CWM — Positive-Path Realizability Correction — 2026-09-02

Status: `CORRECTION / EXACT FINITE POSITIVE-PATH REALIZABILITY`

Researcher-ID: `EM-BRCWLOG-6F42A1`  
Corrects terminology in: `research_notes/BRC_WEIGHTED_CWM_SAFE_QUOTIENT_20260902.md`

## 0. Correction

The prior CWM safe-quotient note defined the closed set

```text
H = {(0,0,0)} union {(c,w,m): c>=1 and 0<m<=w<=c*m}
```

and described it as a path-coherent carrier.

The algebraic theorem proved there is correct: `H` is closed under the CWM semiring operations.

However, `H` is **strictly larger** than the exact set of triples realized by a finite family of `c` strictly positive rational path masses. The phrase “path-coherent” is therefore too strong if read as an exact realizability characterization.

The corrected terminology is:

> `H` is the **closed algebraic CWM envelope**.

The exact positive-path realizability locus is the smaller set `R` characterized below.

## 1. Exact realizability theorem

Let `c` be the number of supported paths, let positive rational path masses be

```text
w_1,...,w_c > 0,
```

and define

```text
W = sum_i w_i,
M = max_i w_i.
```

Then the realizable triples `(c,W,M)` are exactly:

```text
R = {(0,0,0)}
    union {(1,w,w): w>0}
    union {(c,w,m): c>=2 and 0<m<w<=c*m}.
```

### Necessity

For `c=0` there is no supported path, so both mass coordinates are zero.

For `c=1`, the unique positive path is simultaneously the total and the maximum:

```text
W=M>0.
```

For `c>=2`, at least two positive summands occur. One summand equals `M` and at least one further summand is positive, so

```text
W>M>0.
```

Every one of the `c` summands is at most `M`, so

```text
W<=c*M.
```

### Sufficiency

Take any rational triple with

```text
c>=2,
0<m<w<=c*m.
```

Set one path mass to `m`. Let

```text
r=w-m.
```

Then

```text
0<r<=(c-1)m.
```

Assign each of the remaining `c-1` paths the positive rational mass

```text
r/(c-1).
```

Every such mass is at most `m`, the total is exactly `w`, and the maximum remains `m`.

Thus every triple satisfying the stated conditions is realized by positive rational path masses.

**Status:** `PROVED`.

## 2. Strict difference between H and R

Example:

```text
(c,w,m)=(2,1,1).
```

It lies in `H` because

```text
0<1<=1<=2.
```

But it is not realizable by two positive path masses: if one path has maximum mass `1`, the second positive path makes the total strictly greater than `1`.

Therefore

```text
R subsetneq H.
```

## 3. Closure of the exact realizability locus

`R` is itself closed under the CWM semiring operations.

### Recoalescence

If two nonzero realizable path families are merged, their path counts add and their path-mass multisets form a disjoint union. Hence the result is automatically another positive finite path family.

Algebraically, the new count is at least `2` and

```text
W_1+W_2 > max(M_1,M_2).
```

The upper sandwich bound is inherited exactly as in the parent note.

### Path-product composition

The product of two positive finite path families is the Cartesian-product family of pairwise path concatenations. Its size is `c_1*c_2`; every product mass is positive; total mass is `W_1*W_2`; maximum is `M_1*M_2`.

Hence CWM multiplication also stays in `R`.

So both the broader algebraic envelope `H` and the exact positive-path locus `R` are closed, but they answer different questions.

## 4. Consequences for effective multiplicity

On the exact positive-path locus:

```text
E=W/M.
```

Then

```text
c=1  iff E=1 iff Delta=ln(E)=0,
```

while for every `c>=2`,

```text
1<E<=c,
0<Delta<=ln(c).
```

This sharp strict inequality is valid because all supported path masses are strictly positive.

The broader envelope `H` only guarantees the weak inequalities because it contains algebraic triples that are not path-realizable.

## 5. Scope impact

This correction does **not** change:

- the CWM product-semiring laws;
- finite-DAG CWM path evaluation;
- Boolean support projection;
- the all-prefix future-signature safe quotient theorem;
- the local-bisimulation counterexample;
- the previous exact path-family multiplicity bounds.

It only separates:

```text
closed algebraic carrier H
```

from

```text
exact positive-path realizability locus R.
```

Future implementation should use `R` when a trace claims literal finite positive-path realizability and may use `H` when only algebraic closure is required.
