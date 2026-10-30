# EC49BZ — Exact signed-X6 BRC constant-term transfer, fast bit bound, and append-loss counterexample

Date: 2026-10-31. **Scientific status:** AUTHOR_ANALYTIC_PROOF / EXACT_SMALL_PACKED_AUDIT_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED. Author-side mathematics, not an admitted native Result, independent review, or physical heartbeat claim.

## Pinned sources and assumptions

- GLOBAL_KNOWLEDGE_V1 canonical main: 4614eab22d3f6e27e4088bc142d68ff00093b3ab. The bootstrap, operating manual, ACTIVE worldview, mathematics/code/BRC research policies, Enterprise Math project route and activity rules were read under that snapshot.
- Enterprise Math canonical main: 92ea1758627b6620538af4acadc1163fd56ef6d8. Native P000 V5, HEARTBEAT_WORLD signed-X6, joint-observer-preservation, portable and autonomous research protocols were read. P000/ACTIVE worldview are unchanged.
- Prior EC49BY author-side frontier: 22ad2e33df57ab9c7e07542c7e7f27c69b0c7564, same draft PR #1730.
- Verified unchanged native kernel signed_brc.py: Git blob 300a96e3dc24bf6fff73743037a0347a8bc83176, available in the preceding EC49BV/EC49BY evidence package. The published EC49BZ checker expects it in source/signed_brc.py.
- Scope is combinatorial **ordered signed six-axis X6 paths**, positive rational step weights, finite sign-preserving axis-permutation group H, deterministic automaton A; no lower-dimensional native plane, time evolution, amplitude cancellation, or energy inference.

Define Σ={+E_i,-E_i: 1≤i≤6}. Each signed native step a has relative displacement d(a)=±e_i∈Z^6, not a final Cell address. Fix H≤S₆, h=|H|, complete DFA A=(Q,δ,q₀), and common integer weight denominator D with positive integers c_a=D w_a, C=max_a c_a, ℓ=max(1,ceil(log₂(C+1))). For source word p, preserve its joint automaton state Φ(p)=(δ*(q₀,kp))_(k∈H) ∈Q^H, and define U_g(p)=product of c_(g a) along p. Write d₀=|Q|^h. The native closed-return selected numerator is

F_g(n,φ)=Σ_{p∈Σ^n, sum d(a)=0, Φ(p)=φ} U_g(p),

and its rational value is F_g(n,φ)/D^n. All Boolean terminal-automaton selectors correspond to sums over exact φ-atoms. Group weight instruments stay fixed during the observed path permutation.

## Theorem 1 — Exact native six-dimensional coefficient/constant-term representation

Let u=(1,1,1,1,1,1) and α(a)=u+d(a)∈{0,1,2}^6. For g∈H define the d₀×d₀ polynomial transition matrix

T_g(y)[φ,ψ] = Σ_{a∈Σ: δ_H(φ,a)=ψ} c_(g a) y^α(a),

with δ_H((q_k),a)=(δ(q_k,k a))_k and y^β=∏_(i=1)^6 y_i^(β_i). Then, **for every n≥0**,

F_g(n,ψ) = [y₁^n y₂^n y₃^n y₄^n y₅^n y₆^n] (e_(q₀,...,q₀) T_g(y)^n)_ψ.

**Proof.** Expanding the matrix product enumerates every ordered native word exactly once with its unique deterministic joint-state trace and the product of the prescribed group-channel weights. Its monomial exponent is Σ α(a)=n u+Σ d(a). The selected coefficient therefore counts precisely zero-displacement words ending in ψ with their signed-step source multiplicity and positive weights. Summing over ψ removes all filter restrictions, giving unchanged native signed_brc.endpoint_weight(n,0,w⁺,w⁻); setting every c_a=D=1 gives native endpoint_multiplicity(n,0). Odd-length return is zero. This is an exact combinatorial identity, and does not equate spatial return with complete event return. QED.

## Theorem 2 — Exact carry-free Kronecker encoding and a faster bit-operation upper bound

Fix target n≥1; choose R=2n+1, κ(β)=Σ_(i=1)^6 β_i R^(i-1), b=ceil(n log₂(12C))+2 and B=2^b. For polynomial P over nonnegative integer coefficients and exponents within [0,2n]^6, define K(P)=Σ_β P_β B^κ(β). Matrix powers T_g^t with t≤n have each exponent coordinate in [0,2t]. Every intermediate multiplication in binary powering has combined step length t≤n. Thus κ(β+γ)=κ(β)+κ(γ) without base-R exponent carry. Furthermore, all coefficients of any product entry are at most 12^t C^t≤(12C)^n<B: each monomial sums positive products from at most 12^t ordered words. Consequently **there is no base-B coefficient carry**, even after summation over intermediate DFA matrix indices, and

K((T_g^r)(T_g^s)) = K(T_g^r) K(T_g^s)

entrywise with the appropriate matrix multiplication, whenever r+s≤n. The target coefficient is read exactly as the base-B digit at position κ(nu). Positivity of the integer path weights is essential for this specific carry proof.

Every packed integer contains at most L=b(2n+1)^6=O(n^7(ℓ+1)) bits. Binary matrix powering across h channels takes O(h d₀³ log(n+1)) integer multiplications of ≤L-bit operands, plus O(h d₀³ log(n+1)L) bit operations for additions. For M(L), the bit cost of L-bit integer multiplication,

**T(n)=O(h d₀³ log(n+1)[M(L)+L]).**

The published Harvey–van der Hoeven bound M(L)=O(L log L) gives

**T(n)=O(h d₀³ n^7(ℓ+1) log(n+1) log(n(ℓ+1)+2)).**

For fixed H,Q and fixed positive integer numerator weights this is **O(n^7 (log n)^2)** bit operations, an asymptotically smaller upper bound than EC49BY's proved O(n^8) grade-school displacement-DP bound in the same fixed-parameter regime. Dense matrix storage costs O(d₀² L) bits per channel, **excluding multiplication-subroutine workspace**; the giant-integer algorithm may be less practical than sparse DP at moderate lengths. This is a valid existence bound assuming the stated fast arithmetic subroutine, **not a measured runtime claim or a lower bound**. For n=0 the result is the identity transition. QED.

External algorithmic reference (not claimed as a new integer-multiplication discovery): David Harvey and Joris van der Hoeven, “Integer multiplication in time O(n log n),” Annals of Mathematics 193 (2021), 563–617, DOI 10.4007/annals.2021.193.2.4, https://annals.math.princeton.edu/2021/193-2/p04 . Transfer matrices, coefficient extraction and Kronecker substitution are established computational ideas; the contribution here is a type-checked native-X6 BRC bridge and an explicit observer-preservation boundary.

## Theorem 3 — An exact counterexample to future-append sufficiency of terminal Boolean atoms

Take H={id,(E₁ E₂)}, w⁺=(2,3,3,2,1,1), w⁻=(1,1,1,1,1,1). The three-state DFA detects ordered substring A=(+E₁,+E₂) and its swapped detector detects B=(+E₂,+E₁); the final atom is two acceptance bits. Consider closed two-step source words

p=(+E₁,-E₁),     q=(-E₁,+E₁).

Both have endpoint zero, terminal acceptance atom 00, fixed-instrument group-channel weights (2,3), and source count one. Thus singleton bags {p} and {q} agree in **all** current four-atom outputs in both channels, as well as count and endpoint.

Append exactly the same **closed** suffix s=(+E₂,-E₂). Both extended sources remain closed and have identical group weight vector (6,6). Yet p·s has terminal atom 00 while q·s has atom 10: q·s develops substring (+E₁,+E₂) across the boundary. Thus the A-filtered future BRC readout is 0 for one bag and 6 for the other. This proves that the terminal Boolean-atom mass readout is not sufficient for arbitrary future append/filter compositions, even when total weight, path count and endpoint are included. The **full joint transition state** distinguishes the original prefixes ((0,0) versus (1,0)); retaining a transition-state/displacement distribution repairs this loss for the declared DFA future operations. No claim is made for arbitrary additional unmodeled detectors. QED.

## Reproducibility: executed evidence versus all-n argument

The adjacent **VERIFY_EC49BZ_MIN.py** is precisely the executed Python integer checker. With unchanged native signed_brc.py in source/, it tests polynomial matrix Kronecker packing on all four final Boolean atoms and both H channels at n=0,2,4 against independent signed-step displacement/DFA dynamic programming. It additionally verifies the DP aggregates against the native endpoint_weight and endpoint_multiplicity at n=0,2,4,6,8. **Packed powering at n=6 and n=8 was not executed.** The two-word future-append counterexample is checked using exact signed steps, deterministic state transitions and integer weights.

Exact unfiltered results (n : weighted total / count): 0:1/1; 2:24/12; 4:1560/396; 6:152640/19920; 8:18921000/1281420.

At n=4 the atom weights (each H channel) are 00=1488, 01=36, 10=36, 11=0; corresponding counts are 384,6,6,0. At n=8 DP weights are 16560120,1129320,1129320,102240 and counts 1170120,53850,53850,3600 (atoms 00,01,10,11). Two full checker executions produced byte-identical JSON and stdout, SHA256 fa8a8e50c83cf905b92d3015d4f10390ab799754ecd82605d67f36339b4e1ba9. The analytical proof, not these finite checks, establishes the all-n identity and bound. No native physical heartbeat evolution was run.

**Evidence files:** VERIFY_EC49BZ_MIN.py (executed source); EXACT_REPORT_EC49BZ.json (byte-exact local report); prior unchanged native kernel Git blob 300a96e3dc24bf6fff73743037a0347a8bc83176. Reproduce with Python 3.10+ from this directory, using the pinned native kernel at source/signed_brc.py. The original fuller proof and longer checker remain available in the current author-side evidence package.

## Control state and exact next unit

At this run's service observation, em_status exposed research_authority_granted=false and CODE_REVIEW_REQUIRED, and a read-only em_control_tasks owner lookup returned CONTROL_QUOTA. The current winning formal Task owner was not independently established. This PR material is **portable author-side mathematics**; it grants neither Source research activity, CLAIM/Result, independent Driver review, P000 modification nor admission.

**EC49CA successor:** Build a modular/CRT or block-convolution constant-term algorithm that reduces the massive packed operands while preserving all six native signed displacements and source DFA transition-state semantics. State an exact coefficient bound and no-alias proof; validate the four-atom outputs at n=4, then n=6, and distinguish theoretical bit bounds from measured resource use. Preserve original signed-BRC weights, source group action, future-append distinction and native endpoint fidelity.
