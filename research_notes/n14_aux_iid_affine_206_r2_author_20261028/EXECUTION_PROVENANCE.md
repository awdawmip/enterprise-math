# Stage206 provenance and verification scope
Date: 2026-10-28 (Asia/Shanghai). Classification: PORTABLE_AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED.

Run source inputs: Stage205 immutable author commit 256c6fefc55254d58dd3f7cca5b30456b4313785, global main a935c2321a618259b517ed476e73b3b0d81fca60, Enterprise Math main 9b67d426c1eaed49ed517342e0b4a226ca572b6d.

Local execution (Python standard library Fraction):
- verify_stage206.py: STAGE206_AUTHOR_EXACT_FULL_REAL_PASS 313384; SHA256 b8e399b65ae8705b5c27d4dabe45a0f4706442c07d69d9fc2fad531fbf46f119.
- Independently authored REPRO_STAGE206.py: STAGE206_REFERENCE_EXACT_PASS 313384; SHA256 a6b9e0181c12554dafe0ad6d14ca4c8bde25eab34efdf38c82f52a4eb51717a0.
- Derived reproducible REPRO_STAGE206_DERIVED.py (stored here as REPRO_STAGE206.py): STAGE206_DERIVED_REFERENCE_EXACT_PASS 313384; source Git blob expected f28ca3260c0a2b91a3d4cfd33c941377a3848820.
- scan_stage207.py: STAGE207_DUAL_SCAN_PASS; SHA256 8d6064da98e052233eed6e5bcca2d808db7840125111de7685acb11a0d72c303.
- Derived next scanner from the prior immutable source: STAGE207_DERIVED_DUAL_SCAN_PASS, mathematical output agrees with independent scanner.
- Four deterministic corner observations match across exact conditional suffix dynamic program and independent unmerged integer-mass DFS. No joint W/Z paths. Counts [79726,79726,76966,76966], total 313384.
- Precise machine-readable rational observations and the next dual scan are in the two certificates.
- GitHub connector byte readback establishes storage, not GitHub-side execution or independent mathematical acceptance.

Scope limit: finite external IID decision model only. No native X6 Cell dynamics, original P000 modification, native Source CLAIM/Result, or independent Driver review.

Native snapshot diagnostic: em_status version 0.6.11 research_authority_granted=false, executor_binding_configured=false, control state CODE_REVIEW_REQUIRED; em_control_tasks attempted on 2026-10-28 returned CONTROL_QUOTA. Active canonical Task owner remains unconfirmed from this path. Portable author materials are a distinct allowed evidence publication lane.
