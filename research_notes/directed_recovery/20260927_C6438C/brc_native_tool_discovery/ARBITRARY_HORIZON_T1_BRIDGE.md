# T1 interval blocks for an arbitrary aggregate horizon

Status: **PURE_SYMBOLIC_DERIVATION / NOT_EXECUTED / NOT_ADMITTED**. Researcher `EM-DIRECT-C6438C`, activity `RA-CAAAC604CB513AEA8BBC1DFC`. This note reuses the frozen aggregate proof and T1 source audit. It changes no earlier source, plan, execution result or claim. No scientific program, numerical fixture, search or remote operation was run.

The objective is to remove the artificial restriction `Q=2^t` from the selected aggregate factor-certificate observer, while retaining exact native witness typing. An arbitrary public positive integer Q admits a short interval-block certificate. This does not produce a useful Q for unknown factors for free, preserve a first-hit law, or complete Shor.

## 1. New interval-tagged contract

Fix `R=Z/NZ`, `N>1`, and a with a paid unit certificate. For any positive integer Q, let

`I_Q={0,...,Q-1}`, `W_Q=I_Q x I_Q`.

A microscopic witness is its ordered endpoint-tag pair `(r,s)`. Its integer multiplicity is 1 and its unit readout is `u=a^(r-s)`. The integer count is Q squared. Neither endpoint is identified with an unknown cyclic-orbit index, and no factor, order or full orbit is an input.

The selected unnormalized ring observations are

`M_k(Q)=sum_(r,s in I_Q) a^(k(r-s))`, `k=0,1,2`,

`M_0=Q^2 mod N`, `C=M_0 M_2-M_1^2`.

This is the T1 finite tagged-interval observer. For `Q=2^t`, it equals the terminal **unstopped** law of the former dyadic microscopic product `prod_j(2I+T^(2^j)+T^(-2^j))`. For general Q, that dyadic product does not describe this rectangle. There is no claim that an arbitrary binary addition chain is a sequence of the old four-way stochastic layers. The interval contract, its exact witness count and its observation lease replace that claim.

The four registers below preserve the needed algebraic sums, not the whole tagged series, individual paths, full histograms or first-hit events. The public integer Q remains part of the certificate; its residue q cannot reconstruct it. All multiplicities are unnormalized integers before ring reduction. Residue cancellation is not Boolean removal of witnesses.

## 2. Exact block concatenation and the shifted right block

Define, for every nonnegative integer n,

`A_n=a^n`, `G_n=sum_(i=0..n-1) a^i`,

`H_n=sum_(i=0..n-1) a^(2i)`, `q_n=n mod N`.

The empty block has `(A_0,G_0,H_0,q_0)=(1,0,0,0)`. The unit block has `(a,1,1,1)`. The disjoint interval decomposition

`I_(r+s)=I_r disjoint_union (r+I_s)`

gives the exact identities

`A_(r+s)=A_r A_s`,

`G_(r+s)=G_r+A_r G_s`,

`H_(r+s)=H_r+A_r^2 H_s`,

`q_(r+s)=q_r+q_s`.                                      (1)

The proof retains the right-block shift: its tag j becomes r+j, so its first-power contribution is `a^r a^j` and its second-power contribution is `a^(2r) a^(2j)`. Omitting that shift would make both sum recurrences wrong. These are polynomial identities over every commutative ring; no division or cancellation is used. In particular, a zero-divisor G or H is harmless. The unit hypothesis on a is needed for the later negative-exponent observer, not for the forward block concatenation itself.

Equation (1) defines an associative observer-level block composition with identity `(1,0,0,0)`. For three blocks, either bracketing gives

`G_r+A_r G_s+A_r A_s G_t`,

`H_r+A_r^2 H_s+A_r^2 A_s^2 H_t`,

and the same product A and sum q. Thus a composition certificate can be checked locally along any declared addition chain. The source disjoint union retains interval identity; the four-register image intentionally forgets everything except its declared evaluations and public block-length provenance.

### Why the endpoint correlation and cross terms survive

The rectangle for r+s splits into four **disjoint** blocks:

`I_r x I_r`, `I_r x (r+I_s)`,

`(r+I_s) x I_r`, `(r+I_s) x (r+I_s)`.

Their witness counts are `r^2,rs,sr,s^2`. In the tagged generating readout,

`F_(r+s)(X,Y)=[G_r(X)+X^r G_s(X)][G_r(Y)+Y^r G_s(Y)]`.       (2)

Both endpoint tags are retained before evaluating `X=a^k,Y=a^-k`. Consequently the second rectangle contributes the negative shift and the third contributes the positive shift. Explicitly,

`M_k(r+s)=M_k(r)+M_k(s)`

`  + a^(-kr) G_r(a^k) G_s(a^-k)`

`  + a^(kr) G_s(a^k) G_r(a^-k)`.                           (3)

The common shift cancels only in the both-right block. Dropping the cross terms, replacing the rectangle by `M_k(r)+M_k(s)`, or merging endpoints by a Boolean support key would violate this contract. Formula (3), or equivalently (2) followed by evaluation, establishes the selected pair correlation without enumerating the rectangle.

This is T1 disjoint tagged-union/product reuse. It is not an assertion that a right shift preserves the old local grade unchanged. The shift is explicit in the transported tags and block-length certificate. Quotient counts and source witness counts must not be confused.

## 3. O(log Q) block evaluation without a window scan

Scan the public binary representation of Q. Start from the empty block. For each bit, concatenate the accumulator with itself; if the bit is one, append the unit block. The length certificate follows `n -> 2n -> 2n+bit`. Every node is justified by (1), so the final tuple is `(A_Q,G_Q,H_Q,q_Q)`.

There are O(log Q) block compositions. A generic composition uses at most four ring multiplications and three ring additions; doubling reuses the A-square and uses three multiplications. The exact node/operation list depends on the declared chain and can be retained compactly. No iteration over `[0,Q)`, rectangle enumeration, matrix of Q states, known order or modular root solver is required for these selected sums.

This is a symbolic ring-operation bound, not a saved execution or an all-in factoring complexity result. The typed cost of a ring operation, reading/building Q, gcds, factor receipts and repeated candidate horizons must still be charged. If Q is enormous, log Q remains an input/representation cost. The proposed `Q=N-1` and `Q=N+1` choices do have O(log N) bit length, but that fact alone does not make their factor probes successful.

The already frozen dyadic implementation is the special case that performs only doublings from the unit block. No arbitrary-horizon runner is implemented or executed by this note.

## 4. The same moments and inverse-free determinant for every Q

For any positive integer Q, reversing the geometric sum gives

`G_Q(a^-1)=a^[-(Q-1)]G_Q(a)`.

Writing `A=A_Q`, `G=G_Q`, `H=H_Q`, `q=q_Q`, one obtains

`M_1=a^[-(Q-1)]G^2`,

`M_2=a^[-2(Q-1)]H^2`,

`C=a^[-2(Q-1)](q^2 H^2-G^4)`.

Hence the same inverse-free probes are valid:

`D_minus=qH-G^2`, `D_plus=qH+G^2`,

`C_tilde=D_minus D_plus`, `gcd(C_tilde,N)=gcd(C,N)`.         (4)

All equalities are in R, and the gcd equality follows from a unit prefactor, including at prime powers. Nothing requires a power-of-two Q or division by the microscopic count. If Q is divisible by a prime factor of N, normalized moments may be undefined, but (1)-(4) remain well typed.

The previously proved division-free identities also hold for arbitrary Q. Define

`F_minus=q(a-1)(A+1)-(a+1)(A-1)`,

`F_plus =q(a-1)(A+1)+(a+1)(A-1)`.

Then

`(a+1)H=G(A+1)`, `(a-1)G=A-1`,

`(a^2-1)^2 C=a^[-2(Q-1)]G^2 F_minus F_plus`,                (5)

`(a-1)^4(a+1)^2 C=a^[-2(Q-1)](A-1)^2 F_minus F_plus`.      (6)

These follow from finite polynomial sums and require no cancellation. If `a^2-1` and G are certified units, then (5) yields the exact gcd equivalence between C and `F_minus F_plus`. If either is nonunit, retain its actual gcd/setup outcome rather than cancelling it. A proper setup gcd is already a factor; gcd N is a separate degenerate or saturated outcome. The underlying interval probe (4) remains defined for every unit a even if the regular HBW chart fails.

## 5. Forcing Q=N-1 or N+1: exact classical power probes

In R, `Q=N-1` forces `q=-1`, while `Q=N+1` forces `q=1`. Substitute these residues directly into F; no assumption about a-1 or a+1 is needed for the following algebra:

| q | F_minus | F_plus |
|---|---|---|
| -1 | `2(1-aA)` | `2(A-a)` |
| 1 | `2(a-A)` | `2(aA-1)` |

With `A=a^Q`, the actual forced horizons give

| Horizon | F_minus | F_plus |
|---|---|---|
| Q=N-1 | `-2(a^N-1)` | `2a(a^(N-2)-1)` |
| Q=N+1 | `-2a(a^N-1)` | `2(a^(N+2)-1)` |

For odd N and unit a, the displayed factors 2, a and their negatives are units. Therefore the gcds of F_minus and F_plus are **exactly** the gcds of these ordinary exponent-minus-one probes, not just the same zero sets modulo primes. Prime-power valuation information is included in that statement.

The baseline G satisfies `(a-1)G=a^Q-1`. Where a-1 is a certified unit, its gcd is exactly that of `a^Q-1`. Thus the combined baseline and extra determinant sources are the adjacent exponent triple

`Q-1,Q,Q+1`,

which is `N-2,N-1,N` for the first choice and `N,N+1,N+2` for the second. The two extra F exponents alone differ by two; calling them consecutive must not conceal that distinction. Product/square readouts can still inflate valuations or saturate, which is why the separate gcds remain useful.

Under the regular unit conditions of (5), this is a standard modular-power/order-divisibility mechanism. For an unknown odd prime p dividing N, `a^e=1 mod p` means its local multiplicative order divides e. Choosing these three public exponents does not provide that unknown order or a useful separation theorem. It may return a proper factor, a unit, or saturation. No uniform density, probability lower bound or novel factoring mechanism follows from selecting Q near N.

If N is even, 2 is not a unit. The displayed polynomial identities still hold, but the gcd equivalences obtained by removing 2 do not. A paid gcd with 2 resolves the ordinary even-modulus case separately; it is not silently cancelled in the proof.

This does not rule out every arbitrary-horizon strategy. It identifies the exact mechanism of these two forced choices. A better choice or selection law would need its own unknown-factor success and total-cost argument. T1 supplies a cheap evaluation certificate for an already chosen Q, not a free oracle for choosing a favorable Q.

## 6. Boundary checks when leaving the dyadic family

The former dyadic odd-prime shortcuts cannot all be reused unchanged.

* If a=1 modulo N, then `G=q`, `H=q`, all branch labels are 1, and C=0. This is saturation, not a proper factor.
* If a=-1 modulo odd N, then H=q, while G is 0 for even Q and 1 for odd Q. Thus C is `q^4` for even Q and `q^4-1` for odd Q. In particular, when `q=+1` or `-1`, a=-1 gives a unit determinant for even Q but a zero determinant for odd Q. A rule proved only for dyadic even Q must not be imported into arbitrary odd Q. The forced horizons N-1 and N+1 are even when N is odd, so their even-Q boundary is the applicable one.
* For any prime p dividing N and a=1 modulo p, `G_Q(a)=Q mod p`. Unlike the dyadic/odd-p setting, arbitrary Q can vanish modulo p. This changes geometric-sum root accounting; it does not justify normalization by Q.
* C=0 over a finite field still need not mean that all branch labels coincide or that a period was found. The determinant is an algebraic readout with possible cancellation. The root/success analysis has to use its actual polynomial, not Euclidean positivity.

The public horizon integer, its ring residue and the remaining first-hit schedule are three different objects. This note concerns only the first two under the unstopped interval contract.

## 7. Existing-tool match, evidence status and continuation

T1 reuse is the exact interval disjoint-union, tagged product and generating-observer calculus already audited in `AGGREGATE_WITNESS_PROBE_AUDIT.md` (SHA256 `c76465057ce793825916c3d22c85acc83703becfeb5154c05b362468dd5933fd`). Its source report blob is `386a307a81816b27d9753562e53bea254f4062dc`, with narrowing review blob `a98124a42ceff1ac597b0f5ffe6e46ecde56979c`, read from the existing exact local cache. This note reuses those reads; it does not claim a new remote verification or execution of a general GEN compiler.

The current registry pin used in that audit is `3889506451091ebcfbf7a58cda6517c4af8c3597` at Enterprise Math `2e81851d62c869a20b47ae083a24dde1a4c0420c`. The accepted interface does not make every locally finite family polynomial/rational, reconstruct erased provenance or supply arbitrary nonlinear witnesses for free. Here the short formula is proved for this specific tagged interval family, rather than inferred from the tool name.

Classification: **T1 REUSE_APPLIED / domain-observer composition candidate**. No new global tool, native Cell identity or classical number-theory novelty is claimed. The moment/determinant and HBW marked-section proofs continue to apply at their declared algebraic scope; no arbitrary-Q HBW execution has occurred.

The next useful step is to reconcile this interval evaluator with the separate local-section/resonance analysis, preserving its hypotheses and candidate-horizon construction costs. This note intentionally does not import unfinished density claims from another note. If a later candidate needs actual evaluation, it can implement (1) through the already verified typed BRC modular arithmetic under a separate frozen plan and result identity. That execution should verify the block certificate and factor receipts, not rerun or relabel the existing dyadic experiment.

A conversation can continue the symbolic horizon-selection problem without the old runner or a particular host. The open scientific obligations remain unknown-factor success, repetitions/saturation recovery and total native cost; an order-finding endpoint additionally needs an actual order certificate. The parent native BRC Shor objective remains open.

Global-Knowledge-Sync: main@c552120 / GLOBAL_KNOWLEDGE_V1
