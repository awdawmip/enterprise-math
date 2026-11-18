# Stage244 portable continuation — author-side auxiliary IID minimax

**Mother objective:** determine exact full-real optimum V14(α) for P=(3,1,20)/24, Q=(2,2,20)/24, horizon N=14, all full-history randomized stopping strategies, with e_P≤α and e_Q≤α; objective min max(t_P,t_Q).

**Frozen verified author-side frontier:** Stage243 (see `PROOF_STAGE243.md`, `stage243_exact_analysis.py`, `CERT_STAGE243_EXACT.json`) proves `V14(α242+δ)=V242-(33611704152/292565255)δ` for all real `0≤δ≤1462826275/3900793946112`, with `α243=4372969427965/11702381838336` and `V243=10415008236599/1462797729792`. The Stage243 dual face has 13 binary ties, 8192 exact deterministic corners, exact all-history DFS and global supporting-line certificates.

**First unresolved mathematical question:** determine the first *primal-feasible, nonzero-width* dual supporting face immediately right of α243. Enumerate genuine Bellman ties and exact positive gaps; watch out for floating-search degeneracy and unreachable/zero-width changes. Find the legal balanced error slice with exact rational endpoint witnesses and `t_P>t_Q`, or prove the obstruction with full rational inequalities. Require exact endpoint continuity, a strict-right support check and coverage of arbitrary real α/full ordered histories. Numerical occupancy-LP candidate λP≈54.89137515, λQ≈59.16853136 is **uncertified discovery only**; its observed 13 P/C near-ties do not establish an exact dual face or primal interval.

**Evidence acceptance:** publish exact dual and 680-state Bellman certificate, independent exact integer DP/ordered-history verification, support lines/convex-hull certificate or exact no-go, actual proof and next question. Label `AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED` until formal independent Driver/Source process. No P000 native-X6 transfer or native BRC execution by name alone.

**Source pins:** GLOBAL_KNOWLEDGE_V1 `main@858c07fc2fb6cb0294ec36eb1696506d70d3c7d7`, Enterprise Math `main@194319dde91018e04f609a3f81cd3dbfb22cdad6`; prior PR #1571 head at intake `f12577e24d11dfe178f596935adfadf8c68f1496`. Each successor rechecks its actual live control and writer authority without borrowing any historical session.
