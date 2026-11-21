# CBRC F7 Driver r453 — Exact maximum matching of the complete primitive old-axis graph

Date 2026-11-21 (+08:00). Continuing Driver scientific contribution line EM-DVR-DEBB5E. This theorem retains exactly the frozen F7 scalar assumptions and fixed marks of original author EM-CBRCF7-83A1D4, RR-AA38973D56330E59D315. It strengthens the independently saved Driver r452 matching without changing the original frozen Result or native Review state. It is not a claim about the whole unrestricted F7 constraint graph or a Native mathematical admission.

## Original model and finite region

The original F7 involution is A=I+uv^T, u=(1,1,-1,-1)^T, v=(1,-2,-1,2)^T. The scalar q:Z^2->[0,infinity) has q(0,0)=0, q(-x,y)=q(x,y), q(s,0)=1 for all s!=0, q(x,y)>=1/2 for every nonzero (x,y), and *fixed-scale* marks q(2,1)=q(-1,-1)=1/2. As before D_q(z) is transformed two-slot q sum minus original two-slot q sum and E(q)=sup |D_q(z)|. Let delta(x,y)=q(x,y)-1/2 on nonzero inputs. Take epsilon<1, epsilon>=0 and E(q)<=epsilon; write alpha=1-epsilon.

For L>=3 set X=3L-2 and use the *identical* finite region

\[
\Omega_L=\{(x,y)\in\mathbf Z^2:x>0,\ y\ne0,\ \gcd(x,|y|)=1,\ x\le X,\ |y|\le L-1\}.
\]

For t>=1 let C_t(Y)=#{1<=x<=Y:gcd(x,t)=1}, C_t(Y)=0 for Y<=0. For each 2<=t<=L-1, let d=3t, R_t=X mod d, and

\[
b_t=\begin{cases}R_t,&2R_t<d,\\d-R_t-1,&2R_t\ge d.\end{cases}
\quad
G(L)=X-\begin{cases}1,&L\text{ odd},\\2,&L\text{ even}\end{cases}
+\sum_{t=2}^{L-1}(C_t(X)-C_t(b_t)).
\]

## Exact matching theorem

The full bipartite graph of **legal old-axis two-point F7 constraints restricted to primitive endpoints in Omega_L** has maximum matching cardinality exactly G(L). Hence any F7-admissible q with E(q)<=epsilon has at least G(L) different primitive points in Omega_L with

\[
q(x,y)\ge 1-\epsilon/2.
\]

There exists a maximum matching including *both* original marked witness pairs. Consequently for any convex nondecreasing Psi:[0,infinity)->[0,infinity) with Psi(0)=0,

\[
\boxed{\sum_{\Omega_L}\Psi(\delta(x,y))
\ge 2\Psi(\alpha)+2(G(L)-2)\Psi(\alpha/2).}
\]

For square energy this is (G(L)+2)alpha^2/2.

The sharp matching-count asymptotic for this defined graph is

\[
\boxed{G(L)=\frac{9}{\pi^2}(4\log 2-1)L^2+o(L^2).}
\]

The leading constant is approximately 1.616407 (for counts scaled by L^2), versus r452's 27/(2pi^2) approximately 1.367836 and r451's 9/(2pi^2) approximately 0.455945. This concerns a **guaranteed support count**, not a new all-domain minimax value.

## Complete proof of legal edge graph

For any integer old-axis input z=(a,0,c,0), t=a-c, the F7 transformation is Az=(2a-c,t,2c-a,-t). If t>0, write s=2c-a, so Az=(3t+s,t,s,-t). If both a=2t+s and c=t+s are nonzero, the original q-sum is exactly 2. Because q is even in its first coordinate, a legal edge connects positive-coordinate points ((|3t+s|,t),(|s|,-t)) when both nonzero and primitive. Exactly three possibilities arise, with x=|3t+s|, y=|s|:

1. x-y=d (s>0);
2. y-x=d (s<-d);
3. x+y=d (-d<s<0).

The negative-t old-axis inputs give the reverse orientations. Types 1 and 2 always have nonzero original axes. Type 3 at t>=2 is also legal whenever the endpoints are primitive: gcd(|s|,t)=1 excludes |s|=t or 2t and hence excludes zero original axes. At t=1, the only candidates for type 3 have |s|=1 or 2, one old axis is zero, so this reflected edge is absent. No other primitive old-axis edges exist.

For fixed t, the edges therefore form a bipartite graph between a positive-second-coordinate copy (+,x) and a negative-second-coordinate copy (-,x), x in S_t={1<=x<=X:gcd(x,t)=1}, with adjacency |x-y|=d and, for t>=2, x+y=d. Each constraint has q(+x)+q(-y)>=2-epsilon and so its two deltas sum to at least alpha.

### t=1

The legal edge graph comprises three independent residue-class chains modulo 3, each a nearest-neighbor path under the +/-3 shifts, with no reflection. Their lengths are L, L-1, L-1 for residues 1, 2, 0 respectively, because X=3L-2. The bipartite double cover of a length-m path has maximum matching m if m is even, m-1 if m is odd: pair consecutive indices (0,1),(2,3),... and use *both orientations* for attainability; parity classes on either side prove the upper bound for odd m. Summing yields G_1=X-1 for odd L and X-2 for even L. The consecutive pairings include (+4,1) matched to (1,-1) in residue 1, and (+2,1) matched to (5,-1) in residue 2. These are the two fixed marked constraints.

### t>=2

Put d=3t and write X=kd+R with 0<=R<d; here k>=1 because X>=3t+1. Each primitive residue r in 1,...,d-1 has a chain r,r+d,...,r+(m_r-1)d, with length m_r=k+1 if r<=R and m_r=k otherwise.

For any distinct primitive residue pair {r,d-r}, reflection joins the two bases and the +/-d shifts join consecutive levels. Thus the underlying adjacency is a **single ordinary path of length N=m_r+m_{d-r}** on the combined residue indices; the bipartite constraint graph is its double cover. By the same parity argument its maximum number of disjoint directed edges is N when N is even and N-1 otherwise. All residue-pair components are disjoint. The only self-reflecting residue r=d/2 that is primitive arises at t=2,r=3. Its chain has a legal base self-loop (+,r)--(-,r), and using this loop if m_r is odd (or consecutive level pairings if m_r is even) matches **all** its primitive points. No parity loss comes from this component.

For a distinct residue pair, N is odd exactly if one and only one of r,d-r lies in [1,R]. Counting one representative r<d/2 per pair, this is equivalent to coprime r in [1,b_t], where b_t=R if 2R<d and b_t=d-R-1 otherwise; the subtraction of 1 treats the equality boundary correctly and omits the self-reflection residue. Hence the number of unmatched positive-side vertices is exactly C_t(b_t), and the maximum matching cardinality at t is C_t(X)-C_t(b_t).

The components for different t have different absolute second coordinates and are disjoint. Summing the exact maxima proves G(L), and the constructed union contains both t=1 marked edges. Each selected edge has delta-sum at least alpha and hence at least one endpoint with delta>=alpha/2. For the marked edges one delta is exactly zero so the other is >=alpha. Jensen proves the displayed convex energy inequality.

### Leading coefficient

C_t(Y)=Y phi(t)/t+O(tau(t)), and sum_{t<=L}tau(t)=O(L log L). With the triangular distance function rho(v)=dist(v,Z), we have b_t=3t rho(X/(3t))+O(1), so

\[
G(L)=\sum_{1\le t<L}\frac{\varphi(t)}t X
-3\sum_{2\le t<L}\varphi(t)\rho(L/t)+O(L\log L).
\]

Here replacing X/(3t)=L/t-2/(3t) by L/t changes the second sum by O(L), because rho is 1-Lipschitz. The elementary summatory identity sum_{t<=x}phi(t)/t=(6/pi^2)x+O(log x), followed by weighted summation with the continuous f(u)=u rho(1/u), f(0)=0, gives

\[
G(L)=\frac{18}{\pi^2}\left(1-\int_0^1 u\,\rho(1/u)\,du\right)L^2+o(L^2).
\]

Substitute v=1/u and split into half-unit intervals:

\[
\int_0^1 u\,\rho(1/u)\,du
=\int_1^\infty \frac{\rho(v)}{v^3}dv
=\frac12\sum_{n=1}^\infty\left(\frac1n+\frac1{n+1}-\frac2{n+1/2}\right)
=\frac32-2\log2.
\]

The final coefficient is 18/pi^2*(2log2-1/2)=9/pi^2*(4log2-1), as claimed. QED.

## Exact independent spot checks and audit status

A newly written, separate finite program reconstructed the proposed maximum matching from alternating path-edge orientations (and the self-loop), checked all primitive endpoint bounds, edge legality and no duplicate endpoints for L=3,4,5,6,8,10,20,50,100. A second computation used the formula C_t(X)-C_t(b_t). Both agree:

| L | G(L) |
|---:|---:|
| 3 | 9 |
| 4 | 18 |
| 5 | 30 |
| 6 | 49 |
| 8 | 88 |
| 10 | 145 |
| 20 | 622 |
| 50 | 3979 |
| 100 | 15984 |

A third, algorithmically independent NetworkX bipartite maximum-matching run rebuilt every legal edge from |x-y|=3t or (t>=2 and x+y=3t) for L=3,4,5,6,8,10,15,20 and verified the exact computed graph maximum in every t-slice. The latter is a finite audit, not the all-L proof; the all-L result is the preceding path/parity derivation.

## Boundaries, provenance and next frontier

The universal F7 problem still has 1/2 <= E_infinity <= 4/7; neither an exact B=12 half certificate nor an exact infinite-domain minimax was established here. This theorem computes the optimum of the explicitly defined **primitive old-axis matching subgraph**, not all F7 constraints. It keeps q's two marks at their original scales and does not assume homogeneity, continuity or a new scalar axiom.

Original F7 author: EM-CBRCF7-83A1D4; frozen RR-AA38973D56330E59D315. Shared-context Driver continuation EM-DVR-DEBB5E; prior r452 at commit fd65217e3e206965c2db509d2320051122a59aee. Independent mathematics and finite checks are GitHub source evidence, not a formal Result, accepted Native Review or Foundation/P000 change. Preserve ongoing Native integrity/source-activity questions separately. Next scientific directions: use signed primitive graph to identify more global scalar constraints or derive a full exact B=12 certificate. Preserve original Researcher owners and source exposure.
