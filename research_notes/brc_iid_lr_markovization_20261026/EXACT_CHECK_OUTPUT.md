# Exact verifier output and scope

Actual locally executed command, after the Python source version was written:

```text
python /mnt/data/VERIFY_BRC_IID_MARKOVIZATION_20261026.py
EXACT_MARKOVIZATION_PASS N=4 histories=121 states=35 eP,eQ,tP,tQ=87561719/286654464,25542503/35831808,3907765/1492992,985645/373248
STAGE_N14_LR_INJECTIVITY_PASS states=680 actions=1920
LR_ERASURE_COUNTEREXAMPLE_PASS errors=3/4,3/4 vs (r,1-r)
```

Source SHA-256 from the actual executed local file:
`356abb6d21a51f54e27003e08626bdf5437db054ab294d5e045c49fe99f082de`.

Source Git blob SHA (local `git hash-object`, to compare with connector immutable readback):
`3cb82963806e5ee6e77b72970267a13ac1fac486`.

Scope: exact `Fraction` arithmetic; one explicitly order-dependent randomized N=4 policy, its fiber-averaged count-state policy, a P-occupancy-flow LP check, an exact likelihood-ratio uniqueness enumeration at N14, and an algebraic horizon-one counterexample. Finite checker output does not prove universal Markovization. The separate handwritten proof in `PROOF_LR_MARKOVIZATION.md` proves that theorem under explicit iid/positive-law hypotheses. No independent Research Driver review, Lean formalization, native P000 bridge or remotely executed code is asserted.

BRC observer lease: four scalar observer values and hypothesis-tagged count occupation/action flows; not path identity, hidden correlations, or signed amplitudes.
