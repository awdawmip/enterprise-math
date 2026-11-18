# R762P — Optimal secondary parity transport for four signed-X6 BRC pair channels

Date: 2026-11-14 (Asia/Shanghai). Status: author-side exact finite coding theorem, independently executable verifier; not native-physics admission.

Parent: RS-X6-TRIADIC-CLOSURE-DYNAMICS, publication TP2-8B7E13C5904A2D6F1142. Scientific pin: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Predecessor: R762O / Draft PR #2317 / c644cfd4f5d97e7ffc8be8cc32c66de05d5dd431. P000, ACTIVE X6, provenance, source labels, and the actual TRIADIC_CLOSURE_E admissibility question are unchanged.

## Exact problem

The R762O weighted pair observer has eight Boolean candidate-law bits a(t,h), indexed by two visible named source-sign bits t in {00,01,10,11} and a hidden third sign h in {0,1}. For the four disjoint hidden-sign edges, the raw positive-weighted BRC values are W_t=4(a(t,0)+2*a(t,1)). Divide by four and retain the four labelled base-four symbols x_t=a(t,0)+2*a(t,1) in A={0,1,2,3}. The map from 256 Boolean laws to x in A^4 is bijective.

R762O proved that, if every independently corruptible channel is restricted to a single native pair-edge measurement, one-error detection needs eight measurements and one-error correction needs all twelve. Here the declared channel changes: an encoder with access to all four correct labelled x_t values is permitted to transmit additional independently corruptible secondary parity symbols in A. A transmission error occurs after the entire codeword has been computed. This explicitly retains the complete law and source-pair labels at the encoder. Parity symbols are digital joint-relation transport metadata, NOT additional primitive pair-edge BRC readings, positive branch masses, physical forces or event updates. In particular, pre-encoding measurement faults are a different problem.

Question: among all (possibly nonlinear) fixed-length encoders C: A^4 -> A^n, what is the shortest n allowing detection, respectively unique correction, of one arbitrary whole-symbol substitution while retaining all 256 laws?

## Theorem A — Five symbols are necessary and sufficient for one-error detection

Encode x=(x0,x1,x2,x3) as

C5(x)=(x0,x1,x2,x3, x0 XOR x1 XOR x2 XOR x3),

where XOR is bitwise addition in the two-bit additive group (Z/2Z)^2 of the four-element alphabet. C5 has exact minimum Hamming distance 2. Indeed, for distinct x,x' the first four coordinates differ at least once. If they differ exactly once, the parity changes, so the full distance is 2; if they differ more than once the full distance is at least 2. A distance-2 code detects a substituted symbol and can recover any single known-position erasure.

For any A-ary length-n code with minimum distance at least 2, deleting one fixed coordinate is injective (otherwise two codewords differ only there). Thus 256 <= 4^(n-1), so n >= 5. C5 attains this bound. Checking the XOR of all five received symbols detects every single replacement by a different alphabet value.

## Theorem B — Seven symbols are necessary and sufficient for one-error correction

Define three parity symbols:

p0=x0 XOR x1 XOR x3,
p1=x0 XOR x2 XOR x3,
p2=x1 XOR x2 XOR x3.

Encode C7(x)=(x0,x1,x2,x3,p0,p1,p2). Its 3x7 parity-check matrix over the four-element additive alphabet has binary columns:

h0=(1,1,0), h1=(1,0,1), h2=(0,1,1), h3=(1,1,1),
h4=(1,0,0), h5=(0,1,0), h6=(0,0,1).

A nonzero one-symbol error e in {1,2,3} at coordinate j produces syndrome (h_j[0]*e,h_j[1]*e,h_j[2]*e), using multiplication by binary 0 or 1. Each of the seven columns has a distinct nonempty support and every nonzero syndrome component equals e. Hence the syndrome identifies the erroneous coordinate and its full two-bit error, and XOR correction uniquely recovers x. This establishes minimum distance >=3. Equality follows by changing only x0, which affects systematic coordinate x0 and parity p0,p1, giving distance exactly 3.

To prove global minimality for arbitrary 4-ary encoders, radius-one Hamming balls must be pairwise disjoint if one error is correctable. At length 6 a ball contains 1+6*(4-1)=19 words; 256*19=4864 exceeds 4^6=4096. Any code of length <6 could be padded to length 6, so no n<=6 solution exists. Our n=7 construction is optimal.

This is an alphabet-size and fault-model bound, not a claim about time, native force flow, or physical bit reliability. The four-symbol source acquisition is part of the encoder budget; total communication count is n=5 or n=7, not merely the number of added parities.

## Exact computation and independent check

The Python standard-library verifier at research_artifacts/R762P_CODED_OBSERVER.py enumerates all 256 candidate laws, all 32,640 unordered distinct-law pairs, and all single-symbol substitutions in each constructed code. It asserts dmin(C5)=2 and dmin(C7)=3, checks 3,840 substitutions detected by C5 and 5,376 substitutions corrected by C7, and checks the exact Hamming/Singleton inequalities. The JSON at research_artifacts/R762P_CODED_OBSERVER_EVIDENCE.json records the executed result and all seven parity-check columns. These finite checks complement the proofs, rather than extrapolating beyond the 256-law alphabet.

## Research significance and scope

With only four primitive pair-edge measurements, pre-noise joint-relation coding reduces the minimal independently transmitted channel counts from R762O's edge-only 8->5 for one-error detection and 12->7 for one-error correction. The extra symbols require a common encoder that can access correct full signed-source data, and independent post-encoding channel corruption. Faults in the primitive pair readings, restricted local-only observation, loss of source labels, or legal TRIADIC_CLOSURE_E event restrictions must be analysed using their actual interface.

The theorem shows a concrete information-repair mechanism compatible with BRC provenance preservation: four labelled joint branch counts are reconstructed exactly from the codeword. It does not discard the third source or equate positive counts with signed cancellation.

## Next genuinely unresolved scientific unit

Read the frozen Source and identify one exact typed, legal X6 Cell/Link/Port three-force closure event, including named incoming/outgoing ports and the subsequent V29 PASS/TRANSFER and V39 frame/holonomy update. Determine whether the four pair-edge observers can be collected in a lawful shared encoder before error, or whether only independently measured edge channels exist. Use the resulting actual legal event alphabet L to recompute observer-code distances and successive-event admissibility, retaining labelled origins and time indices. This remains the mother task's current hard objective; no formal Result or independent Driver review is asserted by this research note.
