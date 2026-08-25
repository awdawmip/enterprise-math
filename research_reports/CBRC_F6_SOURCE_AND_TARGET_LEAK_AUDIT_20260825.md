# CBRC F6 — Source and Target-Leak Audit

Researcher-ID: `EM-CBRCF6-D694C8`

Task-ID: `RS-CBRC-F6-MINIMAL-RANK-TWO-CONSERVATIVE-CARRIER-CLASSIFICATION`

Owner branch: `research/cbrc-f6-minimal-rank-two-conservative-carrier`

Taskbook source: `e5d3c761e291b3193ccbbd85a4a2b05c70338141`

Raw-freeze / Checkpoint-A head: `e8903934f01af9fade5979ebf2507b763b6aea50`

Audit verdict:

`TARGET_LEAK_AUDIT_PASS`

## 1. Publication-liveness gate

Before any mathematical source was opened:

- fresh Researcher-ID allocated: `EM-CBRCF6-D694C8`;
- owner branch was verified to exist at the taskbook-issuance commit with no prior F6 execution work;
- `evidence/cbrc_f6_execution_stamp.json` was committed as `a741fe611e62fbf54f9c5462ffb9f4a450f49d86`;
- the remote owner branch was verified to resolve exactly to that stamp commit;
- the stamp recorded `phase=STARTED_BEFORE_MATH`, `carrier_verdict=null`, and `math_source_read_before_stamp=false`.

Only after this verification was the blind mathematical packet opened.

## 2. Mathematical source actually used before raw freeze

Exactly one mathematical source was opened and used:

`research_inputs/CBRC_F6_BLIND_MINIMAL_RANK_TWO_CONSERVATIVE_CARRIER_PACKET_20260825.md@d0991001455a0a40a50f66ac6c14595448d29f21`.

No other mathematical file was read before Checkpoint A / raw freeze.

The taskbook itself was used only as specification and routing authority.

## 3. Procedure/governance material read

The following nonmathematical material was used only to execute the repository protocol:

- account-level `GLOBAL_KNOWLEDGE_V1` bootstrap and operating manual;
- GitHub branch/commit metadata needed to identify the taskbook source and remote frontier;
- the existing F5B execution-stamp JSON only as a formatting/procedure example.

None of these supplied a mathematical premise, a candidate rank-two carrier, or a unary-lift target.

## 4. Withheld / forbidden source audit

Before raw freeze, the researcher did **not** open or use:

- the full historical F1 review or its withheld torsion-free counterfactual;
- R063, R064, R065, or FQ mathematics;
- downstream coherent-BRC/wave research;
- external quantum mechanics or related physical formalisms;
- any source presenting a known rank-two target answer;
- complex, Gaussian, Eisenstein, or other quadratic carriers as targets;
- roots of unity or phase groups;
- rings, fields, multiplication, norms, inner products, quadratic/square laws;
- Hadamard/Fourier/splitter targets;
- any two-slot mixing or scalar-law classification.

The F5B Driver review named in taskbook dependencies was not opened as a mathematical source; the blind packet already froze the only upstream facts authorized for F6.

## 5. Discovery-language audit

The derivation was carried out entirely in the language of finitely generated additive abelian groups, a typed old embedding/retraction, finite torsion, and additive automorphisms.

The rank-two normal form was obtained from the retraction splitting and the structure theorem, not by selecting or naming a familiar rank-two number system.

The unary classification was obtained by writing the most general projection-covariant images of the new free complement and solving the exact finite congruence relations. No target matrix, norm, scalar multiplication, or downstream wave object was used as a selector.

## 6. Target-independence audit of the final minimizer

The least carrier is selected by the issued lexicographic order:

1. preserve the frozen upstream layer;
2. minimize torsion beyond the already forced order-three `tau`;
3. add only the one forced new free generator;
4. minimize new unary action on that generator.

The unary minimizer is characterized invariantly as the unique lift class admitting a complement on which all inherited unary maps act trivially. This criterion refers only to added unary structure/data and does not appeal to resemblance to any downstream algebraic object.

## 7. Exact pushed-checker identity and result

Checker path:

`scripts/cbrc_f6_validate_minimal_rank_two_conservative_carrier.py`

Checkpoint-B checker commit:

`e673df1842fd371a66fb827c1f6b8d8a5e02c487`

Remote Git blob SHA-1 returned by GitHub:

`be8f34e8d10bd934497439d8fabd231b82480020`

The locally executed byte sequence had the same Git blob SHA-1, so the executed checker was byte-identical to the pushed checker.

Byte count: `17810`

Checker SHA-256:

`682c3ba50ede00bf5cad9ea948e03b8542f1d8a0ded927c2aef34664bd2e9b2a`

Deterministic stdout SHA-256:

`1cf4c992156d34f12183d7b160805c332e31b146704d3f0bea96429a8e329e7e`

Execution result:

- exit code: `0`;
- status: `PASS`;
- finite-presentation / SNF examples: `C_min -> free rank 2, torsion [3]`; `C_9 -> free rank 2, torsion [9]`; `C_33 -> free rank 2, torsion [3,3]`;
- bounded primitive embedding regression: `48` primitive and `32` nonprimitive vectors at bound `4`;
- exact valid unary parameter cases: `22`;
- typed gauge equivalence classes: `6`;
- unique minimal unary class: `true`;
- composition depth: `4`;
- words checked across all lifts: `2662`;
- upstream generator comparisons: `5324`;
- theorem/model mismatches: `0`;
- all required ablations: passed their expected exact distinction checks.

## 8. Conclusion

No mathematical source outside the F6 blind whitelist influenced the raw discovery or classification, no forbidden target structure was used directly or indirectly as a tie-breaker, and the exact pushed deterministic checker passed with zero theorem/model mismatch.

`TARGET_LEAK_AUDIT_PASS`
