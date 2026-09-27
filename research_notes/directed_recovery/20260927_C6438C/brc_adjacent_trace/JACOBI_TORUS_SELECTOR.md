# Jacobi conditioning selects opposite tori for Blum semiprimes

Status: **PURE_SYMBOLIC_SELECTOR_CANDIDATE / REUSE_IDENTIFIED / NOT_NEWLY_EXECUTED / NOT_ADMITTED**.
Shared researcher context EM-DIRECT-C6438C, activity RA-CAAAC604CB513AEA8BBC1DFC. This note introduces a factor-blind parameter filter for the regular companion/HBW torus. It changes no frozen source, run or cost record and makes no new scientific call.

The concrete pointwise guarantee is restricted but useful: on a promised product of two distinct Blum primes, accepting Jacobi(k^2-4,N)=-1 makes the local tori have opposite split types. At a main clock E=2^s, s>=1, either signed regular return can occur only in the nonsplit component. A nonunit main-clock return divisor is therefore proper; it cannot saturate N. This does not guarantee that a return occurs.

## 1. Domain and observable information

Assume mathematically that N=pq with distinct primes p,q congruent to 3 modulo 4. The program receives N, a proposed integer k and a public s>=1; it does not receive p, q, their sizes, local orders or eigenvalues. Write

    Delta=k^2-4,
    M(k)=[[0,1],[-1,k]],
    E=2^s.

A regular candidate has gcd(Delta,N)=1. Define the computable filter

    J(Delta,N)=-1.

For this squarefree two-prime domain the Jacobi definition gives

    J(Delta,N)=(Delta|p)*(Delta|q),

where each local Legendre symbol is +1 or -1 after regular admission. Acceptance therefore means one split and one nonsplit regular torus. Jacobi computation does not reveal which prime has which type.

The Blum assumption is an input-domain promise for the theorem, not something inferred by the filter. N congruent to 1 modulo 4 is necessary here but does not imply two prime factors, distinctness, or both factors congruent to 3 modulo 4. In particular, two primes both congruent to 1 modulo 4 also give that residue class and do not obey the split-torus obstruction below. The same computational filter may be tried on a wider domain, but its no-saturation proof must not be reported there. Every returned divisor still requires its own exact divisibility/properness certificate.

## 2. Why the dyadic main clock cannot hit the split component

For a Blum prime r, the split eigenvalue group has order r-1=2m with m odd. At E=2^s, gcd(E,r-1)=2. The positive return equation lambda^E=1 therefore has only lambda=1 and lambda=-1, both excluded by regularity.

For the negative equation lambda^E=-1, a cyclic exponent congruence would require gcd(E,r-1)=2 to divide (r-1)/2=m, which is impossible. Equivalently the exact signed-count rule has an odd ratio (r-1)/gcd(E,r-1) and no negative solutions.

Thus a regular split companion has neither M^E=I nor M^E=-I. This is a pointwise statement; no probability model is needed.

After Jacobi acceptance, one of the two prime components is split. Let

    D_epsilon=gcd(N, all entries of M^E-epsilon*I).

The already proved adjacent-trace common observer computes this divisor from

    tau_epsilon=V_E-2*epsilon,
    w_epsilon=V_(E+1)-epsilon*k.

For either epsilon, the split component cannot divide D_epsilon. Consequently

    D_epsilon is either 1 or the nonsplit prime.

In particular it never equals N. Trying both signs can produce a factor only at the nonsplit component; their local signed events are disjoint. On this promised squarefree domain an ordinary signed trace gcd has the same prime support, but the primitive adjacent-trace contract remains available and its actual costs must be retained.

This proof is for the companion's main E return. It does not turn the elliptic curve discriminant or an arbitrary HBW move into the same torus-selection problem.

## 3. Exact acceptance and orientation weights

The following probability claims assume a uniform k modulo N, conditioned on regularity and then on Jacobi acceptance. The pointwise result above holds for every accepted k even without uniform sampling.

For an odd prime r, the regular trace parameters have split count

    S_r=(r-3)/2

and nonsplit count

    U_r=(r-1)/2.

These are the inverse-pair counts from EXACT_TRACE_PARAMETER_FIBERS.md. Conditioning uniform k on regularity gives independent uniform regular local trace parameters. The two allowed orientations have counts

    p split, q nonsplit: S_p U_q,
    p nonsplit, q split: U_p S_q.

Set

    Z=(p-3)(q-1)+(p-1)(q-3),
    D=S_p U_q+U_p S_q=Z/4.

The conditional orientation weights are

    omega_p_split=(p-3)(q-1)/Z,
    omega_p_nonsplit=(p-1)(q-3)/Z.

The notation tracks p's type; q has the opposite type. Within either nonempty orientation, the local trace values remain independent and uniform in their specified split/nonsplit sets. One must not assign the two orientations weight 1/2 in general.

Writing R=(p-2)(q-2), direct expansion gives D=(R-1)/2. Hence

    Pr(J=-1 | regular)=(R-1)/(2R).

If proposals are uniform over all N residues, the acceptance probability is D/(pq); nonregular candidates and their possible setup factors have not been removed from an actual algorithm's bill. These are exact distributional statements, not an implemented sampler or a claim that rejected candidates cost nothing.

The small-prime boundary is explicit. If p=3, S_p=0 and U_p=1, while distinct q>3 has S_q>0. Only the orientation p nonsplit/q split is possible, with weight 1. The formulas have positive denominator and remain valid. If q=3, the symmetric statement holds. Distinctness prevents the p=q=3 empty-orientation case, which is outside the domain.

## 4. Exact conditional main-clock hit rates

Condition on the nonsplit local component being the Blum prime r. Its norm-one group has cyclic order L=r+1. There are U_r=(r-1)/2 regular nonsplit trace parameters.

Let d=gcd(E,r+1) and let h=d if (r+1)/d is even, otherwise h=0. Because E is even, the signed return probabilities within this nonsplit trace family are

    rho_r,+ = (d-2)/(r-1),
    rho_r,- = h/(r-1).

For the positive sign, remove both exceptional eigenvalues from the d solutions, pair inverses and divide by U_r. For the negative sign, the exceptional eigenvalues do not solve the equation at even E; the same inverse-pair normalization gives h/(r-1).

If both signs are actually evaluated, their disjoint union gives

    rho_r = [gcd(2E,r+1)-2]/(r-1).

This formula counts only the declared either-sign main-clock event. One fixed sign must use its own rho_r,epsilon and pay only the readouts its program actually performs.

More explicitly, let t=v_2(r+1)>=2. Then

    rho_r,+ = [2^min(s,t)-2]/(r-1),
    rho_r,- = 2^s/(r-1) if s<t, and 0 otherwise,
    rho_r   = [2^min(s+1,t)-2]/(r-1).

Under the full accepted distribution, the proper-factor probability for evaluating both signed main-clock observers is exactly

    P_hit|accepted = omega_p_split*rho_q
                    + omega_p_nonsplit*rho_p.

For one sign, substitute its signed rho values. There is no main-clock saturated-return event on this domain. The complementary probability is a unit/no-hit event, not success.

At r=3, the nonsplit group has order 4 and the regular nonsplit trace family has one element. The displayed union rate equals 1 for every s>=1. At s=1 its return is negative; at s>=2 it is positive. This is a small-prime boundary of the formulas, not evidence of useful density for large unknown primes.

## 5. What the filter does not solve

The filter forces different torus types, so it removes simultaneous dyadic signed main return. It does not remove the odd part of a nonsplit eigenvalue order. Increasing s eventually caps the conditional hit rate at

    [2^t-2]/(r-1),  t=v_2(r+1).

When t is small, that rate is small for a large r. For instance the entire congruence class r congruent to 3 modulo 8 has t=2 and maximum union rate 2/(r-1). No numerical fixture is being generated by this symbolic observation. The finite filter acceptance probability cannot turn that small subsequent return probability into a general factoring guarantee.

The no-saturation conclusion must not be transferred to the section's second clock E+2. In general E+2 has an odd factor, so a split torus can return there. The scalar w_epsilon combines the E and E+2 branches; it can therefore be saturated by different components even while the main marked branch remains proper. A successor using that union must keep the branch label and its actually paid exact quotient, or retain explicit saturation/no-hit outcomes. Any special second-clock case needs its own proof.

Likewise, choosing both signs, increasing s adaptively, changing k after a failed return or mixing other exponent factors has a new joint/first-hit distribution. The present conditional rates do not authorize treating those events as independent. A useful factor-blind mixed-exponent schedule and its total expected or worst-case work remain open.

## 6. Exact native tool reuse and a proposed executable contract

Actual local source reading identified this already implemented primitive:

    typed_jacobi_trace(a,N)

in character_certificates/typed_jacobi.py, SHA-256

    ce7168c8724d1fff216b903f09cdaf7fe16c8074c48488f7b26fb80584060402.

The full source was read without import. It accepts any integer numerator and positive odd denominator, uses actual lazy_modular.Arithmetic.divide for the initial and Euclidean remainders, and records factor-of-two shifts, low-bit reciprocity decisions, the terminal gcd, operation traces, source bindings and separate deterministic digit/label-wiring costs. Its factor_or_order_input field is false and its source does not use a host modular-power or remainder answer.

The source proof JACOBI_FINAL_BIT_PROOF.md was also read in full at SHA-256

    fc51f6feb6134b2d1443efd9751f26621478a25512cc2d3784ae63045c5c7161.

Only its generic typed Jacobi algorithm, arithmetic-certificate proof and cost scope are reused here. The later certify_square_schedule and certify_program_final_bit interfaces apply to an older reverse-square QFT instrument contract. Their fair-bit, reachability, support and schedule conclusions are not transplanted to this torus selector.

For canonical 0<=Delta<N and n=bit_length(N), that proof supplies a conservative O(n^3) digit-replay bound for its trace-retaining Jacobi implementation, plus separate label wiring. A larger unreduced numerator adds the initial division cost in its own bit length. This is a reused symbolic bound, not a new benchmark or a free filtering step.

A future bounded implementation can declare the following contract:

1. Draw or otherwise specify a public k with its explicit sampling law. Compute the canonical Delta residue using typed multiplication/subtraction/reduction, retaining the operation links.
2. Evaluate the bound typed Jacobi primitive. Its actual terminal gcd can also certify regularity when the integration retains the complete certificate. A proper nonunit setup gcd is already a factor, after paid exact division; a saturated setup is a retained degenerate outcome. An existing separate regularity gcd may be reused only through an actual matching certificate, not by erasing its cost.
3. Retain J=+1 as a rejected candidate. Retain J=0 and its nonunit evidence. Only J=-1 enters this selected main-clock path. Rejections and any cap on attempts remain in the ledger.
4. Use the already certified adjacent-trace or companion power program at E=2^s. Evaluate the declared one or two signed main observers with actual gcd and factor-division receipts. Record every unit/proper/saturated status; no-saturation is a theorem under the external Blum promise, not permission to omit an unexpected status.
5. Keep filter, propagation, observer, exact-factor validation, any certificate replay, source admission, randomness and storage costs distinct. Link the Jacobi output label to the actual typed Delta producer in the outer record. Reuse of two implemented arithmetic interfaces is not automatic proof of their new integration.

The new status is REUSE_IDENTIFIED, not REUSE_EXECUTED for this selector. No new Jacobi invocation, filtered sample, native fixture, useful-exponent experiment or selector benchmark has occurred. Classical Jacobi and torus mathematics are being assembled into this project's explicit native certificate contract; no global novelty or general Shor completion is claimed.

## Continuation

Freeze a bounded filter/observer program only after its literal input domain, proposal law, main clock, output contract and full costs are declared. Preserve the existing ordinary and marked results. The essential scientific question remains whether a factor-blind parameter and mixed-exponent strategy obtains useful separation probability at acceptable total cost; this pointwise removal of one saturation mechanism is one component of that question.

Any authorized conversation can continue the symbolic analysis from this note and the pinned primitive. Actual computation requires the original typed operation/source contract, not a particular host or named conversation tool.

Global-Knowledge-Sync: author actual canonical read lease main@4ae9f3f / GLOBAL_KNOWLEDGE_V1.

