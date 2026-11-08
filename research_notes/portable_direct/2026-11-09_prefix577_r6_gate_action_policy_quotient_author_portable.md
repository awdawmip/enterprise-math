# BRC-X6 gate observer: exact action-control quotient (2026-11-09)

Status: **AUTHOR_PROVED / FINITE_EXACT_CERTIFICATE / UNREVIEWED / NOT_ADMITTED**.

Frozen scientific pin: `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Model: native 96 ports, 48 phases, six labeled transitions `(slot,newbit)`, nine frozen roots `0, ±e1,...,±e4`. Outputs `(R1,...,R6,K)`, where `K` is the gate indicator. No P000 changes, Source execution ownership, native CM experiment or formal Result are claimed.

## Typed observation and future operations

Four operation regimes are distinguished, each preserving its action-conditioned output distribution:

1. **Passive:** all six labels sampled uniformly, their identities hidden.
2. **New-bit control:** user fixes `newbit`; slot is uniform over 3 choices.
3. **Slot control:** user fixes `slot`; newbit is uniform over 2 choices.
4. **Full control:** both components of the action are fixed.

For output subset `O`, define the coarsest strong output-bisimulation partition as follows. Start with all 96 ports equivalent. Given partition `P_n`, the signature at port `p` is the vector, over each allowed control choice `u`, output value `v` and target block `C`, of the **integer number** of actions satisfying `control(a)=u, output_O(p,a)=v, next(p,a)∈C`. Group identical signatures to form `P_(n+1)`, until stable. This is exactly probabilistic strong bisimulation under the declared equal-choice policy; with all labels fixed it is deterministic Mealy equivalence. Stability proves preservation of arbitrary finite ordered-output laws and the allowed subsequent choices by induction. The universal starting partition proves the final stable partition is the coarsest of this specified kind. A strong-bisimulation count is not being equated with the minimal rank of an arbitrary linear/Hankel realization.

## Exact theorem

All counts below hold for **each of the nine frozen roots**:

| Observable | Passive | New-bit control | Slot control | Full control |
| --- | ---: | ---: | ---: | ---: |
| Gate `K` only | **24** | **24** | **51** | **51** |
| `(R5,R6,K)` | 37 | 37 | 51 | 51 |
| All six rewards at root 0 | 24 | 24 | 24 | 24 |
| All six rewards at each of eight nonzero frozen roots | 48 | 48 | 48 | 48 |
| Full `(R1,...,R6,K)` | **51** | **51** | **51** | **51** |

More strongly, for each of the eight tested observables `K`, `R5`, `R6`, `R5R6`, `R5R6K`, `R1..R4`, `R1..R6`, `R1..R6K`, the *full partitions* (not just their class counts) coincide for `passive = new-bit control` and for `slot control = full control`.

For every root there is one identical **51-class partition**:

```
Q(gate, slot-controlled)
 = Q(gate, fully-controlled)
 = Q(all-six-rewards-plus-gate, passive).
```

Its classes are exactly 45 original phase-bit pairs `[2j,2j+1]` for `j=0,...,47` except `j=3,14,15`, plus six singleton ports `6,7,28,29,30,31`. The six singleton ports agree as a set with the previously reported exceptional native starting ports in an author-level first-gate recurrence calculation; this is a connection of exact finite sets, not a new Source admission.

**Operational conclusion:** retaining the choice of transition slot, even while randomizing the new bit, is enough to distinguish all 51 gate-sensitive native state classes. Choosing the new bit without the slot does not refine the passive quotient for these declared observation families.

## Exact witness: output law versus intervention

Ports 0 and 24 are equivalent in the 24-class *passive-gate-only* quotient: all finite gate-word distributions coincide under uniform six-label sampling. But the following single controlled action word distinguishes their gate traces:

```
(slot,newbit): (0,0), (0,0), (0,1), (1,1)
port 0:       0 -> 20 -> 10 ->  5 -> 33, gate 0,0,0,0
port 24:     24 -> 44 -> 34 -> 29 ->  9, gate 0,0,0,1
```

Its length 4 is minimal for that pair, as certified by shortest-path search in the exact deterministic state-pair graph. Passive equality for all lengths follows from stable 24-class bisimulation, not from this example.

## Exact finite certificate and independent check

The native frozen kernel is `frozen_native_kernel_prefix577.py` (eight-kilobyte source from the pre-existing frozen author package). The independent `native_edge_snapshot.csv` (576 rows) was compared action-by-action to the kernel for source, target, gate and fifth/sixth rewards. The certificate then enumerated **9 roots × 4 regimes × 8 observation sets = 288** exact integer partition refinements, checked stable signatures and full pairwise equivalence of the asserted partitions.

Representative successive class counts, including the final unchanged iteration:

```
gate passive/newbit:       2, 3, 6, 15, 23, 24, 24
gate slot/full:            3, 7, 21, 41, 51, 51
R5R6K passive/newbit:      4, 13, 21, 33, 37, 37
R5R6K slot/full:           5, 16, 32, 49, 51, 51
all-seven root0 passive:   7, 36, 47, 51, 51
all-seven nonzero passive: 12, 51, 51
six-rewards root0:         6, 24, 24
six-rewards nonzero passive: 11, 48, 48
```

Code: `verify_gate_observer_action_boundary.py`; original kernel and edge CSV, complete JSON certificate, and the expanded proof are included in the **2026-11-09 portable author bundle** stored with the research conversation.

Certificate SHA-256: `eebe2407d75db09384fd8fc2ced8ef9be86ec3361d045a0bb9fc3f11e9bb5d8d`.

Portable ZIP SHA-256: `67ffc413cde81ca27dbcaf6750b3d420bde5490e53389f1d691f029825df705a`.

Independent ZIP extraction and execution of the verifier completed successfully and reproduced the certificate byte-for-byte. Computation uses integer action counts; the infinite-horizon conclusion follows from the finite stable partition and induction.

## Source / recovery boundary

Earlier D24/UR task Result and review were already officially completed. The author's D25 exact continuation request `h40-r11-d25-continuation-20261108t1512-v1` remained `QUEUED / SOURCE_LOCK_BUSY` in the 2026-11-09 bounded read. Own recovery requires a private session capability and did not grant CLAIM/open. The original four-file UR V2 bundle is still sought under exact length 94,687 bytes and SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`, and has not been substituted. This note is solely author evidence; future Source publication/review must use the actual authorized writer, original request reconciliation and real contribution history.

Next discriminating unit: compare these **strong quotient sizes** with minimal **linear predictive/Hankel dimensions** under the two partial-control regimes, maintaining action-conditioned output provenance. The original D25 H0/B0 and Frobenius scientific target remains the higher-priority unit when legitimately dispatched.
