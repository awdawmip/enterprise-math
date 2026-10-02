# H0M return — exact nonsplit family, scoped transport obstruction, and a missing algebraic seed

Status: RESEARCH_RETURN_FROZEN_AWAITING_DRIVER_REVIEW.
Researcher verdict: EXACT_HARD_BLOCK_WITH_MISSING_OBJECT_AND_UNBLOCK_CONDITION, with a proved scoped discriminant-transport no-go and an actual semiregularity null control.
Date of research: 2026-09-17. The filename retains the published task's 20260831 suffix.

Researcher-ID: EM-PFSS2R-B96E46
Research-Activity-ID: RA-20260917-c49ede787913
Task: RS-HODGE-H0M-WEIL-SIXFOLD-SEMIREGULARITY-OBSTRUCTION-CANCELLATION
Publication: TP2-4D8C1A7E2B609F35C614
Taskbook Git blob: c92aab2a0784814c9d74dfd0042d37c037aa5792
Selection source: 8349d0c93096ffb5f586c7cc692c5c3033e51160
Real claim: issue 240 comment 5708183233, server time 2026-09-17T03:50:12Z, claim chatgpt-20260917-c49ede787913-h0m.
Owner branch: research/h0m-c49ede787913.

## 1. What this return establishes

Prerequisite A is established at an exact unitary-family, very-general-fiber scope: a polarized sixfold family of discriminant [-3] for Q(i), its rational two-dimensional Weil space, and its separation from the divisor algebra. Target B is returned as an exact missing-object classification, not as a cycle-existence theorem. Preferred target C and H1 are not claimed. All conclusions remain researcher evidence pending Driver review. No Working Truth, Foundation, or canonical promotion is granted.

The constructive gain is a precisely identified single missing seed: an actual codimension-three algebraic cycle with nonzero Weil projection on the frozen family. An explicit rational polynomial in an algebraic endomorphism projects onto the entire Weil plane; one nonzero algebraic vector then generates the whole plane under two endomorphism translates. Neither this projector nor semiregularity supplies that seed.

## 2. Current literature and safeguards

The literature ledger records primary-source scope as checked on 2026-09-17. Markman's Theorem 1.5.1 [M25] treats sixfolds of discriminant [-1]; its fourfold consequence must not be promoted to arbitrary sixfold discriminants. His later survey [M26] again states the split sixfold theorem and the generic Hodge/divisor decomposition. The fourfold results of Floccari--Fu and van Geemen--Rapagnetta do not close our sixfold family.

The task's Mostaed reference [AM26] does not provide a known-nonempty, prescribed-discriminant model. Its proposed CM intersection is not used here. Isolation while preserving a full CM action must not be confused with absence of deformations preserving only an imaginary quadratic action: the latter domain here has complex dimension 9.

Two newly surfaced items are disclosed rather than silently ignored. Brosnan's September 2026 abstract [PB26] addresses maximal degeneration; its full text could not be fetched, so it is not a proof input. Indexed original-preprint claims in [RSC26] assert a one-dimensional Weil space and a discriminant-changing inert-prime quotient. Our exact calculations below contradict those displayed intermediate claims. The full page was unavailable, so this is not a complete review of the entire manuscript.

The label CURRENTLY_OPEN_FRONTIER_AT_DECLARED_SCOPE is relative to this dated, qualified ledger, not a proof that no unindexed theorem exists. It is not a claim that every special [-3] fiber is unresolved.

## 3. Actual polarized family and discriminant separation

Let K=Q(i), L=Z[i]^6, and h(z,w)=conjugate(z)^t H w, with

H=diag(1,1,1,-1,-1,-3).

On L_R set E=Im h. In coordinates z_j=x_j+i y_j it is the integral alternating form sum d_j dx_j wedge dy_j. Let J0 act as +i on the first three coordinates and -i on the last three. Then J0^2=-1, J0 commutes with the K action, E(J0x,J0y)=E(x,y), and E(v,J0v)=sum |d_j| |v_j|^2>0. The Riemann relations therefore give a projective complex torus. Its polarization type is (1,1,1,1,1,3); no principal-polarization hypothesis is slipped in.

The compatible complex structures form the connected domain U(3,3)/(U(3) x U(3)), of complex dimension 9. Quotient by the integral unitary group with level 3, or retain the marked analytic family. Choose a very general point outside proper rational Hodge/endomorphism loci. J0 is a decomposable existence control only; it is not substituted as the test fiber.

The determinant is -3. The solved control has class [-1] in Q*/N(K*). Their ratio 3 is not a norm. Indeed, after clearing denominators, a sum A^2+B^2 divisible by 3 has both A and B divisible by 3, by reduction modulo 3. Divide out their maximal common 3-power. The remaining sum has valuation zero, so every nonzero rational norm has even 3-adic valuation. Since v_3(3)=1, [-3] differs from [-1]. The dual determinant -1/3 gives the same class, since its ratio to -3 is N(1/3)=1/9.

This is an infinite arithmetic proof; residue enumeration and nine rational-matrix tests are checks of it, not substitutes for it.

## 4. Exact rational Weil carrier

For V=H^1(A,Q), dim_Q V=12 and dim_K V=6. Over C, V=V_i direct-sum V_-i. Each six-dimensional eigenspace has three (1,0) and three (0,1) directions. Consequently det(V_i) and det(V_-i) have bidegree (3,3). They are exchanged by conjugation and descend to a rational plane W. This is the precise embedding meant by wedge_K^6 V; no naive inclusion of different exterior powers is presumed.

With e_j=dx_j, f_j=dy_j, I*e_j=-f_j and I*f_j=e_j, set omega=wedge_j(e_j+i f_j), r=Re omega, s=Im omega. Then W=Q r+Q s. For the Lie derivation D of I* on wedge^6 V, D r=-6s and D s=6r. Hence W is contained in ker(D^2+36).

On wedge^a V_i tensor wedge^(6-a) V_-i, D has eigenvalue i(2a-6), with multiplicity binom(6,a)^2. Only a=0,6 contribute to that kernel, each with multiplicity one. Thus dim_Q W=2 exactly. The checker independently assembles the occupancy blocks of the 924-dimensional exterior space and obtains rank(D^2+36)=922.

For the very-general fiber, the standard generic Weil-family theorem gives NS_Q=Q theta [M25, section 1.1; M26, section 1.1]. D annihilates theta and theta^3. Since D^2=-36 on W, W intersects Q theta^3 trivially. This generic qualification matters: it is not asserted on every decomposable or CM fiber.

## 5. M1/M3: precise transport no-go, not a universal correspondence no-go

Suppose an allowed rational K-linear transport identifies Hermitian forms by H'=c conjugate(M)^t H M, with M invertible over K and positive rational c. Then

det H'/det H=c^6 N(det M)=N(c^3 det M).

The discriminant class is therefore invariant under every such step and every finite composition. This covers compatible polarized isogenies, Hecke steps inside the fixed unitary similitude datum, and compatible rational basis changes. Duality replaces delta by delta^-1=delta, since q^2=N(q). Deformation inside the fixed polarized K component preserves the discrete class. None of these routes reaches the split control.

At the very-general NS-rank-one scope, pullback of a polarization along a K-compatible isogeny is a positive rational multiple, so the hypothesis is substantive rather than merely a notation restriction. However, an arbitrary algebraic correspondence acting on H^6 is not automatically an H^1 similitude. Nor is an unspecified Fourier--Mukai kernel automatically of this type. Those routes remain uncovered until a concrete kernel and its exact action are supplied. We do not prove that every imaginable derived transport, or every algebraic cycle, is impossible.

The defect registry separately records available family dimension and Hodge invariance; it records missing candidate sheaf, characteristic class, and Ext maps without inventing them.

## 6. M2: an actual zero-trace but nonzero obstruction

On the fixed sixfold take E=O_A direct-sum O_A. Its Atiyah class is zero. Therefore its semiregularity map is matrix trace on Ext^2(E,E)=H^2(O_A) tensor M_2(C), followed by zero higher components. Its domain dimension is 60, rank 15, and kernel dimension 45.

Let u,v be linearly independent invariant (0,1)-forms, X=E12, Y=E21, and alpha=u X+v Y. This is a first-order bundle deformation because dbar alpha=0. Its quadratic Maurer--Cartan obstruction is

alpha wedge alpha=(u wedge v)[X,Y]=(u wedge v)diag(1,-1).

It is nonzero in H^2(O_A) tensor M_2(C), because u wedge v is a nonzero invariant Dolbeault class. Thus there is no beta with dbar beta=-alpha wedge alpha; this first-order deformation does not extend modulo t^3. Yet its entire semiregularity image vanishes: the matrix trace is zero and the higher Atiyah channels vanish. This refutes automatic cancellation from zero trace. It does not contradict the semiregularity theorem, whose injectivity hypothesis fails.

The object has ch_3(E)=0. It is a mandatory negative control, not an exceptional-cycle generator. The calculation is ordinary derived deformation theory and receives zero strict Enterprise attribution.

BRC applicability was audited after fixing the question. Here contributions are signed/complex and matrix-valued, composed by graded multiplication. The positive Weighted-BRC engine is inapplicable; no positive histogram is substituted. The typed-observer discipline is reused: the trace quotient forgets a 45-dimensional component needed by the future full-obstruction observer. That component is retained. No primitive geometry or global Foundation rule is altered.

## 7. M4: a conditional, entirely algebraic single-seed compiler

Let T=[1+2i]^* on H^6(A,Q). Its eigenvalues, according to a=0,...,6, are

117-44i, -35+120i, -75-100i, 125, -75+100i, -35-120i, 117+44i.

The Weil factor is q(x)=x^2-234x+15625. The other factor is

g(x)=(x-125)(x^2+70x+15625)(x^2+150x+15625).

These factors are coprime. Define P(x)=g(x) times the inverse of g modulo q. Then P=1 mod q, P=0 mod g, and P(T) is an idempotent with image exactly W on the full H^6. Its exact rational coefficients are in the class-first registry and checked by polynomial remainder arithmetic. Each power T^j is pullback by the actual algebraic endomorphism [(1+2i)^j]. Thus P(T) acts on rational algebraic cycles; an unproved algebraicity of an abstract Hodge projector is NOT being assumed.

Suppose, conditionally, an actual Z0 in CH^3(A)_Q were supplied with nonzero projected class v=P(T)cl(Z0)=a r+b s. Let Z1=P(T)Z0. In the (r,s) basis T has matrix [[117,44],[-44,117]]. The determinant of the columns v,Tv is -44(a^2+b^2), nonzero for any nonzero rational v. Hence Z1 and T Z1 span all W, and a rational 2x2 solve produces a cycle for any specified target, including negative and denominator-bearing inputs.

Nine exact arithmetic examples check this CONDITIONAL compiler only. They do not instantiate Z0. Divisor-only input is annihilated: theta^3 has eigenvalue 125, so P(T)theta^3=0. The projector cannot manufacture a nonzero class from such input.

The exact missing object is therefore one independently constructed algebraic seed on this same very-general [-3] model with certified nonzero Weil projection. It could come from a new sheaf, cycle, or correspondence. No such seed was obtained in this run. The missing object is not replaced by absolute-Hodge status, a formal characteristic class, or a copied split-locus cycle.

## 8. Checks, attribution, and handoff

The deterministic check returns PASS: polarization/Riemann basepoint controls; exact exterior rank 922/924; rational Weil dimension 2 and determinant-line Hodge typing; theta^3 separation; polynomial projector identities; nine conditional rational solves; nine exact determinant examples; norm-residue certificates; and the nonzero trace-free obstruction matrix. The analytic family and universal determinant/norm statements are separately proved above or attributed; no finite test is represented as an open algebraicity proof.

An initial slow exact-rank implementation hit a local timeout. It was replaced by SymPy's exact DomainMatrix rank implementation. A polynomial-domain equality assertion was then corrected to compare the exact remainder expression to 1; the final checker passes. No failed result was published as PASS. Run:

python research_checks/HODGE_H0M_WEIL_SIXFOLD_SEMIREGULARITY_OBSTRUCTION_CANCELLATION_CHECK_20260831.py

All mathematical mechanisms are available to B_std^Weil6. The exact instance, source audit, and conditional compiler are useful researcher work, not a claimed novel Enterprise theorem. Method harvest: RESULT_ONLY. This is nonblind, source-exposed work in a shared ambient context, not an independent blinded replication.

Hard block fields:
- missing_object: an actual codimension-three algebraic seed Z0 with P(T)cl(Z0) nonzero on the frozen model.
- owner: H0M source-object / algebraic-correspondence construction route.
- necessity: neither a Hodge carrier, an algebraic projector, nor a conditional obstruction theorem guarantees such a seed.
- unblock_condition: supply a concrete source-generated cycle/sheaf/correspondence and verify the nonzero projection on this exact family, without a split-source substitution; then execute the compiler and, where transport is needed, compute the actual obstruction maps.

Driver should review this exact classification and its scope. Do not re-dispatch the completed carrier/transport audit as unexplored work, do not silently broaden the no-go, and do not automatically publish H1. A new mechanism outside the proved similitude closure is not ruled out.

## Sources

[M25] Eyal Markman, arXiv:2502.03415v2, https://arxiv.org/pdf/2502.03415v2 .
[M26] Eyal Markman, arXiv:2509.23403v2, https://arxiv.org/html/2509.23403v2 .
[AM26] Amir Mostaed, arXiv:2603.20268v1, https://arxiv.org/html/2603.20268v1 .
[FF26] Salvatore Floccari and Lie Fu, arXiv:2504.13607, https://arxiv.org/abs/2504.13607 .
[vGR26] Bert van Geemen and Antonio Rapagnetta, arXiv:2607.18341, https://arxiv.org/abs/2607.18341 .
[PB26] Patrick Brosnan, arXiv:2609.14169, https://arxiv.org/abs/2609.14169 (primary indexed abstract only; full-text retrieval failed).
[RSC26] Relative Secant Cycles and the Hodge Conjecture, https://www.preprints.org/manuscript/202602.0462/v3 (original indexed excerpts only; full-page retrieval failed).
