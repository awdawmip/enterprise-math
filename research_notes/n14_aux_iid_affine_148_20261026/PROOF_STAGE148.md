# Stage148 — exact optimal affine segment for the external N14 ternary iid model

**Evidence level:** author exact finite computation-assisted proof, with two algorithms (backward rational dynamic programming and direct ordered-prefix integer-weight DFS). It has not undergone independent Research Driver review or native Result admission. This is an external positive branch model, not a theorem about P000, Heartbeat World, or the native X6 Cell dynamics.

## Statement and exact model

The independent symbols have distributions P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), and the stopping horizon N=14. Decisions may randomize depending on arbitrary *complete ordered histories*. Write eP=P(decide Q), eQ=Q(decide P), tP=E_P(tau), and tQ=E_Q(tau). Define V14(alpha) as the minimum of max(tP,tQ), with eP,eQ <= alpha.

The previously author-proved Stage147 terminal point, fixed by its immutable original proof, is

    alpha147 = 246608842944125560263775 / 708830536865346112978944
    V147 = 273961171711816388948994643 / 22682577179691075615326208

This paper establishes that, for **every real** 0 <= delta <= eta148,

    V14(alpha147 + delta) = V147 - slope148 * delta,

where

    eta148 = 38745474256605512970875 / 10933002200611098446587232256
    slope148 = 31429858952 / 41571575

and the exact right endpoint is

    alpha148 = 6124245463802993075 / 17602807464179269632
    V148 = 35426720708566621357 / 2933801244029878272.

The affine Bellman support is **strictly below** V14(alpha) for every alpha > alpha148 (right-end sharpness).

## Exact Bellman certificate and universal lower bound

At the count state s=(n,a,b), the likelihood ratio for each ordered prefix is r(s)=Q(prefix)/P(prefix)=2^(a+b)/3^a. Select the positive multipliers

    K=15834013488/41571575
    L=15595845464/41571575
    K+L=31429858952/41571575.

For n<14 define the backward rational recurrence

    H(s) = min { K*r(s) [decide P], L [decide Q],
                  1+sum_i P_i*H(next_i(s)) [continue] }.

At n=14 omit continue. All 680 states s with 0<=a+b<=n<=14 are explicitly covered by the exact Fraction checker. It returns

    H(root)=16707106935800437885154981/60728334498563346137088,
    exactly two ties: T=(7,1,2), actions Q/C;
                      B=(11,0,1), actions Q/C;
    1238 strictly positive non-minimal gaps;
    minimum positive gap 2016649859/121222712700;
    zero negative gaps.

Because the iid conditional suffix and prefix likelihood ratio depend only on (n,a,b), the same recurrence lower-bounds *every* policy on full ordered histories; this sufficiency is restricted to these declared model observables. In particular, for every arbitrary ordered-history randomized policy,

    H(root) <= tP + L*eP + K*eQ
            <= max(tP,tQ) + (K+L)*alpha

whenever both errors <= alpha. Therefore

    V14(alpha) >= H(root)-(K+L)*alpha.                          (1)

## Branch provenance, disjoint ties, and exact four-observer map

At all strict states choose the unique Bellman minimizer. In particular the former Stage147 tied state W=(10,4,1) is strictly P-stop at the new dual parameters. At T choose Q-stop with probability v and continue with probability 1-v. At B choose Q-stop with probability b and continue otherwise. All other history decisions are the fixed strict minimizers.

T has second-symbol count 2 at depth 7, while B has second-symbol count 1 at depth 11. Along every ordered history a symbol count never decreases. T therefore cannot precede B; B cannot precede T because it is deeper. The genuine ordered-path cones are disjoint, so the observer is affine in v and b, with no mixed term.

A direct literal-prefix DFS retaining separate P and Q integer weights gives exact first-hit inventories:

    T: 70 ordered words; P-mass=21875/2985984; Q-mass=21875/1119744.
    B: 11 ordered words; P-mass=107421875/1451188224; Q-mass=107421875/725594112.

Let M=(eP,eQ,tP,tQ). Independently computed backward Fraction recurrence and integer-weight literal-prefix DFS on all four deterministic coin corners agree componentwise. Their affine decomposition is

    M(v,b) = M00 + v*dT + b*dB,

with

    M00=(
      1212223114611847135/3505953353861431296,
      74844877872805/213986410758144,
      5336636226821624017/438244169232678912,
      631560277329211/53496602689536
    )
    dT=(
       1191246875/9393093476352,
      -1878471875/20061226008576,
      -377661353125/31701690482688,
      -44855715625/1671768834048
    )
    dB=(
       4619140625/2229025112064,
      -751953125/417942208512,
      -25673828125/278628139008,
      -17939453125/104485552128
    ).

The exact cross-difference M(1,1)-M(1,0)-M(0,1)+M(0,0) is (0,0,0,0). The direct DFS visits, at (v,b)=(0,0),(1,0),(0,1),(1,1), respectively 583684, 567934, 583552, 567802 actual prefixes. The certificate records the complete corner tuples.

## Attainment throughout the real interval

The two errors are equal exactly when

    v(b) = 8421218673713991/463750360640000
           -(25449600000/1449219877)*b.                    (2)

The feasible balanced segment is

    b_star <= b <= 1,
    b_star=7957468313073991/8143872000000000.

At b=1, equation (2) gives v=39620953387713/66250051520000, precisely the Stage147 terminal T coin. At b=b_star, v=1 and B remains strictly inside its coin domain (0<b_star<1). Thus T Q-stop saturates before B. On this segment both coin probabilities are in [0,1], and the common error increases strictly when b decreases.

At b=1 the observer is exactly

    eP=eQ=alpha147,
    tP=V147,
    tP-tQ=386586105152287841810345/840095451099669467234304 >0.

At b=b_star the observer is exactly

    eP=eQ=alpha148,
    tP=V148,
    tP-tQ=36781979533221897065/79212633588806713344 >0.

The endpoint common error increment is exactly eta148; the tP decrement equals slope148*eta148. All four observations, errors, and time differences are affine along (2). It follows that eP=eQ, tP>tQ, feasible randomization, and exact complementary slackness hold for **every real** intermediate b. At the endpoints

    tP+L*eP+K*eQ=H(root)

exactly; affine interpolation makes the same equality true throughout. Combined with the universal bound (1), this proves the asserted equality for every real alpha in the stated closed interval.

## Sharpness of the right endpoint

The finite full ordered-prefix behavioral policy space is compact; randomized actions at finitely many histories induce a compact feasible observer image, so the minimum is attained.

Suppose some alpha>alpha148 attained the **same** lower support H(root)-(K+L)*alpha. Because K,L>0, both error constraints must be saturated, eP=eQ=alpha, and every reached ordered history must use a Bellman-minimizing action (otherwise the strict P-positive Bellman gap would make the inequality strict). Apart from T and B, the action is unique. At each of those count states, all reached ordered prefixes have the same fixed likelihood ratio and continuation future law; history-dependent tie coins may therefore be replaced by one effective P-mass-weighted tie coin without changing any of the four observables. Their cones are disjoint. Thus every policy saturating the support has an observer M(v,b), 0<=v,b<=1.

Equal errors enforce equation (2). Within its feasible portion (b_star<=b<=1), the common error is maximized at b=b_star and equals alpha148. This contradicts alpha>alpha148. The affine lower support is therefore strictly below the optimum at every alpha>alpha148. Sharpness is a support-line statement; later optimal value segments may still exist.

## Next exact dual candidate, provenance, and limits

When T is saturated Q-stop and B is interior, the tangent ray retaining B's Q/C tie yields the first positive closure at the new count state G=(11,7,3) (P/C). The fully recomputed next dual candidate is

    K149=100164600/266527
    L149=98815768/266527
    slope149=198980368/266527.

Exact 680-state Bellman check gives ties B Q/C and G P/C, 1238 positive alternatives, none negative, and H149(root)=2645762825003325844206337/9733658641089851031552. This is only a **dual candidate**, not a proved Stage149 primal interval. See NEXT_TASK_PACKET_149.md and SCAN_STAGE149.py.

Evidence source: this study consumes the verified author Stage147 proof/code/certificate at the Stage147 directory on Enterprise Math main@f6aca129043e9cb061fe85c758e9ce3f350b2e41; its previous global knowledge snapshot is not silently substituted for the present read. Current input snapshot: GLOBAL_KNOWLEDGE_V1 main@e152a10bf216fa48d7c6e66d252ad4a0ac8d2f89; Enterprise Math main@f6aca129043e9cb061fe85c758e9ce3f350b2e41. The published proof is an author-computation-assisted finite result, subject to native CLAIM, independent Driver review, and empirical/native mapping boundaries. The native control task listing returned CONTROL_QUOTA; session_start returned STATIC_READONLY_SCOPE_DENIED (operation_sent=false); the active native owner was not verified. This author source artifact is not a formal native Result or Working Truth. No transfer to P000 six-dimensional Cell geometry has been established.

**Tool reuse:** existing Stage147 rational Bellman plus literal ordered-branch DFS method applied; BRC positive rational mass, ordered branch and provenance preservation applied. The counts-only recursion is asserted sufficient only for the four declared iid observers under this model, never for the native X6 spatial/world state.
