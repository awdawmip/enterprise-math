# P017 — c=103/20 T1–T2 Sub-Root Rosser Canonical Carrier

Status: `PROVED_WIP EXACT UNIQUE ENCODING + MONOTONE PRIME CUTOFF / FACTORIZATION STILL OPEN / NOT CANONICAL / NO FINITE P2 CLAIM`

Date: `2026-08-27`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Depends on:

- `docs/P017_P2_C515_T12_SECOND_BUCHSTAB_PAIR_SHELL_20260827.md`;
- `docs/P017_P2_C515_T12_SUPERROOT_PAIR_ABSORPTION_20260827.md`;
- `docs/P017_P2_C515_T12_GLOBAL_P41_ANCHOR_PRESTRIP_20260827.md`;
- the standard beta-2 upper Rosser–Iwaniec support condition.

Purpose: show that the remaining sub-root T1–T2 upper-sieve carrier has no intrinsic decomposition multiplicity. Every physical modulus has a unique largest/second-largest prime decomposition, and the upper-Rosser dependence on the external second prime is only a monotone cutoff.

---

## 1. Remaining carrier

After the first/second Buchstab reductions, high-LPF pointwise collapse, and super-root absorption, the only ordered-pair sector still requiring an upper-sieve estimate is

\[
\boxed{
 z\le r<D^{73/240},
 \qquad r<p,
 \qquad rp\le W.
}
\tag{C1}

For fixed `(r,p)`, the source upper sieve on

\[
S(\mathcal A_{rp},r)
\]

uses an odd squarefree modulus

\[
d\mid P(r),
\]

so every prime factor of `d` is strictly below `r`.

The available upper-sieve level is

\[
\boxed{Q(r,p)=\frac{D}{rp}.}
\tag{C2}

---

## 2. Exact beta-2 Rosser activation threshold

Write

\[
d=q_1q_2\cdots q_s,
\qquad
q_1>q_2>\cdots>q_s,
\]

and define

\[
\boxed{
q_{\rm crit}(d)
=
\max_{\substack{1\le j\le s\\j\ \mathrm{odd}}}
q_1\cdots q_{j-1}q_j^3,
}
\tag{C3}

with `q_crit(1)=1`.

For the beta-2 upper Rosser weight at level `Q`, the support condition is exactly

\[
\boxed{
\lambda_Q^+(d)\ne0
\iff
q_{\rm crit}(d)<Q.
}
\tag{C4}

On support, the coefficient is the squarefree Möbius sign `mu(d)`.

Substituting (C2),

\[
q_{\rm crit}(d)<\frac{D}{rp}
\]

is equivalent to the one-sided external-prime cutoff

\[
\boxed{
p<\frac{D}{r q_{\rm crit}(d)}.}
\tag{C5}

Thus, once `(r,d)` is fixed, the Rosser support does not introduce a second combinatorial family indexed by `p`: it only shortens the allowed upper endpoint of the already ordered prime variable.

---

## 3. Unique top-two-prime encoding

For every supported physical modulus put

\[
\boxed{q=rpd.}
\tag{C6}

Because every prime divisor of `d` is `<r<p`, the two largest prime divisors of `q` are uniquely

\[
\boxed{P^+(q)=p,\qquad P_2^+(q)=r.}
\tag{C7}

Consequently

\[
\boxed{d=\frac{q}{rp}}
\tag{C8}

is also uniquely recovered from the physical modulus.

Therefore the map

\[
(r,p,d)\longmapsto q=rpd
\]

is injective on the remaining sub-root upper-Rosser carrier.

In particular, two different source triples cannot create the same physical modulus and then be charged separately merely because they arose from different Buchstab or factorization labels.

---

## 4. Canonical two-variable form before analytic factorization

Define the canonical lower carrier

\[
\boxed{m=rd.}
\tag{C9}

Since `r` is the largest prime factor of `m`, it is itself recoverable from `m`, and so is

\[
d=m/r.
\]

Let

\[
R(m)=P^+(m)=r,
\qquad
D_-(m)=m/R(m)=d.
\]

Then the Rosser activation bound (C5) becomes the intrinsic monotone cutoff

\[
\boxed{
 p<P_{\max}(m)
:=
\frac{D}{R(m)\,q_{\rm crit}(D_-(m))}.
}
\tag{C10}

The other source/geometric restrictions contribute only additional upper/lower cutoffs:

\[
R(m)<p,
\qquad
p<\frac{W}{R(m)},
\qquad
p<D^{31/40},
\]

plus the explicit pair kernel `kappa(log_D R(m),log_D p)`.

Hence the entire remaining direct upper-Rosser carrier has the schematic exact form

\[
\boxed{
\sum_m \mu(D_-(m))
\sum_{R(m)<p<\mathcal P(m)}
\kappa\!\left(
\frac{\log R(m)}{\log D},
\frac{\log p}{\log D}
\right)
\,e(mp),
}
\tag{C11}

where

\[
\mathcal P(m)
=
\min\left(
\frac{W}{R(m)},
D^{31/40},
P_{\max}(m)
\right)
\]

and `e(mp)` denotes the sharp odd floor remainder on the chosen target interval (or its exactly descended version after the common anchor prestrip).

No factorization multiplicity appears in (C11).

---

## 5. Interpretation of the old factorization cost

The source Iwaniec remainder theorem rewrites Rosser errors as sums of factorable bilinear forms in order to apply a general analytic lemma. The unique encoding above shows that, for the present ordered-pair carrier, this multiplicity is **representational rather than arithmetic**:

- a physical modulus is counted by at most one `(r,p,d)` triple;
- the upper-Rosser condition is one monotone cutoff in the largest prime `p`;
- after the P(41) prestrip, the hard part of `d` has at most seven prime factors, all at least `43`.

This does not yet produce a factorable coefficient `a_m b_p`, because the endpoint `mathcal P(m)` depends on `m`. It does, however, isolate the exact remaining problem:

> separate one monotone two-variable inequality into a small number of analytic rectangles/canonical cuts, rather than decompose a multiply represented Rosser family.

---

## 6. Next target

Partition the `(m,p)` region by the size of `mathcal P(m)` and by the at-most-seven hard-factor scale pattern of `D_-(m)`. Compare:

1. a deterministic fixed-depth canonical rectangle decomposition; and
2. Iwaniec's well-factorable upper-sieve variant, whose modern formulations give `O(1/epsilon)` convolution pieces for a prescribed factorization scale.

The preferred route is whichever gives the smaller **explicit finite** cost after the P(41) anchor. No finite P2 theorem or all-K claim is made here.
