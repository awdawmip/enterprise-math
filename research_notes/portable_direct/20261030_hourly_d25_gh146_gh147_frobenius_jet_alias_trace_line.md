# D25/LIFT GH-146–GH-147 — Frobenius sampling defect and a short trace-line reconstruction

Date: 2026-10-30 (Asia/Hong_Kong). Author-side portable research by the hourly Research lane chatgpt-research-hourly-enterprise-math-20260923, never the maintenance conversation. Parent Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. P000 ACTIVE_LOCKED; frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged. Status AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. This is not a native Source checkpoint or predecessor completed unit.

## Exact source dependencies and notation

Reuse the GH-127 character-zero identity, GH-131 Hasse reflection, GH-141 marked conjugation and GH-145 trace-polynomial/jet distinction, at their exact author-only strength. Let p=8m+3≥11 be prime, K=F_(p²)=F_p(ρ) with ρ²=2, N=(p−1)/2=4m+1, d=(p−3)/4=2m, e=(p²−1)/2=N(p+1), c=1/4. Define

g_B(X)=X²+X+B; f_B(X)=Xg_B(X); H(B)=[X^N]g_B(X)^N∈F_p[B].

Then deg H=d and H(c−B)=H(B), using GH-131. The finite-field trace polynomial T(B)=Σ_(x∈K) f_B(x)^e ∈F_p[B] satisfies, as a polynomial identity,

(1) T(B)=−H(B)H(B)^p.

Proof: ∑_(x∈K)x^k is −1 for positive k divisible by p²−1 and zero for other positive k. In x^e g_B(x)^e only exponent 2e survives, so T=−[X^e]g_B(X)^e. The decomposition g_B^e=g_B^N(g_B^N)^p has exactly one exponent pair (N,N) contributing X^(N+pN), since deg_X g_B^N=2N=p−1. The formal polynomial derivative (not differentiation of integer point counts) yields

(2) T'(B)=−H'(B)H(B)^p; S_1(B)=−2T'(B)=2H'(B)H(B)^p,

where S_1(B)=Σ_(f_B(x)≠0) χ(f_B(x))x/f_B(x), χ(0)=0. The derivative coefficient e≡−1/2 mod p and e>1 justify the zero support.

Original marked parameter a=B₀=(1+2ρ/3)/8=1/8+ρ/12 satisfies a^p=c−a. Thus H(a)^p=H(a)∈F_p and H'(a)^p=−H'(a).

## GH-146 — a zero-valued sampled residual carries the missing first jet

Let h(t)=H(a+t)∈K[t], deg h=d. Reflection gives h_j^p=(−1)^j h_j for each coefficient. Therefore the *ambient* substituted trace polynomial and the *base-field sample interpolant* are

P(t)=T(a+t)=−h(t)h(−t^p),
G(t)=−h(t)h(−t).

The second is even, has coefficients in F_p and deg G≤2d=(p−3)/2<p. At every t∈F_p, P(t)=G(t), so G is the unique degree-<p interpolating polynomial of the horizontal trace samples. Nevertheless

(3) D(t)=P(t)−G(t)=(t^p−t)Q(t), Q∈K[t],

and **the precise missing jet is Q(0)=H(a)H'(a), S_1(a)=2Q(0)**.

Proof: h(−t^p)−h(−t) is divisible by t^p−t, proving (3). P'(0)=−H(a)H'(a) because the t^p factor has derivative zero; G'(0)=0 by evenness. Differentiation at zero of (3) gives P'(0)=−Q(0), and (2) gives S_1(a)=2Q(0). Hence reducing a polynomial modulo t^p−t preserves all F_p point samples but is *not* a jet-preserving operation. This is not a claim that the full data plus additional family structure could never determine the jet.

The two *actual* conjugate families E_(a+t) and E_(a^p+t), t∈F_p, also have identical integer Frobenius traces at each corresponding t: field Frobenius gives a point bijection. But their marked first moments at t=0 satisfy S_1(a^p)=−S_1(a). At p=3347 these differ nontrivially.

p=3347 exact check, using *prior* Hasse inputs: H(a)=783, H'(a)=1351ρ, Q(0)=181ρ, P'(0)=3166ρ, G'(0)=0 and S_1(a)=362ρ in F_(3347²). This explains the defect mechanism but is not a new independent CM evaluation.

## GH-147 — a much shorter orientation-correct trace sampling interface

Use the **Frobenius-antivariant, trace-fixed parameter line** B(v)=1/8+ρv for v∈F_p. The marked point is v₀=1/12. Each B(v)^p=c−B(v), hence k(v)=H(B(v))∈F_p[v] *as a polynomial*, by GH-131 reflection. Its degree is ≤d. All these curves are nonsingular because the F_p component 1/8 differs from both 0 and 1/4. Define

(4) A(v)=k(v)²∈F_p[v], deg A≤2d=(p−3)/2=N−1<p.

At every v∈F_p, A(v) is the **ordinary integer Frobenius trace** a_(p²)(E_(B(v))) reduced modulo p, because T(B(v))=−A(v) by (1). This is a valid low-degree polynomial representation of the trace samples, but it is not the ambient T(B) polynomial itself. Differentiating (4) at v₀ gives

A'(v₀)=2H(a)ρH'(a)=ρ S_1(a),

so

(5) S_1(a)=ρ^(−1)A'(v₀).

Choose any N distinct v_i∈F_p and Lagrange basis ℓ_i(v)=∏_(j≠i)(v−v_j)/(v_i−v_j). Since deg A<N, this yields the exact finite-field sampling theorem

(6) S_1(a)=ρ^(−1) Σ_(i=1)^N [a_(p²)(E_(1/8+ρv_i)) mod p] ℓ_i'(v₀).

Thus **N=(p−1)/2 distinct labelled integer trace values** suffice, versus p² values in GH-145's general whole-parameter interpolation. This is a reduction in the *number of required curves*, not a claim about the cost of independently counting their points. Actual unmarked point-count inputs can be independently obtained; one must not substitute H-derived samples and call them independent CM evidence.

Coordinate-gradient explanation: writing B=u+ρv, the unique low-total-degree F_p polynomial representing the trace-negative residue on F_p² is F(u,v)=−H(u+ρv)H(u−ρv). At a=(1/8,1/12), ∂_u F=0 and ∂_v F=−2ρH(a)H'(a); ambient T(u+ρv) instead has formal derivatives −H(a)H'(a) and −ρH(a)H'(a). The factor-of-two and zero horizontal derivative follow from Frobenius reduction, not from changing the elliptic curve. Observer: labelled trace samples; future operation: marked first jet; retained residual: Q(0), or the correctly oriented trace-fixed-line derivative. This is an external finite-field auxiliary theorem, not an X6-native spatial theorem.

## Executed exact evidence

The standalone Python 3 standard-library checker d25_gh146_gh147_compact_check.py was actually executed (PASS_GH146_GH147_COMPACT_EXACT). For p=11,19,43,59,67,83,107 it constructs P,G,D; long-divides by t^p−t and verifies zero remainder and Q(0)=HH', checks every t∈F_p, and performs **191 completely independent integer point-count inputs covering 1,181,015 quadratic-character observations**, interpolates from these count-only values and separately checks S_1 by direct character summation. Outputs (p, A(v₀), A'(v₀), S_1/ρ): (11,1,2,1), (19,0,0,0), (43,0,0,0), (59,49,55,57), (67,0,0,0), (83,51,62,31), (107,86,31,69). The p=3347 interpolation check uses 1673 explicitly **HASSE_DERIVED_NOT_INDEPENDENT** samples; it obtains A(v₀)=588, A'(v₀)=724, hence S_1=362ρ. It is not a direct 3347 point-count or native H₀/B₀ divided-power experiment. The expanded local verifier, logs and source manifest are in the portable bundle.

Mathematics status: author-derived universal algebra conditional on exact GH-131/GH-127 dependencies, small-prime exact independent direct-count checks, no Lean checker, no independent reviewer, no native Source admission. The full-prime GH-83/GH-3 proof and independent 3347 special-value prediction remain OPEN.

## Next precise action / no-repeat frontier

Do not redo GH-124 character-moment enumeration, GH-131 reflection proof, GH-141 parity, GH-145 full q-trace interpolation or the 11,202,409-field-element 3347 enumeration. Seek independent CM/Jacobi/Gauss or p-adic evaluations of the N=1673 labelled ordinary trace inputs in (6), or rigorously prove a smaller sufficient CM-compatible trace subset. Most curves along the trace-fixed line need not have CM: no automatic CM value assignment. Independent input values plus (6) would give a noncircular special-value check. The original D25 native same-class H₀/B₀ divided-power module, [X]U modulo p², semilinear Frobenius normalization η and p=373 benchmark are separate open hard targets; see #1559.

Read-only gateway v0.6.11: research_authority_granted=false, executor_binding_configured=false, native jobs 5/5, Source control CODE_REVIEW_REQUIRED. Own recovery/continuation is not directly callable here; #1558 carries prior exact own-lane recovery and predecessor-CAS support. No new service session, CLAIM, authorized OPEN, Source checkpoint, Result, review or native publication is asserted; old session/staging preserved, no maintenance identity used.