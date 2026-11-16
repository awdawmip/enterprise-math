# PREFIX-843 — Exact fiber lattice, irreversible modular aliasing, and minimal named-source repair

Date: 2026-11-16. Scientific status: AUTHOR_PROVED / EXACT_FINITE_REGRESSION / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.
Frozen scientific input: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d (unchanged).
Direct scientific predecessor: PREFIX-842 (2026-11-16_r6_prefix842_uniform_time_modular_provenance_minimal_modulus.md), which proves uniform injectivity and minimum raw modulus.

## Exact auxiliary BRC model and observer

This note stays within the Q-only, positive-integer tagged one-original-deletion observer from PREFIX-840–842. There are p>=1 publicly ordered original sources, weights w_i in {1,...,W}, W>=2, and Q=R+A updates with marked-source addition/removal weights a,b>=1. Formal time t>=1 counts Q updates (not physical heartbeat time). The tagged channel produces

D_i(t)=c_t w_i,  c_t=a^floor(t/2)b^floor((t-1)/2).

Put N=W^p, S=sum_{i=0}^{p-1} W^i and U=sum_{i=1}^p (w_i-1)W^(i-1), so 0<=U<N. The single coded raw output is

Z(t)=c_t(S+U),  Y_t=Z(t) mod m,

for an arbitrary fixed integer modulus m>=1. The receiver knows p,W,a,b,m,t, and retains the typed named-source observer. No native Cell/Link/Port permission is asserted by this auxiliary construction.

## Theorem 843.1 — Exact observation fibers

Let g_t=gcd(m,c_t) and M_t=m/g_t. For two assignments U,V in [0,N),

Y_t(U)=Y_t(V)  iff  U ≡ V (mod M_t).

The number of distinct output classes is min(N,M_t). The fiber of any residue r=U mod M_t consists exactly of

{ r+j M_t: j>=0, r+j M_t<N }.

Consequently its size is either floor(N/M_t) or ceil(N/M_t) (ignoring empty residues), and the largest nonempty fiber has precisely ceil(N/M_t) assignments. These are equality claims for every p,W,a,b,m,t in the declared domain, not merely bounds.

**Proof.** For any integer x, m divides c_t x iff m/gcd(m,c_t) divides x, by factoring the common gcd and using coprimality. Apply this to Z(U)-Z(V)=c_t(U-V). The N possible U form consecutive integers. Their residue classes modulo M_t supply the claimed exact fibers and counts. QED.

## Theorem 843.2 — Future modular observations coarsen, without reversal

For t<s, c_t divides c_s. Hence M_s divides M_t, and

Y_s ≡ (c_s/c_t) Y_t (mod m).

Thus the raw modular observation partition at s is a coarsening of the partition at t. No collection of Y_s,Y_(s+1),... can distinguish two assignments already aliased at time s. Moreover, for C=ab and the C-coprime factor m_perp(C) from PREFIX-842, there exists finite t_0 with M_t=m_perp(C) at every t>=t_0. The eventual number of observable classes is min(N,m_perp(C)).

**Proof.** The exponents of a and b in c_t are nondecreasing, so c_t|c_s. Multiplication by c_s/c_t transports any Y_t to Y_s modulo m. From divisibility, gcd(m,c_t)|gcd(m,c_s), whence M_s|M_t. Every prime dividing C gains unbounded valuation in c_t; every other prime never divides c_t, giving eventual gcd(m,c_t) equal to the full C-primary part of m. This proves stabilization and the exact class count by Theorem 843.1. QED.

**Observer distinction.** PREFIX-832–835 identify temporary re-collisions for the *complete, unreduced Q histogram*; the present theorem concerns only the specified *fixed raw modular tagged scalar*, whose loss is monotone. The observers and their equivalence relations are different.

## Theorem 843.3 — Minimal fixed-length repair coordinate

Given Y_t and the known public parameters, the smallest number of *additional fixed-length bits* needed to distinguish all N ordered weight assignments in the worst case is exactly

B_repair(t)=ceil(log2(ceil(N/M_t))),

with B_repair(t)=0 if M_t>=N.

One optimal extra integer coordinate is h_t=floor(U/M_t), belonging to [0,ceil(N/M_t)-1]. The decoder first recovers r=U mod M_t. Since g_t divides Y_t, put z=Y_t/g_t and d=c_t/g_t. If M_t>1,

r ≡ d^(-1) z - S (mod M_t);

if M_t=1, r=0. Then U=h_t M_t+r, and its p base-W digits recover (w_1,...,w_p).

The minimal *time-uniform* extra bit count for this fixed m is

B_repair(infty)=ceil(log2(ceil(N/m_perp(ab)))).

**Proof.** The largest fiber at time t contains L=ceil(N/M_t) assignments; an ancillary fixed-length binary alphabet distinguishing them needs at least L codes, hence at least ceil(log2 L) bits. Within any observed fiber the assignments have distinct quotient h_t=floor(U/M_t), which is always in [0,L-1]; this attains the bound. gcd(d,M_t)=1, so the displayed inverse recovers r; recombination is exact. The fiber partitions coarsen monotonically and stabilize by Theorem 843.2, yielding the stated uniform optimum. QED.

The repair is a mathematically defined *extra provenance coordinate*; computing it may require access to the hidden named weights. This theorem quantifies the information that the raw observer omits, not a permission to inspect hidden native state.

## Proposition 843.4 — Raw modular storage overhead is unbounded as a,b vary

For any integer L>=4 take p=W=2, N=4, a=lcm(1,2,...,L), b=1. In PREFIX-842's unrestricted-future *single raw modulus* interface, the least uniformly injective modulus satisfies m_infty^*>L, while the intrinsic named-assignment payload is always exactly 2 bits.

**Proof.** Every 2<=m<=L has only prime divisors dividing a. Hence m_perp(ab)=1<N. Also m=1 has C-coprime part one. By PREFIX-842's iff criterion no such m is uniformly injective. The four weight assignments still require and admit 2 bits when represented by normalized U. Thus the raw modulus register width ceil(log2 m_infty^*) can exceed the information-theoretic payload width by an arbitrarily large amount as L grows. QED.

This is an exact *interface-dependent* phenomenon. A normalized, provenance-aware carrier storing U itself uses the optimal ceil(log2 N) bits at every time; recovering U *from an already collapsed raw residue* requires the explicit repair coordinate of Theorem 843.3. Replacing the raw modular observer by normalized U changes the declared interface and computation.

## Worked examples

For p=W=2, a=2,b=1, N=4 and m=4:
- t=1: c_t=1, M_t=4, 4 classes, 0 repair bits;
- t=2,3: c_t=2, M_t=2, 2 classes, 1 repair bit;
- t>=4: c_t multiple of 4, M_t=1, 1 class, 2 repair bits.

For the same model with m=5, M_t=5 at every t, and all four assignments remain distinguishable with zero repair.

For N=9, a=2,b=3, m=10, eventually M_t=5. Nine assignments occupy five fibers, the largest of size two; one extra bit is sufficient and necessary after stabilization.

## Exact finite verification

The accompanying standalone Python exact-integer checker enumerates p=1..4, W=2..4, a,b=1..4, m=1..16 and t=1..8. For every ordered weight assignment (via its base-W index U) it compares actual residues against the predicted congruence fibers, checks exact class sizes, exact quotient repair and divisibility/coarsening, and tests all possible assignment pairs for the forward-ambiguity implication.

Observed scope: 192 parameter families; 24,576 time/modulus cases; 1,003,520 assignment/residue and repair checks; 115,708 observed nonempty fibers; 21,504 monotone-step checks; 69,112,064 temporal pair implications. Seven lcm construction checks use L=4,8,10,20,30,40,50. All assert statements returned ALL_EXACT_ASSERTIONS_PASSED. Python arbitrary precision arithmetic; no floating numerical premise is used in the checker.

A finite enumeration supports the implementation and examples. The four general claims are justified by the arithmetic arguments above; no independent mathematical review has been completed.

## Next discriminating questions

1. When is the quotient repair coordinate h_t available through an actually permitted native Cell/Link/Port event rather than by inspecting hidden weights?
2. For a constrained observer/communication architecture, optimize *joint* output and repair cost, not only conditional repair bits.
3. Determine the smallest BRC state quotient sufficient for multiple tagged observers, not just one raw modular scalar, and preserve source/port attribution.

This result is an independent auxiliary scientific artifact. No shared X6 CLAIM, native event bridge, independent Review, Result admission or Foundation promotion is inferred.
