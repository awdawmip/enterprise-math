# PREFIX-1085 — Quadratic joint cancellation and six-axis orbit-averaged global tail certificate

2026-11-25. AUTHOR_CONDITIONAL_ALGEBRAIC_PROOF / FINITE_EXACT_COMPUTATION / NOT_REVIEWED. Independent continuation of PREFIX-1084. Own registration recovered: MCP-f6d93209fc8e4c5bb2c3b44f69a47174, EM-DIRECT-780BBE / TASK_RESEARCH, RA-0ABD84561C86E53067DB0322; original registration r6-20261123-2358-session-start-own-v1 SUCCEEDED. Current inventory r6-20261125-1950-owner-read SUCCEEDED; LEASED empty at 2026-11-25T11:49:32.734397Z, source f869b78cc5143b7f73e7d59880917fe9ee024b5e. No CLAIM or shared task mutation.

Frozen science unchanged: P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json; Stage46 X6 chart O, incoming -e1, reversal -5 (phase cover 5q), other weights 1, next incoming -d, both orientations of Link {O,e1} blocked without renormalization, exactly two negative steps. Full signed/phase-paired Cell/port/ordered multiplicity carrier remains the input. CT and x are auxiliary observations, not spatial/time coordinates. No original path re-enumeration or classical numerical reference.

Parents:
- ba684dc121d63bef952982f17c35aee8e356475b:research_notes/portable_direct/2026-11-25_r6_prefix1084_newton_global_tail_certificate.md
- e5f4fc3df56133a943b1fd5d1b9784771066b1ea:research_notes/portable_direct/2026-11-25_r6_prefix1082_exact_ct_integer_sign_triangle.md
- 7e8adcd9dac8e9ae5662c71aed1e2211458f12f0:research_notes/portable_direct/2026-11-25_r6_prefix1075_uniform_positive_tail.md
- inherited PREFIX-1084 finite signed tail identity and six-axis positive radial moment estimates. The analytic/native bridges remain author-conditional.

## 1. Quadratic tail certificate retaining the joint cancellation

Let m>=0, r>=1, M=m+r, k>=3, U>=7 integers, D_m(k)>0. Write x=SB/36, y=1-x, c_u=binom(u+r-1,r-1), Q=k+u. CT is the positive normalized Haar observation on the unit character carrier (CT of a nonnegative real integrand is nonnegative), and K2=K+sigma K with sigma swapping the first two axes. PREFIX-1084 proves the exact Newton separation. The explicit polynomial K2 has 84 nonzero Laurent monomials, each with S and B degrees at least two and total degree at least six. For d=0..3 put

    P_d = Delta_n^d K2(M+8)/(S^2 B^2),    c=1/(8*36^6),
    F_Q = sum_d (-1)^d binom(Q,d) P_d x^d y^(3-d).

This quotient is an exact Laurent polynomial in the paired carrier, including at S=0 by its polynomial extension; it is real on unit characters because K2 is star-invariant. Thus

    D_M(Q)=c CT[x^(M+2) y^(Q-3) F_Q].

Define the positive finite weighted measure on u>=U and the joint unit characters with kernel c_u x^(M+2)y^(k+u-3). Its total mass B_U and its second moment C_U are

    B_U=sum_(u>=U) c_u CT[x^(M+2)y^(k+u-3)],
    C_U=sum_(u>=U) c_u CT[x^(M+2)y^(k+u-3) F_(k+u)^2].

Triangle then Cauchy-Schwarz in this single joint measure gives the absolute tail envelope

    sum_(u>=U) c_u |D_M(k+u)| / D_m(k) <= A2_U=c sqrt(B_U C_U)/D_m(k).

The square is formed AFTER the four Newton terms, signs and Laurent carrier terms are combined, not from a sum of absolute coefficients. All moments are real rational; compare squared envelopes exactly, no floating-point square root needed. If S_U is the exact signed tail of PREFIX-1084, the unscanned negative mass obeys

    0 <= N_tail(U) <= (A2_U-S_U)/2.

The smaller of this and the old A_U envelope may always be used; there is no general theorem that A2_U<=A_U. Finite measured negative mass supplies the same global lower bound as before. This controls the declared grouped observer only, not permission to erase native joint state.

## 2. Finite exact formulas

For a fixed Laurent polynomial P and h>=1,V>=1 define

    L(P,i,q,h,V) = sum_(j=0)^(h-1) binom(V+j-1,j)
                         CT[P x^(i-h+j)y^(q+V)].

The PREFIX-1084 negative-binomial tail identity gives L = sum_(v>=V) binom(v+h-1,h-1) CT[P x^i y^(q+v)] whenever all indicated exponents are nonnegative and the sum is integrable. Here all applications satisfy i-h>=2, q>=0. In particular B_U=L(1,M+2,k-3,r,U).

For the product binomial coefficients use

    binom(Q,d)binom(Q,e)=sum_(h=max(d,e))^(d+e)
               binom(h,d)binom(d,d+e-h)binom(Q,h).

This counts pairs of subsets of a Q-element set by union size h. Expand binom(k+u,h)=sum_(j=0)^h binom(k,h-j)binom(u,j). The multiplicity identity from PREFIX-1084 and the change v=u-j give

    C_U = sum_(d,e=0)^3 (-1)^(d+e)
      sum_(h=max(d,e))^(d+e) binom(h,d)binom(d,d+e-h)
      sum_(j=0)^h binom(k,h-j)binom(r+j-1,j)
      L(P_d P_e,M+2+d+e,k+j+3-d-e,r+j,U-j).

Here U-j>=1, q=k+j+3-d-e>=0; i-(r+j)=m+2+d+e-j>=2. This proves a finite rational second-moment certificate without scanning infinitely many terminal bins. The finite sums may have strong exact cancellation; square roots only enter final optional display.

For fixed m,k,r, P_d=O(x) on the character carrier (total remaining S,B degree >=2). The parent bounded zero-edge radial density implies CT[x^i y^Q]=O_i(Q^(-i-1)). Consequently B_U=O(U^(-m-3)); each of the finitely many absolute cross-product terms in the original C_U sum is bounded by a constant times u^(r-1+d+e) CT[x^(M+4+d+e)y^(k+u+3-d-e)] = O(u^(-m-6)), and hence C_U=O(U^(-m-5)). This justifies interchange and yields A2_U=O(U^(-m-4)), preserving the old fixed-parameter convergence order. No uniform complexity or explicit positivity threshold follows.

## 3. Full six-axis orbit averaging before squaring

For each unordered pair a={i,j} of axes (15 choices) let F_Q^a be the same exchange-symmetrized carrier after moving the marked pair to a. It is symmetric within the pair (K2 symmetry); all radial CT observations agree by exchangeability. Define Fbar_Q=(1/15)sum_a F_Q^a. Therefore replacing F_Q by Fbar_Q preserves every D_M(Q) exactly for this radial observer family and its transport, including signs and multiplicities. Jensen gives CT[radial weight Fbar_Q^2]<=CT[radial weight F_Q^2] for all Q. The resulting Cbar_U<=C_U and Aorb_U<=A2_U for all allowed parameters.

There are three orbit types of ordered pairs of unordered pairs, relative to fixed pair {0,1}: identical (1), share one axis (8), disjoint (6). Thus in the finite formula replace P_d P_e by the CT-equivalent polynomial

    (P_d^01 P_e^01 + 8 P_d^01 P_e^02 + 6 P_d^01 P_e^23)/15.

This identity applies INSIDE every radial CT, not as pointwise equality to Fbar^2. Proof: sum ordered pair pairs, fix the first using S6 invariance, then use its stabilizer to move the second to one of the three representatives. It needs at most four marked axes in a cross term, not explicit expansion of 225 ordered pair products. All six original joint matching axes are retained by CT. This is not a new native state equivalence or an arbitrary permutation of the original blocked-link input: it is an exact symmetry of the radial integration after the original carrier has already been constructed.

A further general refinement: partition u>=U into finitely many disjoint consecutive blocks, with an infinite final block. Compute B_i,C_i by differences of the same tail formulas, and replace sqrt(B_U C_U) by sum_i sqrt(B_i C_i). Cauchy-Schwarz over blocks proves the refined envelope is never larger, and any further refinement cannot increase it. Each block's negative mass can also use its exact signed tail difference. This is an analytic refinement, not a measured runtime gain.

## 4. Actual exact computation

We ran the inherited 66-term K and 84-term K2 construction and exact six-axis CT occupation recurrence. Quadratic case: 25 shift classes, Nmax=350; first eight A_m equal the fixed PREFIX-1082 integers. For (m,r,k)=(0,1,115),(0,3,150),(0,5,205), U=7,10,20,40,80,120, computed B_U,C_U,A2_U^2 and old A_U exactly as Fractions. Verified B_U,C_U successive differences against direct finite sums for 15 intervals (339 grouped bins), and each direct bin satisfied c^2 B C>=D^2; verified total squared bound >= S_U^2. Exact compact JSON digest of records described below: 9399d5390b057e7421601475950865f044890758b03919193d2d179fa004ec49.

The full orbit calculation completed for (0,1,115), six cutoffs, Nmax=250, 57 shift classes, five intervals (113 bins), identical exact checks. Digest d233fa0f394147d80806139a9d238b03b88a878f1eb755b8357277995f903fde. Larger three-case orbit execution timed out; only the complete one-case run is used as completed evidence. The following values are rounded solely for presentation; actual bounds are the nonnegative square roots of exact rationals.

r | U | old absolute A | quadratic A2 | full orbit Aorb
1 | 7 | 403732.364586 | 721.979562 | 510.536345
1 | 20 | 276082.768832 | 510.369028 | 362.161831
1 | 120 | 33461.684340 | 68.986065 | 49.597304
3 | 7 | 523283.390556 | 602.733242 | not completed
3 | 120 | 249806.771459 | 299.279016 | not completed
5 | 7 | 751461.145144 | 615.491603 | not completed
5 | 120 | 659478.649031 | 541.187055 | not completed

Across 18 quadratic cases the old/new absolute-envelope ratio ranges about 485.05 to 1220.92. Across the six orbit cases the old/orbit ratio ranges about 674.67 to 790.80; orbit additionally reduces quadratic by about 28–29%. Example r=1,U=120 S=0.20462834069258837: old negative bound 16730.7398557; quadratic (68.98606499383892-S)/2=34.3907183266; orbit (49.59730386129385-S)/2=24.6963377603. Still much larger than a useful small error tolerance. The improvement is on envelope magnitude, NOT measured algorithm speed or certified native execution precision. No classical trigonometric/pi calculation, independent review or formal checker executed.

## 5. Reproduction (exact Python, parent polynomial reused)

Use PREFIX-1082 section 4 from import sympy through definition of K (including H,star), plus imports collections.defaultdict, math.comb, fractions.Fraction as F, json,hashlib. Then execute this suffix. Set ORBIT=False for the 18-record completed run or True for the six-record completed run. The two original executions used equivalent specialized CT routines; the common suffix below unifies their shift indexing and arithmetic. Both expected digests bind the ordered exact rational records, not the displayed decimal values.

    ORBIT=False
    K2=sy.expand(K+K.xreplace({z:1/c,c:1/z}))
    def coeffs(poly):
        out=defaultdict(lambda:0)
        for term in poly.as_ordered_terms():
            p=term.as_powers_dict()
            key=tuple(int(p.get(v,0)) for v in (S,B,z,c))
            out[key]+=term/(S**key[0]*B**key[1]*z**key[2]*c**key[3])
        return {k:sy.Poly(sy.expand(v),n) for k,v in out.items() if sy.expand(v)!=0}
    orig=coeffs(K); sym=coeffs(K2)
    assert len(orig)==66 and len(sym)==84 and max(v.degree() for v in sym.values())==3
    assert all(u>=2 and v>=2 and u+v>=6 for u,v,a,b in sym)
    def canonical(d):
        return min(tuple(sorted(d)),tuple(sorted(-x for x in d)))
    def mul(A,B):
        out=defaultdict(int)
        for a,p in A.items():
            for b,q in B.items():
                out[tuple(x+y for x,y in zip(a,b))]+=p*q
        return {k:v for k,v in out.items() if v}
    def val(poly,n0):
        return {k:int(p.eval(n0)) for k,p in poly.items() if p.eval(n0)}
    def pd(M,d):
        out={(u-2,v-2,a,b):sum((-1)**(d-j)*comb(d,j)*int(p.eval(M+8+j))
                                  for j in range(d+1)) for (u,v,a,b),p in sym.items()}
        return {k:v for k,v in out.items() if v}
    def embed(P,i,j):
        out={}
        for (u,v,a,b),p in P.items():
            ds=[0]*6; ds[i]=-a; ds[j]=b
            out[(u,v,*ds)]=p
        return out
    def product(P,Q):
        base=embed(P,0,1); out=defaultdict(int)
        assert base==embed(P,1,0) and embed(Q,0,1)==embed(Q,1,0)
        for a,b,w in ([(0,1,1),(0,2,8),(2,3,6)] if ORBIT else [(0,1,1)]):
            for key,v in mul(base,embed(Q,a,b)).items():out[key]+=w*v
        return {k:v for k,v in out.items() if v}
    def shift(key):
        u,v,*ds=key; assert u-v==sum(ds)
        return canonical(ds)
    params=[(0,1,115)] if ORBIT else [(0,1,115),(0,3,150),(0,5,205)]
    Nmax=250 if ORBIT else 350; Jmax=Nmax+20
    Ps={r:[pd(m+r,d) for d in range(4)] for m,r,k in params}
    products={r:{(d,e):product(p[d],p[e]) for d in range(4) for e in range(d,4)}
              for r,p in Ps.items()}
    keys=set(shift(k) for k in embed(val(orig,8),0,1)) | {
        shift(k) for p in products.values() for pol in p.values() for k in pol}
    # include all original coefficient shift classes even if vanishing at n=8
    keys |= {canonical((-a,b,0,0,0,0)) for u,v,a,b in orig}
    assert len(keys)==(57 if ORBIT else 25)
    BC=[[1] for _ in range(Jmax+12)]
    for i in range(1,len(BC)):
        prev=BC[i-1]
        BC[i]=[1]+[prev[j-1]+prev[j] for j in range(1,i)]+[1]
    Tzero={1:[1]*(Jmax+1)}
    for l in range(2,7):
        Tzero[l]=[sum(BC[j][q]**2*Tzero[l-1][j-q] for q in range(j+1)) for j in range(Jmax+1)]
    def calc(d):
        d=[x for x in d if x]; T=Tzero[6-len(d)]; ap=am=0
        for di in d:
            pp=max(di,0); mm=max(-di,0); ap+=pp; am+=mm
            T=[sum(BC[j+ap][l+pp]*BC[j+am][l+mm]*T[j-l]
                   for l in range(j+1)) for j in range(Jmax+1)]
        return T
    tables={d:calc(d) for d in sorted(keys)}
    def ct(i,pol):
        total=0
        for (u,v,*d),p in pol.items():
            j=i+u-sum(max(x,0) for x in d)
            assert j==i+v-sum(max(-x,0) for x in d)
            if j>=0:total+=p*tables[canonical(d)][j]
        return total
    A=[ct(i,embed(val(orig,i+8),0,1)) for i in range(Nmax+1)]
    assert A[:8]==[3474227232,83430021744,2013683977632,50005705455360,
       1283772437946144,33996158582646432,924583802183434368,25711602118824644352]
    pow36=[36**i for i in range(Nmax+25)]
    def moments(arr,imax):
        out=[]
        while arr:
            out.append(arr[:imax+1])
            arr=[36*x-y for x,y in zip(arr,arr[1:])]
        return out
    def get(rows,i,q):return F(rows[q][i],pow36[i+q])
    Drows=moments(A,12)
    def D(i,q):return get(Drows,i,q)/(4*36**8)
    rad=moments(tables[(0,0,0,0,0,0)][:Nmax+1],16)
    C0=F(1,8*36**6); divisor=15 if ORBIT else 1
    def hc(d,e,h):return comb(h,d)*comb(d,d+e-h)
    def nb(rows,i,q,r,U):
        return sum(comb(U+l-1,l)*get(rows,i-r+l,q+U) for l in range(r))
    records=[]
    for m,r,k in params:
        M=m+r; den=D(m,k); assert den>0
        prodrows={de:moments([ct(i,pol) for i in range(Nmax+1)],16)
                  for de,pol in products[r].items()}
        def bc(U):
            b=nb(rad,M+2,k-3,r,U); cc=F(0)
            for (d,e),rows in prodrows.items():
                l=d+e; fac=(-1)**l*(1 if d==e else 2)
                for h in range(max(d,e),l+1):
                    for j in range(h+1):
                        cc+=fac*hc(d,e,h)*comb(k,h-j)*comb(r+j-1,j)*nb(
                            rows,M+2+l,k+j+3-l,r+j,U-j)
            return b,cc/divisor
        def direct(u):
            q=k+u; b=get(rad,M+2,q-3); cc=F(0)
            for (d,e),rows in prodrows.items():
                l=d+e
                cc+=(-1)**l*(1 if d==e else 2)*comb(q,d)*comb(q,e)*get(rows,M+2+l,q+3-l)
            cc/=divisor
            assert cc>=0 and D(M,q)**2<=C0*C0*b*cc
            return comb(u+r-1,r-1)*b,comb(u+r-1,r-1)*cc
        def old(U):
            L=[F(sum(abs(sum((-1)**(d-j)*comb(d,j)*int(p.eval(M+8+j))
                      for j in range(d+1)))*6**(a+b) for (a,b,v,w),p in sym.items()),
                      8*36**8) for d in range(4)]
            return sum(L[d]*comb(k,d-e)*comb(r+e-1,e)*comb(U-e+j-1,j)*
                       get(rad,m+d-e+3+j,k+U-d) for d in range(4)
                       for e in range(d+1) for j in range(r+e))/den
        prev=None
        for U in [7,10,20,40,80,120]:
            b,cc=bc(U); assert b>0 and cc>=0
            sig=sum(comb(U+j-1,j)*D(m+j,k+U) for j in range(r))/den
            sq=C0*C0*b*cc/den**2; assert sq>=sig**2
            oldA=old(U)
            if prev:
                V,b0,c0=prev; terms=[direct(u) for u in range(V,U)]
                assert b0-b==sum(x for x,y in terms)
                assert c0-cc==sum(y for x,y in terms)
            prev=U,b,cc
            records.append([m,r,k,U,str(sig),str(b),str(cc),str(sq),str(oldA)])
            print(r,U,float(sig),float(sq)**.5,float(oldA))
        del prodrows
    digest=hashlib.sha256(json.dumps(records,separators=(',',':')).encode()).hexdigest()
    assert digest==('d233fa0f394147d80806139a9d238b03b88a878f1eb755b8357277995f903fde'
                   if ORBIT else '9399d5390b057e7421601475950865f044890758b03919193d2d179fa004ec49')

## 6. Next

Use radial conditional averaging or positive zero-edge density to eliminate the large remaining variance: the current orbit average retains more cancellation but its squared carrier still includes fluctuations invisible to radial CT. Explore rigorous projection onto low-order radial polynomials, with exact CT Gram matrix and residual second-moment certificate; do not treat the projection as native state erasure. Test block refinement only when it can meaningfully lower the remaining bound. The actual strict p,d spectral localization and explicit uniform positivity constant remain open, as does B_fix,odd(32). No claim of mathematical admission.
