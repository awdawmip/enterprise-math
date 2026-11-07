# Stage380-B — Exact Pareto reduction to an active quadratic budget and three residual faces

Research2, 2026-11-02. Author-side theorem in the frozen 16-audit-label, four-residual-channel two-source Bernoulli/BRC auxiliary model. Scientific pins unchanged: global bf84bd7c61a2444b59b1da96be57df0e9ae47e53, Enterprise Math 2af3fc484eb11060b69e0afc1b562bcaf5ad1419, original P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Previous scientific frontier Stage379-B: PR #1736, commit 3dd97cbe4ff6eb293a10d937b59bb976acdb7cdb.

## Definitions and theorem

For k=0,1,2,3 let B_k(z)=z^k(1-z)^(3-k), w=(1,3,3,1), m=(61,21,9,9), and r_k(x,y)=[4B_k(x)+B_k(y)]/5-m_k/160. Define D(a,z)=(1/2)Σ_k w_k|B_k(a)-B_k(z)|, b(x,y)=(5/32)Σ_k w_k|r_k(x,y)| and c(x,y)=[63D(1/4,x)+D(3/4,x)+9D(1/4,y)+7D(3/4,y)]/256. Minimize 33/1024+c(P)+c(Q) over [0,1]^4 subject to b(P)+b(Q)≤B_*:=2β_*+11/5000, β_* the inherited isolated simultaneous r0=r1=0 root budget. A prior exact feasible rational comparison gives nonempty feasibility and continuity plus compactness gives minimizer existence.

Apply the Stage379-B proven localization (swap P/Q if needed):
P=(x_P,y_P)∈(0.2308,0.2345)×(0.55,0.56);
Q=(x_Q,y_Q)∈(0.2365,0.239]×(0.57566,0.57574).

**Theorem.** Every minimizer in these boxes has (i) r0(P)≤0≤r1(P), r1(Q)≥0; (ii) ACTIVE joint budget b(P)+b(Q)=B_*; (iii) on EACH source, b(x,y)=3[4x(1-x)+y(1-y)]/16−45/256; and (iv) at least ONE of r0(P)=0, r1(P)=0, r1(Q)=0. Consequently every global minimizer lies in the three-face union intersected with the exact quadratic budget hypersurface
4[x_P(1−x_P)+x_Q(1−x_Q)]+y_P(1−y_P)+y_Q(1−y_Q)=15/8+(16/3)B_*.
These are codimension-at-least-two exact necessary conditions on the original four parameters.

## Proof: exact sign structure and audit polynomial

The derivatives B0'<0, B3'>0, B1'=(1-z)(1-3z), B2'=z(2-3z) certify monotonicity throughout the inherited boxes. Exact rational endpoint comparisons show the 16 audit signs PER SOURCE (k=0..3): x vs 1/4 (−,+,+,+); x vs 3/4 (−,−,+,+); y vs 1/4 (+,+,−,−); P y vs 3/4 (−,−,+,+); Q y vs 3/4 (−,−,sgn δ(y_Q),+), δ(y)=9/64−y²(1−y). Residual signs are P (?, ?,+,−), Q (−,?,+,−). So 31/32 audit signs and 5/8 residual signs are resolved, while r0(P),r1(P),r1(Q),δ(y_Q) define 16 nonempty open sign chambers in the rectangular tube. The 16 exact rational witnesses in REPRO_STAGE380B.py establish nonemptiness only in the tube, not joint-budget feasibility.

δ(y)=(4y−3)(16y²−4y−3)/64 has its sole Q-box zero α=(1+√13)/8. Expanding ALL original signed 16 audit comparisons per source gives the exact identity
c=C0(x,y)+(21/512)|δ(y)|,
C0=5157/32768−189x/256+93x²/128−61x³/256+33y²/512−29y³/512.
In both boxes c_x=−3(1−x)(63−61x)/256<0. For y<α, c_y=3y(1−y)/64>0; for y>α, c_y=3y(18−25y)/256>0; at α both one-sided derivatives are positive.

Since Σ_k w_k B_k(z)=1 and Σ_k w_k m_k=160, Σ_k w_k r_k=0 exactly. On both boxes r2>0>r3. Therefore the complete four-residual function is
b=(15/16)r2+(5/16)max(r0,0)+(15/16)max(r1,0),
including the sign faces. No residual term is omitted.

## Proof: strict Pareto perturbations

If r0(P)>0, increasing x_P strictly decreases both c and b. In the r1<0 sector b_x=−3(2x−1)²/4<0; in r1>0 sector b_x=−3x²/4<0; at r1=0 the increasing-x side enters r1>0 because r1_x>0.

If r0(P)<0 and r1(P)<0, then b=15r2/16, and b_y=3B2'(y)/16>0; a small negative y_P perturbation strictly improves both cost and budget.

If r0(P)=0 and r1(P)<0, perturb P by t(1/8,−1), t>0. The right derivative of r0 is [B0'(x)−2B0'(y)]/10<0, using (1−x)²>2(1−y)² on P; hence enter r0<0, remain r1<0. The budget derivative becomes 3[B2'(x)−2B2'(y)]/32<0 (because B2'(0.2345)<2B2'(0.56)); cost derivative c_x/8−c_y<0. This excludes the r0=0 boundary in the r1<0 sector.

For Q, r0(Q)<0. If r1(Q)<0, then b=15r2/16, b_y=3B2'(y)/16>0, so decreasing y_Q strictly improves both. These four cases establish r0(P)≤0≤r1(P),r1(Q)≥0 at ANY global minimizer.

On this wedge the exact positive-part formula reduces to b=15(r1+r2)/16. As B1(z)+B2(z)=z(1−z), m1+m2=30, exact simplification yields
b=3[4x(1−x)+y(1−y)]/16−45/256.

## Proof: active budget and face necessity

If the joint budget is slack, increasing x_P slightly stays feasible by continuity but reduces c strictly because c_x<0. Thus b(P)+b(Q)=B_*.

Suppose all three named faces are strict: r0(P)<0<r1(P) and r1(Q)>0. Then both sources lie in the smooth wedge with b_x=3(1−2x)/4>0. Define the marginal cost improvement per budget increment
λ(x)=−c_x/b_x=(1−x)(63−61x)/[64(1−2x)].
Exact differentiation gives λ'(x)=[2+122x(1−x)]/[64(1−2x)²]>1 on [0.2308,0.239] because 378x(1−x)>62 there. Since x_Q>0.2365>0.2345>x_P, λ(x_Q)−λ(x_P)>x_Q−x_P>1/500.

Holding both y coordinates fixed, increase x_Q a small amount and reduce x_P uniquely using the implicit function theorem to preserve the EXACT active quadratic budget. Both b_x are positive and the perturbation stays within original [0,1]^4 and the strict sign sector. Its objective directional derivative is
d[c(P)+c(Q)]/dx_Q=b_x(Q)[λ(x_P)−λ(x_Q)]<−783/1000000,
since b_x(Q)≥3(1−2×0.239)/4=783/2000. Strict improvement contradicts minimality. Hence r0(P)r1(P)r1(Q)=0 in the stated sign wedge. The displayed quadratic equation follows by adding the two exact budget formulas.

## Exact evidence and next question

The self-contained standard-library Fraction checker was executed twice (emit/verify), with byte-identical stdout and 40 exact channel/audit endpoint enclosures, 16 exact sign-chamber rational witnesses, signed audit polynomial coefficients, Pareto inequalities and λ derivative/marginal bound. Marker: STAGE380B_PARETO_FACE_REDUCTION_PORTABLE_PASS. Portable certificate 3350 bytes, SHA256 65c35b8863113dd06903a1e89b855197d7fac7843149272618f01d423a9ac425. An expanded standalone checker and certificate were also executed locally (5670-byte CSV, SHA256 5c4eceb089d1b9d531cc0baca2d4ff5809a844afcb590e2d61b094b4e04a27a9); publication uses the complete shorter portable executable. The certificate is mathematical author-side computational evidence, not independent review.

Stage381-B: classify the three exact cubic faces and their pairwise intersections with the quadratic budget under the original feasibility signs; isolate all stationary/cusp/boundary algebraic candidates, compare exact objective values or produce a strictly cheaper feasible rational competitor. Do not assume y_Q=α. Native P000 X6 3D-slice third-component/update/observer-preservation transfer remains a separate mother-objective obligation.
