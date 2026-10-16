# C104 — Exact transverse BRC zero path connecting C96 and C103

Date: 2026-10-16. Status: **AUTHOR_EXACT_DOUBLE_ROUTE_VERIFIED; NOT_ADMITTED; NO_NATIVE_CLAIM**.
Frozen global knowledge: `c10fc0f5a746dbb53c00ae32ca225605186afea5`.
Frozen Enterprise Math input: `acccfdb0f36ba22d36f497d8a05738077936fe74`.

## Model and scope

This is a theorem for the **classical finite positive-weight BRC auxiliary**, not the native six-dimensional Cell space nor its three-dimensional slice. There are 64 integer-graph vertices, 156 original integer edges, 142 face characters, 48 conditional core bits, 68 weak couplings. Keep the four *joint* port Fourier moments `K=(A,B,C,D)`, using chars `1,U,V,UV`, and determinant `F=AD-BC`. Fourier readout signs are distinct from positive branch masses. Preserve full integer-edge provenance.

Fix the **same core fiber across both mechanisms**: zero-indexed `c_2=c_24=1` and the other 46 core bits 0. Set the six strong/anchor face couplings `H={8,11,44,61,89,118}` to `1/2`; let `G={90,106,107,112,115,119,122,123}`.

## Theorem C104.1: exact three-stage continuous, transverse bridge

Let `t∈[0,1]`, `u∈[2/5,99/100]`, with all unspecified weak couplings initially 0:

* Stage 0, C96 → C94: `r_4=r_42=u`, `r_59=r_74=(1-t)/10`, all `G` off.
* Stage I, C94 → mixed: `r_4=r_42=u`, `r_59=r_74=0`, `r_90=t*u`, other seven `G` faces have `r=9*t/10`.
* Stage II, mixed → C103: `r_4=r_42=(1-t)*u`, `r_59=r_74=0`, `r_90=u`, other seven `G` faces have `r=9/10`.

At both stage junctions all four moment polynomials agree. Exact determinant endpoint identities:

```text
F_0(0,u)    = (255016*u^4 - 1076375*u^2 + 733150)/625
F_0(1,u)    = F_I(0,u) = 4*(5*u^2-17)*(20*u^2-17)
F_II(1,u)   = -151590037*(405*u-362)/200000000
```

Using a **complete 142-coefficient exact rational tensor-product Bernstein certificate** (30, 77, and 35 coefficients on stages 0, I, II), for every `t∈[0,1]` at all three stages,

```text
F(t,2/5) > 100,
F(t,99/100) < -29,
partial_u F(t,u) < -281 throughout [0,1]×[2/5,99/100].
```

Hence each stage has a unique simple zero `u(t)∈(2/5,99/100)`; implicit-function continuity and exactly matching junction values give one concatenated **continuous transverse determinant-zero path** connecting the C96 and C103 mechanisms **in a single 48-bit core fiber**. This is not a theorem on global connectedness of the entire zero set.

## Theorem C104.2: explicit path in strict interior of all 68 weak parameters

Set `epsilon=10^-24` and apply the same affine regularization to every weak face:
`r_f^epsilon=(1-epsilon)*r_f+epsilon`.
Every original path coupling lies in `[0,99/100]`, so all 68 regularized couplings lie in `(0,1)`.

Each baseline positive state has at most 12 nontrivial weak factors, hence baseline total positive mass `M≤64*(3/2)^6*2^12=2,985,984<3,000,000`. Ratios of regularized to baseline factors differ from 1 by at most `100 epsilon`. All four moment errors are `<7000 epsilon M`. There are at most three u-dependent weak face factors, yielding baseline derivative `≤300M` and derivative error `<3,000,000 epsilon M`. By product and determinant inequalities:

```text
|F_epsilon - F| < 42000 epsilon M^2 < 3.78e-7
|partial_u F_epsilon - partial_u F| < 33,000,000 epsilon M^2 < 0.000297
```

Thus the endpoint signs and strictly negative derivative persist, the three stage zero graphs match after the *same* regularization, and there is a **transverse continuous determinant-zero path entirely inside `(0,1)^68`**. This connects selected perturbed C96 and C103 families. It does not prove every sign-wall component is connected or a native X6 theorem.

## Computational evidence / verification

Primary `c104_analytic.py`: original 156-bit integer-edge GF(2) mask high-pivot quotient, exact Fraction polynomials, 142 rational Bernstein coefficients, 68D perturbation inequalities. Independent `c104_independent_walsh.py`: *regenerates the integer multiplication graph*, low-pivot elimination, 2048 exact conditional spin states, integer Walsh transform; compares **every coefficient of all four moment polynomials at every stage** against primary. The independently extracted portable packet's 14 SHA256 manifest entries all passed.

Verification receipts:

```text
C104_THREE_STAGE_142_EXACT_BERNSTEIN_SIGN_CHECKS_AND_68D_INTERIOR_PERTURBATION_PASS
C104_REBUILT_GRAPH_LOW_PIVOT_2048_SPIN_WALSH_ALL_THREE_STAGE_POLYNOMIAL_COEFFICIENTS_EXACT_PASS
C104_CLEAN_MANIFEST_EXACT_SHA256_PASS 14
```

Full author research package: `EM_C104_BRC_TWO_MECHANISM_CONNECTED_ZERO_PATH_PORTABLE.zip`,
SHA256 `00d57960587871b4fee71551f57756cdfa19c742feaa3e0de6c72f4dec437a7e`.
It contains primary and independent programs, exact coefficient certificates, proof, original necessary inherited input, and independent reproduction instructions. This GitHub Markdown is a digest, not a claim that ZIP bytes have been uploaded to Source.

**Method-use:** `REUSE_EXECUTED / COMPOSE_APPLIED` (joint positive-weight BRC Fourier observer, original edge provenance, exact conditional core, Bernstein certificate). **Review:** author-level two-route precision, **not** independent Driver mathematics acceptance, formal Result, or Working Truth.

## Remaining research question / owner-state boundary

Determine if the selected connected component contains all five C102 mixed-gauge inversion pairs, or find obstruction invariants; then formulate a typed relation-preserving lift to the native six-dimensional Cell model, explicitly including the third coordinate semantics in any three-dimensional slice.

Current canonical owner/CLAIM was not verified because the live task inventory returned `CONTROL_QUOTA`; no role-bound session, CLAIM, or Driver acceptance should be inferred from this author draft. Registration to the canonical research activity / formal Source Result remains a separate permission-dependent step.
