# R5 — Complete two-parameter classification of a time-aware, two-law reconvergent stopping family

**Date:** 2026-11-01 Asia/Shanghai. **Status:** AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY. This is an auxiliary stopping-model theorem, not an accepted native-X6 result or a solution of the unrestricted R5 mother question.

## Frozen science and provenance

GLOBAL_KNOWLEDGE_V1 canonical main at a82c707ab85cb527845e1fff1f69aaaf317a52c4 (the original P000 Git blob SHA1 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc agrees with its startup projection), and Enterprise Math canonical main at 4d349d63a10612d9e196f49791bd5946c6dd9bba. Current AGENTS, P000, ACTIVE Heartbeat World and residual-fidelity records and portable research operations were read under these fixed scientific inputs.

Predecessor: PR #1663, commit 5640dd19d27b0911d6ede531f60ee4aa6237aa9a, research_notes/brc_r5_revisited_coarse_key_curved_hull_20261101_t0640/RESEARCH.md and NEXT_TASK.md. The predecessor proved a curved convex hull for a genuinely *repeated coarse key*. Here decisions instead use the actual strictly increasing **(time, likelihood ratio)** keys. This distinction determines whether multi-affine deterministic-corner methods are valid.

## Exact model and BRC observer contract

Under both probability laws P and Q, an origin A or B has initial probability 1/2, initial likelihood ratio 1, and an observable stop/continue decision at integer time 1. FULL may distinguish origin; seedless LR may use only (time, exact dP/dQ), so must use a common time-1 stop probability. A time-1 stop declares P.

Conditional on continuing, origin i with parameter alpha_i produces a low or high signal at time 2. Set alpha_A=a, alpha_B=b, with 0<a,b<1:

| Event | Q conditional mass | P conditional mass | time-2 likelihood ratio |
| --- | ---: | ---: | ---: |
| low | alpha_i | alpha_i/2 | 1/2 |
| high | 1-alpha_i | 1-alpha_i/2 | (1-alpha_i/2)/(1-alpha_i) |

Every P/Q transition probability is strictly positive and the two probabilities in each law sum to one. At time 2, low stopping declares P and high stopping declares Q; continuing to time 3 declares the opposite (Q on low; P on high). No stopping decisions remain at time 3. The same decision protocol applies under both probability measures.

Both low histories reconverge at the genuine LR key (2,1/2). If a!=b, the high likelihood ratios exceed 1 and are distinct because (1-x/2)/(1-x) increases strictly on (0,1). The four seedless LR keys are (1,1), (2,1/2), (2,r_A_high), (2,r_B_high); FULL has six origin-labelled keys. When a=b, high keys also coincide, leaving only three LR keys. Every path uses the time-1 key and at most one time-2 key, so it cannot revisit the same (time,LR) key. All behavioral coins are drawn anew; no persistent seed is allowed. Consequently each P/Q terminal mass and each observer is multi-affine in local stop probabilities: the actual observer convex hull is exactly the hull of deterministic policy observers.

The BRC carrier is a positive, source-labelled four-leaf P/Q path-flow ledger (A-low, A-high, B-low, B-high), preserving source, signal, decision port and time until the declared readout. This is not signed amplitude or native X6 physics. Define the four original-form observer coordinates O=(e_P,e_Q,T_P,T_Q), with e_P=P(declare Q), e_Q=Q(declare P) and T_P,T_Q the expected terminal times. Horizon is three discrete decision times; terminal decision logic is fixed as above. Source i conditional continuation masses before time-1 control are P_low=alpha_i/4, Q_low=alpha_i/2, P_high=1/2-alpha_i/4, Q_high=1/2-alpha_i/2.

## Theorem: complete all-real open-square classification

For **all real** a,b in (0,1):

**(I) If a!=b:** the LR four-observer hull has affine rank 4 and is strictly separated from FULL. Put theta=(a+b)/2 and H_theta(O)=-(1+theta)e_Q-T_Q. Then

  max_FULL H_theta - max_LR H_theta = |a-b|/4 > 0.

There is a deterministic FULL witness with L-infinity distance at least

  |a-b| / [4(2+theta)]

from every LR real-policy observer and from the entire LR convex hull.

**(II) If a=b:** FULL and LR have exactly the **same actual real observer image**, which is a convex polytope of affine rank exactly 3 (therefore the hulls also coincide).

No point in this complete two-parameter family has both LR affine rank 4 and equal FULL/LR observer convex hulls. This does not exclude other model topologies, error responses, or the original unconstrained R5 mother problem.

### Proof of (I): an explicit all-signed Bellman support gap

Minimize C_theta(O)=(1+theta)e_Q+T_Q, i.e. maximize H_theta. Under Q, a low time-2 stop declares P and contributes cost (3+theta) per unit Q mass; a low continuation to time 3 declares Q and costs 3. Thus low always continues when theta>0. A high time-2 stop declares Q and costs 2 per unit Q mass; high continuation to time 3 declares P and costs 4+theta. Thus high always stops. Both optimal time-2 choices agree across sources, so the shared low LR key imposes no additional restriction on this support direction.

For one source with initial Q mass 1/2, stopping at time 1 costs (2+theta)/2=1+theta/2. Continuing then making the optimal time-2 choices costs

  3(alpha/2)+2((1-alpha)/2)=1+alpha/2.

FULL therefore chooses independently for the two origins, giving

  min_FULL C_theta
    = 2 + [min(a,theta)+min(b,theta)]/2
    = 2 + [min(a,b)+theta]/2,

the last identity holding because theta lies between a and b. Under LR, the time-1 action must be the same for A/B, so its optimum is at one of two common deterministic actions (or their indifferent mixtures):

  min_LR C_theta
    = min{ 2+theta, 2+(a+b)/2 }
    = 2+theta.

Subtracting yields the **exact all-real support difference** |a-b|/4. This uses a signed direction with zero e_P and T_P coefficients; it is not a finite sweep or positive-only support comparison. For any deterministic FULL policy attaining its minimum, the dual norm inequality gives distance >= gap / ||H_theta||_1 = |a-b|/[4(2+theta)] to the entire LR hull. Hence the genuine source-dependent Q kernels at time 1 carry an observable future residual; their time-1 likelihood quotient is not predictively lumpable for the declared continuation language.

### Proof of LR rank 4

For a!=b, take the LR policy with all four stop bits zero and the four policies obtained by individually changing one bit to one. Form the 4x4 matrix of observer differences, with columns e_P,e_Q,T_P,T_Q. Exact expansion gives

  det M(a,b) = (b^2-a^2)/8.

Since a,b are strictly positive and unequal, this determinant is nonzero. In particular LR affine rank is exactly four. The accompanying standalone Fraction verifier provides a finite *symbolic-identity certificate*: every M entry is affine in a,b, so the determinant-minus-formula is a polynomial of degree <=4 separately in each variable. Exact equality at a 5-by-5 grid of distinct rational a- and b-values forces the bivariate polynomial to vanish identically (univariate root counting first in a for each fixed b, then in b for each coefficient). This proves the formula over all real a,b without assuming numerical interpolation or an external CAS.

### Proof of (II): exact real-policy Markovization and rank 3

Suppose a=b=alpha. Given any FULL real stop parameters p_A,p_B and q_Alo,q_Blo,q_Ahi,q_Bhi, let s=(1-p_A)+(1-p_B) and set

  p=(p_A+p_B)/2,

  q_lo=((1-p_A)q_Alo+(1-p_B)q_Blo)/s,

  q_hi=((1-p_A)q_Ahi+(1-p_B)q_Bhi)/s.

If s=0 choose either q arbitrarily, since no time-2 node is reached. These quantities are in [0,1]. Since Q/P priors match across origins and both conditional kernels coincide when a=b, this source-aggregated LR policy exactly reproduces every P and Q time/branch/action/decision terminal mass of the FULL policy. All four observers therefore agree. Conversely LR policies are a subset of FULL, proving **actual image equality** for all real behavioral parameters.

The observer is affine in the three aggregate action flows p, f_lo=(1-p)q_lo and f_hi=(1-p)q_hi. Their feasible set is the convex polytope 0<=p<=1, 0<=f_lo,f_hi<=1-p, so the common image is itself convex and has affine rank at most 3. The three LR single-bit observer differences for (p,q_lo,q_hi) from base (0,0,0), using columns (e_P,e_Q,T_P), have determinant alpha(4-alpha)/4>0, establishing rank exactly 3.

## Exact rational certificate and execution scope

For (a,b)=(1/4,1/2), theta=3/8 and legitimate distinct keys (1,1),(2,1/2),(2,7/6),(2,3/2), a FULL policy that continues A and stops B at time 1, continues low on A, and stops high on A produces

  O_FULL=(1/2,1/2,25/16,13/8).

Exact extremal costs are min_FULL C_theta=37/16 and min_LR C_theta=19/8, giving support gap 1/16 and a certified L-infinity distance lower bound 1/38. The LR rank-four determinant is 3/128.

VERIFY.py was **actually run** using standard-library fractions.Fraction: 25 exact polynomial interpolation nodes, 49 off-diagonal rational test pairs each enumerating all 64 FULL and 16 LR deterministic policies, and 46,875 exact diagonal FULL-to-LR real-behavior Markovization comparisons. EXACT_OUTPUT.txt records the literal run output. The all-real claims are proved by the preceding Bellman formula, explicit real Markovization and exact polynomial degree/interpolation argument; test samples alone are not promoted to universal statements.

## Permissions, scope, and next frontier

The native service in this run returned research_authority_granted=false, executor_binding_configured=false, control CODE_REVIEW_REQUIRED; an Owner inventory read returned CONTROL_QUOTA. Thus no active Source Owner, authenticated CLAIM, frozen Result, independent Driver review or theorem admission is claimed. This report is author-side portable evidence saved to PR #1663, not a state-machine bypass. No P000 or protected worldview mutation. The BRC interface is applied at the positive source-labelled flow/observer quotient and provenance-residual level; no unrelated BRC executable is claimed to have been run. There is no native six-dimensional embedding or third-coordinate preservation certificate.

Next: vary the two-law kernels and termination protocol or add a minimal genuine second reconvergence while keeping honest time-LR keys. Search first for rank4 and all-signed full hull equality by exact finite rational primal/Farkas certificates; only then attempt real-policy nonmembership by a valid semialgebraic proof. A recurring key would require a different, non-corner method.
