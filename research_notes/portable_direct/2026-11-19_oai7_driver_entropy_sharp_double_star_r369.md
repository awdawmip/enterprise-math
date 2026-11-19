# OAI7 r369 — Near-minimal random entropy for sharp-support logarithmic-coordinate even-cycle samplers

Date: 2026-11-19. Driver-side author extension of the exact construction and necessity proof in r368; includes an **exact information-theoretic identity** and a vanishing entropy-overhead bound. Independent Native Result admission is not claimed.

## Theorem: entropy is asymptotically optimal

Use the r368 sampler for any even integer (p=2r+2\ge4) with (d=1+\lceil\log_2(p/2)\rceil) coordinates and (m=p-1) pairwise translation-inequivalent ordered profiles, each with exactly two supported translations. Let (Z=(X,T)) be the random atom (profile identifier (X), translation (T)) and (Y=(Y_1,\ldots,Y_d)) its full ordered output, where (Y_i=T+w_{X,i}\in\mathbb Z/p\mathbb Z).

Recall (N=p(p-1)+1), (q=(p-1)/(pN)), (Q=(p+1)/(2N)). The (p-2) outer-leaf atoms have mass (1/p) each, the central profile has two atoms of mass (Q), and the remaining (p-2) hub atoms have mass (q) each. Define
\[
\pi_0=pQ=\frac{p(p+1)}{2N},\qquad
\pi_1=pq=\frac{p-1}{N},\qquad
\pi_0+r\pi_1=1.
\]

**Exact entropy formula.**
\[
\boxed{H(Y)=H(Z)=\log_2 p+\frac2p
\left[-\pi_0\log_2\pi_0-r\pi_1\log_2\pi_1\right].}
\]
In particular,
\[
\boxed{\log_2 p\le H(Y)\le\log_2p+\frac2p\log_2\frac p2.}
\]
Thus (H(Y)=\log_2p+O((\log p)/p)\) as even (p\to\infty\). This is asymptotically entropy-optimal among **all** laws with at least one exactly uniform (p)-residue coordinate, because every such law obeys (H(Y)\ge H(Y_1)=\log_2p).

## Proof

The map from a supported atom ((x,t)) to its full output (Y=(t+w_{x,i})_{i=1}^d) is injective: equality of two complete outputs would imply that their ordered profile shapes differ by a common translation, impossible for distinct profiles in r368. For the same profile, different translations give different first coordinates. Hence (H(Y)=H(X,T)=H(Z)).

The first-coordinate output (Y_1) is uniformly distributed on (p) residues. For every outer-leaf residue (v\in\{2,\ldots,p-1\}), there is exactly one compatible atom with probability (1/p), so (H(Z\mid Y_1=v)=0). At either hub residue (v\in\{0,1\}), one central atom of mass (Q) and (r) leaf-profile hub atoms of mass (q) share total probability (1/p). Their normalized conditional probabilities are ((\pi_0,\pi_1,\ldots,\pi_1)), which sum to one. By the chain rule,
\[
H(Z)=H(Y_1)+H(Z\mid Y_1)
=\log_2p+\frac2p\,H(\pi_0,\pi_1^{\times r}).
\]
The entropy of this ((r+1))-point conditional law lies between (0) and (\log_2(r+1)=\log_2(p/2)), proving both bounds and the asymptotic claim. QED.

The bound depends on the mass profile and support structure, not on the choice of (r) distinct nonzero binary codewords in r368. Thus the coordinate compression has **no entropy penalty** in this family. For example (p=30\) admits (d=5) exactly uniform positions, (S=58) positive atoms, and entropy (H(Y)\approx5.091651482258343) bits versus its uniform-residue lower bound (\log_2(30)\approx4.906890595608519); the excess is about (0.1847608866498245) bit.

## Finite numerical check of the analytical entropy identity

~~~python
from math import log2
def evaluate(p):
    assert p >= 4 and p%2==0
    r=(p-2)//2; N=p*(p-1)+1
    Q=(p+1)/(2*N); q=(p-1)/(p*N)
    weights=[Q]*2+[q]*(p-2)+[1/p]*(p-2)
    assert abs(sum(weights)-1)<1e-12
    direct=-sum(z*log2(z) for z in weights)
    pi0=p*Q; pi1=p*q
    conditional=-pi0*log2(pi0)-r*pi1*log2(pi1)
    chain=log2(p)+2*conditional/p
    assert abs(direct-chain)<1e-11
    assert log2(p)-1e-11<=direct<=log2(p)+2*log2(p/2)/p+1e-11
    return p,direct,chain
for p in range(4,152,2):
    evaluate(p)
print("r369 PASS: 74 even moduli satisfy entropy identity")
~~~

The calculations check the formula on finite inputs. The proof for all even (p\ge4) is the injectivity and exact conditional-probability derivation above.

## Scientific provenance and open boundary

Source construction: r367@43f66e0843e0ef369f8ae38c867e05ab36c8fc76; sharp binary-coordinate classification: r368@6f8f6b04bcee2c628accc73a2cc3bf297327ff2d. Original Task RS-OAI7-028-C-20261007-6F2A81 (publication TP2-96FAC49786245691AE19); original researcher EM-EMF6D046-5A2844. Prime-29 OAI7 has fixed profile data outside this even-modulus existence construction; its exact minimal support remains bounded by 378 and 490 in the previous work. This author-side mathematical result is not a frozen Native Result, independent review, formal Task closure, parent Objective closure, or X6 native transfer.
