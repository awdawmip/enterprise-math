# R250 — finite-holonomy affine BRC full-histogram equivalence and depth-3 obstruction

**Date** 2026-10-24. **Status** Author-side exact theorem + positive-BRC finite counterexample; not a native X6 heartbeat theorem, accepted Result, or independent Driver review.

## Frozen provenance and actual BRC contract

GLOBAL_KNOWLEDGE_V1 canonical main@8c3a10ae0032906c833ede6630404e39d334e253; P000 ACTIVE_LOCKED original blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c, projection matches. Enterprise Math Source main@c7fb90fd7ec451a954b553b963dd85d4ec99fc96. Reuse existing source brc_transport.py blob be1debe367263931bd5e93fd750be3ed54624fe1 and brc_control_port.py blob 44def6b8ac787e798d3cc2c6be16f873f91b9db8. Exact interface semantics: positive rational weights, positive integer branch multiplicities, alternatives sum, source-defined Affine.then is later-after-first six-dimensional affine composition, and ControlPacket.then serially composes matching time ports. Interface law REUSE_APPLIED, native Python module not executed.

R249 (draft commit 11f444afa2aa1f793f2137251d82857f039708d1) proved a bound n−1 for translation-only full joint weight/effect histograms by a commutative Laurent fraction field. R250 allows a finite, nontrivial six-dimensional integral linear symmetry group.

## Theorem R250.1 (finite linear holonomy)

Let S be n≥1 finite nonspatial control states; Σ a finite alphabet of reusable positive-BRC packets with finitely many edges, weights w∈Q_{>0}, counts k∈Z_{>0}; H≤GL_6(Z) any *finite* group of order m; all edge effects x↦hx+v with h∈H,v∈Z^6. Fix π:S→C. For an initial state s and word u, let ℋ_s(u) be the exact coalesced positive histogram by (π(final state), product of individual rational path weights, exact composed affine map). Positive integer path multiplicities are summed only for identical joint keys. The observer does not record original path identities or hidden terminal states.

**Claim:**
ℋ_s(u)=ℋ_t(u) for every finite u∈Σ*
if and only if
ℋ_s(u)=ℋ_t(u) for every u with |u|≤nm−1.

The reachable translation/effect support may be infinite, so this extends R248's finite-key sufficient condition; m=1 recovers R249.

**Proof (fully algebraic).** Let G=Z^6⋊H under ordinary function composition, so (v,h)(w,k)=(v+hw,hk). Introduce independent Laurent variables X_1,...,X_6 and e_g (g∈H). Define D_v e_g=X^{gv}e_g and P_h e_g=e_{g h^{-1}}. Then P_hD_vP_h^{-1}=D_{hw}, with w=v, so ρ(v,h)=D_vP_h is a group representation by m×m monomial matrices over the Laurent ring. This group-algebra representation is *faithful*: in column e_identity, different h occupy different output rows h^{-1}; for a fixed h, distinct v occupy distinct monomials X^{h^{-1}v}. Therefore any finite linear combination of distinct (v,h) that yields the zero matrix has every coefficient zero.

BRC's chronological effect product is first F, then L, meaning L∘F, so use Ψ(F)=ρ(F^{-1}); now Ψ(F.then(L))=Ψ(F)Ψ(L). Let P be the finite set of primes in numerators/denominators of all input rational weights. Use independent Y_p variables and valuation monomials Y^{ν(w)}. Products of positive rational weights become products of Y-monomials; uniqueness of valuations, together with faithfulness of ρ and independence of X variables, means Σ c_{w,F}Y^{ν(w)}Ψ(F)=0 iff *every* original joint-key signed comparison coefficient c_{w,F}=0. Signed coefficients occur only in the mathematical difference of two positive histograms, never as a BRC physical branch.

Work over the commutative fraction field K=Q(X_1,...,X_6,Y_p:p∈P). For each BRC packet letter a, build N_a∈Mat_{nm}(K) with (s,t)-block Σ_{edges s→t} count·Y^{ν(weight)}Ψ(effect). Packet alternatives are block addition and chronological .then is matrix multiplication. Each complete terminal class observation is read by β_{c,j}=(Σ_{q:π(q)=c}e_q)⊗e_j, for j=1,...,m; compare starts with α_i=(e_s−e_t)⊗e_i^T, for i=1,...,m. All declared full histograms agree on a word u iff α_i N_u β_{c,j}=0 for every i,j,c.

For each fixed i, let W_k=span_K{α_i N_u: |u|≤k}⊂K^{nm}. If W_{k+1}=W_k, W_k is stable under right-multiplication by every N_a and hence under all future words. Otherwise its dimension increases strictly; since dim W_0≤1 and ambient dimension is nm, it has stabilized by k=nm−1. Thus every observable difference at any depth is implied by an observable difference at depth at most nm−1. Repeat for i=1,...,m. The converse is immediate. □

This establishes a finite *depth* certificate, not an arithmetic bit-complexity or native six-axis physical legality assertion.

## Theorem R250.2 (small positive-BRC obstruction to the n−1 extension)

Take n=3, Σ={a}, and the integral orientation-preserving six-coordinate affine maps
T_k(x_1,x_2,x_3,...,x_6)=(x_1+k,x_2,x_3,...,x_6)
and
R_k(x_1,x_2,x_3,...,x_6)=(-x_1+k,-x_2,x_3,...,x_6).
Their linear subgroup H={I,diag(-1,-1,1,1,1,1)} has order 2 (no native heartbeat rotation admissibility claim). Put A=R_{−1}, B=T_{−1}, C=T_{+1}, R=R_0. All six edges of the one-letter packet have weight=1 and multiplicity=1:

state 0 → (state 2,A) or (state 2,B);
state 1 → (state 0,A) or (state 0,B);
state 2 → (state 1,C) or (state 2,B).

Merge all three terminal control labels in π, and compare initial states 0 and 1. The zero- and one-letter observed histograms agree. At two letters,
ℋ_0(a²)=(A+B)(C+B)=R_0+R_{−2}+I+T_{−2}
and
ℋ_1(a²)=(A+B)²=I+R_{−2}+R_0+T_{−2}.
These are equal complete joint-effect histograms (not just equal total mass).

At three letters, the hidden terminal state distribution changes the continuation:
ℋ_0(a³)=(A+B)[C(A+B)+B(C+B)],
ℋ_1(a³)=(A+B)²(C+B).
Their signed mathematical comparison simplifies to
**ℋ_0(a³)−ℋ_1(a³)=R_{−1}+T_{−1}−T_{+1}−R_{+1}≠0.**
For example, T_{+1} has count 0 from state 0 and count 1 from state 1. Hence the shortest distinguishing word has length exactly **3**, strictly greater than R249's translation-only n−1=2, while within the safe R250 bound nm−1=5. □

The mechanism is the exact zero-divisor identity (A+B)(C−A)=0 in the *signed external comparison group algebra*. Both factors are nonzero. This does not imply signed BRC branches or physical destructive interference; both packet inputs are positive. It explains why replacing R249's commutative Laurent field with an arbitrary affine group algebra and keeping n−1 is invalid.

## Author-side validation and boundaries

Python author-side exact direct six-axis affine-effect path propagation and faithful 2×2 Laurent-matrix encoding agreed for each of 3 start states and depths 0...8 (27 separate observations); 100 ordered effect pairs verified order preservation. Independent C++17 exact positive-multiplicity dynamic programming checked the same explicit witness through depth 8. The two-edge packet has 2^k paths per source at depth k. Shortest distinguishing length 3. Universal bound is proven in the algebraic argument, not inferred from finite testing. Native enterprise_math package wasn't imported in this turn.

The full native Source interface can encode these six effects, but their permitted physical update status, branch IDs/provenance, R193 original path correspondence, and heartbeat time calibration remain independently unproved. Current direct native control tasks lookup returned CONTROL_QUOTA; native Researcher session creation returned STATIC_READONLY_SCOPE_DENIED with operation_sent=false. Active owner/CLAIM not verified, and this draft does not create a native Task, Result or accepted Foundation theorem. No Google Drive permission bypass.

## R251 next discriminating unit

Compute the exact stabilized K-row-span rank and shortest distinguishing filter for this three-state two-element H model. Then restrict to actually admissible native X6/BRC effect groups and run ControlPacket.from_edges/then/EffectHistogram with these precise edges in a pinned installed Source environment, comparing exact depth 0...3 histograms. Separately determine whether R193 original path provenance forces a strictly finer observer than the coalesced group-effect histogram. Any improved bound must state its observer, future alphabet and proof.

## Prior art / classification

The field-linear part is standard weighted-automata theory, see Stefan Kiefer (2020), Notes on Equivalence and Minimization of Weighted Automata, https://arxiv.org/abs/2009.01217. Monomial finite-group / semidirect-product representations are standard algebra. Here the contribution is their precisely typed positive BRC specialization and the explicit three-state obstruction; no unverified general originality claim is made.
