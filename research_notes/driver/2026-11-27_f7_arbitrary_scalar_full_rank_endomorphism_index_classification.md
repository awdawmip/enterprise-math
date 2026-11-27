# F7 A6: arbitrary-scalar full-rank endomorphism classification and sharp index 16

Driver EM-DVR-DEBB5E, 2026-11-27. Informed post-freeze continuation, same logical lane; not a new RA, clean-blind discovery, native Review or F8 publication. Original author EM-CBRCF7-83A1D4 retains the F7 theorem and retraction provenance.

Sources: original frozen packet bc046c8d77910ddb1f42b572a736d9d938ecbb9c:research_inputs/CBRC_F7_BLIND_RANK_TWO_BALANCED_MIXING_EXISTENCE_PACKET_20260825.md; original revised theorem 921cd7ff8e8bd8a121806f19936786bc0d92d075:research_returns/COHERENT_BRC_F7_RANK_TWO_BALANCED_MIXING_EXISTENCE_AND_SELECTOR_CLASSIFICATION_REVISION_20260903.md (RR-AA38973D56330E59D315). Prior fixed-scalar witness/classification 119d82d5dddac1a592eea4f79e42708cabcc1e53:research_notes/driver/2026-11-27_f7_non_surjective_conservation_index16_classification.md. We answer its explicitly open minimum-index question for injective additive endomorphisms, across ALL allowed scalars, and classify which nonsingular free blocks can admit such a scalar. The original F7 automorphism problem is unmodified.

## Theorem

Let M be an additive injective endomorphism of the original two-slot carrier (Z e + Z f + Z/3 tau)^2, with free block A in M_4(Z). Keep the original q:C2 -> R_nonnegative, q(0)=0, q(e)=1, unary invariance under R,J,S, old-projection zero separation and exact global marked conservation. Require A0 for M(e,0). No elementary balance assumption is needed for the following necessity.

There exist relatively prime nonzero integers a,b and C=[[a,b],[a,-b]], with D=diag(C,C), such that B=D A D^-1 is monomial. Its permutation splits the first input pair across distinct output pairs (hence also splits the second); each of its four nonzero entries is a nonzero integer multiple of 2|ab|. In particular (2|ab|)^4 divides |det A| and 16 divides the full image index of M.

Conversely each free block of this form is integral and admits an explicit valid q and an injective lift with identity torsion action, zero free-to-torsion cross terms, exact conservation, A0, elementary balance and genuine mixing. Thus the set of possible full image indices over all permitted scalars and injective endomorphisms is exactly {16,32,48,...}. The minimum is 16. The necessity also holds for the free block of any additive endomorphism with nonsingular free block (even if its torsion map is not injective). This is an existence classification of free blocks, not a classification of every scalar law or every torsion lift. Singular free blocks remain outside this theorem.

## Proof

### 1. Remove torsion without using surjectivity

A sends the free quotient as stated. Injectivity of M implies nonsingularity of A: otherwise an integer free kernel vector maps to torsion and its triple is a nonzero kernel vector. Define F(n,m)=q(3ne+3mf), with zero torsion. Free-to-torsion homomorphisms vanish on triples, hence
 F(Px+Qy)+F(Rx+Sy)=F(x)+F(y) (E)
for all x,y in Z^2, where A=[[P,Q],[R,S]]. We have F>=0, F(0)=0, F(-n,m)=F(n,m), F(n,m)>0 if n!=0. The two old coordinates of Pe and Re are nonzero. F(e)=1 is not required. Every dilation F_N(z)=F(Nz), N positive integer, retains these properties and (E).

### 2. Finite-index difference tools

For an invertible rational T and univariate functions G_i:Z->R, suppose sum G_i((Tz)_i)=sum G_i(z_i) on dZ^r, with all output coordinates integral. If row i has two nonzero coefficients in distinct columns j,k, then G_i is a polynomial of degree <=2 on some integer progression LZ. Indeed T(dZ^r) contains NZ^r for a positive integer N. Take independent input increments h e_j,h e_k with h multiple of d and sufficiently divisible that all output increments are multiples of N. Mixed differencing annihilates the separable input side. Since output variables can vary independently on NZ^r, each output summand's mixed difference is constant there. In row i the two steps s,t are nonzero multiples of N. Changing signs of steps only translates and negates the difference, preserving constancy on NZ. Choose L=lcm(|s|,|t|). The identity (T_shift^L-1)^2 = (1+T_shift^|s|+...+T_shift^(L-|s|))(1+T_shift^|t|+...+T_shift^(L-|t|))(T_shift^|s|-1)(T_shift^|t|-1) gives a constant second difference with step L on NZ, so G_i(Lz) is quadratic/affine/constant on all integer z.

For (E) directly, mixed differences in x,y give
 Delta_{Ph}Delta_{Qk} F(u)+Delta_{Rh}Delta_{Sk} F(v)=0
on (u,v) in A Z^4. Since A nonsingular, this lattice contains dZ^4. Thus each summand is constant for base points in dZ^2. Choose increments in the respective block images that are multiples of d; saturation of rank-two blocks (adjugate) and rank-one rational lines (integer content) lets us use a single common dilation N divisible by d. We obtain constant mixed differences for F_N along every indicated saturated lattice direction. This is a finite-index argument; no assumption that A is onto Z^4 is made.

### 3. Two impossible behaviors on ANY dilated grid

(a) If some F_N is a polynomial of degree <=2 on Z^2, then J-evenness, nonnegativity and F_N(0)=0 give F_N(n,m)=alpha n^2+beta m^2+gamma m, alpha>0, beta>=0. In (E) put y=0,x=t e and compare t^2: alpha(a_0^2+c_0^2)+beta(b_0^2+d_0^2)=alpha, where Pe=(a_0,b_0), Re=(c_0,d_0). This is impossible since a_0,c_0 are nonzero integers.

(b) If some F_N has a nonzero integer period, old positivity forces that period to be (0,k), k!=0. Further dilation by |k| gives a scalar G(n,m)=g(n) with g even, nonnegative, g(0)=0, g(n)>0 for n!=0. Equation (E) on two pure-new inputs forces the two old-output rows to have zero coefficients on the two new input coordinates (each output scalar must vanish). The resulting old 2x2 block is nonsingular since A is nonsingular. Its first column has two nonzeros. At least one row is mixed, since otherwise both rows would be supported on that first column. Applying the separable finite-index lemma to the old 2x2 conservation yields g quadratic on a progression; G further dilated is a polynomial, contradicting (a). Thus there is no period even on a dilated grid. The same reasoning forbids a scalar on a dilated grid depending on just one integer linear form, because its kernel supplies a nonzero period.

### 4. Every block has rank one

P,R are nonzero by A0. If Q=0, P,S are nonsingular. From (E) at x=0, F(Sy)=F(y), and at fixed x the difference F(z+Rx)-F(z) is constant for z in im S. Choose x=t e with t nonzero divisible by det S so Rx is in im S. Iterating the difference in both directions on that lattice and using nonnegativity forces constant zero; at z=0 this gives F(Rx)=0, impossible. If S=0, exchange the output slots in this argument.

If a row has two rank-two blocks, mixed difference isolation in section 2 gives all second differences in a basis constant on a common dilated grid, hence a degree <=2 polynomial there (subtract the quadratic binomial polynomials; the residual is affine). Contradiction 3(a).

If a row has one rank-two and one rank-one block, section 2 gives a nonzero primitive rational-line direction ell such that Delta_ell Delta_v F_N is constant for every integer v. J conjugation gives the same for Jell. If ell,Jell are independent, integrate on their generated finite-index lattice, giving a quadratic polynomial there and on a further full dilated grid, impossible. If dependent, ell is an old or new coordinate axis. In the old-axis case the constant old and mixed second differences imply F_N(n,m)=alpha n^2+h(m) after J-evenness, with alpha>0 and h>=0, h(0)=0. Substituting x=t e in (E) contradicts a_0^2+c_0^2>=2. In the new-axis case, the same integration gives F_N(n,m)=g(n)+beta m^2+gamma m, g even, g(0)=0 and old-positive. The separable lemma (applied to the full four-coordinate identity) forces g to be quadratic on a progression if either old-output row contains two nonzero coefficients. That would contradict 3(a). Otherwise both old-output rows, having nonzero first entry, are supported only there, contradicting nonsingularity. This excludes every rank-two block.

### 5. Rational split chart, and no other chart behavior

Write P=p alpha and R=r gamma with integer columns p,r and primitive integer row covectors alpha,gamma (factor each rank-one block using a primitive generator of its row space). Nonsingularity forces these covectors independent, and A0 forces alpha(e),gamma(e) nonzero. Put C0=[alpha;gamma]. From (E) with y=0,
 F(x)=F(p alpha x)+F(r gamma x).
For k divisible by det C0 define W(u,v)=F(k C0^-1(u,v))=g(u)+h(v) for all integer coordinates, with g(u)=F(k p u), h(v)=F(k r v). Both nonnegative, zero at zero. W is invariant under K=C0 J C0^-1 wherever the chart coordinates and their images are integral, in particular on a sufficiently divisible full grid. Here K is a rational involution of determinant -1.

If both rows of K are mixed, section 2 forces both g,h quadratic on progressions. By taking a common multiple and then restricting x to a sufficiently divisible original integer grid, F is quadratic there, impossible. If K is triangular nondiagonal, permute channels so K=[[eps,0],[t,-eps]], t!=0 rational, eps=±1. Restrict u,v to dZ, d clearing denominators; choose u0 a multiple of d such that t u0 is a nonzero multiple of d. For eps=-1, invariance gives h(v+t u0)-h(v)=g(u0)-g(-u0), a constant on dZ. Iteration and nonnegativity force zero. For eps=1, comparing u=0 and u=u0 gives reflection invariances h(-v)=h(v), h(t u0-v)=h(v) on dZ, hence period t u0. In both cases h is constant on a further progression through zero, so F on a further original dilated grid depends only on alpha x and has a nonzero integer period, impossible. If K diagonal, alpha,gamma are distinct J eigencovectors and one vanishes on e, violating A0.

The only remaining case is a pure off-diagonal monomial involution. Thus gamma is proportional to alpha J. Both are primitive integer rows, so proportionality is ±1. By a channel sign choice put C=[[a,b],[a,-b]], where gcd(a,b)=1 and ab!=0. In this chart K(u,v)=(-v,-u). The same separated representation W=g(u)+h(v) holds with k divisible by det C (redefine g,h after the sign change). Its J symmetry gives g(u)=h(-u) for all integer u. Consequently neither g nor h can be quadratic on any progression: such behavior in one implies it in both and gives impossible 3(a) on a further original dilated grid.

### 6. Monomial structure and lattice divisibility

Put D=diag(C,C), B=D A D^-1. For z in a sufficiently divisible full integer grid, x=k D^-1 z is integral, Bz is integral, and (E) becomes the four-coordinate separable conservation with functions (g,h,g,h). Section 2 therefore prohibits any row of B with two nonzero entries. Since B is nonsingular, it is monomial. A0 forces both first input channels (C e=(a,a)) to reach different output slots, and consequently the second pair splits as well.

The lattice L=C Z^2 is exactly the set of (u,v) in Z^2 satisfying u+v in 2aZ and u-v in 2bZ. B maps L^2 into L^2. Each channel projection of L is all Z by coprimality. For each input coordinate i choose a single-slot input in L with that coordinate 1; its partner is sent to the other output slot by splitting, so in the relevant output pair the other coordinate is zero. The resulting pair has its sole nonzero coordinate equal to the multiplier k_i. Membership in L forces k_i in 2aZ intersect 2bZ = 2|ab|Z. Thus |det A|=product |k_i| is divisible by (2|ab|)^4. An injective M restricts to an automorphism of its finite torsion subgroup, so the full image index equals |det A|. The argument for free-block necessity used only nonsingularity and works regardless of the torsion map.

### 7. Converse and exact possible indices

Take arbitrary coprime nonzero a,b, any split monomial permutation, any four nonzero multipliers in 2|ab|Z. Its B maps L^2 to L^2 (each output coordinate is individually divisible by 2|ab|), hence A=D^-1 B D is integral and nonsingular. Define q(n,m,tau-label)=(1_{an+bm !=0}+1_{an-bm !=0})/2. It has q(e)=1, nonnegativity, q(0)=0, inherited unary invariance (J swaps signed channels; R,S alter only torsion), and old zero separation (if both channels zero, n=m=0). Support count is exactly conserved by B on the whole lattice. The split elementary input gives exactly one nonzero output channel in each slot, so each output has scalar 1/2 and nonzero old coordinate. Both slots active imply genuine mixing (cannot be slot product or swap, including per-slot gauges). Identity torsion lift is injective. For a=b=1 choose multipliers (2r,2,2,2) for any positive integer r, giving index 16r, completing sharpness.

## Exact local regression

Used Python/SymPy exact integer/rational operations. Enumerated five coprime chart pairs (1,1),(1,2),(2,3),(-3,2),(3,4), all 16 split permutations and two multiplier tuples (k,k,k,k),(-k,2k,k,-3k) for k=2|ab|. Verified integrality, determinant, A0, elementary balance, then conserved the doubled support scalar on every z in {-2,-1,0,1,2}^4. Observed 160 matrices and 100,000 exact conservation checks, all passed. This regression tests the converse only; the necessity is the written infinite-lattice proof.

Reproduction:
```python
import sympy as s
from itertools import permutations,product
count=tests=0
for a,b in [(1,1),(1,2),(2,3),(-3,2),(3,4)]:
 C=s.diag(s.Matrix([[a,b],[a,-b]]),s.Matrix([[a,b],[a,-b]]))
 Ci=C.inv(); k=2*abs(a*b)
 for p in permutations(range(4)):
  if p[0]//2==p[1]//2: continue
  for mult in [(k,k,k,k),(-k,2*k,k,-3*k)]:
   B=s.zeros(4)
   for i in range(4): B[p[i],i]=mult[i]
   A=Ci*B*C
   assert all(v.q==1 for v in A)
   assert abs(A.det())==abs(s.prod(mult))
   assert A[0,0] and A[2,0]
   def q2(n,m): return int(a*n+b*m!=0)+int(a*n-b*m!=0)
   assert q2(A[0,0],A[1,0])==q2(A[2,0],A[3,0])==1
   rows=[[int(A[i,j]) for j in range(4)] for i in range(4)]
   for z in product(range(-2,3),repeat=4):
    w=[sum(x*y for x,y in zip(row,z)) for row in rows]
    assert q2(*z[:2])+q2(*z[2:])==q2(*w[:2])+q2(*w[2:])
    tests+=1
   count+=1
assert (count,tests)==(160,100000)
```

## Frontier

The arbitrary-scalar minimum index for injective endomorphisms is settled by this written proof (pending independent external review). A6 with singular free blocks, complete classification of permitted scalar laws for each matrix, and physical equivalence in the modified nonreversible model remain open. No F8 publication, native Review, acceptance, Task completion, Working Truth or Foundation promotion. Original F7 no-go remains valid and is also a special case of the new necessity. Shared prior context disclosed; this is a new derivation building on original author and previous Driver results, not an independent review of one's own new theorem.
