# P025 Supplement 79 — Odd-Prime Exponent Cyclotomic Pressure and Congruence Precision

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-cyclotomic-stage76`  
Depends on: P025 Supplements 72, 76–78  
Hard block: `NONE`

## 1. The cube mechanism is not special to exponent three

Let

\[
\ell\ge3
\]

be an odd prime, and let

\[
p>q\ge3
\]

be distinct odd primes. For the equal-exponent low-capacity atom with complements

\[
p^\ell,\ q^\ell,
\]

Stage 72's exact denominator is

\[
\ell(p+q).
\]

Hence the two sum/difference projective atoms are

\[
\boxed{
\rho_{\ell,+}
=\frac{m(p^\ell+q^\ell)}{\ell(p+q)},
\qquad
\rho_{\ell,-}
=\frac{m(p^\ell-q^\ell)}{\ell(p+q)}.
}
\]

For `ell=3`, these are exactly the cube atoms studied in Stages 75–78.

## 2. The nonlinear factors

Because `ell` is odd prime,

\[
p^\ell-q^\ell=(p-q)\Phi_\ell(p,q),
\]

and

\[
p^\ell+q^\ell=(p+q)\Phi_{2\ell}(p,q).
\]

Write

\[
L_-=p-q,
\qquad
F_-=\Phi_\ell(p,q),
\]

and

\[
L_+=p+q,
\qquad
F_+=\Phi_{2\ell}(p,q).
\]

Both `L_+` and `L_-` are even, while both nonlinear factors are odd.

The standard prime-exponent cyclotomic gcd identity gives

\[
\gcd(L_\pm,F_\pm)\in\{1,\ell\}.
\]

If `ell` occurs in the nonlinear factor, ordinary LTE gives it valuation exactly one. Thus the exceptional prime `ell` can overlap the linear factor, but it can never contribute nonlinear multiplicity residual.

## 3. P025-T154 — exact residual recomposition

Set

\[
g_\pm:=\gcd(L_\pm,\ell)\in\{1,\ell\}.
\]

Since every common support prime between `L_±` and `F_±` is the single simple prime `ell`, multiplicity residual recomposes exactly as

\[
\boxed{
m(p^\ell\pm q^\ell)
=g_\pm\,m(L_\pm)\,m(F_\pm).
}
\]

Therefore

\[
\boxed{
\rho_{\ell,\pm}
=
\frac{g_\pm m(L_\pm)m(F_\pm)}{\ell(p+q)}.
}
\]

This is the odd-prime-exponent analogue of the centered residual decompositions found at exponent three.

## 4. P025-T155 — threshold-one activation forces nonlinear cyclotomic repetition

Suppose first that `F_±` is squarefree. Then

\[
m(F_\pm)=1.
\]

Because `L_±` is even,

\[
m(L_\pm)=\frac{L_\pm}{\operatorname{rad}(L_\pm)}
\le \frac{L_\pm}{2}.
\]

Also `g_±<=ell`. Hence for the sum branch,

\[
\rho_{\ell,+}
\le
\frac{\ell (p+q)/2}{\ell(p+q)}
=\frac12.
\]

For the difference branch, `p-q<p+q`, so in fact

\[
\rho_{\ell,-}<\frac12.
\]

Therefore

\[
\boxed{
\rho_{\ell,\pm}\ge1
\Longrightarrow
F_\pm\text{ is nonsquarefree}.
}
\]

So every activated odd-prime equal-exponent atom must contain repeated multiplicity in the **nonlinear** cyclotomic factor. The linear factor can never carry the hard state alone.

This is stronger than the wording originally used for the cube-difference branch in Stage 76: at threshold one, nonlinear repetition is necessary there as well.

## 5. P025-T156 — repeated primes are `1 mod 2ell`

Let `r` be a repeated prime divisor of `F_-` or `F_+`.

The exceptional prime `ell` cannot repeat, so `r!=ell`. Also `r` is coprime to `pq`. Let

\[
x=pq^{-1}\pmod r.
\]

For `F_-`, `x` has exact order `ell`; for `F_+`, it has exact order `2ell`. Since `r` is odd, in either case

\[
\boxed{2\ell\mid r-1}.
\]

Thus

\[
\boxed{
r\equiv1\pmod{2\ell}.}
\]

In particular every repeated cyclotomic prime satisfies

\[
r\ge2\ell+1.
\]

For `ell=3`, this recovers Stage 76's `r=1 mod 6` support law.

## 6. P025-T157 — local root count is `ell-1`

Fix a repeated prime power

\[
r^e\mid F_\pm,
\qquad e\ge2.
\]

Modulo `r`, the allowed ratios are the primitive `ell`th roots for the difference branch or primitive `2ell`th roots for the sum branch. In either case their number is

\[
\varphi(\ell)=\varphi(2\ell)=\ell-1.
\]

Because `r` does not divide `ell`, these roots are simple and each has a unique Hensel lift to every `r^e`. Hence the local ratio state has exactly

\[
\boxed{\ell-1}
\]

classes modulo the full repeated prime power.

If the repeated support consists of `k` distinct primes with full repeated modulus

\[
M=\prod_{i=1}^k r_i^{e_i},
\]

CRT gives exactly

\[
\boxed{(\ell-1)^k}
\]

allowed labelled ratio classes modulo `M`.

Stage 77's binary `2^k` state is therefore exactly the specialization `ell=3`.

## 7. P025-T158 — projective pressure forces congruence precision

Assume

\[
\rho_{\ell,\pm}\ge T,
\qquad T\ge1.
\]

The exact residual formula gives

\[
m(F_\pm)
\ge
\frac{T\ell(p+q)}{g_\pm m(L_\pm)}.
\]

Since `g_±<=ell` and `L_±` is even, this implies the universal bound

\[
\boxed{m(F_\pm)\ge2T}
\]

for the sum branch, and the strict bound

\[
\boxed{m(F_-) > 2T}
\]

for the difference branch.

In particular `k>=1`.

Let

\[
R_{\rm rep}=\prod_{i=1}^k r_i.
\]

Because

\[
m(F_\pm)=\frac{M}{R_{\rm rep}}
\]

and every repeated `r_i>=2ell+1`,

\[
\boxed{
M
\ge
(2\ell+1)^k m(F_\pm)
\ge
2T(2\ell+1)^k
}
\]

(with strictness inherited on the difference branch).

The density of allowed ratio classes modulo `M` is therefore bounded by

\[
\boxed{
\frac{(\ell-1)^k}{M}
\le
\frac1{m(F_\pm)}
\left(\frac{\ell-1}{2\ell+1}\right)^k
\le
\frac1{2T}
\left(\frac{\ell-1}{2\ell+1}\right)^k.
}
\]

This is the central Stage-79 pressure/precision law:

> larger projective pressure automatically forces finer congruence precision, while every additional repeated cyclotomic prime decreases the permitted ratio density by at least another factor `(ell-1)/(2ell+1)`.

## 8. Exact calibrations beyond cubes

### Fifth-power sum

For

\[
(q,p)=(37,59),
\qquad \ell=5,
\]

one has

\[
\rho_{5,+}=\frac{31}{30}>1,
\]

and

\[
\Phi_{10}(59,37)=31^2\cdot8501.
\]

The repeated prime satisfies

\[
31\equiv1\pmod{10},
\]

and there are exactly

\[
5-1=4
\]

local ratio classes modulo `31^2`.

### Fifth-power difference

For

\[
(q,p)=(19,29),
\qquad \ell=5,
\]

\[
\rho_{5,-}=\frac{121}{48}>1,
\]

and

\[
\Phi_5(29,19)=5\cdot11^3\cdot271.
\]

The exceptional prime five is simple; the repeated prime is

\[
11\equiv1\pmod{10}.
\]

### Seventh powers

For `ell=7`, exact activated examples contain the repeated prime

\[
29\equiv1\pmod{14},
\]

with six local root classes, exactly as the general theorem predicts.

## 9. Architectural meaning

Stages 72 and 76–78 discovered the sequence

\[
\text{exponent shell}
\to
\text{cyclotomic support}
\to
\text{root-of-unity congruence state}.
\]

Stage 79 shows that this sequence is not a cube-specific trick. For every odd prime exponent, the future query "is this equal-exponent atom projectively activated?" forces a theorem-native congruence precision whose branching and modulus growth are explicit functions of the exponent:

\[
\boxed{
\text{local branching}=\ell-1,
\qquad
\text{repeated-prime modulus}\ge(2\ell+1)^2.
}
\]

The net modulus-per-class compression per repeated prime is at least

\[
\boxed{
\frac{(2\ell+1)^2}{\ell-1}.
}
\]

For `ell=3` this is `49/2`, exactly Stage 78.

Thus increasing exponent makes the local residue branch count larger, but the forced modulus grows faster; the net congruence state becomes more selective, not less.

## 10. Prior-art / novelty discipline

Cyclotomic factorization, the gcd identities, LTE, multiplicative orders, Euler's phi count, Hensel lifting and CRT are classical prior mathematics.

P025 does **not** claim those ingredients. The project-side candidate is their composition with the exact projective low-capacity atom into the pressure-to-congruence-precision law above. Historical novelty remains `NOVELTY_UNVERIFIED`.

## 11. Executable assets

Added:

- `src/enterprise_math/abc_odd_prime_exponent_cyclotomic.py`;
- `tests/test_abc_odd_prime_exponent_cyclotomic.py`.

The executable layer checks the exact residual recomposition, exceptional-prime valuation boundary, `1 mod 2ell` repeated support, observed root orders, CRT class count and pressure-driven modulus/density inequalities for `ell=3,5,7` fixtures.

## 12. Next frontier

No hard block exists. Continue with:

1. combine Stage 78's finite incidence envelope with Stage 79's threshold-dependent lower bound on `M`;
2. determine whether summing over all possible repeated moduli preserves the near-`1/T` pressure tail or loses it to signature multiplicity;
3. compare odd-prime exponents with even exponent four, where the difference branch can activate from centered linear-factor multiplicity even when the nonlinear factor is squarefree;
4. route the pressure-to-precision law back to A2/P023 only after its minimal abstract statement is separated from cyclotomic-specific arithmetic.
