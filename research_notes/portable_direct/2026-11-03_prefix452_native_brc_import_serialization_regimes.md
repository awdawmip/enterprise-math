# PREFIX-452 — Native BRC class execution and exact serialization regimes

Date: 2026-11-03, Asia/Shanghai. Scientific status: AUTHOR_EXACT_NATIVE_CLASS_EXECUTED / UNREVIEWED / NOT_ADMITTED. Frozen scientific source: f42f2906d77f24085c123f3ccfe9667d41caa96d. Continuation of PREFIX-450 and PREFIX-451. This note is a complete scoped report, not an assertion of native Result/Review/Admission.

## Mathematical model and discriminating question

Work inside the P000 six-axis signed native spatial Cell torsor, with 12 elementary directions ±e_i, six-component raw chart x in Z^6, and nonspatial history r = number of occurrences of -e1 modulo q=3. This is an exact combinatorial/typed-BRC observer study, not a spatial seventh axis or physical heartbeat-time evolution. Let path length N=q+d-1=4, moment degree d=2. Reuse the PREFIX-450 explicit 84-word construction indexed by r=0,1,2 and 28 six-dimensional multiindices of degree ≤2; its rank=84 was proved there, and PREFIX-451 gives full reachable endpoint/history support 1059. This run answers the previously pending operational question: can the original frozen Python classes execute the source family and its state-conditioned affine future, and how much serialized information does a valid fixed-degree observer consume in three source-density regimes?

## Actual native class execution and source pin

Three byte-for-byte unchanged pinned original modules were loaded and executed as Python classes:

- src/enterprise_math/brc_transport.py Git blob be1debe367263931bd5e93fd750be3ed54624fe1, containing Affine, EffectHistogram, MomentState and their rational-matrix operators.
- src/enterprise_math/brc_control_port.py Git blob 44def6b8ac787e798d3cc2c6be16f873f91b9db8, containing ControlPacket.
- src/enterprise_math/brc_histogram.py Git blob 9a3962ec095095f14e63a91cfe6b7ebf07d9a1d1, containing WeightHistogram.

The actual test environment imports these isolated original files, checked by Git blob computation. Its sole auxiliary import is an exact test helper for rational_prime_valuations, which the experiment never calls; in a full frozen-source checkout, use the repository's original actual dependency. The existing PREFIX-450 constructor is imported unchanged from research_notes/portable_direct/prefix450_arbitrary_degree_x6_certificate.py. No original pinned class was modified. The test environment's helper has no effect on evaluated moment or control-port operations. This is direct upstream class-level integration, not an assertion that an entire project installation/deployment ran.

For every selected native word (r,x), build a native ControlPacket with one edge (r,r,1,Affine(I6,x),1), start=0, duration=4. Independent exact accumulation at each target r gives the 7×7 homogeneous second-moment matrix sum_[words in r] [x;1][x;1]^T. Native ControlPacket.moment_action({r:MomentState.from_point(0)}) equals this matrix in all three sectors. Native ControlPacket.evaluate(r,0) returns 28 distinct unit-mass terminal Cells per r; splitting the 84 edges into two actual packets and calling native alternatives reconstructs the original blocks.

For the future port at start=4, duration=1, give each historical source r two positive rational branches: to r with weight a_r=(r+2)/(r+3), affine shear x'_1=x_1+x_2 and x'_3=x_3+r+1; and to r+1 modulo 3 with weight b_r=(r+3)/(r+4), affine translation x'_1=x_1-1. This produces 168 positive-rational weighted alternatives. The three mathematically distinct computations are exactly identical: native joined-packet ControlPacket.then(...).moment_action(initial), sequential native future.moment_action(first.moment_action(initial)), and a separate exact Fraction enumeration of the 168 endpoint images. For each input residue, native joined-packet evaluate also equals direct endpoint-weight enumeration. The shear is an allowed affine BRC effect/readout; it is not asserted to be a new primitive X6 direction.

The two legal length-2 words (+e2,-e2) and (+e1,-e1) both terminate at x=0 but have historical r=0 and r=1. Native state-indexed future packets with weights 2 and 3 yield different zeroth moments 2 and 3. This is an exact control-fiber counterexample confirming the historical-label preservation requirement.

## Exact finite JSON serialization evidence

Measured bytes refer to exact UTF-8 json.dumps(sort_keys=True,separators=(',',':')) without compression. Complete histogram entries are [r, [x1,...,x6], mass numerator, mass denominator]; native quadratic moment summaries are three retained-sector records with 28 independent numerator/denominator pairs per control state. No full labeled-path provenance is included in either representation. All arithmetic values are integers/Fraction.

| Source distribution | Occupied (r,x) bins | Complete histogram bytes | Quadratic moment bytes | Histogram / moment bytes |
|---|---:|---:|---:|---:|
| All 12^4=20736 ordered native words | 1059 | 25712 | 616 | 41.740x |
| The 84 distinct PREFIX-450 native words | 84 | 1903 | 579 | 3.287x |
| A single selected native word | 1 | 33 | 196 | 0.168x |

Maximum bit length of moment scalar numerators/denominators is 14 for the full-word source and 8 for the 84-word source. The finite dense result exhibits a measured 41.74-fold JSON storage saving under the declared exact second-moment affine-future observer. The single-word result exhibits a 196/33 = 5.94-fold storage penalty for choosing dense fixed moments. Thus a sparse-support-versus-fixed-moment selection can be advantageous for this certified observer and source family. No general cross-source crossover threshold, best compression codec, in-memory footprint, or bit complexity is claimed.

The complete 1059-bin dense support was built by exact dynamic programming over the 12^4 legal ordered primitive words, respecting the -e1 history transition, and its total multiplicity checked to equal 20736. The above source-dependent byte counts are actual executed results, not estimates based solely on the coordinate count 84.

## Verification, reproducibility, remaining question

Companion executable: research_notes/portable_direct/prefix452_native_brc_integration_certificate.py. It requires a working Python 3 standard-library runtime and the immutable pinned project source, and uses the established PREFIX-450 constructor. Execute within a frozen checkout from project root with PYTHONPATH=src and python research_notes/portable_direct/prefix452_native_brc_integration_certificate.py. The executable verifies all three exact Git blobs before running the native classes; it prints individual PASS checks and exact measured JSON byte counts. In the author's isolated execution, the original import-only helper was supplied as described; exact outputs are in PREFIX452_NATIVE_INTEGRATION.log. Tests validate this q=3,d=2,N=4 case and one-step positive rational affine conditional operations. Mathematical all-q/d results are prior work, not reproved by these tests.

Next actionable research: develop a rigorously observer-safe hybrid codec that chooses sparse exact endpoint bins or full per-sector moments, with precise integer/Fraction bit-length and preprocessing cost. Examine q=3 over N>=4 and varied source sparsity, and test the selection on real native ControlPacket inputs. Preserve any path/provenance or mixed higher-order joint observation needed by the declared consumer. A separate higher-order typed BRC extension can then reuse the same direct-class test pattern.

Actual authority observed: authenticated GitHub login awdawmip with push privilege. The current private Sites gateway reports research_authority_granted=false and the native bounded em_control_tasks query returned CONTROL_QUOTA. Active native owner and Researcher-ID were unconfirmed; no formal CLAIM, Result, independent Review or Admission was asserted. The author-side research source and GitHub storage follow portable protocol; publication/readback receipt is separate evidence.
