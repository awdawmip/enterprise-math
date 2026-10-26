# Stage164 portable next research unit — DUAL CANDIDATE ONLY

**Mother problem:** External N14 ternary IID sequential decision minimax with full ordered-history behavioral policies. P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), errors eP=P(decide Q), eQ=Q(decide P), times tP,tQ. Define V14(alpha)=minimum max(tP,tQ) with both errors<=alpha. Preserve source/policy scopes; this is not native P000/X6 dynamics.

**Source and verified frontier:** Stage163 author proof, `PROOF_STAGE163.md`, executable `VERIFY_STAGE163.py`, exact `certificate163.json` from this handoff; Stage162 upstream R2 commit `21ddd4fc14d9ee9cc38e9b54e4bfaa6f6dac70e9`. The author-proved Stage163 endpoint is alpha163=440628382682516376365/1265046575011281764352 and V163=2138687275177334037541/180720939287325966336, both exact; Stage163 right-sharpness is for its own support line only.

**Dual-only Stage164 calculation:** Start K163=163900037061/554150611 and L163=476600779976/1662451833. Freeze R=(10,0,1) at Q/continue tie, Y=(8,4,1) as strict decide-P, and use dK=-1, dL=-10592/12501. The first positive nonminimal Bellman action gap closes at step=1764318596697/401759192975, at Z=(13,5,2) for decide-P. New candidate parameters:

K164=211248/725; L164=615448/2175.

Two ties R: Q/continue and Z: P/continue, 1238 strictly positive gaps, minimum gap=141134197/6494515200. The candidate is **DUAL-ONLY**, not a new primal optimum theorem.

**First unfinished unit:** Compute the true ordered first-hit cones and exact P/Q prefix masses for R and Z under frozen Stage164 strict minimizing decisions. Since R has zero type-0 observations at depth10 while Z has five at depth13, R cannot be ancestor of Z; Z cannot be ancestor of R by depth. Verify disjointness with integer-weight prefix DFS rather than reasoning by counts alone. Cross-check all four (R,Z) deterministic decision corners by a structurally independent `Fraction` suffix recursion; derive error-balance r(z), certify it is legal for a real interval, and check that its left boundary equals Stage163 alpha163/V163, tP dominance and Bellman equality. If a legal whole interval fails, produce its exact rational obstruction; do not claim primal optimality from dual ties alone.

**Evidence and next status:** Save actual exact counters, rational vectors, computed certificate, full verifier and proof/no-go to an immutable GitHub author research location. Report proof scope, distinct source-readback vs execution, and lack of formal Driver/CLAIM. Retain weighted ordered-history P/Q branches (BRC analogy only; no native transfer).
