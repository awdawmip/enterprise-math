# BRC Critical Primitive-Orbit Euler Product

Status: `RESEARCH CANDIDATE / MAIN-BACKED K-CARRIER / NOT YET FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-BRCPOE-20260903`
Parents: critical-degeneracy Foundation `WBRC-T39..T42` and main-backed critical multiplicity automaton PR #1173.

## 1. Scope and prior-art boundary

Let `K` be the non-negative integer critical-degeneracy matrix of an explicit positive-rational branch system. Interpret `K_ij` as the number of parallel tropical-critical dominant branch symbols from state `i` to state `j`.

Dynamical zeta functions, primitive periodic-orbit Euler products, Möbius inversion and shifts of finite type are classical/general mathematics. No generic novelty claim is made.

The BRC-specific content is the exact arithmetic routing from dominant branch ties to a primitive recurrent-circuit inventory, and its compatibility with the already canonical integer criticality polynomial/root-selector state.

## 2. Closed critical branch words

Define

\[
T_n=\operatorname{tr}(K^n),\qquad n\ge1.
\]

`T_n` is exactly the number of length-`n` **based closed critical dominant branch words** in the expanded multigraph: a starting state and every parallel dominant branch choice are distinguished.

A closed edge-word has primitive period `d|n` if it is the `n/d`-fold repetition of a primitive closed word of length `d`. Cyclic shifts of the same primitive closed word define one primitive periodic orbit.

Let

\[
P_n=\#\{\text{primitive periodic critical branch orbits of exact length }n\}.
\]

Then every primitive orbit of length `d` contributes its `d` choices of base point to `T_n` whenever `d|n`. Hence

\[
\boxed{T_n=\sum_{d\mid n}dP_d.}
\]

Möbius inversion gives

\[
\boxed{
P_n=\frac1n\sum_{d\mid n}\mu(d)T_{n/d}.
}
\]

Although the right side is written as a rational expression, the orbit interpretation proves

\[
\boxed{P_n\in\mathbf N_0.}
\]

## 3. Exact Euler product

The critical multiplicity zeta from the previous result is

\[
Z_{\rm crit}(z)=\frac1{\det(I-zK)}.
\]

Using

\[
\ln Z_{\rm crit}(z)=\sum_{n\ge1}\frac{T_n}{n}z^n
\]

and `T_n=sum_{d|n} d P_d`, reorganize formally:

\[
\begin{aligned}
\ln Z_{\rm crit}(z)
&=\sum_{d\ge1}P_d\sum_{k\ge1}\frac{z^{dk}}k\\
&=-\sum_{d\ge1}P_d\ln(1-z^d).
\end{aligned}
\]

Therefore

\[
\boxed{
Z_{\rm crit}(z)
=\prod_{d\ge1}(1-z^d)^{-P_d}.
}
\]

This is a formal identity. Every coefficient through `z^N` uses only the finite set `P_1,...,P_N`, so finite-order verification is exact integer arithmetic.

## 4. Primitive inventory determines the critical zeta

The sequences

\[
(T_n)_{n\ge1},\qquad(P_n)_{n\ge1},\qquad Z_{\rm crit}(z)
\]

are mutually equivalent exact recurrent observables:

- `K -> T_n` by traces;
- `T -> P` by Möbius inversion;
- `P -> T` by divisor sum;
- `T -> Z` by formal exponential;
- `P -> Z` by Euler product;
- `Z=1/p_K` is already finitely encoded by the integer polynomial `p_K(z)=det(I-zK)`.

Thus the infinite primitive-circuit inventory has a finite exact rational representation through `p_K`.

The smallest positive pole/root remains

\[
z_c=1/\rho(K),
\]

so the BRC residual critical multiplicity rate is

\[
\Gamma_{\rm crit}=-\ln z_c.
\]

No new spectral primitive is introduced.

## 5. Relation to earlier simple-circuit atoms

Do not identify `P_n` with the feedback Möbius circuit atoms of `WBRC-T29`.

- `WBRC-T29` concerns a **finite declared feedback-event support** and Möbius-primitive event subsets; a primitive atom is a simple directed support circuit.
- `P_n` concerns **periodic edge-words in the already condensed critical multiplicity automaton K**; primitive periodic orbits can revisit states and have arbitrary length.

The two constructions live at different semantic levels.

## 6. Gauge invariance

Positive rational vertex gauge leaves `K` exactly unchanged by the main-backed residual-entropy result. Therefore

\[
T_n',P_n',p_K',Z_{\rm crit}',z_c',\Gamma_{\rm crit}'
=
T_n,P_n,p_K,Z_{\rm crit},z_c,\Gamma_{\rm crit}
\]

for all `n`.

Thus the entire primitive orbit inventory is a gauge-invariant integer shadow of the explicit rational branch system.

## 7. Zero-correction case

If `Gamma_crit=0`, every nonzero critical SCC is a unit-multiplicity simple cycle. Then only finitely many primitive orbit lengths occur: exactly the lengths of those component cycles, with one primitive orbit per component of that length.

Conversely, if `Gamma_crit>0`, `rho(K)>1`; the Euler product has radius strictly below one and the primitive orbit inventory is infinite. In a recurrent integer critical graph this is the combinatorial source of positive residual multiplicity growth.

This gives a stronger qualitative distinction than merely `P_n>0` for some `n`: unit cycles have periodic closed words but no proliferation of new primitive recurrent branch orbits.

## 8. Examples

### Unit `r`-cycle

`K` is the permutation matrix of one directed `r`-cycle. Then

\[
T_n=\begin{cases}r,&r\mid n,\\0,&r\nmid n,\end{cases}
\]

and

\[
P_r=1,\qquad P_n=0\ (n\ne r).
\]

Hence

\[
Z_{\rm crit}(z)=\frac1{1-z^r}.
\]

### One-state `d`-fold tie

`K=[d]`. Then `T_n=d^n` and

\[
P_n=\frac1n\sum_{e\mid n}\mu(e)d^{n/e},
\]

which is the classical necklace count of primitive words on `d` symbols. The Euler product satisfies

\[
\frac1{1-dz}=\prod_{n\ge1}(1-z^n)^{-P_n}.
\]

### Branching `K=ones(2x2)`

`T_n=2^n`. Thus the primitive orbit inventory is again the binary primitive-necklace sequence, even though the branching arises from critical route combinatorics rather than parallel ties in one cell.

This illustrates that primitive critical circuits detect both local dominant ties and global critical-route branching.

## 9. Boundaries

Freeze:

```text
T_n = BASED_CLOSED_CRITICAL_BRANCH_WORD_COUNT
P_n = PRIMITIVE_PERIODIC_ORBIT_COUNT
T_n = SUM_{d|n} d P_d
Z_CRIT = PRODUCT_n (1-z^n)^(-P_n)
PRIMITIVE_PERIODIC_ORBIT != SIMPLE_SUPPORT_CIRCUIT
PRIMITIVE_ORBIT_EULER_PRODUCT = CLASSICAL_DYNAMICAL_ZETA_STRUCTURE
P_n != INTEGER_PRIME_COUNT
RATIONAL_GAUGE -> P_n_INVARIANT_EXACTLY
```

No claim is made that `P_n` are arithmetic primes, that the Euler product proves a new generic zeta theorem, or that a finite runtime can explicitly enumerate all primitive orbits at scale.

## 10. Validation plan

1. Exhaust all `2x2` and `3x3` critical-graph-shaped `K` with entries `{0,1,2}`.
2. Compute `T_n=tr(K^n)` for `n<=8`; Möbius-invert to `P_n` and verify every result is a non-negative integer.
3. Reconstruct every `T_n` from `P_d` by the divisor sum.
4. Compare the reciprocal-series coefficients of `1/det(I-zK)` through order 8 with the truncated Euler product built from `P_1,...,P_8`.
5. On selected small matrices, explicitly enumerate edge-labeled closed words modulo cyclic rotation and verify primitive orbit counts independently for `n<=6`.
6. Verify unit-cycle, one-state d-tie, branching, disjoint-class and golden-ratio examples.
7. Reuse rational gauge examples and verify the entire tested `P_n` prefix is unchanged.
