# Anchored coefficient-envelope obstruction

`ANCHORED_ENVELOPE_OBSTRUCTION.md` proves the uniform approximation
`|P_d(n)-B_d(n)/n| <= d^2/(8n^2)` for `n,d>=2`, constructs coherent bounded
coefficients at a fixed anchor, and derives the lower power
`H^5 A^(-2 theta-3)`.

The coefficients of the obstruction are auxiliary `0/1` coefficients. The
result limits a uniform coefficient-envelope-only estimate; it is not a lower
bound for the actual matched road or for every possible arithmetic method.

Run from the bundle root:

```bash
python3 rh_joint_anchor/certify_anchor_obstruction.py
```

The only executable dependency is the unchanged
`rh_correlation_rational/certify_matched_nodes.py`. The output is
`anchor_obstruction_certificate.json`. It retains directed 60-place integer
intervals, the selected integer ranges, both finite constructions, and exact
rational lower bounds. Universal statements are proved in the mathematical
note; finite checks do not replace those proofs.

The first construction, `(A,H)=(16384,1024)`, also directly evaluates all six
points of its coherent window. The second, `(2^24,2^20)`, verifies all 49,343
selected divisors and the exact lower-bound construction without unnecessarily
forming 16 million harmonic terms. It is the first member of the explicitly
proved `H=A^(5/6)` family.

The root author wrote the proof; the variance branch checked its counting and
coherent-window constants, and the certificate branch checked the uniform
approximation argument. These are same-author collaborative checks, not an
independent Project Review or proof-assistant verification.
