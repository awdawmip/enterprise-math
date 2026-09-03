# BRC Modular Feedback Condensation and Conditional Risk Transport

Status: `RESEARCH CANDIDATE / EXACT FINITE-RATIONAL / NOT YET FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-BRCFB-93C7D1`
Parent result: PR #1142 / merge `1fce8294c6116bdd9fd97828a232657fc7ee892c`

## 1. Problem

PR #1142 proved that finitely many new positive feedback branches on a stable finite rational background can be condensed to an event-level feedback kernel `F`, and that the full updated system is stable exactly when `F` is stable.

The next question is compositional:

> Can a large declared feedback set be split into modules, condensed one module at a time, and still reproduce the exact one-shot stability, star, determinant and loop-surplus result?

Yes. The relevant algebra is the classical block Schur complement, but the BRC interpretation is an exact conditional feedback law.

Generic Schur-complement, block determinant and block-inverse identities are classical prior art. The project-specific result is their typed use as a modular positive-total-mass feedback execution interface.

## 2. One-shot feedback kernel split into two groups

Let `W` be stable with

\[
S=(I-W)^{-1}.
\]

Partition the inserted events into ordered groups `A` and `B`. In event ordering `(A,B)`, write the one-shot feedback kernel from PR #1142 as

\[
F=
\begin{pmatrix}
F_A & X\\
Y & F_B
\end{pmatrix}.
\]

Concretely, if `A` has masses `D_A` and `B` has masses `D_B`, then

\[
F_A=K_{AA}D_A,
\quad
X=K_{AB}D_B,
\quad
Y=K_{BA}D_A,
\quad
F_B=K_{BB}D_B,
\]

where

\[
K_{rs}=S_{b_r a_s}.
\]

The off-diagonal blocks are not symmetric in general because each column already includes the mass of the destination inserted event.

## 3. Condense group A first

Assume `F_A` is stable. By PR #1142, the background after inserting group `A` is stable, with exact star

\[
S_A
=
S+S U_A D_A(I-F_A)^{-1}V_A^\top S.
\]

Now compute the feedback kernel seen by the still-uninserted group `B` against this updated background:

\[
F_{B\mid A}
=
V_B^\top S_A U_B D_B.
\]

Substitution gives

\[
\boxed{
F_{B\mid A}
=
F_B+Y(I-F_A)^{-1}X.
}
\]

This is the **conditional feedback kernel**.

Interpretation:

- `F_B` is direct B-to-B recurrence through the old background;
- `Y(I-F_A)^{-1}X` is recurrence that leaves a B event, enters the already-installed A feedback subsystem, makes any finite number of A feedback recurrences, and returns to B.

Thus the Schur correction has a direct positive BRC walk meaning.

## 4. Modular stability theorem

### Candidate BRC-MF1

For stable base `W`, event partition `(A,B)`, and positive rational inserted masses,

\[
\boxed{
W+A+B\text{ is stable}
\iff
F_A\text{ is stable and }F_{B\mid A}\text{ is stable}.
}
\]

**Forward direction.** If the final positive system is stable, deleting all B edges leaves the A-only system stable by monotonicity of positive walk masses. Hence `F_A` is stable. Applying PR #1142 again to B on the stable A-updated background shows `F_{B|A}` is stable.

**Reverse direction.** If `F_A` is stable, the A-updated background is stable. If its B-feedback kernel `F_{B|A}` is stable, a second application of PR #1142 gives final stability.

This result needs no SCC or irreducibility hypothesis.

## 5. Determinant / zeta / Gamma chain rule

The block matrix

\[
I-F=
\begin{pmatrix}
I-F_A & -X\\
-Y & I-F_B
\end{pmatrix}
\]

has Schur complement

\[
I-F_B-Y(I-F_A)^{-1}X
=I-F_{B\mid A}.
\]

Therefore, whenever `F_A` is stable,

\[
\boxed{
\det(I-F)
=
\det(I-F_A)\det(I-F_{B\mid A}).
}
\]

Together with PR #1142,

\[
\frac{\det(I-W-A-B)}{\det(I-W)}
=
\det(I-F_A)\det(I-F_{B\mid A}).
\]

On the stable phase,

\[
\boxed{
\Delta\Gamma_{A\cup B}
=
\Delta\Gamma_A
+
\Delta\Gamma_{B\mid A}.
}
\]

Here

\[
\Delta\Gamma_A=-\ln\det(I-F_A),
\qquad
\Delta\Gamma_{B\mid A}=-\ln\det(I-F_{B\mid A}).
\]

This is an exact chain rule for feedback loop surplus.

## 6. Order-independent total, order-dependent attribution

The same final update can be ordered as `(B,A)`. If the B-only stage is stable,

\[
\Delta\Gamma_{A\cup B}
=
\Delta\Gamma_B+
\Delta\Gamma_{A\mid B}.
\]

The total is order independent because both expressions equal the same final determinant ratio. The two stagewise attributions are generally different.

### One-state exact witness

Let the old one-state background have mass

\[
s=1/4,
\]

and insert two extra self-loop branches

\[
\delta_A=1/8,
\qquad
\delta_B=1/16.
\]

All stages are stable and the total loop-zeta multiplier is

\[
\frac{1-s}{1-s-\delta_A-\delta_B}
=\frac{3/4}{9/16}
=\frac43.
\]

A-first attribution:

\[
Z_A=\frac{3/4}{5/8}=\frac65,
\qquad
Z_{B\mid A}=\frac{5/8}{9/16}=\frac{10}{9}.
\]

B-first attribution:

\[
Z_B=\frac{3/4}{11/16}=\frac{12}{11},
\qquad
Z_{A\mid B}=\frac{11/16}{9/16}=\frac{11}{9}.
\]

Both products are `4/3`, but the factors differ.

Therefore stagewise loop-surplus credit is **order/context dependent**, while final `Gamma` is intrinsic.

This mirrors older BRC retrospective-credit boundaries: a telescoping total does not imply a unique intrinsic allocation to components.

## 7. Single-edge conditional return-mass update

Let group `A` contain one inserted edge

\[
e:a\to b
\]

of mass `delta`, with

\[
\delta S_{ba}<1.
\]

The updated star is

\[
S_A
=S+
\frac{\delta}{1-\delta S_{ba}}
S_{\bullet a}S_{b\bullet}.
\]

For a later candidate edge

\[
f:c\to d,
\]

its return mass changes from

\[
\kappa_f=S_{dc}
\]

to

\[
\boxed{
\kappa_f^{(e)}
=S_{dc}
+
\frac{\delta S_{da}S_{bc}}{1-\delta S_{ba}}.
}
\]

Hence the exact conditional additive radius becomes

\[
\boxed{
\delta_{f,c}\n=1/\kappa_f^{(e)}
}
\]

when the updated return mass is positive.

This formula isolates how an earlier feedback edge creates or amplifies a later feedback channel.

## 8. Risk creation from an initially harmless edge

Use the cooperative-feedback DAG from PR #1142:

- old edge `1->2` of mass `u`;
- old edge `3->0` of mass `v`;
- first inserted edge `e:0->1` of mass `delta_1`;
- second candidate edge `f:2->3`.

Against the old DAG, `f` has no return path `3->2`, so

\[
S_{32}=0
\]

and its single-edge radius is infinite.

After inserting `e`, however,

\[
\boxed{
\kappa_f^{(e)}
=v\delta_1u.
}
\]

Therefore the newly finite conditional radius is

\[
\boxed{
\delta_{2,c}
=\frac1{uv\delta_1}.
}
\]

The pair condition is exactly

\[
uv\delta_1\delta_2<1.
\]

Thus a feedback module can convert a previously transient edge into a recurrent edge. The conditional kernel quantifies the creation of risk exactly.

## 9. Event-level response update

Because `F_{B|A}` is itself a finite positive recurrent BRC kernel, every existing response theorem applies at event level.

For a B event `r`, its conditional recurrent response is computed from

\[
(I-F_{B\mid A})^{-1}
\]

rather than from the original background alone.

This gives a modular workflow:

```text
stable base star S
-> condense installed module A
-> compute conditional kernel F_{B|A}
-> apply finite recurrent / zeta / response / criticality tools to B
```

No new top-level tool family is required.

## 10. Associativity over more than two modules

For three ordered event groups `(A,B,C)`, repeat the construction:

1. condense `A`;
2. form `F_{B|A}` and condense `B`;
3. form `F_{C|A,B}` against the twice-updated background.

Whenever every prefix is stable, repeated applications of PR #1142 yield exactly the same final star and determinant as one-shot insertion of `A∪B∪C`.

The corresponding loop-surplus chain is

\[
\boxed{
\Delta\Gamma_{A\cup B\cup C}
=
\Delta\Gamma_A
+
\Delta\Gamma_{B\mid A}
+
\Delta\Gamma_{C\mid A,B}.
}
\]

By induction, any ordered partition of a stable final feedback set gives a telescoping conditional-Gamma decomposition.

The decomposition values depend on the chosen order/grouping; the sum does not.

## 11. Stability monotonicity and allowed orderings

If the final positive update is stable, then every subset of inserted positive edges is stable, since deleting positive branches can only decrease every finite-depth walk mass.

Therefore **every ordering** of a stable final insertion set has stable prefixes, and the modular condensation procedure is valid in any order.

If the final update is unstable, some orderings may fail at an early prefix and others later. Once a prefix is unstable, the stable-background condensation interface stops there; adding more positive edges cannot restore stability.

## 12. Computational consequence

Suppose the old graph has `n` states but new feedback arrives in modules of sizes

\[
m_1,m_2,\ldots,m_k.
\]

After the old star is available, each stage can be analyzed using only the current module's feedback kernel plus the required old/updated transfer slices. Conceptually, recurrent re-analysis is controlled by module sizes rather than by reconstructing the full `n x n` determinant from zero at every edit.

This is an exact algebraic reduction, not yet a runtime-complexity theorem. Any claimed asymptotic speedup must account for the cost of maintaining star/transfer slices and matrix arithmetic.

## 13. Hard boundaries

This candidate does not claim:

- a unique intrinsic attribution of `Gamma` to inserted modules;
- order independence of conditional module increments;
- that an unstable prefix can be repaired by later positive additions;
- preservation of CWM path count, dominant mass or provenance through total-mass condensation;
- signed/amplitude cancellation;
- infinite-state modular feedback closure;
- a runtime speedup theorem;
- novelty of Schur-complement or block determinant identities.

The project-specific reusable object is the **conditional feedback kernel** and its exact BRC chain rule.

## 14. Validation plan

The exact checker must verify with `Fraction` arithmetic:

1. every two-event case from the PR #1142 small-background corpus: one-shot final stability equals `(first stable AND second conditional stable)` for both event orderings;
2. `F_{B|A}` computed by block Schur formula equals the feedback kernel computed directly from the A-updated full star;
3. block determinant factorization and final full determinant agree exactly;
4. sequential star update equals one-shot Woodbury/full inverse;
5. A-first and B-first total zeta multiplier agree while stage multipliers can differ;
6. the cooperative DAG witness creates the exact return mass `u*v*delta_1` for the second edge;
7. a selected three-event corpus obeys iterative associativity and telescoping determinant factors;
8. stable final sets have stable prefixes under every tested permutation.

A dedicated CI gate should pass before any Foundation backflow.
