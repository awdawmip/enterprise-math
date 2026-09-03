# Viète binary cycle covers: C3 -> C6 -> C12 as precision refinement, and 2-adic resolution versus analytic phase completion

Status: `FREE_RESEARCH / EXACT FINITE-COVER THEOREM + COMPLETION-TYPE BOUNDARY / NOT_FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-FREE-7D3C9A / FREE_AXIOM_DISCOVERY`
Issue: `#1158`
Depends on:
- current three-positive-ray cyclic slice structure;
- `research_notes/VIETE_FINITE_CYCLIC_SHORTEST_ROOT_REFINEMENT_20260903.md`.

## 1. Motivation

The finite shortest-root theorem used the tower

\[
C_6\leftarrow C_{12}\leftarrow C_{24}\leftarrow\cdots
\]

as a G1 direction-resolution system. But the current native three-axis slice starts more primitively with three positive ray classes carrying a cyclic `C3` structure.

This note shows that the six-state shell itself can be understood as the **first connected binary resolution cover** of that `C3` cycle. The quarter-turn shell `C12` is then the second binary cover.

Thus `C6` need not be interpreted as six primitive native signed axes.

## 2. Connected two-fold covers of a cycle are unique

Let `Gamma_N` be the cycle graph with `N>=3` vertices.

Any finite connected covering graph of `Gamma_N` is 2-regular and connected, hence itself a cycle graph.

If the covering has degree two, the covering graph has exactly `2N` vertices. Therefore it is

\[
\Gamma_{2N}.
\]

Hence:

\[
\boxed{
\text{up to covering isomorphism, the unique connected two-sheeted cover of }\Gamma_N\text{ is }\Gamma_{2N}.}
\]

The disconnected two-sheeted alternative is simply two disjoint copies of `Gamma_N`; it does not form one refined cyclic orientation space.

Therefore, if “binary direction refinement” means a connected homogeneous two-sheeted refinement of the coarse orientation cycle, the state count and cycle structure are forced.

## 3. Group form of the cover

Write the refined cycle as

\[
C_{2N}=\mathbb Z/(2N)\mathbb Z
\]

and the coarse cycle as

\[
C_N=\mathbb Z/N\mathbb Z.
\]

The covering projection is

\[
\boxed{
\pi_N(j\bmod2N)=j\bmod N.
}
\]

Each coarse state has two lifts:

\[
\pi_N^{-1}(k)=\{k,k+N\}.
\]

The nontrivial deck transformation is

\[
\boxed{
H_N(j)=j+N\pmod{2N}.
}
\]

It is fixed-point free and has order two.

Thus the binary refinement itself automatically creates a relative two-state “opposite phase” over every coarse ray class.

## 4. First cover: three positive rays become the six-gate shell

Apply the theorem to the current three-ray cycle:

\[
C_3\xleftarrow{\pi_3}C_6.
\]

The coarse three positive ray classes lift to six refined direction states.

The nontrivial deck transformation is

\[
H_3(j)=j+3\pmod6.
\]

This is exactly the half-cycle involution of the six-state shell.

Therefore:

\[
\boxed{
C_6\text{ can be interpreted as the first connected binary precision cover of the current }C_3\text{ positive-ray quotient.}
}
\]

This does not introduce six primitive native axes. The extra three states are resolution-phase lifts over the original three positive ray classes.

In particular the half-turn/opposite state first becomes available **at the first binary refinement**, rather than needing to be primitive at the `C3` layer.

## 5. Second cover: quarter-turn roots emerge in C12

Refine again:

\[
C_6\xleftarrow{\pi_6}C_{12}.
\]

The half-turn state of `C6` is

\[
h=3\pmod6.
\]

Its two lifts are

\[
\boxed{
\pi_6^{-1}(h)=\{3,9\}\pmod{12}.
}
\]

Both have order four in `C12`:

\[
4\cdot3\equiv0\pmod{12},
\qquad
2\cdot3=6\not\equiv0,
\]

and similarly for `9`.

Thus the two quarter-turn root states are forced as the two lifts of the first-refinement half-turn:

\[
\boxed{
C_3\to C_6\to C_{12}
\quad\text{means}
\quad
\text{positive-ray cycle}\to\text{half-turn-resolved shell}\to\text{quarter-turn-resolved shell}.
}
\]

No Euclidean signed-axis ontology is needed.

## 6. Turn-sense inversion is a cover automorphism, not the deck half-turn

Define turn-sense inversion on every cycle by

\[
S_N(j)=-j\pmod N.
\]

It commutes with coarse-graining:

\[
\pi_N\circ S_{2N}=S_N\circ\pi_N.
\]

It also commutes with the deck half-turn:

\[
S_{2N}H_N=H_NS_{2N},
\]

because

\[
-(j+N)\equiv -j+N\pmod{2N}.
\]

This gives a precise finite version of the #1158 distinction:

- `H`: deck half-turn/opposite phase inside the refined **state** space;
- `S`: inversion of turn sense, an **automorphism** of the state cover.

They are different involutions even though both are order two.

At the `C12` quarter-root pair `{3,9}`, inversion swaps the two lifts.

## 7. Iterated binary covers

Continue the connected binary cover tower:

\[
C_3
\xleftarrow{}
C_6
\xleftarrow{}
C_{12}
\xleftarrow{}
C_{24}
\xleftarrow{}
\cdots
\]

with

\[
C_{3\cdot2^m}
\]

at binary resolution depth `m`.

Each coarse state has exactly two lifts at the next depth. Therefore one additional resolution level contributes exactly one binary refinement coordinate.

The Viète shortest-root rule selects, branchwise, the lift of minimum cycle distance to the identity, except at the unique half-turn tie where both lifts are retained.

## 8. Inverse-limit precision address is 2-adic

Use the covering projections

\[
C_{3\cdot2^{m+1}}\to C_{3\cdot2^m}.
\]

By the Chinese remainder theorem,

\[
C_{3\cdot2^m}\cong C_3\times C_{2^m}.
\]

The inverse system preserves the `C3` factor and uses ordinary reduction on the `2^m` factor. Hence

\[
\boxed{
\varprojlim_m C_{3\cdot2^m}
\cong
C_3\times\mathbb Z_2.
}
\]

Thus an infinitely resolved compatible discrete orientation address naturally carries a 2-adic precision coordinate.

This is a **profinite resolution completion**: compact and totally disconnected.

It is not the classical continuous circle.

Freeze:

`BINARY_RESOLUTION_ADDRESS_COMPLETION = C3 x Z_2` at this G1 cover model.

## 9. Character-state union has a different completion

There is also an injective state-preserving character realization

\[
\mu_{3\cdot2^m}\subset\mu_{3\cdot2^{m+1}}
\]

inside the unit complex/algebraic character group, where old character values are retained at every finer level.

The direct union is

\[
\boxed{
\bigcup_m\mu_{3\cdot2^m}
\cong
C_3\times C_{2^\infty},
}
\]

where `C_(2^infinity)` is the Prüfer 2-group.

Under the usual complex character embedding, the mesh size tends to zero and this union is dense in `U(1)`. Its analytic/topological closure is therefore the continuous unit circle.

Hence two different completions coexist:

1. **inverse-limit resolution-address completion**
   \[
   C_3\times\mathbb Z_2;
   \]
2. **character-image analytic phase completion**
   \[
   \overline{\bigcup_m\mu_{3\cdot2^m}}=U(1).
   \]

They must not be identified.

Freeze:

\[
\boxed{
\text{PROFINITE PRECISION COMPLETION} \neq \text{ANALYTIC PHASE COMPLETION}.
}
\]

## 10. Viète branch as a special compatible lift sequence

The half-turn appears at `C6` as the nontrivial deck lift over the coarse identity ray class.

At `C12` it has the two quarter-turn lifts `+3` and `-3` modulo `12`.

Under successive shortest-root refinements, the positive branch is represented by exponent `+3` at every later cycle

\[
C_{3\cdot2^m},\qquad m\ge2,
\]

while the negative branch is exponent `-3`.

In the character realization these have orders

\[
2^m
\]

and approach the identity from the two inversion-related sides as the cycle resolution doubles.

Their real traces generate the Viète nested radicals.

Thus the two-sheeted oriented Viète tower can be viewed as two distinguished compatible refinement rays inside the binary cycle-cover system.

## 11. Precision interpretation

This adds a fourth precision coordinate to the #1158 picture:

- `COVER_DEPTH m` — number of binary orientation-state refinements;
- `DYADIC ALGEBRAIC DEPTH` — nested-root/readout depth;
- `TRACE SCALE` — integer native line approximation scale when rationalizing an irrational ideal direction;
- `STATE DIMENSION` — stationary rational relational width when representing the ideal direction exactly.

At the abstract finite orientation level, each cover adds one bit of state resolution. The intrinsic scalar error theorem then shows that the Viète readout gains asymptotically two scalar precision bits per added cover bit.

## 12. Native/G1 boundary

The current native three-axis slice genuinely supplies a cyclic three-positive-ray structure, but current P000 does not yet prove that physical fixed-radius Cell rotation is **exactly** the connected binary cycle-cover tower above.

Therefore the theorem has the following strength:

- exact as a minimal connected binary refinement of the current `C3` orientation quotient;
- exact as finite group/graph mathematics;
- compatible with the G1 Viète shortest-root mechanism;
- not a promotion of `C_{3*2^m}` to primitive G0 Cell ontology.

The remaining native question is whether actual Cell transition/refinement realizes this minimal connected cover rather than another P000-compatible rotation semantics. Q29 prevents assuming uniqueness.

## 13. Main consequence

The six-gate picture now has a precision-first interpretation:

```text
three positive native ray classes (C3 quotient)
    -> first connected binary direction cover C6
       (half-turn/deck phase emerges)
    -> second connected binary cover C12
       (two quarter-turn lifts emerge)
    -> repeated binary covers
    -> shortest-root branch refinement
    -> nested-radical character traces
    -> intrinsic Pi_rot completion
    -> classical U(1) phase closure and Pi_rot = pi
```

This gives a finite-resolution explanation of why the six-state shell is the natural immediate predecessor of the Viète quarter-turn seed, without treating the old six signed carrier directions as primitive native geometry.
