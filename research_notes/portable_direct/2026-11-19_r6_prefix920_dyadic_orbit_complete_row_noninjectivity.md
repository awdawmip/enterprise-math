# PREFIX-920 — Dyadic residue orbit and complete named-collision witness census for one 19-bit modulus row

Date: 2026-11-19 (Asia/Shanghai). Lane: 进取数论研究6. Status: AUTHOR_PROVED / EXACT_FINITE_COMPUTED / DIRECT_WITNESSES_AUDITED / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.
Frozen scientific input: `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Direct mathematical dependency: `research_notes/portable_direct/2026-11-19_r6_prefix919_complete_zero_one_flip_collision_mass.md`. This is the auxiliary named-XOR two-port observer, with no assertion of X6-native dynamical equivalence.

## Theorem A. Sharp zero-flip support and parity

For `p>=2,N=2^p`, odd `a,b>1`, define named traces `Z_x=(x,x)` and `F_x^i=(x,x xor 2^i)` where `0<=x<N, 0<=i<p`, retaining type, start and source-bit identity. Observe `(start mod a,end mod b)`. Let `M_01(p,a,b)` be unordered collisions with exactly one zero-step and one flip.

Define `H=2^i`, `G_i(A)=floor(A/(2H))*H+max(0,(A mod 2H)-H)`, the exact bit-i one count in `[0,A)`. If `gcd(a,b)>1`, `M_01=0`. Otherwise let `q_i=(H*a^{-1}) mod b`, uniquely represented in `[1,b-1]`, and put `K=floor((N-1)/a)`, `K_i^+=floor((N-1-H)/a)`. For every `0<=i<p`, the following disjoint lists contain every positive mixed-collision mass exactly once:

* Minus: `k=q_i+tb`, `t>=0`, `1<=k<=K`; mass `w_-=N-2 G_i(ka)`.
* Plus: `k=b-q_i+tb`, `t>=0`, `1<=k<=K_i^+`; mass `w_+=N-2(ka-G_i(ka))`.

Every listed mass is an even positive integer (at least 2); their sum is exactly `M_01`. The simple actual named witnesses are respectively `F_0^i=(0,H)`, `Z_(ka)=(ka,ka)` (end difference `ka-H`), and `F_H^i=(H,0)`, `Z_(ka+H)=(ka+H,ka+H)` (end difference `ka+H`). Both satisfy the start difference `ka` and exact divisibility by `b`.

Proof: PREFIX-919-B partitions mixed pairs according to `b|(ka-H)` or `b|(ka+H)` with respective mass `N-ka+tau_i(ka)` and `N-ka-tau_i(ka)`; `tau_i(A)=A-2G_i(A)`. Solving each congruence modulo `b` produces the two progressions above, and substitution gives the displayed bit-population weights. Since `ka<N`, `G_i(ka)<N/2` and `w_->0`. The last bit-i zero in `[0,N)` occurs at `N-H-1`, so `ka-G_i(ka)<N/2` exactly when `ka+H<N`; this proves the sharp plus cutoff. The derived formulas imply evenness. If `gcd(a,b)>1`, any such divisibility would force an odd common divisor to divide `2^i`, impossible. This proves exhaustive support, sign disjointness and parity.

If `K<b`, the two progressions have at most one member each and `q_(i+1)=2q_i mod b`; consequently `M_01=0` iff all `p` orbit points avoid `q_i<=K` and `b-q_i<=K_i^+`. For strict 19-bit odd `a,b` and `p=32`, `K<=16383<b`: 32 doubling steps and at most 64 cutoff comparisons decide the exact mixed-zero property. Boolean support discards named-source multiplicity; the weights above retain it.

## Complete strict-19-bit fixed-b census

Exhaustively enumerate `a=262145,262147,...,524287` (131072 distinct values) at `p=32,b=440665`. The exact mixed-type row partition is:

| Coprime/branch status | Count |
|---|---:|
| Noncoprime (mixed=0) | 29634 |
| Coprime, mixed=0 | 39554 |
| Coprime, plus only | 25153 |
| Coprime, minus only | 26051 |
| Coprime, both signs | 10680 |
| Total | 131072 |

Hence exactly `61884` of the `101438` coprime row entries have mixed collisions. The exact sum of mixed *trajectory-pair multiplicities* over all row observers is `361954708038288`: plus-branch `175192787840598`, minus-branch `186761920197690`. Maximum row mass is `67104018732` at `a=309593`. PREFIX-919 anchor `(a,b)=(321651,440665)` is reproduced with `M_01=59007025662` and 17 minus fibers.

The coprime pair `(262151,440665)` has zero mixed collisions; this supplies an exact counterexample to universal mixed-type collisions, but it has an explicit *two-flip* collision:

`F_1^0=(1,0)` and `F_4140937197^13=(4140937197,4140929005)`.

Start gap `4140937196=15796*262151`; end gap `4140929005=9397*440665`. All four endpoint states lie in `[0,2^32)`.

## Theorem B. Full-row noninjectivity certificate

**Every** strict-19-bit odd `a` in `[262145,524287]` gives a noninjective named zero-or-one XOR trajectory observer `(a,440665)` at `p=32`.

Certificate construction: for each row element first use the zero/zero collision `Z_0,Z_lcm(a,b)` when `lcm(a,b)<2^32`; otherwise use Theorem A's explicit mixed witness where the modular orbit hits; otherwise enumerate all `(i,j,eps,eta)` with `0<=i,j<32`, `eps,eta in {-1,+1}` and exact congruence-compatible `1<=k<=floor((N-1)/a)` satisfying `ka≡eps*2^i-eta*2^j (mod b)`. For each viable `A=ka`, the separately published PREFIX-918 exact two-flip bit-window kernel identifies a permitted starting `x`; binary search the exact prefix kernel, then **directly validate** the real XOR endpoints `F_x^i,F_(x+A)^j` and their two observed congruences. All finite row values are covered by the source-level integer loop.

The complete census returns **1405** zero/zero witnesses, **61884** zero/flip witnesses and **67783** pairs with the first witness in the flip/flip class; **zero** rows without a collision. The C++ generator directly validates all returned named pairs; an independently implemented Python audit rechecks state bounds, source labels and both modular equalities on all **131072** printed witness lines, with zero violations. The ordered full-output ASCII SHA-256 is `1211ab3423d23ff1d88246bc1278db23022c9504bc0a0b33798c784be53366cc`. Independent exact mixed-mass row calculations additionally agree across modular doubling, port reversal and source-by-source inverse/bit-population routes, plus 255 complete small-observer brute-force cases. The mixed-mass row-lines digest is `6b39ed2f950118dbd2c542c6d2a78de54fa98ca20a5f88613699228cf094977d`.

Finite-scope conclusion: the entire `b=440665` strict-19-bit row is excluded as a source of injective auxiliary two-port observers. Other odd `b`, and native X6 geometry/dynamics, are not covered by this row theorem. Formal Result/reviewer/admission and Source Activity association are distinct actions.

## Replication and next question

The full executable reproducibility bundle has the Python exact orbit and independent residue recount, C++ full-row named-witness generator based on the frozen PREFIX-918 window kernel, and Python audit of every emitted witness. Compile C++17 `-O3`; redirect its stdout to a witness file and pass that file to the audit; Python 3 needs only its standard library. The exact row counts and digests above are the expected verification anchors.

Next discriminating unit: extend the directly validated complete-row witness census to further second-port moduli `b`, retaining the frozen observer and source labels; seek either a structurally explained universal collision mechanism or a certified injective auxiliary observer. The separate project mother question remains `B_fix,odd(32) in {19,20}`, with its exact frozen interpretation.
