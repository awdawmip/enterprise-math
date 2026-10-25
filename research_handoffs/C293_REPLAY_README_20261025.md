# C293 portable readback & reproduction

These author research files are preserved on an isolated GitHub research branch. They do not constitute formal Source publication or independent Driver acceptance. Original local complete archive: EM_C293_125_DYADIC_NEWTON_EXACT_PORTABLE.zip (2026-10-25), SHA256 5243b50d32215ca845701191e3c07b9ec403ec7e7a9be632d7fed423b605c412.

Use the **exact matching frozen** C275_STANDALONE_EXACT_REPLAY.py, C284_187_EXACT_DYADIC_BRACKETS.json, C288_ISOLATING_BOXES_EXACT.py, C290_PADDED_CHART_EXACT.py, C291_HESSIAN_EXACT.py, C291_INDEPENDENT_SECOND_JET.py and C292_VERIFY.py from the complete portable archive, in the same directory as the C293 files.

Run from that directory:
  python C293_AUTHOR_VERIFY_EXACT.py
  python C293_INDEPENDENT_PRODUCT_CHECK.py

The independent checker is a separate implementation of the 79-positive-branch product, plus 16 finite dual-jet diagnostics. It is *not* a general proof over every continuous thick box.

The full analysis/proof is in C293_AUTHOR_THEOREM_AND_PROOF_20261025.md. Original upstream pinned commits and exact evidence qualifications are in that proof. No substitutions of similarly named older code versions without checking the hash/semantics. The recent attempt to replay all C290/C292 full-box calculations timed out and produced no full completion receipt, so the dependent Newton theorem is explicitly conditional on the earlier C290/C292 author certificates.

Next research unit C294: uniform parameter-perturbed Newton-map once-step remainder/error and derivative propagation. Pending formal Owner/CLAIM/Result/Driver. Global snapshot 6a246ed94efb5ed584cefd4b0720171067bd94c2, Enterprise Math source snapshot ac9ec4f8065d21239ec9f3d76e9b15924bea65ae.
