# PREFIX-1078 — Sharp positive transport horizon and dimension-uniform signed joint tail

2026-11-25. AUTHOR_CONDITIONAL_ANALYTIC_PROOF / HUMAN_RECHECKABLE / NOT_REVIEWED. Existing informed line EM-DIRECT-780BBE / TASK_RESEARCH. Own session metadata recovered in r6-20261125-1250-recover-own, no formal run or CLAIM. Original r6-20261125-1150-owner-read SUCCEEDED, empty LEASED filter as of 2026-11-25T03:54:40.223996Z; fresh r6-20261125-1250-owner-read admitted QUEUED. No shared task mutation.

Frozen input unchanged: P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json; Stage46 chart O, incoming -e1, reversal signed -5 (phase cover 5q), other weights 1, next incoming -d, both orientations of Link {O,e1} blocked without renormalization, exactly two negative steps. Full X6 joint Cell pairing, port, sign, phase, multiplicity retained in the inherited exact CT observer. All probabilities below are typed analytic readouts, not native spatial coordinates, physical time, or replacement path rules.

Parents read at immutable commits:
- 6b3aeab338c06b4089bbd8402314a66094d8f5ee:research_notes/portable_direct/2026-11-25_r6_prefix1077_multilevel_joint_residual_transport.md (J), (S), (E).
- b47b157958692d0a62f438a3d546baa044168341:research_notes/portable_direct/2026-11-25_r6_prefix1076_uniform_beta_tail_transport.md (1), local beta approximation.
- 7e8adcd9dac8e9ae5662c71aed1e2211458f12f0:research_notes/portable_direct/2026-11-25_r6_prefix1075_uniform_positive_tail.md, exact weighted observer, positive lower edge, K_last(m)=rho_last*m+O(1).
- inherited fixed-m decay of PREFIX-1073 and exact telescoping. Parent claims remain author-conditional, not independently reviewed. Mother B_fix,odd(32) remains open.

## 1. Exact signed extension beyond the positive horizon

Write D_m(k)=D(m+8,k), a=m+4, b=k+1, f=x^m(1-x)^k. Fix integers m,k>=0 with D_m(k)>0. For any finite integer r>=1 define the signed mass on N^r:
    J_r(l)=D_(m+r)(k+s)/D_m(k), s=sum_i l_i.
This extends the positive joint law of PREFIX-1077 without using a conditional probability at a negative or zero denominator. For every fixed m,k,r it is absolutely summable: the fixed-length bound D_(m+r)(k+s)=O_{m,k,r}((1+s)^(-m-r-4)) times the composition count binomial(s+r-1,r-1)=O_r((1+s)^(r-1)) is O((1+s)^(-m-5)). Thus Fubini is legal for this signed series. Telescoping the last coordinate yields J_(r-1), with J_0=1, and hence total signed mass exactly one. Exchangeability and marginal consistency hold for all finite r; translating the lower thresholds gives the exact signed joint survival J_r({l_i>=t_i})=D_m(k+sum_i t_i)/D_m(k). These are algebraic identities, not assertions of a positive probability outside the admitted horizon. If an individual history has zero probability, no conditional kernel at that history is needed.

Define K(j)=max{u>=0:D_j(u)<0}, with K(j)=-1 if none. Uniform eventual positivity makes K(j) finite. If D_j(u)<0, exact absolutely convergent telescoping forces at least one D_(j+1)(v)<0 at v>=u. Hence K(j+1)>=K(j) (also true for sentinel -1). In particular, any negative signed entry at one depth prevents every larger depth from being entirely positive as a mass function, because the smaller depth is a marginal.

The criterion is exact:
    J_r is a probability mass iff k>K(m+r).                 (H)
Indeed all terminal arguments k+s occur (choose l_1=s, other coordinates 0), and D_m(k)>0. If k<=K(m+r), choosing s=K(m+r)-k gives a strictly negative mass. Conversely all arguments are nonnegative when k>K(m+r); absolute summation gives mass one. The criterion allows zero entries; strict positivity needs a separate exclusion of zeros. When (H) holds, every preceding signed marginal is a probability as well, and the genuine transition probabilities are defined on histories of positive mass.

Suppose k>K(m) and D_m(k)>0, as in the initial positive tail. Let R(m,k) be the largest admitted positive depth (0 allowed). Monotonicity and the inherited K(j)=rho_last*j+O(1), rho_last=1/b_last-1>8, imply R exists and
    R(m,k)=k/rho_last-m+O(1),                               (R)
uniformly as k->infinity over such starting pairs. Proof: there is a fixed B with |K(j)-rho_last*j|<=B for all sufficiently large j, and B may be enlarged to include the finitely many earlier j (sentinel included). From K(m+R)<k<=K(m+R+1),
    (k-B)/rho_last-1 <= m+R < (k+B)/rho_last.
Consequently the true maximum depth is not the conservative sufficient depth k/C-m from the parent. For fixed m, R/k->1/rho_last=b_last/(1-b_last), strictly between 0 and 1/8. This family has no infinite probability extension respecting all prescribed higher joint survival identities at any fixed starting pair: some finite J_r has negative mass. This does not exclude arbitrary exchangeable extensions that change the prescribed future joint observations.

## 2. A stronger whole-law bound with no growth in r in its leading term

In the following use 0<eta<1/2 and the frozen analytic assumptions of PREFIX-1075/1076. There exist constants 0<delta<1/9, H, A0>0 such that on [0,delta] the effective density is g(x)=A0*x^3+O(H*x^(3+eta)) and g>=0. For a smooth cutoff 0<=chi<=1 equal to 1 on [0,delta/2] and zero on [delta,1], the inherited exact observer splits
    L(h)=integral chi*g*h + L((1-chi)*h).
Moreover the complete observer has the exact representation
    L(h)=c sum_(v=0)^3 integral w_v(x)(E+8)^v h(x) dx,
    c=1/(4*36^8), E=x*d/dx,
where each w_v is integrable (a finite pushforward of bounded Laurent weights). Equivalently L is an integral of ordinary derivatives h^(j), j<=3, against finite signed/complex measures with finite total variation: expand (E+8)^v as sum of polynomial coefficients times derivatives. Thus sums of absolute derivative contributions may be bounded pointwise before integration; a bound of a sum of suprema is not assumed.

Let q_l(x)=x*(1-x)^l and Q_l(x)=prod_(i=1)^r q_(l_i)(x). Their pointwise sum over l is 1 for x>0. The numerator of J_r is L(f*Q_l). The reference mass is
    J_r^0(l)= B(a+r,b+s)/B(a,b)
            = integral Q_l(x) x^(a-1)(1-x)^(b-1) dx / B(a,b).
For x>=delta/2 and d=1,2,3, differentiating the polynomial q_l gives
    sum_(l>=0)|q_l^(d)(x)| <= 2*d!*x^(-d).
Proof: the two terms of the product derivative have coefficients x*(l)_(falling d) and d*(l)_(falling d-1). Sum using
    sum_(l>=j) (l)_(falling j)*(1-x)^(l-j) = j!*x^(-j-1).
Both terms each contribute d!*x^(-d). Terms with l<j are zero, including at x=1. For d=0 the sum is 1. Multinomial Leibniz for the r product yields
    sum_(l in N^r)|Q_l^(d)(x)|
      <= 2^d*d!*binomial(r+d-1,d)*x^(-d)                    (D)
for d=0,1,2,3. Each multi-index of derivative orders contributes at most 2^d*d!*x^(-d), and their number is the displayed binomial. In particular the derivative mass grows only as O_delta((1+r)^3), not exponentially with the number of components.

Put q=(1-delta/2)/(1-delta/4) in (0,1). For k>=C(m+1) with C sufficiently large (as in PREFIX-1076), m<=k, k>=3, (8/delta)^m<=q^(-k/2), and D_m(k)>=A0*B(a,b)/2. Define mu=a/(a+b). Then for a constant M independent of m,k,r,
    sum_l |J_r(l)-J_r^0(l)|
       <= M*[mu^eta+(1+m+k+r)^3*q^(k/2)].                  (TV)
This is an l1 bound for normalized signed masses; on the admitted probability horizon half the l1 norm is ordinary total variation distance.

Proof: compare the unnormalized vectors N_l=L(f*Q_l) and N_l^0=A0*integral x^3*f*Q_l. The local difference from replacing chi*g by chi*A0*x^3, summed in absolute value, is <=H B(a+eta,b), since Q_l>=0 and sums to one. Relative to B(a,b) this is <=H*mu^eta by concavity. The missing baseline outside chi has total mass <=A0*(1-delta/2)^k. For the complementary observer, expand its derivatives and apply Leibniz to (1-chi)*f*Q_l. On x>=delta/2, ordinary derivatives of f through order 3 are bounded by constants times (1+m+k)^j*(1-delta/2)^(k-j). By (D) and fixed cutoff derivatives, for each j<=3 the sum of absolute complementary derivative values is <=C_delta*(1+m+k+r)^3*(1-delta/2)^(k-3). Integrate against the finite variation coefficient measures and use Tonelli on absolute values. The lower bound B(a,b)>=H2*(delta/8)^m*(1-delta/4)^k from PREFIX-1076 then gives the complementary normalized bound C'*(1+m+k+r)^3*q^(k/2), using the threshold on m/k above. Finally divide by D_m(k), and correct the normalizer from A0*B(a,b) to D_m(k) using the parent relative estimate |D_m/(A0 B)-1|=O(mu^eta). The reference mass sums to 1. This proves (TV) without assuming that each J_r entry has positive sign.

For any fixed A>0, if r<=k^A, the polynomial-exponential term is O_A(mu^eta), uniformly; indeed mu>=4/(k+5). In particular this covers the entire actual positive horizon from (R), including depths comparable to k at which the PREFIX-1077 endpoint pointwise approximation O(nu^eta), nu=(a+r)/(a+b+r), need not tend to zero. Even r<=q^(-k/12) is permitted in (TV): (1+m+k+r)^3*q^(k/2)<=C*(1+k)^3*q^(k/4), since m<=k. Thus the normalized signed readout remains l1-close to the positive reference for an exponentially large finite range of depths, although it ceases to be a probability at the much smaller linear horizon. For any sequence k/(m+1)->infinity, the bound tends to zero uniformly in this range. This statement is not a uniform pointwise relative error beyond the earlier parent's range.

## 3. Exponentially small negative mass: a sharp distinction between sign and norm

Define the negative mass N_r=sum_l max(0,-J_r(l)); J_r is real from the exact BRC observer. The local vector integral chi*g*f*Q_l is entrywise nonnegative. Therefore every negative part is bounded by the absolute complementary observer term. The same proof, now without a baseline approximation, gives
    0<=N_r <= M'*(1+m+k+r)^3*q^(k/2).                      (N)
For k>K(m) in the initial tail, N_r=0 iff r<=R(m,k); for r>R it is strictly positive by (H). At depths of order k beyond R the negative mass is strictly positive but bounded by a polynomial times q^(k/2). Thus even a very accurate full-vector norm approximation can fail to detect the breakdown of positivity. It is a real signed-observer residual, not numerical noise or a license to erase branch information. For a concrete approximation of this specific mass readout only, the normalized positive part J_r^+/(1+N_r) is a probability with l1 error exactly 2*N_r: the positive entries lose total N_r on normalization, and the negative entries contribute N_r. This is an explicitly paid observer approximation, not an identity or native-state quotient.

## 4. Evidence, limitations and next question

New science: exact signed joint extension and marginal identities, monotonicity of the global last-negative integer, necessary and sufficient finite positive-horizon criterion, sharp maximum depth with O(1) error, and dimension-uniform l1 estimate plus exponentially small negative-mass bound. The proof uses the original full signed BRC observer and its finite derivative measures; it does not replace the correlated joint law with independently sampled scales. No new native enumeration, no new classical trigonometric or pi computation, no formal verification or independent review. Constants and rho_last remain existential, so these are conditional analytic estimates, not finite-parameter numerical certificates. Parent mathematical assumptions remain unchanged.

Next: obtain explicit lower-edge constants and a certified interval for b_last; seek a matching lower bound for N_r at depths r=theta*k beyond the first failed horizon, identifying the dominant rare negative terminal s. This would quantify the precision required to detect the first nonpositive extension. Preserve other regular-band sign boundary problems. Do not redo original native enumeration or previously saved endpoint algebra.
