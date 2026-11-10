# PREFIX-677-R6 — Local Taylor proof enlarges the BRC diagonal–edge crossover band

Date: 2026-11-11 (Asia/Shanghai).
Status: AUTHOR_DERIVED / EXACT_FRACTION_IMPLICATION_CHECKED / UNREVIEWED / NOT_ADMITTED.
Science pin (unchanged): f42f2906d77f24085c123f3ccfe9667d41caa96d.
Dependencies: original 189-level frozen BRC Poisson observer, local exact jet certificate d344451396a9bace91a9cbcdb14475c6641a9223, previous explicit radius certificate 3e6943a4350e168d62681a62bed140cb23216d86.
Observer parameters p,z are scalar observation probabilities for a typed Heartbeat World X6 path model, not native spatial axes. No P000 change or formal task claim.

## Theorem: 4000/17 times wider rational radius and an explicit q-band

For independent frozen first-stop clocks Y_p,Y_z, write Y(p,z)=max(Y_p,Y_z), mu=E[Y], W=Var(Y), and V_q=q²W-q mu.
Let A(z)=W(z,z)-W(0,z), B(z)=mu(z,z)-mu(0,z), D(q,z)=q(qA(z)-B(z)), q0(z)=B(z)/A(z) and R(z)=B'(z)A(z)-B(z)A'(z).
Set b=53/1000, rho=1/170000000 and I=[b-rho,b+rho].

For every real z in I:
- 439/1000 < A(z) < 442/1000;
- 1789/100 < q0(z) < 449/25;
- R(z)>200 and q0'(z)>1000.

For **each real q in [17948783/1000000,17948794/1000000]**, there exists **exactly one** z_q in I such that V_q(z_q,z_q)=V_q(0,z_q). The sign of D(q,z) within I is strictly positive for z<z_q and strictly negative for z>z_q. The new radius divided by the previous 1/40000000000 radius equals 4000/17 (>235).

## Complete reduction and proof

1. Exact predecessor 189-layer Fraction jet at b gives
   11/25 < A(b) < 441/1000,
   789/100 < B(b) < 79/10,
   -1681 < A'(b) < -1680,
   128 < B'(b) < 129,
   17948788665/10^9 < q0(b) < 17948788666/10^9.
   Hence R(b) > (11/25)*128+(789/100)*1680 = 332788/25.

2. Normalized survivor Bernstein coefficients of the frozen model are in [0,1], degrees n<=188, giving |s_n'|<=188 and |s_n''|<=70312. Applied to the exact two-clock first and second moment kernels of PREFIX-676, this yields the global, real-parameter bounds |A''(z)|<=A2=281945567232 and |B''(z)|<=B2=133031808 for 0<=z<=1/2. The preceding explicit-radius certificate derives these inequalities from the finite Poisson moments.

3. For |z-b|<=rho, Taylor's theorem yields |A(z)-A(b)|<=dA=1681*rho+A2*rho²/2, |B(z)-B(b)|<=dB=129*rho+B2*rho²/2. Define A_min=11/25-dA, A_max=441/1000+dA, B_min=789/100-dB, B_max=79/10+dB. Direct Fraction comparisons verify A_min>439/1000, A_max<442/1000, B_min>0, B_min>(1789/100)A_max and B_max<(449/25)A_min.

4. The cancellation R'=B''A-B A'' gives |R'|<=L=B2*A_max+A2*B_max throughout I (all relevant A and B are positive). Thus
   R(z)>332788/25-L*rho
   = 62671116307481876441741 / 299865722656250000000 >200.
   Since A>0, q0'=R/A²>200/(442/1000)²>1000. In particular q0 is strictly increasing on I.

5. Integrating q0'>1000 gives q0(I) containing [q0(b)-1000*rho,q0(b)+1000*rho]. The exact center interval in step 1 gives
   17948788666/10^9 -1000*rho < 17948783/10^6
   < 17948794/10^6 <17948788665/10^9+1000*rho.
   The explicit fixed q-band therefore lies in the interior of q0(I). For every q in that band the strictly increasing continuous q0 has a unique inverse z_q in I. Finally D(q,z)=q A(z)(q-q0(z)), and q>0, A>0, prove the asserted sign orientation. QED.

## Evidence, reuse, and next unresolved unit

PREFIX677_R6_LOCAL_TAYLOR_RADIUS_CERTIFICATE.py checks all arithmetic with Python integers and Fraction, including the exact radius gain, derivative budgets, quantitative sign bounds and fixed q interval. PREFIX677_R6_RESULTS.json holds the actual exact output. This is a proof *conditional on verified predecessor local-jet inputs*, not a new execution of the 189-layer path recursion and not an independent review.

The local positive/negative crossing split gives a deterministic regression certificate for q-dependent two-parameter Bernstein pruning. Next: tighten A2,B2 by local signed Bernstein second-derivative bounds; expand toward the PREFIX-676 crossing bracket (13/250,27/500); compare resulting two-dimensional boxes with the full p=0 optimum certified by PREFIX-675.
