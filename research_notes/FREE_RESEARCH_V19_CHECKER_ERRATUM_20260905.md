# V19 Checker Erratum

Status: `CORRECTION / SUPERSEDES FIRST-DRAFT FIXTURE ONLY`
Date: `2026-09-05`
Researcher-ID: `EM-FREE-PI-PRIME-20260905`

The first draft script

`script/check_free_research_growing_depth_commutator_frame_v19.py`

used an arbitrary diagonal matrix in its finite test fixture.  The arithmetic mass identity

\[
\Delta_k1=A\mathcal C_k-(k+1)\mathcal C_{k+1}
\]

requires the carrier normalization

\[
M_A1=L1.
\]

That normalization was not imposed by the first fixture, so the first script must not be cited as verification of the mass identity.

The corrected checker is

`scripts/check_free_research_growing_depth_commutator_frame_v19_corrected.py`.

It defines the diagonal multiplier from the row masses of the positive history operator, verifies `M_A 1 = L 1` explicitly, and then checks the derivation identity, mass identity, placement frame, parametrix, and nilpotent no-go using exact `Fraction` arithmetic.

The mathematical statements in the V19 research notes are unchanged; this erratum concerns only the original synthetic fixture.
