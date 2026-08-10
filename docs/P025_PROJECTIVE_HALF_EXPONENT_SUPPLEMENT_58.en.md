# P025 Supplement 58 — The Critical One-Half Exponent in the Projective ABC Route

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-certificate-index-stage34`  
Depends on: P025 Supplements 47, 48, 57  
Hard block: `NONE`

## 1. Two elementary reverse bounds

The explicit projective resource is

\[
\sigma_{\rm proj}
=
\max\left\{
\frac{c}{R(S_a+S_b)},
\frac{b}{R(S_a+S_c)},
\frac{a}{R(S_b+S_c)}
\right\}.
\]

Assume an Oesterle-type radical bound

\[
c<R^M,
\qquad
1<M<2.
\]

### Nonunit slice

Supplement 48 proves

\[
\sigma_{\rm proj}
\le
\frac{c}{2\sqrt R}
<
\frac12 c^{1-1/(2M)}.
\]

### Pasten-nonexceptional unit slice

Supplement 57 proves that both nonunit entries are composite and

\[
S(n)\ge2/\sqrt n.
\]

Hence

\[
\sigma_{\rm proj}
\le
\frac{c^{3/2}}{2R}
<
\frac12 c^{3/2-1/M}.
\]

The unit threshold is larger:

\[
\boxed{
\frac32-\frac1M
>
1-\frac1{2M}
\qquad(M>1).
}
\]

Therefore the global direct projective threshold over Pasten's nonexceptional triples is

\[
\boxed{
\eta_{\rm dir}(M)
=
\frac32-\frac1M.
}
\]

## 2. P025-T123 — full Masser-Oesterle abc forces every PCC exponent above one half

The full Masser-Oesterle abc conjecture supplies radical exponents `M>1` arbitrarily close to one.

Since

\[
\lim_{M\downarrow1}
\left(\frac32-\frac1M\right)
=
\frac12,
\]

for every fixed

\[
\varepsilon>0
\]

one may choose `M>1` sufficiently close to one so that

\[
\frac32-\frac1M
<
\frac12+\varepsilon.
\]

Thus, with Pasten's same exceptional convention,

\[
\boxed{
\text{Masser-Oesterle abc}
\Longrightarrow
\mathrm{PCC}_{1/2+\varepsilon}
\quad\text{for every }\varepsilon>0.
}
\]

This implication no longer needs the arithmetic-derivative shortest-vector theorem; it follows from the explicit projective formula and elementary support-load bounds.

## 3. P025-T124 — any PCC exponent below one half crosses into Oesterle's `M<2` range

Supplement 47 proves

\[
\mathrm{PCC}_\eta
\Longrightarrow
\text{Oesterle-abc}_M
\quad
\text{for every }
M>\frac1{1-\eta}.
\]

If

\[
\eta<\frac12,
\]

then

\[
\boxed{
\frac1{1-\eta}<2.
}
\]

Therefore one may choose

\[
\frac1{1-\eta}<M<2,
\]

which is exactly Pasten's Oesterle weak-abc exponent range.

Hence

\[
\boxed{
\mathrm{PCC}_{1/2-\varepsilon}
\Longrightarrow
\text{Oesterle abc}
\qquad(\varepsilon>0).
}
\]

## 4. The phase boundary

The current implication architecture is therefore

\[
\boxed{
\text{full abc}
\Longrightarrow
\mathrm{PCC}_{1/2+}
\qquad\Big|\qquad
\mathrm{PCC}_{1/2-}
\Longrightarrow
\text{Oesterle abc}.
}
\]

At exactly

\[
\eta=1/2,
\]

PCC gives only

\[
M>2
\]

through the Stage-47 map, so it does not cross into Oesterle's strict `M<2` domain.

Thus `1/2` is a genuine logical transition in the compressed projective route, not an arbitrary optimization artifact.

## 5. Pointwise PCC at one half is false

The unit slice already supplies exact counterexamples to

\[
\sigma_{\rm proj}\le\sqrt c.
\]

For example

\[
1+288=289
\]

has

\[
\sigma_{\rm proj}=24
>
17=\sqrt{289}.
\]

Likewise

\[
1+239^2=2\cdot13^4
\]

has

\[
\sigma_{\rm proj}=2197/2
\gg
\sqrt{57122}.
\]

So the critical exponent should not be interpreted as a universal pointwise square-root bound.

The meaningful research questions are asymptotic/uniform-with-epsilon statements and the structure/sparsity of crossings above the square-root scale.

## 6. New primary target

Earlier P025 stages asked for some exponent

\[
\eta<1
\]

because that matches the Small Derivatives/Oesterle architecture.

The projective compression makes the sharper target visible:

\[
\boxed{
\text{understand whether the true nonexceptional projective exponent sits at, above, or below }1/2.
}
\]

The route naturally divides into:

- **upper side:** derive `PCC_(1/2+epsilon)` from sufficiently strong radical information;
- **lower side:** any uniform `PCC_(1/2-epsilon)` would already imply Oesterle abc;
- **critical layer:** classify explicit square-root-scale obstructions, especially the low-capacity unit Pell branches.

## 7. Relation to Stage 50

Stage 50 proves that for every fixed positive `eta`, PCC failures are power-saving sparse among all additive triples.

At the critical exponent `eta=1/2`, the coarse theorem gives

\[
O(X^{7/4})
\]

failures through height `X`, versus `Theta(X^2)` ambient additive triples.

This does not prove `PCC_(1/2+)`, but it shows that the square-root barrier is already accompanied by an unconditional sparse-exception statement.

The prime-square Pell subbranch has the stronger specialized count from Stages 54–55.

## 8. Prior-art / ownership boundary

The external abc/Oesterle implication language follows Pasten and classical abc literature. The direct support-load inequalities are elementary.

The project-specific candidate is the identification of `1/2` as the critical exponent after exact projective elimination of the arithmetic-derivative witness search.

This interpretation remains `NOVELTY_UNVERIFIED`; no priority language is permitted.

## 9. Executable assets

Added:

- `src/enterprise_math/abc_projective_half_exponent.py`;
- `tests/test_abc_projective_half_exponent.py`.

## 10. Next frontier

No hard block exists. Continue with:

1. square-root-scale unit Pell obstructions;
2. limsup/exceptional-set behavior of `log_c sigma_proj`;
3. whether prime-square Pell families can force infinitely many crossings above `1/2` under primality restrictions;
4. direct bounds for composite-unit cross capacities stronger than `2/sqrt n`;
5. no claim that `1/2` itself is attained as a universal theorem.
