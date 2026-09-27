# Aggregate witness probes for the native symmetric branch kernel

Status: **SYMBOLIC_DERIVATION_AND_EXACT_SOURCE_SCOPE_AUDIT / NOT_EXECUTED / NOT_ADMITTED**. Author context: `EM-DIRECT-C6438C`, activity `RA-CAAAC604CB513AEA8BBC1DFC`. No scientific program, numerical search, provider query or remote operation was performed for this note. Source reads, symbolic derivation and this file write are the evidence. The frozen relative-port and conic experiments and their report remain unchanged.

The current parent objective is to complete the Shor objective along native BRC, using Enterprise geometry, Heartbeat World and new tools when necessary. This note studies a possible factor-witness component. Neither a short recurrence nor a specially constructed factor hit completes that parent objective. The question is whether preserving every first-hit branch law is unnecessarily strong when the required output is any verified proper divisor.

The answer is qualified: **the unstopped branch family has exact constant-size algebraic summaries, and gcd of a derived summary can be a sound weak certificate probe.** The first branch sum primarily restates a familiar order test. A second-moment determinant has additional polynomial factor sources and is not entirely that same test. Neither supplies a general useful success rate or total-cost guarantee yet.

## 1. Exact carrier and the changed output contract

Let `R=Z/NZ`, `N>1`, and let `a` have a paid unit certificate. For `t>=0`, put `Q=2^t`. Consider the **unstopped** four-alternative kernel

`prod_(j=0..t-1) (2 I + T^(2^j) + T^(-2^j))`,

starting from unit 1, where T multiplies the label by a. A microscopic branch is an ordered pair `(r,s)` with `0<=r,s<Q`; its unit label is `u=a^(r-s)`. Every microscopic branch has integer count 1. There are `Q^2=4^t` branches, including repetitions of the same residue. The two identity alternatives must retain their multiplicity.

Define the unnormalized ring-valued branch sums

`M_k(Q) = sum_(0<=r,s<Q) a^(k(r-s))`,

in particular `M_0=Q^2`, `S1=M_1`, and `S2=M_2`. The exact integer branch count can be retained separately; the value used in ring arithmetic is its residue modulo N. No division by `Q^2` is needed. In an even modulus this distinction matters because that count need not be a unit.

These summaries do not retain first-hit depth, the factor law, individual labels or path provenance. First-hit absorption would remove a state-dependent set of branches and break the displayed product recurrence. The proposed contract is instead:

`probe -> FOUND(d, exact divisibility receipt)` if `1<d<N`,

or `NO_FACTOR_FROM_THIS_PROBE`, or `UNKNOWN` if computation/verification is incomplete.

A unit probe value proves only that this value has gcd 1 with N. It does not prove that N is prime, that no branch has a proper gcd, or that no factor can be found. Gcd N is saturation, not success and not an emptiness certificate.

## 2. Ring-safe recurrences for the first two moments and determinant

At layer t let `c=a^(2^t)` and let `c^-1` be its certified inverse. The four next labels from u are `u,u,cu,c^-1u`. Therefore, for every fixed integer k,

`M_k' = (2+c^k+c^(-k)) M_k`.

For k=0,1,2, write `s=c+c^-1`. The complete update is

`M_0' = 4 M_0`,

`M_1' = (s+2) M_1`,

`M_2' = s^2 M_2`,

`c' = c^2`, `(c^-1)'=(c^-1)^2`.

The equality `2+c^2+c^-2=(c+c^-1)^2` uses only the certified unit relation. Initial moments at t=0 are `(1,1,1)`. A constant number of ring operations per layer suffices for this fixed family. This is a proved algebraic operation count, not an executed typed-bit cost or a factorization complexity result.

The homogeneous two-moment matrix and its determinant are

`H = [[M_0,M_1],[M_1,M_2]]`,

`C = det(H) = M_0 M_2 - M_1^2`.

Its exact update is

`C' = 4 s^2 C + (s-2)(3s+2) M_1^2`.                 (1)

Proof: substitute the three moment updates, write `M_0 M_2=C+M_1^2`, and use `4s^2-(s+2)^2=(s-2)(3s+2)`. This is a polynomial identity over every commutative ring. No field inverse or cancellation of an unproved unit is involved.

If `M_0` is a unit, the normalized algebraic variance is `C/M_0^2`; for odd N and dyadic Q it is defined. The unnormalized determinant C is preferable because it makes sense without this assumption. Both are derived readouts, not new positive branch masses.

For any finite branch-label list `u_1,...,u_m`, with multiplicity and `m=Q^2`,

`C = sum_(i<j) (u_i-u_j)^2`.                         (2)

Expand both sides to prove (2) without dividing by 2. **Over R, or over a finite prime field, C=0 does not imply that all branch labels coincide.** Nonzero squared differences can cancel, and the ambient quadratic form can be isotropic. The real positive-variance inference is unavailable. A vanishing aggregate is a possible gcd certificate source, not proof of support collapse, branch equality, positive factor probability or a genuine factor-producing branch.

## 3. T1 GEN/DELTA derivation and what it compresses

Let `G_Q(X)=1+X+...+X^(Q-1)` and `G_0=0`. At a fixed horizon the tagged branch enumerator is

`F_t(X,Y)=prod_(j<t)(1+X^(2^j))(1+Y^(2^j))=G_Q(X)G_Q(Y)`.

Using the two nonnegative endpoint tags `(r,s)` fits T1's tagged-witness interface without declaring a negative native grade. Evaluation at `X=a^k,Y=a^-k` is a subsequent ring readout. The coefficient multiplicities remain integer counts before evaluation; residue cancellation is not deletion of witnesses. Thus

`M_k(Q)=G_Q(a^k)G_Q(a^-k)`.                         (3)

There is also an exact T1 shell and rational-series certificate as Q varies. Put `x=a^k`, `zeta=x+x^-1`, and `M(Q)=G_Q(x)G_Q(x^-1)`. Then

`M(Q)=Q + sum_(d=1..Q-1) (Q-d)(x^d+x^-d)`,

`M(Q+1)-M(Q)=1+sum_(d=1..Q)(x^d+x^-d)`,

`M(Q+1)-2M(Q)+M(Q-1)=x^Q+x^-Q` for `Q>=1`.

The first difference is the tagged new row/column shell when the endpoint square grows from `[0,Q-1]^2` to `[0,Q]^2`. It is not an unsupported claim that a finite difference reveals a factor.

In the formal series ring `R[[z]]`,

`sum_(Q>=0) M(Q) z^Q = z(1+z) / ((1-z)(1-zeta z+z^2))`.       (4)

All denominator factors have constant term 1, so their formal inverses exist even when R has zero divisors. This is not division by `a-1`, and no field assumption enters. Equivalently,

`M(Q+3)=(zeta+1)M(Q+2)-(zeta+1)M(Q+1)+M(Q)`,

with `M(0)=0`, `M(1)=1`, `M(2)=zeta+2`. The product/doubling recurrence is simpler at Q=2^t, but (4) is a genuine GEN certificate rather than a fitted sequence. Its compression preserves this selected algebraic readout, not the unknown-order orbit or a gcd-indicator law.

## 4. What the first branch sum detects

Set `A=a^Q`, `G=G_Q(a)`. Reversing the sum gives the identities

`G_Q(a^-1)=a^(-(Q-1))G`,

`M_1=a^(-(Q-1))G^2`,

`(a-1)G=A-1`.                                         (5)

Consequently `gcd(M_1,N)=gcd(G^2,N)`. A square can inflate valuations and saturate: at `p^e`, its gcd exponent is `min(e,2 v_p(G))`, whereas probing G itself gives `min(e,v_p(G))`. When N is squarefree the two gcds coincide. A probe of G can therefore be more informative than blindly probing its squared moment.

If `a-1` is a unit modulo N, G differs from `a^Q-1` by a unit, so its prime support is precisely the standard dyadic exponent test. More exactly, `gcd(G,N)=gcd(a^Q-1,N)`, while the squared M1 readout has the corresponding squared valuation profile. If `gcd(a-1,N)` is proper, that direct preliminary test has already found a factor. If a=1 modulo N, G=Q and the branch family has no relative separation.

For an odd prime p dividing N, let `r=ord_p(a)` as a proof variable only. If `a!=1 mod p`, then G vanishes modulo p exactly when r divides Q. If `a=1 mod p`, G equals Q, nonzero for dyadic Q and odd p. Hence M1 vanishes at odd p exactly for **nontrivial two-power local order dividing Q**. This is not a new order-finding mechanism.

Similarly, M2 probes `G_Q(a^2)`. At odd p it vanishes exactly when `ord_p(a^2)` is a nontrivial divisor of Q: in terms of r, a power of two from 4 through `2^(t+1)`. Orders 1 and 2 do not give that zero. More generally fixed Mk uses the standard change of base `a -> a^k`; it does not freely detect arbitrary odd factors of the order.

These sums can miss genuine proper-factor branches. Symbolically, if the local orders at two distinct prime factors are 3 and 5 and Q=8, neither order divides Q, so M1 is a unit at both primes. Yet exponent differences 3 and 5 occur among the declared branches and can each give a proper partial collision. This is a conditional algebraic example, not an executed fixture. Thus a moment's gcd cannot be interpreted as the probability that some branch would factor N.

## 5. The determinant has additional factor sources

Let `Hq=G_Q(a^2)`; this scalar name is distinct from the moment matrix H. Then

`M_2=a^(-2(Q-1)) Hq^2`,

`C=a^(-2(Q-1)) [Q^2 Hq^2-G^4]`.

Define the division-free polynomial probes

`D_minus=Q Hq-G^2`, `D_plus=Q Hq+G^2`.

The exact factorization is

`C=a^(-2(Q-1)) D_minus D_plus`.                     (6)

Because a is a unit, `gcd(C,N)=gcd(D_minus D_plus,N)`. The determinant can be probed without constructing its inverse prefactor. Separate gcds of D_minus and D_plus can resolve some product saturation; they do not guarantee a proper factor in all saturated cases.

For a comparison with familiar exponent tests, use the polynomial identity

`(a+1)Hq=G(A+1)`.

Define

`F_minus=Q(a-1)(A+1)-(a+1)(A-1)`,

`F_plus =Q(a-1)(A+1)+(a+1)(A-1)`.

The following two **division-free identities have been independently checked algebraically**:

`(a^2-1)^2 C = a^(-2(Q-1)) G^2 F_minus F_plus`,             (7)

`(a-1)^4(a+1)^2 C = a^(-2(Q-1))(A-1)^2 F_minus F_plus`.    (8)

They follow by multiplying (6), using `(a+1)Hq=G(A+1)` and `(a-1)G=A-1`; no cancellation is needed. The negative power of a is legal from the declared unit certificate. The nonunit quantities `a-1` and `a+1` must not be cancelled silently. Formula (8) includes the extra `(a-1)^2` on the left that is needed when replacing G by the exponent expression.

If both `a^2-1` and G are units, (7) gives

`gcd(C,N)=gcd(F_minus F_plus,N)`.

Thus the determinant has extra zero conditions beyond `A-1=0`. Under further justified denominator-unit assumptions these can be written as a Cayley/Mobius-coordinate relation between a and A, but that notation supplies no new root solver or success guarantee. The polynomial formulas already give the safe interface. This is ordinary algebraic factorization of a moment determinant, not a newly named number-theoretic theory.

### A sharp one-layer distinction

At Q=2 the four labels are `1,1,a,a^-1`. Put `s=a+a^-1`. Then

`M_0=4`, `M_1=s+2`, `M_2=s^2`,

`C=(s-2)(3s+2)=(a-1)^2(3a^2+2a+3)/a^2`.             (9)

The quadratic `3a^2+2a+3` is an additional factor source. It is not equivalent to the one-layer dyadic-order condition.

For an explicitly **constructed symbolic illustration**, set a=2 and N=`19*23`. Formula (9) gives `C=19*4^-1 mod N`, hence gcd(C,N)=19. Meanwhile `a-1=1`, `a+1=3`, `G_2(a)=3` and `G_2(a^2)=5` are units modulo that N. Each individual label in `1,1,2,2^-1` has difference from 1 either zero or a unit, so no branch supplies a proper factor through the old `gcd(u-1,N)` port. The aggregate determinant nevertheless does.

This is a hand-derived input built to illustrate the algebra; **it is not a blind factorization trial, native execution receipt, performance result or success-frequency estimate**. It also exhibits why finite-field zero determinant is not support collapse: modulo 19 the list includes distinct labels even though C=0.

For general inputs, F_minus and F_plus may be units at every unknown prime, vanish at only some primes, or vanish at all and saturate. Raising their degree does not prove a higher useful hit rate. A finite-field polynomial root bound is an upper bound, not a lower success guarantee, and can be vacuous when the degree is large. No input distribution, independence, genericity or random-sampling assumption is supplied here.

## 6. A smaller inverse-free certificate computation

The weakened factor objective permits eliminating the inverse prefactor entirely. Maintain only

`A=a^Q`, `G=G_Q(a)`, `Hq=G_Q(a^2)`, and `q=Q mod N`.

Start at Q=1 with `(A,G,Hq,q)=(a,1,1,1)`. Doubling gives

`A' = A^2`,

`G' = G(1+A)`,

`Hq' = Hq(1+A^2)`,

`q' = 2q`,

all modulo N, using the old A in both geometric-sum updates. The identities are valid even with zero divisors. The exact integer Q can also be retained by its public exponent t; it is not inferred from residues.

At the desired horizon compute `D_minus=q Hq-G^2` and `D_plus=q Hq+G^2`, or their product. These have exactly the determinant's divisor content up to a unit by (6). No actual modular inverse of a is needed in this implementation after checking that a is a unit. Initial nonunit a is routed by its paid gcd; it is not passed silently to the proof's unit family. This is a useful simplification of the **output certificate computation**, not a simulation of the branch law.

An alternative after the indicated unit checks is to probe F_minus/F_plus directly using q,A,a. This isolates the additional determinant conditions from the baseline G factor. The probes are inexpensive in algebraic ring-operation count, but their statistical or deterministic effectiveness on unknown factors remains unproved.

Any actual implementation must use the existing typed BRC modular/addition/comparison/gcd interfaces, expose every operation and factor receipt, and separately charge unit checks, schedule construction, the probe gcds, repetition and failed/saturated outcomes. Ordinary host modular arithmetic is not licensed by this symbolic recurrence. No such new implementation has been run in this note.

## 7. Exact existing-tool scope

The current registry and `brc_transport.py` were read from `D:/em/TEMP/sep27-qft-research/latest_frontier/source_cache/`. Their actual local Git blob hashes match the already verified source pins at Enterprise Math commit `2e81851d62c869a20b47ae083a24dde1a4c0420c`:

| Exact source | Git blob | Scope actually used |
|---|---|---|
| `enterprise_toolbox_registry.json` | `3889506451091ebcfbf7a58cda6517c4af8c3597` | T0 observer-scoped affine moments; T1 scale enumeration and conditional GEN/DELTA certificates; routing authority only. |
| `src/enterprise_math/brc_transport.py` | `be1debe367263931bd5e93fd750be3ed54624fe1` | `EffectHistogram.moment_action` sums `weight*multiplicity*H M H^T`; `MomentState.then` retains a packed symmetric homogeneous matrix. Exact fixed-weight total affine actions and degree-at-most-two observations over integer/Fraction arithmetic. |

T0's actual module uses rational matrices. It does **not** expose a modular-ring moment API, and `Affine.inverse` is a rational Gauss-Jordan readout rather than a modular inverse. For the present recurrence choose unnormalized integer multiplicities, integral lifts of certified modular multipliers, and only addition/multiplication before reduction. Reduction `Z -> Z/NZ` then commutes with those polynomial updates. That is a proved ring-specialization bridge, not a claim that the existing Fraction implementation was already invoked as a typed modular executor. A native typed-ring adapter or direct typed recurrence still needs separate implementation and evidence.

The source's excluded occupancy/threshold/nonlinear branch-observer lease remains intact. Preserving M0,M1,M2 and then taking a gcd of their determinant is legitimate for the newly declared summary-probe contract. It does not mean T0 has acquired exact per-branch gcd probabilities or first-hit distributions. A signed determinant is a derived ring readout; no negative branch weight is introduced.

T1's full report, driver narrowing and checker source were read from the existing local cache `D:/em/TEMP/t6-exact-remote-result-audit-4lv27l1h/snapshot/`. Their exact blobs are:

| Exact cached source | Git blob |
|---|---|
| `research_notes/TOOL_DISCOVERY_NATIVE_VALUATION_EHRHART_BRION_CALCULUS_REPORT_20260822.md` | `386a307a81816b27d9753562e53bea254f4062dc` |
| `driver_reviews/TOOL_DISCOVERY_NATIVE_VALUATION_EHRHART_BRION_DRIVER_REVIEW_20260822.md` | `a98124a42ceff1ac597b0f5ffe6e46ecde56979c` |
| `tools/tool_discovery_native_valuation_ehrhart_brion_calculus_check.py` | `38c24460841e3c716acc0c76f91815b24937d688` |

These are exact local-blob reads; this note did not newly verify those three blobs against the current remote commit. The current registry routes to these report/review paths. The report supplies locally finite graded typed witnesses, tagged generating functions, additive-scale product laws and explicit quotient information loss. DELTA recovers shells; GEN is justified by actual finite-difference/recurrence data, not by local finiteness alone. Its acceptance expressly excludes universal native Ehrhart polynomiality and automatic inference of geometric dimension.

The inspected checker implements finite spatial/path-count examples, convolution and a third-difference check. It is not a ready-made modular factor-probe compiler, and it was not executed. The present use of T1 is **REUSE_APPLIED** through the explicit tag/product, shell and rational-recurrence proofs above. A finite generating description by itself does not grant cheap arbitrary coefficient extraction or nonlinear witness recovery.

No new generic tool family, Foundation mutation, native spatial Cell identity or HBW execution is claimed. The appropriate classification is a domain-specific composition/extension candidate with a deliberately weaker certificate output. No external literature or novelty search has been performed, and no novelty is claimed for geometric sums, moments, polynomial gcd probes or the determinant identities as classical mathematics.

## 8. What this changes, and the remaining Shor gap

It is reasonable to stop paying for exact first-hit law preservation **when that law is not the required result**. This branch family admits a genuinely short summary and an even shorter inverse-free certificate computation. The extra determinant factors show that the summary can create a verifiable aggregate witness without extracting a successful old branch. That is a different output contract from the former QFT/floor moment optimization; no QFT law approximation is its target.

The M1 route is largely a standard dyadic local-order probe. The determinant route has additional F_minus/F_plus conditions and therefore must not be dismissed as exactly the same probe. Conversely, those extra conditions do not supply a general algorithmic advantage merely because they exist.

The next mathematical gap is specific: choose a and a horizon/repetition strategy, without knowing a factor, such that these lawful native aggregate probes separate the unknown prime-power components with a proved useful probability or deterministic guarantee; account for all typed construction, gcd, repetition, saturation and recovery work. Test whether Enterprise-coordinate or HBW structure gives that selection law rather than merely another representation of the same polynomial. A source-backed obstruction is useful if it rules out a proposed selection rule.

A later small typed implementation can verify the polynomial/ring interface and factor receipts, but a specially chosen successful fixture cannot settle that gap. If the required Shor endpoint includes order finding, a separate valid order or order-multiple certificate and its extraction/cost analysis are still needed. Completing a general native BRC factorization/order algorithm remains the parent objective, not a claim of this audit.

Global-Knowledge-Sync: main@7a63984 / GLOBAL_KNOWLEDGE_V1
