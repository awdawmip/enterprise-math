# BRC Feedback Möbius Interaction Hierarchy

Status: `RESEARCH CANDIDATE / EXACT FINITE-RATIONAL / NOT YET FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-BRCFB-93C7D1`
Parents: recurrent loop-zeta / response; PR #1142 feedback condensation; PR #1144 modular feedback condensation

## 1. Purpose

The feedback-condensation results show that positive recurrent risk is cooperative: adding an edge can make later edges more dangerous, and stagewise Gamma attribution depends on context/order.

This note identifies the exact all-orders structure behind that phenomenon.

The ingredients — positive closed-walk expansions, finite-set Möbius inversion, supermodularity/increasing differences, M-matrix/log-determinant theory — have substantial classical prior art. Related spectral-function supermodularity and M-matrix extensions exist in the literature. No generic novelty claim is made for those theories.

The Enterprise Math contribution claimed here is the exact BRC interface:

```text
stable background + finite declared feedback-event set
-> exact rational subset zeta factors Z(A)
-> nonnegative all-orders event-support interactions Phi_T
-> exact rational interaction factors J_T=exp(Phi_T)
-> conditional risk / modular Gamma factors as products of J_T
```

No floating logarithm is required in the exact layer.

## 2. Stable declared event universe

Let `W` be a stable finite non-negative rational background. Fix a finite set `E` of distinguishable positive inserted branch events, each with a fixed positive rational mass.

Assume the full update `W_E` is stable. Then every subset update `W_A`, `A subseteq E`, is stable by positivity/monotonicity.

Define

\[
G(A)=\Gamma(W_A)-\Gamma(W),
\]

and the exact rational relative loop-zeta factor

\[
\boxed{
Z(A)=\exp G(A)
=\frac{Z_{\rm loop}(W_A)}{Z_{\rm loop}(W)}
=\frac{\det(I-W)}{\det(I-W_A)}.
}
\]

Thus `Z(empty)=1` and every `Z(A)` is a positive rational.

By PR #1142, if `F_E` is the feedback-event kernel against the old background and `F_A` is its principal subkernel on `A`, then

\[
\boxed{Z(A)=\frac1{\det(I-F_A)}}.
\]

Hence all interaction calculations may be performed entirely at event level after the old background star has been condensed.

## 3. Positive closed-walk support decomposition

For every stable subset `A`,

\[
G(A)
=\sum_{k\ge1}\frac{\operatorname{tr}(W_A^k)-\operatorname{tr}(W^k)}k.
\]

Expand each trace term into positive weighted marked closed walks. Every walk surviving the subtraction uses at least one inserted event. Let

\[
\operatorname{supp}_E(\gamma)\subseteq A
\]

be the set of distinct inserted event labels used by the walk.

For each nonempty `T subseteq E`, define

\[
\boxed{
\Phi_T
=\sum_{k\ge1}\frac1k
\sum_{\substack{\gamma:\text{marked closed walk of length }k\\
\operatorname{supp}_E(\gamma)=T}}
\operatorname{wt}(\gamma).
}
\]

All terms are non-negative. Full stability gives absolute/monotone convergence, so grouping by the finite event support is legitimate.

Therefore

\[
\boxed{
G(A)=\sum_{\varnothing\ne T\subseteq A}\Phi_T,
\qquad
\Phi_T\ge0.
}
\]

This is the fundamental feedback-interaction decomposition.

## 4. Möbius inversion and exact rational interaction factors

Finite-set Möbius inversion gives

\[
\boxed{
\Phi_T
=\sum_{A\subseteq T}
(-1)^{|T|-|A|}G(A).
}
\]

Define

\[
\boxed{J_T=e^{\Phi_T}.}
\]

Because every `G(A)=ln Z(A)`, we have the exact no-log formula

\[
\boxed{
J_T
=
\prod_{A\subseteq T}
Z(A)^{(-1)^{|T|-|A|}}
\in\mathbb Q_{\ge1}.
}
\]

Only when an additive readout is requested do we materialize

\[
\Phi_T=\ln J_T
\]

through the existing exact BRC `LN` facade.

Conversely,

\[
\boxed{
Z(A)=
\prod_{\varnothing\ne T\subseteq A}J_T.
}
\]

Thus the complete subset zeta table and the complete interaction-factor table determine each other exactly.

## 5. Support criterion for a positive interaction

By construction,

\[
\Phi_T>0
\]

iff there exists a positive closed walk whose inserted-event support is exactly `T`.

Equivalently at the feedback-event-kernel level, the induced positive-support digraph on `T` admits a positive-length closed walk visiting every event in `T`.

For `|T|>=2`, this is equivalent to the induced event subgraph on `T` being strongly connected. For a singleton `T={e}`, positivity requires an event self-return `F_{ee}>0`.

Therefore `J_T>1` is an exact support-sensitive certificate that the events in `T` can participate together in a recurrent closed walk without requiring any other inserted event.

## 6. Supermodularity is a corollary

Let `A subseteq B subseteq E` and `e notin B`. The marginal loop surplus is

\[
G(A\cup\{e\})-G(A)
=
\sum_{\substack{T\subseteq A\cup\{e\}\\e\in T}}
\Phi_T.
\]

The corresponding marginal for `B` contains all of those non-negative terms plus possibly more. Hence

\[
\boxed{
G(A\cup\{e\})-G(A)
\le
G(B\cup\{e\})-G(B).
}
\]

So `G` is monotone and supermodular on every fully stable declared event universe.

The exact rational marginal zeta multiplier is

\[
\boxed{
M_e(A)
:=\frac{Z(A\cup\{e\})}{Z(A)}
=
\prod_{\substack{T\subseteq A\cup\{e\}\\e\in T}}J_T.
}
\]

It is non-decreasing as the installed context grows.

Using the updated star `S_A`, PR #1142 gives the equivalent single-edge form

\[
M_e(A)
=\frac1{1-\delta_e(S_A)_{b_ea_e}}.
\]

Thus the Möbius hierarchy and the conditional-return-mass formula are the same risk law in two coordinate systems.

## 7. Critical-radius monotonicity

Define the conditional additive radius

\[
r_e(A)=
\begin{cases}
1/(S_A)_{b_ea_e},&(S_A)_{b_ea_e}>0,\\
+\infty,&(S_A)_{b_ea_e}=0.
\end{cases}
\]

Positive feedback additions increase the star entrywise, so

\[
A\subseteq B
\quad\Longrightarrow\quad
\boxed{r_e(B)\le r_e(A).}
\]

Hence feedback can only consume future stability radius; it cannot create extra positive-mass robustness.

At exact rational points, the finite radii remain rational.

## 8. Pair interaction surplus

For two proposed events

\[
e:a_e\to b_e,\qquad f:a_f\to b_f
\]

with masses `delta_e,delta_f`, use the old background star `S` and write the two-event kernel as

\[
F_{ef}=\begin{pmatrix}
a&b\\c&d
\end{pmatrix}
\]

with

\[
a=\delta_eS_{b_ea_e},
\quad
b=\delta_fS_{b_ea_f},
\quad
c=\delta_eS_{b_fa_e},
\quad
d=\delta_fS_{b_fa_f}.
\]

Assume the pair update is stable. Then

\[
Z(\{e\})=\frac1{1-a},
\qquad
Z(\{f\})=\frac1{1-d},
\]

and

\[
Z(\{e,f\})
=\frac1{(1-a)(1-d)-bc}.
\]

Therefore the exact pair interaction factor is

\[
\boxed{
J_{ef}
=\frac{(1-a)(1-d)}{(1-a)(1-d)-bc}
=\frac1{1-\dfrac{bc}{(1-a)(1-d)}}
\ge1.
}
\]

The additive interaction surplus is

\[
\Phi_{ef}=\ln J_{ef}.
\]

Strict interaction occurs exactly when

\[
\boxed{bc>0},
\]

i.e. when the background permits both cross transfers

\[
b_e\leadsto a_f,
\qquad
b_f\leadsto a_e.
\]

This is precisely the condition that the two inserted events can close a recurrent event-level 2-cycle together.

## 9. Pair interaction equals conditional risk amplification

After inserting `e`, the conditional one-step self-return mass of event `f` is

\[
d_{f\mid e}
=d+\frac{bc}{1-a}.
\]

Therefore

\[
\boxed{
J_{ef}
=\frac{1-d}{1-d_{f\mid e}}
=\frac{M_f(\{e\})}{M_f(\varnothing)}.
}
\]

So pair interaction is exactly the factor by which installing `e` amplifies the zeta-risk multiplier of `f`.

This equality makes the supermodular interpretation operational rather than merely combinatorial.

## 10. Pure cooperative pair

If both events are individually harmless,

\[
a=d=0,
\]

but mutually close a feedback cycle (`bc>0`), then

\[
\boxed{
J_{ef}=\frac1{1-bc},
\qquad
\Phi_{ef}=-\ln(1-bc).
}
\]

This is the PR #1142 cooperative-feedback phenomenon in pure interaction coordinates: all singleton surplus vanishes and the entire recurrent burden appears at order two.

## 11. Pairwise analysis is still incomplete: pure third-order feedback

Consider three inserted events with feedback-event kernel

\[
F=\begin{pmatrix}
0&x&0\\
0&0&y\\
z&0&0
\end{pmatrix},
\qquad xyz<1.
\]

Every singleton and every two-event principal subkernel is acyclic/nilpotent, hence

\[
J_{\{i\}}=1,
\qquad
J_{\{i,j\}}=1.
\]

But the three events form a directed feedback cycle, so

\[
\det(I-F)=1-xyz
\]

and

\[
\boxed{
J_{\{1,2,3\}}
=\frac1{1-xyz}>1.
}
\]

Thus all pairwise interactions may vanish while a genuine third-order feedback interaction is positive.

A pairwise interaction graph is therefore not a complete recurrent-risk representation.

## 12. Full-graph realization of pure third-order feedback

The previous event kernel is realized by a six-state DAG background:

old background edges

\[
1\to2\text{ of mass }u,
\qquad
3\to4\text{ of mass }v,
\qquad
5\to0\text{ of mass }w,
\]

and inserted events

\[
e_1:0\to1\text{ of mass }\delta_1,
\quad
e_2:2\to3\text{ of mass }\delta_2,
\quad
e_3:4\to5\text{ of mass }\delta_3.
\]

The feedback kernel is

\[
F=\begin{pmatrix}
0&u\delta_2&0\\
0&0&v\delta_3\\
w\delta_1&0&0
\end{pmatrix}.
\]

Every one- or two-event insertion remains feed-forward, but all three together create the first recurrent loop. The phase condition is

\[
\boxed{uvw\delta_1\delta_2\delta_3<1}.
\]

The entire loop surplus is the third-order interaction

\[
\boxed{
\Phi_{123}
=-\ln(1-uvw\delta_1\delta_2\delta_3).
}
\]

## 13. Group interaction factor

For disjoint event groups `A,B` with stable union, define

\[
\Phi(A;B)
:=G(A\cup B)-G(A)-G(B).
\]

Then

\[
\boxed{
\Phi(A;B)
=
\sum_{\substack{\varnothing\ne T\subseteq A\cup B\\
T\cap A\ne\varnothing,\ T\cap B\ne\varnothing}}
\Phi_T
\ge0.
}
\]

Its exact rational factor is

\[
\boxed{
J(A;B)
=\frac{Z(A\cup B)}{Z(A)Z(B)}
=\prod_{T\text{ crossing }A|B}J_T
\ge1.
}
\]

By PR #1144,

\[
\boxed{
J(A;B)
=\frac{Z(B\mid A)}{Z(B)},
}
\]

so group interaction is exactly the multiplicative risk amplification of B caused by installing A first.

## 14. Exact interaction reconstruction of conditional attribution

For an ordered insertion sequence `e_1,...,e_m`, the stage multiplier at step `j` is

\[
M_{e_j}(\{e_1,\ldots,e_{j-1}\})
=\prod_{\substack{T\subseteq\{e_1,\ldots,e_j\}\\e_j\in T}}J_T.
\]

Therefore each exact interaction factor `J_T` appears for the first time precisely when the **last member of T** is inserted.

Different orderings assign the same `J_T` to different stages, explaining why the PR #1144 stagewise Gamma decomposition is order dependent while the total is invariant.

This gives a complete exact account of attribution nonuniqueness.

## 15. Relation to determinant cycle-interaction polynomial

PR #1134 gave a finite alternating determinant polynomial over vertex-disjoint directed cycle systems. The present hierarchy is different:

- determinant polynomial: finite, alternating, exclusion/cycle-system certificate;
- `Gamma=-ln det`: infinite positive closed-walk closure;
- feedback Möbius interactions: positive closed-walk closure grouped by **exact inserted-event support**.

Thus the Möbius hierarchy sits between raw infinite closed walks and a single scalar Gamma, preserving exactly which declared feedback events must cooperate.

The alternating determinant sign remains inclusion-exclusion, not signed/amplitude BRC mass.

## 16. Prior-art boundary

Finite-set Möbius inversion, belief/capacity transforms, positive closed-walk expansions, log-determinant identities, M-matrix monotonicity and supermodular spectral-function theory are classical/general mathematics.

No generic novelty claim is made for those ingredients.

The project-specific result is the typed exact-rational BRC synthesis:

```text
feedback-event condensation
-> rational subset zeta factors Z(A)
-> rational all-order interaction factors J_T >= 1
-> LN readout Phi_T
-> conditional risk / critical-radius monotonicity
-> pure higher-order recurrent cooperation
```

## 17. Boundaries

This candidate does not claim:

- signed/amplitude interaction semantics;
- that pairwise interactions determine higher-order feedback;
- that `Phi_T` is additive over ordinary graph edges;
- a unique intrinsic allocation of `Gamma` to events;
- an infinite event universe or infinite-state theorem;
- that every standard notion called complete monotonicity uses the same sign convention as this note;
- novelty of generic supermodularity or Möbius inversion.

## 18. Validation plan

Use exact rational arithmetic only.

1. Exhaust all stable `3x3` event kernels with entries in `{0,1/10,1/5}` and compute `Z(A)` for all subsets.
2. Möbius-transform every nonempty subset and verify every rational `J_T>=1`.
3. Verify `Z(A)=product_{T subseteq A,T nonempty} J_T` exactly.
4. Verify `J_T>1` iff the induced event-support subgraph admits a closed walk visiting every T (singleton handled by self-loop).
5. Verify all supermodular marginal inequalities on every full-stable kernel.
6. Verify the pair closed formula and strictness iff mutual cross transfer exists.
7. Verify group interaction factors equal both crossing-interaction products and modular conditional-risk amplification.
8. Verify the pure 3-cycle has all singleton/pair factors 1 and only the third-order factor `1/(1-xyz)` positive.
9. Realize the same pure third-order effect in the six-state DAG background.
10. Verify conditional critical radii never increase as positive event subsets grow.

A dedicated research CI gate must pass before any Foundation backflow.
