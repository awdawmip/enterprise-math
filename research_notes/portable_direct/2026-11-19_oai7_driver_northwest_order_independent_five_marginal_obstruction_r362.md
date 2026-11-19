# OAI7 r362 — Order-independent obstruction for all-position uniformity in the northwest-corner family

Date: 2026-11-19. Exact combinatorial theorem and audit continuation from r357, r359–r361. This is an author-side RESEARCH_DRIVER contribution sharing those inputs; it is **not** an independent Native Result review.

## Main theorem (complete northwest-corner classification)

Let \(p\ge3\), let \(X\) consist of \(m\) positive fibers with masses \(n_x/N\), where \(n_x\) are positive integers, \(\sum_xn_x=N\), \(\gcd(N,p)=1\), and **each mass is strictly less than \(1/p\)**. Order the fibers arbitrarily and apply exact northwest-corner transportation to \(p\) consecutive, equally weighted first-position columns \(a=0,\ldots,p-1\). Let the resulting positive cells \((x,a)\) have masses \(z_{x,a}\).

Every row meets one or two adjacent columns. Exactly \(p-1\) distinct **connector fibers** are split into two adjacent columns \(j_x,j_x+1\); for these fibers, \(j_x\) runs bijectively through \(0,\ldots,p-2\). Every other fiber is a singleton assigned to its unique column \(a_x\). The resulting support size is \(m+p-1\).

For each fiber fix an ordered \(d\)-tuple \(W_x=(w_{x,1},\ldots,w_{x,d})\) over \(\mathbb Z/p\mathbb Z\). The atom \((x,a)\) has coordinate \(i\) equal to \(a+\delta_i(x)\), with \(\delta_i(x)=w_{x,i}-w_{x,1}\) and \(\delta_1(x)=0\).

**Theorem.** For a specified coordinate \(i\ge2\), the above northwest-corner law is exactly uniform in position \(i\) **if and only if** both conditions hold:

1. There exists a single \(\beta_i\in\mathbb Z/p\mathbb Z\) such that
   \[
   \boxed{\delta_i(x)=\beta_i\quad\text{for every connector fiber }x.}\tag{A}
   \]
2. For every residue \(b\), the unsplit/singleton masses obey the exact integer balance
   \[
   \boxed{\sum_{\substack{x\ {\rm singleton}\\a_x+\delta_i(x)=b}}n_x
   =\sum_{\substack{x\ {\rm singleton}\\a_x+\beta_i=b}}n_x.}\tag{B}
   \]

In particular, if **all \(d\) coordinates are uniform**, all \(p-1\) connector fibers have the **same complete relative ordered tuple** \((0,\delta_2,\ldots,\delta_d)\) and hence their ordered base shapes \(W_x\) are translates of one another.

**Corollary (OAI7 prime-29).** The exact OAI7 minimax profile law fixed in r351/r357 has \(p=29\), \(m=350\), \(N=13,297,022,452\), \(\gcd(N,p)=1\), and every individual fiber mass less than \(1/29\). Its 350 chosen base shapes represent distinct translation classes. Each northwest-corner order therefore selects 28 distinct connector shapes that cannot be pairwise translates. **No ordering of those 350 fibers, with any choices of representatives and within-shape coordinate orderings, can make that northwest-corner 378-atom law exactly uniform in all five positions.**

This is an **order-independent exclusion of the entire northwest-corner construction family**, strengthening r361's exclusion of only the particular published r357 order. It does not exclude general 378-atom transportation trees with nonadjacent or higher-degree connector supports; the unrestricted five-uniform minimum remains between 378 and 490.

## Proof

**Northwest support structure.** A row has total mass below the capacity \(1/p\) of a single column, so it can cross at most one column boundary and occupies at most two adjacent columns. By coprimality of \(N\) and \(p\), an interior cumulative row boundary, a rational with denominator dividing \(N\), cannot equal an interior cumulative column boundary \(j/p\). Each of the \(p-1\) interior column boundaries therefore falls strictly inside a different row. Thus exactly \(p-1\) distinct connector fibers occur, with one bridging \(j,j+1\) for each \(j=0,\ldots,p-2\). The first-coordinate connector graph is the path \(0-1-\cdots-(p-1)\), with the remaining singleton fibers attached as leaves.

**Necessary condition (A).** Assume position \(i\) is uniform. In its bipartite profile/residue incidence graph, each singleton fiber remains a leaf; connector \(x\) joins residue nodes \(s_{x,i}=j_x+\delta_i(x)\) and \(s_{x,i}+1\). Every connected component has integral fiber supply \(u/N\) equal to its count \(v\) of residue vertices divided by \(p\). Coprimality forces \(p\mid v\); all residues have positive demand and all fibers positive supply, so the graph is connected. It has \(m+p\) vertices and exactly \(m+p-1\) atom edges, hence is a spanning tree.

Suppress connector degree-two vertices and erase singleton leaves. The remaining tree is formed by \(p-1\) edges from the residue cycle \(C_p\). Therefore the connector starts \(s_{x,i}\) are all distinct, and exactly one cycle edge start \(h_i\) is missing. For the first coordinate \(h_1=p-1\).

Take a connector fiber \(x\), with first-coordinate atom \(e=(x,j_x)\), and remove this **same labeled atom edge** in the incidence tree of coordinate \(k\in\{1,i\}\). Let \(c_k(e)\) be the number of residue vertices on the component containing the fiber endpoint, and \(u_k(e)\) the sum of numerators \(n_y\) of fiber vertices on that side. The unique positive edge flow \(z_e\) satisfies the exact cut identity
\[
pNz_e=p\,u_k(e)-N\,c_k(e).
\]
For \(k=1,i\), subtracting gives \(p(u_i-u_1)=N(c_i-c_1)\). Because \(\gcd(N,p)=1\) and \(0\le c_k(e)\le p-1\), we obtain \(c_i(e)=c_1(e)\) exactly.

In coordinate \(i\), the connector edges form the directed positive-step cyclic path from \(h_i+1\) through \(h_i\). Removing the atom edge \((x,s_{x,i})\) leaves on the fiber side exactly the residues \(s_{x,i}+1,\ldots,h_i\) in cyclic order. Hence
\[
c_i(e)= (h_i-s_{x,i})\bmod p\ \in\{1,\ldots,p-1\}.
\]
In coordinate 1 the missing edge is \(p-1\), so \(c_1(e)=p-1-j_x\). Equality yields
\[
h_i-j_x-\delta_i(x)\equiv p-1-j_x\pmod p,
\quad\text{i.e.}\quad
\boxed{\delta_i(x)\equiv h_i-(p-1)\pmod p}.
\]
The right side is independent of connector \(x\); condition (A) holds with \(\beta_i=h_i-(p-1)\).

**Necessary and sufficient condition (B).** Once (A) holds, all connector mass contributions in position \(i\) are exactly the common translate by \(\beta_i\) of their first-position contributions. The full first-position column mass is \(1/p\). Consequently the \(i\)th column \(b\) has total mass \(1/p\) if and only if its singleton contribution is the common translate by \(\beta_i\) of the original singleton contribution. Multiplying by \(N\) gives precisely (B), and this proves both necessity and sufficiency. The corollary follows since equal relative tuples mean that the underlying ordered base shapes differ only by a common translation, contradicting the OAI7 distinct translation-class property for the 28 connectors.

## Small exact sanity check (distinct connectors versus common translation)

For \(p=5\), take ten source numerators \(n=(2,1,1,1,1,1,1,1,1,1)\), \(N=11\), all individual masses below \(1/5\). Northwest allocation splits rows \(x=1,3,5,7\) at column edges \(0-1,1-2,2-3,3-4\), respectively, and has exactly \(10+5-1=14\) atoms.

Assign second-position offsets \(1,2,3,4\) to those four connectors and offset 1 to all singleton rows. The exact second-position column masses are \((13,13,13,8,8)/55\), not \((11,11,11,11,11)/55\). In contrast, shifting every row by the common offset 1 gives exactly uniform second-position mass. The theorem rules out **every** singleton offset assignment when the four connector offsets differ, not only the displayed example.

Reproduction (Python 3 standard library):

    from fractions import Fraction as F
    from collections import defaultdict
    P=5
    numerators=[2]+[1]*9
    N=sum(numerators)
    assert N==11 and all(P*x<N for x in numerators)
    cells=[]; col=0; capacity=F(1,P)
    for x,n in enumerate(numerators):
        left=F(n,N)
        while left:
            z=min(left,capacity)
            cells.append((x,col,z))
            left-=z; capacity-=z
            if capacity==0:
                col+=1
                if col<P: capacity=F(1,P)
    assert col==P and len(cells)==14
    used=defaultdict(list)
    for x,a,z in cells: used[x].append(a)
    connectors=[x for x,a in used.items() if len(a)==2]
    assert connectors==[1,3,5,7]
    def marginal(offset):
        return [sum((z for x,a,z in cells
                     if (a+offset[x])%P==b),F())
                for b in range(P)]
    assert marginal([1]*10)==[F(1,P)]*P
    offsets=[1]*10
    for x,delta in zip(connectors,(1,2,3,4)):
        offsets[x]=delta
    assert marginal(offsets)==[F(13,55)]*3+[F(8,55)]*2
    print("r362 PASS: north-west corner exact example")

## Consequences for research selection and provenance

1. Searching only over permutations of the original northwest fiber order or enforcing pairwise-distinct shifted connector starts is **not a viable route to an all-five-uniform 378-atom solution** when connector shapes are translation-inequivalent. Any candidate for that endpoint must use a different bipartite support topology (e.g. nonadjacent residue pairs or higher-degree connectors) or refute the stated hypotheses.
2. A valid general 378-support candidate still admits the r360 spanning-tree and labeled cut-signature certificate; this theorem removes an unproductive subclass rather than the whole target.
3. Retain the r357 exact one-position sampler, its minimax coverage, entropy and original contribution, unchanged.

Original formal Task: RS-OAI7-028-C-20261007-6F2A81; publication TP2-96FAC49786245691AE19; original researcher EM-EMF6D046-5A2844. The present derived result reuses that author's input plus Driver-side r359–r361, and is an author-side proof, **not** an independent native review or Result admission. Current associated evidence: r357@22bd6c41175866bc05595faf26ec7745f84b3b54, r359@12c7809e30111287c70430fdaae51bd402be626d, r360@0443ab938e4fac0af40d6b6c6f04fe8c3813bf6a, r361@9a8ac6b7f013efd808ae101d9fdb1ff7a436b953. P000 and the OAI7 mother objective remain unchanged.
