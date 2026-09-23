# p^15/H10 verification transcript

Status: STAGED VERIFICATION EVIDENCE ONLY / NOT SOURCE-PUBLISHED / NOT RESULT.

Companion local checker: `check_finite_3f2_p15_h10_boundary_defect_20260923.py`.
SHA-256: `204af2ce8559cc103d639510ffdcb5725b467f530a001c3ee9a0ced14e8e1597`.
Observed local file size: 2435 bytes.

The checker was executed again after the proof note was finalized. It independently computes `U_p` from the original three multiplicative ports modulo `p^12`, computes the H2/H4/H6/H8/H10 formula separately, computes `F_p,F_p',F_p'',F_p'''` directly from the finite hypergeometric recurrence modulo `p^15`, and compares the compact jet certificate.

Observed output:

```text
primes 166 classes {13: 83, 19: 83}
U12_failures []
J15_failures []
```

Scope of finite check: every prime `p < 5000` with `p ≡ 13 or 19 (mod 24)`, 83 primes in each residue class.

Interpretation: zero falsification failures for both the boundary-unit congruence modulo `p^12` and the half-point jet congruence modulo `p^15`. This finite computation is regression/falsification evidence only; the proof is the symbolic p-adic logarithm, exact reflection identity, valuation-controlled exponentiation, and the previously established exact top-boundary identity.

The executable checker source itself was not staged in this request; this transcript preserves its exact hash and observed output so the current portable unit has a durable verification witness without claiming Source publication or mathematical acceptance.
