# Free Research — Simplified maximal Hamming carry witness

Status: `EXACT_FINITE_LEMMA / FORMALIZATION_REDUCTION / NOT_FOUNDATION`
Date: `2026-09-04`
Parent theorem: `PHC-T01`

Let `p` be prime, `N>=1`,

\[
q=\lfloor\log_pN\rfloor,
\qquad a=v_p(N),
\]

and set the single explicit shell

\[
\boxed{k_p(N)=p^q-1.}
\]

Then `0<=k_p(N)<=N-1` and

\[
\boxed{
v_p\binom{N-1}{p^q-1}=q-a.
}
\]

This is a simpler universal witness for PHC-T01 than the previously recorded valid witness `p^q-p^a`.

## Carry proof

For every `1<=r<=q`,

\[
(p^q-1)\bmod p^r=p^r-1.
\]

Also `p^q` is divisible by `p^r`, so

\[
(N-1-(p^q-1))\bmod p^r
=(N-p^q)\bmod p^r
=N\bmod p^r.
\]

Therefore the Kummer residue sum at level `r` is

\[
(p^r-1)+(N\bmod p^r).
\]

It reaches at least `p^r` exactly when `N mod p^r !=0`, equivalently exactly when `r>a`. Thus carries occur at precisely the levels

\[
a+1,a+2,\ldots,q,
\]

and their number is `q-a`.

## Formalization advantage

The witness separates the Lean proof into three reusable local lemmas:

1. `(p^q-1) % p^r = p^r-1` for `r<=q`;
2. `(N-p^q) % p^r = N % p^r` for `r<=q`;
3. for prime `p` and nonzero `N`, `N % p^r = 0` iff `r<=N.factorization p`.

Substitution into mathlib's exact Kummer factorization theorem identifies the filtered carry set with `Finset.Ioc a q`, whose cardinality is `q-a`.

A second route uses

\[
N\binom{N-1}{p^q-1}=p^q\binom N{p^q}
\]

plus the carry-free fact `v_p(binomial(N,p^q))=0`. The direct residue-set route appears more reusable for the current carry geometry.

## Executable status

`check_free_research_max_carry_simple_witness.py` checks the valuation formula and the levelwise carry equivalence for every prime `p<=N<=1200` using exact integers only; current status `PASS`.
