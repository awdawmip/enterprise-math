# R62 actual verification and authority status

Scientific pin: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`; predecessor R61 Draft PR #2055@358023379ffe8016b8856d83b8440c8bad2ffc0f; date 2026-11-11.

Full author source locally executed: `CHECK_R62.py` using Python exact `Fraction` and integer arithmetic; actual generated `R62_CERTIFICATE.json` recorded below. GitHub's `CHECK_R62_MIN.py` is also independently run and contains the exact m=2 witness, three S23 sparse label checks and 704-difference margin. The full longer program and expanded certificate are provided separately in the complete R62 handoff bundle.

Full run: 500 base cases / 2,509 certified queries / 12,545 exact oracle checks / 15,253 older sources bypassed by certificate; 3,885 near-crossing queries, 1,414 certified / 2,471 rejected / 2,031 endpoint divergences / 7,070 independent checks; 120 huge-anchor cases / 3,736 exact phase transport identities; S23 128 certified label queries / 256 endpoint oracles / 21,336 source-boundary noncollisions; 704 integer differences, minimum margin 1538749354821431426740.

Project native service: `session_start` initially returned QUEUED, later `em_control_result` returned `BACKEND_IDENTITY_CHECK_UNAVAILABLE` and `operation_sent=false`. A live Researcher-ID, Activity-ID, S23 Owner/CLAIM and native Source checkpoint could not be established from this service. This GitHub branch is an independent author-side durable science artifact, not a formal task claim/Result, nor a mathematically independent review.
