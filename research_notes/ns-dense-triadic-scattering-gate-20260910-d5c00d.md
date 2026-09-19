# Triadic gate for dense lossless X6 scattering: symmetry, order state, and the sign of the coarse Laplacian

Event: `NS-DENSE-TRIADIC-SCATTERING-GATE-20260910-D5C00D-18`  
Researcher: `EM-DIRECT-D5C00D / TASK_RESEARCH`  
Activity: `RA-D5C00DF7D77F4AA2ACE0`  
Status: **TESTING — exact finite/algebraic proofs and exhaustive finite checks; not a primitive-force admission and not Navier–Stokes.**

## 0. Frontier and purpose

Event 17 produced an autonomous, translation-invariant, exactly lossless X6 scatterer whose zero-residual two-tick compression is

    T = I + (1/16) Delta_X6,

while retained residual ports later return and destroy the Markov-semigroup interpretation. The next question is whether a comparable positive native-Laplacian coefficient can arise when the local algebra is itself decomposed into three-participant events, in a way compatible with the project’s primitive-arity discipline rather than by using one 13-mode interaction as a black box.

This note does **not** identify algebraic three-mode updates with `PRIMITIVE_FORCE_QUANTUM` or certify `TRIADIC_CLOSURE_E`. P000 explicitly requires that extra semantic/dynamical certificate. The note instead establishes a scoped gate: what is and is not possible for a natural class of participant-symmetric, lossless three-mode updates, and what order/provenance state is required before such updates can touch all six native axis pairs.

Native X6 coordinates, signed primitive paths and Joint Relation Observer Preservation are retained. No continuum limit, smoothing, post-hoc force, residual reset, or fitted target trajectory is used.

## 1. One conflict-free three-mode layer cannot implement the 13-mode symmetric scatter

Consider one resolved local mode `c` and twelve residual ports `p_{i,+},p_{i,-}`. A conflict-free primitive algebraic layer is a family of disjoint three-mode events: one mode may participate in at most one event during that layer.

If the only initially perturbed mode is `c`, then at most one event contains `c`; hence at most two residual ports can be directly coupled to it in that layer. Any disjoint triple made only of zero residual inputs stays zero under a homogeneous linear update.

Therefore a one-layer three-mode realization cannot map

    (1,0,...,0)

into a state with nonzero amplitude on all twelve residual ports. The 13-mode Householder first column from event 17 does exactly that. Thus its one-tick action is not a conflict-free single layer of three-mode events.

There are `C(12,2)=66` possible cavity-containing triples, but selecting one does not remove the resource bound: each touches only two residual ports.

This is a one-layer resource statement, not a ban on sequential reuse, replicated internal resources, relation-valued branching, or environment-dependent scheduling.

## 2. A symmetric state cannot manufacture an axis order

Suppose the local state is invariant under the full permutation group `S6` on native axis labels, and a deterministic rule is required to select one axis as the first axis pair to process. Equivariance would require that selected axis to be fixed by the stabilizer of the state. The stabilizer is all of `S6`, which has no fixed axis. Hence there is no deterministic equivariant selector from the bare symmetric state.

This is the direct stabilizer obstruction used by the existing T7 equivariant-section calculus. Waiting does not create the missing information: a deterministic equivariant history generated from the same symmetric state remains fixed by the same stabilizer.

A spatial/material environment can of course carry a distinction. So can an explicit current relation/frame state. Such data must be retained and transformed under relabelling; it cannot be described as having arisen from a completely symmetric observation.

### Fair autonomous order-state lower bound in a stated class

Let an internal controller state `h` carry an `S6` action, update deterministically/equivariantly, and output one current axis. If the future orbit of `h` outputs all six axis labels, then any permutation fixing `h` fixes every future state and every future output. It therefore fixes all six labels and must be the identity. Thus the `S6` orbit of `h` is free and contains

    6! = 720

states.

Ordered six-axis frames attain this lower bound; cyclically shifting a frame visits all six axes. The result is scoped to this stand-alone deterministic equivariant fair-controller class. It is not a lower bound on mechanisms whose asymmetry is stored in the environment, on random/relation-valued updates, or on a differently typed native relation.

## 3. Classification of participant-symmetric lossless linear triadic maps

Let `M` be a real/rational `3 x 3` linear map that commutes with every permutation of its three participants. Then

    M = a I + b J,

where `J` is the all-ones matrix. Equivalently, M has one eigenvalue `epsilon_c` on the common line `(1,1,1)` and one eigenvalue `epsilon_d` on the two-dimensional difference subspace.

If M is orthogonal, both eigenvalues lie in `{+1,-1}`. Hence there are exactly four possibilities. Written by diagonal/off-diagonal entries:

| common | difference | diagonal | off-diagonal | mixing |
|---:|---:|---:|---:|:---:|
| +1 | +1 | 1 | 0 | no |
| +1 | -1 | -1/3 | +2/3 | yes |
| -1 | +1 | +1/3 | -2/3 | yes |
| -1 | -1 | -1 | 0 | no |

The first/last are nonmixing. The two nontrivial reflections are negatives of one another.

If, in addition, the **scalar sum of the three amplitudes is conserved eventwise**, the common eigenvalue must be `+1`. Therefore the unique nontrivial map in this class is

    G = (2/3)J - I,

with diagonal `r=-1/3` and off-diagonal `s=+2/3`.

The other nontrivial reflection

    -G = I - (2/3)J

has `r=+1/3`, `s=-2/3`; it preserves the full quadratic norm but flips the common/sum mode. It therefore does not preserve the scalar sum on an arbitrary triad.

This classification is a theorem about this declared algebraic class. It does not assert that a native force quantum is a linear amplitude or that its physical conservation law must be scalar-sum conservation.

## 4. Six sequential triads and exact two-sweep compression

Pair the twelve residual ports into the six signed axis pairs. Fix a retained ordered axis frame

    h=(i_0,...,i_5).

One local sweep applies the same nontrivial symmetric triadic map successively to

    (c,p_{i_k,+},p_{i_k,-}),      k=0,...,5,

then every residual port streams one signed primitive X6 step. The next sweep uses the same material frame. The frame is part of current state/relation data; it transforms under axis relabelling.

Let the triad matrix have diagonal `r=+/-1/3` and off-diagonal

    s=-2r.

Inject an arbitrary resolved field `a_0(z)` and zero residual deviations. During the first local sweep, before rank k the cavity coefficient is `r^k`. Thus after the first sweep

    c_1(z)=r^6 a_0(z),

and the two ports of axis `i_k`, after streaming, carry

    s r^k a_0(z -/+ e_{i_k}).

During the second sweep, an incoming port pair at rank k enters the final cavity with multiplier `s r^(5-k)`. Hence the rank cancels:

    (s r^(5-k))(s r^k)=s^2 r^5=4 r^7.

Therefore the exact resolved output after two full sweeps is independent of the chosen one of the `720` axis orders:

    a_2(z)
      = r^12 a_0(z)
        + 4 r^7 sum_{v in V12} a_0(z-v).                 (4.1)

Writing

    Delta_X6 a(z)=sum_v a(z-v)-12a(z),

we obtain

    a_2
      = (r^12+48r^7) I a_0 + 4r^7 Delta_X6 a_0.          (4.2)

The full state remains exactly norm-preserving because every local triad is orthogonal and streaming is a permutation.

### Sum-preserving triad: negative Laplacian sign

For `G`, `r=-1/3`. Then

    a_2(z)
      = 1/531441 a_0(z)
        - 4/2187 sum_v a_0(z-v),

so the `Delta_X6` coefficient is

    -4/2187 < 0.                                          (4.3)

Thus, inside this participant-symmetric linear orthogonal class, imposing eventwise scalar-sum conservation selects the **anti-diffusive sign** at this two-sweep resolved level.

### Quadratic-preserving common-flip triad: positive Laplacian sign

For `-G`, `r=+1/3`. Then

    a_2(z)
      = 1/531441 a_0(z)
        + 4/2187 sum_v a_0(z-v)

      = 11665/531441 a_0(z)
        + 4/2187 Delta_X6 a_0(z).                         (4.4)

Now the native-Laplacian coefficient is strictly positive.

The constant-field resolved attenuation factor in (4.4) is

    lambda0 = 11665/531441.

Factoring it **as an observer normalization only** gives the positive Markov shape

    a_2/lambda0
      = [I + (972/11665) Delta_X6] a_0,                   (4.5)

whose center weight is `1/11665` and each of twelve neighbor weights is `972/11665`; these weights are positive and sum to one.

Equation (4.5) is not a physical renormalization step and must not be iterated by silently resetting residual ports. It only states the exact spatial shape of the two-sweep zero-residual compression.

## 5. What the sign gate means

The main scoped conclusion is

> In the class of nontrivial linear, participant-symmetric, orthogonal three-mode exchanges, **eventwise scalar-sum conservation forces the negative X6-Laplacian sign in the two-sweep resolved compression. The positive sign is obtained by the other reflection, which preserves the quadratic norm but flips the common triad mode.**

Therefore “discrete + triadic + lossless” does not by itself determine the sign of an effective viscosity-like term. The sign depends on which native quantity/relation is actually conserved by the microscopic event.

This is precisely where the physics obligation now sits. If the physically meaningful conserved object is not the signed scalar amplitude sum, we must identify it from the native force/event semantics rather than add a compensator after seeing the desired sign.

## 6. Dense backgrounds exist for both algebraic signs

The positive/negative sign comparison does not require empty space.

For `G` (common eigenvalue +1), the constant local state with cavity and all ports equal to `beta` is fixed by each triad and by streaming.

For `-G` (difference eigenvalue +1), the constant local state

    cavity = 2 beta,
    every signed port = -beta

has zero sum on every `(c,p_{i,+},p_{i,-})` triple, hence lies in the fixed difference subspace of every triad and is also fixed by streaming.

Thus both test laws admit densely occupied stationary backgrounds. Quantitative perturbation statements use finite-norm deviations from them on the infinite lattice, or ordinary finite states on a periodic lattice.

This does not certify either background as a primitive stable force state.

## 7. A useful BRC result: order disappears from the two-sweep cavity but not from the residual

The checker exhausts all `720` ordered axis frames. For both nontrivial triad signs, equation (4.1) gives exactly the same resolved two-sweep field for every order.

However, after one sweep the residual-port state has `720` distinct order signatures for the unit cavity impulse. The k-th processed axis receives magnitude proportional to `r^k`, so the full residual carries the frame provenance.

Thus:

* dropping the frame is safe for the **specific two-sweep resolved field from zero residual input** because exact fiber constancy was proved;
* dropping it from the full state, or asserting unbounded-horizon safety, is not certified.

This is a positive example of scoped BRC compression rather than a blanket anti-compression rule.

## 8. Relation to event 17 and the f=0 line

Event 17 showed a one-step 13-mode lossless scatterer with exact positive heat compression, but it was not triadically decomposed. Event 18 shows something subtler:

1. a single conflict-free triad layer cannot perform that all-port coupling;
2. sequential reuse requires retained order/relation state;
3. a natural participant-symmetric triad class has an exact sign classification;
4. positive X6 diffusion can occur in a fully lossless sequential triad model, but only when the triad’s common scalar mode is not conserved eventwise;
5. the full residual must still be retained, so none of this creates an all-time Markov heat semigroup by itself.

The model is autonomous and has no external forcing term. This is relevant to the project’s `f=0` direction only as a discrete mechanism candidate. It is not yet a derivation of Navier--Stokes viscosity or nonlinear self-advection.

The next minimal question is now sharper than “can triads diffuse?”

> What is the native conserved object of a legal `TRIADIC_CLOSURE_E` event, and does its induced algebra select the positive or negative coarse Laplacian branch?

A valid answer must derive the conserved relation and local update before using the resulting sign as evidence.

## 9. Exact executed checks

The standard-library checker uses `Fraction` arithmetic only and verifies:

* the four `S3`-equivariant orthogonal classes;
* uniqueness of the nontrivial eventwise-sum-preserving mixer;
* all `66` cavity-containing one-layer triad choices and the two-port capacity bound;
* absence of an `S6`-fixed axis selector from the fully symmetric bare state;
* all `720` ordered six-axis frames and fair cyclic visitation;
* `720` exact two-sweep full-norm checks for each nontrivial triad sign;
* frame-independence of the resolved two-sweep impulse for all `720` orders;
* `720` distinct one-sweep residual order signatures;
* exact coefficients `+/-4/2187`, center `1/531441`, and the positive normalized kernel `1/11665 + 12*(972/11665)=1`;
* dense stationary backgrounds for both algebraic signs.

A fresh rerun produced a byte-identical result JSON.

Checker: `experiments/ns_dense_triadic_scattering_gate_d5c00d/check_triadic_gate.py`.

## 10. Nonclaims

This note does not establish:

* that the three algebraic modes are primitive force quanta;
* that either reflection satisfies `TRIADIC_CLOSURE_E`;
* that scalar sum or quadratic norm is the complete physical conservation law;
* that the 720-state bound applies to environment-driven or relation-valued mechanisms;
* an all-time heat semigroup, viscosity law, Navier--Stokes result, quantum result, independent review, Lean verification, or historical novelty.
