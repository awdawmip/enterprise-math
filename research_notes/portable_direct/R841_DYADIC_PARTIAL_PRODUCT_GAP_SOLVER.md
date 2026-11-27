# R841 - Certified dyadic partial-product states for multi-anchor joint optimization

2026-11-27. AUTHOR_ANALYTIC_PROOF / EXACT_AUXILIARY_RATIONAL_CHECKED / NOT_REVIEWED.
Independent informed portable continuation, own EM-DIRECT-82A007 / RA-708BCC309CE076D8BB599B91. Own session metadata r3-20261127-r841-own-read verified, no run, execution_authorized=false. Prior R840 owner read SUCCEEDED (empty RUNNING projection as of 2026-11-27T09:20:25.139581Z, Source drift); current r3-20261127-r841-running-read RUNNING at last check, NATIVE_RUNNER. No shared Task or owner mutation. Global entry same immutable main snapshot 19f37ef1b2bdf28f756bd8ba5ba08f49d16d486b, ACTIVE worldview and current normative and portable routes read. Frozen scientific pin a72226e2430ffa4786321ac86e7f0c599d5f0389, P000 V5 blob dc84bdae6595b5e237a2ad50d8b21916adb2e447 and joint observer blob 3923890d77a02d84b772f789e6912dd14f220d14 read directly (generated foundation startup 404); global V4 startup matches canonical blob. Preserve full original labels, signed joint moments, road matrices, ordered steps, branch provenance and common depth. This is auxiliary certificate optimization, not a native Heartbeat/BRC experiment.

Sources: R840 ff9f799ab47556dca24303b3a8679d8ae414dfe3:research_notes/portable_direct/R840_MULTI_ANCHOR_GRID_JOINT_WIDTH_SOLVER.md; R839 f5840f229dc8d90cb25f1f6674751d0814f7ddd6:research_notes/portable_direct/R839_SHARP_LOCAL_KRAFT_CAP_AND_BOUNDED_WIDTH_SOLVER.md; R837 9d062156808e49e28ff18098f507ddd7c409bc1a:research_notes/portable_direct/R837_RATIONAL_GRID_PAYMENT_SEARCH_AND_SHARP_ROUNDING.md. Inherit R834/R835 observer, cover and connected enumeration hypotheses as in R840. New scope: avoid whole-anchor K^a domains and whole-bundle footprint tables via approximate but sound auxiliary certificate states. No external priority claim.

## 1. Dyadic upward rounding and nonnegative residual recurrence

Fix explicit original graph, partition H, valid anchor cover A, b_f>0 rational, R>1 rational, margin eta in (0,1), epsilon in (0,1], fixed positive finite rational payment grids. R839 bounds each nonnegative integer L_f by M_f=max({0} union {deg(x)-1:x in N(f)}). Set u_f=b_f R^(L_f+2), w_H=prod_{f in H}(1+u_f)-1. Let n=max(1,number of labels + number of anchor-bundle incidences), choose the least nonnegative integer p with 2^(-p)<=eta epsilon/(64 n^2); h=1+2^(-p), delta=eta epsilon/(32n). For x>0 let e=floor(log2 x) and round x upward to the next multiple of 2^(e-p), including x itself if exact. Define U(0)=0. This is exact rational arithmetic, with x<=U(x)<=h x; it has p fractional mantissa bits (plus leading 1), normalized at a power of 2. No logarithm approximation is needed to determine e.

For nonnegative x_j let s_j=(1+s_{j-1})(1+x_j)-1, s_0=0. Store S_0=0, S_j=U(S_{j-1}+x_j+S_{j-1}x_j). Then s_j<=S_j<=h^j s_j by induction: if S<=h^k s, the next unrounded residual is <=h^k(s+x+sx), since x>=0. Similarly rounded product from 1 using P_j=U(P_{j-1}x_j) for x_j>=1 is between the exact product and h^j times that product. For j<=n, h^j<=1/(1-n(h-1))<=1+delta, using the binomial expansion bound (1+x)^m<=1/(1-mx) for mx<1. Rounding residuals rather than the whole product avoids subtractive cancellation when activity or payment is very small.

## 2. Sound certificate with constant-arity local recurrences

For each anchor A, split the computation of s_A=Q_A-1=prod_H(1+d_AH)-1 into the above residual chain, output Sh_A. Impose Sh_A<=1-eta/2. Define Qh_A=1+Sh_A, That_AH=Qh_A/(1+d_AH), rh_AH=That_AH/(2-That_AH). These are positive exact rationals; 1<=T_AH<=That_AH<2, 1<=r_AH<=rh_AH. For each bundle H, compute wh_H by the residual chain over u_f. Compute Ph_H by a rounded product chain over rh_AH for incident anchors. Compute m_H=min_A(d_AH rh_AH) by a separate exact running minimum. Impose
    wh_H Ph_H <= m_H.
Keep every original neighborhood Kraft inequality exact. Use positive payment variables separately, not a joint anchor vector.

Soundness: wh_H>=w_H, Ph_H>=prod_A rh_AH. For each A, dividing the terminal inequality by rh_AH>0 gives w_H prod_{D!=A} r_DH <= d_AH. The exact margin Q_A<=Qh_A<=2-eta/2 holds. Hence every returned assignment certifies the R834 inequalities at R. The exact tail coefficient C=sum_A s_A/(1-s_A) is bounded by Ch=sum_A Sh_A/(1-Sh_A). Original joint moments are unchanged and P_U(1) retains its original value for every original subset; only auxiliary resources are rounded. Return the original exact certificate as well as its upper objective. An exact final check can use the unrounded R834 inequalities.

## 3. Gap completeness with explicit objective guarantee

Consider any grid assignment with original margin Q_A<=2-eta and inflated directed inequalities (1+epsilon) w_H prod_{D!=A} r_DH<=d_AH. From section 1, Sh_A<= (1+delta)s_A, wh_H<=(1+delta)w_H, so Qh_A<=Q_A+delta<=2-eta/2. Also That_AH<= (1+delta)T_AH, That_AH-T_AH<=delta, because s_A<=1 and denominator 1+d_AH>=1. Consequently
    rh_AH/r_AH <= (1+delta)/(1-delta/eta) <= 1+6delta/eta.
The loose constant is valid since delta/eta<=1/32. For every H, |A_H|<=n, and
    wh_H Ph_H <= (1+delta)^2(1+6delta/eta)^n w_H prod_A r_AH
              <= (1+epsilon) w_H prod_A r_AH.
Indeed the product is bounded by 1/(1-2delta-6n delta/eta)<=1/(1-epsilon/4)<=1+epsilon, by expanding products of factors 1+x with total x<1 and bounding each elementary sum by the corresponding power of the total. The same inflated directed inequality implies the last expression is <=d_AH r_AH<=d_AH rh_AH for every A. All rounded constraints follow. Each objective summand is increased by at most (1+delta)/(1-delta/eta)<=1+epsilon, including zero summands by continuity or direct equality. Thus Ch<= (1+epsilon) C.

For fixed geometric grids a_H=w_H(1), ratio q in (1,2], cap 1-eta, suppose a real integer certificate d* exists at R2>R1>1 with margin eta. R839 caps its grading. For q(1+epsilon)<=(R2/R1)^2, the positive activity polynomial has w_H(R2)>=q(1+epsilon)w_H(R1). Round d* down to the grid point d<=d*: d*>=q(1+epsilon)w_H(R1)>=q a_H, so the point exists, d>=d*/q, and the cap holds. Since propagation is increasing in every payment, (1+epsilon) w_H(R1) prod_{D!=A}r_DH(d)<=d*_AH/q<=d_AH. Thus the constructed rounded CSP at R1 is feasible. Its minimum upper objective is <=(1+epsilon) times the exact tail coefficient of the original witness at R2. The returned exact coefficient is no larger than that minimum upper objective. In particular the extra discretization consumes the additional multiplicative radius factor sqrt(1+epsilon) on top of R837's sqrt(q), and reduces the guaranteed margin to eta/2. Failure excludes the specified larger-radius stronger-margin real witness, not exact feasibility at R1.

## 4. State and width bounds, and limits

Make individual variables L_f and d_AH, one dyadic state per prefix of each anchor residual, bundle residual and bundle propagation chain, and one exact minimum state per bundle incidence prefix. Keep the last anchor residual linked to each of its incident r computations. A local transition uses at most three or four variables (e.g. previous product, current payment, last anchor residual, next product); compute rh as a rational function on those arguments, so no extra high-arity factor. The minimum transition has the same arity. Terminal product test uses three variables. The unary cost is Sh_A/(1-Sh_A). Keep the original Kraft scopes (their arity may be large). The expanded primal constraint graph, not the old bundled graph, controls width.

The dyadic state domain is polynomial: positive residuals are at least the least positive input grid payment or min b_f (or a lower dyadic power of 2); feasible anchor prefixes are <=1-eta/2; feasible activity prefixes are <=1, since rh>=1 and the terminal test implies wh<=d<=1. These prefix caps do not discard a witness accepted by section 3, because prefixes are nondecreasing. Propagation prefixes lie in [1,(8/eta)^n], since rh<=4/eta and h<=2. Hence the exponent interval length is O(B+n log(8/eta)), where B bounds input/derived grid and b bit lengths. There are 2^p=O(n^2/(eta epsilon)) mantissas per exponent. The exact minimum domain consists of the union of all d_AH rh_AH values from local payment and terminal anchor state choices, at most J K times the dyadic domain size (plus initial infinity sentinel), where J is total incidence count, K is maximum payment domain size. It is not a Cartesian product of all such choices. All dyadic and rational numbers have polynomial bit size in B,n,log(1/(eta epsilon)), with L<=Delta-1 from R839. All computed values and inequalities can be evaluated exactly on these finite domains. Denote by D' the maximum of the finite-domain sizes above, max(1,Delta), and K. It is polynomial in explicit input size, K, 1/eta and 1/epsilon, independent of any exponential K^a term. For a supplied expanded-graph elimination order of width t', use R840 exact min-sum elimination on these tables in poly(input,bit lengths) (D')^(t'+1) time and space. Minimize Ch and reconstruct all assignments by backpointers. This is a gap-complete solver construction, not an exact solver for the original real-payment problem. No uniform bound on t' in terms of the unexpanded incidence graph treewidth is asserted. The remaining high-arity Kraft constraints and possible expanded-graph width are concrete next problems. Constants and polynomial domains are conservative, not measured large-scale speedup. The solver construction is proved; a full end-to-end expanded-graph DP implementation/benchmark has not been executed.

## 5. Exact executed replay

JavaScript BigInt reduced rationals, no floating-point certificate decisions. Enumerate all 2- and 3-vertex labeled simple graphs, singleton or merged first two labels, two weight profiles; use fixed capped grading, projected edge anchors, first three geometric grid values per incidence, R=5/4, eta=1/2, epsilon=1/4. For margin-valid vectors check exact/rounded implication, inflated gap implication, anchor/activity/propagation/objective bounds. Also check witnesses from a high-radius grid search at R2=2, two tight one-label cases and eight specified large-anchor/long-footprint cases with up to 64 incidences. The large-anchor and footprint cases test arithmetic recurrences only, not the full DP. One exact-feasible vector is rejected by the conservative rounding (non-dyadic exact tight case), as expected; this is not a contradiction or a proof of exact infeasibility. Code and output:
```json
{
  "instances": 40,
  "assignments": 2505,
  "exactFeasible": 301,
  "roundedFeasible": 300,
  "exactOnly": 1,
  "gapWitnesses": 181,
  "highArityCases": 8,
  "rounds": 32765,
  "anchorBounds": 6536,
  "activityBounds": 7395,
  "propagationBounds": 7395,
  "objectiveBounds": 2505
}
```
```javascript
function replay(){
 const gcd=(a,b)=>{while(b){[a,b]=[b,a%b]}return a<0n?-a:a};
 const F=(a,b=1n)=>{a=BigInt(a);b=BigInt(b);if(b<=0n)throw Error("denominator");const g=gcd(a,b);return [a/g,b/g]};
 const add=(a,b)=>F(a[0]*b[1]+b[0]*a[1],a[1]*b[1]),sub=(a,b)=>F(a[0]*b[1]-b[0]*a[1],a[1]*b[1]),mul=(a,b)=>F(a[0]*b[0],a[1]*b[1]),div=(a,b)=>F(a[0]*b[1],a[1]*b[0]),le=(a,b)=>a[0]*b[1]<=b[0]*a[1],pow=(a,k)=>F(a[0]**BigInt(k),a[1]**BigInt(k)),one=F(1),two=F(2),zero=F(0),prod=a=>a.reduce(mul,one),sum=a=>a.reduce(add,zero),min=a=>a.reduce((x,y)=>le(x,y)?x:y);
 const ok=(x,s)=>{if(!x)throw Error(s)};
 const stats={instances:0,assignments:0,exactFeasible:0,roundedFeasible:0,exactOnly:0,gapWitnesses:0,highArityCases:0,rounds:0,anchorBounds:0,activityBounds:0,propagationBounds:0,objectiveBounds:0};
 function up(x,p){
  if(x[0]===0n)return zero;
  let e=x[0].toString(2).length-x[1].toString(2).length;
  const dy=k=>k>=0?F(1n<<BigInt(k)):F(1n,1n<<BigInt(-k));
  if(!le(dy(e),x))e--;
  const step=dy(e-p),v=div(x,step),k=(v[0]+v[1]-1n)/v[1],y=mul(F(k),step);
  ok(le(x,y)&&le(y,mul(x,add(one,dy(-p)))),"round bound");stats.rounds++;return y;
 }
 function check(H,A,b,L,d,R,eta,eps,expectGap=false){
  const n=Math.max(1,b.length+A.reduce((s,a)=>s+a.length,0)),delta=div(mul(eta,eps),F(32*n));
  let p=0;while(!le(F(1,1n<<BigInt(p)),div(mul(eta,eps),F(64*n*n))))p++;
  const margin=sub(two,eta),relax=sub(two,div(eta,two));
  const AH=H.map((_,i)=>A.map((a,j)=>a.includes(i)?j:-1).filter(j=>j>=0));
  const u=b.map((x,i)=>mul(x,pow(R,L[i]+2)));
  const accumulate=xs=>xs.reduce((s,x)=>up(add(add(s,x),mul(s,x)),p),zero);
  const s=d.map(ds=>sub(prod(ds.map(x=>add(one,x))),one)),sh=d.map(accumulate),Q=s.map(x=>add(one,x)),Qh=sh.map(x=>add(one,x));
  for(let a=0;a<A.length;a++){ok(le(s[a],sh[a])&&le(sh[a],mul(add(one,delta),s[a])),"anchor");stats.anchorBounds++}
  if(Q.some(x=>!le(x,margin))){ok(!expectGap,"gap margin");return;}
  const w=H.map(hs=>sub(prod(hs.map(i=>add(one,u[i]))),one)),wh=H.map(hs=>accumulate(hs.map(i=>u[i])));
  for(let i=0;i<H.length;i++){ok(le(w[i],wh[i])&&le(wh[i],mul(add(one,delta),w[i])),"activity");stats.activityBounds++}
  ok(Qh.every(x=>le(x,relax)),"relaxed margin");
  const rs=(QQ)=>A.map((a,j)=>a.map((_,i)=>{let T=div(QQ[j],add(one,d[j][i]));return div(T,sub(two,T))}));
  const r=rs(Q),rh=rs(Qh);
  let exact=true,approx=true,gap=true;
  for(let i=0;i<H.length;i++){
   const rr=AH[i].map(a=>r[a][A[a].indexOf(i)]),rrh=AH[i].map(a=>rh[a][A[a].indexOf(i)]),dd=AH[i].map(a=>d[a][A[a].indexOf(i)]);
   const P=prod(rr),Ph=rrh.reduce((s,x)=>up(mul(s,x),p),one),bound=mul(wh[i],Ph),actual=mul(w[i],P);
   ok(le(actual,bound)&&le(bound,mul(add(one,eps),actual)),"aggregate");stats.propagationBounds++;
   exact&&=dd.every((x,j)=>le(actual,mul(x,rr[j])));
   approx&&=le(bound,min(dd.map((x,j)=>mul(x,rrh[j]))));
   gap&&=dd.every((x,j)=>le(mul(add(one,eps),actual),mul(x,rr[j])));
  }
  ok(!approx||exact,"soundness");ok(!gap||approx,"gap");
  const C=sum(s.map(x=>div(x,sub(one,x)))),Ch=sum(sh.map(x=>div(x,sub(one,x))));
  ok(le(C,Ch)&&le(Ch,mul(add(one,eps),C)),"objective");stats.objectiveBounds++;
  stats.assignments++;if(exact)stats.exactFeasible++;if(approx)stats.roundedFeasible++;if(exact&&!approx)stats.exactOnly++;if(gap)stats.gapWitnesses++;if(expectGap)ok(gap&&approx,"expected gap");
 }
 function instance(n,edges,merge,profile){
  const G=Array.from({length:n},()=>[]);for(const [v,w] of edges){G[v].push(w);G[w].push(v)}
  const H=merge?[[0,1],...Array.from({length:n-2},(_,i)=>[i+2])]:Array.from({length:n},(_,i)=>[i]);
  const own=Array(n);H.forEach((h,i)=>h.forEach(v=>own[v]=i));
  const A=[...new Set(edges.map(([v,w])=>[...new Set([own[v],own[w]])].sort((a,b)=>a-b).join(",")))].map(s=>s.split(",").map(Number));
  for(let i=0;i<H.length;i++)if(!A.some(a=>a.includes(i)))A.push([i]);
  const b=G.map((_,i)=>F(1+i%2,profile===0?128:64)),L=G.map(N=>Math.max(0,...N.map(v=>G[v].length-1)));
  const base=H.map(h=>sub(prod(h.map(v=>add(one,b[v]))),one));
  const inc=A.flatMap((a,i)=>a.map((h,j)=>[i,j,h]));
  for(let m=0;m<3**inc.length;m++){
   let t=m,d=A.map(a=>a.map(()=>zero));for(const [i,j,h] of inc){d[i][j]=mul(base[h],F(2**(t%3)));t=Math.floor(t/3)}
   check(H,A,b,L,d,F(5,4),F(1,2),F(1,4));
  }
  const R2=F(2),w=H.map(h=>sub(prod(h.map(v=>add(one,mul(b[v],pow(R2,L[v]+2))))),one));
  let d=A.map(a=>a.map(h=>base[h])),success=false;
  for(let it=0;it<20;it++){
   const Q=d.map(ds=>prod(ds.map(x=>add(one,x))));
   if(Q.some(x=>!le(x,F(3,2))))break;
   let next=d.map(a=>a.slice()),changed=false,fail=false;
   for(const [i,j,h] of inc){
    let phi=w[h];
    for(let a=0;a<A.length;a++)if(a!==i&&A[a].includes(h)){let T=div(Q[a],add(one,d[a][A[a].indexOf(h)]));phi=mul(phi,div(T,sub(two,T)))}
    let x=d[i][j];while(!le(phi,x)&&le(x,F(1,2)))x=mul(x,two);
    if(!le(x,F(1,2))){fail=true;break}if(!le(x,d[i][j]))changed=true;next[i][j]=x;
   }
   if(fail)break;if(!changed){success=true;break}d=next;
  }
  if(success)check(H,A,b,L,d,F(5,4),F(1,2),F(1,4),true);
  stats.instances++;
 }
 for(let n=2;n<=3;n++){let E=[];for(let i=0;i<n;i++)for(let j=i+1;j<n;j++)E.push([i,j]);for(let mask=0;mask<2**E.length;mask++)for(let merge of [false,true])for(let profile=0;profile<2;profile++)instance(n,E.filter((_,i)=>mask&(1<<i)),merge,profile)}
 check([[0]],[[0]],[F(1,25)],[0],[[F(1,16)]],F(5,4),F(1,2),F(1,4));
 check([[0]],[[0]],[F(1,27)],[0],[[F(25,432)]],F(5,4),F(1,2),F(1,4));
 for(let a of [8,16,32,64]){
  let H=Array.from({length:a},(_,i)=>[i]),A=[H.map((_,i)=>i)],b=H.map(()=>F(1,64*a)),L=H.map(()=>Math.ceil(Math.log2(a)));
  b=b.map(x=>div(x,F(16)));let d=[H.map((_,i)=>mul(mul(b[i],pow(F(5,4),L[i]+2)),F(5,4)))];
  check(H,A,b,L,d,F(5,4),F(1,2),F(1,4),true);stats.highArityCases++;
  H=[[0],...Array.from({length:a},(_,i)=>[i+1])];A=Array.from({length:a},(_,i)=>[0,i+1]);b=H.map(()=>F(1,256*a));L=H.map((_,i)=>i===0?0:Math.ceil(Math.log2(a)));d=A.map(()=>[F(1,8*a),F(1,8*a)]);
  check(H,A,b,L,d,F(5,4),F(1,2),F(1,4),true);stats.highArityCases++;
 }
 return stats;
}
console.log(replay());
```
Next: exploit tree decompositions to order partial-product chains, compress exact Kraft constraints with a carry-state automaton or bounded residual dominance, and implement actual expanded-graph DP with measured comparisons. Maintain the unresolved native Port realizability, exact joint moment oracle and general Port FPTAS. No formal Result, review, or native attribution asserted.
