# PREFIX-597-R2 — Instantaneous 48-state BRC decoder and optimal four-coordinate gate repair

Date: 2026-11-08. Status: exact author-side proof and native integer/polynomial certificate; independent Driver review pending.
Source pin: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Verified predecessors: PREFIX-587 phase inverse; PREFIX-595 49-state positive model; PREFIX-596 48-state positive tail (PR #1805, commit c5a6a6c21a8551c1f60f85de0b9e8e9e1ff5f54f).
Current researcher: EM-DIRECT-A9F022; native activity RA-BB6445D786B142A6E5EC58D2. No formal Task CLAIM.
Mother question: exact, minimal state for full original 96-port linear BRC observations under nonstationary typed transitions.

## Original native model

Retain the four original STAR triples ((1,3,6),(1,4,5),(2,3,5),(2,4,6)), the 48 enumerated phases (a,p,c), 96 bit ports, six original axis labels and all three marked gate edges. Write S for the original 48x48 phase adjacency (three successors per phase), A(x,z) for the 96x96 native weighted transition with axis weights x1,...,x6 and marked gate multiplier z. Parameters may vary at each step; the positive domain is xa>=0,z>=0.

Let g=IX[(0,1,-3)]=4; its three predecessor phases H={3,14,15}. Define phase reversal rho(a,p,c)=(a,c,p), and h=rho(g)=2. The four distinct phases {2,3,14,15} all have original current axis 1, and g is not its own successor.

C:Q^96->Q^48 sums each unmarked phase's two bit ports and selects the first marked-g bit. E:Q^48->Q^96 embeds each ordinary phase coordinate into its first bit and embeds the marked coordinate into both marked bits. Then CE=I48. PREFIX-596 establishes Q(x,z)=C A(x,z) E and a 48-state evolution v_t=Q(x_t,z_t)v_(t-1) from the second native step onward; v1=C A(x1,z1)r0.

## Theorem 597.1 — complete 96-port readout from v_t and z_t alone

Define the four-supported integer functional

    L(v) = v[3]+v[14]+v[15]-2*v[2].

For every t>=2, every nonnegative original 96-port r0, and every time-varying nonnegative weight sequence, put

    delta_t = (z_t-1)*L(v_t) / (3*(z_t+3)).

The complete original native port vector at time t is recovered, using only v_t and the current gate parameter z_t, by

    r[t,g,0] = r[t,g,1] = v_t[g];
    r[t,i,0] = (v_t[i] - 1_{i in H}*delta_t)/2;
    r[t,i,1] = (v_t[i] + 1_{i in H}*delta_t)/2,  i!=g.

Let D_z be the corresponding 96x48 rational decoder. Then, as exact matrix identities,

    A(x,z) E = D_z Q(x,z)    and    C D_z=I48

for all xa>=0,z>=0. The identity is algebraically valid for arbitrary rational/formal xa,z except z=-3, with denominators cleared. In particular, no strictly positive axis hypothesis is needed; z=0 and any zero axis weights are included.

Proof: The only native port-bit difference in any output is at i in H: the two bit rows there differ by x1(z-1) times the previous marked *second* bit. All other output bit pairs agree (including g, since g not in N(g)). After the first step, the previous marked bits are equal, so their shared value is v_(t-1)[g]. Thus the common discrepancy at the three i in H is delta_t=x_(t,1)(z_t-1)v_(t-1)[g], and all port reconstruction equations follow from the known phase sums.

The exact combinatorial inverse from PREFIX-587 is 3*S^{-1}=S^T-2*R, R being the native phase-reversal permutation. Its g-th row has coefficient +1 at H, -2 at h, and zero elsewhere. With ell=e3+e14+e15-2e2 this yields ell^T S=3 e_g^T.

PREFIX-596's exact 48-state factorization is Q=diag(x_axis(i)) Drow S Dcol(z), with Drow(g)=1, Drow(i)=2 otherwise, Dcol(g)=(z+3)/2 and all other Dcol diagonal entries 1. The four indices in supp(ell) are different from g and have axis=1. Consequently

    ell^T Q = 2*x1*ell^T S Dcol(z)
            = 3*x1*(z+3)*e_g^T.

Therefore L(v_t)=3*x_(t,1)*(z_t+3)*v_(t-1)[g]. Eliminate v_(t-1)[g] from the discrepancy equation, obtaining exactly the zero-history delta formula. No division by x1 occurs. Substitution in the original typed port actions gives A E=D_z Q; direct addition of bit pairs gives C D_z=I. QED.

For integer native input and integer x,z>=0 the reachable states satisfy the exact integer checks

    3*(z_t+3) divides (z_t-1)*L(v_t);
    v_t[i] == 1_{i in H}*delta_t (mod 2), i!=g.

All 96 reconstructed port entries are nonnegative integers for reachable nonnegative native states.

## Theorem 597.2 — four-coordinate repair is optimal in this basis

When every xa>0 and z>=0,z!=1, PREFIX-596 proves

    det Q=2^46*3^12*(z+3)*product_a xa^8 != 0.

The linear discrepancy functional on the complete 48-dimensional state space must be x1(z-1)*e_g^T Q^{-1}. Theorem 597.1 gives its unique expression as (z-1)*L/[3(z+3)]. All four coefficients of L are nonzero when z!=1. Therefore *every linear memoryless discrepancy readout from the fixed 48 coordinates* must inspect four coordinates, with exact support {2,3,14,15}. z=1 is a special case with zero discrepancy; zero axis weights retain the valid decoder but are outside this generic uniqueness proof.

The first step with arbitrary original gate bits retains the known rank-49 phenomenon. Hence the instantaneous 48-state formula starts at t=2 unless the initial gate pair is already equal. This is a statement about full port-linear observation, not a claim that finer ordered-path or provenance observers factor automatically.

## Exact executed verification

The companion standalone Python certificate reconstructs the frozen original 576 labeled actions from the four STAR triples; it never replaces native BRC semantics with a generic untyped walker. It certifies

    6*(z+3) A(x,z) E = Dnum(z) Q(x,z)

for the six axis-weight unit vectors, z=0,1,2 and all 48 tail basis vectors. Both sides are linear in x and polynomial in z of degree <=2, so the 864 exact integer checks give full coefficient verification, not sampling. The same 864 probes verify the row identity L(Qv)=3*x1*(z+3)*v[g].

Independent original 96-port integer propagation checks 120 input families (including all 96 standard basis inputs), six nine-step varying-weight sequences including zero axis weights and nonunit/zero gates, 5,760 exact later-step 96-port reconstructions and 270,720 parity checks. A first-step unequal-gate-bit input gives an explicit boundary counterexample to using D_z immediately. All assertions passed locally.

**New capability:** a stored positive 48-state snapshot plus its contemporary gate z suffices to recover all 96 current original port values. The prior PREFIX-596 reconstruction read the *previous* 48-state vector and all current axis weights. The four-coordinate correction is optimal for linear memoryless gate-discrepancy recovery in the declared coordinates. This is a state-observer/interface improvement; full runtime cost must also count initial conversion, sparse factorized native baseline, materialization, integer bit lengths and query workload.

## Next science units

1. Benchmark original 96-port phase-factorized propagation against 48-state Q evolution with (a) previous-step O-readout and (b) instantaneous D_z snapshot readout. Count transformations, output schedule, memory traffic and integer bit lengths.
2. Characterize the reachable 48-state integer lattice: mod-2 plus 3(z+3) divisibility are necessary; test sufficiency with a lattice basis or explicit counterexample.
3. Test preservation of additional typed path/provenance-sensitive observers separately, adding exact repair coordinates when endpoint state is insufficient.

P000 and frozen science unchanged. Author-side proof, program and result have not received independent Driver/Native Result acceptance.
