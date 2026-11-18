# R5 — Exact minimum static choose-one optimum-source output alphabet

Date: 2026-11-16 (Asia/Shanghai). Frozen pin 435e77af0d180eac32bd1f9c4c464bc4010b7551. Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.

## Question and inherited input

Continue SHARED_SOURCE_HELLY_AND_ROBUST_CONTROLLER_THEOREM.md in this directory, reusing the prior exact cycle-of-triangles indexed-center model and its source-labeled repair certificates. k>=3; u is the length-k binary *unavailability* mask of named spine helpers; q(u)=sum_(i mod k) u_i*u_(i+1); exact minimum single-a old library size is 5k+q(u). For a nonempty family of masks, a common *individually optimal* labeled old library exists exactly when q(bitwise_OR masks)=q(each member).

This note concerns a **static choose-one output**: a deterministic lookup which receives mask u and outputs one source-labelled old library whose cardinality is minimum for that u. Multiple masks may share an output library, if it is optimal for each. What is the smallest possible number M_k of **distinct library outputs** needed to serve all 2^k masks? This is an output-alphabet question, not yet the number of states of a transition-preserving controller.

## Theorem — Exact answer and tribonacci recurrence

For every k>=3,

  M_k = #{u in {0,1}^k : u contains no cyclic run 000}.

The count satisfies

  M_1=1, M_2=3, M_3=7,
  M_k=M_(k-1)+M_(k-2)+M_(k-3) for k>=4.

In particular M_3,...,M_12 =
7, 11, 21, 39, 71, 131, 241, 443, 815, 1499.

The asymptotic exponential base is the positive real root of x^3=x^2+x+1, approximately 1.839286755, compared with 2^k full source-spectrum states. The sequence is the cyclic binary-word count with forbidden triple-zero word, not a new arithmetic sequence or a native X6 identity.

## Proof of optimizer-alphabet minimum

For every mask u define its q-fiber F_q={v:q(v)=q(u)}, and use the Boolean partial order u<=v for inclusion of unavailable positions. q is monotone under that order. Call u **fiber-maximal** if no strict supermask v>u has q(v)=q(u).

(1) Every mask u has a fiber-maximal supermask w>=u with q(w)=q(u). This is obtained by repeatedly turning an available position into an unavailable position *only if* doing so leaves q unchanged; the process stops in at most k flips. Monotonicity ensures a nonmaximal state has some admissible one-bit extension: if w>u and q(w)=q(u), every intermediate one-bit flip along a chain from u to w also has the same q value.

(2) Each fiber-maximal mask w has a canonical source-labelled optimum library L(w) containing the paired one-hot helper sources for all available spine vertices. If u<=w with equal q, every source available at w is available at u and the library cardinality is 5k+q(w)=5k+q(u). So L(w) is individually optimal for u. Choose one maximal extension for each u and return L(w). This uses no more than one output per fiber-maximal mask.

(3) Distinct fiber-maximal masks w,z cannot use the same individually optimal library. Indeed, the exact common-source theorem would require q(w OR z)=q(w)=q(z). If q(w)!=q(z), impossible immediately. If q values coincide, w OR z strictly exceeds at least one of the distinct incomparable fiber maxima, or one is a strict supermask of the other (contrary to maximality in the same fiber); monotonicity and maximality imply q(w OR z)>q(w) or >q(z). Contradiction. Thus each maximal mask requires its own distinct output. Combined with (2), the minimum number of output libraries is exactly the number of fiber-maximal masks.

(4) A zero bit u_i can be flipped from 0 to 1 without increasing q precisely when both neighbors u_(i-1)=u_(i+1)=0. Therefore u is fiber-maximal if and only if every zero has at least one neighboring one, equivalently no three consecutive cyclic zero bits occur. This proves the combinatorial formula.

## Proof of recurrence

Use the de Bruijn transition matrix T indexed by ordered pairs (00,01,10,11); the allowed triple transitions are 00->01, 01->10 or 11, 10->00 or 01, and 11->10 or 11. Explicitly

  T = [[0,1,0,0],
       [0,0,1,1],
       [1,1,0,0],
       [0,0,1,1]].

For k>=1 each closed k-step path uniquely specifies a labelled binary cyclic word of length k avoiding 000, and conversely. The count equals tr(T^k). Direct calculation gives characteristic polynomial x^4-x^3-x^2-x, hence T^4=T^3+T^2+T by Cayley-Hamilton. Taking traces after multiplication by T^(k-4) proves the recurrence for k>=4. Initial traces are tr(T)=1, tr(T^2)=3, tr(T^3)=7. The k>=3 assertions follow.

## Verification and boundary

A standard-library checker independently enumerates all masks for k=3,...,12 (8,184 masks); constructs a q-preserving maximal extension for each; verifies distinct maxima have no common individually optimal library via the precise q(OR) criterion (1,593,306 maximal-mask pairs); and checks the recurrence. Observed PASS_R5_STATIC_OPTIMUM_ALPHABET_TRIBONACCI. This is an exact finite cross-check, supplementary to the universal proof above. Independent review remains pending.

The result answers the static choose-one output-alphabet minimization. **Next**: incorporate named Set transition compatibility and compute the truly minimal deterministic adaptive choose-one witness transducer, for each control subset J. This requires a transition-stable partition, not just a minimum static output alphabet. Compare the size with full Opt source-spectrum 2^k and the robust reserve 2^(k-|J|) counts.

P000/Heartbeat World remain unchanged; this auxiliary suffix graph is not a native X6 coordinate collapse. Historical contribution: EM-DIRECT-B78E55 / RA-33C87C2B703418F0706695E9, not a current CLAIM.
