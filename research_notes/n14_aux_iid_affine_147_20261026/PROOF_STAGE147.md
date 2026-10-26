# Stage147 — exact full-real optimal affine interval (external N14 iid model)

**Evidence level:** author computation-assisted finite proof; no independent Driver review or native Result. This is an auxiliary positive ordered-branch model, not a native P000 / Heartbeat / X6 theorem.

## Exact model and theorem
Symbols are iid under P=(1/8,1/24,5/6) and Q=(1/12,1/12,5/6); decisions and randomized stopping use arbitrary *complete ordered prefixes* up to N=14. Let eP=P(decide Q), eQ=Q(decide P), tP=E_P tau, tQ=E_Q tau, and V14(alpha)=min max(tP,tQ) subject to both errors <=alpha.

The Stage146 exact source is the immutable author proof at commit d8d1b8bb79e2280031884cf8aefabc6e453bb89d. Its right endpoint and optimum are

    alpha146=246603954391193214663775/708830536865346112978944
    V146=274086831038532347195394643/22682577179691075615326208

Define

    eta147=3274332971875/474771825210949632
    alpha147=246608842944125560263775/708830536865346112978944
    V147=273961171711816388948994643/22682577179691075615326208
    slope147=961898383273/1197470344

**Exact theorem:** for EVERY REAL 0<=delta<=eta147,

    V14(alpha146+delta)=V146-slope147*delta.

Furthermore for every alpha>alpha147 the same affine Bellman support is STRICTLY below V14(alpha): its right endpoint is sharp.

## Universal Bellman lower bound
For count state s=(n,a,b), iid likelihood ratio is r(s)=Q(prefix)/P(prefix)=2^(a+b)/3^a. Take positive multipliers

    K=488636304489/1197470344
    L=59157759848/149683793
    K+L=961898383273/1197470344.

Backward evaluate H(s)=min{K*r(s) [decide P], L [decide Q], 1+sum_i P_i H(child_i) [continue, n<14]}. Exact Fraction evaluation on all 680 possible count states gives

    Hroot=59027133919370211202074389/202463115774324935491584;
    ties exactly T=(7,1,2) Q/continue, W=(10,4,1) P/continue;
    1238 strictly positive alternative gaps, minimum
    6129035788073/1340860232871936; zero negative gaps.

The same Bellman inequality holds at each literal ordered history, because the iid conditional future and likelihood ratio are count-sufficient for this observer. It does not equate distinct histories or infer anything about native X6. Consequently every ordered-history randomized policy obeys

    Hroot <= tP+L*eP+K*eQ <= max(tP,tQ)+(K+L)*alpha

whenever both errors are <=alpha, so V14(alpha)>=Hroot-slope147*alpha.

## Exact ordered-branch observer certificate
At all other states use the strict Bellman minimizer; at the old Stage146 state U=(8,6,2) stop and decide P. At T let v be the probability of Q-stop (otherwise continue); at W let w be the probability of P-stop (otherwise continue). The true ordered cones are disjoint: T has symbol-b count 2 at depth 7, whereas W has symbol-b count 1 at depth 10, so T cannot precede W; W cannot precede T by time order. Thus no mixed randomization term occurs.

Independent P- and Q-integer-weight ordered-prefix DFS (branch weights P=(3,1,20)/24 and Q=(1,1,10)/12) finds first-hit inventories:

    T: 70 prefixes, massP=21875/2985984, massQ=21875/1119744
    W: 756 prefixes, massP=21875/7077888, massQ=21875/17915904.

Let M=(eP,eQ,tP,tQ). The exact complete four-observer map is

    M(v,w)=M00+v*dT+w*dW
    M00=(1219541629107847135/3505953353861431296,
         8272768163645/23776267862016,
         5297773635576824017/438244169232678912,
         622456093729211/53496602689536)
    dT=(1191246875/9393093476352,
        -1878471875/20061226008576,
        -377661353125/31701690482688,
        -44855715625/1671768834048)
    dW=(-17828125/1174136684544,
        4309375/185752092672,
        -169553125/48922361856,
        -23384375/15479341056).
    M11-M10-M01+M00=(0,0,0,0).

Four deterministic corner policies (v,w)=(0,0),(1,0),(0,1),(1,1) are independently evaluated with a backward Fraction observer recurrence and a literal ordered-prefix integer-weight forward DFS; the four complete tuples are in certificate147.json. Exact DFS visits: 606232,590482,583552,567802. Both methods agree componentwise. This separation retains actual ordered branches during first-hit counting, while the count recurrence is applied only to the declared iid suffix observer.

## Attainment for every real alpha in the interval
Balancing the two errors yields precisely

    v(w)=28086276907713/66250051520000
           +(36045864/207031411)*w.

For all real 0<=w<=1, 0<v(w)<1. Both errors are equal and strictly increase with rate

    d(alpha)/dw=3274332971875/474771825210949632 >0.

At w=0 the balanced policy reproduces alpha146,V146 EXACTLY. At w=1 it yields alpha147,V147, and the old T coin is strictly interior:

    v_end=39620953387713/66250051520000.

The larger expected time is tP throughout: its excess over tQ at the endpoints is respectively

    386046490754488341010345/840095451099669467234304 >0,
    386586105152287841810345/840095451099669467234304 >0.

All four observers are affine in w, hence tP>tQ and error balance hold throughout the REAL interval. At BOTH endpoints, tP+L*eP+K*eQ=Hroot exactly, hence it holds for all intervening w. Thus the policies attain the universal dual lower bound, establishing the stated exact value for every real alpha in the interval.

## Strict right-end sharpness
The feasible finite ordered-prefix policy space (or its occupancy-measure image) is compact, so an optimum exists. If alpha>alpha147 attained the same support, positivity of K,L would force eP=eQ=alpha and equality in the Bellman bound. Every reached action must minimize Bellman, leaving only T and W as possible nontrivial randomizations. At a tied count state every reachable ordered history has the same likelihood ratio and the same fixed continuation suffix, so any history-varying tie coins have exactly the same observer as one P-mass-weighted effective coin. The cones do not overlap, so all such policies are represented by M(v,w), with 0<=v,w<=1. Error equality forces the compensation v=v(w) above, and its common error is strictly increasing in w. Its maximum for w<=1 is alpha147, contradiction. Therefore Hroot-slope147*alpha<V14(alpha) for all alpha>alpha147.

## Verification, provenance, limits and next unit
Author locally executed exact Fraction Bellman enumeration, backward four-observer recurrence, and separately structured literal integer-weight DFS, checking all four corners, history masses, zero cross-term, balanced endpoints, positive time gap, and dual equality. Source VERIFY_STAGE147.py, certificate147.json, and this proof were prepared as same-run artifacts. These are **author** validations, not independent Research Driver passes. No native Source CLAIM or Result is asserted: direct control tasks returned CONTROL_QUOTA; session_start returned STATIC_READONLY_SCOPE_DENIED (operation_sent=false). The owner cannot be certified from these replies.

Input sources: GLOBAL_KNOWLEDGE_V1 main@3f9231cf4cf28d5b4db3319e2226095790a66ffc, Enterprise Math main@3f087ba35e490062aa45f4752d788d0d53e8923d, predecessor Stage146 immutable commit d8d1b8bb79e2280031884cf8aefabc6e453bb89d. The auxiliary result has no proved native-P000 transfer.

**Stage148 open unit:** From W saturated P-stop=1 and interior T Q-stop, find the next valid exact Bellman dual-ray candidate and nontrivial tie; prove/refute the next full-real primal interval, preserving literal branch provenance and checking any intersecting history cones.
