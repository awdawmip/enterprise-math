# C88 proof package

Start with `C88_RESEARCH_NOTE.md` for a self-contained account of the new
results and their scope. The seven new research proof notes are:

1. `bridge/GENERAL_MOVING_POSITION.md`: the full-inventory tracking theorem
   for arbitrary moving positions; mixed spectral nondegeneracy.
2. `bridge/MOVING_ENDPOINT_BRIDGE.md`: the detailed native bridge, endpoint
   specialization, near version, Fourier weights, and grid-origin uniformity.
3. `endpoint/UNIFORM_ENDPOINT_TRANSITION.md`: the uniform two-scale formula,
   affine-window tails, and low-precision optimizer localization.
4. `UNIFORM_POSITION_OPTIMIZATION.md`: the uniform high-precision tail and
   global asymptotic optimizer location.
5. `critical/FINITE_SEPARATION_BRANCH_FILTER.md`: finite separation,
   necessary phase filters, the strengthened full-inventory bracket, and the
   remaining coupled affine lattices.
6. `POSITION_DESIGN.md`: slowly growing integer designs and realizable
   endpoint performance.
7. `ADJACENT_MIDDLE_GAIN.md`: strict full-inventory gain when the added
   middle inventory is only `c+1`.

Independent, project-internal analytic checks are recorded in
`critical/INDEPENDENT_BRIDGE_REVIEW.md`,
`bridge/INDEPENDENT_TRANSITION_REVIEW.md`, and
`endpoint/INDEPENDENT_DESIGN_REVIEW.md`. `PROOF_REVIEW.md` records the
integrating author's review and exact limits of the claims. These are not
external peer reviews or formal acceptance records.

In the delivered archive, `inputs/` contains the direct inherited proof
notes used in this turn. These unchanged notes are not republished in the
new Source directory; the repository reuses their existing immutable pins.
`SOURCE_REFS.json` gives their immutable repository identities. Earlier
theorems remain inputs at those versions; their whole historical dependency
closure is not re-proved in this package. In particular, C87's validated
integrated-kernel certificate is reused at its published source, not rerun.

No new numerical enumeration or executable theorem checker is needed for the
new proofs. The mathematical verification consists of the explicit analytic
arguments, inherited pinned inputs, and independent review notes.
`SHA256SUMS` checks the new Source files only; inherited archive inputs have
their byte identities in `SOURCE_REFS.json`. These checks concern integrity
only. An optional publication sidecar
in the delivered archive identifies the actual Source and journal commits;
it carries no mathematical or task-completion authority.
