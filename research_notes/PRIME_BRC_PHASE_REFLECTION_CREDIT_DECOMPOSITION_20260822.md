# Prime-BRC Phase Reflection / Credit Decomposition

Status: `L3 OWNER-LOCAL RESEARCH CHECKPOINT / NOT CANONICAL / NOT LEGENDRE PROOF`
Date: 2026-08-22
Researcher: EM-PRIMEBRC-7F3A21
Owner branch: `research/prime-brc-stage-a`

## 1. Exact block-count normal form for quotient phase

Let

- `A=k^2`, `B=(k+1)^2`, `G=B-A=2k+1`;
- `A<n<B`;
- `d>=2`, `d|n`;
- `x=n-A`, `y=B-n`, so `x+y=G`.

Define

`Theta_d(n)=(n/d-floor(A/d))/(floor(B/d)-floor(A/d))`.

Because `d|n`, exactly

`L_d(n)=ceil(x/d)`,

`R_d(n)=floor(y/d)`,

and

`Theta_d(n)=L_d/(L_d+R_d)`.

Thus quotient phase is the ratio of the integer number of `d`-blocks needed to reach the state from the lower boundary to the total left-plus-right quotient block count.

The terminal condition is exact:

`Theta_d(n)=1 <=> d>y=B-n`.

For canonical `p=spf(n)`, phase-one sinks are exactly composite states `B-s` satisfying `spf(B-s)>s`.

## 2. Nonnegative factor-path credit cocycle

If `D|E|n` and both quotient widths are positive, then

`Theta_D(n)<=Theta_E(n)`.

Writing `E=D e`, and in the `D`-quotient interval

`a=floor(A/D)=e alpha+r`,

`b=floor(B/D)=e beta+s`,

`n/D=e z`,

with `W=beta-alpha` and `Y=z-alpha`, one has

`Theta_E-Theta_D = [r(W-Y)+sY]/[W(eW+s-r)] >= 0`.

Hence

`C_n(D,E)=Theta_E(n)-Theta_D(n)`

is a nonnegative additive cocycle:

`C_n(D,F)=C_n(D,E)+C_n(E,F)` for `D|E|F|n`.

At terminal divisor `E=n`, `Theta_n(n)=1`.

## 3. Raw divisor-column reflection

For a divisor `d|n`, put

`a_d=floor(A/d)`, `b_d=floor(B/d)`, `w_d=b_d-a_d`,

`m_d=n/d-a_d`.

If `m_d<w_d`, define

`R_d(n)=d(a_d+b_d-n/d)`.

Then `R_d(n)` lies strictly inside the square basin, `d|R_d(n)`, the operation is an involution on the two interior ranks, and

`Theta_d(n)+Theta_d(R_d(n))=1`.

If `m_d=w_d`, the reflected point falls to/below the lower boundary; these are exactly the phase-one sinks.

## 4. Canonical least-factor reflection descent

Take `p=spf(n)` and apply the raw `p`-reflection whenever it remains interior.

Since the reflected state is still divisible by `p`,

`spf(R_p(n))<=p`.

If equality holds, the two states form an exact same-`p` two-cycle and their canonical phases sum to one.

If inequality is strict, canonical least factor strictly decreases. Therefore canonical reflection dynamics has no cycle involving a changing least factor; every orbit reaches a same-factor two-cycle/fixed midpoint or a boundary sink.

This is a well-founded BRC descent, not a statistical observation.

## 5. Minimum-factor phase removes reclassification damage locally

For a composite state define

`Phi(n)=min_{1<d<n, d|n} Theta_d(n)`.

If `m=R_d(n)` is an interior composite state, then

`Phi(n)+Phi(m)<=Theta_d(n)+Theta_d(m)=1`.

Thus the local reflection balance survives arbitrary canonical-factor changes when the runtime is allowed to branch over true divisor channels and retain the minimum future-credit readout.

This does not yet supply a global matching; the top state `B-1=k(k+2)` is an unavoidable reflection sink for every one of its divisors, so a pairwise matching proof alone cannot close Legendre.

## 6. Exact least-factor phase-excess localization

Let `S_p` be the least-prime-factor shell in the square basin. Under `p`-reflection, partition `S_p` into:

1. same-`p` two-cycles;
2. possible same-`p` midpoint fixed states (`Theta=1/2`);
3. cross sources whose reflected target has smaller least factor;
4. the unique possible phase-one top sink for that shell.

Let

- `C_k` = number of composite states in the basin;
- `F_k=sum_{n composite} Theta_spf(n)(n)`;
- `T_k` = total number of phase-one least-factor sinks;
- `E_k` = directed cross-reflection edges `(p,m)` where `m=R_p(n)` and `spf(m)<p`.

Then exactly

`F_k-C_k/2 = T_k/2 + sum_{(p,m) in E_k} (1/2-Theta_p(m))`.

Proof: same-factor pairs contribute exactly one per two states; midpoint fixed states contribute exactly `1/2`; a cross source has phase `1-Theta_p(m)`; a top sink contributes one.

This identity localizes every departure from the `1/2 per composite` baseline to boundary sinks and strict least-factor descents.

## 7. Cross-reflection targets are not the semiprime parity core

Every strict cross target `m` is divisible by two distinct small primes:

`r=spf(m)<p<=k` and `r p | m`.

Therefore cross-reflection load is supported only on states with at least two distinct small prime resources.

If additionally `r^2>=2k` (P017 high band), canonical P017 gives `Omega(m)<=3`. Such a cross target cannot be semiprime: if `m=r p` with `p<=k`, then the canonical cofactor `m/r=p<=k`, contradicting the square-basin fact `m/r>k`. Hence it is a three-prime state. Moreover `rp>=2k`, so its final factor is at most `((k+1)^2-1)/(2k)<=(k+2)/2`, hence all three prime factors are <=k.

Therefore high-band cross-reflection load lies entirely in the already resource-controlled fully-small three-prime population. Semiprime `p*q` states with one large prime tail do not create strict high-band cross-reflection load; they live in same-shell balance or sink channels.

## 8. Two mirror involutions and the unit translation

On offset coordinates `x=n-A` (`1<=x<=2k`):

- integer-center reflection around `M=k(k+1)=A+k` is `J_0(x)=2k-x` where interior-defined;
- half-integer reflection of the full interior set is `J_1/2(x)=2k+1-x`.

Their composition is the unit translation:

`J_1/2(J_0(x))=x+1`.

Thus the difference between the integer-center and half-integer mirror decompositions is literally one discrete lattice step.

For canonical phase weight `w_x` (prime -> 0, composite -> least-factor phase), define half-mirror margins

`H_i=w_i+w_{2k+1-i}-1`, `1<=i<=k`,

and integer-mirror margins

`I_i=w_i+w_{2k-i}-1`, `1<=i<=k-1`.

Then locally

`H_i-I_i=w_{2k+1-i}-w_{2k-i}`,

and globally the differences telescope to

`sum H_i - sum I_i = w_{2k}+w_k-1 = 1/2`,

because the two always-composite special states satisfy

`w_k=Theta_spf(k(k+1))(k(k+1))=1/2`,

`w_{2k}=Theta_spf(k(k+2))(k(k+2))=1`.

This is a discrete mirror-credit conservation law induced by the one-unit separation of the two reflection centers.

## 9. Canonical integer-mirror margin theorem

For `1<=r<k`, suppose both `M-r` and `M+r` are composite, with least factors `p,q`.

Then

`Theta_p(M-r)+Theta_q(M+r)>=1`,

with equality exactly in the same-least-factor case `p=q`; when `p!=q` the inequality is strict.

One proof uses the integer counter identities. Put left/right quotient counts `(m_-,u_-)` and `(m_+,u_+)`. Then

`p m_- - q u_+ = (A mod p)+(B mod q)-1`,

`q m_+ - p u_- = (A mod q)+(B mod p)-1`.

For canonical distinct least factors neither right side can be `-1`; if both were zero, endpoint divisibility forces both primes to be common anchor factors and hence the least factors would coincide. Thus the product margin

`m_- m_+ - u_- u_+`

is positive for `p!=q`, giving strict phase crossing. For `p=q`, the common least factor is an anchor/common mirror factor and the two quotient counter pairs swap, giving exact equality.

## 10. Half-integer mirror pointwise classifier

Pair all `2k` interior states by

`n_x=A+x`, `n_x*=B-x`, `1<=x<=k`.

Their continuous positions sum exactly one. Every composite quotient phase strictly leads its own continuous position; primes are assigned weight zero. Hence

- if both states are composite, their phase weights sum strictly greater than `1`;
- if at least one is prime, their phase weights sum at most `1`.

Thus the half-integer pairing gives an exact pointwise double-composite classifier at the semantic level of the phase weight.

Summing these `k` pair margins gives exactly `F_k-k`. Therefore the numerical candidate `F_k<=k` is equivalent to saying the total deficit of prime-containing half-mirror pairs pays for all double-composite half-mirror excess. It is stronger than Legendre and remains unproved.

## 11. Current hard boundary

The new reflection decomposition removes a major ambiguity but does not prove the global phase budget. The remaining obstruction is now typed:

`GLOBAL_PHASE_BUDGET_OBSTRUCTION = PHASE_ONE_SINKS + LOWER_BAND_CROSS_REFLECTION_CREDIT`.

High-band cross load is already forced into the fully-small three-prime resource layer; the dominant unresolved cross load is lower-band and should be coupled to P017 L052/L054 and P018 T110-T113 root descent.

Do not claim `F_k<=k` as theorem. Computation through large tested k remains evidence only.
