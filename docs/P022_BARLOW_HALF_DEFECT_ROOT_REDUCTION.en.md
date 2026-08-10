# P022 — Direct-Root Half-Defect Incidence as an Offset-Divisor Problem

Status: `ACTIVE RESEARCH NOTE / EXACT NECESSARY NORMAL FORM`  
Owner: `program/p022-geometry-v2`  
Depends on: half-defect prime-halving support tree; integer midpoint companion

## 1. Direct root setup

Let

\[
p\equiv5,23\pmod{24},\qquad m=(p-1)/2,
\]

and let an odd prime `q` divide `p-2` directly.  Write

\[
p-2=(2t+1)q.
\]

The A-basis node `q` creates the adjacent candidates

\[
j_+=(q+1)/2,
\qquad
j_-=(q-1)/2.
\]

Their companion offsets are

\[
d_+=m-j_+=tq,
\qquad
 d_-=m-j_-=tq+1.
\]

## 2. P022-LI40 — eliminate p and q from the root geometry

The preceding equalities can be inverted.

For the plus candidate,

\[
q\mid d,
\qquad
\boxed{p=2d+q+2.}
\]

For the minus candidate,

\[
q\mid d-1,
\qquad
\boxed{p=2d+q.}
\]

Thus every direct-root cancellation candidate at a fixed companion offset `d` is generated solely from odd prime divisors of `d` or `d-1`.

No factorization of `F_{m-d}` and no scan over primes `p` is needed to list the direct-root candidate moduli.

## 3. P022-LI41 — target mod-3 quotient restriction

All target primes satisfy

\[
p\equiv2\pmod3.
\]

If `q!=3`, then from

\[
p-2=(2t+1)q
\]

we obtain

\[
3\mid(2t+1),
\]

hence

\[
\boxed{t\equiv1\pmod3.}
\]

Equivalently:

- plus side: `q|d` and `(d/q)=1 (mod 3)`;
- minus side: `q|(d-1)` and `((d-1)/q)=1 (mod 3)`.

The root `q=3` is harmless for target `p>5`, because it creates only A-indices `2` and `1`, while

\[
F_1=2,\qquad F_2=10
\]

are `p`-adic units.

## 4. P022-LI42 — direct-root incidence is one gcd question

Let `C_d` be the finite set of target primes produced by the divisor rules above.  The universal integer companion supplies `H_d`.

Then direct-root support cancellation exists at offset `d` exactly when

\[
\boxed{
\gcd\!\left(H_d,\prod_{p\in C_d}p\right)>1.}
\]

This is a strict reduction of the direct-root problem to two ordinary integer objects attached to `d`.

The current executable pressure test finds no such target incidence for `d<1000`.  This is regression evidence only, not an infinite proof.

## 5. Why p=157 is informative but not a target counterexample

The known cancellation

\[
p=157,\quad d=62,\quad q=31
\]

has

\[
d/q=2,
\]

so it violates the target condition `t=1 (mod 3)`.  Correspondingly

\[
157\equiv13\pmod{24},
\]

outside the target residue classes.

Thus the arithmetic progression restriction is doing genuine work: it excludes the first known direct-root cancellation mechanism exactly at the quotient level.

## 6. Remaining frontier

There are now two distinct unresolved pieces:

1. **direct-root theorem:** prove that the gcd in P022-LI42 is always `1`;
2. **descendant theorem:** exclude hits created deeper in the prime-halving tree.

The second cannot be replaced by the first: a descendant node need not divide `p-2` directly.

The present reduction is intended to make the first problem accessible to congruence or recurrence methods without pretending that it settles the second.

## 7. Executable assets

- `src/enterprise_math/p022_barlow_half_defect_root_reduction.py`
- `tests/test_p022_barlow_half_defect_root_reduction.py`
