# Stage144 — exact dual-only candidate; primal theorem still open

Scope: external ternary iid N=14 P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), arbitrary randomized **ordered** prefix tests, stop by 14. Errors eP=P(decide Q), eQ=Q(decide P); minimize max(tP,tQ). No P000/X6/Heartbeat transfer.

Stage143 author-proved endpoint: alpha143=1529836197244652353/4400701866044817408, V143=1503998623662640921/122241718501244928. Stage143 dual K143=19411949464309662/45614547809953, L143=18882041753802888/45614547809953. B=(11,0,1) Q/continue has interior Q-stop coin 6345912551670737/10179840000000000; C=(3,3,0) P/continue is saturated P-stop=1.

Along the B tie-preserving dual ray dK=-43/1536, dL=-7/288, C strictly favors P. The earliest of **833** positive directional action-gap closures is at

```
lambda144=15535936721619293184/45204016879663423
K144=412200/991
L144=401944/991
Hroot144=1347680099447446704127/4523958038641508352
new tied state R=(11,2,0): P versus continue
old tied state B=(11,0,1): Q versus continue
```

Fresh exact 680-state Bellman at this candidate: 2 ties, 1238 strictly positive remaining gaps, 0 negative gaps; minimum positive gap 392134385/79895973888. This is **dual-only**. No Stage144 primal feasibility or right-sharpness theorem is claimed.

**Next exact unit:** determine R and B literal first-hit counts and P/Q masses. Use backward Fraction observer recurrence and a separately implemented literal integer-weight DFS for four deterministic corners. Check disjoint cones, and keep previously fixed C P-stop. Solve eP=eQ for both coins; check coin feasibility, alpha growth from alpha143, tP>=tQ, primal equality with Hroot, and strict right sharpness. An exact infeasibility witness also counts as progress. This remains an external auxiliary BRC-like positive weighted path model; do not silently identify it with native Heartbeat/BRC–Shor.

Input pins: GLOBAL_KNOWLEDGE_V1 main@a7b8a07c3e007b62749724b848c8d96a681e2868, initial Enterprise Math main@77698674b3e3d50ff916d474b309e0a4e906b622, Stage142 proof blob 4ba1af74b0f644a2ba38c3d06a9b6dbc4859f727. Author code and exact logs in local Stage143 archive. Native task list CONTROL_QUOTA; session start STATIC_READONLY_SCOPE_DENIED, operation_sent=false; no verified native CLAIM/Result or independent Driver review.
