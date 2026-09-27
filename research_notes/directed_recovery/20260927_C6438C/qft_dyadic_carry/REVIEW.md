# Symbolic review of the displacement-correlation proposal

Status: completed shared-context symbolic cross-review; no material defect
found in the candidate at the source hash below. This is not an admission or
independent-source review. No scientific arithmetic or external query was run.

Reviewed source: `DYADIC_CARRY_CORRELATION.md`, SHA-256
`70b35a57ee0ffe628b2090f0ddeb0a7bce7eb076a03b627ca10ba8e1f815f3d1`.
The actual inherited `gram_sampler.py` was also read, including its Gamma
recurrence, observer direction and unconditional three-child requests.
Its SHA-256 is
`468de944518fbc6afa81a17555676436376da63921a784c810ffe8fab3ca17e9`.
The initial draft read during this review had hash
`ea63b76f492bae24e9ec193b40fffef430644c571e7f9211b0c47131981cf252`;
the final source above includes the depth-contract and comparison clarifications.

## Independently derived contraction contract

The notation below uses U for a matrix and makes its seed explicit. The
candidate instead defines U_h(n) as the column U(n)e0, so its equations
already contain the correct seed e0e0^T. The initial seed concern is resolved;
it is not an outstanding finding against the reviewed source.

Fix a readout prefix, hence fixed real internal matrices A_0,...,A_(i-1).
For n with i binary digits b_0,...,b_(i-1), listed most significant first, define

    U(n) = A_(i-1)^b_(i-1) ... A_1^b_1 A_0^b_0.

Here an exponent 0 means I and an exponent 1 means A_j; it does not denote a
power computed by another dynamics. Readout signs can be included in A_j.
For a fixed seed matrix X, the relevant correlation is

    C_i^X(d) = 4^(-i) sum_{0 <= n,n+d < 2^i} U(n) X U(n+d)^T.

If U(n) is a matrix rather than a column, the actual pure internal initial
state requires X = e_0 e_0^T. Replacing this with I changes the quantity to a
sum over all internal input columns. The seed-I and seed-projector quantities
are different; the same recurrence computes either at the same matrix cost.

For 0 <= d < 2^i, write d_p for its digit at significance p (p=0 is the low
bit). An addition path consists of carries c_0,...,c_i with c_0=c_i=0 and

    b + d_p + c_p = b' + 2 c_(p+1),   b,b',c_p,c_(p+1) in {0,1}.

The high carry is fixed to zero to exclude overflow. The low carry is zero
because the operation is n+d with no extra incoming unit. Process p from
i-1 down to 0, which is the circuit's time order j=i-1-p. Initialize

    F_i(0)=X,  F_i(1)=0.

For each p, form a fresh two-entry array

    F_p(c) = sum A_j^b F_(p+1)(c') (A_j^b')^T,

where the sum ranges over b,b',c' satisfying b+d_p+c=b'+2c'. The returned
matrix is 4^(-i) F_0(0). These are reverse *constraints* on low-to-high
addition carries, not a reversal of matrix multiplication. Inductively the
processed high-bit prefix has already been applied in time order; wrapping
it on both sides with the current bit's matrices appends the next operation
in exactly the required order. Every valid nonoverflowing pair (n,n+d) has
one carry path, so no multiplicities are introduced or lost.

Boundary checks are C_0^X(0)=X and C_i^X(d)=0 for |d|>=2^i. For symmetric X,

    C_i^X(-d) = C_i^X(d)^T.

For unrestricted X the correct formula is
C_i^X(-d) = C_i^(X^T)(d)^T. The latter qualification matters only if the
candidate advertises arbitrary nonsymmetric seed matrices.

## Noncommutative order check

For i=2, with A first and B second, U(0)=I, U(1)=B, U(2)=A, U(3)=BA.
The three allowed pairs at d=1 give the exact formal identity

    16 C_2^X(1) = X B^T + B X A^T + A X A^T B^T.

For orthogonal A and X=I this becomes 2 B^T+B A^T. Replacing the last
product U(3)=BA by AB instead gives B^T+B A^T+A B^T A^T, which is generally
different. The swap matrices A=(0 1), B=(1 2), embedded into the internal
space, already distinguish these expressions. No numerical execution is
needed for this formal counterexample to order reversal.

## Collision orientation and discovery cost

Suppose parent work labels are g^n and the shifted arm applies P, all in the
same unit group. With the above definition m=n+d, the pairing of a row at
g^n with the row at P^(-1)g^n requires

    g^d = P^(-1).

For real internal shift T, its signed overlap contribution is
tr(T^T C_i^X(d)). If a note instead lists g^d=P, it must consistently use
C_i^X(-d) or the corresponding transposed trace. Renaming d is harmless;
mixing the two conventions is not.

Given an explicit complete displacement list with J entries, computing all
these correlations has cost proportional to J times the two-state matrix
recurrence, plus the trace aggregation. That is a conditional bound. The
work to discover the list and certify its completeness must be added. With
unknown order, testing each d in [-(2^i-1),2^i-1] is exponentially many
candidate tests in i even when J is small or zero. Passing the true order,
a complete collision list, or a residue-class period to the method for free
would hide the unresolved number-theoretic work. Outputting J separate
entries also costs at least Omega(J) labels; any compressed representation
needs its own certified construction and aggregation rule.

Thus a polynomial-in-i recurrence for one integer displacement does not by
itself prove polynomial-bit Shor simulation. Nor does an exact signed sum
automatically provide a bound on the sum of absolute row overlaps needed
for a joint bit/latent fair-replacement certificate.

## Source-specific findings

1. **Noncommutative order and boundaries pass.** Candidate equation (8)
   wraps the already processed high-bit contribution on both sides with the
   next chronological word. Its induction matches the recurrence above.
   Both carry endpoints are zero; overflow is excluded rather than wrapped.
   Negative displacement uses the transpose of the pure-state correlation.
   The two-round expansion is now explicit in the candidate. The swap
   example above is an algebraic order-reversal counterexample, not a claim
   that those two swaps are the canonical instrument's first two feedback
   rounds. A later executable check must separately use a genuinely
   noncommuting reachable feedback history, as the candidate requests.

2. **Gamma orientation passes.** The candidate uses
   Gamma_h(z)=sum_w v_h(w)v_h(zw)^T, so its displacement condition is
   b^d=z. Its observer is tr(T_i Gamma_h(p_i)). Expanding that trace gives
   sum_w v_h(p_i w)^T T_i v_h(w), which becomes the actual cross-arm overlap
   after renaming p_i w as the destination label. This is equivalent to the
   inverse-shift convention in the earlier review derivation; the candidate
   does not mix the two conventions. Its source observer has the same
   orientation.

3. **Conditional coefficient cost passes.** There are four local carry/bit
   tuples per digit. Fixed native word actions and signed sums give the
   stated polynomial work per displacement, once the actual word list is
   given. Exact dyadic numerator/denominator lengths grow polynomially in
   i and the supplied word denominator lengths. Live matrix-slot count
   excludes neither big-integer bytes nor retained receipt/transcript bytes;
   the candidate explicitly lists those additional costs. No typed
   implementation or measured improvement has been supplied in this unit.

4. **Full collision discovery is accounted for.** The bounded BSGS scheme
   keeps every exponent attached to a repeated baby residue, covers both
   signs of d, and excludes duplicate zero. Unique decomposition d=vB+u
   proves completeness. Its cost includes B+L/B+J rather than hiding J.
   A final partial giant-step block can inspect at most B discarded
   candidates, already covered by the B term. If a first return R<=B is
   found by consecutive powers, exact state evolution on its R labels is a
   valid explicitly costed fallback; no order was supplied for free. If no
   return through B occurs, R>B and the claimed O(L/B) output bound follows.
   The generic square-root-L bound remains exponential in bit length at
   the default Shor width. The final draft explicitly gives the same return
   multiples/order information to the classical comparator.

5. **The residue-quotient boundary is appropriately restricted.** The
   reachable N=65, a=3 first-prefix example distinguishes Gamma(1) from
   Gamma(61), although both shifts have the same quartic color. Thus a bare
   four-color point-value replacement loses signed data. The separate
   min(R,L) class bound is now explicitly for queries at one common depth i
   with all i prescribed positive/negative/zero descents available. Under
   that contract, the negative binary expansion of d distinguishes b^d
   from b^e by the terminal identity test. This proves neither a bound for
   fewer remaining descents nor a general lower bound for weighted sums,
   amortized queries or classical Shor simulation. The candidate says so.

6. **Old-cache comparison passes under its stated unpruned contract.**
   At depth k below an initial depth-i query, the called shifts are all
   b^d with |d|<=2^(i-k)-1. Consecutive exponents modulo an order-R cycle
   produce min(R,2^(i-k+1)-1) distinct keys. The actual old code requests
   center, lower and upper before its phase actions and coefficient sums,
   so cancellation does not remove those calls. This key-count statement
   presumes the query completes rather than stopping at its finite budget.

The lemma provides an exact representation change for signed correlations.
It does not close the generic modular discovery cost, produce a joint work
label for free, or certify a small joint error through signed cancellation
alone. Those limits are retained in the candidate. The next step is its
bounded actual-kernel implementation and full-entry comparison, not an
asymptotic factoring claim.

Only this review file was written. Prior coherence science and the author's
candidate source were not modified by this reviewer.

Global-Knowledge-Sync: main@06788df / GLOBAL_KNOWLEDGE_V1
