# Signed scalar gaps: exact refinement and a three-call special case

Status: **AUTHOR_SYMBOLIC_RESULT / SHARED_CONTEXT / NOT_ADMITTED**. No new scientific execution, professional query, or remote write is part of this note. It refines the frozen `FINITE_FEEDBACK_AND_MULTIWINDOW.md`, SHA-256 `00cf4dd1de1a0c019a0c2b19f8504992269b4f0bfd4cd1a480eb20edb2af7b0e`, without changing that file. All signs and residual coordinates are retained.

The positive result is that a position with a certified scalar operator can be removed from the matrix contraction even when that scalar is -1. Its sign goes into an exact signed pair counter. For a continuous scalar gap with exactly one negative bit, at any bit position, that counter reduces to three calls to the existing actual typed floor-moment interface, for arbitrary paid period R. Arbitrary masks also admit the existing small-odd-part aggregation specialized to scalars. Neither result makes arbitrary Walsh sums on arithmetic progressions free.

## 1. Source contract and sign extraction

Use the frozen note's actual order, work-address convention and complete pure seed:

    O_j=(-1)^h_j T_j,
    U(n)=O_(i-1)^n_(i-1) ... O_0^n_0 e_0,
    n=sum_j n_j 2^(i-1-j),
    Gamma_h(z)=4^-i sum_(m-n=r mod R) U(n)U(m)^T.             (1)

The exact order R=ord_N(b_depth) and address b_depth^r=z are separately obtained and verified. No factor, order or target logarithm is introduced as a hidden free input.

The new counting source reused here is frozen adaptive `nonzero_structure/typed_floor_moments.py`, SHA-256 `633502c9b484e60e5dc5fcf6edd0420f12d52c33c43e88851b9e1e6465ea94a2`, with the adjacent proof `ACTIVE_WINDOW_FLOOR_MOMENTS.md`, SHA-256 `20a93f15f241f9c3220c031032cc2af697e4d4a448669f5b637396c1a05529d4`. Both are at EM commit `c0f04346c520fddc8016c86227b3b6cc2e9f30f6`, prefix `research_notes/directed_recovery/20260927_C6438C/qft_adaptive/`. The actual public methods `interval_count`, `weighted_affine_count`, and `window_weight` were read; they count integers using admitted typed arithmetic and do not certify a modular order.

The scalar small-odd-part specialization below reuses `aggregation_theory/PERIOD_AGGREGATION.md`, SHA-256 `be20eb9409b1b250edfe9e0bc83fda9701253a71add4f98e3ccea8325d2302be`, EM `8e2f54ce5581636b9169845a54f018c25d00b165`, prefix `research_notes/directed_recovery/20260927_C6438C/qft_carry_execution/`. Its q-state/high-block and two-carry/low-block structure is prior work; this note does not claim a new order-discovery algorithm.

For fixed public h, the scalar factors commute with every actual matrix, so

    U(n)=(-1)^(sum_j h_j n_j)
         T_(i-1)^n_(i-1) ... T_0^n_0 e_0.                    (2)

This pulls out only scalar signs. It never commutes any pair of feedback matrices. Selected feedback words and scalar certificates must remain bound to the same committed history, full column source, complete carrier and actual gate order.

## 2. Scalar-gap lemma

Let F be a set of positions whose complete operators are certified as

    T_j=tau_j I, tau_j in {+1,-1}, j in F.

Equivalently O_j=sigma_j I, with sigma_j=(-1)^h_j tau_j. An exact reachable-subspace version would require its own common invariant-subspace and metric certificate; mere agreement on one vector is insufficient here. Orthogonality permits no other real scalar than +/-1.

For the free-bit address beta with arbitrary bits at F and zeros elsewhere, define

    chi(beta)=product_(j in F) sigma_j^(beta_j),
    K_h(rho)=sum_(beta'-beta=rho mod R) chi(beta)chi(beta').   (3)

This is a signed integer, not a nonnegative number of pairs. If j in F has physical address weight w=2^(i-1-j), adding that free bit updates its counter by

    k_new(rho)=2k_old(rho)
                 +sigma_j[k_old(rho-w)+k_old(rho+w)],        (4)
    k_initial(rho)=1 if rho=0, otherwise 0.

Proof: the bit pair (0,0) or (1,1) has sign +1 and difference 0; the pairs (0,1) and (1,0) have sign sigma_j and difference +/-w. All pairs are retained exactly once. Processing order in (4) is immaterial because only scalar factors have been extracted. A dense realization costs O(|F|R) scalar operations and O(R) entries, before improved special cases.

Useful checks, including what must not be claimed, are

    K_h(-rho)=K_h(rho),
    sum_rho K_h(rho)=product_(j in F)(2+2sigma_j),
    |K_h(rho)|<=K_h(0)<=4^|F|.                              (5)

To prove the last inequality, put a_s=sum_(beta=s mod R) chi(beta). Then K_h(rho)=sum_s a_s a_(s+rho), so Cauchy--Schwarz applies and K_h(0)=sum_s a_s^2. This also proves that the cyclic autocorrelation kernel is positive semidefinite, although individual off-diagonal entries can be negative. For a one-bit gap with sign -1, weight 1, and R=3, direct symbolic enumeration gives K(0)=2 and K(1)=K(2)=-1. No positivity guard may reject these legitimate entries.

If any sigma is negative, the total signed sum in (5) is zero. That is not a zero array or an invalid probability distribution: K is an intermediate correlation coefficient, not a distribution. At R=1 it does force K(0)=0, representing exact destructive interference. No normalization by sum K is defined or needed.

## 3. Multiwindow normalization and composition remain exact

Enclose all positions outside F in ordered active windows I_a of widths ell_a, leaving G=|F| free positions; positions certified scalar may optionally remain inside a window. Let V_a be the physical weight of the window's last bit. Define A_a(x) from the actual O_j, in their original temporal order, and

    C_(a,d)[X]=4^(-ell_a)
      sum_(0<=x,x+d<2^ell_a) A_a(x) X A_a(x+d)^T.             (6)

Then the frozen formula generalizes exactly to

    Gamma_h(z)=4^-G sum_(d_1,...,d_b)
      K_h(r-sum_a V_a d_a)
      (C_(b,d_b) o ... o C_(1,d_1))[e_0e_0^T].              (7)

In the expansion of (1), free scalar bits contribute chi(beta)chi(beta'), while active windows contribute the maps (6). Factoring these finite sums proves (7). The free sign does not remove the raw factor 4^-G. In particular a negative scalar bit still represents two preparation choices on each side of the outer product.

One can instead form each A_a from T_j and place the corresponding local Walsh signs explicitly inside (6); that is algebraically identical to retaining O_j there. Mixing both conventions would double-count signs. The correct negative-displacement identity remains

    C_(a,-d)[X]=(C_(a,d)[X^T])^T,

including for asymmetric intermediate matrices. No seeded-window matrix product, implicit transpose shortcut, or partial residual projection is allowed.

After K_h is supplied, the same conservative bound applies: at most product_a(2^(ell_a+1)-1) displacement tuples and O(sum ell_a) complete carry layers per tuple, with all D^2 entries, actual word actions and exact bit costs charged. This lemma removes scalar-only positions from those matrix layers; it does not make the scalar modular query free.

## 4. Arbitrary masks with a paid small odd part

The general signed counter has a finite state representation even for punctured free-bit sets, but its dimension is not automatically poly(log R). Write the certified R=2^s q, q odd, and first suppose s<=i. In this section bit positions are indexed from the least significant end. A bit outside F is fixed to zero on both sides.

Write beta=2^s A+u, beta'=2^s B+v, and r=r_0+2^s r_H with 0<=r_0<2^s. The full congruence is equivalent to

    u+r_0=v+2^s c, c in {0,1},
    B-A=r_H+c mod q.                                       (8)

Construct q scalar high-block accumulators H_e. Begin with H_0=1 and all other entries zero. Process numerical bit positions i-1,...,s, in descending order. If a position is free, choose x,y in {0,1}; otherwise choose only x=y=0. With its free sign sigma, add

    sigma^(x+y) H_e to H_new(2e+y-x mod q).                 (9)

The sign is 1 at fixed zero positions. This is the signed high-address pair sum classified by B-A mod q; it uses fresh accumulators. It is scalar specialization of the existing period aggregator, not a matrix reordering.

For the low block, initialize two high-boundary carry values

    X_c=H_(r_H+c mod q), c=0,1.

For k=s-1,...,0, with known target bit r_k, reverse the binary carry constraint

    x+r_k+c_k=y+2c_(k+1).                                  (10)

For each allowed pair x,y, add sigma_k^(x+y) X_(c_(k+1)) to the fresh state at c_k. Return X_0 after the last bit. Every low pair has exactly one carry path, so the procedure returns exactly K_h(r). In particular c_s is not forced to zero; modular overflow is retained through the two high seeds. If the high residues coincide, the two equal-valued seeds are still distinct carry states. A forward scalar version may instead merge them by summing when it discards the carry; it must not duplicate an already merged value.

The conditional bound is

    O(q(i-s)+s) scalar transitions, O(q) stored integers.    (11)

Their magnitudes have at most 2G+1 bits, apart from bounded summation overhead. Coefficient signs may cancel and are retained exactly. At s=0 use just H_r with no duplicated low seed. At q=1 all high words are scalar; the method takes O(i) steps for an arbitrary mask. At s=i the high block is empty with H_0=1. If s>i, then R>=2^(i+1); at most one integer displacement in [-(2^i-1),2^i-1] is congruent to r. Select r, r-R, or none, and use the ordinary two-carry signed coefficient with no wraparound and both endpoint carries zero. This costs O(i) scalar transitions after the comparison, avoiding padding to a huge fictitious matrix state.

More generally, if R>=2^i, at most two such displacements exist. Each can be evaluated by a two-carry scalar digit recursion with the specified fixed/free bits and signs, in O(i) transitions. Negative displacement has the same scalar coefficient as positive displacement by (5). This is another paid-address special case, not a discovery algorithm.

Thus a verified power-of-two period, or an odd part q bounded by a polynomial in the input bit width, gives a polynomial-bit scalar counter for every mask. For a general large odd q the q-state part remains expensive. This is precisely where the existing small-odd-part limitation reappears; the symbol-generation automaton for a Walsh mask does not eliminate the modular-residue state.

## 5. One negative bit in a continuous gap: three existing floor queries

This special case removes dependence on the size of q, while restricting the mask. Suppose the scalar-free positions form one contiguous block of g>=1 numerical bits with physical unit V, a power of two. Their addresses are beta=Vx, 0<=x<2^g. All signs are +1 except numerical bit k, 0<=k<g, whose sign is -1. The desired coefficient is

    K(rho)=sum_(V(y-x)=rho mod R) (-1)^(bit_k(x)+bit_k(y)).  (12)

Reduce the physical stride, charging the exact arithmetic. Put d_0=gcd(V,R). If d_0 does not divide rho, K=0. Otherwise put R'=R/d_0 and choose the unique residue r' satisfying

    (V/d_0) r' = rho/d_0 mod R'.                            (13)

When R'=1 define r'=0 without requesting an inverse modulo one. For R'>1 the inverse exists and can be obtained by typed Euclid. For the dyadic V, its gcd with R is also directly certified by the 2-adic valuation; it is not an uncharged factorization oracle.

Set U=2^k and H=2^(g-k-1). Decompose

    x=2U A+U e+v,
    0<=A<H, e in {0,1}, 0<=v<U.

Define the existing unsigned weight

    J_delta = window_weight(H,U,2,R',r',delta),
    delta in {-1,0,1}.                                    (14)

This interface counts the pairs (A,v),(A',v') with

    2U(A'-A)+(v'-v)=r'-U delta mod R'.

The bit pairs e=e' contribute two copies of J_0 with sign +1. The pairs (e,e')=(0,1) and (1,0) contribute -J_1 and -J_-1. Therefore

    K(rho)=2J_0-J_1-J_-1.                                  (15)

This proves the formula for every g,k,R,V,rho, including the lowest and highest sign bit, a nonunit physical stride, R'=1, and negative signed output. All three displacements obey the existing interface's strict condition -2<delta<2. The existing `window_weight` values remain nonnegative counts. Only the new outer combination is signed; its validator must not copy that method's `answer>=0` condition.

The existing proof evaluates each J_delta with a constant number of simultaneous degree-three Euclidean floor-moment systems in O(log(R'+1)) arithmetic stages. The argument integers have polynomial bit length in g+log V+log(R+1). Hence three calls plus a typed gcd/inverse and signed additions give an explicit polynomial-bit algorithm for this one-negative-bit family, without enumerating R, x, or the modular aliases. This is a conditional integer-observer result; native-source admission and typed receipts are still required for an actual run.

If there are no negative bits, the same stride reduction leaves the ordinary `interval_count(2^g,R',r')`. A second negative bit at an arbitrary position generally leaves three unsigned subintervals after its choices are fixed; the current degree-three single-window formula does not automatically evaluate that new modular geometry. Nor does computing individual gap kernels cheaply make arbitrary convolutions of many gaps cheap. Formula (15) is the precise limited family proved here.

The smallest new implementation is therefore a wrapper that validates a single contiguous scalar gap and its one-negative-bit mask, records (13), calls the frozen `window_weight` three times, and emits (15) with signed arithmetic evidence. Its raw contribution to (7) is still scaled by 4^-g, not 4^-(g-1). The eliminated bit has not disappeared from the two preparation sums.

## 6. Reassessment of the determinant argument and C=3 example

The frozen determinant observation remains correct: on the complete odd D=61 carrier with T_j in SO(D), det(O_j)=(-1)^h_j, so every one bit gives O_j!=I. It only excludes an unsigned full-identity premise. It does **not** force a non-scalar matrix operation: when T_j=I and h_j=1, O_j=-I is precisely a signed scalar gap. Therefore the earlier determinant obstruction is not a lower bound for the refined method.

Indeed, for odd D, -I has determinant -1, so a scalar T_j in SO(D) can only be +I. This makes the actual SO-family test simpler: certify T_j=I and retain the public sign (-1)^h_j. The broader +/-I formulation also handles other certified dimensions or word families. A planar -I on only two coordinates is not full-carrier -I; it cannot be removed without an appropriate invariant-subspace proof.

For the actual C=3 bank from the frozen note, W_2=Q and W_m=I for m>=3, the exact feedback is

    T_j=Q^(h_(j-1)), h_-1=0.

Since Q is not scalar on the complete carrier, the genuine matrix-active positions after extracting signs are exactly

    A_matrix={j:1<=j<i and h_(j-1)=1}.                     (16)

The structural envelope for a general first-identity cutoff C correspondingly improves to the union of [c+1,c+C-2] over prior one positions, with endpoints clipped to the prefix, plus any positions lacking a scalar certificate for other reasons. The old immediate readout-sign endpoint c is no longer a matrix requirement. Cancellation can still shrink the envelope only after exact certification.

On the same easy family N=5*3^k, a=2, default t, and 2^i<=3^(k-1), the frozen alias-free proof makes h_0,...,h_(i-1) independent fair bits for any actual orthogonal bank. Let W be the number of ones among the first i-1 history bits. Then |A_matrix|=W, E W=(i-1)/2 and Var W=(i-1)/4. For i>1,

    Pr[|A_matrix|<(i-1)/4] <= min(1,4/(i-1)).               (17)

Matrix-active components are runs of ones in that shifted prefix. For m=floor((i-1)/2)>0, each independent history pair `01` creates a distinct matrix-component start. Their sum Y has mean m/4 and variance 3m/16, so the component count B_matrix satisfies

    Pr[B_matrix<m/8] <= min(1,12/m).                        (18)

Thus C=3 still has typically linear non-scalar support and components, with different constants from the old unsigned envelope. This is a statement about this representation's structure, not a lower bound on all algorithms. Its Q matrices even have special commuting finite-order structure that another method could exploit. The input family remains easily factored and the aggressive cutoff remains without a small ideal-QFT error guarantee. No contrary complexity or accuracy claim is inferred.

## 7. Deliverable boundary

The constructive improvement is exact removal of scalar-only positions with signed coefficients and unchanged multiwindow normalization. The immediately implementable new special case is (15), using three existing typed floor queries. Arbitrary masks have the paid small-odd-part scalar specialization (11), and few-alias regimes have a two-carry scalar evaluator. Large arbitrary Walsh/AP queries and non-scalar matrix windows remain charged; no general poly(log N) simulator is obtained.

Future bounded checks should keep the actual full scalar-column certificate, both signs, stride reduction, asymmetric active-window boundary matrices, and complete final Gram entries. The old frozen files are unchanged. No such new checker or native execution is claimed by this symbolic note.

Global-Knowledge-Sync: main@a462f7a / GLOBAL_KNOWLEDGE_V1
