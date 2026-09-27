# Parent review: geometric escape and torsion mark

Verdict: SHARED_CONTEXT_SYMBOLIC_REVIEW_PASS / NOT_FORMAL_ADMISSION.
Reviewed full source in actual tool chunk `a48f90`:
`CLOCK_ESCAPE_AND_TORSION_MARK.md`, SHA256 `ac743ae40288095cc1633de2e91aa2453d61b921e362e941db2b1eab27207542`.
Also reread the full frozen translated Kummer proof in actual tool chunk `4ab660`.

The matrix ideal proof uses both invertible conjugations, so it covers the full ideal and every prime-power depth. The chosen cyclic basis for trace reparameterization has determinant -U_m; the fixed companion convention differs only by a unit basis change. The cross-clock trace product expands correctly. Nonunit cyclic determinants remain explicit paid witnesses.

The isogeny divisibility chain follows from actual point reduction and the supplied R-defined dual identity. It does not infer that finite-field existence of an isogeny is an algorithm over a composite ring. Its middle divisor can be proper despite endpoints 1 and N; the text correctly preserves that useful possibility. The external point-count theorem is sourced separately and does not replace the internal hypotheses.

For the concrete new observer, the globally defined translation by T descends to the projective swap (X:Z)->(Z:X). This is a unit transformation even where the affine expression 1/x would be undefined. Translating BOTH supplied adjacent pairs gives points Q+T and Q+P+T. Their difference remains the same admitted P, so the frozen translated-mark theorem applies without changing its base mark or requiring a new y lift. Its expression becomes Z1-aX1, whose sign gives the displayed g_T. Thus g_T has the exact primitive depth at T rather than the squared depth of X0 alone. Primitivity prevents any prime from dividing both g_O and g_T.

The quotient by {O,T} is a degree-two etale map in the admitted odd smooth setting. Its disjoint identity fiber yields the product of the two primitive ideal divisors; their coprime support prevents valuation overcount. This supports the quotient interpretation, although no quotient needs construction just to evaluate g_T.

The stronger exact-two-torsion special case is valid: Q=-Q with 2 invertible gives affine y=0; x and x^2+alpha*x+beta cannot both be nonunits at a common residue prime since beta is a unit. Their product vanishes modulo the entire prime power, forcing exactly one factor to vanish to full depth in each component. The displayed coprime factorization of N follows. Without this strong premise the use of X alone remains invalid for primitive depth, as the text states.

The CRT witness is conditional geometry, not an algorithm that can be fed hidden factors. It proves strict extra detection on already certified endpoints, while producing such endpoints from a factor-blind public point and clock remains open. The construction/transport/observer costs and source admission are not removed by the constant-size extra formula. The prior 99-bit no-hit result is unchanged.

No new arithmetic was run in this review. A separate planned observer-only experiment can apply the formula to frozen, already certified adjacent pairs without rerunning the old ladder, using new native receipts and all cuts in a predeclared scope. This review does not pre-certify that execution or its record checker.

Global-Knowledge-Sync: main@2450bbb / GLOBAL_KNOWLEDGE_V1
