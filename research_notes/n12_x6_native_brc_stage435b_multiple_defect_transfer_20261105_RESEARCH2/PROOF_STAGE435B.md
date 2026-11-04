# Stage435-B — Multiple nonadjacent native-X6 defects: exact future quotient and transfer masses

Date: 2026-11-05 (Asia/Shanghai). Research2. Status: AUTHOR_SIDE_PROOF / EXACT_INTEGER_EXECUTED / UNREVIEWED / NOT_ADMITTED.

Scientific input frozen: global main@bf84bd7c61a2444b59b1da96be57df0e9ae47e53; Enterprise Math main@2af3fc484eb11060b69e0afc1b562bcaf5ad1419; original P000 Git blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Parent Stage434-B: research/r2-stage294b-adaptive-weak-port-20261030, commit 0e31791150f3d9524df92d401f961a97ab04614b, PROOF_STAGE434B.md. Current normative rules were independently read from main. The vector coordinates below are chart-relative signed native X6 steps, not final cell addresses.

## Population, observer and future operations

Let A=+E1, B=-E1, C=+E2 be three distinct directions of the twelve signed native X6 directions. Fix integers k>=1, n>=p+1, 0<=p, r>=1, m>=max(2k+1,n+r+2). For every size-k subset D of {2,...,m-1} with no consecutive elements form the native ordered word P(D), length m, using B precisely at indices in D and A otherwise; Q=C^n. Keep each original D as a separate provenance-bearing path, counted with positive integer multiplicity one.

The complete present observation is (m,n, endpoint(P),endpoint(Q),J_P,J_Q,K) where J is the full directed 12-by-12 adjacent-direction histogram and K counts equality at the same absolute indices up to min(m,n). Future operations hold P fixed and give Q at most p individual POPs and r APPENDs, in any legal order, with APPEND choosing any of the twelve native directions. Compare operation legality and every intermediate complete observation.

## Theorem 435.1 — Entire current observation fiber

The entire fiber specified by these observations is precisely the set of all such P(D),Q, and has size binomial(m-k-1,k). In all histories endpoint(P)=(m-2k)E1, J_P(A,A)=m-1-2k, J_P(A,B)=J_P(B,A)=k, all other J_P entries zero, endpoint(Q)=n E2, J_Q(C,C)=n-1, K=0.

Proof. For any nonempty word w,
endpoint(w)-sum_{u,v}J_w(u,v)vec(v)=vec(w_1).
The twelve distinct signed native X6 vectors make the starting label unique. For P that label is A. The only nonzero directed transitions allowed by J_P are AA, AB and BA, so each B is internal and isolated, with exactly k B labels. There is no BB edge. All remaining labels are A. Conversely every internal nonadjacent size-k defect set produces exactly the stated observation. The Q graph has only CC edges and starts C, so Q=C^n. With L=m-2 internal candidate sites, the count of nonconsecutive k-subsets is binomial(L-k+1,k)=binomial(m-k-1,k). This also proves the provenance multiplicity formula.

## Theorem 435.2 — Exact future equivalence

Put a=n-p+1, z=n+r, I={a,...,z}, w=p+r. On this entire present observation fiber,

P(D),Q and P(D'),Q have identical complete observations under every common legal future operation word **if and only if** D intersect I = D' intersect I.

Proof (sufficiency). At most p POPs can remove original Q indices, so original Q labels strictly below a remain C. Every newly appended Q position lies between a and z, independent of the operation order. Positions beyond z cannot be visited. Original C never matches either native P label A or B. Hence all K contributions that can vary with D are exactly at positions I, where P is determined by the retained intersection. All endpoint and directed-J observations of P agree by Theorem 435.1. The full observation of Q, its operation legality, and each Q transition are determined solely by the common operation word. Thus every intermediate full observation descends through the intersection.

Proof (necessity). If the intersections differ, choose i in their symmetric difference. For i<=n, perform exactly n-i+1 POPs, then APPEND(B); since i>=a these use <=p POPs. For i>n, APPEND(C) exactly i-n-1 times then APPEND(B), using <=r APPENDs. Every Q label other than the new B is C, so the final absolute-position K is exactly 1 when i belongs to D, and 0 otherwise. Both sequences are legal because n>=p+1 and i is in I. Therefore the histories are distinguished. The same argument supplies explicit finite separating certificates.

## Theorem 435.3 — Integer transfer matrix for exact class populations

For any subset S of I with no adjacent elements and |S|<=k, let M(S) be the number of legal D satisfying D intersect I=S. Set D_1(0,0)=1 and every other entry zero. For each internal original index i=2,...,m-1, let e=0/1 mean P_i=A/B and t count B labels. Given the prescribed S, permit e=1 at i in I iff i is in S, and permit e=0 iff i is not in S. Outside I both values are permitted. Apply the exact recurrence:

D_i(t,0)=D_{i-1}(t,0)+D_{i-1}(t,1) when 0 permitted, else 0;
D_i(t,1)=D_{i-1}(t-1,0) when 1 permitted, else 0.

Then M(S)=D_{m-1}(k,0)+D_{m-1}(k,1), every summand is a nonnegative integer, and sum over S M(S)=binomial(m-k-1,k). The **exact** number of future-equivalence classes is

q_F(k;m,n,p,r)=sum over nonadjacent S subset I with |S|<=k of indicator(M(S)>0).

Proof. The states record the previous letter's defect bit and the exact number of B symbols already used. A transition to B from previous B is excluded, while all other allowed transitions are present exactly once. Starting with P_1=A and ending with P_m=A makes every accepted internal bit sequence correspond bijectively to one ordered native word P(D), with no permutation factorial. Fixing the bits on I gives exactly the desired fiber class. Summing over all S partitions the original D population disjointly.

Optional equivalent exterior formula: for L=[2,a-1] and R=[z+1,m-1] of lengths l=a-2, u=m-z-1, delete the L boundary site a-1 if S includes a and it exists, and the R boundary site z+1 if S includes z. Write l_S=l-indicator(a in S and l>0) and u_S=u-indicator(z in S and u>0). Then M(S)=sum_{j=0}^{k-|S|} binomial(l_S-j+1,j) binomial(u_S-(k-|S|-j)+1,k-|S|-j), treating out-of-range binomial coefficients as zero. The two exterior intervals are separated by the fixed window, so their nonadjacency restrictions are independent.

## Corollary 435.4 — Closed formula with a sufficient exterior reservoir

If in addition a-2>=2k-1, every nonadjacent S subset I of size at most k extends to a full D: choose k-|S| nonadjacent positions in the left exterior, avoiding a-1 when S includes a. That exterior has enough sites by the stated inequality. Consequently

q_F(k,w)=sum_{j=0}^{k} binomial(w-j+1,j), with out-of-range binomial = 0.

For k=2, this is q_F(2,w)=1+w+binomial(w-1,2); for fixed k it grows as a degree-k polynomial in w (when w grows with the exterior reservoir maintained). When k>=ceil(w/2), all nonadjacent subsets of the window occur and q_F=F_{w+2} with F_1=F_2=1. The shortest fixed-length binary class code within this known observation fiber needs ceil(log2 q_F) bits. These formulae preserve the exact population M(S), not only class support.

## Explicit native separation

Set (m,n,p,r,k)=(13,6,2,2,2), Q=C^6 and compare D={5,7} with D'={6,8}. Both are members of the same 45-history complete present fiber. POP, POP, APPEND(B) makes Q=C^4 B; its final K values are 1 and 0. APPEND(C), APPEND(B) makes Q=C^7 B; its K values are 0 and 1. Every preceding complete observation follows the same declared native observer.

## Exact encoding, online reader and total computational cost

Input: fully ordered native X6 letters P,Q. Check the fiber conditions and construct endpoint/J/counts and the sorted defect positions in O(m+n) word operations; six component sums and 12x12 J counters require O(log(m+n)) bits each. The class is S=D intersect I; extracting it from the sorted defects is O(k) word operations. A succinct *class description* is its sorted list of at most k absolute indices (O(k log m) bits), or a w-bit window mask. The information-theoretic minimum *fixed-width class ID* costs ceil(log2 q_F) bits once a rank/unrank codebook for feasible S is supplied.

The transfer DP evaluates one M(S) in O(mk) integer additions and O(k) rolling integer cells. Every partial-DP count is bounded by 2^(m-2), since it enumerates a subset of all binary assignments to the m-2 internal sites. Thus H=m-1 bits is a safe uniform integer-width bound for all intermediate states; the final class masses have the potentially smaller bound ceil(log2(binomial(m-k-1,k)+1)) bits. Enumerating all N(w,k)=sum_{j=0}^k binomial(w-j+1,j) potential nonadjacent S and building an explicit (S,M(S)) codebook costs O(N(w,k) m k H) bit operations and O(q_F(w+H)+kH) bits of workspace/output, up to normal index overhead; the intrinsic output is q_F class/mass pairs. This explicit generation cost is not hidden inside an O(1) encoding claim. With a prebuilt indexed codebook, rank lookup depends on the chosen index structure; input conversion remains O(m+n).

For an online Q APPEND at absolute index i, update K by the indicator that i is in I and the appended label equals the P label encoded by S at i. For POP of current Q label at index i, subtract that same indicator. At original Q positions below a, the label is C and contributes zero. Q's endpoint, J, length and trailing stack update locally; the original C-run can be kept as a run-length count with an appended suffix stack. Thus the observer can be updated in O(1) native label comparisons per step with indexed S membership and O(log(m+n+p+r)) bit-size counters. The exact original P cannot in general be reconstructed from S alone: the M(S) exterior possibilities are intentionally aggregated. A canonical representative is recoverable by DP/backtracking and O(m) emitted characters; exact path reconstruction requires an exterior-rank repair coordinate. Retain full history whenever future operations expand beyond the declared budget.

## Verification and next step

The exact checker REPRO_STAGE435B.js uses the full twelve-direction APPEND alphabet, enumerates complete finite operation languages, compares the intermediate K traces of every original history to the class reader, checks direct future indistinguishability/separation for each tested class, compares integer transfer masses to direct nonadjacent-subset enumeration, and verifies both explicit separating words. REPRO_STAGE435B_EXECUTED.json records the actual executed result and finite domains. Infinite-parameter assertions above are supported by the written bijection and future-witness proof.

Stage436-B: develop a ranked/unranked *implicit* feasible-class coder with polynomial preprocessing (rather than explicit enumeration of q_F classes), and test whether the transfer automaton admits a direct future-observer composition across two mutable native paths. Keep exact population/provenance and all conversion/bit costs.
