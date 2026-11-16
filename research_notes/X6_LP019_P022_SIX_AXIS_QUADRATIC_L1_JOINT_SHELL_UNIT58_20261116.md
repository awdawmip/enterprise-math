# X6 / LP019 / P022 — full native six-axis quadratic–L1 joint-shell transfer (unit 58)

Date: 2026-11-16. Role: TASK_RESEARCH. Parent: RS-X6-LEGACY-PLANE-RECONCILIATION, publication TP2-B4A441B23DA3159232C2. Author Researcher EM-X6-FB6990, existing SID MCP-082892eb480e45dea6d4b9fcc0491034. Status: AUTHOR-PROVED / AUTHOR-EXECUTED EXACT CHECK / UNREVIEWED / NOT_ADMITTED. No formal Result/Driver acceptance.

## Inputs and typed objective

Frozen scientific P000 V5 at enterprise-math commit 59538f585d037d09ef687b28715c4bc1a3f9fe03; signed unit-native-axis relative Cell displacement z in Z^6. This is the six-axis relative displacement model, NOT a claim that arbitrary six nonnegative numbers are valid final Cell addresses, nor an assertion that apparent composite diagonals are primitive paths.

Contemporary reference module: src/enterprise_math/p022_geodesic_multiplicity.py, Git blob 46373050168d2430b6cb3952aa763f3081284632, read at main de0040fb80bbaca2c2f30a990a579aaf3db89b60; exact tests tests/test_p022_geodesic_multiplicity.py, blob ef3da1a789186867c538b604da1b642bf6039591. The P022 simple-cubic sc_shell_total_geodesic_paths function aggregates L1 graph shells. The X6 frozen quadratic component readout uses G(z)=sum_i z_i^2. The former is not a G-shell aggregate without a typed transfer.

This unit directly extends unit 57's three-axis counterexample to the full six-axis native model and supplies the exact missing conditional distribution, rather than repeating the old raw R063 benchmark.

## Exact bivariate theorem

Let T(z)=sum_i |z_i|, G(z)=sum_i z_i^2, s(z)=number of nonzero signed components. For primitive signed-unit-axis adjacency, the number of natural shortest paths to z is

    N(z) = T(z)! / product_i |z_i|!.

For nonnegative integers g,t, the joint natural BRC mass is exactly

    M_d(g,t) = t! [x^t y^g] (1 + 2 sum_{a>=1} x^a y^(a*a)/a!)^d.

This is a formal-power-series identity, evaluated at finite g,t. Proof: each coordinate has magnitude a>=0, with 2 sign choices if a>0, one if a=0. Expanding d factors yields each signed magnitude vector with weight 1/product a!. Multiplying its x^t coefficient by t! counts the exact shuffles of the primitive axis steps. No signed paths are subtracted. A refinement tracks support s by multiplying every positive-a term by a support marker w.

The endpoint-count analogue drops the factorial denominators and t!:

    C_d(g,t) = [x^t y^g] (1 + 2 sum_{a>=1} x^a y^(a*a))^d.

The finite dynamic-programming recurrence appending absolute coordinate a is

    count' += (2 if a>0 else 1) * count
    mass'  += (2 if a>0 else 1) * mass * binom(t+a,a),

where state records (G,T,s). Independently, one can recursively enumerate signed endpoints with G=g and sum the exact multinomials.

General necessary support bounds for G=g>0: T>=ceil(sqrt(g)) by (sum |z_i|)^2>=G; T<=floor(sqrt(d*g)) by Cauchy; T<=g because a^2>=a for integer a>=0; and T==g (mod 2) because a^2==a (mod 2). These bounds are necessary, not sufficient to assert every parity-compatible T occurs.

## Complete G=25, six-axis certificate

| L1 primitive graph length T | Nonzero axes s | Signed endpoints | Natural BRC shortest-path mass |
|---:|---:|---:|---:|
| 5 | 1 | 12 | 12 |
| 7 | 2 | 120 | 4,200 |
| 9 | 4 | 2,880 | 10,886,400 |
| 11 | 5 | 960 | 399,168,000 |
| 11 | 6 | 3,840 | 2,128,896,000 |
| **All G=25** | | **7,812** | **2,538,954,612** |

The old R063 all-axis-pair support truncation (at most two nonzero axes) covers exactly 132 endpoints and 4,212 BRC paths. Its missed complement is 7,680 endpoints and 2,538,950,400 paths, agreeing exactly with the previously saved unit-46 r=5 omission certificate. Thus the exact independent new transfer identifies which L1 layers generate the old coverage defect: only T=5 and T=7 lie in the old support.

The real P022 L1-radius-5 shell has 2,364 endpoints and 106,452 BRC paths; its intersection with the G=25 shell has only 12 signed one-axis endpoints, mass 12. In particular, blindly inserting P022 radius=5 as a G=25 observable gives 106,452 instead of 2,538,954,612.

## Executed verification

Executed local Python script in ordinary and -O modes with identical JSON output and exit code 0. The program cross-checks two algorithmically independent approaches: a finite exact integer coefficient DP over (G,T,s) and a recursive enumeration of every signed G=25 six-axis endpoint, with multinomial calculation. It independently computes P022's published simple-cubic L1 shell formula using Stirling numbers, and checks the previous frozen R063 two-axis support result. All numerical comparisons passed. Local code SHA256 7f0924529387bbc9f8d530eab9e6d141b2af8bfc9698c894f33382a8d4b3d207; local result SHA256 24b2053158b740b1e65d96261b91d6ac12c5aeaf54c31c7e345b4c02aacd7c18. Exact executed code was Git-blob matched after publication.

Published immutable sources:
- Checker: research_checks/X6_P022_QUADRATIC_L1_JOINT_SHELL_UNIT58_20261116.py at a5daefffcc73d9fd13d65da1e0b7f0bc93826591, blob 63fc9b0e91b98748b961dc0a98af2572c6d3c6d5.
- Certificate JSON: research_checks/X6_P022_QUADRATIC_L1_JOINT_SHELL_UNIT58_RESULTS_20261116.json at eee3c0cd63d0f5b1da7b3cb0aa5030fb718a6c12, blob 5db1464d87def517b3a836acaae0b3b044b14841.

## Actual downstream source audit and remaining mother target

At exact main de0040fb80bbaca2c2f30a990a579aaf3db89b60, bounded direct reads covered the P022 geodesic producer/test and selected P022 Barlow, HCP, precision and growth modules/tests, material boundary shell, BRC histogram/control mass, and two P022 scripts. In this bounded set, direct sc_shell_total_geodesic_paths invocation was found in its appropriately L1-typed test; neither a genuine incorrect G-shell production caller nor an erroneous LP019 signed-natural cancellation was identified. GitHub code search returned incomplete_results=true with zero hits, so it is not evidence of complete repository-wide absence. Do not modify the correct production function.

Type disposition: per-endpoint P022 simple-cubic BRC is reusable; the exact six-axis quadratic G aggregate must sum across conditional (G,T,s) coefficients, without collapsing source axes, sign, natural mass or observer type. No native original R063 or Helly benchmark was repeated. The old R063 experiment already ran as unit 50, and independent Driver review is still required.

Next scientific/source action: find concrete production and historical import/call sites outside this bounded sample, especially exact LP011 wrong singleton argmax and LP019 positive-path signed cancellation; update/repair only a proven wrong actual caller. Preserve canonical native Source progress request receipts, unchanged P000 pins and Researcher ownership separately.
