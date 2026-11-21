# X6 Native Time — Unit252: mixed-resolution in-trace observer and an unavoidable C12-blind parity residual

Date: 2026-11-22. Task `RS-X6-NATIVE-TIME-DYNAMICS`; parent `PO-X6-UPPER-STRUCTURE-20260906`. Status: **AUTHOR-PROVED / EXACT-ORIGINAL-BRC-REPLAY-EXECUTED / UNREVIEWED / NOT_ADMITTED**.

## Exact sources and model scope

Frozen P000: `enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`. Original Unit245 36 signed BRC shortest histories: `f56840285cafeb9f5767ea91e903e1f53808186f:research_checks/X6_TIME_UNIT245_DIRECTED_CENTER_PORT_PAIR_RESULTS_20261121_2200.json`, blob `113d2102fe393bfd6f77bf7cca093b4cecf6796f`. Reuse Unit250 terminal-observer kernel and Unit251 already-existing trajectory prefixes. Preserve original signed six-axis primitive provenance, triad labels, occupancy and event order. The ring is the selected 3D-slice carrier, not the entire native spatial state; C24 is a separate hypothetical calibrated observer, not physical proof.

Assume stable additive centre-Port precision weights `alpha_k,beta_l in C24` for six even-indexed ingress/egress sites; known ring increments `g5=g10=3`, others zero. Original 36 labelled endpoint C24 observations reduce the modulo-gauge ambiguity to 18 laws. Unit250 identified the difference fibre by `t in C2` and `p,q in C3`, with `alpha_0=0` and `beta_k=-alpha_k`, and

`alpha_k mod 8 = 4 t (k mod 2), alpha_k mod 3 = (0,p,q)[k mod 3]`.

The two existing original Unit245 routes provide in-trace labelled A reads: route (ingress,egress)=(0,2), after primitive event 3 gives `X=alpha_0+beta_1=-alpha_1`; route (2,4), after event 7 gives `Y=alpha_1+beta_2=alpha_1-alpha_2`. Ring contributions before both samples equal zero.

## Theorem 252A — one C24 read and one C3 residue suffice, sharp five-bit output

The first observation `X mod 24` takes exactly six values across the 18 terminal-compatible laws, jointly encoding the order-2 parity `t` and ternary coordinate `p`. Once `X` is known, `Y mod 3=p-q` determines the remaining coordinate `q`. Consequently

```
18 terminal-equivalent laws -> (first C24 after event 3) 3 laws
                            -> (second C3 after event 7) 1 law.
```

There are exactly six possible first outputs and three conditional second outputs. Their fixed-width encodings require respectively 3 and 2 bits, **five bits in total**, meeting `ceil(log2(18))=5` for fixed-length identification of these classes. This is a *readout-encoding* bound, not a physical sensor-cost or time-cost bound. Two non-invasive samples remain necessary in the scalar-prefix observation class. The second need only be the mod-3 reduction of the independently calibrated labelled C24 register, not a full-resolution C24 reading.

## Theorem 252B — arbitrary C12-only intermediate samples cannot recover the C24 law

Consider the two distinct terminal-compatible laws `L0: alpha_k=beta_k=0` and `L1: alpha_k=beta_k=12(k mod 2) in C24`. For any signed BRC trajectory, any triad label and **every primitive-event prefix**, the precision difference is a sum of integers divisible by 12, hence is 0 in C12; ring-step contributions agree exactly. Thus no number or adaptive placement of reads that only retain `C24 -> C12` can distinguish the two laws, even given all original 36 **full-C24 terminal** observations, because those terminals also coincide in the original-source cases.

In particular the two Unit251 prefixes recorded only modulo 12 yield nine, not eighteen, joint classes. The 12-valued reduction loses the residual `12 mod24`, which is observable by the C24 first read (`X=12` versus `0`). This is an exact observer nonfactorization witness, not a change of spatial dimension or a new force law. **A finer-than-C12 channel at least once** is necessary for this normalized fibre; the displayed C24+C3 construction is sufficient. A full C24 reading is one concrete interface, not a general claim that every alternative sensor must implement C24.

## Original BRC source replay and evidence limits

An independent, embedded-source JavaScript checker traverses **all 36 immutable Unit245 shortest histories** (total **1,312 ordered signed native events**), checking labelled triad Cell exclusion, signed ring primitives, precisely allowed directed centre ports, `L_A=-12,L_B=+12` and exact original returns. For each of the 36 paths, it checks **every event prefix** for both triad labels under `L0,L1`, plus exact terminal C24 equality. It exhausts all 18 normalized original terminal kernel laws for the mixed-resolution inverse. Executed: **11590 integer assertions, zero failures**. This is exact historical *conditional* replay, not execution of the Source-qualified native physical experiment or the separate R063 benchmark.

## Discriminating native action and necessary provenance

Retain Unit251's original two full routes and full terminal C24 observations; if Source actually permits the signed intact-triad/Cell/Port/environment updates, obtain non-invasive, calibrated labelled-triad precision at event 3 on (0,2) **mod24** and event 7 on (2,4) **mod3**. Preserve the underlying raw readings if available, their units, resolution, Cell and event chronology, along with independent Port stability tests. A C12-only instrument is insufficient to distinguish the parity counterlaw. No physical sensor calibration, Source-signed Port transition or native benchmark occurred in this work; Native semantic PROGRESS remains unissued without own current winning CLAIM. Next meaningful action is actual source-qualified sensor/Port availability and original-route execution, not additional hypothetical Port algebra.

