# Stage493-B continuation — provenance-aware address transport

Parent: Stage492-B, under research PR #1736. Preserve frozen science inputs global bf84bd7c61a2444b59b1da96be57df0e9ae47e53; EM 2af3fc484eb11060b69e0afc1b562bcaf5ad1419; P000 source blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Read current normative context separately.

Completed: For base POP/APPEND with at most one relative-end SET, provided every pre-SET target and BOTH neighbors are surviving original directions and outside reachable P overlap, the exact additional future signature is the set of original triples at all reachable addresses. POP and an individually unobservable interior DELETE may each move the target one step earlier and reveal an extra original neighbor. Full proof and exact executed evidence are in the parent directory.

Next question 1: Allow a single interior INSERT(j,z) before a moving SET, with bounded Q POP and APPEND, and with public inserted direction sometimes becoming the edited center or its neighbor. Build a finite provenance-aware address transfer automaton: for each action prefix output current original/public source for center and neighbors. Test necessity and sufficiency of its reachable-triple signature, including possible redundancies.

Next question 2: Compose one DELETE or INSERT with one POP and one APPEND in all legal orders. Produce smallest same-observer collision witness if the simpler original-triples key fails. Give exact directed edge corrections including interaction terms.

Next question 3: In X6, retain 12 signed directions, all 144 potential ordered-edge coordinates, Boolean support distinct from exact integer raw population. Test sparse Euler–BRC counting/ranking on genuinely high-support instances; account for input construction, representation and rank/unrank output cost.

Formal Source CLAIM/Result/Review requires an actually authenticated native session and correct current owner; current Site gateway reported BACKEND_IDENTITY_OR_VERSION_MISMATCH with operation_sent=false. Author-side GitHub PR is evidence storage, not native admission.
