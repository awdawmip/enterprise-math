# R673 extension｜V29 端口许可的最小对称闭包

Sources: frozen R462@18783e01e3646c72b7aab3b16d3f565e83e6446f; V29@b62110008321d9147212cb89f2627ff613c2550d:`research_notes/X6_NETWORK_EVENT_LEDGER_AND_CONTRAST_TRANSDUCER_V29_20260906.md`; R660@53353d25dac6cff8a2722df8ac235ebc8b7056f5, including its V28/V29/V30 source-alignment addendum. Author-side mathematical result; no independent Driver acceptance.

## Parameterized native V29 permission instance

In the original six-axis X6 spatial model, select adjacent Cells c0 and c1=c0+E1 relative to a chosen Cell anchor, without introducing a native two-dimensional plane. Give each four typed ports P={0,1,2,3}, declare the directed inter-Cell port license

`H_diag={(0,0),(1,1),(2,2),(3,3)}`.

V29 allows a TRANSFER only across a **declared network port relation**, and does not prescribe a universal H for every application. R660's fixed three TRANSFER occurrences use exactly (2,2),(3,3),(0,0), all included in H_diag. Thus, conditional on this explicit H_diag, both R660 event orders are licensed nonnegative V29 ledger histories. V29 proves Q conservation for every matched transfer; R660 supplies the strict V27/V17 slot derivation and relative three-cycle under its declared event sequence. There is still no native autonomous selector choosing the event order.

## Minimal symmetry-envelope theorem

**Theorem.** If a finite group K acts on the set P×P and W is a required license set, the unique smallest K-invariant relation H containing W is `H_min=⋃_{g∈K}gW`.

**Proof.** The orbit union is invariant and contains W. Every K-invariant superset of W contains each orbit gW, hence contains their union.

Apply this theorem with W={(0,0),(2,2),(3,3)}. Under simultaneous port relabeling by S4, `(a,b)↦(π(a),π(b))`, the smallest invariant H is exactly the four-pair diagonal H_diag. Under independent relabeling by S4×S4, `(a,b)↦(π(a),ρ(b))`, the smallest invariant H is all 16 elements of P×P. In both cases R660's three-port witness remains licensed, with distinct permitted future event languages.

`R673_PORT_VERIFY.py` independently exhausts all 24 simultaneous permutations and all 576 independent permutation pairs, confirming the 4/16 exact orbit closures.

The covariance proved here is for **the port permission relation** under the stated abstract label actions. Whether native X6 rotations act as either group on these typed ports is not established; full covariance of V27 selection, V17 slots, ledger updates and combined multi-Cell dynamics is a separate mathematical test.

Next: instantiate H_diag and rerun R660's two-Cell three-TRANSFER history in an explicit finite network with time-indexed events, then add an adjacent second loop and a declared, source-compatible event scheduler; test locality, signed Q conservation, S3 residual preservation and the actual native rotation action.
