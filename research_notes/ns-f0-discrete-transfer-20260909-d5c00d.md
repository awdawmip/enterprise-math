# A finite-resolution autonomous transfer certificate and a discrete residual Gram

Record-ID: FINDING-EM-NS-F0-DISCRETE-TRANSFER-20260909-D5C00D
Progress-Event-ID: NS-F0-DISCRETE-TRANSFER-20260909-D5C00D-06
Status: TESTING / FINITE_ALGEBRA_PROOFS_AND_EXACT_RATIONAL_CHECKS
Researcher-ID: EM-DIRECT-D5C00D
Research-Activity-ID: RA-D5C00DF7D77F4AA2ACE0
Session: local-chat-ns-openai-audit-d5c00df7d77f4aa2ace0 (local continuation key, not a platform-authenticated ID).
No independent review, Lean verification, Foundation promotion, or full NS theorem is claimed. P000 is unchanged.

## 0. Exact scope, concurrent work, and sources

The user requested parallel continuation of the "AS" proof. No separate AS definition was recovered in the bounded context/source search. This note provisionally follows the conversation's existing NS / f=0 line; it does not create a new theorem named AS or take ownership of another conversation's task.

Own read snapshot: awdawmip/enterprise-math@8f660a596d43b68b7fad43a302888feb43bf3ef2.
Global read snapshot: awdawmip/chatgpt-global-knowledge@3fe4f902772b2da5ef6dcb68b469932c4fd72d5f.
The other observed NS frontier is `research_notes/ns-jitter-initial-data-certificate-20260909.md` and its verification JSON: an initial-data full-feedback sufficient regularity certificate. That work is consumed, not reissued, and its author/activity remain EM-DIRECT-F00A51 / RA-076944AE1950A916ACC95399. Its live conversational execution state is not inferred from a stored note.

This complementary unit studies a fixed finite carrier, a discrete-time rational update, fixed quantization, exact signed phase transfer, and a finite Cauchy-Gram identity. Continuous smoothness is not used to infer a physical conclusion.

Method-level sources, not accepted blow-up inputs:
- OpenAI frozen `8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538:NavierStokes/MixedCandidateWitness.lean`: keep the same witness/schedule through the calculation.
- Same pin, `NavierStokes/ActualIntermediateDebtBounds.lean`: evaluate defects on actual intermediate states instead of supplying the desired bound as a premise.
- EM initial-data note above: preserve output, input damping rate, and complex phase in the complete residual Gram.
- EM `logic_blacklist.json` and current README position: no target-imprinted forcing, no automatic promotion of a continuum model to nature, and no inference of blow-up from instability.

Borrowing these bookkeeping/assembly principles asserts neither their originality nor the correctness of the entire OpenAI construction. The midpoint/Cayley and finite Gram algebra below are standard mathematical mechanisms applied to this explicit carrier; no priority claim is made.

## 1. Freeze the law before selecting the example

Fix integers M>=1 and positive rational viscosity nu, step theta, and resolution delta. The actual grid state is

    X=(b,a_{-M},...,a_M),
    b in delta Z, a_j in delta Z[i].

The underlying exact rational workspace uses Q and Q[i]. Coefficients outside [-M,M] are zero. Define the nonlinear generator once and for all:

    F_b(X)=-nu b,
    F_j(X)=-nu(1+j^2)a_j - (i b/2)(a_{j-1}+a_{j+1}).           (1)

There is no forcing parameter. The coefficient b evolves as part of the same state; it is not a frozen external pump.

As a typed classical-carrier interpretation only, (1) is the spectral Galerkin system for

    u=(Re[e^(iy) sum_j a_j e^(ijz)], b cos z, 0)

in the normalized 2pi-periodic, streamwise-independent, incompressible NS class. The third velocity component is zero and all x derivatives vanish. The nonlinear x component is b cos z times the y derivative of the first component; the pressure gradient can be zero. This is a restricted two-spatial-variable carrier, not general rank-three NS and not native six-dimensional dynamics. The algebraic law (1), rather than an assumption about nature, is the premise of this note.

The unrounded update is implicit midpoint:

    Xhat^+ - X^- = theta F(Xbar),
    Xbar=(Xhat^+ + X^-)/2.                                   (2)

It is an explicit, uniquely computable forward rule. First

    beta=b^-/(1+theta nu/2).

Then solve

    [I+(theta/2)(nu D+i beta C/2)] abar = a^-,
    D_jj=1+j^2, C_{j,j+1}=C_{j+1,j}=1,                       (3)

and set ahat^+=2 abar-a^-, bhat^+=2 beta-b^-.

The Hermitian real part of the matrix in (3) is I+(theta nu/2)D, positive definite. Equivalently, exact tridiagonal elimination has real pivots

    p_0=d_0>0, p_j=d_j+(theta beta/4)^2/p_{j-1}>0.

Thus the rule is unique for every positive step; rational inputs produce Gaussian-rational outputs. No local-existence or small-step smoothness argument is used.

Finally, round each real/imaginary component toward zero to the fixed grid delta:

    X^+ = Q_delta(Xhat^+).                                   (4)

This rounding is part of the declared finite-resolution law, not an unreported force. Its defect and energy loss are recorded separately. This selected law is not claimed to be nature's native update law.

## 2. Exact dissipation, including all retained feedback

Define the finite algebraic energy and dissipation

    E(X)=(b^2+sum_j |a_j|^2)/4,
    D_E(X)=(b^2+sum_j (1+j^2)|a_j|^2)/2.

The tridiagonal matrix C is real symmetric, so i b C/2 is skew-Hermitian. Taking the finite inner product in (2), with no differentiation in time, gives

    E(Xhat^+)-E(X^-) = -theta nu D_E(Xbar).                    (5)

Rounding toward zero decreases each component's squared magnitude, hence

    E(X^+) <= E(Xhat^+) < E(X^-)   for X^- != 0.               (6)

The strict inequality follows because Xbar=0 in (2) would force X^-=0. Therefore every finite-grid orbit reaches zero after at most

    4 E(X_0)/delta^2

nonzero steps: grid energies are multiples of delta^2/4, and each nonzero step decreases that integer. This is a theorem of the chosen dissipative quantized model, not a physical finite-time extinction claim. In particular this model cannot furnish an unlimited-growth or blow-up counterexample.

## 3. Yet a high-frequency-weighted quantity grows exactly

Define the readout

    K(X)=(b^2+sum_j sqrt(1+j^2)|a_j|^2)/2.                    (7)

In the stated classical interpretation, this is the squared homogeneous H^(1/2) norm. Here it is a finite algebraic readout, with square roots represented symbolically and signs certified by rational inequalities, not by infinitely precise decimal data.

Set lambda_j=sqrt(1+j^2). Direct finite expansion of (2) gives

    K(Xhat^+)-K(X^-)
      =theta [T(Xbar)-nu D_K(Xbar)],                         (8)

    T(X)=(b/2) sum_{j=-M}^{M-1}
          (lambda_j-lambda_{j+1}) Im(conj(a_j)a_{j+1}),

    D_K(X)=b^2+sum_j (1+j^2)^(3/2)|a_j|^2.

This is the actual signed nearest-shell transfer, not a positive-mass estimate.

For the midpoint family

    b=B, a_0=A, a_{-1}=a_1=-i C/2, a_j=0 otherwise,

(8) becomes

    Delta K=theta [(sqrt(2)-1)ABC/2
                    -nu(A^2+B^2+sqrt(2)C^2)].               (9)

The same step has

    Delta E=-(theta nu/2)(A^2+B^2+C^2).

Thus energy dissipation does not force this weighted readout to decrease. This conclusion concerns a particular observable; it is not Lyapunov instability or finite-time blow-up.

### Exact fixed-grid witness

Take M>=2, nu=1, theta=1/64, delta=1/4, A=B=C=32. The *initial* state supplied to the forward algorithm (3)-(4) is

    b^-=129/4,
    a_0^-=145/4,
    a_{-1}^-=a_1^-=-49i/4,
    a_{-2}^-=a_2^-=2,

with all other coefficients zero. The uniquely calculated next state is

    b^+=127/4,
    a_0^+=111/4,
    a_{-1}^+=a_1^+=-79i/4,
    a_{-2}^+=a_2^+=-2.

Both states already lie on the quarter grid: rounding changes neither. All nonlinear outputs of the midpoint lie within |j|<=2, so this first step has no omitted-mode defect and works unchanged in every larger M.

Exactly,

    E^- =10649/16, E^+=10265/16,
    Delta E=-24,
    Delta K=240 sqrt(2)-288 > 48.                            (10)

The positive margin uses only sqrt(2)>7/5, proved by 2>49/25. No floating-point sign decision is involved. Choosing a midpoint was a way of discovering an initial datum; the final certificate reruns the fixed, unique forward update from that datum. No residual/force is subsequently defined to make it pass.

## 4. BRC obstruction: modal energy alone is not a sufficient observer

Even recording every individual modal energy, rather than just total energy, loses information needed to predict the next weighted readout.

Under the same fixed parameters and M=2, compare *initial* states

    X_P: b=32, a_0=32, a_{-1}=a_1=-16i,
    X_N: b=32, a_0=32, a_{-1}=a_1=+16i.

They have identical b, identical |a_j|^2 for every j, identical E, and identical K. Apply the same forward rule and quarter-grid rounding. Exact calculation gives

    Delta K_P = -8971/32 +(825/4)sqrt(2)+(289/16)sqrt(5) > 0,
    Delta K_N = 1253/8 -(855/4)sqrt(2)+(25/4)sqrt(5) < 0.       (11)

Simple rational root bounds suffice: for the first expression use sqrt(2)>7/5 and sqrt(5)>11/5; for the second use sqrt(2)>7/5 and sqrt(5)<9/4. Both trajectories lose total energy.

Let O(X)=(b,(|a_j|^2)_j). Equation (11) proves that there is no function F_O with

    K(S(X))=F_O(O(X))

on this state class, where S is the frozen quantized update. The observer fibers are not constant under the next operation. At least signed cross-phase data, such as Im(conj(a_j)a_{j+1}), must be retained or explicitly repaired. This witness does not claim that adjacent phase data alone are sufficient for every future update.

REUSE_APPLIED: BRC observer/fiber-constancy rule, before phase compression.

## 5. A discrete residual Gram without a smoothness argument

The linear part of the same unrounded midpoint rule has rational multipliers

    r_j=(1-theta nu(1+j^2)/2)/(1+theta nu(1+j^2)/2),
    H(b,a)=(r_0 b,(r_j a_j)_j), |r_j|<1.

For each full nonlinear output j, including j=+/- (M+1), retain the two possible input indices k=j-1,j+1 that belong to [-M,M], and put rho_k=r_0 r_k.

Define the finite expression

    J_d(X)=sum_{j=-M-1}^{M+1} b^2/[8 sqrt(1+j^2)]
             sum_{k,l in {j-1,j+1} intersect [-M,M]}
               Re[conj(a_k)a_l]/(1-rho_k rho_l).              (12)

It is a quartic finite algebraic form; its coefficients are explicitly known rational numbers times positive algebraic weights. No infinite series is evaluated.

Each output's two-by-two real kernel C(r,s) is positive semidefinite because its diagonal entries are positive and

    det C(r,s)=(r-s)^2/
       [(1-r^2)(1-s^2)(1-rs)^2] >=0,  |r|,|s|<1.            (13)

This is a finite algebraic proof of J_d>=0. Equal rates give the rank-one kernel and preserve exact coherent cancellation; no off-diagonal positivity is assumed for the amplitude contractions.

Let

    R_d(X)=sum_{j=-M-1}^{M+1}
      |-(i b/2)(a_{j-1}+a_{j+1})|^2/[2 sqrt(1+j^2)].

Multiplication of a pair's amplitudes by rho_k rho_l yields the exact identity

    J_d(HX)=J_d(X)-R_d(X).                                   (14)

For the actual grid update S=Q_delta M_theta, where M_theta is the unrounded nonlinear midpoint map, define separate defects

    I_feedback=J_d(M_theta X)-J_d(HX),
    I_precision=J_d(Q_delta M_theta X)-J_d(M_theta X).

Then

    J_d(SX)-J_d(X)+R_d(X)=I_feedback+I_precision.              (15)

This transfers the useful complete-Gram/damping-budget idea from the existing heat-reference line into a finite discrete algebraic setting. It is not a proof that the right-hand side is nonpositive or summable. In particular, componentwise rounding is dissipative for E and K but must not automatically be called dissipative for a phase-interference quartic Gram. The two quantities have separate ledgers.

There is an exact rounding-only witness to that last warning. Set b=1,
a_{-1}=11/10, a_1=-1/5, and all other a_j=0. Quarter-grid truncation gives
a_{-1}=1,a_1=0. For the same theta,nu, put rho=r_0 r_1. The energy decreases,
but the Gram changes by

    [19/100-1/(4 sqrt(5))]/[8(1-rho^2)] > 0.                 (15a)

This tests the rounding operator on a rational intermediate state; it is not
claimed to be a complete grid-started trajectory. It suffices to refute a
blanket claim that coordinatewise dissipative rounding always dissipates J_d.

EXTEND_EXISTING_TOOL: phase-resolved residual Gram with rational Cayley rates.
COMPOSE_APPLIED: same-witness midpoint balance plus precision/source defect split.

## 6. The missing-mode and precision debts are not hidden

If one compares the finite carrier with its untruncated classical interpretation, the two omitted generator outputs are

    -(i b/2)a_M at j=M+1,
    -(i b/2)a_{-M} at j=-M-1.

Their normalized squared L2 size is

    R_edge^2=b^2(|a_M|^2+|a_{-M}|^2)/8.                      (16)

It is zero at the certified midpoint in (10). It is not generally zero later. The checker records it, rather than relabeling it as a physical force or deleting it. Formula (12) includes these full outputs from the beginning.

The checker also records the energy lost by quantization on the same actual trajectory. Neither increasing M nor removing quantization is an admissible automatic theorem promotion.

## 7. Executed checks, results, and next proof obligation

Implementation: `experiments/ns_f0_discrete_transfer_d5c00d.py`.
Results: `research_notes/ns-f0-discrete-transfer-20260909-d5c00d.results.json`.

All certificate decisions use Fraction arithmetic in Q[i] and finite rational enclosures for positive square roots. No external Python dependency is required.

Executed:
- the exact witness (10), including a unique forward solve;
- embedding of the same zero-edge-defect step at M=2,3,5,8;
- the same-initial-modal-energy opposite-phase witness (11);
- 24 additional exact rational states, M=1,2,3,4, different viscosities and steps, checking both update equations and E/K balances;
- 24 finite-Gram identities (14), positivity checks, separated defect balances (15), and the explicit rounding-only positive-Gram defect (15a);
- the full fixed-grid trajectory from (10), reaching exactly zero after 96 steps, against the proven integer upper bound 42596;
- 56 of those steps have nonzero edge defect relative to the untruncated interpretation, explicitly recorded.

These checks supplement the finite algebraic proofs above. They are not a Lean proof, independent mathematical review, continuum trajectory validation, native-X6 construction, or NS singularity certificate.

The useful conclusion is precise: an autonomous, energy-dissipative finite-resolution network can transfer enough internally to increase a critical-style high-frequency readout, and that transfer cannot be predicted from energy-only state data. In this chosen model the growth is transient and eventual absorption is proved, so it cannot be presented as a blow-up example.

The next substantive task is to extend the phase-aware discrete Gram/defect balance to a genuinely three-direction coupled carrier, retaining all generated ports and precision defects, and derive a bound or counterexample for the *coherent accumulated* feedback term. Any observer retaining only the modal energies is already excluded as an exact predictor of the next signed K change by (11). This does not invalidate E as a dissipative bound or rule out other Lyapunov functions. No claim is made that enlarging a finite carrier by itself supplies the uniform or physical bridge needed by the parent NS problem.

The user's f=0 and no-answer-leakage requirements remain in force. The separate continuous mathematical NS problem and the native discrete physical model are not identified without an explicit bridge.
