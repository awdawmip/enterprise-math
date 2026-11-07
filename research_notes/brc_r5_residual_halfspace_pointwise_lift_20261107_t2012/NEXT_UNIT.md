# R5 next unit — exact reverse-residual nonconvex fiber

Frozen scientific pins: GLOBAL `a01383f825ef9d43b4b754254303298c64041568`, EM `86149263e38c22292c9def1e0f69092efa1be77e`.

Mother target: determine whether `K_FULL=K_seedless` for the actual four-dimensional observer `(e_P,e_Q,T_P,T_Q)` in the frozen four-stage seven-key P/Q-BRC model. Equal convex hulls were proved in `research_notes/brc_r5_four_observer_convex_hull_20261107/` at `f20b9a0bdc8c1fc8f69a2abeb7c231181d1a0d27`. **Do not redo that part.**

This unit just proved a *constructive exact single-process lift* for every FULL_HIST flow satisfying `R=9bz-4a(v-z)>=0` and every terminal declaration vector. All-real proof and runnable `Fraction` checker are in this directory. The R<0 fixed-flow declaration transfer sometimes succeeds too, but its failure alone cannot separate the global nonconvex images.

**Smallest remaining exact unit:** Choose the R<0 corner `(g,a,b,u,v,w,z)=(1,1,1,0,9/40,0,0)`, with residual -9/10 and both times 129/40. For selected rational seven-key declarations, solve *global* seedless feasibility: all early flow variables, `9*b*z=4*a*(v-z)`, both times, both errors, all declaration bounds. Provide an actual rational lift or an exact polynomial infeasibility certificate. Float optimizer failure is merely exploratory.

**Alternative route:** Construct a change of `(g,a,b,u,w)` preserving these stopping times which makes a seedless experiment Blackwell dominate the reverse full corner, then recover declarations. A success enlarges the same-image domain; a verified obstruction focuses the nonconvex question.

Source status: author-side portable research; native owner/CLAIM unconfirmed due to service backend identity/version error; independent mathematical review not yet performed. Command to verify the current solved half-space: `python3 VERIFY.py` (captured stdout `EXACT_OUTPUT.txt`).
