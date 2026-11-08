# NEXT: bridge kappa from 19/20 to 1

Input: same frozen seven-node P/Q-BRC observer as research_notes/brc_r5_kappa_prism_20261108_t11/RESEARCH.md. Do not change previous scientific input pins, P000, task ownership, or seven likelihood ratios.

Smallest discriminating point:
(t,p,q,theta,kappa)=(1/50,77/152,17/2112,1,1).
For the old explicit a'=z'=0 target, v'=9/40+9/800>9/40, an exact *target-capacity* obstruction. Test a legal target in a different seedless chart: choose positive a', a matching z' and v'-z' with 9b'z'=4a'(v'-z'), enforce T_P,T_Q exactly, and solve seven Q/P moment constraints for a nonnegative kernel. A success enables a new chart; then seek a shared chart on its neighboring rational corners and an overlap with the proved kappa≤19/20 prism. A failure of one chart is scoped to that chart.

Parallel route: move p>77/152 or q<17/2112 by choosing a new seedless target; current a'=z'=0 chart hits exact u'/w' capacity faces. Record each exact kernel, its support, and all seven likelihood-ratio moment equations. Reuse PR #1813 and this round's sparse certificates.

Scientific theorem status: AUTHOR_PROVED / UNREVIEWED. Native Task Owner and formal CLAIM must be independently verified before any shared task state mutation. Exact evidence is in RESEARCH.md and VERIFY_KAPPA_PRISM.py.
