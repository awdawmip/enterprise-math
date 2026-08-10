# P025 Supplement 86 — Signed Exponent Transport and Dyadic Non-Attenuation

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-cyclotomic-stage76`  
Depends on: P025 Supplements 84–85  
Hard block: `NONE`

## 1. The two sign graphs are connected

Stage 85 studies same-sign pressure transport separately for sums and differences. The missing cover edge is multiplication of the exponent by two.

For odd prime bases `p>q`, define

\[
D_m:=p^m-q^m,
\qquad
S_m:=p^m+q^m.
\]

Then

\[
\boxed{D_{2m}=D_mS_m.}
\]

Thus there is a natural cross-sign cover

\[
\boxed{(m,+)\longrightarrow(2m,-).}
\]

At the same time `(m,-)->(2m,-)` remains the ordinary difference cover.

## 2. P025-T180 — the two lower components overlap at exactly two

Since `p,q` are odd,

\[
D_m\text{ and }S_m\text{ are both even}.
\]

Any common divisor divides

\[
S_m-D_m=2q^m
\]

and

\[
S_m+D_m=2p^m.
\]

Because `p,q` are distinct primes,

\[
\boxed{\gcd(D_m,S_m)=2.}
\]

Therefore the two-block overlap correction is exactly

\[
\boxed{\Gamma=2.}
\]

for every exponent `m`.

## 3. P025-T181 — exact dyadic residual recomposition

The radical identity gives

\[
\operatorname{rad}(D_mS_m)
=
\frac{\operatorname{rad}(D_m)\operatorname{rad}(S_m)}2.
\]

Hence

\[
\boxed{
m(D_{2m})=2m(D_m)m(S_m).}
\]

Unlike a generic cyclotomic overlap, the correction is universal and independent of the prime values.

## 4. P025-T182 — exact signed doubling transport

The projective denominator at exponent `m` is

\[
m(p+q),
\]

while at exponent `2m` it is

\[
2m(p+q).
\]

Using P025-T181,

\[
\begin{aligned}
\rho_{2m,-}
&=
\frac{2m(D_m)m(S_m)}{2m(p+q)}\\
&=
\frac{m(D_m)}{m(p+q)}m(S_m)\\
&=
\rho_{m,-}m(S_m).
\end{aligned}
\]

Similarly,

\[
\boxed{
\rho_{2m,-}
=ho_{m,+}m(D_m).
}
\]

Thus

\[
\boxed{
\rho_{2m,-}
=ho_{m,-}m(p^m+q^m)
=ho_{m,+}m(p^m-q^m).
}
\]

This is the exact signed doubling law.

## 5. P025-T183 — doubling never attenuates pressure

Multiplicity residuals are positive integers, so

\[
m(D_m)\ge1,
\qquad
m(S_m)\ge1.
\]

Therefore

\[
\boxed{
\rho_{2m,-}\ge\rho_{m,-},
\qquad
\rho_{2m,-}\ge\rho_{m,+}.
}
\]

Equivalently,

\[
\boxed{
\rho_{2m,-}\ge
\max\{\rho_{m,-},\rho_{m,+}\}.
}
\]

So the prime-two exponent cover is fundamentally different from a generic odd-prime cover: it can be resonant or amplified, but never attenuated.

## 6. P025-C28 — the fourth-power counterexample is the resonant case

For

\[
(q,p)=(23,41),
\qquad m=2,
\]

Stage 82 gives

\[
p^2+q^2=2210
\]

squarefree. Thus

\[
m(S_2)=1.
\]

Therefore

\[
\boxed{
\rho_{4,-}=ho_{2,-}=\frac32.
}
\]

The fourth-power counterexample is exactly the resonant dyadic case.

Viewed from the sum branch,

\[
\rho_{2,+}=\frac1{128},
\]

while

\[
m(D_2)=192,
\]

so the same doubled state is also

\[
\rho_{4,-}
=rac1{128}\cdot192
=rac32.
\]

Thus one incoming edge is resonant while the other is strongly amplified.

## 7. P025-C29 — strict dyadic amplification occurs

For

\[
(q,p)=(7,17),
\qquad m=2,
\]

one has

\[
S_2=17^2+7^2=338=2\cdot13^2,
\]

so

\[
m(S_2)=13.
\]

Therefore

\[
\boxed{
\rho_{4,-}=13\rho_{2,-}.
}
\]

In this example

\[
\rho_{2,-}=\frac16,
\qquad
\rho_{4,-}=\frac{13}{6}>1.
\]

A subunit difference state becomes hard after one doubling step.

## 8. P025-T184 — dyadic difference towers are monotone

Iterate P025-T182. For

\[
e_j:=2^jm,
\]

we obtain

\[
\boxed{
\rho_{e_{j+1},-}
=
\rho_{e_j,-}
\,m(p^{e_j}+q^{e_j}).
}
\]

Hence

\[
\boxed{
\rho_{2^am,-}
=
\rho_{m,-}
\prod_{j=0}^{a-1}
m(p^{2^jm}+q^{2^jm}).
}
\]

Every factor in the product is a positive integer. Therefore

\[
\boxed{
\rho_{m,-}\le
\rho_{2m,-}\le
\rho_{4m,-}\le\cdots.
}
\]

In particular:

\[
\boxed{
\rho_{m,-}\ge1
\Longrightarrow
\rho_{2^am,-}\ge1
\quad\forall a\ge0.
}
\]

And because the first cross-sign doubling also never attenuates,

\[
\boxed{
\rho_{m,+}\ge1
\Longrightarrow
\rho_{2^am,-}\ge1
\quad\forall a\ge1.
}
\]

## 9. Consequence for hard-state counting

This produces infinite exponent descendants from one fixed prime-base pair whenever a lower state is active.

Those descendants are not independent hard mechanisms. They lie on one deterministic dyadic transport orbit.

Therefore any future exceptional-set argument that ranges over exponents should avoid counting

\[
m,2m,4m,8m,\ldots
\]

as unrelated events after a common active ancestor has been identified.

The correct state is an orbit / ancestor representation plus the integer edge multipliers.

## 10. The signed Hasse graph

Combining Stages 85–86 gives three cover types:

1. difference odd-prime cover
   \[
   (m,-)\to(mp,-);
   \]
2. difference dyadic cover
   \[
   (m,-)\to(2m,-);
   \]
3. sum covers
   \[
   (m,+)\to(mp,+)
   \quad(p\text{ odd prime}),
   \]
   together with the cross-sign edge
   \[
   (m,+)\to(2m,-).
   \]

There is no reverse difference-to-sum cover induced by exponent divisibility.

Thus the two same-sign Hasse diagrams are shadows of one directed signed transport graph.

## 11. Primitive roots are unchanged, but their descendants interact

Allowing cross-sign edges does not create an incoming edge to a prime difference node or to a sum root from Stage 85.

So the primitive nodes remain:

- difference roots: prime exponents;
- sum roots: odd prime exponents and powers of two.

But the descendants are now coupled: every sum node feeds its doubled difference node.

This explains why operation language changes both connectivity and monotonicity.

## 12. Precision interpretation

The special prime-two edge has a universal overlap correction that exactly cancels its exponent normalization cost:

\[
\frac{\Gamma}{2}=1.
\]

What remains is only a positive-integer residual multiplier.

Thus dyadic refinement is a **lossless-or-amplifying pressure transport**. In precision language, the doubling operation never forgets an already-visible hard-state signal on the difference output.

This is stronger than generic future compatibility: it is monotone signal preservation along a distinguished refinement edge.

## 13. Prior-art / novelty discipline

Difference-of-squares factorization and `gcd(x-y,x+y)=2` for odd coprime inputs are classical mathematics.

P025 claims none of those ingredients individually.

The project-side candidate is the exact projective signed-doubling law, its non-attenuation consequence, and its use to identify dyadic hard-state orbits that should be deduplicated in later precision/counting arguments. Historical novelty remains `NOVELTY_UNVERIFIED`.

## 14. Executable assets

Added:

- `src/enterprise_math/abc_signed_exponent_transport.py`;
- `tests/test_abc_signed_exponent_transport.py`.

The executable layer checks the universal overlap two, exact residual recomposition, both incoming doubling multipliers, resonant and amplified examples, and monotonicity on finite dyadic towers.

## 15. Next frontier

No hard block exists. Continue with:

1. derive the local multiplier for a generic odd-prime cover `m->rm` in terms of the new cyclotomic quotient and its overlap with the ancestor;
2. identify when an odd-prime cover is forced to attenuate, resonate, or amplify;
3. determine whether the special non-attenuation of prime two is unique among cover primes;
4. build an orbit-normal form that quotients out deterministic dyadic descendants before any exponent-family counting;
5. then relay signed transport / monotone dyadic refinement to A2/P023.
