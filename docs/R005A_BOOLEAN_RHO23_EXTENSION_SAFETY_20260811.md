# R005-A — 23# Exact Boolean Horizon and Prime-Extension Safety Checkpoint

Status: `PROVED STRUCTURAL CHECKPOINT / EXECUTABLE CHECKED / NOT CANONICAL / LEAN PENDING`  
Task: `RS-R005-PRIME-ALGORITHM-LAB`  
Researcher-ID: `R005A-7C2`  
Date: `2026-08-11`

This continues the existing R005-A owner generation and Draft PR #364. It does not create a new task, does not modify the canonical Prime Toolkit, does not promote Draft #333, and does not claim a new generic safe-quotient theorem.

The canonical internal prime capability layer remains authoritative for reusable prime helpers. This checkpoint uses a fixed theorem instance `P={2,3,5,7,11,13,17,19,23}` in the C++ certificate; it does not implement a replacement prime enumerator or primality oracle.

## 0. Main closure

The previous checkpoint left two live questions:

1. whether the exact Boolean steady phase-separation radius could be pushed beyond `19#` without scanning every primorial phase;
2. whether the fixed-modulus XOR separator certificate remains sufficient when the verifier/future language is allowed to adjoin another sieve prime.

Both now have sharp answers at this research level:

- `rho(23#)=535` exactly;
- the full actual `p^2`-activation Boolean horizon at `23#` is also exactly `535`;
- the fixed-modulus XOR separator bit is **not** composition-safe under adjoining a new prime whose shift coordinate changes;
- the four-state paired-coprimality carrier is the coarsest pointwise carrier that is safe for such a changed-coordinate prime extension, conditional on the extension's new-prime residue inputs.

The generic safe-operation/quotient theorem belongs to the existing precision/future-language owners. R005 contributes only the sieve-specific realization and counterexample.

## 1. Prior-art demotion of the generic `rho` complexity

For a binary periodic word `w` of least period `Q`, define

`rho(w)=max_{a!=b} min{t>=0:w(a+t)!=w(b+t)}`.

Then `rho(w)+1` is the least cyclic window length for which all `Q` starting positions have distinct length-`L` factors. Equivalently it is one plus the maximum longest-common-prefix length of distinct cyclic shifts.

Therefore the **generic** complexity is not an R005 novelty target. It sits next to established cyclic-word, conjugate-language/state-complexity, generalized de Bruijn, nonlinear/maximum-order-complexity, and periodic-sequence literature.

Relevant prior art includes:

- D. Gabric, S. Holub, J. Shallit, *Generalized de Bruijn Words and the State Complexity of Conjugate Sets*, DCFS 2019, DOI `10.1007/978-3-030-23247-4_10`, expanded as arXiv `1903.05442`.
- Q. Yuan, C. Li, X. Zeng, T. Helleseth, D. He, *Further Investigations on Nonlinear Complexity of Periodic Binary Sequences*, Cryptology ePrint `2024/632`.
- J. Cassaigne, G. Fici, M. Sciortino, L. Q. Zamboni, *Cyclic Complexity of Words*, arXiv `1402.5843`.

R005's retained arithmetic specialization is the primorial/squarefree wheel word

`w_Q(n)=1[gcd(n,Q)>1]`

and the exact separator representation

`M_d = U_Q triangle (U_Q-d)`.

## 2. T-A49 — exact `23#` steady radius and full actual horizon

Let

`Q=23#=223,092,870`.

For each prime `p|Q`, the classical Jacobsthal separator bound gives

`gap(d) <= p*j(Q/p)`

whenever `p` is a changed coordinate of the shift `d`.

The executable certificate recomputes the exact classical caps:

| p | `j(Q/p)` | `p*j(Q/p)` |
|---:|---:|---:|
| 2 | 20 | 40 |
| 3 | 20 | 60 |
| 5 | 26 | 130 |
| 7 | 26 | 182 |
| 11 | 28 | 308 |
| 13 | 30 | 390 |
| 17 | 34 | 578 |
| 19 | 34 | 646 |
| 23 | 34 | 782 |

A concrete singleton-23 shift

`d = 2*(Q/23) = 19,399,380`

has separator gap exactly `536`.

Therefore every hypothetical improving shift must fix all coordinates whose classical cap is `<=536`, i.e. it must be divisible by

`2*3*5*7*11*13 = 30030`.

The full nonzero shift space of size `Q-1` is thus reduced exactly to

`17*19*23-1 = 7428`

residual CRT phases.

`experiments/r005a_boolean_rho23_certificate.cpp` exhausts every one of these residual shifts and finds no separator gap above `536`.

Hence

`rho(23#)+1 = 536`, so

`rho(23#)=535`.

### Actual activation transient

For the standard prime-prefix Boolean Eratosthenes stream, the exact preperiod remains

`mu_U(23)=24`.

A transient/steady pair can exceed the steady radius only if its post-activation separator gap is large. Any shift changing a coordinate `<=13` has steady gap at most `390`, hence its transient/steady depth is at most

`23+390=413 < 535`.

So only the same `7428` residual shifts can threaten the steady radius. On those shifts, the executable uses only:

- the exact activation defect mask `D_23={0} union {p:p<=23}` on `[0,23]`;
- the first steady separator after 23.

The largest residual transient/steady depth is

`213`,

attained at

`d = 9*(Q/23) = 87,297,210`,

with earliest surviving transient start `s=20` and next post-23 separator distance `210`.

The exact transient/transient maximum over the `24 choose 2` finite pairs is `15`, attained at starts `(4,10)`.

Therefore

`H_U^actual(23)=max(535, <=413, 213, 15)=535`.

So the prime-prefix equality conjecture

`H_U^actual(q)=rho(q#)`

is now executable-verified through the consecutive checked primes

`q=7,11,13,17,19,23`.

It remains `CONJECTURAL` as an all-prime theorem. The already-proved asymptotic statement

`H_U^actual(q)/rho(q#) -> 1`

is independent of this exact-equality conjecture.

## 3. Fixed-modulus separator certificate versus future prime extension

For a squarefree wheel modulus `Q` and shift `d`, define the paired coprimality state at position `n`:

`C_{Q,d}(n) = (u_Q(n), u_Q(n+d)) in {00,01,10,11}`,

where

`u_Q(x)=1[gcd(x,Q)=1]`.

The fixed-modulus Boolean separator is only

`m_{Q,d}(n)=u_Q(n) xor u_Q(n+d)`.

Thus the XOR collapse identifies

`00 ~ 11`

and

`01 ~ 10`.

This is exact for the declared fixed-`Q` separator observation.

Now adjoin a new prime `p` not dividing `Q`. Let

`delta = d mod p`,

`r = n mod p`,

`alpha_r = 1[r != 0]`,

`beta_r = 1[r+delta != 0]`.

Then the exact lifted pair is

`C_{Qp,d}(n) = (a*alpha_r, b*beta_r)`

when

`C_{Q,d}(n)=(a,b)`.

The lifted XOR output is therefore

`(a*alpha_r) xor (b*beta_r)`.

This is ordinary CRT/wheel arithmetic; the semantic question is which old carrier is sufficient for the declared future operation.

## 4. T-A50 — sharp prime-extension safety boundary

### Fixed new-prime coordinate: `delta=0`

If `p|d`, then

`alpha_r=beta_r`

for every residue `r`.

Hence

`m_{Qp,d}(n)=alpha_r * m_{Q,d}(n)`.

So the two-state XOR separator carrier is safe for this extension.

### Changed new-prime coordinate: `delta!=0`

If `p` does not divide `d`, then as `r` ranges modulo `p` the extension realizes the masks

- `(0,1)` at `r=0`;
- `(1,0)` at `r=-delta`;
- `(1,1)` at the ordinary residues when `p>2`.

For `p=2`, the first two masks already suffice.

The old XOR class `0` is not stable:

- `00` remains XOR `0` under mask `(0,1)`;
- `11` becomes `01`, hence XOR `1`.

Therefore the fixed-modulus XOR collapse is dynamically unsafe.

Moreover the four old pair states have distinct one-prime future signatures:

- `00`: all-zero signature;
- `01`: zero exactly at the right-killed residue;
- `10`: zero exactly at the left-killed residue;
- `11`: XOR one on the two special residues (for `p=2`, on both residues).

Thus all four states are future-distinguishable.

### Exact statement

Conditional on `p`, `r=n mod p`, and `delta=d mod p` being supplied as the extension operation's own inputs:

`XOR separator collapse is safe for adjoining p iff delta=0`.

If the future language allows a changed new-prime coordinate (`delta!=0`), the coarsest pointwise exact carrier is the full four-state paired coprimality state.

This is a prime-specific specialization of the project's existing safe-operation/future-signature theory, not a new generic quotient theorem.

### Scope guard

This does **not** say that the ordinary single-stream Boolean sieve output is unsafe under wheel extension. For one stream,

`w_{Qp}(n)=w_Q(n) OR 1[p|n]`

is compositional.

The theorem concerns the **pair-separator certificate used to compare two future trajectories**. Compressing that pair to XOR loses information required by a later modulus-extension verifier.

## 5. T-A51 — aggregate Hamming mass remains much coarser

Let the current pair-word counts over one `Q`-period be

`N00,N01,N10,N11`.

For a fixed-coordinate extension `delta=0`:

- `N01'=(p-1)N01`;
- `N10'=(p-1)N10`;
- `N11'=(p-1)N11`.

Therefore the separator mass

`M=N01+N10`

obeys

`M'=(p-1)M`.

For a changed-coordinate extension `delta!=0`:

- `N00'=p*N00+N01+N10`;
- `N01'=(p-1)N01+N11`;
- `N10'=(p-1)N10+N11`;
- `N11'=(p-2)N11`.

Since translation gives

`N01=N10=phi(Q)-N11`

and

`M=2(phi(Q)-N11)`,

we obtain the scalar recurrence

`M'=(p-2)M+2*phi(Q)`

when the new prime coordinate changes.

Thus there is a sharp semantic hierarchy:

1. **aggregate separator mass** closes under a coarse scalar recurrence;
2. **fixed-modulus separator word** needs the XOR positions;
3. **prime-extension-safe separator certificate** needs the four-state oriented pair word;
4. **additive observation depth** additionally depends on ordered phase geometry, and support/mass alone are already known to be insufficient.

This is exactly the task-relative precision distinction the R005 second round was seeking. Stronger future languages require strictly finer carriers even when the coarser statistic is exact for its original task.

## 6. Prior-art attack on wheel recursion

Recursive wheel/gap mechanics are not new. Relevant prior art includes:

- F. B. Holt, H. Rudd, *Eratosthenes sieve and the gaps between primes*, arXiv `1408.6002`, which studies recursions on cycles of gaps across Eratosthenes stages.
- M. Ziller, J. F. Morack, paired-Jacobsthal work, including arXiv `1706.03668`, which adapts Jacobsthal algorithms to paired progressions.
- M. Ziller, *On differences between consecutive numbers coprime to primorials*, arXiv `2007.01808`.

Therefore R005 must not claim novelty for recursive primorial/wheel construction, CRT pair counting, or paired-progression state itself.

The retained R005 content is the **future-language boundary**:

- XOR is exact for fixed-modulus separation;
- XOR is not a safe carrier for a changed-coordinate prime-extension verifier;
- aggregate Hamming mass can nevertheless remain closed;
- additive future-depth needs still finer ordered phase information.

## 7. Consequence for Draft #333 / compiler provenance

No status change is made to Draft #333.

The new result should be used only as a falsification/refinement test:

- #333's semantic prime-support compiler is not refuted;
- a compiler that additionally claims exact additive runtime or future modulus-extension cost cannot assume that support/XOR data alone is sufficient;
- the relevant extra information depends on the declared future operation: oriented pair state for p-extension, residual unit phase/order geometry for additive depth.

This supports a product-of-concerns interpretation but does **not** prove a canonical product decomposition of compiler state.

## 8. Current four-layer return

### Already supplied by canonical Internal Prime Toolkit

Unchanged. No R005 replacement implementation was added.

### External classical capability

- ordinary and paired Jacobsthal algorithms/bounds;
- wheel/primorial recursion;
- generic cyclic-word/state-complexity machinery;
- practical factor-discovery/proved-factor backends such as FLINT/PARI.

These remain `CLASSICAL_BASELINE` or `PRIOR_ART_ONLY`.

### Enterprise specialization

- exact `p^2` activation defect and future quotient;
- XOR separator geometry for primorial Boolean wheels;
- Jacobsthal branch-and-bound for exact phase-separation certificates;
- task-relative prime-extension safety of the pair-separator carrier;
- storage/observation-depth and static/dynamic-closure separations.

### Live theorem/boundary frontier

- `R005A-BOOL-DOM`: exact equality `H_U^actual(q)=rho(q#)` for all prime `q>=7` remains `CONJECTURAL`, now verified through `q=23`.
- scalable post-23 exact computation should adapt paired/wheel recursion rather than materialize the full primorial word.
- any generic safe-quotient statement routes to the existing precision/Foundation owner rather than being duplicated here.

## 9. Executable evidence

`experiments/r005a_boolean_rho23_certificate.cpp` is a deterministic exact certificate.

It:

1. recomputes all nine Jacobsthal caps for `23#`;
2. verifies the gap-536 singleton-23 candidate;
3. exhausts all 7428 residual CRT shifts after exact cap pruning;
4. certifies `rho(23#)=535`;
5. checks the transient defect frontier and finite transient/transient pairs;
6. certifies `H_U^actual(23)=535`;
7. exhaustively checks the 2-state-versus-4-state p-extension signature boundary on the four local pair states.

Local optimized run command:

`g++ -O3 -march=native -fopenmp -std=c++20 experiments/r005a_boolean_rho23_certificate.cpp -o /tmp/r005a_boolean_rho23_certificate && OMP_NUM_THREADS=8 /tmp/r005a_boolean_rho23_certificate`

Local result:

`rho23_exact gap=536 rho=535 candidate_d=19399380 residual_ts_best=213 tt_best=15 full_actual_H=535`

`CI_NOT_REQUIRED_FOR_RESEARCH`.
