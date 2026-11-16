# PREFIX-844 — Joint modular BRC observers: CRT fibers, temporal recovery, optimal fixed bank

Status: AUTHOR_PROVED / EXACT_BIGINT_REGRESSION / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.
Continuity: independent R6 portable research after PREFIX-843; inherited frozen scientific pin f42f2906d77f24085c123f3ccfe9667d41caa96d.
Reference: 2026-11-16_r6_prefix843_modular_fiber_lattice_exact_repair.md.
Scope: the exact positive-integer tagged BRC model with fixed named source weights and Q-only time evolution. No native X6 Cell/Link/Port event bridge, shared CLAIM, Result, Review or Foundation status is asserted.

## Mathematical input and observer scope

Let p>=1 original named sources have positive integer weights 1<=w_i<=W, W>=2. The N=W^p ordered assignments correspond bijectively to U in {0,...,N-1} using
\[
S=\sum_{i=0}^{p-1}W^i,\quad U=\sum_{i=1}^{p}(w_i-1)W^{i-1}.
\]
For fixed positive integers a,b, PREFIX-840 gives the tagged Q-only scalar \(c_t(S+U)\) at integer time t>=1, with
\[
c_t=a^{\lfloor t/2\rfloor}b^{\lfloor(t-1)/2\rfloor}.
\]
Allow k>=1 raw modular channels. Channel j at time t_j reads
\[
Y_j(U)=[c_{t_j}(S+U)]_{m_j},\quad m_j\ge1.
\]
Raw channels do not expose U, individual weights or extra repair bits. The future operation in this note is repeated Q-only tagged evolution and explicitly declared new readout channels; native space, source-port and path metadata are not projected away by this abstract result.

## Theorem 844.1: exact joint fibers, reconstruction and minimal repair

Write \(c_j=c_{t_j}\), \(g_j=\gcd(m_j,c_j)\) and
\[
L=\operatorname{lcm}_{1\le j\le k}(m_j/g_j).
\]
Then for any named assignments U,V:
\[
(Y_j(U))_{j=1}^k=(Y_j(V))_{j=1}^k \iff U\equiv V\pmod L.
\]
Exactly min(N,L) distinct joint observations occur, the largest fiber contains ceil(N/L) assignments, and the raw joint observation is injective iff L>=N. The exact worst-case number of extra fixed-length binary bits sufficient and necessary for recovery is
\[
\boxed{B_{\rm repair}=\lceil\log_2\lceil N/L\rceil\rceil}.
\]

Proof: For each channel, m_j divides c_j(U-V) exactly when m_j/g_j divides U-V; the reduced coefficient is invertible modulo the reduced modulus. Taking the lcm gives the joint equivalence. N consecutive integers occupy min(N,L) residue classes, with the largest class ceil(N/L). Each channel can be divided by g_j and the reduced coefficient inverted; generalized CRT reconstructs r=U mod L from the consistent joint residues even when moduli overlap. The additional coordinate h=floor(U/L) reconstructs U=r+hL and hence the named base-W digits. The largest fiber forces at least the displayed number of binary labels, which this h coordinate achieves. QED.

## Theorem 844.2: common-time multichannel readout equals one larger raw modulus

If all channels read at time t, let M=lcm(m_1,...,m_k). Then
\[
\boxed{L=M/\gcd(M,c_t)}.
\]
Thus the entire fixed-time bank and the single raw residue of c_t(S+U) modulo M have identical information fibers on this tagged population.

Proof: At a prime \ell let v=v_\ell(c_t) and s_j=v_\ell(m_j), s=max_j s_j. The exponent in each reduced modulus is max(0,s_j-v), and in their lcm is max(0,s-v); this is the exponent in M/gcd(M,c_t). QED.

This is an exact preservation certificate for the declared raw scalar partition, not a license to merge distinct native ports, joint interaction channels or histories.

## Theorem 844.3: fixed-bank information degrades and stabilizes

For a fixed bank repeatedly read at every t>=1, set L_t=M/gcd(M,c_t), C=ab, and let M_{\perp C} be the largest divisor of M coprime to C. Then
\[
L_{t+1}\mid L_t,\quad L_t=M_{\perp C}\ \hbox{eventually}.
\]
Consequently uniform injectivity at all positive times is equivalent to
\[
\boxed{M_{\perp(ab)}\ge N}.
\]
Proof: c_t divides c_{t+1}; every effective prime power is nonincreasing. The exponent of any prime dividing ab in c_t grows without bound, so eventually its contribution to L_t is zero. Primes not dividing ab retain their full exponents from M. Apply Theorem 844.1. QED.

Once two assignments become aliased by this fixed bank, future Q-only reads with the same bank remain aliased. A genuinely new modulus can refine the observer and restore discrimination.

## Theorem 844.4: total register width optimum across all fixed raw banks

Define the PREFIX-842 uniformly admissible single modulus
\[
m_\infty^*=\min\{m\ge N:\gcd(m,ab)=1\}.
\]
If any finite fixed bank of raw modular channels is uniformly injective for all t>=1, then
\[
\boxed{\sum_{j=1}^{k}\lceil\log_2m_j\rceil\ge\lceil\log_2m_\infty^*\rceil}.
\]
The one-channel bank m_1=m_\infty^* attains equality.

Proof: Uniform injectivity implies M_{\perp(ab)}>=N. This number is coprime to ab and hence at least m_\infty^*. Meanwhile product(m_j)>=M>=M_{\perp(ab)}. Apply log2 and integer ceiling. The singleton bank is uniformly injective by Theorem 844.3. QED.

The optimality claim counts raw register bits under the specified fixed-bank interface, not normalized U storage, network topology, fault-tolerance overhead, or native-port obligations.

## Concrete counterexample and exact computer check

Let p=W=2, a=2, b=1, t=4, hence N=4,S=3,c_4=4. A raw modulus-4 observer produces zero for U=0,1,2,3, including at all later times. A newly introduced modulus-5 observer at t=4 yields respectively 2,1,0,4 and distinguishes all four configurations. Here joint effective L=lcm(1,5)=5.

The accompanying Node.js BigInt checker exhaustively tested p=1..3; W=2..3; a,b=1..3; t=1..7; m1,m2=1..9, covering 54 parameter families, 30,618 observer cases, 270,459 assignment checks, 2,168,775 unordered pair comparisons, and 26,244 temporal divisibility checks. At t=28 it verified stabilization in 4,374 cases; the four-assignment restoration example was separately asserted. Output: ALL_EXACT_ASSERTIONS_PASSED. The finite tests check the formulas within this domain; the general conclusions follow from the proofs.

Reproduction files: PREFIX844_R6_JOINT_MODULAR_OBSERVER_CHECK.js and PREFIX844_R6_JOINT_MODULAR_OBSERVER_RESULTS.json.

## Unresolved research frontier

1. Construct and verify a genuinely native X6 Cell/Link/Port event and permissioned observation law realizing the tagged scalar without losing signed path, port, provenance or time order.
2. With channel-alphabet or topology constraints, minimize maximum per-port width and communication rounds; the raw sum-bit optimum above is already fixed.
3. Extend the joint-fiber result to operations that change source weights and require retained transition/interaction residuals.
4. Preserve earlier q>=5 nonnegative Q carrier and even-time recollision resource questions for independent study.
