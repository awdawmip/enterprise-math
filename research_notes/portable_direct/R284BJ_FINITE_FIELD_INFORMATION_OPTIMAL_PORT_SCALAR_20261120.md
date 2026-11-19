# R284BJ — Near-information-optimal finite-field star-Port scalar with adversarial integer-noise tolerance

Date: 2026-11-20 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FINITE_CHECK_PASSED / NOT_REVIEWED. Portable mathematical research; not a native Task CLAIM, Result, or independent review.

## Scope and exact inherited source

Scientific predecessor: R284BB (nonconstant-coefficient completeness) at `78dffb8ba23314c0fc4395f87e1124b031261986`, and R284BG/R284BI at `e90b92c1bd61cbde527f7d034ed768fd685faf21` / `e91d67d0d2a8bee62fc264c26e9deb2166a6af93`. These are immutable mathematical source pins, not behavioral-policy pins.

This is a **new, explicitly finite-field measurement interface**, not a claim about the bit length of the old unprocessed integer determinant. The source offers exactly one determinant **modulo a selected prime**, with a declared bounded integer disturbance. The receiver knows n,H,delta,prime and controls, but not the matrix C. All named directed Port identities are preserved: the returned residue is injective on the declared C population even after the allowed bounded errors. For a native X6/heartbeat interpretation, additional typed embedding and observation-preservation evidence would be required; no such transfer is claimed.

## Model

Fix n>=3, H>=2 and a nonnegative integer delta. The unknown C belongs to the full population {1,...,H}^{n×n}, of cardinality N=H^(n²). Over the field F_p, the single scalar response with m=2n-1 controls is

[
P_C(d,z)=detleft(operatorname{diag}(d_0,ldots,d_{n-1})-C-sum_{i=1}^{n-1}z_iE_{0i}ight)pmod p.
]

All d_i,z_i are fixed **before** C is observed, and each is independently uniform on F_p in the existence/probability construction. The observed scalar is `r=P_C(d,z)+e (mod p)` for an adversarial integer e in {-delta,...,delta}. We use cyclic residue distance `dist_p(a,b)=min(|a-b|,p-|a-b|)`.

## Theorem BJ1 (one finite-field scalar, near-optimal transmission bits)

Define

[
J=inom{N}{2},quad M=n!(H+2)^n,quad
B=max{2M,;4(n-1)(4delta+1)J}.
]

Choose any prime p>B. With independent uniform controls (d,z) in F_p^(2n-1), the probability that **all** distinct matrices C,C' satisfy

[
operatorname{dist}_p(P_C(d,z),P_{C'}(d,z))>2delta
]

is strictly greater than 3/4. Consequently there exists a fixed nonadaptive setting that recovers **every** C exactly from one possibly corrupted residue r by a finite candidate-table decoder. It is possible to find such settings by finite exhaustive search and certify the separation against all candidates, at potentially exponential cost.

By Bertrand's postulate, choosing the least prime above B permits

[
log_2 p=O(n^2log(H+1)+nlog n+log(delta+1)).
]

This is the transmitted scalar's bit length and an upper bound on each finite-field control's bit length. The oracle can calculate a finite-field determinant in polynomial time in n and log p; **the stated decoder and deterministic choice of a successful setting are not claimed polynomial time**.

### Proof

1. **The difference is never constant.** R284BB's nonconstant coefficient completeness, for n>=3 and strictly positive matrix entries, reconstructs C from the following nonconstant coefficients of the formal polynomial P_C(d,z):
   * `[prod_{k!=i} d_k] P_C=-C_ii`;
   * `[prod_{k notin {i,j}} d_k] P_C=C_ii C_jj-C_ij C_ji`;
   * `[z_i prod_{k notin {0,i}} d_k] P_C=-C_i0`;
   * `[z_i prod_{k notin {0,i,j}} d_k] P_C=C_i0 C_jj-C_ij C_j0` for i,j>=1, i!=j.
   In the last family, n=3 leaves the explicit variable z_i, so the term remains nonconstant. Positivity makes the exact divisions legal. Hence distinct C,C' yield a nonconstant integer polynomial `Q=P_C-P_C'`. For **every** integer c, `Q-c` is a nonzero polynomial of total degree at most n-1: its degree-n top term `prod_i d_i` cancels and star terms use at most n-1 variables in each Leibniz monomial.

2. **The prime preserves a nonzero coefficient.** In the formal determinant expansion, each matrix entry has coefficient L1 norm at most H+2; by Leibniz and multiplicativity/subadditivity, the full coefficient L1 norm of P_C is at most M=n!(H+2)^n. Therefore every coefficient of Q has magnitude at most 2M. As p>2M, at least one nonconstant coefficient of Q remains nonzero in F_p, so `Q-c` is nonzero over F_p for **all** c (including c divisible by p).

3. **Uniform separation.** The finite-field Schwartz–Zippel bound gives `Pr[Q(d,z)=c mod p] <= (n-1)/p`. Two error balls of radius delta overlap iff some `c=e'-e` with integer e,e'∈[-delta,delta] gives `Q(d,z)=c mod p`; there are 4delta+1 such differences. Union bound over J unordered matrix pairs gives
   [
   Pr[	ext{some overlapping pair}]le J(4delta+1)(n-1)/p<1/4.
   ]
   On the complementary event, all cyclic error balls are disjoint and a candidate matching the received residue within distance delta exists and is unique. QED.

## Theorem BJ2 (measurement-channel cardinality lower bound)

For any one-symbol channel using residues in F_p that guarantees recovery for all N candidates and adversarial integer errors |e|<=delta, the N cyclic error balls of size 2delta+1 must be disjoint (provided p>=2delta+1, automatically necessary when N>=2). Therefore

[
pge N(2delta+1),qquad
lceillog_2 pceilge lceil n^2log_2 H+log_2(2delta+1)ceil.
]

Thus BJ1 reaches the **correct information-theoretic order** in transmitted bits, with asymptotically about twice the noiseless cardinality exponent using this pairwise-union-bound construction. BJ2 applies to one-symbol injective channel coding and does not assert a lower bound on native instrumentation or a polynomial-time algorithm.

## Exact finite verification

Companion `R284BJ_finite_field_port_checker.py` uses Python 3 standard library only, exhaustive candidate enumeration, exact primality trial division for the displayed fixture primes, modular Gaussian determinant elimination and integer cyclic-gap checking. `R284BJ_finite_field_port_verification.json` holds complete parameters and sorted-residue SHA256 commitments.

* n=3,H=2,delta=3: all 512 matrices; p=13,604,881 (24 bits); minimum cyclic gap 10>6.
* n=4,H=2,delta=3: all 65,536 matrices; p=335,002,337,287 (39 bits); minimum cyclic gap 79>6.
* Both fixtures use seed 20261120, all controls in F_p, zero collisions and fully disjoint radius-3 error balls. These are exact finite checks of two **specific random settings**, not a measurement of the general success probability or independent mathematical review.

## Interpretation and open frontier

This closes the order-of-growth communication-bit question for an **exact modular determinant observer with bounded integer noise and unrestricted finite-field control**, at the cost of an exponential candidate decoder. It does not solve the R284BG original raw integer determinant output problem: simply applying `mod p` at the receiver would still require transporting the full raw integer; the modulus must be a native source-side operation or a separately costed preprocessing stage. Nor does it establish a physically implementable finite-field sensor or robustness to arbitrary real-valued noise.

The next discriminating questions are (i) a deterministic explicitly computable control setting with O(n² log H) output bits, (ii) polynomial-time decoding in the finite-field one-symbol interface, (iii) closing the factor-two information exponent gap without losing worst-case global injectivity, and (iv) testing whether an exact source-side modular determinant can be implemented without first forming a full huge integer readout in a specified hardware/oracle model.

No P000 axiom, native X6 axis, BRC native arithmetic or three-dimensional slice is modified. The modular Port observation is a typed auxiliary algebraic experiment; its declared fiber-constancy result is exactly preservation of C for the one-step reconstruction task, not an unconditional equivalence under undeclared future native operations.
