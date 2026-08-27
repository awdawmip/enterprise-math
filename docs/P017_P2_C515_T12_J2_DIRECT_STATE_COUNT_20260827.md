# P017 — c=103/20 T1–T2 j=2 Direct Square-Divisor State Bound

Status: `PROVED_WIP WHOLE j=2 RESIDUAL PENALTY < 0.00012 L23 / BYPASSES INNER ROSSER SIEVE / NOT CANONICAL / NO FINITE P2 CLAIM`

Date: `2026-08-27`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Companion checker:

`experiments/p017_p2_c515_t12_j2_direct_state_count_20260827.py`

Depends on:

- `docs/P017_P2_C515_T12_LEAST_SHELL_BUDGET_CORRECTION_20260827.md`;
- `docs/P017_P2_C515_T12_RESIDUAL_TRIPLE_VALUATION_LADDER_20260827.md`;
- the P(23)-anchored full-basin interval.

Purpose: close the complete corrected residual carrier with least-prime valuation `j=2` by direct physical-space counting. The previously isolated 254-state inner Rosser family is not needed for this valuation.

---

## 1. The j=2 residual carrier

After the corrected least-shell plus one-pair credit, every residual occurrence has a canonical least prime `r`, second distinct prime `q`, and later distinct prime `p>q`. On the valuation-two shell,

\[
\nu_r(n)=2,
\]

so every residual state is divisible by

\[
\boxed{r^2qp.}
\tag{J2-1}

The residual ordered-pair kernel obeys

\[
\kappa\le\frac{73}{80},
\]

and the source outside denominator is

\[
\Delta=\frac{93}{20}.
\]

---

## 2. A valuation-two state has at most seven residual later primes

All primes occurring in the residual triple satisfy

\[
r,q,p\ge z=D^{1/6}.
\]

Suppose a `j=2` state has `k` distinct primes after the second distinct prime `q`. Counting multiplicity, `r^2`, `q`, and those `k` later primes contribute at least

\[
z^{k+3}=D^{(k+3)/6}.
\]

Every state in the square basin is below

\[
W^2=D^{9/5}.
\]

Hence

\[
\frac{k+3}{6}<\frac95,
\]

or

\[
5(k+3)<54.
\]

Therefore

\[
\boxed{k\le7.}
\tag{J2-2}

Each later distinct prime gives at most one residual ordered-pair occurrence, so the residual multiplicity of any `j=2` state is at most seven.

---

## 3. The dangerous least-prime range is finite and small

The corrected pointwise theorem leaves only

\[
z\le r<D^{73/240}.
\]

At the Tier-A splice,

\[
z=W^{5/27},
\]

and exact integer comparison gives

\[
1439<z<1447.
\]

Also

\[
D^{73/240}=W^{73/216},
\]

with

\[
\boxed{585014<W^{73/216}<585015.}
\tag{J2-3}

Thus every dangerous least prime belongs to the finite set

\[
1447\le r\le585013.
\]

Exact prime enumeration gives

\[
\boxed{47735}
\tag{J2-4}

such primes.

---

## 4. Direct square-divisor incidence count

Let `J_23` be the P(23)-anchored interval of length

\[
L_{23}=232018561402828200.
\]

For each fixed prime `r`, the number of states of `J_23` divisible by `r^2` is at most

\[
\frac{L_{23}}{r^2}+1.
\]

Therefore, by (J2-2), the entire `j=2` residual penalty is bounded by

\[
|R_{j=2}|
\le
\frac1\Delta\frac{73}{80}\,7
\sum_{1447\le r<D^{73/240}}
\left(\frac{L_{23}}{r^2}+1\right).
\tag{J2-5}

The checker upper-encloses every `1/r^2` with common denominator `10^18` and proves

\[
\boxed{
\sum_{1447\le r<D^{73/240}\atop r\text{ prime}}
\frac1{r^2}
<
\frac{423}{5000000}.
}
\tag{J2-6}

Restoring the `+1` term for all 47735 primes gives

\[
\frac{|R_{j=2}|}{L_{23}}
<
\frac{20}{93}\frac{73}{80}\,7
\left(
\frac{423}{5000000}
+rac{47735}{L_{23}}
\right).
\]

The exact rational checker proves

\[
\boxed{
\frac{|R_{j=2}|}{L_{23}}
<
\frac3{25000}
=0.00012.
}
\tag{J2-7}

For orientation only, the displayed rational upper bound is about `0.00011622`.

---

## 5. Consequence

The complete valuation-two residual carrier is now finite-closed in physical space:

\[
\boxed{j=2\Longrightarrow |R_{j=2}|<0.00012L_{23}.}
\]

This is stronger for the finite splice than passing through the 254-state beta-2 inner support. It uses only:

1. the exact corrected residual reindexing;
2. least-prime valuation `2`;
3. the square-basin product ceiling;
4. elementary interval divisibility counts.

The result is a bound on the actual residual ordered-pair penalty after the corrected pointwise credit. It is not presented as an independent correction to the old source-main coefficient, so no source-main budget is double-counted here.

Together with the valuation ladder, the nontrivial residual frontier is now concentrated entirely in `j=1`; `j>=3` has no nontrivial P(23)-hard inner Rosser state, while `j=2` is directly bounded by (J2-7).

No finite P2 theorem or all-K claim is made.
