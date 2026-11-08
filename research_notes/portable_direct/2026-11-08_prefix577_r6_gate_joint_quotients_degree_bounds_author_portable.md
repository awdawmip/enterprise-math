# PREFIX-577-R6 gate first-return exact quotient and denominator bounds (author portable, 2026-11-08)

**Frozen original science:** `f42f2906d77f24085c123f3ccfe9667d41caa96d`; original 96-port/576-tagged-edge evaluator Git blob `7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41`. **Status:** `AUTHOR_EXACT_INTEGER_AND_RATIONAL_PROVED / UNREVIEWED / NOT_ADMITTED`. Parent first-gate formula, ninth-root coboundary and 37-class passive quotient are reused (author notes `1ef152800b51d4a6b4e364078b1564764014474c`, `72d01473b004b9233ff2bd2bff12a457eb044825`), not claimed as new predecessor progress. No Source CLAIM, OPEN, native experiment, review or Result is claimed.

## New exact finite-state results

For an initial original port 9, the first later `K=1` edge has time `T` and total `(R5,R6)=(U,V)`. Set `C_pq(x,y)=sum_(original nongate actions p->q) x^r5 y^r6` and `g_p(x,y)=sum_(original marked actions p->9) x^r5 y^r6`, retaining **all 576 original labeled actions** and their multiplicities. The inherited joint return generating function is

`F(z,x,y) = E_9[z^T x^U y^V] = z e_9^T (6I-z C(x,y))^{-1} g(x,y)`.

**Declared passive observer:** all future six-equiprobable-action trajectories, the ordered `(R5,R6,K)` rewards, first-gate stopping, arbitrary finite horizons. Exact integer weighted partition refinement yields `96 -> 2 -> 7 -> 21 -> 33 -> 37 -> 37`; the existing 37-class quotient is verified, preserving all future passive observed-word distributions.

**Declared action-conditioned observer:** all fixed/external tag-conditioned action sequences among the six native actions, their ordered `(R5,R6,K)` readouts and first-gate stopping (no hidden-port-dependent policy). Exact per-tag partition refinement yields `96 -> 3 -> 11 -> 32 -> 49 -> 51 -> 51`. The new 51-class quotient preserves this stronger intervention language. The 37 passive quotient is not reused to infer action-intervention safety.

Let the passive 37-class nongate transition be `M(x,y) = M_00 + x M_10 + y M_01`, where each coefficient matrix is an **integer 37×37** matrix extracted from original `R5,R6`-labeled transitions. Over `Q`, the row module generated from `e_[9]^T` under every finite word in `M_00,M_10,M_01` has **exact dimension 34**. An explicit 34-vector exact-rational basis was computed and tested closed under all three matrices (102 closure matrix applications plus 102 independent post-checks). This induces a 34-dimensional rational linear realization of `F/z`, hence its *generic reduced rational denominator degree* over `Q(x,y)` is **at most 34**. This is a signed linear evaluation representation, not a 34-port native physical chain.

**Independent exact 96-port lower bound:** work modulo `p=1000000007` and specialize `(x,y)=(2,3)`. Set `s_n=e_9^T C(2,3)^n g(2,3)`. Original 96-port integer action propagation (without using the 37 quotient) gives

`det([s_(i+j)]_(0<=i,j<28)) = 595325725 (mod 1000000007) != 0.`

The degree-28 recurrence `s_n + sum_(j=1..28) c_j s_(n-j)=0` has `c_0=1, c_28=66525565` modulo `p`. Checking all **96 consecutive residuals** for `n=28,...,123` and applying Cayley–Hamilton to the original 96×96 transfer proves that recurrence for **every later n**. These exact facts establish reduced denominator degree **28** over `F_p` at the specialization. Since the original transfer has a polynomial numerator/denominator with nonzero constant denominator, the generic reduced denominator cannot have smaller degree than this specialization.

\[
\boxed{28\le\deg_z Q_{\rm reduced}(z,x,y)\le34\quad\text{over }\mathbf Q(x,y).}
\]

**The exact generic degree is an open next step.** Specialized degrees in the same modular computation: `(3,5):28`, `(7,11):28`, `(1,1):10` (agrees with inherited unmarked-return law), `(2,2):18`, `(1,2):24`, `(5,1):24`. These do not assert a generic-degree identity.

## Verifiability and information boundaries

Self-contained **ten-file author package** in this conversation, ZIP SHA-256 `5a7d18808920bf3d5f5d8d3a8d58fe89c56824e2cf2de029b5bdfd8f96d077d7`, with original frozen kernel evaluator, native edge snapshot, full 37/51 class maps, 34-dimensional exact basis, three checking programs, theorem and manifest. Exact certificate SHA-256 hashes:

- 37/51 passive/action quotient and modular specializations: `f63d2c0ccd863badb5010984bab0f4f86199f283b3bf7bd70963b10a7734cd47`.
- 34-dimensional rational invariant module: `ac01f69329c1500c9d8435837a47e0132f52f669e88ab266fe9f0fe6a65a31cd`.
- Independent original 96-state finite-field Hankel/recurrence: `654ecaf27e5a60b5521e1b7d35e3b8f5c80aa805d725bfd1ac9ecbb8f2b94a2a`.

All original branches, port identities, extra four six-axis spatial reward coordinates, original tags and exact integer information remain in the native evidence. The two quotients and 34-dimensional signed module may be used only for the declared observations and operations; new hidden-state controls or wider readouts require a separate equivalence proof.

**Source and continuity:** original native session-start request `h40-r11-self-researcher-session-start-20261108t1954-v1` succeeded with session `MCP-c66336a518d94c30b596df19011362b3`, activity `RA-E889C3B8461F5844B53CAF15`; the private session capability is unavailable, current own recovery returns `SESSION_CAPABILITY_REQUIRED`. A wrongly scoped read using short alias `D25` failed `unknown current immutable task publication`, and did not create a claim. Preserve D24 terminal Result/Review, D25 original-class H0/B0 and CM `NOT_RUN` frontier, and authentic UR V2 four-file 94687-byte SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76` recovery separately. No original bundle was regenerated.

**Next discriminating math action:** find and verify a field-`Q(x,y)` 28-dimensional state realization, or demonstrate a nonzero symbolic Hankel minor above order 28 to tighten the lower bound. Independent review and Source admission remain pending.