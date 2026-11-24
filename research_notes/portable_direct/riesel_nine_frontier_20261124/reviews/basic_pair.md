# Targeted collaborative check of the budget-nine basic-pair obstruction

2026-11-24. Scope: `nine_prefix_v14/proof.md`, Sections 3 and 4, together with
the relevant order inventory in `inventory_certificate.json`. This is an
author-side, shared-context mathematical check, not an independent project
Review, formal acceptance, or new native BRC execution. It does not re-run the
whole classification or its execution suite.

## Finding

No mathematical error was found in the two basic-prime exclusion arguments.
The all-order remainder bounds cover every possible effective period. The
eight exceptional-prime capacities in Section 3 and the 22 finite residual
mass bounds in Section 4 are correct. Their resulting full-exponent gaps are
respectively at least 1/13860 and at least 1/210.

The only suggested exposition clarification is to say explicitly that the
parity fiber is pulled back to the original u residue set before using
`r1=|{x in R:x=1 mod3}|`. Under `u=epsilon+2z`, the maxima c_g are invariant
under this invertible affine change modulo 105. Both fixed W channels still
correspond to u=1 modulo three and cover one of the three compatible lifts.
Thus their mass is indeed r1/3, for either parity. No numerical correction
is required. The author has now added this clarification explicitly to
Section 4. The complete 22 rows are also now retained in
`nine_prefix_certificate.json`, under `basic_pair_geometry.parity_cases`.

## Section 3: all possible orders, including every excluded small period

For t=ord_q(4), the base-two order is t or 2t when t is odd, and is exactly
2t when t is even. This gives the following complete removals below the
stated remainder thresholds:

| gcd(t,105) | Smaller effective periods that must be considered | Eligible exceptions |
|---:|---|---|
| 1 | 1,2,4,8,11 | t=11 gives 23,89,683; the others give inactive/basic/old primes |
| 3 | 3,6,9,12,18 | t=9 gives fixed 19,73; t=18 gives inactive 37,109 |
| 5 | 5,10 | inactive 11 and old 31,41 |
| 7 | 7,14 | 43 at t=7 and 29 at t=14; old 127 is removed |
| 15 | 15 | old 151 and inactive 331 |
| 21 | 21 | 5419; old 337 is removed |
| 35 | none below 35 | none needed |
| 105 | none below 105 | none needed |

The remaining lower periods are consequently 13,24,20,28,30,42,35,105,
exactly as stated. Substituting the inherited incidence maxima
(36,23,11,7,6,4,2,1) gives the displayed capacities, all at most 1/12.

The exceptions have capacities

\[
7/36,\quad13/108,13/108,\quad1/9,\quad7/72,
\quad1/11,1/11,1/11.
\]

The two fixed W values use the actual shared u phase modulo three and its
count 13, not the unrestricted incidence maximum 23. Every listed exception
is larger than the generic bound 1/12. Hence nine slots are bounded by all
eight exceptions plus one generic slot, even if a proposed dictionary omits
some exceptions. Exact rational arithmetic confirms

\[
7/36+2(13/108)+1/9+7/72+3/11+1/12=2375/2376.
\]

Multiplication of the remaining fraction 1/2376 by the full old-hole density
6/35 gives 1/13860, as claimed.

## Section 4: period inventories and the affine parity restriction

For e=ord_q(16), the base-two order is one of e,2e,4e for odd e, and is
exactly 4e for even e. Therefore the exceptional eligible inventory is exactly:

| e | Base-two orders to examine | Eligible primes |
|---:|---|---|
| 7 | 7,14,28 | 29,43 |
| 9 | 9,18,36 | fixed 19,73; 37 and 109 are inactive |
| 10 | 40 | 61681 |
| 14 | 56 | 15790321 |
| 18 | 72 | 433,38737 |
| 21 | 21,42,84 | 1429,5419; 337 and 14449 are old |

The unavailable small periods e=1,2,3,4,5,6,8,12,15 reduce to old, basic,
or inactive primes. In particular e=15 includes base-two orders 15,30,60,
whose relevant primes 151,331,61,1321 are all excluded for those reasons.
No candidate has been silently discarded by a prime-size cutoff.

After removing the exceptional periods, the eight gcd-column thresholds are
11,24,20,28,30,42,35,105. This gives exactly the eight terms in G(R).
The exceptional absolute masses are c21 twice, c5/2, c7/2, c3/6 twice, and
r1/3 twice. Using eight copies of the generic bound is a relaxation, because
there are at most eight slots remaining before e=7 deletions; it cannot
underestimate a cover.

Removing m distinct nonempty e=7 rows leaves at most 8-m useful slots. If a
prime repeats an already removed row or is empty on the parity fiber, it
uses an additional slot while covering none of the residual set; the stated
bound still overestimates its possible contribution.

## Targeted arithmetic check of the 22 residual sets

Only this finite mass table was recomputed, with exact rational arithmetic.
The occupied original H rows modulo seven are

\[
(0,7),(1,7),(2,7),(3,5),(5,4),(6,6),
\]

where each pair is (residue,row size). For each of the 1+6+15 deletions of
zero, one or two distinct rows, the largest 8-m entries of the stated bound
multiset were summed. The results agree exactly with the proof:

| m | Number of cases | Maximum U(R)/|R| | Minimum gap | Extremal deleted rows |
|---:|---:|---:|---:|---|
| 0 | 1 | 25/27 | 8/3 | empty set |
| 1 | 6 | 155/174 | 19/6 | any one of 0,1,2 |
| 2 | 15 | 10/11 | 2 | any two of 0,1,2 |

In the last row |R|=22 and U(R)=20. In the middle extremal row |R|=29 and
U(R)=155/6. At m=0, |R|=36 and U(R)=100/3.

The normalization uses the original parity old-hole mass 36, not the reduced
size |R|: two uncovered absolute units therefore have full-exponent density
(3/35)(2/36)=1/210. This is consistent with deleting entire e=7 rows and with
either choice of the sole present basic prime.

## Evidence boundary

The displayed inventory certificate was read for its complete factorizations
and scope. Its full primality tree and all unrelated classification cases
were not rerun in this targeted check. The all-order exhaustiveness above is
an analytic check using the order-lifting formula, and the 22 mass cases are
an independent focused arithmetic recomputation. These checks support the
two claimed universal basic-pair obstructions without extending their scope.
