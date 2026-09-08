# OpenAI NS comparison, audit 1: smooth forcing and the positive heat-Gram budget

Record-ID: FINDING-EM-NS-OPENAI-FORCING-AUDIT-20260909-D5C00D
Progress-Event-ID: NS-OPENAI-FORCING-AUDIT-20260909-D5C00D-01
Status: TESTING / ORDINARY_DERIVATION / FINITE_FOURIER_CONSISTENCY_CHECKED
Not independently reviewed. Not a Lean kernel verification or a proof of arbitrary-data NS regularity.
Researcher-ID: EM-DIRECT-D5C00D
Research-Activity-ID: RA-D5C00DF7D77F4AA2ACE0
Session: local-chat-ns-openai-audit-d5c00df7d77f4aa2ace0 (locally assigned, not a platform-authenticated identifier).
P000 unchanged. All PDE calculations concern the classical effective 3D model; no native X6 dynamics or ontological identification is asserted.

## 1. Exact source alignment

Global snapshot: awdawmip/chatgpt-global-knowledge@3ad395d666b488e89f4e1cef56ec8fbdf9732a18.
Own latest frontier: awdawmip/enterprise-math@f797247d78e24ee8451c3df1f10e8b71f67958ff:research_notes/ns-viscous-jitter-budget-20260909.md.
Parent heat-Gram: global knowledge/projects/enterprise-math/pde-brc-latent-jitter-gram-lyapunov-20260908.md at the global snapshot.

OpenAI snapshot: openai/NavierStokesAndEuler@8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538.
Read:
- formalization.yaml: full; C/D are forced NS, separate Euler results are unforced; review self-assessed.
- NavierStokes/CandidateAssembly.lean: lines 1-200; this module is conditional outer assembly, not a standalone existence proof.
- NavierStokes/R3ActualCandidate.lean: full; selected_compact_candidate uses ActualCandidateAssembly.selected_witness.
- NavierStokes/R3CompactCandidate.lean: lines 1-230; Properties includes smooth future force, fixed compact spatial support, compact future time support, zero initial velocity, exact residual equality and unbounded endpoint speed.
- NavierStokes/ActualCandidateAssembly.lean: lines 1-180; only initialization/support was inspected.
- NavierStokes/ComparatorR3Theorem.lean: full; general positive viscosity and option C bridge.

Previous conversational comparison relied too heavily on external Bingham R3C/MORP/DCRP terminology. That is not a substitute for the current EM source frontier F=J+nu^2*K/4. No quantitative q4/carrier equivalence has been established.

No whole repository build, Comparator execution, full proof review, or quantitative evaluation of the OpenAI infinite candidate was performed. Correctness of that candidate is conditional throughout its application below.

## 2. Scaling correction

For a classical forced NS solution near (x*,T), use

u_r(y,s)=r*u(x*+r*y,T+r^2*s),
p_r(y,s)=r^2*p(x*+r*y,T+r^2*s),
f_r(y,s)=r^3*f(x*+r*y,T+r^2*s).

Viscosity is unchanged. Every fixed mixed derivative satisfies

d_y^alpha d_s^m f_r
= r^(3+|alpha|+2m)*(d_x^alpha d_t^m f)(x*+r*y,T+r^2*s).

A force smooth across (x*,T) therefore tends to zero in C^k on each fixed compact rescaled cylinder. For the fixed-compact-support smooth forcing in R3CompactCandidate.Properties, its Leray projection g=P f also satisfies

||g_r(s)||_(Hdot^1/2)=r^2*||g(T+r^2*s)||_(Hdot^1/2).

This is automatic, not a special success of a carrier construction. It does not imply convergence of u_r to a nontrivial smooth ancient solution, preservation of singularity in a limit, or a singular unforced trajectory. Ratios to a possibly vanishing signed nonlinear flux are not justified by these absolute estimates.

## 3. Forced extension of the exact EM balance

Work first on R3 with a smooth finite-Sobolev solution on every shorter interval [0,t], t<T. Assume f is smooth across T with uniformly compact spatial support. Thus g=P f has bounded H^m norms on compact time intervals. The corresponding mean-zero torus calculation is identical; nonzero torus mean requires a separate mean ledger.

Let Lambda=(-Delta)^(1/2), S(tau)=exp(-tau*Lambda^2), u_s=P_s u, and N(u)=P(u cross curl u). Define

C(v)=-v cross Lambda v,
A=sum_s ||C(u_s)||_(Hdot^-1/2)^2,
J=sum_s integral_0^infinity ||C(S(tau)u_s)||_(Hdot^-1/2)^2 dtau,
K=||Lambda^(1/2)u||_2^2, Q=||Lambda^(3/2)u||_2^2,
F=J+(nu^2/4)*K.

The projected equation is u_t=-nu*Lambda^2*u+N(u)+g. Hence exactly

J'+nu*A=I_NL+I_f,
I_NL=sum_s D J_s(u_s)[P_s N(u)],
I_f=sum_s D J_s(u_s)[P_s g].

The critical energy identity is

K'/2+nu*Q=Pcrit+<Lambda u,g>,

Pcrit=2<Lambda u_+,C(u_-)>-2<Lambda u_-,C(u_+)>.

Duality and Young give |Pcrit|<=2*sqrt(Q*A)<=nu*Q/2+2*A/nu. Therefore

F'+nu^3*Q/4 <= I_NL+I_f+(nu^2/2)*<Lambda u,g>.       (F1)

In particular omitting either forcing term is an error.

## 4. A global bound on the direct forcing terms

Here is an ordinary proof, not a finite-frequency extrapolation. Sobolev product estimates give

||v cross Lambda v||_(Hdot^-1/2)
<= C_* ||v||_(Hdot^1/2)*||v||_(Hdot^3/2).

For H(tau)=||S(tau)v||_(Hdot^1/2)^2, H'=-2D. Integrating H*D yields

J_s(v)<=C_*^2*||v||_(Hdot^1/2)^4/4.

Put Phi(v)(tau)=Lambda^-1/2 C(S(tau)v), valued in the Hilbert space L^2_tau L^2_x. It is quadratic and ||Phi(v)||<=C_*/2*||v||^2. Polarization plus the Hilbert parallelogram identity, optimized by replacing (v,w) with (a v,a^-1 w), proves

||D Phi(v)[w]||<=C_*||v||*||w||.

The construction preserves signed complex amplitudes, helicity, output and input heat rates until the complete Gram is formed. Positivity is never imposed on individual off-diagonal Gram entries.

Consequently

|I_f| <= 2*C_* sqrt(J*K)*||g||_(Hdot^1/2)
      <= (2*C_*/nu)*F*||g||_(Hdot^1/2),                (F2)

because nu*sqrt(J*K)<=J+nu^2*K/4=F. Also

|(nu^2/2)<Lambda u,g>|
<=nu*sqrt(F)*||g||_(Hdot^1/2).                        (F3)

Fix any positive reference F_* with the units of F, and set G=F_*+F. Since sqrt(F)<=G/(2sqrt(F_*)), equations F1-F3 imply

G'+nu^3*Q/4 <= (I_NL)_+ + b(t)*G,                    (F4)

b(t)=[2*C_*/nu+nu/(2sqrt(F_*))]*||g(t)||_(Hdot^1/2).

For our force class, integral_0^T b(t)dt is finite. The proof controls DIRECT normalized forcing injection; it does not claim that the absolute injected energy, or the force's influence on the entire trajectory, is zero.

The offset matters for rest-started flows: F(0)=0. On a mean-zero torus the exact smooth flow u=t*e2*sin(x1), with force (1+nu*t)*e2*sin(x1), has N=J=0 but F'/F=2/t for t>0. The logarithmic rate at such a smooth birth is not a singularity diagnostic. G avoids division by zero.

## 5. Forced continuation criterion and candidate obligation

Define Gamma_NL=(I_NL)_+/G. If

integral_0^T Gamma_NL(t)dt < infinity,                 (F5)

then with B=int_0^T (Gamma_NL+b),

G(t)+(nu^3/4)*integral_0^t Q(s)ds <= G(0)*exp(B).

Proof: apply the integrating factor for the nonnegative coefficient Gamma_NL+b in F4. This bounds K and the time integral of Q. Interpolation gives

||u||_6^4<=C*||u||_(Hdot^1)^4<=C*K*Q,

so u belongs to L^4_t L^6_x up to T. The usual nonendpoint strong continuation argument applies. More explicitly, testing NS at H^1 level yields

Y'+nu*||Delta u||_2^2
<=C*nu^-3*||u||_6^4*Y+C*nu^-1*||g||_2^2,

where Y=||grad u||_2^2. Gronwall bounds Y, and local strong existence at this subcritical norm extends the solution. Smooth f supplies the required finite force norm and smoothness. No endpoint critical compactness theorem is used.

Thus any actual finite-time singularity in this class MUST satisfy

integral_0^T (I_NL)_+/(F_*+J+nu^2*K/4) dt=infinity.    (F6)

Application: IF the OpenAI compact candidate has its stated mathematical properties, it must satisfy F6. This is a rigorous conditional audit obligation, not a direct calculation of its injection integral. Its smooth direct force cannot be the nonintegrable coefficient in F4.

The criterion is sufficient, not necessary for smoothness. A divergent Gamma_NL alone never proves blowup. No arbitrary-data bound for F5 has been proved.

## 6. Research consequence and exact remaining frontier

A proof of a globally integrable upper bound on Gamma_NL that automatically remains valid for every smooth compactly forced flow would contradict a correct OpenAI candidate. An unforced-only route must exhibit the precise global/dynamical restriction using g=0, not rely on g_r -> 0 or on a static 120-degree analogy. This conditional incompatibility does not establish that such an unforced proof is impossible.

A finite isolated viscous triad does not provide that restriction: its closed pump energy estimate is lost under inter-triad transfers. Independent finite gains need a common full-network metric and coherent cross-channel bounds.

Next unresolved unit: translate the actual candidate potential/direct/pressure sums into sector heat-rate packets and decompose I_NL into same/mixed-helicity, same/different-shell and cross-cycle terms with uniform tail control. No gate has been declared passed for q4 membership, temporal genealogy or a five-power barrier. No earlier external R3C theorem was imported as an EM theorem.

REUSE_APPLIED: phase-resolved helical radial commutator, exact heat Gram, zero-safe combined F energy.
COMPOSE_APPLIED: Hilbert-valued quadratic polarization with the projected forcing direction.
No new Foundation promotion, formal task claim, or independent review.

## 7. Executed finite checks

Implementation: experiments/ns_openai_forcing_audit_d5c00d.py, initially published at c0f12c15b19fe0b3d872ed2b0b64c989ba9ac34b.
12 random real divergence-free finite Fourier states, RNG seed 20260909, viscosities 0.2/1/3; all generated nonlinear output frequencies retained.
Checked heat balance, exact helical critical identity, forced Frechet chain rule, combined F inequality, and a directional finite difference.

Maximum normalized errors:
- heat balance: 1.1060375036309948e-16
- critical identity: 2.5242618801594815e-16
- forced chain rule: 1.7425650728800089e-16
- combined inequality positive violation: 0
- directional finite difference: 1.0179700407137233e-11

These are floating-point consistency checks, NOT interval arithmetic certificates, a full PDE trajectory, an OpenAI candidate simulation, or Lean validation.

Code SHA256: bb84ce19bdc9dd16e1dfefd29e8f3531ff958a3563af0fba88f2b52c23712e4a.
Result JSON SHA256: 7d747e1c9c81fbcb5e86fbeaecce601a217313b30f55383e352af33ea04f7c30.
