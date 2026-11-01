# D25 — a prime-square arithmetic-progression Lucas transport with signed p² source repair

Date: 2026-10-31 Asia/Hong_Kong. Author-side mathematical research; proof and exact tests, UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. Distinct Research-onhour conversation: `chatgpt-research-onhour-enterprise-math-20260923`; not maintenance `chatgpt-hourly-enterprise-math-20260921`. Research mother: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION; Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; original frozen scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. This is an external integer/p-adic auxiliary lemma, **not** original H0/B0 execution or native P000 promotion.

## Consumed theorem and exact new question

Consume the author's p² two-port coefficient repair `20261031_onhour_d25_lucas_p2_first_frobenius_defect.md` at Enterprise Math commit `698c957b38d58886df86599a9eb2e76ba8de1cc4`: for n=a+pb and k=c+pd,
```text
C(n,k) = C(a,c)C(b,d)
   + pb {T_(p,a)(c) C(b-1,d) + T_(p,a)(c+p) C(b-1,d-1)} (mod p²),
T_(p,a)(v) = [x^v](1+x)^a ((1+x)^p-1-x^p)/p,
```
with all out-of-range coefficients zero. For the signed three-binomial carrier
```text
U_l^(gamma) = sum_(k=0)^(2l) (6k+gamma)(-1)^k 2^(2l-k)
                             C(3l,k) C(2l,k) C(4l,k),
```
the original carrier is gamma=1. The previously conjectured all-integer `(6l+1)|U_l^(1)` remains open.

## Theorem — exact conditional p² progression transport (proved)

Let p>=5 be prime, `l0=(p²-1)/6`, and let gamma be any integer such that the signed **lowest-digit weighted observer**
```text
Phi_(p,gamma) =
    sum_(c>=0) (6c+gamma) lambda^c
       product_(s in {3,2,4}) C((s*l0) mod p,c),  lambda=-1/2
```
vanishes in F_p. Define the signed *unweighted* higher-digit observation on t>=0,
```text
H_p(t)=product_(j>=0) sum_(r>=0) lambda^r
            product_(s in {3,2,4}) C(digit_j(s*t),r)  in F_p,
```
where digit_j is the jth base-p digit; products and sums are finite and the empty product at t=0 equals 1.

Then for every integer t>=0, **with the same gamma**,
```text
2^(-2*(l0+p²*t)) U_(l0+p²*t)^(gamma)
       = H_p(t) 2^(-2*l0) U_l0^(gamma)  (mod p²).
                                                        (PT)
```
Equivalently, in integer arithmetic modulo p²,
```text
U_(l0+p²*t)^(gamma)
       = 2^(2*p²*t) H_p(t) U_l0^(gamma)   (mod p²).
```
A residue representative of H_p(t) suffices on the right, because the hypothesis implies p | U_l0^(gamma).

For gamma=1, Phi equals the **original weighted-216** first-digit observer A_p mod p, by the separately proved onhour Lucas alignment. Thus the theorem applies to every frozen target p=13 or 19 (mod24) from the consumed first-digit UR theorem. It does not imply the p² seed `U_l0=0 (mod p²)` for all target p.

**Corollary: finite-verified seed, infinite progression.** For each p in the explicitly certified finite set
```text
{5,7,11,13,17,19,23,29,31,37},
```
the direct signed integer seed U_((p²-1)/6)^(1) was exactly computed modulo p² and equals zero. Therefore (PT) PROVES an infinite family of l:
```text
For every such p and ALL integers t>=0,
l=(p²-1)/6+p²*t  =>  p² | U_l^(1).
```
For any p in the target classes outside this finite seed set, the theorem provides an exact conditional transport; seed divisibility remains an independent open input. For arbitrary prime powers p^e, e>2, further digit-defect interfaces are needed.

## Proof of the progression theorem

Put `V_l=2^(-2l) U_l^(gamma)` and `lambda=-1/2` in Z_(p). For each s in {3,2,4}, write `s*l=a_s+p*b_s` with 0<=a_s<p. At l=l0+p²*t, `a_s=(s*l0) mod p` and
```text
b_s = e_s+p*s*t,  e_s=floor(s*l0/p),  1<=e_s<p.
```
The e_s bounds follow from `p <= s*l0 < p²` for 2<=s<=4 and p>=5.

Write k=c+pd. Apply the two-port binomial congruence *independently* in all three s sources. Let `A(c)=product_s C(a_s,c)`, `B_b(d)=product_s C(b_s,d)` and `q_p(2)=(2^(p-1)-1)/p`. Since `lambda^p=lambda*2^(-(p-1))=lambda(1-p*q_p(2))` modulo p² and `6k+gamma=6c+gamma+6pd`, the no-defect part of V_l has exact expansion modulo p²:
```text
Phi * D0(b) + p (6*C0-q_p(2)*Phi) D1(b),           (A)
C0=sum_c lambda^c A(c),  Phi=sum_c (6c+gamma)lambda^c A(c),
D0(b)=sum_d lambda^d B_b(d),
D1(b)=sum_d d lambda^d B_b(d).
```
This visibly retains the signed weighted lowest digit, the high-digit d-moment and the Fermat carry.

Each of the three first binomial defects from the consumed theorem enters V_l multiplied by p. Its coefficient modulo p is
```text
b_s sum_(c,d) (6c+gamma) lambda^(c+d)
      product_(u!=s) C(a_u,c) C(b_u,d)
      * {T_(p,a_s)(c) C(b_s-1,d)
                     + T_(p,a_s)(c+p) C(b_s-1,d-1)}.       (B_s)
```
All second-defect cross terms are multiples of p², so (A)+p sum_s(B_s) is the full V_l mod p². No positivity, absolute values or unlabeled aggregate quotient is used.

Use ordinary Lucas reduction, *only mod p*, on each upper index `b_s=e_s+p(s*t)`. Every product `B_b(d)` has a factor `prod_{j>=1}prod_s C(digit_(j-1)(s*t),digit_j(d))`. For `d mod p=d0`, the same factor occurs for `C(b_s-1,d)` because e_s>=1 and `b_s-1=(e_s-1)+p(s*t)`. For `C(b_s-1,d-1)`, a nonzero term requires d0>=1; otherwise the low digit of d-1 is p-1, larger than e_s-1<=p-2, and the binomial vanishes mod p. When d0>=1, d-1 has low digit d0-1 and **unchanged higher digits**. Thus every D1 and (B_s) reduction factors by the *same* H_p(t) after summation over upper digits; b_s reduces to e_s mod p. The factor 6c+gamma also stays entirely on the low digit modulo p.

Finally, `Phi=0 (mod p)` implies the term Phi*D0(b) in (A) only needs D0(b) modulo p, so it too factors by H_p(t) modulo p². All remaining terms have an explicit factor p. At t=0, e_s=b_s and H_p(0)=1, so the shared low two-digit expression is exactly V_l0. Therefore V_(l0+p²t)=H_p(t)V_l0 modulo p². QED.

## Executed exact testing and nonvacuous controls

The published script `research_notes/portable_direct/d25_lucas_p2_transport_20261031.py` uses standard-library integer binomials and modular powers, independently computing the **full weighted U_l** and high-digit H_p(t). It checks p in {5,7,11,13,17,19}, gamma in {1,1+p,1+2p}, and t=0..4 for p<=11 or t=0..2 for p>=13: **72 independent exact triplets** all pass, including 6 nonzero seed controls. Marker: `PASS_D25_P2_LUCAS_ARITHMETIC_PROGRESSION_TRANSPORT`.

The test perturbs the original weight by multiples of p but retains the exact lowest-digit Phi, preventing a false pass solely because both sides vanish:
- p=5, gamma=6, seed l0=4: U_seed=20 mod25 (NONZERO), H_p(1)=1, and U_29=5 mod25, matching `2^50 * 20=5` mod25; at t=4, H=4, U_104=5 mod25.
- p=7, gamma=8, seed l0=8: U_seed=28 mod49, H_p(1)=4, U_57=7 mod49. At t=3, H=5 and U_155=42 mod49.
- p=11, gamma=12, seed l0=20: U_seed=11 mod121, H_p(1)=10, U_141=77 mod121.

The unperturbed gamma=1 version passes every checked t for the six tested primes; the ten seed p² certificates listed above are independently computed by the prior source-repair script. Finite tests corroborate the formula; the universal transport is from the proof.

## Remaining mother target and original native benchmark

The same frozen D25 second-digit target is still `A_p=p mod p³` in both p mod24 classes {13,19}, equivalently `C01+F2+I_p=0 mod p`, with the previously proved three-stratum p³ jets and signed high strip. The new transport proves no all-target second digit and does not eliminate the high strip. Its specific contribution to the composite auxiliary conjecture is an exact source-preserving p² reduction to seed cases.

The genuine native fixed p373 H0/B0 test, `[X]U mod139129`, module rank, semilinear Frobenius/eta, signed odd Green/Hesse, kappa and independent replication remain under existing support issue `awdawmip/enterprise-math#1559`, OPEN / pending real executor as observed 2026-10-31. Canonical Source authority from Site gateway still false; author-side GitHub commits and GLOBAL_KNOWLEDGE progress capture do not turn into CLAIM/open/Result. Prior original Research dispatch request #6633 stays on its original failure receipt; no replay or maintenance identity was used.

Next exact scientific step: either prove the p² **seed cancellation** for all target primes (then PT gives infinite-square progressions), or construct a counterexample; and prioritize joint WZ/CM cancellation of `C01+F2+I_p` for the original hard target. No new Source role or mathematical acceptance claimed.
