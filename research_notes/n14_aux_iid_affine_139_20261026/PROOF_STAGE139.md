# Stage139 — exact finite-model full-real optimum and sharp right support (author)
 
**Claim scope:** Auxiliary ternary iid sequential decision problem, horizon 14, under arbitrary literal history-dependent randomized stopping rules. This is **not** a P000, native X6, or physical Heartbeat theorem. This is an *author-level exact finite-model proof*, pending independent Research Driver assessment and native research control CLAIM.
 
## 1. Model and inherited frontier
 
Each observed symbol has distribution `P=(1/8,1/24,5/6)` or `Q=(1/12,1/12,5/6)`. Strategies must stop and decide P or Q by observation 14, with private randomness permitted at each literal prefix. Define `eP=P(decide Q)`, `eQ=Q(decide P)`, and `tP=E_P tau`, `tQ=E_Q tau`. Let `V14(alpha)` be the infimum of `max(tP,tQ)` over rules with both errors at most alpha.
 
Stage138's author theorem (not independently reviewed) supplies the left endpoint:
 
```
alpha138=4078711246246925855/11735204976119513088
V138=217809339038053734409/17602807464179269632
```
 
See `research_notes/n14_aux_iid_affine_138_20261026/PROOF_STAGE138.md` and `NEXT_TASK_PACKET_139.md`. Do not conflate these author certificates with formal native Results or reviewer acceptance.
 
## 2. Exact theorem
 
For **every real number** `0 <= delta <= eta139`, where
 
```
eta139=1171440983125/34380483328475136
```
 
the exact optimum is
 
```
V14(alpha138+delta) = V138 - (1910746361590/1874305573)*delta.
```
 
In particular,
 
```
alpha139=12237333294307497565/35205614928358539264
V139=217197900202344934409/17602807464179269632
```
 
The same supporting affine line is **strictly below** `V14(alpha)` whenever `alpha > alpha139`; this sharpness concerns that line, not the existence of further feasible strategies at higher alpha.
 
## 3. Universal dual certificate covering *all literal-history policies*
 
Choose
 
```
K139=978154621902/1874305573
L139=133227391384/267757939
K139+L139=1910746361590/1874305573
```
 
For count state `s=(n,a,b)`, a and b being the counts of symbols 0 and 1, the likelihood ratio is `r(s)=Q(prefix)/P(prefix)=2^(a+b)/3^a`. Define the rational Bellman function backwards by
 
```
H(s)=min{ K139*r(s) [declare P], L139 [declare Q],
          1+sum_j P_j*H(next_j(s)) [continue if n<14] }.
```
 
Exact rational evaluation visits **all 680 count states** and finds only the two ties
 
```
B=(11,0,1): declare Q / continue
C=(6,3,0): declare P / continue
```
 
with 1238 strictly positive nonchosen action gaps, **zero negative gaps**, minimum strict gap `211792744307/7287300067824`, and root
 
```
H(0,0,0)=1792874224751669050640467609/4889306480521221538578432.
```
 
The count-state Bellman quotient is sound for these four declared observers at this finite horizon: under either iid hypothesis, prefix-conditional suffix laws depend only on the sufficient counts, while the literal prefixes and their P/Q probability masses remain distinct before aggregating. Backward induction therefore bounds **every** ordered-history randomized policy (not only count-state policies) by
 
```
H0 <= tP+L139*eP+K139*eQ
   <= max(tP,tQ)+(K139+L139)*alpha.
```
 
The first inequality arises from the exact conditional cost at every literal prefix; the second uses `K,L>0` and both error constraints.
 
## 4. Retained positive branch carrier and four observations
 
We retain individual ternary prefix IDs and exact *positive* word weights P=(3,1,20)/24 and Q=(1,1,10)/12; there is no signed cancellation, path-identity erasure, X6 projection or native physical inference. The first-hit inventory under the strict Bellman policy prior to both ties is
 
| tie | literal prefixes | P mass | Q mass |
| --- | ---: | ---: | ---: |
| B=(11,0,1) | 11 | 107421875/1451188224 | 107421875/725594112 |
| C=(6,3,0) | 20 | 625/27648 | 625/93312 |
 
All 20 nominal C prefixes actually survive earlier strict stops. B cannot follow C because its count of symbol 0 would have to decrease from 3 to 0; C cannot follow B because its depth 6 precedes B's depth 11. Therefore **no literal path visits both ties** and their conditional stopping perturbations have no cross term.
 
Let `w in [0,1]` be the probability of immediate decision Q at B and `h in [0,1]` the probability of immediate decision P at C. Elsewhere choose the unique Bellman-minimizing action. Set `M=(eP,eQ,tP,tQ)`. Exact count-state recursions produce
 
```
M(w,h)=M00+w*dB+h*dC
M00=(
 2430209012880070769/7011906707722862592,
 447332352063541/1283918464548864,
 10883425288197503711/876488338465357824,
 47209626318979/3962711310336
)
dB=(
 4619140625/2229025112064,
 -751953125/417942208512,
 -25673828125/278628139008,
 -17939453125/104485552128
)
dC=(
 -90883789375/760840571584512,
 559593125/3343537668096,
 -884756456875/31701690482688,
 -8395435625/835884417024
)
```
 
An independently implemented literal-word DFS using integer P/Q weights (rather than the Fraction observer backward recursion) matched the exact four-observer vector at **all four** deterministic corners. It visited 691060, 690928, 672820, and 672688 literal prefixes respectively at (w,h)=(0,0),(1,0),(0,1),(1,1). All four runs reproduced the first-hit counts 11 and 20 and the exact P/Q masses above. The resulting mixed four-corner finite difference is exactly zero.
 
## 5. Full continuum: primal attainment
 
Solving `eP=eQ` gives the exact affine compensation law
 
```
w(h)=38466217568843437/81438720000000000
     +(3142401319/42416000000)*h.
```
 
Both endpoints lie strictly inside (0,1):
 
```
w(0)=38466217568843437/81438720000000000
w(1)=44499628101323437/81438720000000000.
```
 
Consequently every real `h in [0,1]` defines a valid policy with equal errors, and exact substitution into `M00+w*dB+h*dC` yields
 
```
eP=eQ=alpha138+eta139*h
tP=V138-(K139+L139)*eta139*h
tP-tQ at h=0: 85737739727005324807/158425267177613426688 > 0
tP-tQ at h=1: 83841137177769484807/158425267177613426688 > 0.
```
 
The time difference is affine and positive throughout. The same exact substitution gives `tP+L139*eP+K139*eQ=H0`. This policy family attains the universal dual lower bound for **every real** `h` in the interval and proves the theorem without sampling intermediate points.
 
## 6. Sharpness
 
Finite-horizon behavioral policies form a compact product of finite probability simplexes, and their four observers are continuous, so any feasible optimum is attained. If a policy at any `alpha>alpha139` attained the same supporting line, equality in both steps of the lower bound with `K,L>0` would force `eP=eQ=alpha`, `tP=max(tP,tQ)`, and Bellman-optimal decisions at every reached positive-mass prefix. The 1238 positive action gaps exclude any other action; the only possible randomization is at B and C. Their disjoint cones permit averaging an arbitrary prefix-dependent random coin into effective `w,h in [0,1]`, with precisely the same four observed quantities. Equal errors force the displayed `w(h)`, whence `alpha=alpha138+eta139*h<=alpha139`, contradiction. Thus the affine support has a sharp right endpoint.
 
## 7. Evidence, authority and next gap
 
This proof is for the **external ternary iid auxiliary model only** and depends on exact finite computations. Two author-side local checkers ran with exact fractions / integer ordered-prefix weights; **no independent Research Driver review or Lean validation** is claimed. A GitHub-portable adaptation of the previous verifier is stored beside this note; unlike the two original local files, that adapted remote version was not asserted to be executed in the original local run.
 
Global source pin: `awdawmip/chatgpt-global-knowledge@161bf0e1b76d81ea489a1358996cbf749d840e1b` / `GLOBAL_KNOWLEDGE_V1`. Stage139 research-control input was read from Enterprise Math `d7e06a8e4371c04f74e01e7ee5331a7f33739294`. P000 projection's canonical blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc` was matched to original metadata; ACTIVE residual-faithful worldview retained. Native tasks endpoint returned `CONTROL_QUOTA`, so **active owner / native CLAIM / Result / admission remain unverified**. Ordinary GitHub write permission does not confer research ownership.
 
Next unit Stage140: At h=1 (C fully P-stop) and w<1 (B still mixed), find the new permissible Bellman dual direction and its first positive action-gap closure, then prove a new primal family or a precise obstruction. Preserve exact first-hit branch identities and all owner, Source, and review boundaries.