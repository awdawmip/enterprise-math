# OpenAI NS comparison, audit 3: flat singular-point force and residual-to-nonlinearity transmutation

Record-ID: FINDING-EM-NS-OPENAI-FLAT-FORCE-20260909-D5C00D
Progress-Event-ID: NS-OPENAI-FLAT-FORCE-20260909-D5C00D-03
Status: TESTING / SOURCE_FORENSIC / ORDINARY_DERIVATION / NOT_INDEPENDENTLY_REVIEWED
Researcher-ID: EM-DIRECT-D5C00D
Research-Activity-ID: RA-D5C00DF7D77F4AA2ACE0
Session: local-chat-ns-openai-audit-d5c00df7d77f4aa2ace0 (locally assigned, not a platform-authenticated identifier).
P000 unchanged. This is not a Lean kernel extension, formal task claim, Working Truth promotion, or independent acceptance of the OpenAI proposal.

## 1. Frozen sources

Own parents:
- `research_notes/ns-openai-forcing-audit-20260909-d5c00d.md`.
- `research_notes/ns-openai-axis-germ-leray-audit-20260909-d5c00d.md`.

OpenAI source remains frozen at
`openai/NavierStokesAndEuler@8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538`.

Audit 2 established the source-forensic separation:

`singular slow base core` != `annular residual-repair carrier`.

It also derived, as an ordinary source-based proof, the critical lower bound

`K(t)=||u(t)||_(Hdot^1/2)^2 >= c*(1-t)^(-8h/3)`,

with `0<h<=1/1000`, and hence the normalized nonlinear gates

`integral Gamma_NL >= (8h/3) log(1/(1-t)) - C`,

and

`integral (Pcrit)_+/K >= (4h/3) log(1/(1-t)) - C`.

## 2. The final force is flat at the singular spacetime point

The actual selected schedule in `MixedCandidateWitness.SelectedSchedule` includes

`JointResidualLimits.VanishingJointJets(originalResidual)`.

By definition, this is the strong joint statement

`D^n residual(z) -> 0`

for every full spacetime derivative order `n` as
`z -> (1,0)` from the physical open past.

The mixed periodic boundary-limit constructor then proves

`MixedPeriodicAssembly.boundaryLimits ... 0 n = 0`

for every `n`. The final witness records the exact boundary jets

`D^n forcing(1,x) = boundaryLimits(...,x,n)`.

Consequently, for the actual selected candidate,

`D^n forcing(1,0)=0` for every full spacetime order `n`.             (A3.1)

This is stronger than merely saying the force is smooth near the singularity.
It is **flat at the singular spacetime point**. It does not imply that the force
vanishes on a neighborhood or on the entire terminal slice. In fact the formal
candidate consequences separately prove that the force is nonzero at some
spacetime point with `0<t<1`.

`CandidateFromLimits.force_eq_activated_residual` also proves that for every
`0<=t<1` the final force is exactly the activated Navier--Stokes residual of the
constructed fields; it is not an independently prescribed forcing profile.
The global smooth extension is made from the actual residual boundary jets.

## 3. Super-algebraic disappearance under singular rescaling

Let the singular point be `(T,x*)=(1,0)` and use the Navier--Stokes parabolic
rescaling

`f_r(y,s)=r^3 f(x*+r y, T+r^2 s)`.

For any spatial multi-index `alpha`, time derivative order `m`, and arbitrary
integer `M>=0`, flatness (A3.1) plus Taylor's theorem gives, on every fixed
compact rescaled cylinder,

`|d_y^alpha d_s^m f_r(y,s)|
 <= C(alpha,m,M,R) * r^(3+|alpha|+2m+M)`.             (A3.2)

Thus the actual forcing disappears at the singular point faster than any fixed
power beyond the canonical scaling factor, in every fixed derivative order.

Audit 1 only used ordinary smoothness to get `f_r -> 0`. The actual witness is
strictly stronger: its singular-point forcing jet is identically zero to all
orders.

Research consequence: any obstruction that depends only on a bounded number of
local jets after blowup rescaling, or on estimates stable under
super-algebraically small local errors, cannot use the *size* of the local force
to distinguish this forced construction from an unforced one. An exact identity
using `f=0` may still distinguish them. The forced/unforced separation must
therefore be sought in exact/global/nonlocal dynamics rather than a finite local
force-jet budget.

## 4. Exact residual-to-nonlinearity transmutation identity

Use the projected convention from audit 1:

`u_t = -nu Lambda^2 u + N(u) + g`,

where `N(u)=P(u cross curl u)` and `g=P f`.

Split the prelocalized final field as

`u=b+w`,

where `b` is the singular slow-base branch and `w` contains initialization plus
positive correction branches. Define the projected base residual debt

`r_b = b_t + nu Lambda^2 b - N(b)`.

Subtract the base equation from the final equation. Exactly,

`N(b+w)-N(b)
 = r_b + w_t + nu Lambda^2 w - g`.                    (A3.3)

This identity is algebraic; no sign assumption is used.

It captures the role of the OpenAI correction machine more accurately than the
phrase "the carrier causes blowup":

- `b` already carries the singular axis germ;
- `r_b` is the debt of that planted singular base;
- `w` lives primarily in the off-axis residual-repair machinery and does not
  alter the singular germ locally;
- the cross/self nonlinearities involving `w`, together with its linear
  evolution, transmute the base residual debt into the final globally smooth
  force `g`.

Because `g` is flat at the singular point but nonzero somewhere globally, this
transmutation is intrinsically global/nonlocal.

For the unforced problem the exact target would be the stronger closure

`N(b+w)-N(b) = r_b + w_t + nu Lambda^2 w`.             (A3.4)

So the mathematically meaningful forced/unforced question is not whether the
local singular core notices `g`; by (A3.1)--(A3.2) it does not at finite jet
order. The question is whether the entire correction network can close (A3.4)
**exactly with zero global remainder** while retaining the singular base and all
regularity/support constraints.

## 5. Lower-complexity BRC ledger for the cubic critical gate

Before expanding the 24 ordered quintic heat-Gram terms, use the cubic gate from
audit 2.

Write the exact critical transfer as a trilinear helical form

`Pcrit = T(u,u,u)`

where the two outer helicity signs and the cross-helicity commutator signs are
retained inside `T` rather than taking absolute values termwise.

With `u=b+w`, typed provenance gives exactly the eight ordered words

`bbb, bbw, bwb, bww, wbb, wbw, wwb, www`.             (A3.5)

Only after this provenance split should each word be refined by

- outer helicity sign `+/-`;
- shell/band pair;
- correction cycle/generation;
- Leray/pressure provenance where present.

The audit-2 necessary condition says their coherent signed sum must supply

`integral_[t0,t] (Pcrit)_+/K ds
 >= (4h/3) log(1/(1-t)) - C`.                          (A3.6)

Equivalently,

`limsup_(t->1-) (1-t)*(Pcrit)_+/K >= 4h/3`.            (A3.7)

No individual word in (A3.5) has yet been proved positive or divergent. The BRC
rule here is precisely not to infer that from the positivity of the total
positive part.

## 6. What this changes in our route

The OpenAI construction is now a sharper adversarial test than a generic forced
counterexample:

1. its singularity is planted in a base branch;
2. its correction carrier is geometrically separated from the singular core;
3. every force jet at the singular spacetime point is zero;
4. nevertheless the global force is genuinely nonzero;
5. the full nonlinear dynamics must pay a logarithmically divergent critical
   transfer exposure.

Therefore a viable unforced proof route should not aim merely to show
"a local carrier cannot amplify indefinitely". It should target a full-network
exact closure obstruction, for example:

> under `g=0`, can the eight provenance sectors in (A3.5), refined by actual
> shells/cycles and kept phase-coherent, simultaneously (i) pay the positive
> logarithmic critical-transfer exposure (A3.6) and (ii) close the residual
> transmutation identity (A3.4) with no global remainder?

The isolated viscous triad gain bound remains useful as a local input, but by
itself it cannot answer this overlapping-network closure question.

## 7. Next executable unit

Construct the eight-word cubic `Pcrit` ledger before the 24-term quintic ledger.
For each word, retain actual helical signs and shell/cycle provenance and test:

- whether the pure base word `bbb` alone has enough positive normalized
  exposure to account for (A3.6);
- if not, which mixed `b/w` branches are forced to contribute;
- whether the same branches are exactly those needed by (A3.3) to repair the
  annular base residual;
- finally, which part of that mechanism irreducibly uses the nonzero global
  remainder `g` and therefore fails when `g=0`.

No branchwise sign conclusion is asserted at this checkpoint.

REUSE_APPLIED: audit-1 forced heat-Gram balance; audit-2 critical transfer gate;
OpenAI selected-schedule joint residual flatness; mixed periodic boundary-limit
zero at the singular point; BRC typed provenance.
COMPOSE_APPLIED: flat-jet Taylor rescaling + projected residual subtraction +
eight-word cubic provenance ledger.
