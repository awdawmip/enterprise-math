# OAI7 r340 — Prime cyclic rigidity of two-shape translation switching

Date: 2026-11-18. Evidence: new exact finite-algebra obstruction, with a fully enumerated composite-modulus contrast; author-side mathematical note, not an independent Native review or a formal Result. The original OAI7 researcher EM-EMF6D046-5A2844 and all source contributors retain their provenance.

## Theorem: Two different shift shapes cannot be switched on a proper set of prime translations while preserving exact incidence regularity

Let p be prime and W,V be two **distinct n-element subsets** of F_p, where 1<=n<p. For each t in F_p choose one of the two translated sets by a switching set T subseteq F_p:

```
C_t = V+t   if t in T;
C_t = W+t   if t not in T.
```

Then the following are equivalent:

1. Every residue a in F_p occurs in exactly n of the p sets C_t, counting labeled rows;
2. T is empty or T=F_p.

In particular, **a nonempty proper mix of two distinct translation orbits cannot produce a p-row n-regular codebook**. This is an exact assertion about the displayed one-translate-per-index switching class, not about arbitrary n-regular p-row codebooks, mixtures of three or more shapes, or weighted/nonuniform schedules. It rules out a specific inexpensive attempt to convert r330's mixed covering codebook into the entropy-log-p capacity class of r339.

### Proof by the cyclotomic field factor

For a subset S of F_p write its characteristic polynomial F_S(X)=sum_(s in S) X^s in Z[X] (representatives 0,...,p-1). Exact incidence degree n at every residue means that, in the group ring Z[X]/(X^p-1),

```
sum_(t not in T) X^t F_W(X) + sum_(t in T) X^t F_V(X)
     = n*(1+X+...+X^(p-1)).
```

The all-W orbit already has this exact degree-n identity, since each a lies in exactly n translated copies W+t. Subtracting its identity shows that regularity is equivalent to

```
F_T(X)*(F_V(X)-F_W(X)) = 0 mod (X^p-1).         (340.1)
```

Let zeta be a primitive p-th root of unity. From (340.1),

```
F_T(zeta)*(F_V(zeta)-F_W(zeta))=0.
```

For prime p, zeta has irreducible minimal polynomial Phi_p(X)=1+X+...+X^(p-1) over Q. If T is nonempty proper, F_T has degree <=p-1 with coefficients in {0,1}, not all equal. Consequently Phi_p cannot divide F_T, and F_T(zeta) is nonzero: otherwise degree comparison would make F_T a rational multiple of Phi_p and therefore constant coefficient-by-coefficient.

Likewise F_V-F_W has degree <=p-1 and total coefficient sum |V|-|W|=0. If (F_V-F_W)(zeta)=0, irreducibility forces F_V-F_W=c Phi_p. Evaluation at X=1 gives 0=cp, so c=0 and F_V=F_W, contradicting V!=W. Thus both factors are nonzero, contradicting (340.1). Therefore T is empty or all F_p.

For those two endpoint choices the family is a complete translate orbit of W or V, hence every symbol indeed occurs n times. QED.

This proof is exact over Q and uses no probabilistic sampling, numerical approximations, or assumptions about all-K coverage.

## Why primality is material: an explicit modulus-4 counterexample

Take the cyclic group Z/4Z with n=2, W={0,1}, V={2,3}, T={0,2}. The four labeled translated rows are

```
t=0: V+0 = {2,3}
t=1: W+1 = {1,2}
t=2: V+2 = {0,1}
t=3: W+3 = {3,0}.
```

They are pairwise distinct; residues 0,1,2,3 each appear exactly twice. Thus this is a genuine nontrivial two-shape switch maintaining exact regularity in a **composite** cyclic group. Algebraically, 1+X^2 annihilates the difference F_V-F_W modulo X^4-1. The proof for prime p succeeds because the nontrivial cyclotomic component of Q[C_p] is a field; composite cyclic rings may have additional nontrivial factors and zero divisors.

## Connection with r338/r339 and next design route

In r339, any p-row, n-regular codebook over F_p with pairwise distinct rows admits a zero-extra-seed deterministic ordering with equal complete position marginals and Shannon entropy log p. A single full translate orbit reaches the regularity condition automatically, but its all-fixed-K bad-start statistic is identical across all rows; achieving q<1 in that orbit family therefore needs one universally good base W.

The theorem shows that choosing a single W or V at each translation index t cannot nontrivially combine two different shapes *and* keep that exact regularity. Hence building an all-fixed-K-good regular p-row codebook should test genuinely different designs, e.g. more than two independently coupled shape classes or non-orbit incidence matrices. This is a **structural elimination of one proposal**, not a general no-go theorem for entropy log p.

The r329/r330 all-K estimates are cited background only. No claim is made that all-K covering is impossible or that Gaussian-prime/native X6 dynamics follows from this algebraic result.

## Source and contribution provenance

- OAI7 formal task RS-OAI7-028-C-20261007-6F2A81, TP2-96FAC49786245691AE19; original researcher EM-EMF6D046-5A2844.
- r337: cf352564a8f985fbc3151783fa0ee74f1a0b2a7f; equal-position deterministic ordering criterion.
- r338: ef08b7b5dbdb489647fc70e1f88f7a714cec991f; exact uniform auxiliary seed branching count.
- r339: b7bd6de6e1381fd04b0b37c16a56f14cea3b92f2; support capacity Mt>=m and prime-field equality case.
- New r340: prime two-shape switching rigidity and a modulus-4 counterexample. Status remains author-side saved finite proof; current Native Result acceptance, independent reviewer act, Source/Activity semantic linkage and formal Task completion require separate evidence.
