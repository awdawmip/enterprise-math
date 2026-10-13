# Complete two-list CRT QR indices: a uniform prefix and paid-cost lemma

Status: NEW_SCOPED_PAPER_LEMMA / AUXILIARY_DIRECTED_NONBLIND / NO_NATIVE_RESULT_OR_SOURCE_WRITE.
Auxiliary identity: UNKNOWN. Root mathematical direction and supplied candidate formulas: EM-DVR-FBF223, original Owner unchanged.
Formal parent task supplied by Root: RS-FACTOR-BLIND-QR-CRT-PREFIX-INDEX-COST / TP2-F3369CF79B942BBC9DAB, Source803be63388c22d91e637c580e4a8bf65e3278964. This note is assistance for the actual selected Researcher, not another Task, session, claim, authority or decisive native review.
Objects: explicitly external integer and finite-field arithmetic. Fixed project basis remains Heartbeat World native X6; no native-state bridge, Foundation, Working Truth, general factoring no-go or new-method novelty is inferred.

## Precise model and conclusions

Let M be a squarefree product of k distinct odd primes, with M=1 permitted. Let gcd(N,M)=1, let c be any integer, and let L>=1 be an integer. Set

    I_M(x)=1 iff x^2-N is a square, including zero,
                    modulo every prime dividing M,
    C_L(c)=sum_(t=0..L-1) I_M(c+t),
    a_p=(p+chi_p(N))/2,
    S=product_(p|M) a_p,  delta=S/M.

For M=1 put S=delta=1. Every a_p>=1. The exact complete-period density and the standard elementary lower bounds are

    delta >= 2^(1-k)/(k+2),
    M >= (k+2)!/2.                                      (A)

The new uniform prefix discrepancy bound is

    |C_L(c)-delta L|
       <= delta (1+log M)
            sum_(d|M, d>1) 5^omega(d)*sqrt(d)
       <= delta 6^k sqrt(M)(1+log M).                    (B)

Here log is natural, omega(d) counts distinct prime divisors, and the first sum is zero at M=1. The statement is uniform in N, c, L, and the choice of squarefree odd M. It includes L<M without deriving an unjustified prefix density from complete-period density.

Now partition the primes arbitrarily into coprime group moduli P,Q, and materialize their COMPLETE accepted CRT residue lists A,B, of cardinalities S_P,S_Q. Empty groups have modulus1 and the singleton list{0}. CRT gives

    S_P S_Q=S,  S_P+S_Q>=2sqrt(S).

Assume each nontrivial group has its COMPLETE list actually materialized, at a cost at least lambda>0 per real list entry, and EVERY accepted prefix candidate is inspected at a cost at least mu>0. A modulus1 group may be a virtual singleton{0}; it is not charged an imaginary allocated cell. Let E denote the number of real materialized list entries. These are separate additive charges, with fixed lambda,mu and no free or shared preprocessing:

    W >= lambda E + mu C_L(c),
    E >= sqrt(S) when M>1.

Indeed, for two nontrivial groups E>=S_P+S_Q>=2sqrt(S). If one group is virtual, the actual other list has S entries, so E>=S>=sqrt(S). If M=1 both groups may be virtual and E=0; C_L=L gives the bound directly. The stronger additive inequality W>=lambda(S_P+S_Q)+mu C_L is available only when both singleton/list arrays are actually charged. The theorem below needs only the robust real-entry account.

Additional local tables, inverses, validation, sorting, rank/select, heap, arithmetic-width and verifier operations may only add work. No balanced partition is assumed.

Define

    K=K_2(L)=max {j>=0:(j+2)!/2<=L^2},
    Phi(L)=(6sqrt(2))^K (K+2)(1+2log L).

Then the following finite inequality holds for EVERY allowed modulus, including M much larger than any polynomial in L:

    W >= min(lambda,mu) L/Phi(L).                       (C)

Consequently,

    W >= L exp(-O(log L/log log L)) = L^(1-o(1)).        (D)

The argument covers precisely complete TWO partial lists plus complete prefix-survivor enumeration. It is not a lower bound for rank-only queries, early stopping or early successful factor extraction, additional selective predicates, prebuilt/compressed/shared structures, arbitrary implicit CRT representations, or general factoring algorithms.

## The one external theorem: exact Weil parameters and checked source

We use only the classical prime-modulus Kloosterman bound. In the notation

    e_p(v)=exp(2pi i v/p),
    Kl(A,B;p)=sum_(u in F_p^times) e_p(Au+B/u),

if p>2 is prime and A,B are both nonzero modulo p, then

    |Kl(A,B;p)|<=2sqrt(p).

The exact statement is Theorem1 on page1 of Gergely Harcos, [Weil's bound for Kloosterman sums](https://users.renyi.hu/~gharcos/weil.pdf). The author's PDF was actually opened by the connected web reader; its definition and parameters appear on parsed lines5–21. A short parameter excerpt is: “Let p > 2 be a prime number. Let a and b be integers coprime to p.” The full PDF was downloaded from that exact author-hosted URL: 229506 bytes, SHA256 ee17d5dff37e572d0a00727954cb5cbab0ea57693f90e010a4e6446edb2cc394. Its first page was locally extracted with pdftotext and the theorem parameters/definition were actually read. The read-only PDF, first-page text and actual-byte record WEIL_PRIMARY_REFERENCE_ACTUAL_BYTES.json preserve the evidence. This is a checked theorem reference, not a guessed citation or reliance solely on a search snippet.

Original attribution: Andre Weil, On Some Exponential Sums, PNAS34(5),1948,204–207, DOI10.1073/pnas.34.5.204. Its bibliographic metadata was verified through [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC1079093/); the original article's full text was not read. The operational theorem above was read in Harcos's complete author-hosted proof. No novelty is claimed for Weil, Gauss identities, CRT, or completion.

## Derivation of the local mixed sum, including its sign

Fix an odd prime p not dividing N, and write chi=chi_p with chi(0)=0. Let

    tau=sum_(v modp) chi(v)e_p(v).

The standard Gauss change of variables gives, also at z=0,

    chi(z)=tau^(-1) sum_(u!=0) chi(u)e_p(uz).

For completeness tau!=0 follows from |tau|^2=p: replace the two nonzero summation variables by (v b,b), sum in b, and use sum_(v!=0)chi(v)=0. Also

    sum_x e_p(u x^2+h x)
       = chi(u)tau e_p(-h^2/(4u))    (u!=0),

by completing the square and counting the square roots of each residue. All factors2,4,u are invertible since p is odd.

Therefore, for every h modulo p,

    B_p(h):=sum_x chi(x^2-N)e_p(hx)
       = tau^(-1) sum_(u!=0) chi(u)e_p(-Nu)
                             sum_x e_p(ux^2+hx)
       = sum_(u!=0) e_p(-Nu-h^2/(4u)).                 (E)

The two chi(u) factors multiply to1; the same tau cancels, including its complex sign for p=3 mod4. There is no extra chi(-1), Gauss phase or absolute-value substitution.

When h!=0, (E) is the ordinary Kloosterman sum with A=-N and B=-h^2/4, both nonzero modulo p. The checked Weil theorem applies and gives |B_p(h)|<=2sqrt(p). When h=0, the second parameter is zero and we do NOT invoke the nondegenerate theorem: (E) reduces exactly to sum_(u!=0)e_p(-Nu)=-1.

## Zero-inclusive local Fourier coefficients

The exact indicator is

    I_p(x)=(1+chi(x^2-N)+1_(x^2=N))/2.

This formula includes zero; (1+chi)/2 alone would give the incorrect half-weight there. Define

    H_p(h)=sum_(x modp) I_p(x)e_p(hx).

There are r_p=1+chi(N)<=2 roots of x^2=N. At h=0,

    H_p(0)=(p-1+r_p)/2=(p+chi(N))/2=a_p.               (F)

At h!=0, the constant term sums to0, and the root correction has absolute value at most r_p. Thus

    |H_p(h)| <= (2sqrt(p)+2)/2 = sqrt(p)+1.

Since a_p>=(p-1)/2,

    |H_p(h)|/a_p <= 2/(sqrt(p)-1) <= 5/sqrt(p),        (G)

where the last inequality is equivalent to3sqrt(p)>=5 and holds for every p>=3. Zero roots are charged explicitly, rather than discarded or treated as an uncontrolled exceptional set.

## CRT Fourier factorization and the correct frequency conductor

For M>1 define H_M(h)=sum_(x modM) I_M(x)e_M(hx). Let b_p be the inverse of M/p modulo p. CRT yields the EXACT factorization

    H_M(h)=product_(p|M) H_p(h b_p modp).

In particular, the local frequency is zero precisely when p divides h. Set

    d=M/gcd(h,M)        (1<=h<M).

Because M is squarefree, the primes of d are exactly the primes where the local additive frequency is NONZERO. Keeping the zero-frequency mean a_p from(F), and using(G) only at the nonzero frequencies, gives

    |H_M(h)| <= S * 5^omega(d)/sqrt(d).                (H)

We never claim a uniform O(C^k sqrt(M)) bound for all nonzero h. Such a claim can fail when h is divisible by a large part of M, because those local factors contribute means of order p/2. Equation(H) retains those means, and the subsequent conductor completion accounts for them.

The shift c enters Fourier inversion as the unit phase e_M(-hc). Hence

    C_L(c)-delta L
      = (1/M) sum_(h=1..M-1)
            H_M(h)e_M(-hc) sum_(t=0..L-1)e_M(-ht).    (I)

This is exact for arbitrary integer c and L, with no alignment or unproved density assumption on the prefix.

## Completion at each conductor

Fix d>1 dividing M. The frequencies in(I) of this conductor are exactly

    h=(M/d)b,  1<=b<d,  gcd(b,d)=1.

The geometric progression then has frequency b/d. For theta not an integer,

    |sum_(t=0..L-1)exp(2pi i theta t)|
       <=1/(2||theta||).

Summing over all b=1,...,d-1, rather than only units, and pairing b and d-b (d is odd), gives

    sum_(gcd(b,d)=1) |sum_(t=0..L-1)e_d(bt)|
       <= d sum_(j=1..(d-1)/2) 1/j
       <= d(1+log d).                                (J)

The bound is independent of L, so it also covers incomplete blocks and multiple periods. Insert(H),(J) into(I):

    |C_L(c)-delta L|
      <= (S/M) sum_(d|M,d>1) [5^omega(d)/sqrt(d)]
                              d(1+log d)
      <= delta(1+log M) sum_(d|M,d>1)5^omega(d)sqrt(d).

The divisor sum is

    product_(p|M)(1+5sqrt(p))-1
       <=6^k sqrt(M),

because each1+5sqrt(p)<=6sqrt(p). This proves(B). For M=1, Fourier has no nonzero frequencies and C_L=L exactly.

In particular, for every fixed epsilon>0, if M<=L^(2-epsilon), distinctness implies k=O(log L/log log L), so6^k sqrt(M)(1+log M)=o(L). Hence C_L(c)>=delta L/2=L^(1-o(1)) uniformly. This is a justified PREFIX result, rather than an inference from S/M alone.

## Elementary density and factorial facts

Order the odd primes p_1<...<p_k. Since p_i>=i+2 and a_p>= (p-1)/2,

    delta >=2^(-k) product_i(1-1/p_i)
           >=2^(-k) product_i(i+1)/(i+2)
           =2^(1-k)/(k+2),

and

    M>=product_i(i+2)=(k+2)!/2.

The same bounds apply to ANY subset of these primes, using that subset's own cardinality. The empty product k=0 gives density1 and modulus1.

## Fully finite paid-cost bound when M<=L^2

Let

    D(M)=6^k sqrt(M)(1+log M).

From(B),

    C_L(c)>=delta (L-D(M)).

When M<=L^2, the factorial fact gives k<=K_2(L)=K.

If D(M)<=L/2, then

    W>=mu C_L(c)>=mu delta L/2
      >=mu L/[2^k(k+2)]
      >=mu L/[2^K(K+2)]
      >=mu L/Phi(L).                                 (K)

If D(M)>L/2 and M>1, then sqrt(M)>L/[2*6^k(1+log M)]. The REAL complete-group entries instead give

    W>=lambda sqrt(S)=lambda sqrt(M)*sqrt(delta)
      >lambda L sqrt(delta)/[2*6^k(1+log M)]
      >=lambda L/
          [sqrt(2)*(6sqrt(2))^k sqrt(k+2)(1+log M)]
      >=lambda L/Phi(L).                             (L)

For the last step use k<=K, log M<=2log L, and sqrt(2)*sqrt(K+2)<=K+2. At M=1 use C_L=L directly, rather than any virtual list charge. No prefix count is assumed positive in this second case; storage/preparation supplies the lower bound. The costs are not charged twice.

## Extremely large M: shortest prime prefix, not a false bound on k

Suppose M>L^2. Let j be the smallest index with

    R_j=product_(i=1..j)p_i>L^2.

Then R_(j-1)<=L^2, so the factorial fact gives j-1<=K, hence j<=K+1. This constrains the SHORT prefix only; it does not assert k_total<=K.

Its complete accepted count satisfies

    S_j=product_(i=1..j)a_(p_i)
       >=R_j 2^(1-j)/(j+2)
       >L^2/[2^K(K+3)].                              (M)

Every remaining a_p>=1, including the smallest possibility a_3=1. Thus multiplying the remaining factors cannot decrease the accepted count:

    S>=S_j,
    W>=lambda sqrt(S)>
         lambda L/[2^(K/2)sqrt(K+3)]
         >=lambda L/Phi(L).                          (N)

The last inequality follows from6^K>=1,1+2log L>=1 and K+2>=sqrt(K+3). This is valid even if M is super-polynomial in L and k_total is far larger than log L. It closes that possible uniformity loophole without an unproved bound on the total prime count.

Combining(K),(L),(N) proves(C).

## Boundary values and asymptotics

For L=1, K=0 and Phi(1)=2. At M=1, both groups can be virtual and C_1=1, so W>=mu. At M>1, at least one nontrivial group has an actual complete nonempty list, so E>=1 and W>=lambda. Both imply(C), whose right side is min(lambda,mu)/2. Thus L=1/K=0 is covered directly with no imaginary unit-entry charge.

Empty or unbalanced groups retain S_P S_Q=S; AM-GM is used only for two real lists, while one real group has S actual entries. Any c-shift only changes the phase in(I), so there is no c-dependent loss. The predicate includes zero and every prime satisfies p∤N, which are the exact hypotheses used in(F), the local positivity a_p>=1, and the nondegenerate Kloosterman parameters.

Since K_2(L)=O(log L/log log L), log Phi(L)=O(log L/log log L), proving(D). In the Fermat application set L=T+1 and retain the true endpoint. The theorem concerns the work of inspecting ALL accepted offsets through that endpoint in the declared paid model. It does not claim that a particular run cannot terminate earlier on a factor, nor that a single rank query alone has this cost.

## What remains outside this lemma

The requested complete-list model now has a uniform paper bound, so its L<M density gap is closed under its exact assumptions. A scheme that never materializes both complete lists, amortizes them, prunes by an additional predicate, batches survivors without per-candidate inspection, or only queries rank/select has not inherited this lower bound. Such a scheme needs its own construction/retrieval/bit-cost analysis and matched comparator. Prime powers and even primes are not silently added to the conductor argument; their local Fourier estimates would be a different extension.

No old63/3043 checks, frozen600/1400 experiments, producer/scientific imports, census, KQB, native registration, claim or Source mutation is performed in this paper unit. The prior prime-power report remains frozen. This is a new scoped deduction using a classical checked theorem, not a general factorization complexity claim or a new mathematical Task. Root and the actual Researcher decide adoption.

