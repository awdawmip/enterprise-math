# Viète native half-turn arcs: a principal root pro-state bundle section selected by sweep chirality

Status: `FREE_RESEARCH / EXACT RESTRICTED POSITIVE BRIDGE / NOT_FOUNDATION`
Date: `2026-09-05`
Researcher: `EM-FREE-7D3C9A / FREE_AXIOM_DISCOVERY`
Parent issue: `#1255`
Parent line: `#1158`
Depends on:
- `research_notes/VIETE_X6_FIXED_RADIUS_MICROTRACE_C12_20260905.md`
- `research_notes/VIETE_PHASE_REFINEMENT_VS_PRECISION_PROSTATE_CLOCK_20260905.md`
- `research_notes/VIETE_ROTATION_PRECISION_PROSTATE_FIRST_WINDING_20260905.md`
- `research_notes/VIETE_2ADIC_ROOT_GAUGE_ARCHIMEDEAN_SELECTION_20260905.md`
Checker: `experiments/viete_native_root_bundle_section_20260905/check_native_root_bundle_section.py`
Checker source commit: `317e6cd986f9422f714ee03a8464573164c91721`

## 1. Purpose

The synchronous map

\[
\text{physical trajectory time}\to\mathcal P_{\rm rot}
\]

was refuted because physical C6/C12 refinement uses a two-fine-steps/one-coarse-step clock, while the precision inverse limit uses same-residue projection and does not represent physical time refinement.

The surviving positive question is therefore:

> can an actual native trajectory object select a **precision/root lineage** in `P_rot` without treating that lineage as the physical time phase?

For oriented native half-turn arcs on the proved outer C12 microcycle, the answer is yes.

## 2. Physical C12 indexing

Use the already-proved typed cycle

\[
E_k\to G_k\to E_{k+1},
\qquad k\in\mathbf Z/6\mathbf Z,
\]

and temporal indices

\[
E_k=[2k]_{12},
\qquad
G_k=[2k+1]_{12}.
\]

On the centered-X6 OUTER native lift:

- every `E_k` is a radius-one native Cell;
- every `G_k` is read from the corresponding radius-`sqrt(2)` outer intermediate native Cell;
- one C12 successor is one primitive native Cell microstep on this restricted cycle.

## 3. Oriented native half-turn arcs

Fix a starting Cell phase `E_k`.

The endpoint half-turn is

\[
E_{k+3}.
\]

There are two sweep orientations around the same 12-cycle.

Let

\[
\varepsilon\in\{+1,-1\}
\]

record sweep chirality.

The oriented half-turn arc is the six-microstep path

\[
A(k,\varepsilon):
E_k\xrightarrow{\;6\varepsilon\;}E_{k+3}.
\]

Because `+6=-6 mod 12`, both chiralities have the same endpoint.

Their oriented half-way states occur after three microsteps:

\[
R(k,+)=Q_{12}^{3}(E_k)=G_{k+1},
\]

\[
R(k,-)=Q_{12}^{-3}(E_k)=G_{k-2}.
\]

These are distinct and opposite quarter-turn roots of the same physical half-turn.

Relative to the start, their C12 phase increments are exactly

\[
+3
\quad\text{and}\quad
-3.
\]

## 4. Native chirality produces the principal pro-state section

Let

\[
\mathcal P_{\rm rot}
=\varprojlim_m C_{6\cdot2^m}
\cong C_3\times\mathbf Z_2.
\]

Embed ordinary integers diagonally by residue at every level.

Define

\[
\boxed{
\Sigma(A(k,\varepsilon))
:=3\varepsilon\in\mathcal P_{\rm rot}.
}
\]

Thus the finite precision readout at level `m` is

\[
O_m\Sigma(A(k,\varepsilon))
=[3\varepsilon]_{6\cdot2^m}.
\]

This value is independent of the absolute start index `k`. It records the **relative root lineage of the oriented half-turn**, not the absolute trajectory phase.

## 5. Exact root orders

At level `m`, let

\[
N_m=6\cdot2^m.
\]

Then

\[
\operatorname{ord}_{C_{N_m}}([3])
=\frac{N_m}{\gcd(N_m,3)}
=2^{m+1}.
\]

The same is true for `[-3]`.

Therefore the section has the exact scale meaning:

- `m=0`: order 2 — half-turn;
- `m=1`: order 4 — quarter-turn;
- `m=2`: order 8 — eighth-turn;
- in general: exact `2^(m+1)`-th root order.

Thus

\[
\boxed{
\Sigma\text{ IS THE PRINCIPAL DYADIC HALF-TURN ROOT LINEAGE.}
}
\]

No value of standard `pi` is used.

## 6. The first physical root is exactly recovered

At C6,

\[
[3]_6=[-3]_6.
\]

So chirality is invisible at the coarse half-turn observer, exactly as it should be: both sweeps connect the same endpoint half-turn.

At C12,

\[
[3]_{12}\neq[-3]_{12}=[9]_{12}.
\]

These are precisely the two physical quarter-turn root states encountered three microsteps forward or backward from the same `E_k`.

Hence the first refinement is not merely algebraically compatible. It is anchored to the actual centered-X6 OUTER native microcycle:

\[
\boxed{
\text{NATIVE SWEEP CHIRALITY}
\longrightarrow
\text{PHYSICAL C12 ROOT PAIR}
\longrightarrow
\text{PRINCIPAL }\pm3\text{ PRO-STATE TOWERS}.
}
\]

## 7. Compatibility with the previously proved principal-root selection

The prior root-gauge theorem classified compatible primitive half-turn root towers by

\[
\mathbf Z_2^\times.
\]

It then proved:

- strict all-level normalized phase refinement leaves only `alpha=±1`;
- forward sweep chirality selects `alpha=+1`;
- reversal selects `alpha=-1`.

The corresponding pro-state integer representatives are precisely

\[
+3
\quad\text{and}\quad
-3.
\]

The present native C12 theorem supplies the missing first-layer trajectory meaning of that sign:

\[
\boxed{
\varepsilon=\text{ORIENTED NATIVE SWEEP SIGN}.
}
\]

Thus the principal tower sign is not an arbitrary external convention once an oriented native outer half-turn arc is supplied.

## 8. Time evolution leaves the precision lineage fixed

Move the start of the oriented half-turn arc one coarse phase forward:

\[
E_k\mapsto E_{k+1}.
\]

If the sweep orientation is unchanged, then `epsilon` is unchanged. Therefore

\[
\Sigma(A(k+1,\varepsilon))
=
\Sigma(A(k,\varepsilon)).
\]

This is intentional.

The precision fiber does **not** advance under physical trajectory time. It describes the root/refinement lineage of the relative half-turn operation.

Freeze:

\[
\boxed{
\text{TRAJECTORY SUCCESSOR ACTS ON THE BASE; ROOT-PRECISION ADDRESS IS STATIC ALONG A FIXED-CHIRALITY ORBIT.}
}
\]

This is exactly the clock separation required by the preceding no-go theorem.

## 9. Endpoint half-turn versus sweep reversal

Two operations now separate cleanly.

### Endpoint half-turn

Shift the entire oriented arc by six C12 microsteps:

\[
E_k\mapsto E_{k+3}.
\]

Its sweep chirality does not change. Therefore

\[
\boxed{
\Sigma(H A)=\Sigma(A).
}
\]

### Sweep reversal

Reverse the traversal direction while retaining the same endpoint pair. Then

\[
\varepsilon\mapsto-\varepsilon,
\]

so

\[
\boxed{
\Sigma(R A)=-\Sigma(A).
}
\]

At C6 this sign flip is invisible because `+3=-3 mod 6`; at C12+ it becomes visible.

Therefore

\[
\boxed{
\text{ENDPOINT HALF-TURN}
\neq
\text{SWEEP REVERSAL}
}
\]

at the precision-fiber level, exactly as required by #1255.

## 10. Translation and local rotation covariance

The section depends only on:

- the relative half-turn relation;
- the ordered sweep chirality.

Common translation of the pivot and every native Cell changes neither.

Likewise, any orientation-preserving local STAR/cycle relabeling shifts `k` but preserves `epsilon`, hence preserves `Sigma`.

A local reflection reverses cyclic orientation and therefore sends

\[
\Sigma\mapsto-\Sigma.
\]

Thus the restricted bundle section has the expected covariance:

\[
\boxed{
\text{translation / orientation-preserving rotation: invariant precision address; reflection/sweep reversal: sign inversion.}
}
\]

No claim is made here for arbitrary full-X6 rotation laws outside the established local STAR interface.

## 11. Domain memory needed to select the section

A current shell Cell alone does not determine sweep chirality because the same line family belongs to two STAR slices.

The prior centered-X6 result proved that an ordered previous/current local phase pair identifies:

- the unique STAR frame;
- the direction of sweep.

Therefore the root-bundle section can be computed from the local incoming phase edge:

\[
\boxed{
(\text{previous phase},\text{current phase})
\Longrightarrow
\varepsilon
\Longrightarrow
\Sigma=3\varepsilon.
}
\]

This gives a finite native source for selecting the **principal** infinite precision lineage.

It does not contradict the earlier finite-memory lower bound, because that lower bound applied only to the rejected synchronous `P_rot` time-odometer interpretation.

A finite state may select one of finitely many computable infinite precision addresses without dynamically traversing all of `P_rot`.

## 12. BRC branch lease

The native C12 root witness uses the OUTER microcycle.

If both shortest C6 macro-edge branches are allowed, the branch bit

\[
\beta\in\{\mathrm{INNER},\mathrm{OUTER}\}
\]

must be retained for any future operation that inspects intermediate native states or path provenance.

For the present root-bundle section, restrict the domain to the already-proved phase-refining subpopulation

\[
\beta=\mathrm{OUTER},
\]

selected within the two-shortest-path population by the requirement of a defined nonzero intermediate phase.

On that restricted domain `beta` is constant and need not be stored as an additional varying precision coordinate.

This does not erase the general BRC theorem; it narrows the domain explicitly.

## 13. Information-layer separation

The present bridge makes the three binary roles even more explicit.

1. `INNER/OUTER` — native shortest-path provenance.
2. `CELL/GATE` — physical C12 fine-clock parity.
3. `epsilon=±1` — oriented sweep chirality selecting the principal root lineage.

Deep dyadic digits of a generic `P_rot` point are a fourth, more general precision-address layer. The principal section does not expose arbitrary digits because the selected address is the computable diagonal integer `±3`.

Therefore

\[
\boxed{
\text{PATH BRANCH}
\neq
\text{PHYSICAL CLOCK PARITY}
\neq
\text{SWEEP CHIRALITY}
\neq
\text{GENERIC DEEP PRECISION DATA}.
}
\]

For the principal Viète line, chirality plus the previously proved strict-refinement selector collapses the generic precision gauge to the two computable addresses `±3`.

## 14. What this positively solves

On the declared local centered-X6 OUTER half-turn scope, we now have an exact non-synchronous bridge:

\[
\boxed{
\text{ORIENTED NATIVE HALF-TURN ARC}
\xrightarrow{\;\Sigma\;}
\{+3,-3\}\subset\mathcal P_{\rm rot}.
}
\]

It satisfies:

- exact first physical C12 root anchoring;
- all-level compatible principal root readouts;
- sweep-reversal sign inversion;
- endpoint-half-turn invariance of the relative precision lineage;
- common-translation covariance;
- local orientation-preserving rotation covariance;
- explicit BRC outer-branch lease;
- no identification of precision depth with physical time.

This is a `SUCCESS` for the **retyped principal-root bundle-section problem**, not for the original synchronous trajectory-state factorization.

## 15. Remaining frontier

The result does not map arbitrary trajectory phase states onto arbitrary points of `P_rot`.

Nor should it: the clock-separation theorem showed that such a synchronous interpretation is the wrong type.

The remaining genuinely hard questions are:

1. globalize the oriented-half-turn/root section across the relevant full-X6 rotation atlas;
2. prove the OUTER branch from an accepted native rotation law rather than only the declared nonzero-phase refinement lease;
3. integrate the existing C24 balanced-spinor witness explicitly as the second physical/typed anchor of the same `±3` root lineage;
4. formulate the general bundle/cocycle category for non-half-turn rotation increments without conflating physical phase composition with precision-root composition;
5. determine whether any non-principal `P_rot` addresses have a native history semantics, or should remain pure precision observers.

Strongest current synthesis:

\[
\boxed{
\text{THE NATIVE TRAJECTORY DOES NOT MOVE THROUGH }P_{\rm rot};
\text{ ITS ORIENTED HALF-TURN GERM SELECTS A ROOT LINEAGE IN }P_{\rm rot}.
}
\]

That is the first exact centered-X6 trajectory-to-principal-precision bridge that survives the clock-typing audit.
