# Stage188: complete real-parameter optimality for a ternary IID stopping model

Date: 2026-10-27. Author-level exact proof and computational certificate for the **external** N14 model. This is not a native P000 X6 statement or an independently admitted Research Driver Result.

## Sources and scope
Fixed GLOBAL_KNOWLEDGE_V1: `awdawmip/chatgpt-global-knowledge@8bb9a989344e8317654f0d9b79873213fad73574`. EM canonical control source: `awdawmip/enterprise-math@f42f247fc0e5d99450a1a8b5af005824135b543b`. Stage187 immutable scientific predecessor `df3002a04596f1f8e793557754238a68fdc76c08` and its `NEXT_TASK_PACKET_188.md`. The 2026-10-27 native task inventory read returned `CONTROL_QUOTA`, and native session creation returned `STATIC_READONLY_SCOPE_DENIED`, `operation_sent=false`; no live Task owner was asserted or displaced.

Let `P=(1/8,1/24,5/6)`, `Q=(1/12,1/12,5/6)`; for all randomized stopping/decision rules by observation 14, including those depending on the **entire ordered history**, write `eP=P(output Q)`, `eQ=Q(output P)`, `tP=E_P[T]`, `tQ=E_Q[T]`, and `V14(alpha)=min_{eP,eQ<=alpha} max(tP,tQ)`.

## Exact full-real theorem
The preceding boundary is
`alpha187=47564236941933996508186187/135753377754634620902572032`,
`V187=47526009692613945133124984819/4344108088148307868882305024`.
For **every real**
`0<=delta<=292456756478102828004390419621/706073590206266022084331922522112`,
we prove

`V14(alpha187+delta)=V187-(79199149578269845/226849611128761)*delta`.

The exact next endpoint is

`alpha188=9370003598922725167379/26711406663770723844096`,
`V188=1153476444134184737662789/106845626655082895376384`.

For every real `alpha>alpha188` the same fixed Stage188 support line is **strictly below** `V14(alpha)`.

## Dual Bellman certificate
Take `K=39993714743501421/226849611128761`, `L=39205434834768424/226849611128761`, `H=552023450050793309312530706424493/4142313307078339047903008391168`. At count state `s=(n,a,b)` with counts of the first two outcomes `a,b`, the exact likelihood ratio is `ell(s)=Q(path)/P(path)=2^(a+b)/3^a`. Backward induction computes

`h(s)=min{K*ell(s), L, 1+sum_i P_i*h(child_i)}`, without continue at `n=14`.

All 680 states are covered. The root is H. The **only** ties are `R=(5,2,0):P/C` and `X=(8,0,1):Q/C`. All 1,238 other action alternatives have strictly positive gaps, minimum `1858369546682908/55124455504288923`, none negative. Conditioning each history's chosen action and inducting backward proves the same lower bound for all full-history randomization policies:

`tP + K*eQ + L*eP >= H`, hence `V14(alpha)>=H-(K+L)*alpha`.

## Exact primal four-corner observers
Let r be stop-P probability at R, x stop-Q probability at X, with unique Bellman actions elsewhere, and `O(r,x)=(eP,eQ,tP,tQ)`. Independent exact-rational suffix DP and a fully unmerged integer-weight DFS give
`O(r,x)=B+r*DR+x*DX+r*x*C`, with

`B=(614327156485249049/1752976676930715648,112420429746569/320979616137216,2399458169537790935/219122084616339456,285698064489565/26748301344768)`

`DR=(-2017385723125/2282521714753536,30670091875/20061226008576,-11106583313125/95105071448064,-105153394375/1671768834048)`

`DX=(84427421875/17832200896512,-58984375/15479341056,-326450234375/2229025112064,-26297890625/104485552128)`

`C=(0,0,0,0)`.

The cones are disjoint: a path at R already has two zeros, whereas X has zero zeros despite greater depth; reverse ancestry is impossible by time. Full ordered-history DFS nodes at corners (r,x)=(0,0),(0,1),(1,0),(1,1) are respectively **196954, 196186, 186574, 185806** (total **765520**), with componentwise exact agreement against independent suffix DP; R first-hit paths=10 and X first-hit paths=8 in the continue/continue baseline.

## Attainment for every real alpha in the interval
Solving exact balance `eP=eQ` gives

`r(x)=1085148487960651/12688037270560000+(280862064000/79300232941)*x`.

This coin is legal precisely from x=0 until the R coin reaches 1 at

`x*=1289209864733261/4993103360000000`, with `0<x*<1`.

The algebraic x=1 extrapolation yields `r(1)=46023078727960651/12688037270560000>1`: the saturation at **R**, not X, determines the next optimum endpoint. Along the legal segment:

`alpha(x)=alpha187+(17722625869434453125/11047638163625864331264)*x`,

`tP(x)=V187-(6187433560802331640625/11047638163625864331264)*x`,

`tP(x)-tQ(x)=1150048379079279125875697267/4344108088148307868882305024-(2837185427537112109375/33142914490877592993792)*x`.

Both endpoint time gaps are positive, including `(tP-tQ)(x*)=960164553826484768591/3957245431669736865792>0`; the affine expression is positive throughout. `alpha'(x)>0`, giving every real alpha between the endpoints. Every action used is Bellman-minimizing; exact equality `tP+K*eQ+L*eP=H` plus `eP=eQ=alpha(x)` and `tP>tQ` proves attainment and the stated slope `-(K+L)=-79199149578269845/226849611128761`.

## Full-history sufficiency and right sharpness
At a fixed count state, all individual ordered histories share the same IID P/Q likelihood ratio and conditional future law. Under an arbitrary history-dependent **Bellman-equality** policy, average stop probabilities over each state's incoming exact P mass to define effective r,x; the same averages preserve Q contributions due the constant ratio. The R and X first-hit cones are disjoint, so neither coin modifies the other's incoming mass; thus every equality policy has precisely the affine observer O(r,x) above. This proves a task-scoped sufficient quotient, with its retained BRC positive-rational branch and ordered provenance, not a native X6 compression theorem.

For alpha>alpha188, attaining `H-(K+L)*alpha` would force Bellman equality, `eP=eQ=alpha` (since K,L>0), and `tP>=tQ`. The effective coins must obey `r=r(x)`, `r<=1`, hence `x<=x*` and `alpha<=alpha188`, contradiction. The finite full-history randomized-policy space is compact, so a minimum exists and strictness follows for every real alpha to the right.

## Exact executable evidence and next frontier
The author ran `fractions.Fraction` suffix DP, a separate full ordered-history DFS with exact P/Q integer weights on denominator `24^14`, four corner comparisons, exact endpoint/legal/time checks and a new Bellman candidate scan. Sentinel: `STAGE188_AUTHOR_EXACT_FULL_REAL_PASS`. The local portable archive retains the **full executed** Python, exact JSON certificate and raw stdout; `REPRO_STAGE188.py` in this branch is a separate reproducible reference checker.

At x=x*, R is forced to P and X still has an interior Q/C coin. Perturbing dual weights along `dK=-1080671/869760,dL=-1` preserves X and opens R strictly toward P. The first closure is `T=(13,6,4):Q/C`, step `129884102431306558560/78751523052182767433`. Stage189 exact **dual-only** values: `K189=241967493/1388612`, `L189=59424392/347153`, `H189=209137371682549614928313/1584768521683668566016`; 680 states, only X/T ties, 1238 positive gaps, minimum `66370340952961/3582466457075712`. Stage189 primal/full-real theorem is the next bounded question; see `NEXT_TASK_PACKET_189.md`.

BRC method: `REUSE_APPLIED` for exact positive-rational branch mass, multiplicity, source provenance, and future-observer sufficiency. Positive mass is not signed/phase cancellation. This external model is not a P000 X6 dynamics theorem, and no independent Driver mathematical admission is implied by GitHub persistence.
