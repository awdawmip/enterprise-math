# BRC Feedback Condensation and Exact Stability-Radius Calculus

Status: `RESEARCH CANDIDATE / EXACT FINITE-RATIONAL / NOT YET FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-BRCFB-93C7D1`
Parent line: Weighted-BRC finite recurrence (`WBRC-T12..T16`) + recurrent loop-zeta/response + prime-valuation parity/thickness + determinant cycle-interaction polynomial

## 1. Purpose

The current finite recurrent Weighted-BRC layer can decide whether a finite non-negative rational transition-mass matrix is stable, compute its exact star, and expose recurrent loop response. The next question is operational:

> If a stable background receives one or several new positive feedback branches, can the new global recurrent problem be reduced exactly to a smaller BRC system whose state set is only the inserted feedback events?

The answer is yes.

The generic matrix determinant lemma, Sherman-Morrison-Woodbury identity, Schur-complement/feedback reduction, and their classical consequences are prior art. No novelty claim is made for those identities. The Enterprise Math contribution claimed here is the exact typed BRC interpretation: stable background paths are condensed into an event-level recurrent total-mass kernel, with exact loop-zeta factorization, gauge transport, single-edge robustness radii, and a direct bridge to the previously frozen parity/thickness fibers.

## 2. Stable background and inserted branch events

Let

\[
W\in M_n(\mathbb Q_{\ge0})
\]

be total-mass stable and write

\[
S=(I-W)^{-1}=I+W+W^2+\cdots.
\]

Choose `m>=1` new positive branch events

\[
e_r:a_r\to b_r,
\qquad
\delta_r\in\mathbb Q_{>0},
\qquad r=1,\ldots,m.
\]

Let `U` have columns `e_{a_r}`, let `V` have columns `e_{b_r}`, and set

\[
D=\operatorname{diag}(\delta_1,\ldots,\delta_m).
\]

The updated transition-mass matrix is

\[
\widetilde W=W+UDV^\top.
\]

Define the background transfer matrix between feedback events by

\[
K=V^\top S U,
\qquad
K_{rs}=S_{b_r a_s},
\]

and define the **feedback event kernel**

\[
\boxed{F=KD},
\qquad
\boxed{F_{rs}=S_{b_r a_s}\,\delta_s.}
\]

Interpretation: after traversing inserted edge `r`, the old background runs from `b_r` to `a_s` with total mass `S_{b_r a_s}`, then inserted edge `s` is traversed with mass `delta_s`.

`F` is therefore not an arbitrary linear-algebra compression. It is the exact positive total-mass recurrence on the declared inserted-edge occurrences after every maximal background-only segment has been summed out.

## 3. Unique path segmentation and the exact star formula

Every walk in the updated system has a unique decomposition by its occurrences of inserted edges:

```text
background segment
-> inserted edge
-> background segment
-> inserted edge
-> ...
-> background segment.
```

All background segments contain only old `W` edges. Therefore the total mass of walks using exactly `k>=1` inserted edges is

\[
SUD\,F^{k-1}V^\top S.
\]

Summing over `k` gives, whenever `F` is stable,

\[
\boxed{
\widetilde S
=(I-\widetilde W)^{-1}
=S+SUD(I-F)^{-1}V^\top S.
}
\]

This is the Woodbury formula, but here it is also an exact BRC walk decomposition by feedback-event count.

## 4. Feedback condensation theorem

### Theorem candidate BRC-FB1

For stable finite non-negative rational background `W` and finitely many positive rational inserted branches as above,

\[
\boxed{
\widetilde W\text{ is total-mass stable}
\iff
F\text{ is total-mass stable}.
}
\]

**Sufficiency.** If `F` is stable, the star formula above is a finite non-negative rational matrix, hence it is the exact updated star.

**Necessity.** If the feedback-event closure diverges, then some sum of entries of `F^k` diverges. Each such event walk expands into a disjoint family of updated-system walks, using empty background segments at the selected event endpoints when necessary. Hence the updated positive walk sum diverges as well.

No irreducibility or SCC hypothesis is required.

This is a typed total-mass result only. Condensing through `S` has already summed background multiplicity/provenance and does not by itself preserve CWM count, dominant-path mass, or path identity.

## 5. Determinant and recurrent loop-zeta factorization

The matrix determinant lemma gives

\[
\det(I-\widetilde W)
=
\det(I-W)\det(I-DK).
\]

Since `det(I-DK)=det(I-KD)`, we obtain

\[
\boxed{
\det(I-\widetilde W)
=
\det(I-W)\det(I-F).
}
\]

On the stable phase, with

\[
Z_{\rm loop}(X)=\frac1{\det(I-X)},
\qquad
\Gamma(X)=-\ln\det(I-X),
\]

this becomes

\[
\boxed{Z_{\rm loop}(\widetilde W)=Z_{\rm loop}(W)Z_{\rm loop}(F)},
\]

\[
\boxed{\Gamma(\widetilde W)=\Gamma(W)+\Gamma(F)}.
\]

Thus all **new** recurrent loop surplus created by the inserted branches is exactly the loop surplus of the much smaller feedback-event kernel.

This is stronger than a determinant shortcut: it identifies the low-dimensional object whose positive walk closure is the new recurrence.

## 6. Gauge naturality of the feedback kernel

Apply a positive rational vertex gauge

\[
W'_{ij}=W_{ij}\frac{h_j}{h_i}.
\]

Then

\[
S'_{ij}=S_{ij}\frac{h_j}{h_i},
\qquad
\delta'_s=\delta_s\frac{h_{b_s}}{h_{a_s}}.
\]

Therefore

\[
F'_{rs}
=S'_{b_r a_s}\delta'_s
=F_{rs}\frac{h_{b_s}}{h_{b_r}}.
\]

If

\[
G=\operatorname{diag}(h_{b_1},\ldots,h_{b_m}),
\]

then

\[
\boxed{F'=G^{-1}FG}.
\]

So feedback condensation is gauge-natural: vertex gauge on the original graph descends to ordinary positive diagonal gauge on feedback-event states. Consequently feedback stability, determinant, loop zeta and `Gamma(F)` are gauge invariant.

## 7. Single-edge insertion: exact additive stability radius

For one inserted edge

\[
e:a\to b,\qquad\delta>0,
\]

the feedback kernel is the scalar

\[
F=[\delta\kappa_e],
\qquad
\kappa_e:=S_{ba}.
\]

`kappa_e` is the exact background return mass from the target of the new edge back to its source.

### If `kappa_e=0`

There is no old positive path `b->a`, so the new edge cannot participate in a directed cycle. Then for every finite `delta>0`,

\[
\det(I-\widetilde W)=\det(I-W),
\]

and the updated system remains stable. The additive stability radius is infinite.

### If `kappa_e>0`

The exact phase condition is

\[
\boxed{\delta\kappa_e<1}.
\]

Hence

\[
\boxed{\delta_c(e)=\frac1{S_{ba}}}.
\]

For `0<=delta<delta_c`,

\[
\boxed{
\widetilde S_{ij}
=S_{ij}
+\frac{\delta S_{ia}S_{bj}}{1-\delta S_{ba}}.
}
\]

The determinant and loop-zeta increments are

\[
\frac{\det(I-\widetilde W)}{\det(I-W)}
=1-\delta S_{ba},
\]

\[
\frac{Z_{\rm loop}(\widetilde W)}{Z_{\rm loop}(W)}
=\frac1{1-\delta S_{ba}},
\]

\[
\boxed{
\Gamma(\widetilde W)-\Gamma(W)
=-\ln(1-\delta S_{ba}).
}
\]

The log is a derived BRC `LN` readout of an exact positive rational ratio; no floating determinant/log evaluation is needed.

## 8. New-edge response and the exact one-edge closure identity

In the updated stable system the response of the newly inserted edge is

\[
R_{\rm new}
=\delta\widetilde S_{ba}
=\frac{\delta S_{ba}}{1-\delta S_{ba}}.
\]

Therefore

\[
\boxed{
\Gamma(\widetilde W)-\Gamma(W)
=\ln(1+R_{\rm new}).
}
\]

This is an exact finite-graph analogue of the one-state geometric closure: the inserted edge and the entire old return-path family behave as one effective recurrent loop with one-step mass `delta*S_ba`.

## 9. Existing-edge strengthening: gauge-invariant multiplicative radius

Let an existing explicit positive branch `e:a->b` have weight `q_e>0`. Its current recurrent response is

\[
R_e=q_eS_{ba}.
\]

Strengthen only this branch by

\[
q_e\mapsto\lambda q_e,
\qquad\lambda\ge1.
\]

This is equivalent to inserting a parallel increment

\[
\delta=(\lambda-1)q_e.
\]

Hence the exact stability condition is

\[
(\lambda-1)R_e<1.
\]

If `R_e>0`, the critical multiplicative factor is

\[
\boxed{
\Lambda_e
=1+\frac1{R_e}.
}
\]

If `R_e=0`, the branch is transient and may be scaled by any finite factor without creating recurrence.

Unlike the additive radius `1/S_ba`, `Lambda_e` is individually vertex-gauge invariant because `R_e` is gauge invariant.

This gives a canonical per-edge recurrent robustness coordinate.

## 10. Exact deletion contribution

For an existing explicit branch of weight `q_e`, removing that branch keeps the system stable. Applying the same determinant identity with the signed update `-q_e E_{ab}` gives

\[
\frac{\det(I-(W-q_eE_{ab}))}{\det(I-W)}
=1+q_eS_{ba}
=1+R_e.
\]

Therefore the exact leave-one-edge-out loop-surplus contribution is

\[
\boxed{
\Gamma(W)-\Gamma(W-q_eE_{ab})
=\ln(1+R_e).
}
\]

This quantity is positive exactly for recurrent edges and zero for transient edges.

It is **not additive over edges**. For example, every edge of a simple directed cycle can individually carry the entire loop surplus because deleting any one of them kills that cycle. It is therefore a deletion sensitivity, not a partition of `Gamma`.

## 11. Determinant-polynomial form

Let

\[
P=\det(I-W)
\]

and let `P_e` be the derivative of the branch-resolved determinant polynomial with respect to explicit edge `e`. From the previously merged polynomial-response identity,

\[
P_e=-P\,S_{ba}.
\]

For a recurrent edge (`P_e<0`), the additive critical increment is therefore

\[
\boxed{
\delta_c=-\frac{P}{P_e}.
}
\]

For an existing branch `q_e>0`,

\[
\boxed{
\Lambda_e
=1-\frac{P}{q_eP_e}
=1+\frac1{R_e}.
}
\]

Thus the exact robustness radius can be read either from the infinite positive star or from the finite multiaffine determinant polynomial.

## 12. Fixed parity / mod-m thickness phase boundary

In the tree-normal gauge of the prime-valuation holonomy work, let a fundamental non-tree branch coordinate be written

\[
q_e=s_m\,t^m,
\]

where `s_m` is the fixed `m`-power-free skeleton and `t in Q_{>0}` is the exact thickness coordinate.

Change thickness only:

\[
t\mapsto\mu t.
\]

Then the branch weight is scaled by

\[
\lambda=\mu^m.
\]

For `mu>=1` and recurrent edge `e`, the exact phase condition is

\[
(\mu^m-1)R_e<1.
\]

Hence the critical thickness satisfies the purely rational power-coordinate law

\[
\boxed{
\mu_c^m
=1+\frac1{R_e}
=\Lambda_e.
}
\]

No irrational root need be materialized. A rational candidate `mu` is classified exactly by comparing `mu^m` with the rational `Lambda_e`.

For `m=2`, this is the exact phase boundary inside a fixed squarefree/C2 parity skeleton fiber.

This sharpens the previous negative result “parity alone does not determine phase”: parity fixes the skeleton, while the recurrent response gives the exact remaining thickness budget along one fundamental coordinate.

## 13. Collective feedback: single-edge safety is not enough

Several individually harmless edges may form a recurrent cycle only when inserted together.

Take a four-state acyclic background with only

\[
1\to2\text{ of mass }u,
\qquad
3\to0\text{ of mass }v.
\]

Insert

\[
e_1:0\to1\text{ of mass }\delta_1,
\qquad
e_2:2\to3\text{ of mass }\delta_2.
\]

Each inserted edge separately has zero return mass and is harmless at every finite weight. But the joint feedback kernel is

\[
F=
\begin{pmatrix}
0&u\delta_2\\
v\delta_1&0
\end{pmatrix}.
\]

The pair is stable exactly when

\[
\boxed{uv\delta_1\delta_2<1}.
\]

Thus recurrent risk is genuinely cooperative. Independent single-edge margins do not classify simultaneous branch additions; the correct object is the full feedback-event kernel.

## 14. DAG background specialization

If the old background is a DAG, its star `S` is a finite polynomial path sum. Feedback condensation then has an especially direct interpretation:

```text
large feed-forward BRC
-> exact finite background transfer S
-> small event-level feedback kernel F
-> recurrent stability / zeta / Gamma on F only.
```

If the support of `F` is acyclic, then `F` is nilpotent for every positive choice of inserted masses, `det(I-F)=1`, and the inserted edges create no recurrent loop surplus at all.

This gives a precise separation between large transient multipath structure and genuinely recurrent branch interaction.

## 15. Boundaries

The current candidate does **not** claim:

- preservation of CWM path count or dominant-path mass under feedback condensation;
- preservation of path provenance after background summation;
- signed/amplitude cancellation semantics;
- an infinite-state feedback theorem;
- that single-edge robustness radii combine independently;
- novelty of determinant-lemma, Woodbury or Schur-complement mathematics;
- that additive edge radius is gauge invariant (only the multiplicative radius is);
- that critical thickness itself is rational when `m>1` (only its `m`-th power is canonically rational here).

The intended project-specific object is an **exact positive-total-mass feedback-event BRC kernel**, together with its loop-zeta and robustness interfaces.

## 16. Exact validation plan

The companion checker must verify, using only integers and `Fraction` arithmetic:

1. exhaustive small stable `2x2` backgrounds and one/two inserted edges: full updated stability iff feedback-kernel stability;
2. determinant factorization for stable and unstable insertions;
3. Woodbury/BRC segmented-walk star formula on every stable sampled case;
4. exact single-edge below/equal/above critical radius behavior;
5. infinite-radius behavior when no return path exists;
6. existing-edge multiplicative critical factor `1+1/R_e`;
7. deletion determinant ratio `1+R_e`;
8. gauge naturality `F'=G^{-1}FG`;
9. two-edge cooperative feedback where each edge is individually harmless but the pair can diverge;
10. fixed-squarefree-skeleton thickness examples crossing phase exactly at the predicted rational square threshold.

A dedicated research CI gate should freeze these checks before any Foundation backflow.
