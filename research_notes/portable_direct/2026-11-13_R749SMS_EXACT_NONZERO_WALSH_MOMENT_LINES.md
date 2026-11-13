# R749SMS — Exact nonzero one-character moment-fiber minimax radii

Date: 2026-11-13, Asia/Shanghai. Direct continuation from R749SMQ and R749SMR in Draft PR #2233. Researcher EM-DIRECT-0DA8D3, Activity RA-36A3BAF67529B7EAA8A55ABE; service-issued SID MCP-e787dd41e0bb4a5f9fa1ef6531c3273c, registered and source-readback verified. Frozen scientific evidence pin: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Scope: abstract finite signed-source observer, distinct from six-axis P000 native spatial structure.

## 1. Exact question and results

On G=F_2^4, define chi_a(x)=(-1)^(a·x), C={1,2,4,8,15}, B=G\({0}∪C). For any retained family U and moment vector m, define the probability fiber F_U(m)={mu∈Delta(G): E_mu chi_a=m_a for every a∈U}. Its Chebyshev TV radius is rho_U(m)=inf_{q∈Delta(G)} sup_{mu∈F_U(m)} TV(q,mu).

**Theorem A (all five circuit-coordinate lines).** Choose any a∈C. For every real t∈[-1,1] with retained moments m_a=t and m_c=0 for all c∈C\{a}, the exact minimax radius is
`rho_C(m)=3/4`.

**Theorem B (all ten complement-coordinate lines).** Choose any b∈B. For every real t∈[-1,1] with m_b=t and all other B-moments zero,
`rho_B(m)=1/2`.

These equalities include nonzero and deterministic boundary data t=±1. At t=0 they recover R749SMR. They hold for arbitrary probability decoders and the full continuum of t, not only tested values.

## 2. Symmetry determines an optimal decoder

For a one-coordinate moment line of U, translations by every g∈ker(a) act on the fiber: chi_a(g)=1 preserves its specified t, while all other specified zero moments remain zero under translation. The worst-case TV loss as a function of q is convex and invariant under this 8-element group; averaging q over that group cannot increase risk. A translation-invariant decoder is uniform within each of the two chi_a sign-classes, but **symmetry alone leaves its two class masses free**. We choose the explicit candidate with the same class masses as the source fiber:

`q_{a,t}(x)=[1+t chi_a(x)]/16.`

The complete finite certificate in Section 4 proves that its worst-case error meets the disjoint-support lower bound in Section 3. **Together**, these establish that this particular q is minimax-optimal; there is no unjustified uniqueness assumption or inference that symmetry alone fixes the decoder masses.

## 3. Matching lower bounds from disjoint compatible laws

For a=1 in C, let h=14 (in binary, h has first bit 0 and the other three bits 1). Every circuit character except 1 flips sign under xor h, while chi_1 does not. For each r∈{0,2,4,6}, define mu_r supported on `{r,r⊕14,r⊕1,r⊕15}` by assigning probability `(1+t)/4` to each of the first two and `(1-t)/4` to each of the latter two. These are four mutually disjoint probability laws, each with m_1=t and all remaining C-moments zero. For any q at least one support has q-mass at most 1/4; its TV distance to that mu_r is at least 3/4. This proves the lower bound of Theorem A for every t.

For b=3 in B, take H={0,4,8,12}=span{4,8}. The dual annihilator H^perp={0,1,2,3} meets B exactly in {3}. With p_±=(1±t)/2, form mu_0 by placing p_+ uniformly on H and p_- uniformly on 1⊕H. Form mu_1 by placing p_+ uniformly on 3⊕H and p_- uniformly on 2⊕H. These two laws have disjoint supports and the same B-moments: m_3=t and all other m_b=0. Every q has TV at least 1/2 from one law. This proves the lower bound of Theorem B.

Every permutation of the five circuit characters induces an invertible linear map on the four-dimensional dual space (because any four members of C are independent, with the fifth their XOR). The induced group acts transitively on C and on the ten unordered pairs whose XORs are exactly B. Thus proofs for a=1 and b=3 transfer to all a∈C, b∈B.

## 4. Exact finite certificate for the upper bounds for every real parameter

The companion Python checker uses only exact `fractions.Fraction` arithmetic.

For C and a=1, each extreme point of F_C(t,0,0,0,0) is a basic feasible solution with at most six source states. Enumerate all `binom(16,6)=8008` six-state column bases for the six linearly independent probability/moment equations; nonsingular ones give affine functions of t. The positive-coordinate constraints intersect [-1,1] in a closed rational interval. Along each feasible basis interval, both the source law and q_{1,t} are affine in t; their total variation distance is convex in t, so the maximum is attained at an interval endpoint. Exact checks show: 4048 nonsingular bases, 3568 feasible segments, 5376 endpoints; only t∈{-1,-1/3,0,1/3,1} occur as feasible endpoints, and all TV values are at most 3/4.

For B and b=3, Fourier inversion gives every compatible source as
`mu_{t,z}(x)=[1+t chi_3(x)+sum_{a∈C} z_a chi_a(x)]/16.`
The five-dimensional z-feasibility region has exactly sixteen affine nonnegativity constraints. It is full-dimensional whenever |t|<1, and the endpoint cases are included by the same feasible-basis enumeration. Every vertex has five independent active constraints. Enumerate all `binom(16,5)=4368` possible five-active sets. Exact checks give 3008 nonsingular sets, 2288 feasible segments and 2816 parameter endpoints; the only endpoint parameters are {-1,-1/2,0,1/2,1}. All TV values from the explicit q_{3,t} are at most 1/2.

For both lines, finite candidate enumeration is **complete** by the standard basic-feasible-solution representation of a bounded polytope, and convexity propagates every endpoint bound across the complete real parameter interval. The attached code asserts the enumerator totals and maximal exact bounds and returns PASS.

## 5. Scientific implication and next frontier

The centered ambiguity in R749SMR does not vanish as soon as a retained Walsh moment becomes nonzero: it stays exactly 3/4 along each of five one-coordinate circuit lines, and exactly 1/2 along each of ten complement lines. Thus a full global nonlinear minimax risk strictly above these levels, if present, must arise from *at least two simultaneously nonzero retained moments*. This reduces the unresolved geometry to genuinely joint moment constraints.

Next: analyze two-coordinate moment slices, first symmetric t=s and then all rational breakpoints, looking for a strict radius increase or a global nonlinear decoder with certified maximum. Only later connect to a licensed V29/V39 native Cell/Link/Port event with explicit observer preservation. This is author-side proof and complete finite arithmetic verification, not independent review or native theorem acceptance.
