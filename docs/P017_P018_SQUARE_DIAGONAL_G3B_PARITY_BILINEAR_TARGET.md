# P017×P018 square diagonal — G3B parity-bilinear target

Status: `PROVED_WIP REDUCTION / NEGATIVE BOUNDARY / ANALYTIC TARGET OPEN`

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

and

\[
\mathcal R_2(k)=
\{n:k^2<n\le U_k,\ (n,P_{z_2})=1\}.
\]

Every member of `R_2(k)` is either a prime with `mu(n)=-1` or a squarefree
semiprime with `mu(n)=+1`.  Hence

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

Thus

\[
\boxed{
\text{Legendre failure at }k
\iff M_2(k)=R_2(k).
}
\]

The final endpoint is **complete positive Möbius polarization** of the
minimal-P2 rough set.

## B2. Prior-art mother object: asymptotic-sieve bilinear Möbius cancellation

Friedlander--Iwaniec's asymptotic sieve separates ordinary unsigned sieve
distribution from the additional signed information needed to overcome parity.
Its remainder axiom `(R)` is not enough by itself to detect primes; the extra
axiom `(B)` contains a Möbius-signed bilinear form of the shape

\[
\sum_m
\left|
\sum_{N<n\le2N,\ mn\le x}
\gamma(n,C)\mu(mn)a_{mn}
\right|,
\qquad
\gamma(n,C)=\sum_{d\mid n,\ d\le C}\mu(d).
\]

Their point is exactly the one relevant here: **unsigned divisibility data and
Möbius-signed bilinear cancellation are different analytic resources**.  The
latter is what defeats the classical parity counterexamples.

This is prior mathematics.  The square-shell forms below identify the relevant
geometry; they do not assert that all hypotheses of the 1998 theorem are
already available here.

## B3. Raw square-shell specialization

For

\[
a_k(t)=1_{\{k^2<t\le U_k\}},
\]

the direct FI-shaped moving hyperbolic form is

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

For fixed positive `n`, the exact outer-factor fiber is

\[
\boxed{
\left\lfloor\frac{k^2}{n}\right\rfloor+1
\le m\le
\left\lfloor\frac{U_k}{n}\right\rfloor,
}
\]

with cardinality

\[
\boxed{
F_k(n)=
\left\lfloor\frac{U_k}{n}\right\rfloor
-
\left\lfloor\frac{k^2}{n}\right\rfloor
=
\frac{2k}{n}+\rho_k(n),
\quad |\rho_k(n)|<1.
}
\]

Thus the signed target lives on a non-uniform moving strip:

- `n~k`: fibers have `O(1)` natural length;
- `n~k^(2/3)`: natural length `~k^(1/3)`;
- `n~k^(1/2)`: natural length `~k^(1/2)`.

This is the quotient-channel geometry with the Möbius sign retained.

## B4. Critical correction: the final P2 rough set freezes the bilinear state sign

It is tempting to impose `(mn,P_{z_2})=1` directly inside the bilinear form and
call the result the final parity-breaking target.  That is **not** the right
analytic continuation.

Suppose

\[
k^2<mn\le U_k,
\qquad
(mn,P_{z_2})=1,
\qquad
m>1,\ n>1.
\]

The root cutoff gives `Omega(mn)<=2`.  Since both factors are nontrivial, each
contains at least one prime factor, hence `Omega(mn)=2`.  The square shell
contains no perfect square, so the two factors are distinct primes.  Therefore

\[
\boxed{
\mu(mn)=+1
}
\]

on **every nontrivial factorization** of the final minimal-P2 rough support.
Prime states have no factorization with both variables `>1` and therefore do
not enter such bilinear ranges at all.

This is `P2_BILINEAR_MOBIUS_SIGN_FREEZE`.

So a form obtained by first restricting completely to the final `z_2`-rough
set cannot obtain its parity-breaking power from the state factor `mu(mn)`:
that sign has already frozen.  Auxiliary coefficients such as `gamma(n,C)` may
still change sign, but that is not the prime/semiprime state parity resource.

**Correction to the first G3B draft:** a `z_2`-rough-only FI-shaped bilinear form
is retained only as a finite diagnostic/oracle.  It is not the candidate mother
mechanism for the final prime step.

## B5. Where the Möbius cancellation must live

The FI-type signed resource must therefore be consumed **before** the final P2
rough restriction, or through an equivalent descent identity which still sees
mixed factor-count states.

This explains the root ladder structurally:

- at root-P3 precision, nontrivial factorizations still encounter P2 and P3
  states and the sieve can use bilinear/weighted information to remove the
  three-factor contamination;
- after root-P2 precision is reached, every nontrivially factorable survivor is
  already a positive-Möbius semiprime and the remaining negative-Möbius objects
  are exactly the primes, which have disappeared from nontrivial bilinear
  factor ranges.

This is a finite root-cutoff form of the parity barrier.  It also clarifies why
Iwaniec--Laborde can use bilinear weighted-sieve information to reach P2, while
another application of the same final-rough bilinear language cannot simply be
iterated to primes.

The actual analytic target is therefore a **parity transport theorem**:
control a Möbius-signed bilinear form on a pre-P2/descent layer strongly enough
that, after the unsigned sieve descent reaches `z_2`, its information implies

\[
\boxed{M_2(k)<R_2(k).}
\]

The project does not yet have that transport theorem.

## B6. Signed parity refinement matches the P017 mod-2D capacity language

For odd `D`, odd shell states divisible by `D` occupy exactly one residue class

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

At root-P3 pair products `D=ab>k`, this incidence is `0/1` and is exactly the
unique odd-third-factor gate.  Therefore P017 signed-capacity geometry and the
Chen/Iwaniec short-interval remainder geometry meet at one exact finite object.

The factor `2` does not itself break parity.  It localizes the correct signed
residue classes on which a future Möbius-cancellation theorem would have to
operate.

## B7. Why the 1998 theorem cannot simply be quoted as a Legendre proof

The asymptotic sieve also assumes a strong unsigned distribution/remainder
axiom to a level `D>x^(2/3)`.  For a shell of length only `H~x^(1/2)`, the
individual consecutive-interval divisor remainder has only the trivial bound
`|r(A,d)|<=1`; summing this absolutely to level `D` gives `O(D)`, already larger
than the shell mass once `D>x^(1/2)`.

This does **not** prove that every stronger short-interval distribution theorem
is false.  It proves that the 1998 theorem is not an immediate plug-in.  A
square-root-shell proof needs both:

1. short-interval distribution/rough-mass input beyond the trivial absolute
   remainder sum;
2. a pre-sieve Möbius-signed bilinear input whose parity information survives
   the descent to the P2 endpoint.

The first resource is the territory of Chen--Iwaniec/Harman-style short-interval
sieves.  The second is the genuinely parity-sensitive bridge still missing
here.

## B8. Minimal new theorem to seek

The most precise current target is:

> **Square-diagonal parity transport.**  Establish a Möbius-signed bilinear
> estimate on a pre-P2 root/descent layer, in the moving square-shell geometry,
> and prove that the estimate survives the sieve descent as a strict endpoint
> inequality `M_2(k)<R_2(k)`.

A direct estimate only for the completely `z_2`-rough nontrivial factorization
support is insufficient because of `P2_BILINEAR_MOBIUS_SIGN_FREEZE`.

The minimal endpoint obligation remains only a strict inequality; a uniform
proportional gap

\[
M_2(k)\le(1-\eta)R_2(k)
\]

would be much stronger than required.

## B9. Current negative boundary

Do not treat any of the following as final parity-breaking by themselves:

- stronger absolute control of unsigned divisor remainders;
- another fixed-cutoff Fourier norm;
- more Bonferroni precision after terminal exactness;
- signed residue-class counting modulo `2D` without a Möbius-sign transport;
- the `1/42` direct-P2 lower-linear-sieve level gap from Generation 3A;
- an FI-shaped bilinear form imposed only after the support has already been
  reduced to minimal-P2 rough states.

These can improve or explicate the almost-prime layer, but the final prime step
still requires a sign-sensitive mechanism whose information is present before
the P2 sign freezes and remains visible afterward.

## Prior-art source

- J. B. Friedlander and H. Iwaniec, *Asymptotic sieve for primes*, Ann. of Math.
  (2) 148 (1998), 1041--1065.  The paper explicitly distinguishes its ordinary
  remainder axiom from a Möbius-bilinear axiom and explains that the latter
  supplies the cancellation which defeats the classical parity obstruction.
