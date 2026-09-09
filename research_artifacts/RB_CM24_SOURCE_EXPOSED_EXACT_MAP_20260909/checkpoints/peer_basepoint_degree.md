# Conditional peer paper review: all base points and degree six

Date: 2026-09-09. Reviewed input: `review-basepoint-degree-conditional.md`, SHA256 `77536b7de0a99d58c54534b9664da921693851095d20fd33eefac375fdd851a4`. The formulas remain those frozen at `341f36bb53c25d97c3ae533a71c92ad273a7b904`.

**CONDITIONAL PASS.** I found no gap in the proposed exhaustive basepoint argument or either degree-six deduction, provided the stated full Norm(A) identity and B0 substitutions pass the source-bound exact checks. This review did not perform those computations, inspect their evolving outputs, or rerun v1. It uses the previously reviewed field/nonzero/O-point facts without reopening that review.

## Conditions and exhaustive support

The Norm identity must retain its exact nonzero factor \(-s u_N^2\) and hold in the full presented curve algebra:
\[
A(R,t)A(R,-t)=-s u_N^2(R+s)(R+3s)(R-r)^2.
\]
The B0 checks must establish that the stated point is on the carrier and that \(A(B_0)=D_0(B_0)=0\); equivalently, \(N(B_0)=0\) implies \(A(B_0)=0\) because \(R(B_0)+2=2-3s\ne0\).

Given these conditions, no other finite A-zero is possible: every finite zero projects to a zero of the norm. The three coordinates \(-s,-3s,r\) are distinct. In particular \(r<-10\), whereas \(-3s>-6\); \(-2\) is distinct from all three as well.

At \(T_-\), the leading term \(a t\) has order one and the remaining summand has order at least two. At B0 the conjugate A-value is \(-2a t(B_0)\ne0\), and the simple norm factor gives order one. Above r, the cover is unramified, and the two A-values cannot both vanish since their difference is \(2at\ne0\). The norm gives a unique zero Z, defined over the stated coefficient field by the displayed \(t_Z\), of order two. Above \(-2\), both t-values are nonzero and the norm of A is nonzero; hence \(R+2\) contributes exactly the two simple zeros \(P_\pm\).

Thus the asserted six-point-degree finite zero divisor of N is exhaustive. The previously checked pole of order six at O confirms the degree count; as an \(L(7O)\) section N has its separate extra zero at O.

## Excluding every other common zero

- **\(T_-\):** the displayed D0 specialization is correct. The factor \(-s-M_D=s+\beta(3-s)>0\), while \(u_D<0\), so it is nonzero.
- **\(P_\pm\):** the displayed \(Q_D(-2)=10-12\beta-10s+4s\beta\) is a nonzero vector in \(\mathbb Q(s,\beta)\). Independence of 1 and alpha over that subfield rules out cancellation of the two bracketed summands. No sign assumption on the other coefficient is required.
- **Z:** the inequalities are sufficient and strict. The stated coefficient bounds give \(b<5,\ c>-30\). Since \(r<-10\),
  \[
  Q_D(r)>r^2+5r-30>20.
  \]
  Also \(u_N<0,\ a>0,\ r+s<0,\ r-L_N<0\), so \(t_Z\) is positive imaginary. The three factors \(r,r-s,r-M_D\) are negative and \(u_D<0\); consequently the other D0 summand is positive imaginary too. The sum cannot vanish. This is an argument in the fixed faithful embedding, not a numerical approximation.
- **O:** D0 has section order zero, by the previous O-point result.

All possible common zeros have therefore been considered. At B0, \(\operatorname{ord}(N)=1\) and \(\operatorname{ord}(D_0)\ge1\); their minimum is exactly one. **This does not determine the individual order of D0 or the value/pole behavior of X at B0.**

## Both degree statements

The D0 section of \(L(7O)\) has effective zero divisor of degree seven. Removing the complete common section divisor \([B_0]\) leaves a basepoint-free pencil of degree six. Equivalently, the pole divisor of \(N/D_0\) is the D0 zero divisor minus the common minimum divisor, of degree \(7-1=6\). This remains correct if D0 has order greater than one at B0. It proves the degree of the carrier-to-\(\mathbb P^1\) map, not merely a generic polynomial-degree bound.

For the source double cover D, the previously established quadratic field extension gives \([L(D):L(X)]=2\cdot6=12\). The target cubic has three distinct simple roots, so its square-root polynomial is irreducible over \(L(X)\), including its nonzero constant twist. The rational Y supplied by the full ODE embeds that degree-two target field into \(L(D)\). The tower law gives degree six from D to the target elliptic curve. The usual extension of a rational map from a smooth projective curve to a proper curve applies on the stated normalizations. There is no additional loss of degree from that extension.

## Scope

If the exact checks pass, this route supports the **complete common-section divisor and both exact degree-six claims for this fixed formula**. It does not by itself certify every individual fiber multiplicity, all four special-fiber divisors, the transformed empty-infinity representative, unramified twists/half-points/constants or descent. It also does not replace the remaining differential/exceptional-point, countercheck, proof/certificate and return obligations. Period/homology and exhaustive 1980-family classification remain open.

No new mathematical run, source mutation, claim, task status, or formal Driver disposition was produced.
