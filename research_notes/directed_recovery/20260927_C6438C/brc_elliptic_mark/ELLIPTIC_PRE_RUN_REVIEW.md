# Elliptic translated-mark source review

Status: **STATIC PASS / SHARED-CONTEXT REVIEW / NOT EXECUTED / NOT ADMITTED**. This review read the complete implementation, plan and validation proof without importing scientific modules, executing arithmetic fixtures or using a numerical reference. It is not a saved-record review or independent admission.

## Exact reviewed inputs

| File | SHA-256 |
| --- | --- |
| `elliptic_mark.py` | `a0186eb10a02f7ad3ed4106cd1395d495379e18e12f03b82b212db7c90fb60da` |
| `PLAN.md` | `8f8660262c7b60fc20def4ddc58164757aa908b9c1854d948bd0093fcb0599fc` |
| `JACOBIAN_VALIDATION_PROOF.md` | `ba77080e3d4400cd669f4f819c49e6e2dfacc65f4507d0b8718498c1712517be` |

The source binds the frozen fixed-difference chart proof `GEOMETRIC_NEXT_TOOL.md` at `76e39469669e4068b297377ad9beb0c6dd5b19b9a1a929a2f07378f1dfe281e2`, the translated-mark theorem at `50e899863bcec4001ee6a5dd7d2f069a57358e97b6de07b90bc7378b013fd492`, their listed parent reviews, and the Kummer valuation proof. The old wrapper bytes were rechecked: `native_relative_port.py` is `0821cf958b99988b5dbb95f5a42b97629155ca80c07e1f5bee8e2e9165bc39a8`; `hbw_marked_section.py` is `e2929468d9b430f9a0ef93a3412f132c692ce994c7b5061bece21a3960974851`. The relevant wrapper and actual typed arithmetic definitions were read, not executed.

## Mathematical and implementation findings

No blocking defect was found for the declared grid `(9,0,4), (35,4,8), (19,0,4)` and fixed initial point `(2,1)`. Setup constructs and verifies the curve and fixed unit difference before using the complete ladder chart. It does not admit an arbitrary triple of Kummer pairs as an addition relation. The ladder starts at `(O,P)` and its literal bit updates retain `(mP,(m+1)P)`; all intermediate pairs are saved. The multiplication order and selected doubling agree with that induction.

The ordinary denominator, translated expression, joint gcd and single-expression gcd are separate observations. The common gcd consumes actual typed Euclidean division links, and every proper output divisor receives exact division of N. No factor, point order or numerical expected answer is supplied to production. Single-W is not claimed to identify only the identity. The translated theorem is applied only to the certified true adjacent pairs and the fixed original point.

The full-point transformation `x'=Bx, y'=B^2 y`, coefficients `a2=AB, a4=B^2`, initial `(2B,B^2,1)` and all stated Jacobian doubling polynomials agree with the affine tangent law. The extra `-a2*Z3^2` in X3 is required and present. Over every odd smooth residue field, the Y=0, Z=0 and ordinary cases cover all primitive inputs and retain primitive output; this includes characteristic three. The ordinary projective representative `[XZ:Y:Z^3]` gives the unsquared return ideal `(Z)` near the identity. Thus the paid validator's gcd of Z, original-x cross relation and square-valuation comparison have the stated contracts.

The independent full-point route checks only EP. It does not separately propagate `(E+1)P`; that adjacency remains justified by the production formula and bit induction. The plan and output explicitly state this boundary. The N=9 fixture is a deliberately selected prime-power observation test and cannot establish unknown-input success probability.

## Provenance, accounting and failure scope

All scientific arithmetic in the new program is wired to the frozen actual typed operations. Exponent formatting and bit selection are public control. The seven routes separate setup, ladder, ordinary gcd, mark expression, joint gcd, single-W gcd and validation. The cost collector includes direct operations and all cached gcd certificates; native catalog calls are a separate count. The duplicate modular subtraction inside the reused observed-gcd wrapper is paid rather than omitted from the ledger. The square-valuation check also accepts a saturated gcd as an unsigned integer input before actual modular multiplication/reduction.

Guard and dependency checks precede scientific imports, STARTED uses exclusive creation, and existing success or failure artifacts prevent blind reruns. Source, plan, guard and frozen dependencies are rechecked before success. Parent records and steps are appended before child arithmetic, preserving available partial evidence. As documented, an exception inside an unreturned constructor or primitive can precede its final internal receipt; the failure snapshot is not a complete resumable machine state. Success and failure serialization have separate preservation paths.

This is a finite correctness and cost experiment. Its source makes no claim of fast factoring, favorable curve sampling, a general success probability, or a nonlinear native BRC closure beyond the certified typed register program. No run outcome is certified by this pre-run review.

Global-Knowledge-Sync: author reuse of the actually read canonical `7a639845946cb5f8edfa22d3d5d0d47a44f6080e`; execution must bind the coordinator's actual current guard and read SHA through the runner arguments. No fresh independent handshake is claimed here.
