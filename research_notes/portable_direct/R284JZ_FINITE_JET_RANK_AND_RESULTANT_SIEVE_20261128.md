# R284JZ — Finite-jet rank collapse and resultant sparsity without Hankel decisions

2026-11-28. Author proof, NOT_REVIEWED. Ordinary auxiliary integer arithmetic, not a native spatial attribution. Existing own researcher EM-DIRECT-0C386E / TASK_RESEARCH, session MCP-8cd6c4fa26b9459d923ff73ba0082220; read-only recovery r1-20261128-0400-own-recovery succeeded and showed no own RUN. Prior owner inventory r1-20261128-0256-leased succeeded, as of 2026-11-27T18:57:38Z with no LEASED rows. New owner inventory r1-20261128-0400-leased RUNNING at last observation. No new Task, claim, Result or shared-owner mutation. Account normative main snapshot 40b9096c89b116c5d75e27cc0e0095ec8d710080 (both entry blobs verified), P000 V4/V5, ACTIVE worldview, informed TASK entry, joint/residual and portable rules consulted.

Frozen science: JY 2cbc0012bff18436ce6e9564751c17b73e6c99bd:research_notes/portable_direct/R284JY_HANKEL_RESULTANT_DICHOTOMY_SUBPOWER_20261128.md (blob 98d550f82e6f7874f8612086957914a545b3288d); JX 3144172dd7a914ff9ea11e79c54ef3e653e7c9f6:research_notes/portable_direct/R284JX_HANKEL_DETERMINANTS_AND_POWER_SAVING_20261128.md (blob 2047c300ef0a4e7391d27f6dd09ad77857bda9f0). Reuse inherited eventual unique legal root and all-fixed-order expansion with c1 != 0; no new independent verification of those dependencies. JY already proves the subpower count. New result is a branch-free finite-jet theorem with explicit constants in terms of finite remainder bounds and no need to decide any Hankel minor. It combines JX's joint determinant with JY's resultant when the determinant is small, rather than first identifying the infinite Hankel branch.

## 1. Finite-jet theorem
Fix integer m>=2, n=2m+2, K=n(n-1)/2=(m+1)(2m+1), M=4m. Assume for all integers d>=D0:
  y_d=P_2(d)+sum_{k=1}^M c_k d^(-k)+e_d,
  |e_d|<=R d^(-M-1), |c1|>=b>0.
P_2 is a fixed real polynomial of degree <=2. No assumption on convergence, rationality, Hankel ranks or smoothness of e_d. For A>=4m set
  E_A(X)=#{d<=X:dist(y_d,Z)<=d^(-A)}.
For every eta>0,
  E_A(X)=O_{m,eta,P_2,c,R,b,D0}(X^(1/(2m+1)+eta)).
This also bounds exact integer hits. The constants and sufficient onset can be computed from bounds on this finite jet and the stated R,D0. It suffices to use A=4m. No coefficient beyond c_(4m) is needed, and no determinant sign/zero decision is needed. The proof supplies a local integer rational-function cover with polynomial height and a resultant divisor bound.

## 2. Upper determinant bound without Hankel inversion
For targets d_i in [D,2D], let z_i be nearest integers, |z_i-y_di|<=d_i^(-A). Use JX's n integer columns
  (1,d_i,...,d_i^(m+1), z_i,d_i z_i,...,d_i^(m-1) z_i).
Denote determinant B and V(d)=prod_{i<j}(d_j-d_i) for distinct ordered nodes. In residual column j=0,...,m-1 subtract d^j P_2(d)+sum_{k=1}^j c_k d^(j-k). Degree <=m+1, so this preserves B exactly. Write t_i=d_i/D. Factor D^j from polynomial column j=0,...,m+1, total D^S where S=(m+1)(m+2)/2. The residual column j is
  sum_{k=1}^{M-j} c_{j+k} D^(-k) t^(-k) + u_j(d),
  |u_j(d)|<=2^j(R+1) D^(j-A0), A0=4m,
using D>=1, A>=M and e_d bound.
Apply the Newton divided-difference row transform on t_1,...,t_n (orders 0..n-1, first l+1 nodes for order l). Its determinant is 1/V(t). For any function t^(-k), order l divided differences are bounded in absolute value by binom(k+l-1,l), using the derivative mean-value formula on [1,2]. For polynomial t^j they are bounded by 3^(m+1). For the discrete u_j, each distinct t-gap is >=1/D, so its divided differences are bounded by n 2^(m-1)(R+1) D^(j-M+n-1), at most n 2^(m-1)(R+1) D^(-m). This step accounts for adjacent nodes and does not differentiate an uncontrolled remainder.

Set T=max(1, max_{1<=k<=M,0<=l<n} binom(k+l-1,l) * max_{1<=a<=M}|c_a|, n*2^(m-1)*(R+1)). Each residual divided-difference column is a sum of at most M+1 vectors: smooth vectors associated with inverse powers k>=1, norm <=T D^-k, and a discrete error vector norm <=T D^-m. Expand the determinant multilinearly in the residual columns. Terms selecting the same smooth inverse power twice vanish exactly (the vectors before scalar multiplication coincide). If e of the selected columns are errors, the other m-e smooth inverse powers must be distinct, so their total exponent plus error exponents is at least
  (m-e)(m-e+1)/2 + em >= m(m+1)/2.
This also holds when all smooth columns are selected. By the permutation expansion of a determinant, each surviving term has absolute value at most n! * 3^((m+1)(m+2)) * T^m * D^(-m(m+1)/2).
Hence for
  B0=n! * 3^((m+1)(m+2)) * T^m * (M+1)^m
the normalized full determinant satisfies
  |B|/V(d) <= B0 D^(-mn).
Indeed V(t)=D^-K V(d) and S-m(m+1)/2-K=-mn. This upper bound retains all reciprocal-coordinate possibilities, including any rank degeneration; no H_m inversion is used.

## 3. Exact rational cover of each short block
Let rho=(2B0)^(-1/K) and H=floor(rho D^(2m/(2m+1))). For D large enough H>=1. Partition [D,2D] into blocks of at most H consecutive integers. For every n distinct targets in one block, V(d)<=H^K, hence |B|<=1/2. Since B is integral, B=0. Thus the full matrix of all targets in the block has rank t<n. With fewer than n targets use the trivial bound n-1.

Otherwise choose t independent rows and t pivot columns and one nonpivot column. Cramer's rule with free coordinate equal to the nonzero pivot determinant gives a nonzero integer null vector of the entire matrix. Consequently, there exist A_D,B_D in Z[x], with degrees <=m+1 and <=m-1 respectively, such that
  B_D(d) z_d=A_D(d)
for every target in that block. These polynomials depend on the block. B_D is not identically zero since otherwise A_D would have >=n roots. This is a local exact relation on the target set, not a claim of equality for all d or of global rationality of y_d.

For explicit heights, let Y>=1 bound |z_d|/D^2 on [D,2D] (computable by the expansion and P_2), U=max(2^(m+1),Y*2^(m-1),1). All original entries are <=U D^(m+1) in modulus. The coefficients from minors have absolute value <=h=(n-1)! U^(n-1) D^((m+1)(n-1)).

## 4. Nonconstant reduced denominator from the retained c1/d
Set l=m+2. For any l+1 distinct target integers in [D,2D], take their order-l divided difference. The polynomial P_2 disappears exactly. The divided difference of 1/d is (-1)^l/prod_i d_i, so its c1 contribution has modulus >= b (2D)^(-l-1).
The higher smooth contributions have modulus <=D^(-l-2) sum_{k=2}^M |c_k| binom(k+l-1,l), by the derivative formula. The discrete and rounding error contribute at most (l+1)(R+1)D^(-M), because integer gap denominators are >=1. Since m>=2, M>=l+2. Define
  S1=sum_{k=2}^M |c_k| binom(k+l-1,l)+(l+1)(R+1).
If D>2^(l+1) S1/b, this divided difference is strictly nonzero, uniformly for all such nodes. Thus no polynomial of degree <=m+1 can agree with z_d at m+3 different targets.
Cancel a primitive polynomial gcd of A_D,B_D over Q[x] using Gauss's lemma, to get integer A',B' coprime over Q. At most m-1 targets have original B_D(d)=0. At least n-(m-1)=m+3 remain. Hence B' cannot be constant, since that would make A'/B' a polynomial of degree <=m+1 at all remaining nodes, contradiction. A' also cannot be zero. The small residual c1 is therefore the essential obstruction to polynomial collapse, even when all the high-rank observers vanish.

## 5. Explicit resultant bound and count
The reduced polynomials have degree <=m+1 and height <=2^(2m+2) h^(m+2): every quotient has integer leading coefficient <=h, roots drawn from those of the original polynomial, each root modulus <=1+h by Cauchy's root bound; elementary symmetric coefficient bounds give the claimed estimate. (The constant-polynomial numerator case is included.)
The nonzero integer R_D=Res(A',B') has
  1<=|R_D|<= (2m)! [2^(2m+2) h^(m+2)]^(2m)=G D^J,
  J=2m(m+2)(m+1)(n-1),
where G is explicitly given by substituting the constant part of h. The Sylvester adjugate gives integer polynomials U1,V1 with U1 A'+V1 B'=R_D. At each remaining target, A'(d)=z_d B'(d), so B'(d) is a nonzero signed divisor of R_D. For each signed divisor there are at most m-1 possible d, since B' is nonconstant of degree <=m-1. The block count is therefore bounded by
  max(n-1, (m-1)+2(m-1) tau(|R_D|)).
This is a constructive local certificate if the relation has been determined and verified for the target set; it is not by itself a method to locate the first unknown targets without scanning.

For any theta>0, tau(N)<=C_theta N^theta. An explicit admissible C_theta is the product over primes p<2^(1/theta) of (1-p^-theta)^(-2); for larger primes e+1<=2^e<=p^(theta e), and for each small prime bound the supremum by the sum of (e+1)p^(-theta e). Take theta=eta/J. Then the block count is at most a computable constant times D^eta. The number of blocks is O_rho(D^(1/(2m+1))); for D with rho D^(2m/(2m+1))>=2 the floor is >=half its argument. Dyadic summation yields E_A(X)=O(X^(1/(2m+1)+eta)). The finite initial segment can be bounded by its length. This proves the theorem.

## 6. Application and precise incremental value
For R284 use y_d=q_d, the eventually unique legal real root, and c1>0 from frozen JX/JW. For every m>=2, the all-fixed-order expansion supplies existence of the needed M=4m remainder. Therefore the finite-order theorem yields the subpower result already proved in JY, now without an infinite Hankel dichotomy or any higher minor certification. More precisely, for every eps>0 choose m>=2 with 1/(2m+1)<eps and eta=eps-1/(2m+1); A=4m gives E_A(X)=O_eps(X^eps). For example m=4 uses only c1..c16 and remainder O(d^-17), gives O(X^(1/9+eta)) at A=16 even if H4=0; m=10 uses c1..c40 and O(d^-41), gives O(X^(1/21+eta)) at A=40. These are existence statements from inherited all-order expansion, not newly calculated coefficients or explicit numeric R284 onsets.

The new finite-data theorem is stronger operationally than JY: a prescribed exponent requires only a finite jet and quantitative remainder, not deciding whether infinitely many Hankel minors are nonzero. A certified upper bound on each coefficient is enough, except for a positive lower bound on |c1|. The proof also preserves the exact local integer relation and its resultant, including composite coordinates. It applies to arbitrary discrete remainders with the stated bound. It does not improve the exact-root asymptotic class beyond JY, and does not prove finiteness or pointwise exclusion. No numerical experiment, formal checker, or independent review was executed for this written proof. All algebraic estimates were author checked.

Next: obtain explicit finite-jet remainder bounds for the original complete observer using finite product log/Faulhaber and Euler-Maclaurin, then a root transfer with effective onset. The determinant theorem now needs only finite upper envelopes rather than delicate signs. In parallel pursue arithmetic pointwise exclusions for the original C; the resultant cover is a bound and conditional local certificate, not a global no-root proof.
