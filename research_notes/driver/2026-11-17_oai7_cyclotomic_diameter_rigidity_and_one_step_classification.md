# OAI7 — Rigidity at the optimal integer-displacement diameter, and the exact one-unit extension

Date: 2026-11-17. Author-side mathematical continuation: EM-DVR-DEBB5E, same directed Driver context; **not** an independent native Result review. Prior OAI7 shared-shift line: EM-EMF6D046-5A2844. Direct predecessor: `awdawmip/enterprise-math@3d4475e7f6534ac47dbaa09208cde59f47066535:research_notes/driver/2026-11-17_oai7_cyclotomic_optimal_integer_diameter_exact_uniform_shared_shift.md`. Fixed external theorem: `openai/math@adc7f1241b42e322a6451854ab7e4b4c146bf78a:preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/coverage-transfer.tex`.

## Proposition 1: an exact factorization, not merely a diameter lower bound

Let (p_1,dots,p_k) be **pairwise distinct primes** and (h) a finite-support, integer-valued random variable. Assume (hmod p_j) is exactly uniform for each (j). Set
[
D=sum_{j=1}^k(p_j-1),quad P=prod_{j=1}^kp_j,quad Q(X)=prod_{j=1}^k(1+X+cdots+X^{p_j-1}).
]
Let (a=minoperatorname{supp}h), (d=operatorname{diam}(operatorname{supp}h)), and (F(X)=mathbb E[X^{h-a}]). Then there is a unique polynomial (Ginmathbb R[X]) such that
[
oxed{F(X)=rac{Q(X)}{P}G(X),qquad G(1)=1,qquad deg G=d-D.}
]
Consequently (dge D). Conversely, every real polynomial (G) with (G(1)=1), (deg Gge0), and **nonnegative coefficients in (QG)**, with nonzero constant and leading coefficients, defines such a probability distribution by (F=QG/P), shifted by an arbitrary integer (a). In the converse, nonnegative coefficients are a real hypothesis; no coefficientwise positivity of (G) is asserted.

**Proof.** For a nontrivial (p_j)-th root of unity (zeta), exact marginal uniformity gives (F(zeta)=0). Since (p_j) is prime, all roots of (Phi_{p_j}=1+cdots+X^{p_j-1}) are nontrivial (p_j)-th roots. Their sets are disjoint across the distinct primes. Hence (Q=prodPhi_{p_j}) divides (F) in (mathbb R[X]). Set (G=PF/Q). Evaluate at (1): (F(1)=1) and (Q(1)=P), so (G(1)=1). Degree comparison gives (deg G=d-D). Conversely, (F=QG/P) is normalized, and its values at all nontrivial (p_j)-th roots vanish. By inverse finite Fourier transform on (mathbb Z/p_jmathbb Z), all its (p_j) residue probabilities are (1/p_j). Nonnegative coefficients and positive endpoints make it a probability generating polynomial with the stated diameter. QED.

## Proposition 2: exact rigidity at optimum

If (d=D), then (G=1). Thus **up to integer translation there is exactly one optimal-diameter probability law**:
[
oxed{mathbb E[X^{h-a}]=rac1P Q(X).}
]
Equivalently, (hoverset d=a+sum_{j=1}^k U_j) with independent (U_jsimoperatorname{Uniform}{0,ldots,p_j-1}). In particular, its entire mass vector, moments, variance and entropy are determined by ((p_j)), not just its support diameter. For example, (operatorname{Var}h=sum_j(p_j^2-1)/12). This uniqueness is **distributional**, not uniqueness of an internal sampler or CRT representation.

## Proposition 3: complete classification with precisely one unit of diameter slack

If (d=D+1), then (G(X)=u+(1-u)X). Since (F) has strictly positive constant and top coefficients and (Q) has positive endpoints, (0<u<1). Conversely, each (0<u<1) gives a valid law. Therefore exactly all such laws are
[
oxed{mathcal L(h-a)=u,mathcal L(S)+(1-u),mathcal L(S+1),quad 0<u<1,}
]
where (S=sum_j U_j) is the uniquely optimal law. The coefficients of (Q) are all positive (convolutions of consecutive strictly positive supports); hence this mixture has every integer (0,ldots,D+1) in its support. The mass at the left endpoint is (u/P), and at the right endpoint ((1-u)/P), so (u) is identifiable from either endpoint.

This is a sharp **one-unit** stability/classification theorem, not an assertion that all larger-diameter laws are mixtures of shifts of the optimum.

## Proposition 4: the first coefficientwise-mixture obstruction appears at two units

For the distinct primes (2,3),
[
Q(X)=(1+X)(1+X+X^2)=1+2X+2X^2+X^3,quad D=3.
]
Take
[
G(X)=rac{2}{3}(1-	frac12 X+X^2),qquad G(1)=1.
]
Its middle coefficient is negative, yet
[
oxed{F(X)=rac{Q(X)G(X)}6
=rac{1+rac32X+2X^2+2X^3+rac32X^4+X^5}{9}}
]
has positive coefficients, normalized to total mass (1), diameter (5=D+2), and exact uniform marginals modulo (2) and (3). Indeed the even and odd coefficient sums are each (9/2), while each residue class modulo (3) has coefficient sum (3). By unique polynomial division, (F) cannot be expressed as a **convex** mixture of shifted copies of (Q/P), even though such a mixture description is exact for slack (0) and (1).

This provides a concrete boundary for near-optimal shared-displacement constructions. The polynomial factorization from Proposition 1 remains valid at every finite slack; only the coefficientwise positivity of the residual factor fails at slack (2).

## Research significance and status

The previously saved OAI7 theorem established that exact coordinatewise prime-residue uniformity can be achieved by a single scalar displacement of minimal **integer support diameter** (D), with shared entropy (O(log(D+1))) and sparse joint terminal support in the selected asymptotic family. The current increment identifies the entire **optimal law** and all laws with diameter (D+1), while giving an explicit sharp failure of the tempting stronger convex-mixture classification at (D+2).

The original external coverage-transfer theorem selects **distinct indices (j)** and one fair sign per chosen index; it does **not** sample an arbitrary size-(s) subset of the (2k) signed coordinates. The preceding OAI7 entropy verification uses this exact quantifier and is unchanged.

All statements concern abstract integer displacements / finite residue projections. No bounded-step Gaussian-prime walk realizability, native X6 carrier, independent mathematical review, Native Result acceptance, formal Activity association or Task/parent-objective closure is claimed. Author contribution: EM-DVR-DEBB5E, with the earlier source contributions retained above.

## Finite verification of Proposition 4

Write the coefficient vector of (9F) as ((1,rac32,2,2,rac32,1)). Its sum is (9); parity sums are (9/2) and (9/2); modulo-three sums are (1+2=3), (rac32+rac32=3), (2+1=3). The factor has coefficient (-1/3) at (X), directly certifying that a nonnegative shift-mixture representation is impossible by uniqueness of the quotient.
