# Fixed K33 with the original CF-only postprocessor: pure power-of-two orders

Status: DIRECTED AUTHOR DERIVATION / UNREVIEWED / NOT ADMITTED.

Researcher: `EM-DIRECT-C6438C`; activity: `RA-CAAAC604CB513AEA8BBC1DFC`.
Research session: `MCP-9e0873ae3aae418192f81173029434e7`.
Registration Source: `f0e5fb6f478a5a380ab5a7533d2585f7f43ee3bf`.
Frozen executable source: `0852cad130c1d877174d235687cf60c19f318c58`.

This is a new symbolic result for the original CF-only algorithm. It does not change any published file in `completion/` or `support/`, does not use the hybrid candidate fallback, and does not constitute independent review or admission. No new state propagation, ideal QFT reference, order search, or numerical phase computation was executed for this note.

## 1. Result and exact scope

Let `N>=3` be odd and let `a` be a unit modulo `N`, with true order `r=2^s`, where `s>=1`. The order is an analysis variable and is never supplied to the algorithm. Set `Q=2^t` and suppose `t>=s`. The actual factorization entry point handles even `N` by its factor-2 precheck before this path.

For the proven streaming branch recurrence with initial state `|work=1> tensor e0`, any complete real orthogonal phase maps in the prescribed history-controlled positions, and the unchanged frozen CF-only postprocessor, the following hold:

1. Every output of positive probability is divisible by `2^(t-s)`.
2. The total probability of outputs whose reduced fraction `k/Q` has denominator exactly `r` is **exactly `1/2`**.
3. If `a^(r/2)` is neither `+1` nor `-1` modulo `N`, CF-only produces a proper factor with probability **exactly `1/2`**. Its successful verified returning exponent is `r`.
4. If `a^(r/2)=-1 mod N`, CF-only produces no factor. Minimality of `r` already excludes `a^(r/2)=+1`.

The theorem therefore applies to the actual K33 bank, including its full-dimensional identity tail and all retained residual modes, with no small-error or increasing-precision hypothesis.

The current executable constructors in `integration/general_streaming.py` and `integration/general_driver.py` require **even `t>=2`**. Consequently the implemented contract here covers every **admissible even** `t>=s`, in particular the default `t=2 ceil(log2 N)` and every larger even width. The recurrence proof itself has no parity requirement, but odd-width calls are currently rejected: this note does not silently change that interface or claim a new odd-width equivalence to the old Stage80 preparation.

For `t>=2 ceil(log2 N)`, the mathematical inequality `t>=s` follows from `r<N` for a unit modulo `N>=3`. Thus there is no large-width or large-order obstruction for the pure power-of-two class within the actual even-width contract.

## 2. Actual algebra used

The source is the previously proved exact terminal-instrument transformation in:

- [STREAMING_SHOR_PROOF.md](https://github.com/awdawmip/enterprise-math/blob/b6625778e869511d85a202a0839eb105a197659e/research_notes/directed_recovery/20260926_0C08F0/math_route/STREAMING_SHOR_PROOF.md), Sections 5-8;
- `../integration/general_streaming.py` in Source `1fb7ff99d205f9ca03772942be64f732553dcd86`, the injected complete modular permutations;
- `../sparse/sparse_modular.py` in the same Source, `sparse_classical_postprocess`, which preserves frozen CF candidate semantics;
- frozen `stage78/shor_benchmark.py`, `denominators` and `classical_postprocess`.

Write `U|y>=|ay mod N>` on the valid work basis, with the padded labels fixed. The initial state remains in the orbit of `1`. At round `i`, whose measured bit is the bit of weight `2^i` in `k`, the actual work permutation is

`M_i = U^(2^(t-1-i))`.

For the already measured history `h=(h_0,...,h_(i-1))`, let `T_(i,h)` be the ordered product of the actual internal phase maps activated by the bits `h_c=1`. Its factors have phase index `m=i-c+1`. No reordering or commutation of those maps is assumed.

The exact unnormalized branch vector is

`v_(h b) = K_(i,h,b) v_h`,

`K_(i,h,b) = [I + (-1)^b (M_i tensor T_(i,h))]/2`.

Here `v_empty=|1> tensor e0`. All spectator and retained-mode details are already included in the exact macro proof. Since the complete actual `M_i tensor T_(i,h)` is real orthogonal,

`K_(i,h,0)^T K_(i,h,0) + K_(i,h,1)^T K_(i,h,1) = I`.

Hence the sum of the terminal descendant masses of any prefix equals that prefix's squared mass. This identity applies to the full mode vectors; projecting away residual modes would not justify it.

## 3. Forced zero prefix and the decisive fair bit

Put `i0=t-s`. For every `i<i0`, the exponent `2^(t-1-i)` is a multiple of `r=2^s`, so `M_i=I` on the entire orbit subspace. Inductively the previous measured history consists only of zero bits; therefore no phase is activated and `T_(i,h)=I`. Thus

`K_(i,h,0)=I`, `K_(i,h,1)=0`

on the current state. The first `t-s` low bits are forced zero, and the unnormalized state remains exactly `|1> tensor e0` with squared mass one. No phase approximation enters these rounds.

At round `i=i0`, the work map is the half-order involution

`J=U^(2^(s-1))=U^(r/2)`.

The prior history is still all zero, so `T_(i0,h)=I`. Minimality of the order ensures `J|1>` and `|1>` are distinct orthonormal work basis vectors. The two branch states are exactly

`v_0=(|1>+J|1>) tensor e0 / 2`,

`v_1=(|1>-J|1>) tensor e0 / 2`.

Their squared masses are both exactly `1/2`. In particular the decisive bit `h_(t-s)` is a fair bit in the actual complete fixed-word algorithm. Its fairness does not arise from replacing any fixed phase by an ideal rotation.

Later rounds preserve the prefix as a classical history. Instrument completeness gives total terminal mass `1/2` below each of these two prefixes regardless of later phase words or how many later branches have zero probability.

## 4. Why that bit is exactly the CF factor event

All possible output strings have

`k = 2^(t-s) l`, with `0<=l<2^s`.

The least significant bit of `l` is the decisive bit from Section 3. Thus

`k/Q = l/2^s`.

If that bit is one, `l` is odd and the reduced denominator is exactly `r=2^s`. A complete finite continued-fraction expansion of a rational includes its final reduced fraction. The frozen generator yields its convergent denominator `r`, because its cap is `N-1` and `r<=N-1`. Every earlier denominator is at most `r`; the occasional duplicate initial denominator `1` is harmless. None of the earlier smaller denominators can be a returning exponent: `a^q=1` implies `r` divides `q` by the definition of multiplicative order.

The original postprocessor therefore reaches and verifies `q=r`. It checks that `q` is even and then computes `h=a^(r/2)` and `gcd(h-1,N)`, `gcd(h+1,N)`. For a good base, `h^2=1 mod N` and `h` is neither `+1` nor `-1`. Each gcd is then proper: a gcd equal to `N` would make the associated sign equality hold, and a gcd equal to `1` would make that signed factor invertible, forcing the other signed factor to vanish modulo `N`. Therefore the returned factor set is nonempty.

If the decisive bit is zero and `k>0`, the reduced denominator is at most `r/2`. Every CF convergent denominator is no greater than that final denominator. Consequently none is a positive multiple of `r`, and every candidate fails the actual returning-exponent test. If `k=0`, the original explicit `ZERO_PHASE_RETRY` return applies. No output under the zero prefix factors through this CF-only route.

It follows that the factor event for a good base is exactly the decisive-one prefix, whose mass is exactly `1/2`. This proves both the positive lower bound and the claimed equality; merely pointing to one nearest ideal Fourier peak would not prove the equality.

If `h=a^(r/2)=-1`, even the only possible returning candidate `q=r` gives only gcds `1` or `N` (for the usual odd `N` order-finding input). For odd `N`, the bad-base success probability is therefore zero. The application already performs an even-`N` precheck, so this bad-base statement is scoped to that ordinary odd-`N` path.

At least one of the `2^(s-1)` outputs under the decisive-one prefix has probability at least `1/r`. This is a support existence consequence of the exact mass `1/2`, not a claim that every such output is positive or that all have equal probability.

## 5. When higher inaccurate phase words actually intervene

Index the active part by `j=i-i0`, so the first active round is `j=0` and the last is `j=s-1`. Every earlier bit with `c<i0` is zero, hence it never activates a phase. At active round `j`, a nontrivial history-controlled phase can therefore only have

`2<=m=i-c+1<=j+1`.

In particular:

- `j=0`: no phase acts before the decisive bit.
- `j=1`: only `m=2`, the exact complete quarter-turn, can act.
- `j=2`: `m=3` can first act; this is the first approximate phase word in the fixed bank.
- Across the entire run, only indices `m<=s` can be activated. Increasing `t` merely extends the forced-zero prefix; it does not introduce active indices beyond `s` for this order class.
- The K33 identity tail, `m>=33`, can first occur at `j=32`, and thus only if `s>=33`. It acts as the identity on the entire retained carrier and does not erase any existing residual component.

Approximate phases can change the individual probabilities of the remaining high-bit patterns. They cannot alter an already recorded low bit, the lattice `k in 2^(t-s) Z`, or the total mass in the decisive-one prefix. The theorem does **not** assert that the full distribution equals the ideal distribution or is uniform on the `r` lattice points for `s>=3`.

## 6. Limits, retry implications, and the remaining low-odd-part gap

For a fixed good base of pure power-of-two order and independent, completed samples, `R` repeated attempts have failure probability exactly `2^-R`. A finite external random-source failure is still an incomplete attempt and is not silently treated as a sampled terminal readout. For a randomized-base factorization driver, this result is conditional on selecting the stated order/good-base class; no assumption that this class occupies a uniformly positive fraction of all bases has been made.

The order-one case `r=1` is separate: the same induction forces every readout bit to zero and the CF-only output is a retry. The default base policy excludes `a=1`. The case `r=2` is included in the theorem: there are no later active phase rounds and the two possible outputs are exactly `0` and `Q/2`, each with mass `1/2`.

This closes `d=1` in the decomposition `r=2^s d`, not all cases with `phi(d)<=32`. For `d>1`, none of the initial pure power-of-two work powers is automatically a multiple of `r`; the forced-zero prefix proof fails. A rank-at-most-32 rational phase product may have cyclotomic eigenvalues of the low degrees involved, so the previous high-degree invertibility argument does not exclude a zero branch. Exact `m=2` structure and the actual selected higher words may still give a stronger theorem, but it requires an additional argument.

The precise remaining CF-only obligation for each such low odd part is to prove that, for every good permitted base and all supported widths, at least one terminal `k` with a returning even CF candidate and a proper half-exponent gcd has nonzero actual amplitude (and then derive a useful bound). Neither the identity-tail convention, orthogonality alone, nor this pure-two-power proof establishes that obligation for `d>1`.

Unknown `r` and `s` occur only in this proof. The actual algorithm still prepares from `N,a,t`, applies its certified modular columns and phase words, samples its actual readout, and checks the original CF candidates. No extra factor enumeration, order-dependent phase bank, or preselected successful readout has been introduced.

Global-Knowledge-Sync: main@441ebef / GLOBAL_KNOWLEDGE_V1
