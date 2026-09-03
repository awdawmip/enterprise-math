# Free Research #1161 — one commuting-diamond ensemble unifies `P_n` and the completion constant

Status: `FREE_RESEARCH_RESULT / NATIVE-MULTIPATH UNIFICATION / NOT WORKING_TRUTH / NOT FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-FREE-G61R8`
Parent issue: `#1161`

## 1. One repeated native diamond process

Use the frozen `(1,1)` commuting diamond with two concrete native path witnesses

\[
\alpha=X_iX_j,
\qquad
\beta=X_jX_i.
\]

Repeat this translated macroblock `m` times and retain the macroblock path provenance.

The history set is

\[
\Omega_m=\{\alpha,\beta\}^m.
\]

Every macroblock ends at the same translated terminal cell regardless of whether `alpha` or `beta` was chosen. Hence the process spatially recoalesces after each block while preserving path provenance.

## 2. Raw branch growth is exactly the Gauss–Legendre `P_m`

The raw history count is

\[
D_m:=|\Omega_m|=2^m.
\]

The Gauss–Legendre multiplier obeys

\[
P_0=1,
\qquad
P_{m+1}=2P_m,
\]

so

\[
\boxed{P_m=D_m=2^m.}
\]

Thus `P_m` need not be treated as an externally inserted doubling counter. It is the raw multiplicity of the repeated native commuting-diamond provenance ensemble.

## 3. Central provenance shell

At even depth `m=2n`, define the central shell

\[
\mathcal B_n
=
\{\omega\in\Omega_{2n}:\#\alpha(\omega)=\#\beta(\omega)=n\}.
\]

Its cardinality is

\[
B_n:=|\mathcal B_n|=\binom{2n}{n}.
\]

Normalize by the raw history count

\[
p_n:=\frac{B_n}{D_{2n}}
=
\frac{\binom{2n}{n}}{2^{2n}}.
\]

This is a derived normalized multiplicity/concentration readout of the same native path ensemble.

The #1161 return coefficient is exactly

\[
\boxed{
c_n=p_n^2.}
\]

No second physical trajectory is required: the square may be taken as an ordinary scalar readout of the one-channel central concentration. A two-copy interpretation is optional, not foundational.

## 4. The completion constant is the inverse squared central concentration density

The already proved internal completion result is

\[
\Pi_*=\tau
=\left(\lim_{n\to\infty}n c_n\right)^{-1}.
\]

Substituting `c_n=p_n^2` gives

\[
\boxed{
\Pi_*
=\tau
=\left[
\lim_{n\to\infty}
 n\left(\frac{B_n}{P_{2n}}\right)^2
\right]^{-1}.
}
\]

Thus the same native diamond ensemble supplies:

- **raw branch growth** `P_m`;
- **central provenance concentration** `B_n/P_{2n}`;
- the global completion normalization through the asymptotic squared central concentration.

## 5. #1159 Wallis ratio on the same ensemble

The exact finite relation

\[
W_n=\frac1{(2n+1)c_n}
\]

becomes

\[
\boxed{
W_n
=
\frac{P_{2n}^2}{(2n+1)B_n^2}.
}
\]

Therefore the #1159 finite parity-sector determinant ratio is also an exact raw-versus-central statistic of the same repeated diamond history counts once the #1161 bridge is used.

This gives a direct finite integer bridge among

1. #1161 raw multiplier `P`;
2. #1161 central provenance shell;
3. #1159 Wallis determinant ratio.

## 6. Defect budget versus completion concentration

The Gauss–Legendre retired defect mass is

\[
\delta_n=P_nU_n^2.
\]

With the present interpretation,

\[
\boxed{
\delta_n
=\text{raw diamond-history multiplicity at depth }n
\times
\text{local squared cone defect}.
}
\]

By contrast, the global completion constant is determined by the central concentration at doubled history depth:

\[
\boxed{
\Pi_*^{-1}
=
\lim_n n(B_n/P_{2n})^2.
}
\]

This separates two complementary statistics of one ensemble:

`RAW_GROWTH -> LOCAL_DEFECT_BUDGET`,

`CENTRAL_CONCENTRATION -> GLOBAL_COMPLETION_NORMALIZATION`.

The common source is the repeated native commuting diamond.

## 7. Information typing

Spatially, every macroblock recoalesces. If the trajectory is projected to Boolean terminal support after each block, both `P_m` and `B_n` are erased.

The theorem-critical state therefore lives at a provenance/multiplicity enrichment:

\[
\boxed{
SPATIAL_RECOALESCENCE
\neq
PROVENANCE/MULTIPLICITY_ERASURE.
}
\]

Flattening the macroblock language to the complete trace fiber also changes the branch count, so the block decomposition must remain typed until the relevant readout is taken.

## 8. Native-strength boundary

The primitive path witnesses and translated diamond concatenation are current native/multipath structures. The following remain layered:

- declaration of the repeated diamond process as the dynamics under study;
- provenance-count shell observer;
- normalization by total branch multiplicity;
- asymptotic central-concentration completion.

Hence this is a strong native-multipath/N1 bridge, not an N0 claim that a Cell alone stores the completion constant.

## 9. Strongest current interpretation

At free-research-result strength:

\[
\boxed{
\text{Gauss--Legendre }P_n
\text{ and }\Pi_*
\text{ are dual statistics of one repeated native commuting-diamond ensemble.}
}
\]

`P_n` is raw branch growth; `Pi_*` is inverse asymptotic squared central provenance concentration; `delta_n=P_nU_n^2` couples the raw branch count to the local chord/cone defect.

This provides the most unified current discrete interpretation of the algorithm's multiplicity and completion channels.
