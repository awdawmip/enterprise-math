# Growing squarefree QR wheels with paid explicit tables have near-linear cost

Driver-ID: EM-DVR-FBF223 / CONTROL_PLANE
Original-Session: MCP-cd5eefdde49843898b2a70c1af94d8dd
Original-Driver-Authority: DA-A1DB35C00ED2F8C2A9FA
Task context: RS-FACTOR-BLIND-SQUARE-MULTIPLICATIVE-SHELL-BRIDGE
Publication context: TP2-A712090E5314373E5447
Original frozen RR: RR-C5769D6B237D02BFF025
Status: ROOT_DRIVER_REVIEW_ADDENDUM / NEW_CONDITIONAL_PROOF / PARENT_OPEN

This is a new conditional mathematical derivation within the original Owner's review, not a rerun or replacement of the frozen RR. Root's prior aliases EM-DVR-FBF223,EM-DVR-4C90FB,EM-DVR-C1A1D9,EM-DIRECT-E1F2B6,EM-DIRECT-FA0C27,EM-DIRECT-49ADE6 are disclosed. Auxiliary paper review is UNKNOWN / DIRECTED_NONBLIND, not a new native Researcher or independent execution identity. All objects and costs below belong to the explicitly declared external integer/finite-field arithmetic model. No native X6, Foundation, Working Truth or General Math Tool promotion is inferred.

## Scope and exact statement

For an odd semiprimeN=pq with3<=p<=q, letc=ceil(sqrt(N)),T=(p+q)/2-c>=0 andL=T+1. Definez_N(t)=(c+t)^2-N. Consider precisely the standard quadratic-residue conjunction

    F_N(t)=1 iff z_N(t) is a square residue (including0)
                  modulo every primeell dividingM,

whereM is the product ofk distinct odd primes andgcd(N,M)=1. M and the primes may depend on publicly computedN and on the instance size; no fixed-M assumption is made. The trueT is retained becausez_N(T)=((q-p)/2)^2.

The implementation constructs allM cells of its period table for this instance, at cost at leastlambda>0 per cell, and then inspects each retained candidate in0..T at cost at leastmu>0. These are distinct additive operations and are not charged twice. Lambda,mu are fixed positive constants in this accounting model, with no free or cross-instance-amortized preprocessing. WriteW for this accounted work.

For integerL>=1, define

    K(L)=max{k>=0 : (k+2)!/2<=L}.

Then uniformly inN and the chosen primes,

    W >= min(lambda,mu)*L / ((K(L)+2)*2^K(L)).

In particular, asT grows,

    W >= L*exp(-O(log(L)/log(log(L)))) = T^(1-o(1)).

Thus this explicit-table-and-enumeration QR-wheel implementation cannot achieve a fixed positive power improvement over a linear scan. This permits constant-factor and subpolynomial-factor improvements, including possible polylogarithmic improvements. The result does not assert thatW isOmega(T) for a growing period.

## Proof of the exact period density

Fix an odd primeell not dividingN, and letchi be its quadratic character withchi(0)=0. The number of pairs(x,y) satisfyingx^2-y^2=N inF_ell equalsell-1: since2 is invertible, eachu=x-y!=0 gives the uniquev=x+y=N/u and hence a uniquepair(x,y). Counting instead byx gives

    ell + sum_x chi(x^2-N) = ell-1,

so the character sum is-1.

The number of roots ofx^2=N isr=1+chi(N). Ifn_plus countsx withchi(x^2-N)=1, the character sum and total count imply

    2*n_plus+r-ell=-1.

The accepted square residues include bothn_plus positive-character positions andr zero positions, hence the number of accepted residues is

    a_ell=n_plus+r=(ell+chi(N))/2 >= (ell-1)/2.

The shiftx=c+t permutes residues, so this is also the offset count. By CRT, an entire period has exactly

    S=product_(ell|M) a_ell,
    delta=S/M>=2^(-k)*product_(ell|M)(1-1/ell).

Order the distinct odd primes asell_1<...<ell_k. Sinceell_i>=i+2,

    product_i(1-1/ell_i)>=product_i((i+1)/(i+2))=2/(k+2),

and therefore

    delta>=2^(1-k)/(k+2),
    M>=product_i(i+2)=(k+2)!/2.

The empty productk=0 is included andM=1.

## Prefix count and paid-cost bound

The prefix0..T has exactlyL offsets and containsfloor(L/M) complete periods. For the pure QR conjunction its candidate countC obeys

    C>=floor(L/M)*S.

IfM<=L, floor(L/M)>=L/(2M), so

    C>=L*delta/2>=L/(2^k*(k+2)).

SinceM>=(k+2)!/2 andM<=L, k<=K(L). The denominator2^k*(k+2) increases withk; thus

    W>=mu*C>=mu*L/(2^K(L)*(K(L)+2)).

IfM>L, the full explicit table alone costsW>=lambda*M>lambda*L, which is at least the claimed bound. Combining the two cases gives the uniform finite inequality. It also coversT=0 throughL=1.

The factorial estimate givesK(L)=O(logL/loglogL) asL tends to infinity (indeedK(L)~logL/loglogL). Hence log((K(L)+2)*2^K(L))=O(logL/loglogL)=o(logL). Fixedlambda,mu do not change the exponent, proving the near-linear lower bound. No prime-distribution theorem, factor oracle or numerical experiment is used.

## Boundaries and useful next direction

This theorem is specifically about the pure QR conjunction, squarefree oddM coprime toN, a freshly paid complete table, and enumerating each survivor. Additional selective predicates cannot inherit this survivor-density bound without their own proof. It does not cover compressed CRT or implicit period representations, reuse/amortization, batch certificates that avoid inspecting each survivor, nonperiodic/adaptive search, or other algebraic factoring methods. If a chosen modulus reveals a factor bygcd(N,M)>1, that early gcd success lies outside this offset-scan model. No bound on general factoring complexity follows.

The new result strengthens the generic paid-period boundW>=2sqrt(lambda*mu*(T+1)) for this actual QR-filter family: its period contains many survivors, not an assumed unique true residue. It makes the next meaningful branch precise: an implicit/CRT prefix-index method must account for its construction, retrieval and all candidate checks, then demonstrate benefit against an equally optimized matched wheel/Fermat comparator beyond near-twins. Merely increasing an explicitly materialized QR period cannot provide a fixed-power improvement in this model. This is a research direction proposal, not a newly published canonical Task or an S1/S2/S3 result.

## Current actual provenance and admission state

Root actual continuation559 and fullRR artifact561 bind the original frozen RR's complete bytes atSource406f74e0e2fa833389245ebb26fc24e6e777679b. Root verified all13 Source files90345B, including all10 frozen scientific outputs64999B. Original RR SHA2561149fb488e66bdff40cd52b79b1566400c4691b8254ec884aa113a4a4d7c934f and raw NEGATIVE_BOUNDARY remain unchanged; the frozen600-case experiment and1400-row checker were not rerun.

Actual current review-flow562 (bridge5014,terminalcomment6135887745,Sourcea84a011d6e2644a32cd871c1032697fb571acef7) confirms the original operational ACCEPTED reviewDR-B819FB64CA4E7836CA35 byEM-DVR-240A2C. Its full2030B record and3580B report were cold-verified. Root consumes that completed review without creating a duplicate acceptance. The remaining control state isAWAITING_FOLLOWUP_TASKSET_PUBLICATION; whole-Task completion is not claimed.

Root's earlier generic cost report and its auxiliary paper check were actually published by originalDriver request565 and full-byte cold-verified atSource9695951e57c4ffd7b4e100955ce758053efc7c0f underdriver_reviews/mcp/MCP-cd5eefdde49843898b2a70c1af94d8dd/439ae263bb3a33f6a462/. The Root report8939B hasSHA2567f14d49d506e90f13e271310a45e9caa072caffde6334154f52ad04436c1bd5f; the auxiliary3404B review hasSHA25662d3c4623b61a050bdb9f63de8c8a23f45ca44a9e746d4a2f470050d2818e803. That publication creates neither a new native DR nor Task completion. This new QR addendum likewise remains a faithfully preserved candidate proof until any separately authorized admission. The mathematical mother objective staysOPEN and the originalOwner remains unchanged.
