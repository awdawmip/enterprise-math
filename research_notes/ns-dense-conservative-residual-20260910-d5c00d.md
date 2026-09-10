# Dense occupancy, conservative exchange and correlation residuals

Event: `NS-DENSE-CONSERVATIVE-RESIDUAL-20260910-D5C00D-16`  
Researcher: `EM-DIRECT-D5C00D / TASK_RESEARCH`  
Activity: `RA-D5C00DF7D77F4AA2ACE0`  
Status: **TESTING: ordinary algebraic proofs and exact executed checks; conditional quantum comparison, not a native-force or NS theorem.**

## 1. New user hypothesis and scope

The current user asks to try dense occupancy, no arbitrary dissipation, and entanglement as residual transmission. Here dense means populated discrete Cells with interacting internal degrees of freedom, NOT topological density in a continuum. The wording about residual transmission is a working interpretation. This is a task hypothesis: no protected worldview, P000, README or accepted theorem is changed.

Native positions remain signed Z6 coordinates with primitive spatial edges +/-e_i. A resident Cell with an internal zero label or unexcited level is not absent. Internal ports and Hilbert-space axes do not redefine spatial dimension or Enterprise angles. We explicitly choose reversible updates to isolate exchange, but conservation alone does not imply reversibility.

Source snapshot: awdawmip/enterprise-math@902318ee8a5dd5065fa43710c3521898bec4120b. Reuse: the conservative reflect3 function in experiments/ns_native_integer_exchange_d5c00d/check_exchange.py is imported UNCHANGED, SHA256 90018aba469afdc3b2c8cd44fff1a442d5b830943c92f381dbcca5802968e493 (REUSE_EXECUTED). The signed X6 Cell torsor and Joint Relation Observer Preservation/fiber contracts are applied (REUSE_APPLIED). The old complete test suite is not claimed rerun. A bounded combined-term source search found no match; this is not a novelty or absence proof.

## 2. Exact reversible integer exchange, without an added reservoir

For x in Z3 with sum S divisible by three use the existing C(x)_i=2S/3-x_i; for other totals use identity. C is an integer involution, preserving S and Phi=sum x_i^2. This is a constitutive comparison law, not a physically certified exchange.

For six existing internal slots, fix observer blocks 123 and 456. Put

    Phi=sum_i q_i^2,
    E_visible=((q1+q2+q3)^2+(q4+q5+q6)^2)/3,
    E_residual=Phi-E_visible.

Expanding squares gives E_residual=sum_blocks sum_i(q_i-block_mean)^2>=0. The rational mean is an observer, not written back into integer slots. Apply C only to slots 234:

    (0,3,3,0,0,0) -> (0,1,1,4,0,0) -> (0,3,3,0,0,0).

The (total,visible,residual) ledger is

    (18,12,6) -> (18,20/3,34/3) -> (18,12,6).

Visible loss 16/3 is precisely the gain of residual variation already carried by the original slots, and returns. No free compensating variable was created. Phi is a specified quadratic diagnostic, NOT already identified as nature's total energy.

A finite integer system with bounded Phi, finitely many control phases and an invertible update has finite periodic orbits: every coordinate is bounded by floor(sqrt(Phi)), and bijectivity rules out transient merging. This excludes permanent strict relaxation in that finite reversible model. It does not cover noninvertible conservative laws or growing systems.

## 3. Exact residual memory, derived from a fixed full update

Split any specified finite unitary/orthogonal update into observed and unobserved coordinates:

    x_(n+1)=A x_n+B y_n,
    y_(n+1)=C x_n+D y_n.

Finite substitution proves

    x_(n+1)=A x_n+B D^n y0
                +sum_(j=0)^(n-1) B D^(n-1-j) C x_j.

All coefficients and the initial residual y0 come from the prior full state and update, not a desired trajectory. Unitarity also gives

    ||x_(n+1)||^2-||x_n||^2=||y_n||^2-||y_(n+1)||^2.

Use the rational reflection G=(2/3)J-I, whose diagonal is -1/3 and off-diagonal entries 2/3. G^2=I=G^T G; for P=J/3, G=P-(I-P). It preserves the common component and reverses the difference component. As a linear amplitude operation it is defined on all inputs; the integer-label operation retains its divisibility guard, so the two types must not be conflated.

Observe the first amplitude. Then A=-1/3, B=(2/3,2/3), C=B^T, D=[[-1/3,2/3],[2/3,-1/3]], and

    B D^m C=8/3^(m+2).

From (1,0,0), the first amplitude is 1,-1/3,1,-1/3,..., with visible square 1,1/9,1,... . Artificially resetting the other amplitudes after every step instead gives (-1/3)^n. That reset is a changed open operation, not dissipation proved for the original closed update.

## 4. A quantum comparison that conserves an explicit excitation indicator

ADDITIONAL ASSUMPTIONS: tensor-product quantum states, Born measurements and the declared unitary. These are not derived from P000, discreteness or dense occupancy [1]. Three internal two-level ports A,B,C are present. Their |0> means unexcited, not an absent Cell.

Define U to be G on the ordered single-excitation subspace |100>,|010>,|001> and identity on the other five computational basis states. For N=N_A+N_B+N_C,

    U^dagger U=I, U^2=I, [U,N]=0.

Thus the specified internal excitation energy indicator H0=epsilon*N is conserved: U^dagger H0 U=H0. Unitarity alone would not establish this; the commutator is checked. H0 is not claimed to be the complete physical Hamiltonian including any implementation/controller. A primitive force implementation of U remains open.

The actual output from |100> is

    |psi>=(-|100>+2|010>+2|001>)/3.

It remains in the exact N=1 sector. A's excitation probability is 1/9, and B,C each have 4/9. Applying the SAME U again returns |100>. No sink or new energy store is added.

Ignoring A WITHOUT measuring or postselecting it gives, in the basis 00,01,10,11,

    rho_BC=(1/9)[[1,0,0,0],[0,4,4,0],[0,4,4,0],[0,0,0,0]].

Its partial transpose has principal block [[1/9,4/9],[4/9,0]], determinant -16/81. Since every separable state's partial transpose is positive semidefinite, this proves entanglement [2].

A stronger exact operational check uses B-side observables A0=X,A1=Y, and C-side B0=(3X+4Y)/5,B1=(3X-4Y)/5. Each is Hermitian and squares to identity. The four correlations are

    E00=E01=8/15, E10=32/45, E11=-32/45,
    CHSH=E00+E01+E10-E11=112/45>2.

All 16 joint outcome probabilities are nonnegative rational numbers; each measurement-setting pair normalizes to one, and each local marginal is one half. No A-result is discarded.

A classical local hidden-variable model with setting independence and local outcome factorization obeys |CHSH|<=2: at each deterministic hidden state lambda, A0(B0+B1)+A1(B0-B1)=+/-2; averaging over the same setting-independent distribution preserves the bound [3]. Arbitrarily dense shared past data, residuals or extra coordinates do not change this algebra while those assumptions remain. Bell experiments supply a real constraint on any proposed physical alternative [4].

Hence the quantum calculation is a consistency example, NOT a derivation of quantum entanglement from classical residual transport. Its tensor product, complex amplitudes and Born rule are explicit inputs.

## 5. Correlation residual is not energy residual

Let chi=rho_BC-rho_B tensor rho_C. Its two partial traces vanish. It records joint information absent from either marginal, but is not an independent probability state or automatically a physical energy store. In particular

    Tr[(H_B tensor I+I tensor H_C)chi]=0.

Correlation energy would need a separately specified interaction operator; it cannot be assigned by terminology.

Dephasing the full rho_ABC into its computational-basis diagonal preserves each excitation marginal and total N but gives a separable mixture. The coherent state returns with probability one under U; the dephased state returns to |100> with probability 11/27. Thus population/energy marginals alone do not preserve the future. Dephasing can change information even when H0 does not change.

## 6. Primitive-edge transport and non-signalling

Provide an unexcited auxiliary register D at the source Cell and E at a native neighbor c+/-e_i. A ternary register cycle sends old B to E, old E to D and old D to B. It is an explicitly given reversible permutation conserving total excitation. For any rho_ABC with D,E initially zero, the E,C output equals the original B,C state, while B,D return to zero. It transfers rather than copies an unknown quantum state.

Each register crossing between Cells traverses exactly one signed native edge; the source Cell and target Cell remain occupied. Route and phase are declared initial relation data, not generated from a symmetric empty selector. This interface is not certified as TRIADIC_CLOSURE_E. For local layers, tracing operator support backward proves a finite native-step dependency cone, not a calibrated claim about physical light speed.

After separation, for any nonselective trace-preserving local operation E_B,

    Tr_B[(E_B tensor I)(rho_BC)]=rho_C.

Proof: write E_B(X)=sum K_mu X K_mu^dagger, use sum K_mu^dagger K_mu=I and cyclicity of partial trace on B [1]. Conditional postselected remote states can change, but their unconditioned local statistics cannot send a message. Residual transmission must not be described as a controllable energy/signal pulse sent instantaneously by a distant measurement.

## 7. Finite precision and executed checks

The specified matrices, state, entanglement witness and selected Bell probabilities use only finite integer/rational/Gaussian-rational algebra; no smooth limit is used. The restricted unmeasured U-orbit of the three basis states has exactly six states. Finite Hilbert dimension is nevertheless NOT a finite alphabet of all quantum states. Additional arbitrary gates or indefinitely many different overlapping interactions may grow exact coefficient complexity. No unrestricted fixed-finite-resolution quantum theory or measurement-device implementation is proved.

Executed with SymPy 1.14.0: 729 integer cross-block states; full 8x8 unitary/involution/excitation identities; six port permutations; the exact partial-transpose minor and CHSH value; all 16 measurement outcomes; 16 deterministic classical assignments; 7 trace-preserving channels times 2 sides times 16 matrix units =224 non-signalling identities; 24 residual-memory steps; 32 register-transport basis states; 12 signed native-neighbor routes (24 nonzero register-edge movements). Fresh-directory rerun output is byte-identical. This is reproducibility, not independent review or Lean verification.

A first checker draft compared unsimplified complex products structurally; replacing that check with exact simplification of the difference resolved it. No update or coefficient changed.

Checker: experiments/ns_dense_residual_d5c00d/check_dense_residual.py.
Run from repository root with SymPy available:

    python experiments/ns_dense_residual_d5c00d/check_dense_residual.py --output results_16.json

Next physical obligation: an independently justified native realization/measurement correspondence for joint coherent state and local conserved interactions under dense occupancy, or a falsifying constraint. Do not discard residual coordinates to obtain decay, and do not count the quantum assumptions already supplied as a derivation of quantum origin. The classical f=0 NS bridge remains a separate task.

## Primary references

[1] John Preskill, Quantum Information, Chapter 2 (July 2015), sections 2.1, 2.3-2.5, Caltech: https://www.preskill.caltech.edu/ph219/chap2_15.pdf
[2] Asher Peres, Separability Criterion for Density Matrices, PRL 77, 1413 (1996), DOI 10.1103/PhysRevLett.77.1413; arXiv:quant-ph/9604005.
[3] Clauser, Horne, Shimony, Holt, Proposed Experiment to Test Local Hidden-Variable Theories, PRL 23, 880 (1969), DOI 10.1103/PhysRevLett.23.880.
[4] Hensen et al., Experimental loophole-free violation of a Bell inequality using entangled electron spins separated by 1.3 km, arXiv:1508.05949; Nature 526, 682-686 (2015), DOI 10.1038/nature15759.

No historical novelty, primitive-force, world-foundation, physical f=0, NS, independent-review, or Lean-admission claim.
