# R770 — All-rank sharp graphic reserve saving via opposed incidence signs

2026-11-24. AUTHOR_ANALYTIC_PROOF / EXACT_JS_CHECKED / NOT_REVIEWED. Independent portable continuation of R769, 131e23c0a2cd0842ec6499d7d24ac3701446528a:research_notes/portable_direct/R769_RANK4_CORES_SHARP_SAVING_BOUND.md, especially its section 3 vertex cut. R769's frozen scientific pin a72226e2430ffa4786321ac86e7f0c599d5f0389 is retained; P000 V5 blob dc84bdae6595b5e237a2ad50d8b21916adb2e447, joint-relation contract 3923890d77a02d84b772f789e6912dd14f220d14, weighted substrate f375a059fa4af8c6eefaddb4d4a8689a0c063674 were fetched by exact blob, with pin association inherited from R769. The generated foundation startup path was queried at the original pin and returned 404; no repinning. Current ACTIVE worldview, global P000 projection and canonical V4 matching blob, portable/continuation/method policies consulted. This is the existing Boolean auxiliary boundary observer, not an identification with the full signed, weighted, ordered, provenance-sensitive or common-depth native BRC state.

Own recovery r3-20261124-1920-own-recovery-v1 verified the existing session MCP-ec17f2f30fb8409f8e664eb29ae6c08c, registration r3-20261124-0124-own-research-registration-v1 SUCCEEDED, no runs and execution_authorized=false. Activity RA-708BCC309CE076D8BB599B91, Researcher-ID EM-DIRECT-82A007, TASK_RESEARCH. Owner inventory r3-20261124-1920-owner-read-v1 was queued at derivation. No shared CLAIM/PROGRESS or formal Result.

## 1. Statement

Let G be an arbitrary finite loop-free subcubic multigraph; isolated vertices and parallel edges are allowed. At each vertex the three distinct local Ports include private ports if degree <3. Identify the four even triples with V_i=F2^2, so S(0)={0}, S(1)=V_i\{0}, S(2)=V_i. Addition is XOR. The relation kernel K is the graphic cycle space: even incident edge bits consistent at both ends, private ports zero. Write n=|V(G)|, r=dim K=|E|-n+components, p_i=min(raw prefix inventory,2), B=sum p_i. Let q be the quotient of the product of all V_i by K. Feasibility of suffix t at terminal q(w) is precisely
for every x in product S(p_i), there exists z in K with x_i+w_i+z_i in S(t_i) for every i.
Truncate t at 2 without changing feasibility. Write k_p(q(w)) for minimum sum t_i.

**Theorem A (all ranks, all terminals).** Every feasible suffix satisfies sum t_i >= B-r. Thus k_p(q(w)) >= B-r for all p,w.
**Theorem B (all-rank attainment).** For every G there is one fixed suffix t of cost 2n-r whose attainable boundary set equals the whole quotient. For the saturated prefix p_i=2 this gives k_p(q(w))=2n-r at EVERY terminal, and the largest saving B-min_w k_p(q(w)) over all p is exactly r. No cycle-rank cutoff, core enumeration, or conjectural dependency is needed. This settles the general sharp-saving conjecture in R769. It does not settle zero-terminal optimality for nonsaturated prefixes at ranks >=4.

## 2. Inductive local reduction

For each vertex i let d_i be the rank of K's local projection. Removing vertex i, replacing its lost incidences at neighboring vertices by private Ports, gives a graph of the same type whose cycle space is K' = ker(projection_i|K), naturally on the remaining vertices. Indeed cycles vanishing on the local triple have zero on every removed edge, and the converse extends uniquely by zeros. Its cycle rank is r-d_i. If there is a fixed prefix value x_i whose allowed corrections force a single local projected value a, choose any z0 in K with (z0)_i=a. Feasibility for every combination of the other independent prefixes then implies feasibility on the reduced graph at terminal lift w_j+(z0)_j. Every possible correction for that fixed x_i is in z0+K'. If p_i-t_i<=d_i, inducting on r gives sum t >= B-r. The case r=0 follows immediately from |S(0)|=1, |S(1)|=3, |S(2)|=4.

At rank zero no saving is possible (translation must contain a set of cardinality |S(p_i)|). At rank one a suffix t_i=0 with p_i>=1 is impossible: only two possible local corrections, while prefix size is at least three. The only positive saving at rank one is therefore (p_i,t_i)=(2,1); choose x_i=w_i to exclude the local zero correction, forcing the other of the two. Saving one equals d_i. At rank two, any t_i=0 fixes the local projection for any chosen x_i, and saving p_i<=2=d_i. These reductions decrease r strictly. If none applies, all positively saving vertices have rank two and (p_i,t_i)=(2,1); their saving is one each. Other vertices have nonpositive saving. It now suffices to bound the number of these vertices by r.

## 3. Opposed incidence signs: the all-rank obstruction

Remove bridges; their cycle bits are always zero. In each connected cyclic component, a degree-two vertex has rank-one local projection and a degree-three vertex has rank-two projection: at degree three, rank one would force a third edge never to occur in a cycle, contrary to being nonbridge. Components with no degree-three vertex have rank one and no marked vertices. Suppressing degree-two paths in a component with rank r_c>=2 preserves the cycle space and all rank-two local projections. The resulting connected bridgeless cubic multigraph H has N=2(r_c-1) vertices, M=3N/2 edges. It is loop-free: a loop at a cubic vertex would leave a single connecting edge, a bridge. This description also includes two vertices with three parallel edges. The component ranks sum to r.

Mark vertices having (p_i,t_i)=(2,1). Suppose a component has more than r_c marks. Select exactly r_c+1 marks as A (if not enough vertices, the hypothesis is impossible). For each edge uv of H assign incidence signs s_{u,e},s_{v,e} in {+1,-1}, with s_{u,e}=-s_{v,e}. Require the product of the three incidence signs at a vertex to equal -1 precisely on A and +1 elsewhere. Such signs exist: the sole compatibility condition in a connected graph is product of desired vertex products = (-1)^M. It holds since r_c+1=M-N+2 and N is even. To construct, start with arbitrary opposite signs on edges, then flip both signs along tree edges leaf-to-root to repair each nonroot vertex product; root matches by parity.

For a graphic cycle z, write its edge bits z_e. At each vertex v form
L_v(z)=sum_{e incident to v} s_{v,e} (-1)^(z_e).
Because the two endpoint signs oppose, sum_v L_v(z)=0 exactly. Cycle bits have even local parity. At marked vertices v in A the product of the three summands is -1; hence L_v(z) is either -3 or +1. Exactly one even local triple realizes -3, namely the one that makes all three summands negative. Since p_v=2, choose the independent prefix value x_v so that this triple is the unique forbidden correction (x_v+w_v+z_v=0) for t_v=1. This is possible for every terminal lift w. At unselected vertices product +1 implies L_v(z) in {-1,3} without imposing any extra prefix constraints.

Any correction satisfying all selected vertices would have
0=sum_v L_v(z) >= |A|-(N-|A|)=2(r_c+1)-2(r_c-1)=4,
a contradiction. Thus for this explicit adversarial prefix the selected constraints alone exclude all cycles. This certificate depends only on the graphic incidence relation, not on r, the terminal lift, or other prefix constraints. It is an integer certificate; there is no numerical tolerance or counting heuristic. If total marks exceed r, one component has more than its r_c and yields the same contradiction. Therefore marks <=r, completing Theorem A by induction. This proof replaces the finite-core bound comparisons for the sharp-saving inequality, including beyond rank 4; it does not replace their separate terminal-cost comparisons.

## 4. Constructive upper bound by ordered rank release

This part holds for any linear relation kernel K inside product V_i with dim V_i=2. Choose any vertex order v_1,...,v_n and set K_i={z in K: z_{v_j}=0 for j<i}; K_1=K and K_{n+1}=0. Define d_i=rank of local projection of K_i at v_i. Then d_i in {0,1,2} and sum d_i=r by telescoping dimensions. Fix t_{v_i}=2-d_i in advance.

For arbitrary x and w, start with correction z=0. At step i adjust z by a vector from K_i, so all previously fixed local values remain unchanged. The possible new local values at v_i are an affine subspace of dimension d_i. If d_i=2 it contains zero, so S(0) suffices. If d_i=1 it has two distinct points and at least one is nonzero, so S(1) suffices. If d_i=0, S(2) contains the single value. Choose one satisfying value and a preimage increment from K_i. By induction the final correction satisfies all vertices. This is valid for every x,w and uses a fixed t of cost sum(2-d_i)=2n-r. It can be constructed by successive kernel restrictions (ordinary exact binary elimination), and the correction can be reconstructed by the chosen local preimages. For a graphic kernel the lower bound from Theorem A with saturated p proves optimality. For any p the same t is a universal reserve, even though a smaller target-specific t may exist. In particular the least cost of reaching every quotient boundary from no prefix is also 2n-r, because that property is identical to being able to correct the entire saturated prefix to zero.

## 5. Exact verification of the new incidence certificate

The following executed JavaScript independently enumerates cycle states and every selected subset of cardinality r+1 in 21 labeled bridgeless cubic graph instances. They are Hamiltonian cycle plus rotated perfect matching, n=4,6,8,10,12,14, with shifts 1,...,n/2-1; some are isomorphic and no isomorphism-completeness claim is made. The cycle basis uses the path edges as a spanning tree. For each selected subset construct signs using leaf-to-root flips on that tree and check every cycle state has a marked vertex with L_v=-3. All arithmetic is exact integer bit operations, maximum 21 edges. Actual observed result: graphCount=21; subsetCertificates=15064; cycleChecks=3425480; failures=0. This verifies examples of the load-bearing incidence certificate, not the full arbitrary-inventory theorem, whose proof is in sections 2–4.

```javascript
const cases=[4,6,8,10,12,14];let checks=0,states=0,graphCount=0;
for(const n of cases){
 const m=n*3/2,r=n/2+1;
 for(let shift=1;shift<n/2;shift++){
  const E=Array.from({length:n},(_,i)=>[i,(i+1)%n]);
  for(let i=0;i<n/2;i++)E.push([i,n/2+(i+shift)%(n/2)]);
  let cyc=[];
  for(let z=0;z<(1<<r);z++){
   let mask=0;
   for(let k=0;k<r;k++)if(z>>k&1){
    let [a,b]=E[n-1+k];if(a>b)[a,b]=[b,a];
    mask^=1<<(n-1+k);for(let j=a;j<b;j++)mask^=1<<j;
   }
   cyc.push(mask);
  }
  for(let S=0;S<(1<<n);S++){
   let s=0;for(let i=0;i<n;i++)s+=S>>i&1;
   if(s!==r+1)continue;
   let signs=Array(n).fill(0);
   for(const [a,b] of E)signs[b]^=1;
   let flips=0;
   for(let i=n-1;i>0;i--)if(signs[i]!==((S>>i)&1)){
    signs[i]^=1;signs[i-1]^=1;flips^=1<<(i-1);
   }
   if(signs[0]!== (S&1))throw Error("parity");
   for(const z of cyc){
    let sums=Array(n).fill(0);
    for(let j=0;j<m;j++){
     let [a,b]=E[j];let q=((z^flips)>>j&1)?-1:1;
     sums[a]+=q;sums[b]-=q;
    }
    if(!sums.some((v,i)=>(S>>i&1)&&v===-3))throw Error("cover");
    states++;
   }
   checks++;
  }
  graphCount++;
 }
}
console.log({graphCount,subsetCertificates:checks,cycleChecks:states,failures:0});
```

## 6. Next problem

The general graphic maximum saving is now exactly r, with an explicit correction and obstruction. The more delicate nonsaturated comparison k_p(0)<=k_p(w) remains unresolved for arbitrary rank. Investigate the extent to which an optimal nonzero-terminal suffix can be converted to a zero-terminal suffix by local kernel restriction while retaining inventory-dependent savings. In particular the rank-two p=1,t=0 reduction costs one unit of slack relative to its rank-two drop, and the opposed-sign certificate alone does not compare the two terminals when their savings are both below r. Seek an inventory-sensitive lower bound and matching construction; do not redo the core-by-core sharp-saving bound. R764's abstract non-graphic counterexample retains its original scope. All future transfer to native signed BRC or full three-dimensional slice states must preserve order, weights, provenance and common depth separately.
