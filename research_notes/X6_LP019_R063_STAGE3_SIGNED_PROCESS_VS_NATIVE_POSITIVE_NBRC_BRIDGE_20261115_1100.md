# X6 LP019: Frozen R063 Stage3 signed-process caller and positive native N-BRC interface

Date: 2026-11-15 11:00 Asia/Hong_Kong
Mother Task: RS-X6-LEGACY-PLANE-RECONCILIATION
Publication: TP2-B4A441B23DA3159232C2
Research lane: chatgpt-research-onhour-enterprise-math-20260923
Researcher: EM-X6-FB6990 / own SID MCP-082892eb480e45dea6d4b9fcc0491034
Classification: NEW BOUNDED SOURCE-PROVENANCE CONSUMER + EXACT TYPED BRIDGE
Status: AUTHOR-PROVED; LOCAL EXACT INTEGER WITNESSES EXECUTED; UNREVIEWED; NOT_ADMITTED

## Frozen inputs and exact old caller

Original R063 Stage3 branch: awdawmip/enterprise-math@69b7a90328bdb72852d47b338dedd7b276740ac9.
Relevant frozen source files and Git blobs:
- scripts/r063_stage3_validate_pairwise_interaction_process.py : 4fca0c160acaa2b5d257d9bc1aefe82e1e3f4636.
- research_results/R063_STAGE3/R063_STAGE3_FINAL_CLASSIFICATION.md : 295f8cd7a0f5a42458bce5583e27708082f9a636.
- research_results/R063_STAGE3/R063_STAGE3_MULTIPLICITY_SPECTRUM.json : e4f07584c42131496c218d7e06b021c84baba35b.
- research_results/R063_STAGE3/R063_STAGE3_CANCELLATION_CONFLUENCE_OR_NO_GO.md : 5e4be3be6848ed2d88b24f9b773a351f6bea1788.
- Frozen historical Driver review on current main, driver_reviews/R063_STAGE3_PAIRWISE_INTERACTION_SIGNED_CANCELLATION_DRIVER_REVIEW_20260822.md blob 32ab69b84c479f34846ae9addf4a601f80645194, accepts the Stage3 N1 sector-local process only.

Read-back of the original checker shows: local(x,y) assigns four C4 labels; interaction_cells labels Cartesian position pairs; residual_sets removes opposite C4-labelled cells by signed cancellation; oriented_product unit-normalizes the signed raw component trace; relation_weights counts derived residual-poset linearizations. Crucially the checker's independent full target native multiplicity is comb(sum(target),target[0]). It does not compute that natural multiplicity by subtracting signed process labels or by summing signed linearization weights.

## Typed interface theorem (exact, all nonnegative component counts)

Let a,b,c,d be nonnegative integers and let p and q be ordered source two-letter words with counts (a,b) and (c,d), respectively, in the frozen Stage3 i/j chart. Its derived C4 interaction rectangle has

    n(+i)=ac, n(-i)=bd, n(+j)=ad+bc, n(-j)=0.

After its explicitly typed SIGNED C4 process projection, the raw component is
    x=ac-bd, y=ad+bc.
The original Stage3 orientation/unit readout returns ordered nonnegative target
    (A,B)=(x,y) if x>=0;  (A,B)=(y,-x) if x<0.

Choose two named distinct native signed X6 axes i,j inside one declared three-axis slice (i,j,k), and explicitly fix the third displacement to zero. Embed the resulting *endpoint* as z=A e_i+B e_j with every other native component zero. Under the ordinary P000 V5 signed-axis shortest primitive-step carrier,

    B_native_short(z)=binomial(A+B,A).

Proof: A,B are nonnegative. Every shortest signed-native word reaching z uses exactly A steps +e_i and B steps +e_j: any -e_i/-e_j step or any other axis step raises word length beyond L=A+B. Thus the full native shortest-word fiber consists of the binomial(A+B,A) permutations. The Stage3 source-order/process relation is a (generally strict) derived relation of target words, not the native path population and not its natural count.

This is an endpoint/observer bridge only; Stage3 Cartesian product and destructive C4 cancellation do not become a native three-dimensional process or intrinsic multiplication. The third slice coordinate is DECLARED ZERO in this embedding, not silently omitted. For native signed endpoints with nonzero third coordinate, no transfer is claimed.

## Direct original-caller audit and sharp integer witnesses

The following were independently recomputed with Python stdlib exact integers from the frozen formulas (not by launching the historical 15,876-pair Stage3 checker):

- p=iij, q=iij: (a,b,c,d)=(2,1,2,1), interaction counts (+i,+j,-i,-j)=(4,4,1,0), signed projection (3,4), native endpoint (3,4,0), L=7, B_native_short=35. Original Stage3 spectrum separately records FOUR residual process objects, FIVE generated target words and 102 formal process witnesses for this one source pair. Each is a different typed quantity; 102 must not replace, subtract from or cancel 35.
- p=iij, q=ij: (2,1,1,1), interaction counts (2,3,1,0), signed projection (1,3), L=4, B_native_short=4. The frozen Stage3 minimal 3x2 positional cancellation witness produces source-sensitive target support {ijjj,jijj}; this subset of size 2 does not mean the full four-word native endpoint fiber has cardinality 2.
- (a,b)=(c,d)=(1,2): counts (1,4,4,0), signed (-3,4); unit-normalized target (4,3), L=7, native B=35. Unit normalization is a derived orientation operation and does not alter positivity of natural native word counts.
- Original Stage3 W2 all nine (2,1)x(2,1) source pairs: support-size matrix [[5,14,8],[14,11,14],[8,14,5]], union 31 of the full 35 target native words, independently accepted in the old Driver review. This is source-sensitive information, not a deletion of the remaining four native target words.

## No positivity-preserving signed-cancellation shortcut

Let m be any additive nonnegative path-population measure assigning one to each distinct C4 elementary interaction cell, with m(empty)=0. A C4 opposite-pair cancellation identifies (+i)+(-i) with the empty signed process component, but m of the two original positive-population cells is 2. Therefore no such additive positive-population observer factors through the destructive signed cancellation quotient. Retaining cell/source provenance or a separate positive carrier is mathematically necessary whenever positive counts must be observed after this operation.

The claim is about typed information loss, not about a physically observed force cancellation, and it neither assumes nor changes the protected P000 foundation.

## LP019 provenance decision, exact next source action

The frozen R063 Stage3 checker and accepted historical source are an actual source-located SIGNED cancellation caller. Its subtraction applies to the C4 derived signed interaction channel and its original implementation separately recomputes positive R062 N_BRC by binomial. Consequently this caller is EXCLUDED as evidence of a positive-natural-N-BRC signed-subtraction bug. The separate LP019 alleged WRONG callsite remains UNRESOLVED_PROVENANCE, as does LP011 native absolute-argmax wrong callsite. A real positive-count bug requires an actual function/dataflow where a signed coefficient replaces a positive path count; a name containing "signed_cancellation" is not sufficient.

Next discriminating action: inspect remaining frozen/current real consumers that transfer R063 Stage3 process relation_weights/formal_witness_count to N_BRC or to signed-X6 endpoints; identify exact callsites and data types before any corrective patch. Retain 28-LP dependent consumers, independent X6 Driver REQUEST_REVISION, and #2416 original pinned R063 Stage0 512-case/17-gate native replay as separate outstanding work. #2416 remained OPEN and unassigned at this read. Do not represent this exact small integer check as a rerun of that benchmark.

Sources remain independent: frozen Stage3/Driver historical evidence, X6 P000-V5 selected signed slice, original Source-author checkpoint 29 units @b80d0703b6096b22418081bce0ea70d15590163d. This X6 note is a new author-side interface/provenance audit, not an alteration, ownership claim or reacceptance of the historical Stage3 author result.
