# R428 durable handoff / next problem

- **Object:** original signed BRC auxiliary coefficient H(r,s) from R427, not Heartbeat X6 dynamics.
- **Completed:** exact fixed-right-edge asymptotic H(r,r-h)/(Cat(r)*r^h)->1/h! for every fixed h; strict eventual positivity of every fixed admissible Toeplitz minor of the reversed edge, of any fixed order; explicit third-order right-edge formula Delta_r/Cat(r)^3=(r-2)(r+2)(r^2-2r-9)/(3(2r-1)), negative at r=4, positive at all integers r>=5.
- **Proof mechanisms:** signed branch-preserving binomial difference (equations 1-4); Pascal binomial minors and concrete disjoint monotone paths (equation 5); exact factorial cancellations (equations 6-7).
- **Evidence:** R428_PROOF.zh-CN.md, R428_VERIFY.py and R428_EVIDENCE.json; exact integer checks, source definition cross-check, 1204 Pascal minors and 4816 right-edge minors, finite parameter range specified in proof.
- **Unresolved:** no explicit R(K) for an arbitrary bounded window; no PF3 classification for full rows r>=25; no proof of a growing-window positivity scale, no X6 native transfer. No formal Source CLAIM/Result or independent review.
- **Next executable question:** derive uniform rational error bound |H(r,r-h)/(Cat(r)r^h)-1/h!| valid for 0<=h<=K, translate determinant margin for Pascal minors into explicit sufficient r>=R(K). Seek counterexample to overly strong bound if needed.
- **Read provenance:** GLOBAL_KNOWLEDGE_V1 main@0ef0983353275a71778fe8071d7742c8173d1332; Enterprise Math main@cf4dc7ae3d5c91f3659bc16d603877164db812ec; R427 original 3951756a5cd8b0da0a6f80fd57dedc617dee160d.
- **Auth:** author-side portable research, no permission to impersonate a Source owner or promote mathematical acceptance; P000 and ACTIVE worldview unchanged.
