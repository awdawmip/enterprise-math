# R802 — Exact degree-two transfer and certified long-road cut

2026-11-26. AUTHOR_ANALYTIC_PROOF / EXACT_JS_CHECKED / NOT_REVIEWED. Independent portable continuation of R801 (202e892e89ada1986fb673cb3ff25d68a5a65727:research_notes/portable_direct/R801_POSITIVE_CLUSTER_RESIDUAL_AND_LEAF_CONDENSATION.md). Prior line identity EM-DIRECT-82A007, RA-708BCC309CE076D8BB599B91: Source session and activity record read, private possession not confirmed in this transport; no shared execution or claim. Owner inventory original request r3-20261126-0320-owner-read pending at research start; no inferred absence. Frozen science a72226e2430ffa4786321ac86e7f0c599d5f0389: P000 V5 dc84bdae6595b5e237a2ad50d8b21916adb2e447 and joint observer read; generated startup package 404. ACTIVE worldview and global canonical entries at ed4cd9dfd527fc66ccd3cf90037f73cc72432a2d read; current portable and method rules consulted. Auxiliary unsigned aligned Boolean observer only. No native signed BRC, time, path-provenance or X6 dynamics inference.

## 1. Positive tensor and exact degree-two road condensation

Reuse R801 Q_B(a)=H/D=sum_{A subset F} 2^{k(A)} prod_{v isolated in A} a_v, with 7/8<=a_v<=1. This includes its leaf-condensed rational activities. Here B is the aligned simple bipartite overlap graph of R799-R801, but the auxiliary Q identity below makes sense for any finite loopless undirected graph. For each edge give it one of three labels 0,+,-. At vertex v put local factor f_v=0 if both signs occur, 1 if one sign occurs, and 2a_v if all labels are zero (including degree zero). Then Q=sum over all edge labels prod f_v. Proof: for fixed nonzero edge set A, consistency forces one sign per nontrivial connected component, and isolated vertices contribute 2a_v. This is precisely R801's positive sum, retaining the joint sign constraints.

At a degree-two vertex with activity a, the exact transfer in state order (0,+,-) is
M(a)=[[2a,1,1],[1,1,0],[1,0,1]].
For a maximal road with ell internal degree-two vertices (possibly ell=0), its endpoint label tensor is P=M(a_1)...M(a_ell), with P=identity when ell=0. This follows by summing each shared intermediate edge label once. It holds with arbitrary nonnegative functions of the endpoint labels and for any network formed by contracting those endpoint labels. Roads returning to the same branching vertex retain both distinct incidences. A component consisting solely of a cycle of degree-two vertices is evaluated by tr(P). Its symmetric two-coordinate sector in basis (x,y,y) is N(a)=[[2a,2],[1,1]], and its antisymmetric sector (0,1,-1) has eigenvalue 1, so tr(P)=1+tr(N(a_1)...N(a_ell)). Isolated and leaf nodes may be handled by R801 before road extraction. Keep original graph and ordered road data for provenance: this exact condensation covers the nonnegative endpoint contractions, not arbitrary interior observations.

## 2. Uniform certified rank-one approximation of long roads

For ell>=2 write r=floor(ell/2). Define the positive rank-one tensor R_ij=P_i0 P_0j/P_00 and b_ell=2*3^{-(r-1)}. Then, componentwise,
 R_ij/(1+b_ell) <= P_ij <= (1+b_ell) R_ij.
Proof: a two-step block B=M(a)M(b) has rows [4ab+2,2a+1,2a+1], [2b+1,2,1], [2b+1,1,2]. Every pair of rows has max/min ratio of corresponding entries at most 4. For rows +/- the ratios are 1,2,1/2; for row 0 vs row +, the col- and col+ ratios differ by 2 and the col0 ratio lies between them (4ab-2a-2b+3>=0 and 2a+2b>=1). The row - case is symmetric. For any positive vector z, the row-normalized distributions p_k=B_ik z_k/(Bz)_i have likelihood ratio spread at most 4 between any two rows. If likelihood ratio lies in [l,h] with mean 1, total variation <=(h-1)(1-l)/(h-l). With h/l<=4 this is <=1/3: increase h to 4l, then use 4l+1/l>=4. Hence for any other positive vector y, the oscillation across rows of (By)_i/(Bz)_i is at most 1/3 of that of y_i/z_i. Its extrema stay inside the previous interval by weighted averaging. In the rightmost block the ratios of column j to column 0 lie in [1/3,1] (j=0 gives 1); directly from entries and a,b in [7/8,1]. Each further two-step block contracts oscillation by 1/3. A remaining single left factor M is nonnegative with nonzero rows and cannot increase oscillation. Thus all final column ratios are >=1/3 and differ by <=(2/3)3^{-(r-1)}. Dividing any two gives a ratio in [1/(1+b_ell),1+b_ell]. Taking the reference row 0 proves the bound. All constants are rational, uniform in the inhomogeneous activities, and valid without sign assumptions beyond the declared aligned positive observer.

The road is NOT discarded: retain exact P and R and their error certificate. The positive tensor R factors into independent endpoint unaries; it can temporarily split the computation. For a set C of long roads replaced by R, every retained outer assignment has a pointwise multiplicative bound and hence
 Q_approx / K <= Q <= K Q_approx, K=prod_{e in C}(1+b_ell(e)).
All scalar factors D and any R801 leaf factors carry through. A computable choice is r>=1+ceil(log_3(4 max(1,|C|)/epsilon)), for 0<epsilon<=1, making sum b<=epsilon/2, K<=exp(epsilon/2)<=1+epsilon. The actual rational certificate K can be used instead of logarithms. This controls both sides of the total and arbitrary nonnegative endpoint observations; it does not license signed cancellation or interior path recovery from R alone.

## 3. Consequence: structured deterministic approximation after long-road separation

Extract the degree-two roads of the 2-core, evaluating pure cycles exactly. For each chosen cut road absorb its rank-one endpoint factors into the two adjacent vertex tensors. The remaining short-road graph splits into independent components. At a vertex, sum over the cut-road label variables with nonnegative unary weights g_j. If fixed short labels contain both signs, contribution is zero. If they contain a single sign s, contribution is prod_j(g_j(0)+g_j(s)). If all fixed short labels are zero, contribution is
 [prod(g0+g+) - prod g0] + [prod(g0+g-) - prod g0] + 2a_v prod g0.
This sums exactly the disjoint nonzero-positive, nonzero-negative and all-zero cases. It takes linear arithmetic operations in the cut incidences. Now enumerate only the endpoint labels of remaining short roads inside each component. For h equal to the maximum number of short-road incidences in any component, the simple contraction costs O(poly(N)*3^h) arithmetic operations, including exact matrix products, road extraction, scalar factors, and local unary aggregation. Exact mode uses the same solver without cutting. Rationals have polynomial bit length in explicit input and the retained products (common denominators of each local rational factor multiply; all summands share these denominators, and number of summed terms has logarithm O(N)). When h=O(log N+log(1/epsilon)) for the certified threshold, the entire deterministic approximation runs in polynomial time in N and 1/epsilon. This is a structural criterion on the actual instance/accuracy, not an FPTAS claim for every graph. It complements R801's residual-budget FPRAS: a long-road network can have extensive total isolated residual while its remaining short-road components are small. Example: subdivide every edge of an arbitrary cubic graph by a sufficiently long odd/even compatible road to make a bipartite overlap; all roads cut at the requested precision, leaving independent branching nodes. No claim that all graphs admit such a separator.

## 4. Exact finite evidence
Executed the following JavaScript BigInt code in the current run. It checks the tensor condensation independently against R801 edge-subset sums for every labeled bipartite graph of part sizes (1,1),(1,2),(2,1),(2,2),(2,3),(3,3), including empty graphs, two activity choices. Activities are scaled by 16; 14,15,16 mean 7/8,15/16,1. Each remaining vertex factor and each eliminated matrix carries the same scale 16, so graph equality uses identical scaling. Matrix error inequalities are checked by cross multiplication on all sequences of length 2..8 over the three activities and deterministic longer sequences 9..64. Three-road theta graphs with even internal lengths are bipartite (three odd-length roads), with exact versus rank-one tensor contractions. Reported example ratios are display-only. No performance benchmark or new native XOR execution; R801 supplies the underlying aligned observer theorem.
```json
{
  "graphs": 602,
  "graphCases": 1204,
  "eliminations": 2764,
  "matrices": 9893,
  "entries": 89037,
  "cutCases": 6,
  "examples": [
    {
      "internalVerticesPerPath": 4,
      "ratio": 0.9999327748387906,
      "certifiedFactor": 4.62962962962963
    },
    {
      "internalVerticesPerPath": 8,
      "ratio": 0.999999987163806,
      "certifiedFactor": 1.2390895696794189
    },
    {
      "internalVerticesPerPath": 12,
      "ratio": 0.9999999999975471,
      "certifiedFactor": 1.0248951366121475
    },
    {
      "internalVerticesPerPath": 16,
      "ratio": 0.9999999999999996,
      "certifiedFactor": 1.0027459938916559
    },
    {
      "internalVerticesPerPath": 24,
      "ratio": 1,
      "certifiedFactor": 1.0000338705580145
    },
    {
      "internalVerticesPerPath": 32,
      "ratio": null,
      "certifiedFactor": 1.0000004181503745
    }
  ],
  "mismatches": 0
}
```
```javascript
function verify(){
 const assert=(b)=>{if(!b)throw Error("mismatch")},I=()=>[[1n,0n,0n],[0n,1n,0n],[0n,0n,1n]], M=b=>[[2n*BigInt(b),16n,16n],[16n,16n,0n],[16n,0n,16n]], mul=(A,B)=>A.map(r=>B[0].map((_,j)=>r.reduce((s,x,k)=>s+x*B[k][j],0n))),tr=A=>A.map((r,i)=>r.map((_,j)=>A[j][i]));
 const power=(b,e)=>BigInt(b)**BigInt(e);
 let matrices=0,entries=0,graphs=0,graphCases=0,eliminations=0,cutCases=0;const examples=[];
 function check(P,l){let d=power(3,Math.floor(l/2)-1);for(let i=0;i<3;i++)for(let j=0;j<3;j++){let x=P[i][j]*P[0][0],y=P[i][0]*P[0][j];assert(x*d<=y*(d+2n)&&y*d<=x*(d+2n));entries++}matrices++}
 function seq(P,l){if(l>=2)check(P,l);if(l<8)for(let b of [14,15,16])seq(mul(P,M(b)),l+1)}
 seq(I(),0);
 for(let l=9;l<=64;l++){let P=I();for(let i=0;i<l;i++)P=mul(P,M(14+(i*7+l)%3));check(P,l)}
 function subset(n,F,b){let total=0n;for(let s=0;s<2**F.length;s++){let par=Array.from({length:n},(_,i)=>i),used=Array(n).fill(false),k=n;function root(i){while(par[i]!=i)i=par[i];return i}for(let j=0;j<F.length;j++)if(s>>j&1){let [u,v]=F[j];used[u]=used[v]=true;let x=root(u),y=root(v);if(x!==y){par[x]=y;k--}}let w=power(2,k);for(let i=0;i<n;i++)w*=used[i]?16n:BigInt(b[i]);total+=w}return total}
 function kernel(n,F,b){let E=F.map(([u,v])=>({u,v,P:I(),l:0})),V=Array.from({length:n},(_,i)=>i);while(true){let u=V.find(v=>{let e=E.filter(x=>x.u===v||x.v===v);return e.length===2&&e.every(x=>x.u!==x.v)});if(u===undefined)break;let [x,y]=E.filter(e=>e.u===u||e.v===u);let v=x.u===u?x.v:x.u,w=y.u===u?y.v:y.u;let A=x.v===u?x.P:tr(x.P),B=y.u===u?y.P:tr(y.P);E=E.filter(e=>e!==x&&e!==y);E.push({u:v,v:w,P:mul(mul(A,M(b[u])),B),l:x.l+y.l+1});V=V.filter(v=>v!==u);eliminations++}return {V,E}}
 function evaluate(n,K,b,cut=Infinity){let signs=Array(n).fill(0),den=1n;let E=K.E.map(e=>{if(e.l<cut)return e;den*=e.P[0][0];return {...e,P:e.P.map((r,i)=>r.map((_,j)=>e.P[i][0]*e.P[0][j]))}});function rec(k){if(k===E.length){let w=1n;for(let v of K.V){if(signs[v]===3)return 0n;w*=signs[v]?16n:2n*BigInt(b[v])}return w}let {u,v,P}=E[k],z=0n;for(let i=0;i<3;i++)for(let j=0;j<3;j++){if(P[i][j]===0n)continue;let su=signs[u],sv=signs[v];signs[u]|=i;signs[v]|=j;if(signs[u]!==3&&signs[v]!==3)z+=P[i][j]*rec(k+1);signs[u]=su;signs[v]=sv}return z}return [rec(0),den]}
 for(let [p,q] of [[1,1],[1,2],[2,1],[2,2],[2,3],[3,3]]){let all=[];for(let i=0;i<p;i++)for(let j=0;j<q;j++)all.push([i,p+j]);for(let s=0;s<2**all.length;s++){let F=all.filter((_,i)=>s>>i&1);graphs++;for(let pattern=0;pattern<2;pattern++){let n=p+q,b=Array.from({length:n},(_,i)=>pattern?14+(i+s)%3:14);let K=kernel(n,F,b),[exact,den]=evaluate(n,K,b);assert(den===1n&&exact===subset(n,F,b));graphCases++;}}}
 for(let l of [4,8,12,16,24,32]){let F=[],n=2;for(let p=0;p<3;p++){let v=0;for(let j=0;j<l;j++){F.push([v,n]);v=n++}F.push([v,1])}let b=Array.from({length:n},(_,i)=>14+i%3),K=kernel(n,F,b);assert(K.V.length===2&&K.E.length===3);let [x]=evaluate(n,K,b),[y,d]=evaluate(n,K,b,2);let h=power(3,Math.floor(l/2)-1),hi=power(h+2n,3),lo=power(h,3);assert(x*d*lo<=y*hi&&y*lo<=x*d*hi);cutCases++;examples.push({internalVerticesPerPath:l,ratio:Number(y)/Number(x*d),certifiedFactor:Number(hi)/Number(lo)})}
 return {graphs,graphCases,eliminations,matrices,entries,cutCases,examples,mismatches:0};
}
console.log(JSON.stringify(verify(),null,2));
```

## 5. Next
Investigate stronger low-rank certificates retaining both symmetric and antisymmetric channels when paths are short; quantify optimal cut budgets and compare with R801 residual bounds. General direct tilted-cluster sampler / FPRAS remains open. The new road approximation is a scoped numerical observer; preserve full joint source, exact matrices and provenance for later stronger BRC operations.
