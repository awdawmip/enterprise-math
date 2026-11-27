# R284JW — Fourth root coefficient and sparse integer-root theorem

2026-11-28. Author proof and exact rational interval computation; NOT_REVIEWED. Own recovered session metadata EM-DIRECT-0C386E / TASK_RESEARCH, MCP-8cd6c4fa26b9459d923ff73ba0082220, no formal run. Owner inventory request r1-20261128-0055-leased SUCCEEDED, INV-424682d578461f24594a9b66a2429cf1, as of 2026-11-27T16:56:25.263752Z, filtered LEASED tasks empty; no shared task mutation. Current global normative snapshot f7966f6c07f2b2a79026ad9c881d1cfcddb167ef; EM behavioral snapshot 28665c59f04df2b7edcbdae5a1e967f587305cde; P000 V4/V5, ACTIVE worldview, portable/continuation and joint/residual contracts read. Ordinary auxiliary arithmetic observer; no native spatial attribution.

Frozen scientific frontier: R284JV b19f621164a985ba2b4d7c59a157a34cbebe7b71:research_notes/portable_direct/R284JV_TRANSCENDENTAL_SCALE_AND_DENSITY_ONE_SEPARATION_20261128.md (full text read this turn), with its frozen JS/JT inputs. In particular use JV's all-order expansion, eventual unique real root q_d, and normalized minimum residual g_d comparable to dist(q_d,Z). No premise from the unpublished JU numerical report. Same full C, including endpoint E.

## 1. Certified fourth root coefficient

For sufficiently large positive integers d the unique real root in the legal range satisfies
q_d = alpha*d^2 + beta*d + gamma + delta/d + O(d^-2).
New rigorous enclosures:
-12.5336350561 < gamma < -12.5336350560;
10.2559198987 < delta < 10.2559198988.
In particular delta is strictly positive. This supplies independent numerical certification for gamma (the previous JU report lacked verified remote proof/code) and a new fourth coefficient.

Let h=1/d, s=d^2/q, x=k/d, y=1-x, phi=x^2+y^2/2. Write v,b,a,e for V,Q,A,E divided by d^3. By the exact JV observer,
f_d(s)=C/(q^3 d^5)=h^-1{3[4+s(3h+h^2)]^2(a+e)b -32[3+s(h+h^2)][a+s h^2(v+b)]^2}.
Compute the braces through h^4, retaining the joint cancellation at h^0. This yields f_d=L+hM+h^2N+h^3P+O_{C^1}(h^4). Existence and uniform error follow from JV; this computation supplies exact coefficient evaluation. For lambda=1,2 define n=lambda*q+d. For j=1..5 expand the coefficient c_j(t,s) of h^j in
log(1+s(1-t)h/lambda)-log(1+s(1+t)h/lambda+3s h^2/lambda).
Sum each monomial t^m over i=0..k-1 using the exact identity
sum (i h)^m = sum_{ell=0}^m binom(m+1,ell) B_ell x^(m+1-ell) h^(ell-1)/(m+1).
Here B_1=-1/2; the constant Bernoulli polynomial term cancels at the lower endpoint and ell=m+1 MUST NOT be included. Then exponentiate the nonconstant h series by p_0=1, p_j=(1/j) sum_{i=1}^j i log_i p_{j-i}. The two leading logarithms combine to -s*phi.

For the normalized sums v,b,a, use h times the sum of the resulting joint carrier times weights:
v: (x+h)(y+h);
b: (x+h)y * [1+s h(1+y)/2+s h^2]/[1+s h(1-y)/2+s h^2/2];
a: (weight_v+weight_b)*[(1+s h(1-x))(1+s h(1+x)+2s h^2)]/[2(1+s h)(2+2s h+s h^2)].
The full endpoint is e=h^2 R_u(d)*(2+3h)*(2+s h+2s h^2)/[2(2+2s h+s h^2)(8+4s h+2s h^2)].
These are exact rational weights before truncation. Euler-Maclaurin for h times the full sum including k=0,d supplies integral, h/2 times the two endpoints, h^2/12 times first derivative difference, and -h^4/720 times third derivative difference. Derivative of a polynomial multiplying exp(-s phi) uses partial_x - s partial_x phi. The same algebra for s derivatives uses partial_s - phi. Uniform smoothness on the compact rectangle and JV justify every fixed-order truncation.

For the simple root s_*, write s_d=s_*+a1 h+a2 h^2+a3 h^3+O(h^4). At s_*,
a1=-M/L';
a2=-(N+M'a1+L''a1^2/2)/L';
a3=-(P+N'a1+M'a2+M''a1^2/2+L''a1a2+L'''a1^3/6)/L'.
Taylor substitution gives residual O(h^4); the uniform positive derivative near s_* bounds root error by O(h^4). Inversion gives beta=-a1/s_*^2, gamma=a1^2/s_*^3-a2/s_*^2 and
delta=-a1^3/s_*^4+2a1a2/s_*^3-a3/s_*^2.

### Exact evidence
Full executed Python/SymPy QQ + Fraction interval code:
ea8929c7bceecc66e8f8f2a1cbfe8ee74fb11263:research_notes/portable_direct/R284JW_exact_fourth_root_coefficient.py.
Local executed code SHA256 591bcfa966fdf9cb5fad063a6ff45ce30feef3a2f07426fd211a34e3d80623d8; remote full readback matched authored text, blob 5b99125eb631b4d6a60bd6200b999f721fabeadf.
The exact bracket is 937181823342286298624673/10^24 < s_* < 937181823342286298624674/10^24. Direct integral L interval evaluations at these rational endpoints have strict opposite signs. Alternating exp Taylor degrees 31 and 32 bound every moment integral x^m exp(-s phi) and endpoint exponential, since 0<s phi<1; all polynomial moment integrals and interval arithmetic use rational numbers. Multiplication handles arbitrary signs via four endpoint products. The reported float formatting is display only; assertions compare exact rational endpoints. Observed stdout (rounded display):
L(lo) about -1.972419037891e-25; L(hi) about 2.647819816887e-25.
L' about 0.46202388547775775; M about -1.7874274652674034;
N about -14.66356851400102; P about -54.06516458049629.
beta about -4.404699500829311, gamma about -12.53363505603851, delta about 10.255919898762528.
Certified delta and gamma intervals; all assertions passed.
A preliminary Faulhaber implementation mistakenly included ell=m+1 and yielded delta about 9.8572257; it was corrected by the exact lower endpoint cancellation above before the final run. No claim is based on that preliminary output.

## 2. Deterministic sparse integer-root theorem

Let E(X) count d<=X for which some legal integer q has C(q,d)=0 (and hence bound all target equalities qK=32/3). Then
E(X)=O(X^(1/3)).
This is a power-count bound, stronger than JV's qualitative density zero. It uses the nonzero reciprocal correction, not an irrationality measure for alpha.

Proof. By JV, expand q_d to include terms through d^-4 with remainder O(d^-5). Uniformly over four distinct integers D<=d1<d2<d3<d4<=2D, consider the third divided difference
T=[d1,d2,d3,d4]q = sum_i q_di / prod_{j!=i}(di-dj).
The quadratic polynomial part cancels exactly. The identity [d1,d2,d3,d4](1/x)=-1/(d1*d2*d3*d4) follows by repeated divided differences. Every fixed smooth inverse power x^-j for j>=2 has third divided difference O(D^(-j-3)) by the standard divided difference mean value formula on [D,2D]. The discrete remainder contributes O(D^-5) because the integer denominators have modulus at least 1. Therefore
T=-delta/(d1*d2*d3*d4)+O(D^-5),
uniformly even for consecutive integer arguments, without assuming a smooth interpolation of the remainder. In particular for sufficiently large D, T<0 and c D^-4<=|T|<=C D^-4 with c>0 and C=12 possible, by the certified delta enclosure.

Form the integer determinant if all four q_di are integers:
det rows (1,di,di^2,q_di) = prod_{i<j}(dj-di)*T.
For four arguments in an interval of length H=floor(D^(2/3)/2), the Vandermonde product is positive and at most H^6. Thus the determinant is nonzero and has absolute value <=12 H^6/D^4<=12/64<1, a contradiction. Every such block contains at most three exact integer roots. Partition [D,2D] into O(D^(1/3)) blocks and sum dyadic ranges to obtain the stated bound, including the finite initial range. The theorem is asymptotic; the onset D_0 is not numerically certified.

## 3. Quantitative shrinking-target refinement

For fixed A>2 and C0>0, let E_A(X) count d<=X with dist(q_d,Z)<=C0*d^-A, ignoring the finitely many d before eventual uniqueness. For A>=4, E_A(X)=O(X^(1/3)). For 2<A<4, for every eta>0,
E_A(X)=O_{A,C0,eta}(X^((5-A)/3+eta)).
The same statements apply to g_d<=d^-A by JV's two-sided comparison with distance. For eta large the trivial bound suffices.

Proof. Replace q_di in the determinant by nearest integers n_i. Its perturbation is bounded by 4 C0 D^-A H^3, since each cofactor is a triple Vandermonde. For A>2 this tends to zero; the determinant still has absolute value <1. To ensure it is nonzero, select four arguments separated successively by at least T0. Their divided difference perturbation is <=4 C0 D^-A/T0^3. For A>4 use T0=1; for A=4 choose a sufficiently large fixed integer T0 so this is <(c/2)D^-4. For 2<A<4 choose T0=ceil(D^kappa) with kappa=(4-A)/3+eta (take eta small enough that kappa<2/3). Then the perturbation is o(D^-4). The same determinant contradiction applies. If a block had more than 3 T0 integer arguments, greedy selection from smallest argument, discarding the next T0-1 sites each time, would select four. Thus each block contains O(T0) exceptions and the dyadic count is O(D^(1/3)T0), giving the exponents stated. The implied constants may depend on the asymptotic remainder and the fixed threshold; no effective onset supplied. This gives a quantitative exceptional count without a quantitative Weyl theorem.

## 4. Scope and next
The count is in d, with all legal integer budgets simultaneously covered outside the exceptional d. No pointwise non-equality for all d or all-d inverse polynomial lower bound follows. JR's finite d and JQ's conditional modular results remain unchanged. Next seek a compatible congruence obstruction for the sparse remaining d; alternatively make JV remainder effective to produce an explicit onset for the determinant bound. The determinant is a joint residual across four distinct deficiency coordinates and retains the small reciprocal correction invisible in the leading quadratic projection. It is a reusable ordinary auxiliary arithmetic tool, not a new admitted BRC primitive or native geometry statement.
