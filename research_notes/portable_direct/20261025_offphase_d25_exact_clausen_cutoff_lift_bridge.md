# D25/LIFT — all-target exact Clausen cutoff bridge for the divided second digit

2026-10-25 | TASK_RESEARCH | **PORTABLE AUTHOR-SIDE ALGEBRA / UNREVIEWED / NOT_ADMITTED / NONBLIND / REGISTER_PENDING / SYNC_DEBT / NO_NATIVE_CLAIM / NO_SOURCE_CHECKPOINT**.

**Mother:** ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. **Task:** RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT. **Publication:** TP2-B6F4FC938FF94941C1B7. **Immutable mathematical Source:** c47e13e4aba0e006366f989d6334d443f6333ae3 (not shifted by later operating-control commits). This is source-labeled portable research, not a role-bearing Result, an authorized Source checkpoint or an independent review. Its mathematical antecedents—accepted CM0/SIMPLE, the first-digit UR/JT0 theorem, the frozen scalar interface, and the classical Clausen identity—are all **inherited, not re-credited**. It does not re-prove the previously published WZ Frobenius jets.

## Exact input and the new question

For a prime p congruent to 13 or 19 (mod 24), let m=(p-1)/6, and work in Z_(p). Define for 0<=k<p:

\[
b_k=\frac{(1/6)_k(1/3)_k}{(k!)^2}2^{-k},\qquad
d_k=\frac{(1/2)_k(1/3)_k(2/3)_k}{(k!)^3}2^{-k},
\]
\[
g=\sum_{k=0}^{p-1}b_k,\quad
h=\sum_{k=0}^{p-1}(12k+1)b_k,\quad
W_p=\sum_{k=0}^{p-1}(6k+1)d_k.
\]

The frozen parent provides p|g and the **accepted first-digit unit reciprocity** G_p h = 1 (mod p), where G_p=g/p. Only the divided *second* digit is open:

\[
\Delta_p=(G_ph-1)/p=(gh-p)/p^2\pmod p.
\]

We address one specific lost source component: the finite cutoff when multiplying the two truncated 2F1 series before taking the second digit.

## Main theorem — p-uniform reflected Clausen cutoff certificate

For 1<=i<=m, put

\[
\bar b_i=2^{-i}{m\choose i}{2m\choose i}\in\mathbb F_p.
\]

Define e_1=1 and for 2<=t<=m

\[
e_t=e_{t-1}\frac{36(t-1)^2}{(6t-1)(3t-1)}\pmod p;
\quad E_0(i)=\sum_{t=1}^{i}e_t,\quad
E_1(i)=\sum_{t=1}^{i}t e_t.
\]

All inverses exist: for 2<=t<=m the factors (6t-1),(3t-1) are nonzero modulo p. Define the finite-field scalar

\[
\boxed{\mathcal C_p=\frac15\sum_{i=1}^{m}
\bar b_i\bigl[(6i+1)E_0(i)-6E_1(i)\bigr]\pmod p.} \tag{C}
\]

Then **for every target prime**, not merely the finite tested sample,

\[
\boxed{\frac{gh-W_p}{p^2}\equiv\mathcal C_p\pmod p,\qquad
\Delta_p\equiv\frac{W_p-p}{p^2}+\mathcal C_p\pmod p.} \tag{L}
\]

The fractions divided by p^2 are integral in the indicated hypotheses. The correction (C) is executable with O(m) field operations and O(1) streaming scratch space. A closed-form independent check of the reflected coefficients is

\[
\boxed{e_t=\frac{2^{t-1}}{{m+t\choose t-1}{2m+t\choose t-1}}\pmod p.} \tag{E}
\]

**Proof (all load-bearing steps).**

1. Apply the classical coefficient-wise Clausen identity

\[
{}_2F_1(1/6,1/3;1;z)^2={}_3F_2(1/2,1/3,2/3;1,1;z).
\]

With c_k=(1/6)_k(1/3)_k/(k!)^2 and F(z)=sum_{0<=k<p}c_k z^k, the terms of F(z)^2 of degree n<p coincide *exactly over Q* with the 3F2 coefficient at n. Evaluating the operator 1+6z*d/dz at z=1/2 gives F(1/2)*(F(1/2)+12zF'(1/2))=gh. Thus the exact **finite-truncation** discrepancy is

\[
gh-W_p=\sum_{n=p}^{2p-2}(6n+1)
\sum_{\substack{i+j=n\\0\le i,j<p}} b_i b_j. \tag{1}
\]

Only coefficients n<p of the classical identity were used. We do not claim p-integrality of hypothetical untruncated coefficients n>=p.

2. The products (1/6)_k and (1/3)_k meet their unique factor p first at k=m+1 and k=2m+1, respectively. All k! with k<p are units, so

\[
v_p(b_k)=0\ (0\le k\le m);\quad
1\ (m<k\le2m);\quad
2\ (2m<k<p). \tag{2}
\]

For i+j>=p, a summand of total valuation exactly 2 must have one index 1<=i<=m and its partner j=p-t with 1<=t<=i, of valuation 2. The two index orderings are distinct. Pairs with both indices >m have valuation >=3, because two indices <=2m cannot sum to p=6m+1. Therefore (1), modulo p^3, reduces to the *source-preserving triangular tail*

\[
gh-W_p\equiv
2\sum_{i=1}^{m}\sum_{t=1}^{i}(6(i+p-t)+1)b_i b_{p-t}
\pmod{p^3}. \tag{3}
\]

3. The p-1 products contain exactly one factor p each. For (1/6)_{p-1}/p, the nonzero residues of (6r+1) omit -5, so Wilson gives (-1)/(-5)=1/5. For (1/3)_{p-1}/p the omitted residue is -2, giving 1/2. Powers 6^(p-1),3^(p-1),2^(p-1), and ((p-1)!)^2 are units congruent to 1. Hence

\[
\frac{b_{p-1}}{p^2}\equiv\frac1{10}\pmod p. \tag{4}
\]

Reversing the *exact* b_k recurrence gives
\[
\frac{b_{p-t}/p^2}{b_{p-t+1}/p^2}
\equiv\frac{36(t-1)^2}{(6t-1)(3t-1)}\pmod p
\quad(2\le t\le m).
\]
Thus b_{p-t}/p^2=e_t/10 mod p. Writing e_t as a rising-factorial ratio,
\[
e_t=\frac{2^{t-1}((t-1)!)^2}{(11/6)_{t-1}(5/3)_{t-1}}
\equiv\frac{2^{t-1}}{{m+t\choose t-1}{2m+t\choose t-1}}\pmod p,
\]
proves (E), since 11/6=m+2 and 5/3=2m+2 modulo p. Finally 1/6=-m and 1/3=-2m modulo p, yielding b_i=\bar b_i for i<=m.

4. Insert the reflected unit, binomial b_i and 6(i+p-t)+1=6i+1-6t mod p into (3). The factor 2*(1/10)=1/5 gives (C) and the first identity in (L). The accepted UR implies gh=p modulo p^2, while the first identity implies W_p=gh modulo p^2; hence both (gh-p)/p^2 and (W_p-p)/p^2 are integral. Subtracting gives the second identity (L). **QED.**

## Actual exact computation (author-side; not an all-prime proof)

The complete standard-library Python program embedded below was **executed**, using independently generated integer-mod-p^3 2F1/3F2 coefficients and the O(m) F_p reflected/binomial computation. For **all 166 primes p<5000 with p mod 24 in {13,19}**, the cutoff equality, all reflected b_{p-t}/p^2 units, the division integrality and the second-digit decomposition passed. For seven sample primes the checker additionally verified every Clausen coefficient n<p and rebuilt the full triangular tail.

| p | Delta_p | (W_p-p)/p^2 mod p | C_p |
|---:|---:|---:|---:|
| 13 | 0 | 0 | 0 |
| 19 | 12 | 0 | 12 |
| 37 | 11 | 0 | 11 |
| 43 | 15 | 0 | 15 |
| 61 | 3 | 0 | 3 |
| 67 | 21 | 0 | 21 |
| 109 | 50 | 0 | 50 |

**Unproved finite observation:** W_p=p modulo p^3 in all 166 tested target primes. It is a conjectural *uniform strengthening* and is **not used as a premise** of (L). Nor has the separate required comparison C_p=R_p been proved. The actual task's LIFT/JT2 acceptance gate therefore remains **OPEN**. In particular, without first obtaining the frozen source's precise R_p definition and CM/DP same-prime/underlying-class mapping, (L) must not be relabeled as the solved hard target or as a native experiment.

**BRC/observer resolution:** COMPOSE_APPLIED to source-labeled finite p-valuation groups and symmetric cutoff pairs, with exact second-digit observation. F_p compression happens only *after* proving which pairs survive modulo p^3; symmetric multiplicity and original provenance remain explicit. No positive-mass interpretation, native X6/Heartbeat transfer or independent reviewer identity is inferred.

**Source and support boundary:** current Site transport is static_machine_readonly, write_relay_enabled=false, research_authority_granted=false; canonical task inventory probe returned CONTROL_QUOTA. No own session, winning CLAIM, open/run, Source checkpoint, Result, freeze or HANDOFF is asserted. This verified GitHub file is **portable provenance only**, subject to legal Source writer and later independent review. The UR V2 authentic four-file bundle (historical 94,687 bytes and SHA-256 4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76) is still unverified; accepted UR mathematics must not be repeated to fill the provenance gap.

**Next precise action:** with available Source authority, first read own recovery_status and reconcile *original* pending request IDs, read exact continuation and respect the winning claim. On the mathematical side, (i) retrieve the actual source-bound R_p formula, (ii) prove/disprove all-prime W_p=p modulo p^3, (iii) compare the genuine C_p to R_p under the same-prime original CM/DP class. Only after those gates should the valid Source writer checkpoint the reviewed evidence. No new scheduled job, runner or user wake-up is needed.

**Classical reference:** NIST DLMF [16.12.2, Clausen's formula](https://dlmf.nist.gov/16.12.E2), specialized at (a,b)=(1/6,1/3). The new part here is the specific **truncated p-adic cutoff boundary**, reflected Wilson term and streaming second-digit certificate, not the 1828 Clausen identity.

## Executed reproducible exact checker


```python
"""Author-side exact checks for the D24/D25 second-digit Clausen cutoff bridge.

No native Source/CLAIM/Driver assertion. Arithmetic uses only Z/(p^3)Z
with unit inverses, and an independent F_p binomial reflection.
"""
from math import comb, isqrt


def primes_under(n):
    for p in range(13, n):
        if p % 24 not in (13, 19):
            continue
        if all(p % d for d in range(2, isqrt(p) + 1)):
            yield p


def direct_quantities(p):
    M = p ** 3
    b, w = [1], [1]
    for k in range(p - 1):
        b.append(b[-1] * (6*k + 1) * (3*k + 1) *
                 pow(36*(k+1)**2, -1, M) % M)
        w.append(w[-1] * (2*k + 1) * (3*k + 1) * (3*k + 2) *
                 pow(36*(k+1)**3, -1, M) % M)
    g = sum(b) % M
    h = sum((12*k+1)*a for k,a in enumerate(b)) % M
    W = sum((6*k+1)*a for k,a in enumerate(w)) % M
    U = (g*h - W) % M
    assert g % p == 0
    assert U % p**2 == 0
    assert (W - p) % p**2 == 0
    assert (g*h-p) % p**2 == 0
    return b, w, g, h, W, U


def reflected_tail(p, B):
    m = (p - 1)//6
    # A second route via finite-field terminated binomial coefficients.
    s0 = s1 = acc = 0
    b0 = 1
    d = 1
    for i in range(1,m+1):
        # b_i = 2^{-i} binom(m,i) binom(2m,i), because 1/6=-m,1/3=-2m in F_p.
        b0 = b0 * (m-i+1)*(2*m-i+1) * pow(2*i*i, -1,p) % p
        # d_i=2^(i-1)*(i-1)!^2/[(11/6)_(i-1)(5/3)_(i-1)]
        if i > 1:
            d = d * 36*(i-1)**2 * pow((6*i-1)*(3*i-1), -1,p) % p
        # Direct independent residue checks against p^3 series coefficients.
        assert B[i] % p == b0
        assert B[p-i] % p**2 == 0
        assert B[p-i] // p**2 == d * pow(10, -1, p) % p
        # Exact finite-field binomial checksum for small test points.
        if p <= 109:
            assert b0 == comb(m,i)*comb(2*m,i)*pow(2,-i,p)%p
            assert d == pow(2,i-1,p)*pow(comb(m+i,i-1)*comb(2*m+i,i-1),-1,p)%p
        s0 = (s0 + d)%p
        s1 = (s1 + i*d)%p
        acc = (acc + b0 * ((6*i+1)*s0-6*s1))%p
    return acc*pow(5,-1,p)%p


def direct_triangular_tail(p, B):
    m=(p-1)//6; M=p**3; acc=0
    for i in range(1,m+1):
        for j in range(p-i,p):
            # Both i,j admitted, one carries valuation zero, the other two.
            assert B[i] % p and B[j] % p**2 == 0
            acc += 2*(6*(i+j)+1)*B[i]*B[j]
    return (acc%M)//p**2


def main():
    samples = []
    count = w3 = 0
    for p in primes_under(5000):
        B, D, g, h, W, U = direct_quantities(p)
        t = reflected_tail(p,B)
        assert U // p**2 == t, (p, 'tail',U//p**2,t)
        assert (g*h-p)%(p**3)//p**2 == ((W-p)%(p**3)//p**2+t)%p
        if p in (13,19,37,43,61,67,109):
            assert t == direct_triangular_tail(p,B)
            # Degree <p exact Clausen coefficient, modulo p^3.
            M=p**3
            for n in range(p):
                cn=sum(B[k]*B[n-k] for k in range(n+1))%M
                assert cn == D[n],(p,n,cn,D[n])
            samples.append((p, ((g*h-p)%(p**3))//p**2,
                            ((W-p)%(p**3))//p**2, t))
        count += 1
        w3 += (W-p) % p**3 == 0
    print('ALL-PRIME IDENTITY SUPPORTED BY ALGEBRAIC DERIVATION; CHECKS BELOW ARE AUTHOR-SIDE')
    print(f'EXACT MODULAR REGRESSION: {count} target primes p<5000; {count} tail/Clausen bridge passes')
    print(f'FINITE OBSERVATION ONLY: W_p = p (mod p^3) on {w3}/{count} sampled target primes')
    print('p, Delta_p, (W_p-p)/p^2, cutoff_tail/p^2 (all modulo p):')
    for sample in samples:
        print(*sample)

if __name__=='__main__':
    main()

```
