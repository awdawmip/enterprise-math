# R1/N14 monitor-safe BRC compression — continuation (author task packet)

Date: 2026-10-26. **Not** a formal immutable-V2 task, native CLAIM, Driver assignment, or Stage171 primal continuation. External finite IID auxiliary model.

## Mother question and frozen dependencies

Given positive ordered-history branch flows in a finite-alphabet IID sequential decision system, which information about observed order can be discarded while preserving a declared family of terminal and future-operation observers?

- Already proved author source: `research_notes/r1_n14_brc_observer_safe_markovization_20261026/PROOF.md` — count-only preservation of the joint terminal (T,count,decision) law.
- This run: `research_notes/r1_n14_brc_order_observer_monitor_20261026/PROOF.md` — exact count-fiber factorization criterion for universal scalar terminal observers; 2-step no-go for an ordered fifth observer; exact rescue by count plus deterministic finite observer monitor under P and Q.
- Exact executed checker: `VERIFY.py`, source/result `RESULT.json`, horizons 3,4,5.
- Global `GLOBAL_KNOWLEDGE_V1` pin `468fd2fb5d79232c1fa1f8f34d1e0519e6f5bbd2`. EM base pin `7ce2f8cebef341c08cbde799d67e93bb974655b6`. P000 / ACTIVE residual preservation / portable research protocol applied. Any subsequent research run must re-pin its own current snapshot.

## Single smallest unproved unit

For a fixed finite horizon N and a finite family of terminal ordered-history readouts f_j(h,d), construct a **provably coarsest deterministic right-congruence monitor** (possibly time indexed) such that each f_j factors through (t,k,s,d), and every transition on the next observed letter is well-defined on monitor classes.

Concrete first test input: alphabet {0,1,2}, horizon N=4, observers:
  (a) whether ordered substring 01 occurred;
  (b) whether ordered substring 10 occurred;
  (c) whether the last two symbols are equal.
Construct the finite trie states at t<=4; partition by all terminal readout vectors and refine backward under every next-letter transition until stable. Record the monitor cardinality per t, all class representatives, the transition table, and an exact proof of minimality **for deterministic transition-respecting monitors**, not for all arbitrary stochastic sufficient representations. Compare with 3-state single-substring monitor.

## Exact success/failure criterion

PASS if terminal observer factorization and right-congruence are proved for all ordered words of length <=4; an independently built enumerator checks every transition and readout. Minimality means every partition merging two distinct final classes violates a readout or a future suffix readout; produce distinguishing suffix witnesses for every attempted merge. FAIL if a counterexample demonstrates a weaker proposed bound; preserve its actual word pair/suffix.

Preserve separate proof scope for randomized policies, P/Q IID laws, and native X6 correspondence. The quotient is only observer-safe on the stated horizon and declared operations; not a lossless representation of ordered BRC paths.

## Suggested next generalization (not yet proved)

For non-IID path-dependent laws, identify a sufficient per-fiber likelihood-ratio and transition-congruence condition that permits one law-independent compressed policy. If a naive likelihood-ratio compression fails, produce a two-law rational path witness before proposing an enlarged carrier.

## Current real authority

Native `em_control_tasks`: `CONTROL_QUOTA`. Native session: `STATIC_READONLY_SCOPE_DENIED`, `operation_sent=false`. GitHub source author activity `RA-R1T11-OBSERVER-20261026T2110` uses a locally assigned session key and `EM-DIRECT-OBS21`, not a server-issued native identity. Independent Research Driver review, formal Result and X6 transfer remain pending. Do not usurp Stage171 primal ownership.
