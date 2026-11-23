# Native execution of the new five-channel families and fixed-fiber staircases

This note records actual execution on the same frozen native integer BRC source as the earlier research. Its purpose is to connect the new phase families to the existing state update and digit readout, while the global classification and sharp lower bounds are proved separately in the companion notes.

## State, update, and readout

For each root parameter a, initialize the typed integer register at

\[
x_0=a^2-1.
\]

The fixed positive singleton BRC effect is constructed through

```python
EffectHistogram.from_terms(1, [(1, Affine(((2,),), (1,)), 1)])
```

Its exact update is \(x\mapsto2x+1\), so after n updates

\[
x_n=a^2 2^n-1=F_n(a).
\]

Composition through the native `then` operation gives \(x\mapsto4x+3\) on the even subsequence. The calculation checks the native singleton coefficient and multiplicity, and evaluates actual arbitrary-precision integer states. For a prime q it calls

```python
euclidean_digits(x, (q,))
```

and checks the exact quotient-remainder identity and the divisibility predicate. Every observed divisor is also checked to be proper.

The fixed X6 anchor is unchanged. The integer register and its cofactor information remain part of the state. Prime readouts are observations, not additional axes or branches. The index n counts updates and is not interpreted as physical time.

## Four new representative executions

The root values and phase rows are taken from the proved CRT constructions in the companion observer and fiber notes. A row \((q,c)\) means \(q\mid F_{2u}(a)\) when \(u\equiv c\pmod{\operatorname{ord}_q4}\).

| Root example | Digits in a | Ordered new primes | Full period in n of the coverage predicate | Uncovered counts after 0, 1, ... selected primes |
|---|---:|---|---:|---|
| Least W/H1 root | 59 | 5, 13, 19, 37, 109 | 1260 | 216, 108, 39, 26, 13, 0 |
| Least W/H0 root | 59 | 5, 13, 37, 19, 109 | 1260 | 216, 108, 69, 46, 23, 0 |
| Least cost-five root in the fixed 25-channel fiber R0 | 65 | 5, 13, 37, 19, 73 | 1260 | 216, 108, 39, 26, 13, 0 |
| Least nested-optimal six-channel root in the fixed 29-channel fiber R1 | 76 | 5, 13, 19, 73, 433, 38737 | 2520 | 432, 216, 78, 52, 26, 13, 0 |

For all four executions, every old-prime readout equals the corresponding readout of the old root a*. Thus the old trajectory is fixed at every checked index, with all-future equality following directly from the fixed root congruence modulo each old prime. For R0, the five additional fixed coordinates are also checked; for R1, all nine additional fixed coordinates are checked.

The complete result is:

- 6,300 native integer updates;
- 187,740 native quotient-remainder readouts;
- 126,000 equalities with the old P trajectory;
- 28,980 additional equalities with the fixed R0 or R1 trajectory;
- the four exact residual-count rows displayed above, together with a private old-hole index for every selected channel.

The native calculation passed. `native_certificate.json` retains the exact roots, phases, counts, proper private witnesses, and final-state digests. `verify_native.py` reproduces it.

## Why the full-period check extends to all future indices

The inherited old-hole predicate has period 210 in n. A new prime's zero-readout predicate, when active, is one congruence class modulo \(\operatorname{ord}_q2\). The calculation checks that the least common multiple of 210 and the new zero periods is exactly 1260 or 2520, as appropriate. Hence one complete period decides these coverage predicates for every positive index.

The **full numerical old residue readouts** need not have period 210. Only their joint zero/nonzero hole predicate uses that smaller period. The exact old trajectory equality instead follows from \(a\equiv a_*\pmod p\) for every old p. This distinction prevents a coverage-period statement from being misread as a statement about the entire state.

## Reused native result and exact scope

The least root among all cost-five roots is unchanged from the preceding nested-only minimum. Its actual native membership execution is already published at commit `a2ae4d93398425e67dacbb4c99b7f3a6755e5771`, in `research_notes/portable_direct/riesel_observers_20261122/native/native_certificate.json`, field `minimal_root_native_check`. That execution is reused. The new all-prime classification supplies the stronger global minimum property within the fixed old root class.

The present executions do not independently prove that the 108 phase dictionaries are exhaustive. Exhaustiveness is established in `../global/proof.md`; exact root counting and the global minimum are established in `../observer/proof.md`. The sharp fixed-fiber staircases and the scope of each fiber minimum are established in `../fiber/proof.md`.

The compact R0 example has exact supplementary cost 5, and the compact R1 example has exact supplementary cost 6 by the proved lower bounds and displayed covers. Their unrestricted total cover costs are bounded above by 25 and 26. Equality of those total minima is not inferred from private witnesses belonging to a single chosen dictionary. The separate coprimalized all-cost construction proves exact total cost \(20+s\) for its own roots.

## Frozen source

The native source commit is `b1efc6c805661ed7b476e6e730107da6043176ee`. Its four source blobs are fixed by the earlier base certificate at commit `e61a43115cf9dcbd0b3d8a746a5ac8086b8ca8fe`, path `research_notes/portable_direct/riesel_mixed_20261119/certificate.json`, git blob `c1909a5e2e209b0f6bd5f613d0f758dde45caee9`.

The calculator checks these exact source blobs before execution. Current operational rules are taken from the current project entrance; the frozen native source is a scientific dependency, not a substitute for current rules. This is author execution within Researcher `EM-DIRECT-970E1C`, Activity `RA-D2EC212845B63844081F9A14`. No independent project Review or formal admission is asserted.
