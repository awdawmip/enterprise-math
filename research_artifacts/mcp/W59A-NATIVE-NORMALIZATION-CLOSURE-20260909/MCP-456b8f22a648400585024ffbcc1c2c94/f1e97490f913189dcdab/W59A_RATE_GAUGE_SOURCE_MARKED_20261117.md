# W59A: source-marked event-order rate gauge and exact Dirichlet bridge

Date: 2026-11-17. Task: W59A-NATIVE-NORMALIZATION-CLOSURE-20260909, immutable publication TP2-93D3E62DA555016FCCAB. Scope: conditional path/operator theorem with finite exact tests; native TRIADIC_CLOSURE_E admissibility and independent mathematical review are not claimed.

## Old frontier and target

The pinned W59A posterior certificate already proves arbitrary-depth finite precision, uniform condition number below 2, and a 100-digit target-free interval. It also proves the finite-matrix normalization gap: replacing L_M by cL_M, c positive rational, leaves finite matrix structure intact but moves the first root by sqrt(c). This work addresses the previously unresolved *event-order* version, without repeating precision tests. P000's six signed native axes, source-preserving composite paths, native triadic closure and separately typed time remain unchanged.

## W59A-RATE-01 — exact marked event-order invariance

Let V be a finite source-marked state set, with an already declared legal directed transition set (possibly including a cemetery state). For transient u let q_uv >= 0 be finite jump rates, d_u=sum_{v!=u} q_uv > 0, q_uu=-d_u, and let Q be the resulting generator. Each jump may retain signed native-axis direction, complete source word, branch ID and a triad witness; mark law conditioned on previous events is assumed independent of c. Define Q_c=cQ for c>0.

**Theorem.** All c-models admit a coupling with exactly the same ordered marked jump word, every source/branch multiplicity and the same absorbing jump index. Their jump times differ by T_k^(c)=T_k^(1)/c. Hence any observer factoring only through ordered, fully source-marked events is c-independent; the positive rate gauge R_(>0) survives, or Q_(>0) under imposed rational-rate restriction.

**Proof.** At state u the destination probability in the c-model is cq_uv/(cd_u)=q_uv/d_u. Use the same destination choice, c-independent transition mark, and unit-rate exponential E at every step. The holding time is E/(cd_u), exactly 1/c times the base holding time. Induction through the stopping jump proves pathwise equality of source-marked words and the time-rescaling identity. Finite-state chains are non-explosive. QED.

The theorem is conditional on a legitimate source-labelled transition set. Defining rates does not demonstrate that a primitive P000 E-triad realizes these jumps. In particular, time as ordered relational change by itself supplies no calibrated holding-time observable that distinguishes c.

## W59A-RATE-02 — Dirichlet transfer and normalization

For M>=2, take an explicitly selected one-native-axis **observer** inside full X6, with transient sites 1,...,M-1. Give each signed nearest-neighbor jump conditional rate c and send jumps beyond the endpoints to a cemetery state. Keep their signed directions and any supplied source witness. The transient generator is Q_c=-cL_M, with L_M tridiagonal (diagonal 2, adjacent entries -1). The ordered direction/absorption history has a c-independent law by RATE-01.

For n=M-1,
  det(xI_n-cL_M)=c^n det((x/c)I_n-L_M).
Thus the finite eigenvalues scale by c; when the W59A spectral equation uses z=x^2/M^2, the first positive completion root scales by sqrt(c). This extends the previously recorded matrix rescaling obstruction to an entire marked event-history carrier.

Proof: every transient exit rate equals 2c including the exit-to-cemetery direction; therefore the killed generator equals -cL_M. The determinant relation follows by factoring c from each row; its eigenvalue/root implication is immediate. QED.

No information-reducing identification of source words, Port, branch multiplicity or triad witnesses is performed. The finite line is an observation embedded within six-axis native space, not a standalone native plane, nor a primitive two-force balance.

## Discriminating next unit

Read one actual Source-licensed native triad/axis event and prove a boundary/transfer map. Test whether global rate rescaling preserves every permitted *native temporal observer*, or whether the event law itself supplies a distinguished rate/cadence that breaks the gauge. A native time normalization must be derived from the legal events, not inserted as c=1 by convention. The open W59A target still requires the complete NativeCarrier, TransferBridge, NormalizationClassification, and CompletionBridge.

## Validation

A standard-library exact rational checker verifies 45 characteristic-polynomial scaling cases: M=2,...,10, c∈{1/2,3/5,1,2,7/3}, and the equal signed conditional jump probabilities. It is a finite corroboration; the all-c theorem follows from coupling.

Source pins: W59A taskbook blob 77eb6ba64a91b65711f0cba69c77f05d9b057c31; historical W59A posterior proof commit 5c78f2b1eaf71f4bc362d5dce0b375942bf8286d blob 1a1e4c212fbf22117a7370c2c4a9e67015250a04. Current Source P000 V5 and Heartbeat X6/time contract govern native typing.