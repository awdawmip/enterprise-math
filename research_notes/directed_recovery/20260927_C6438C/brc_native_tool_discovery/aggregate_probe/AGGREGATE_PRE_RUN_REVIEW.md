# Aggregate probe static review

Verdict: PASS for the declared single execution of four fixed cases, after consuming the coordinator's actual current activity guard. No blocking mathematical or source issue was found. This review read the complete source, PLAN and frozen aggregate derivation; it did not import scientific modules, execute arithmetic, run fixtures, query a provider, or modify the reviewed source.

Reviewed byte pins:

* `aggregate_probe.py`: `830f28774f3a9e6e4aa9135dd7816c33e5cac78db6b8992990ae094b64d50b48`.
* `PLAN.md`: `de5c24bd2a0a8894be4dfd14928e0189f8a862e8d91a54d57bf4268c15d7fe62`.
* `../AGGREGATE_WITNESS_PROBE_AUDIT.md`: `c76465057ce793825916c3d22c85acc83703becfeb5154c05b362468dd5933fd`.
* Reused wrapper: `../hbw_marked_section/hbw_marked_section.py`, `e2929468d9b430f9a0ef93a3412f132c692ce994c7b5061bece21a3960974851`.

The inputs are exactly `(437,2,1),(35,2,2),(19,2,1),(25,2,1)`. The production registers start at Q=1. Doubling uses the old A in G's multiplier and its already paid square in H's multiplier, giving the stated geometric sums. Reducing q modulo N is legitimate because every readout is polynomial over the residue ring; no invertibility of q or normalized probability is assumed.

The three final probes are all computed and charged, even if an earlier probe succeeds. The readout's product equals the unstopped moment determinant up to the proved unit `a^[-2(Q-1)]`; production never computes that inverse or requests an inverse-bearing modular table. The separate paid unit-gcd admission is present. Each classification depends on the obtained gcd, and every proper factor uses the existing typed divisibility receipt. No expected factor/order enters the calculation.

Case 0 alone validates the moment/HBW bridge. Its original M2 update uses `(a+b)^2=2+a^2+b^2` under the paid inverse relation. The marked affine update correctly includes its linear term, offset sum, second-moment coefficient, doubled cross term and squared offsets. The transpose in the dual-row check applies `ell M`, and its initial L is actually checked as zero. The centered-moment identities and determinant scaling use the original fixed delta. The final `C=b^2*C_tilde` is specifically the Q=2 identity, with an explicit one-layer case guard; it is not reused at other horizons. All inverse/setup/original-moment/marked-moment/identity costs are separated from production.

The source uses typed arithmetic wrappers for scientific values; host loops only route a fixed calculation, transpose indices, classify returned labels, and sum cost metadata. Work records pending outer operations before their children. Preflight refuses existing start/success/failure outputs and creates STARTED before scientific imports. Source/dependency/guard bytes are checked before and after the run. Exceptions attempt a full available Work snapshot, then a plain-text fallback if serialization fails. This is not a complete snapshot inside an unreturned primitive and is not a partial-resume contract.

The wrapper's explicit difference calculation followed by the Route gcd readout repeats some typed subtraction. It is a visible cost, not a correctness defect; no last-minute optimization is required for this bounded unit.

Remaining claim boundary: these targeted inputs can certify the interface and sound factors, but do not establish a generic hit rate, saturation recovery, a first-hit law, support collapse, lower wall-clock cost, or a general native Shor algorithm. The PLAN states these limitations. This is a shared-context static review, not formal independent admission or an executed result.

Global-Knowledge-Sync: main@7a63984 / GLOBAL_KNOWLEDGE_V1.
