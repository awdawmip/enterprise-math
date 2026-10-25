# N=14 auxiliary iid Stage121: exact next affine optimal interval

Status: **AUTHOR_EXACT_COMPUTATION_ASSISTED_PROOF**. This theorem concerns only the declared external finite iid stopping problem, not P000/native X6, and has no independently admitted Research Driver Result.

## Statement and inherited exact frontier

Let P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), N=14, and let all possibly randomized policies depend on the full ordered ternary history. Write eP=P(decide Q), eQ=Q(decide P), tP=E_P(tau), tQ=E_Q(tau), and V14(alpha)=inf max(tP,tQ) over eP,eQ<=alpha.

From the published author-verified Stage120,
alpha120=2573764724900518487425/7411551152237344456704,
V120=378361860665073597077285/29646204608949377826816.

Define K121=320913819/414584, L121=37979256/51823 and S121=K121+L121=624747867/414584.

**Theorem (all real parameters):** for EVERY real 0<=delta<=eta121=48771920875/25734552611935223808,

    V14(alpha120+delta) = V120 - (624747867/414584)*delta.

Exact new endpoint:
alpha121=2573764738946831699425/7411551152237344456704,
V121=378361775997993165503285/29646204608949377826816.
The support line is right-sharp: for every alpha>alpha121, V14(alpha)>H121(0)-S121*alpha.

## Universal ordered-history dual

At each count state (n,a,b), n<=14, ratio Q(prefix)/P(prefix)=2^(a+b)/3^a. The backward Bellman value H is the minimum among K*ratio (declare P), L (declare Q), and when n<14 the continuation cost 1+(1/8)H(n+1,a+1,b)+(1/24)H(n+1,a,b+1)+(5/6)H(n+1,a,b). There are exactly 680 count states. Complete exact Fraction comparison gives 1238 strictly positive nonchosen action gaps, no negative gaps, and only the two ties:

* A=(9,3,0), declare P versus continue;
* G=(13,6,4), declare Q versus continue.

Minimum strictly positive gap: 110828719979/9903529525248.
Root H121(0)=1521827441858168590625795/2838890947768139907072 = V120+S121*alpha120.

Bellman induction can be applied to each literal ordered prefix: at that prefix the ratio and iid conditional suffix depend only on counts. Thus **for every ordered-history randomized policy** (not just count-based policies),

    H121(0) <= tP + L121*eP + K121*eQ <= max(tP,tQ)+S121*alpha.

It follows that V14(alpha)>=H121(0)-S121*alpha.

## Constructed attaining strategy and BRC-style path evidence

At A declare P with probability y (otherwise continue); at G declare Q with probability z (otherwise continue). At every other state select its unique Bellman minimizer. D=(9,1,2) is strictly declare Q, already saturated after Stage120. The actual first-hit ordered histories are:

| site | word count | P first-hit mass | Q first-hit mass |
|---|---:|---:|---:|
| A=(9,3,0) | 84 | 109375/1990656 | 109375/6718464 |
| G=(13,6,4) | 15058 | 941125/9393093476352 | 941125/6687075336192 |

The A and G cones are disjoint: reaching G from A would require three additional zeros and four additional ones in only four observations. All four declared observers are therefore affine in the two probabilities, with no mixed yz term.

Write M=(eP,eQ,tP,tQ). With both sites continuing M(y,z)=M00+y*dA+z*dG, exactly:

M00=(608842883532273911/1752976676930715648,
13930229812525/40122452017152,
2799712788061487261/219122084616339456,
13506681488747/1114512556032);

dA=(-1921609375/7925422620672,
259765625/835884417024,
-20758609375/330225942528,
-1476453125/69657034752);

dG=(941125/75144747810816,
-941125/80244904034304,
-941125/9393093476352,
-941125/6687075336192).

The exact equality eP=eQ forces

    y(z)=665568609544933/2909391744000000 + (911009/20781369600)*z.

For every real 0<=z<=1 both y(z) and z lie in [0,1], and y(0) equals the preceding Stage120 boundary probability. In this interval eP=eQ=alpha120+eta121*z and tP=V120-S121*eta121*z. Exact time-dominance margins tP-tQ at z=0 and z=1 respectively equal
19225817524111600585621/29646204608949377826816 and
19225764576247514675621/29646204608949377826816;
both are positive, hence positivity holds for every real z in the interval.

Every chosen action is Bellman minimizing. With both errors equal the allowed alpha and tP>tQ, the dual lower bound is attained everywhere on the displayed interval.

## Sharpness

The finite randomized ordered-history policy domain is compact, so an optimum exists. If the same positive-multiplier support were attained for some alpha>alpha121, both errors would have to equal alpha and all positively reached decisions would have to minimize their Bellman action costs. Only A and G have such tie flexibility. On each count-state fiber, possible word-specific mixtures can be averaged without altering these four observables because the iid suffix laws and likelihood ratio are constant on the fiber. Their first-hit cones are disjoint. Hence all attaining policies are observer-equivalent to (y,z) in [0,1]^2 satisfying the displayed balance law. Balanced alpha strictly increases with z; z<=1 implies alpha<=alpha121, a contradiction.

## Execution and authority distinctions

Author executed standard-library exact Fraction bottom-up Bellman and a separate literal ordered-word DFS with integer weights P=(3,1,20)/24, Q=(1,1,10)/12. Four DFS corner visit counts for (y,z)=(0,0),(0,1),(1,0),(1,1) were 885985,840811,880945,835771; every corner's four moments matched the recurrence exactly, with zero mixed difference. Actual local full source SHA256 82447fa5001a1bef6a1c29bba24a04be75e82843874bcc3599674e5753992375; local JSON certificate SHA256 837d82f2a749a0954507426b6f2d5c6203e87d37f00fc76df61874c8e1b13491. Published portable checker is a source-equivalent reproduction, not falsely described as the identical executed local script or remotely executed code.

BRC resolution: REUSE_APPLIED for a positive-rational, multiplicity- and provenance-preserving ordered-history carrier and only an iid/four-observer-specific count quotient. No P000/native-X6 observer-preserving map is asserted. No independent Research Driver review, native owner verification, CLAIM, frozen Result, Foundation admission or physical model theorem is claimed. Native task inventory responded CONTROL_QUOTA and native own-session creation was denied STATIC_READONLY_SCOPE_DENIED, operation_sent=false.

Read pins for this run: GLOBAL_KNOWLEDGE_V1 canonical main@3b69d2cbad6ee388c6643689eae5d5fcd1a8a4ff; previous Stage120 read from EM main@526cdeb461e9297c7ada9473a162bf1220ecd73c. P000 canonical blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc unchanged. The separate Stage122 candidate in NEXT_TASK_PACKET_122.md remains a dual candidate, not a proved primal interval.
