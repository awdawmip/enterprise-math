# Stage194: exact full-real optimal segment — external N14 ternary IID

**2026-10-27. AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED / PORTABLE_RESEARCH.** No native Heartbeat-X6 Cell theorem or independently accepted Source Result is implied.

## Model, provenance and theorem

Fixed input: P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6); horizon N=14. Policies may randomize as functions of any *full ordered history*, stopping and deciding P or Q or continuing before N. Define eP=P(decide Q), eQ=Q(decide P), tP=E_P(T), tQ=E_Q(T), and V14(alpha)=min under eP,eQ<=alpha of max(tP,tQ).

Global knowledge canonical `main@90b04585448a8466a336c0edca93a67a3e831156`, P000 projection original blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc` checked, EM initial `main@872dd27b755e8b33c8f7351a1f048188f210a42a`. Immediate author-level Stage193 proof: commit `ff0f96e1231fca59d269961ad1eab368d6cf5eda`; mathematical admission pending.

Start from exact author-level Stage193 endpoint
alpha193=14081565109314017676563/40067109995656085766144,
V193=1695052604792714166418885/160268439982624343064576.

**Theorem.** For every real delta, including irrational values, with
0<=delta<=Delta194=1608301826875170716615/10257180158887957956132864,

V14(alpha193+delta)=V193-(66857008/210911)*delta.

The next exact endpoint is
alpha194=1849072830472476953/5258930030792146944,
V194=1153308642566039965/109561042308169728.
For every alpha>alpha194, the *fixed Stage194 Bellman support line* lies **strictly** below V14(alpha).

## Bellman universal lower bound

At state s=(n,a,b), where a and b count symbols of types 0 and 1, the likelihood ratio Q/P equals ell(s)=2^(a+b)/3^a. Set

K=L=33428504/210911,
H=2114050937763575719833221/17330721745693789126656.

Backward induction calculates h(s)=min{K ell(s),L,1+sum_i P_i h(next_i(s))}; no continue for n=14. Exact rational evaluation on all **680 states** gives h(0,0,0)=H; **1238 strictly positive** action gaps, minimum 5619528281901114949/541585054552930910208; exactly two ties: X=(8,0,1), Q/C; Z=(14,0,0), terminal P/Q. For arbitrary full ordered-history randomized policies, conditional Bellman at each prefix yields

tP+K eQ+L eP >= H,
thus V14(alpha)>=H-(K+L)*alpha,
K+L=66857008/210911.

## Full ordered-history four-corner certificate; BRC-provenance preservation

At X, stop choosing Q with probability x, else continue. At Z (terminal all symbol-2 history) decide P with probability z, else decide Q. Else use the unique Bellman minimizing action.

**The two tie cones do not intersect.** X has count b=1 at depth 8, whereas Z has b=0 at depth 14. Counts never decrease, so X cannot precede Z, even though the first-symbol count a=0 in both. Z cannot precede X by depth. This second-count obstruction rules out a potential nonzero randomization interaction; the mixed coefficient is *exactly* C_XZ=(0,0,0,0).

For the observable O=(eP,eQ,tP,tQ), exact rational suffix dynamic programming gives O(x,z)=B+x DX+z DZ, where

B=(
  305299945102548403/876488338465357824,
  56808062771291/160489808068608,
  1169354324486039965/109561042308169728,
  15646813875599/1486016741376
),
DX=(
  84427421875/17832200896512,
  -58984375/15479341056,
  -326450234375/2229025112064,
  -26297890625/104485552128
),
DZ=(
  -6103515625/78364164096,
  6103515625/78364164096,
  0,0
).

All four deterministic policy corners (x,z)=(0,0),(0,1),(1,0),(1,1) were **independently cross-checked exactly** against unmerged full ordered-history integer P/Q-weighted DFS with branch weights P=(3,1,20)/24 and Q=(2,2,20)/24 and denominator 24^14. DFS nodes at those corners are 139822, 139822, 139054, 139054, totaling **557752**; eight ordered first-hit X paths and one Z path each, with zero ancestor intersections.

This use of positive P/Q rational branch masses, path provenance and full ordered-history multiplicity respects the BRC information-preservation principle. Count-state compression is justified for this *declared finite IID Bellman observer*, **not** for arbitrary native X6 path/field dynamics or signed amplitudes.

## All-real balancing coin, early saturation and right-side strictness

Impose eP=eQ. Solving exactly produces

x(z)=2968693027437307/4493793024000000 + (320000000/17553879)z.

At the left endpoint x(0)=the Stage193 terminal X coin. The admissible range ends *early*, at
zmax=1525099996562693/81920000000000000,
where x(zmax)=1. In particular zmax<1. Normalize u=z/zmax in [0,1]. The *physical randomization probability* is z=zmax u, so expressions below are normalized in u, **not** derivatives with respect to the unnormalized z:

eP(u)=eQ(u)=alpha193 + (1608301826875170716615/10257180158887957956132864)u;

tP(u)=V193 - (31863632084684980750795/641073759930497372258304)u;

tP(u)-tQ(u)=102526768638213155412863/480805319947873029193728
          +(68687018991691546966495/1923221279791492116774912)u > 0.

All x(z),z values are legal randomization probabilities for the entire **real** u interval. Shared errors rise strictly while tP>tQ, so the objective is tP. Every used action is Bellman minimizing, and tP+K eQ+L eP=H. Exact rational arithmetic gives the slope identity

- (tP(1)-tP(0))/(eP(1)-eP(0)) = K+L = 66857008/210911.

For arbitrary real delta in [0,Delta194], take u=delta/Delta194 and the coins z=zmax u, x=x(z). The resulting arbitrary-history admissible policy attains the universal Bellman lower bound: this proves the theorem without gridding or rational restriction.

For alpha>alpha194, equality with the fixed support would force *every reached* action to be Bellman minimizing because the other gaps are strict and all P/Q branch probabilities are positive. A full-history tie policy is observationally equivalent, **for this IID declared observer**, to one effective X coin and one effective Z coin: likelihood ratio and IID suffix responses coincide within each tied count state and the tied cones are disjoint. Since K,L>0 equality forces both errors exactly alpha, and solving the balance equation above forces x<=1, z<=zmax and alpha<=alpha194. Contradiction. The bounded finite policy space is compact with continuous constraints, so the minimum is attained and the inequality is strictly separated for all alpha>alpha194.

## Executed evidence, constraints, next frontier

The actual local `VERIFY_STAGE194_EXECUTED.py` (rational Bellman + suffix DP + independent unmerged integer DFS) returned `STAGE194_AUTHOR_EXACT_FULL_REAL_PASS`; local `SCAN_STAGE195.py` returned `STAGE195_DUAL_SCAN_PASS`. Their **actual executed sources**, complete original logs, exact certificates, proof, and SHA256 manifest are in `EM_STAGE194_AUTHOR_EXACT_PORTABLE_20261027.tar.xz`; archive SHA256 `26c9a325d88a498a2f6509e0c7822e2616a731dc435d79b1a542a996ca63401f`. Repository reference reproductions may be distinct programs and should not be described as remotely executed.

Native `research_authority_granted=false`; canonical control task inventory blocked by `CONTROL_QUOTA`; no verified active owner, native session/CLAIM, freeze, independent Driver review or admission. All results are author-level. P000 remains native Heartbeat X6+separately typed time; **no X6 readout/future-operation bridge** has been established.

**Stage195: DUAL_ONLY** — K195=L195=82768824/535283, H195=1748561457410484827718287/14661540852461004128256, ties Y=(9,5,2) P/C and Z=(14,0,0) terminal P/Q; 680 states, 1238 positive action gaps, min 3412925531/88797026304. Next calculate full ordered Y/Z four corners, test ancestry/mixed term, prove legal error-balance interval and tP/tQ dominance or return a precise rational obstruction. Do not call Stage195 primal-proved.
