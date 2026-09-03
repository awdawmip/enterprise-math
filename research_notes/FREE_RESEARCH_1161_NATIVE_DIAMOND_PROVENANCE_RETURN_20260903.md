# Free Research #1161 — native commuting-diamond provenance realization of the return masses

Status: `FREE_RESEARCH_RESULT / NATIVE-MULTIPATH PROVENANCE BRIDGE / NOT WORKING_TRUTH / NOT FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-FREE-G61R8`
Parent issue: `#1161`
Dependencies:
- frozen R061 `(1,1)` commuting diamond;
- R062 Path-formal/N-BRC/Boolean-BRC enrichment tower;
- #1161 balanced-return mass completion.

## 1. Native two-choice macroblock

In one frozen native right sector, the `(1,1)` trace has exactly two distinct native path witnesses

\[
\alpha=X_iX_j,
\qquad
\beta=X_jX_i,
\]

with the same typed terminal cell.

Treat one such translated commuting diamond as a macroblock and retain a provenance tag recording whether its concrete witness was `alpha` or `beta`.

At the end of each macroblock the two spatial path alternatives have already recoalesced to the same native cell. The provenance tag is nevertheless retained at the Path-formal/N-BRC enrichment level.

Freeze the typing distinction used below:

`SPATIAL_RECOALESCENCE != PROVENANCE_ERASURE`.

## 2. One provenance channel

Concatenate `2n` tagged diamond macroblocks. The macroblock endpoint after each time step is deterministic, while the provenance word lies in

\[
\{\alpha,\beta\}^{2n}.
\]

There are `2^(2n)` such provenance histories.

Define the **balanced provenance shell** by requiring exactly `n` occurrences of `alpha` and `n` occurrences of `beta`.

Its cardinality is

\[
\binom{2n}{n}.
\]

This balance predicate is a provenance-count relation. It is not a signed native spatial axis and does not identify `alpha` with an opposite geometric direction.

## 3. Two independent tagged channels

Take two independently tagged copies of the same macroblock process. A combined time slot has four branch choices

\[
(\alpha,\alpha),
(\alpha,\beta),
(\beta,\alpha),
(\beta,\beta).
\]

Over `2n` macro-times, the total combined history count is

\[
4^{2n}=16^n.
\]

Require each provenance channel separately to lie in its balanced shell. The balanced combined-history count is

\[
\boxed{\binom{2n}{n}^2}.
\]

Give each combined macro-time branch equal positive rational weight `1/4`. Then each length-`2n` combined history has weight `16^{-n}` and the total balanced provenance mass is

\[
\boxed{
c_n=\frac{\binom{2n}{n}^2}{16^n}.
}
\]

This is exactly the coefficient used in the #1161 return Green completion.

Therefore

`POWER_SERIES_COEFFICIENT c_n = NATIVE_DIAMOND_PROVENANCE_BALANCE_MASS`

at a typed Path-formal/positive-weight enrichment layer.

## 4. Why block provenance is essential

Each macroblock contributes one `X_i` and one `X_j` to the underlying native component trace. If the `2n` macroblock boundaries and their `alpha/beta` provenance are erased and one replaces the process by the complete flattened trace fiber, the branch population is no longer the binary macrohistory set.

For one channel, the block-preserving history count is

\[
2^{2n},
\]

whereas the full flattened trace `T_{2n,2n}` has

\[
\binom{4n}{2n}
\]

path linearizations.

These disagree for `n>=2`.

Thus the balanced-return mass is not a function of the flattened endpoint/trace support alone.

The construction requires

\[
\boxed{
\text{macroblock provenance before recoalescence/flattening}.
}
\]

This is the same typed information principle already encountered in the #1161 derivation of `P_n=2^n`, now applied to a two-channel long-time balance observable.

## 5. Boolean support is insufficient

At every individual diamond, Boolean BRC sees one reachable terminal support state regardless of whether the witness is `alpha` or `beta`.

After `2n` macroblocks, Boolean support therefore still sees only the deterministic terminal macrostate. It cannot distinguish

- the total `2^(2n)` provenance histories;
- the balanced shell `binom(2n,n)`;
- the two-channel balanced mass `c_n`.

Hence

\[
\boxed{
BOOLEAN\_SUPPORT
\not\Rightarrow
PROVENANCE\_BALANCE\_MASS.
}
\]

The Path-formal/weighted enrichment is not optional bookkeeping for this completion mechanism; it carries theorem-critical information.

## 6. Return Green and completion constant on the native multipath carrier

The #1161 return Green is

\[
G(s)=\sum_{n\ge0}c_ns^{2n}.
\]

The present construction shows that every finite coefficient `c_n` is the positive mass of a concrete finite native commuting-diamond provenance event.

The previously proved completion identities therefore become

\[
\Pi_*=\tau
=\left(\lim_{n\to\infty}n c_n\right)^{-1},
\]

where `c_n` is now realized directly by the native multipath enrichment rather than by an abstract binary walk.

Likewise the exact RG invariant

\[
G(s)/H
\]

is a derived completion of these finite native-path provenance masses.

## 7. Native-strength boundary

This result moves the branch carrier substantially closer to the current native path substrate, but it does not close all N0 obligations.

What is native/frozen input:

- the `(1,1)` commuting diamond and its two concrete path witnesses;
- typed translated concatenation;
- concrete path provenance at the Path-formal enrichment level;
- spatial recoalescence of the two witnesses.

What is newly layered/derived:

- the macroblock boundary tags;
- the two independent provenance channels;
- the balanced-count observer;
- equal positive rational branch weights;
- the infinite return Green completion.

Therefore the construction is best typed as

`NATIVE_MULTIPATH_CARRIER + N1/WEIGHTED_PROVENANCE_OBSERVER`,

not a proof that the full `G` function or the AGM scalar state is an N0 Cell primitive.

## 8. Strongest current conclusion

At free-research-result strength:

`c_n` no longer requires an external random-walk carrier.

It is exactly the balanced positive mass of two provenance channels built from repeated current-native commuting diamonds.

The completion identity

\[
\boxed{\Pi_*=\tau=(\lim n c_n)^{-1}}
\]

therefore has a direct finite native-multipath provenance realization coefficient by coefficient.

The remaining foundational question is whether the extra provenance observer/root/readout structure can itself be canonically descended to G0/N0 Cell data; current Boolean support cannot do so.
