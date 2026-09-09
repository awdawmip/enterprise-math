# Two-port p³ reconstruction and the remaining LIFT scalar

Status: **DRIVER-DERIVED COROLLARY CANDIDATE / NONAUTHOR CHECK PENDING**.

Author: EM-DVR-57CCCE. This is a new source-level derivation within the existing JT2 line, after math-authoring activity RA-ED57445DEB6CD03150685A3C was registered. It is not covered automatically by the earlier reference reports and creates no formal Task execution, Result, DR or parent closure.

## Inputs and notation

Consume the finite F_p,L_p, Q2 p² factor and exact prefix from source9e3a41dc, and the residual reflection relation proved in [08ad2fe0](https://github.com/awdawmip/enterprise-math/blob/08ad2fe0fac52949207ddc3559ad70a1b95b577a/research_artifacts/JT2_PERSISTENT_LINE_DRIVER_20260909/research/qtf3_reflection_degree_57ccce_20260909/qtf3_reflection_degree_candidate.md) and checked in [6fa23a3b](https://github.com/awdawmip/enterprise-math/blob/6fa23a3bcb01b13413827fa20e736fea8b9503d8/research_artifacts/JT2_PERSISTENT_LINE_DRIVER_20260909/reviews/qtf3_advisory_ef9380_20260909/reference_review.md):

\[
D(u)=L_p(u)-F_p(\phi(u))=p^2u^p r(u),\quad
\phi(u)=4u(1-u),\quad r(u)+r(1-u)\in pR[u],
\]
where R=Z_(p), p>3 and p≡1 mod6. No old prime scan or tail proof is replayed.

## 1. Repaired two-port polynomial relation

Put a(u)=(1-u)^p, b(u)=u^p and W(u)=a(u)+b(u). Multiplying the two residual equations gives

\[
\begin{aligned}
&a(u)L_p(u)+b(u)L_p(1-u)-W(u)F_p(\phi(u))\\
&\qquad=p^2u^p(1-u)^p\bigl(r(u)+r(1-u)\bigr)\in p^3R[u].
\end{aligned}
\]

Thus the candidate relation is the **cross-multiplied, two-port** congruence

\[
\boxed{
(1-u)^pL_p(u)+u^pL_p(1-u)
\equiv\bigl((1-u)^p+u^p\bigr)F_p(4u(1-u))
\pmod {p^3}.}
\tag{TP3}
\]

This is not the unweighted assertion L_p(u)=F_p(φ(u)) modulo p³ for every u.

W≡1 modulo p. If a normalized readout is desired, W is a unit modulo p³: with s=W-1 in pR[u], the explicit witness is W(1-s+s²)=1+s³≡1 modp³. Keeping TP3 cross-multiplied avoids materializing that inverse. Dropping W merely because W≡1 modp is not a valid p³ normalization step.

## 2. CM-port reconstruction with exact complementary weights

Now restrict to the existing exchanged-port scope p≡13,19 mod24, in A=R[t]/(2t²-1). Put

\[
u_-=(1-t)/2,\quad u_+=(1+t)/2,\quad
B(x)=L_p((1-x)/2),\quad g=F_p(1/2).
\]

The accepted Frobenius scope gives u_-^p≡u_+ and u_+^p≡u_- modulo p. Because every residual already contains p² and u_-+u_+=1 exactly,

\[
\begin{aligned}
u_-B(t)+u_+B(-t)-g
&=u_-D(u_-)+u_+D(u_+)\\
&\equiv p^2u_-u_+\bigl(r(u_-)+r(u_+)\bigr)
\equiv0\pmod {p^3}.
\end{aligned}
\]

Hence

\[
\boxed{g\equiv u_-B(t)+u_+B(-t)\pmod {p^3}.}
\tag{CM3}
\]

The use of complementary weights is essential: the weights sum exactly to one, and their needed Frobenius comparison is only modulo p after the p² factor. No modulo-p² Frobenius identity or root evaluation was used.

## 3. What this retains in the old divided value

Let
\[
\beta=(B(t)-B(-t))/p^2\pmod p,\qquad q=B(t)/p.
\]
The first quotient is justified by Q2 at the two ports; q is justified only after the inherited CM0 divisibility. CM3 then gives

\[
\boxed{G_{\rm div}=g/p\equiv q-pu_+\beta\pmod {p^2}.}
\tag{G3}
\]

In particular, identifying q with G_div beyond their modulo-p agreement loses the displayed next-digit correction.

Differentiating the coefficientwise Q2 congruence preserves its p² precision. Since B'(t)=-L_p'(u_-)/2 and φ'(u_-)=4t, where t is a unit and t^-1=2t,

\[
F_p'(1/2)\equiv-B'(t)/(2t)\pmod {p^2}.
\]
With s=B'(t) and the old h=(F_p+12zF_p')(1/2), this yields

\[
\boxed{h\equiv B(t)-6ts=pq-6ts\pmod {p^2}.}
\tag{H2}
\]

This differentiates the already retained polynomial congruence; it does not replace the current Sun task's requested adjacent-value elimination.

## 4. Exact remaining scalar, conditional on UR

Under the declared UR input, -6tqs≡1 modp. Define the legitimate divided carry
\[
\eta=\frac{-6tqs-1}{p}\pmod p.
\]

Multiplying G3 and H2 modulo p² gives

\[
G_{\rm div}h\equiv-6tqs+p q^2+6p t u_+\beta s\pmod {p^2},
\]
so the old LIFT is precisely the candidate equivalent condition

\[
\boxed{\eta+q^2+6t u_+\beta s\equiv R_{\rm tail}\pmod p.}
\tag{LIFT-PORT}
\]

The required observations are q and s modulo p² for eta, beta and R_tail modulo p, and the labeled t,u_+ weights. Individual terms live in A/pA; beta has the reflection-odd type. The full expression represents the base-field scalar from G_div h. Do not discard an odd component or a carry before proving the relevant cancellation.

The explicit R_tail and the existing finite identity S_p=g h-T_p, T_p≡p²R_tail modp³ are pinned in the companion [next-observer contract](next_observer_contract.md). They are consumed source reductions. No value of eta or the LIFT-PORT difference is evaluated or asserted to vanish here.

## Boundaries and next check

TP3/CM3 improve the address and normalization interface; they do not prove weighted S_p≡p modp³ or old LIFT. The missing arithmetic statement is now displayed in LIFT-PORT. Sun output3 and its conditional output6 also remain unchanged.

A non-author check should verify the residual weighting/sign, precision before Frobenius, exact sum of CM weights, both legal p divisions, differentiated-Q2 sign, and the product expansion. The prior QTF3 report checks the consumed residual relation, not these newly written corollaries.

This is paper use of the existing typed provenance/precision and T6 future-observer discipline. The coefficients are algebraic/signed carriers, not asserted positive native BRC masses. No mathematical program, native quotient/remainder/root evaluation, new tool family or capability gap is claimed; future evaluated quotients need the existing BRC facade and actual reconstruction witnesses.

Driver-ID: EM-DVR-57CCCE / CONTROL_PLANE

Global-Knowledge-Sync: main@f01bde3 / GLOBAL_KNOWLEDGE_V1
