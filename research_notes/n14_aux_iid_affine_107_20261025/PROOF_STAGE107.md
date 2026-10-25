# Stage107 — exact affine minimax segment ending by B-probability saturation

**Evidence:** author-side exact-rational computation-assisted proof, cross-checked with two separately implemented Python algorithms. Not a Research Driver admission, canonical native CLAIM/Result, or theorem about P000's six-dimensional Cell world.

**Frozen sources:** GLOBAL_KNOWLEDGE_V1 main 04aa116d3c89bc5fee453d6467cd87eed27221fe, P000 canonical original Git blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc; Enterprise Math main cbece42d9ec43fe8dfd9f16b2261d18b59ce1b7e, especially Stage106 PROOF_STAGE106.md and NEXT_TASK_PACKET_107.md. The current model is the external iid ternary experiment P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), horizon n<=14, and arbitrary full-ordered-history randomized stopping/decisions.

## Exact result

Let eP=P(decide Q), eQ=Q(decide P), tP=E_P tau, tQ=E_Q tau, and V14(alpha)=min_{eP,eQ<=alpha} max(tP,tQ). From the Stage106 author-verified endpoint

alpha106=646648605512624167/1862537719238885376,
V106=6009214469256084569/465634429809721344,

**for every real 0<=delta<=855824768552109707/23915605160933701189632**,

V14(alpha106+delta)=V106-(1526472/767)*delta.

Its exact right endpoint is

alpha107=91588670614917102449/263775056922062880768,
V107=13541383133505475882195/1055100227688251523072.

The same support line is unattainable at any alpha>alpha107 (support sharpness). The endpoint is reached when B's Q-decision probability equals one, **not** when the new A tie mixing reaches one.

## Proof: dual for all ordered-history tests

At count prefix z=(n,a,b), the conditional likelihood ratio is Q/P=2^(a+b)/3^a. Put K=778896/767, L=747576/767=72+(8/9)K, Gamma=K+L=1526472/767. For n<=14 define the exact rational Bellman recursion

D(z)=min{K*2^(a+b)/3^a [decide P], L [decide Q], 1+sum_j P_j*D(next_j z) [continue]},

where continuation is absent at n=14. This is a backward induction over **every ordered prefix**, even though the conditional value is a function of counts. It yields D(root)<=tP+L*eP+K*eQ<=max(tP,tQ)+Gamma*alpha for every randomized policy.

Full rational enumeration of 680 states and 1,240 nonselected-action gaps: 1,238 positive, zero negative, exactly two zero alternatives:
A=(10,3,0): P / continue; B=(12,0,1): Q / continue.
Minimum strictly positive gap: 12607/331344.
D(root)=14787165590378589778037/21008329862591545344.
The strict continuation policy, continuing at A and choosing Q at B, has nonnegative action gaps at both K106=107892/101 and K107 on the fixed dual pencil L=72+8K/9. Every fixed-policy gap is affine in K, proving the intervening dual region is valid.

## Ordered branch carrier, actual masses, no cross term

Before either tie, follow the unique Bellman action, preserving *each ordered word*, its P/Q mass and multiplicity. Actual first-hit data:

A: 120 ordered prefixes; P mass 390625/5971968; Q mass 390625/20155392.
B: 12 ordered prefixes; P mass 48828125/725594112; Q mass 48828125/362797056.

For forced continuation at each tie and strict downstream policy, conditional tuples (P-error,Q-error,additional P-time,additional Q-time,number of ordered terminal suffixes) are

RA=(635/165888,10201/10368,7711/6912,1069/864,21).
RB=(63/64,1/144,9/8,13/12,5).

No ordered history can hit both ties: A already has three occurrences of symbol 0; B has zero; B has depth 12 > A's depth 10. Therefore mixed actions generate no u*s cross terms. This is a scoped BRC-style positive-rational provenance carrier; count compression is justified only for the declared iid conditional moments and common likelihood ratios, not a native X6 derivation.

## Full feasible real interval

At the Stage106 endpoint, policy chooses continue at A and Q at B with probability
s0=4106591957559179/5222400000000000.
At Stage107, u is probability of deciding P rather than continuing at A, s is probability of Q rather than continuing at B. With exact first-hit products,

eP=alpha106+x*u+e*(s-s0), eQ=alpha106+y*u+f*(s-s0),

x=-248046875/990677827584,
y=65234375/208971104256,
e=48828125/46438023168,
f=-48828125/52242776064.

Since e-f>0, error equality is equivalent to

s(u)=s0+(38521/136000)*u,
eP=eQ=alpha106+(299609375/6315571150848)*u.

The entire feasible interval is
0<=u<=u*=1115808042440821/1479206400000000<1,
s(u*)=1.
Its error increase is delta*=855824768552109707/23915605160933701189632.

The root moments at u=0:
(eP,eQ)=(alpha106,alpha106);
tP=6009214469256084569/465634429809721344;
tQ=5708989891929406961/465634429809721344.

At u=u*:
(eP,eQ)=(alpha107,alpha107);
tP=13541383133505475882195/1055100227688251523072;
tQ=805267616960628807535/65943764230515720192.

Both endpoints have tP>tQ. All moments are exactly affine along s(u), because the ordered tie cones are disjoint. Therefore tP>tQ throughout; all taken actions minimize the Bellman dual, hence tP+L*eP+K*eQ=D(root), attaining the lower bound for every real intermediate alpha.

## Sharpness and history-dependent rules

Equality with the same supporting line at any larger alpha would force (by L,K>0) both errors to equal alpha and every visited action to be a Bellman minimizer. Only A and B have ties. A full-history mixture has P-first-hit weighted averages u,s in [0,1]; all prefixes at either state have the same Q/P ratio and the same forced suffix moments. The disjoint cones make these averaged probabilities sufficient for the four root moments. Error balance then forces s=s0+(38521/136000)u, which with s<=1 forces u<=u* and alpha<=alpha107: contradiction. Compactness of finite-horizon randomized-policy space ensures optimum existence, so the support line strictly fails beyond alpha107. This does not identify the next support slope.

## Verification and next question

Locally executed PRIMARY_STAGE107.py (exact fractions; all states/gaps, pinned gap endpoints, true ordered first hits, forced suffixes, endpoints, midpoint and saturation), and separately implemented INDEPENDENT_ORDERED_STAGE107.py (top-down Bellman plus literal ordered DFS at u=0,u*/2,u*; visits respectively 1,022,896, 1,022,896, 1,022,824 nodes). Both pass. They remain author-side checks. Their full version, certificate107.json, manifest and a more detailed manuscript are in the attached author research archive; publication and code readback are separate from actually executing remote copies.

**Next scientific unit:** B saturates at s=1 before A reaches u=1. Derive the adjacent dual face in *both* multipliers (K,L), not by blindly extending L=72+8K/9. Find the next exact value segment or an exact obstruction with Bellman action-gap and root error/time certification. Preserve full branch weight provenance and no native-P000 promotion.

**Authority:** connected GitHub principal awdawmip has repository push access; native em_control_tasks failed CONTROL_QUOTA and native em_session_start was refused with STATIC_READONLY_SCOPE_DENIED (operation_sent=false). Native active owner, Researcher/CLAIM and Result admission cannot be verified. Ordinary author evidence is not a native result. Google Drive was not used to evade this denial.
