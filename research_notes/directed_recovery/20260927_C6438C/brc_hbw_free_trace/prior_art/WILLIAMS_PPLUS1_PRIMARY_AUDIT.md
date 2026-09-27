# Free-trace HBW and Williams p+1: primary-source boundary

Status: **PRIMARY_SOURCE_COMPARISON / SYMBOLIC_INTERFACE_AUDIT / NO_SCIENTIFIC_EXECUTION**.
Shared author context: `EM-DIRECT-C6438C`, activity `RA-CAAAC604CB513AEA8BBC1DFC`.
This is a shared-context source check, not an independent admission or a new factoring experiment.

The free-trace companion reaches the classical split/nonsplit Lucas mechanism. Its trace-only smooth-exponent factor probe is already present in Williams p+1 implementations. The useful project contribution to pursue is a precisely typed geometric observer and certificate contract. Neither free trace, a conic drawing, nor logarithmic-time evaluation at a supplied exponent closes general Shor order finding or factoring.

## 1. Actual reading and attribution

**Williams original: reference identified, full text not read.** H. C. Williams, *A p+1 method of factoring*, Mathematics of Computation 39 (159), 225–234 (1982), DOI [10.1090/S0025-5718-1982-0658227-7](https://doi.org/10.1090/S0025-5718-1982-0658227-7). Root reported an AMS access refusal; this subtask did not retry or bypass it. The title, journal, year and pages were corroborated in the author-hosted implementation and the independently read reference below. No assertion here depends on pretending to have read Williams's complete proof.

**Direct implementation primary source.** Paul Zimmermann and Alexander Kruppa's [GMP-ECM pp1.c source coverage snapshot](https://members.loria.fr/PZimmermann/ecmnet/cov/ecm/pp1.c.gcov.html), dated 2022-03-21 on the page, was actually read. Source lines 25–29 cite Williams and Montgomery's Lucas-chain work. Lines 54–58 specify the Lucas doubling/differential-addition identities; 77–80 initialize adjacent V values. Lines 172–205 accumulate prime-power exponents; 225–226 subtract 2 and compute a gcd. Lines 243–255 distinguish a split P−1 hit using the character of the initial seed squared minus 4. This is direct implementation evidence, not proof that the present installed GMP-ECM version is identical. Coverage counters belong to that published snapshot, not to our run.

**Primary analysis paper, correctly identified.** The public [Dartmouth paper100 PDF](https://math.dartmouth.edu/~carlp/PDF/paper100.pdf) is Carl Pomerance and Jonathan Sorenson, *Counting the Integers Factorable via Cyclotomic Methods*, Journal of Algorithms 19, 250–265 (1995). It is **not** Williams's original. We visually read printed pp. 250–253 and 262–265; the relevant complete section is §3 on p. 263 and its continuation on p. 264. It explains that the p+1 algorithm can benefit from a factor with either smooth p−1 or smooth p+1. Its counting questions concern populations of inputs and specified arithmetic budgets. They do not furnish a polynomial-time guarantee for every unknown composite. Reference 25 on p. 265 identifies Williams's 1982 paper. We did not audit the unviewed middle proof or import its asymptotic constants.

**Author-maintained corroboration.** Zimmermann's [p+1 record page](https://members.loria.fr/PZimmermann/records/Pplus1.html) attributes the method to Williams and describes the favorable p+1 smoothness situation. The record table is historical evidence of this method's use; it is not a runtime benchmark for our candidate.

The scanned Dartmouth PDF was downloaded from its already accessible author URL for local rendering because the web extraction returned no text. Its exact downloaded bytes are 563376, SHA-256
`35f1f18597bb9bd5a68b0c98a151c42b65c41f20319e6f9262b9ed09f5cf8e4c`.
The file is `pomerance-paper100.pdf`. Page PNGs are reading intermediates, not newly authored research figures.

## 2. Explicit algebraic correspondence

The following calculation is our symbolic identification of the candidate interface; it is not a quotation from an unread Williams paper.

Let
`M=[[0,1],[-1,k]]`, `Delta=k²−4`, over `Z/NZ`.
Cayley–Hamilton gives `M²−kM+I=0`. Therefore
`V_n=tr(M^n)` satisfies
`V_0=2, V_1=k, V_(n+1)=k V_n−V_(n−1)`.
Also `V_(2n)=V_n²−2` and
`V_(m+n)=V_m V_n−V_(m−n)`.
Thus this trace is exactly the V recurrence used by the cited pp1.c snapshot, with its initial seed corresponding to k. The companion can be evaluated without computing an eigenvalue.

For an odd prime p with nonzero Delta, the two eigenvalues are lambda and its inverse. In the split case they lie in the base field, so the order divides p−1. In the nonsplit case Frobenius swaps them, so the order divides p+1. This is the local Lucas/p-plus-minus-one mechanism. If k was previously forced to be a+a^(-1), Delta=(a−a^(-1))² and every regular local component was split. Free k genuinely enlarges the project's accessible geometry, while reusing established number theory.

For the same supplied E, `gcd(V_E−2,N)` is exactly the trace probe in the cited implementation. Any proper gcd is a valid divisor. A global return or a saturated gcd is not itself a proper factor or an exact-order certificate.

## 3. What remains distinct in the native observer contract

The local parent note
`../FREE_TRACE_TORUS_WITNESS.md` was read at SHA-256
`6ad4bbf2db92ffbec7fc57c8da3e16aca9f43a6fb05b89a73aa396aca6f1730c`.
Its companion refinement
`../TRACE_SQUARE_VALUATION_LEMMA.md` was read at
`35a8259080ccfb7b608eab922a1562c20836e718b9dff09f2af6209937bcb3d5`.
They remain unchanged.

For the fixed cyclic mark v=(0,1)^T and residual
`M^E v−v=(x,y)^T`, direct commutation gives
`M^E−I=[[y−kx,x],[-x,y]]`.
Consequently the common coordinate gcd
`g=gcd(N,x,y)` equals the common gcd of all matrix-return entries, even over a composite ring. This is a complete matrix-return observer, unlike an isolated coordinate zero.

The already proved regular odd-modulus valuation identity is
`gcd(tr(M^E)−2,N)=gcd(g²,N)`.
It has an important limitation: **for squarefree N, the trace gcd and common-coordinate gcd are identical**. Preserving the common return ideal avoids square inflation at repeated prime factors; it does not improve the successful divisor or hit probability on regular squarefree inputs. A proper coordinate-only gcd may be used by a weaker factor-only contract, but must not be mislabeled a simultaneous matrix return.

These are independently stated project interface proofs. This narrow literature check does not establish global originality of cyclic-vector or ideal-based readouts. Nor does it make the common-coordinate implementation automatically cheaper than the established trace computation.

Native reuse still requires actual source-compatible BRC arithmetic, the declared HBW macro/observer boundary, gcd and exact-division receipts, and honest setup/exponent/retry cost accounting. The current candidate is not an already executed native Lucas engine.

## 4. Why the prior art matters for the next step

A public smooth exponent can supply a conditional certificate: if it is a multiple of a local matrix order and not of every component's order, a proper divisor can emerge. With `E_B=lcm(1,...,B)`, each necessary prime-power factor must fit the chosen exponent. Small prime factors alone do not imply that every required prime power divides E_B.

Fast evaluation uses the supplied exponent's bit length. It does not supply an efficiently successful exponent, prove that an unknown p±1 is suitably smooth, or guarantee separation rather than saturation. Trying free traces changes elements and split type; its success distribution and total retry cost need a separate bound. A matrix-order multiple also does not certify the original Shor multiplier's exact order.

The defensible continuation is to implement and compare the declared weak factor-witness contract, with the classical Lucas trace as an explicit baseline, and prove any new exponent-selection or geometric-family advantage separately. No general success probability, asymptotic advantage, independent novelty, or Shor closure was established by this source check.

## 5. Shared-turn query receipt: no extra submission

Current canonical GK was actually obtained by the unchanged repository helper as
`8c23cca3ed79ca2d6ecbdf76734606eabd94fd0d`.
The three canonical entry files were unchanged relative to the previously read c552 snapshot. Current professional routing, cache policy, execution protocol, transport protocol, professional README and catalog were read. The actual pinned KQB capability enables `scholar.paper_search`; its connector response is saved as `KQB_CAPABILITIES_CFC2ACA_READBACK.json`.

There is no matching Williams/DOI source record in the catalog. However, the shared standard turn
`4ec7c225-8ee0-4565-9d9c-36957858ba21`, conversation
`01a079d7-5d03-7a21-abe9-f70606fee0ee`,
already has **3 accepted jobs out of 3**:
[issue 2489](https://github.com/awdawmip/kimi-query-bridge/issues/2489) used two, and
[issue 2495](https://github.com/awdawmip/kimi-query-bridge/issues/2495) used one.
Both identities and accepted receipts were checked against preserved canonical source data. The later 2497 record belongs to another historical turn. PARTIAL child results and FAILED envelopes do not erase accepted-job usage.

Accordingly, no Williams query was submitted, no batch UUID was minted, and no new turn or mode was used to reset quota. The proposed exact-title Scholar query remains merely a proposal. `PROFESSIONAL_QUERY_EXECUTION_RECEIPT.json` records **BLOCKED_BEFORE_SUBMISSION / CURRENT_QUOTA_LIMIT**, with the observed ledger in `SHARED_TURN_QUOTA_AUDIT.json`. The unchanged canonical validator passed this administrative receipt; see `RECEIPT_VALIDATION.json`.

Only the dedicated query subflow is blocked. Public primary-source reading and independent symbolic research continued. No Williams provider result, complete literature search, or global canonical archive was created. These files are local evidence; the parent may publish them through its authorized checkpoint process. There was no scientific execution or remote write in this subtask.

Global-Knowledge-Sync: main@8c23cca / GLOBAL_KNOWLEDGE_V1.

