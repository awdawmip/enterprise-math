# D25 — exact Clausen-square truncation-tail visibility for 216/2304 (2026-11-04 +08)

Status: TASK_RESEARCH author-side portable proof, exact integer test, UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. Not a native checkpoint or admitted Result.
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication: TP2-B6F4FC938FF94941C1B7; frozen science pin: c47e13e4aba0e006366f989d6334d443f6333ae3. Logical research conversation: chatgpt-research-hourly-enterprise-math-20260923.

## 1. Exact source-preserving identity (Clausen plus finite truncation)

Let u_i=(1/6)_i(1/3)_i/[i!² 2^i] and v_i=(1/8)_i(3/8)_i/[i!² 9^i].
Their exact recurrences are
u_(i+1)/u_i=(6i+1)(3i+1)/[36(i+1)²];
v_(i+1)/v_i=(8i+1)(8i+3)/[576(i+1)²].

Clausen's formal power series identity, specialized to (a,b)=(1/6,1/3) and (1/8,3/8), yields coefficientwise over Q:

b_k=(2k)!(3k)!/[k!^5 216^k]=sum_(i+j=k)u_i u_j;
c_k=(4k)!/[k!^4 2304^k]=sum_(i+j=k)v_i v_j.

Reference: NIST DLMF §16.12.2 https://dlmf.nist.gov/16.12.E2

For p>3 let U=sum_(i<p)u_i, U1=sum_(i<p)i u_i, V=sum_(i<p)v_i, V1=sum_(i<p)i v_i, and retain the ordered-pair tails
T216=sum_(0<=i,j<p, i+j>=p)(6(i+j)+1)u_i u_j;
T2304=sum_(0<=i,j<p, i+j>=p)(8(i+j)+1)v_i v_j.
Then exactly over Q, without any modular assumption:

W216(p-1)=U²+12UU1-T216;
S2304(p-1)=V²+16VV1-T2304.

This retains both original source kernels, weights, indices, complete p-1 truncation and the discarded-boundary residual.

## 2. PROVED: sharp termwise valuations

For every prime p>=5, the minimum p-adic valuation over the individual weighted summands of each tail is EXACTLY:

| source | p class | min v_p |
| --- | --- | ---: |
| 216 | p≡1 (mod 6) | 2 |
| 216 | p≡5 (mod 6) | 0 |
| 2304 | p≡1 or 3 (mod 8) | 2 |
| 2304 | p≡5 or 7 (mod 8) | 0 |

Proof. All denominators of u_i and v_i, i<p, are p-units. For p=6r+1 the two numerator roots for u occur at j=r and j=2r. Thus v_p(u_i)=0,1,2 on i<=r, r<i<=2r, and i>2r respectively. If i+j>=p, either both indices exceed r, or one exceeds 2r; both imply at least two p factors. The pair (i,j)=(1,p-1) attains order 2 since 6p+1 is a unit. For p≡5 (mod6) the earliest root is j=(2p-1)/3 >=(p+1)/2. Choosing i=j=(p+1)/2 gives unit u_i and the weight 6(p+1)+1≡7 (modp), also a unit in this prime class.

For 2304, when p≡1 or3 (mod8), the two numerator roots j of v occur respectively at ((p-1)/8,(3p-3)/8) or ((p-3)/8,(3p-1)/8), both below (p+1)/2; hence a high-degree pair always contains an index with valuation 2, attained at (1,p-1). When p≡5 or7 (mod8), the earliest root is (5p-1)/8 or (5p-3)/8 respectively, at least (p+1)/2. The pair i=j=(p+1)/2 has two unit v terms and weight 8(p+1)+1≡9 (modp), a unit. QED.

For the frozen prime classes, p≡13 (mod24) entails tail216 termwise order >=2 but tail2304 can contain units; p≡19 (mod24) entails both tails termwise order >=2. Thus the finite truncation tail is a genuinely source-sensitive residual before modular comparison.

## 3. Exact checks and separated conjectures

Companion standalone Python stdlib checker ran over all 301 primes 5<=p<=2000, modulo p³, with independent recurrences for original 216/2304 and Clausen sources, O(p) suffix-sum evaluation of both tails and direct binomial-source checks for p=13,19,373. All assertions PASS.

| p | T216 mod p³ | T2304 mod p³ | W216=S2304 mod p³ |
| ---: | ---: | ---: | ---: |
| 13 | 0 | 1170 | 13 |
| 19 | 4332 | 1083 | 19 |
| 373 | 27269284 | 29773233 | 373 |

At p=13, the uncorrected weighted Gauss squares differ by 13 modulo 13², despite the original truncated sums matching modulo 13³; omitting the 2304 tail would create a false modulo p² comparison.

**Numerical candidates, not proofs for arbitrary primes:** for p≡5 (mod6), T216≡(7/2)p (modp²); for p≡5 or7 (mod8), T2304≡-p*(-3/p) (modp²). In the other classes the corresponding tails vanish mod p² by the termwise theorem. All these signatures held for the 301-prime range. The already-known observed full W216=S2304=p*(-3/p) mod p³ was rechecked, not newly proved.

## 4. BRC and continuation

Carrier: source label, (i,j), weight, numerator roots, p-valuation and i+j>=p predicate. Observer: weighted full square vs complete truncated sum, modulo p² or p³. Operation: Clausen factorization, squaring, truncation and residue. The p=13 witness isolates information lost if the truncation residual is removed.

Next scientific unit: construct an exact telescoper or character-sum argument for T2304≡-p*(-3/p) mod p² in p≡5,7 (mod8). Then compare the two Gauss square-and-derivative moments with full tail corrections at 13,19,373. The original F4-glued signed Green–WZ cancellation and native fixed-373 H0/B0 experiment remain separate and open.

Native status observed via em_status: service v0.6.11; control=UPSTREAM_CODE_REVIEW_REQUIRED; research_authority_granted=false; executor_binding_configured=false; active_jobs=5/5. Previous recovery #6637, failed continuation #6638 and support #1558 preserve their existing control provenance. No new native CLAIM, OPEN, Source checkpoint, Result or independent review.
