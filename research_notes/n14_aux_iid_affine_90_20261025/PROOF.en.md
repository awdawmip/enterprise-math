# N=14 auxiliary iid sequential testing — Stage 90 exact affine support

Date 2026-10-25. AUTHOR-SIDE EXACT FINITE-MODEL PROOF; not an independent Research Driver review, native CLAIM/Result, P000 theorem, or BRC/X6/Heartbeat bridge.

## Precise problem and theorem

For iid P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), consider **all ordered-history randomized sequential tests of horizon N=14**, with errors eP=P(decide Q), eQ=Q(decide P) and mean sample sizes tP,tQ. Set V14(alpha)=inf{max(tP,tQ):eP<=alpha,eQ<=alpha}. The inherited exact stage89 boundary is
alpha89=5172392071501613543/14900301753911083008,
V89=24307502088163349729/1862537719238885376,
s89=29743962535332427/41779200000000000,
where s89 is the immediate-Q probability at B=(12,0,1). All earlier deterministic actions are inherited from source commit 96e04e09dce8716acaecf3a69fb2dc8b0e845a80; in particular A89=(11,5,4) is now immediately Q.

**Theorem.** For every real 0<=delta<=eta90=291531275/8622859811291136,
V14(alpha89+delta) = V89 - (6100591284/1665893)*delta.
In particular
alpha90=5172392575267656743/14900301753911083008,
V14(alpha90)=24307271485812814529/1862537719238885376.
This affine support is right-sharp.

## Global dual lower bound

At K=lambdaQ=3166224876/1665893 set lambdaP=72+(8/9)K=2934366408/1665893 and Gamma=lambdaP+lambdaQ=6100591284/1665893. At a count state h=(n,a,b), Q/P=2^(a+b)/3^a. Define terminal P decision cost D_P=lambdaQ*Q/P, terminal Q decision cost D_Q=lambdaP, and continue cost D_C=1+sum_i P_i D(h+i); D(h)=min(D_P,D_Q,D_C), omitting continue at n=14.

Exact rational backward evaluation over all 680 states produces 1240 alternative-action comparisons against the inherited chosen action: 1238 strictly positive gaps, zero negative gaps and precisely **two** zero gaps, continue/Q at A90=(7,2,3) and B=(12,0,1). The smallest positive gap is 40045614911/35373012221952. Independently minimizing each state's actions gives the same root:
D0=468802934844745618084160341/365033946907767585374208
   =V89+Gamma*alpha89.
The count-state Bellman value bounds arbitrary ordered-history policies because independent suffix laws and their likelihood ratios depend only on h. For every feasible policy,
D0 <= tP+lambdaP*eP+lambdaQ*eQ <= max(tP,tQ)+Gamma*alpha,
hence V14(alpha)>=D0-Gamma*alpha.

## Exact positive ordered-history statistics and disjoint cones

At A90, 210 nominal ordered words exist; only **126** are truly first-reachable under the inherited stopping rules. Separate first-hit masses are
pA=175/1769472, qA=175/497664.
Exact ordered-depth-first enumeration yields **103** terminal suffix words in 26 terminal action/state classes. Early stopping at A90 truncates 126*103=**12978** complete histories, a count not to be confused with probability.
Under the inherited continuation suffix policy, conditional (P-error,Q-error,P remaining mean samples,Q remaining mean samples) is
RA=(28225835/28311552, 10307/17915904, 1704899/1179648, 628895/497664).
At B the 12 nominal first-hit prefixes are all reached:
pB=48828125/725594112, qB=48828125/362797056,
RB=(63/64,1/144,9/8,13/12); there are five B terminal suffix words.
The two randomized decision cones are disjoint: A90 has already accumulated a=2 zeros by depth 7 while B has a=0 zeros at depth 12. Counts are monotone, and B cannot reach earlier A90.

This is a typed finite positive-rational ordered-branch audit in the spirit of weighted BRC: prefix multiplicity, first-hit P/Q mass and suffix distribution are retained separately. No signed cancellation, native BRC embedding or native geometry claim is made.

## A continuum of optimal randomized policies

For every real u in [0,1], stop at A90 and decide Q with probability u. At B independently decide Q with probability s. The base point is (u,s)=(0,s89). Define exact coefficients
X=pA*(1-RA[P-error])=15000475/50096498540544,
Y=qA*RA[Q-error]=1803725/8916100448256,
E=pB*(1-RB[P-error])=48828125/46438023168,
H=qB*RB[Q-error]=48828125/52242776064.
Disjointness makes the following exact for **all real** (u,s), without an interaction term:
eP-alpha89=X*u+E*(s-s89),
eQ-alpha89=-Y*u-H*(s-s89).

Equal errors force s=s89+h90*u with
h90=-(X+Y)/(E+H)=-439761693/1740800000000.
Then eP=eQ=alpha89+eta90*u where
eta90=291531275/8622859811291136>0.
At u=1,
s90=29733408254700427/41779200000000000,
so 0<s90<s89<1, hence probability feasibility along the entire real segment.

tP-tQ is affine along this line, with exact endpoint values
at u=0: 2166717554273724305/3725075438477770752>0,
at u=1: 2167774451913429905/3725075438477770752>0.
Thus tP>tQ for every real u in the segment. All actions used by the policy are minimizers of the fixed dual Bellman recursion (only ties are at A90 and B), giving
tP+lambdaP*eP+lambdaQ*eQ=D0.
Consequently max(tP,tQ)=tP=D0-Gamma*(alpha89+eta90*u); the global lower bound is attained for every real delta=eta90*u.

## Right endpoint is sharp

The finite-horizon ordered-history randomized policy/occupation-measure set is a compact finite-dimensional polytope, so the optimum is attained. If alpha>alpha90 attained equality with this *same* support, positive dual multipliers would force both errors to equal alpha, and only Bellman-minimizing actions could occur at positive-mass histories. The gap audit permits randomization solely at the two count states A90,B. Different ordered prefixes at the same count state have identical Q/P and identical deterministic continuation suffix statistics; replacing history-varying randomization with the P-mass-weighted average preserves all errors and sample means. The two cones are disjoint, so the same pair (u,s) in [0,1]^2 and the exact equations above apply. Equality of errors forces s=s89+h90*u and alpha=alpha89+eta90*u<=alpha90, a contradiction.

## Reproducibility, limitations, next unit

Run Python standard-library exact rational programs derive90.py and crosscheck90.py together with the pinned predecessors derive89.py and derive88.py from the stage89/stage88 research notes. crosscheck90.py enumerates all ordered first-hit prefixes and suffix words separately, and recomputes true minima at every Bellman state; it shares the inherited stop-action table, so it is not an independent Driver review. Full locally executed outputs, original predecessor scripts and expanded bilingual research bundle are available separately in the user-delivered stage90 zip.

Native em_control_tasks returned CONTROL_QUOTA, and native em_session_start returned STATIC_READONLY_SCOPE_DENIED with operation_sent=false. Neither active Owner nor CLAIM is verified; this is only author-side source persistence.

New **unproved** stage91 directional crossing: K91=4256337294/2241499 at A91=(6,0,2), continue versus immediate Q. Prove or refute its feasible continuum with the exact stage90 endpoint action table.