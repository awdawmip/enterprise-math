# X6 native time — Unit232: OUTER-C12 macroshift/reflection holonomy obstruction

Date: 2026-11-21 12:00 Asia/Hong_Kong. Task: `RS-X6-NATIVE-TIME-DYNAMICS`, parent `PO-X6-UPPER-STRUCTURE-20260906`. Author lineage: Researcher `EM-X6-FB6990`, session `MCP-082892eb480e45dea6d4b9fcc0491034`, original Research lane `chatgpt-research-onhour-enterprise-math-20260923`. **AUTHOR_PROVED / EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED.**

## Immutable source and exact target

Scientific pin: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`.

- `p000_reality_foundation.json`: six signed native spatial axes; time orders relational changes, not a seventh spatial axis.
- `research_notes/VIETE_X6_FIXED_RADIUS_MICROTRACE_C12_20260905.md` §§3–8: restricted OUTER branch has twelve **distinct native Cells** and twelve primitive signed-axis Links, with `E_r=a_r`, `G_r=m_r=a_r+a_{r+1}`, `a_{r+3}=-a_r`.
- `research_notes/VIETE_NATIVE_HALF_TURN_PRINCIPAL_ROOT_BUNDLE_20260905.md`: relative principal-root address `Sigma=3 epsilon` changes sign under sweep reversal but stays static under phase-origin translation; this is a typed observation, not a physical fiber update.
- Unit231: `research_notes/X6_TIME_NATIVE_OUTER_C12_LINK_CIRCULATION_NO_GO_20261121_1100.md`: every homogeneous orientation-odd signed-axis increment yields zero loop holonomy; the conditional edge-specific `H=6` example has no source-backed physical selection or fiber readout.

Here we test what **additional symmetry hypotheses** would allow or exclude that particular conditional `H=6` mechanism. They are explicitly hypotheses about an internal additive fiber `A`, not a newly adopted physical law or P000 extension.

## Native signed-Cell witnesses for the relevant graph symmetries

Choose three native axes in the frozen STAR slice:
`a=(e1,e2,e3,-e1,-e2,-e3)`, `v_{2r}=a_r`, `v_{2r+1}=a_r+a_{r+1}` (indices mod 6/12).

There are two explicit signed-permutation **graph automorphisms** of this restricted Cell cycle:
- `R(x1,x2,x3)=(-x3,x1,x2)`, sending `v_q` to `v_{q+2}` (the one-macrostep phase shift);
- `S(x1,x2,x3)=(x1,-x3,-x2)`, sending `v_q` to `v_{-q}` (a parity-preserving reversal of the C12 cycle).

Both maps preserve primitive signed-axis adjacency on this chosen STAR slice. We do **not** assume they act as physical time evolution or that arbitrary native dynamics must respect both: covariance of a proposed fiber update is tested separately.

Write `e_q:v_q -> v_{q+1}` for each forward directed Link and `w_q in A` for its additive fiber increment. Traversing a Link backwards gives `-w_q`. The clockwise circuit increment is `H = sum_{q=0}^{11} w_q`.

## Exact symmetry-covariant holonomy theorem

**Hypotheses.** Suppose a proposed reversible Link update is (i) covariant under the local macroshift `R` with trivial action on the fiber, so `w_{q+2}=w_q`; and (ii) covariant under the local reflection `S`, acting on the fiber by an involutive additive automorphism `theta:A->A`, so `theta(w_q)=-w_{-q-1}`.

**Theorem.** There is an `a in A` with the full edge field
`
w_{2r}=a,  w_{2r+1}=-theta(a),
`
and all such fields satisfy
`
H=6(a-theta(a)),   theta(H)=-H.
`
Conversely, every `a in A` defines a field satisfying both symmetries. Consequently the **exact attainable holonomy subgroup** under these hypotheses is `6 Im(id-theta)`.

**Proof.** Two-step shift covariance makes all even edge weights equal to `a`, all odd equal to `b`. Since `S` maps forward `e_q` to the inverse of `e_{-q-1}`, parity is exchanged, so reflection covariance is precisely `theta(a)=-b` and `theta(b)=-a`. The first gives `b=-theta(a)`; the second follows using `theta^2=id`. Six even and six odd edges yield `H=6(a+b)=6(a-theta(a))`. Applying `theta` yields `-H`. Conversely these assignments satisfy every required relation. This is an exact infinite-group proof with no finite-modulus assumption.

**Corollary 1 (orientation-even fiber).** With `theta=id`, `b=-a` and `H=0` for every abelian fiber `A`.

**Corollary 2 (orientation-odd fiber).** With `theta=-id`, `b=a` and `H=12a`. In the precision readout `A=C_{6*2^m}`, for every `m>=1`, no field in this class can have `H=[6]`: the congruence `12a=6 (mod 6*2^m)` implies `2a-1=0 (mod 2^m)`, impossible because the left side is odd. Thus the candidate `H=6` is excluded even when the fiber itself changes sign under reflection, **provided both symmetries and their stated fiber actions hold**.

At `C24`, the allowed orientation-odd holonomies are exactly `0,12`; at `C48`, exactly `0,12,24,36`. At `C12` both `theta=+id` and `theta=-id` yield `H=0`. The restriction comes from the explicit pairing of six even and six odd native Link increments, not from ordinary signed-axis homogeneity.

## Independent minimal repairs / distinguishing experiment

The assumptions are genuinely independent:

1. **Keep macroshift covariance but drop reflection-sign covariance:** `w_{even}=1,w_{odd}=0` gives `H=6`, and is reversible on each Link. This model retains Cell/gate parity as an internal Link distinction.
2. **Keep reflection-sign covariance but drop macroshift covariance:** `w_5=w_6=3`, others zero, gives `H=6`. Indeed `w_q=w_{-q-1}` is exactly the `theta=-id` reflection condition. This model has a distinguished phase location.

These countermodels identify the missing structure needed to evade the no-go: a symmetry-breaking Link/Port state, a nontrivial macroshift action on the fiber, an affine/non-additive update, or a different physical symmetry contract. We have **not** proven any of those mechanisms is physically selected.

A source-backed observation distinguishing these cases must give a real independent `z` readout and an event rule (including its action under the actual macroshift and reflection). At an unchanged Cell after one full positive cycle, the candidate `H=6` yields `z_{+12}-z_0=6 mod N`; if the two explicit symmetry hypotheses hold with `theta=+id`, the result must be 0; with `theta=-id`, it must lie in `12A`. A negative-cycle observation independently tests reversibility. At C24 a measured `6` would refute the **combination of model assumptions** just stated, not P000.

**BRC observer boundary.** Population: the frozen twelve forward oriented primitive Links on the OUTER branch of one selected STAR slice. Observer: additive independent fiber holonomy after a complete circuit, with optional chirality and macroshift/reflection operations. The Cell-only endpoint, event count, fixed `Sigma`, Link incidence, and deep precision address are different observers. No quotient to endpoints is made for future Link or path queries.

## Reproduction and evidence scope

`research_checks/X6_TIME_OUTER_C12_MACROSHIFT_REFLECTION_HOLONOMY_CHECK_20261121.py` enumerates actual signed three-axis vertex/edge maps, then all `(a,b)` mod `6,12,24,48,96` for both `theta=+id` and `theta=-id`, and verifies the two independent `H=6` escape fields. Exact integer arithmetic: **25,768 assertions; 0 mismatches**. The finite computation checks the stated residue examples; the proof above covers general abelian `A`.

## Remaining mother-objective dependency

Find a *frozen/source-backed actual* Cell/Link/Port internal update with a declared transformation law for its fiber and a readout at the same Cell before and after the clockwise and counterclockwise OUTER loop. Test its actual covariance, rather than assuming all graph automorphisms are dynamical symmetries. The original R063 six-file native benchmark remains a separate unexecuted evidence item. No independent Driver review, Result freeze, P000 change or physical acceptance is asserted here.
