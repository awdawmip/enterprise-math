# EC49FQP — Exact Bellman certificate manifest (new 20; reused 41)

Date: 2026-11-16. Original scientific Source pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Scope: native BRC class 16943; 310 configurations, 141 full profiles, 144 terminal and 84 named-root observations.

This manifest indexes **20 newly computed exact unrestricted integer Bellman certificates**. The original JSON contents are retained in the accompanying complete archive; their SHA256 hashes follow (one certificate per root:terminal price and prior rational pair). The 41 earlier EC49FQO certificates are unchanged, revalidated against their original SHA256 manifest in PR #2559.

`certificates/r13_t8_lambda_0_1.json` — `488e2c534fe309559e7dac2bd53c32600d964983c583e9acd8b20a8fcf06a3fe`

`certificates/r13_t8_lambda_3410_58259.json` — `0d44a70f6c67c310950ce97f8bfc7c3c445c9f2d01b562e077babea131440103`

`certificates/r13_t8_lambda_620_3299.json` — `3f6235b0ce6eaa51b43b98e3828f21089f3881eda6be471814af57c258077e6a`

`certificates/r13_t8_lambda_1_1.json` — `cd7ca52808c590f8ce6a7a9c86719dfe239fceab9a3add4c0ed513d9dc842586`

`certificates/r15_t8_lambda_0_1.json` — `69e0157d4b1d9f08eab4c0358e79265e8ab6f694e97d038f1e4a4f39d18c1eee`

`certificates/r15_t8_lambda_930_19307.json` — `123ad65162d148d0b6f928fafc96af1f3729f8072c098e34788930e506654abb`

`certificates/r15_t8_lambda_620_3299.json` — `24d52b86754b329fd1aabca36ca03ed4a09ee913ddd2098578421d188d963856`

`certificates/r15_t8_lambda_1_1.json` — `2375587c60853f9aa7df0a4ad8eda306f86149606f0175aaceb6bbb71e9d63bb`

`certificates/r17_t8_lambda_0_1.json` — `f68b91860ca2cd36b488f2d502f67ed055e75f0ed37409e7f42e24d68cb3a9ae`

`certificates/r17_t8_lambda_2170_57583.json` — `62945f0cbaf90ad5fa7aa684fecb25ece9303a09c5ef8d88e69df37fe0b46802`

`certificates/r17_t8_lambda_620_3299.json` — `4f88423c2bdd867995628f7699ee5081709c1f39d49efe23b88d35438130a4fd`

`certificates/r17_t8_lambda_1_1.json` — `30b554a69a25003833ec313ef4a1545c4a0fd2cd3e219d6a481caffe823e926c`

`certificates/r19_t8_lambda_0_1.json` — `24cf3b7b259e8a276171acfcac395e3df1419a941be9aa82d9665281fbdd8339`

`certificates/r19_t8_lambda_310_11449.json` — `1d832b7798fcd053cb5890127c4e55b3cc30a6c5b875aaa7d22135375209162a`

`certificates/r19_t8_lambda_620_3299.json` — `0b19ed6b6b950f30049275ef8a9e938b05224ed4c1e3eb61e7289f41e6d9fc45`

`certificates/r19_t8_lambda_1_1.json` — `622a27dc2d8de5e5913d4468c36b4c27a56f397f2231e7ac9440b51d6d60ec7b`

`certificates/r23_t8_lambda_0_1.json` — `bf8eeead14145656c0ea88f796b758d09b524529be40949c2ef16eeebf607f1a`

`certificates/r23_t8_lambda_310_56569.json` — `1107ba4858c228271729eae577d5c4364af6be37ebad8ac413956611689952c8`

`certificates/r23_t8_lambda_620_3299.json` — `62265e470865ed92f413e4b048a94c0a5e886a50e86c4cd917808b59f737df24`

`certificates/r23_t8_lambda_1_1.json` — `ef0a12f3c058c6703163398ed5ba902e3cff03ba41001151b193b83001f224f8`

The five complete all-prior sections have precise A/B crossover gamma values `3410/58259,930/19307,2170/57583,310/11449,310/56569`; the B/C crossover is `620/3299` at each price. The independently recomputed first-label sets are `{32,34}` (left), `{32,34,140,142}` (first tie), `{140,142}` (middle), `{16,23,140,142}` (second tie), `{16,23}` (right).

Verification: source SHA256 master `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e` and profile `a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f`. Independent exact weighted Bellman DP and full first-label tree replays passed all 20 cases in five batches; the 41 old JSON hashes passed. The rational area and radical-envelope argument are in the theorem document. Program source is `EC49FQP_INDEPENDENT_VERIFY_20_20261116.py`; full program, primary solver, logs and all JSON inputs are retained in the self-contained evidence package.

The verified 16-price grid is `1,7/6,4/3,3/2,13/8,7/4,15/8,2,17/8,9/4,19/8,5/2,8/3,17/6,23/8,3`. The exact potentially-unresolved area is `43591107646076555945/3699405948091520330244` out of total area 2. The exact proven maximum secant-envelope gap is `(25/3)/(sqrt(21319/3)+sqrt(42469/6))^2` terminal-price units.

Admission: **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED**. Repository branch/PR author publication is not a native formal Task Claim/Result or an Activity checkpoint. Frozen P000 and science retained. Research next: parametric Bellman separation or an exact full native competing tree inside one of the 15 residual narrow bands.
