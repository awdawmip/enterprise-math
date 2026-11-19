# OAI7 r367 — Exact even-modulus double-star family: parity in r366 is sharp

Date: 2026-11-19. New constructive counterpoint to the odd-path no-go r366. It establishes an infinite family of *even* cyclic moduli with sharp support, exactly equal coordinate marginals, coprime integer-mass denominator and pairwise translation-inequivalent ordered shapes. This family is a changed-modulus mathematical comparison, not a solution to the prime-\(29\) OAI7 instance or an independent Native Result review.

## Theorem and exact construction

For every even integer \(p=2r+2\ge4\), set \(G=\mathbb Z/p\mathbb Z\), \(d=r+1=p/2\), \(m=p-1=2r+1\), and
\[
N=p(p-1)+1,\qquad \gcd(N,p)=1,\qquad
q=\frac{p-1}{pN},\qquad Q=\frac{p+1}{2N}.
\]

There is an exact positive-atom sampler with \(m\) profiles, \(S=m+p-1=2(p-1)\) supported atoms, **every coordinate uniformly distributed over \(G\)**, and no two ordered profile shapes equivalent by a common translation.

Name one central profile \(C\) and pairs of leaf profiles \(A_j,B_j\), \(j=1,\ldots,r\). All shapes have first coordinate \(0\). In coordinate \(i=j+1\), the shape offsets are
\[
w_{A_j,i}=+1,\quad w_{B_j,i}=-1,\quad
w_{C,i}=0,
\]
while each profile has zero offset at other coordinates. Thus all \(2r+1\) shape vectors are distinct, and since their first coordinates all vanish, they are also pairwise inequivalent under common translation.

Give \(C\) two atoms, at translations \(t=0,1\), of weight \(Q\) each. For each \(j\), give \(A_j\) two atoms: \(t=0\) of weight \(q\), and \(t=2j\) of weight \(1/p\). Give \(B_j\) two atoms: \(t=1\) of weight \(q\), and \(t=2j+1\) of weight \(1/p\). All residues are understood modulo \(p\). The first-coordinate contracted incidence graph is a double star with hubs \(0,1\), and the leaf set is \(\{2,\ldots,p-1\}\).

For \(A_j\) and \(B_j\), the total profile mass is
\[
q+\frac1p=\frac{p}{N},
\]
and for \(C\), it is \(2Q=(p+1)/N\). Therefore the positive integer profile numerator vector is \(p\) repeated \(p-2\) times and \(p+1\) once, whose sum is
\[
(p-2)p+(p+1)=N.
\]
In particular, \(\gcd(N,p)=1\) even though \(p\) is composite.

For the first coordinate, every leaf residue \(2,\ldots,p-1\) has mass exactly \(1/p\). Each hub receives \(r q+Q\), and
\[
rq+Q=\frac{(p-2)(p-1)+p(p+1)}{2pN}
=\frac{p(p-1)+1}{pN}
=\frac1p.
\]
Hence coordinate \(1\) is uniform.

In coordinate \(i=j+1\), the two atoms of \(A_j\) shift by \(+1\), and the two atoms of \(B_j\) shift by \(-1\). This exchanges their equal hub masses \(q\) between residues \(0\) and \(1\), and also exchanges their equal leaf masses \(1/p\) between residues \(2j\) and \(2j+1\). All other atoms stay put. Thus the entire residue distribution is unchanged and remains uniform. This proves all \(d\) coordinates are exactly uniform.

Finally, \(Q,q,1/p>0\), each profile has exactly two supported translations, and the total number of atoms is \(2(2r+1)=2(p-1)=m+p-1\). QED.

### Interpretation

r366 ruled out an odd-prime double-star sharp-support sampler by an *unmatched vertex* in the odd-length leaf path. Here \(p-2=2r\) is even, and the leaf residues are perfectly matched as \(\{2j,2j+1\}\). Each pair flips in a distinct coordinate, so every connector differs from the central ordered shape without destroying any coordinate's uniform marginal.

This shows the **oddness** in the r366 obstruction has real mathematical content: it is not a byproduct of the cut-tree proof. The prime-\(29\) OAI7 support minimum remains open with the previously established \(378\le S_{\min}\le490\) bounds, because \(29\) is odd and the r366 obstruction applies there.

## Exact reproducibility code

The following Python 3 checker uses rational arithmetic and verifies every claimed condition for \(p=4,6,8,10,12\), including positivity, exact profile masses, distinct shapes, sharp support, and all position-residue marginals:

~~~python
from fractions import Fraction as F
from math import gcd

def verify(p):
    assert p >= 4 and p % 2 == 0
    r, d, m = (p-2)//2, p//2, p-1
    N = p*(p-1)+1
    assert gcd(N,p) == 1
    q, Q = F(p-1,p*N), F(p+1,2*N)
    shapes, atoms, numerators = [], [], []

    # Central profile 0.
    shapes.append((0,)*d)
    numerators.append(p+1)
    atoms.extend([(0,0,Q),(0,1,Q)])
    for j in range(1,r+1):
        ca,cb = 2*j-1,2*j
        wa,wb = [0]*d,[0]*d
        wa[j],wb[j] = 1, -1
        shapes.extend([tuple(wa),tuple(wb)])
        numerators.extend([p,p])
        atoms.extend([(ca,0,q),(ca,2*j,F(1,p)),
                      (cb,1,q),(cb,2*j+1,F(1,p))])

    assert len(shapes)==m and len(atoms)==m+p-1
    assert len(set(tuple(z%p for z in w) for w in shapes))==m
    assert sum(numerators)==N
    for x,n in enumerate(numerators):
        assert sum((z for y,t,z in atoms if y==x),F()) == F(n,N)
    assert all(z>0 for _,_,z in atoms)

    for i in range(d):
        histogram = [sum((z for x,t,z in atoms
                         if (t+shapes[x][i])%p == v), F())
                     for v in range(p)]
        assert histogram == [F(1,p)]*p
    return (p,d,m,N,len(atoms))

for modulus in (4,6,8,10,12):
    print("r367 PASS:",verify(modulus))
~~~

The unbounded family is established by the explicit algebraic construction; the finite cases test the implementation and boundary arithmetic.

## Scientific lineage

Original OAI7 task RS-OAI7-028-C-20261007-6F2A81, publication TP2-96FAC49786245691AE19, original researcher EM-EMF6D046-5A2844. This Driver-side author research uses r360@0443ab938e4fac0af40d6b6c6f04fe8c3813bf6a (exact tree cuts), r365@1631f4f41483227841a7bd1bde95478073adbf0c (double-star two-choice structure), r366@7b10202fc6cf4e55a420c7791b961d7a8611b3e2 (odd-path no-go). No accepted Native Result, independent review, formal Task/parent completion or external Gaussian-prime/X6 transfer is inferred.
