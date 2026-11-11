# PREFIX-709-R6 — Exact joint-survivor two-stream variance exclusion on 192×192 boxes

Date: 2026-11-12 (Asia/Shanghai).
Frozen scientific pin: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Mother objective: PREFIX-675, the full-square variance maximization of the frozen auxiliary BRC statistical observer.
Dependencies: PREFIX-705 exact survivor stochastic monotonicity; PREFIX-706 fixed rational witness.
Evidence: AUTHOR_RECOMPUTED / EXACT_INTEGER_RATIONAL / UNREVIEWED / NOT_ADMITTED.

## Main theorem

Let T_p be the frozen first-stop clock, with survival tails s_n(p)=Pr(T_p>n) for n=0,...,188. Let the two clocks at parameters p,z be independent and Y(p,z)=max(T_p,T_z). Write mu=E[Y], W=Var(Y), V_q=q² W-q mu for real q>=2, D=[0,1/2]². Fix e=(0,3/20), b=559812917/1000000, G=192, and the closed boxes

B_ij=[i/(2G),(i+1)/(2G)] × [j/(2G),(j+1)/(2G)], 0<=i,j<G.

Define J_n(p,z)=s_n(p)+s_n(z)-s_n(p)s_n(z),
M(p,z)=sum_{n=0}^{188} J_n(p,z), and
C(p,z)=sum_{n=0}^{188}(2n+1)J_n(p,z).

For each box let a be its lower-left corner and h its upper-right corner. Set the exact rational upper bound

U_ij=min( C(h)-M(a)^2, [189²-378 M(a)+C(a)]-[189-M(h)]² ).

Let S={(i,j):U_ij<b}, and R be the union of the selected boxes.

**Theorem 709.1.** The full exact integer calculation finds |S|=33766 ordered boxes and verifies

min_{(i,j) in S}(b-U_ij) > 169821/1000000.

For every real q>=2 and all (p,z) in R,

V_q(e)-V_q(p,z) > (169821/1000000)q² >0.

Hence every global maximizer lies outside R. The exact excluded fraction of D is

33766/36864 = 16883/18432 = 91.596137152777...%,

and the absolute excluded area is 16883/73728. The certified-area ratio to PREFIX-708 is 8644096/3113379 (>2.77). The remaining 3098 cells are undecided by this bound and provide the next local frontier.

## Proof of the continuous exclusion

PREFIX-705 establishes that each s_n(p) is nondecreasing on [0,1/2]. Independence gives Pr(Y(p,z)>n)=J_n(p,z)=1-(1-s_n(p))(1-s_n(z)), nondecreasing in both coordinates. For bounded nonnegative integer Y, tail sums give M=E[Y] and C=E[Y²]. Both functions are therefore nondecreasing. The complementary variable 189-Y is stochastically nonincreasing in both coordinates, so its first and second moments are nonincreasing.

For x in a closed B_ij, M(x)>=M(a)>=0 and C(x)<=C(h), yielding W(x)=C(x)-M(x)² <= C(h)-M(a)². Also

W(x)=E[(189-Y(x))²]-E[189-Y(x)]²
    <= (189²-378 M(a)+C(a)) - (189-M(h))².

Consequently W(x)<=U_ij. The PREFIX-706 exact witness establishes W(e)-M(e)/2>b. Since q>=2 and M(e)>=0, W(e)-M(e)/q>b; since M(x)>=0,

[V_q(e)-V_q(x)]/q²
  =W(e)-M(e)/q-W(x)+M(x)/q
  > b-U_ij.

The companion script recomputes all 189 labeled survivor rows under the frozen integer width test, checks 9529 nonzero count cells, evaluates all rational endpoint tails and joint raw moments from integer powers, and tests U_ij<b using a single exact common denominator. The symmetry U_ij=U_ji only halves repeated work: the result counts both ordered boxes. It verifies |S|=33766, undecided=3098, the exact area and strict minimum gap. The box interiors are disjoint, hence the stated area fraction. QED.

## Scope and next question

This is a uniform certificate for all real q>=2 in the *frozen auxiliary statistical model*. It improves the Efron-Stein marginal bound in PREFIX-708 by retaining the joint max-survival observer, with branch provenance contained in the original integer recurrence; it does not assert a native physical X6 law.

Next: refine the remaining 3098 boxes with joint-survivor/Bernstein bounds, and for q in [12,24] exploit the affine t=1/q interval by exact endpoint tests at t=1/24 and t=1/12. Continue toward actual optimizer location under PREFIX-675. Formal independent review and admission remain separate.
