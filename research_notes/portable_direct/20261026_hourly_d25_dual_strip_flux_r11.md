# D25/LIFT — Dual corrected-Clausen finite-strip operator flux and harmonic port

Date: 2026-10-26. Research lane: chatgpt-research-hourly-enterprise-math-20260923. Parent Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged.

**Status:** AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY. This is external corrected-Clausen algebra, not native CM/divided-power evidence, scientific acceptance, or an authorized Source checkpoint.

## Inputs, new problem, and coefficient ring

Consume (without re-claiming) the exact rank/Hasse recurrence at research_notes/portable_direct/20261025_hourly_d25_clausen_operator_rank_boundary.md and the three-channel p^4 reflection/polar reconstruction at research_notes/portable_direct/20261026_hourly_d25_three_channel_clausen_p4_residue_polar_r11.md. New question: evaluate **both** rank-strip boundary fluxes under the actual corrected parameter operator, rather than extrapolating a homogeneous equation from a truncated strip.

Take prime p=6m+1>=7, J=2m, K=p-J=4m+1, theta=z*d/dz, and set

\[
u_{a,r}=[t^a]\frac{(-m-t)_r(-2m-2t)_r}{(1-p/2-3t)_r\,r!}.
\]

For a<0 set u_{a,r}=0; u_{a,0}=1 exactly at a=0, otherwise 0. For r<p all denominators are p-local units. Define

\[
L_0=\theta(\theta-p/2)-z(\theta-m)(\theta-2m),\quad
L_1=3(z-1)\theta-4mz,\quad L_2=-2z.
\]

The lower strip is A_a(z)=sum_{j=1}^{J}u_{a,j}z^j and the mirrored upper strip is B_b(z)=sum_{ell=1}^{J}u_{b,p-ell}z^ell. In the original ordered reflection ell<=j, with distinct channels (a,b)=(0,2),(1,2),(0,3).

## Theorem 1 — lower strip has exactly two boundary degrees

For every Hasse order a>=0, with A_{negative}=0,

\[
\boxed{L_0A_a+L_1A_{a-1}+L_2A_{a-2}
=(2m^2[ a=0 ]+4m[ a=1 ]+2[ a=2 ])z
+(2m\,u_{a-1,J}-2u_{a-2,J})z^{J+1}.}\tag{1}
\]

Proof: In the untruncated coefficient recurrence all coefficients at ranks 1..J vanish. Suppressing rank 0 removes shifted terms -2m^2 u_{a,0}, -4m u_{a-1,0}, -2 u_{a-2,0} at rank 1, hence the positive first port. Rank J+1 is only the shifted predecessor: the u_{a,J} coefficient -(J-m)(J-2m) vanishes, leaving +2m u_{a-1,J}-2u_{a-2,J}. No other powers survive. This holds exactly in the p-local coefficient ring.

## Theorem 2 — high strip reflected dual operator retains *both* endpoints

Define mirrored operators, with theta acting on z as before,

\[
R_0=(p-\theta)(p/2-\theta)-z^{-1}(p-\theta-m)(p-\theta-2m),
\]
\[
R_1=3(z^{-1}-1)(p-\theta)-4mz^{-1},\quad R_2=-2z^{-1}.
\]

Put

\[
\Lambda_{b,K}=(K-1-m)(K-1-2m)u_{b,K-1}-
(3(K-1)-4m)u_{b-1,K-1}+2u_{b-2,K-1},
\]
\[
J_{b,p}=-(p-1-m)(p-1-2m)u_{b,p-1}+
(3(p-1)-4m)u_{b-1,p-1}-2u_{b-2,p-1}.
\]

Then

\[
\boxed{R_0B_b+R_1B_{b-1}+R_2B_{b-2}=J_{b,p}+\Lambda_{b,K}z^J.}\tag{2}
\]

Proof: Use the unreflected high strip H_b(w)=sum_{r=K}^{p-1}u_{b,r}w^r. The exact rank recurrence annihilates all interior ranks; at r=K the omission of rank K-1 leaves Lambda, and at r=p the omitted cutoff gives J. Hence (L_0H_b+L_1H_{b-1}+L_2H_{b-2})(w)=Lambda w^K+J w^p. Conjugate by B_b(z)=z^pH_b(z^{-1}), so theta_w maps to p-theta_z and multiplication by w maps to z^{-1}. This yields (2), including BOTH the constant cutoff and the rank-K (z^J) source.

For b=2 and 2m<r<p, both numerator factors have one simple t-zero (at k=m and k=2m), giving the exact leading-jet reduction

\[
\boxed{u_{2,r}\equiv\frac{2(-1)^m m!(2m)!(r-m-1)!(r-2m-1)!}{(r!)^2}\pmod p.}\tag{3}
\]

In particular

\[
\boxed{\Lambda_{2,K}=6m^2u_{2,4m}\not\equiv0\pmod p.}\tag{4}
\]

Using Wilson reflection (p-1-s)! = (-1)^{s+1}/s! (mod p) for s=m+1 and 2m+1, equation (3) at r=p-1 gives

\[
u_{2,p-1}\equiv2/((m+1)(2m+1))\equiv18/5,\quad
\boxed{J_{2,p}\equiv-2\pmod p.}\tag{5}
\]

Thus two distinct high-strip boundary sources are **independently nonzero** in channel b=2, even mod p. This does not rule out an eventual proven cancellation after the actual ordered signed observer is applied.

## Theorem 3 — harmonic criterion for the third Hasse channel

For 2m<r<p and H_n=sum_{i=1}^n i^{-1} in F_p,

\[
\boxed{\frac{u_{3,r}}{u_{2,r}}\equiv
H_m-H_{r-m-1}+2H_{2m}-2H_{r-2m-1}+3H_r\pmod p.}\tag{6}
\]

Proof: Extract the two t-zero factors, then the remaining logarithmic derivative is
-sum_{k != m}(k-m)^{-1} -2sum_{k != 2m}(k-2m)^{-1} +3sum_{k=0}^{r-1}(k+1-p/2)^{-1}.
Split the first two at the missing roots and reduce the last denominator modulo p; division by u_{2,r} is legal from (3).

For r=4m, write E_m=H_m-H_{3m-1}+m^{-1}+3H_{4m}. Then

\[
\boxed{\Lambda_{3,K}\equiv u_{2,4m}(6m^2E_m-8m)\pmod p.}\tag{7}
\]

Therefore Lambda_{3,K}=0 (mod p) iff E_m=4/(3m) (mod p). This is an exact harmonic *criterion*, NOT a universal nonvanishing claim.

## Checks, observer integrity, continuation

Companion Python stdlib checker constructs the full corrected Pochhammer jets modulo p^2 through order 4, validates the two polynomial strip equations coefficientwise (Hasse orders 0..4), factorial nonzero port, cutoff -2, harmonic ratio at all 2m<r<p, and Lambda_3 criterion. **Author-executed: PASS for 80 target primes 7<=p<=997, p≡1 mod6.** At p=13: m=2, upper Lambda_{2,9}=8 (mod13) and cutoff J_{2,13}=11 (mod13). Checks are finite and not an independent review or substitute for the proofs.

**BRC COMPOSE_APPLIED:** keep the tagged rank, Hasse index, p-local valuation, signed coefficient, low/high strip, reflection orientation, and boundary-source port. The scalar tail projection is not known to preserve the shifted quadratic operator; dropping rank-1/K/J+1/p ports is information loss without an actual factorization proof. This is an external algebraic model, not a declaration of a six-axis native-plane embedding.

**Next exact unit:** apply (1),(2) jointly to the real triangular ell<=j weighted Hasse channel product, carry diagonal ell=j and two endpoint sources, then derive a coupled WZ/adjoint cancellation or a certified nonzero defect. For original-class D25/LIFT, actual H0/B0, [X]U mod p^2, native Frobenius direction/normalization and kappa mapping remain unresolved. Parent OPEN; no native Source CLAIM/OPEN/publish, Result, review or admission is claimed by this portable note.
