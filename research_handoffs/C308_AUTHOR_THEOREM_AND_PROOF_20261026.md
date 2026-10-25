# C308 — One-pass, per-layer precision Newton content recovery

Date: 2026-10-26. Status: AUTHOR_PROOF / EXACT_FINITE_EVIDENCE / NOT_SOURCE_ADMITTED.
Mathematical domain: arbitrary integer polynomials, with a conditional application to the C195/H168 79-positive-rational-branch auxiliary scalar model. This is not a native GF(2)-BRC or X6 dynamics theorem.

## Source pins, identity, authority

Account control: awdawmip/chatgpt-global-knowledge main@52fb90fc028769a7be5127028e954a0182947d89, GLOBAL_KNOWLEDGE_V1, with the bootstrap/manual, exact P000 projection and original blob SHA1 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc, ACTIVE worldview and relevant mathematical/code/BRC rules. Initial EM control read: awdawmip/enterprise-math main@0e8eda0b046aafd500c082fab9f1e22e3d8e6451; later observed main head 95d8a80baed9146e4ce12b9cbc022b66af25c1d6. Portable research protocol read at the initial EM pin. Immutable predecessor: C307 commit 7ad6c714c8ec554c2395513d59b1a68422ba275a, building on author-level C306 d204fa8d28b88722c92ba54a36f8b76aa4fc7aad and C300/C305. Frozen C293 input SHA256 03083a77480e6be5615797c2f4ffc503eee6603e9e60cbad1f11fb3ea83b3c89.

Actual connected GitHub user: awdawmip, push permission for enterprise-math. Native gateway v0.6.11 was readable, but control_tasks returned CONTROL_QUOTA and RESEARCHER session_start returned STATIC_READONLY_SCOPE_DENIED with operation_sent=false. Thus there is no verified live Owner, Source CLAIM, formal Result, independent Driver admission or accepted Foundation claim. This is a durable, author-level mathematics handoff.

## Problem and exact algebra

Let s>=1 and d>=0 be integers, T in Z, and P(t) in Z[t] with degree <=d, including P=0 with content(0)=0. We seek G(P)=gcd(s,content(P)). Let H_s(n) denote the part of positive integer n supported on primes dividing s, and h_k=H_s(k!) (h_0=1).

C307's individually minimal fixed observation modulus at sample j is
    N_j = s*h_j*h_{d-j} = (s*h_d)/gcd(s*h_d, binomial(d,j)).
Define the per-layer modulus
    R_k = s*h_k.
Both schedules can be built with integer gcd extraction and require no prime factorization.

### Theorem C308-A — Exact streaming recovery with layer precision

When s>1, query samples in order j=0,...,d, keeping only the canonical representative r_j = P(T+j) mod N_j during each query, and initialize A_0,...,A_d to zero. For each newly received r_j apply
    A_k = [A_k + (-1)^(k-j)*binomial(k,j)*r_j] mod R_k,
for every k=j,...,d. Do not retain the sample vector.

Let b_k=k!/h_k, which is coprime to s. At the end, each canonical A_k is exactly divisible by h_k and
    beta_k = ((A_k/h_k) * inverse_mod_s(b_k)) mod s
is the kth Newton falling-factorial coefficient of P modulo s. Therefore
    G(P)=gcd(s,beta_0,...,beta_d).
For s=1 return 1 without any sample. The s>1 kernel uses d+1 samples and (d+1)(d+2)/2 signed binomial modular updates, with O(d*bit_length(s*h_d)) bits for the accumulator modulus-width budget.

**Proof.** The monic polynomials e_k(t)=prod_{a=0}^{k-1}(t-T-a), e_0=1, form an integer unitriangular basis of the integer polynomials of degree at most d. Write P=sum B_k e_k with integral B_k and content(P)=gcd(B_0,...,B_d). Newton's exact formula gives
    Delta^k P(T) = sum_{j=0}^k (-1)^(k-j)*binomial(k,j)*P(T+j) = k!*B_k.
For p dividing s, 0<=j<=k<=d,
    v_p(binomial(k,j)*N_j)
      = v_p(s)+v_p(k!)+v_p((d-j)!)-v_p((k-j)!)
      >= v_p(s)+v_p(k!) = v_p(R_k).
Consequently each replacement of P(T+j) by its residue mod N_j preserves every affected partial difference modulo its assigned R_k. Induction on streamed samples gives A_k congruent to the partial alternating binomial sum. At stream end, A_k is congruent to k!*B_k modulo s*h_k. Since k!=h_k*b_k with gcd(b_k,s)=1, exact division by h_k and modular inversion give B_k mod s. The integer-unimodular basis change proves the claimed gcd. QED.

Implementation detail: compute h_k/h_(k-1)=H_s(k) through repeated gcd extraction, maintain b_k mod s by multiplying k/H_s(k), and form each N_j only when sample j is requested. No factorial expansion is needed in the stream accumulator.

### Theorem C308-B — Minimal modulus for one raw-difference observer

Fix k<=d and s>=1. An observer receiving *only* Delta^k P(T) modulo a fixed positive L for arbitrary P in Z[t] degree <=d can recover B_k mod s for every P if and only if R_k divides L. Thus R_k is minimal under divisibility for this one-observation interface.

**Proof.** Sufficiency is the final normalization step of Theorem A. For necessity, suppose at some p|s, v_p(L) < v_p(s)+v_p(k!). Set c=L/gcd(L,k!), P_0=0 and P_1=c*e_k. Then Delta^k P_1(T)=k!*c is divisible by L, so P_0,P_1 have indistinguishable raw observations, while their kth Newton coefficients are 0 and c, different modulo s. Contradiction. For s=1 all positive moduli work and R_k=1. QED.

This sharpness is local to the raw kth difference observation and does *not* assert global minimal memory, global adaptive optimality or a lower bound under joint encodings of all observations.

## Exact state-width comparison

The product identity
    prod_(j=0)^d N_j / prod_(k=0)^d R_k = prod_(j=0)^d h_j
is an exact integer identity. The sum of bit_length(N_j)-bit_length(R_j) gives a clearly defined logical fixed-width modulus/storage budget comparison between a saved C307 residue vector and C308 per-layer streaming accumulators. It is not a measurement of Python process RSS, CPU speed or actual memory peak; source evaluation and binomial multiplication may dominate resources. A conservative schoolbook bound for d(d+1)/2 nontrivial integer modular updates is O(d^2*(B+d)^2) bit operations, with B=bit_length(s*h_d), excluding model evaluator cost.

Worked example: s=10, d=4. C307 sample moduli (80,20,40,20,80) require 30 total representative bit slots; C308 accumulator moduli (10,10,20,20,80) require 25, preserving the exact G(P) for all integer P of degree <=4.

## Executed evidence, 2026-10-26

Actual local reference program: C308_STREAMING_LAYERED_NEWTON.py, full executable and audit in the C308 portable archive. Runs use only exact Python integers, integer gcd and modular inverses for equality decisions.

- 3,900 seeded exact synthetic polynomials; 27,300 independently computed Newton coefficient-residue comparisons: PASS.
- 558 altered-residue lift/fiber invariance checks: PASS.
- 1,452 independent explicit omitted-prime-power raw-difference indistinguishability witnesses: PASS.
- 125/125 frozen auxiliary-model *schedule* reconstructions using actual C293 factors/coefficients; all 44,038 C307 node modulus slots match predecessor identities: PASS.
- C307 saved-sample-vector modulus-width total: 307,673,050 bits. C308 streaming accumulator modulus-width total: 270,117,377 bits. Exact difference: 37,555,673 logical bits. All 125 paths strictly decrease this budget; minimum per path 188,054, median 302,146, maximum 309,086 bits. Uniform-M vector baseline 310,152,234 bits.
- Streaming direct evaluation of frozen 79-branch auxiliary reduced numerator on paths 0, 28 and 63 (972 exact modular sample calls), compared to C305 author-level gcd witnesses: 3/3 PASS.
- **Scope:** the other 122 paths have the new complete schedule audit only; their direct full numerator circuits were not rerun with this kernel. Model correspondence still depends on C300's unreviewed cancellation identity and C305/C306 predecessor author evidence. No independent Source mathematical review or Lean proof is asserted.

For exact 125 per-path results see the C308 portable archive's C308_EXACT_AUDIT_20261026.json; this repository research handoff stores the concise audit summary and reusable independent integer-polynomial kernel.

## BRC / observer-preserving boundary and next question

The derived quotient preserves only the scalar observer G(P) under the declared fixed polynomial input and readout. This neither erases original 79 branch labels nor certifies preservation of BRC joint multiplicity, signed phase, provenance, ports, interactions or allowed future X6 Cell operations. BRC fiber/descent safety is observer-scoped; this problem requires integer-polynomial arithmetic and does not provide a native Heartbeat model computation. P000 six-axis space plus separately typed time, active worldview and the three-axis slice's explicit embedding duties remain unchanged.

Next C309: factor/block the streaming binomial-update transform to reduce exact multiplication/update costs or actual measured peak memory compared with the C307 reference. Independently verify the C300-C306 cancellation chain, and finish remaining 122 actual-circuit reruns only if materially useful. Maintain distinct author proof, finite evidence, native Owner status and final admission.
