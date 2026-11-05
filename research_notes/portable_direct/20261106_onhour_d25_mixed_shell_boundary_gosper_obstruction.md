# D25 — exact bottom/middle cubic boundary and rational Gosper obstruction
2026-11-06 · TASK_RESEARCH · AUTHOR-SIDE EXACT DERIVATION / FINITE VERIFIED · UNREVIEWED / NOT_ADMITTED.
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; immutable scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3.
Research logical conversation: chatgpt-research-onhour-enterprise-math-20260923; exclude maintenance chatgpt-hourly-enterprise-math-20260921.

## A. Exact new cross-shell boundary
Let p=6m+1 be prime >3, h=3m, a_k=(2k)!(3k)!/(216^k(k!)^5), and u_j=a_(h-j)/p for 0<=j<=m. Note that u_m=a_(2m)/p has p-adic valuation -1. Put
G_h(j)=(2h-2j+1)(3h-3j+2)(3h-3j+1),
P_h(j)=36(h-j)^3-G_h(j)
= -18j^3+(54h-27)j^2+(-54h^2+54h+13)j+18h^3-27h^2-13h-2.
Then the following identity holds in Q, with **no reduction or truncation**:

sum_(j=0)^(m-1) P_h(j) a_(h-j)/p
 = (4m+1)(p+1)a_(2m) - (9m+1)(9m+2)a_(3m).      (A)

Proof: original factorial ratios give
u_(j+1)/u_j=36(h-j)^3/[(2h-2j-1)(3h-3j-1)(3h-3j-2)].
The denominator equals G_h(j+1), so
G_h(j+1)u_(j+1)-G_h(j)u_j=P_h(j)u_j.
Sum from j=0 to m-1 and use G_h(m)=p(p+1)(4m+1), G_h(0)=p(9m+2)(9m+1). QED.

Valuations v_p(a_(2m))=0, v_p(a_(3m))=1 imply
sum_(j=0)^(m-1) P_h(j)u_j = a_(2m)/3 (mod p).   (B)
This is a nonzero bottom/middle boundary for a cubic moment; p divides G_h(m), but u_m has valuation -1. Equation (A) supplies both p-adic digits when the prior proven seed u_0 mod p² is consumed.

## B. Exact obstruction to a standalone rational Gosper telescoper
For any fixed h in Q, set
R_h(j)=36(h-j)^3/[(2h-2j-1)(3h-3j-1)(3h-3j-2)]
and L_h(f)=R_h(j)f(j+1)-f(j).
If L_h(f) is polynomial and f in Q(j), then f must be a polynomial divisible by G_h(j). Moreover
L_h(G_h q)=36(h-j)^3q(j+1)-G_h(j)q(j)
has degree deg(q)+3 for every nonzero polynomial q. Consequently the quotient of polynomial weights by rational Gosper differences is **exactly three-dimensional**, with representatives 1,j,j². In particular, there is no rational f satisfying L_h(f)=3p-2-6j (p=2h+1), nor any other nonzero polynomial RHS of degree <=2.

Proof: in any integer-shift orbit of poles of rational f, a leftmost pole alpha would require a zero of R_h at alpha-1, forcing alpha=h+1, while a rightmost pole beta would require a pole of R_h at beta. The poles of R_h are h-1/2,h-1/3,h-2/3, none in h+Z: contradiction. Hence f is polynomial. The three poles of R_h require G_h(j)|f(j). For f=G_h q, the displayed polynomial difference has leading coefficient -18 times that of q and degree deg(q)+3. No image contains a nonzero weight of degree <=2. Repeated leading-term elimination modulo such images reduces any polynomial weight uniquely to degree <=2. QED.

## C. Executed exact verification and significance
The companion integer checker independently reconstructs original factorial p-units and verifies (A) modulo p² and (B) modulo p for all 80 primes p<=997 with p=1 mod6, zero failures. An additional independent Fraction evaluation verifies the exact rational identity and every telescoping step for p=13 and p=19.

p=13: bottom boundary 95, starting boundary 78, signed cubic sum 17 (mod169), first digit 4 (mod13).
p=19: bottom 29, start 190, cubic sum 200 (mod361), first digit 10 (mod19).
p=67: 991 - 2278 = 3202 (mod4489).
p=373: 74905 - 69378 = 5527 (mod139129).

Theorem B specifically excludes a **characteristic-zero, p-independent, one-channel rational antidifference** for the original middle weight. It leaves p-dependent or multichannel telescopers open. The next discriminating unit is to couple the original bottom compensation D_p=(B_p-V_h)/p mod p² to the three remaining moment classes, while preserving all signed boundaries and the original source observer. The mother target Delta_p-R_p=0 modulo p for all p=13,19 modulo24 stays OPEN.

Status: author-side theorem and finite verification, NOT native H0/B0 experiment, NOT formal Source Result/review. Native p373 fixed divided-power [X]U mod139129/rank/semilinear eta-kappa/odd Green-Hesse remains NOT_EXECUTED, support issue #1559 still OPEN and unassigned as last observed. Prior read-only control request onhour11-20261106-0504-d25-readonly-cont was reconciled as SUCCEEDED / execution_authorized=false. No own CLAIM/open/run is asserted.