# P025 Supplement 62 — Pair-Radical Compression and the de Bruijn Prior-Art Ceiling

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-paired-square-tail-stage61`  
Depends on: P025 Supplements 47, 50, 60, 61  
Hard block: `NONE`

## 1. Stage 61 compresses a non-unit PCC failure to one pair product

Let `eta in (0,1)` be fixed. Stage 61 proves that every non-unit `PCC_eta` failure contains two distinct components `x,y` with

\[
\boxed{
m(x)m(y)\ge\frac12c^{1+\eta}.}
\]

Because primitive abc components are pairwise coprime,

\[
\operatorname{rad}(xy)=\operatorname{rad}(x)\operatorname{rad}(y)
=
\frac{xy}{m(x)m(y)}.
\]

On a dyadic range

\[
X/2<c\le X
\]

we have `xy<=X^2`, so

\[
\boxed{
\operatorname{rad}(xy)
\ll_\eta X^{1-\eta}.
}
\]

Thus the two-component failure state can be collapsed again to the single integer pair product

\[
\boxed{n=xy\le X^2}
\]

with small radical.

This reduction is exact arithmetic. The counting theorem applied to it below is classical prior art.

## 2. External de Bruijn input

Current abc exceptional-set literature records the classical de Bruijn estimate

\[
\#\{n\le x:\operatorname{rad}(n)\le x^\lambda\}
=
O_\varepsilon(x^{\lambda+\varepsilon})
\]

for fixed positive `lambda` [SRC-BERNERT-BROWNING-LICHTMAN-TERAVAINEN-2026-ABC-EXCEPTIONAL-CURRENT]. Lichtman's exposition also records the resulting classical almost-all abc consequence [SRC-LICHTMAN-2025-ABC-ALMOST-ALWAYS].

P025 adopts these facts as prior art. No radical-counting theorem is claimed here.

## 3. P025-T129 — de Bruijn improves the PCC-specific sparse-failure exponent

Apply the de Bruijn estimate to the pair product

\[
n=xy\le X^2.
\]

The Stage-61 radical bound has scale

\[
\operatorname{rad}(n)
\ll X^{1-\eta}
=
(X^2)^{(1-\eta)/2}.
\]

Therefore, after the arbitrary epsilon loss in the external estimate, the number of possible pair products is

\[
O_{\eta,\varepsilon}(X^{1-\eta+\varepsilon}).
\]

Each product has only `X^epsilon` possible factor pairs by the standard divisor bound, and the third additive component is then determined. Hence the non-unit PCC failures satisfy

\[
\boxed{
N^{\rm nonunit}_{\rm PCC-fail}(X)
=
O_{\eta,\varepsilon}(X^{1-\eta+\varepsilon}).
}
\]

For a unit triple, Stage 50 already forces one non-unit component `n<=X` with

\[
m(n)\ge c^\eta,
\]

hence on a dyadic range

\[
\operatorname{rad}(n)\ll_\eta X^{1-\eta}.
\]

The same de Bruijn estimate counts those one-variable unit failures by

\[
O_{\eta,\varepsilon}(X^{1-\eta+\varepsilon}).
\]

Thus, after dyadic summation,

\[
\boxed{
N_{\rm PCC-fail}(c\le X)
=
O_{\eta,\varepsilon}(X^{1-\eta+\varepsilon}).
}
\]

This is a PCC-specific theorem obtained by combining the project-specific paired-state reduction with an external classical counting theorem.

## 4. Consequence for the Stage-60 Oesterle benchmark

Stage 60 proves that for a fixed Oesterle exponent `M>1`, every sufficiently large failure of

\[
c<\operatorname{rad}(abc)^M
\]

must fail `PCC_eta` for any fixed

\[
0<\eta<1-1/M.
\]

Combining with P025-T129 and taking `eta` arbitrarily close to the boundary yields the internal route benchmark

\[
\boxed{
N_M(X)
=
O_{M,\varepsilon}(X^{1/M+\varepsilon}).
}
\]

This improves the elementary Stage-60 exponent, but it is still not competitive with the classical direct radical argument.

## 5. P025-NB12 — direct de Bruijn radical selection strictly dominates this Oesterle route

An Oesterle-M failure itself gives

\[
R=\operatorname{rad}(abc)\le X^{1/M}.
\]

Since `a,b,c` are pairwise coprime, at least one of the three pair-radical products is at most

\[
R^{2/3}\le X^{2/(3M)}.
\]

The classical de Bruijn argument then gives directly

\[
\boxed{
N_M(X)
=
O_{M,\varepsilon}(X^{2/(3M)+\varepsilon}),
}
\]

which is exactly the standard pair-radical-selector bound recorded in current exceptional-set literature [SRC-BERNERT-BROWNING-LICHTMAN-TERAVAINEN-2026-ABC-EXCEPTIONAL-CURRENT].

Because

\[
\frac{2}{3M}<\frac1M,
\]

the direct classical route strictly dominates the P025-via-PCC exceptional exponent for every `M>1`.

This is a **negative routing result**, not a failure of the PCC state itself:

> do not spend further P025 effort trying to make the Stage-50/60 counting layer competitive for ordinary abc exceptional sets unless a genuinely new input beats the classical pair-radical selector.

## 6. What remains valuable after the prior-art collision

The P025 route still contributes a different object:

\[
\text{PCC failure}
\to
\text{paired residual state}
\to
\text{pair-product radical state}.
\]

The PCC failure set is not itself the classical abc exceptional set. P025-T129 gives an unconditional sparse theorem about that project-defined finite-precision observable.

Architecturally, the important lesson is that a failure certificate can be compressed in stages:

1. one failed cyclic weighted-radical coordinate;
2. two residual components;
3. one pair product;
4. one pair radical;
5. external counting on the resulting coarse state.

But for ordinary Oesterle exceptional counting, the original global radical contains a still coarser and stronger selector, so the projective detour loses information relevant to that task.

This is exactly a P023-style task-relative quotient boundary: a representation that is useful for one future language can be inferior for another.

## 7. Prior-art discipline

The de Bruijn radical-counting estimate and its abc exceptional-set consequence are external prior mathematics. Current literature gives substantially stronger results beyond this classical bound. P025 makes no priority claim for those estimates [SRC-LICHTMAN-2025-ABC-ALMOST-ALWAYS; SRC-BERNERT-BROWNING-LICHTMAN-TERAVAINEN-2026-ABC-EXCEPTIONAL-CURRENT].

P025-T129 is only the composition of that prior theorem with the project-specific paired-residual compression from Stage 61. Its historical novelty is `NOVELTY_UNVERIFIED`, and no competitive analytic-number-theory claim is permitted.

## 8. Executable assets

Added:

- `src/enterprise_math/abc_projective_debruijn_bridge.py`;
- `tests/test_abc_projective_debruijn_bridge.py`;
- `sources_p025_paired_tail.json`.

The executable layer stores only exact finite reductions and rational exponent comparisons. It does not implement or re-prove the external asymptotic radical-counting theorem.

## 9. Next frontier

No hard block exists. Continue with:

1. stop optimizing Stage-60 ordinary abc exceptional exponents unless an input can beat the direct pair-radical selector;
2. study PCC failure as its own finite-precision exceptional language, where P025-T129 remains meaningful;
3. compare the explicit weighted-radical projective state with the anatomic radical decomposition used in modern exceptional-set work;
4. relay the negative routing result to A2/P023: task-relative coarse states can reverse which representation is information-optimal.
