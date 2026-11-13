# R693: S₃ 原生 BRC 回归观察的完整谱不变量与纯整数证书

Date: 2026-11-10. Research status: AUTHOR-PROVED / EXACT-COMPUTATION-VERIFIED / UNREVIEWED / NOT ADMITTED.

Mother Task: `RS-X6-TRIADIC-CLOSURE-DYNAMICS`; current publication `TP2-8B7E13C5904A2D6F1142`. Author-side Researcher-ID `EM-X6-B30671`, Research-Activity-ID `RA-467117BBDE4D7BD1E01C9781`. No formal CLAIM, Result or review was issued.

Frozen scientific source remains `a72226e2430ffa4786321ac86e7f0c599d5f0389` per native continuation control; the control reported one `DRAFT_OR_UNVERIFIED` locator at that old source commit, so this study uses the directly verified existing E* model and does not claim verification of that absent artifact. The exact input is the twelve integer S₃ group kernels in `R692C_ESTAR_MASK_RETURN_EXACT.js` at immutable commit `3dacca5010104893d96301af4d61608d5a5a0879`, Git Blob `0c6d51f99eac5903a30770c8c393c972a68d93ad`. These are 15 labelled four-step native X6 returning Cell paths per direction sign and root phase. The persistent future protocol is unchanged: every macro uniformly chooses one allowed labelled path in a fixed nonempty mask M⊆{--,-+,+-,++}; the observation is the probability that the *complete S₃ frame* returns after k such macros, with the initial phase, Cell and frame specified. The six-dimensional Cell and path provenance remain at the input level, prior to the observer quotient.

## Theorem R693-A: exact classification of all future return observations

Let μ be **any rational probability measure on S₃** and r_k=μ^{*k}(e), k≥0 (r₀=1). Let ρ:S₃→GL₂(Q) be the faithful standard representation on {(x₀,x₁,x₂):x₀+x₁+x₂=0}, in basis e₀−e₂, e₁−e₂. Put

* s=Σ_g μ(g) sign(g);
* B=Σ_g μ(g) ρ(g), t=tr(B), d=det(B).

Then the *exact formal power series* is

```text
R(z) = sum_{k>=0} r_k z^k
     = (1/(1-z) + 1/(1-s*z) + 2*(2-t*z)/(1-t*z+d*z*z))/6.
```

For **any two** such probability measures μ,ν, their return probabilities agree at **every** k≥0 if and only if their rational triples (s,t,d) agree. Thus (s,t,d) is a complete exact all-future-return observer classifier. This is an observation-scope theorem; it does not identify the full labelled group distribution, trajectory or original Link/Port state.

**Proof:** The left regular S₃ representation decomposes into the 1-dimensional trivial, 1-dimensional sign and two copies of the standard 2-dimensional representation. Its trace at power k is 6 r_k, so

```text
6*r_k = 1 + s^k + 2*h_k
h_0=2; h_1=t; h_{k+2}=t*h_{k+1}-d*h_k.
```

Cayley–Hamilton for B yields the recurrence; summing its series gives R(z). Conversely equality of all r_k implies equality of the six first power traces of the regular convolution matrices, and Newton identities give equality of their characteristic polynomials

```text
chi_mu(X)=(X-1)*(X-s_mu)*(X^2-t_mu*X+d_mu)^2.
```

Remove one common (X−1). Over the algebraic closure the **unique root of odd multiplicity** in the remaining polynomial is s_μ, even when s_μ equals either root of the quadratic. Equality forces s_μ=s_ν. Dividing by (X−s) and comparing monic squares forces the quadratic factors to match, hence t_μ=t_ν and d_μ=d_ν. This completes both implications.

## Corollary R693-A0: all-integer exact BRC path-count certificate

Let nonnegative integer kernel weights n_g count original labelled macro paths giving g∈S₃, D=Σ_g n_g>0. Define the integers

```text
S=Σ n_g sign(g)
M=Σ n_g rho(g) ∈ Mat_2(Z)
T=tr(M), Delta=det(M)
H_0=2, H_1=T, H_{k+2}=T*H_{k+1}-Delta*H_k.
```

Let C_k count labelled sequences of k independent allowed macros whose composed group action returns to e, with multiplicity and ordering intact. Then **for every integer k≥0**:

```text
             6*C_k = D^k + S^k + 2*H_k .
```

Proof: substitute μ(g)=n_g/D in R693-A and multiply by D^k. It is a complete integer identity, including k=0 and zero-weight branches. Thus exact large-k return counts follow from a two-term recurrence and integer powers. Binary lifting yields O(log k) arithmetic operations for a fixed kernel; actual bit and original-input preprocessing costs remain explicit variables.

## Corollaries R693-B/C: shorter horizons for special native-support subgroups

If supp(μ)⊆A₃={e,c,c²}, write μ=(p,u,v), p+u+v=1. Then s=1, t=3p−1, d=1−3p+3p²−3uv and r₁=p, r₂=p²+2uv. **The two numbers r₁,r₂ determine all future r_k.** Swapping u and v can change labelled group laws without changing return probabilities.

If supp(μ)⊆C₂={e,τ} and p=μ(e), then s=2p−1, t=1+s,d=s, and for every k≥0:

```text
r_k = (1 + (2p-1)^k)/2.
```

Thus r₁ alone determines the entire future return sequence inside this C₂ family. The proof follows directly by the respective subgroup supports and R693-A.

## Exact frozen E* computational evidence

The program `R693_S3_BRC_INTEGER_CERTIFICATE.js` includes the **unaltered R692C input-program source** (same blob verified) and the new exact integer implementation. It checks 36 representation multiplication laws and, for every a∈{0,1,2}, every nonempty mask 1..15 and all k=0..20, independently convolves the native integer group path kernels and verifies the boxed integer formula: **45×21=945 exact equalities** using BigInt. It checks input mass and exact R692C six-horizon probabilities. For phase a=1 every kernel is supported on A₃; for phase a=2 every kernel is supported on C₂. Classification by the rational spectral triple reproduces **12,12,9** future-observer equivalence classes and sharp horizons **3,2,1**, including mask equivalence {2,5} and {6,9,15} at a=0. The 45 individual rational triples, return signatures up to six, 20-macro return probability, and complete partitions are saved in `R693_S3_BRC_INTEGER_RESULTS.json`.

Executed outcome: `R693_ALL_INTEGER_ASSERTIONS_PASS`. This verifies the **specified finite E* candidate model** and the integer formula over those inputs; the general theorem above is an algebraic proof. The 360 original individual X6 square paths were already checked in upstream R692/R691 and are *reused*, not claimed to be independently re-enumerated in this round.

## Scientific increment, current boundary and next discriminating action

R692's sufficient six-step return trace signature is replaced by three directly computable rational spectral quantities (s,t,d). The computation is an integer BRC path-count certificate, avoiding repeated dense S₃ group convolution when performing huge-k queries. The E* observer’s equivalence classes and subgroups now have structural explanations. REUSE_APPLIED: exact native labelled BRC group kernels and R692 return-observer interface. EXTEND_EXISTING_TOOL: exact integer S₃ representation and two-term trace recurrence.

Next: read the frozen real X6 Link/Port, V29 PASS/TRANSFER, and V39 event-state transition definitions; form the allowed state-dependent signed-port BRC kernels; test whether (Cell,phase,full frame,port/source) dynamics descend to fixed S₃ group convolution. If so apply the present complete invariant. If not, construct explicit distinguishing future traces and a minimal provenance repair coordinate. This would advance the mother Task’s typed triadic closure/covariance objective. No present mathematical admission, Foundation change, or native V29 semantics is asserted.

Artifacts: this Markdown, `R693_S3_BRC_INTEGER_CERTIFICATE.js`, `R693_S3_BRC_INTEGER_RESULTS.json`. Additional independent Python Fraction verifier, JSON and local SHA256-checkable bundle are available as session delivery.
