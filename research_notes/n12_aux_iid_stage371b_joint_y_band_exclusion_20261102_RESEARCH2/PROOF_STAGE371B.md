# Stage371-B — exact joint two-source central-band necessity

2026-11-02. Enterprise Math Research2 portable author-side theorem; frozen 16-label, four-port Bernoulli/BRC **external auxiliary observer**. This source preserves previous scientific pins (GLOBAL bf84bd7c61a2444b59b1da96be57df0e9ae47e53; Enterprise Math 2af3fc484eb11060b69e0afc1b562bcaf5ad1419). P000 remains ACTIVE_LOCKED V5; no X6 transfer is claimed.

## Definitions and theorem

For k=0,1,2,3 set w=(1,3,3,1), m=(61,21,9,9) and

\[
B_k(z)=z^k(1-z)^{3-k},\quad
r_k(x,y)=\frac{4B_k(x)+B_k(y)}5-\frac{m_k}{160}.
\]

Define
\[
b(x,y)=\frac5{32}\sum_{k=0}^3w_k|r_k(x,y)|,\qquad
D_3(a,z)=\frac12\sum_{k=0}^3w_k|B_k(a)-B_k(z)|,
\]
\[
c(x,y)=\frac{63D_3(1/4,x)+D_3(3/4,x)+9D_3(1/4,y)+7D_3(3/4,y)}{256}.
\]
Each of the four D3 terms is a separate audit port and all 16 port-outcome comparisons remain distinct. The common residual root q* (r0=r1=0) and beta*=b(q*) were isolated in Stages369–370. A pair P,Q in [0,1]^2 is feasible iff b(P)+b(Q) <= 2 beta*+11/5000; minimize T(P,Q)=33/1024+c(P)+c(Q).

**Theorem.** Every global minimizer has **at least one** source with
\[
\boxed{14/25<y<29/50}\qquad(\text{i.e. }0.56<y<0.58).
\]
In the previously established per-source core (577/2500,239/1000] x (27/50,59/100), every feasible pair whose two y coordinates are outside the open central band has a strict total-cost gap relative to the exact feasible reference P0=(231138/10^6,555681/10^6), Q0=(237807/10^6,575694/10^6): at least 29/500000 for low-low, 19/500000 for low-high, and 9/500000 for high-high, all bounds strict. This is a coupled two-source/four-real-parameter exclusion and does not establish global optimality of the cusp candidate.

## Exact proof

Let L=c+(6/5)b, X=[577/2500,239/1000], Rlow=X x [27/50,14/25], Rhigh=X x [29/50,59/100]. The two new universal **real-continuous** inequalities are
\[
\boxed{L>3748/100000\;\text{ on }Rlow},\qquad
\boxed{L>3746/100000\;\text{ on }Rhigh}.
\]

Proof of those bounds: for any exact rational interval [u,v] subset [0,1], B_k has extreme values at endpoints and, if inside, at k/3. Thus the range of each cubic on a box is bounded rationally. For a point t and interval [a,b], the lower bound on |t-z| for z in [a,b] is zero if t is inside; otherwise it is min(|t-a|,|t-b|). Apply this separately to all four r_k error summands and to all **16 individual port-label differences** in the four weighted D3 terms, preserving their distinct source labels. The resulting rational interval lower bounds b_lower(J), c_lower(J) prove L(x,y)>=c_lower(J)+(6/5)b_lower(J) for every real point of each rectangle J. Bisect x if 5*width_x >= width_y, else y; keep both closed halves. Accept a leaf only when its exact rational lower bound is strictly greater than the region's target. The entire two initial closed rectangles are covered including their edges.

The executed exact checker (composing the already published Stage370 checker without changing its formulas) certifies **6257 closed low-band leaves** (6256 splits, depth <=20) and **127 closed high-band leaves** (126 splits, depth <=18), all strictly accepted and with no unresolved leaves. Its deterministic verbose CSV contains 6384 leaves; 1,194,451 UTF-8 bytes, SHA256 8fba0070613f342bd96ac92f49f980bc94e56c723dc8ff443387c072ae47bf01. Regenerate it by running the published REPRO_STAGE371B.py with --emit and an output CSV path. The generator is the complete reproducible interval-certificate specification; integer-ratio arithmetic throughout, with no sampling or float approximation.

The exact Stage369–370 algebraic-root bracket and rational reference bounds, also checked by the imported source program, give
\[
b(P0)+b(Q0)<2\beta_*+11/5000<61/6250,\quad
c(P0)+c(Q0)<6319/100000.
\]
For any feasible pair P,Q in Rlow union Rhigh, use sP,sQ equal to the appropriate strict thresholds. Then
\[
c(P)+c(Q)=L(P)+L(Q)-(6/5)(b(P)+b(Q))
>sP+sQ-(6/5)(61/6250).
\]
Subtract the reference cost (and cancel constant 33/1024). All three exact positive gaps are
\[
2(3748/100000)-(6/5)(61/6250)-6319/100000=29/500000,
\]
\[
(3748+3746)/100000-(6/5)(61/6250)-6319/100000=19/500000,
\]
\[
2(3746/100000)-(6/5)(61/6250)-6319/100000=9/500000.
\]
Stages368–370 already prove that every feasible global minimizer is within their reduced core. The feasible set is nonempty and compact and T is continuous, so a minimum exists. If both y coordinates were outside the open central band, both points would lie in the union of the two certified closed rectangles, where the strict cost gap contradicts optimality. QED.

## Verified extent and remaining questions

The independent standalone local rational checker and the compact published checker reusing Stage370 gave byte-identical certificate CSV and stdout (exact pass label STAGE371B_EXACT_JOINT_Y_BAND_EXCLUSION_PASS). This is author-side interval proof evidence, not Lean/formal-kernel certification, independent review, native Source Result or P000 adoption. Researcher session start was denied STATIC_READONLY_SCOPE_DENIED by the configured Site static-readonly identity; Owner list failed CONTROL_QUOTA. No CLAIM/Driver authority was inferred from GitHub access.

Next Stage372-B: exploit the surviving necessity (at least one y in (0.56,0.58)) and exact coupled budget to test a sharper near-root/near-audit-cusp allocation restriction or construct a strictly cheaper **rational feasible pair**. Preserve frozen inputs, all distinct audit-port labels and native X6 observer-preserving transport as independent work.
