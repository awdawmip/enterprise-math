# Viète scalar versus oriented native state: trace suffices for the scalar seed, path history is necessary for the two-sheeted lift

Status: `FREE_RESEARCH / EXACT CURRENT-SEMANTICS STATE-MINIMALITY BOUNDARY / NOT_FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-FREE-7D3C9A / FREE_AXIOM_DISCOVERY`
Issue: `#1158`
Parent: `research_notes/VIETE_NATIVE_T11_TORSOR_NO_EUCLIDEAN_BISECTOR_20260903.md`

## 1. Three current native semantic levels

For the first equal-component Viète seed in one sector, current native line theory supplies three distinct objects:

1. terminal instantaneous Cell `C_{ij}(1,1)`;
2. native trace identity

\[
T_{1,1}^{(ij)}=[X_iX_j]=[X_jX_i]
\]

under the frozen component-preserving commutation;
3. the two-element realization fiber

\[
\operatorname{Realize}_E(T_{1,1})
=
\{\Sigma;X_iX_j,\;\Sigma;X_jX_i\}.
\]

These semantic levels deliberately retain different information.

## 2. Scalar first-half-angle state factors through the trace identity

The normalized Enterprise component observer on the trace is

\[
O_{\rm scalar}(T_{a,b})
=
\frac{(a,b)}{\sqrt{a^2+b^2}}.
\]

For `T_11`,

\[
O_{\rm scalar}(T_{1,1})
=
\frac{(1,1)}{\sqrt2}.
\]

Both path representatives have the same trace identity and therefore the same scalar readout.

Thus the first scalar Viète factor

\[
\frac{\sqrt2}{2}
\]

is completely determined at trace strength. No path-order bit is needed.

Freeze:

`FIRST_SCALAR_VIETE_SEED_FACTORS_THROUGH_T11_TRACE = true`.

## 3. Oriented two-sheeted seed cannot factor through the trace identity

The oriented quarter-root readout has two distinct sheets

\[
Q(h)=\{q_+,q_-\}.
\]

Suppose one tries to assign the two native path representatives to the two distinct sheets through a function that factors through the trace identity:

\[
\operatorname{Realize}_E(T_{1,1})
\xrightarrow{\pi}
\{T_{1,1}\}
\xrightarrow{\chi}
Q(h).
\]

Because both paths have the same image under `pi`, the composite `chi∘pi` is constant. It cannot map one path to `q_+` and the other to `q_-`.

Therefore

\[
\boxed{
\text{any oriented two-sheeted seed assignment distinguishing the two native paths cannot factor through native trace identity alone.}
}
\]

The same is a fortiori true for bare terminal Cell state, because the two paths also terminate at the same Cell.

## 4. Exact information lower bound

The realization fiber has cardinality two while both the trace quotient and terminal Cell forget the path-order distinction.

Therefore an oriented lift using this native seed carrier needs at least one binary distinction beyond the trace identity:

\[
\boxed{
\text{oriented seed information lower bound}=1\text{ bit relative to }T_{1,1}\text{ trace strength}.
}
\]

This bit need not be an invented primitive variable. The existing concrete path representative already carries it:

\[
X_iX_j\quad\text{versus}\quad X_jX_i.
\]

Equivalently, if one insists on storing only a trace identity, then one additional order/history bit is necessary to reconstruct which path sheet was taken.

Freeze:

`PATH_REPRESENTATIVE_OR_EQUIVALENT_ONE_BIT_HISTORY_REQUIRED_FOR_ORIENTED_T11_LIFT`.

## 5. Sufficiency at structural torsor strength

At pure set-with-involution strength, the two concrete path representatives are sufficient to realize a two-sheeted carrier:

\[
\tau(X_iX_j)=X_jX_i,
\]

with no fixed point.

The quarter-root set also has a free involution

\[
S(q_+)=q_-.
\]

Hence there exist exactly two equivariant bijections between them, differing by global chirality relabeling.

Thus one bit of retained path history is both:

- necessary to distinguish the two oriented sheets;
- sufficient to carry their abstract free-`C2` torsor structure.

What remains unproved is the physical/native interpretation of this abstract torsor matching.

## 6. Observer-relative minimality

Different precision observers therefore have genuinely different minimal native state requirements.

### Scalar observer

For any `S`-even observer such as longitudinal factor, absolute transverse residual, Viète product factor, or scalar `Pi_n`, the two oriented path sheets recoalesce:

\[
O(q_+)=O(q_-).
\]

At the first seed, trace identity `T_11` suffices.

### Oriented observer

For an `S`-odd observer such as signed transverse component, the two sheets differ. Trace identity is insufficient; path/history strength is necessary.

Therefore

\[
\boxed{
\text{MINIMUM_NATIVE_STATE depends on the declared observer.}
}
\]

This is a concrete example of observer-relative state minimality inside Enterprise precision semantics.

## 7. Consequence for later native-bridge design

The native bridge for #1158 should not ask for one universally “minimal” Cell/trace state without specifying which readout must be preserved.

The correct typed hierarchy is:

```text
scalar first-half-angle observer:
    T_11 trace identity is sufficient

oriented two-sheeted first-half-angle observer:
    T_11 path representative (or trace + one order bit) is necessary and structurally sufficient

transition-sensitive instantaneous orientation:
    bare terminal Cell is insufficient
```

A future bridge theorem must state its observer before claiming minimality.

## 8. Boundary

This result does not prove that the path-order distinction is physical chirality. It proves an information-theoretic/current-semantics statement:

- trace commutation intentionally erases exactly the distinction needed to separate the two candidate oriented sheets;
- retaining one of the two path representatives restores exactly one binary distinction;
- scalar even observers do not need that distinction.

Thus any eventual identification of path order with rotation chirality is a separate intertwining theorem, not a prerequisite for the scalar Viète mechanism.
