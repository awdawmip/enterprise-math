# R845 — Multi-anchor pendant Kraft approximate residual frontier

2026-11-27. AUTHOR_ANALYTIC_PROOF / EXACT_AUXILIARY_RATIONAL_CHECKED / NOT_REVIEWED.
Continuation of R844 (a54e958db252ff8533224c99cd3326d9c840d7ed:research_notes/portable_direct/R844_PENDANT_BUNDLE_EXACT_MULTIANCHOR_ELIMINATION.md), R843 (321f9d8c48366bb1385ede42a6269db1be67ef5c), R839 cap and R837 grid. Frozen science a72226e2430ffa4786321ac86e7f0c599d5f0389 unchanged; P000 V5 and joint observer read at pin. Global entries verified at 9d623d5657615a671715d46ca12975aeff4dfad2; ACTIVE worldview and applicable research/portable rules read. Independent informed auxiliary certificate research, no formal Task claim, no native BRC experiment. Existing lane activity RA-708BCC309CE076D8BB599B91; public identity metadata read, no private execution authority established. Owner read r3-20261127-r845-running-read initially QUEUED; no shared task mutation. No external novelty claim.

## 1. The conditional approximate frontier

Remove R844 hypothesis (ii): private labels in one nontrivial Kraft scope may belong to different anchors, but retain (i), and eliminate only whole bundles each occurring in exactly one anchor. Fix all retained lengths. For a private scope S partition its private labels into g groups by anchor A, with positive rational weights b_i, rational R>1. Boundary labels have fixed integer lengths. Each private length is in 0..C, C=|S|-1 by R839 (nonempty nontrivial scope); allow any explicitly supplied common cap C for the standalone lemma. Set M=max(C, all boundary lengths,0). Let d=|S|. For an assignment satisfying sum of 2^(-L) <=1, define P_h=prod_(private labels in group h)(1+b_i R^(L_i+2)), residual v_h=P_h-1. Empty groups have P=1. Given rational 0<eps<=1, there is a finite list of actual feasible private assignments, with exact rational products, such that every feasible assignment has a listed witness with v'_h <= (1+eps)v_h simultaneously for all h. For fixed g, construction, recovery and verification have polynomial bit/time complexity in input length and 1/eps, for polynomially bounded M,C (as supplied by R839). No relaxation of Kraft feasibility is made. The list need not equal the exact Pareto frontier.

Proof. Within each group sort weights descending. The R842 exchange identity (1+bc)(1+b'c') <= (1+bc')(1+b'c) for b>=b', c<=c' implies that a feasible grade vector may be sorted ascending within each group without increasing any group product or changing the Kraft sum. Thus it suffices to assign the next x_h unassigned labels of each group at each depth l=0..M (x_h=0 for l>C).

Use R843 saturated slots: state counts i_h already assigned, s available nodes capped by total remaining private+boundary labels; start at s=min(1,d). Let c_l count fixed boundary labels at depth l. Choose nonnegative integers x_h<=n_h-i_h with c_l+sum x_h<=s. Update i'_h=i_h+x_h, s'=min(r,2(s-c_l-sum x_h)), where r counts all labels still unassigned after this depth. At last depth require r=0. This is exact: unsaturated availability evolves by doubling unused slots, and replacing s by min(s,r_before) preserves every possible future allocation, since allocating at most r_before leaves at least r_after slots in the saturated case and doubling cannot reduce them. Conversely a capped state never overstates actual availability. Hence the sequence is equivalent to the original Kraft inequality. Boundary counts must be reserved at their own depths, including those above the private cap.

For each nonempty group choose base a_h=min_i b_i R^2 and bound U_h=prod_i(1+b_i R^(C+2))-1. Every nonzero partial product residual lies in [a_h,U_h]. Put q0=1+eps/[2(M+1)]. Use half-open bins [a_h q0^j,a_h q0^(j+1)), plus a separate zero bin. State includes exact witness residuals but keys only (i_1,...,i_g,s,bin(v_1),...,bin(v_g)). After each depth keep an arbitrary actual representative for each key, storing its exact products and reconstruction pointer. For a transition multiplying the group product by a fixed F>=1, the residual map is v -> Fv+(F-1), which preserves componentwise multiplicative comparison: if v'<=lambda v, lambda>=1, then Fv'+F-1<=lambda(Fv+F-1). Representatives with identical bin differ by a factor less than q0 in either direction (zero exactly). Representatives have identical counts/slots so all future choices remain available; no approximation enters Kraft. By induction a sorted reference trajectory has a retained trajectory with v'_h<=q0^j v_h after j depths. At j=M+1, q0^(M+1)<=exp(eps/2)<=1+eps (log(1+eps)>=eps/2 for eps<=1). All kept points are actual feasible witnesses. Reconstruction by pointers restores original labels. For d=0 or no private labels the same reasoning gives empty feasible product if boundary fits, else no states.

Complexity: each group has O(1+log(U_h/a_h)/log(q0)) bins plus zero; denote their maximum by J. For rational inputs and polynomial C, log(U/a) is bounded polynomially by input length (even for tiny positive weights). q0 has polynomial bit length and the rational endpoints a_h q0^j have polynomial bit length for polynomial j and 1/eps. Each depth has at most (d+1)^(g+1)(J+1)^g states, and each state at most (d+1)^g transition choices. Total O((M+1)(d+1)^(2g+1)(J+1)^g) transitions, plus polynomial arithmetic, sorting, endpoint generation/search, storage and recovery costs. Exact products have polynomial bit length since each factor is used at most once per witness. Output may be pruned by exact Pareto domination but does not require that step. This is a local conditional frontier, not a global polynomial algorithm for unbounded anchor count or unrestricted shared width.

## 2. Simultaneous gap guarantee: max, not product

In R844 replace each scalar private minimum F_S by a selectable vector from this list, and multiply its component P_h into the corresponding anchor. Free private labels have length zero. Retain every original Kraft constraint not eliminated and all retained payments and grades. The reconstructed exact private payments are d_AH=w_H at R1 for pendant bundles; all original retained inequalities and safety margins are verified exactly from reconstructed Q_A. Any feasible reduced solution is therefore sound. Distinct private scopes have disjoint private labels; a pendant bundle can cross scopes, since 1+w_H is exactly the product over its labels. A local witness may increase one exact component relative to the optimum at the same R, hence no unconditional same-radius completeness is claimed.

Suppose an original real certificate exists at R2>R1>1 with Q_A<=2-eta. Cap grades by R839, set original pendant payments to exact w_H, and condition on retained lengths. At R1 for every group residual the positive polynomial expansion in R has nonzero exponents at least 2. Therefore v_h(R2)>=(R2/R1)^2 v_h(R1). If 1+eps <= (R2/R1)^2, a listed witness at R1 has P'_h<=P_h(reference at R2). All pendant multipliers are simultaneously no larger at every anchor, even across many private scopes. For each retained incidence use the R837 fixed grid with base a_H=w_H(1) for the capped retained grading, ratio q (1<q<=2), upper cap 1-eta, rounding the reference payment down. If grid domains must be independent of grades, choose instead the lower base prod_(f in H)(1+b_f)-1, which is exactly w_H(1) and grade independent. A grid floor exists because d*>=w_H(R2)>=q a_H when q<=(R2/R1)^2; floor d>=d*/q. Then all Q_A and all T_AH for retained H are no larger than their reference values, by direct factor comparison excluding the relevant retained payment. Monotonicity of r(T)=T/(2-T) gives the original retained inequality at R1: w_H(R1) prod r(T_new)<=d*_AH/q<=d_AH. All Q_A<=2-eta and total C=sum_A(Q_A-1)/(2-Q_A) <= reference C. Thus a sufficient combined gap is

    max(q,1+eps) <= (R2/R1)^2,

rather than q(1+eps). These two losses are paid on different components (private residual approximation and retained payment floor). This guarantee keeps the original safety margin and does not inflate the reference objective. For fixed number of anchor groups per private scope and bounded reduced width (including frontier-selection variables and their boundary-dependence), finite-domain variable elimination as in R840 gives polynomial time for fixed structural bounds, fixed gap, polynomial input bits. Build each conditional list for every allowed boundary tuple, include exact products in anchor factors, and check compatible list-index/tuple; number of choices per tuple is polynomial, so table construction and witness recovery are included. If the reduced width grows this does not imply polynomial time. If exact full Port observer is unavailable no native FPTAS follows.

## 3. Evidence and scope

Executed exact BigInt rational checks for n=2..5, all two-group nonempty splits, three fixed boundary profiles [],[2],[1,3], R in {4/3,2}, eps in {1/4,1/2}. Brute force enumerates all capped assignments of the labeled weights (not only sorted), compares each feasible vector against a returned simultaneous residual witness, verifies every returned Kraft condition and exact product, and checks no larger anchor products at R2=(5/4)R. This verifies the local gap, not an end-to-end multi-anchor solver. General results above are analytical. Exact output:
```json
{
  "instances": 120,
  "feasibleVectors": 41260,
  "frontierWitnesses": 5713,
  "transitions": 19501,
  "merged": 1625,
  "dominationChecks": 781644,
  "peakStates": 208,
  "strictGapChecks": 41260
}
```

```javascript
function replay(){
 const gcd=(a,b)=>{while(b)[a,b]=[b,a%b];return a};
 const F=(a,b=1n)=>{a=BigInt(a);b=BigInt(b);let g=gcd(a<0n?-a:a,b);return[a/g,b/g]};
 const add=(a,b)=>F(a[0]*b[1]+b[0]*a[1],a[1]*b[1]),sub=(a,b)=>F(a[0]*b[1]-b[0]*a[1],a[1]*b[1]),mul=(a,b)=>F(a[0]*b[0],a[1]*b[1]),le=(a,b)=>a[0]*b[1]<=b[0]*a[1],pow=(a,k)=>F(a[0]**BigInt(k),a[1]**BigInt(k)),one=F(1),zero=F(0);
 const stats={instances:0,feasibleVectors:0,frontierWitnesses:0,transitions:0,merged:0,dominationChecks:0,peakStates:0,strictGapChecks:0};
 const product=(a)=>a.reduce(mul,one);
 function solve(B,fixed,R,eps,C){
  const g=B.length,n=B.reduce((s,b)=>s+b.length,0),M=Math.max(C,0,...fixed),d=n+fixed.length,q=add(one,mul(eps,F(1,2*(M+1))));
  const bs=B.map(b=>b.slice().sort((a,b)=>le(a,b)?(le(b,a)?0:1):-1));
  const c=Array(M+1).fill(0),tail=Array(M+2).fill(0);for(const l of fixed)c[l]++;for(let l=M;l>=0;l--)tail[l]=tail[l+1]+c[l];
  const costs=bs.map(b=>b.map(x=>Array.from({length:C+1},(_,l)=>add(one,mul(x,pow(R,l+2))))));
  const grids=bs.map((b,h)=>{if(!b.length)return[];let a=mul(b[b.length-1],pow(R,2)),U=sub(product(costs[h].map(x=>x[C])),one),v=[a];while(le(v[v.length-1],U))v.push(mul(v[v.length-1],q));return v});
  function bin(x,h){if(x[0]===0n)return -1;let a=0,b=grids[h].length-1;while(a+1<b){let m=(a+b)>>1;if(le(grids[h][m],x))a=m;else b=m}return a}
  const init={i:Array(g).fill(0),s:Math.min(1,d),p:Array(g).fill(one),L:Array.from({length:g},()=>[])};
  let states=new Map([["init",init]]);
  for(let l=0;l<=M;l++){let next=new Map();for(const o of states.values()){
   if(o.s<c[l])continue;
   function rec(h,available,counts,ps,ls){
    if(h===g){let rem=tail[l+1]+bs.reduce((s,b,k)=>s+b.length-counts[k],0);if(l===M&&rem)return;let s=Math.min(rem,2*available),key=[...counts,s,...ps.map((p,k)=>bin(sub(p,one),k))].join(",");stats.transitions++;
     if(next.has(key)){stats.merged++;return}next.set(key,{i:counts,s,p:ps,L:ls});return;
    }
    let cap=l<=C?Math.min(available,bs[h].length-o.i[h]):0,p=o.p[h];
    for(let x=0;x<=cap;x++){if(x)p=mul(p,costs[h][o.i[h]+x-1][l]);rec(h+1,available-x,[...counts,o.i[h]+x],[...ps,p],[...ls,o.L[h].concat(Array(x).fill(l))])}
   }rec(0,o.s-c[l],[],[],[])
  }states=next;stats.peakStates=Math.max(stats.peakStates,states.size)}
  return {out:[...states.values()],bs,M,q};
 }
 function kraft(ls,M){return ls.reduce((s,l)=>s+(1n<<BigInt(M-l)),0n)<=1n<<BigInt(M)}
 for(let n=2;n<=5;n++)for(let split=1;split<n;split++)for(const fixed of [[],[2],[1,3]])for(const R of [F(4,3),F(2)])for(const eps of [F(1,4),F(1,2)]){
  let B=[Array.from({length:split},(_,i)=>F(1+i%3,128)),Array.from({length:n-split},(_,i)=>F(2+i%2,192))],C=n+fixed.length-1;
  let {out,bs,M,q}=solve(B,fixed,R,eps,C);stats.instances++;stats.frontierWitnesses+=out.length;
  for(const o of out){if(!kraft([...fixed,...o.L.flat()],M))throw Error("invalid witness");for(let h=0;h<bs.length;h++)if(!le(o.p[h],product(bs[h].map((b,i)=>add(one,mul(b,pow(R,o.L[h][i]+2))))))||!le(product(bs[h].map((b,i)=>add(one,mul(b,pow(R,o.L[h][i]+2))))),o.p[h]))throw Error("bad product")}
  let ls=[];function rec(i){if(i<n){for(let l=0;l<=C;l++){ls[i]=l;rec(i+1)}return}if(!kraft([...fixed,...ls],M))return;stats.feasibleVectors++;let p=[product(bs[0].map((b,j)=>add(one,mul(b,pow(R,ls[j]+2))))),product(bs[1].map((b,j)=>add(one,mul(b,pow(R,ls[split+j]+2)))))];
   let found=out.some(o=>{stats.dominationChecks++;return o.p.every((v,h)=>le(sub(v,one),mul(add(one,eps),sub(p[h],one))))});if(!found)throw Error("frontier gap");
   const R2=mul(R,F(5,4));let p2=[product(bs[0].map((b,j)=>add(one,mul(b,pow(R2,ls[j]+2))))),product(bs[1].map((b,j)=>add(one,mul(b,pow(R2,ls[split+j]+2)))))];if(!out.some(o=>o.p.every((v,h)=>le(v,p2[h]))))throw Error("radius gap");stats.strictGapChecks++;
  }rec(0);
 }
 return stats;
}
console.log(JSON.stringify(replay(),null,2));
```

Original signed joint moments, road matrix, branch identities, ordered steps, multiplicities, provenance and common depth remain unchanged. The approximation pertains solely to positive certificate resources, not native observation or arbitrary original resource vectors. No independent review, native realization, large-scale timing, or new BRC run performed. Next: implement reduced multi-anchor solver with frontier-selection variables and test end-to-end gap and width; investigate whether an exponential exact Pareto frontier is forced for even two anchor groups. Full Port observer and native realization remain open.
