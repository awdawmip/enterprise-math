# Native prime-power resultant law for spectral cyclotomic factors

Status: `FREE_RESEARCH / EXACT FINITE SPECTRAL ARITHMETIC THEOREM-CANDIDATE / NOT_FOUNDATION`
Date: `2026-09-04`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`
Depends on:
- monic spectral factorization `Q_M=prod_(d|M,d>1) Psi_d`;
- finite scale cocycle;
- internal phase quantization at primitive roots;
- primitive spectral mass law.

This is a non-circular native proof route. No roots of unity or classical cyclotomic resultant theorem are used.

## 1. Integer primitive factors

The monic length polynomial

\[
Q_M(u)=(-1)^{M-1}D_{M-1}(u)
\]

lies in `Z[u]` and factors as

\[
\boxed{
Q_M(u)=\prod_{\substack{d\mid M\\d>1}}\Psi_d(u),
}
\tag{NRL-1}
\]

where `Psi_d` is monic and its roots are exactly the primitive denominator-`d` finite mode roots.

Inductively each `Psi_d` lies in `Z[u]`: the already constructed product of proper primitive factors is monic integral and divides the monic integral polynomial `Q_d`, so monic polynomial division preserves integrality.

Hence, for distinct `m,n`,

\[
\operatorname{Res}(\Psi_m,\Psi_n)\in\mathbb Z\setminus\{0\}.
\]

Write

\[
\boxed{
r_m(n):=
|\operatorname{Res}(\Psi_m,\Psi_n)|\in\mathbb Z_{>0}.
}
\tag{NRL-2}
\]

## 2. Primitive sine product from primitive spectral mass

For `m>1`, define the positive internal primitive sine product

\[
B_m
:=
\prod_{\substack{1\le r<m\\(r,m)=1}}
S\left(\frac{r\tau}{m}\right).
\]

All factors are positive because `0<r tau/m<tau`.

Let

\[
P_m
:=
\prod_{\substack{1\le r<m\\(r,m)=1}}
u_{r,m}
\]

be the primitive spectral root mass. The internal double-angle/decimation law gives

\[
R_2(u_{r,m})
=u_{r,m}(4-u_{r,m})
=4S(r\tau/m)^2.
\]

The complement map `r->m-r` permutes primitive residues and satisfies

\[
4-u_{r,m}=u_{m-r,m}.
\]

Therefore

\[
\prod_r R_2(u_{r,m})
=P_m^2
=4^{\varphi(m)}B_m^2.
\]

All quantities are positive, so

\[
\boxed{
B_m=\frac{P_m}{2^{\varphi(m)}}.
}
\tag{NRL-3}
\]

The already proved spectral Möbius law is

\[
\boxed{
P_m=
\begin{cases}
p,&m=p^a,\\1,&\omega(m)\ge2.
\end{cases}
}
\tag{NRL-4}
\]

## 3. Resultant against a full length polynomial

Assume `m` does not divide `d`, so `Psi_m` and `Q_d` have no common root. Define

\[
A_m(d):=
|\operatorname{Res}(\Psi_m,Q_d)|.
\]

At a primitive `m` root

\[
\alpha_r=u_{r,m},
\qquad (r,m)=1,
\]

the internal recurrence identity gives

\[
D_{d-1}(\alpha_r)
S(r\tau/m)
=
S(dr\tau/m).
\]

Since `Q_d=(-1)^{d-1}D_(d-1)`,

\[
|Q_d(\alpha_r)|
=
\frac{|S(dr\tau/m)|}{S(r\tau/m)}.
\]

Let

\[
g=(m,d),
\qquad
m'=m/g,
\qquad
d'=d/g.
\]

Then `(m',d')=1`. Reduction of primitive residues modulo `m'` is surjective with uniform fiber size

\[
\frac{\varphi(m)}{\varphi(m')}.
\]

Multiplication by `d'` permutes the primitive residues modulo `m'`. Internal antiperiodicity changes only signs when representatives are reduced, so absolute values are unaffected. Hence the numerator product is

\[
B_{m'}^{\varphi(m)/\varphi(m')}.
\]

Dividing by the denominator product `B_m` and using (NRL-3), all powers of `2` cancel. Thus

\[
\boxed{
A_m(d)
=
\frac{
P_{m'}^{\varphi(m)/\varphi(m')}
}{P_m},
\qquad
m'=\frac{m}{(m,d)}.
}
\tag{NRL-5}
\]

This is the key non-circular evaluation formula.

For convenience set `A_m(1)=1`; (NRL-5) also gives this value because `m'=m`.

## 4. Resultant Möbius inversion when m does not divide n

Suppose

\[
m\nmid n.
\]

Then no divisor `d|n` is divisible by `m`, so every `A_m(d)` is nonzero and defined by (NRL-5).

From the primitive factorization

\[
Q_d=\prod_{\substack{e\mid d\\e>1}}\Psi_e,
\]

resultant multiplicativity gives

\[
A_m(d)
=
\prod_{\substack{e\mid d\\e>1}}r_m(e).
\]

Multiplicative Möbius inversion in the positive rationals therefore yields

\[
\boxed{
 r_m(n)
=
\prod_{d\mid n}
A_m(d)^{\mu(n/d)}.
}
\tag{NRL-6}
\]

This formula resolves all incomparable index pairs before the scale-multiple case is considered.

## 5. Incomparable indices give unit resultants

Assume now

\[
2\le m<n,
\qquad
m\nmid n.
\]

Insert (NRL-5) into (NRL-6). Since `n>1`,

\[
\sum_{d\mid n}\mu(n/d)=0,
\]

so the denominator `P_m` cancels completely.

Fix a prime `p`. A `p`-adic contribution from the numerator can occur only when

\[
\frac{m}{(m,d)}=p^a
\]

for some `a>=1`, because `P_h` is nontrivial only for prime powers.

Write

\[
m=p^b c,
\qquad (p,c)=1.
\]

The condition `m/(m,d)=p^a` forces

\[
c\mid d.
\]

If `c` does not divide `n`, there are no such divisors and the `p`-exponent is zero.

Suppose `c|n`. If some prime `q!=p` occurs in `n` to an exponent strictly larger than in `c` (including any extra prime absent from `c`), then in the divisor sum the two allowed squarefree Möbius choices for that last `q`-exponent are both compatible with `c|d`, have opposite signs, and leave the `p`-dependent weight unchanged. They cancel pairwise. Hence the total `p`-exponent is again zero.

The only remaining possibility would be

\[
n=c p^t
\]

with no extra non-`p` exponent. But `m<n` then forces `t>b`, which implies `m|n`, contradicting the hypothesis.

Therefore every prime exponent in (NRL-6) is zero. Since the resultant magnitude is a positive integer,

\[
\boxed{
2\le m<n,\ m\nmid n
\quad\Longrightarrow\quad
r_m(n)=1.
}
\tag{NRL-7}

This establishes the incomparable case independently, with no appeal to the multiple case.

## 6. Exact scale-multiple quotient

Now let

\[
N=mt,
\qquad t>1.
\]

The normalized scale cocycle gives

\[
H_{mt}(u)=H_m(u)H_t(R_m(u)).
\]

Since

\[
Q_M=(-1)^{M-1}M H_M,
\]

we obtain

\[
\boxed{
\frac{Q_{mt}(u)}{Q_m(u)}
=(-1)^{mt-m}\,t\,H_t(R_m(u)).
}
\tag{NRL-8}

At a primitive `m` root `alpha=u_(r,m)`, internal phase multiplication gives

\[
R_m(\alpha)
=2-2C(r\tau)
\in\{0,4\}.
\]

Moreover

\[
H_t(0)=1,
\qquad
H_t(4)=(-1)^{t-1}.
\]

Therefore at every primitive root

\[
\boxed{
\left|
\frac{Q_{mt}}{Q_m}(\alpha)
\right|=t.
}
\tag{NRL-9}

Multiplying over the `phi(m)` roots gives

\[
\boxed{
 t^{\varphi(m)}
=
\prod_{\substack{d\mid mt\\d\nmid m}}
r_m(d).
}
\tag{NRL-10}

Here `d\nmid m` means that `d` is a divisor of `mt` which is not already a divisor of `m`.

## 7. Remove all incomparable factors

Every new divisor `d` in (NRL-10) is of one of two types:

1. `d=ms` for some divisor `s|t`, `s>1`;
2. `d` is incomparable with `m` under divisibility.

All type-2 factors have resultant magnitude one by (NRL-7), using symmetry if `d<m`.

Hence (NRL-10) reduces exactly to

\[
\boxed{
 t^{\varphi(m)}
=
\prod_{\substack{s\mid t\\s>1}}
r_m(ms).
}
\tag{NRL-11}

This is now an ordinary divisor-zeta relation in the multiplier `t`.

## 8. Möbius inversion in the multiplier

Apply multiplicative Möbius inversion to (NRL-11):

\[
\boxed{
 r_m(mt)
=
\prod_{s\mid t}
s^{\varphi(m)\mu(t/s)}.
}
\tag{NRL-12}

The inner arithmetic product is exactly the primitive mass expression, raised to `phi(m)`. Therefore

\[
\boxed{
 r_m(mt)
=
\begin{cases}
 p^{\varphi(m)},&t=p^a,\\
 1,&t\text{ has at least two distinct prime factors}.
\end{cases}
}
\tag{NRL-13}

No induction cycle remains.

## 9. Native spectral resultant theorem

Combining the incomparable and multiple cases, for `2<=m<n`,

\[
\boxed{
|\operatorname{Res}(\Psi_m,\Psi_n)|
=
\begin{cases}
 p^{\varphi(m)},& n/m=p^a\text{ for a prime }p,\\[1mm]
 1,&\text{otherwise}.
\end{cases}
}
\tag{NRL-14}

By symmetry of absolute resultants, for arbitrary distinct `m,n>1`,

\[
\boxed{
|\operatorname{Res}(\Psi_m,\Psi_n)|
=
\begin{cases}
 p^{\varphi(\min(m,n))},&
 \max(m,n)/\min(m,n)=p^a,\\[1mm]
 1,&\text{otherwise},
\end{cases}
}
\tag{NRL-15}

where the first case requires the displayed quotient to be an integer prime power.

## 10. Sign

The argument determines the invariant absolute value. Exact examples show both signs:

```text
Res(Psi_2,Psi_4)   = -2
Res(Psi_3,Psi_9)   =  9
Res(Psi_3,Psi_15)  = -25
```

The prime-power arithmetic statement is (NRL-15).

## 11. Classical compatibility

A separate later theorem identifies the spectral primitive factors with real trace transforms of ordinary cyclotomic factors. Under that map, (NRL-15) becomes the classical Apostol prime-power cyclotomic resultant law.

But the proof above uses only:

```text
native primitive factorization
+ internal S/C phase quantization
+ primitive spectral mass
+ integer resultant multiplicativity
+ two Möbius inversions
+ exact scale cocycle
```

Therefore the resultant law is already a finite spectral arithmetic theorem; classical roots of unity are not a proof input.

Freeze:

`SPECTRAL_PRIMITIVE_RESULTANT_PRIME_POWER_LAW = NATIVE_FINITE_ARITHMETIC`.

`CLASSICAL_APOSTOL_RESULTANT = LATER_TRACE_COMPATIBILITY_IMAGE`.
