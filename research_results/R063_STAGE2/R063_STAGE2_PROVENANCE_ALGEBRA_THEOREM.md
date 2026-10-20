# R063 Stage 2 — Multiplicative Provenance Algebra Theorem

Status: `PROVED / FROZEN-STAGE1-DEPENDENT / SECTOR-LOCAL ALGEBRA`

Task-ID: `RS-R063-STAGE2-MULTIPLICATIVE-PATH-NORM-ROOT-PROVENANCE-ALGEBRA`  
Researcher-ID: `EM-R063S2-52118B`  
Taskbook source: `74cacc89ec09a8af7dd7ff01c10f2baf082daf81`  
Frozen Stage 1: `65f4e98cd707c634d805f2a9ec7c41f24ab06185`  
Stage 1 Driver acceptance: `fb2331b0602e74cae506ebac49c4582e7147479d`

## 1. Scope

This theorem classifies the factorization/Gaussian algebra above the frozen R061 sector-local component-trace semantics. It does **not** promote Gaussian multiplication to a global Enterprise-plane native multiplication law.

All multiplication theorems below have domain **supported positive factors** unless stated otherwise. Here supported means the frozen Stage 1 integer-component support condition.

## 2. Provenance carrier

For supported

`N = 2^e2 * product_{q == 3 mod 4} q^(2h_q) * product_{p == 1 mod 4} p^e_p`,

fix the deterministic Stage 1 split-prime representatives

`p = pi_p * conjugate(pi_p)`.

Define

`Prov(N) = U x product_{p == 1 mod 4} {0,...,e_p}`,

where `U={1,J,-1,-J}`. An element is written

`P=(u,(t_p)_p)`.

The ramified `2` contribution and supported inert contributions are fixed by `N`; `t_p` records the exponent of `pi_p`, while `e_p-t_p` records the exponent of its conjugate.

Evaluation is

`ev_N(P)`

`= u (1+J)^e2 product_q q^h_q product_p pi_p^t_p conjugate(pi_p)^(e_p-t_p)`.

By the frozen Stage 1 Gaussian generator plus uniqueness of this normalized exponent-allocation data, `ev_N` is a bijection

`Prov(N) -> SRoot(N)`,

where

`SRoot(N)={z in Z[J] : Norm(z)=N}`.

## 3. Exact provenance multiplication

Let supported `A,B` have split-prime allocation coordinates `i_p,j_p`, with missing exponents interpreted as zero. Define

`mu_Prov((u,(i_p)),(v,(j_p)))=(uv,(i_p+j_p))`.

The target bounds hold because

`0 <= i_p+j_p <= v_p(A)+v_p(B)=v_p(AB)`.

### Theorem 3.1 — evaluation multiplicativity

For every `P in Prov(A)`, `Q in Prov(B)`,

`ev_AB(mu_Prov(P,Q)) = ev_A(P) ev_B(Q)`.

**Proof.** Ramified, inert and split-prime exponents add primewise, while the unit multiplies from `u,v` to `uv`. Gaussian multiplication is commutative and associative, so regrouping the exact factors gives the displayed equality. No target-root search is used. ∎

### Theorem 3.2 — graded commutative monoid laws

Across the disjoint union of supported norms, `mu_Prov` is associative and commutative. The identity is the norm-one provenance

`1_Prov=(1, empty allocation)`.

**Proof.** Split-prime coordinates use ordinary integer addition and unit coordinates use the abelian group `U`; both are associative and commutative and have their stated identities. ∎

If provenance is enriched further with ordered factor-origin labels, strict commutativity is replaced by commutativity after the obvious factor-origin relabeling. The normalized Stage 2 `Prov` carrier deliberately omits those redundant ordered source labels.

### Theorem 3.3 — surjectivity for supported factors

`mu_Prov : Prov(A) x Prov(B) -> Prov(AB)` is surjective for supported `A,B`.

**Proof.** Fix target `(w,(t_p))`. For every split prime, choose any solution

`i_p+j_p=t_p`, `0<=i_p<=alpha_p`, `0<=j_p<=beta_p`,

where `alpha_p=v_p(A)`, `beta_p=v_p(B)`. Such a solution always exists because `0<=t_p<=alpha_p+beta_p`; for example the interval proof in Section 4 gives a nonempty interval. Choose any first unit `u`; then `v=u^{-1}w` uniquely determines the second unit. Thus a preimage exists. ∎

The support hypothesis is essential. If the theorem is incorrectly widened to arbitrary positive factors, `A=B=3` is the minimal boundary: `Prov(3)=empty`, while `Prov(9)` is nonempty. Therefore no map from the empty factor domain can be surjective onto `Prov(9)`.

## 4. Exact primewise provenance-fiber count

Fix a split prime `p`, write

`alpha=v_p(A)`, `beta=v_p(B)`,

and fix target total `pi_p` exponent `t` in `AB`.

The preimage constraint is

`i+j=t`, `0<=i<=alpha`, `0<=j<=beta`.

Equivalently,

`max(0,t-beta) <= i <= min(alpha,t)`.

Hence the exact local count is

`m_p(alpha,beta;t)`

`= max(0, min(alpha,t)-max(0,t-beta)+1)`.

This proves the taskbook candidate exactly.

### Theorem 4.1 — fixed signed target formula

For a fixed signed target provenance/root channel,

`PreimageCount_signed(A,B,target)`

`= 4 * product_{p == 1 mod 4} m_p(v_p(A),v_p(B);t_p)`.

**Proof.** The split-prime choices are independent, giving the product. For units, if target unit is `w`, the equation `uv=w` has exactly four ordered solutions: choose any of the four `u in U`, then `v=u^{-1}w` is forced. This factor is therefore exactly `4`; it is not assumed. ∎

After quotienting the target and factors by units, the unit factor disappears:

`PreimageCount_URoot(A,B,target orbit)`

`= product_p m_p(alpha_p,beta_p;t_p)`.

## 5. Signed Gaussian root multiplication

Because `ev` is bijective on supported norms and intertwines `mu_Prov` with Gaussian multiplication, multiplication of signed roots

`SRoot(A) x SRoot(B) -> SRoot(AB)`, `(z,w) |-> zw`

is surjective for supported `A,B`. Norm grading is exact:

`Norm(zw)=Norm(z)Norm(w)=AB`.

This is a theorem about the Stage 1 sector-local Gaussian factorization/component algebra. It is not a theorem that the entire Enterprise plane possesses global native Gaussian multiplication.

## 6. Evidence separation

The ordinary proof above is the theorem. The committed checker supplies finite exact replay evidence only:

- frozen Stage 1 root-generator replay anchors;
- all `7 x 7 = 49` ordered base pairs over `{1,2,5,13,17,25,65}`;
- direct verification of the local formula on all exponent triples needed through the exhaustive range;
- all `1<=A,B<=128` ordered pairs as compact exact regression records;
- deterministic supported/unsupported sparse cases with products reaching `9*10^12`;
- zero checker mismatches.

Finite replay is not used as a substitute for the general proof.

## 7. Classification

`PROVENANCE_MULTIPLICATION_EXACT = true` on supported factor domains.

`PROVENANCE_MULTIPLICATION_SURJECTIVE = true` on supported factor domains.

`FIXED_SIGNED_TARGET_PREIMAGE_COUNT = 4 * product_p m_p`.

`FIXED_UNIT_ORBIT_TARGET_PREIMAGE_COUNT = product_p m_p`.

`GLOBAL_FULL_PLANE_GAUSSIAN_MULTIPLICATION_NATIVE = NOT_CLAIMED`.
