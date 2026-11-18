# EC49FGL addendum — Exact 98-edge original-24-label witness on one Pareto-only 7-key inventory

Date: 2026-11-10. Immutable scientific pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Original nine-state observer and signed native-X6 expansions (blob `7e97065ac9a0ff70435b92ee2f4bd718c9bf1859`) remain unchanged.

Select **exactly these seven raw complete positive-axis keys** from the 14 Pareto set:

```
(2,1,1), (3,0,1), (3,1,1), (4,2,1), (5,4,1), (6,3,1), (6,4,1)
```

The adjacent `WITNESS_EC49FGL_98.json` contains 24 explicit operation words: one for each originally frozen H2–H9 observation label. The standalone `CHECK_EC49FGL_98.py` expands every operation into literal ordered signed X6 primitive steps, executes the frozen nine-state DFA, checks the terminal labels, full key, endpoint `(+2,0,0,0,0,0)`, and accumulates the full prefix union. Its independently executed integer-only replay reports

```
PASS 24 frozen DFA labels; 7 complete raw keys; 98 literal native signed-X6 prefixes
```

**Exact constructive conclusion**: this one Pareto-only seven-key inventory admits a legal original-24-label path family with 98 distinct nonempty native signed X6 microstep prefixes. It is a legitimate seven-key witness, but weaker than the existing EC49FGJ 94-edge global upper bound.

**Fixed-inventory optimizer evidence (scope separate from the exact witness).** The existing EC49FGF operation-prefix model and SciPy/HiGHS MILP, run with precisely the above allowlist, returned status 0, objective `97.99999999999976`, dual bound `97.99999999999976`, zero MIP gap, using 10,901 nonroot operation prefix nodes, 1,904 shared microstep discount variables and 14,728 inequalities; execution about 12.8 seconds. Therefore **this inventory** has solver-backed optimum 98. No portable exact-integer infeasibility certificate for cost <=97 was independently exported. `SOLVE_EC49FGL_98.py` reproduces the fixed-inventory run against the already published sibling EC49FGF generator.

The useful distinction exposed by this experiment: a fully Pareto-efficient key inventory can be substantially worse (98 versus 94) on the true **shared-prefix** objective than a fixed inventory containing support/length-dominated keys. Consequently, keep Pareto-only sets as prioritized experiments; never eliminate the other 108,239 seven-key support covers in a global >=94 proof.

**Open mother-unit:** either construct a legal original-24-label witness with at most 7 raw keys and at most 93 ordered signed-native prefixes, or certify minimum >=94 across all 108,434 exact seven-key support inventories. No formal EC49AS CLAIM/Result or independent Driver admission is asserted. Author researcher `EM-DIRECT-52F078`, native activity `RA-65693E1A8CE24C095D65015E`.
