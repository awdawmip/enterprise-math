# D25 / signed upper-shell transport: 216 versus 2304 and a source-backed all-prime cancellation

2026-11-05; TASK_RESEARCH author-side mathematics; **UNREVIEWED / NOT_ADMITTED**. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7, frozen input c47e13e4aba0e006366f989d6334d443f6333ae3. Research lane chatgpt-research-onhour-enterprise-math-20260923, distinct from maintenance.

## Exact original-source theorem (proved)

Let p>3 be prime, write a_k=binom(2k,k)^2 binom(3k,k)/216^k, b_k=binom(2k,k)^2 binom(4k,2k)/2304^k, and let W_p=sum_{k=0}^{p-1}(6k+1)a_k, V_p=sum_{k=0}^{p-1}(8k+1)b_k. Subscript half denotes k=0,...,(p-1)/2. Define the explicit F_p factorial sums

    T_A(p)=sum_{j=floor(p/3)+1}^{(p-1)/2} (6j-1)*216^(j-1)*(j-1)!^5/((2j-1)!*(3j-p-1)!)
    T_B(p)=2*sum_{j=floor(p/4)+1}^{(p-1)/2} (8j-1)*2304^(j-1)*(j-1)!^4/(4j-p-1)!.

All displayed factorial indices lie in [0,p-1] and are invertible in F_p. Then for **every prime p>3**

    W_p-W_half ≡ p^2*T_A(p) (mod p^3);
    V_p-V_half ≡ p^2*T_B(p) (mod p^3).

**Proof.** On p/2<k<p, v_p(binom(2k,k))=1. For k≥2p/3, v_p(binom(3k,k))=1 and a_k vanishes mod p^3; for k≥3p/4, v_p(binom(4k,2k))=1 and b_k vanishes mod p^3. Remaining upper shells are respectively p/2<k<2p/3 and p/2<k<3p/4. Put k=p-j. Wilson reflection and Lucas give, for the relevant j windows,

    binom(2(p-j),p-j)/p ≡ -(j-1)!^2/(2j-1)!   (mod p)
    binom(3(p-j),p-j) ≡ -(j-1)!*(2j-1)!/(3j-p-1)! (mod p)
    binom(4(p-j),2(p-j)) ≡ -2*(2j-1)!^2/(4j-p-1)! (mod p).

The third equality is only needed on the b-shell, the second only on the a-shell. Fermat gives 216^{j-p}=216^{j-1} and 2304^{j-p}=2304^{j-1} mod p. Weighted factors 6k+1, 8k+1 become 1-6j, 1-8j. Multiply to obtain the two announced sums with their positive signs. QED.

## Published full-and-half 2304 supercongruence and consequence

Victor J. W. Guo and Wadim Zudilin, *A q-microscope for supercongruences*, Advances in Mathematics **346** (2019), 329–358, DOI 10.1016/j.aim.2019.02.008, arXiv:1803.01830v6 (revised 2019-02-13), prove for **all p>3** both

    V_p ≡ p*((-3)/p) (mod p^3) and V_half ≡ p*((-3)/p) (mod p^3).

Their summand has denominator 2^(8k)*3^(2k)=2304^k and is exactly this original b_k, including weight (8k+1). Applying the proved shell theorem yields the following **all-prime exact literature corollary**:

    sum_{j=floor(p/4)+1}^{(p-1)/2}
        (8j-1)*2304^(j-1)*(j-1)!^4/(4j-p-1)! ≡ 0 (mod p).

This is a derivative corollary of a 2019 published theorem; independent peer review of the present arithmetic re-expression remains pending.

Consequently the remaining cross-model target reduces **exactly** for every p>3 to

    W_p-V_p ≡ W_half-V_half+p^2*T_A(p) (mod p^3).

It follows that W_p≡V_p (mod p^3) if and only if

    W_half ≡ p*((-3)/p)-p^2*T_A(p) (mod p^3).

On the frozen target classes p≡13,19 (mod 24), ((-3)/p)=+1, giving the explicit unresolved target W_half ≡ p-p²*T_A(p) (mod p³). This reduction uses the published 2304 source, not a conjectural equality of the two full sums. The 216 high shell retains a genuinely nonzero signed repair coordinate in the tested range.

## Independent exact computation

The accompanying checker uses (a) original integral factorial-ratio recurrences for a_k and b_k mod p³, and independently (b) these F_p factorial shells, checking all 301 primes 5≤p≤2000. The 602 original-shell comparisons and 602 full-sum comparisons against p*((-3)/p) have 0 failures. T_B(p)=0 and T_A(p)≠0 for each of these 301 primes. **Those are finite checks; the W congruence for all primes is not claimed proved.** Exact witnesses (p,T_A,T_B): (5,1,0), (13,10,0), (19,9,0), (139,13,0), (373,266,0).

BRC: COMPOSE_APPLIED; retained carrier (model label, term index, p-valuation, signed weight, mod-p^3 residue). Only the proven Guo–Zudilin cancellation permits collapsing the b shell. The a shell repair survives. No native X6 bridge is claimed.

## Remaining scientific and Source obligations

Proof target: find an exact finite WZ/q-microscope/CM kernel for the corrected 216 half-sum, first discriminating witnesses p=13,19,139,373, then close weighted W_p-V_p before frozen Delta_p-R_p. Existing Sun/Green/CM first-jet proofs are consumed, not reissued. Native fixed p=373 original-class H0/B0 divided-power [X]U mod 139129, module rank, semilinear Frobenius, eta/kappa and independent replication remain Issue #1559, NOT_EXECUTED. No native CLAIM/run/checkpoint/Result is created by this author-side GitHub note.
