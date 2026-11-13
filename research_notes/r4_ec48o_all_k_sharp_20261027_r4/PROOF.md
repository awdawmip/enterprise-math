# EC48O — Sharp memory cardinality for every finite three-stage BRC source size

Date: 2026-10-27, Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_COMPUTATION_PASS / UNREVIEWED / NOT_ADMITTED. Local research identity: EM-R004-EC48O-20261027T1400-LOCAL; this is not a native session or CLAIM. Current owner lookup returned CONTROL_QUOTA.

Verified source pins: GLOBAL_KNOWLEDGE_V1 main@cdd8723f1b670a3bfe1f27075649a5b48791801d; Enterprise Math main@0a253aea95b51ba1f19abfc4a34f22da068e6729. The P000 startup projection names canonical blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc, matching the original P000 blob. ACTIVE worldview, TASK bootstrap, portable research, native X6, positive BRC and joint-observer-preservation interfaces apply. This is an auxiliary finite observation theorem, not a claim about native heartbeat dynamics.

## Exact observer contract

Two strictly positive source laws P,Q on finite three-stage paths (h,x,y). There are k first-stage histories h. At times 1 and 2, a full observer may stop/accept, stop/reject or continue; at time 3 it must accept/reject. The observable vector is O=(alpha,beta,tauP,tauQ)=(P(accept),Q(accept),E_P T,E_Q T). S_full and S_m are the *raw* sets attainable with arbitrary source-neutral private randomization and no persistent shared public seed.

An m-state compressed observer writes a register using h at time 1. At time 2, after observing x, it may rewrite this register from (old register,x,current joint P/Q likelihood ratio) *before* the stopping action. Action readouts see (time,current joint likelihood ratio,current register). Terminal acceptance reads terminal joint likelihood ratio and register. No discarded h is available. All kernels may depend on the intended policy.

## Theorem: exact worst-case state capacity

For every integer k>=1, the least state cardinality that preserves the full *raw four-dimensional observer region for every finite positive horizon-three model* with k first histories is

    M_*(k) = max(k,2).

For every k>=2 there is a positive source family with exact finite-memory support separation, simultaneously for all real epsilon,c with

    0 < epsilon < 1,  0 < c < epsilon/[2(k+3)]:

    V_full = epsilon/k - (4+2/k)c,
    V_(k-1) = V_full - 4c/k^2,
    V_full - V_(k-1) = 4c/k^2 > 0,

where V_m is the maximum of J=alpha-beta-c(tauP+tauQ) on S_m.

### Positive source family

Let h,x range over {1,...,k}. Every time-two prefix has p_hx=q_hx=1/k^2, so all time-one and time-two joint likelihood ratios are exactly 1. For h!=x, one terminal leaf y=0 has p=q=1/k^2. For h=x there are two terminal leaves:

    p_hh+ = (1+epsilon)/(2k^2), q_hh+ = (1-epsilon)/(2k^2)
    p_hh- = (1-epsilon)/(2k^2), q_hh- = (1+epsilon)/(2k^2).

All k^2+k leaves have strictly positive P and Q weights and both measures sum to 1. The only positive terminal P-Q contrast comes from h=x,y=+, with exact value epsilon/k^2. The current terminal joint LR is (1+epsilon)/(1-epsilon) for +, its inverse for -, and 1 otherwise.

The full observer continues at time 1 for all h, continues at time 2 exactly for x=h, and accepts exactly y=+ at time 3. Its vector is

    O_full=((1+epsilon)/(2k),(1-epsilon)/(2k),2+1/k,2+1/k).

After the mandatory initial time cost -2c, each first history contributes

    g = epsilon/k^2 - 2c/k - 2c/k^2
      = [epsilon-2c(k+1)]/k^2.

The declared range makes g positive. Continuing a diagonal time-two cell adds net (epsilon-2c)/k^2>0; continuing an off-diagonal cell costs 2c/k^2>0. Hence the displayed full strategy optimizes each node (all early accept/reject decisions at LR=1 are dual-neutral) and V_full=-2c+kg.

### Randomization and memory partition certificate

For the finite-horizon *linear* support functional, fixing every stochastic kernel except one leaves the expected reward affine in the remaining kernel row: no trajectory visits the same time-indexed row twice. Successively selecting maximizing simplex vertices yields an equally good deterministic finite-memory controller. This extremal reduction is for support values; raw-set equality is not inferred from it.

A deterministic first writer assigns each h to one of at most m register classes. All members G of a class see the same LR=1, so they either all stop at time one or all continue. If continued, each member sees an identical time-two decision for any fixed x, because (old register,x,LR=1) is equal. Let s=|G| and D_G be the shared set of x on which continuation occurs. Optimal terminal acceptance depends only on terminal joint LR. The group's gain above initial -2c is exactly

    B(G,D_G) = -2cs/k + epsilon*|G intersect D_G|/k^2
               -2cs*|D_G|/k^2.

For x outside G, including x in D_G loses 2cs/k^2. For x inside G, including x gains (epsilon-2cs)/k^2>0 throughout the declared parameter range. Therefore the unique optimal time-two continuation set for a continued class is D_G=G. Such a class obtains

    B(G,G)=s*epsilon/k^2 - 2cs/k - 2c*s^2/k^2.

Relative to s distinct full-history classes, its unavoidable loss is

    s*g-B(G,G) = 2c*s(s-1)/k^2.

If any first history stops at time one, its loss g is greater than 4c/k^2, since epsilon>2c(k+3). All other first histories separately earn at most g. Otherwise all k histories continue, and for m<=k-1 the partition has some class of size s>=2. Consequently sum_G s(s-1)>=2, and the value gap is at least 4c/k^2.

This bound is attained for m=k-1: place exactly two histories in a common class and give the remaining k-2 histories individual classes; continue all at time one and at time two continue precisely when x belongs to the old-register class. For k>=3 the writer rewrites to two of its k-1 states representing the time-two stop/continue flag. For k=2 the only one-state class contains both possible x, so continuing for both requires no extra flag. At time three the joint LR suffices for optimal acceptance. Exactly one size-two class contributes loss 4c/k^2. Thus the displayed V_(k-1) formula holds for *every real parameter in the declared interval*, not just sampled rationals. Fewer states have a subset of the (k-1)-state policy class, so the strict support separation persists.

### k=1 sharpness

For one first-stage history and two equally weighted second-stage signals x=a,b, take a neutral terminal at b with p=q=1/2, and two terminals at a with

    p_a+=(1+epsilon)/4, q_a+=(1-epsilon)/4;
    p_a-=(1-epsilon)/4, q_a-=(1+epsilon)/4.

Every weight is positive. Stage-two ratios at a,b are both 1. A full observer continues at t=1, continues only at a at t=2, then accepts +. With 0<c<epsilon/8,

    V_full=epsilon/2-5c.

A one-state register cannot react differently to a and b at t=2: in every deterministic extreme policy it continues on both or neither. The best value is

    V_1=epsilon/2-6c,

hence the exact support loss is c>0. This proves the lower bound 2 for k=1.

### Matching original-region upper bound (EC48N constructive interface)

For arbitrary positive sources with k first histories, max(k,2) states preserve *every* full-history behavioral policy's four coordinates. At t=1 injectively encode h in k register states and exactly reproduce its time-one actions. At t=2 recover (h,x), rewrite to a source-neutral continue bit with the original t=2 continuation probability, and stop/continue according to that bit. For a stopped state at joint LR=r, choose the accept probability to be the original stop-and-accept Q-mass divided by the stopped Q-mass in the entire exact r fiber. All P masses are r times the Q masses within that fiber, so alpha and beta are both preserved. At t=3 use the same exact joint-LR Q-mass averaging for original terminal acceptance, conditioned on reaching the continued register; source-neutral continuation factors preserve P/Q proportionality. Per-prefix continuation probabilities preserve both time expectations, giving identical (alpha,beta,tauP,tauQ) without any common random seed. Only two flags are needed after t=2; the register can be reused. Conversely every memory policy is a full-history policy. Hence S_max(k,2)=S_full. The timing and *joint* LR qualifications are essential.

This upper construction, combined with the new lower witnesses, establishes M_*(k)=max(k,2).

## k=4 exact positive rational certificate

Set k=4, epsilon=1/2, c=1/64. Every off-diagonal (h,x) has one leaf with (P,Q)=(4,4)/64; each diagonal (h,h) has + leaf (3,1)/64 and - leaf (1,3)/64. There are 20 positive leaves, and every first-stage history has (16,16)/64. The full optimal observation vector and value are

    O_full=(3/16,1/16,9/4,9/4),   V_full=7/128.

The best three-state machine groups first histories 1 and 2, and otherwise keeps histories 3 and 4 separate. It continues x in the stored class, resulting in

    O_3=(3/16,1/16,19/8,19/8),  V_3=13/256,
    V_full-V_3=1/256.

The included exact JavaScript checker enumerates 3^4=81 initial register assignments, 2^3=8 time-one action vectors each, and all 2^4=16 time-two masks for every active class: 12,480 exact integer mask evaluations. Every terminal signal is evaluated under its exact P/Q sign; off-diagonal acceptances are dual-neutral. The computed optimum is 13/256. Independent Python Fraction computation on this same family and nine parameter instances k=3,4,5 also passed; that original author-side program and its detailed report are available in the accompanying local evidence package.

## Scientific and admission boundary

BRC reuse: REUSE_APPLIED — positive rational source-labelled weighted branches and exact joint-LR fibers from the T0 weighted BRC substrate and EC48N; P-Q is a **difference of positive measures used as a dual observer**, not a signed BRC amplitude carrier. Compressing history into current LR deletes future-relevant branch identity until adequate memory repairs the four declared observables over the stated horizon.

P000 remains the project's fixed six-native-axis discrete X6 space plus separately typed time. No native plane or untyped two-dimensional reduction is introduced. Native transfer needs explicit admissible Cell path embeddings, observer/readout maps, and preservation of future operations; none is assumed here. No Lean formal check, external novelty certification, independent Driver review, native Result, Working Truth or Foundation promotion is asserted.

**Next question EC48P:** Fix exactly *two* possible time-two signals for all first histories (independent of k). Does a fixed number of register states suffice to preserve the original raw four-coordinate region for arbitrarily many first histories? Analyze support signatures first, then the separate stochastic raw-set issue; provide exact lower/upper certificates. The k-signal diagonal family in this proof does not answer that restricted-alphabet question.
