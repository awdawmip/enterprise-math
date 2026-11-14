# R5 next unit — exact nonconvex four-observer fiber

Frozen pins: GLOBAL a01383f825ef9d43b4b754254303298c64041568; EM 86149263e38c22292c9def1e0f69092efa1be77e. Mother target: determine whether K_F=K_L for W=(e_P,e_Q,T_P,T_Q) under the frozen 7-key P/Q-BRC observer.

Completed: the supports are equal for **every** real four-dimensional linear normal; in particular conv(K_F)=conv(K_L), proved by 34/26 multi-affine corners and eight exact simultaneous convex-order domination certificates. Read RESEARCH.md, VERIFY.py and EXACT_OUTPUT.txt in this directory.

Next discriminating experiment: Fix an exact FULL_HIST point with g=a=b=1, u=w=0, v=z=1/10 (T_P=T_Q=31/10, history residual 9/10), and vary the seven declaration probabilities. For selected rational W, solve the full seedless feasibility constraints (including 9bz=4a(v-z), both stopping times, both errors, all seven declaration bounds). One outcome is a rational seedless lifting; another is a complete global polynomial-infeasibility certificate. Float nonlinear programming failure is diagnostic, not proof of infeasibility.

Alternative: derive a direct observer-preserving history-erasure transformation that upgrades convex-hull support equivalence to pointwise image equality, explicitly checking whether per-run external random mixture belongs to the task's allowed seedless policy class.

R5 mother remains open; author-side source is in Draft PR #1767. Native active owner/CLAIM and mathematical admission await valid Source authority and independent review.
