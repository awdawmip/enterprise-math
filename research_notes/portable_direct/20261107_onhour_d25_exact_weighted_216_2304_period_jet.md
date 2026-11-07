# D25 — Exact *weighted* 216/2304 period correspondence and first jet

Date: 2026-11-07. Mother task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7, frozen science c47e13e4aba0e006366f989d6334d443f6333ae3. Consumes the two successive explicit Fricke map/second-cusp notes at commits 7f5107ce41724bbcf5efdc47c2f58d8649bf4ace and a07c5f834461bcac510491782eb67a7143918456. AUTHOR_SIDE_PROVED / EXACT_SYMBOLIC_CHECKED / UNREVIEWED / NOT_ADMITTED.

## The exact first-jet result

Define the analytic hypergeometric periods
[
U(z)={}_3F_2(	frac12,	frac13,	frac23;1,1;z),quad
B(w)={}_3F_2(	frac14,	frac12,	frac34;1,1;w)
]
and their positive-term coefficients
[
a_k=inom{2k}{k}^2inom{3k}{k}/216^k,quad
b_k=inom{2k}{k}^2inom{4k}{2k}/2304^k.
]
The prior exact second-cusp transformation proves, on 0<t<12+12sqrt(3),
[
U(z(t))=H(t)B(w(t)),quad
H(t)=rac{3(t+12)^2}{2(t^2+36t+216)},
]
with the degree-(6,8) rational functions z,w explicitly stored in the predecessor.

**Theorem.** The complete *first derivative* connection at the frozen special arguments is
[
oxed{
U'(	frac12)=Big(rac12-rac{sqrt2}{4}Big)B(	frac19)
+rac49 B'(	frac19).}	ag{1}
]
It follows that the full weighted infinite sums satisfy the exact real identity
[
oxed{
sum_{k=0}^infty (6k+1)a_k
=rac32sum_{k=0}^infty(8k+1)b_k.}	ag{2}
]

**Proof.** Put t_*=6sqrt(2), which belongs to the principal analytic interval and obeys z(t_*)=1/2, w(t_*)=1/9. Direct differentiation of the rational maps and H gives the exact values
[
H(t_*)=rac{3sqrt2}{4},qquad
left.rac{H'}{z'}ight|_{t_*}=rac12-rac{sqrt2}{4},qquad
left.rac{H w'}{z'}ight|_{t_*}=rac49.
]
The chain rule on U(z(t))=H(t)B(w(t)) gives (1). Now
(U(1/2)=rac{3sqrt2}{4}B(1/9)) from the prior theorem. Since
(sum (6k+1)a_k=U(1/2)+6(1/2)U'(1/2)) and
(sum(8k+1)b_k=B(1/9)+8(1/9)B'(1/9)), substitution cancels the algebraic square-root contribution and yields
[
U(1/2)+3U'(1/2)=	frac32 B(1/9)+	frac43 B'(1/9)
=	frac32[B(1/9)+	frac89 B'(1/9)].
]
All series are absolutely convergent, so termwise differentiation is valid at the interior arguments. QED.

## Scientific interpretation and exact next action

This proves a global analytic correspondence for the **weighted** sequences used in the frozen 216/2304 finite-sum supercongruence program; it is stronger than the old 110-digit unweighted agreement, and it directly retains the first derivative/weight rather than losing it when squaring periods. In BRC terms the two full positive-series observer ports and their weighting differential operators have an exact common readout after a factor 3/2, with the common t branch and normalization recorded.

This **does not** entail (W_p=(3/2)V_p) for finite sums: the cutoff and Frobenius introduce an integral boundary defect. For comparison, the separate empirical finite-sum fourth-digit conjecture is (2V_p-W_p-p(rac{-3}{p})equiv0mod p^4), with distinct coefficient 2 and a quadratic twist. The rigorous next unit is therefore the *finite-truncation defect of (2)*, first at exact p=19 and p=373, retaining termwise p-adic valuations and the existing p^4 signed tail/Wilson correction, rather than applying the infinite 3/2 multiplier to a finite sum.

Symbolic check: differentiate H,z,w at t_*, use exact Q(sqrt2), verify coefficients (1/2-sqrt2/4,4/9), and the (3/2,4/3) weighted combination. The predecessor checker verifies the rational maps, q-identities, special fiber and Gauss gauge. This is author-side analytical proof; Source Result remains unadmitted. Native p373 same-original-class H0/B0/Frobenius and independent reproduction remains separate #1559.
