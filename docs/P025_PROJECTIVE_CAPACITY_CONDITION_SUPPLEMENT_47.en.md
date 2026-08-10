# P025 Supplement 47 — Projective Capacity Condition: Removing Witness Search Entirely

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-certificate-index-stage34`  
Depends on: P025 Supplements 43, 46  
Hard block: `NONE`
Novelty status: `NOVELTY_UNVERIFIED / PRIORITY SEARCH INCOMPLETE`

## 1. The projective optimum is already explicit arithmetic

Supplement 43 computes

\[
\sigma_{\rm proj}
=
\inf_{x\in T\setminus T^\circ}
\frac{\|x\|_\infty}{\eta(x)}.
\]

Let

\[
S(n)
=
\sum_{p\mid n}
\frac{v_p(n)}p,
\qquad
R=\operatorname{rad}(abc).
\]

Since

\[
U_n
=nS(n),
\]

the three raw pair capacities become

\[
P_{ab}=ab(S(a)+S(b)),
\]

\[
P_{ac}=ac(S(a)+S(c)),
\]

\[
P_{bc}=bc(S(b)+S(c)).
\]

Also

\[
M=abc/R.
\]

Therefore

\[
\boxed{
\sigma_{\rm proj}
=
\max\left\{
\frac{c}{R(S(a)+S(b))},
\frac{b}{R(S(a)+S(c))},
\frac{a}{R(S(b)+S(c))}
\right\}.
}
\]

No derivative/witness optimization remains in this expression.

## 2. P025-D28 — cyclic weighted-radical defects

Define

\[
\rho_c
=
\frac{c}{R(S(a)+S(b))},
\]

\[
\rho_b
=
\frac{b}{R(S(a)+S(c))},
\]

\[
\rho_a
=
\frac{a}{R(S(b)+S(c))}.
\]

Then

\[
\boxed{
\sigma_{\rm proj}
=
\max\{\rho_a,\rho_b,\rho_c\}.
}
\]

The projective arithmetic-derivative route has therefore collapsed to an explicit cyclic weighted-radical state.

## 3. P025-C06 — Projective Capacity Condition

For fixed

\[
0<\eta<1,
\]

define the **Projective Capacity Condition** `PCC_eta` by

\[
\boxed{
\sigma_{\rm proj}<c^\eta
}
\]

outside Pasten's same finite/exceptional triple convention.

For rational

\[
\eta=p/q,
\]

the condition is decidable exactly by integer/rational powers.

## 4. P025-T113 — PCC is pointwise weaker than ESD

Supplement 43 proves

\[
\sigma_{\rm proj}
\le
\frac{\mu}{\eta_{\min}}
\le
\mu.
\]

Hence at every exponent

\[
\boxed{
\mathrm{SD}_\eta
\Longrightarrow
\mathrm{ESD}_\eta
\Longrightarrow
\mathrm{PCC}_\eta.
}
\]

The inequalities can be strict.

For the classical high-quality triple

\[
2+3^{10}\cdot109=23^5,
\]

\[
\sigma_{\rm proj}=6561/11
<
601=\mu/\eta_{\min}.
\]

The rational exponent

\[
\eta=31/76
\]

lies between their exact logarithmic thresholds: the PCC power inequality holds while the ESD inequality at the same exponent fails.

Thus PCC is not merely a renaming of ESD.

## 5. P025-T114 — PCC gives the same Oesterle direction

The c-oriented term satisfies

\[
\rho_c
\le
\sigma_{\rm proj}.
\]

Assume PCC at exponent `eta`. Then

\[
\frac{c}{R(S(a)+S(b))}
<c^\eta,
\]

so

\[
\boxed{
 c
<
R c^\eta(S(a)+S(b)).
}
\]

As in Supplement 46,

\[
S(a)+S(b)
<
\frac{\log c}{\log2}.
\]

Therefore

\[
\boxed{
\frac{c}{\log c}
<
R\frac{c^\eta}{\log2}.
}
\]

The same final argument as Pasten's Lemma 4.1 gives Oesterle-abc for every

\[
\boxed{
M>1/(1-\eta).
}
\]

So witness search can be removed entirely without weakening this implication.

## 6. Reverse arrow inherited from Pasten

Pasten's Theorem 4.5 gives, from Oesterle-abc at `1<M<2`, ordinary Small Derivatives for every

\[
\eta>1-(2-M)/(4M).
\]

By the pointwise resource chain,

\[
\boxed{
\text{Oesterle-abc}_M
\Longrightarrow
\mathrm{SD}_\eta
\Longrightarrow
\mathrm{ESD}_\eta
\Longrightarrow
\mathrm{PCC}_\eta.
}
\]

Thus PCC preserves the same published endpoint implication diagram while being a still weaker intermediate condition.

This statement uses Pasten's theorem as prior art; P025 does not re-prove the reverse abc-to-derivative arrow.

## 7. What has changed conceptually

The route has successively removed three kinds of unnecessary structure:

\[
\text{fine prime-coordinate witness}
\to
\mu
\to
\mu/\eta_{\min}
\to
\boxed{\sigma_{\rm proj}}
\to
\boxed{\text{explicit weighted-radical state}}.
\]

At the PCC level there is no existential certificate problem left. The remaining conjectural content is entirely an explicit relation among:

- radicals;
- prime-power exponents through `S(n)`;
- the additive ordering `a+b=c`.

This is a major simplification of the research surface, but it may also be close to a weighted reformulation of abc itself. That is precisely why prior-art and equivalence auditing are required before any novelty claim.

## 8. Negative boundary: PCC does not make the problem trivial

Because the c-oriented component is

\[
\rho_c
=
\frac{c}{R(S(a)+S(b))},
\]

any high-quality abc failure would force a correspondingly large projective defect unless the logarithmic-derivative load compensates it.

Thus a power-saving bound on `sigma_proj` remains genuinely abc-strength information; it is not an unconditional consequence of projective optimization.

The projective calculation removes the witness search, not the number-theoretic difficulty.

## 9. Prior-art search status

A focused search found Pasten's arithmetic-Wronskian / Small Derivatives framework and general arithmetic-derivative discussions, but did not identify this exact cyclic maximum

\[
\max\{c/[R(S_a+S_b)],b/[R(S_a+S_c)],a/[R(S_b+S_c)]\}
\]

as a named projective intermediate conjecture.

This absence is not evidence of originality. Status remains

\[
\boxed{\texttt{NOVELTY_UNVERIFIED}.}
\]

## 10. Executable assets

Added:

- `src/enterprise_math/abc_projective_capacity_condition.py`;
- `tests/test_abc_projective_capacity_condition.py`.

The code cross-checks the explicit weighted-radical formula against the independent LP/projective formula from Supplement 43.

## 11. Next frontier

No hard block exists. Continue with:

1. compare PCC with known weighted/radical reformulations of abc;
2. determine whether one cyclic component generically dominates in high-quality triples;
3. seek direct additive constraints on the three support loads `S(a),S(b),S(c)`;
4. use Stage 45 modular alignment only when returning from PCC to low-radius constructive witnesses;
5. keep PCC, ESD, and ordinary SD as distinct nodes in the implication graph.
