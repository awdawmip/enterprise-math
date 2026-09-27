# Public witnesses for more than one uniform terminal bit

Status: proved and bounded actual execution, shared-context author evidence; not independent admission. Project snapshot `671530e485921a9eeed91c1635decd60cc195dc3`; native activity `RA-CAAAC604CB513AEA8BBC1DFC`. This directory composes the existing typed arithmetic and admitted full native instrument. It does not introduce an ideal propagator, alter the fixed phase bank, compute a factorization/order, or drop residual coordinates.

## 1. An executable public power-sum witness

Let `N >= 3` be odd, `1 <= a < N`, and let `ell >= 1`, `u,v > 0` be public integers satisfying

\[
 \gcd(u,v)=1,\quad u\not\equiv v\pmod2,\quad
 N=u^{2^{\ell-1}}+v^{2^{\ell-1}},\quad J(a,N)=-1.
\]

Then `a` is a unit modulo `N`, and

\[
 2^\ell\mid\operatorname{ord}_N(a).
\]

**Proof.** For each prime `p | N`, primitiveness implies `p` divides neither `u` nor `v`. The ratio `x=u/v` in the field modulo `p` satisfies `x^(2^(ell-1))=-1`. Because `p` is odd, the order of `x` is exactly `2^ell`: its order divides `2^ell` but not its half, and all divisors of this power of two form a chain. Consequently `2^ell | p-1`.

The Jacobi symbol is the product of prime Legendre symbols, with their multiplicities. A negative product contains a prime of odd multiplicity at which `a` is a quadratic nonresidue. In the cyclic group of order `p-1`, write `a=g^k`; a nonresidue has odd `k`. Therefore the two-part of `ord_p(a)` equals the two-part of `p-1`, which is at least `2^ell`. Reduction modulo `p` makes `ord_p(a)` divide `ord_N(a)`. This proves the assertion without obtaining any of those primes or either order. The definition and multiplicativity of the Jacobi symbol are standard; see [NIST DLMF 27.9](https://dlmf.nist.gov/27.9).

`power_sum_certificate.py::certify_power_sum_structure(N,a,ell,u,v)` implements the displayed witness. The squares, sum, comparisons, gcd and Jacobi reductions retain actual full-adder-column arithmetic traces. `verify_power_sum_structure` rebuilds and compares the entire certificate, including source pins. A nonnegative Jacobi symbol returns `UNAVAILABLE`, without a claim that the actual suffix is nonuniform. Malformed structural witnesses are rejected.

This is a sufficient condition. Primitiveness is deliberately required by this interface; there are valid nonprimitive examples outside its scope. Finding such a public representation of an arbitrary input is not supplied for free.

## 2. Why all certified suffix rounds can omit row queries

Use the original actual program, canonical initial work label `1`, its complete reverse-square modular schedule, and the original complete internal vectors. No arbitrary intermediate state is accepted. `certify_program_suffix` obtains these bindings from the existing actual `certify_program_final_bit` adapter and adds the public order-two-part lower bound. Its verifier rebuilds both witnesses.

For the proof alone put `r=ord_N(a)` and `q=2^ell`; the algorithm is not given `r`. Since `q | r`, the map

\[
 \chi:\langle a\rangle\longrightarrow\mathbb Z/q\mathbb Z,
 \qquad \chi(a^j)=j\bmod q
\]

is well-defined. This is an abstract support invariant, **not an implemented algorithm for recovering a color from an arbitrary bare work label**.

Before the last `ell` rounds, every scheduled exponent is a multiple of `q`, so every possible reachable work label has color zero. After `j` of the last `ell` rounds (`0 <= j < ell`), the support colors lie in the subgroup of multiples of `2^(ell-j)`. The next modular multiplier adds color `2^(ell-j-1)`. Its translate and the current support envelope are disjoint. This follows for every reported-bit history, since a branch only combines the current envelope with that translated envelope; cancellation can remove labels but cannot create a label outside the union.

Let `v_w` be a complete raw internal row at a positive-mass history, `M=sum_w ||v_w||^2`, and let `P,T` be the next actual work permutation and full internal isometry. The two children have rows

\[
 v'_{\sigma,z}=(v_z+\sigma T v_{P^{-1}z})/2,\qquad \sigma\in\{+1,-1\}.
\]

Disjoint support makes at most one of the two summands nonzero, including all residual coordinates. Therefore

\[
 \Pr(\sigma,z\mid h)
 =\frac{\|v_z\|^2+\|v_{P^{-1}z}\|^2}{4M}.
\]

If the incoming latent label has law `Pr(W=w | h)=||v_w||^2/M`, a fair auxiliary coin chooses `Z=W` or `Z=P W`. An independent fair reported bit gives exactly the displayed **joint** law. This renews the same latent invariant at the next history, so the shortcut applies at every one of the consecutive certified rounds. Equivalently, conditional on any reachable history before the suffix, the `ell` reported bits are uniform on all `2^ell` strings. This is stronger than a terminal marginal statement and requires no commutation between different `T` matrices.

The complete history and original row oracle remain necessary. Skipping the scoring query does not authorize replacing the postmeasurement field by a scalar or deleting internal phases. `PowerSumWalker` retains that oracle and all outcome history; full subsequent row reconstruction uses the original native recursion. It accepts no external initial field or private latent injection. The admitted program must stay unchanged. These are scientific execution contracts, not security against arbitrary hostile Python monkeypatching.

The support induction specializes the existing [Stage94 uniform-suffix proof](https://github.com/awdawmip/enterprise-math/blob/d8447e4dc9c6500720c671649798e4ae08df2ae2/research_notes/HEARTBEAT94_UNIFORM_SUFFIX_PROOF_20260926.md), Git blob `6d6552cdcfaa58a609d88b9582ef79bfa3ff0d82`. The new contribution here is an executable sufficient witness for its order divisibility premise, and integration with the exact single-walker joint law.

## 3. Executed evidence and costs

`check_power_sum_certificate.py` passed six structure cases and six complete replays:

| N | a | (ell,u,v) | certified bits | execution scope |
|---:|---:|---:|---:|---|
| 65 | 3 | (2,1,8) | 2 | full native t=4 tree |
| 85 | 2 | (2,2,9) | 2 | arithmetic certificate |
| 4097 | 3 | (3,8,1) | 3 | full native t=4 tree |
| 4294967297 | 3 | (6,2,1) | 6 | arithmetic certificate only |
| 18446744073709551617 | 3 | (7,2,1) | 7 | arithmetic certificate only |
| 65 | 2 | (2,1,8) | 0 / unavailable | arithmetic certificate |

The two full native trees contain 30 positive prefixes and 52 certified fair child edges. Their total terminal masses are exactly one. Seventeen malformed/tampered input and program controls were rejected. Initial generation of the six structure certificates replayed 4,782 full-adder digits; the complete fixture, including bank verification and actual full instrument execution, used 244 native core calls. Counts of native calls and replayed typed digits are separate resource units. The large Fermat-shaped inputs are **not** large-width native-sampler executions.

`check_power_sum_walker.py` then compared the full joint `(next reported bit, next latent label)` law against every one of those 52 native children, using complete 61-component rows and the actual positive-path observer. Eight baseline/shortcut pairs used the same full random tapes. All selected histories and latent labels agreed. Before the suffix, each shortcut oracle's budget was capped at its then-current cache size: all consecutive suffix steps performed zero point queries. Restoring the budget afterward reconstructed every retained complete terminal row and all 61 components in all eight runs. Unavailable-certificate fallback agreed with baseline; an interrupted auxiliary coin was retained across live continuation; a tampered certificate could not shortcut; external latent injection was rejected. This checker used 1,663 native core calls over its entire fixture, not zero arithmetic work.

Artifacts and exact pins:

| artifact | SHA-256 |
|---|---|
| `power_sum_certificate.py` | `8748aa22a76eb7b3fab557b613db1c1d594a19bdac8289934dc0d621b59af9a7` |
| `check_power_sum_certificate.py` | `53572083411ae06b1a44b7e70dbd6e943292cf1667f351249d204ea8021f54a2` |
| `POWER_SUM_CERTIFICATE_RESULTS.json.gz` decompressed payload | `1ab0f8a6c0b06d7495038e00be32fe434881c941e480a5049e8a1aa2664e400c` |
| `power_sum_walker.py` | `0058ace802972ebd8460db28550a57f40c01f1524b0018f5b4f5a5449921e091` |
| `check_power_sum_walker.py` | `efa8d62e1cba5cc24840b52e001fef25e988134a24d581895870dc198dc992ce` |
| `POWER_SUM_WALKER_RESULTS.json.gz` decompressed payload | `3f7f4b62675b94b7627b824c99f04f5a84bf7f325dcf2de80926f42c36e46e2d` |

For `n=bit_length(N)`, repeated squaring uses `O(ell n^2)` schoolbook typed digit work on valid inputs; conservative Euclid/Jacobi bounds are polynomial in `n`. The existing full schedule certificate, its inverse proofs, phase-bank construction, and every fresh replay are additional costs, recorded rather than treated as free. The walker currently revalidates the full certificate at each eligible step. Row queries outside the certified suffix can still be exponential.

An integer power-sum witness has an intrinsic limitation: one of `u,v` is at least two, so `2^(ell-1) < log2(N)`. Consequently this construction certifies at most `O(log n)` bits, even though the allowed witness family is unbounded. It does not make the whole Shor simulation polynomial, and the existence of a witness does not make finding one cheap.

## 4. Informative limits on other character routes

**The modulus congruence alone is insufficient.** `N=21` is `1 mod 4` and `J(2,21)=-1`, but the actual typed witness `2^6=1 mod 21` rules out `4 | ord_21(2)`. This finite power equality is in the first result payload; no order search or ideal QFT reference was executed.

**Odd-exponent extraction from the same base often has already answered the factoring question.** Suppose public odd `e` makes `g=a^e` have exact order `2^ell`. Writing `ord_N(a)=2^s d` with `d` odd shows `s=ell` and `d | e`. Thus the top involution is `g^(2^(ell-1))=a^(ord_N(a)/2)`. If it is not `-1`, its difference from one has a proper gcd with odd `N`; if it is `-1`, this is a bad base for the usual Shor half-order split. This can be a useful certificate, but its discovery cannot be counted as a free general higher-character oracle. This observation does not apply to an independent publicly supplied root witness for a different unit.

**CRT and small divisors need honest discovery costs.** A known proper divisor can support a component character, but it has already split the input. The remaining cofactor must still be handled. Likewise an even modulus already exposes factor two. Reducing a canonical residue modulo an unrelated small integer is generally not a multiplicative character modulo `N`: wrapping by `N` changes that smaller residue. If every prime divisor of an odd modulus is `3 mod 4`, its unit group's two-primary part has exponent two, so no character onto a cyclic group of order four is possible. This is a symbolic limitation, not a supplied factorization used by our algorithm.

**Gaussian quartic symbols offer a different implementation route when a public norm representation is available.** For a primitive representation `N=u^2+v^2`, a quartic Jacobi character with Gaussian denominator `u+iv` can give an actual four-color evaluator; on rational numerators its square is the ordinary Jacobi character. Polynomial Euclidean algorithms for the quartic Jacobi symbol are described by [Bach and Sandlund, *On Euclidean Methods for Cubic and Quartic Jacobi Symbols*, section 7](https://arxiv.org/abs/1807.07719). No Gaussian arithmetic or quartic-symbol implementation was executed here. Our suffix certificate avoids needing a bare-label character evaluator. General higher residue symbols and the required public representations remain separate algorithmic obligations.

## 5. A separate generalization to modular root witnesses

The equality witness can be replaced mathematically by a public independent unit `b` with `b^(2^(ell-1))=-1 mod N`, together with the same negative Jacobi symbol of the Shor base `a`. For every prime divisor the order of `b` is exactly `2^ell`, so the first proof applies unchanged. This need not obey the integer power-sum restriction `ell=O(log n)`; locating such a root is nevertheless not solved. A separate module and execution report are required so the frozen evidence above is not retroactively attributed to this stronger interface.

There is also classical information in this promise: all prime factors are `1 mod 2^ell`. Trial division therefore only needs candidates `1+j*2^ell` up to `sqrt(N)`, at most `floor((floor(sqrt(N))-1)/2^ell)` divisions. If the promised minimum possible prime factor exceeds `sqrt(N)`, the input is already certified prime. Savings from a large public root witness must be compared against this structure, not presented as a uniform complexity breakthrough on unrestricted inputs.

Global-Knowledge-Sync: main@f44ed59 / GLOBAL_KNOWLEDGE_V1
