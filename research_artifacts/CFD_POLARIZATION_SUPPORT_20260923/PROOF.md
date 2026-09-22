# A polarization-aware obstruction and the complete real two-mode criterion

Researcher-ID: EM-DIRECT-3AD825 / TASK_RESEARCH
Scope: direct-user mathematical support to RS-CFD-SPECTRAL-HYBRID-20260910.
No parent CLAIM, formal Driver Acceptance or native benchmark is asserted.

## Source and exact contract

The source adapter is
`research_artifacts/CFD_SPECTRAL_HYBRID_292BCE_20260917/static_carrier_native_adapter.py`
from Source snapshot 85e7 (the copied file and actual SHA are in certificate.json).
Its original pure integer closure AST is reused unchanged. The existing
`research_notes/CFD-B1F673/prior_chat_bundle_20260910/RAW_VORTEX_INTERFACE.md`
already distinguishes raw Vortex R from its Leray projection and the scalar
sigma. The raw-gradient identity and one-mode shear are not new results here.

The actual newer R23 was read at branch
`research/cfd-frontier-b7e2c1-20260922-r23`, head
1b47d2cf8ec96868cf49722617e9f90ae7464a9c, material parent
51ee293c8537b86e5e922f9f379f9d0d2ab7b981, return
`research_returns/RS-CFD-SPECTRAL-HYBRID-20260910_B7E2C1_20260922_R23.md`
(blob 1e3fef6483ea55f4b745fc82f313b2cc266e4cd1).
It concerns deterministic cost bounds with measurement error, not this
polarization criterion. Neither R19 nor R23 supplies the still-required
matched native 32^3 Taylor-Green benchmark. No benchmark is run here.

Work on an auxiliary periodic three-dimensional Fourier model with convention
exp(i k dot x). This is the declared external CFD model, not a redefinition of
Heartbeat World or its native six spatial axes. P000 remains unconditional.
The raw API value is R=Fourier(u cross curl u). At a nonzero mode m retain
both P_m R_m and sigma_m=(m dot R_m)/|m|^2; the latter is the interface scalar,
not an unqualified physical-pressure convention. For an ordered pair p+q=m,
the raw contribution is

    i [q (u_p dot u_q) - (q dot u_p) u_q].

The dot product is bilinear; no absolute-value substitution, positive mass
replacement or pruning is allowed. Ordered pairs are all counted, including
self-pairs once. Real fields have conjugate negative-frequency partners.

## Same support and energies, different nonlinear output

Let u=e3(cos x+cos y), v=e2 cos x+e3 cos y. Both are divergence-free with
identical signed support {+e1,-e1,+e2,-e2} and energy 1/4 per Fourier mode.
Enumerating all 16 ordered pairs exactly gives eight raw output modes in
either case. For u all projected coefficients vanish, but all eight raw
sigma values are nonzero. For v the projected support is the four modes
(+/-1,+/-1,0). At m=(1,1,0):

    R_u = i(1,1,0)/4, sigma_u=i/4, P_m R_u=0;
    R_v = -i e3/4,      sigma_v=0,   P_m R_v=-i e3/4.

Thus signed support and per-mode energy do not determine the next projected
output. A finite observer retaining only those data cannot certify the exact
polarization cancellation. The raw API still needs its gradient information.

Within the n=32 box [-15,15]^3, the least negation/addition carrier containing
the four seed labels is [-15,15]^2 x {0}, of size 961: each point is reachable
by axis steps inside the box, and this plane grid is itself closed under every
retained sum. The existing integer closure function returns FALLBACK_DENSE at
limits 128 and 384, with exact lower bounds 129 and 385. This is a conservative
route, not a correctness defect or a measured performance claim.

## Universal real two-mode theorem

Let k,l be noncollinear nonzero integer vectors and a,b real vectors satisfying
a dot k=b dot l=0. Put u(x)=a cos(k dot x)+b cos(l dot x). Assume no aliasing
and that BOTH cross frequencies k+l and k-l are retained. The projected
quadratic nonlinearity vanishes identically if and only if, with
alpha=a dot l, beta=b dot k and n=k cross l,

    (|k|^2-|l|^2) alpha beta = 0,
    alpha (b dot n) = 0,
    beta  (a dot n) = 0.                         (1)

Self-mode raw terms are gradients; opposite self-pairs cancel at zero. The
remaining projected coefficients at k+l and k-l are respectively

    -i P_(k+l)(alpha b+beta a)/4,
     i P_(k-l)(alpha b-beta a)/4.                (2)

To prove equivalence, write U=|k|^2, V=|l|^2, s=k dot l and Delta=UV-s^2>0.
The components in span(k,l) are

    a_parallel=alpha(U l-s k)/Delta,
    b_parallel=beta(V k-s l)/Delta.

The plane component of alpha b+beta a is
alpha beta[(V-s)k+(U-s)l]/Delta. Because k,l are independent, it is parallel
to k+l exactly when (U-V)alpha beta=0. The difference is
alpha beta[(V+s)k-(U+s)l]/Delta and is parallel to k-l under the same condition.
The two independent normal conditions are
alpha(b dot n)+beta(a dot n)=0 and
alpha(b dot n)-beta(a dot n)=0. Over the reals they are exactly the last two
conditions in (1). This proves both directions, including zero amplitudes.

For nonzero a,b the classification is especially simple. If alpha=0 then a
is normal to the k,l plane, so a dot n is nonzero and (1) forces beta=0;
the same holds interchanging the modes. Thus either both are normal, or
alpha beta is nonzero. In the latter case (1) forces both amplitudes into
span(k,l) and U=V. Conversely either family satisfies (1). Therefore unequal
lengths allow only common normal polarization; equal lengths additionally
allow both in-plane polarizations. If one amplitude is zero, the remaining
single mode always has zero projected quadratic nonlinearity.

For k=e1,l=e2, a=(0,A,B), b=(C,0,D), (2) reduces to
-i(AD+BC)e3/4 and i(AD-BC)e3/4. The exact condition is BC=AD=0.
The general theorem has thus already resolved the unequal-length real case;
it is not left as an artificial next task.

If just one cross frequency is retained, only its corresponding equation
in (2) is required; (1) must not be applied as a necessary condition. If
neither is retained, every such two-mode field has zero retained projected
nonlinearity. Aliasing, forcing and generic complex amplitudes need separate
contracts. Diagonal viscosity preserves common-normal fields; equal-length
in-plane modes also decay by a common multiplier. These algebraic statements
do not certify an arbitrary native callback, implementation roundoff or cost.

## Actual evidence and complete complex extension

check_polarization.py records the full two 16-pair calculations and two calls
to the unchanged source closure. check_real_family.py checks (1) against the
ordered-pair calculation for 180 nonorthogonal/equal/unequal-length and zero
cases plus all 81 choices A,B,C,D in {-1,0,1}. All comparisons use integers
and explicit unevaluated denominators. No quotient, remainder or root is
materialized; no Fraction or floating oracle replaces native BRC state.
The universal conclusion follows from the proof, not the finite sample.

The same short calculation ALSO completes the classification for complex amplitudes
A at k, B at l, conjugates at -k,-l, with k dot A=l dot B=0. With both cross
frequencies retained and no aliasing, begin from the necessary and sufficient
projected equations

    P_(k+l)[(A dot l)B+(B dot k)A]=0,
    P_(k-l)[(A dot l)conj(B)-(conj(B) dot k)A]=0.

Write alpha=A dot l, beta=B dot k, A_n=A dot n, B_n=B dot n. Plane components
give (U-V)alpha beta=0 and (U-V)alpha conj(beta)=0. Normal components give
alpha B_n+beta A_n=0 and alpha conj(B_n)-conj(beta) A_n=0. If A,B are nonzero,
alpha=0 forces beta=0 and conversely, because a nonzero amplitude with zero
in-plane component has nonzero normal coefficient. This gives the family of
two arbitrary complex normal amplitudes. Otherwise alpha beta is nonzero,
U=V and division of the two normal equations gives

    r=A_n/alpha, s=B_n/beta, s=-r, conj(s)=r.

Thus r is purely imaginary. All remaining fields have, for arbitrary nonzero
complex alpha,beta and a real parameter tau,

    A = alpha [U l-s0 k+i tau n]/Delta,
    B = beta  [U k-s0 l-i tau n]/Delta,
    s0=k dot l, Delta=U^2-s0^2>0.               (3)

Conversely (3) satisfies both projected equations, so this list is complete.
Zero amplitudes give arbitrary remaining single-mode polarization, as before.
When U differs from V only the normal or single-mode families remain. The
real-amplitude result is recovered by tau=0 in the mixed in-plane family;
arbitrary spatial phases are already contained in complex alpha,beta. This
extension is a direct algebraic corollary, not a presumed answer from the real
case or a new unverified task. Rational complex inputs admit rational tau in
this parameterization. Noncollinearity and full retention remain essential.

The concrete remaining support work is a portable certificate consumer for this
COMPLETE classification. It must bind exact k,l,A,B, validate the declared
carrier and retention scope, compute raw R and sigma as well as projection,
and reject tampered data. Merely restating the equations or checking only
projected zero is insufficient. Native benchmark performance remains open;
a correct algebraic certificate alone does not establish acceleration.

No global novelty, Foundation promotion, new native dimension, formal Driver
Acceptance or CFD speedup is claimed. Root independently checked the real
algebra in a separate process; its acceptance status remains ordinary local
scientific review, not a parent Task terminal event.

Global-Knowledge-Sync: main@6f6fa5c / GLOBAL_KNOWLEDGE_V1
