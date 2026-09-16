# 三参与者有限关系门：无旁观者分解、守恒编码与奇支撑障碍

Event: `NS-TRIADIC-RELATION-GATE-20260916-D5C00D-20`  
Researcher: `EM-DIRECT-D5C00D / TASK_RESEARCH`  
Activity: `RA-D5C00DF7D77F4AA2ACE0`  
Status: **TESTING — ordinary finite/algebraic proofs and exact executed checks; quantum comparator, not native force admission.**

## 0. Question, frozen inputs, and semantic boundary

Continue the exact event19 frontier at `awdawmip/enterprise-math@93c915c8f265ac19ada274cb34f02730c7ab91ca`. Event19 supplied finite endpoint fragments, but its preparation used two CNOT encounters. This event asks whether a structurally three-party, permutation-compatible relation transformation can replace those pair gates, preserve the already specified finite relation alphabet and a declared excitation indicator, and run only after three actual X6 participants meet.

P000, its signed six-axis Cell torsor, and the distinction between spatial coordinates and internal decorations are unchanged. The task-local dense-resident/no-arbitrary-erasure hypothesis is retained. No protected worldview, README, Foundation status, other researcher's task, or physical force law is modified.

**Important:** three quantum tensor factors are not three certified primitive forces. A ternary operation not factoring into a spectator and a pair is a necessary structural test for this candidate, not a certificate of `TRIADIC_CLOSURE_E`. Quantum Pauli algebra, stabilizer states, tensor products and Born measurements remain explicit comparison assumptions. Internal complex phases are not native spatial angles. No physical outcome is used to choose a residual, force or reservoir.

Reuse is executable, not terminological. The event18 checker SHA256 `6ff48da0bbd6a041f580696f464353216696bd21a27d0ac411b0e2dafe4202a4` and event19 checker SHA256 `e3ea2ebb040b00969a5896164978b92c4726bd53bc7f1c4e6784d08c573c98a7` are imported unchanged. We use their Pauli matrices, finite orbit, density reconstruction, endpoint `Distributed` class, gauge transform and native unit-step validator. This is a specialized extension, not a new admitted toolbox family. The 1080-state stabilizer orbit is prior work/standard subtheory, not a new discovery here.

## 1. A fixed ternary relation transformation

For a positive Pauli word P in {X,Y,Z}^3, define the comparator

    R_P=(I-iP)/sqrt(2).

It is unitary because P=P^dagger and P^2=I. Its action on a signed Hermitian Pauli row S is exactly

    T_P(S)=S                     if PS=SP,
    T_P(S)=-iPS                  if PS=-SP.                 (1)

This follows by expanding R_P S R_P^dagger. In the second case PS is anti-Hermitian and -iPS is another signed Hermitian Pauli. Thus (1), not a sequence of rounding amplitude calculations, is the runtime relation rule. It uses only a finite product table and signs. T_P^4=identity. Every commuting independent generator family remains so by conjugation, so its stabilizer state remains valid.

Select P=XXX for the spatial test. Applied to the product-state generators it gives

    ZII -> -YXX,   IZI -> -XYX,   IIZ -> -XXY.             (2)

All three initially local independent rows gain three-party support in one actual co-located event. The corresponding comparator state is

    psi_-=(|000>-i|111>)/sqrt(2).                           (3)

No CNOT is called by this update. The defining law was frozen in law.json before execution. It is a constitutive test choice, not a law derived from P000.

## 2. No removable participant, but no false claim of physical primitivity

For every bipartition a | bc,

    R_XXX=(I_a tensor I_bc - i X_a tensor X_b X_c)/sqrt(2).

The two factors on each side are linearly independent. Its operator Schmidt rank is therefore exactly two, not one, across every cut. No participant can be discarded by writing R=V_ab tensor W_c, and similarly for the other cuts. On input |000>, every one-party marginal changes from |0><0| to I/2; all three take a nontrivial role on the chosen experiment.

These are scoped statements. On |+++>, R contributes only a global phase, so no density changes. Requiring a nontrivial observable change on every legal input would be false. Structural three-party dependence does not mean all inputs activate that dependence.

Nor does rank two prove an indivisible elementary event. Set V=CNOT_(1->3) CNOT_(2->3), W=H^tensor3 V. Then W Z_3 W^dagger=XXX and

    R_XXX=W R_Z3 W^dagger.                                (4)

The checker verifies (4) exactly. A pair-gate implementation exists in the larger comparator gate family. The distinction is: the new rule has no spectator factor as a map, but can be a composition of other operations. Native force admission still requires independently specified event/exchange semantics; neither three labels nor nonfactorization is enough.

## 3. Permutation-compatible endpoint signs; no distinguished sign sink

Use the event19 representation of three independent row IDs. Each endpoint stores one Pauli letter and one sign per row. Their signed tensor product reconstructs the global row.

For one row let k be the number of local anticommutions between P_a and S_a. If k is even, change nothing. If k is odd, multiply each local pair P_a S_a. A local anticommuting product is i*tau_a times a Hermitian Pauli, tau_a in {+1,-1}. Retain the resulting local letter and multiply that endpoint's sign by tau_a. When k=3, additionally flip all three endpoint signs. When k=1, do not add those flips.

The global sign factor is product(tau_a) for k=1 and -product(tau_a) for k=3, exactly the factor -i*i^k in (1). No endpoint is privileged to receive a global minus sign. Simultaneous permutation of the three participants, P's letters and endpoint data commutes with this raw update. The checker exhausts 27*64*8=13,824 raw row inputs and 82,944 permutation equalities.

Each endpoint still has at most 4^3*2^3=512 raw relation symbols for this fixed three-row system. That count does not include spatial position, retained source roles, or controller phase. Validity constraints reduce the usable set. It is not a fixed per-site storage theorem for arbitrarily large entangled networks.

The event19 sign-gauge family (four even sign redistributions per row; 64 for three rows) remains safe: the update ignores the existing sign split and multiplies only the local factors above. Equal global products remain equal after every step, hence after any composition of these specified maps. This gives an all-finite-depth gauge descent proof; the 64-lift/four-step test is a regression check. Local Pauli letters and row IDs are not thereby discardable.

## 4. A conserved-indicator realization without an added loss reservoir

On three bare two-level ports, R_XXX does NOT conserve bare excitation. From |000> it gives expected bare excitation 3/2. Thus 'unitary' alone would be insufficient to claim conservation.

Use the already-declared dual-rail internal code at each of the three participants:

    |0_L>=|01>,   |1_L>=|10>.

The six binary modes are internal decorations, not the six spatial axes. Let E embed the logical eight-dimensional space into the physical 64-dimensional space and F=EE^dagger. Define on that complete space

    U_phys=E R_XXX E^dagger + (I-F).                       (5)

This is a fully specified extension, identity outside the code. E^dagger E=I and the two subspaces are orthogonal, so (5) is unitary. Each pair-number operator N_a acts as identity on the code and preserves its complement. Therefore

    [U_phys,N_a]=0  for a=1,2,3.                          (6)

Initially and throughout the selected protocol, every pair has one excitation and total N=3. Logical X/Y measurements act inside these fixed-number subspaces. No environment is reset and no missing quadratic amount is sent into an invented sink.

If equal mode energies epsilon are an additional physical convention, epsilon*sum N_a is a conserved internal excitation indicator. It is NOT a complete Hamiltonian for controller, transport and interaction. This event neither identifies the relation sign as energy nor accounts for a physical apparatus's full energetics. Relational/degenerate encoding is an established quantum resource method [3].

A useful algebraic obstruction explains why encoding matters. If a Clifford V on bare n qubits commutes with N=(nI-sum Z_i)/2, then

    sum_i V Z_i V^dagger = sum_i Z_i.

Distinct Pauli words are linearly independent and conjugation preserves their independence, so each V Z_i V^dagger must be a different positive Z_j. Every joint Z basis vector is then mapped to another joint Z basis vector up to phase. Such a V cannot entangle a computational-basis input. This statement does not exclude diagonal Clifford entangling already coherent inputs. The coded gate escapes it because logical Z is NOT the conserved physical pair number.

## 5. A three-phase autonomous spatial test, without remote updates

Supply a Cell anchor c and three retained source roles z_a=c+s_a e_(i_a), with distinct i_a and s_a in {+1,-1}. The complete test state consists of the current relation fragments, current positions, source-role data and phase phi in Z/3. Define:

    phi=0: gather all three by their one signed step to c;
    phi=1: apply T_XXX only if all three are at c;
    phi=2: return each to its retained source, then repeat.

This is one fixed function of current state. It is not an externally supplied gate timetable. Nevertheless the three-phase program and selected triple are declared material control data of a test apparatus, not a derived selection law for a dense world. Source/phase information is indispensable: co-location alone cannot determine which source to return to, and the two co-located phases have different next actions.

Every nonzero movement is a signed primitive X6 edge. The fixed-state-family map is bijective: reverse the return, use T_XXX^3 for inverse conjugation, then reverse the gather, retaining phase/source data. Its relation has period four, so from the chosen product state its complete density/endpoint controller orbit has exact period twelve ticks. At the four completed exchanges the logical state projectors follow

    |000> -> psi_- -> |111> -> psi_+ -> |000>.             (7)

This is coherent return, not convergence, dissipation, or unbounded instability. The code's three excitation indicators remain constant even though logical-Z populations alternate.

All 6*5*4*2^3=960 signed ordered three-axis placements were checked for twelve ticks, totaling 23,040 nonzero native moves. The same relation trajectory holds for every placement. Translating c translates all paths, by the formula. Separated gate input is rejected, not repaired with a nonlocal channel. Extended spectator systems are unchanged outside the actual gate's support; conjugation commutes with all their local operators, proving remote-marginal invariance for arbitrary joint states.

## 6. BRC witness stronger than unchanged marginals: equal pair states, different later local populations

The two coherent states psi_+ and psi_- have the same reduced density on every one- and two-party subset. Both also share these reductions with the incoherent half-|000>, half-|111> mixture. For two parties the reduced state is half-|00>, half-|11>.

But using the SAME R_XXX at a new actual three-party encounter gives

    R rho_- R^dagger=|111><111|,
    R rho_+ R^dagger=|000><000|.                           (8)

Their future local populations are opposite. Therefore even the complete collection of all one- and two-party density matrices is not a sufficient closed state for this next allowed operation. The missing triple phase is operational; it cannot be replaced by the pair marginals. No energy reservoir is associated to that difference by definition.

For rho_-, the explicitly chosen Mermin operator

    M=YYY-YXX-XYX-XXY

has expectation four; the incoherent mixture has zero. At every deterministic setting-independent local hidden assignment, its value is +/-2. Averaging does not change that bound. The checker executes all 64 assignments and all 64 probabilities for the eight X/Y setting triples, verifies nonnegative normalized distributions and uniform one-party marginals. These are ordinary quantum comparator predictions, not a derivation of Bell violation from local classical residuals [2].

Local finite endpoint preparation does NOT supply a local classical outcome sampler. If outcomes after separation were functions only of each endpoint, its independently chosen setting and shared classical initial data, the Mermin bound would still be two. The current executable reconstructs the joint quantum relation and uses Born measurements as an explicit additional interface. No faster-than-light communication or locally factorized hidden-variable realization is claimed.

## 7. New arbitrary-composition obstruction: odd Pauli support parity

This section is independent of a finite run. Encode an n-party Pauli up to sign by (x,z) in F2^(2n), using I=(0,0), X=(1,0), Z=(0,1), Y=(1,1) per site. Define

    q(x,z)=sum_a (x_a+z_a+x_a z_a) mod 2.

It equals the parity of the number of nonidentity factors. Its polarization is the symplectic commutation form:

    q(v+w)=q(v)+q(w)+[v,w].

Conjugation by R_P has binary action t_p(v)=v+[v,p]p. If [v,p]=0, q is unchanged. If [v,p]=1,

    q(t_p(v))=q(v)+q(p)+1.

Hence every odd-weight P preserves q, including every weight-three gate above. Single-party Clifford gates permute X,Y,Z and also preserve q; party permutations do too. Thus any finite composition of these operations, including overlapping triples on any fixed register, preserves Pauli support parity.

CNOT on the same register sends XII to XXI and changes this parity. Therefore it cannot be implemented by this odd-weight gate family plus single-party Cliffords and swaps, without extra resources such as ancillas, conditioning, measurements or a broader gate family. This is a restriction of the specified comparator, NOT a no-go theorem for all P000 ternary laws.

The construction (2) is permitted: support 1 becomes support 3. The old event19 support transition 1->2 is not a legal row transition in this family.

There is a useful counterweight. Exact BFS under the six single-party H/S generators plus all 27 weight-three R_P gates nevertheless reaches ALL 1080 three-party pure stabilizer states from |000>. All 29,160 triple-gate images of the parent orbit remain inside it. This is a finite exhaustive state-reachability certificate, not a claim of quantum universality. It is consistent with the parity obstruction because mapping one selected initial state is weaker than matching a channel on every possible input.

    PREPARE_EVERY_STATE_IN_A_FINITE_FAMILY != IMPLEMENT_EVERY_CHANNEL_ON_THAT_FAMILY.

## 8. Execution, status, and next physical obligation

The exact checker completed 1,728 independently matrix-verified conjugations, 13,824 raw endpoint rows, 82,944 permutation equalities, 29,160 stabilizer-state images, the restricted 1080-state orbit, 64 gauge lifts, all X/Y probabilities, the three operator-cut ranks, the physical-number embedding, the pair-circuit decomposition and 960 spatial tests. The modulo-two proof and the general bare-number/Clifford obstruction are analytic finite-algebra arguments, not extrapolations from these tests.

No numerical fitting, decimal rounding, smooth limit, Monte Carlo inference, hardware experiment, independent review or Lean build is represented by these checks. Exact finite relation closure is scoped to fixed qubit count and the stated subtheory. It does not derive the Born rule or a fixed-alphabet theory of all growing many-body systems.

The candidate now meets three narrower obligations: all three factors are structurally essential; their finite endpoint update can be permutation-compatible without a privileged sign sink; and their exchange can be embedded in a specified conserved internal-number sector with actual primitive paths. It still needs an independent native interaction/measurement derivation. Inventing a third force called 'whatever restores the desired rule' would not discharge that obligation.

The next admissibility problem is to specify a native three-event interaction and its measurements whose exact induced map equals or differs from this finite interface, while retaining the extra parity invariant and all resource assumptions. The current cycle is a conservative recurrent control, not evidence of NS blow-up or natural instability.

## References and provenance

[1] Daniel Gottesman, *The Heisenberg Representation of Quantum Computers*, arXiv:quant-ph/9807006; and *Stabilizer Codes and Quantum Error Correction*, arXiv:quant-ph/9705052. Standard stabilizer/Clifford comparator background, no priority claim.

[2] N. David Mermin, *Extreme quantum entanglement in a superposition of macroscopically distinct states*, Phys. Rev. Lett. 65, 1838 (1990), DOI 10.1103/PhysRevLett.65.1838. The concrete phase-convention computation is supplied above.

[3] Bartlett, Rudolph and Spekkens, *Reference frames, superselection rules, and quantum information*, arXiv:quant-ph/0610030, Rev. Mod. Phys. 79, 555 (2007). Relational encoding and explicit resources, not a P000 derivation.

Source constraints: current global `00_BOOTSTRAP.md`, `OPERATING_MANUAL.md`, project P000 and BRC first-line contract at global main@9287624cfebacc32cb4f15312a0a5c81ca89cc62. Research source pin as in section 0. No new formal task claim or mathematical admission is created by this research note.
