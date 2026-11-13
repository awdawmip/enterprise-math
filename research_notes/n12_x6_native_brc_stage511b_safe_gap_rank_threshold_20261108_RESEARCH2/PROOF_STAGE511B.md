# Stage511-B — D_h-safe gap provenance cap improves from K to K−1

Date: 2026-11-08 Asia/Shanghai. Status: author-side mathematics with local exact checks; independent Driver review outstanding.

**Source lineage:** Stage510-B at immutable commit `0fc5434f76d8483125bea72dae37a32e54d1eed6`, files `PROOF_STAGE510B.md`, `NEXT_STAGE511B.md`. Scientific freeze preserved as recorded there: GK `bf84bd7c61a2444b59b1da96be57df0e9ae47e53`; EM `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`; P000 blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`. Contemporary behavioral entry read separately: GK `76363534cd78ed0ef30a5d58ea0e17963f9bc49c`; EM `7712b96451d8484c04fec9055341650c0bb3c8cd`.

## 1. Model and claim

Native signed X6 alphabet A={±E1,...,±E6}; each token carries a private original identity and public provenance tag P/O. The BRC observation F is the complete triple (history length, signed six-coordinate displacement, all 144 directed adjacency counts). Let the horizon be h. Operations: POP; DELETE2 (third from end); INSERT2(a) (new P-tagged token immediately before the final two); SET_END(r,a) for r in a fixed finite set R; DELETE_KTH_PUBLIC(k) for k in nonempty finite S⊆N+. Set K=max(S)≥1. Operation legality and F after all prefixes of length ≤h are observed; exact total public-count is *not* a direct observer.

As in Stage509–510, compute D_h(w) **from the full, original identity-and-tag skeleton**: the original token identities which can be directly SET or deleted at a reachable pre-action state of length <h. Every such original remains explicit. All other maximal original intervals (gaps) are immutable under the declared horizon; INSERT2 does not split a gap, because its adjacent left original is exposed by the available DELETE2 operation in the same pre-action state. The Stage510 F monoid remains unchanged.

**Theorem 511.1 (safe-gap saturated count).** Instead of the Stage510 gap public count min(K,#P(g)), save

`c(g)=min(max(0,K−1),#P(g))`

for each opaque gap g, alongside its unmodified full F(g). Together with the explicit tokens in D_h(w), this represents the legality and exact full F of every allowed operation sequence of length ≤h. In particular if K=1, all opaque gaps require **no public-count metadata at all**.

**Proof.** Put T=K−1. Consider an arbitrary reachable pre-action word at depth t<h and a ranked P deletion k∈S, k≤K. Traverse its ordered pieces from right to left and let r be the residual rank upon entering any opaque gap g. Initially r=k; previous exact explicit singletons and gaps with count <T remove the same rank in both evaluators. The *only* possible discrepancy at g is p(g)≥T but min(T,p(g)) differs from p(g).

If 1≤r≤T and p(g)≥T, the true ranked deletion would target an original P inside opaque gap g. This contradicts construction of D_h(w): that original would be a directly deleted original in a future of length ≤h and hence would be explicit. If r=K=T+1 and p(g)≥K, the same contradiction holds. Therefore, whenever the evaluator actually reaches an opaque gap with r>0, either p(g)<T (count unchanged), or r=K and p(g)=K−1 (count unchanged), or p(g)=0 when K=1. Hence each true surviving rank and the capped rank route make identical skip/selection/legality decisions. A selected original P is always explicit. This reasoning applies at every reachable pre-action state and hence inductively to all legal futures. Positional legality is decided from lengths and edits act only on explicit pieces, while the 6D and all 144 directed adjacency counts compose exactly by the unchanged F monoid. QED.

The argument is **specific to D_h-safe opaque gaps**, not generic piece-rank search. Generic routers still need Stage510's K cap. It does not eliminate cost of computing exact D_h.

## 2. Sharpness within this cap representation

**Proposition 511.2.** For each K≥2, there exist h=1, S={K}, finite R and two native tagged histories with the same D_h explicit mask and identical gap F, but different responses to DELETE_KTH_PUBLIC(K), which are conflated by cap K−2. Thus K−1 is the smallest **uniform** cap sufficient over all such D_h-safe histories (including choice of S,R).

Construct two initial P-tagged prefix directions (+E1,+E2). Follow them by a gap of g=max(K,4) repetitions of +E3, with exactly K−2 (first word) or K−1 (second word) P tags. Finish with five O-tagged +E4 directions. Let n=2+g+5 and R={n−1,n−2} (zero-based end offsets), ensuring the two prefix originals are explicitly targeted by allowed SET_END actions. With h=1, POP, DELETE2 and SET_END(0) affect the suffix, and INSERT2 has no extra original direct target. DELETE_KTH_PUBLIC(K) deletes +E1 for the first word and +E2 for the second; neither touches the gap. Therefore both D_1 masks agree and omit the gap. The two gap F summaries agree (direction words equal), and both truncated counts at threshold K−2 equal K−2. Yet the observed displacement after the deletion differs by (−1,+1,0,0,0,0) between the two deletion choices. Threshold K−1 distinguishes their public counts exactly. QED.

For K=1 the sufficient cap is 0, which is minimal among nonnegative caps.

**Bit consequence:** each opaque gap of length g needs at most ceil(log2(min(K−1,g)+1)) public-count bits versus Stage510's ceil(log2(min(K,g)+1)), with K=1 requiring zero bits. This concerns source-count metadata, not the six coordinates/144 edges or D_h preprocessing.

## 3. Executed finite tests and scope

The independently written Python-standard-library program in `REPRO_STAGE511B.py` executed 6,800 tagged two-direction word/parameter roots (n=2,...,5), 932 comparisons of future response trees sharing the same cap-(K−1) signature, 15,828 reachable pre-action nodes, and 135,812 operation transitions. All assertions passed. It also checks the sharpness construction at K=2,3,4,5,6 with native six-coordinate displacement and all 144 adjacency coordinates. An independent exploratory scan at S={1,3} found no cap-1 collision for 21,840 roots at h=1; h=2 scans are also finite and do not establish a general cap-1 theorem. Raw summaries: `STAGE511B_EXECUTED.json`, `STAGE511B_SECONDARY.json`. General theorem is proved above rather than inferred from finite testing.

## 4. Next unresolved units

(a) Compute D_h by a compressed reachability transducer, not all future identity/tag skeletons; compare identical n=19,h=3 and n=28,h=2 cases with complete preprocessing/time/RSS. (b) Determine S- and R-specific optimal caps, especially S={1,3} and K=3 with h≥2; differentiate exact proof from finite collision-free scans. (c) Independently benchmark complete twelve-direction, all-144-active heterogeneous Euler–BRC exact rank **and unrank** with full big-integer, input-encoding, precomputation and verification costs.

**Authority:** GitHub identity is authenticated as awdawmip, but the Enterprise Math native session request `em-r2-stage511b-20261108-session-001` ended FAILED/OSError and task list request `em-r2-stage511b-20261108-list-001` ended WAITING_RESOURCE/OSError at this research checkpoint. No authenticated CLAIM, native Result or independent Driver review is asserted.