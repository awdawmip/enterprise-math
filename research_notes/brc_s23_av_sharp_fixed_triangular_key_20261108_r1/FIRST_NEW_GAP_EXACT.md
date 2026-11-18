# S23/AV: first new w+u threshold gap at H=2,455,579 has exact minimum prefix length 4,910,648

Date: 2026-11-08 Asia/Shanghai. Status: symbolic exact proof and executable integer certificate; author-side, independent review pending.
Frozen scientific source: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Context: follows the seven-plateau source checkpoint at commit 24c35e02b959409960645753bd2bc8c92147a390, which left the exact overall capacity N(2455579) open; uses the strict lexicographic threshold-order theorem in this research directory.

## Theorem

Define u=(79,431), w=(D,P)=(380295,2074774), M=D+P=2455069, r=ln7/ln(10/7), epsilon=79r-431, eta=P-Dr. Let H=M+510=2455579. The two threshold values

   0=t(0,0)  and  t(u+w)=epsilon-eta>0,

with u+w=(380374,2075205), are consecutive in the exact future threshold set

   T_H={rv-j : v,j>=0, v+j<=H}.

Define an attainable prefix score E(k,l)=k-r*l for nonnegative k,l. The smallest prefix length k+l for which

   0 < E(k,l) < epsilon-eta

is EXACTLY 4910648, attained at

   (l,k)=u+2w=(760669,4149979),
   E(k,l)=2eta-epsilon.

### Exact proof

The rational logarithm enclosure from the previous proofs rigorously gives

    0<eta<epsilon<2eta   and   2epsilon>3eta.

At H=M+510 the strict order is represented by the exact lexicographic integer key (P*v-D*j,-v), proved throughout H<2M+510 in PROOF_LEX_EXTENSION.md.

The key-zero fiber in the nonnegative triangle is exactly w,(0,0), in increasing threshold order (w has threshold -eta). The key-one fiber is exactly u+w,u, in increasing threshold order (u+w has epsilon-eta and u has epsilon). No key can lie strictly between integers 0 and 1. Therefore (0,0) and u+w are adjacent, with the indicated exact gap.

For the prefix (l,k), use the unimodular expansion

    (l,k)=A*u+B*w,     A=P*l-D*k,   B=79*k-431*l,

so

    E(k,l)=B*eta-A*epsilon,
    k+l=510*A+M*B.

If 0<E<epsilon-eta, then B>0: B<=0 together with l=79*A+D*B>=0 forces A>=0, hence E<=0. Also A>=0: A<=-1 would imply E>=eta+epsilon>epsilon-eta. Thus B>=1 and A>=0.

When B=1, A=0 gives E=eta>epsilon-eta because epsilon<2eta, whereas A>=1 gives E<=eta-epsilon<0. Hence B>=2. When B>=3 the length is >=3M>2M+510. The candidate B=2,A=1 has length 2M+510=4910648 and score E=2eta-epsilon, which is strictly between zero and epsilon-eta exactly because epsilon<2eta and 2epsilon>3eta. This proves sharp first entry.

A new gap appearing at H=2455579 therefore has an explicit optimal prefix witness with length 4910648. Since the preceding seventh-plateau capacity was 14905515, this particular gap is covered by that existing capacity budget. This finding resolves the first new w+u gap, not the completeness of all other new cells or the exact N(2455579).

## Executable certificate / next

VERIFY_NEW_GAP.py checks the rational inequalities with integer cross products, the entire relevant key-zero/key-one fibers, exact consecutive ranks, the explicit prefix witness and the short algebraic lower-bound inequality. RUN_NEW_GAP.txt is its actual console output. The verifier imports the neighboring two exact libraries from this directory; all three source files are published and checked against the executed local versions.

Next: evaluate every other new cell at H=2455579 under the old n=14905515 budget with the exact prefix occupancy oracle, or classify the changed cells by key and boundary. Either produce an empty-cell certificate proving the jump or a full upper-cover certificate proving persistence.