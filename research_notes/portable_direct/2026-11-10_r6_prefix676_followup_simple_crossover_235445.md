# BRC observer: local simple diagonal-edge crossover and positive slot sensitivity (R6 follow-up to PREFIX-676)

Status: AUTHOR_DERIVED / EXACT_RATIONAL_COMPUTATION / UNREVIEWED / NOT_ADMITTED.
Research route: independent TASK_RESEARCH; no formal CLAIM, Result, Review or Foundation promotion.
Frozen scientific source pin: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Immediate predecessor: PREFIX-676, commit cd2c6681a6ed4857bb7d416e82a8642f6cc0739f.
Observer interpretation: p,z are probabilities parameterizing an observable of Heartbeat World X6, not primitive spatial axes. P000 and the frozen recursion are unchanged.

## Problem

PREFIX-676 proved existence of at least one z-crossover in (13/250,27/500), and established the unique slot parameter q0 at z=53/1000 satisfying D_q0(z)=0. Existence alone does not show whether this particular crossover is transverse, locally unique, or how its position responds to varying the slot parameter.

Let s_n(x)=sum_k A_n(k)x^k(1-x)^(n-k), n=0,...,188, from the frozen 189-layer survivor recursion (row 189 is empty). Y_x is the Poissonized first-stop time, and Y(p,z)=max(Y_p,Y_z) for independent clocks. Set mu=E[Y], W=Var(Y), V_q=q^2 W-q mu, and

Delta_mu(z)=mu(z,z)-mu(0,z);
Delta_W(z)=W(z,z)-W(0,z);
D(q,z)=V_q(z,z)-V_q(0,z)=q(q Delta_W(z)-Delta_mu(z)).

## Certified exact-point statement

At b=53/1000 the rational quantities Delta_W(b), Delta_mu(b), Delta_mu'(b) are positive and Delta_W'(b) is negative. In particular the unique slot threshold q0=Delta_mu(b)/Delta_W(b) obeys the *strict rational brackets*

17948788665/1000000000 < q0 < 17948788666/1000000000,

68846312/1000 < q0'(b) < 68846313/1000,

where q0(z)=Delta_mu(z)/Delta_W(z) wherever Delta_W(z) is nonzero.

The same exact computation gives D(12,b)<0<D(24,b), and

partial_z D(q0,b) = -q0 Delta_W(b) q0'(b) < 0,
partial_q D(q0,b) = q0 Delta_W(b) > 0.

By the real-analytic implicit function theorem, there are open neighborhoods of b and q0 and a UNIQUE analytic crossing branch z=z(q) within those neighborhoods satisfying D(q,z(q))=0 and z(q0)=b. It is strictly increasing on a sufficiently small neighborhood, with

1000/68846313 < z'(q0) < 1000/68846312.

The exact local transversality is stronger than the earlier pointwise slot threshold and general crossover existence. No global uniqueness over the entire (13/250,27/500) interval is inferred.

## Exact arithmetic kernel and coverage

For rational a/d, survivor values and derivatives are computed with integer powers:

s_n(a/d)=d^(-n) sum_k A_n(k) a^k(d-a)^(n-k),

s_n'(a/d)=d^(1-n) sum_k A_n(k)[k a^(k-1)(d-a)^(n-k)-(n-k)a^k(d-a)^(n-k-1)],

where zero-coefficient terms are omitted. The original 189-step recurrence produces 9,529 occupied histogram cells; the reused normalized Bernstein check tests 8,836 integer comparisons. There is no floating-point inference.

Writing K_nm=binom(n+m,n)/2^(n+m+1), J_nm=(n+m+1)K_nm/2, the exact moments are

mu(p,z)=sum_n(s_n(p)+s_n(z))-sum_nm K_nm s_n(p)s_m(z),

E[Y(p,z)^2]/2=sum_n(n+1)(s_n(p)+s_n(z))-sum_nm J_nm s_n(p)s_m(z).

Differentiate these finite sums exactly to obtain Delta_mu', Delta_W'. The companion certificate evaluates all expressions as Python Fraction, checks the signs, exact q0 and q0' brackets, and confirms the equality defining partial_z D. Thus the theorem covers a local OPEN NEIGHBORHOOD via the implicit function theorem, whose existence is established but no explicit radius is certified.

The local author's earlier script on the same frozen recurrence reported: at b, Delta_mu*1e8 floor=789752024, Delta_W*1e8 floor=44000296, Delta_mu'*1e8 floor=12845959424, Delta_W'*1e8 floor=-168056589514, q0*1e8 floor=1794878866 and q0'*1e8 floor=6884631251314. These are exact rational floors, not approximate-sign evidence. A standalone source verifier accompanies this note.

## Reusable lemma and next

For a continuous family D(q,z)=q(q A(z)-B(z)), if A(b)>0, q0=B(b)/A(b), and q0'(b)>0, then D_z(q0,b)=-q0 A(b)q0'(b)<0 and an increasing simple crossing branch exists locally. Apply this to the BRC diagonal-edge sign frontier as a regression certificate for two-dimensional Bernstein box pruning.

Next unresolved step: establish an *explicit rational interval* around b on which Delta_W>0 and q0'>0, preferably with signed Bernstein or interval rational derivatives. Then establish or refute global uniqueness of diagonal-edge crossings on (13/250,27/500). This result alone does not settle the full two-parameter maximum, for which PREFIX-675 gives the complete p=0 boundary benchmark.

Provenance: verified project control/source at main@4f13bd606e89c465060780e49ab4c02f19f621fe on 2026-11-10; all scientific inputs are frozen at the pin above. Reference algorithm PREFIX-676; no theorem admission implied by repository persistence.
