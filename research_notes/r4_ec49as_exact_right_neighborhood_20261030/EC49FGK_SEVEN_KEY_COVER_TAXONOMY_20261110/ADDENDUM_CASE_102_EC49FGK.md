# EC49FGK — One no-(3,1,1) seven-key profile with fixed-inventory optimum 102

Date 2026-11-10. Frozen original BRC nine-state DFA, 24 demand labels, original signed ordered X6 microsteps, and `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.

**Chosen exact raw-key inventory:**

```
(2,1,1), (3,0,1), (2,2,1), (4,0,1), (4,2,1), (5,4,1), (6,4,1)
```

This seven-key set covers all 24 demand labels and omits `(3,1,1)`. It is a concrete member of the newly identified 1956 seven-key support covers without `(3,1,1)`.

**Exact witness:** the adjacent `WITNESS_WITHOUT_311_EC49FGK.json` lists all 24 operation words. Directly replaying the frozen 9-state DFA and signed native X6 microsteps verifies every required signature and endpoint (+2,0,0,0,0,0), seven *used* raw keys, and exactly **102 distinct nonempty ordered signed native prefixes**.

**Fixed-allowlist solver result:** reuse the prior `EC49FGF_EXACT_16_CLASS_DUAL_20261110/VERIFY_EC49FGF.py` operation-prefix MIP builder, with the precise seven-key inventory above. Local SciPy/HiGHS integer optimizer returned status 0, objective 102, dual bound 102, zero MIP gap. Its model has 10901 operation-prefix nodes, 1904 discount variables and 14728 linear inequalities. The earlier LP relaxation returned 93.66666666666667. Thus this **particular fixed seven-key inventory** cannot attain a 93-edge solution according to the solver's complete integer run, even though its linear relaxation is below 94. The lower-bound claim is solver-backed and not a separately published integer UNSAT proof; the independent 102-edge construction supplies an exact upper bound.

The adjacent `VERIFY_EC49FGK_CASE.py` is a standalone exact integer witness checker. Separate local verification using the frozen operation model's `check()` function returned `WITNESS 102 RAW_KEYS [(2,1,1),(2,2,1),(3,0,1),(4,0,1),(4,2,1),(5,4,1),(6,4,1)]`. Scope: one fixed allowed-key set, not all 1956 non-(3,1,1) seven-key covers and not global seven-key optimality. Next test: select additional structurally distinct sets, include nonminimal covers, and search for at most 93 native prefixes or extract exact lower bound certificates.

Researcher `EM-DIRECT-F4374F` / activity `RA-31878E628876370CC15873E4` (Source-recorded). Independent-author draft; no EC49AS current CLAIM, formal Result or Driver acceptance.
