# R749STV — Exact source-order fibers and minimal future-safe residual bits

Date: 2026-11-18 (+08:00). Evidence class: **AUTHOR_EXACT_NOT_REVIEWED**. Independent portable research (no shared Task CLAIM/Result/Review). Frozen source pin: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`; retain the five named weights (1,1,2,3,6). Predecessor: R749STU, Draft PR #2657, commit `dd9133125418d611583aa3a1da4ecf731e93cfe1`.

## Typed restricted carrier and observers

Use only the **two distinct named weight-one sources** A,B from the frozen five-source alphabet. A symbolic provenance trace is a word w in {A,B}^ell, ell>=0. Define its auxiliary cumulative scalar weight readings sigma(w)=(1,...,ell). Both sources have unit weight, so sigma is independent of their order. This is a *new pathwise diagnostic*, not R749STU's aggregate rational observable Y_n; no unproved map Y_n -> native event is used.

For a **proposed restricted raw X6 coordinate adapter**, choose a native Cell as chart anchor o in the signed Z^6 affine torsor, and two distinct signed native axes e1,e2. Map A to +e1 and B to +e2 as ordered unit steps. Write k=#A(w). The endpoint is o+k e1+(ell-k)e2. Other four raw signed coordinates are 0 *relative to that chosen anchor*, not erased spatial dimensions. Each word retains the entire ordered step/source/branch trace. This is coordinate combinatorics, not an assertion that these paths are physically admitted triadic events, BRC updates or heartbeat counts. ell is symbolic path length, not physical duration.

Two explicitly **different** permitted future-operation/observer scopes:

- O_cell: observe the raw X6 endpoint now and after any future appended A/B symbolic suffix. No historical-port queries.
- O_pop: also permit a *proposed typed provenance-port operation* pop that returns the final source label and removes the final trace step. Repeated pop queries the whole ordered source history. No claim is made that an existing native BRC kernel implements pop.

An observer-safe quotient identifies states only if all permitted future output sequences agree.

## Theorem 1: exact fibers

For every ell>=0, 0<=k<=ell, the fiber of (sigma, endpoint) has exactly

N(ell,k)=binomial(ell,k)

ordered source histories. In particular AB and BA have the same scalar-prefix readings (1,2) and the same *full raw signed X6 endpoint*, but distinct path provenance.

*Proof.* Sigma only depends on ell. The endpoint determines k because e1,e2 are independent native axes. Choosing k of ell ordered positions for A gives every word once, so the fiber has binomial(ell,k) members. QED.

## Theorem 2: sharp observer-specific memory budgets

(i) Under O_cell, two words are future-observationally equivalent **iff** they have equal endpoint, equivalently equal k at fixed ell. The endpoint is a sufficient lossless quotient for O_cell; extra order bits needed: 0.

(ii) Under O_pop, two words are future-observationally equivalent **iff** the words are identical. Once the endpoint (and hence ell,k) is known, the exact minimum number of extra *fixed-length bits* that preserves all permitted future observations is

b(ell,k)=ceil(log_2 binomial(ell,k)), with b=0 for binomial(ell,k)=1.

For one common fixed-length residual budget across all endpoints of length ell, this is maximized at the central content:

B(ell)=ceil(log_2 binomial(ell,floor(ell/2))).

If the endpoint is discarded and only sigma is retained, all 2^ell words share the same scalar trace, so O_pop needs exactly ell bits.

*Proof of (i).* Appending the same suffix adds the same signed native displacement to both endpoints, preserving their equality. Every allowed read is an endpoint read; unequal endpoints are distinguished immediately. QED.

*Proof of (ii), lower bound.* Sequential pop emits the letters in reverse order. Distinct words therefore have distinct possible future readout traces; all binomial(ell,k) words in one endpoint fiber must have different codes. A b-bit field has 2^b values, giving the lower bound. Without the endpoint the same argument gives ell bits for 2^ell words.

*Constructive attainment.* Use lexicographic rank r in [0,binomial(ell,k)-1] among length-ell words with k A's (A<B). At any step with a A and b B remaining, choosing B skips binomial(a+b-1,a-1) words beginning with A (0 if a=0). Add that count then decrement b; choosing A decrements a without changing r. Conversely unranking chooses A when r is less than this count, and otherwise subtracts it and chooses B. Induction on a+b proves the two procedures inverse. Given endpoint, a fixed b(ell,k)-bit rank reconstructs the exact word and therefore all O_pop output traces. QED.

Since binomial(ell,k+1)/binomial(ell,k)=(ell-k)/(k+1), the central coefficient is maximal. Also sum_k binomial(ell,k)=2^ell implies binomial(ell,floor(ell/2))>=2^ell/(ell+1), hence B(ell)>=ell-log_2(ell+1). Thus the required future-safe provenance residual grows without bound with symbolic path length when pop is permitted.

## Reproducible examples and evidence

| ell | k | same-endpoint ordered histories | extra fixed bits |
|---:|---:|---:|---:|
| 2 | 1 | 2 | 1 |
| 10 | 5 | 252 | 8 |
| 20 | 10 | 184756 | 18 |
| 40 | 20 | 137846528820 | 38 |

The accompanying pure-Python certificate exhaustively checks every source word of lengths 0 through 14: **32767** words, including all fixed-endpoint fiber sizes, exact lexicographic ranks, inverse unranking, prefix scalar readings, and pop traces. Larger examples use exact integer binomial arithmetic. Author execution: **PASS**. The all-length proof is the counting and constructive inverse argument above, not an inference from finite testing.

Files: `R749STV_PORT_ORDER_FIBER_CERT.py` and `R749STV_PORT_ORDER_FIBER_RESULTS.json`.

## Precise BRC/X6 continuation and applicability

This provides a scoped BRC-*compatible candidate* history-carrier codec, **not** a native BRC computation or mapping. It proves an exact source-provenance information obstruction even when the final X6 Cell address is preserved. It also provides an exact *safe* quotient when the declared future operations only append source steps and observe endpoints. Both claims are tied to their explicit observer/future-operation sets, consistent with P000, the ACTIVE worldview and the mandatory joint-relation observer-preservation contract.

Next unit: identify a real typed BRC Port/Cell observer and native admitted event on a minimal Cell/Link/Port example, with source/target, triadic/resource guard, branch/phase/sign/provenance and typed event clock. Determine which proposed operations really descend to that interface and whether O_cell, O_pop or an intermediate residual is future-safe. Do not equate symbolic path index, physical heartbeat, phase or precision/refinement count. Preserve the previous frozen scientific input pin and previously saved scalar results.

Research scope: exact combinatorial model-internal theorem with source-typed X6 chart adapter. Native event dynamics, actual BRC operator execution, phase interference, and correspondence to R749STU's aggregate scalar Y_n remain separate open checks. No proof acceptance or shared owner authority is asserted.
