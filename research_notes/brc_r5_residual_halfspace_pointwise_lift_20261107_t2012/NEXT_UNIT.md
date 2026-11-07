# R5 next unit — joint seven-key nonconvex reverse-residual fiber

Frozen scientific pins: GLOBAL `a01383f825ef9d43b4b754254303298c64041568`; EM `86149263e38c22292c9def1e0f69092efa1be77e`. Mother: determine whether FULL_HIST and seedless LR have the same *actual* four-observer image `(e_P,e_Q,T_P,T_Q)` under the frozen four-stage, seven-key observer.

**Completed and not to redo:**

- All real four-dimensional linear supports, and hence convex hulls, coincide (previous R5 result `f20b9a0bdc8c1fc8f69a2abeb7c231181d1a0d27`).
- `RESEARCH.md`: all real FULL_HIST flows with `R=9bz-4a(v-z)>=0` and arbitrary seven terminal declarations admit explicit pointwise *single-process* seedless lifts preserving both stopping times and both errors.
- `REVERSE_CORNER_RECTANGLE.md`: although `R=-9/10` at `x=(1,1,1,0,9/40,0,0)`, **every** two-extreme-key declaration `d_0=s,d_6=t`, all other d's zero and `s,t in [0,1]`, admits an explicit single-process seedless lift using `y=(1,19/20,19/20,0,11/40,0,11/130)` and `d'_0=335s/363,d'_6=335t/363`. Both stopping times equal 129/40.

**Smallest still-open discriminating unit:** At the same R<0 corner, include declarations of the LR=1/2,3/4,1,5/4,3/2 keys rather than rerunning the solved extreme-tail rectangle. For each rational W candidate, solve *globally over all legal seedless flows*, seedless bilinear equation, both times, both errors and all declaration bounds. A valid rational lift or rigorous global polynomial infeasibility certificate is a meaningful outcome. Fixed-flow failure and floating nonlinear solver failure are not such certificates.

**Parallel analytic option:** Derive a general observer-preserving transformation of negative-R flows by changing early flow parameters `(g,a,b,u,w)` while preserving time; test whether it uniformly Blackwell-dominates the original LR experiment. Preserve the nonconvex image distinction; do not replace it with the completed support-function theorem.

**Exact reproducibility:** `python3 VERIFY.py`, `python3 VERIFY_REVERSE.py`; corresponding captured files `EXACT_OUTPUT.txt`, `OUTPUT_REVERSE.txt`. Status: author-side checked, unreviewed, no native CLAIM due to Source backend identity/version mismatch.
