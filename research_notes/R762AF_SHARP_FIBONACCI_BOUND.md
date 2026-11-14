# R762AF — Sharp Fibonacci upper bound for chronological source-blind BRC fibers

Status: author-side conditional theorem and exact reproducible test; NOT_REVIEWED / NOT_NATIVE_ADMITTED.
Source: R762AE, 02c36f124254fb5da5122ebf3d1c6251001c0eb8. Task RS-X6-TRIADIC-CLOSURE-DYNAMICS, TP2-8B7E13C5904A2D6F1142. Frozen P000 a72226e2430ffa4786321ac86e7f0c599d5f0389. The prior EM-X6-3050F6 CLAIM is historical provenance, not present authenticated author/owner authority.

## Assumptions

The same *conditional* capacity-two hub star as R762AC–AE has m named, initially occupied unit-capacity outer ports. Every source token ingresses once and egresses once to a different destination; every port i emits I_i before receiving O_i. The hub starts and ends empty, and each chronological transcript tau records all I/O port labels in order but suppresses the outgoing source token identity. An admitted full-moved-support sequence has 2m steps, never exceeds two simultaneous hub tokens, and its terminal source map is a derangement. A(tau) denotes the number of distinct compatible source maps, equal to the 0/1 permanent defined in R762AE. This is neither P000 force admissibility nor a V17/V39 physical update.

## Lemma 1 (the cycle-block interval property)

**For any compatible source permutation, each directed nontrivial permutation cycle occupies a consecutive interval in the chronological ingress ordering.**

Proof. If a cycle C has only a nonempty proper subset U of its source tokens already ingressed, at least one token of U must be destined for a port in C\U: a single directed cycle has no nonempty proper subset closed under its permutation. The token cannot exit because its destination has not yet been vacated and therefore remains as a blocked hub occupant. If the first ingress of a different, unstarted cycle D occurred at this point, that new token would likewise be blocked, since its distinct destination belongs to D and has not yet ingressed. The two blocked tokens fill the hub, leaving neither a legal output nor room for another ingress, contradicting the existence of a complete execution. Thus a cycle's last ingress must precede the first ingress of another cycle. Repeating yields an ordered partition into consecutive ingress intervals. A final egress from the preceding cycle may overlap an ingress of the next one, but not this order of ingresses. QED.

## Lemma 2 (unique one-cycle source map per cycle interval and observed word)

**Given a fixed interval of ingress labels and the restricted I/O transcript, at most one compatible source map forms a single directed cycle on that interval.**

Proof. Until the final ingress of that cycle, at each moment just before the next ingress there is exactly one blocked hub token t and one vacant port v belonging to a connected open permutation path; otherwise the cycle would have prematurely closed. Initially the pending token and vacancy both carry the first ingress label. At the next ingress x, the hub contains t and x, and the vacancies are v and x. The next recorded output has exactly two compatible ways to extend this one connected path: O_x forces t to exit into x (leaving x pending and v vacant); O_v forces x to exit into v (leaving t pending and x vacant). An output t->v would close a proper subcycle prematurely, and x->x is a forbidden fixed point. The observed output label determines which of the two moves happened. The last ingress and final outputs are forced by the same rule. Thus the given temporal port word uniquely determines its one-cycle matching, if one exists. Projecting interleaved outputs of other disjoint cycles away does not affect this forcing rule. QED.

## Theorem AF1 (sharp universal maximum; closes AE's conjecture)

For every integer m>=2, among physically realizable complete chronological source-blind transcripts,

$$
\boxed{\max_{\tau} A(\tau)=F_{m-1}},
\qquad F_0=0,\ F_1=1,\ F_{n+2}=F_{n+1}+F_n.
$$

Proof. Fix tau, and order its m ingress labels as p_1,...,p_m. By Lemma 1 every compatible derangement gives a composition of m into consecutive cycle-block lengths >=2. By Lemma 2 there is at most one source permutation for each such ordered block partition. Hence A(tau) is at most the number c_m of compositions with parts >=2. The counts satisfy c_0=1,c_1=0,c_m=sum_{j=2}^m c_{m-j}; equivalently c_m=F_{m-1} for m>=2. For sharpness, use the explicit R762AE chronology I_0,I_1,O_0,I_2,O_1,...,I_(m-1),O_(m-2),O_(m-1). R762AE proves exactly F_{m-1} compatible maps for this chronology. Thus the global maximum equals F_{m-1}. QED.

**Corollary AF2.** If a later query can distinguish every final source permutation, while the complete chronology tau is already known, the sharp worst-case *fixed-length* source-identity repair requirement is ceil(log2 F_(m-1)) bits. This is an observer-specific exact combinatorial statement, not Shannon entropy, full future-operational equivalence, a signed BRC amplitude, or native force admissibility.

## Independent verification

The executable R762AF_FIBER_VERIFY.js enumerates all physically realizable words after relabeling the ingress order to I_0,...,I_(m-1). The relabeling is bijective and preserves source fibers, so this is exhaustive modulo simultaneous port/source renaming. An exact physical token-mask dynamic program counts compatible source choices for each observed word. A *separately implemented* composition-of-contiguous-cycle-blocks dynamic program checks the same integer for each word using the unique forced one-cycle replay of the word restricted to each block. A third construction replays the explicit Fibonacci extremizer.

The complete normalized enumeration covers m=2,...,11. Numbers of physically realized normalized transcripts: 2,4,12,32,88,240,656,1792,4896,13376. Their maximum source fibers are 1,1,2,3,5,8,13,21,34,55. All comparisons passed with exact integer arithmetic; the JSON evidence is machine-generated by the same executable. The theorem for all m follows from the proof, not by extrapolating these finite checks.

## Boundary and next research question

No proof here admits the auxiliary star as a native TRIADIC_CLOSURE_E, or supplies its actual signed-source PASS/TRANSFER alphabet, V17 internal frame rule, V39 transport or multi-macro repeat legality. The m>6 tests are entirely abstract; even within six X6 axes, m>3 is a nonprimitive auxiliary population. P000 and ACTIVE worldview are unchanged. This GitHub contribution is author-side preservation, not a Source CLAIM, PROGRESS, Result or independent Driver review.

Next: use the actual native triadic force incidence/update laws to restrict the admissible source-to-port permutation graph and temporal transcript language, and determine the resulting BRC fiber bound and source-preserving observation/repair requirements.
