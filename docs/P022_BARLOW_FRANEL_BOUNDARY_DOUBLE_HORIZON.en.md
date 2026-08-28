# P022 Barlow — Double-horizon integer kernel at the Franel twin boundary

Status: **PROVED_WIP / exact reduction / all-m nonvanishing still open**  
Owner: `RS-P022-OBSERVATION-HISTORY / TP2-2346F5D3E731ED56DB0A`  
Depends on: accepted P022 Bailey-tail / boundary exact-reduction chain

## 1. Why this normalization is useful

The accepted P022 arithmetic-core return reduces the first dangerous boundary to

\[
r=6m,\qquad q=18m-1,
\]

with the remaining obstruction

\[
q\mid F_{6m}.
\]

The older Bailey-tail owner theorem already gives, for a prime

\[
p=6M-1,
\]

\[
p\mid F_{2M}
\iff
T_M\equiv0\pmod p,
\]

where

\[
T_M={}_3F_2\!\left[
\begin{matrix}-M,-M,-M\\-3M,3M\end{matrix};1
\right].
\]

The Driver-routed boundary is exactly the subfamily `M=3m`, so the current
question is `T_(3m) != 0 (mod 18m-1)` under the surviving twin-boundary
hypotheses.

The point of this note is not to claim another zero-equivalence as a final
solution.  It puts the same obstruction into a second denominator-free form
whose horizon is `2M`, and then into a sign-free binomial form modulo `p`.
That gives a new surface on which a 3-section / pairing / finite-field argument
can act when `3 | M`.

## 2. The terminating transformation used

We use the standard terminating Thomae transformation

\[
{}_3F_2\!\left[
\begin{matrix}a,b,-N\\d,e\end{matrix};1
\right]
=
\frac{(d-a)_N}{(d)_N}
{}_3F_2\!\left[
\begin{matrix}a,e-b,-N\\1+a-d-N,e\end{matrix};1
\right].
\]

This is a terminating specialization in the classical `3F2(1)` transformation
orbit; compare DLMF §16.4(iii), especially the Thomae transformations around
16.4.11.  All identities below are finite rational identities, so no analytic
convergence issue enters.

Starting from `T_M`, four applications, with harmless permutations of upper and
lower parameters between steps, give

\[
\begin{aligned}
&{}_3F_2(-M,-M,-M;-3M,3M;1)\\
&\quad\xrightarrow{\ (-2M)_M/(-3M)_M\ }
{}_3F_2(-M,-M,4M;M+1,3M;1)\\
&\quad\xrightarrow{\ (1-3M)_M/(M+1)_M\ }
{}_3F_2(-M,4M,4M;2M,3M;1)\\
&\quad\xrightarrow{\ (-M)_M/(3M)_M\ }
{}_3F_2(-2M,-M,4M;1,2M;1)\\
&\quad\xrightarrow{\ (-2M)_{2M}/(2M)_{2M}\ }
{}_3F_2(-2M,M+1,4M;1,1;1).
\end{aligned}
\]

Multiplying and simplifying the four prefactors yields

\[
\boxed{
T_M=E_M K_M,
}
\]

where

\[
\boxed{
E_M=
\frac23
\frac{M!(2M)!(2M-1)!(3M-1)!}{(4M-1)!^2}
}
\]

and

\[
K_M={}_3F_2\!\left[
\begin{matrix}-2M,M+1,4M\\1,1\end{matrix};1
\right].
\]

Because the first upper parameter is `-2M`, this last value integerizes term by
term:

\[
\boxed{
K_M=
\sum_{j=0}^{2M}
(-1)^j
\binom{2M}{j}
\binom{M+j}{j}
\binom{4M+j-1}{j}
\in\mathbb Z.
}
\]

The first values are

\[
15,\ 1351,\ 154374,\ 19594887,\ 2639533390,\ldots
\]

for `M=1,2,3,4,5`.

## 3. No new denominator obstruction

For prime `p=6M-1>3`, every factorial argument in `E_M` is strictly below
`p`.  Hence

\[
\boxed{E_M\in\mathbb Z_p^\times.}
\]

Therefore

\[
\boxed{
T_M\equiv0\pmod p
\iff
K_M\equiv0\pmod p.
}
\]

This is a true zero-locus equivalence, not merely a numerical match.

## 4. Exact relation to the earlier integer kernel

The older owner branch already has

\[
D_M T_M=U_M,
\]

with

\[
D_M=\binom{3M}{M}\binom{4M-1}{M},
\]

\[
U_M=
\sum_{k=0}^M
\binom{M}{k}
\binom{2M+k}{k}
\binom{4M-1}{k}.
\]

Combining that identity with `T_M=E_M K_M` gives the exact rational conversion

\[
\boxed{
K_M=
\frac{\binom{4M-1}{M}}
{2\binom{2M-1}{M}}
\,U_M.
}
\]

When `p=6M-1` is prime, both binomial coefficients here have top argument below
`p`, hence the conversion multiplier is again a `p`-adic unit.  Thus `K_M`
does not manufacture a new exceptional prime: it exposes the same obstruction
in a different combinatorial geometry.

## 5. New sign-free companion modulo p

The double horizon gives an additional simplification that is not visible in
`U_M`.

Put `p=6M-1`.  For `0<=j<=2M-1`,

\[
4M+j-1=p-1-(2M-j-1),
\]

so the standard binomial complement congruence gives

\[
\binom{4M+j-1}{j}
\equiv
(-1)^j\binom{2M-1}{j}
\pmod p.
\]

The final term `j=2M` contains

\[
\binom{6M-1}{2M}=\binom p{2M}\equiv0\pmod p.
\]

Consequently the two signs cancel on every surviving term and

\[
\boxed{
K_M\equiv W_M\pmod p,
}
\]

where

\[
\boxed{
W_M=
\sum_{j=0}^{2M-1}
\binom{2M}{j}
\binom{M+j}{j}
\binom{2M-1}{j}.
}
\]

This is the main new normal form: the same P022 zero condition is represented
modulo `p` by a completely sign-free product of three ordinary binomial
coefficients.

## 6. Specialization to the accepted q=3r-1 boundary

At the Driver-routed boundary

\[
M=3m,\qquad r=2M=6m,\qquad q=6M-1=18m-1.
\]

Therefore

\[
\boxed{
q\mid F_{6m}
\iff
K_{3m}\equiv0\pmod q
\iff
W_{3m}\equiv0\pmod q.
}
\]

The P022 twin-center branch additionally requires `12m-1` and `12m+1` to be
prime, and the already-frozen survivor routing leaves the relevant `q` classes
`17,35 (mod 72)`.

The known non-boundary control remains visible: `p=149`, `M=25` has

\[
K_{25}\equiv U_{25}\equiv0\pmod{149},
\]

but `25=1 (mod 3)` and `4M-1=99` is composite.  Hence no theorem may claim
nonvanishing for all `M`; the `3|M` / twin-boundary structure is essential.

## 7. Exact remaining target

This note sharpens the unfinished unit to

\[
\boxed{
W_{3m}
ot\equiv0\pmod{18m-1}
}
\]

under the P022 admissible prime/twin hypotheses.

The next useful attacks are now concrete:

1. split the sign-free `2M` horizon into the three residue classes `j mod 3`
   when `M=3m` and search for a finite-field 3-section identity;
2. seek a reflection or Casoratian relation for the `W_M` summands that forces
   any common prime divisor into a residue class incompatible with the P022
   boundary;
3. connect the sign-free kernel to the already identified period-two
   cyclotomic Frobenius system.

A larger finite census is not a substitute for any of these proofs.

## 8. Executable assets

Added on the task execution branch:

- `src/enterprise_math/p022_barlow_franel_boundary_double_horizon.py`;
- `tests/test_p022_barlow_franel_boundary_double_horizon.py`.

They certify the exact rational transform, the exact conversion to the older
`U_M`, the sign-free modular companion, the known `p=149` control, and several
actual twin-boundary nonzero regression samples.
