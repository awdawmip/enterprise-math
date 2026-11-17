# R762DO — Exact three-adic BRC denominator for the diagonal area observer

Date: 2026-11-18 (Asia/Shanghai). Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS / TP2-8B7E13C5904A2D6F1142. Researcher: EM-X6-3050F6, existing SID MCP-4b2d70a97f594366a7c94a0f8b45df38. Independent review: NOT_REVIEWED.

## Sources and conditional scope

Reuse frozen taskbook research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md@e3f42efac29a2da2d95be391f3231a664e2fade0, P000 V5@a72226e2430ffa4786321ac86e7f0c599d5f0389, and R762DI–DN candidate six-step return-area BRC. No native TRIADIC_CLOSURE_E event-licence or V17/V29/V39 Port-transport inference is made.

The six distinct named positive integer BRC microbranches are
(0,0,0), (1,0,0), (0,0,1), (1,1,0), (0,1,1), (1,1,1).
Their count polynomial in Z[C_Q^3] is
P(X,Y,Z)=1+X+Z+XY+YZ+XYZ.
For Q=3^a, declare the diagonal endpoint observer σ(u,v,w)=u+v+w mod Q. It sends X,Y,Z to t, retains the SIX branch multiplicities 0,1,1,2,2,3, and induces
F(t)=σ_*(P)=1+2t+2t²+t³=(1+t)Γ(t),
Γ(t)=1+t+t², in Z[C_Q].
The compressed observer reproduces only final σ and its future common additive BRC branch updates. Ordered sources, signed Port provenance, and the two omitted joint-area coordinates remain in the full carrier.

For any nonnegative integer group-ring histogram H with total 6^n, define content(H)=gcd of its coefficients (including possible zero entries). Its minimum equiprobable deterministic seed population reproducing the exact endpoint distribution is 6^n/content(H).

## Theorem: exact answer for all powers of three, all exponents

For a>=2, write Q=3^a, d=3^(a-1), n=md+r (n>=1, 0<=r<d). Set

\[
\nu_a(n)=
\begin{cases}
0,&m=0,\\
m-1,&m\ge1,\ 2r<d,\\
m,&m\ge1,\ 2r\ge d.
\end{cases}
\]

Then the *entire integer coefficient gcd*, and therefore the exact diagonal BRC seed count, are

\[
\boxed{\operatorname{content}(F^n)=3^{\nu_a(n)},\qquad
M_{\rm diagonal}(Q,n)=6^n/3^{\nu_a(n)}.}
\]

For a=1 (Q=3), F=2(1+t+t²), so for n>=1:
content(F^n)=2^n 3^{n-1} and M_diagonal(3,n)=3.
For n=0, both the content and seed count are one.

### Proof 1: remove the diagonal unit

Because Q is odd and t^Q=1,
(1+t)(1-t+t²-...+t^{Q-1})=2.
Thus 1+t is a unit in Z_(3)[C_Q], so it preserves exact coefficientwise three-adic divisibility. Consequently v3(content(F^n))=v3(content(Γ^n)).

### Proof 2: sharp lower threshold from an order-three subgroup

For a>=2 put d=3^(a-1) and A=1+t^d+t^(2d). We have A²=3A. By integer Frobenius Γ(t)^d=A+3B for some B in Z[C_Q]. Augmenting at t=1 gives B(1)=3^(d-1)-1 ≡ -1 mod 3.

For m>=1 the binomial theorem and A^j=3^(j-1) A yield the exact identity

\[
(A+3B)^m
=3^{m-1}A((1+B)^m-B^m)+3^mB^m. \tag{1}
\]

Hence Γ^(md+r) is coefficientwise divisible by 3^(m-1). For the sharp residue, work in F3[C_Q] = F3[x]/(x^(3d)) with x=t-1. We have A=x^(2d) and Γ^r=x^(2r) modulo 3. Moreover U_m=(1+B)^m-B^m has constant coefficient U_m(1)=-(-1)^m in F3; therefore it is a unit in that local algebra. Dividing (1) by 3^(m-1), multiplying by Γ^r, and reducing mod 3 gives

\[
\frac{\Gamma^{md+r}}{3^{m-1}}
\equiv x^{2d+2r}U_m\pmod3. \tag{2}
\]

When 2r<d this is nonzero, proving valuation exactly m-1. When 2r>=d it vanishes, proving valuation at least m. If m=0, Γ^r mod 3 equals x^(2r)≠0, proving valuation zero.

### Proof 3: ramification rules out any higher valuation

Let ζ be a primitive Q-th root in a 3-adic cyclotomic field with v3(3)=1. For a>=2,
v3(1-ζ)=1/(2·3^(a-1)),
v3(1-ζ³)=1/(2·3^(a-2)).
It follows from Γ(ζ)=(1-ζ³)/(1-ζ) that v3(Γ(ζ))=1/d.
Thus for n=md+r:
v3(Γ(ζ)^n)=m+r/d <m+1.
If all coefficients of Γ^n were divisible by 3^(m+1), evaluating at ζ would have valuation at least m+1, contradiction. Hence valuation at most m. Together with Proof 2 this settles every remainder and every exponent.

For Q=3, Γ²=3Γ and F=2Γ, which gives the exceptional formula. QED.

### No concealed factor 2

For a>=2, choose a primitive Q-th root ξ in an algebraic closure of F2 (Q is odd). Neither 1+ξ nor 1+ξ+ξ² vanishes when Q>=9; hence F(ξ)^n≠0. Therefore not all coefficients of F^n are even. Any prime dividing their gcd must divide their sum 6^n, so only 2 or 3 can occur. The established three-adic value is the *complete* gcd. Reducing the positive probabilities coeff(F^n)/6^n shows the minimal seed formula. QED.

## Examples and frontier

At Q=9, the first valuation jump occurs at n=5, followed by n=8,11,14,... . At Q=27 the first jumps occur at n=14,23,32,... . By contrast, the full three-coordinate BRC count studied in R762DL begins nontrivial three-divisibility only at n=Q. This proves that the diagonal observer has strictly cheaper exact information requirements for some horizons, at the cost of removing observer-relevant joint-area distinctions.

If c_full(Q,n) denotes the gcd of all full three-coordinate BRC path counts, the diagonal observer gives the exact new upper certificate
c_full(Q,n) | 3^ν_a(n).
Together with R762DN, for a>=2 and n=md+r:
max(0,m-2) <= v3(c_full(Q,n)) <= ν_a(n).
The equality conjecture for full three-coordinate Q=3^a remains unresolved beyond its previously proved plateaux.

## Reproducible arithmetic and next action

The companion Python program executes only the six named positive BRC branch convolution after the declared diagonal observer; it checks complete integer coefficient gcds, factorization and the formula. The summary evidence covers Q=3,9,27,81,243, n ranges 1..36, 1..100, 1..130, 1..165, 1..180 (611 exact pairs). General validity is supplied by the proof above, not inferred from the finite tests. Review remains NOT_REVIEWED.

Next: attack the full three-coordinate all-a sharp-content conjecture using the lifted Frobenius B0 and H-coset socle, or construct a certified violating exponent. Independently resolve licensed primitive TRIADIC_CLOSURE_E signed Cell/Link/Port operations and V17/V29/V39 transport. Preserve frozen science, original CLAIM and original owner; no source-event admission is inferred from this candidate histogram.