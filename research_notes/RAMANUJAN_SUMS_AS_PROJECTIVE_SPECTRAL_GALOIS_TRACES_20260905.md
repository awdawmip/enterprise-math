# Ramanujan sums as projective spectral Galois traces

Status: `FREE_RESEARCH / EXACT FINITE SPECTRAL TRACE THEOREM-CANDIDATE / NOT_FOUNDATION`
Date: `2026-09-05`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`
Depends on:
- irreducible/Galois projective factor `Omega_d`;
- decimation automorphisms `sigma_r(alpha)=R_r(alpha)`;
- denominator transition `d -> d/gcd(d,n)`.

## 1. Primitive field trace of the basic root

Let `d>2`, let

\[
\alpha_d=v_{1,d}
\]

be one root of `Omega_d`, and let

\[
K_d=\mathbf Q(\alpha_d).
\]

Define the root sum

\[
S_d:=\operatorname{Tr}_{K_d/\mathbf Q}(\alpha_d).
\]

Then

\[
\boxed{
S_d=\varphi(d)-\mu(d).
}
\tag{RA-1}

### Prime base case

For an odd prime `p`,

\[
R_p(v)=v\Omega_p(v)^2.
\]

The monic polynomial `R_p` has coefficient `-2p` on `v^(p-1)`, so the sum of all roots of `R_p`, with critical multiplicity, is `2p`.

The zero root contributes nothing and every root of `Omega_p` occurs twice.  Hence

\[
2S_p=2p,
\]

so

\[
S_p=p=(p-1)-(-1)=\varphi(p)-\mu(p).
\]

### Prime extension recursion

For an odd prime `p`, the leading terms of the monic decimation polynomial are

\[
R_p(v)=v^p-2pv^{p-1}+\cdots.
\]

If `p \nmid d`, the monic projective Frobenius identity is

\[
\Omega_d(R_p(v))
=
\Omega_d(v)\Omega_{pd}(v).
\]

If `h=phi(d)/2`, the coefficient of degree `ph-1` on the left comes only from the top power `R_p(v)^h`, so its root sum is

\[
2ph=p\varphi(d).
\]

Therefore

\[
\boxed{S_{pd}=p\varphi(d)-S_d.}
\tag{RA-2}
\]

If `p|d`, the single-preimage identity gives

\[
\Omega_{pd}(v)=\Omega_d(R_p(v)),
\]

and hence

\[
\boxed{S_{pd}=p\varphi(d).}
\tag{RA-3}

The recurrences (RA-2)-(RA-3), together with the complement relation for the single redundant factor of two, are exactly the recurrences of `phi(d)-mu(d)`.  This proves (RA-1) for all `d>2`.

---

## 2. Trace of the decimation trace polynomial

Let `C_n` be the integer trace/Dickson polynomial defined by

\[
C_0(x)=2,
\quad C_1(x)=x,
\quad C_{n+1}(x)=xC_n(x)-C_{n-1}(x),
\]

so

\[
\boxed{2-R_n(v)=C_n(2-v).}
\tag{RA-4}

Define

\[
\boxed{
T_d(n)
:=
\operatorname{Tr}_{K_d/\mathbf Q}
\bigl(C_n(2-\alpha_d)\bigr).
}
\tag{RA-5}

Let

\[
g=\gcd(d,n),
\qquad
e=d/g.
\]

Under `R_n`, every primitive denominator-`d` root maps to a primitive denominator-`e` root.  The map on Galois-conjugate root sets has constant fiber size

\[
\boxed{
\frac{\varphi(d)}{\varphi(e)}
}
\tag{RA-6}

with the natural endpoint interpretation for `e=1,2`.

Hence the trace of `R_n(alpha_d)` is

\[
\frac{\varphi(d)}{\varphi(e)}S_e.
\]

Using `2[K_d:Q]=phi(d)` and (RA-1),

\[
\begin{aligned}
T_d(n)
&=
\varphi(d)
-
\frac{\varphi(d)}{\varphi(e)}
(\varphi(e)-\mu(e))\\
&=
\boxed{
\mu(e)\frac{\varphi(d)}{\varphi(e)}.
}
\end{aligned}
\tag{RA-7}

But the classical arithmetic formula for the Ramanujan sum is

\[
c_d(n)
=
\mu\!\left(\frac d{\gcd(d,n)}\right)
\frac{\varphi(d)}
{\varphi(d/\gcd(d,n))}.
\]

Therefore

\[
\boxed{
\operatorname{Tr}_{K_d/\mathbf Q}
\bigl(C_n(2-\alpha_d)\bigr)
=c_d(n).
}
\tag{RA-8}

This identity can be taken as an internal spectral realization of Ramanujan sums; the right-hand closed formula is the arithmetic compatibility readout.

---

## 3. Special cases

For `n=1`, `C_1(x)=x`, so

\[
\boxed{
\operatorname{Tr}(2-\alpha_d)=\mu(d).
}
\tag{RA-9}

Equivalently,

\[
\boxed{
\operatorname{Tr}(\alpha_d)
=\varphi(d)-\mu(d),
}
\]

recovering (RA-1).

If `d|n`, then `e=1` and

\[
\boxed{T_d(n)=\varphi(d).}
\tag{RA-10}

If `e=2`, then

\[
\boxed{T_d(n)=-\varphi(d).}
\tag{RA-11}

These are exactly the two endpoint critical values in trace coordinates.

---

## 4. Coefficient of the projective primitive polynomial

Since `Omega_d` is monic of degree

\[
h=\varphi(d)/2,
\]

its next coefficient is minus the root trace.  Hence

\[
\boxed{
\Omega_d(v)
=
v^h
-
(\varphi(d)-\mu(d))v^{h-1}
+\cdots.
}
\tag{RA-12}

This explains the observed leading pairs:

```text
Omega_5  = v^2 - 5v + 5
Omega_7  = v^3 - 7v^2 + ...
Omega_8  = v^2 - 4v + 2
Omega_9  = v^3 - 6v^2 + ...
Omega_15 = v^4 - 7v^3 + ...
```

without factoring the full spectral polynomial.

---

## 5. All power traces from the `C_n` trace basis

Let

\[
x:=2-\alpha_d.
\]

The polynomials `C_n(x)` form the symmetric Laurent trace basis.  Algebraically,

\[
\boxed{
x^m
=
\mathbf 1_{2\mid m}\binom{m}{m/2}
+
\sum_{j=0}^{\lfloor(m-1)/2\rfloor}
\binom{m}{j}C_{m-2j}(x).
}
\tag{RA-13}

This follows by expanding `(z+z^-1)^m` and pairing opposite exponents; it is a polynomial identity over `Z[x]`.

Taking field traces and using (RA-8):

\[
\boxed{
\operatorname{Tr}(x^m)
=
\mathbf 1_{2\mid m}
\frac{\varphi(d)}2
\binom{m}{m/2}
+
\sum_{j=0}^{\lfloor(m-1)/2\rfloor}
\binom{m}{j}c_d(m-2j).
}
\tag{RA-14}

Now

\[
\alpha_d=2-x.
\]

Therefore

\[
\boxed{
\operatorname{Tr}(\alpha_d^m)
=
\sum_{q=0}^{m}
\binom{m}{q}2^{m-q}(-1)^q
\operatorname{Tr}(x^q),
}
\tag{RA-15}

with `Tr(x^q)` supplied explicitly by (RA-14).

Thus **every positive power sum of the primitive projective roots is an explicit integer combination of Ramanujan sums**.

---

## 6. Direct arithmetic compilation of `Omega_d`

Let

\[
p_m(d):=\operatorname{Tr}(\alpha_d^m).
\]

Equations (RA-14)-(RA-15) compute `p_1,...,p_h` using only:

- gcd;
- `mu`;
- `phi`;
- binomial coefficients;
- integer arithmetic.

Newton identities then recover the coefficients of the monic degree-`h` polynomial `Omega_d` exactly.

So there is a new native compilation route:

```text
input d
  -> Ramanujan sums c_d(1),...,c_d(h)
  -> power traces of alpha_d
  -> Newton identities
  -> Omega_d(v)
```

This avoids:

- building the degree `d-1` full polynomial `Q_d` first;
- polynomial division over all proper divisors;
- numerical root computation;
- classical cyclotomic factorization.

Complexity is governed by `h=phi(d)/2`, the actual irreducible projective block degree.

---

## 7. Frobenius/Galois meaning

The Galois group is

\[
(\mathbf Z/d\mathbf Z)^\times/\{\pm1\},
\]

and `sigma_r(alpha)=R_r(alpha)`.

Thus (RA-8) can be written intrinsically as

\[
\boxed{
 c_d(n)
=
\sum_{\sigma\in\operatorname{Gal}(K_d/\mathbf Q)}
\left(2-R_n(\sigma\alpha_d)\right).
}
\tag{RA-16}

Ramanujan sums are therefore character-free traces of the finite spectral Frobenius/decimation action.

---

## 8. BRC implication

For a BRC projective spectral root block `Omega_d`, the compiler can expose exact trace observables without algebraic-number root isolation:

- root sum from `phi(d)-mu(d)`;
- decimation trace from `c_d(n)`;
- all power traces via (RA-14)-(RA-15);
- the entire root block via Newton reconstruction.

This is especially useful when the requested BRC observation is trace/moment based rather than individual-root based.

Hard boundary: the Ramanujan trace formulas apply to this identified spectral division family, not to arbitrary BRC root blocks.

Freeze at free-research strength:

`RAMANUJAN_SUM = GALOIS_TRACE_OF_PROJECTIVE_SPECTRAL_DECIMATION`.

`TRACE(alpha_d) = PHI(d)-MU(d)`.

`OMEGA_d_CAN_BE_COMPILED_DIRECTLY_FROM_RAMANUJAN_TRACES_AND_NEWTON_IDENTITIES`.
