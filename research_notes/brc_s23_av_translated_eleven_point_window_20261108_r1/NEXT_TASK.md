# Research frontier after exact S23/AV eleven- and sixteen-point local sorting windows

Date 2026-11-08; frozen scientific pin `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Author-side continuation preserved in Draft PR #1777. Native researcher `EM-DIRECT-502FC9`, activity `RA-A6816BD38EEFF1BFC6BD7AF8` registered to canonical Source. Formal Task Owner/CLAIM and independent proof review are separate.

## Verified exact frontier (proof files in this directory)

- `PROOF.md` + `VERIFY.py` + `RUN_EVIDENCE.txt`: exact eleven-point translated interleaving, for all 510 integers `H=9821296..9821805`. At endpoint: 130305 eleven blocks, and total 15075927373081 inverted pairs.
- `FIRST_OVERLAP_H9821806.md` + `VERIFY_FIRST_OVERLAP.py` + `RUN_FIRST_OVERLAP.txt`: exact 16-point onset at H=9821806, total 15075934741862 inverted pairs.
- `PROOF_SIXTEEN_WINDOW.md` + `VERIFY_SIXTEEN_WINDOW.py` + `RUN_SIXTEEN_WINDOW.txt`: exact 16-point translated interleaving, for all 510 integers `H=9821806..9822315`. At endpoint H=9822315: `130305` sixteen blocks, `260100` eleven blocks, `260100` six blocks, `3017438209270` four blocks, `6027363794761` swaps, and `15079685970571` inverted pairs. All remote source/code/log blobs are nonempty; executed verifiers compared complete scaled-order arrays, symbolic exact count arithmetic and strict rational log enclosure.

## Next concrete research unit

At **H=9822316**, translated sixteen-point blocks starting at x=0 and x=u first overlap. Determine the union as a contiguous old-key block, its exact true permutation, the resulting inversion count and a finite disjoint decomposition for the next H window. Candidate next merger has 21 entries, but verify against actual fiber boundaries before asserting. Test in two scaled unimodular models with M>4d, then prove finite interval by inversion-type classification.

Separately: complete entire changed-gap prefix occupancy at H=2455579 to decide the capacity N(H), rather than only sorting. The mother-model six-source/ten-label lawful observation transfer and four-observation minimax delta4 remain distinct tasks.

No credentials or confidential material accompany these proofs.