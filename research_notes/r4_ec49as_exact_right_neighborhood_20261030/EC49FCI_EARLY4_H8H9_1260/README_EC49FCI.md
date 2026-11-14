# EC49FCI — 1,260 exact five-slot rigidity certificates (native signed X6/BRC)

Date: 2026-11-06. Scientific pin: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Predecessor: EC49FCH at 752454dad8644e247e25ab17cc598d2e6bf31ee6. Status: exact author-side finite proof; independent Driver review pending.

## Theorem

Fix the 24 original observation slots of EC49FBU, H2/H3 roots, nine-state DFA, the original horizon and terminal observer signatures, full BRC keys L=(4,2,1,0,0,0) for H4-H5 and M=(7,3,2,0,0,0) for H6-H9, and distinct ordered signed-native six-axis primitive prefixes. The exact legal-word generator is frozen_model.py in sibling EC49FCF_EARLY1_LATE3_150, Git blob d262d4a06da862823cce2e34684a59bb081f20c2.

Let E be the ten H4-H6 slots, J8 the four H8 slots, and J9 the two H9 slots. For **every** subset S consisting of exactly four distinct E slots and exactly one slot in J8 or J9, the minimum number of nonempty distinct signed-primitive-prefix edges after simultaneous legal replacement is **158**. The original witness attains this bound. There are C(10,4)*4=840 H8 cases and C(10,4)*2=420 H9 cases, so 1,260 previously uncovered five-slot neighborhoods are solved.

## Complete finite reduction

For a fixed S, let F be the union of prefixes of the 19 unchanged paths, P(w) all signed ordered primitive prefixes of a legal replacement, and R(w)=P(w) setminus F. For candidate words w1,...,w5 the exact cost is

    C = |F| + |R(w1) union ... union R(w5)|.

Let d=158-|F|. A strict improvement is equivalent to a residual union of cardinality strictly less than d. The frozen source enumerates every legal word by multiset permutations of the complete cache key, rejecting the DFA sink state and retaining precisely its terminal signature. Each distinct primitive prefix maps injectively to one bit. The verifier forms all legal residual masks for each slot, deduplicates equal masks, and keeps only masks with popcount < d. Sorting candidate pools is a permutation of the five union operations.

Starting with D0={0}, use the recurrence

    D_i = { u OR r : u in D_(i-1), r in residual_pool_i, popcount(u OR r)<d }.

The union cardinality is monotone under extension. By induction, every prefix union that can participate in a strict improvement survives; only equal masks and monotone-bound failures are removed. Thus D5 empty proves that no five-word improvement exists. The exhaustive Python verifier obtained D5 empty for each of the 1,260 cases. The existing 158-edge words establish equality.

## Reproducible evidence

Executed six disjoint exact batches: H8 [0,400), [400,700), [700,760), [760,840); H9 [0,200), [200,420). All 1,260 results have minimum=158, and no strict-improvement state survives. The hypothetical unpruned Cartesian space totals 332,078,745,600 word tuples (not the number of operations actually executed). Maximum retained intermediate states: 72. State elimination: 30 groups at depth 3 and 1,230 groups at depth 5. Nine selected cases were checked independently with direct Python frozensets of raw ordered signed prefix strings, returning 158 each.

Run from the parent research directory:

    python EC49FCI_EARLY4_H8H9_1260/VERIFY_EC49FCI.py --late 8 --start 0 --stop 400
    python EC49FCI_EARLY4_H8H9_1260/VERIFY_EC49FCI.py --late 8 --start 400 --stop 700
    python EC49FCI_EARLY4_H8H9_1260/VERIFY_EC49FCI.py --late 8 --start 700 --stop 760
    python EC49FCI_EARLY4_H8H9_1260/VERIFY_EC49FCI.py --late 8 --start 760 --stop 840
    python EC49FCI_EARLY4_H8H9_1260/VERIFY_EC49FCI.py --late 9 --start 0 --stop 200
    python EC49FCI_EARLY4_H8H9_1260/VERIFY_EC49FCI.py --late 9 --start 200 --stop 420
    python EC49FCI_EARLY4_H8H9_1260/CROSSCHECK_EC49FCI.py

Each run produces JSON rows with a canonical SHA-256. Concatenating the six rows arrays in the listed order and encoding them with Python json.dumps(rows,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode() yields SHA-256 27b87f0c53633b5502a6ba2ff658e4b0f1746efed5204a961057a2b723d0c208. EC49FCI_SUMMARY.json contains each batch hash, cardinalities and ranges. The author's complete 1,260-row evidence and scripts are preserved in the same-turn EC49FCI_1260_exact_evidence.zip, with all six original executed JSON outputs. This repository delivery includes self-reproducing verifier and per-batch immutable evidence hashes.

## Accumulated frontier and next task EC49FCJ

Together with the predecessor EC49FCH, exact fixed-schedule five-slot coverage now includes all 252 five-early cases and all 2,100 four-early plus one-late cases: **2,352** distinct five-slot neighborhoods. Next test three E slots plus two late slots (begin H7 paired with H8/H9), using the same exact residual-union recurrence to seek 157 edges or to extend the finite rigidity proof. In parallel, study alternative lawful BRC cache-key schedules as a distinct research input. The mother objective remains reducing the native X6 nine-window construction toward the unrestricted 93-edge benchmark.

Scope: author-side finite exact result for the frozen fixed-schedule legal-word domain, not an unrestricted global minimum, independent mathematical admission or physical/P000 statement.
