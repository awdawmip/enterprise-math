# P022 — Franel third-index Bailey tail and the first composite-boundary witness

Status: `PROVED_WIP / EXACT MOD-p REDUCTION + EXACT p=149 SPECIALIZATION`  
Owner: `P022 / program/p022-geometry-v2`  
Scope: special first-zero candidates at `n=(p+1)/3`

## 1. Why the one-third index matters

The current Franel rank program asks when a prescribed index can occur as

\[
r_p=\min\{n>0:p\mid F_n\}.
\]

The forced midpoint family gives one structured source, but midpoint
divisibility is often not primitive.  A second natural moving index is

\[
n=\frac{p+1}{3}
\]

for primes

\[
p\equiv5\pmod6.
\]

Write

\[
p=6d+5,\qquad
M=d+1=\frac{p+1}{6},
\qquad
n=2M=\frac{p+1}{3}.
\]

The newest P022 reduction turns divisibility at this moving Franel index into
a fixed terminating hypergeometric diagonal problem.

## 2. Prior-art boundary

The Bailey transformation and the q-supercongruence input used here come from
Xiaoxia Wang and Chang Xu, *New q-supercongruences from the Bailey
transformation*, arXiv:`2201.05378`.

P022 does not claim the Bailey transformation or the source q-supercongruence.
The project-specific step is the pole extraction at this Franel specialization
and its use as a rank/defect detector.

Historical novelty of the resulting specialized identities remains
`NOVELTY_UNVERIFIED`.

## 3. P022-TI01 — Bailey pole-tail reduction

The pole extraction gives

\[
\boxed{
F_{2M}\equiv-C_dH_d\pmod p,
}
\]

where `C_d` is a p-adic unit and

\[
H_d=
\sum_{j=0}^{d+1}
\frac{(-1/6)_j^2(2/3)_j}
     {(7/6)_j(1/2)_j\,j!}.
\]

Consequently,

\[
\boxed{
p\mid F_{2M}
\iff
H_d\equiv0\pmod p.
}
\]

The moving Franel value has therefore been replaced by a bounded
hypergeometric tail.

## 4. P022-TI02 — terminating diagonal transform

Because

\[
M=\frac{p+1}{6},
\]

the five rational parameters reduce modulo `p` to

\[
(-1/6,-1/6,2/3;7/6,1/2)
\equiv
(-M,-M,4M;M+1,3M).
\]

Define

\[
S_M=
{}_3F_2
\left(
\begin{matrix}
-M,-M,4M\\
M+1,3M
\end{matrix};1
\right).
\]

This terminates at `j=M`.  The exact modular bridge is

\[
\boxed{
H_d\equiv S_M\pmod p,
\qquad p=6M-1.
}
\]

Hence

\[
\boxed{
p\mid F_{2M}
\iff
S_M\equiv0\pmod{6M-1}.
}
\]

The distinction “modulo `p`” is essential.  `H_d` and `S_M` are generally
different rational numbers.  For example,

\[
H_0=\frac{65}{63},
\qquad
S_1=\frac53,
\]

and

\[
H_1=\frac{22940}{22113},
\qquad
S_2=\frac{193}{63}.
\]

Their reductions agree at the corresponding primes `5` and `11`.  A previous
test oracle accidentally used the exact values of `S_M` as though they were
the exact values of `H_d`; that test has now been repaired and the modular
bridge is executable directly.

## 5. P022-TI03 — `p=149` is a simple primitive third-index pivot

Take

\[
p=149=6\cdot25-1.
\]

Then

\[
M=25,\qquad
n=2M=50,
\]

and the Bailey tail vanishes:

\[
\boxed{S_{25}\equiv0\pmod{149}.}
\]

The recurrence rank scanner gives the complete zero alphabet

\[
\boxed{
Z_{149}=\{50,74,98\}.
}
\]

Therefore

\[
\boxed{r_{149}=50.}
\]

So `149` is not merely a divisor at the one-third index: it is a primitive
prime divisor of `F_50`.

The valuation is simple:

\[
\boxed{v_{149}(F_{50})=1.}
\]

Finally,

\[
2\cdot50-1=99
\]

is composite.  The primitive-defect theorem therefore gives the direct Barlow
pivot

\[
\boxed{v_{149}(D_{50})=1.}
\]

This is a clean non-midpoint, composite-boundary, unimodular Franel pivot
coming from the Bailey-tail family.

## 6. Why the zero alphabet makes `149` especially transparent

Since

\[
149\equiv5\pmod8,
\]

the midpoint

\[
74=\frac{149-1}{2}
\]

is forced to be a Franel zero.  Reflection pairs the other two zeros:

\[
50\longleftrightarrow98.
\]

Thus `z_149=3`, the smallest possible zero alphabet containing a non-midpoint
zero in a forced-midpoint residue class.  The minimal-basin criterion from the
rank note then certifies that the left-hand zero `50` must be the first zero.

So the same witness has three mutually consistent descriptions:

\[
\boxed{
S_{25}\equiv0
\Longleftrightarrow
149\mid F_{50}
\Longrightarrow
Z_{149}=\{50,74,98\}
\Longrightarrow
r_{149}=50.
}
\]

The first equivalence is the Bailey reduction; the full zero alphabet and
rank are independently checked by the Franel recurrence scanner.

## 7. An arithmetic progression that lands on composite Barlow boundaries

Suppose

\[
p\equiv5\pmod{72}.
\]

Write `p=72t+5`.  Then

\[
M=\frac{p+1}{6}=12t+1
\]

and the one-third index is

\[
n=2M=24t+2.
\]

Its Barlow odd boundary is

\[
2n-1=4M-1=48t+3,
\]

which is divisible by three and is composite for `t>=1`.

Therefore every prime in this progression satisfying the diagonal vanishing

\[
S_M\equiv0\pmod p
\]

produces a Franel divisor exactly on a composite Barlow boundary.  To upgrade
that divisor to the direct primitive pivot one must additionally prove that
`r_p=2M`; for primes `p=5 mod 8`, the minimal condition `z_p=3` is sufficient.

The example `p=149` is the first nontrivial exact instance currently recorded
by this route.

## 8. Finite pressure test

A recurrence-based scan in the current research session checked primes

\[
p\equiv5\pmod6,\qquad p\le500000.
\]

Within that finite range the one-third divisibility condition appeared only at

\[
p=5,\qquad p=149,
\]

and both occurrences were primitive at their one-third index.

This is **pressure-test evidence only**.  It is not a finiteness theorem and
must not be used to conjecture that `149` is the last such prime.

The repository's bounded regression suite locks only the much smaller
reproducible range below `500`; the larger scan is recorded here as
noncanonical experimental evidence.

## 9. New frontier

The one-third route has now been compressed to the diagonal problem

\[
\boxed{
S_M\equiv0\pmod{6M-1},
\qquad 6M-1\text{ prime}.
}
\]

For Barlow purposes there are then two separate questions:

1. **divisibility:** when does the terminating diagonal hypergeometric value
   vanish?
2. **primitivity:** when is `2M` the first zero digit rather than one member of
   a larger zero alphabet?

The `p=149` witness shows that the intersection is nonempty and already hits a
composite defect with a simple unit pivot.  What remains open is to turn this
isolated exact witness into an infinite or structurally classified family.

## 10. Executable assets

- `src/enterprise_math/p022_barlow_franel_third_index_bailey_tail.py`
  separates the rational pole tail `H_d`, the terminating transform `S_M`,
  their mod-`p` bridge, and the Franel residue.
- `tests/test_p022_barlow_franel_third_index_bailey_tail.py`
  locks the exact rational distinction, modular bridge, and the simple
  primitive `p=149, n=50` witness.
- `src/enterprise_math/p022_barlow_franel_lucas_rank.py`
  independently supplies the recurrence rank and complete zero alphabet.
