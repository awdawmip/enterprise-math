# X6 Unit104 — FCC Johnson residue observer typing and exact native-collision certificate

**2026-11-18 · TASK_RESEARCH · AUTHOR-PROVED / EXACT-FINITE-EXECUTED / UNREVIEWED / NOT_ADMITTED**

**Mother objective:** `PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905`; Task `RS-X6-LEGACY-PLANE-RECONCILIATION`; publication `TP2-B4A441B23DA3159232C2`.

**Frozen science:** `P000 V5 @59538f585d037d09ef687b28715c4bc1a3f9fe03` with six signed native Cell axes; historical comparison `fd2bcff10ca6e147348b6c1236027fc0d2877df3`. No new native axes, axioms, changed P000, or rewriting of historical Results.

## 1. The exact executable source and its type

Historical and current source `research_checks/P000_SIX_AXIS_JOHNSON_TROPICAL_ARITHMETIC_INTEGRATION_CHECK_20260830.py`, immutable Git blob `62ea223dcbbb118186513737243ead040b77adc0`, defines complementary pairs `(0,5),(1,4),(2,3)` (lines 10–13), the 48-element pair-preserving wreath action `C2 wr S3` (lines 39–59), `rho` (lines 82–83) and `rho_orbit` (lines 85–87). The exact expressions are:

```python
rho_J(x) = ((x[0]-x[5]) % 2, (x[1]-x[4]) % 2,
            (x[2]-x[3]) % 2, sum(x) % 3)
rho_J_orbit(x) = tuple(sorted(rho_J(x)[:3])) + (rho_J(x)[3],)
```

This `rho_J` is a **pair-parity/mod-3 FCC/Johnson carrier residue**, distinct from the X6 relative/min-zero spatial observer `can6(x)=x-min(x)·1`, the full signed Cell endpoint `x`, the path-word observer and natural N-BRC multiplicity. The source itself distinguishes pair-sum/product alignment by explicit witnesses (lines 130–173); those earlier findings remain credited.

## 2. Exact theorem and typed witness

Define `rho_J: Z^6 -> (Z/2)^3 × (Z/3)` as above. It is a surjective additive group homomorphism. Its kernel has index 24 and consists exactly of `x` for which the three complementary-pair differences are even and the six-coordinate sum is divisible by 3. A direct constructive proof of surjectivity: for any residues `b0,b1,b2∈{0,1}`, `t∈Z/3`, choose `x=(b0+2k,b1,b2,0,0,0)` with `2k≡t-b0-b1-b2 (mod 3)`. Such a `k` always exists, because 2 is invertible modulo 3.

The sorted reader `rho_J_orbit` is invariant under all 48 pair-preserving carrier permutations, since switching partners reverses a difference without changing its parity, and changing pair order just permutes the first three parity bits. The full image has exactly 12 values (four possible numbers of odd complementary pairs, times three possible total residues).

The typed counterexample uses the full native Cell zero `z=(0,0,0,0,0,0)` and the composite native displacement `w=(6,0,0,0,0,0)`:

- `rho_J(z)=rho_J(w)=(0,0,0,0)` and the sorted `rho_J_orbit` also coincides;
- the source's complementary-product `q_orbit` is `(0,0,0)` for both inputs;
- `can6(z)=z`, `can6(w)=w`: the native full endpoints differ, with `L_E(w-z)^2=36`;
- the primitive signed-step minimum is `||w-z||_1=6`, with exactly `6!/6!=1` shortest native path word;
- the 48 carrier permutations cannot turn all-zero `z` into nonzero `w`.

Thus **the executable Johnson residue/derived product packet does not determine a full native signed endpoint**, even after retaining this extra `q_orbit` at this witness. It is valid as a declared finite carrier/observer readout. Any later consumer needing native endpoint, common depth, signed-axis trace or path multiplicity must retain the appropriate typed source data. This tests the exact LP-003/005/023/028 downstream boundary; it does not establish a faulty current caller.

## 3. Actual independent finite execution

The new standalone standard-library checker performs:

- complete enumeration of `[-2,2]^6`: **15,625 signed states**;
- exact invariance testing under all 48 pair-preserving permutations: **750,000 integer equalities**, no failures;
- exact image cardinalities: `|im rho_J|=24`, `|im rho_J_orbit|=12`;
- explicit endpoint, `q_orbit`, native squared-norm, L1 and one-path multiplicity checks for the witness above.

Python ordinary, `-O` and `-OO` executions all passed and produced byte-identical result JSON. This is an independently executed **finite integer checker**, not an original project native benchmark, a reproduced R063/Helly test, or a downstream live consumer regression.

New checker `research_checks/X6_UNIT104_FCC_JOHNSON_RHO_TYPED_OBSERVER_CHECK_20261118.py`: Git blob `9a8a31788d5a898ded208501f8e4410cedd65f2a`, local SHA256 `2a996202c26132d60ef98c02130d0647a617b2977ff704ff3e445efa2afa38f1`, committed at `f865691e9dd01df0631ec68a62b0ca83d1661fcc`.

Exact result `research_checks/X6_UNIT104_FCC_JOHNSON_RHO_TYPED_OBSERVER_RESULTS_20261118.json`: Git blob `04c4303cb6ac86612abc931ae115b2622ca438da`, local SHA256 `3e5a116880db042a5e016882f780a1d802e36887f1030ad796c4551df8b560fc`, committed at `c03a0df354ab3fc970dbf24e0a29fb572a3be71a`.

## 4. Bounded source-consumer audit

In addition to the previously verified Units 97–103, this unit read the frozen `research_checks/` directory inventory (120 entries) and fully inspected **16 selected Python sources**, including `P000_*NATIVE*`, `P000_*RETURN_MULTIPLICITY*`, both selected `BRC_*BRIDGE*`, and the Johnson carrier source. The explicit source consumer `P000_SIX_AXIS_JOHNSON_TROPICAL_ARITHMETIC_INTEGRATION_CHECK_20260830.py:82–87,132–143,156–173` operates on its declared `rho_J`, positive/negative integer input and carrier quotient; it is **not** a use of native X6 signed `argmax_i|d_i|` nor positive N-BRC sign cancellation. The sampled other files do not document an invalid historical LP011/LP019 caller in their inspected scopes.

The earlier claims `LP011` and `LP019` remain `UNRESOLVED_PROVENANCE` for any actual alleged wrong executable callsite. No historical allegation has been silently converted to a finding of broken current code. This scope is a bounded 16-file examination, not all 120 files or all downstream theorem references. Original 28-LP coverage and independent Driver `REQUEST_REVISION` remain open.

## 5. Durable continuity

Prior completed Units64–103, archived claim-ledger dispositions, existing approved frozen results, original R063/Helly native experiments and the current semantics of P000 are all consumed unchanged. Original Researcher `EM-X6-FB6990`, session `MCP-082892eb480e45dea6d4b9fcc0491034`, claim `MCP-3e221a50dc8818f914e228f6`, run `RUN-95866d78d35721116c362956` remain provenance pointers, subject to fresh Source authorization for protected writes. Original Units102–103 Native PROGRESS request `onhour-20261118-0204-x6-own-units102-103-native-progress-v1` has now read back `SUCCEEDED / SOURCE_CHECKPOINT_PUBLISHED`, `Source@c024460007fc7d0fa52d45e571801043e150dcfe`. The new exact continuation read `onhour-20261118-0308-x6-own-exact-cont-v1` was last `QUEUED`; consume its own receipt before a new protected step.

**Next exact research:** finish the remaining 28-LP typed theorem-facing dependencies, especially a source:line consumer that actually replaces signed Cell endpoints with `rho_J`, minzero `rho` or Johnson `q_orbit`; if a wrong live call exists, repair and regress that precise call without changing the historical baseline. Continue independent LP011/LP019 provenance judgement without manufacturing a wrong caller. The Native semantics of Unit104 remain awaiting actual own authorized checkpoint and independent review.
