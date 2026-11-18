# EC49BY — Exact bit-operation complexity of signed-X6 BRC filtered returns

**2026-10-31** · Status: AUTHOR_ANALYTIC_PROOF / EXACT_NATIVE_INTEGER_AUDIT_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED.

## Source and model

Fixed source snapshot GLOBAL_KNOWLEDGE_V1 main f5a8aabee2e1108f23a9ad441de31cec7b0c4524, and Enterprise Math main e4da8741fc91c6b584de6a61a9c8cd6b7ae1ed66. Read both account entries, project router, matching P000 projection and original (blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc), ACTIVE worldview, applicable BRC/math/code policies, project portable and autonomous-research protocols. The parent author branch is PR #1730, EC49BX at commit bf1a38f1ee3f142fb347d132328662c3828ab44f. The exact native kernel actually executed unchanged is signed_brc.py Git blob 300a96e3dc24bf6fff73743037a0347a8bc83176, restored from EC49BV preserved sources and verified locally with git hash-object.

Carrier is the six native signed spatial axes with twelve primitive steps Σ={±E_i : i=1,...,6}. Displacements are relative signed X6 integers, not complete Cell addresses. Ordered paths, their branch multiplicity, and per-step positive-rational weights are preserved. This is a **combinatorial signed-path BRC** result, not a theorem about a three-dimensional native slice, time dynamics, energy, amplitude cancellation, or physics.

## Theorem 1 — All-pairs DFA/group observer has a polynomial bit bound for fixed H,Q

Let H be a finite group of sign-preserving axis permutations, h=|H|, and A=(Q,δ,q0) a complete deterministic finite automaton, q=|Q|. Write each positive rational direction weight w_a=c_a/D with positive integer c_a and common denominator D. Let C=max(c_a) and ℓ=max(1,ceil(log₂(C+1))).

For an ordered native path p, define its endpoint d(p), the **joint source automaton state**

Φ(p)=(δ*(q0,k p))_(k∈H) in Q^H,

and transformed integer weight U_g(p)=∏_(a∈p)c_(g a), g∈H. For each φ∈Q^H and g∈H define

F(n,φ,g)=Σ_{p∈Σ^n, d(p)=0, Φ(p)=φ} U_g(p).

The filtered rational BRC output is F(n,φ,g)/D^n. Every Boolean selector on the joint automaton state is a sum of the F for selected φ. All these values can be computed in

**O(h q^h n^8 (ℓ+1)^2) bit operations and O(h q^h n^7 (ℓ+1)) bits of two-layer working memory**

using grade-school integer arithmetic. This is an exact **algorithmic upper bound**, not an assertion of computational optimality. The number of final scalar coordinates is at most h q^h, independent of n.

**Proof.** Initialize each channel g to 1 at spatial offset zero and state (q0)_(k∈H). At each time t and signed step a, perform

F_(t+1)(x+sgn(a)e_|a|, (δ(φ_k,k a))_(k∈H),g) += c_(g a) F_t(x,φ,g).

By induction each ordered path contributes its product exactly once to the unique displacement/joint-DFA state, retaining sign and multiplicity. At time n choose x=0. Removing DFA selectors and summing all final states is exactly the native endpoint_weight enumeration; with all weights 1 it is native endpoint_multiplicity.

At layer t the number of possible x is ≤(2t+1)^6, the number of joint DFA states is ≤q^h, and there are h channels. Thus at most 12 h q^h Σ_{t=0}^{n−1}(2t+1)^6 multiply/add transitions occur. Each nonnegative integer entry is bounded by (12C)^t because no more than 12^t words contribute, each product is ≤C^t. Consequently its bit length is at most B=bitlen((12C)^n)=O(n(ℓ+1)). Elementary multiplication by the at-most-ℓ-bit step coefficient costs O(Bℓ), and addition O(B). This proves the time bound; retaining consecutive time layers proves the space bound. These are proofs for all n, not extrapolations from computed n. QED.

This source state is sufficient **only** for declared selectors and future operations factoring through Φ and the stored orbit weights. It does not retain arbitrary path ID, omitted provenance or a newly introduced detector. Keeping a DFA accepting flag alone before future append is not necessarily sufficient; the full transition state matters.

## Theorem 2 — Explicit sparse bags have a different complexity envelope

For an explicitly supplied bag containing K signed words of common length n, positive integer multiplicities with total M≥1, evaluate each path in all h group channels, determine Φ, and add to a dictionary indexed by Φ. There are ≤min(K,q^h) nonempty buckets. Every exact integer output uses at most

B_sparse=O(n(ℓ+1)+log₂(M+1)) bits.

One valid schoolbook implementation runs in

**O(Kh[n²(ℓ+1)² + n(ℓ+1)log₂(M+1) + B_sparse]) bit operations,**

with output-bucket memory O(h min(K,q^h) B_sparse) bits, plus O(h min(K,q^h)log q) key bits and O(h n(ℓ+1)) evaluation scratch. Even reading the explicit data requires Ω(Kn) signed symbols. Sparse bags and the complete length-n closed-word population are distinct inputs.

**Proof.** A path product is n multiplications by ℓ-bit coefficients; its evolving numeral length is at most nℓ and elementary multiplication total O(n²ℓ²) per channel. Multiplication by a log(M+1)-bit bag multiplicity and addition to a B_sparse-bit bucket give the displayed costs. Since each path product is ≤C^n and all multiplicities sum to M, each bucket is ≤M C^n. QED.

The EC49BX observer's **minimal terminal rational-linear rank** is 8 (fixed instrument) and 4 (covariant) for every even n≥6 under its specific four-atom query language. That does *not* imply bounded bit size or bounded working DP state count. In the executed n=8 example, the terminal rank remains 8 but 82,634 displacement×joint-state entries existed in the final DP layer. This is not a lower bound for every algorithm.

## Theorem 3 — Unfiltered closed-return convolution is asymptotically cheaper than generic DFA DP

For the complete closed-word population without filters, reuse EC49BX's exact recurrence with q_i=c_(+i)c_(-i):

T_0(0)=1, T_0(m>0)=0,

T_j(m)=Σ_{k=0}^m binom(2m,2k) binom(2k,k) q_j^k T_(j−1)(m−k).

It yields native endpoint_weight(2m,0,w⁺,w⁻)=T_6(m)/D^(2m) exactly. Precomputing the integer Pascal table gives a conservative schoolbook upper bound of

**O(6 n^4(ℓ+1)^2) bit operations and O(n^3(ℓ+1)) working bits, n=2m.**

**Proof.** Each length-2m closed ordered path has k copies of +E_j and k copies of −E_j for the jth axis. Choosing 2k positions and then their k positive signs gives the displayed binomial factors and a bijection with the remaining shorter-axis closed word. There are O(6m²) summands over the full coefficient table. Factors are O(n(ℓ+1))-bit integers, and a fixed number of grade-school multiplications per term costs O(n²(ℓ+1)²); the Pascal table has O(n²) O(n)-bit entries. QED.

The scalar output has dimension one but, for all-unit weights, the expanded integer return C_n has Θ(n) bits: inject all (±E_i paired) m-loop choices to get 6^(n/2)≤C_n≤12^n. Coordinate rank, exact numeral bits, temporary working memory and arbitrary symbolic-compression length are **different resources**.

**Orbit-symmetry lemma:** for the full H-invariant set of closed words, Σ_p χ_w(gp)=Σ_p χ_w(p) because p→gp bijects the path population. This need not hold for a non-invariant source bag or selected fiber. Aggregate equality for one population is not a proof that all path-bag orbit-weight rows are proportional.

## Exact executed native-kernel evidence

The standalone VERIFY_EC49BY_MIN.py is the actually executed 2,285-byte verifier (its Git blob is checked against its local executed source). It imports unchanged native signed_brc.py from a sibling source/ directory. Model: H={identity, transposition E1↔E2}; w⁺=(2,3,3,2,1,1); w⁻=(1,1,1,1,1,1); complete three-state detector for ordered substring (+E1,+E2), and its swapped counterpart for (+E2,+E1). Everything uses integers, not floats. Endpoint-pruned direct enumeration checked **every closed signed ordered path** for n=0,2,4,6 against the separate DFA dynamic program. At n=8 the DP was compared with native unfiltered endpoint total; n=8 direct enumeration was **not** run here.

| length n | closed ordered words | native weighted sum | final DP states | DP transitions |
|---:|---:|---:|---:|---:|
| 0 | 1 | 1 | 1 | 0 |
| 2 | 12 | 24 | 94 | 156 |
| 4 | 396 | 1,560 | 1,874 | 7,044 |
| 6 | 19,920 | 152,640 | 16,022 | 100,716 |
| 8 | 1,281,420 | 18,921,000 | 82,634 | 751,764 |

For n=8, orbit-channel weight totals by four Boolean atoms (00,01,10,11) are exactly (16,560,120, 1,129,320, 1,129,320, 102,240), the same in both aggregate channels, while counts are (1,170,120, 53,850, 53,850, 3,600). The coincidence of population sums does not erase the earlier path-bag rank-two witnesses. The recurrence was compared to native for all even n≤18. **Only** recurrence, not word enumeration or DFA, was evaluated at n=200: its weighted integer has 789 bits, and all-unit return count has 695 bits.

Reproduce by retrieving the pinned signed_brc.py Git blob (already in the EC49BV sources archive), putting it at source/signed_brc.py next to VERIFY_EC49BY_MIN.py, and running python VERIFY_EC49BY_MIN.py. The exact checks above and source preconditions are encoded in that executed program. The native kernel source is not changed.

## Real research status, successor

The native service 0.6.11 reported research_authority_granted=false. Attempted active-owner/task query returned CONTROL_QUOTA (5/5 jobs); owner and winning claim could not be independently established. This GitHub source artifact is **author-side portable research evidence**, not a canonical Source CLAIM/Result, independent Driver verdict, accepted theorem or P000 modification. No private credentials or user access permissions were changed.

**EC49BZ:** For fixed DFA/H path selectors, derive a faster rigorous bit bound using typed constant terms, multivariate generating functions/diagonals or compressed transitions; or return a precisely scoped obstruction. Prove which future append/filter operations are preserved, reproduce the four-atom native test, and avoid treating finite runtime observations as an asymptotic theorem.
