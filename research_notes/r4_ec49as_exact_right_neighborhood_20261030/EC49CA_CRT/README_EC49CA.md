# EC49CA — Exact CRT reconstruction and backward-cone pruning for signed-X6 BRC

**2026-10-31 · AUTHOR_ANALYTIC_PROOF / EXACT_NATIVE_X6_CRT_AUDIT_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED.** This is independent author-side mathematical material, not a formal Source-native CLAIM/Result or Driver admission. All results are finite combinatorial BRC observations, not physical Heartbeat dynamics.

## Frozen source and declared observer

GLOBAL_KNOWLEDGE_V1 `main@d8a7f5790a674c170799731e728aa401bfe66d11` (00_BOOTSTRAP, OPERATING_MANUAL, P000 startup, ACTIVE worldview and relevant code/math/BRC policies); Enterprise Math `main@1cad8a9d12ac18449b710c4fc682bd16659ef4b1` (P000 V5, native X6, current autonomous/portable research protocol and joint-observer contract). Parent EC49BZ: `d2ba0246b2533930d6e89176aa9c28abefeeb0de`, PR #1730. Native unchanged `signed_brc.py` blob: `300a96e3dc24bf6fff73743037a0347a8bc83176`. This study genuinely executes that kernel's `endpoint_weight` and `endpoint_multiplicity` functions, reusing the prior ordered-DFA construction.

The step alphabet is `Σ={±E_i:1≤i≤6}`, with signed **relative** displacement `d(±E_i)=±e_i∈Z^6` from a chosen Cell. There is no global ontic origin or primitive two-dimensional plane. Let `H≤S₆` be a finite sign-preserving axis-permutation group, `A=(Q,δ,q₀)` a complete DFA and `Φ(p)=(δ*(q₀,h·p))_{h∈H}` the **joint** terminal transition state in `Q^H`. For positive rational weights `w_a=c_a/D`, with common positive denominator `D` and positive integer numerators `c_a`, define the exact integer numerator

`F_{h,φ}(n)=Σ_{p∈Σ^n,Σd(p)=0,Φ(p)=φ}∏_{a∈p}c_{h·a}.`

Its rational BRC observable is `F_{h,φ}(n)/D^n`. Boolean terminal filters sum selected atoms. The full joint DFA state and signed six-dimensional displacement remain typed through composition; no source-path or positive-weight cancellation is inferred.

### Theorem A — Native return majorant and CRT uniqueness

Let `B_n=Σ_{p∈Σ^n,Σd(p)=0}∏_{a∈p}c_a`, the *unfiltered numerator* of native `endpoint_weight(n,0,c⁺,c⁻)`. For every group channel `h` and terminal atom `φ`,

`0≤F_{h,φ}(n)≤B_n≤(Σ_{a∈Σ}c_a)^n≤(12·max_a c_a)^n.`

**Proof.** Strict positivity implies each atom contributes a nonnegative subset of the unfiltered return sum. The map `p↦h·p` bijects zero-return ordered paths with zero-return ordered paths and exactly transforms their weight products, so the unfiltered total is the same `B_n` in every `h` channel. Omitting the endpoint constraint leaves the unrestricted sum over all ordered paths, which equals `(Σc_a)^n`. The last inequality is termwise. This is an integer-numerator result; rational division by `D^n` is performed **after** reconstruction. ∎

For pairwise coprime integers `m_1,…,m_k`, if `M=∏m_i>B_n`, then the residues `(F_{h,φ}(n) mod m_i)_i` identify **exactly one** integer in `[0,B_n]`. Indeed, two such integers with equal residues have a difference divisible by `M` but of absolute value less than `M`; hence the difference is zero. Standard constructive CRT produces the representative. This is an exact all-n theorem, not an extrapolation from finite experiments. For a *nonzero* endpoint `z`, replace the uniform majorant by the maximum of the channel-specific unfiltered endpoint numerators; equality across channels is not asserted there.

The capacity hypothesis matters: at `n=4` the true `00` atom has numerator 1488, whose residue modulo 101 is 74. Using 101 alone and lifting the residue to 74 is incorrect. Our condition is sufficient for every admissible atom, not claimed minimal for a known individual atom. Because `B_n` is obtainable from the existing native unfiltered return recurrence, one need not solve the filtered problem to certify the CRT modulus.

### Theorem B — No displacement alias and safe fixed-horizon backward cone

For each modulus separately, maintain `(t,z,φ)` with `z∈Z^6` as a **genuine integer coordinate tuple** and a vector of modular BRC channel sums. Transition on letter `a`: `(z,φ)↦(z+d(a),δ_H(φ,a))`, multiplying its channel coefficient by `c_{h·a} mod m_i`. By induction on `t`, this state equals the residue of the sum of all original ordered words with that exact displacement and joint DFA state. Since **only coefficient arithmetic** is reduced modulo the primes, and never the six displacement coordinates, a nonzero spatial displacement cannot wrap into the zero-return coefficient. The CRT reconstructed terminal atoms therefore agree with the original source-respecting BRC for every `n`. This supplies an explicit no-alias proof and does not rely on a cyclic convolution with undersized spatial periods.

For a fixed zero-return target at path length `n`, a layer-`t` displacement `z` admits a completion in exactly `n−t` signed-axis steps if and only if

`||z||₁≤n−t` and `n−t−||z||₁≡0 (mod 2)`.

**Proof.** At least `||z||₁` unit-axis moves are necessary. Exactly `||z||₁` inverse-axis moves cancel `z`; every remaining *even* number of steps can be filled with adjacent inverse-axis pairs. The parity of `||z||₁` changes at each signed unit step, proving necessity. For an even-n walk already reached at t, the parity condition follows automatically. Thus all and only the outside-cone states can be dropped without altering *any* terminal atom. ∎

This `ℓ₁` is the graph distance for unit steps in the six-coordinate signed chart, **not** a claim about P000 Euclidean-like angles. The pruning is scoped to the fixed target/horizon; it is not sufficient for **arbitrary later suffix append**, a future-operation scope requiring retained transition/displacement information (see EC49BZ's exact append counterexample).

### Resource certificate and comparison

Write `h=|H|`, `q=|Q|^h`, `k` pairwise coprime moduli of maximum bit size `b`, and `ℓ=ceil(log₂(max c_a+1))`. At layer t the backward cone contains at most `q(2·min(t,n−t)+1)^6` joint displacement states. Twelve transitions per state and `Σ_{t=0}^n min(t,n−t)^6=O(n^7)` give at most `O(k h q n^7)` modular arithmetic operations. Conservatively, grade-school modular operations cost `O((b+ℓ)^2)` bit operations, yielding `O(k hq n^7(b+ℓ)^2)` for the modular passes; direct incremental CRT over at most `O(hq)` terminal integers adds at most `O(hq k(kb)^2)` bit operations using elementary big-integer arithmetic. Two-layer streaming DP payload memory is `O(hq n^6 b + hq kb)` bits, **excluding** interpreter/dictionary overhead, native BRC evaluation and arithmetic workspaces.

These are explicit upper bounds and not optimality or faster-run claims. A fixed finite set of constant-bit primes cannot serve all unbounded n; the bound is parametrized by the actual chosen k and b. EC49BZ's dense packed-integer transfer has a different (theoretical) `O(n^7(log n)^2)` fixed-model bit-time upper bound but can require enormous dense packed matrices. This modular route trades additional passes for smaller per-pass integers, and the backward cone makes a separate, exact state-count reduction.

## Executed finite certificate

Reproduce from this directory using `python VERIFY_EC49CA_MIN.py` (Python 3.10+, standard library). The adjacent `native_signed_brc.py` is **identical to project Git blob** `300a96e3dc24bf6fff73743037a0347a8bc83176`; it is not a new BRC implementation. `VERIFY_EC49CA_MIN.py` was executed twice, yielding identical `EXACT_REPORT_EC49CA_MIN.json` (SHA256 `72dd3c2440d003501ba6f787d3cc59aa1b2f54c6c9016f8fbff48707674be3d1`). Executed verifier SHA256: `eba723f1fa9676ec656b01a4749d81c1c117bd066581e8becb1e2e95eef5c0ae`, Git Blob: `82261a6ad86bd608b8a74558f47ae4f579a5d39a`.

The test compares full modular/CRT terminal outputs with an exact unmodded DP, validates all totals against the unchanged native BRC, compares pruned and unpruned exact DP, and **independently enumerates each literal closed word** with direct substring inspection for n=0,2,4,6 (respectively 1,12,396,19,920 words). At n=8, an exact DP and native unfiltered check are performed but direct literal word enumeration is not. The separate EC49BZ packed multiplication algorithm is not rerun here.

| n | native return B_n | closed words | prime factors M | M | peak pruned states | peak unpruned states |
|---:|---:|---:|---|---:|---:|---:|
| 0 | 1 | 1 | 101 | 101 | 1 | 1 |
| 2 | 24 | 12 | 101 | 101 | 12 | 94 |
| 4 | 1,560 | 396 | 101·103 | 10,403 | 94 | 1,874 |
| 6 | 152,640 | 19,920 | 101·103·107 | 1,113,121 | 480 | 16,022 |
| 8 | 18,921,000 | 1,281,420 | 101·103·107·109 | 121,330,189 | 1,874 | 82,634 |

Atom triplets list two fixed-instrument channels then path count. At n=4: `00:(1488,1488,384)`, `01:(36,36,6)`, `10:(36,36,6)`, `11:(0,0,0)`. At n=6: `00:(139320,139320,18744)`, `01:(6480,6480,576)`, `10:(6480,6480,576)`, `11:(360,360,24)`. At n=8: `00:(16560120,16560120,1170120)`, `01/10:(1129320,1129320,53850)`, `11:(102240,102240,3600)`. All exact values and checks are machine-readable in the adjacent JSON. Peak-layer states decrease by over 44-fold at n=8 *due to pruning*, not proved due to CRT alone. One local minimal checker execution took about 3.24 seconds and reported ~139 MB process RSS including unpruned test; neither observation is a portable performance guarantee.

## Authority, reproducibility and next EC49CB

At research intake, the native gateway reported `research_authority_granted=false` with 5/5 active job quota; the actual `em_control_tasks` query returned `CONTROL_QUOTA`. The active formal owner was therefore **not independently verified**. No Source-native session, CLAIM, Result or Driver approval has been obtained; PR publication is evidence preservation only. Protected P000 and ACTIVE worldview remain unchanged. External novelty is not claimed: CRT, DFA methods and co-reachability are established algorithmic principles; this is the project-scoped exact X6/BRC application and verified resource tradeoff.

**EC49CB:** Test a transposed/block-modulus constant-term scheme that avoids k full n-step passes, with exact no-alias proof, explicit time/memory bounds including modulus selection, and fair exact benchmarks against integer sparse DP, the CRT route and EC49BZ packed n≤4. First seek a larger-n *measured* memory win; otherwise record the performance obstruction rather than asserting a practical advantage.
