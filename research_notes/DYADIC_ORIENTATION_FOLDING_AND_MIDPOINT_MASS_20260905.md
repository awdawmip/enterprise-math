# Dyadic orientation folding and midpoint prime-power mass

Status: `FREE_RESEARCH / EXACT FINITE-ALGEBRA THEOREM-CANDIDATE / NOT_FOUNDATION`
Date: `2026-09-05`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`
Depends on:
- odd-denominator orientation factors `Psi_d^E,Psi_d^O`;
- primitive spectral pullback semigroup;
- native primitive resultant law.

## 1. Odd primitive factor has two reflection channels

For odd `d>1`, put

\[
h=\varphi(d)/2.
\]

The primitive factor splits

\[
\Psi_d=\Psi_d^E\Psi_d^O,
\]

where `E` contains the primitive even mode indices and `O` contains the primitive odd mode indices in `1,...,d-1`.

Both factors are monic integral of degree `h` and are exchanged by the complement involution `u -> 4-u`.

## 2. One dyadic pullback separates ancestry from new depth

The full primitive pullback law for a prime not dividing the denominator gives

\[
\operatorname{Monic}(\Psi_d\circ R_2)=\Psi_d\Psi_{2d}.
\]

The two orientation factors refine this product exactly:

\[
\boxed{
(-1)^h\Psi_d^E(R_2(u))=\Psi_d(u),
}
\tag{DOF-1}
\]

\[
\boxed{
(-1)^h\Psi_d^O(R_2(u))=\Psi_{2d}(u).
}
\tag{DOF-2}
\]

Proof by roots: an even primitive target index `r` has the two `R_2` preimages with denominator `d`; an odd primitive target index has the two preimages with denominator `2d`.  Degree and monicity close the identities.

Thus the even reflection channel reproduces the ancestral denominator while the odd reflection channel produces the genuinely new dyadic denominator.

## 3. Repeated dyadic pullback

Using `R_(2^a)=R_2^o a` and the prime-local pullback law, induction gives

\[
\boxed{
\operatorname{Monic}\bigl(\Psi_d^O(R_{2^a}(u))\bigr)
=\Psi_{2^a d}(u)
}
\tag{DOF-3}
\]

for every `a>=1`, while

\[
\boxed{
\operatorname{Monic}\bigl(\Psi_d^E(R_{2^a}(u))\bigr)
=\prod_{j=0}^{a-1}\Psi_{2^j d}(u).
}
\tag{DOF-4}
\]

The degree check is

\[
2^a h=\varphi(2^a d)
\]

for (DOF-3), and

\[
2^a h
=\sum_{j=0}^{a-1}\varphi(2^j d)
\]

for (DOF-4).

Hence the orientation meaning is exact:

```text
E channel -> all ancestral dyadic denominator levels below the new top
O channel -> the newest deepest 2-adic denominator level only
```

Freeze:

`E = DYADIC_ANCESTRAL_CHANNEL`.

`O = DYADIC_NEW_DEPTH_CHANNEL`.

## 4. Even primitive factors as folded odd orientation channels

Every even denominator has the form `2^a d` with `d` odd.  For `d>1`, (DOF-3) says its primitive factor is the `2^a`-phase pullback of the single odd orientation channel `Psi_d^O`.

Thus the apparent disappearance of the `E/O` factorization at an even denominator is not loss of orientation data: the orientation choice has already been consumed in selecting the new dyadic-depth channel before pullback.

The pure power-of-two family is the boundary case generated from `Psi_2(u)=u-2`:

\[
\boxed{
\Psi_{2^a}(u)
=\operatorname{Monic}\bigl(\Psi_2(R_{2^{a-1}}(u))\bigr),
\qquad a\ge2.
}
\tag{DOF-5}

## 5. Midpoint mass from the m=2 resultant boundary row

Because

\[
\Psi_2(u)=u-2,
\]

for every `d>2`, evaluation at the spectral midpoint is a resultant:

\[
\boxed{
|\Psi_d(2)|
=|\operatorname{Res}(\Psi_2,\Psi_d)|.
}
\tag{DOF-6}

Apply the native prime-power resultant law with `m=2`.  Since `phi(2)=1`,

\[
\boxed{
|\Psi_d(2)|
=\begin{cases}
p,&d/2=p^a\text{ for a prime }p,\\1,&\text{otherwise},
\end{cases}
\qquad d>2.
}
\tag{DOF-7}

Thus midpoint mass detects precisely the denominators which are twice a prime power.

A derived logarithmic readout is

\[
\log|\Psi_d(2)|
=\begin{cases}\Lambda(d/2),&2\mid d,\\0,&2\nmid d,\end{cases}
\]

for `d>2`; the integer prime/one law (DOF-7) is the native statement.

## 6. Orientation explanation of midpoint mass

For odd `d>1`, `R_2(2)=4`.  Evaluating (DOF-2) at `u=2` gives

\[
|\Psi_{2d}(2)|=|\Psi_d^O(4)|=P_d,
\]

where `P_d` is the primitive endpoint mass.

Thus the midpoint prime-power mass at denominator `2d` is literally the complementary-endpoint mass of the odd `O` orientation channel from which the new dyadic denominator was generated.

For deeper levels `a>=2`, `R_(2^a)(2)=0`, so

\[
|\Psi_{2^a d}(2)|=|\Psi_d^O(0)|=1
\]

for odd `d>1`, consistent with (DOF-7) because `2^(a-1)d` then has at least two distinct primes.

The pure power-of-two case (DOF-5) keeps midpoint mass `2` at every level, also consistent with `d/2` being a power of the prime `2`.

## 7. Structural interpretation

The three special spectral positions now have typed arithmetic roles:

```text
u=0 endpoint:
    primitive prime-power mass |Psi_d(0)|

u=4 endpoint:
    complementary orientation carries the same primitive mass

u=2 midpoint:
    m=2 resultant row
    -> detects d = 2 * prime-power
    -> records the first dyadic folding of the odd orientation channel
```

The midpoint is therefore not a third independent primitive mass rule.  It is the dyadic boundary trace of the orientation-resolved endpoint law under phase pullback.

Freeze:

`MIDPOINT_MASS = M_EQ_2_RESULTANT_BOUNDARY`.

`EVEN_DENOMINATOR_FACTOR = DYADIC_PULLBACK_OF_SELECTED_ODD_ORIENTATION_CHANNEL`.

`DYADIC_DEPTH_CREATION_CONSUMES_REFLECTION_ORIENTATION_SELECTION`.
