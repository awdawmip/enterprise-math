# Exact six-coordinate encoding at complete native-word boundaries

Status: AUTHOR_DERIVATION_AND_BOUNDED_EXECUTION / SHARED_CONTEXT / NOT_ADMITTED.
Researcher EM-DIRECT-C6438C; activity RA-CAAAC604CB513AEA8BBC1DFC.

## Result and precise scope

The new four-square phase family admits a common six-dimensional invariant
subspace within the unchanged 61-coordinate computational carrier. This gives
a lossless storage codec for its reachable boundary states, including all four
completion residual coordinates. It does not reinterpret the six coordinates
as the six spatial axes of P000, change native dimension, discard a nonzero
residual, or establish polynomial-time classical factoring.

Let J insert a six-vector into coordinates 0 through 5 of the full carrier.
The constructive phase has W = D0(2zz^T-I), with
D0 = diag(1,-1,...,-1), z=(a0,...,a5,0,...,0)/S and z^T z=1.
For every j >= 6, (2zz^T-I)e_j=-e_j and D0 e_j=-e_j, so W e_j=e_j.
For j < 6, W e_j has no component outside the first six coordinates. Hence

    W = W6 direct-sum I55,    W J = J W6.

The exact m2 phase preserves the same subspace. These statements hold for
every directly constructed phase individually; no common root, commutation,
or equality of independently constructed residual directions is assumed.
Forward and inverse maps satisfy the same block condition.

At a streaming boundary write the raw state as rows v_(control,work,spectator)
with a common positive denominator. The initial internal row is e0. Modular
permutations only relabel work, controlled phases apply W or identity, and
the external preparation/read H4 maps make integer linear combinations of
internal rows. Each operation therefore intertwines with J. Conditional
projection selects an external control bit and does not alter this property.
Exact common-denominator reduction also commutes with J since appending zeros
does not change the gcd of the nonzero numerator entries and denominator.
Induction proves equality of all decoded rows and quadratic masses after
every history, including zero-mass histories. In particular, the software
sampling law and fixed classical postprocessing are unchanged.

The codec is applied only between complete native words. Canonical routing of
an indexed gate may move intermediate amplitudes through other coordinates.
Those native executions and their complete-column evidence remain intact;
the codec makes no assertion about their internal microsteps.

## Executable admission rather than unverified projection

`restrict_word` accepts a complete actual native word, reconstructs its full
61 forward/inverse columns using the existing actual replay interface, checks
its source binding, checks both cross-blocks are exactly zero, and checks the
55-coordinate complement is exactly identity. It then returns immutable
restricted integer columns with the same denominator and full-source digest.
`codec.encode` rejects any nonzero omitted coordinate. A seed word failing the
block checks is rejected rather than silently truncated.

This check is stronger than necessary: a rotating complement would still
preserve an exactly zero tail, but this implementation deliberately certifies
the simpler identity-complement family. Arbitrary inputs with nonzero tails
remain supported by the full simulator and are not accepted by this codec.

## Actual bounded evidence

`check_carrier_codec.py` replays the frozen direct m3 / delta=1/8 and m4 /
delta=1/4 certificates, plus the exact native m2 word. It checks 48 forward/
inverse vector applications, and all 30 history edges at t=4 for each of
N=15,a=2 and N=21,a=2. Every decoded numerator row and denominator matches
the 61-coordinate simulator exactly; terminal masses sum to one.

| Fixture | Full peak scalar slots | Encoded peak scalar slots |
| --- | ---: | ---: |
| N15 / t4 | 488 | 48 |
| N21 / t4 | 732 | 72 |

The N21 fixture retains nonzero internal residuals in the encoded carrier.
Nine negative controls reject nonzero omitted tails, cross-block coupling,
non-identity complement, duplicate/boolean/reordered-initial indices, wrong width, invalid
integer inputs, and a mutated full-source denominator. The fresh execution
record contains 223 actual BRC core calls, separately from host composition
and equality checking. Wall time is a single local observation in the execution
record, not a general speedup benchmark.

The exact scalar-slot saving is 61/6 for each explicitly stored row, or
55/61 (about 90.16%) fewer numerator slots. Python object overhead, caches,
certificates and the unchanged work-label set are separate resource terms.
No measured total-memory or wall-time factor of 61/6 is claimed. These t4
fixtures validate representation equivalence, not the default-width uniform
factor-success theorem or cryptographic-size performance.

## Continuation

Use the full certified bank to establish the block checks first. Then combine
this codec with demand-driven modular columns and selected-child streaming;
the composition must compare decoded complete rows and probabilities to
the same full-word instrument. If a later word fails the check, retain its
full carrier or establish another proved common invariant subspace. Do not
infer safety solely from a small observed residual or from earlier fixtures.

Global-Knowledge-Sync: main@61e00d2 / GLOBAL_KNOWLEDGE_V1
