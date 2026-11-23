# R762JV — Five singleton colors: exact parity-channel component classification

Date: 2026-11-23 Asia/Shanghai. Model: six-axis **composite Port–Euler observer** only. Status: EXACT_FINITE_COMPONENT_ENUMERATION + elementary GF(2) rank proof, NOT_REVIEWED. This follows R762JU (four singleton pencil repair) and studies the next structural question for the remaining 44-event histograms.

## Statement and finite domain

Set A={0,...,5}, P=C(A,2), S=C(A,3). For a matching M of m inactive Ports, m=0,1,2,3, put V=P\M. For each five-element singleton-color set D subset S, form a graph G_F(D,M) on V by including all three triangle sides from each **flexible non-singleton color** s in S\D for which all its three Ports belong to V. Graph components are counted on V, including isolated vertices.

**Parity-rank lemma (exact):** Let U be the GF(2) linear span of all local degree-boundary vectors e_u+e_v from those flexible non-singleton color sides. If G_F(D,M) has c connected components, then rank(U)=|V|-c. The full even-degree boundary space on V has dimension |V|-1, so the flexible non-singleton colors alone have parity-span deficiency **c-1**. This follows by choosing a spanning forest of G_F and observing that its incidence vectors form a basis of the direct sum of even-boundary spaces on the connected components. No numerical approximation occurs.

## Complete S6-representative enumeration

For each m, choose a canonical matching M: empty; {01}; {01,23}; {01,23,45}. Every m-matching is S6-equivalent to this representative. Enumerate all C(20,5)=15504 different D exactly and compute components by a disjoint-set forest on all active Ports.

| m | active Ports | connected U graph | disconnected U graph | maximum parity deficiency |
|---:|---:|---:|---:|---:|
| 0 | 15 | 15,264 | 240 | 1 |
| 1 | 14 | 14,332 | 1,172 | 2 |
| 2 | 13 | 11,496 | 4,008 | 4 |
| 3 | 12 | 8,272 | 7,232 | 5 |
| **Total** | | **49,364** | **12,652** | |

The component-size spectra (size separated by hyphens, value = number of D) are:

- m=0: 15:15264; 14-1:240.
- m=1: 14:14332; 13-1:1160; 12-1-1:12.
- m=2: 13:11496; 12-1:3640; 11-1-1:356; 10-3:8; 9-1-1-1-1:4.
- m=3: 12:8272; 11-1:4224; 10-1-1:1584; 9-3:528; 9-1-1-1:384; 7-3-1-1:288; 5-5-1-1:72; 8-1-1-1-1:72; 5-3-1-1-1-1:24; 7-1-1-1-1-1:24; 3-3-3-3:24; 3-3-3-1-1-1:8.

A standalone Python 3 integer-only checker, \`R762JV_FIVE_SINGLETON_GRAPH_COMPONENTS.py\`, regenerates these counts without any solver. This is complete for the stated component-graph statistic, **not** an exhaustive check of all 42-event Euler inventories.

## Consequence and new discriminating question

For m>=1, many five-singleton configurations have c>1; attempting to repair all parity defects solely with non-singleton flexible colors is therefore unsound. The missing c-1 quotient parity degrees must be supplied, when possible, by the selected singleton-color sides and the fixed forced-color parity; connectivity across those components must also be supplied. This does not imply that an Euler realization is impossible: disconnected flexible parity graphs are an **obstruction to that sufficient method**, not a counterexample to the target theorem.

The next research unit is to construct the exact GF(2) quotient reachable set from five singleton sides together with forced support parity (for each target multiplicity), and to couple this with component-connecting witnesses. It can decide whether a proposed 44→42 reduction remains feasible in the (8,8,4,0) histogram, without confusing method failure with true impossibility.

P000's native signed axes, ordered Cell paths, branch/time and BRC residual dynamics remain separate and unpromoted.
