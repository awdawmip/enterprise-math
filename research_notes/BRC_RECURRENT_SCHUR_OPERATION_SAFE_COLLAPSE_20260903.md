# BRC Recurrent Schur Collapse as a Boundary-Operation-Safe Quotient

Status: `RESEARCH CANDIDATE / EXACT FINITE-RATIONAL / NOT YET FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-BRCFB-93C7D1`
Parent Foundation: `WBRC-T12..T29`

## 1. Purpose

The current Weighted-BRC Foundation can evaluate finite rational recurrence exactly, condense newly inserted feedback events, and compute recurrent loop/zeta/interaction observables. The next compression problem is structural:

> Can an already-existing stable internal recurrent subsystem be removed, leaving a smaller exact positive-rational boundary system that is safe under every later positive operation supported only on the retained boundary?

The answer is yes. The generic algebra is the classical Schur/stochastic complement (closely related to Kron reduction and stochastic complementation in Markov/network theory). No novelty claim is made for Schur complement identities or stochastic complements.

The project-specific contribution proposed here is a typed BRC semantic statement: **exact recurrent state elimination is an operation-safe collapse for a declared family of boundary-supported future operations**, with a separately retained internal loop-zeta/Gamma offset.

This is distinct from `src/enterprise_math/operation_quotient.py`, which computes finite deterministic endomap-compatible state partitions. The present object is non-idempotent, positive-weight, recurrent and port/boundary typed.

## 2. Block typing

Let a finite non-negative rational total-mass matrix be partitioned into internal states `I` and retained boundary states `B`. In the order `(I,B)`, write

\[
W=
\begin{pmatrix}
A & X\\
Y & B
\end{pmatrix},
\]

where rows are sources and columns are targets:

- `A`: internal -> internal;
- `X`: internal -> boundary;
- `Y`: boundary -> internal;
- `B`: boundary -> boundary.

Assume only that the internal block `A` is total-mass stable. Define its exact star

\[
S_I=(I-A)^{-1}.
\]

Define the **recurrent Schur collapse** (effective boundary matrix)

\[
\boxed{
W_{\rm eff}=B+YS_IX.
}
\]

Every entry remains a non-negative rational.

## 3. BRC path meaning of the effective edge

For boundary states `u,v`,

\[
(W_{\rm eff})_{uv}
=B_{uv}
+\sum_{i,j\in I}Y_{ui}(S_I)_{ij}X_{jv}.
\]

The second term is exactly the total positive mass of one **internal excursion**:

```text
boundary u
-> enter I
-> spend any finite number of I-only steps
-> exit I
-> boundary v
```

with no intermediate boundary visit.

Therefore every full walk whose endpoints are boundary states has a unique decomposition into a sequence of effective boundary steps. Direct boundary edges and complete internal excursions are alternatives recoalesced by positive addition.

The effective matrix is thus a BRC path-sum object, not merely a formal matrix quotient.

## 4. Exact boundary star theorem

### Candidate BRC-SC1

If `A` is stable, then

\[
\boxed{
W\text{ is stable}
\iff
W_{\rm eff}\text{ is stable}.
}
\]

When stable, if

\[
S=(I-W)^{-1},
\qquad
S_B=(I-W_{\rm eff})^{-1},
\]

then the retained boundary block of the full star is exactly

\[
\boxed{S[B,B]=S_B.}
\]

**BRC proof.** Internal excursions have finite exact mass because `A` is stable. Boundary-to-boundary walks segment uniquely by successive boundary visits, and each segment has one-step effective mass `W_eff`. Hence summing all full boundary walks is exactly the star of `W_eff`. Divergence on either side transfers through the same positive segmentation.

This is also the lower-right block of the classical block inverse of `I-W`.

## 5. Determinant / loop-zeta / Gamma decomposition

Schur determinant factorization gives

\[
\det(I-W)
=\det(I-A)\det(I-W_{\rm eff}).
\]

On the full stable phase,

\[
\boxed{
Z_{\rm loop}(W)
=Z_{\rm loop}(A)Z_{\rm loop}(W_{\rm eff}),
}
\]

and

\[
\boxed{
\Gamma(W)
=\Gamma(A)+\Gamma(W_{\rm eff}).
}
\]

Thus recurrent collapse separates:

- a fixed internal recurrent offset `Gamma(A)`;
- the complete retained-boundary recurrent state `W_eff`.

If the eliminated internal support is acyclic, then `Gamma(A)=0` and the scalar global loop surplus is preserved without any extra offset.

## 6. Full-star reconstruction

When both `A` and `W_eff` are stable, the full star is recoverable from

\[
S_I=(I-A)^{-1},
\qquad
S_B=(I-W_{\rm eff})^{-1}
\]

by

\[
\boxed{
S=
\begin{pmatrix}
S_I+S_IXS_BY S_I & S_IXS_B\\
S_BY S_I & S_B
\end{pmatrix}.
}
\]

Therefore eliminating internal states need not destroy the ability to reconstruct full **total-mass** transfer if the coupling blocks and internal star are retained. The minimal collapsed boundary object alone intentionally forgets that extra reconstruction data.

## 7. Boundary-operation-safe theorem

Let `C` be any later non-negative rational matrix supported only on boundary-to-boundary entries. The future full operation is

\[
W[C]
=
\begin{pmatrix}
A & X\\
Y & B+C
\end{pmatrix}.
\]

The internal block and couplings are unchanged. Its effective matrix is simply

\[
\boxed{
W_{\rm eff}[C]=W_{\rm eff}+C.
}
\]

### Candidate BRC-SC2

For every such boundary-supported positive operation `C`,

\[
\boxed{
W[C]\text{ stable}
\iff
W_{\rm eff}+C\text{ stable}.
}
\]

If stable,

\[
\boxed{
(I-W[C])^{-1}[B,B]
=(I-W_{\rm eff}-C)^{-1}.
}
\]

Moreover

\[
\boxed{
\Gamma(W[C])-\Gamma(W)
=
\Gamma(W_{\rm eff}+C)-\Gamma(W_{\rm eff}).
}
\]

Thus the collapse is **operation-safe** for the declared operation family

```text
all future non-negative rational updates supported on retained boundary edges.
```

Any feedback insertion/robustness/Möbius analysis whose event endpoints lie entirely in the retained boundary may therefore be performed on `W_eff` with exactly the same stability outcome and recurrent Gamma increment as on the full graph.

## 8. Boundary feedback compatibility

Suppose later feedback events all have sources/targets in `B`. Their event kernel computed in the full graph uses full-star entries

\[
S_{b_ra_s}.
\]

By BRC-SC1 these are exactly the corresponding entries of `S_B`. Therefore

\[
\boxed{
F_{\rm full}=F_{\rm eff}
}
\]

for every declared boundary-only feedback event family.

Consequently all already-Foundation results `WBRC-T25..T29` commute with recurrent Schur collapse:

- feedback stability;
- feedback loop-zeta/Gamma increment;
- conditional/modular feedback kernels;
- all-orders interaction factors `J_T`;
- interaction girth and circuit atoms.

This is the strongest practical operation-safe consequence of the collapse.

## 9. Gauge naturality

Apply a positive rational state gauge

\[
W'=H^{-1}WH,
\qquad
H=\operatorname{diag}(H_I,H_B).
\]

Then

\[
A'=H_I^{-1}AH_I,
\quad
X'=H_I^{-1}XH_B,
\quad
Y'=H_B^{-1}YH_I,
\quad
B'=H_B^{-1}BH_B.
\]

Because

\[
(I-A')^{-1}=H_I^{-1}S_IH_I,
\]

we obtain

\[
\boxed{
W'_{\rm eff}=H_B^{-1}W_{\rm eff}H_B.
}
\]

The internal offset `Gamma(A)` is gauge invariant, and the effective boundary gauge is exactly the restriction of the original state gauge.

Therefore recurrent Schur collapse descends correctly to the existing rational gauge/holonomy quotient.

## 10. Sequential elimination / associativity

Partition internal states further into `I_1` and `I_2`, with retained boundary `B`.

Whenever the chosen elimination prefixes have stable internal blocks, one may:

1. eliminate `I_1`;
2. eliminate the resulting effective `I_2` block;
3. retain `B`.

Classical Schur-complement transitivity and the unique path segmentation imply the final effective boundary matrix is exactly the same as eliminating `I_1 union I_2` in one step.

Thus

\[
\boxed{
\operatorname{Collapse}_{I_2}
(\operatorname{Collapse}_{I_1}(W))
=
\operatorname{Collapse}_{I_1\cup I_2}(W)
}
\]

at the retained-boundary total-mass level.

For a globally stable positive system every principal submatrix is stable, so every elimination ordering is admissible. This yields an exact recurrent coarse-graining hierarchy.

The Gamma offsets telescope conditionally, just as in `WBRC-T27`; their stagewise allocation may depend on elimination order although the final total is invariant.

## 11. Relation to T6 operation-safe quotient

`T6_OPERATION_SAFE_QUOTIENT` computes a partition of a finite deterministic state machine so a declared endomap family descends.

The present collapse is structurally analogous but mathematically distinct:

- T6 carrier: finite states + deterministic maps + observation partition;
- recurrent Schur carrier: non-negative rational transition mass + positive path sums + recurrent star;
- T6 output: a quotient partition;
- recurrent output: a smaller weighted boundary matrix plus optional scalar/internal reconstruction data.

Therefore this work should **extend T0 weighted/recurrent BRC**, not mutate T6.

The common principle is retained:

```text
SAFE COLLAPSE IS DEFINED RELATIVE TO FUTURE OBSERVATIONS/OPERATIONS.
```

## 12. Exact negative boundary: CWM/provenance is not preserved

The effective entry

\[
B_{uv}+YS_IX
\]

stores total positive mass only. It can merge distinct internal path families with different path count, dominant-path mass or provenance.

Example: one module can realize total boundary transfer `1` through one internal route of mass `1`, while another realizes the same transfer through two internal routes of mass `1/2` each. Both collapse to the same effective boundary edge mass `1`, but their CWM data differ:

\[
(1,1,1)
\neq
(2,1,1/2).
\]

Hence recurrent Schur collapse is **not** a CWM-safe or provenance-safe quotient unless those additional observables are separately included in the interface.

## 13. Exact negative boundary: internal/coupling operations are outside the lease

If a future operation changes `A`, `X` or `Y`, the old effective matrix need not remain correct. The operation-safe contract is boundary-only:

\[
(A,X,Y)\text{ fixed},
\qquad
B\mapsto B+C.
\]

A larger future-operation family would require a richer port signature that retains the needed internal transfer/coupling data.

No claim of universal quotient safety is made.

## 14. Ported signature viewpoint

For the present boundary-operation family, a collapsed module is represented by

\[
\boxed{
\mathcal S_B(W)
=(W_{\rm eff},\,\Gamma(A))
}
\]

if one wants both future boundary dynamics and total global Gamma.

If only future boundary stability/star/feedback increments matter, `W_eff` alone is sufficient.

If full transfer reconstruction is also required, retain

\[
(S_I,X,Y,W_{\rm eff}).
\]

This makes explicit that “minimal sufficient state” depends on the declared observation/operation contract.

## 15. Prior-art boundary

Schur complements, block matrix inversion, stochastic complements, censoring/reduction of Markov chains, and Kron-style reductions are classical/general mathematics.

Enterprise Math does not claim those generic identities as novel.

The project-specific reusable synthesis proposed here is:

```text
positive recurrent BRC
-> stable internal star
-> effective boundary excursion matrix
-> exact boundary star
-> Gamma offset factorization
-> all boundary-only future feedback operations commute with collapse
```

with explicit boundaries against CWM/provenance and internal/coupling mutations.

## 16. Validation plan

Use exact `Fraction` arithmetic only.

1. Exhaust all `3^9=19,683` three-state matrices with entries `{0,1/3,2/3}`, eliminate state 0 (which is always internally stable), and verify full stability iff 2-state effective stability.
2. On every stable full sample verify boundary star block equality and determinant factorization.
3. On every stable sample verify exact loop-zeta factorization `Z_full=Z_A*Z_eff`.
4. Apply a fixed corpus of positive boundary-only updates to selected stable/unstable samples and verify operation-safe stability, boundary-star equality and Gamma-increment equality.
5. Verify boundary feedback-event kernels are exactly identical before/after collapse.
6. Verify positive rational gauge naturality on nontrivial 4-state examples.
7. Verify one-shot versus sequential elimination on 4-state examples and multiple elimination orders.
8. Verify DAG-internal specialization has `Gamma(A)=0` and therefore no scalar offset.
9. Include the explicit CWM-loss counterexample to freeze the total-mass-only boundary.

A dedicated research CI gate must pass before any Foundation backflow.
