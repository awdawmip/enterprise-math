# Native discriminant formula for primitive Dirichlet spectral factors

Status: `FREE_RESEARCH / EXACT FINITE-ARITHMETIC THEOREM-CANDIDATE / NOT_FOUNDATION`
Date: `2026-09-05`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`
Depends on:
- internal phase quantization and recurrence identity;
- primitive factorization `Q_M=prod Psi_d`;
- native primitive resultant law;
- primitive endpoint mass `P_n`.

## 1. Full finite spectral discriminant

Let

\[
Q_M(u)=(-1)^{M-1}D_{M-1}(u)
\]

be the monic length-`M` finite spectral polynomial.  Its roots are the simple interior modes

\[
\alpha_k=u_{k,M},\qquad 1\le k<M.
\]

The internal phase recurrence identity is

\[
D_{M-1}(2-2C(\theta))S(\theta)=S(M\theta).
\]

At the root phase

\[
\theta_k=\frac{k\tau}{M},
\]

we have

\[
S(M\theta_k)=0,
\qquad
C(M\theta_k)=(-1)^k.
\]

Differentiate in `theta`.  Since

\[
\frac{d}{d\theta}(2-2C(\theta))=2S(\theta),
\]

and the factor `D_(M-1)` itself vanishes at the root, one obtains

\[
2D_{M-1}'(\alpha_k)S(\theta_k)^2
=M(-1)^k.
\]

The double-angle identity gives

\[
\alpha_k(4-\alpha_k)=4S(\theta_k)^2.
\]

Therefore

\[
\boxed{
|Q_M'(\alpha_k)|
=|D_{M-1}'(\alpha_k)|
=\frac{2M}{\alpha_k(4-\alpha_k)}.
}
\tag{PSD-1}

For a monic polynomial with simple roots,

\[
|\operatorname{Disc}Q_M|
=\prod_{k=1}^{M-1}|Q_M'(\alpha_k)|.
\]

The root product is

\[
\prod_k\alpha_k=M,
\]

and complement symmetry gives

\[
\prod_k(4-\alpha_k)=M.
\]

Hence

\[
\boxed{
|\operatorname{Disc}Q_M|
=2^{M-1}M^{M-3}.
}
\tag{PSD-2}

The formula includes `M=2`, where the right side is `2*2^(-1)=1` and `Q_2` is linear.

## 2. Discriminant factorization over primitive denominators

The monic primitive factorization is

\[
Q_M=\prod_{\substack{d\mid M\\d>1}}\Psi_d.
\]

Write

\[
\delta_d:=|\operatorname{Disc}\Psi_d|,
\]

and

\[
r(d,e):=|\operatorname{Res}(\Psi_d,\Psi_e)|.
\]

Then

\[
\boxed{
|\operatorname{Disc}Q_M|
=
\prod_{d\mid M,d>1}\delta_d
\prod_{\substack{d<e\\d,e\mid M}}r(d,e)^2.
}
\tag{PSD-3}

The native resultant law says

\[
r(d,e)=\begin{cases}
p^{\varphi(d)},&e/d=p^a,\\1,&\text{otherwise}.
\end{cases}
\]

For each top divisor `e`, define its cross-factor contribution

\[
B_e
:=\prod_{\substack{d\mid e\\2\le d<e}}r(d,e)^2
=
\prod_{p\mid e}
\prod_{\substack{1\le a\le v_p(e)\\e/p^a>1}}
 p^{2\varphi(e/p^a)}.
\tag{PSD-4}
\]

Then (PSD-3) becomes the divisor product

\[
\boxed{
2^{M-1}M^{M-3}
=
\prod_{e\mid M,e>1}\delta_e B_e.
}
\tag{PSD-5}

## 3. Divisor Möbius inversion

Apply multiplicative Möbius inversion to (PSD-5):

\[
\boxed{
\delta_nB_n
=
\prod_{d\mid n}
\left(2^{d-1}d^{d-3}\right)^{\mu(n/d)}.
}
\tag{PSD-6}

Here the `d=1` factor is interpreted as one.

The power of two contributed by the explicit `2^(d-1)` terms is

\[
\sum_{d\mid n}\mu(n/d)(d-1)=\varphi(n)
\]

for `n>1`.

Prime-by-prime simplification of the remaining integer powers and subtraction of (PSD-4) gives the closed primitive formula below.

## 4. Primitive spectral discriminant formula

Let

\[
P_n:=|\Psi_n(0)|
=\begin{cases}p,&n=p^a,\\1,&\text{otherwise}.
\end{cases}
\]

Then for every `n>=2`,

\[
\boxed{
|\operatorname{Disc}\Psi_n|
=
\frac{
2^{\varphi(n)}n^{\varphi(n)}
}{
P_n\displaystyle\prod_{p\mid n}p^{\varphi(n)/(p-1)}
}.
}
\tag{PSD-7}

The right side is an integer because it equals the discriminant of the monic integral factor `Psi_n`.

### valuation form

For an odd prime `p|n`, with `a=v_p(n)`,

\[
\boxed{
v_p(|\operatorname{Disc}\Psi_n|)
=a\varphi(n)-\frac{\varphi(n)}{p-1}
-\mathbf 1_{\{n=p^a\}}.
}
\tag{PSD-8}

For `p=2`,

\[
\boxed{
v_2(|\operatorname{Disc}\Psi_n|)
=\begin{cases}
\varphi(n),&n\text{ odd},\\
v_2(n)\varphi(n)-\mathbf 1_{\{n=2^a\}},&n\text{ even}.
\end{cases}}
\tag{PSD-9}

No odd prime outside the support of `n` divides the primitive spectral discriminant.

Thus the ramification support is contained in the prime support of `2n`.

## 5. Examples

\[
|\operatorname{Disc}\Psi_5|
=2^4 5^2=400,
\]

\[
|\operatorname{Disc}\Psi_9|
=2^6 3^8=419904,
\]

\[
|\operatorname{Disc}\Psi_{15}|
=2^8 3^4 5^6=324000000,
\]

\[
|\operatorname{Disc}\Psi_8|
=2^{11}=2048,
\]

\[
|\operatorname{Disc}\Psi_{12}|
=2^8 3^2=2304.
\]

These agree with exact symbolic checks of the finite primitive factors.

## 6. Classical cyclotomic discriminant appears as a compatibility image

The standard arithmetic expression for the absolute cyclotomic discriminant is

\[
|\operatorname{Disc}\Phi_n|
=
\frac{n^{\varphi(n)}}
{\displaystyle\prod_{p\mid n}p^{\varphi(n)/(p-1)}}.
\]

Comparing with the native spectral formula (PSD-7) gives

\[
\boxed{
|\operatorname{Disc}\Psi_n|
=
\frac{2^{\varphi(n)}}{P_n}
|\operatorname{Disc}\Phi_n|.
}
\tag{PSD-10}

Equivalently,

\[
\boxed{
|\operatorname{Disc}\Phi_n|
=
\frac{P_n}{2^{\varphi(n)}}
|\operatorname{Disc}\Psi_n|.
}
\tag{PSD-11}

The native proof of (PSD-7) does not require `Phi_n`; (PSD-10)--(PSD-11) are later classical compatibility readouts.

## 7. Orientation-resolved consequence for odd n

For odd `n>1`,

\[
\Psi_n=\Psi_n^E\Psi_n^O,
\]

with complementary orientation factors having equal discriminant magnitude, while

\[
|\operatorname{Res}(\Psi_n^E,\Psi_n^O)|
=2^{\varphi(n)/2}.
\]

Hence

\[
|\operatorname{Disc}\Psi_n|
=|\operatorname{Disc}\Psi_n^E|^2\,2^{\varphi(n)}.
\]

Combining with (PSD-7),

\[
\boxed{
|\operatorname{Disc}\Psi_n^E|^2
=|\operatorname{Disc}\Psi_n^O|^2
=
\frac{n^{\varphi(n)}}
{P_n\displaystyle\prod_{p\mid n}p^{\varphi(n)/(p-1)}}.
}
\tag{PSD-12}

This also proves arithmetically that the right side is a perfect square for odd `n>1`.

## 8. Interpretation

The full finite discriminant is controlled by three previously separated spectral readouts:

```text
within one primitive factor:
    Disc(Psi_n)

between different primitive factors:
    prime-power resultants

at the endpoint:
    primitive mass P_n
```

After all cross-denominator resultants are removed by divisor Möbius inversion, the remaining primitive self-separation is exactly (PSD-7).

Freeze:

`FULL_DIRICHLET_DISCRIMINANT = 2^(M-1) M^(M-3)`.

`PRIMITIVE_DISCRIMINANT = NATIVE_RESULTANT_MOBIUS_REMAINDER`.

`CYCLOTOMIC_DISCRIMINANT = SPECTRAL_DISCRIMINANT * ENDPOINT_MASS / 2^PHI`.
