# R762JX.3 — Triple-color connectivity is sufficient but not necessary

Date: 2026-11-23. Model: **unsigned six-axis composite Port–Euler**, with 20 colors, 15 Port vertices and exact target histogram (seven triple, eight double, five singleton) of 42 events. Status: **FOUR_EXACT_CONSTRUCTIVE_COUNTEREXAMPLES_TO_METHOD_NECESSITY / NOT_REVIEWED**.

The new conditional lifting theorem JX.1 in \`R762JX_FULL_EULER_TRIPLE_SPANNING_LIFT.md\` requires the *full flexible triple-color candidate graph* to span every flexible-support component. This is a sufficient way to preserve connectivity while repairing parity, not a necessary existence condition.

For each inactive matching size \(m=0,1,2,3\), an explicit 42-edge connected Euler graph has now been found where this triple-spanning criterion fails.

| \(M\) (inactive Port indices) | Five singleton color indices \(D\) | Seven triple color indices \(T\) | Certificate |
|---|---|---|---|
| empty | 0,1,2,3,4 | 5,6,7,8,9,10,11 | \`CASES[0]\` |
| 0 | 4,5,6,7,8 | 0,1,2,3,9,10,11 | \`CASES[1]\` |
| 0,9 | 5,6,7,8,9 | 0,1,2,3,4,10,11 | \`CASES[2]\` |
| 0,9,14 | 5,6,7,8,11 | 0,1,2,3,4,9,10 | \`CASES[3]\` |

Indices mean that 0,9,14 are respectively Ports 01,23,45 in lexicographic \(\binom{[6]}2\) order; color 0 means 012 in lexicographic \(\binom{[6]}3\) order.

The file \`R762JX_FOUR_NONSPANNING_42.py\` stores **all 168 edges** explicitly, by 20 color assignments in each of four examples. It verifies with the Python standard library that each example has exactly one/few/multiple permissible edges per color as required, exactly 42 total, degree at least 2 and even at every active Port, zero degree at inactive Ports, and a connected full graph. It separately constructs both the flexible all-color candidate graph and the triple-only candidate graph, proving the latter fails to span at least one component. All four examples pass.

The examples were discovered by a temporary finite integer linear feasibility search (SciPy/HiGHS), then exported as integer constants and independently checked without SciPy. A correct checker for these four constants provides a direct finite mathematical certificate regardless of the searcher's floating-point or termination status.

Re-inflate each witness by adding two duplicate events of any chosen singleton color \(j\in D\); its original count becomes three and all connectedness/degree requirements persist. Thus each example is a marked 44→42 compression example even though JX.1's second hypothesis fails.

**Combined unique examples in the four fixed labeled slices:** the 2,184 earlier triple-spanning successes and these four explicitly non-spanning successes are distinct target inventories \((M,D,T)\). Therefore at least **2,188** of the 25,740 enumerated 42-event target inventories in those four slices have exact Euler witnesses. They furnish at least **10,940 marked 44→42 reductions** by the five choices of \(j\).

**Next:** The four non-spanning certificates suggest parity-flexible *double*-color triangles can preserve connectivity missed by triple-only support. Find a verifiable sufficient double+triple backbone condition and classify larger subsets of the remaining 23,552 unresolved target inventories in these four slices. These are model-internal finite claims only; source-to-P000 signed Cell/path/BRC lift remains a separate proof obligation.
