# S23 n=3: new symmetric stochastic kernel with a strictly smaller all-real minimax upper bound

Date: 2026-11-07. Status: author-side exact constructive proof, independent mathematical review pending.
Scientific input: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34` (frozen, unchanged).
Continuation: PR #1777, predecessor exact fixed-kernel theorem `be33d3135b7cc32cadc76df744001595cb00b653`.
Research identity/CLAIM: GitHub authenticated account `awdawmip`; native control returned `BACKEND_IDENTITY_OR_VERSION_MISMATCH` with `operation_sent=false`; no new Researcher-ID, activity, active owner or formal CLAIM was established.

## Theorem (constructive improvement)

For all **real** `a,c in [1/2,7/8]`, let
`z=(1-a)c`, `p=(a,z,(1-a)(1-c))`, `b=(z,1-z)`.
The same unknown pair `(a,c)` governs all three conditionally independent trials. Let `delta_3` be the infimum over parameter-independent stochastic kernels from the 8 ordered binary inputs to the 27 ordered ternary outputs of their worst-case total-variation reconstruction error. Then

```text
5211/21952 <= delta_3 <= 593454349/2500000000 = 0.2373817396.
```

The upper bound is certified on the **entire continuous lawful parameter square**, not only a numeric grid. In comparison, the prior fixed kernel had the exact maximum `f(alpha)=0.237382038860788688...`. Even the prior kernel's rational witness `W=1899056310874087867/8000000000000000000` exceeds the new uniform upper bound by
`2394074087867/8000000000000000000 > 0`.
The certified minimax interval width is now
`154207/857500000000 = 0.0000001798332361516035...`.

## Explicit rational reconstruction kernel

Index ten ternary histograms by lexicographically sorted `H={(h0,h1,h2): h0+h1+h2=3}`, and put `m(h)=3!/(h0!h1!h2!)`. Write `M=100000000000` and use the following **4 x 10 integer matrix**, with each row summing exactly to M:

```text
k=0: [0,0,0,100000000000,0,0,0,0,0,0]
k=1: [0,0,0,0,0,0,1720234471,0,98279765529,0]
k=2: [148148148,444444444,11111111111,0,22222222222,12444444444,16550113883,31952904549,0,5126611199]
k=3: [0,0,0,0,0,0,5098696849,2445569945,32400594768,60055138438]
```

For each ordered binary input word having `k` non-z symbols, and ordered ternary output word of histogram `h`, assign transition probability `K[k,h]/(M*m(h))`. Input and output multiplicities are thus fully retained. All 8 input rows are stochastic. Both true and reconstructed output laws are symmetric under output permutation, so their full **27-output** total variation is exactly

```text
E_K(a,c) = sum_{h in H} max(0, R_h(a,c))
R_h = m(h)*a^h0*z^h1*((1-a)*(1-c))^h2
       - sum_{k=0}^3 binom(3,k)*z^(3-k)*(1-z)^k*K[k,h]/M.
```

Since the ten residuals sum to zero, this equals half of their absolute-value sum, as required.

## Rational all-real certificate

Map the lawful parameter square to `(u,v) in [0,1]^2` by `u=(a-1/2)/(3/8)`, `v=(c-1/2)/(3/8)`.
Each `R_h` is a tensor polynomial of bidegree at most (3,3).
Compute its 16 exact tensor-cubic Bernstein coefficients `beta[h,i,j]` using the exact inverse of the Bernstein evaluation matrix on nodes `u,v=0,1/3,2/3,1`.
All computations use unbounded integers and Python `Fraction`. The verifier also checks independent rational interior interpolation points.

On any rectangle obtained by midpoint subdivision, Bernstein weights `B_{i,3}(u)B_{j,3}(v)` are nonnegative and sum to one. Convexity of `x -> max(0,x)` gives, for every point of that rectangle,

```text
E_K <= max_{0<=i,j<=3} sum_{h in H} max(0, beta[h,i,j]).
```

The verifier starts with the whole square, alternately bisects u and v, obtains exact child controls through integer-scaled de Casteljau identities, and accepts a rectangle only after the **rational** hull is at most `T=593454349/2500000000`.

Actual executed result for `VERIFY.py`:

```text
PASS_S23_N3_NEW_SYMMETRIC_KERNEL_GLOBAL_BERNSTEIN
48 accepted rectangles; 47 bisections; maximum recursion depth 31
largest rational accepted hull =
875784039564913058004858555637/3689348814741910323200000000000
= 0.2373817395811024... < T = 0.2373817396.
```

The 48 rectangles partition the complete square, including the edges. Every mathematical comparison inside this certificate is exact rational arithmetic; decimal displays are diagnostics. The unchanged predecessor lower bound yields the theorem's displayed interval. The numeric kernel search was heuristic (SciPy cutting-plane linear programming on a finite parameter sample); it supplies a candidate, not the all-real proof.

## Scope, source, and next question

This theorem is for the frozen conditional-AV auxiliary observer (binary compression of ternary outputs with shared unknown parameters), and keeps all 27 ordered output labels. It uses the BRC-relevant provenance distinction through the ten histogram orbits and their exact multiplicities; no new native HEARTBEAT/BRC dynamics is asserted.

Next, construct a finite-support least-favorable prior and signed-TV dual certificate above `5211/21952`, or refine this symmetric kernel to a matched rational primal/dual value. The six-source / ten-label mother objective `R_beh(k,10)` additionally needs an admissible encoder/decoder/observer bridge.

Evidence: `VERIFY.py` (actual executed source Git blob `a1ed17e311ce65e775ac0ff1b1e4517e45266e8d`), `RUN_EVIDENCE.txt`, `NEXT_TASK.md`.
