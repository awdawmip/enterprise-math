# X6 upper structure: signed-cell endpoint quotient and ordered-provenance separation
2026-11-20 · Task RS-X6-UPPER-STRUCTURE-INTEGRATION · Researcher EM-X6-C7A253
Scientific status: new, author-derived exact finite-domain propositions; NOT independent review, not accepted Foundation, not a native TRIADIC_CLOSURE_E transition admission.

## Exact inherited model and source
Use the frozen P000 native six-axis Cell torsor Z^6, signed primitive spatial steps T_{i,eps}(z)=z+eps e_i, eps in {-1,+1}, and the verified *S6 axis-permutation skeleton* R_sigma(z)_{sigma(i)}=z_i. Source S6 interface: prior researcher EM-EMF6D046-5A2844, GitHub ca9d35a5c2a3a79ca503de6e2e7c646a3be49354 at research_artifacts/mcp/RS-X6-UPPER-STRUCTURE-INTEGRATION/MCP-c618a61189764f23846a391a08518a1a/0bf4c36b9aefb57d9d89/X6_UPPER_S6_STEP_HOLONOMY_INTERFACE_20261117.md (blob 67b2c62bd6d78f16c8f62b56d34cfb44debbbd1e). This note derives a different bounded six-axis endpoint/provenance interface, not that prior S6 commutator census.

## Theorem 1: least finite lossless endpoint alphabet on the signed unit Cell cube
Fix a Cell anchor and C={-1,0,1}^6 subset of Z^6 (729 possible signed relative endpoints). Let q3:Z^6 -> (Z/3Z)^6 reduce every coordinate modulo 3. It is injective on C. Any function from C into a finite set that preserves the ability to reconstruct every z in C must have >=729 images (therefore >=ceil(log2(729))=10 fixed-length binary bits). q3 achieves exactly 729 values.

Proof: integers -1,0,1 have distinct residues 2,0,1 modulo 3, so q3 is injective in each coordinate and on their Cartesian product. Pigeonhole gives the lower bound with no assumption of linearity or rotational invariance. Note that 10 fixed bits is only a storage lower bound, not a model of its physical cost.

The S6-equivariance diagram commutes exactly: q3 R_sigma=Rbar_sigma q3. Every signed primitive spatial step also descends to a well-defined quotient step: q3 T_{i,eps}=Tbar_{i,eps} q3. The twelve signed step effects from zero are distinct modulo 3. Consequently the established S6 cross-interface
R_sigma T_{i,eps}=T_{sigma(i),eps} R_sigma
holds exactly in this finite quotient, for all sigma and signed ports, and the prior commutator h=eps(e_{sigma(i)}-e_i) remains visible whenever sigma(i)!=i. This proves one operation-safe endpoint observer under the *declared* rotation/translation skeleton.

Proof: permutation of coordinates commutes with coordinatewise reduction; additive reduction commutes with ±1 primitive translations. The two nonzero entries of h, with opposite signs, remain nonzero modulo 3. q3 never identifies distinct sign-cube endpoints, including all prefixes of paths that use each of the six axes at most once (one choice of sign per axis). These are endpoint and observer claims, not evidence that full BRC path histories or force-event legality survive.

## Theorem 2: ordered BRC provenance cannot be recovered from any endpoint-only quotient
Fix signs eps_1,...,eps_6 in {-1,+1}. For all 720 permutations pi of six different native axes, consider the length-six native primitive word
w_pi=(T_{pi(1),eps_{pi(1)}},...,T_{pi(6),eps_{pi(6)}}).
All 720 paths have the same final Cell endpoint z_final=z_initial+sum_i eps_i e_i, but are different ordered port histories. Any augmented state or output required to reconstruct the *complete order* of these histories has at least 720 distinguishable states above that fixed endpoint, or >=ceil(log2 720)=10 fixed-length bits of additional branch information within this fiber. A six-step axis permutation is one exact optimal label for this narrowly defined history family; it does not provide a general all-length path codec.

Proof: translations along distinct axes commute on endpoints; the 720 port sequences differ at their first differing position. An endpoint-only map factors through a single common endpoint and must identify every pair, even if the endpoint quotient is exactly q3. Injectivity of an order-reconstructing augmented readout on this fiber forces >=720 values. The construction uses the actual allowed signed primitive *spatial steps* as a formal path alphabet; it does not assert these sequences are all permitted force/triadic events in a higher native gate language.

## Sharp scope limits and integration
q2:Z^6 -> (Z/2)^6 represents only 64 signed-cube endpoints: +e_i and -e_i collide, so it cannot preserve signed port direction in this domain. q3 is faithfully lossless on C but not on all Z^6: z and z+3e_i collide. q3 is an exact finite quotient transition system for all lengths in its own reduced observation semantics, not an inverse to the entire infinite Cell. Theorem 2 shows that a typed decorated state must retain a separate ordered provenance factor if future observers can query that order. A product q3(Cell)×History is a permitted formal interface; its physical independence/minimality and completeness for actual X6 triadic closure, native time, internal channels, non-FCC carrier and BRC readout remain open and require their own pinned operator tests. Preserve original author and any additional prior contributors.

## Exact verification
A new standard-library checker exhaustively tested the 729 signed-cube endpoints, all 720 S6 coordinate permutations (524880 covariance input pairs), injectivity of q3, all 12 signed step images, and 64 distinct mod2 images; six-axis order history cardinality is 6!=720. The combinatorial proof, rather than the finite checker alone, establishes the stated quantifiers. Source manuscript and checker must be authenticated before counted as a canonical result.
