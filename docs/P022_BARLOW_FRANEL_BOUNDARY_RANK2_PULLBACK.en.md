# P022 Barlow — Rank-two Franel pullback and cusp-transfer bridge

Status: **PROVED_WIP / exact prior-art interface + P022 specialization / boundary nonvanishing still open**  
Task: `RS-P022-OBSERVATION-HISTORY`  
Publication: `TP2-2346F5D3E731ED56DB0A`  
Researcher: `EM-P022OBS-D5D438`

## 1. Prior-art rank-two mother equation

Caruso, Fürnsinn, Vargas-Montoya and Zudilin, *Galois Groups of Apéry-like
Series Modulo Primes*, Bull. Aust. Math. Soc. 114 (2026), prove/use the Franel
generating-series representation

\[
h(x)=\sum_{n\ge0}F_nx^n
=\frac1{1-2x}
{}_2F_1\!\left(
\frac13,\frac23;1;
\frac{27x^2}{(1-2x)^3}
\right),
\]

and the second-order differential equation

\[
\boxed{
 x(x+1)(8x-1)h''
 +(24x^2+14x-1)h'
 +(8x+2)h=0.
}
\]

They also show that the Franel coefficients are p-Lucas.  If

\[
H_p(x)=\sum_{n=0}^{p-1}F_nx^n,
\]

then `h=H_p h^p` modulo `p`.

The point of the present note is not to re-prove that prior art.  It freezes the
exact consequences that are specific to the current P022 `q=3r-1` boundary and
connects them to the already-frozen Hahn / conductor-18 reductions.

## 2. Exact coefficient extraction over the integers

Expanding the rank-two pullback gives

\[
\frac1{1-2x}
{}_2F_1\left(\frac13,\frac23;1;
\frac{27x^2}{(1-2x)^3}\right)
=
\sum_{k\ge0}
\frac{(3k)!}{(k!)^3}
 x^{2k}(1-2x)^{-3k-1}.
\]

Therefore, for every `n>=0`,

\[
\boxed{
F_n=
\sum_{0\le k\le n/2}
\frac{(3k)!}{(k!)^3}
2^{n-2k}
\binom{n+k}{n-2k}.
}
\]

At an even index `n=2M`, duplication gives the exact terminating identity

\[
\boxed{
F_{2M}
=4^M\,{}_3F_2\!\left[
\begin{matrix}
-M,\ \frac12-M,\ 2M+1\\
1,\ 1
\end{matrix};1
\right].
}
\]

This is an integer identity, not merely a congruence.

Now impose the live boundary prime relation

\[
p=6M-1.
\]

Termwise modulo `p`,

\[
-M\equiv-\frac16,
\qquad
\frac12-M\equiv\frac13,
\qquad
2M+1\equiv\frac43.
\]

Thus the previously isolated fixed one-third Franel obstruction is exactly the
coefficient-extraction shadow of the rank-two Franel period.  The rank-three
`3F2` object was not introduced independently of the rank-two geometry.

For the P022 boundary `M=3m`,

\[
p=18m-1,
\qquad
F_{2M}=F_{6m},
\]

so this is the exact same residual already identified by the accepted Hahn and
double-horizon reductions.

## 3. Finite rank-two Hasse pullback

Let

\[
p=6M-1,
\qquad
N=2M-1=\frac{p-2}{3}.
\]

For

\[
g(y)={}_2F_1(1/3,2/3;1;y),
\]

the mod-`p` truncation has live degree `N`, because the next `(2/3)` Pochhammer
factor contains `p`.  Multiplying out the rational pullback gives the finite
polynomial identity

\[
\boxed{
H_p(x)
=
\sum_{k=0}^{N}
\frac{(3k)!}{(k!)^3}
 x^{2k}(1-2x)^{p-1-3k}
\pmod p.
}
\]

The last exponent is exactly one:

\[
p-1-3N=1,
\]

so the right side is an honest polynomial of degree at most `p-1`.

The executable companion reconstructs **every coefficient** and checks

\[
[x^n]H_p=F_n\pmod p
\qquad(0\le n<p),
\]

rather than checking only the boundary coefficient.

## 4. Three projective cusp involutions

The same 2026 prior-art analysis gives, for `p=5 (mod 6)`, three projective
involutions of the Franel truncation.  The two needed explicitly here are

\[
\sigma_A(x)=\frac{1-8x}{8+8x},
\qquad
H_p(x)=-(1+x)^{p-1}H_p(\sigma_A(x)),
\]

and

\[
\sigma_D(x)=\frac{1+x}{8x-1},
\qquad
H_p(x)=-(8x-1)^{p-1}H_p(\sigma_D(x)).
\]

The third is

\[
\sigma_X(x)=-\frac1{8x},
\qquad
H_p(x)=x^{p-1}H_p(\sigma_X(x)),
\]

which is the projective form of the Jarvis--Verrill reflection symmetry.

Evaluating the first two relations at `x=0` gives

\[
H_p(1/8)=H_p(-1)=-1,
\]

while `H_p(0)=1`.

The second-order Franel equation degenerates to a first-order condition at its
three finite singular points.  Hence

\[
H_p'(0)=2,
\qquad
H_p'(-1)=-\frac23,
\qquad
H_p'(1/8)=\frac83.
\]

Thus the canonical first-jet states are

\[
v_0=\binom{1}{2},
\qquad
v_{-1}=\binom{-1}{-2/3},
\qquad
v_{1/8}=\binom{-1}{8/3}.
\]

## 5. Exact 2x2 cusp-transfer matrices

Differentiating a gauge-Möbius relation

\[
H(x)=\chi g(x)H(\sigma(x))
\]

gives the state transfer

\[
\binom{H(x)}{H'(x)}
=
\chi
\begin{pmatrix}
g(x)&0\\g'(x)&g(x)\sigma'(x)
\end{pmatrix}
\binom{H(\sigma(x))}{H'(\sigma(x))}.
\]

At `x=0`, the Apéry-side involution gives

\[
\boxed{
 v_0=A_0v_{1/8},
 \qquad
 A_0=
 \begin{pmatrix}
 -1&0\\
 1&9/8
 \end{pmatrix}.
}
\]

The Domb-side involution gives

\[
\boxed{
 v_0=D_0v_{-1},
 \qquad
 D_0=
 \begin{pmatrix}
 -1&0\\
 -8&9
 \end{pmatrix}.
}
\]

Consequently

\[
\boxed{
 v_{1/8}
 =A_0^{-1}D_0v_{-1}
 =
 \begin{pmatrix}
 1&0\\
 -8&8
 \end{pmatrix}v_{-1}.
}
\]

This is the first natural rank-two matrix surface exposed in the current
boundary analysis.  It comes from the actual second-order mother equation, not
from fitting a matrix to finite P022 data.

## 6. The determinant carries the midpoint quadratic character

The first transfer determinant is

\[
\boxed{
\det A_0=-\frac98.
}
\]

Since `9` is a square and the cubic power `8` has the same quadratic character
as `2`,

\[
\boxed{
\left(\frac{\det A_0}{p}\right)
=
\left(\frac{-2}{p}\right).
}
\]

But `(-2/p)` is exactly the Jarvis--Verrill midpoint discriminator:

- it equals `-1` for `p=5,7 (mod 8)`, where the midpoint is forced to be a
  Franel zero;
- it equals `+1` for `p=1,3 (mod 8)`, where that particular mirror argument
  does not force a midpoint zero.

This is a genuine structural bridge between the rank-two transfer and the
previously isolated mod-eight midpoint phenomenon.

It is **not** yet the desired closure theorem.  What remains unproved is the
implication

\[
p\mid F_{(p+1)/3}
\Longrightarrow
\left(\frac{-2}{p}\right)=-1,
\]

or any equivalent statement saying that the one-third boundary-zero line can
exist only in the nonsquare transfer-discriminant sector.  The current P022
survivor classes lie in the opposite/selected residue sectors, so such an
implication would close the first-reentry boundary immediately; it must not be
asserted before proof.

## 7. Interface with the accepted Hahn / conductor-18 routes

We now have three exact views of the same residual:

1. **rank-two coefficient extraction** from the Franel `2F1` mother period;
2. **Hahn diagonal**
   \[
   Q_{3m}(3m;-9m,3m-1,9m);
   \]
3. **sign-free conductor-18 three-section kernel** `W_(3m)`.

The scalar dual-Hasse route was already proved redundant by the formal-adjoint
Lagrange identity.  The rank-two pullback identifies a more natural place for
the requested matrix invariant: it should compare local/cusp states of the
second-order mother equation with the coefficient-extraction/Hahn functional,
not merely add another scalar period value.

The next exact target is therefore one of the following equivalent-looking
bridges:

- prove that boundary-zero forces the nonsquare `det(A_0)` sector;
- express the boundary coefficient as a rank-two connection/Cartier minor whose
  determinant contains `det(A_0)`;
- or derive the same discriminant constraint from the accepted Hahn
  second-order difference operator.

No finite census is accepted as a substitute.
