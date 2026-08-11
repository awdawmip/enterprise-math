# P022 Barlow — Franel digit transversality via a two-integral Lagrange invariant

Status: **owner-branch research theorem + open arithmetic frontier / not canonical**

## 1. Problem

For the Franel sequence

\[
F_n=\sum_{k=0}^n\binom nk^3,
\]

Straub's Gessel--Lucas framework uses the formal derivative

\[
F'_n
=3\sum_{k=0}^n\binom nk^3(H_n-H_{n-k}).
\]

A particularly useful strengthening of single-digit zero control would be

\[
\boxed{p>n,\ p\mid F_n\Longrightarrow F'_n\not\equiv0\pmod p.}
\]

Call this **first-digit transversality**.  It is currently not proved here.

The exact bounded computation presently supports the stronger integer pattern

\[
\boxed{\gcd(F_n,\operatorname{num}F'_n)\mid2n!},
\]

checked through the current pressure horizon.  The factor `2` is necessary at
small n (`n=3` gives gcd 4).  This divisibility pattern is evidence, not a
canonical theorem.

## 2. Deep reflection split

The P022 p-square Jarvis--Verrill lift gives, at a deep digit zero `p^2|F_n`
and mirror `m=p-1-n`,

\[
(-8)^n\frac{F_m}{p}\equiv-F'_n\pmod p.
\]

Hence:

- `F'_n != 0 (mod p)` forces the reflected zero to have exact depth one;
- `F'_n = 0 (mod p)` forces the reflected zero to be deep as well.

Thus arbitrary higher valuation can be split into a transverse deep branch and
a genuine multiple-root locus `F_n=F'_n=0 (mod p)`.

The regression `p=67,n=23` is important: `v_67(F_23)=2`, but the mirror `43`
has depth one and `F'_23` is nonzero.  Therefore "deep" is not synonymous with
"multiple root".

## 3. Exact derivative Wronskian

Define

\[
W_n=F_nF'_{n+1}-F_{n+1}F'_n.
\]

Combining the Franel recurrence and its differentiated recurrence yields

\[
\boxed{
(n+1)^3W_n
=-8n^2(n+1)W_{n-1}
+F_n\bigl((7n+3)F_n+16nF_{n-1}\bigr).
}
\]

Put

\[
B_n=(7n+3)F_n+16nF_{n-1}.
\]

The forcing quotient

\[
T_n=\frac{F_nB_n}{n+1}
\]

is always an integer.  Indeed the Franel recurrence modulo `n+1` gives

\[
2(F_n+4F_{n-1})\equiv0\pmod{n+1},
\]

and

\[
B_n\equiv-4(F_n+4F_{n-1})\pmod{n+1}.
\]

If `n+1` is odd this directly supplies the denominator.  If it is even,
`(n+1)/2|B_n`; the missing factor two comes from the elementary parity theorem
`2|F_n` for every `n>=1`.

Therefore the integrating-factor coordinate

\[
\boxed{
Y_n=(n+1)^2(-8)^{-n}W_n
}
\]

satisfies

\[
\boxed{
Y_n-Y_{n-1}=(-8)^{-n}T_n
}
\]

with `T_n` integral.  Consequently

\[
\boxed{Y_n\in\mathbf Z[1/2].}
\]

All odd harmonic denominators in the formal derivative disappear from this
local Lagrange coordinate.

At a prime `p>n` with `p|F_n`, recurrence nonadjacency makes `F_(n+1)` a unit,
so

\[
F'_n\equiv0\pmod p
\Longleftrightarrow
W_n\equiv0\pmod p
\Longleftrightarrow
Y_n\equiv0\pmod p.
\]

Thus first-digit transversality is equivalent to nonvanishing of a 2-integral
Lagrange sequence at Franel roots.

## 4. Exact zero-transfer reflection

Let `H_L(x)` be the zero-normalized moving-interval solution of the same Franel
recurrence, `H_0=0,H_1=1`.  The formal recurrence reflection gives

\[
\boxed{
H_L(-L-1-x)
=
\left(\frac{x+L}{x+1}\right)^2H_L(x).
}
\]

At the fixed point

\[
x_0=-\frac{L+1}{2}
\]

this implies

\[
\boxed{
H'_L(x_0)=-\frac4{L-1}H_L(x_0).
}
\]

For an actual reflected digit pair, `L=p-1-2n` is even and `n=x_0 (mod p)`.
This is a useful **negative boundary**: a symmetric zero return automatically
has zero fixed-gap translation derivative, so one cannot prove first-digit
transversality merely by observing that a multiple root would reflect to a
multiple root.  The reflection derivative condition contains no independent
extra obstruction at this level.

## 5. Failed global-discriminant shortcut

For fixed n one may define

\[
P_n(X)=\sum_{k=0}^n\binom Xk^3,
\]

so `P_n(n)=F_n` and `P'_n(n)=F'_n`.  It is tempting to prove that the whole
polynomial has only small discriminant primes.  This is false: already very
small n produce discriminant factors much larger than n.  Therefore the desired
statement is genuinely about the **special endpoint X=n**, not global
squarefreeness of `P_n modulo p`.

Do not revive the global-discriminant route without additional endpoint
structure.

## 6. Current proof targets

The shortest transversality targets are now:

1. prove the observed endpoint divisibility
   \[
   \gcd(F_n,\operatorname{num}F'_n)\mid2n!;
   \]
2. or prove directly that a prime `p>n` cannot divide both `F_n` and the
   2-integral Lagrange coordinate `Y_n`;
3. use harmonic-weight identities only if they specifically control the
   endpoint sum
   \[
   \sum_k\binom nk^3H_k
   \]
   modulo a new prime divisor of `F_n`.

The Sofo harmonic-binomial literature and Straub Gessel--Lucas theory supply
relevant prior-art language, but no theorem located in the current audit closes
this endpoint nonvanishing problem directly.
