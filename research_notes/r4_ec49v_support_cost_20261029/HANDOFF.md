# EC49V — author-side durable handoff
Frozen scientific parent: EC49U Draft PR #1668, immutable commit `b2ce9c962ffb662f31fb1166c5c2641f1eb0fa2b`. Scientific input pins and external prior art in `SOURCES.md`.

**Reproduce:** In this directory, `python REPRODUCE.py` (Python stdlib; `EC49U_VERIFY.py` is the exact Git blob copied from parent). The author separately executed an exhaustive Fraction affine-arrangement checker (125 prefixes, 9 local-mask cells, 13 global cells), plus exact cost certificate. See `PROOF.md` and `EXACT_REPORT.json` / `FACE_REPORT.json` for verified results. The GitHub copy of REPRODUCE.py was copied from the locally executed source, and the parent Git blob is reused exactly.

**New theorems:** For all real eta in [0,1/2), h(eta)=max(1/27,eta/6-1/36), switch 7/18; fixed-cost at eta=1/200 has legal behavioral lower delta=59/576, all-behavioral upper delta=11/96, and full-vs-compressed discrimination gap at least 1/32. The upper is attained in the convex hull using a shared seed, not proven in the actual behavioral class. The exact behavioral face is OPEN; follow EC49W.

**Control:** Native `session_start` returned `STATIC_READONLY_SCOPE_DENIED`; `em_control_tasks` returned `CONTROL_QUOTA`; no native session/claim/Result/independent review. This draft PR is independent author-side storage only, not an active owner's work and not canonical theorem admission. Source-exposed, not blind-independent. Protected P000 and ACTIVE worldview unchanged.
