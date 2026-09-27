# Finite feedback does not imply short or few active windows

Status: **AUTHOR_SYMBOLIC_RESULT / SHARED_CONTEXT / NOT_ADMITTED**. This unit contains a self-contained sufficient-condition contraction and an actual-instrument counterexample to a structural shortcut. It performs no new scientific calculation, professional query, or remote publication. All carrier coordinates and signed cross terms are retained.

## 1. Exact source and convention

The frozen adaptive `nonzero_structure/ACTIVE_WINDOW_FLOOR_MOMENTS.md` is used at SHA-256 `20a93f15f241f9c3220c031032cc2af697e4d4a448669f5b637396c1a05529d4`, EM commit `c0f04346c520fddc8016c86227b3b6cc2e9f30f6`, prefix `research_notes/directed_recovery/20260927_C6438C/qft_adaptive/`. Its arbitrary even/odd period formula, full-carrier identity premise and raw normalization are preserved.

The actual feedback order was read from `optimization/collision_analysis/gram_sampler.py`, SHA-256 `468de944518fbc6afa81a17555676436376da63921a784c810ffe8fab3ca17e9`, EM `0e6380ff74d31b842ba0b54802c1f0595a7dd60d`, prefix `research_notes/directed_recovery/20260926_C6438C/`. `_gates(j)` lists phase indices `j-c+1` for increasing earlier positions c with h_c=1. `_left` applies that list in its recorded order. Thus, if c_1<...<c_v are those earlier positions,

    T_j = W_(j-c_v+1) ... W_(j-c_1+1),
    O_j = (-1)^h_j T_j.                                      (1)

The rightmost factor acts first. No commutation or cancellation is assumed. A selected-word policy uses its committed ordered sublist in (1), never retrospectively recomputed past choices.

Use the following cutoff convention throughout:

    C >= 3 is the FIRST identity phase index:
    W_m = I on the complete carrier for every m >= C.         (2)

Equivalently the largest possibly retained index is J=C-1. The existing `phases/closed_phase_bank.py::truncated_tail_bank` uses exactly this first-identity convention, SHA-256 `16b2bd768fcd89c50971ab8ddf06c81af562a7f4608373ff497f294d5ce6e6ed`, EM general source `1fb7ff99d205f9ca03772942be64f732553dcd86`. Its `IdentityTail` is the entire-space empty word, not a residual truncation.

The concrete uniform policy was read at `sep27-qft-uniform/uniform_execution/uniform_feedback.py`, SHA-256 `755d398a19881508112c9e360c94bf10133681af8d3cbdbb103accdecc306e28`. It inherits frozen adaptive source `86263eb4a70fe53f8960aae2c1f0b8695dbca40a597b2711af90f20667ed3c45` and only tests omission of the oldest listed word. An accepted decision charges all the remaining budget. This rule does not provide a bank-wide cutoff (2); it cannot be substituted for that premise. Its final immutable publication identity is supplied by the root closeout, not invented here.

The shared native activity is `RA-CAAAC604CB513AEA8BBC1DFC`; the root supplied the passing startup guard, and the boundary startup record was read. The shipped GK helper was independently run, returning PASS/LEASE_REUSED at canonical `a462f7a7002648c047d58a4cf1d5038fe98d5b09`; its three entrypoints were read and the applicable policy paths were unchanged from the prior lease. No new admission authority follows from that guard.

## 2. What a cutoff actually certifies

Let h have length i and S={c: h_c=1}. Define the structural envelope

    Abar(h,C) = union_(c in S) [c, min(i-1,c+C-2)].            (3)

Then the true full-matrix nonidentity support A={j:O_j!=I} satisfies

    A subset Abar(h,C).                                      (4)

Proof: if j is outside (3), h_j=0. Every earlier one c then has j>=c+C-1, hence j-c+1>=C, so its phase factor is I. Formula (1) gives O_j=I. The current sign at c accounts for the left endpoint c. The last possibly active feedback from c has m=C-1 and occurs at j=c+C-2. This explains both endpoints without an off-by-one convention change.

Equality in (4) is not automatic: legal factors may cancel, or some retained phases may themselves be I. Conversely, h_j=0 is not an identity certificate. With h_c=1, all later bits zero, and W_2!=I, one has O_(c+1)=W_2. Exact cancellation may shrink the envelope only when it is independently proved from the complete words or a certified common invariant subspace.

If w is the Hamming weight, |Abar|<=min(i,(C-1)w). If the nonzero bits lie between f and l, a sufficient single enclosing window is

    [f, min(i-1,l+C-2)],
    ell = min(i,l+C-1)-f.                                    (5)

The old active-window theorem applies exactly with this ell and the original ordered gates. A small C does not bound w, l-f, or the number of envelope components. When words are omitted by a public-history policy, the same envelope remains a sufficient upper bound only if every retained factor satisfies the verified cutoff premise. A current policy decision must not rewrite earlier operators used by the coefficient oracle.

## 3. An actual reachable family with many active bits and components

Take the permitted changed bank with C=3:

    W_2=Q,  W_m=I for m>=3,
    Q(v_0,v_1,v_2,...)=(v_1,-v_0,v_2,...).                   (6)

This Q is `stage80/fixed_phase.py::QuarterTurn.apply_numer`, native bundle snapshot `0852cad130c1d877174d235687cf60c19f318c58`, file SHA-256 `d9981004a89c651f072ff88732c8b402baf83c16690a0cfacfa9c32199fde254`. Its sign is obtained by `primitives()` from the actual equal-matching junction and checked as -1; it is not an ideal-angle replacement. The existing complete direct-word bank also carries exact m=2. Reading these pinned columns is source reuse, not new scientific execution.

With h_-1=0, (1) becomes exactly

    O_j=(-1)^h_j Q^(h_(j-1)).

Since Q is neither I nor -I,

    O_j=I iff h_j=h_(j-1)=0.                                 (7)

Consequently A=Abar for this bank. The all-ones word has active width i. Repeated `100` gives separated two-position active windows, up to the endpoint. The following family proves these histories are actually reachable and that typical histories need not be sparse.

For k>=2 set

    N=5*3^k, a=2, q=3^(k-1), n=ceil(log_2 N), t=2n.

The exact order of 4 modulo 3^k is 3^(k-1): elementary binomial expansion gives v_3(4^d-1)=1+v_3(d) for d>=1. To see the valuation without assuming an order oracle, start with 4=1+3; cubing a number of the form 1+3^j u, 3 not dividing u, increases that valuation by exactly one. Raising it to an exponent prime to 3 preserves it, again by the first binomial term. Since 2=-1 modulo 3, its order modulo 3^k is 2q. Its order modulo 5 is 4. Coprime CRT components therefore give

    ord_N(2)=lcm(2q,4)=4q.                                   (8)

Choose any prefix depth i with 2^i<=q. In particular i=floor(log_2 q) grows linearly with the input bit length n, and t-i>=2. The depth-i preparation base is b=2^(2^(t-i)) modulo N, hence ord_N(b)=q. The work labels b^x, 0<=x<2^i, are all distinct. No modular alias is present in this prefix.

For each fixed public history h and every preparation address x, the actual row contribution is 2^-i U_h(x), where U_h(x) is a chronological product of complete orthogonal O_j applied to e_0. It has squared norm 4^-i. Distinct addresses occupy distinct work labels, so no cross term enters the total prefix mass. Thus

    M_h=2^i*4^-i=2^-i for EVERY h in {0,1}^i.                (9)

This argument uses the actual orthogonal instrument, including its residuals; it holds regardless of the bank's approximation to ideal QFT. The history distribution on this prefix is exactly the uniform bit distribution.

Two elementary quantitative consequences now follow for the actual bank (6):

1. Active positions include all one bits. If A_i=|A|, the variance of their number is i/4, so Chebyshev gives Pr[A_i<i/4]<=min(1,4/i). Thus a constant fraction of the prefix is active with probability tending to one.
2. Let B_i be the number of active components and m=floor(i/3). Each disjoint triple `001` creates a component start at its third position by (7). The m triple indicators are independent, each with probability 1/8. Their sum Y has mean m/8 and variance 7m/64, and B_i>=Y. For m>0,

       Pr[B_i<m/16] <= min(1,28/m).                         (10)

Thus the number of components is also linear with probability tending to one. Equivalently, an unrestricted position j>=2 starts a component exactly when the local word ending there is `001`, with probability 1/8. The disjoint-triple proof avoids needing a separate dependence theorem.

There is also a broader full-carrier width obstruction for the actual odd-dimensional fixed-rotor family, without choosing the aggressive C=3 tail. The same pinned `FixedRotor` source writes each phase as D_0 G^T D_0 G, so its determinant is +1 by orthogonality and paired factors; Q and I also have determinant +1. On the full D=61 carrier, det(O_j)=(-1)^h_j. Every one bit therefore forces O_j!=I regardless of feedback cancellations or the cutoff. The alias-free argument (9) applies to any such actual orthogonal bank, including a varying cutoff, so the first probability bound still rules out a universally short enclosing full-carrier window on this easy family. This determinant argument does not certify the number of components, nor exclude a different separately proved reachable-subspace reduction. The linear component count (10) is specifically the C=3 construction.

This is an exact counterexample to inferring short/few windows from finite feedback alone, including a typical-history version. It is **not** a general Shor complexity lower bound. The family has the public small factor 5 and an elementary known order; it is intentionally an easy classical family. The C=3 cutoff is also not asserted to meet a small global ideal-QFT error target. A claim restricted to a particular growing cutoff, accuracy guarantee, or different sampled-history distribution needs an additional argument; (10) neither proves nor disproves such a claim.

## 4. Conditional multiwindow contraction that preserves order

Now fix any actual public history, and suppose complete-word evidence certifies O_j=I outside b disjoint chronological windows

    I_a=[s_a,e_a], ell_a=e_a-s_a+1,
    V_a=2^(i-1-e_a),  a=1,...,b.

Windows may include identity positions; this changes cost but not correctness. Let s=sum ell_a and G=i-s be the number of free identity positions. At window a write its local integer x in ell_a chronological bits and define the full operator

    A_a(x)=O_(e_a)^(last bit) ... O_(s_a)^(first bit).

For every full address n there is a unique decomposition

    n = beta + sum_a V_a x_a,

where beta has arbitrary bits at free identity positions and zero bits in all windows. Its vector is exactly

    U(n)=A_b(x_b)...A_1(x_1)e_0.                             (11)

This identity removes only proven identity factors. It does not reorder operators from distinct active windows.

Assume the caller has separately paid for and verified R=ord_N(b_depth) and an address 0<=r<R with b_depth^r=z. These are order/target-address inputs, not free oracles. If z is outside this cyclic subgroup, the corresponding Gamma is zero only after a suitable membership certificate.

Define the integer free-position pair count

    K_R(rho) = #{(beta,beta'): beta'-beta=rho modulo R}.       (12)

For each window define a linear map on **arbitrary full D by D matrices X**:

    C_(a,d)[X] = 4^(-ell_a)
       sum_(0<=x,x+d<2^ell_a) A_a(x) X A_a(x+d)^T.           (13)

Then the exact relative Gram matrix is

    Gamma_h(z) = 4^(-G) sum_(d_1,...,d_b)
      K_R(r-sum_a V_a d_a)
      (C_(b,d_b) o ... o C_(1,d_1))[e_0 e_0^T],             (14)

where |d_a|<2^ell_a, the K argument is taken modulo R, and o denotes composition. For b=0 the sum has one term and the composed map is the identity.

Proof: expand Gamma as 4^-i sum U(n)U(m)^T over m-n=r modulo R, retaining its original orientation. Fix d_a=x'_a-x_a. The modular condition on free bits is beta'-beta=r-sum V_a d_a, counted by (12), independently of the particular local x_a. Grouping each pair (x_a,x'_a) successively yields the composition (13) in chronological order. These maps supply 4^-s, and the remaining raw factor is 4^-G. No probability renormalization, matrix commutation, or cancellation enters the grouping.

For one window this is precisely the old active-window result: the leading and trailing free positions supply K_R as its J_d. The old degree-three floor-moment evaluator remains the cheaper known way to evaluate that special weight. For R=1, K_R(0)=4^G and the outer scale cancels, as required. These observations check normalization without scientific execution.

## 5. Two important matrix pitfalls

First, each window must act on the matrix produced by earlier windows. The e_0-seeded coefficient C_(a,d)[e_0e_0^T] is not a sufficient substitute for the map (13). Multiplying separately seeded matrices loses the correlations that connect windows.

For a one-bit Q window, C_1[X]=XQ^T/4. Two such maps give C_1[C_1[E]]=E(Q^T)^2/16=-E/16 for E=e_0e_0^T. Multiplying the two separately seeded matrices instead gives (EQ^T)(EQ^T)/16=0, using the actual Q columns in (6). This is a symbolic illustration of the missing boundary matrix, not a new numerical native fixture.

Second, the correct negative-displacement identity for arbitrary X is

    C_(a,-d)[X] = (C_(a,d)[X^T])^T.                        (15)

It reduces to the familiar output transpose only when X is symmetric. Earlier off-diagonal window coefficients need not be symmetric. For example X=e_0e_1^T and the one-bit Q window give C_-1[X]=QX/4=-e_1e_1^T/4, whereas (C_1[X])^T=QX^T/4=e_0e_0^T/4. Dropping the input transpose is a substantive error.

The two-carry recurrence can be extended linearly to arbitrary signed X, with X as the initial seed and the original temporal factors at every layer. This is a mathematical extension, not a claim that the currently frozen executor exposes or validates that API. Its empty carry state is zero, not I; the physical initial matrix remains e_0e_0^T. A future implementation must bind its ordered gate list and certify all matrix entries, including (15).

## 6. Explicit conditional cost, including scalar weights

There is a simple finite exact evaluator of all (12), without pretending its cost is polynomial in log R. Start with a scalar residue array k_0(0)=1 and zero elsewhere. For each free bit with address weight w, update

    k_new(rho)=2k_old(rho)+k_old(rho-w)+k_old(rho+w).          (16)

The choices (bit,bit')=(0,0),(1,1),(1,0),(0,1) prove this recurrence; it is an integer pair-count observer, not a new amplitude propagator. After G bits, k=K_R, sum k=4^G and each entry has at most 2G+1 bits. A dense exact array takes O(GR) scalar additions and O(R) entries. A sparse representation may reduce actual work but can become dense. Residue addressing, signed arithmetic, bit lengths and typed-receipt costs must all be charged.

Let

    M = product_a (2^(ell_a+1)-1) <= 2^(s+b).                (17)

For each displacement tuple, apply the maps in (14) to one full matrix using ell_a two-carry layers per window. This gives a conservative O(Ms) full-matrix carry-layer bound after K_R is available, plus M weight lookups and weighted matrix additions. Full D^2 entries, actual word actions, denominator sizes and typed arithmetic multiply these stage counts. A streaming evaluator need not materialize a D^4 superoperator tensor or store every displacement tuple. Reuse can improve the bound but is not presumed.

Thus one explicit sufficient implementation has conditional cost

    O(GR) scalar pair-count steps + O(2^(s+b) s) carry layers,

plus paid order/address acquisition, source/word admission and exact arithmetic. This trades dependence on the entire preparation length for dependence on the active bits/windows, while the residue table can remain expensive. It is useful when those parameters and R are genuinely small or already paid. It does not remove a large unknown odd-order bottleneck.

An equivalent safe representation is a cyclic group-algebra coefficient array of full D by D matrices, dimension R D^2. Identity digits multiply it by the scalar Laurent factor (2+X^w+X^-w)/4. Active digits act by

    F -> [F + X^-w O F + X^w F O^T + O F O^T]/4.

Scalar identity factors commute with these linear maps; active factors still retain their chronological order. This proves why identity gaps can be collected into K_R and why generic active-window maps cannot be multiplied as scalar coefficients. R D^2 is a sufficient representation size, not a lower bound on every possible representation.

With several long identity gaps, the single-window degree-three floor formula must not be reused without a new derivation: the free-address set is now a binary-mask sumset and its pair weights contain coupled congruences. Formula (16) is a proved fallback. This unit makes no unproved O(poly(log R)) claim for general multi-gap weights. The same discovered order and target-address information must be offered to the classical comparator; often the order already supports ordinary factor postprocessing.

## 7. Result and next concrete boundary

Finite feedback supplies the exact envelope (3), not a promise about its size. The C=3 native example supplies both worst-case and typical reachable histories with linear active support/components. Equation (14) nevertheless gives an exact conditional multiwindow reduction with explicit paid information and representation costs. Neither result claims a generic efficient simulator or a precision guarantee for the aggressive cutoff example.

The smallest new implementation justified by this note would be an arbitrary-matrix seeded window adapter with the input-transpose rule (15), and an explicit scalar free-bit counter (16). A bounded comparison should use two separated noncommuting actual windows, retain all residual entries, include asymmetric intermediate X, and compare the complete final Gram matrix. This is a future verification target; no such implementation or new scientific run is asserted here.

Global-Knowledge-Sync: main@a462f7a / GLOBAL_KNOWLEDGE_V1
