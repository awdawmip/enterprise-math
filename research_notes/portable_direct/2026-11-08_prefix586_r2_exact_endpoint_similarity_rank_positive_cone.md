# PREFIX-586-R2 — Generic invertibility, exact rank stratification and positive endpoint repair for native X6-BRC

Date: 2026-11-08 (Asia/Shanghai).
Status: AUTHOR-SIDE PROVED / EXACT COMPUTATION EXECUTED / UNREVIEWED / NOT ADMITTED.
Immutable science pin: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Predecessor: PREFIX-585-R2 at 5ec3c4c3787fb1e98cc9d8f288cf0d2f28f2efd7, research_notes/portable_direct/2026-11-08_prefix585_r2_native_spectral_ABBA_intertwiner.md.
Native scope: original four STARs, 48 original phases, 96 phase/branch ports, 144 directed phase edges, all 576 labelled native actions; six axis weight variables and original fixed gate target (0,1,-3). No frozen input, P000, world view or gate observer changed.

## Selected question

PREFIX-585 proved a polynomial UV/VU factorization of the original 96-port weighted transition A and its axis-swapped transpose. Does U generically lose open-path endpoint information, and what exact repair is available, including singular parameters and positivity?

## Native definitions

The four original STARs are (1,3,6), (1,4,5), (2,3,5), (2,4,6).
Let S be their 48-by-48 integer phase successor adjacency, S_ij=1 exactly when original phase j is one of the three native successors of phase i. For each phase i=(a,p,c), let its positive axis label be |c|; exactly eight original phases carry each label a=1,...,6. Write X=diag(x_|c_i|), B=(XS) tensor I_2. The 96-port original gate factor D(z) is block diagonal with M_t=[[1,1],[1,z^t]], where t=1 only at the original fixed target phase. Set A(x,z)=B(x)D(z), as in PREFIX-585. This is the original 96-port weighted operator, preserving all action sources.

Write alpha=(1 3)(2 4), and H for the bit-preserving lift of the proven 48-phase reversal involution. The existing finite polynomial identities are A(alpha*x,z)=UV, A(x,z)^T=VU with U=H B(x)^T and V=D(z)H^-1.

## Theorem 586.1 — Exact generic similarity and sparse inverse

For every nonzero choice of x_1,...,x_6 over any characteristic-zero field, and EVERY gate parameter z, including z=0 and z=1, the 96-port matrix U is invertible and

    det(U) = 3^24 * PRODUCT_{a=1}^6 (x_a^16).

Let T=3 S^-1. Then T is an INTEGER 48-by-48 matrix with exactly four nonzero entries in EACH row and column: one -2 and three +1. Its other entries are 0. The exact inverse is

    U^-1 = (1/3) (X^-1 T^T tensor I_2) H^-1.

Consequently the polynomial PREFIX-585 UV/VU identity is an actual similarity:

    A(alpha*x,z) = U A(x,z)^T U^-1.

Proof. The original 48-phase construction is finite and completely explicit in the attached standard-library certificate. Direct rational Gaussian elimination yields det(S)=531441=3^12 and T=3S^-1 integer. The complete 48-by-48 exact certificates ST=TS=3I, with 48 entries -2, 144 entries +1 and 2112 zeros, establish the claimed inverse and local sparsity (not just a finite sample of an infinite conjecture). As B=(XS) tensor I_2, det(B)=det(XS)^2=3^24 PRODUCT x_a^16. H is the same phase permutation on both branch bits and therefore det(H)=+1. Hence det(U)=det(B). Substituting S^-1=T/3 proves the inverse formula. The predecessor UV/VU identities then imply the similarity for all z by multiplying with the actual inverse. QED.

The inverse is computationally local: 4 rational coefficients per row rather than a generic dense 96-port inverse. Some coefficients are negative, so full-orthant positivity is not automatic.

## Theorem 586.2 — All singular axis and gate strata

Let s be the number of nonzero axis weights among x_1,...,x_6. Over characteristic zero,

    rank(U)=16s,
    rank(V)=48 if z=1, and 49 if z!=1,
    rank(A(x,z))=8s + indicator(x_1!=0 and z!=1).

Proof. The invertible S makes rank(XS)=rank(X)=8s. Thus B and U each have rank 16s. D has 47 unmarked 2-by-2 rank-one blocks and one marked block of determinant z-1, yielding the V ranks.

At z=1, every original source phase has two identical outgoing branch rows, and the selected nonzero rows of XS are independent, so rank(A(x,1))=8s. For other z the only difference is the rank-one marked-gate term (z-1) v e_(target,branch1)^T. Its source phase predecessors have source-axis label 1, hence it vanishes exactly if x_1=0. If x_1 is nonzero it creates a direction outside the column space at z=1 (which is equal across paired source branch bits), while its target covector is outside the row space at z=1 (which is equal across paired target branch bits). Rank increases exactly once. QED.

An independent finite exact check built the COMPLETE 96-port matrix over GF(101) for every 64-element axis support mask and z in {0,1,2}: 192 rank calculations, all matching this formula. This validates the original implementation; the algebraic rank-one argument establishes the arbitrary-z result.

## Theorem 586.3 — Unbounded open-path boundary transport

For any two 96-component boundary columns l and r, define Z_d(x,z;l,r)=l^T A(x,z)^d r. For every integer d>=0 and nonzero x_a,

    Z_d(x,z;l,r) =
      (U^-T r)^T A(alpha*x,z)^d (U l).

Proof. Rearrange the similarity as A(x,z)^T=U^-1 A(alpha*x,z) U; take its d-th power, and transpose the scalar bilinear form. QED. This is a complete endpoint-transport identity, not an assertion that unchanged endpoints give the same open-path total after alpha.

## Exact positive endpoint cone

Assume all six x_a>0. For nonnegative l, U l>=0 because B and H have nonnegative coefficients. Let h(j,u)=(Theta(j),u), with j an original phase and u=0 or 1. The four nonzero entries T[j,i] are -2,+1,+1,+1 and all corresponding phases i have source axis |c_i|=|p_j|, the preceding-axis label of target phase j. Therefore

    (U^-T r)_(h(j,u))
       = ( -2 r_(i_minus(j),u)
            + r_(i1(j),u) + r_(i2(j),u) + r_(i3(j),u) )
         / (3 x_|p_j|).

For nonnegative r, the transformed endpoint is nonnegative IF AND ONLY IF all 96 (48 phases times 2 branch bits) precise inequalities

    2 r_(i_minus(j),u) <=
       r_(i1(j),u)+r_(i2(j),u)+r_(i3(j),u)

hold. These are necessary and sufficient for THIS explicit U endpoint repair; no broader positive-realization minimality claim is made.

In particular the all-ones vector 1 satisfies all inequalities, and exactly

    (U 1)_(h(j,u))=3 x_|p_j|,
    (U^-T 1)_(h(j,u))=1/(3 x_|p_j|).

Thus UNIFORM original endpoints admit strictly positive transported endpoints for every x_a>0, all z>=0, and every length d>=0. The transition probability A/6 obeys the same identity divided by 6^d. This is a nontrivial positive BRC observation despite the signed inverse on the full ambient space.

An exact distinguishing open-path witness: x=(2,3,5,7,11,13), z=17, d=1. The uncorrected original total 1^T A(x,z) 1=4032; the naive swapped total 1^T A(alpha*x,z) 1=4176; the transported positive-endpoint total is exactly 4032. At d=8 the original and transported totals both equal 335036471205888.

## Exact executed verification, evidence and limits

The author-side standard-library exact verifier reconstructed every original phase, phase edge and labelled branch action, performed exact Fraction elimination for S and full ST=TS=3I, checked integer-T row and column histograms, checked 96-by-96 similarity at three parameter assignments (including z=0 and z=1), 192 modular-rank specializations, positive endpoint inequalities and nonuniform boundary tests, and direct open-path checks through d=8. It produced ALL_ASSERTIONS_PASS_AUTHOR_SIDE_UNREVIEWED. All computations are exact integers, rationals or modular arithmetic. The universal claims rely on the displayed proofs. The separate small independent certificate repeats the exact S/T kernel, row support and cone source-axis property.

BRC interface: COMPOSE_APPLIED from frozen original native 96-port transition, PREFIX-584 phase reversal and PREFIX-585 polynomial two-factor operator; no discarded source or original axis. Source code and a full JSON result accompany this note. This is an author-side theorem candidate, awaiting independent review and Source-native admission.

## Next PREFIX-587 discriminating question

Under repeated composition of the two axis transformations (5 6) and alpha=(1 3)(2 4), characterize the smallest family of endpoint repair coordinates stable under composition and determine whether the 96 cone inequalities have a smaller irredundant generator set. Alternatively derive T from a direct integer local BRC path-count formula without 48-by-48 elimination.
