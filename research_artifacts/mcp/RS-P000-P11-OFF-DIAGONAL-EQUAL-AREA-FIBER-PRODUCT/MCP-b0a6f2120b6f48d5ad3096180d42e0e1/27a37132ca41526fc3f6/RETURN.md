# P11 off-diagonal equal-area arithmetic — Researcher Return

Researcher-ID: EM-P000-298FC9

Task: RS-P000-P11-OFF-DIAGONAL-EQUAL-AREA-FIBER-PRODUCT

Publication: TP2-74D161216AAF385EE27F. Claim MCP-d4a06240a4876acc1ab18e8f (server epoch 6060656264), ER-8AAACF67EF70A0F0126A, run RUN-bad5f7abfc8667ef2a63c7ac generation 1. Session MCP-b0a6f2120b6f48d5ad3096180d42e0e1; RA-A10B7F7B4F7D04C137083FC2.

## Claimed terminal strength

**OFF_DIAGONAL_EQUAL_AREA_INFINITE_PRIMITIVE_FAMILIES_PROVED**, the first success alternative explicitly permitted by this Task.

The explicit sequence consists of every positive odd multiple of (9,2112) on the external arithmetic curve

\[
v^2=u(u-1945)(u-265),
\]

followed by the proved rational-square lifts, exact root reconstruction and minimal-denominator normalization in OFFDIAG_INCREMENT_1.md. It preserves the ordered equal-area triangle factors proportional to (21,20,29) and (35,12,37). The new points have h != 0, integer AP sums/products, all eight outer pairable cells, and common sixteen-root gcd 1. They are pairwise different primitive data. This is not a scaling orbit of the old witness.

Lutz–Nagell gives a strict nontorsion certificate at the prime 11; a direct chord/tangent square-class identity preserves both middle-row cuts for all positive odd multiples. The top-right discriminant c=1 proves that the least common root denominator already gives gcd 1. The scaling-invariant ratio d/29 proves injectivity. The n=3 member is an explicit new primitive (-,-,+) product-sign witness. The attached exact checkers are regression, not the proof of infinitude.

## Binding correction to the frozen first report

OFFDIAG_INCREMENT_1.md remains byte-for-byte frozen at SHA256 b9f17ce40045eeedd85ff128d462650c3dc1206bf3b30a77cec58f936e498dc4. Its Section 1 sentence “It has generically four sign preimages” must be read only for the **full signed algebraic cover**, allowing both signs of d. On the real/rational slice d>0 actually used in equation (1), a fixed nonzero signed elliptic point (u,v) instead has **two** sign preimages for (mu,nu). With d,mu,nu all chosen positive, the P11 readout is unique and uses |v|=d mu nu. The signed elliptic point is retained as auxiliary orbit provenance for further group operations. The four-to-one algebraic-map statement must not be assigned to the positive-d slice. This correction changes no square-class, rational-root, nontorsion, primitive or injectivity proof.

For clarity, the fixed-integral-core criterion in that same section includes d in Z_{>0}; the notation 4d|K is ordinary integer divisibility. The rational-denominator route is the separate, explicitly proved method used by the infinite family.

## Evidence and requirement coverage

- OFFDIAG_INCREMENT_1.md: necessary-and-sufficient fixed-core cut carrier and reconstruction; complete classical Euclid parameters with labeled equal-area equation; proof of the infinite primitive family; all-sixteen-root denominator/gcd theorem; genus-one residual object; exact global zero-column residual equations and complete zero-column classification on the displayed fixed core; sign and BRC/observer accounting. The correction above is binding.
- DENOMINATOR_REFINEMENT.md: optional strengthening to a closed minimal-denominator formula in d=p/q, including its exceptional 2-adic factor. It is not needed for the infinite-family theorem, which already has a complete lcm/gcd proof.
- CHECK_PLAN.md and check_offdiag_family.py: the predeclared n=1,3,5,7,9,11 control, exact group arithmetic, direct cell reconstruction, factor preservation, swap, boundary and gcd checks.
- offdiag_checks.json: complete exact fractions and all sixteen integer roots for those six points. All assertions passed.
- parent_checker.py: unchanged classical/parent checker bytes, SHA256 dec70c04830e0291aca3e09bac595fcb22731670a00d4be9e1c86313713bf26b, Source blob 6b0b5780ce5c9c554a470792e0c071fec097920c. Only its direct reconstruction/normal-form/gcd functions were reused; its old finite census was not run.
- DENOMINATOR_REFINEMENT_PLAN.md, check_denominator_refinement.py and denominator_checks.json: the stronger formula checked on the same six curve points and 318 predeclared artificial integer-gcd cases. The latter are explicitly not asserted to be curve points.
- PROVENANCE_AND_COVERAGE.md: exact input pins and disclosed directed context, existing-tool reuse resolution, classical prior-art boundary and native/external semantic typing.

## Limits and next control action

This Return does not classify every primitive point on every ordered equal-area core, determine exact ranks or generators, or solve the global zero-column locus. It proves the Task's specified infinite-family success alternative with exact primitive reconstruction and isolates the other arithmetic as a family of explicit genus-one cut curves over the labeled Euclid equal-area relation. The old zero-column witness orbit on the displayed fixed core is fully classified; it is not claimed to represent the global locus. Parent OBJ-P000-SIX-AXIS-ARITHMETIC-TROPICAL-INTEGRATION remains OPEN, as do other EM research objectives.

All derived triangles/curves are external arithmetic carriers. P000 native space remains six-dimensional discrete Cells with no native plane, with time separately typed only when needed. Ordered factor provenance, coupling sign, square witnesses, denominators, parity, zero/composite roots and all sixteen cell positions remain retained. No Working Truth, Foundation status or canonical promotion is declared.

Next action: freeze this claimed Researcher result through the authorized native Result writer and obtain the actual line Driver's independent review of the stated infinite-family scope. The Driver decides any downstream audit/integration gate and parent routing. Do not open a Selmer task automatically or infer parent completion from this Task's success alternative.

No-repeat units: inherited normal form and h=0 classification; old common-root scaling census; all-odd-multiple square-class preservation on the specified fixed core; top-c=1 primitive calibration; fixed-core zero-column candidates; the exact denominator valuation refinement. Stronger global questions must start from these preserved units.
