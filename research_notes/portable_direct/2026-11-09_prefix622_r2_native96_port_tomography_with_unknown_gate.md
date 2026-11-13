# PREFIX-622-R2 — Native 96-port tomography from robust phase sensors and a sharp unknown-terminal-gate witness

2026-11-09 (Asia/Shanghai). Author-side exact theorem, original-native 576-action rational checker executed. Independent mathematics review pending.

**Frozen scientific input**: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`; weights `(1,1,1,1,0,0)`. Original 48 signed STAR phases; 96 current bit ports, 576 distinct typed transition actions. The four-point phase input is `d=e4+e11+e14+e32` (zero-based). Parent verified author-side records are PREFIX-597 (full current 96-port instant decoder, PR #1807, `1a09403fe0647fbfbf8ad37ca32b60283e270bfb`) and PREFIX-621 (6/8/14 phase sensors, PR #1860, `caf83e99db2395fa96f03e2d772dd322b1fa1130`), with author-side review statuses preserved.

## Observers, state, and exact operations

Let `A(z)` be the original native 96-port typed BRC transition with the specified six weights, and `Q(z)` its positive 48-phase tail transition. `C` is the PREFIX-597 96-to-48 current phase readout: ordinary phase bit-pairs are summed; at marked phase `g=4` the first bit is selected. Its original native tail decoder `D_z` satisfies `CD_z=I` and, after at least two native steps, `r=D_z(Cr)`. The terminal gate parameter is `z`; it is an operation parameter, not a sensor coordinate.

Choose original native input `r_0=E(λd)`, with the canonical original embedding `E` (the marked phase has equal bit ports). Apply initial native gates `a,b`, then `q_1,...,q_t`, all nonnegative, with unknown `λ>0`. The terminal 48-phase sum is

    v_t = λ Q(q_t)...Q(q_1)Q(b)Q(a)d.

The associated original current native port state is `r_t` after `t+2` actions. The time index `t` is known, and `z_t=q_t` if `t>=1`, or `z_0=b`.

PREFIX-597 provides the exact local repair formula, with `H={3,14,15}`:

    L(v)=v[3]+v[14]+v[15]-2v[2],
    δ=(z-1)L(v)/(3(z+3)),
    r[g,0]=r[g,1]=v[g],
    r[i,0]=(v[i]-1_{i∈H}δ)/2,  i != g,
    r[i,1]=(v[i]+1_{i∈H}δ)/2,  i != g.

All denominators are strictly positive for `z>=0`. These formulas are *original 96-port endpoint state* identities and preserve the bit-port readout of the 576 typed actions; they make no statement about ordered ancestral route identities.

## Theorem 622.1 — exact 96-port terminal reconstruction at the same sharp fixed phase sensor counts (current gate known)

If `z_t` is provided, PREFIX-621's fixed phase sets reconstruct the complete original current 96-port `r_t` for arbitrary nonnegative gates, unknown `a,b,λ`, and every `t>=0`:

* `S6={14,3,40,26,27,4}` without erasure (from PREFIX-620);
* `S8={3,4,5,14,17,26,27,40}` after any one known missing phase reading;
* `S14={2,3,4,5,14,15,17,26,27,29,38,39,40,41}` after any two known missing readings or one unknown-location arbitrary corruption.

For `t>=4`, the minimum number of fixed *distinct original phase-coordinate* sensors for these three contracts is, respectively, **6, 8, 14**.

**Proof.** The PREFIX-621 exact sensor decoders reconstruct `v_t`; apply the displayed `D_{z_t}` to recover all 96 ports. Conversely, `C D_z=I` implies that any observer reconstructing the current 96-port vector also reconstructs `v_t`. Therefore the original phase-sensor-class lower bounds of PREFIX-620/621 transfer without a new rank hypothesis. The correction and erasure guarantees transfer by composition. ∎

## Theorem 622.2 — an exact equal-phase / unequal-port history pair when the terminal gate is unobserved

For `t=3` set `λ=1,b=1,q_1=q_2=1`. Consider the two legitimate original native histories

    A: (a,b,q1,q2,q3)=(1,1,1,1,2)
    B: (a,b,q1,q2,q3)=(2,1,1,1,1).

Both produce **exactly the same 48-phase vector**, whose 14 nonzero entries are:

    (index:value) =
    (3:80),(4:16),(5:64),(14:80),(15:80),
    (17:32),(26:32),(27:64),(28:32),(29:64),
    (38:32),(39:64),(40:32),(41:32).

Nevertheless their current native 96-port states differ at exactly six bit coordinates `{6,7,28,29,30,31}`. In history A the three marked-predecessor bit pairs (phase indices 3,14,15) are all `(32,48)`; in history B all three are `(40,40)`.

**Proof.** The eight-state exact nonnegative representation from PREFIX-617/621 has an autonomous 4-cycle `w'=(4(q+3)w_3,w_0,w_1,w_2)`, initial `w=(λ(b+3),λ(a+3),λ,λ/2)`, and a gate-independent `c` component. At `t=3`, `w_0=4(q_3+3)λ(a+3)`, so swapping `a=1,q3=2` and `a=2,q3=1` preserves every `w` component and therefore the full 48-phase state. In this state `L(v)=240`. The current terminal gates 2 and 1 give respectively `δ_A=16` and `δ_B=0`, by the native decoder above. All three H bit pairs separate as stated. The original-native 576-action script independently realizes the pair from `E(d)`; all 48 entries coincide and exactly these six ports differ. ∎

This construction generalizes to every `t>=3`: the gate `q_t` shares a single four-cycle product with an earlier gate factor (for `t=3`, `a`; `t=4`, `b`; `t>=5`, `q_{t-4}`). Swapping the values 1 and 2 between that earlier gate and `q_t`, while holding all other gates and `λ` fixed, leaves all four final `w` components and all 48 phase outputs unchanged, but changes `δ`, since `L(v)=3w_0>0`. Thus **even complete 48-phase observation cannot uniformly reconstruct current 96 ports without a terminal-gate datum** on this family for any `t>=3`.

This is a typed original-native endpoint residual, rather than a claim of persistent ordered-history memory after a common next gate: the two port states become identical after a common subsequent native gate once their phase sums and marked bits coincide.

## Theorem 622.3 — exactly one current original port-bit reading repairs the missing terminal gate

Suppose the complete `v_t` is reconstructed, but `z_t` is not supplied. One further native port coordinate `r[t,3,1]` suffices for all `t>=0`: put

    δ = 2*r[t,3,1] - v_t[3],
    r_t = D(v_t,δ).

This reconstructs all 96 port coordinates without knowing `z_t`. Furthermore, since

    L(v_t)=3*w_{t,0}>0

for every `λ>0` and all nonnegative gates in the four-point probe, the actual current gate is itself uniquely recoverable:

    z_t=(L(v_t)+9δ)/(L(v_t)-3δ),

where `L(v_t)-3δ=4L(v_t)/(z_t+3)>0`.

**Proof.** The port decoder gives `r[3,1]=(v[3]+δ)/2`; this determines `δ` directly. Substituting `δ=(z-1)L/[3(z+3)]` yields the displayed gate inverse. Theorem 622.2 proves that **zero extra non-phase measurements** are insufficient for uniform complete port reconstruction for `t>=3`, even when all 48 phase readings are available. Hence one additional original port-bit reading is sharp as a repair count *given the complete phase state*. ∎

In particular, `S6/S8/S14` plus this one port coordinate gives constructive erasure/corruption-robust complete 96-port readout without current-gate calibration. The cardinalities `6+1,8+1,14+1` are constructive configurations, not a joint optimality claim over all possible mixed port/phase sensor sets.

## Exact execution certificate

The attached standard-library checker reconstructs the original four STAR triples, enumerates 48 phases and all 576 typed port actions, and uses rational arithmetic throughout. It independently propagates native 96-bit-port vectors and 48-phase sums under nonstationary nonnegative original gates. Executed checks include:

* 52 rational gate histories (4 initial parameter configurations × 13 lengths `t=0,...,12`);
* 249,600 exact phase-coordinate comparisons and 504,192 exact native-port-coordinate comparisons;
* 5,200 exhaustive relevant fixed-set erasure reconstructions (S6 none, S8 one, S14 two), each with one-raw-port-bit repair and terminal-gate inversion;
* the explicit equal-48 / unequal-96 native witness, including all six differing bit coordinates.

All executed assertions passed. Infinite-time assertions follow from the exact predecessor matrix identities and four-cycle product structure; the finite computation checks their original typed implementation. Results are in `PREFIX622_native_port_tomography_results.json` and executable source `PREFIX622_native_port_tomography_checker.py`.

**Scope and next question.** This establishes full *current original native port-state* reconstruction for the four-point family. Full ordered 576-action provenance and ancestor/path multiplicities remain a distinct observer language. The next task is to construct a tagged-path statistic distinguishing two native histories with the same current 96 ports, or prove the exact no-history language under which the reconstructed endpoint state is a sufficient quotient. The mathematical statements here are author-side and await independent Driver review; no formal CLAIM, Result, or Foundation admission is asserted.
