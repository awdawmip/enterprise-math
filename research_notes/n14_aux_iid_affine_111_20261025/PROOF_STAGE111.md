# Stage111: exact real affine optimality interval (external ternary iid N=14)

**Evidence level:** AUTHOR_EXACT_COMPUTATIONAL_PROOF, independent-author-code crosscheck, **NOT** native Result/CLAIM or independent Research Driver review. This is an external finite iid model, not P000 native six-dimensional Cell mathematics.

**Fixed source reads:** GLOBAL_KNOWLEDGE_V1 `d3e40172c14682a8e844944968e921446949d7dc`, Enterprise Math `b0b7ff022e02b76d53c75401de46ef596df0a120`, P000 original Git blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`. Exact predecessor: `research_notes/n14_aux_iid_affine_110_20261025/PROOF_STAGE110.md` and `certificate110.json` in that EM snapshot.

## Model and theorem

The complete ordered history tree of 0 through 14 observations has ternary iid laws
`P=(1/8,1/24,5/6)`, `Q=(1/12,1/12,5/6)`. Strategies may randomize at any history, must stop by 14, and choose P or Q. Write `eP=P(decide Q)`, `eQ=Q(decide P)`, `tP=E_P(tau)`, `tQ=E_Q(tau)`. Define `V14(alpha)=inf_{eP,eQ<=alpha} max(tP,tQ)`.

Let
`alpha110=13084102571183753507/37682150988866125824`,
`V110=1934432098641265410385/150728603955464503296`.
**Claim (two author exact checks):** For *every real* `0<=delta<=eta111`, where
`eta111=609395080925/43613600681558016`,
the exact optimal value is
`V14(alpha110+delta)=V110-Gamma111*delta` with
`Gamma111=91322550865947/48751606474`.
The new endpoint is
`alpha111=13084629088533672707/37682150988866125824`,
`V111=1930486964443856499985/150728603955464503296`.
The **same supporting line** is unattainable for any greater alpha; no claim is made that V14 itself ceases there.

## Bellman dual lower bound

For count state `z=(n,a,b)`, the conditional likelihood ratio is `R(z)=Q/P=2^(a+b)/3^a`. For `K,L>0`, the exact 680-state induction is
`H(z)=min{K*R(z),L,1+sum_j P_j H(child_j)}`, with no continuation at n=14.
For *every ordered-history randomized policy*,
`H(root)<=tP+L*eP+K*eQ<=max(tP,tQ)+(K+L)*alpha`.
At
`K111=328788597439629/341261245318`,
`L111=155234629311000/170630622659`,
the root is
`H(root)=442831288641869703211215721001/667659602436144401831952384
=V110+(K111+L111)*alpha110`.

Exhaustive exact comparison of 1240 nonchosen actions on 680 states: 1238 strictly positive gaps, 2 tied alternatives, 0 negative. The smallest positive gap is `67830632993/3071351207862`. **Only** these two states admit multiple minimizing actions: `A=(10,3,0)` immediate P vs continue, `F=(4,0,2)` immediate Q vs continue. The old `E=(13,6,4)` is now uniquely Q-stop. Every other minimizing action matches the Stage110 right-end policy.

## BRC path carrier; key structural correction

A potential predecessor question was whether F can be an ancestor of A. It cannot: `b_F=2>b_A=0`, while the symbol-2 count b never decreases. A cannot be an ancestor of F either, because `n_A=10>n_F=4`. Hence no history encounters both critical states; the ordered-path cones are **disjoint**, and all root moments depend *affinely* on the two randomization parameters with no u*w term. This uses the positive rational first-hit branch mass (BRC method, preserving ordered provenance); the Bellman quotient by counts is sufficient only by iid likelihood and continuation factorization.

With forced continuation at A,F, exact first hits are:
- A: 120 literal ordered prefixes; P-mass `390625/5971968`; Q-mass `390625/20155392`.
- F: 6 literal ordered prefixes; P-mass `25/3456`; Q-mass `25/864`.

Conditional forced-continuation suffix `(Perror,Qerror,additional Ptime,additional Qtime,ordered terminal suffix count)`:
- A: `(635/165888,10201/10368,7711/6912,1069/864,21)`.
- F: `(97026796793/97844723712,23538461/15479341056,21341487367/12230590464,1826080831/1289945088,1555)`.

## Real-family primal certificate

Let u be probability of P-stop at A, w probability of Q-stop at F. Stage110 right endpoint: `u0=159869038712303/211315200000000`, w=0. The exact error sensitivities are
`x=d eP/du=-248046875/990677827584`,
`y=d eQ/du=65234375/208971104256`,
`zP=d eP/dw=20448172975/338151365148672`,
`zQ=d eQ/dw=-588461525/13374150672384`.

The equation eP=eQ uniquely requires
`u(w)=u0+((zP-zQ)/(y-x))*w=u0+(16351264081/88048000000)*w`.
For `0<=w<=1`, `0<u(w)<1`, with `u(1)=199112072506703/211315200000000`. The errors satisfy `eP=eQ=alpha110+eta111*w`. Full exact root moment recurrences give
`tP=V110-Gamma111*eta111*w>tQ`.
At w=1,
`tQ=114606239754171547805/9420537747216531456` and
`tP-tQ=96787128377111735105/150728603955464503296>0`.
Two exact programs agreed at w=0,1 (the state checker also at 1/2). Since cones are disjoint, root moments are affine, so these identities hold at **every real w**, not just sampled rational values. Each used action minimizes the K111,L111 Bellman objective; equality with the global lower bound proves the theorem against all ordered-history policies.

## Sharpness

Finite randomized history-tree policies have a compact realization-measure feasible set. Equality beyond alpha111 in the *same* dual line would force `eP=eQ=alpha` (both multipliers positive) and Bellman-minimizing actions wherever positive history mass occurs. Only A/F tie. Within any fixed count state, Q/P is constant across all ordered prefixes; averaging potentially history-dependent random decisions by the P first-hit weights therefore gives the **same effective probability under Q**. Nonintersecting A/F cones make the two-error affine equations necessary even for arbitrary history policies. They force `alpha=alpha110+eta111*w<=alpha111` as w<=1, contradicting alpha>alpha111. This proves the supporting-line right boundary is sharp.

## Stage112 **dual-only** successor

Along the exact A-face `L(K)=-185064/635+(21376/17145)*K`, fixed-policy gaps are affine. Sweeping the 849 downward-exposed positive gaps gives the next dual root
`K112=50591871/53872`, `L112=2961024/3367`, new state `T=(14,7,4)` immediate P vs Q; A remains P vs continue. Endpoint gap checks establish the *dual* breakpoint, not a Stage112 primal interval. Next compute T's **actual reachable first-hit mass**, error balance, primal feasibility and sharpness before promotion.

## Independent execution evidence and limits

Local author exact-rational `CHECKER_STAGE111.py` passed the full 680-state/1240-gap enumeration and all moment/sweep assertions. Separately written top-down memoized Bellman + *literal ordered-history DFS* `INDEPENDENT_ORDERED_STAGE111.py` matched exactly. Literal DFS visited **903895** root-reachable nodes at w=0 and **889909** at w=1, with 120 A hits, 6 F hits. The local complete archive includes runnable code, `certificate111.json`, logs, SHA256 manifest, and full expanded proof; archive SHA256 `c094b3f1f8bc95de24fef3c5124c4f6ac732c3bf4988a80d3e93eade93b2fbdd`. Independent mathematical Driver review and formal native CLAIM/Result were unavailable: `CONTROL_QUOTA` and `STATIC_READONLY_SCOPE_DENIED`; do not interpret ordinary GitHub author-side publication as native admission.
