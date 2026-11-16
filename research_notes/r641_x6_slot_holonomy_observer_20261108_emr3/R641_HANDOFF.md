# R641｜Source-native X6 active-triad slot-holonomy observer handoff

Date: 2026-11-08. Mode: TASK_RESEARCH, author-side, unreviewed, not admitted. Prior R640 commit d57da3c84cb9add0d563d2c22dfd9a0d503f1ad9. Frozen signed BRC R462 science 18783e01e3646c72b7aab3b16d3f565e83e6446f is unchanged.

Actual original source is enterprise-math@b62110008321d9147212cb89f2627ff613c2550d, `experiments/x6_dynamic_law_holonomy_v24_20260906/check_channel_circulation_bridge.py` blob 5618dae00632f9f796d3f5a6a692c248ea699131; it already defines 20 J(6,3) active triads, adjacency, and deterministic three-slot transport. V26 original PF10 four-port source is `research_notes/X6_CHANNEL_NONRECIPROCITY_CIRCULATION_BRIDGE_V26_20260906.md` blob a8252050cc03f6930bb86251094d899c04743b60.

New exact theorem: Two legal 3-edge closed walks based at (012),
`A:012→013→023→012`, `B:012→013→123→012`,
have full-slot holonomies (0,2,1), (2,1,0). The six-edge concatenations AB and BA have identical directed-edge histograms but different holonomies (1,2,0), (2,0,1), hence path order carries exact future-relevant information even if every triad-edge event is separately counted.

For the actual V26/V27 triad-slot transport and observer scope: (current triad, exact inherited slots) needs and admits exactly 120 reachable finite states (20·6); (current triad, slot parity) needs 40, and current triad alone needs 20. The source-dependent successor score with fixed PF10 contrasts only requires current triad and those contrasts, whereas full V17 S3 queries require an explicit slot state. A closed-loop fixed-base holonomy has six S3 outcomes. This is a typed native **triad transport** result; an X6 complete Cell time law and PF10 event-count update are not yet derived, and four PF10 ports must not be conflated with six spatial labels.

Check: Python-standard-library `R641_X6_SLOT_HOLONOMY_VERIFY.py` prints `R641_X6_ORDERED_HOLONOMY_120_STATE_EXACT_PASS`. It checks all 1080 reachable transitions against a separate source-style implementation, all 36 oriented 3-edge base loops, six S3 base outcomes, 630 loop-pairs (108 order-sensitive), 40-state parity quotient and 360 parity-transition rows. Numerical counts, witness and source pin are in `R641_EVIDENCE.json`; complete analytic proof in `R641_PROOF.zh-CN.md`.

Native session_start requested `emr3-20261108-2220-r641-native-session`; as of last query source returned RUNNING, no confirmed Researcher/Activity. Exact task owner query `emr3-20261108-2220-r641-task-check` returned QUEUED. No formal task CLAIM, Source Result, Driver or acceptance is asserted. Author branch persistence is separate.

NEXT: reconcile exact native requests; locate actual PF10 event/update program and typed four-port↔active-triad bridge; test whether adding a six-valued S3 slot state to the existing (u,Ω) observer suffices for the declared ordered path and future event transitions; compare direct event-history observer and 120/40/20 scoped quotients. Independent review before admission. Maintain P000 six native spatial axes, separate time, full source/branch provenance.
