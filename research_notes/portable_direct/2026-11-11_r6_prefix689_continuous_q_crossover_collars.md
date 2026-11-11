# PREFIX-689-R6 — Uniform analytic parameter collars around the q=12 and q=24 BRC variance crossovers

Date: 2026-11-11 (Asia/Shanghai). Mode: independent author-side TASK_RESEARCH. Frozen scientific pin: \`f42f2906d77f24085c123f3ccfe9667d41caa96d\`. The object is the exact finite 189-row independent Poissonized first-stop observer of PREFIX-688, not a newly claimed native Heartbeat evolution or physical identification.

## Definitions and inherited evidence

For that *same frozen model*, let Y(p,z) be the maximum of two independent Poissonized first-stop times and set

A(z) = Var(Y(z,z)) - Var(Y(0,z)),
B(z) = E[Y(z,z)] - E[Y(0,z)),
F_q(z) = q A(z) - B(z).

For q>0 the normalized variance contrast has the same sign as F_q(z): V_q(z,z)-V_q(0,z) = q F_q(z), where V_q=q² Var(Y)-q E[Y].

Use the immutable PREFIX-688 source files:
- \`research_notes/portable_direct/2026-11-11_r6_prefix688_low_slot_exact_local_crossover.md\`;
- \`research_notes/portable_direct/PREFIX688_R6_RESULTS.json\`;
- \`research_notes/portable_direct/PREFIX688_R6_CROSSING_BRACKETS.py\`.

PREFIX-688's exact integer/Fraction calculation established endpoint signs, midpoint derivative jets (integer floors scaled by 10^6) and local uniqueness for q=12 and q=24. Its third-derivative bound is inherited from PREFIX-680:

|q0|[l,u]|F_q0(l) floor at 10^9|F_q0(u) floor at 10^9|A(c) floor at 10^6|A'(c) floor at 10^6|A''(c) floor at 10^6|B'(c) floor at 10^6|B''(c) floor at 10^6|
|---|---|---:|---:|---:|---:|---:|---:|---:|
|12|[0.0528706,0.0528708]|2028625|-2009751|656742|-1671941380|-66726857069|128587655|-989565080|
|24|[0.0530655,0.0530659]|8857119|-7369717|329445|-1684945674|-66650317279|128394438|-992151722|

M_A3=218571424275456; M_B3=69527880576 are valid on [0,1/2]. A floor m at scale 10^6 means m/10^6 <= X < (m+1)/10^6 (including negative m). Likewise for signed endpoint F floors at 10^9.

## New theorem: continuum collars and comparative slopes

**Theorem 689.1 (q near 12).** For **every real** 11.997 <= q <= 12.003, the equation F_q(z)=0 has exactly one solution z(q) in the OPEN interval (0.0528706,0.0528708). Across this entire closed z-window and q-band,

0.656 < A(z) < 0.657,
-20220 < partial_z F_q(z) < -20170 < 0.

The root is continuously differentiable, strictly increasing in q, and

0.656/20220 < dz/dq < 0.657/20170.

Consequently any 11.997 <= q1<q2 <=12.003 satisfy

(0.656/20220)*(q2-q1) < z(q2)-z(q1) < (0.657/20170)*(q2-q1).

**Theorem 689.2 (q near 24).** For **every real** 23.978 <= q <= 24.022, F_q(z)=0 has exactly one solution z(q) in (0.0530655,0.0530659). Throughout this closed window and band,

0.329 < A(z) < 0.330,
-40720 < partial_z F_q(z) < -40420 < 0,

and

0.329/40720 < dz/dq < 0.330/40420.

The corresponding strict two-sided Lipschitz inequalities hold for any q1<q2 inside this band.

The two spatial windows are disjoint, with the entire q-near-12 branch left of the q-near-24 branch.

## Exact proof

For each row define midpoint c=(l+u)/2, radius r=(u-l)/2 and delta=0.003 or 0.022. Denote the exact inherited jet interval for derivative order j by I_Aj, I_Bj: each is [floor/10^6, (floor+1)/10^6]. Write |I|_max=max(abs(inf I),abs(sup I)).

(1) Taylor with inherited global third-derivative bound gives throughout [l,u]:

A(c) - E_A <= A(z) <= A(c)+E_A,
E_A = |I_A1|_max r + |I_A2|_max r²/2 + M_A3 r³/6.

Using the two strict rational endpoints for A(c), the checker proves 0.656<A<0.657 for the first window and 0.329<A<0.330 for the second.

(2) For F'_q0(c) = q0 A'(c)-B'(c), interval arithmetic on the exact floors supplies rigorous center bounds. The center to window excursion is at most

E_F = [q0 |I_A2|_max + |I_B2|_max] r + (q0 M_A3 + M_B3)r²/2.

Additionally, |A'(z)| <= |I_A1|_max + |I_A2|_max r + M_A3 r²/2. Because F'_q = F'_q0+(q-q0)A', the checker evaluates these entire expressions as exact Fraction inequalities and obtains the strict derivative bounds in the theorem uniformly over both rectangles.

(3) The scaled endpoint floor inequalities and A(z)<a_max imply for every |q-q0|<=delta:

F_q(l) >= floor(10^9 F_q0(l))/10^9 - delta*a_max >0;
F_q(u) < [floor(10^9 F_q0(u))+1]/10^9 + delta*a_max <0.

Their exact conservative margins for q0=12 are >461/8000000 at the left and <-31/800000 at the right. For q0=24 the margins are >1597119/10^9 and <-27429/250000000. Thus IVT and F'_q<0 yield existence and uniqueness for all real q in each continuum band.

(4) F_q is a finite polynomial in z and affine in q. At each crossing F'_q<0, so the implicit function theorem gives dz/dq = -A(z)/F'_q(z)>0. Inserting the certified bounds in (1),(2) yields the two-sided slope estimates and integrating gives the asserted strict Lipschitz inequalities.

## Computational scope, provenance and continuation

Verifier: \`PREFIX689_R6_PARAMETER_COLLAR_CERTIFICATE.py\`; output: \`PREFIX689_R6_RESULTS.json\`. Both use standard Python integer and Fraction operations only. The current proof performs a new implication audit on the immutable numerical certificates; it does NOT rerun the 189-row recurrence or independently validate the predecessor's M_A3/M_B3 derivation. Result: ALL_CHECKS_PASS PREFIX689-R6.

This extends the two isolated q=12,24 local uniqueness results to **two genuine continuous q-neighborhoods** and proves a quantitative monotone continuation map within each. It does not assert a complete root count outside the stated windows.

NEXT SCIENTIFIC UNIT: build a genuine signed interval/Bernstein certificate for A'<0 and B'>0 (or directly F'_q<0) on the connecting region 0.0528708 <= z <= 0.0530655; compare with exact endpoint signs and decide whether a single monotone crossing branch connects q=12 through q=24. In parallel, extend the q-specific root-count certificate to the full 0.052<=z<=0.054 before connecting to the PREFIX-675 2D variance maximum.

STATUS: AUTHOR_DERIVED / EXACT_RATIONAL_IMPLICATION_CHECKED / UNREVIEWED / NOT_ADMITTED.
