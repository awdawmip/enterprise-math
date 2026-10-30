# D25/LIFT GH-155–GH-156: CM(-24), inert branch, and exact integer trace

2026-10-30 (+08). AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. Research logical lane: chatgpt-research-hourly-enterprise-math-20260923. These GH labels are author-side working identifiers, not new native Task registrations. Parent D25/LIFT/JT2 remains OPEN; task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. P000 ACTIVE_LOCKED and frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged.

## GH-155 — exact CM identification and inert Hasse zero

For p ≡ 3 (mod 8), p>=11, fix rho²=2 in F_(p²), B+=(1+2rho/3)/8=1/8+rho/12 and B-=B+^p. The marked elliptic curve is E_B: y²=x(x²+x+B). Note B(1-4B)=1/144 and Norm(B)=1/576, giving good reduction for all these primes.

The standard j formula j=256(1-3B)³/[B²(1-4B)] gives, by exact Q(rho) arithmetic,

j(B+)=2417472-1707264rho, j(B-)=2417472+1707264rho.

Thus both satisfy X²-4834944X+14670139392=0. This is precisely the Hilbert class polynomial H_{-24}(X), whose two roots are the CM j-invariants of the maximal order of Q(sqrt(-6)). The identification of H_{-24} is established by NumberDB / OEIS A305474 (literature below), rather than conjectured from numerical data.

For p ≡19 (mod 24), (-6/p)=-1. The classical Deuring theorem gives supersingular reduction at these good primes. For this exact Weierstrass model the Hasse coefficient is H_p(B)=[X^((p-1)/2)](X²+X+B)^((p-1)/2). Hence the new infinite-subfamily theorem is

p ≡ 19 (mod 24)  ==>  H_p(B+)=H_p(B-)=0.

For p ≡11 (mod 24), the CM prime splits and H_p(B+) != 0. This is a complete CM inert/split classification for the Hasse vanishing at the selected marked parameter, not an all-prime stationary-jet theorem.

## GH-156 — exact integer Frobenius trace on the inert class

Assume p ≡19 (mod 24), q=p². Then (6/p)=+1, so choose eta∈F_p with eta²=6, and rho^p=-rho. The two nonzero rational 2-torsion abscissas are
alpha=(-1+(rho-1)/eta)/2, beta=(-1-(rho-1)/eta)/2,
with alpha+beta=-1, alpha beta=B+, and alpha != beta.

Their exact field norms are:
Norm(alpha)=(5+2eta)/24 = 2*((2+eta)/(4eta))²,
Norm(beta)=(5-2eta)/24 = 2*((2-eta)/(4eta))².
Since (2/p)=-1 and both square factors are nonzero, alpha and beta are NONSQUARE in F_q. Also chi_q(-1)=+1, so -alpha and -beta are nonsquares.

The standard rational 2-division criterion for y²=(x-e1)(x-e2)(x-e3) says (ei,0) is rationally divisible by 2 iff ei-ej and ei-ek are both squares. For (0,0) the obstructing differences are -alpha,-beta; for (alpha,0) and (beta,0), one obstructing difference is alpha or beta. Thus E_B(F_q) has all four rational 2-torsion points and no rational 4-torsion. Its 2-primary subgroup is (Z/2)², so #E_B(F_q)≡4(mod8).

Deuring gives supersingular a_q divisible by p. Weil's bound gives |a_q|<=2p, hence a_q∈{-2p,-p,0,p,2p}. Since q+1≡2(mod8), the group-order congruence requires a_q≡6(mod8). As p≡3(mod8), precisely a_q=+2p meets this condition. Therefore, for EVERY prime p≡19(mod24):

a_(p²)(E_B+)=a_(p²)(E_B-)=2p,
#E_B±(F_(p²))=(p-1)².

This integer-valued infinite-family result uses classical Deuring reduction, the independently displayed 2-torsion norm computation, finite-group 2-division and the Weil bound. It does not assume GH-151 trace reconstruction or any numerical fit.

## Consequences, dependency strength, and frontier

Using imported AUTHOR-SIDE GH-153's exact reflected-tail derivative factorization, H_p(B+)=f(1/144)=0 forces R'_p(9)=0 for all p≡19(mod24); GH-153 transversality yields R''_p(9)!=0 there. Using imported GH-124's S_1=-C H^p, S_1(B+)=0 on the same inert class. These reflected-tail/character-moment deductions are DEPENDENCY-BOUND, not a new independent validation of their imported identities.

For p≡11(mod24), H(B+) !=0, so the source-derived stationary condition requires the OTHER branch K(1/144)=0. If H'(B+)=h1*rho, the relation K=(1-128W)f'-8f at W=1/144 becomes K=4h1/3-8H; the unresolved split-branch theorem is h1=6H. At p=3347, H=783, h1=1351, and 6*783=1351(mod3347), a verified instance, NOT an all-prime proof. R_p(9)=0 and source-original GH-3 remain separate open obligations.

## Exact executed evidence

Python 3 stdlib-only direct Q(sqrt2) j arithmetic and F_(p²) exact enumeration, no float. Scan over 140 primes p<4000 (69 inert, 71 split) directly recomputed H, H' and the reflected-tail derivative, checking the predicted two CM branches (finite test, not proof). Independent integer counts over ten fields p=11,19,43,59,67,83,107,139,163,283 returned traces {-10,38,86,-10,134,134,86,278,326,566}; every inert trace is 2p. Direct H_3347=783 and H'_3347=1351rho. Full executed local script SHA256: 57f098f4b3057481e66d977100a9561a8b2259b704487097151fa4c0ed178cb1; terminal marker PASS_CM24_DIRECT_J_ALGEBRA_AND_BRANCH_CHECK. The entire author-executed script and log are in the dated portable handoff, not a native p=373 divided-power run.

BRC COMPOSE_APPLIED: retain (p mod24, CM field, root labels, rho orientation, exact norms and quadratic characters, group 2-division operations, integral trace, Hasse value, f/K branch, provenance). A single Boolean R'_p(9)=0 loses the true inert H=0 versus split K=0 mechanism. This is a typed finite-field observation result, not native P000/X6 spatial derivation.

Literature: https://numberdb.org/Hilbert_class_polynomials ; https://oeis.org/A305474 ; https://math.mit.edu/~drew/vantage/ElkiesSlides21.pdf ; https://mathoverflow.net/questions/18591/reduction-of-cm-elliptic-curves .

Next unrepeated science: seek an independent CM/Jacobi/Gauss or p-adic proof of the SPLIT-only p≡11(mod24) jet identity H'_p(B+)=6rho*H_p(B+), then separately establish the original GH-3 comparison and R_p(9) vanishing. Native D25 divided-power H0/B0, [X]U mod p², semilinear Frobenius normalization eta and p373 experiments require their own authorized path. Do not alter Source pin, Task owner or the research/maintenance lane separation.