# P017×P018 square diagonal — G3B parity-bilinear target

Status: `PROVED_WIP REDUCTION / ANALYTIC TARGET OPEN`

Companion to `P017_P018_SQUARE_DIAGONAL_GENERATION_3_WIP.md` and
`P017_P018_SQUARE_DIAGONAL_G3A_ROOT_PARITY_LEVEL_WIP.md`.

No Legendre proof is claimed.

## B1. Exact endpoint: prime existence is failure of positive Möbius polarization

Let

\[
U_k=k^2+2k,
\qquad
z_2(k)=\lfloor U_k^{1/3}\rfloor,
\]

and let

\[
\mathcal R_2(k)=
\{n:k^2<n\le U_k,\ (n,P_{z_2})=1\}.
\]

Generation 3A proves that every member of `R_2(k)` is either a prime with
`mu(n)=-1` or a squarefree semiprime with `mu(n)=+1`.  Therefore

\[
R_2(k)=|\mathcal R_2(k)|,
\qquad
M_2(k)=\sum_{n\in\mathcal R_2(k)}\mu(n)
\]

satisfy

\[
\boxed{
\pi((k+1)^2)-\pi(k^2)=\frac{R_2(k)-M_2(k)}2.
}
\]

Hence a Legendre failure is exactly

\[
\boxed{M_2(k)=R_2(k).}
\]

The final problem is therefore not another unsigned survivor estimate.  It is
to rule out **complete positive Möbius polarization** on this moving rough set.

## B2. Prior-art mother object: asymptotic-sieve bilinear Möbius cancellation

Friedlander--Iwaniec's asymptotic sieve separates ordinary sieve distribution
from the additional signed information needed to overcome parity.  Its
classical remainder axiom `(R)` is not enough by itself to detect primes; the
additional axiom `(B)` is a bilinear form containing the Möbius sign
`mu(mn)`.

In their notation, a representative form is

\[
\sum_m
\left|
\sum_{N<n\le2N,\ mn\le x}
\gamma(n,C)\mu(mn)a_{mn}
\right|,
\]

where

\[
\gamma(n,C)=\sum_{d\mid n,\ d\le C}\mu(d).
\]

The conceptual point is exact for the present project: **unsigned divisibility
remainders and signed Möbius bilinear cancellation are different resources**.
The former is the language that repeatedly collapsed back to ordinary sieve;
the latter is precisely the kind of information that can distinguish the two
signs at the minimal-P2 endpoint.

This is prior mathematics.  The bridge below is a square-shell specialization,
not a new generic asymptotic-sieve theorem.

## B3. Square-shell specialization

For the raw consecutive-square shell define

\[
a_k(t)=1_{\{k^2<t\le U_k\}}.
\]

Its direct Friedlander--Iwaniec-shaped signed hyperbolic form is

\[
\boxed{
\mathfrak B_k(N,C)
=
\sum_{m\ge1}
\left|
\sum_{\substack{N<n\le2N\\k^2<mn\le U_k}}
\gamma(n,C)\mu(mn)
\right|.
}
\]

For the actual minimal-P2 parity endpoint it is natural to insert the root
roughness condition:

\[
\boxed{
\mathfrak B^{(2)}_k(N,C)
=
\sum_{m\ge1}
\left|
\sum_{\substack{N<n\le2N\\k^2<mn\le U_k\\
(mn,P_{z_2})=1}}
\gamma(n,C)\mu(mn)
\right|.
}
\]

On the support of the second form, `mu(mn)` is exactly the prime/semiprime sign
of Generation 3A whenever `mn` is viewed as the square-shell state.  This is a
concrete candidate parity-breaking observable rather than a generic request
for "more precision".

No theorem here asserts that the 1998 asymptotic-sieve hypotheses are already
verified by the square-shell sequence.  The expression is a **target shape**
identified by the prior-art parity mechanism.

## B4. Exact moving hyperbolic fibers

For fixed positive `n`, the allowed outer factor is the integer interval

\[
\boxed{
\left\lfloor\frac{k^2}{n}\right\rfloor+1
\le m\le
\left\lfloor\frac{U_k}{n}\right\rfloor.
}
\]

Its exact cardinality is

\[
\boxed{
F_k(n)=
\left\lfloor\frac{U_k}{n}\right\rfloor
-
\left\lfloor\frac{k^2}{n}\right\rfloor.
}
\]

and

\[
F_k(n)=\frac{2k}{n}+\rho_k(n),
\qquad |\rho_k(n)|<1.
\]

Thus the parity target lives on a highly non-uniform moving strip:

- `n ~ k` gives `F_k(n)=O(1)`;
- `n ~ k^(2/3)` gives natural width `~k^(1/3)`;
- `n ~ k^(1/2)` gives natural width `~k^(1/2)`.

This scale variation is the same quotient-channel phenomenon seen internally,
but now the target retains the Möbius sign instead of taking an unsigned norm.

## B5. Signed parity refinement matches the P017 mod-2D capacity language

For odd `D`, odd shell states divisible by `D` are exactly one residue class

\[
n\equiv D\pmod{2D}.
\]

The exact incidence is

\[
g_k^{\rm odd}(D)
=
\left\lfloor\frac{U_k+D}{2D}\right\rfloor
-
\left\lfloor\frac{k^2+D}{2D}\right\rfloor.
\]

This is the same finite object as the P017 rule

`parity + divisibility = one class mod 2D`.

At root-P3 pair products `D=ab>k`, this incidence is `0/1` and coincides with
the unique odd-third-factor gate.  Therefore the earlier P017 signed-capacity
language and the Chen/Iwaniec bilinear-remainder language have now met at one
exact finite boundary object.  The factor `2` itself is not parity-breaking;
the new resource is cancellation of the **Möbius sign across those signed
fibers**.

## B6. Why the 1998 theorem cannot simply be quoted as a Legendre proof

The asymptotic sieve also assumes a strong unsigned distribution/remainder
axiom to a level `D>x^(2/3)`.  For a shell of length only `H~x^(1/2)`, the
individual consecutive-interval divisor remainder satisfies only the trivial
bound `|r(A,d)|<=1`; summing this absolutely to level `D` gives `O(D)`, which is
larger than the shell mass once `D>x^(1/2)`.

This does **not** prove that every stronger short-interval distribution axiom is
false.  It proves only that the 1998 theorem is not an immediate plug-in: the
square-root shell requires a short-interval replacement for the ordinary
unsigned distribution input *as well as* a Möbius-signed parity input.

This separates two resources which earlier project routes repeatedly mixed:

1. **distribution level / rough mass**, supplied asymptotically for almost
   primes by Chen--Iwaniec short-interval machinery;
2. **parity-breaking Möbius cancellation**, represented by a signed bilinear
   form such as `B_k^(2)` above.

## B7. Minimal new analytic theorem to seek

The most informative next theorem is not "improve the sieve" in the abstract.
It is a square-specific estimate which supplies a nontrivial cancellation for
`B_k^(2)(N,C)` (or an equivalent Möbius-signed hyperbolic form) on enough of the
moving factor ranges to force

\[
\boxed{M_2(k)<R_2(k).}
\]

Because `R_2-M_2` is an even nonnegative integer, any rigorous strict inequality
already forces at least one prime in the square shell.

A stronger but analytically natural target would be a uniform sign gap

\[
M_2(k)\le(1-\eta)R_2(k)
\]

for some absolute `eta>0`; this is much more than Legendre requires and should
not be treated as the minimal obligation.

## B8. Current negative boundary

Do not treat any of the following as parity-breaking by themselves:

- a stronger absolute bound on unsigned divisor remainders;
- another fixed-cutoff Fourier norm;
- more Bonferroni order after terminal exactness;
- local CRT compatibility or signed residue-class counting without the
  Möbius sign;
- the `1/42` direct-P2 lower-linear-sieve level gap from Generation 3A.

Those inputs may improve the P2 or explicit almost-prime layer, but the final
prime step still needs a sign-sensitive statement equivalent in strength to
ruling out `M_2=R_2`.

## Prior-art source

- J. B. Friedlander and H. Iwaniec, *Asymptotic sieve for primes*, Ann. of Math.
  (2) 148 (1998), 1041--1065.  The paper explicitly distinguishes the ordinary
  remainder axiom from its Möbius-bilinear axiom and explains that the latter
  supplies the cancellation which breaks the parity obstruction.
