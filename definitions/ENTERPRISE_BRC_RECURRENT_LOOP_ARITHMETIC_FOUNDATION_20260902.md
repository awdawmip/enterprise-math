# Enterprise Math — Recurrent Loop Arithmetic Foundation Addendum

Status: `CANONICAL ALL-RESEARCH FOUNDATION ADDENDUM / MAIN-BACKED / EXACT RATIONAL-INTEGER`
Effective: `2026-09-02`
Parent: `ENTERPRISE_BRC_FINITE_RECURRENT_FOUNDATION_20260902.md`
Theorem interface: `ENTERPRISE_BRC_RECURRENT_LOOP_THEOREM_LEDGER_20260902.json`

Main-backed evidence:

- PR #1130 / `edfbeacb13d1fa741c76cd7a6db328bd1b324ad3` — determinant / loop-zeta surplus;
- PR #1131 / `86f42d9ebd06dc86ad262ab794ce64cd67517b7f` — edge response, Hessian, criticality polynomial;
- PR #1132 / `4f6761bbb5fb5b256d856cbfd25958483ebc1d72` — prime-valuation rational gauge classification;
- PR #1133 / `3a6bb471a10fd8673483ea5163687ce850bba9bb` — parity skeleton / rational thickness;
- PR #1134 / `6f8f53230f6e36e0b55c873a72052176dd40b673` — finite cycle-interaction polynomial.

## 1. Scope

This addendum is available to all Enterprise Math research modes under the existing universal-but-lazy Weighted-BRC rule.

It applies when the declared object contains finite positive-rational branch weights, rational vertex gauge, finite recurrent total-mass structure, or exact cycle-holonomy arithmetic.

It does **not** change the canonical Boolean R023 base and does not import signed/amplitude semantics.

Freeze:

```text
POSITIVE_RATIONAL_RECURRENCE -> EXACT LOOP ARITHMETIC AVAILABLE
RATIONAL_VERTEX_GAUGE -> PRIME_VALUATION INTEGER COORDINATES AVAILABLE
LOG / DET READOUTS = DERIVED, NOT PRIMITIVE NATIVE STATE
DETERMINANT SIGNS != SIGNED BRC BRANCHES
C2 / MOD-m SHADOW != FULL POSITIVE RATIONAL STATE
```

## 2. Exact loop-zeta carrier

For a stable finite non-negative rational transition-mass matrix

\[
W\in M_n(\mathbb Q_{\ge0}),
\]

define

\[
\boxed{Z_{\rm loop}(W)=\det(I-W)^{-1}}
\]

and the derived logarithmic loop surplus

\[
\boxed{\Gamma(W)=\ln Z_{\rm loop}(W)=-\ln\det(I-W).}
\]

By `WBRC-T14`,

\[
W^\star=(I-W)^{-1},
\]

so

\[
\boxed{Z_{\rm loop}(W)=\det(W^\star).}
\]

If `W=A/D` with `A` non-negative integer and

\[
B=DI-A,
\]

then

\[
\boxed{Z_{\rm loop}(W)=D^n/\det(B).}
\]

Thus `Gamma` can be materialized through the existing exact BRC `DIV -> LN` path without floating determinant or spectral evaluation.

## 3. Determinant equal-slack potential

On the stable phase, put

\[
\delta=\det(B)>0,
\qquad
C=\operatorname{adj}(B).
\]

Then

\[
\boxed{h_0=C\mathbf1\in\mathbb N_{>0}^n}
\]

and

\[
\boxed{Bh_0=\delta\mathbf1.}
\]

Equivalently,

\[
Ah_0=Dh_0-\delta\mathbf1.
\]

The same determinant integer `delta` is therefore:

- the uniform absolute slack of the adjugate integer stability ray;
- the denominator factor of the exact loop-zeta ratio `D^n/delta`.

The canonical rational potential is

\[
\boxed{x=W^\star\mathbf1=(D/\delta)h_0.}
\]

If `h_0` is divided by its coordinate gcd, the resulting primitive integer certificate remains on the same ray but need not retain slack `delta` itself.

## 4. Closed-walk and primitive-loop meaning

Stable positive recurrence satisfies the classical trace/log-determinant identity

\[
\boxed{
\Gamma(W)=\sum_{k\ge1}\frac{\operatorname{tr}(W^k)}k.
}
\]

By `WBRC-T12`, `tr(W^k)` is the exact total positive mass of length-`k` closed walks with marked starting state.

The standard directed graph-zeta reorganization gives the classical primitive-loop product

\[
Z_{\rm loop}
=\prod_{[p]\ \mathrm{primitive}}(1-w(p))^{-1}.
\]

These graph-zeta identities are prior mathematics. Their Foundation role here is typed BRC interpretation, not novelty.

The one-state law reduces exactly to

\[
Z=(1-S)^{-1},
\qquad
\Gamma=-\ln(1-S).
\]

A simple directed cycle with product `Q` has

\[
Z=(1-Q)^{-1},
\qquad
\Gamma=-\ln(1-Q).
\]

## 5. Gauge invariance, SCC additivity and DAG zero law

For positive diagonal `H`,

\[
W'=H^{-1}WH
\]

implies

\[
\det(I-W')=\det(I-W).
\]

Therefore `Z_loop` and `Gamma` are gauge invariant.

After SCC block ordering,

\[
\boxed{
\Gamma(W)=\sum_a\Gamma(W_a),
\qquad
Z_{\rm loop}(W)=\prod_aZ_{\rm loop}(W_a).
}
\]

Feed-forward inter-SCC weights do not enter this recurrent scalar.

For stable non-negative weights,

\[
\boxed{
\Gamma(W)=0
\iff
\text{the positive-support digraph is acyclic}.
}
\]

Thus `Gamma` is a pure recurrent gauge invariant, whereas the canonical state potential remains transient-sensitive.

## 6. Exact edge-loop response

For explicit positive branch edge

\[
e:a\to b
\]

with weight `q_e`, define formal log coordinate `theta_e=ln q_e` only as a derived readout coordinate.

Let

\[
S=(I-W)^{-1}.
\]

Then

\[
\boxed{
R_e:=\frac{\partial\Gamma}{\partial\theta_e}
=q_eS_{ba}.
}
\]

`R_e` is exact rational and equals the total positive mass of closed walks with one distinguished occurrence of edge `e`.

It is individually gauge invariant and

\[
\boxed{
R_e>0
\iff
e\text{ lies on a directed cycle}.
}
\]

Hence its support is exactly the recurrent edge core.

The total recurrent susceptibility is

\[
\boxed{
\chi(W)=\sum_eR_e
=\operatorname{tr}(S-I)
=\sum_{k\ge1}\operatorname{tr}(W^k).
}
\]

## 7. Recurrent loop-response Hessian

For

\[
e:a\to b,
\qquad
f:c\to d,
\]

define

\[
H_{ef}=\frac{\partial^2\Gamma}{\partial\theta_e\partial\theta_f}.
\]

Then

\[
\boxed{
H_{ef}
=\delta_{ef}q_eS_{ba}
+q_eq_fS_{bc}S_{da}.
}
\]

`H` is symmetric, rational and positive semidefinite.

On a strongly connected recurrent support graph,

\[
\boxed{
\ker H=\operatorname{im}(d:C^0\to C^1),
}
\]

so for `m=|E|`, `n=|V|`,

\[
\boxed{\operatorname{rank}H=m-n+1.}
\]

Therefore `H` descends to a positive definite exact-rational quadratic form on the recurrent cycle/gauge quotient.

For a general graph, transient edges have zero Hessian rows/columns and cyclic SCCs split as independent response blocks.

## 8. Integer response certificate

Choose a common edge denominator `D` and write

\[
q_e=a_e/D,
\qquad
B=DI-A,
\qquad
\delta=\det B,
\qquad
C=\operatorname{adj}(B).
\]

Then

\[
\boxed{R_e=a_eC_{ba}/\delta.}
\]

For `e:a->b`, `f:c->d`,

\[
\boxed{
H_{ef}
=\frac{
\delta_{ef}a_eC_{ba}\delta
+a_ea_fC_{bc}C_{da}
}{\delta^2}.
}
\]

Thus the complete first/second loop-response geometry has a symmetric integer numerator certificate controlled by the same determinant slack as the stability and zeta layers.

## 9. Exact uniform criticality polynomial

For rational `W=A/D`, define

\[
\boxed{p(t)=\det(DI-tA)\in\mathbb Z[t].}
\]

If the positive support is acyclic, `p(t)=D^n` and every non-negative scale `t` remains stable.

If a directed positive cycle exists, the stability endpoint

\[
t_c=\sup\{t\ge0:tW\text{ stable}\}
\]

is finite and equals the **smallest positive real root** of `p(t)`.

At every rational stable scale `0<t<t_c`,

\[
\boxed{
\chi(t)
=-t\,p'(t)/p(t)
=\operatorname{tr}((I-tW)^{-1}-I)
}
\]

is exact rational.

As `t->t_c^-`, `Gamma(t)` diverges. If the critical root has multiplicity `r`,

\[
\chi(t)\sim r t_c/(t_c-t).
\]

A rational stability potential `h` with

\[
\alpha(h)=\max_i(Wh)_i/h_i<1
\]

certifies the rational lower bound

\[
t_c\ge1/\alpha(h).
\]

No canonical rational optimizer is asserted.

## 10. Positive rational vertex-gauge cohomology

For rational edge weights

\[
q_e\in\mathbb Q_{>0}^{\times},
\]

unique factorization gives

\[
\boxed{
\mathbb Q_{>0}^{\times}
\cong
\bigoplus_{p\ \mathrm{prime}}\mathbb Z
}
\]

through prime valuations `v_p`.

Under vertex gauge

\[
q'_e=q_eh_{t(e)}/h_{s(e)},
\]

each valuation transforms by an integer coboundary:

\[
\boxed{
v_p(q'_e)=v_p(q_e)+v_p(h_{t(e)})-v_p(h_{s(e)}).}
\]

Hence

\[
\boxed{
H^1(G;\mathbb Q_{>0}^{\times})
\cong
\bigoplus_pH^1(G;\mathbb Z).
}
\]

For connected `G` with first Betti number `beta_1`, this is a finite-prime-support family of integer `Z^{beta_1}` coordinates.

The logarithmic expression

\[
\ln q=\sum_pv_p(q)\ln p
\]

is a faithful derived readout, but its image is not generally a discrete Euclidean lattice.

## 11. Spanning-tree rational gauge normal form

Fix a connected underlying graph, root and spanning tree `T`.

There is a unique rational vertex gauge with root scale `1` and all tree-edge weights equal to `1`.

The remaining

\[
\beta_1=|E|-|V|+1
\]

non-tree weights

\[
\widehat q_1,\ldots,\widehat q_{\beta_1}
\]

are complete rational gauge coordinates and equal the fundamental algebraic cycle products.

Factoring them primewise gives a complete integer holonomy normal form.

The full rational gauge cohomology can be strictly richer than recurrent loop observables: feed-forward graphs can retain path/cross-ratio gauge information while `Gamma`, `R` and `H` remain zero.

## 12. mod-m holonomy shadows

For every prime `p` and `m>=2`, valuation reduction induces

\[
\boxed{
H^1(G;\mathbb Q_{>0}^{\times})
\to H^1(G;\mathbb Z/m\mathbb Z).
}
\]

Collecting all primes,

\[
\boxed{
H^1(G;\mathbb Q_{>0}^{\times})/m
\cong
\bigoplus_pH^1(G;\mathbb Z/m\mathbb Z).
}
\]

For `m=2`, every prime gives a canonical parity shadow in `H^1(G;F_2)`, compatible with the existing typed `C_2` flat-holonomy layer.

Every finite-coefficient graph holonomy class admits a positive rational `p`-power lift.

## 13. m-power-free skeleton and rational thickness

For `q>0` rational and `m>=2`, write

\[
v_p(q)=mk_p+r_p,
\qquad0\le r_p<m.
\]

Define

\[
\boxed{s_m(q)=\prod_pp^{r_p}}
\]

and

\[
\boxed{t_m(q)=\prod_pp^{k_p}.}
\]

Then uniquely

\[
\boxed{q=s_m(q)t_m(q)^m.}
\]

`s_m(q)` is a positive `m`-power-free integer and `t_m(q)` is positive rational.

For `m=2`,

\[
\boxed{q=s(q)r(q)^2}
\]

with `s(q)` squarefree. The squarefree factor is the all-prime `C_2` parity skeleton; `r(q)` is the exact rational square-thickness root.

After reducing `q/s_m(q)=N/M`, both `N` and `M` are perfect `m`-th powers, so the thickness root may be verified/materialized by the existing BRC `ROOT_m` facade.

The abstract mod-`m` cohomology shadow is basis independent. A concrete tuple of `m`-power-free fundamental coordinates requires the selected tree/cycle basis.

## 14. Parity is not dynamically complete

The `C_2`/parity shadow is many-to-one and does not determine positive recurrent dynamics.

One-state examples:

\[
1/2=2(1/2)^2,
\qquad
2=2(1)^2
\]

share squarefree skeleton `2`, but the first is stable and the second divergent.

Likewise

\[
1/2=2(1/2)^2,
\qquad
1/8=2(1/4)^2
\]

are both stable with the same parity skeleton but have loop-zeta ratios `2` and `8/7`.

Therefore C2 parity does not determine either positive mass phase or recurrent loop surplus; the rational thickness coordinate is dynamically material.

## 15. Finite explicit-edge cycle-interaction polynomial

Assign one formal variable `x_e` to every explicit directed branch edge and put

\[
W(x)_{ij}=\sum_{e:i\to j}x_e.
\]

Define

\[
\boxed{P_G(x)=\det(I-W(x)).}
\]

Then

\[
\boxed{
P_G(x)
=\sum_F(-1)^{c(F)}\prod_{e\in F}x_e,
}
\]

where `F` ranges over vertex-disjoint explicit directed cycle systems and `c(F)` is the number of cycles.

At explicit-edge resolution:

- `P_G` is multiaffine;
- every nonzero coefficient is exactly `+1` or `-1`;
- `P_G identically 1` iff the support is a DAG;
- every cycle-system monomial is individually gauge invariant.

The alternating coefficient is determinant inclusion-exclusion and is **not** a signed BRC branch weight.

## 16. Tree-gauge cycle-interaction coordinates

Set every spanning-tree edge variable to `1` in the tree gauge and retain the fundamental holonomy variables

\[
z_1,\ldots,z_{\beta_1}.
\]

The resulting

\[
\boxed{P_{G,T}(z_1,\ldots,z_{\beta_1})}
\]

is a finite multiaffine polynomial with integer coefficients and satisfies

\[
\det(I-W(q))
=P_{G,T}(\widehat q_1,\ldots,\widehat q_{\beta_1}).
\]

Prime-valuation and parity/thickness data substitute directly via

\[
z_j=s_jr_j^2.
\]

For a fixed C2 skeleton `(s_j)`, thickness variables can move the system across recurrent phase boundaries.

## 17. Finite polynomial response identities

At a stable positive specialization `P=P_G(q)>0`,

\[
\boxed{R_e=-q_eP_e/P.}
\]

Hence `P_e<=0`, strict exactly on recurrent edges.

Because the explicit-edge polynomial is multiaffine,

\[
\boxed{H_{ee}=R_e(1+R_e).}
\]

For distinct edges,

\[
\boxed{
H_{ef}
=\frac{q_eq_f}{P^2}(P_eP_f-PP_{ef})\ge0.
}
\]

Thus the infinite positive loop response has a finite exact polynomial numerator/denominator representation.

## 18. Finite exclusion versus infinite positive closure

The same recurrent object has two exact representations:

```text
FINITE:
P_G = alternating sum over vertex-disjoint cycle systems

INFINITE POSITIVE:
Z_loop = 1/P_G
Gamma = -LN(P_G)
      = positive closed-walk / primitive-loop expansion
```

Overlapping cycles cannot coexist in one determinant cycle system but reappear through repeated/interacting terms after inversion/log closure.

This is the typed BRC meaning of the finite determinant certificate versus the infinite recurrent branch family.

## 19. Current hard boundaries

This addendum does not assert:

- signed/amplitude or complex-weight recurrence;
- infinite-state loop arithmetic;
- probability/Fisher semantics for the Hessian;
- a canonical rational optimizer of the critical scale;
- that the log-prime image is a discrete Euclidean lattice;
- that C2/mod-m shadows are complete positive-weight states;
- that recurrent loop observables classify feed-forward rational gauge data;
- that determinant alternating signs are positive/signed branch states;
- novelty of generic determinant-cycle, graph-zeta, graph-cohomology or rational power-class mathematics.

## 20. Reusable interfaces

Current reusable implementations are routed as T0_BRC global subtools:

- `t0.weighted_brc_recurrent_loop` — exact loop-zeta, response and criticality observables;
- `t0.weighted_brc_rational_holonomy` — prime valuations, tree gauge and power-class thickness;
- `t0.weighted_brc_cycle_polynomial` — explicit finite cycle-interaction polynomial calculus.

The exact theorem IDs are listed in `ENTERPRISE_BRC_RECURRENT_LOOP_THEOREM_LEDGER_20260902.json`.
