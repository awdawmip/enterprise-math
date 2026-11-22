# R5 continuation: first seven contraction thresholds and return to the maximum at 44

Date: 2026-11-22. Same frozen R5 five-event scalar partition, prices 214..314, original S0,...,S4 and joint overlap constraints as in RESEARCH.md. Status: **AUTHOR_EXACT_PROOF / MODULAR_INTEGER_CERTIFICATE / NOT_REVIEWED**.

## Extended exact period classification

Let \`L=229746052653717600\`. Combining RESEARCH.md's complete finite prefix with this additional exact witness calculation yields

\`\`\`
M_m(O_m(N)) = L       for 1 <= m <= 36
M_m(O_m(N)) = L / 43  for 37 <= m <= 43
M_44(O_44(N)) = L
\`\`\`

This locates not merely the first contraction at 37, but the entire first block of **seven consecutive contracting thresholds** and the first return to the maximum at 44.

## Proof

The global denominator pole-count upper bound is L for all m. At a primitive 43rd root, the exact threshold generating function from RESEARCH.md has the form \`B(t)/(1-t^43)\` with degree B=35. Consequently the order-43 numerator vanishes **in characteristic zero** for thresholds 37,38,39,40,41,42,43, and is nonzero at threshold 44 (same phase as threshold 1). No other denominator order with pole multiplicity >=3 is divisible by 43, giving period upper bound L/43 for thresholds 37..43.

Using the exact finite-field jet evaluator from VERIFY_MODULAR.py, we computed all **14 primitive-root witness orders** for each of m=38,...,44, retaining three core events' overlapping capacity counters and disjoint S3/S4 factors. For every m=38,...,43, all 13 orders distinct from 43 have a nonzero zero-jet or a nonzero first jet at their certified exact-order finite-field roots, as required for poles of order >=3. These orders have lcm L/43, giving a matching lower bound. At m=44, the root-43 zero-jet also becomes nonzero; all 14 orders contribute and their lcm is L. The exact m37 first case was checked in RESEARCH.md.

A finite-field nonzero jet proves a complex nonzero jet via divisibility by \`Phi_d\` or \`Phi_d^2\` over integers (as detailed in RESEARCH.md); an accidentally zero finite-field evaluation is never used to prove complex cancellation.

## Selected exact residue data at primitive order 43

Field prime P=10321; exact-order root w=3215; denominator has triple zero. Values are exact modulo P:

| Threshold m | R_m(w) | (q d/dq)R_m(w) | Order-43 quadratic contribution |
|---:|---:|---:|---|
| 37 | 0 | 6843 | Absent by exact cyclotomic proof |
| 38 | 0 | 3004 | Absent by exact cyclotomic proof |
| 39 | 0 | 7546 | Absent by exact cyclotomic proof |
| 40 | 0 | 4671 | Absent by exact cyclotomic proof |
| 41 | 0 | 8856 | Absent by exact cyclotomic proof |
| 42 | 0 | 1044 | Absent by exact cyclotomic proof |
| 43 | 0 | 787 | Absent by exact cyclotomic proof |
| 44 | 10275 | 3626 | Present, nonzero zero-jet |

The seventh root-zero threshold m=43 and the return m=44 agree with the threshold generating-function's exact 43-phase recurrence. The values of other 13 orders were calculated for each threshold; the source file VERIFY_RECOVERY.py reproduces their complete 8×14 jet table and verifies the precise 13/14 and 14/14 patterns.

## Reproduce and boundaries

Run \`python3 VERIFY_RECOVERY.py\` from the same directory as \`VERIFY_MODULAR.py\`; it writes \`R5_O1_M37_44_RECOVERY.json\` after all exact assertions pass. The original complete 1..37 proof remains untouched, and this extension tests additional thresholds with the same frozen inputs and witness method. The output file is generated locally when the verifier is run; its publication is not asserted by this note.

The model is a frozen R5 scalar observer, not a substitute for the P000 native X6 framework. Signed inclusion-exclusion and joint event provenance are preserved. This is an author-side exact algebraic argument with finite computational certificates; independent mathematical review remains NOT_REVIEWED. No formal task execution or Result is claimed.

Next: advance to thresholds 45..49 to test whether every surviving root remains nonzero after the 43-component returns, and derive root-specific rational threshold generating functions for 29, 32 and 37 to obtain a true all-threshold classification.
