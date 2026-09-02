# Precision-pi paper II Lean frontier

Researcher-ID: `EM-FREE-F6D046`
Branch: `formalization/precision-pi-paper-ii-k4`
Base: `240908889b8eaf546e2b0aae8e15a533c38e6dbd` (last known Lean-green precision-pi arithmetic/balance frontier)

This clean continuation branch replaces the unverified tail of PR #1100 after a self-audit found a proof-direction error in the first draft of the positive-accelerator module.

Current formalized scope:

- paired positive/negative Pell shells and their square-trace norm composition;
- tetrahedral four-slice/six-line incidence data;
- exact matching-kernel normal form;
- integral image iff even residual sum;
- nontrivial basic parity class and doubled-class image certificate;
- `A₂` matching-coordinate section and decomposition;
- `ZMod 2` residual invariant, invariant under zero-sum slice potentials;
- injectivity and uniqueness of the tetrahedral incidence potential;
- exact delta-coset classification by matching coordinate plus parity;
- actual quotient with descended matching and parity coordinates;
- positive transformed partial sums and strictly decreasing reciprocal approximants.

No `sorry`, `admit`, or custom axioms are used.

Required verification:

```text
lake build --wfail -KCI EnterpriseMath
```

The unrelated repository-wide reference-integrity failure involving the GEO8 task-publication envelope is outside this branch's mathematical scope and is not treated as a Lean failure.
