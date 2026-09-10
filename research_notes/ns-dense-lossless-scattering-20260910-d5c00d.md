# Dense X6 lossless scattering: exact coarse damping, residual return, and pathwise relation transport

Event: `NS-DENSE-LOSSLESS-SCATTERING-20260910-D5C00D-17`  
Researcher: `EM-DIRECT-D5C00D / TASK_RESEARCH`  
Activity: `RA-D5C00DF7D77F4AA2ACE0`  
Status: **TESTING — ordinary finite/algebraic proofs and exact executed checks; not primitive-force admission, not a quantum-origin theorem, and not Navier–Stokes.**

## 0. Question and scope

The working hypothesis from the user is: the native world is densely populated by discrete degrees of freedom, closed dynamics should not discard quantities without an explicit destination, and some apparently lost information may remain as transported residual relation. The previous event established exact reversible residual exchange and a quantum comparison, but did not yet exhibit a fully local six-axis scattering law whose coarse observable looks dissipative while the full state is lossless.

This note supplies such a **test model**, then shows the precise point at which a Markov/heat interpretation fails if the residual is retained. It also upgrades the quantum comparison from a single local correlation to an exact primitive-edge transport statement.

The assumptions are deliberately typed:

* native space is the existing signed X6 Cell torsor;
* every nonzero spatial movement is one `+/-e_i` step;
* “dense” means resident local degrees of freedom exist throughout the discrete lattice; it does **not** mean a continuum or topological density;
* a rational orthogonal scattering matrix is an additional constitutive test choice, not a consequence of P000;
* the quadratic norm below is a conserved model diagnostic, not already identified with total physical energy;
* the quantum subsection explicitly adds tensor-product quantum states, unitary gates and Born-observable semantics. It is a consistency/transport result, not a derivation of quantum mechanics from classical residuals.

Source snapshot used for the mathematical audit: `awdawmip/enterprise-math@3c5abd9dd2b0756dbb89c9eb13dc4396f1843fa7`. Current P000 and Joint Relation Observer Preservation were read before compression. A bounded code search for the combined terms “lossless scattering residual transport quantum walk” returned no hit; this is not a historical novelty or absence certificate.

## 1. A signed-axis symmetric 13-mode local scatterer

At each Cell `z in Z^6` let there be twelve directed residual ports indexed by the primitive signed directions

    V12={+/-e_1,...,+/-e_6}.

For the bulk construction there is also one resolved scalar amplitude `a(z)`. Write the local thirteen-component vector as

    X(z)=(a(z), f_v(z)_{v in V12}).

Define

    w=(2,1,1,...,1) in Q^13,        w^T w=16,

and the local Householder reflection

    H = I - (1/8) w w^T.                                     (1.1)

Because `(w w^T)^2=(w^T w)w w^T=16 w w^T`, direct multiplication gives

    H^2=I,       H^T H=I.                                    (1.2)

Thus H is exactly reversible and preserves the local square sum. Its cavity coefficients are

    H_00=1/2,        H_0v=H_v0=-1/4.                         (1.3)

After applying H independently at every Cell, stream every residual port one primitive step in its own signed direction:

    f'_v(z+v) = (H X(z))_v.                                  (1.4)

The resolved component stays at the same Cell after the local scattering. Call the global update U.

The local product of H matrices is orthogonal and (1.4) is a permutation of spatial-port slots. Therefore, for every finitely supported state, every periodic finite system, or every finite-norm deviation from a fixed background,

    ||U X||^2 = ||X||^2.                                     (1.5)

The rule is translation covariant and treats all twelve signed native directions identically. Under an axis relabeling/sign reversal, spatial coordinates and port labels must be transported together. No carrier projection is used to define the update.

### Dense stationary background

For any rational/real beta, put at every Cell

    f_v(z)=beta  for all v,
    a(z)=-6 beta.                                            (1.6)

Then the local Householder dot product is

    2(-6 beta)+12 beta=0,

so H leaves every local state fixed, and streaming preserves the constant port field. Hence (1.6) is a dense stationary background.

On the infinite lattice its absolute square sum is infinite when beta is nonzero, so all quantitative statements below are made for a finite-norm deviation from it. On a finite periodic lattice the same background is an ordinary finite exact fixed state. This distinction prevents an infinite background from being passed off as a finite-energy datum.

Because U is linear, deviations evolve by the same U.

## 2. Exact no-return damping without any sink

First isolate one material scatterer at an anchor c and let its twelve directed port fields stream ballistically away on the full X6 lattice. Start from a unit cavity deviation and zero port deviations:

    a_0=1,      f_0=0.                                       (2.1)

No emitted amplitude can return to the anchor: the `v` port emitted at c moves through

    c+v, c+2v, c+3v, ...

and the center receives that port only from the opposite upstream ray, which remains zero.

Therefore at every tick the local incoming residual is zero and (1.3) gives

    a_n = 2^{-n}.                                            (2.2)

The emission created at tick k has amplitude `-2^{-k-2}` in each of the twelve signed directions. At time n it is at distance `n-k` from c. Equivalently, for `1<=d<=n`,

    f_v(c+d v,n) = -2^{-(n-d+2)}.                            (2.3)

Hence the visible and residual square sums are exactly

    E_vis(n)=4^{-n},

    E_res(n)=12 sum_{k=0}^{n-1} (2^{-k-2})^2
            =1-4^{-n}.                                      (2.4)

Thus

    E_vis(n+1)-E_vis(n)=-(3/4)E_vis(n),

    E_vis(n)+E_res(n)=1.                                    (2.5)

The coarse variable exhibits an exact geometric “damping law”, but the full state has lost nothing. The missing visible square sum is the norm of actual outgoing residual amplitudes on actual primitive paths.

This is an existence statement for one declared lossless scatterer. It does not prove that all observed damping is of this form.

## 3. Finite return destroys permanent dissipation

Put each directed residual port on a finite directed cycle of length L, preserving the same local H. The full finite map remains orthogonal and exactly reversible.

For the initial state (2.1), no residual returns to the scatterer during the first L center updates. Thus

    a_n=2^{-n},        0<=n<=L.                              (3.1)

The first emission `-1/4` in each of the twelve channels returns before the next scattering. At that update the local Householder input satisfies

    sum_v f_v(c) = -3,

so

    a_{L+1}
      = 2^{-L} - (1/4)(2^{1-L}-3)
      = 3/4 + 2^{-(L+1)}.                                   (3.2)

For L=5 this is `49/64`; for L=7 it is `193/256`.

Therefore finite lossless residual capacity naturally produces a no-return window followed by coherent backflow. “The local variable decayed for many steps” is not by itself a certificate of permanent microscopic dissipation.

## 4. A translation-invariant bulk model produces an exact X6 heat step — once

Now use H at **every** Cell of X6 and stream all twelve ports by (1.4). This is a translation-invariant, signed-axis symmetric, globally orthogonal bulk update.

Inject an arbitrary resolved field `a_0(z)` with all residual ports initially zero. After one native tick,

    a_1(z)=1/2 a_0(z),

    f_{1,v}(z)=-1/4 a_0(z-v).                               (4.1)

At the second local scattering, the Householder dot product at z is

    2 a_1(z)+sum_v f_{1,v}(z)
      = a_0(z) - (1/4) sum_v a_0(z-v).

Therefore

    a_2(z)
      = 1/4 a_0(z) + (1/16) sum_{v in V12} a_0(z-v).        (4.2)

Define the native twelve-neighbor discrete Laplacian

    Delta_X6 a(z)=sum_{v in V12}a(z-v)-12a(z).              (4.3)

Then the exact two-tick resolved map is

    a_2 = T a_0,

    T = I + (1/16) Delta_X6.                                (4.4)

This is not an asymptotic limit. It is an exact finite algebraic identity for the stated residual-zero input.

The kernel of T has weights `1/4` at the same Cell and `1/16` at each of the twelve native neighbors; the weights are nonnegative and sum to one. Consequently T is an l2 contraction by the finite/discrete Young inequality (and on finite periodic boxes by the same convolution calculation).

### The semigroup trap

Equation (4.4) does **not** imply

    a_{2m}=T^m a_0.                                         (4.5)

After the first two ticks the residual ports are nonzero and must participate in later updates. For the delta input at the origin, exact computation gives visible square sums

    1,
    1/4,
    7/64,
    403/4096,
    9553/65536                                              (4.6)

at native ticks 0 through 4. In particular the visible square sum increases from tick 3 to tick 4 by

    3105/65536 > 0.                                         (4.7)

Even at the field level the fourth-tick resolved center is

    a_4(0)=1/64,

whereas a residual-reset heat iteration would give

    (T^2 delta_0)(0)=7/64.                                  (4.8)

Thus

    P U^2 J = T

for the injection J of zero residual and projection P onto the resolved field, but

    P U^4 J != T^2.                                         (4.9)

Replacing the true residual after every macro-step by zero would produce repeated heat evolution, but that is a different open/reset operation. A closed dense model must either retain the memory/backflow or separately prove a mechanism that makes it irrelevant at the declared observational scale.

This is the precise version of “do not manufacture dissipation by erasing the residual”.

## 5. Persistent exact heat under reversibility needs unbounded residual capacity

The preceding finite return is not an accident of the chosen ring. There is a general finite-dimensional obstruction.

Let H_vis be finite-dimensional and let T be a self-adjoint contraction on it with an eigenvector x and eigenvalue lambda satisfying

    0<|lambda|<1.                                           (5.1)

Suppose a finite-dimensional Hilbert space K, a unitary U on K, and an isometric embedding J:H_vis->K satisfy the exact all-time compression

    J^* U^n J = T^n        for every n>=0.                  (5.2)

Take ||x||=1. Then

    <Jx,U^n Jx> = lambda^n -> 0.                            (5.3)

But write the spectral decomposition of U on the finite cyclic subspace generated by Jx:

    <Jx,U^n Jx> = sum_j c_j z_j^n,

where `|z_j|=1`, `c_j>=0`, and `sum c_j=1`. The sequence of phase vectors `(z_1^n,...,z_m^n)` has a subsequence approaching `(1,...,1)` (compactness of the finite torus, applied to differences of a convergent subsequence). Along that subsequence the right-hand side approaches `sum c_j=1`, contradicting (5.3).

Therefore no finite-dimensional closed unitary system can reproduce a strict contractive eigenmode exactly for all times.

For the X6 heat operator (4.4) on a side-4 periodic box, the Fourier mode `k=(1,0,0,0,0,0)` has the exact eigenvalue

    lambda = 1/4 + (1/8)(0+1+1+1+1+1) = 7/8.              (5.4)

Hence an exact all-time reversible realization of repeated T must have effectively unbounded residual capacity (or abandon one of the assumptions: finite dimension, exact all-time equality, closed unitarity, or the same Markov T).

This theorem does not prove that the physical universe is infinite. It states a precise cost of reconciling permanent exact coarse dissipation with a closed reversible model.

## 6. Positive residual energy is not a sufficient state

BRC/observer preservation is active here. Even if one accepts a residual sector, compressing it to positive energy loses future dynamics.

Take two local inputs with the same cavity amplitude `a=1` and one nonzero incoming port, respectively `+1` and `-1`. Their cavity energy, every per-port positive energy, and total square sum are identical.

By (1.1), however,

    a'_+ = 1/4,
    a'_- = 3/4,

so

    E'_{vis,+}=1/16,
    E'_{vis,-}=9/16.                                      (6.1)

Therefore the observer containing **all per-slot positive energies** fails fiber constancy for the next visible energy. The signed/phase relation between resolved and residual amplitudes must be retained for this future operation.

This is why “the residual energy went somewhere” is not yet a closed model. One must retain enough of the residual's phase/path/provenance to compute its return.

## 7. Quantum relation residual can be transported one native edge at a time

This subsection adds standard quantum assumptions explicitly. Consider one fixed qubit A and a chain of resident qubits B_0,...,B_m placed along any declared native composite path

    z_0 -> z_1 -> ... -> z_m,

where every displacement `z_{j+1}-z_j` is exactly one signed native basis step.

Start with the single-excitation Bell state

    |Psi+>_(A,B0) = (|10>+|01>)/sqrt(2)                   (7.1)

and every later B_j in |0>. At tick j apply only the local SWAP between B_{j-1} and B_j.

By direct tensor-factor permutation,

    rho_j
      = |Psi+><Psi+|_(A,Bj)
        tensor (product of |0><0| on the vacated B registers).   (7.2)

Thus the entangled endpoint advances exactly one primitive spatial edge per tick. The total excitation number remains one.

For the Bell pair define the joint-relation residual

    chi_AB = rho_AB - rho_A tensor rho_B.                  (7.3)

Its two partial traces vanish and

    ||chi_AB||_HS^2 = 3/4.                                 (7.4)

Equation (7.2) means that this same joint relation is transported from `(A,B_{j-1})` to `(A,B_j)` by a local gate; it is not copied. The previously occupied endpoint becomes uncorrelated with A.

The endpoint state remains operationally entangled. Its partial transpose has the principal determinant

    -1/4 < 0.                                              (7.5)

With the exact rational observables

    A0=X,        A1=-Z,
    B0=(3X+4Z)/5,
    B1=(3X-4Z)/5,

one obtains

    E00=3/5, E01=3/5, E10=4/5, E11=-4/5,

    CHSH = 14/5 > 2.                                      (7.6)

The violation is unchanged as the B endpoint is moved by SWAPs.

This supports a precise version of the user's phrase “entanglement as transmitted residual”: **a joint, phase-sensitive relation can be locally transported through resident degrees of freedom while local marginals do not encode the whole relation.** It does not support replacing that relation by a classical scalar hidden cargo. Under setting independence and local outcome factorization, the ordinary CHSH bound remains two.

Nothing here permits superluminal signalling: the correlation endpoint moves by one declared local gate per native edge; later remote measurement statistics still obey the usual non-signalling statement under nonselective local operations.

## 8. What is common — and what is not

The classical/amplitude and quantum examples share one observer principle:

    full closed state -> chosen local/marginal observer + retained complementary relation.

If the observer drops the complement, its dynamics can look contractive, stochastic, or dissipative. Retaining the complement restores the exact reversible ledger in the declared examples.

But two residuals must **not** be identified merely by the word “residual”:

* the Householder residual is a signed/phase amplitude field carrying square norm on native paths;
* `chi_AB` is an operator-valued joint correlation with zero local partial traces;
* neither is automatically a physical heat reservoir;
* entanglement requires quantum state/composition/measurement structure beyond classical positive hidden variables.

The safe research statement is therefore:

> Apparent local loss should first be tested as transfer into retained joint degrees of freedom. If the future depends on signed, phase, path, or correlation information, those coordinates cannot be replaced by a scalar loss term without an exact closure certificate.

## 9. Consequence for the f=0 / effective-viscosity research line

The bulk identity (4.4) is the important new bridge candidate:

    a_2 = a_0 + (1/16) Delta_X6 a_0

appears **inside a globally lossless, autonomous, translation-invariant X6 update**, with no external force and no continuum limit.

However (4.9) is equally important. It forbids claiming that this already derives a permanent heat semigroup or Navier–Stokes viscosity. The retained residual produces memory and backflow.

The next valid route is therefore not “erase the residual to obtain viscosity”. It is:

1. identify a physical resolved variable and a physical conserved full quantity;
2. derive the residual coupling from a native legal event law;
3. characterize the exact memory kernel/no-return horizon;
4. prove, rather than assume, when the residual contribution becomes negligible for a declared coarse observer;
5. only then compare the resulting effective operator with a viscous Laplacian;
6. keep the nonlinear `f=0` self-state dynamics autonomous throughout.

This is compatible with the project's anti-erasure/BRC rules and avoids target-imprinted residual completion: the residual state is generated by a fixed full update before the coarse equation is read off.

## 10. Executed exact checks

The standard-library checker uses `Fraction` only. It verifies:

* all 169 inner products needed for exact H13 orthogonality and H^2=I;
* dense stationary local background;
* the infinite no-return formulas through n=10;
* finite 12-channel ring return for L=5,7,11, including exact full norm conservation;
* the positive-energy fiber counterexample `1/16` versus `9/16`;
* the translation-invariant bulk update through four native ticks, exact `T=I+Delta_X6/16` at tick two, and explicit failure of `T^2` at tick four;
* exact visible backflow `3105/65536` from tick three to four;
* the periodic side-4 strict heat eigenvalue `7/8` used in the finite-unitary obstruction;
* a four-edge mixed-axis X6 path carrying a Bell relation by exact sparse density-matrix SWAPs;
* exact one-excitation preservation, partial-transpose determinant `-1/4`, relation Hilbert--Schmidt square `3/4`, and CHSH `14/5`.

No floating point, smooth extension, continuum limit, residual fitting, or postselected quantum sample is used in these checks.

Checker: `experiments/ns_dense_lossless_scattering_d5c00d/check_lossless_scattering.py`.

Run:

    python experiments/ns_dense_lossless_scattering_d5c00d/check_lossless_scattering.py --output results_17.json

## 11. Nonclaims and next frontier

This note does not establish:

* that the Householder scatterer is the native force law;
* that its quadratic is complete physical energy;
* that nature is exactly reversible;
* that entanglement is derived from classical residual transport;
* a calibrated speed of light;
* an exact infinite-time Markov heat law;
* a Navier–Stokes viscosity derivation, regularity theorem, or blowup theorem;
* independent review, Lean verification, or historical novelty.

The next smallest research unit is to replace the test scatterer by a legally typed native three-force exchange/transport mechanism and ask whether its **resolved two-tick compression still produces a positive X6 Laplacian coefficient while the full update remains conservative**. A second, independent branch is to determine what operator-valued native relation would be needed to reproduce the transported Bell residual without inserting quantum tensor-product semantics by fiat.
