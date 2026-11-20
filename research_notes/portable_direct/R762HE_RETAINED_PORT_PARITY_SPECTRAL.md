# R762HE — Exact retained-endpoint parity and seven-character spectral certificate for the S6 Port candidate

Status: AUTHOR-PROVED CONDITIONAL CANDIDATE / EXACT INTEGER CHECK PASS / NOT_REVIEWED.
Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS; publication TP2-8B7E13C5904A2D6F1142.
Continuation: R762HD, Draft PR #2863 at fe573942ec85d02ebfc513880a4cc53195b919c0; original author provenance EM-X6-3050F6.
Frozen science: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389, including P000 and the X6 native Cell torsor. Current normative policy read separately.

## Model and observer

This theorem holds for the explicitly defined **candidate** R762HD gate, not an admitted primitive TRIADIC_CLOSURE_E event. The native spatial chart is the signed six-axis Cell torsor C in Z^6, anchored at one chosen Cell, and time is an independent event index. There are 15 unordered named Ports P subset {0,...,5}, |P|=2. One unsigned source step P -> Q is allowed exactly if |P intersect Q|=1. Write S(P,Q)=P union Q (three axes), a(P,Q) for its unique retained/common endpoint, and b(P) in F_2^6 for the indicator of P.

A signed branch additionally chooses sigma in {+1,-1}, giving C'=C+sigma*h_S and the candidate relational Link update ell'=ell-sigma*h_S; positive BRC weights count all named branches without signed-mass cancellation. Here h_S=sum_{i in S}e_i. The coefficientwise mod-two readout of C is meaningful for any signed Cell chart and is not the complete Cell state. The proposed triple is a composite spatial path label; force-closure admission remains open.

## Theorem HE1: retained-endpoint parity identity

For an arbitrary length-m Port walk P_0,P_1,...,P_m, let S_t=P_(t-1) union P_t and a_t=P_(t-1) intersect P_t. Define the F_2^6 residual

    r_m = sum_{t=1}^m e_(a_t)   (mod 2).

For **every** assignment of signed branch labels sigma_t, its full Cell displacement obeys

    C_m-C_0 (mod 2) = b(P_0)+b(P_m)+r_m.                       (HE1)

Proof. Over F_2, sigma_t=+1 and sigma_t=-1 both reduce to 1. Since the two Ports have precisely one shared vertex, their two incidence vectors sum to indicators of the deleted and inserted axes. Therefore b(S_t)=b(P_(t-1))+b(P_t)+e_(a_t). Summing telescopes the Port indicators, leaving (HE1).

If P_m=P_0, the Cell parity residual equals r_m exactly. A signed full-Cell return therefore requires every native axis to be retained an even number of times. This is a sign-independent **necessary filter**, not a sign-completion existence claim. For odd m a zero Cell return is impossible: total coordinate displacement has parity 3m=m mod 2, whereas a zero vector has even total parity. At each t the chosen sigma remains part of the full positive-BRC source record.

## Theorem HE2: exact all-length parity-zero Port-return counts

Let H_m be the number of unsigned, ordered, named Port-return walks of length m starting at any fixed Port P_* for which the triple-support parity is zero in all six coordinates. Thus H_m counts the support of a necessary sign-agnostic condition for eventual zero Cell displacement, **not** signed return multiplicities. Let

    U_m = (8^m+5*2^m+9*(-2)^m)/15

be the R762HD number of all unsigned named Port returns.

For each x=(x_0,...,x_5) in {+1,-1}^6 define a real symmetric 15-by-15 matrix

    B_x[P,Q] = x_a   if P,Q are adjacent and {a}=P intersect Q,
                0     otherwise.

For k=0,1,2,3 define B_k as a representative B_x with exactly k negative x_i, and let T_k(m)=tr(B_k^m). Then for every integer m>=0,

    H_m = 0                                               if m is odd,
    H_m = [T_0(m)+6*T_1(m)+15*T_2(m)+10*T_3(m)]/480       if m is even.       (HE2)

The exact characteristic polynomials, verifiable solely with integer matrix arithmetic, are

    det(XI-B_0)=(X-8)(X-2)^5(X+2)^9
    det(XI-B_1)=(X+2)^5(X^2-2X-32)(X^2-2X-2)^4
    det(XI-B_2)=X^3(X+2)^2(X+4)(X^2-2X-4)^3(X^3-2X^2-28X+32)
    det(XI-B_3)=X^5(X^2-28)(X^2-2X-6)^2(X^2+2X-6)^2.

Proof. The parity-zero indicator of a sequence of triple supports is the Fourier projector
    2^-6 sum_{x in {+/-1}^6} prod_{t=1}^m prod_{i in S_t} x_i.
Let W_x[P,Q]=prod_{i in P union Q}x_i for adjacent P,Q and 0 otherwise. The walk sum is (W_x^m)[P_*,P_*]. Define diagonal D_x[P,P]=prod_{i in P}x_i. Since x_i^2=1, direct multiplication gives
    (D_x W_x D_x)[P,Q] = x_(P intersect Q)=B_x[P,Q].
Thus the diagonal walk sum is the same for W_x and B_x. For a fixed number k of negative signs, axis-permutation covariance makes the sum of diagonal entries over all such x independent of P_*. Consequently the sum at P_* equals binom(6,k)*tr(B_k^m)/15. Finally B_(-x)=-B_x, so opposite sign-character classes cancel for odd m and pair for even m, giving (HE2). The listed polynomials follow by exact 15-by-15 integer determinants; the included standard-library verifier independently rebuilds their coefficients with Newton trace identities. This is a finite, complete matrix certificate.

## Theorem HE3: exact spectral asymptotics

For even positive m, put alpha=1+sqrt(33). Then

    H_m/U_m = 1/32 + (3/16)*(alpha/8)^m + O((3/4)^m)     as m -> infinity through even m.      (HE3)

In particular, the proportion of Port-return histories passing the six-bit parity obstruction tends to exactly 1/32. Proof: B_0 has unique eigenvalue of magnitude 8; B_1 has one eigenvalue alpha and all others of magnitude <6. The cubic of B_2 has three real roots, respectively in (-5,-4), (1,2) and (5,6), while all its other eigenvalues have magnitude <6. All B_3 eigenvalues have magnitude <=sqrt(28)<6. Hence T_0(m)=8^m+O(2^m), T_1(m)=alpha^m+O(6^m), T_2(m),T_3(m)=O(6^m) for even m. Insert these into (HE2) and divide by U_m=(8^m+14*2^m)/15 for even m. The leading coefficient is (1/480)/(1/15)=1/32, and the next coefficient is (6/480)/(1/15)=3/16. All remaining terms are O((6/8)^m).

## Exact finite audit

The attached Python standard-library verifier performs two algebraically distinct calculations: (i) full 15-state signed-common-endpoint matrix traces and integer Newton characteristic polynomials; (ii) a 15 x 64 Port/parity positive integer dynamic program for m=0,...,16. They agree exactly. The direct telescoping parity identity is also exhaustively checked for all Port walks up to four transitions. The even-length results are:

| m | U_m: unsigned Port returns | H_m: parity-zero returns |
|---:|---:|---:|
| 0 | 1 | 1 |
| 2 | 8 | 8 |
| 4 | 288 | 168 |
| 6 | 17,536 | 4,960 |
| 8 | 1,118,720 | 177,536 |
| 10 | 71,583,744 | 7,289,184 |
| 12 | 4,581,302,272 | 333,869,824 |
| 14 | 293,203,116,032 | 16,704,767,360 |
| 16 | 18,764,998,508,544 | 895,432,338,432 |

Audit status: AUTHOR_CHECK_PASS; independent review NOT_REVIEWED. The asymptotic and all-m formulas are deduced algebraically from the complete finite characteristic-polynomial certificate, not extrapolated from the table.

## Scientific and operational boundary

HE1 adds a portable six-bit **retained-axis residue** whose presence is determined by the ordered Port transitions, independently of sign. HE2 compresses 64 parity characters to four symmetric matrix classes for even lengths while retaining exact positive-BRC counts. It gives a sharp necessary obstruction to a primitive Cell/Port return. Signed event existence, actual sign solutions for a parity-zero walk, native Link and rotation legality, and TRIADIC_CLOSURE_E force closure remain separate unsolved obligations; so do the pre-existing q9 full-vector period/lift problems. No P000, Working Truth, or Foundation modification is proposed.

Next discriminating task: classify which parity-zero walks admit a genuine common signed solution B_path*sigma=0, compare exact signed return fibers to the parity-filter counts, and restrict the transfer to an actually typed P000-compliant primitive force/Cell/Link/Port/time permission predicate. Retain original ordered paths, multiplicities, branch signs, and provenance until an observer-safe quotient is proved.
