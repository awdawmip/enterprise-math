# R063 Stage 4 — Sector Process Atlas

Status: `COMPLETE / EXACT FINITE ATLAS`

Researcher-ID: `EM-R063S4-978726`

## Frozen local carrier

For each sector `S_ab`, the Stage 3 process fiber is the four-state additive label torsor

`C4={0,1,2,3}`

with tensor label law

`x box y = x+y mod 4`.

The process label is not a native axis identity. Native axis tags remain `E1,E2,E3`.

The three chart objects are:

- `Proc_12` over `S12=(E1,E2)`;
- `Proc_23` over `S23=(E2,E3)`;
- `Proc_31` over `S31=(E3,E1)`.

## Orientation parameterization

Let `epsilon_12,epsilon_23,epsilon_31 in {0,1}`.

`epsilon=0` means the listed cyclic sector order maps to `(0,1)`.

`epsilon=1` means the opposite local orientation maps the listed pair to `(1,0)`.

Hence:

`S12: phase(E1)=epsilon_12, phase(E2)=1-epsilon_12`;

`S23: phase(E2)=epsilon_23, phase(E3)=1-epsilon_23`;

`S31: phase(E3)=epsilon_31, phase(E1)=1-epsilon_31`.

All `2^3=8` assignments are admissible local conventions and are classified in the transition certificate.

## Local Stage 3 table

In any chart, if `A0` is the native axis with local phase `0` and `A1` the native axis with phase `1`, then:

- `A0 box A0 -> +A0` (`0+0=0`);
- `A0 box A1 -> +A1` (`0+1=1`);
- `A1 box A0 -> +A1` (`1+0=1`);
- `A1 box A1 -> -A0` (`1+1=2`).

The other two states are the signed/unit closure required by Stage 3.

## Overlaps

The native overlaps are:

- `S12 cap S23 = E2-axis`;
- `S23 cap S31 = E3-axis`;
- `S31 cap S12 = E1-axis`.

On an overlap the **native axis tag is identical**, while its local `C4` phase may differ.

This distinction is load-bearing for Stage 4.

## Semantic status

The three-sector atlas and native axis tags are part of the current N0 three-positive-axis foundation. The `C4` process fibers and all process transitions remain `N1_DERIVED_OPERATIONAL`.

No negative native axis is introduced: phases `2,3` are process states, not native spatial directions.
