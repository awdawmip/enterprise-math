# Enterprise Math — Recurrent BRC Interaction Foundation Addendum

Status: `CANONICAL ALL-RESEARCH FOUNDATION ADDENDUM / MAIN-BACKED / FINITE-POSITIVE-RATIONAL`
Effective: `2026-09-03`
Parent foundations:
- `ENTERPRISE_BRC_WEIGHTED_LOG_FOUNDATION_20260902.md`;
- `ENTERPRISE_BRC_FINITE_RECURRENT_FOUNDATION_20260902.md`.
Theorem ledger: `ENTERPRISE_BRC_RECURRENT_INTERACTION_THEOREM_LEDGER_20260903.json`.

## 1. Foundation role

This addendum packages the main-backed recurrent/feedback BRC research from PRs #1130–#1147 into a reusable all-research layer.

It does **not** change canonical R023 Boolean support semantics. It extends the separately typed positive Weighted-BRC layer only when the declared problem actually contains finite non-negative rational recurrence, positive rational gauge/holonomy, or finite positive feedback-event updates.

The hot-start rule remains universal-but-lazy:

```text
RELEVANT FINITE RATIONAL RECURRENCE/FEEDBACK
-> LOAD THIS ADDENDUM / T17..T29 AS NEEDED

DETERMINISTIC OR SIGNED/AMPLITUDE PROBLEM
-> DO NOT FORCE THIS LAYER
```

## 2. Recurrent loop scalar

For stable

\[
W\in M_n(\mathbb Q_{\ge0}),
\qquad
S=(I-W)^{-1},
\]

define

\[
\boxed{Z_{\rm loop}(W)=\det S=\frac1{\det(I-W)}}
\]

and the derived readout

\[
\boxed{\Gamma(W)=\ln Z_{\rm loop}(W)=-\ln\det(I-W)}.
\]

The positive closed-walk expansion is

\[
\Gamma(W)=\sum_{k\ge1}\frac{\operatorname{tr}(W^k)}k.
\]

Consequences frozen at Foundation strength:

- positive diagonal state gauge leaves `Z_loop` and `Gamma` invariant;
- SCC block decomposition makes `Gamma` additive across cyclic diagonal blocks;
- feed-forward inter-SCC weights do not alter `Gamma`;
- `Gamma=0` iff the positive support is acyclic;
- for one state `W=[S]`, `Gamma=-ln(1-S)`.

Canonical ID: `WBRC-T17`.

## 3. Integer determinant/equal-slack synthesis

Choose a common denominator and write

\[
W=A/D,
\qquad
B=DI-A.
\]

On the stable phase let

\[
\delta=\det B>0,
\qquad
C=\operatorname{adj}(B).
\]

Then

\[
\boxed{h_0=C\mathbf1>0}
\]

and

\[
\boxed{Bh_0=\delta\mathbf1},
\qquad
\boxed{Ah_0=Dh_0-\delta\mathbf1}.
\]

Moreover

\[
\boxed{Z_{\rm loop}=D^n/\delta},
\qquad
\boxed{S\mathbf1=(D/\delta)h_0}.
\]

Thus the same integer determinant controls canonical equal slack and recurrent zeta denominator.

Canonical ID: `WBRC-T18`.

## 4. Edge response and recurrent response geometry

For an explicit positive branch

\[
e:a\to b,
\qquad q_e>0,
\]

define

\[
\boxed{R_e=\frac{\partial\Gamma}{\partial\ln q_e}=q_eS_{ba}}.
\]

Then

\[
R_e>0
\iff
e\text{ lies on a positive directed recurrent cycle}.
\]

For another branch `f:c->d`, the log-coordinate Hessian is

\[
\boxed{
H_{ef}
=\delta_{ef}R_e+q_eq_fS_{bc}S_{da}.
}
\]

It is exact rational, symmetric and PSD. On a strongly connected recurrent support its kernel is exactly the vertex-gauge coboundary space, so

\[
\operatorname{rank}H=|E|-|V|+1.
\]

The induced quadratic form is positive definite on the cycle/gauge quotient. Transient edges contribute zero response rows/columns.

Canonical IDs: `WBRC-T19`, `WBRC-T20`.

## 5. Exact criticality polynomial

Under uniform scale `W(t)=tW`, with `W=A/D`, define

\[
\boxed{p(t)=\det(DI-tA)\in\mathbb Z[t]}.
\]

If support is acyclic, `p(t)=D^n` and all non-negative scales remain stable. Otherwise the positive stability endpoint is the smallest positive real root of `p`.

At rational stable scales,

\[
\boxed{
\chi(t)
=-t\frac{p'(t)}{p(t)}
=\operatorname{tr}((I-tW)^{-1}-I)
}
\]

is exact rational. A rational stability potential gives an exact rational lower bound on the critical scale.

Canonical ID: `WBRC-T21`.

## 6. Positive-rational gauge lives in integer valuation coordinates

Unique factorization gives

\[
\mathbb Q_{>0}^{\times}\cong\bigoplus_p\mathbb Z.
\]

For rational vertex gauge

\[
q'_{uv}=q_{uv}\frac{h_v}{h_u},
\]

prime valuations transform by integer coboundaries. Hence

\[
\boxed{
H^1(G;\mathbb Q_{>0}^{\times})
\cong
\bigoplus_p H^1(G;\mathbb Z).
}
\]

For a fixed root and underlying spanning tree, there is a unique rational gauge with root scale `1` and every tree-edge weight `1`; the non-tree normalized rational weights are complete fundamental holonomy coordinates.

Logarithm is a derived faithful readout

\[
\ln q=\sum_p v_p(q)\ln p,
\]

not the primitive coordinate system.

Canonical ID: `WBRC-T22`.

## 7. Mod-m skeleton and rational thickness

For every positive rational `q` and integer `m>=2`, uniquely write

\[
\boxed{q=s_m(q)t_m(q)^m}
\]

where `s_m` is a positive m-power-free integer and `t_m` a positive rational.

For `m=2`, `s_2` is the squarefree/all-prime `C_2` parity skeleton and `t_2` is the even-valuation thickness.

This decomposition is exact before any root/log numerical readout. The ratio `q/s_m` is a rational perfect m-th power and may be verified/materialized through the existing BRC ROOT facade.

Skeleton alone does not determine recurrent phase; thickness remains necessary.

Canonical ID: `WBRC-T23`.

## 8. Finite determinant cycle polynomial

For explicit branch variables `x_e` and

\[
W_{ij}=\sum_{e:i\to j}x_e,
\]

set

\[
P_G(x)=\det(I-W(x)).
\]

It is multiaffine. Its nonzero monomials are indexed by vertex-disjoint directed cycle systems with coefficient

\[
(-1)^{\#\text{cycles}}.
\]

`P_G` is identically `1` iff support is acyclic, and every cycle-system monomial is vertex-gauge invariant. On the stable phase

\[
Z_{\rm loop}=1/P_G,
\qquad
\Gamma=-\ln P_G.
\]

For explicit edge `e`,

\[
R_e=-q_eP_e/P.
\]

Alternating determinant signs are inclusion-exclusion only; they are not signed/amplitude BRC mass.

Canonical ID: `WBRC-T24`.

## 9. Feedback-event condensation

Let `W` be a stable old background with star `S`. Insert positive events

\[
e_r:a_r\to b_r,
\qquad
\delta_r>0.
\]

Define the event-level feedback kernel

\[
\boxed{F_{rs}=S_{b_ra_s}\delta_s}.
\]

Then

\[
\boxed{
\widetilde W\text{ stable}
\iff
F\text{ stable}.
}
\]

On the stable phase,

\[
\boxed{
\widetilde S
=S+SUD(I-F)^{-1}V^\top S,
}
\]

\[
\boxed{
\det(I-\widetilde W)
=\det(I-W)\det(I-F),
}
\]

and

\[
\boxed{
\Gamma(\widetilde W)-\Gamma(W)=\Gamma(F).
}
\]

Original vertex gauge descends to positive diagonal similarity on event states.

Canonical ID: `WBRC-T25`.

## 10. Exact edge robustness

For one new edge `a->b`, let

\[
\kappa=S_{ba}.
\]

If `kappa=0`, the finite positive insertion radius is infinite. Otherwise

\[
\boxed{\delta_c=1/\kappa}
\]

and below criticality

\[
\Delta\Gamma=-\ln(1-\delta\kappa).
\]

For an existing explicit branch of weight `q` and response `R=qS_{ba}`, the gauge-invariant multiplicative critical factor is

\[
\boxed{\Lambda=1+1/R}.
\]

Deleting that branch changes loop surplus by

\[
\boxed{\ln(1+R)}.
\]

If `P=det(I-W)` and `P_e` is the explicit branch derivative,

\[
\delta_c=-P/P_e,
\qquad
\Lambda=1-P/(qP_e).
\]

At fixed mod-m skeleton `q=s_mt^m`, thickness scaling `t->mu t` remains stable while

\[
\mu^m<\Lambda.
\]

Canonical ID: `WBRC-T26`.

## 11. Modular/conditional feedback chain

Partition a one-shot feedback kernel as

\[
F=\begin{pmatrix}F_A&X\\Y&F_B\end{pmatrix}.
\]

If `F_A` is stable, after installing module `A`, module `B` sees

\[
\boxed{
F_{B\mid A}
=F_B+Y(I-F_A)^{-1}X.
}
\]

Final stability is equivalent to stability of `F_A` and `F_{B|A}`. The determinant chain is

\[
\boxed{
\det(I-F)
=\det(I-F_A)\det(I-F_{B\mid A}),
}
\]

hence

\[
\boxed{
\Delta\Gamma_{A\cup B}
=\Delta\Gamma_A+\Delta\Gamma_{B\mid A}.
}
\]

Repeated conditioning gives the same final star/determinant for every stable ordering, but stagewise attribution generally changes with order.

Canonical ID: `WBRC-T27`.

## 12. All-orders feedback interaction hierarchy

Fix a finite declared feedback-event universe `E` whose full update is stable. For `A subseteq E`, define

\[
G(A)=\Gamma(W_A)-\Gamma(W),
\qquad
Z(A)=e^{G(A)}\in\mathbb Q_{>0}.
\]

There are unique exact-support interactions

\[
\boxed{
G(A)=\sum_{\varnothing\ne T\subseteq A}\Phi_T,
\qquad
\Phi_T\ge0.
}
\]

Define exact rational factors

\[
\boxed{
J_T=e^{\Phi_T}
=\prod_{B\subseteq T}Z(B)^{(-1)^{|T|-|B|}}
\ge1.
}
\]

Then

\[
\boxed{
Z(A)=\prod_{\varnothing\ne T\subseteq A}J_T.
}
\]

`J_T>1` iff a positive closed event walk uses exactly the inserted-event set `T`.

Consequences:

- `G` is monotone and supermodular;
- conditional marginal risk only increases as positive feedback context grows;
- critical radii only shrink;
- group interaction factor is the product of all `J_T` crossing the group partition;
- pairwise interactions are not complete: pure higher-order recurrent cooperation can occur.

Canonical ID: `WBRC-T28`.

## 13. Circuit atoms and interaction girth

Call `T` Möbius-primitive when

\[
J_T>1
\]

and every proper nonempty interaction factor is `1`.

Then:

- `|T|=1`: one positive self-return;
- `|T|>=2`: induced event support is exactly one directed simple cycle.

If its rational circuit holonomy is

\[
Q_T=\prod_{\text{cycle}}F_{ij},
\]

then

\[
\boxed{J_T=1/(1-Q_T)},
\qquad
\boxed{\Phi_T=-\ln(1-Q_T)}.
\]

The first nonzero interaction order is exactly directed girth:

\[
\boxed{
\min\{|T|:J_T>1\}
=g_{\rm dir}(F).
}
\]

`Q_T` is vertex-gauge invariant and inherits the prime-valuation and skeleton/thickness coordinates above.

Canonical ID: `WBRC-T29`.

## 14. Critical negative boundaries

Freeze:

```text
FULL_RATIONAL_GAUGE_COHOMOLOGY != RECURRENT_GAMMA_RESPONSE_COMPLETENESS
DETERMINANT_ALTERNATING_SIGN != SIGNED_AMPLITUDE_BRC
PAIRWISE_FEEDBACK != COMPLETE_FEEDBACK_INTERACTION
CONDITIONAL_GAMMA_ATTRIBUTION != CANONICAL_COMPONENT_CREDIT
FINITE_POSITIVE_RATIONAL_INTERACTION != INFINITE_OR_SIGNED_OR_COMPLEX_RECURRENCE
```

A feed-forward diamond may carry nontrivial rational gauge cross-ratio while all recurrent loop observables vanish. A pure three-event circuit may have all singleton/pair interactions equal `1` while third-order interaction is positive.

Canonical negative IDs: `WBRC-N07…N11`.

## 15. Reusable tool surfaces

This addendum is implemented by three T0 subtool surfaces:

- `src/enterprise_math/brc_recurrent_invariants.py` — loop zeta, equal-slack integer certificate, response/radius/deletion/Hessian;
- `src/enterprise_math/brc_rational_holonomy.py` — prime valuations, mod-m skeleton/thickness, tree gauge normal form;
- `src/enterprise_math/brc_feedback.py` — event condensation, conditional kernels, subset zeta/Möbius factors and circuit atoms.

Exact `LN/ROOT` readouts continue to route through existing BRC arithmetic facades.

## 16. Prior-art boundary

Matrix determinant/logdet identities, Neumann series, M-matrix theory, Perron/Frobenius equivalences, Woodbury/Schur complements, graph zeta, directed cycles/girth, graph cohomology, unique factorization and finite-set Möbius inversion are classical mathematics.

Enterprise Math does not claim generic novelty for those ingredients.

The reusable project-specific synthesis is the typed exact chain

```text
positive Weighted-BRC recurrence
-> exact integer/rational stability
-> recurrent zeta/response
-> rational gauge holonomy
-> feedback-event condensation
-> all-orders exact interaction factors
-> circuit atoms / interaction girth
```

with explicit boundaries against Boolean-only, signed/amplitude and infinite-state interpretations.
