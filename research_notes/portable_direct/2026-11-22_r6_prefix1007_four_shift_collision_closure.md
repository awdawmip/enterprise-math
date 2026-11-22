# PREFIX-1007 — All eleven marked X6 BRC collisions eliminate into four unmarked A₆ shifts

**Date:** 2026-11-22 (+08). **Status:** AUTHOR_FORMAL_SERIES_PROOF / EXACT_SYMBOLIC_AND_INTEGER_CHECKED / NOT_REVIEWED. Portable independent mathematics; **no new canonical Stage46 dynamical execution, shared CLAIM, formal Result or Review**.

## Fixed science and provenance

Scientific foundation remains frozen at \`awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json\`. The native model is the X6 six-axis Cell torsor (twelve signed directions, a separately typed update count). Continue the **Stage46 candidate** signed, typed Z₂ BRC kernel \`C(h,j)=1/6-[h=j]\`, starting incoming-neighbour port \`-e1\`. Absorb both orientations of the single Link between the chosen chart anchor and its +e1 neighbour, **without degree renormalization**. The observed quantity is the one-negative-step (first interior grade) joint **terminal Cell and incoming-neighbour port** probability: coherently sum signed histories in each complete fibre, then square and add over fibres.

Inherited results: [PREFIX-1003](https://github.com/awdawmip/enterprise-math/blob/d9c53f6af236cf7d128409c9eb07dd3e735f523c/research_notes/portable_direct/2026-11-22_r6_prefix1003_single_link_first_interior_finite_prefix.md) proves the three-packet BRC amplitude identity; [PREFIX-1004](https://github.com/awdawmip/enterprise-math/blob/aec844a083f0517570ce1dd5924717db6880da98/research_notes/portable_direct/2026-11-22_r6_prefix1004_marked_collision_asymptotic.md) gives its Laurent observer; [PREFIX-1005](https://github.com/awdawmip/enterprise-math/blob/1e5cb76e806d3da352ba68f9e160474095950c93/research_notes/portable_direct/2026-11-22_r6_prefix1005_marked_collision_orbit_reduction.md) proves the eleven exact marked-collision orbit coefficients; [PREFIX-1006](https://github.com/awdawmip/enterprise-math/blob/134f84c5d91e18ec72f325c4eab40509102a7c52/research_notes/portable_direct/2026-11-22_r6_prefix1006_marked_collision_integer_transfer.md) supplies an O(m²) exact evaluator. This note **changes only the last, already specified scalar observation**.

## Theorem 1007.1 — universal formal-series factorization and hidden sign redistribution

For arbitrary d≥1 and integer δ=(δ₁,…,δ_d) satisfying Σδ_i=0, let

\[
H_m^{(d)}(\delta)=\sum_{|a|=m}\binom{m}{a}\binom{m}{a+\delta},\qquad
A_d(m)=H_m^{(d)}(0).
\]

Invalid multinomials are zero. Define \`g_k(t)=Σ_{r≥0}t^r/(r!(r+k)!)\` for k≥0, and \`p=Σ_i max(δ_i,0)=||δ||₁/2\`. In the formal-power-series ring over Q,

\[
\boxed{\sum_{m\ge0}\frac{H_m^{(d)}(\delta)}{(m!)^2}t^m
=t^p\prod_{i=1}^d g_{|\delta_i|}(t).}\tag{1}
\]

Consequently \`H_m(δ)\` is **exactly invariant under any redistribution of signs** that preserves the multiset of absolute displacements and total displacement zero, even if the redistribution is not an axis permutation or a global reversal.

**Proof.** Expand each multinomial. For one signed shift k the corresponding single-label series is \`Σ_{a≥max(0,-k)}t^a/(a!(a+k)!)\`, equal to \`g_k\` for k≥0 and \`t^{-k}g_{-k}\` for k<0. Multiplying these d series and extracting coefficient t^m gives \`H_m/(m!)²\` exactly. The total power of t contributed by negative shifts is \`-Σ_{k<0}k=p\`. The remaining factors depend only on absolute shift magnitudes. QED.

**Genuine new sign-symmetry witness (six axes):** δ=(3,2,-2,-1,-1,-1) and ε=(-3,2,2,1,-1,-1) have equal absolute multisets (3,2,2,1,1,1), but are related by neither axis permutation nor global sign reversal. Equation (1) proves \`H_m(δ)=H_m(ε)\` for **all** m≥0; at m=5 the common integer is 600, at m=6 it is 52,200.

## Theorem 1007.2 — seven-state linear-arithmetic transfer and reduction to A_d

The \`g_k\` obey exact formal identities

\[
g_1=g_0',\qquad
t g_1'=g_0-g_1,\qquad
t g_{k+1}=g_{k-1}-k g_k\quad(k\ge1).
\tag{2}
\]

In particular every \`g_k\` belongs to the Q(t)-span of \`g_0,g_1\`. For a fixed d put \`u_j=g_0^{d-j}g_1^j\`, \`0≤j≤d\`; then

\[
\boxed{t u_j'=(d-j)t u_{j+1}+j u_{j-1}-j u_j,}
\tag{3}
\]

with absent end states omitted. Writing \`c_{j,m}=[t^m]u_j\`, all \`c_{j,0}=1\`, while for m≥1

\[
c_{0,m}=\frac d m c_{1,m-1},\qquad
\boxed{c_{j,m}=\frac{(d-j)c_{j+1,m-1}+jc_{j-1,m}}{m+j}}\quad (1≤j≤d).
\tag{4}
\]

Compute row m in ascending j using row m−1. This evaluates all d+1 components through m using **O(dm) exact rational operations and O(d) live coefficients** (for any fixed target δ, retain a bounded number of nearby rows according to its fixed Laurent shifts). Integer bit complexity, factorials and output serialization are excluded.

More strongly, write \`f(t)=u_0(t)=Σ_m A_d(m)t^m/(m!)²\`. From (3),

\[
u_1=f'/d,\qquad
u_{j+1}=\frac{t u_j'+ju_j-ju_{j-1}}{(d-j)t}\quad(1≤j<d).
\tag{5}
\]

Thus every u_j is a **finite rational-Laurent differential operator in f**, and by (1)–(2) so is every marked series. Every \`H_m^{(d)}(δ)\` is consequently a **finite, explicitly constructible rational-in-m linear combination of nearby values A_d(m+s)** for fixed δ. This is exact post-observer information-preserving algebra; it does **not** identify intermediate Cell/port/phase histories or assert global BRC state equivalence.

**Example (all m≥0, i≠j, d=6):**

\[
\boxed{H_m(2e_i-2e_j)
=A_6(m)-\frac{A_6(m+1)}{3(m+1)}
+\frac{A_6(m+2)-6A_6(m+1)}{30(m+1)^2}.}\tag{6}
\]

Proof: \`t²g₂²g₀⁴=(g₀-g₁)²g₀⁴=u₀-2u₁+u₂\`; use \`u₁=f'/6\` and \`u₂=(t f''+f'-6f)/(30t)\` and extract exact coefficients. QED.

## Theorem 1007.3 — COMPLETE four-shift scalarization of the absorbed X6 first interior

Use the proven eleven polynomial coefficients \`K_α(n)\` and eleven shift representatives from PREFIX-1005. Set m=n−4≥1 and \`A(m)=A₆(m)\`. Then **for every integer n≥5**,

\[
\boxed{\begin{aligned}
36^n M^L_{n,1}={}&6(36m+25)^2 A(m)\\
&+\frac{12(396m^3+869m^2+443m+36)}{m+1}A(m+1)\\
&-\frac{2(141m^4+614m^3+418m^2-827m-706)}{(m+1)(m+2)}A(m+2)\\
&+\frac{2(2m+3)(m^2+2m-6)}{m+2}A(m+3).
\end{aligned}}\tag{7}
\]

**Proof and finite algebra certificate.** By PREFIX-1005, the exact numerator is \`Σ_α K_α(m+4)H_m(δ_α)\`. Derive the Laurent operator for each δ_α using (1),(2) and substitute (5). For a monomial \`a t^q f^(r)\`, its contribution to the marked integer is

\[
a\,\frac{(m!)^2}{(m-q)!\,(m-q+r)!}\,A(m-q+r),
\tag{8}
\]

when m−q≥0, and zero otherwise. Terms with negative q use ordinary positive factorials; this is a formal power-series identity, including low m. In all eleven orbit operators \`r-q∈{0,1,2,3}\`. Collect each shift \`s=r-q\`, substitute the **exact** K_α quadratic polynomials and clear the (m+1),(m+2) denominators. Straight polynomial coefficient simplification gives respectively the **four rational functions displayed in (7)**. The companion SymPy checker recreates all eleven operators independently from the formal recurrence, verifies the four rational-function identities identically (not by numerical fitting), and checks the exact old orbit sum at n=5…50. Thus the earlier apparent need for eleven independent marked collision sequences **disappears for this explicitly scoped scalar observer**. QED.

## Reproducible validation and boundary

1. A separate Fraction-only checker computes (4) and all marked Laurent factors; it agrees with direct six-label multinomial enumeration for **all eleven orbits plus three additional sign/size cases at m=0…8 (126 exact comparisons)**.
2. The generated finite A-only differential operators agree with the seven-state coefficients for those fourteen test shifts at m=0…31 (**448 exact comparisons**) using **independent** \`A_6\` multinomial convolution, including the explicit identity (6).
3. Old PREFIX-1006 masked masses at n=5,6,8,20,30 match exactly. The four-shift polynomial certificate matches the eleven-orbit sum for n=5…50. New direct seven-state evaluations extend the same scalar to n=300.
4. These are author-proved exact integer/formal-series conclusions, not independent mathematical review, proof-assistant certification, canonical Task Result or a new native Stage46 experimental run. The sign-cover kernel and final-observer formula are inherited from the pinned PREFIX-1003–1005 science. π, trigonometry and physical heartbeat time are not inputs to these calculations.

**Next:** use (7) to derive a shorter standalone recurrence for the masked first-interior sequence from the exact seven-dimensional Q(t) differential module, including explicit minimal recurrence order; separately build the full five-step typed Z₂ prefix transfer for two negative steps k=2 to test where the four-shift scalar quotient ceases to be safe. The mother problem \`B_fix,odd(32)∈{19,20}\` remains open.

**Control provenance:** Historical R6 \`EM-DIRECT-FBEA5D\` and Activity \`RA-3FB2D033BE6048D8712FF056\` are **source attribution only**. The current managed SID \`MCP-45ad6d29cd534c1aad25595a72e3c532\` has reported \`execution_authorized=false\`; no shared CLAIM/PROGRESS or Activity CAS is implied by this GitHub science publication.
