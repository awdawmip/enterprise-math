# PREFIX-611-R2 — Two unknown native transient gates and all later gates recovered by one paired phase sensor

Date: 2026-11-09 (Asia/Shanghai). Status: AUTHOR-SIDE EXACT THEOREM + EXECUTED CERTIFICATES; independent Driver review pending.
Frozen scientific input: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Continuation: PREFIX-596 (96-port native-to-phase observer), PREFIX-602 (common 16D two-step tail), PREFIX-604 (12+4 split), PREFIX-609 (paired fixed sensor with **known** initial transient), and PREFIX-610 (single-run blind four-step residual).

## 1. Native carrier, experiment, and unknown parameters

Use the frozen 48 STAR phases, 96 native two-bit ports and 576 tagged actions, with fixed weights `(1,1,1,1,0,0)` and exact nonnegative phase-sum transfer `Q(q)` (PREFIX-602). Take an arbitrary **unknown** nonnegative 48-phase source `v`, and a second independently prepared source `v+u` with `u=ones(48)`. Give the two runs the **same** unknown ordered gate word
```
b, a, q_1, q_2, ..., q_n  (all >= 0).
```
Both gate parameters `b,a` of the initial two-step transient are unknown, along with all later `q_t`. Read only the *zero-based native phase-sum sensor 3* in each run immediately after gate b, immediately after gate a, and after each subsequent gate. Let `s_{-1},s_0,s_1,...,s_n` denote the exact **difference** of the two runs' readings at these moments. All native paths and their labels remain on the original source carrier; this result concerns one declared phase-sum observer.

## 2. Theorem 611.1: complete constructive identifiability

For every nonnegative source `v`, every `n>=0`, and every nonnegative gate word `(b,a,q_1,...,q_n)`, the `n+2` phase-3 contrast scalars uniquely determine every gate, by an explicit rational decoder.

First, direct evaluation in the **frozen original** 48-phase operator gives exact identities
```text
s_{-1} = (Q(b)u)[3] = b+7,
s_0    = (Q(a)Q(b)u)[3] = 3(a+7).
```
Thus immediately
```text
b = s_{-1}-7,              a = s_0/3-7.         (611.1)
```

Next use the same fixed 16D encoder `E,K,T,W,L,P` and gate-sensitive 4×4 transfer `B(q)` as PREFIX-602/604. The source increment after the unknown two-step transient, `d_0=Q(a)Q(b)u`, has the **all-parameter exact** sensitive coordinates
```text
c_0 = L K d_0 = ( 3(a+3)/2, (b+7)/2, 3/2, 3/4 )^T.     (611.2)
```
For the complementary gate-free vector `f_0=(I-P)K d_0`, direct exact polynomial evaluation gives
```text
(ET^j f_0)[3] = 12 * 2^j, j=0,1,2,3.
```
Because `T^4 f_0=16 f_0`, the gate-free phase-3 contribution for **every** subsequent integer time `t>=0` is `12*2^t`, entirely independent of a and b.

With `c_t=B(q_t)c_{t-1}` and the phase-3 reconstruction row `(EW)[3,:]=(2,0,0,0)`, the sensor at later time t satisfies
```text
s_t = 12*2^t + 8(q_t+3)c_{t-1,3}  (t>=1),
q_t = (s_t-12*2^t)/(8*c_{t-1,3}) - 3.                (611.3)
```
After each recovery update `c_t=B(q_t)c_{t-1}`, and repeat.

For a,b>=0, every coordinate of c_0 in (611.2) is strictly positive. Since B(q) is a positive weighted permutation when q>=0, every denominator `c_{t-1,3}` is strictly positive. The decoder therefore works for arbitrary length and for gate values 0 and 1 as well as positive rational or real gates. Uniqueness follows inductively from the displayed identities. QED.

The same local Jacobian yields a sharp observation-dimension statement: on the open parameter domain `a,b,q_1,...,q_n>0`, the map to `(s_{-1},s_0,s_1,...,s_n)` is lower triangular by time, with diagonal entries `1, 3, 8c_{0,3}, ...,8c_{n-1,3}`, all nonzero. Any differentiable exact encoding into k real scalars with differentiable recovery of all n+2 independent gates requires `k>=n+2` by the chain-rule rank; the construction reaches this bound in **contrast scalars**. Its experimental raw-reading cost is `2(n+2)`, due to the two synchronized runs.

## 3. Why this advances the unknown-transient frontier

PREFIX-609 required the known transient `Q(0)Q(1)`. Here the transient is the two-parameter family `Q(a)Q(b)` with both a,b unknown. Two early measurements of the same sensor calibrate the transient; the gate-free sensor component remains `12*2^t` for the known uniform difference input under *every* a,b. Thus the later recursive single-phase decoder needs neither the original source v nor knowledge of a,b before those two observations. The result applies to one known differential input `u=ones(48)`, not arbitrary unknown control injection; synchronization of the same unknown gate word across the two runs is a theorem hypothesis.

## 4. Exact native arithmetic execution and example

The stand-alone companion code constructs the actual 48 STAR phase ordering and transfer, then its exact 16D common tail and 12+4 split. It verifies the symbolic b/a identities and the four rational polynomial entries of c_0, plus the first four gate-free observations. SymPy's exact algebra and `T^4=16I` prove the all-time formula.

Actual executed coverage: **4** distinct nonnegative initial transient pairs (including exact rational), **3** arbitrary unknown nonnegative source vectors and **3** gate words, for **36** full paired experiments. It recovered **480** subsequent gates exactly, checked **1,728** full 48-phase initial differential coordinates, and verified **1,104** nonnegative full phase states. All assertions passed.

For example, `(b,a)=(1,2)` gives `s_{-1}=8`, `s_0=27` and `c_0=(15/2,4,3/2,3/4)`. If `q_1=0`, then `s_1=12*2 + 8*3*(3/4)=42` and (611.3) recovers `q_1=0` exactly.

Code: `PREFIX611_R2_unknown_twostep_single_sensor_checker.py`; executed results: `PREFIX611_R2_unknown_twostep_single_sensor_results.json`.

## 5. Reuse, cost, and next question

Applied exact original `Q` and prior 16D and 12+4 BRC interfaces (`COMPOSE_APPLIED`); this is a new all-parameter inverse statement for the unknown **two-gate** transient family, not a new primitive dynamics or a complete labeled-port observer.

The remaining useful extension is to allow an **unknown initial input difference**, or two trajectories that do not share an exactly identical gate word, and characterize the gauge/identifiability after extra excitation or calibration. Separately benchmark actual original 96-port source preparation, two-run synchronization, big-integer arithmetic, and complete observer recovery costs; the n+2 bound is about differentiable contrast dimension only.

Persistence: author-side proof and exact checks; independent Driver review, Native Result/CLAIM and Foundation admission retain their own authorities.
