# PREFIX-584-R2 — All-length closed native BRC trace symmetry from an exact phase anti-involution

Date: 2026-11-08 Asia/Shanghai. Author-side mathematical proof with finite exact structural certificate; UNREVIEWED / NOT_ADMITTED.
Scientific input fixed at awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d (no changes to P000).
Dependency: PREFIX-581's 126-coefficient exact fourth-cumulant polynomial; PREFIX-583-R2 exact quartic and marked-native axis stabilizer and closed trace enumeration for d<=12.

## Declared carrier and observation

Original native four STARs: S0=(1,3,6), S1=(1,4,5), S2=(2,3,5), S3=(2,4,6).
There are 48 signed phases i=(a,p,c), where a indexes a STAR, p and c belong to this STAR, have opposite signs and different absolute axis labels; and 96 states (i,u) with branch bit u∈{0,1}. From phase i=(a,p,c) the three successor phases j=(a,c,c') for the two allowed c' in the same STAR other than p, and the unique other STAR b containing |c| with its successor c'. Each original phase transition j is followed by an independent new branch bit v∈{0,1}; thus there are exactly 144 directed phase edges and 576 directed labeled native port actions.

An original action (i,u)->(j,v) has reward axis |c_i| (also |p_j|), and gate bit 1{u=v=1} 1{j=T}, where T=(0,+1,-3) is the unique distinguished gate target phase. These definitions are exactly the frozen native original 96-port observer.

For formal commuting variables x1,...,x6,z, define the 96x96 original labeled multivariate transition matrix
    A(x,z)[(i,u),(j,v)] = sum over corresponding original native actions x_|c_i| z^(1{u=v=1}1{j=T}).
Thus A(1,...,1,1) has row sum 6; the physical probability transition is A/6.

For each integer d>=1 define the original closed-path trace polynomial
    C_d(x,z) = tr(A(x,z)^d)
              = sum over all cyclic length-d ORIGINAL labeled 96-port paths
                    x1^R1 ... x6^R6 z^K.
Every integer coefficient is an exact labeled path multiplicity.

Set α=(1 3)(2 4), fixing 5,6, and set β=(5 6), fixing 1,...,4. Both act on the six original reward variables; z is fixed.

## Exact phase anti-involution for α

For signed native axis t≠0 set
    f(t) = -sgn(t) α(|t|).
For a phase i=(a,p,c), define
    Θ(i) = (a',f(c),f(p)),
where a' is the unique STAR containing |f(p)| and |f(c)|.

The companion structural checker exhaustively confirms on the frozen original carrier:
1. Θ is a well-defined involutive bijection of all 48 original phases.
2. Θ(T)=T.
3. For every original directed phase edge i->j, the reversed edge Θ(j)->Θ(i) is original and
       |c_{Θ(j)}| = α(|c_i|).
   All 144 distinct phase edges are checked. The phase map is provided in the JSON evidence.
Thus reversing a cyclic PHASE path and applying Θ is a length-preserving involution that transforms each source-axis count by α. It maps each original cyclic phase path into a unique original cyclic phase path. This phase-only construction does not assert an automorphism of the original marked 96-port graph.

## All-length gate retention after exact branch summation

Let t_k=1{i_k=T} for a cyclic original phase path (i0,i1,...,id=i0). At an original step i_{k-1}->i_k, the branch-bit weight is
    z^(t_k b_{k-1}b_k).
Introduce the 2x2 symmetric formal matrix
    M_t(z) = [[1,1],[1,z^t]]     (t=0 or 1).
Summing all cyclic branch-bit sequences b0,...,bd=b0, exactly over the allowed labeled original native actions, gives
    W(i0,...,id) = tr(M_{t1}(z) M_{t2}(z) ... M_{td}(z)).
This identity is a finite distributive expansion: each matrix index is an original source/target branch bit. No stochastic, numerical or asymptotic approximation is used.

Reverse the phase path and apply Θ. Because Θ(T)=T, the new ordered target-visit indicators are
    (t_{d-1}, t_{d-2}, ..., t_1, t_0),
a cyclic rotation of the reverse of the original list (t1,...,t_{d-1},t0).
For any symmetric matrices M_t, trace is invariant under cyclic rotation and reversal:
    tr(M_1 ... M_d) = tr((M_1 ... M_d)^T)
                    = tr(M_d ... M_1).
Therefore the exact summed branch/gate polynomial W is identical for each paired phase cycle, for every length d>=1 and for symbolic z.

## THEOREM 584.1 — Original closed trace invariant at EVERY length

For all d≥1, as an identity of integer polynomials in the seven independent formal commuting variables,

    C_d(x1,x2,x3,x4,x5,x6,z)
      = C_d(x3,x4,x1,x2,x5,x6,z).

Proof: pair each original cyclic phase walk with its Θ-reversed walk. The first part supplies the α permutation of all original axis rewards, preserving the path length and multiplicity of phase walk edges. The second part supplies equal symbolic branch/gate polynomial after summing all cyclic original branch-bit choices. The paired sums are identical term-for-term after applying α to the variables. Summing all original cyclic phases gives the asserted identity for arbitrary d. QED.

The prior 1≤d≤12 exhaustive integer DP is an independent finite check; the proof above is unbounded in d.

## THEOREM 584.2 — Exact characteristic polynomial and ALL-ORDER spectral stabilizer

Let χ(λ;x,z)=det(λI_96-A(x,z)). By Newton identities, the 96 characteristic-polynomial coefficients are uniquely determined over the rational function field Q(x1,...,x6,z) by the first 96 traces tr(A^d). Theorem 584.1 gives all these power sums exactly, hence

    χ(λ;x1,x2,x3,x4,x5,x6,z)
      = χ(λ;x3,x4,x1,x2,x5,x6,z)

as a formal polynomial identity. The same holds with A/6 in place of A.

For strictly positive real x_i,z, the Perron root of the original nonnegative irreducible weighted matrix is therefore invariant under α. Consequently the log-Perron spectral pressure and all its existing joint partial derivatives (all asymptotic cumulant rates of six original axes and gate) have exact α symmetry.

The β=(5 6) action has an independently constructed full marked-native 96-port isomorphism (PREFIX-583-R2); it preserves A by matrix permutation similarity with the corresponding variable relabeling. Thus the complete characteristic-polynomial / all-order spectral pressure axis stabilizer contains
    G4={id, β, α, αβ} ≅ C2×C2.

Conversely, any axis permutation preserving the complete characteristic polynomial as a polynomial in the original variables must preserve log-Perron pressure at positive weights and hence its exact fourth derivative at unity. PREFIX-583-R2 independently proves that the complete fourth-cumulant polynomial has no other axis permutations beyond G4. Therefore the exact full characteristic-polynomial stabilizer, with gate variable fixed, is *precisely*
    G_spectrum = G4, order 4.

## THEOREM 584.3 — Observer-dependent symmetry contrast

The marked-original 96-port native axis-automorphism group is only
    G_native={id,β} ≅ C2,
because all three gate edges have source axis 1, preventing α as a marked native graph automorphism. Meanwhile the complete original closed-cycle trace and all-order spectral group is
    G_spectrum={id,β,α,αβ} ≅ C2×C2.

This distinction persists despite a direct finite-open-path failure of α: starting from the exact uniform 96-port distribution and taking one uniform native step,
    Cov(R1(1), K(1)) = 5/1152,
    Cov(R3(1), K(1)) = -1/1152.
The first moments remain axis symmetric; the two-variable second cumulant already sees the difference. Thus cyclic/all-order spectral invariance is a strictly coarser observer symmetry, and retaining native branch and gate provenance matters.

## Certificate and continuation

Executable standard-library structural certificate: PREFIX584_R2_all_length_trace_involution_certificate.py.
Actual original finite checks: 48-phase involution, 144 reversed native phase edges, unique gate target fixed; all 576 labeled port transitions remain in the underlying frozen model. The formal two-by-two transfer trace argument is proved symbolically above; the certificate additionally checks cyclic/transpose trace equality for every binary gate-visit word of lengths 1..10 at z∈{0,2,7} as regression, not as the universal proof.
Machine evidence: PREFIX584_R2_all_length_trace_involution_results.json. Earlier exact original 96-port DP evidence depths 1..12: PREFIX583_R2_finite_trace_scan.py plus its JSON.

BRC reuse status REUSE_EXECUTED; carrier is all 96 original ports, six labeled original axis rewards, branch bit and gate; no hidden native state or source is quotiented in the scientific input. The reduction is **only** the declared cyclic trace observer after exact branch summation.

Next useful question: characterize which opening/endpoint boundary vectors yield finite-depth generating functions invariant under α; construct a minimal endpoint repair coordinate or exact boundary correction when open-path symmetry fails. The parity/branch transfer representation gives a direct route without a 96-state floating-point solver. A complementary question is to find a direct finite-dimensional intertwining or transpose conjugacy certifying χ symmetry.

Researcher role: author-side math; own native Researcher-ID/CLAIM/Result and independent Driver review are not established due to STATUS_DATABASE_UNAVAILABLE. PR is Draft for review, not mathematical admission.
