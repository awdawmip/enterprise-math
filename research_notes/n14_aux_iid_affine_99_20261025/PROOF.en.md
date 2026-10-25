# Stage99 exact affine minimax theorem — external N=14 iid auxiliary model

**Status:** author-side exact finite-model proof; two local exact rational checks; NOT independently reviewed, NOT a native Task/CLAIM/Result, and NOT transferred to P000/X6/Heartbeat or native BRC dynamics. Source: prior Stage98 author frontier in research_notes/n14_aux_iid_affine_98_20261025.

## Statement

Let P=(1/8,1/24,5/6) and Q=(1/12,1/12,5/6) be iid distributions on {0,1,2}. A randomized sequential test may use all ordered histories, stops by N=14, and decides P or Q. Write eP=P(decide Q), eQ=Q(decide P), tP=E_P(tau), tQ=E_Q(tau), and V14(alpha)=min max(tP,tQ) over tests with eP,eQ<=alpha.

The exact Stage98 endpoint is

    alpha98=2586269937332842327/7450150876955541504
    V98=757686022002985135/58204303726215168
    s98=12366057190345211/20889600000000000

where A98=(13,6,4) continues, A97=(4,4,0) and A96=(14,7,4) decide P, and B=(12,0,1) immediately decides Q with probability s98. Remaining actions are the K98=17496/13 Bellman minimizers with tie priority C,P,Q.

Set K99=6696/5, lambdaP=6312/5, lambdaQ=6696/5, Gamma99=13008/5 and eta99=107421875/2806920511488.

**Theorem. For every real 0<=delta<=eta99,**

    V14(alpha98+delta)=V98-(13008/5)*delta.

The sharp right endpoint is

    alpha99=2586555057332842327/7450150876955541504
    V99=751890958002985135/58204303726215168.

Here sharp means the same dual supporting line cannot achieve V14(alpha) at any alpha>alpha99, not that the optimum stops decreasing.

## Proof I: universal all-history Bellman bound

At count state v=(n,a,b), where a=#0, b=#1, the word likelihood ratio is Q(w)/P(w)=2^(a+b)/3^a. Backward define

    D(v)=min{lambdaQ*2^(a+b)/3^a, lambdaP, 1+sum_i P_i*D(v+i)}

and omit continuation at n=14. This minimizes tP+lambdaP*eP+lambdaQ*eQ over all randomized history-dependent tests, because the likelihood ratio and iid conditional future law depend only on the count state. This is a certified scope-typed quotient of branch histories, not erasure of their first-hit multiplicity.

The exact rational audit of the frozen Stage98 endpoint policy at K99 checks 680 states and 1240 nonselected comparisons: 1238 strictly positive gaps (minimum 12889/699840), 0 negative gaps, and only two ties:

    A99=(11,3,0): C versus immediate P;
    B=(12,0,1): C versus immediate Q.

It obtains

    D(root)=125467347054807071603/136951302885212160
           =V98+Gamma99*alpha98.

Thus V14(alpha)>=D(root)-Gamma99*alpha for arbitrary randomized ordered-history policies.

## Proof II: true first-hit masses and exact primal interval

At A=A99=(11,3,0), precisely 165 of the 165 nominal words are actually first reached. Their P/Q masses are

    pA=21484375/286654464, qA=21484375/967458816.

Continuing at A follows nine terminal ordered suffixes with conditional (P-error,Q-error,P-extra-time,Q-extra-time) vector

    RA=(41/13824,569/576,69/64,167/144).

At B=(12,0,1), 12 true first-hit words have

    pB=48828125/725594112, qB=48828125/362797056,

and five continued suffix words give

    RB=(63/64,1/144,9/8,13/12).

The A and B cones cannot intersect: after eleven observations A has three zeros, whereas B after twelve has zero; nonnegative counts cannot decrease. At A an immediate P-stop truncates 165*9=1485 formerly complete terminal histories. The weights are finite exact positive rational branch weights, with ordered-history provenance retained in enumeration.

For u in [0,1], stop immediately and decide P at A with probability u (otherwise continue); at B stop and decide Q with probability s (otherwise continue). Every other action stays frozen. Define

    X=pA*RA.Perror=880859375/3962711310336
    Y=qA*(1-RA.Qerror)=150390625/557256278016
    E=pB*(1-RB.Perror)=48828125/46438023168
    H=qB*RB.Qerror=48828125/52242776064.

The disjoint cones imply exactly for all real u,s in [0,1]:

    eP=alpha98-X*u+E*(s-s98)
    eQ=alpha98+Y*u-H*(s-s98).

Choose

    s=s98+h99*u,
    h99=(X+Y)/(E+H)=26961/108800,
    s99=s98+h99=17542569190345211/20889600000000000.

Since 0<s98<s99<1, all u in [0,1] are feasible. The two errors are exactly equal:

    eP=eQ=alpha98+eta99*u,
    eta99=E*h99-X=Y-H*h99=107421875/2806920511488 > 0.

All chosen actions minimize their Bellman values at K99; hence tP+lambdaP*eP+lambdaQ*eQ=D(root). The four expectations are affine functions of u since the critical cones are disjoint. At u=0,

    tP-tQ=1207595370727759775/1862537719238885376 > 0,

and at u=1,

    tP-tQ=1137415722727759775/1862537719238885376 > 0.

Consequently tP>tQ for every real u in [0,1], and tP=D(root)-Gamma99*(alpha98+eta99*u). The primal policy meets the universal dual lower bound pointwise across the entire real interval, proving the theorem without numerical interpolation.

## Proof III: sharpness on the right

The finite randomized history-policy occupation polytope is compact, so the optimal value is attained. Equality with the same supporting line for any alpha>alpha99 would force both eP=eQ=alpha (positive dual multipliers) and use only Bellman-minimizing reached actions. All strict gaps exclude variation outside A and B. History-dependent mixtures within one count fiber can be replaced by their P-arrival-weighted mean because Q/P is constant on that fiber and the future conditional iid law is identical. The critical cones are disjoint. Therefore their effective u,s in [0,1] still satisfy the two error equations, giving alpha=alpha98+eta99*u<=alpha99, a contradiction. Hence the right endpoint is sharp.

## Reproduction and scope

Local derive99.py reconstructs the Stage98 action table and enumerates all exact Bellman gaps, first-hit masses, suffixes, compensation and dual crossing. A separately coded crosscheck99.py uses independent K99 Bellman minimization and *ordered* DFS for first hits/suffixes, then checks seven exact rational randomized policies; it does not import derive99. Both local runs PASS, as does independent ZIP extraction/reproduction. The portable CHECKER.py here is the executed independent crosscheck implementation, and certificate99.json records its expected outputs. These are two author implementations, NOT an independent Research Driver pass. The all-real proof rests on affine and Bellman identities rather than finitely sampled parameters.

The next **dual-only** candidate is K100=177963480/134551, A100=(9,5,1), with C/P tie (and B's C/Q tie). Just below K100 the frozen C action at A100 develops negative gap -134551/1209323520000. Stage100 is not yet a primal theorem.

BRC applicability: the positive rational ordered-branch accounting is reused with exact P and Q histograms and likelihood ratios. Count compression is valid only for this finite iid cost/future observer. No claim is made about native BRC phase cancellation, Heartbeat, X6 or physical semantics. P000 and ACTIVE worldview are unchanged. Native control listing yielded CONTROL_QUOTA; native Researcher session creation yielded STATIC_READONLY_SCOPE_DENIED with operation_sent=false. Live owner, CLAIM, native Result and Driver mathematical admission remain unverified.
