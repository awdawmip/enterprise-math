# Current-Source application: the finite-presentation support readout

2026-10-15 UTC. Revision V2 (row count r, readout δ; fixed bridge V2). **Local application completed; full coverage Task OPEN.**
Same actual EM-N-DEA587 / RUN-d226418286530d5099e4a5c9 execution and original
coverage owner as the fixed typed-terminal bridge report V2. This application
does not modify that report or claim a new theorem for an already closed
mechanism class. The inherited finite-presentation/Fitting boundary and
RRBF7 remain credited to their original authors. Root supplied the direction
to instantiate the interface on an actual Source-licensed class; this is
directed, source-exposed work, not independent review.

## Actual interface, not a hypothetical additional primitive

At Source `a2b4f908009eda28ccfef8638dda7ab28f856ecd`, the actual coverage
Taskbook `research_tasks/RR133_COVERAGE_PROSPECTIVE_GEN2.md` line 80 preserves
the boundary "explicit finite presentations expose one-sided hidden support
through determinantal/Fitting gcds"; lines 99-103 require preservation of the
relevant terminal presentation/readout. The retained Objective
`OG-7F2B4C1D9A6E83F05211` /success_criteria/2 explicitly separates generation,
observability and extraction. Its permission for a final gcd does not
license a new generation mechanism. The prior-art Source review
`driver_reviews/N_COUPLED_NONRING_PRIOR_ART_DRIVER_REVIEW_20260831.md` places
direct nonunit/gcd endpoints inside the inherited firewall.

We instantiate **that finite-module presentation boundary**, not all
possible native carriers or every conceivable "finite presentation" in
another algebraic category. Its explicit interface is:

* Input: public `N≥2` and `C=(r,e,A)`, `A:(Z/NZ)^e→(Z/NZ)^r`, with finite
  dimensions and all entries explicitly supplied. Retain any supplied
  generator/port/provenance annotations as additional typed data `a`.
* Algebraic output interpretation: `M(C)=coker A`.
* Observer: residue-characteristic support `Supp_N(C)` as defined in the
  fixed report, represented by the public divisor below.
* Public operation: exact finite determinant enumeration followed by integer
  gcd; no hidden prime is an argument or an implementation step.
* Terminal output: the joint tuple `(C,a,δ_N(C))`, not just the scalar δ.
* Future scope: all declared effective operations/readouts on the retained
  `(C,a)` representation, with process order retained as needed. This does
  not assert that `(C,a)` is sufficient for some additional native state
  or future operation absent from its Source contract.

The finite matrix interface gives complete *operational input data* for
this readout. It does not give a way to produce such a C from an arbitrary
opaque resource handle; that different obligation remains separate.

## Uniform public construction and exact support equality

Lift the entries of A to integers in `[0,N-1]`. Let `Delta_r(A)` be the
finite list of determinants of all `r×r` column submatrices. Define

`δ_N(C) = gcd(N, Delta_r(A))`, with a nonnegative gcd.                 (A1)

The conventions are explicit: if `e<r`, there are no such submatrices and
`gcd(N,empty)=N`; if `r=0`, the list contains the single empty determinant
`1`, so δ=1. They give, respectively, full residue-characteristic support
and empty support, exactly as the corresponding cokernels require.

For each prime `ell|N`,

`ell | δ_N(C)`
`  ⇔ every r×r minor of A vanishes modulo ell`
`  ⇔ rank_(F_ell)(A mod ell) < r`
`  ⇔ M(C) ⊗ F_ell ≠ 0`.                                             (A2)

The middle rank criterion includes both conventions above. Thus

`Supp_N(C) = {ell | N : ell | δ_N(C)}`.                              (A3)

Changing an integer lift changes each determinant by a multiple of N,
so (A1) is independent of the lift. It uses only finite public data.
For example, the Leibniz determinant formula gives a uniform terminating
algorithm without invoking field division or knowing which entries are
units. Euclid's algorithm then computes δ. This is an existence and
effectiveness argument; no determinant expansion, sample or checker was
executed for this application, and no feasible cost bound is asserted.

If `1<δ<N`, δ is a proper public nonunit divisor. That is the already known
endpoint, not a new factoring route. A proper nonempty support set implies
this proper-divisor condition. The converse needs care when N is not
squarefree: a proper divisor can involve every prime dividing N. We do
**not** identify the two notions without the relevant additional condition.
Nor does the support set determine all module multiplicities or valuation
data. Keeping C avoids confusing the support observer with the whole
terminal algebraic object.

## The actual commuting square and the automatic simulator pipeline

Let `q(C,a)=(C,a,δ_N(C))` and `pi(C,a,δ)=(C,a)`. Then `pi∘q=id`.
Consequently for any declared operation f on `(C,a)`, its lifted operation
on the image of q can be defined by

`f_hat = q ∘ f ∘ pi`; hence `f_hat ∘ q = q ∘ f`.                     (A4)

Definedness is preserved through pi. If f is effective, so is this lift;
the recomputed δ is a deterministic total readout of the new C. Every
scoped observer o of `(C,a)` satisfies `o_hat=o∘pi`, and finite compositions
obey the fixed V2 report's Lemma 1, including saturated partial-observer domains. This is a conservative *extension* of the
retained representation, not a lossy quotient. In particular no branch,
matrix, annotation or correlation is discarded merely because δ is known.

Now take any public effective program P whose actual terminal type is this
explicit `(C,a)`, with the random/branching/termination assumptions of the
accepted contract. The program

`Q(N,p): run P(N,p); compute (A1); return (C,a,δ_N(C))`                (A5)

is effective and public. The presentation component is exactly the original
C; no arbitrary word is rebranded as a support-bearing module. The finite
annotations and δ can equivalently be readouts evaluated on the same
retained terminal execution. The existing emulator therefore reproduces
their **joint** law, or enumerates their reachable joint output support in
the appropriate effective-branching mode. Equations (A2)-(A4) supply the
typed support and scoped future-observer transfer. There is no separate
external oracle and no need to reconstruct hidden CRT factors.

If P already computes (A1), Q need only retain that effective terminal
readout. If P outputs only a scalar or a handle, (A5) cannot be claimed
without showing that its actual terminal scope supplies C or that the
selected observation-level bridge needs no C. The unit does not silently
strengthen either case.

## Exact contribution to the remaining coverage inclusion

Define `U_mat` as the public effective runtime class just described, with
this explicit finite-module terminal interface. The equations above prove
its entire support-readout pipeline is covered; they do not require a
separate per-program readout oracle or a new semantic assumption on each
matrix. This is a concrete application of the fixed bridge, not merely an
interface checklist. The scalarization identity itself is an inherited
boundary, given here explicitly to verify the bridge's exact types and
degenerate cases, not claimed as a new mechanism or repeated experiment.

This still does not establish that **every** mechanism licensed by the
Objective has terminal behavior in `U_mat`, nor that all of them require
the finite-module interface rather than an already effective specified
word readout. The actual remaining obligation is an inclusion at the
declared observation strength:

`licensed resource behaviors → public effective complete scoped terminal behavior`.

The effective-superclass route remains available: under a Source-justified
reading that all licensed behavior already consists of public effective
programs with a complete effective declared readout, composing that readout
with the interpreter provides the positive observation-level coverage.
One then has to verify that this is the Task's whole required behavior;
neither a larger ontology reconstruction nor a finite opcode census is
automatically needed. If the required observation includes an additional
relationally specified object, that interpretation needs its actual bridge.

No currently supplied source proves that this unresolved universal
inclusion is false, proves an admissible escape, or establishes two
actually licensed incompatible semantic completions. Thus full Task
coverage and Specification-gap remain OPEN. No parent closure, new Task,
new singularization, efficiency claim or changed hard target follows.

## Revision and execution boundary

The 9118-byte V1 application (SHA256 8725ceebe61ae7da51d5fea364c7f15cd04525de4f52b1fbc060cbc111bfd963) is retained unchanged. V2 uses r for row count and δ for the divisor readout, and binds the clarified partial-observer convention of the bridge V2. The actual application, inherited-mathematics boundary and OPEN disposition are unchanged.


All work is paper reasoning and exact source reading. No scientific
program, matrix sample, old theorem checker or benchmark was run. Source
pins were checked with ordinary local hashing only. The original Task,
owner, current run, historical authors and isolation holds remain unchanged.
This document is local evidence awaiting distinct review/checkpoint; it is
not a Native Result or Driver adjudication.

Researcher-ID: EM-N-DEA587 / RS-N-COUPLED-PUBLIC-EFFECTIVE-RESOURCE-COVERAGE-OR-ESCAPE-CLASSIFICATION
