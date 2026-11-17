# R5: an upstream J-kernel mixture kills the old support direction but has a sharp adaptive obstruction

**Author-side research, 2026-11-01 (Asia/Shanghai).** Mathematical status: `AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING`. The source is an auxiliary positive rational two-law stopping experiment, not a native X6 theorem.

## 1. Frozen inputs and precise scope

The immutable scientific input pins are GLOBAL_KNOWLEDGE_V1 `main@a01383f825ef9d43b4b754254303298c64041568` and Enterprise Math `main@86149263e38c22292c9def1e0f69092efa1be77e`. The immediately preceding verified author frontier is Enterprise Math commit `78372e8bdc479b3f914d0f3bfd9224b8fdf3313d`, `research_notes/brc_r5_uniform_global_no_go_20261101_t2237/{RESEARCH.md,VERIFY.py}`. Current normative inputs were separately read at GLOBAL_KNOWLEDGE_V1 `main@6c4f440a4f8fe9b518955b7b2da3d1427f672905` and Enterprise Math `main@d91def73651442bcabcb0b84a4fd2cd088a6a4c2`: global bootstrap/manual, project router, P000 projection/original blob, ACTIVE worldview, mathematical/code/temporal policy, BRC provenance constraints, `docs/RESEARCH_CONTINUATION_PROTOCOL.md#current-normative-context`, current `docs/PORTABLE_RESEARCH_PROTOCOL.md`, and `research_priorities/research_method.json`. Protected P000 and worldview were not modified. P000 is the project's research premise; this auxiliary model does not identify the four scalar observers with native X6 coordinates.

The mother question remains: construct a finite, strictly positive P/Q stopping experiment with equal convex hulls of FULL-history and seedless time/likelihood-ratio-policy four-observer images but unequal **actual real** images. Here the local question is whether a real, source-specific **upstream J transition** can eliminate the previous uniform signed obstruction, and whether that suffices for all-signed hull equality.

## 2. New one-parameter model and BRC typing

Retain positive labelled source masses under P/Q: `A1=A2=(1/8,1/8)`, `B=(1/4,1/8)`, `C=(1/2,5/8)`. Observe `O=(eP,eQ,TP,TQ)`, where `eP=Pr_P(final answer P)`, `eQ=Pr_Q(final answer Q)` and `T_P,T_Q` are expected integer stopping times. Decisions at a genuine shared `(time,likelihood ratio)` key are constrained to the same seedless LR behavioral probability; FULL may condition on the hidden source. Keys are `I=(1,1)`, `J=(2,2)`, `K=(3,8/5)`, `L=(4,12/5)`; C has its separate time-1 LR `4/5` decision. Every trajectory encounters each key at most once.

Keep predecessor `eta=1/2` and terminal response `z=3/4`. At J a continued A source takes the old A conditional natural kernel, with t3-Q-termination P/Q probabilities `(3/5,1/2)` and K arrival `(2/5,1/2)`; further P/Q natural branches are exactly `VERIFY.py::A_kernel_after_J`. A continued B source now takes the **same A kernel with a law-independent nature probability `lambda`**, or the predecessor B kernel with probability `1-lambda`. In the original B kernel the t4-L branch has conditional P/Q probabilities `(3/5,1/2)`, and the complementary t4 terminal branch has `(2/5,1/2)`; that terminal response is P with `1-z=1/4`, Q with `z=3/4` under either law. Thus all natural transition probabilities on the fixed graph are strictly positive for **real `0<lambda<1`**, and all terminal P/Q masses sum to exactly one. The boundary lambda=0 recovers the original model (the added K-source bit becomes dormant); lambda=1 is the reduced, source-independent J continuation topology after removing the zero-probability old B route.

The FULL behavioral vector has 12 independent parameters in `[0,1]`, ordered `(p1,p2,q1,q2,qB,r,k1,k2,kB,l1,l2,lB)`. The LR vector has five `(p,q,r,k,l)` with `p1=p2=p`, `q1=q2=qB=q`, `k1=k2=kB=k`, `l1=l2=lB=l`. The flow is a finite exact positive rational branch carrier with source labels and paths retained through all transitions. Its signed support functionals operate **after** the positive flow and are not interpreted as negative BRC branch masses. The only information reduction is the explicitly declared four-dimensional observation, for which we do not presume source redundancy.

## 3. The former fixed direction has an exact disappearance threshold

Let `M=(-211,10,-113,0)` and denote by `h_FULL(M,lambda)` / `h_LR(M,lambda)` the maximum of `M.O` over every real legal behavioral strategy. The new **all-real exact phase equations** for `0<=lambda<=1` are

```
h_FULL(M,lambda) = max[-238, -42061/160 + (4781/160)*lambda],
h_LR(M,lambda)   = max[-481/2, -42061/160 + (4781/160)*lambda].
```

Consequently the FULL/LR M gap is exactly

```
                  5/2                             if 0 <= lambda <= 3581/4781,
Delta_M(lambda) =  (3981 - 4781*lambda)/160       if 3581/4781 <= lambda <= 3981/4781,
                  0                               if 3981/4781 <= lambda <= 1.
```

These are exact extrema, not a search over finitely many objective directions. The constant FULL witness has bits `(0,0,0,0,1,1,0,0,0,0,0,0)` and observer `(11/40,55/64,267/160,187/128)`. The constant LR witness is `(p,q,r,k,l)=(0,1,1,0,0)`. The common affine winning observer is reached by FULL `(0,0,0,0,0,1,0,0,0,0,0,0)` and LR `(0,0,1,0,0)`. A fixed deterministic observer is affine in lambda because B uses one nature mixture exactly once. The exhaustive rational checker verifies the candidate envelope values at `lambda=0`, the respective exact kink, and `lambda=1`. Linearity on each of the two resulting intervals proves that **every** deterministic policy lies below the displayed piecewise-affine upper envelope throughout `[0,1]`. The explicit candidate strategies attain those bounds for all lambda. Behavioral multi-affinity then extends to all real policy probabilities.

The original fixed uniform M separation therefore **really disappears in a nonempty strictly-positive interval** `3981/4781 <= lambda <1`, despite source B still using a different J kernel from source A. This is the first exact upstream mechanism in this R5 line that erases the old M-direction support gap without first requiring all future kernels to be source-independent.

## 4. Adaptive signed direction still separates every non-lumpable interior point

For each `lambda in [0,1]`, define the explicitly parameter-dependent **signed observer direction**

```
n(lambda) = (200-680*lambda,
             -1280-1216*lambda,
             -760-200*lambda,
             1936+656*lambda).
```

**Theorem (complete all-real adaptive-support classification).** For every real `lambda in [0,1]`,

```
max_FULL  n(lambda).O(lambda) = 3146 + 370*lambda,
max_LR    n(lambda).O(lambda) = 3117 + 399*lambda.
```

Therefore the exact support gap is `29*(1-lambda)`, strictly positive for every `0<=lambda<1`. In particular FULL/LR four-observer convex hulls are **unequal throughout the entire strictly-positive interior**, including the interval where Delta_M is zero. The FULL maximizing deterministic bits are `(0,0,1,1,0,0,0,0,0,0,0,1)`; the LR maximizing bits `(0,0,0,0,1)`. Both are independent of lambda. From the dual l1/l-infinity inequality, this particular FULL witness is at distance

```
dist_infinity(W(lambda),conv(LR(lambda)))
   >= 29*(1-lambda) / ||n(lambda)||_1
   >= 29*(1-lambda) / 6528   > 0       (0<=lambda<1).
```

The denominator `||n(lambda)||_1` is exactly `4176+1392*lambda` for `lambda<=5/17`, and `3776+2752*lambda` for `lambda>=5/17`; its maximum on `[0,1]` is `6528`. This is a quantitative **scoped non-membership of convex hulls**, not a native X6 theorem.

**Proof and complete finite certificate.** For any fixed deterministic policy `b`, the exact observation is `O_b(lambda)=u_b+lambda*v_b`. Hence the difference between the claimed affine upper support bound `c+s*lambda` and `n(lambda).O_b(lambda)` is the quadratic `A*lambda^2+B*lambda+C`, with

```
C = c - n0.u_b,
B = s - n1.u_b - n0.v_b,
A = -n1.v_b,
n0 = (200,-1280,-760,1936), n1 = (-680,-1216,-200,656).
```

It has the degree-two Bernstein representation

```
C*(1-lambda)^2 + 2*(C+B/2)*lambda*(1-lambda)
                        + (C+B+A)*lambda^2.
```

The standalone `VERIFY.py` **exhaustively enumerates** all `2^12=4096` FULL deterministic strategies and all `2^5=32` LR deterministic strategies and confirms that each of the three Bernstein coefficients is a **nonnegative exact rational** for each policy, using `(c,s)=(3146,370)` and `(3117,399)` respectively. The minimum of each coefficient over each entire class is exactly zero. Since the Bernstein basis is nonnegative over the full real interval `[0,1]`, the claimed inequalities hold for all real lambda. For the two displayed witnesses, the quadratic coefficient is exactly zero and the value equals its class bound identically. This proves the exact extrema. Finally, because a trajectory encounters any decision parameter at most once, each real behavioral observer is multi-affine in its policy parameters, hence is a convex combination of all deterministic observations. A signed linear support functional has the same extrema over the behavioral cube and deterministic vectors. QED.

## 5. Endpoint lambda=1: actual image equality by predictive Markovization

At lambda=1, B's continued J kernel is exactly the A kernel, and the conditional K and L natural laws are identical across every source reaching each shared key. Every incoming source mass at a key `(t,r)` obeys `dP=r*dQ`. For a FULL history-dependent strategy, aggregate Q action mass `f_(key,action)` over the source/history fiber and set a seedless LR action probability `f_(key,action)/f_(key,total)`, arbitrarily if total mass is zero. The corresponding P action mass is automatically `r*f_(key,action)`. Induction through I, J, K, L and the source-independent outgoing conditional kernels then reproduces every P/Q terminal answer and time flow. Thus **the actual four-observer images coincide at lambda=1** (and therefore their convex hulls coincide), not merely the tested direction. This equality uses the source-independent kernel and time/LR flow structure; it does not claim that source identity is globally redundant under other observers.

## 6. Exact verification, permissions, unresolved target

`VERIFY.py` is a Python 3 standard-library `fractions.Fraction` script; `EXACT_OUTPUT.txt` is its actual captured output. It checks normalization on every evaluated terminal flow, **4096+32 exact Bernstein certificates**, adaptive extremal witness identities and the two old-M piecewise envelope certificates, with 20,671 exact observer-flow evaluations in this run. The finite exhaustive certificates imply the all-real statements via the proven interpolation and multi-affinity; no floating-point samples are used for the theorem. The independent design/exploration heuristics using floating ConvexHull were not part of the final verification trust basis.

The live native service `em_status` (v0.6.11) returned `research_authority_granted=false`, `executor_binding_configured=false`. A bounded `em_control_tasks` owner check returned `CONTROL_QUOTA` and disclosed no verified current owner. Accordingly no CLAIM, Result, independent Driver review, mathematical admission, or Foundation promotion is asserted. The activity/state-machine registration remains pending a genuine native identity or authorized project flow. The GitHub record is an **author-side portable research artifact only**.

**Next smallest question:** Change the upstream topology beyond a single source-B law-independent J-kernel mixture. Seek a strictly-positive, genuinely source-sensitive candidate with *complete* all-signed FULL/LR four-observer convex-hull equality; use adaptive separating directions/facet interpolation as a quick rejection certificate. For one that passes, certify actual real LR-image nonmembership (or prove image equality). The R5 mother counterexample remains open.
