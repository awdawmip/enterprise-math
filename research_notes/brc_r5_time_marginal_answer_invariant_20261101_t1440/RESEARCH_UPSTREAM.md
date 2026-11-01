# R5 upstream-kernel classification — COMPLETE two-parameter all-real exclusion

Date: 2026-11-01 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. Frozen GLOBAL_KNOWLEDGE_V1 main a79db1aa492e6e05d95da61481bce3e3292109d8; Enterprise Math main 1cce3e5a5246da8660e995cc5ea67182785504ef. Base model/evidence: da5f5835bc20e2059bc7de82e99d28274c10f623 and the time-only theorem in this directory. Scope: finite two-law auxiliary stopping model, not native P000/X6 theorem. The mother four-observer question remains OPEN outside this exact family.

## 1. Exact lawful model and full parameter domain

Hidden origins A1,A2,B,C carry P masses (1/8,1/8,1/4,1/2) and Q masses (1/8,1/8,1/8,5/8). The genuine shared time–likelihood ratio keys remain I=(t1,LR1) and J=(t2,LR2). Independent upstream low nature chances are A1 (P,Q)=(2a,a), A2=(2b,b), where 0<a,b<1/2. A1/A2 high branches stop at time2 answering P; low branches meet bypass B at J. At I, A1/A2 stop answering Q at time1 with probabilities p1,p2. At J, A1/A2/B stop answering Q at time2 with probabilities q1,q2,qB or continue to time3. C stops answering P at time1 with probability r or continues to time3 answering Q. A1 continuing from J splits X/Y at time3 with conditional P(X)=3/5,Q(X)=1/2; X answers P and Y answers Q. A2/B continuing from J answer Q at time3. The same behavioral randomization is used under P and Q; FULL uses independent (p1,p2,q1,q2,qB,r) and LR ties p1=p2=p, q1=q2=qB=q. All probabilities are in [0,1].

All exogenous nature chances remain strictly positive in the given open domain. Each A low path has LR 2 by construction, hence J is still a genuine collision with B. High time2 LRs (1-2a)/(1-a), (1-2b)/(1-b) lie in (0,1); both answer P and cannot collide with J's time2 LR2/Q answer. A1 X/Y at time3 have LR12/5 and8/5, A2/B time3 LR2, C time3 LR4/5: answers are consistent with one time/LR terminal answer map. This is a lawful double-measure stop model, not a relabelled coarse key.

## 2. Exact all-signed time support and the equality locus

Put si=1-pi, ti=1-qi, tB=1-qB, z=1-r. Direct source-mass conservation under both P,Q gives

T=(TP,TQ)=T0+v(s1+s2)+w(a*s1*t1+b*s2*t2+tB)+c*z,
T0=(5/4,9/8); v=(1/8,1/8); w=(1/4,1/8); c=(1,5/4).

Under LR this becomes T_LR=T0+2s*v+w*(1+(a+b)s)*t+c*z. For any real signed time direction n, define V=n·v, D=max(0,n·w). Since a,b,si are nonnegative, optimizing each t term takes value 1 if n·w>0 and 0 otherwise; r/z is independent. The **exact support functions of all real behavioral images** are:

h_FULL(n)=n·T0+max(0,n·c)+D+max(0,V+aD)+max(0,V+bD),
h_LR(n)=n·T0+max(0,n·c)+D+max(0,2V+(a+b)D).

Thus Delta(n)=max(0,V+aD)+max(0,V+bD)-max(0,2V+(a+b)D) >=0. If a=b, Delta(n)=0 in every real signed direction, because 2*max(0,x)=max(0,2x). Bounded compact convex sets with identical support functions are equal: the entire two-dimensional FULL/LR time-marginal convex hulls then coincide.

If a!=b, choose n(a,b)=(8+4(a+b), -8-8(a+b)). Exactly n·w=1 and n·v=-(a+b)/2. The two source advantages equal ±(a-b)/2, and the common LR advantage is zero, hence the **exact all-real signed gap**

h_FULL(n)-h_LR(n)=|a-b|/2>0.

Therefore the time-marginal convex hulls are equal **if and only if a=b** throughout 0<a,b<1/2. At original a=1/4,b=3/8, twice n is (21,-26), yielding the previous time-only gap 1/8.

## 3. Full four-observer LR rank and exact chart

With the same fixed X/Y terminal answers, direct positive source-flow counting gives

eP = [p1+(1-p1)*2a*(q1+(1-q1)*2/5)]/8
    +[p2+(1-p2)*2b]/8 +1/4+(1-r)/2,
eQ = [(1-p1)*((1-a)+a*(1-q1)/2)]/8
    +[(1-p2)*(1-b)]/8+5r/8.

The time components are as above. The four-observer LR image has exact multi-affine chart

O_LR(p,q,r)=O0+pB+qC+pqD+rE,

with these four-vectors in order (eP,eQ,TP,TQ):

O0=(a/10+b/4+3/4, 1/4-a/16-b/8, 11/4+(a+b)/4, 11/4+(a+b)/8)
B=(1/4-a/10-b/4, a/16+b/8-1/4, -(a+b+1)/4, -(a+b)/8-1/4)
C=(3a/20, -a/16, -(a+b+1)/4, -(a+b+1)/8)
D=(-3a/20, a/16, (a+b)/4, (a+b)/8)
E=(-1/2,5/8,-1,-5/4).

The exact 4-by-4 determinant is

det[B C D E] = a*(31-3a-3b)/5120 > 0

for every 0<a,b<1/2. This follows from expanding the displayed columns. The standalone exact verifier also evaluates the polynomial on a 4-by-4 rational tensor interpolation grid: E is constant, other three columns are affine in a,b, so the difference from the displayed expression has bidegree at most (3,3); sixteen exact zero checks prove the identity for all real (a,b) by elementary polynomial interpolation. Consequently LR retains **full four-dimensional affine rank for all parameters**, diagonal included.

Because the chart is invertible, any actual LR behavior has the unique affine coefficients (u,v,s,w)=(p,q,pq,r). Its actual image is nonconvex: the midpoint of (0,0,0,0) and (1,1,1,0) has s=1/2 but u*v=1/4. This holds throughout the open parameter domain.

## 4. On the diagonal, the time obstruction vanishes but a four-dimensional obstacle survives

Let a=b=t in (0,1/2). The valid FULL policy (p1,p2,q1,q2,qB,r)=(1,0,0,0,0,1) yields

W_t=(3/8+t/4, 3/4-t/8, 13/8+t/4, 11/8+t/8).

Direct substitution into the four displayed LR columns gives the exact polynomial identity

W_t-O0_t = (1/2) B_t - t C_t - (t+1/2) D_t + E_t.

Invertibility makes this chart unique: W_t has (u,v,s,w)=(1/2,-t,-t-1/2,1), so its s-coordinate is strictly negative. Every *real* LR point has s=pq>=0, and every LR convex combination also has s>=0. Therefore the affine functional taking the D coefficient of A_t^{-1}(O-O0_t) separates W_t from the entire LR four-dimensional convex hull with a strict score difference at least t+1/2. This is a valid **all-real** separating hyperplane, not an observation about finite sampled parameters.

## Complete theorem / interpretation

For every 0<a,b<1/2 in this entire genuine-key, strictly positive two-source upstream-kernel family, the LR four-observer image has rank 4 and is nonconvex, yet FULL/LR full four-observer convex hulls are strictly unequal. If a!=b, an explicit signed time-only support direction has gap |a-b|/2. If a=b, the time convex hulls coincide in all signed directions, but the given exact four-dimensional McCormick-coordinate witness violates s>=0 by t+1/2. **No parameter in this family solves the mother question.**

VERIFY_UPSTREAM.py uses Python stdlib Fraction, 64 FULL and 8 LR deterministic corners, 16 rational parameter pairs, 125 exact LR parameter triples per pair, exact rational 4x4 determinant, time hull, and the diagonal affine witness. The universal classification is established by the displayed algebraic identities plus determinant polynomial degree/interpolation, not by numerical extrapolation. Full input, executed output, and smallest next task are saved in this same immutable GitHub directory.

Native gateway did not grant research authority; bounded owner lookup returned CONTROL_QUOTA and an own session request STATIC_READONLY_SCOPE_DENIED. This is portable author evidence, not native CLAIM/Result, independent Driver review, formal X6 transfer or Foundation admission. P000 and ACTIVE worldview untouched.

**Next mathematical unit:** Leave the now closed two-parameter (a,b) family. Preserve a=b to satisfy the proven time-hull necessary condition, but introduce a second independently source-sensitive terminal split or a third coupled true time/LR key; calculate complete 4D hull certificates before attempting actual-image nonmembership.
