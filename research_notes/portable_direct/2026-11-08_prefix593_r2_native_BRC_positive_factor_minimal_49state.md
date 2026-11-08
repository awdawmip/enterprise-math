# PREFIX-593-R2 — Native X6-BRC positive two-factor and minimal 49-coordinate linear future state

Date: 2026-11-08. Research role: `EM-DIRECT-EEAACA / TASK_RESEARCH`; native activity `RA-0EF8EF41E688E715E5CB9419`. Author-side proof with executed exact certificate; independent review pending. Frozen science: `enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`. Predecessors: PREFIX-585,586,587,588,589,591,592; original 48 native phases, 96 branch ports, 576 labelled actions and the three original gate edges are unchanged.

## Theorem 593.1: exact positive two-factorization over the labelled native BRC

Let `S` be the native 48-phase adjacency (three successors per phase), `R:(a,p,c)↦(a,c,p)` its exact native reversal, `X(x)` the original six-axis diagonal weight matrix, and `D(z)` the original bit-branch transfer (48 diagonal 2×2 blocks). Ordinary blocks of `D` equal `[[1,1],[1,1]]`; the unique marked gate-target block is `[[1,1],[1,z]]`. Hats denote phase-to-96-port lifts. The original 96-port transition is

`A(x,z)=X̂(x) Ŝ D(z)`.

The established identity `SR=W_phase` implies `W=Ŝ R̂`, where `W` is the block diagonal matrix with 24 blocks `J4-I4`. Since the four ports of each such block share one signed source axis, `W X̂=X̂ W`. Hence, exactly over `Z[x1,...,x6,z]`,

`E(x,z):=W^{-1} A(x,z)=X̂(x) R̂ D(z)`,  
`A(x,z)=W E(x,z)`,  
`T(x,z)=W^{-1}A(x,z)W=E(x,z)W`.

The seven coefficient matrices of `E=Σ_{a=1}^6 x_a E_a+x_1z E_gate` are disjoint {0,1} incidence arrays; their edge counts are `(31,32,32,32,32,32,1)`, hence 192 labelled edges, exactly two per row and two per column in the union. Every original coefficient column, restricted to any four-port W block, is either zero or exactly three ones and one zero, which are reproduced by the unique omitted-position indicator `E`; the gate triple remains a separate labelled coefficient. These are exact native relation identities, including zero and formal parameters.

**Corollary (one-step positive entry).** With the earlier integer transform `H=3 W^{-1}`, for each of the seven labelled generators `H A_k=3E_k≥0`. For every nonnegative original right endpoint `r` and any nonnegative axis/gate parameters,

`H A_1 r=3E_1 r≥0`.

Because each subsequent `T_t=E_tW` is nonnegative, there is no need for a signed dual split after this first original step. The whole arbitrary-length varying-weight evolution factors as

`A_d⋯A_1 r=W T_d⋯T_2 E_1 r` for every integer `d≥1`.

This applies to native linear port/path-weight observers with the original labels. It does not assert preservation of every individual, separately named source-bit itinerary.

## Theorem 593.2: 49-coordinate exact recurrence with all 96-port readouts

Let `g` be the original marked phase, `N(i)` the three original successors of phase `i`, `a(i)` its native signed axis index, and `η_i=[g∈N(i)]`. The original incidence has `η_g=0` and `Σ_iη_i=3`. For a sequence `r_t=A(x_t,z_t)r_{t-1}`, define at each `t≥1` the 48 bit-transfer sums and one gate difference:

`b_i(t)=r_{t-1,(i,0)}+r_{t-1,(i,1)}`,  
`δ_t=(z_t-1)r_{t-1,(g,1)}`.

All ordinary `D(z_t)` blocks have identical two output rows; the marked block contributes the sole independent difference `δ_t`. Put

`q_i(t)=x_{t,a(i)} Σ_{j∈N(i)} b_j(t)`.

The **entire 96-port original next vector** is recovered exactly as

`r_{t,(i,0)}=q_i(t)`,  
`r_{t,(i,1)}=q_i(t)+x_{t,a(i)}η_iδ_t`.

The 49 coordinates evolve without expanding 96 ports:

`b_i(t+1)=2q_i(t)+x_{t,a(i)}η_iδ_t`,  
`δ_{t+1}=(z_{t+1}-1)q_g(t)`.

The last identity uses `η_g=0`. Induction proves exactness at every `t≥1` for every initial port vector and every successive native parameter choice, including zero weights and `z=0`. `δ` may be signed when `z<1`, so this 49-dimensional representation and the positive 96-port factorization are distinct valid algorithms.

**Generic optimality, precisely scoped.** With all six axis weights nonzero and `z≠1`, `S` is invertible (native `det S=3^12` from PREFIX-586), `X` is invertible and `D` has 47 ordinary rank-one bit blocks plus one marked rank-two block. Consequently `rank A=rank D=49`. Any one-step *linear* sufficient intermediary `A=L R` that reconstructs every one of the 96 native port outputs for every original input must have `m≥rank A=49`. The recurrence attains this bound. At `z=1` with all axes nonzero the rank is 48. The optimality statement is restricted to exact linear future port observations, not full history/individual path reconstruction.

**Source information witness.** Two initial singleton inputs `e_(i,0)` and `e_(i,1)` at an ordinary non-gate phase are different source bits but produce the same bit-transfer 49-state encoding and the same future linear port observations. Anyone requiring the initial named bit or entire ordered itinerary must retain that source provenance separately. Original six-axis weight, gate label and final 96-port observations are retained. No physical-time or numerical-residual interpretation is claimed.

## Executed exact evidence and algorithmic accounting

`PREFIX593_R2_native_49state_cert.py` reconstructs original native BRC from the co-located source `PREFIX589_R2_dual_carrier_certificate.py`. It checks all 7×96×96=64,512 original/dual coefficient positions for both factor identities, all triple-block and labelled E-edge positions, and 3,168 full 96-port exact-integer equalities: 99 inputs (all 96 singleton ports plus 3 patterns), three genuinely varying/singular weight sequences, each checked at all specified depths. Executed result `ALL_ASSERTIONS_PASS_AUTHOR_SIDE_UNREVIEWED`. This finite certificate checks the implementation; the displayed matrix factorization and induction prove the arbitrary-length theorem.

For a basic weighted-edge model the native A has 576 original edge terms, while E has 192 and W has 288 unit entries. Evaluating W with one shared sum per four-port block takes (3 sums + 4 subtractions)×24 = 168 additions/subtractions. The factor method uses 192 weighted edge contributions plus 168 block operations per full vector. This is **not** a wall-time or asymptotic speedup claim: compare against a similarly optimized original `X S D` implementation, counting weight reuse, integer bit lengths, conversions, full readout and batch observers. The 49-state recurrence requires only 48 phase sums and one gate difference between steps, with exact full-state reconstruction when demanded.

## Next discriminating research unit

Implement three comparably optimized original native `X S D`, positive `W E`, and minimal 49-state recurrences, all with the same nonnegative original integer inputs and marked gate sequences. Report addition/multiplication and bit-length costs, full readout vs scalar observer vs repeated queries, and retain any source-bit history required by the chosen observer. Separately test a 49-coordinate positive two-stream lift for signed gate difference without replacing native provenance.

Native registration `EM-DIRECT-EEAACA` succeeded; formal task/owner CLAIM, native Result and independent review are separate and not asserted here.
