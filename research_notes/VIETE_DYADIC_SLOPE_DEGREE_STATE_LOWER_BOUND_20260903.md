# Viète dyadic slope degree doubling and stationary rational precision-state lower bound

Status: `FREE_RESEARCH / EXACT_FINITE-CYCLOTOMIC DEGREE THEOREM + CONDITIONAL STATE-DIMENSION LOWER BOUND / NOT_FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-FREE-7D3C9A / FREE_AXIOM_DISCOVERY`
Issue: `#1158`
Parent: `research_notes/VIETE_ENTERPRISE_J_TRACE_PELL_PRECISION_20260903.md`

## 1. Question

The previous note found:

- the first post-seed half-angle direction is exactly the normalized native trace `T_11`;
- the next ideal direction has slope `sqrt(2)-1`, algebraic degree two, and admits a stationary 2x2 integer Pell-type precision recurrence;
- one further half-angle has a degree-four slope and cannot be an isolated fixed point of a stationary rational Möbius recurrence.

This note proves the general algebraic-degree law for every dyadic half-angle depth and converts it into a lower bound for a broad class of stationary rational/integer projective precision engines.

## 2. Finite group indexing without using continuous pi

Start with the candidate coarse orientation state chain

\[
C_6\hookrightarrow C_{12}\hookrightarrow C_{24}\hookrightarrow C_{48}\hookrightarrow\cdots.
\]

The `C3` factor records the coarse three-ray structure. The Viète square-root chain after the quarter-turn seed lives in the 2-primary subcycle.

At post-seed depth `n>=1`, the ambient cyclic resolution group has order

\[
12\,2^n=3\cdot2^{n+2}.
\]

Choose a character and let `u_n` be a state of exact order

\[
2^{n+2}
\]

inside that ambient group. Its square

\[
zeta_n:=u_n^2
\]

has exact order

\[
2^{n+1}.
\]

Thus the algebraic degree calculation below is a theorem about finite roots of unity and does not need a real angle or the numerical value of `pi` as input.

## 3. Cayley slope coordinate

For `n>=1`, define the real Cayley slope coordinate

\[
\boxed{
\tau_n=-i\,\frac{\zeta_n-1}{\zeta_n+1}
}
\]

where `i` is the order-four algebraic unit contained in the same 2-power cyclotomic field.

In the classical analytic completion this becomes the familiar slope of the `n`th post-quarter-turn half-angle, but that interpretation is not used in the degree proof.

Solving for `zeta_n` gives

\[
\boxed{
\zeta_n=\frac{1+i\tau_n}{1-i\tau_n}.
}
\]

Therefore

\[
\mathbb Q(\zeta_n)=\mathbb Q(i,\tau_n).
\]

## 4. Exact degree-doubling theorem

Because `zeta_n` is a primitive `2^{n+1}`-th root of unity,

\[
[\mathbb Q(\zeta_n):\mathbb Q]
=\varphi(2^{n+1})
=2^n.
\]

The slope `tau_n` is real, so

\[
\mathbb Q(\tau_n)\subset\mathbb R.
\]

Hence `i` is not in `Q(tau_n)`, and adjoining `i` has degree exactly two:

\[
[\mathbb Q(i,\tau_n):\mathbb Q(\tau_n)]=2.
\]

Using

\[
\mathbb Q(i,\tau_n)=\mathbb Q(\zeta_n),
\]

we obtain

\[
2^n
=
[\mathbb Q(\zeta_n):\mathbb Q]
=
2\,[\mathbb Q(\tau_n):\mathbb Q].
\]

Therefore

\[
\boxed{
[\mathbb Q(\tau_n):\mathbb Q]=2^{n-1}.
}
\]

So every additional post-seed half-angle exactly doubles the algebraic degree of the ideal slope.

Examples:

- `n=1`: degree `1`; the slope is rational and is exactly represented by `T_11`;
- `n=2`: degree `2`; this is the `sqrt(2)-1` Pell layer;
- `n=3`: degree `4`; this is the quartic layer found in the predecessor;
- `n=4`: degree `8`;
- and so on.

Freeze:

`VIETE_IDEAL_SLOPE_DEGREE(n)=2^(n-1)` for the finite cyclotomic readout defined above.

## 5. Relation to the nested-radical tower

The degree law is the field-theoretic shadow of the nested square-root chain. Each dyadic refinement adjoins a new square-root layer to the real orientation coordinate.

The important typing is:

`DYADIC_STATE_RESOLUTION_DOUBLING -> REAL_SLOPE_FIELD_DEGREE_DOUBLING`.

The coarse three-ray `C3` factor is needed to motivate the `C6` orientation seed but does not contribute to the subsequent 2-primary degree growth.

Thus the Viète radical depth is not merely a count of written square-root symbols; it records an exact exponential growth in the algebraic information needed to specify the ideal orientation over `Q`.

## 6. Stationary rational projective-linear precision engine

Consider a stationary precision engine with rational state matrix

\[
M\in\operatorname{Mat}_m(\mathbb Q).
\]

Assume:

1. `M` has a simple real eigenvalue `lambda` whose projective eigendirection is the attracting precision state under consideration;
2. an eigenvector `v` for `lambda` has a coordinate ratio equal to the target ideal slope `tau_n`;
3. the target ratio is read directly from that stationary projective fixed direction.

Because the eigenspace is one-dimensional, row reduction of

\[
(M-\lambda I)v=0
\]

over `Q(lambda)` allows `v` to be chosen with coordinate ratios in `Q(lambda)`.

Therefore

\[
\tau_n\in\mathbb Q(\lambda).
\]

Hence

\[
[\mathbb Q(\tau_n):\mathbb Q]
\le
[\mathbb Q(\lambda):\mathbb Q].
\]

But the minimal polynomial of `lambda` divides the characteristic polynomial of the `m x m` rational matrix, so

\[
[\mathbb Q(\lambda):\mathbb Q]\le m.
\]

Combining with the degree theorem gives

\[
\boxed{
m\ge2^{n-1}.
}
\]

Thus any stationary rational/integer **linear projective** precision engine whose attracting fixed direction directly encodes the exact `n`th ideal Viète slope needs state dimension at least exponential in the half-angle depth.

## 7. Pell recurrence is dimension-minimal at n=2

For `n=2`,

\[
[\mathbb Q(\tau_2):\mathbb Q]=2.
\]

The predecessor constructed the exact integer matrix

\[
M_2=
\begin{pmatrix}
2&1\\
1&0
\end{pmatrix}
\]

whose projective recurrence on `x=b/a` is

\[
x\mapsto\frac1{2+x}
\]

and whose attracting fixed direction is `tau_2=sqrt(2)-1`.

Therefore the lower bound `m>=2` is achieved exactly:

\[
\boxed{
\text{the Pell trace precision engine is stationary-linear dimension-minimal at the first irrational Viète layer.}
}
\]

At `n=3`, the lower bound jumps to

\[
m\ge4,
\]

which strictly strengthens the predecessor's Möbius-only no-go.

## 8. What the lower bound does and does not forbid

The theorem is deliberately scoped.

It forbids keeping **all** of the following simultaneously at arbitrary depth:

- stationary update rule;
- rational/integer linear state evolution;
- projective fixed-direction decoding;
- fixed small state dimension;
- exact ideal Viète slope as the limiting direction.

It does **not** forbid:

- nonstationary 2D continued-fraction-like recurrences whose coefficients change with depth;
- nonlinear rational recurrences with higher-degree fixed equations;
- algebraic-coefficient state updates;
- approximate rather than exact target directions;
- larger relational state;
- direct branch/algebraic readout without integer rationalization.

Thus the result is a native-precision complexity boundary, not a claim that deep Viète refinement is impossible.

## 9. Consequence for line-segment rotation precision

The previous note already separated two precision coordinates:

- `DYADIC_DEPTH` — ideal orientation half-angle depth;
- `TRACE_SCALE` — size of an integer trace approximating that ideal direction.

The new theorem adds a third structural coordinate:

- `PRECISION_STATE_DIMENSION` — amount of stationary rational relational state needed to make the ideal direction an exact projective attractor.

For stationary rational linear engines,

\[
\boxed{
\text{required state dimension grows at least as }2^{n-1}.
}
\]

This means that “increase precision by one half-angle level” is not just “use bigger integers.” At exact stationary native-rational strength, each level can require qualitatively more relational state.

This is a concrete realization of the broader Enterprise principle that finite precision is endogenous to the ontology/state description rather than a post-hoc decimal setting.

## 10. New frontier

The next useful discrimination is now between two possible native precision architectures:

1. `GROWING_STATE` — keep a stationary integer/rational update law but let the relational state dimension grow with dyadic depth;
2. `NONSTATIONARY_LOW_STATE` — keep low-dimensional integer traces but allow the refinement/update coefficients to vary with depth.

A third route is to stop forcing exact ideal orientation into native integer traces and treat the nested-radical state as the G1 algebraic readout of a discrete Cell trajectory.

Determining which of these is actually induced by Enterprise Cell rotation dynamics remains open.
