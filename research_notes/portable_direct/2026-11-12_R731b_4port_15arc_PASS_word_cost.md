# R731b — Sharp off-diagonal four-port PASS-word cost for 15-arc BRC transport

Date: 2026-11-12. Parent: `RS-X6-TRIADIC-CLOSURE-DYNAMICS`. Author-side exact follow-up to R731. Frozen P000 scientific pin: `a72226e2430ffa4786321ac86e7f0c599d5f0389`. V29 source grammar declared separately from `research_notes/X6_NETWORK_EVENT_LEDGER_AND_CONTRAST_TRANSDUCER_V29_20260906.md` at Source `30fb16d39465708fd1b54c70a58d06ad20f310f8`. Two abstract carriers and V17 law: R730 `8fdfef5e3f2097d9e6ebb29682b2b81a6ea0247a`.

## Exact coding theorem

Fix one Cell with \(p\ge2\) local *port labels* (not spatial axes). Restrict to off-diagonal native V29 PASS event types \(\operatorname{PASS}(a\to b)\) with \(a\ne b\). There are \(q=p(p-1)\) such typed count operations, each incrementing a single nonnegative native \(M[a,b]\) counter.

Encode each of 15 distinct abstract directed arcs with an *ordered word of exactly \(\ell\) PASS operations*, so different arc labels have different words and decoding starts at a known word boundary.

**Theorem:**

\[
\boxed{\text{An injective fixed-length code exists iff } [p(p-1)]^\ell\ge15.}
\]

**Proof.** There are exactly \(q^\ell\) ordered words of length \(\ell\). Necessity follows from injectivity; sufficiency follows by selecting 15 distinct words. Each word's letters denote legitimate V29 positive count increments in the specified no-capacity-gate grammar, and a fixed block boundary permits unique decoding. Concatenated words preserve ordered BRC branch provenance, their positive multiplicities and exact ledger grade \(\Delta\Gamma=\ell\) per abstract arc. ∎

Sharp resource table:

| Local ports \(p\) | Off-diagonal PASS symbols \(q\) | Minimum fixed word length \(\ell\) |
|---:|---:|---:|
| 2 | 2 | 4 |
| 3 | 6 | 2 |
| 4 | 12 | 2 |
| 5 | 20 | 1 |
| 6 | 30 | 1 |

Thus R731's six-port one-PASS interface can be reduced to **five ports**, which is sharp under one-off-diagonal-PASS-per-arc injectivity. A four-port Cell cannot assign 15 distinct arcs to 12 one-PASS labels, but admits a two-PASS-per-arc code. Diagonal PASS labels are excluded by the precise stated coding problem.

## An explicit four-port two-PASS code

Enumerate the 12 off-diagonal port pairs on labels \(\{0,1,2,3\}\) lexicographically, indexed \(0,\ldots,11\). Enumerate each carrier's 15 arcs in R730's original 60-arc order. For arc index \(i=0,\ldots,14\), encode

\[
\boxed{\jmath(i)=(\lfloor i/12\rfloor,\ i\bmod12).}
\]

These are 15 distinct two-letter words over the 12-symbol native V29 PASS alphabet.

Define an auxiliary coupled transducer which performs the two authentic V29 PASS count operations of a codeword *in order* and then performs the explicitly declared V17 active-triad/slot successor update. For every cyclic-nonbacktracking abstract path with \(m\) arcs, exactly one ordered lifted history exists with \(2m\) PASS operations and \(\Delta\Gamma=2m\). Consecutive two-event block decoding reconstructs all arc labels and path provenance. For an online partial-block Markov implementation, the code boundary/phase and first pending port symbol must be retained or recoverable from event history; cumulative M alone forgets event order.

The inherited V17 frame holonomies and seam checks are unchanged:

| Carrier | CNB loop | Holonomy | First abstract frame return | Actual PASS events and \(\Delta\Gamma\) |
|---|---|---|---:|---:|
| A | `012>023>123>012` | `102` | 6 arc steps | 12 |
| B | `012>023>123>013>012` | `201` | 12 arc steps | 24 |

The abstract all-length six-state reachability of R730 transfers by this exact code to the *declared coupled event model*. Full native V29 ledger return still fails whenever the event history is nonempty.

## Verification and research boundary

The standalone `R731B_4PORT_CODE_VERIFY.js` reconstructs both original 15-arc masks and all 12 off-diagonal symbols; checks codeword injectivity, unique block decoding, V17 slot updates, cyclic seam legality and the two first-return witnesses. It exhaustively checks nonbacktracking rooted prefixes through 7 arc steps: **419** for A, **382** for B. `R731B_4PORT_CODE_RESULTS.json` records exact generated codebooks and integers, with `status=PASS`. The universal statements follow the finite-alphabet bijection plus grade induction.

This is an exact **count-event coding law**. Two PASS events are not two P000 primitive force quanta, and the coupled V17 successor selection is an explicitly declared model interface, not an already established force law. The remaining parent-task objective is to attach a genuine Cell/triad native force action certificate, the three nonzero signed X6 force occurrences, `TRIADIC_CLOSURE_E`, rotation covariance and a source-backed scheduler.

**Next:** specify one permitted signed X6 Cell force-triad event with a native closure certificate, and test whether both one-step/five-port and two-step/four-port codes can be scheduled while retaining ordered BRC provenance.