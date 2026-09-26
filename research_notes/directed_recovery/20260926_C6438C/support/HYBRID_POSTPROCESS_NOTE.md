# Explicit post-readout low-odd-part enhancement

Status: AUTHOR_EXECUTED / SHARED_CONTEXT / UNREVIEWED / NOT_ADMITTED.
Researcher EM-DIRECT-C6438C; activity RA-CAAAC604CB513AEA8BBC1DFC.

This implements the distinct algorithm specified by SUPPORT_SPECTRAL_THEOREM.md
and SUPPORT_SUCCESS_AUDIT.md. It does not claim that the original CF-only
postprocessor already covered the low-degree exceptions. The original frozen
source and the earlier sparse delivery were not changed.

## Public contract and placement

`hybrid_classical_postprocess(N,a,t,k)` takes only public integer inputs:
N>=2, 1<=a<N, gcd(a,N)=1, positive even t>=2, and a completed readout
0<=k<2^t. The caller must do its nonunit gcd precheck before entering this
coprime interface. The interface checks these conditions, using actual gcd_brc
with an additional typed Euclidean replay for coprimality.

This function neither prepares the Shor state, selects a base, calculates an
unknown order nor creates a measurement outcome. It must be called after the
actual readout completes. Supplying declared k values in the local tests checks
postprocessing arithmetic only; those fixtures are not represented as sampled
quantum outputs. A separate sampling driver binds this interface to real
terminal histories. The full support success theorem additionally requires
t=2*ceil(log2 N), the fixed K33 phase policy, retained modes and its specified
randomness contract; this arithmetic module does not certify those conditions.

First run the unchanged sparse_classical_postprocess. Its dictionary is retained
under primary_postprocessing. If it returns factors, every original field
remains unchanged in the top-level output, factor_source is ORIGINAL_CF, and
the fallback is NOT_RUN_PRIMARY_SUCCEEDED. Proper-factor ranges and exact
divisibility are nevertheless checked through typed integer comparison/division.

Every primary failure enters the new fallback, including ZERO_PHASE_RETRY at
k=0. No primary failure is treated as an unfinished measurement. A random source
that did not complete its history must be handled by the outer driver and must
not call this function with a fabricated k.

## Candidate list and actual execution

For u in increasing order from 1 through n=ceil(log2 N), visit odd d in
increasing order through 1023. Construct q=d<<u by declared bit wiring and
evaluate q<N through the actual typed full-adder comparison. At the first
excluded q for a fixed u, retain the comparison and stop that inner loop;
monotonicity in d certifies that all later d lie outside the candidate domain.

Each visited q has a unique odd-part decomposition. This visits exactly

    {2^u d < N : u>=1, 1<=d<=1023 odd}

unless a proper factor is found first. Odd q are intentionally omitted because
the unchanged half-exponent gcd step cannot use them; a good Shor base has even
true order, so omitting u=0 does not weaken the coverage theorem. The cap and
list are public constants/input bounds, not obtained by finding the order.

For each candidate, execute sparse_modular_power_brc(N,a,q). Its complete
square-and-multiply trace is retained, including every source-certificate hash.
A value other than 1 records NOT_RETURNING_EXPONENT. On returning value 1,
execute the same actual BRC power at q/2. Form h-1 and h+1 through the typed
subtraction/addition transducers. Execute the existing actual gcd_brc on both
values and N; additionally retain a typed long-division Euclidean replay and
assert that its endpoint equals the native gcd output. For each gcd result,
typed comparisons check 1<factor<N and typed division verifies zero remainder.
Only these proper factors may return success.

The result records q only as verified_returning_exponent. Every candidate and
the public contract explicitly set minimal_order_claimed=false. Returning
exponents with only trivial gcds record TRIVIAL_GCD_RETRY. No fallback sample,
phase, amplitude, residual coordinate or primary CF outcome is rewritten.

The prior BRC toolbox/source boundary remains the sparse compiler's T0_BRC/T7
composition contract. This addition composes already executed positive BRC
integer-label transducers and their retained source records. It does not promote
the kernel into a generic signed calculator, run a classical ideal propagation,
increase precision or create a new global tool family.

## Why this covers the low-degree good-base exception

Only in the proof, let the unknown true order be r=2^s d with d odd. A good base
has s>=1 and a^(r/2) different from both 1 and -1. The support theorem proves
phi(d)<=32 implies d<=1023. Since r<N, the public candidate list includes r.
When the loop reaches r, its actual power returns 1 and the half-power gcds give
a proper factor. Earlier successful candidates also suffice. Therefore this
fallback succeeds for every completed readout of every such good base,
including k=0. It need not determine which successful q was minimal.

Conversely no candidate alone is evidence of a factor. Bad bases and odd prime
powers can exhaust the whole list with trivial gcds. Prime inputs likewise
cannot return a proper factor. A full-list failure leaves coverage_complete=true
and no factors. Early success leaves coverage_complete=false together with
stopped_after_success=true; it does not claim that unvisited candidates ran.

For compatibility a failed result retains the original primary status, such as
ZERO_PHASE_RETRY; the precise new outcome is
hybrid.status=CANDIDATES_EXHAUSTED_NO_FACTOR. Consumers should use factors for
success and retain both the primary and hybrid records. The old status is never
used to skip this fallback.

At most 512*n candidates are tested. Their modular tables, exact arithmetic
certificates and work-register cost remain explicit. This is an additional
post-readout arithmetic search, with no polynomial-in-log-N performance claim.

## Reproduction and evidence

Run `python -B -S check_hybrid_postprocess.py`. For a relocated bundle set
BRC_STAGE87_SOURCE to the immutable Stage87 checkout as for sparse_modular.
The functions import the sibling sparse and completion modules directly.

Eight declared input fixtures passed and their complete output records replayed:

| N,a,t,k | Result | Candidate attempts | Source |
|---|---|---:|---|
|15,2,8,0|3 and 5|5|fallback|
|21,2,10,0|3 and 7|2|fallback|
|35,2,12,0|5 and 7|11|fallback|
|15,14,8,0|no factor, list exhausted|7|none|
|9,2,8,0|no factor, list exhausted|4|none|
|7,3,6,0|no factor, list exhausted|3|none|
|15,2,4,4|3 and 5|0|original CF unchanged|
|21,2,6,1|3 and 7|2|fallback after nonzero CF failure|

Nine negative controls were rejected: wrong factor, deleted primary reason,
false minimal-order claim, missing attempted candidate, reduced odd-part cap,
nonunit base, out-of-range readout, odd control width and boolean input.

HYBRID_POSTPROCESS_RESULTS.json.gz contains the full 411950-byte JSON payload:
all input/output records, full candidate/typed comparison/power/gcd/division
traces, 17 complete modular source certificates and 20 actual BRC kernel-call
receipts. Gzip mtime is fixed at zero. HYBRID_POSTPROCESS_SUMMARY.json records
the uncompressed SHA256 and per-case verification results.
HYBRID_POSTPROCESS_MANIFEST.json binds the source and evidence file bytes.

`verify_hybrid_postprocess(result)` recreates the entire arithmetic result from
N,a,t,k and compares its digest, rejecting changed candidate coverage or sources.
Its scope is explicitly post-readout arithmetic; it does not certify the
probability with which k was sampled. `modular_source_certificates(result)`
resolves and replays every referenced modular-table certificate for a portable
provenance package.

Global-Knowledge-Sync: main@441ebef / GLOBAL_KNOWLEDGE_V1
