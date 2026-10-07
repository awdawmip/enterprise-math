# P11 final shared-context audit

Verdict: `PASS / NO_MATHEMATICAL_BLOCKER_FOUND` for the proof composition in `RETURN.md`, the local supporting `ARITHMETIC.md`, and `FAMILY.md`.

Scope: root `EM-DIRECT-49ADE6`, authorized run `RUN-85b48f2b4121a8b72c6c03a1`, generation 1. This is a source-exposed collaborative audit, **not independent Driver review or formal acceptance**. The audit reviewed current P000 V5, Heartbeat, residual-fidelity, joint-observer, exact taskbook, accepted parent and Driver inputs.

## Verified load-bearing steps

1. **Model and maps.** The three transformed cubic factors are `PQ(a+T)/(a-T)`, `Pa(T-b)/(a-T)`, and `Qa(T+b)/(a-T)`. Their product gives exactly the square of `aPQY/(a-T)^2`. Solving the first map gives the stated inverse with coefficient `4aPQ`; the parent sum/difference relation then reconstructs U and V without a square-root choice.

2. **All rational exceptions.** There are no rational intersection points at Z=0 and no rational E points at xi=+PQ or -PQ. T=0 is impossible. The four D=0 sign corners correspond to precisely O and the three nonzero two-torsion points, in the order displayed in the return. Every other rational E point yields `0<|D|<Q`; equality is excluded by the frozen positive fourth-power descent. Thus the family does not need an unproved real-density argument or an empirical positivity filter.

3. **Uniform torsion.** The actual Bekker–Zarhin Theorem 2.1 includes two-torsion and treats zero as a square. Negative differences exclude halving the roots 0 and Q²; the frozen nonsquare 4AB excludes halving P². Mazur then leaves only Z/2 x Z/2 or Z/2 x Z/6. The stated third division polynomial is correct for a2=-(P²+Q²), a4=P²Q², a6=0. Generalized Nagell–Lutz integrality plus the integer-root divisor rule makes the j|K² test finite and necessary; the nonzero square ordinate and division polynomial make it sufficient. No unproved universal exclusion of three-torsion is used.

4. **Descent strength.** The signed squareclass product and the finite support/cover argument in ARITHMETIC are exact. The all-trivial squareclass criterion is equivalent to divisibility by two by the cited theorem. This does not compute all local covers, Selmer groups or ranks, and does not license replacing a signed elliptic point by squareclasses for future group operations. The final RETURN now uses the explicitly sourced two-division criterion and retains the boundary table, resolving the initial citation-strength cleanup. Its additional direct derivation of the third division polynomial from the doubling law has also been checked.

5. **Non-torsion certificate.** The seed is `(194089,69872040)` on E_{233,119}. Its nonzero ordinate is divisible by 5 and the cubic discriminant is 4 modulo 5. Pasten Theorem 1.6 applies to this integral cubic with a quadratic term and gives the required contradiction to torsion. The optional short-model conversion in FAMILY has correct coefficients and discriminant scaling by 3^12. At good reduction 5 the ordinate counts `1,1,2,2,1` plus O give 8; rational three-torsion injects, so the fixed-core torsion is exactly `(Z/2)^2`.

6. **Primitive reconstruction.** Multiplying by twice the common denominator makes the parity constraints hold. The gcd is that of the sixteen actual outer roots. If it is m, differences give m|k0P and m|k0Q; coprimality gives m|k0. Dividing actual integer roots preserves half-sum parity and reconstructs the divided six coordinates and products. This is not the naive gcd of six coordinates. Positive normalized rational coordinates can be recovered from the final sextuple and its fixed core, so primitive normalization cannot merge different positive normalized triples.

7. **Infinite image.** Every positive multiple of the non-torsion seed avoids the two-torsion boundary; all signed inverse points are therefore strict. Passing to absolute values has fibers at most eight, and the subsequent primitive map is injective on positive normalized triples. Hence at least ceil(N/8) outputs occur from the first N multiples. Duplicate sequence values are allowed and bounded; no claim that the seed generates the complete free group is made. More generally, per-core primitive infinitude is exactly equivalent to positive Mordell–Weil rank. Rank zero is not automatically an empty strict fiber.

## Scope and remaining boundary

The three manuscripts agree: an explicit fixed-core infinite primitive family is proved, while all-core Mordell–Weil ranks, complete generators and uniform point classification remain unproved. Finite exact checks verify certificates and transcription only. Native X6 geometry is unchanged. Signed points, core, multiplier, sign bits, denominator scale and root-gcd data are retained; no group law is claimed on bare unsigned primitive outputs.

The completed `checker/RUN.json` was read: both required known witnesses, n=1,2,3, exact roundtrips and root reconstruction pass. The n=2 output has six-coordinate gcd 2 but true outer-root gcd 1; its rejected naive division is a concrete check of the essential parity/primitive distinction. Raw sign patterns (+,+,-) and (-,+,-) validate retention of the sign coordinate. No large census was run for this audit. These finite checks are corroboration, not the all-n proof. Formal Source publication, immutable bindings and independent Driver review remain root/control responsibilities.

## Portable exact reproduction

The flat five-file checker was copied to a new temporary directory and run with isolated Python. Its RUN.json was byte-identical to the published record; the directory was removed afterwards. This is environmental isolation, not independent mathematical review.

```json
{
  "status": "PASS",
  "command": [
    "python",
    "-I",
    "check_p11_family.py",
    "--output",
    "REPRODUCED.json"
  ],
  "temporary_directory_removed": true,
  "result_byte_identical": true,
  "RUN_sha256": "bdf09151413daba50f5c17d18cf67538f455c63190ed58fcc8c156cca560d3f7",
  "stdout": "{\"status\": \"PASS\", \"known_witnesses\": 2, \"family_multipliers\": [1, 2, 3], \"outer_root_primitive\": true, \"finite_validation_only\": true, \"output\": \"REPRODUCED.json\"}",
  "stderr": ""
}
```

No old b<=100000 census was executed. The all-n and uniform algebraic claims are proved in RETURN.md and FAMILY.md; sample checks are not their proof.
