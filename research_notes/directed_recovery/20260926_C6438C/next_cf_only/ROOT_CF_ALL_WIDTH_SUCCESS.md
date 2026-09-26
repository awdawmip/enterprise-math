# Fixed K33, original CF-only: all-width positive success support

Status: ROOT-PROPOSED / SHARED AUTHOR SYMBOLIC CROSS-CHECK / UNREVIEWED / NOT ADMITTED.

Root proposed the nearest-readout proof for odd part three. This file records the shared-context audit and its composition with the phase agent's near-rank-two cyclotomic argument and the completion agent's power-of-two proof. It is not an independent review or admission.

Researcher: `EM-DIRECT-C6438C`; activity: `RA-CAAAC604CB513AEA8BBC1DFC`.
Research session: `MCP-9e0873ae3aae418192f81173029434e7`.
Registration Source: `f0e5fb6f478a5a380ab5a7533d2585f7f43ee3bf`.
Frozen executable source: `0852cad130c1d877174d235687cf60c19f318c58`.
Pinned bank payload SHA256: `feecbc02808991f6d7b1e2c3179c8da2018b76901ef34c26ef0d28b65729dd5c`.

No new state propagation, ideal numerical reference, trigonometric computation, higher precision, order input, or hybrid postprocessing is used in this proof. Existing full-dimensional certificates and symbolic reference inequalities are composed. Actual executable regressions are separate evidence supplied by the root.

## 1. The precise algorithm and conclusion

The algorithm is the actual full-mode K33 streaming instrument: exact quarter-turn at `m=2`, the pinned target32/vector64 certified words at `m=3,...,32`, and the full-dimensional identity at `m>=33`. It retains the entire internal carrier, work state, and measured history. It uses the original convergent-denominator CF postprocessor, with verified returning exponents and half-exponent gcds. In particular `k=0` remains `ZERO_PHASE_RETRY`; this proof does not add the hybrid fallback.

Let `N>=3` be odd, let `gcd(a,N)=1`, and let the unknown multiplicative order be `r=2^s d`, with `d` odd. Call the base good when `s>=1` and `a^(r/2) != -1 mod N`. Minimality of `r` excludes `a^(r/2)=+1`. Let `t` be an allowed even width with `Q=2^t>=N^2`, as provided by the default `t=2 ceil(log2 N)`.

**Theorem.** For every such good base, the original CF-only K33 algorithm has a successful terminal readout with positive actual probability. In fact its per-base success probability is at least

`epsilon(t)=2^(-2 B(t))`,

where

`B(t)=2t + 128 sum_(m=3)^min(t,32) (t-m+1)`.

For `t>=32`, this is `B(t)=3842t-63360`. The conclusion holds for every allowed width, without requiring the whole-circuit ideal TV error to be small. It is a positive-support and finite-retry theorem, not an efficient classical factoring algorithm or an all-width fixed-small-TV theorem.

The three cases are:

- `d>3`: every terminal bit string has positive mass.
- `d=3`: the nearest integer to `Q/r` has positive mass and is CF-successful.
- `d=1`: the existing exact theorem gives CF factor success probability `1/2`.

Unknown `r,s,d` are only proof variables. They are never passed to the implementation, used to choose a bank, or used to prescribe a sampled output.

## 2. Actual branch recurrence and the two different comparison angles

The exact streaming proof gives, on a primitive work eigencomponent `lambda=exp(2 pi i/r)`,

`v_(h b) = [I + sigma mu_i T_(i,h)] v_h / 2`,

`sigma=(-1)^b`, `mu_i=lambda^(2^(t-1-i))`.

Here `T_(i,h)` is the actual ordered product of complete phase maps activated by the previously measured low bits. The primitive component of the initial state is nonzero; its work weight is `1/r`. This complex spectral notation is only a proof device for the real exact state.

Put `delta=2^-32`. The existing individual full-space word bound is `w_m+4 delta`, where `w_m` is the actual target interval width. For `m=3,...,32`, the sum is `177 delta`. It can be recovered directly from the stored K33 affine error slope `185 delta`, subtracting `4 u33=8 delta`, with the stored endpoint `u33=2 delta`. A weaker independent bound from `w_m<=4 delta` would also suffice for all invertibility arguments below.

There are two useful ideal comparison operators, both used symbolically:

1. **Truncated product:** replace only the retained `m=2,...,32` words by their exact planar rotations; keep all `m>=33` identities. The product is one rotation on `span(e0,e1)` and the identity on its orthogonal complement. Its distance from `T_(i,h)` is at most `eta_trunc=177 delta`, uniformly in the round and history. This is the comparison used in the cyclotomic argument and the finite mask windows.
2. **Full feedback product:** include the ideal planar phases at every activated `m`, including `m>=33`. The ideal half-angle bound gives `r_(33+j)<=u33/2^j` and a single omitted gate error at most `2r_(33+j)`. Thus the entire omitted tail in any one round has norm error at most `4u33=8 delta`. The distance from `T_(i,h)` is therefore at most `eta_full=185 delta<1/2`.

If `h` is the prefix of the integer `k`, the full feedback angle is exactly

`theta_i = 2 pi (k mod 2^i)/2^(i+1)`.

The second comparison has eigenvalues `exp(-i theta_i)`, `exp(+i theta_i)`, and `1` on the remaining modes. **The bound `177 delta` alone must not be used with this full angle when omitted tail controls are present.** The `185 delta` bound resolves that distinction without changing precision or the executed words.

All bounds are full operator bounds, not estimates only on `e0`, and are valid on arbitrary retained residual input. Telescoping preserves actual factor order; ideal commutation is used only to name the resulting planar comparison angle.

## 3. Near-rank-two rational orthogonal products exclude high-degree roots of unity

Let `T` be any actual history product. It is real orthogonal and rational. Its truncated comparison is `R_theta direct_sum I`, within `eta_trunc<1/2`. The comparison minus identity has rank at most two. Consequently at most two singular values of `T-I` can exceed `eta_trunc`: on the codimension-at-most-two kernel of the comparison minus identity, `T-I` has norm at most `eta_trunc`, giving this statement by the singular-value variational principle.

Since `T` is normal, the singular values of `T-I` are the numbers `|lambda_j(T)-1|`. Suppose `T` has a primitive `L`th root of unity as an eigenvalue, with `L>1` and `f=phi(L)>=4`. Its rational characteristic polynomial then contains the irreducible cyclotomic factor `Phi_L`; all `f` primitive roots occur as eigenvalues. At most two of these roots have distance from one exceeding `eta_trunc`; each of those two distances is at most two. Hence

`0 < |Phi_L(1)| = product_(zeta primitive L) |1-zeta|`

`                  <= 4 eta_trunc^(f-2) < 1`.

This contradicts the fact that `Phi_L(1)` is a nonzero integer. Thus no such factor can occur. The only remaining root-of-unity orders are `1,2,3,4,6`; among these, only `3,6` have nontrivial odd part.

This proof does not assert that an arbitrary dyadic orthogonal matrix has this property. It depends essentially on the certified norm proximity to a rank-two modification of the identity.

For a primitive work eigenvalue of order `r=2^s d`, every `mu_i` has the same odd part `d`. If `d>3`, then `phi(d)>=4`. A singular branch matrix would require an eigenvalue `-sigma mu_i^(-1)` of `T_(i,h)`; its order has odd part `d` and cyclotomic degree at least four, just excluded. Every branch matrix is therefore invertible, so every history preserves the nonzero primitive work component and has positive terminal mass.

In particular, the nearest integer to `Q/r` is positive and supported for every good base in this class.

## 4. Odd part three: the nearest CF readout avoids every possible cancellation

Suppose `r=3*2^s`. Take `k` to be the nearest integer to `Q/r` for purposes of the proof. Since `t>=s`, the fractional part of `Q/r=2^(t-s)/3` is either `1/3` or `2/3`. There is no tie, and with the fixed sign convention

`Delta=Q/r-k`, one has `Delta=+1/3` or `-1/3`.

Follow the low-to-high bit prefix of this `k` in the exact recurrence. At round `i`, write `b` for bit `i`, `sigma=(-1)^b`, and let `theta_i` be the full feedback angle of Section 2. Direct substitution gives the exact identity

`sigma mu_i exp(-i theta_i) = exp(i alpha_i)`,

`alpha_i = 2 pi Delta/2^(i+1)`.

Indeed `k mod 2^(i+1)=(k mod 2^i)+b 2^i`; the sign `sigma` supplies the missing bit's half-turn, and replacing this residue by `k` changes the exponent by a full integer turn. This checks the streaming bit order and inverse-phase sign convention explicitly.

For the full ideal comparison, the unscaled branch matrix `I+sigma mu_i (R_(-theta_i) direct_sum I)` is normal, with eigenvalue factors

`1+exp(i alpha_i)`,

`1+mu_i^2 exp(-i alpha_i)`,

and `1+sigma mu_i` on the complement.

The second factor uses `(sigma mu_i)^2=mu_i^2`; no sign is omitted.

For `i>=2`, in fact `|alpha_i|<=pi/12`; the weaker bound `|alpha_i|<=pi/6` already suffices. There are two possible order cases.

### 4.1 `ord(mu_i)` equals three or six

Then `mu_i^2` is a primitive cube root. The first factor has modulus at least `2 cos(pi/12)>1`, and the complementary factor has modulus at least one for either sign `sigma`. The second factor has modulus at least

`2 sin(pi/12) = sqrt(2-sqrt(3)) > 1/2`.

The last strict inequality follows, for example, from `sqrt(3)<7/4`. Thus the full ideal unscaled branch has smallest singular value greater than `1/2`.

Replacing the ideal full feedback by the actual `T_(i,h)` changes this matrix by norm at most `eta_full=185 delta<1/2`, because `|sigma mu_i|=1`. The actual branch is consequently invertible. This comparison is applied to the operator on the entire internal space, so it is valid on the actual residual-bearing vector at that round.

### 4.2 `ord(mu_i)` is at least twelve

Its order is `3*2^v` with `v>=2`; multiplying by a sign does not reduce its cyclotomic degree below four. Section 3 excludes the necessary root-of-unity eigenvalue of `T`, so the actual branch is invertible without an angle-margin estimate.

### 4.3 The first two rounds

At `i=0`, `T=I`. At `i=1`, `T` is either `I` or the exact quarter-turn on the principal plane, with identity on the remaining modes. Their only root-of-unity eigenvalues have orders one or four. Since each `mu_i` has odd part three, `-sigma mu_i^(-1)` cannot equal any of them. Both rounds' branch matrices are invertible.

All rounds along the nearest-integer history preserve its initially nonzero primitive work component. Its terminal actual vector is therefore nonzero. Other work spectral components cannot cancel its squared mass, because distinct work eigenspaces are orthogonal. The selected `k` has positive actual probability.

This proof only needs one CF-good history for odd part three. It does not claim every history is positive, does not require enumerating the phase masks, and does not use the still-unexecuted finite cyclotomic exclusion certificate.

## 5. Pure power-of-two orders and CF success

For `d=1`, the separate `POWER_OF_TWO_ANALYSIS.md` proves the stronger statement directly from the actual recurrence. The first `t-s` output bits are forced zero. The first active bit has probabilities exactly `1/2,1/2`; when it is one, every later completion gives `k/Q` reduced denominator exactly `r`, and when it is zero all convergent denominators are less than `r`. For a good base the exact CF factor success probability is `1/2`, independent of the later phase words.

For `d>1`, use the supported nearest integer `k` from Sections 3-4. Since `Q>=N^2` and `r<N`,

`|k/Q-1/r| <= 1/(2Q) < 1/(2r^2)`.

The continued-fraction criterion supplies the reduced convergent `1/r`. Its denominator is within the actual cap `N-1`, and the postprocessor checks `a^r=1`, evenness, and the two half-exponent gcds. A good base therefore returns a proper factor. All earlier smaller convergent denominators fail the returning-exponent test by minimality of `r`.

This is an existence proof for an event under the actual readout law. The real driver still samples without knowing `r` or `k`; the proof does not turn the selected history into an external algorithmic input.

## 6. Uniform positive bound from the existing dyadic denominator certificate

At terminal macro boundaries, each actual real coordinate is an integer divided by a power of two whose exponent is at most `B(t)` from Section 1. This follows from two actual H4 operations per round, at most one occurrence of each phase index per history-controlled position, and denominator at most `2^128` for each retained nonexact phase macro. The identity tail adds no phase denominator. Exact common-factor reduction only decreases the exponent.

Therefore every nonzero terminal vector has total squared mass at least `2^(-2B(t))`: at least one integer numerator coordinate is nonzero. This bound is taken in the actual real work/internal coordinates, not in the proof-only primitive spectral basis, so no additional `1/r` factor is needed.

Every good base has a nonzero successful readout by the preceding cases, giving the claimed per-base lower bound. Pure power-of-two success `1/2` is stronger and is compatible with it.

For an odd composite that is not a prime power, use the already proved random-base lemma under the actual declared uniform-base policy: a proper gcd at base selection, or a good unit base, has probability at least `1/2`. Hence a freshly and independently sampled complete attempt has

`p_success >= gamma_support(t) = 2^(-2B(t)-1)`.

This replaces the hybrid support lower bound with a theorem about the **original CF-only** path. It does not change the zero-readout, no-factor, or source-failure semantics.

If the existing ideal-success-minus-TV lower bound is also available, the larger of the two valid lower bounds may be used. A global transcript TV sum is a different statement and is not substituted for the repeated-attempt success bound.

## 7. Finite retry and full factorization implications

For a node with the stated composite/non-prime-power conditions, let `M=2^(2B(t)+1)` and let `u>=1` be the node's allocated failure bits. Then `R=M*u` independent complete attempts satisfy

`P(no factor in R attempts) <= (1-1/M)^(M*u) <= exp(-u) <= 2^(-u)`.

This retry budget is finite and generally enormous. A smaller user-supplied resource cap remains legitimate, but exhaustion must return an unresolved cofactor or partial factorization, not a prime claim or a completed random guarantee.

The already specified complete-factorization wrapper still needs its actual factor-2 preprocessing, exact perfect-power reduction, certified prime leaves, recursive splitting, product ledger, and global failure-budget allocation. With input bit length `n`, allocating `u=s+ceil(log2 n)` at each random split and using at most `n-1` such nodes gives the previous union bound at most `2^-s`. The theorem changes the support justification for the original CF-only attempts; it does not remove any peripheral obligation.

Exact rational sampling still depends on an external independent unbiased random source. An unfinished readout or random-source budget failure is explicit `INCOMPLETE`/`PARTIAL` behavior; it is not assigned an artificial `k`, and its missing probability is not silently conditioned away.

No runtime claim has improved to polynomial input-bit complexity. The exact simulator retains work-state and large-integer costs, the conservative retry bound is extremely large, and the existing Wilson prime-certificate baseline itself has exponential bit-length cost. Nor does this result prove physical Born sampling, six-axis hardware realizability, or independent mathematical admission.

Global-Knowledge-Sync: main@441ebef / GLOBAL_KNOWLEDGE_V1
