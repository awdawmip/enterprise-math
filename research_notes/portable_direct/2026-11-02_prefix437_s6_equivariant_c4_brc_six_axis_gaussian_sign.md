# PREFIX-437 — Full-S6 equivariant phase holonomy, all-six-axis BRC sign law, and a 64-state control carrier

Date: 2026-11-02. Research mode: portable direct. Evidence: author-side mathematical derivation with executed exact BRC tests; UNREVIEWED / NOT_ADMITTED / NATIVE_CLAIM_ABSENT.

## Sources and fixed scope

The scientific input remains frozen at enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d. This work follows PREFIX-436 at c4d450536bf71ed87fd74555295ec60485262f0a. The current project control read was main@1656181794935bb191381ba4b51a7941e80ffdca, with P000, the Heartbeat World X6 definition, joint-observer preservation, the active residual world position, the portable-research and BRC-only arithmetic protocols, and the typed BRC source files. The global account policy snapshot was main@8916715838c5cf6433a62b7890f476f8ba46a04e.

The six native signed axes are the P000 X6 spatial Cell torsor; x in Z^6 denotes a chosen chart relative to an actual Cell. Control and phase states introduced below are non-spatial auxiliary types. Step counts do not assert physical heartbeat times. The native positive shortest-path BRC source used in executed checks was experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py, Git blob 300a96e3dc24bf6fff73743037a0347a8bc83176. The code verified this exact blob before import. The current source-level typed ports inspected were src/enterprise_math/brc_control_port.py and src/enterprise_math/brc_transport.py.

Mother research question: can X6 ordered native paths, typed BRC control effects and prospective phase/Port observers be joined without erasing relevant branch information? This unit determines the consequences of additionally requiring an honest full S6 axis-permutation symmetry, builds a compatible phase sidecar and tests its exact signed-X6 shortest-path observations.

## Theorem A — C4 central commutators under honest S6 lifts

Let 1 -> C4 -> G -> Z^6 -> 1 be any central group extension. Suppose every pi in S6 lifts to an automorphism inducing pi on the Z^6 quotient and inducing a homomorphism chi:S6 -> Aut(C4)={+1,-1} on the center. Let B(d,e) be the commutator of lifts, valued in C4=Z/4Z. Then there exists b in {0,2} such that B(e_i,e_j)=b for every ordered pair i != j. Both b=0 and b=2 occur.

Proof. The commutator on a central extension of an abelian group is alternating and biadditive. All even permutations fix C4 because their image under any homomorphism S6 -> C2 is trivial. For i != j, choose k,l disjoint from i,j. The even double transposition (i j)(k l) interchanges e_i and e_j and fixes the center. Thus B(e_i,e_j)=B(e_j,e_i)=-B(e_i,e_j), giving 2B(e_i,e_j)=0 mod4. A6 acts transitively on ordered distinct-axis pairs, since any parity correction can exchange two unused axes. Consequently all off-diagonal entries are the same b in {0,2}. The direct product realizes b=0. The cocycle in Theorem B realizes b=2 and admits an honest full S6 lift. QED.

This classifies the commutator/plaquette flux under the stated full-symmetry hypothesis; it is not a classification of arbitrary native field dynamics. In particular, PREFIX-436's odd C4 flux is a valid auxiliary oriented model when that extra symmetry is not required.

## Theorem B — Constructive full-S6 cocycle and explicit gauge intertwiner

For d,e in Z^6, define

    c(d,e) = 2 sum_{1<=i<j<=6} d_i e_j (mod 4),
    (d,t) star (e,s) = (d+e, t+s+c(d,e) mod 4).

Bilinearity proves the normalized cocycle condition and associativity; the commutator is c(d,e)-c(e,d). Every distinct-axis oriented elementary plaquette has tag 2 mod 4, namely sign -1. The center C4 remains present while loop commutators land in {0,2}.

For pi in S6, define Inv(pi)={(i,j):i<j,pi(i)>pi(j)} and

    f_pi(d)=2 sum_{(i,j) in Inv(pi)} d_i d_j (mod 4).

With (pi d)_{pi(i)}=d_i, set Phi_pi(d,t)=(pi d,t+f_pi(d)). These satisfy

    Phi_pi(g star h)=Phi_pi(g) star Phi_pi(h)
    Phi_pi Phi_sigma = Phi_{pi sigma}.

Proof. On each inversion pair, c(pi d,pi e)-c(d,e) equals 2(d_j e_i-d_i e_j), congruent modulo 4 to 2(d_j e_i+d_i e_j), which is the corresponding cross-term in f_pi(d+e)-f_pi(d)-f_pi(e). Thus Phi_pi is a homomorphism. For the composition law, the parity of an unordered pair's inversion under pi sigma is the sum modulo two of its inversions under sigma and under pi on the relabeled pair. Multiplication by 2 makes this identity exact in C4. QED. Changing the spatial chart alters the edge phases by an endpoint gauge; comparisons of coherent intensity for equal endpoints are chart independent.

## Theorem C — Exact coherent six-axis shortest-path BRC formula

Fix a chart Cell x in Z^6. For any signed legal primitive edge x -> x+sigma e_j, sigma in {+1,-1}, introduce the auxiliary phase tag

    theta(x,sigma e_j) = 2 sigma sum_{i<j} x_i (mod 4).

The reverse edge cancels its phase exactly. For d in Z^6, define m_i=|d_i|, n=sum_i m_i, and take all signed-native shortest path words using each axis i exactly m_i times with its fixed signed direction. Their existing native positive BRC count is

    B(d) = n! / product_i m_i!.

For a word w let N(w) count ordered pairs of its steps for which the earlier axis index is lower than the later axis index. Expanding theta along the actual intermediate Cells gives

    tau_x(w) = 2[sum_{i<j} x_i d_j + N(w)] (mod 4).

This also holds for negative native directions since the product of two signed unit steps is odd modulo 2. Define the exact integer sign-BRC amplitude E_x(d)=sum_w i^{tau_x(w)}, and intensity I(d)=|E_x(d)|^2. All summands are exactly +1 or -1. Let o(m) count odd entries among m_1,...,m_6. Then, FOR EVERY d in Z^6,

    E_x(d)=(-1)^[sum_{i<j} x_i d_j] A(m),

    A(m)=0, when o(m)>=2;
    A(m)= floor(n/2)! / product_i floor(m_i/2)!, when o(m)<=1.

Consequently I(d)=A(m)^2, independently of the chosen chart start.

Proof. For a two-letter shuffle, let G(n,a) denote the sum of (-1)^{number of first-letter-before-second-letter pairs} over every word containing a first letters and n-a second letters. The polynomial coefficient identity

    product_{j=0}^{n-1}(1+q^j t) = sum_a q^{a(a-1)/2} [n choose a]_q t^a

holds over Z[q,t], without division at roots of unity. At q=-1 each adjacent factor pair is (1+t)(1-t)=1-t^2, and a remaining factor is 1+t. Writing n=2N+r and a=2K+s with r,s in {0,1}, its coefficient is zero for s>r and otherwise (-1)^K binom(N,K). The prefactor (-1)^{a(a-1)/2}=(-1)^K cancels it. Therefore G(n,a)=0 precisely when n is even and a odd, and otherwise G(n,a)=binom(floor(n/2),floor(a/2)).

For six letters, first shuffle axis 1 with the fixed subword of axes 2,...,6, then recursively shuffle axis 2 with axes 3,...,6. The cross-axis pair signs factor, so the all-word signed sum is

    product_{j=1}^5 G(sum_{k=j}^6 m_k,m_j).

If at least two m_i are odd, select the second-to-last odd axis: the remaining total at that stage is even while its count is odd, forcing a zero factor. If at most one m_i is odd, every factor survives, and the binomial coefficients telescope to floor(n/2)! / product_i floor(m_i/2)!. The chart phase multiplies every word by the same sign. This proves the claimed amplitude and intensity for all signed displacements. QED.

Witnesses at x=0: m=(1,1,0,0,0,0) has BRC=2, phase histogram (1,0,1,0), amplitude=0, intensity=0. m=(1,1,1,1,0,0) has BRC=24, histogram (12,0,12,0), intensity=0. m=(2,2,0,0,0,0) has BRC=6, histogram (4,0,2,0), amplitude=2, intensity=4. m=(2,2,2,2,0,0) has BRC=2520, histogram (1272,0,1248,0), amplitude=24, intensity=576. For m=(1,1), PREFIX-436's odd-flux C4 construction instead gives intensity 2, a discriminating future observer test.

## Theorem D — Minimal 64-state deterministic sign-control carrier

For the specified sign-trace observation language of all legal signed-axis future words, let the auxiliary state comprise the first five native chart-position parities p_i=x_i mod2 and one sign bit t=tau/2 mod2. There are exactly 2^6=64 states (p_1,...,p_5,t). Every signed primitive edge sigma e_j has the same mod2 update:

    p_k' = p_k + indicator(k=j) mod2, for k<=5;
    t' = t + sum_{i<j} p_i mod2.

This recovers precisely the auxiliary edge theta and inverse cancellation for all 12 signed primitive edges, while retaining the native spatial translation x -> x+sigma e_j as a separate effect.

Minimality for the DECLARED deterministic observation language, with no separate parity oracle: two states with different t are distinguished at observation horizon zero. For equal t and different p vectors, choose the first differing bit k and append the legal step +e_{k+1}; the next sign differs because the preceding parities agree and p_k differs. Hence all 64 states are pairwise distinguishable with horizon <=1. Both t values are reachable at any selected Cell using a nontrivial elementary plaquette and its alternatives. Thus an exact deterministic state machine implementing this language requires at least 64 states.

The actual current source src/enterprise_math/brc_control_port.py::ControlPacket.deterministic supports 64 finite control states, with six-dimensional src/enterprise_math/brc_transport.py::Affine spatial effects. A 12-packet family, each with the displayed 64-state transition and translation by +/-e_j, is therefore expressible in that typed source interface. Current source also exposes packet then / alternatives and exact positive effect histograms. This establishes source-level REPRESENTABILITY; assembling and executing ControlPacket objects and demonstrating an original native X6 physical phase/Port actuation are the open implementation and scientific bridge.

## Actual verification, precise evidence, next research problem

The executed exact checker prefix437_equivariant_brc_certificate.py imports signed_brc.py from an earlier preserved evidence source, first checking the actual Git blob SHA 300a96e3dc24bf6fff73743037a0347a8bc83176. It used integer native signed-X6 positive BRC counts and a separately typed proposed C4-tag dynamic-programming extension. Checks passed: all 720 axis permutations for the lift homomorphism on finite signed test vectors, sampled permutation compositions, 64 selected cocycle triples; 2187 signed-X6 DP/chart-start cases (m_i in {0,1,2}); complete enumeration of 55,987 ordered words of length <=6 over six native axes; 2016 unordered pairs of 64 control states and their distinguishability, plus all 64x6 parity involutions. Exact finite checks supplement the all-scale mathematical proofs.

Provenance: full author-side proof/source/log and manifest are in the separately generated PREFIX437_COMPLETE_RESEARCH_EVIDENCE.tar.gz evidence bundle, SHA-256 6cf125e924b72e50ea6c228e07020ed9423cd79ff5d64377ebafab18f3d31647. This project's ordinary checkpoint contains proof/code/log; no native execution session or task completion was claimed. Native Sites connector reported static-machine-readonly (research_authority_granted=false), active owner query failed CONTROL_QUOTA, session start returned STATIC_READONLY_SCOPE_DENIED (operation_sent=false). GitHub identity was awdawmip (push/admin). Author-side / UNREVIEWED / NOT_ADMITTED.

PREFIX-438 next: actually construct and execute the 12 source-native ControlPacket objects on a shared 64-state control layout and compare their then/alternatives/evaluate semantics with the exact sign-BRC DP and branch-provenance needs; seek a permitted native Port probe distinguishing the odd-flux I=2 and even-flux I=0 predictions at the (1,1) witness. Four-phase tomography of PREFIX-435 still requires an additional admissible phase operator or weaker symmetry. Preserve the parent X6/typed-BRC bridge problem.
