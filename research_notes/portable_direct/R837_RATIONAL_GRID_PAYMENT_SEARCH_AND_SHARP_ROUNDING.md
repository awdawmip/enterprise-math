# R837 — Rational-grid payment search, radius gap guarantee and sharp fixed-payment rounding

2026-11-27. AUTHOR_ANALYTIC_PROOF / EXACT_AUXILIARY_RATIONAL_CHECKED / NOT_REVIEWED.
Independent portable TASK_RESEARCH, EM-DIRECT-82A007 / RA-708BCC309CE076D8BB599B91. Own session metadata verified by r3-20261127-r837-own-read, no run, execution_authorized=false. Owner query r3-20261127-r837-running-read was RUNNING during derivation (event guard changed, native runner continued). No shared claim, ownership or Result mutation. Frozen science a72226e2430ffa4786321ac86e7f0c599d5f0389; P000 V5 and joint observer blob 3923890d77a02d84b772f789e6912dd14f220d14 read. Frozen Heartbeat companion path returned 404; current machine terminology companion read (blob 94a02d067be2b039ca4c0f7ffedb5ebde8430e08) without repinning. Global entries at main@0bf30e5a24f3922a6dd51ff67675511fedd9d974, ACTIVE worldview, research method, portable, residual and BRC-only scope read. Auxiliary combinatorial observer, not a native Heartbeat experiment or new physical reference run. Retain original signed joint moments, road matrices, branch identity, provenance, time order and common depth.
Direct dependencies: R836 2bcc65992adb4ae3b77cb1125554a25399c5752e:research_notes/portable_direct/R836_JOINT_NEIGHBOR_KRAFT_CONVEX_CERTIFICATE.md; R835 5bbb0f700911cefec0c28aa434b0d73be0a4d6cf:research_notes/portable_direct/R835_NEIGHBOR_PREFIX_REGRADING_HIGH_GIRTH_OBSTRUCTION.md; R834 6fd1421bb2e12caf06677625b23706d5d04444bf:research_notes/portable_direct/R834_DEPENDENCY_COVER_QUOTIENT_AND_COST_REGRADING.md. Reuse their exact scope, joint moment oracle and positive baseline hypotheses. No independent review asserted.

## 1. Fixed-grading rational-grid theorem (arbitrary bundles and explicit anchor cover)

Fix R834's partition H and anchor sets A covering all bundle dependence edges. Fix R835's integer lengths satisfying neighborhood Kraft, degrees c_f=L_f+2, rational R>1, positive rational b_f=|alpha_f|lambda_f. Define w_H=prod_{f in H}(1+b_f R^c_f)-1, Q_A=prod_{H in A}(1+d_AH), T_{A|H}=prod_{K in A minus H}(1+d_AK). Zero activity labels may be omitted for this observer only. For rational margin 0<eta<1 require Q_A<=2-eta. Let
    Phi_i(d)=w_H prod_{D in A_H minus A} T_{D|H}/(2-T_{D|H}),  i=(A,H).
Use a rational q in (1,2], and positive rational base a_H<=w_H. For incidence i=(A,H), use the grid G_i={a_H q^k:k>=0 integer, a_H q^k<=1-eta}. If empty, return BASE_CAP. Start at each grid minimum. If some Q_A>2-eta, return MARGIN. Otherwise replace each coordinate by max(d_i,ceil_grid(Phi_i(d))); if no grid point meets the bound, return GRID_CAP. At a stationary point return the exact rational witness and verify all inequalities.

Theorem. The algorithm terminates, returns the componentwise least feasible grid witness when one exists, and proves there is no feasible grid witness when it fails. Moreover, if there is any real witness d* with margin Q_A<=2-eta for inflated activities q w_H, the algorithm succeeds and its output is <=d* coordinatewise. Failure rules out such an inflated witness, but need not rule out an uninflated real witness.

Proof. Within the margin domain all T are in [1,2-eta], and the ratio T/(2-T) is increasing. Hence Phi is componentwise increasing. Iterates are increasing; any feasible grid witness dominates the initial point and by monotonicity dominates every subsequent point, including the rounded update. Thus cap/margin failure rules out every feasible grid witness, and the fixed point is least. For arbitrary inflated supersolution d*, every d*_i>=q w_H>=a_H and d*_i<=1-eta by its margin. When d<=d*, the unbounded geometric ceiling of x=Phi_i(d) satisfies ceil(x)<=q x (since x>=a_H); hence ceil(x)<=q Phi_i(d*)<=d*_i. That ceiling is in the truncated grid. Inductively d<=d*, and Q_A never exceeds its allowed margin. Termination follows because every nonstationary successful step strictly increments at least one finite grid index. At success the R834 analytic inequalities hold exactly; the margin makes its log-tail estimate finite. This argument permits arbitrary explicit bundles and overlapping anchors; no independence assumption beyond the inherited joint observer is introduced.

Complexity. Let J be the number of incidences and B bound the bit length of computed rational activities, bases, q and eta. Each grid has at most 1+O(B/(q-1)) points, using log(q)>= (q-1)/2 on (1,2]. At most 1+sum_i(|G_i|-1) update rounds before success or failure, since each changing round increases an index. Each rational grid point has bit length O(B(1+B/(q-1))). Products and ratios in a round involve at most polynomially many explicit incidences; reduced integer arithmetic is polynomial in these bounds. Compute ceilings by exact comparisons (binary search possible). Thus a deterministic polynomial-time gap-feasibility algorithm for fixed q>1, or polynomial in 1/(q-1) with variable q. Computing w from rational inputs costs polynomial time when exponents/power bit lengths are polynomial, as in R835/R836's explicit grading; arbitrary binary-encoded giant exponents are not claimed polynomial. This is a witness search for fixed grading, bundle partition and cover, not an exact general real feasibility decision.

## 2. Radius-gap completeness and monotone search

Let R1<R2, with the same grading/cover. For each nonempty bundle, its activity polynomial in R has nonnegative coefficients, all monomials of degree >=c_min=min_f c_f>=2. Therefore w_H(R2)>=(R2/R1)^c_min w_H(R1). Any witness at R2 and margin eta is an inflated witness for R1 whenever q<=(R2/R1)^c_min. By section 1 the algorithm produces a rational witness at R1 with the same margin. In particular a constant radius gap and margin give polynomial-time payment generation, removing the need to supply a witness for such a promise. With R1 fixed >1, the R835 enumeration and R834 tail bound then give the same deterministic FPTAS under the inherited oracle assumptions.

To make exact radius search monotone, choose fixed bases a_H=w_H(1) for all R>=1, rather than rephasing the grid with w_H(R). The finite grids and margin are now radius-independent. Any grid witness at R2 remains feasible at every smaller R>=1 because Phi decreases. Section 1 decides this grid existence exactly; bisection on rational radii is legitimate. Success provides a true lower bound on attainable radius; failure at R excludes a real witness at any R2>=R q^(1/c_min) with that margin. It does not certify nominal failure at R. The gray zone is multiplicative and can be made small at polynomial cost in 1/(q-1). A fixed prevalidated upper bracket or the necessary cap w_H<=1-eta gives the search boundary. No claim of global optimum over covers or gradings.

## 3. Exact gray-zone witness and fixed-grid radius experiment

Path with 3 singleton bundles, edge anchors {0,1},{1,2}, w=1/10 uniformly, eta=3/4. Leaf payments equal 1/10; the two middle-label payments equal (1/10)(11/9)=11/90. These form the least real supersolution (each leaf has one anchor, each middle incidence depends on the opposite leaf). Q=(11/10)(101/90)=1111/900<5/4. On base w and q=2, middle payments must round to 1/5, giving Q=33/25>5/4, so no grid witness. On q=9/8, middle payments 81/640 yield Q=7931/6400<5/4. This is a concrete separation between nominal feasibility and coarse-grid feasibility.

Fixed-grid test: on this path let w(R)=R^2/20 and a=1/20, q=9/8, eta=3/4. At each radius in {100/100,...,200/100} use the exact least real witness and the exact least grid witness (round leaves, then middle incidences). 101 radii, 14 grid points per incidence. Last grid success R=142/100; first failure 143/100. Last nominal success R=145/100; first failure 146/100. Verified monotonicity, absence of false witnesses and inflated-activity completeness at every sampled radius. These are grid observations, not exact continuous optimal radii.

## 4. R836 integer rounding: a sharp universal fixed-payment bound

The exponent 2/3 in R836 is optimal in the following scope: for every theta>2/3 there exists a rational singleton-bundle instance with a continuous feasible point at R=2 for which keeping the same analytic payments makes integer feasibility at R'=2^theta impossible.

Proof. Take original dependency graph path 1-0-2; analytic cover is the one anchor {0,1,2} (extra edge allowed). Choose d=1/16 for all three incidences, eta=1/2. Q=(17/16)^3<3/2. Let p_0=1, p_1=1-2^(-m), p_2=2^(-m), ell_v=-log_2 p_v, b_v=d p_v/4. Then every neighborhood Kraft constraint is exact, all b are rational, and b_v 2^(ell_v+2)=d. There are no other anchor ratios, so the continuous certificate holds exactly. Choose m large enough that (1-2^(-m)) 2^(3theta)>4; possible since 3theta>2. If an integer L_1>=1 were used at R', its activity b_1 (R')^(L_1+2)>d. Consequently L_1 must be zero (or even L_1=0 is disallowed), and for any finite integer L_2 the Kraft sum at vertex 0 is at least 1+2^(-L_2)>1. Thus infeasible. The model is realizable with independent edge Bernoulli variables and I_v products, lambda_v=1, alpha_v=b_v; the true dependency graph is exactly the path if edge probabilities are strictly between zero and one. Exact moments have polynomial bit length. This sharpness concerns retaining the given payments; changed payments or cover may succeed. It is not a universal FPTAS limitation.

Exact rational examples R'=8/5,159/100,127/80,158741/100000 (each cube >4) require m=6,8,13,16 respectively, and all checked (1-2^-m)(R')^3>4 and (1-2^-m)(R')^2<=4. These values approach the uniform guarantee from above.

Practical improvement when slack exists: for singleton bundles use R836's exact cap C_f and compute M_f(r)=max{m>=0:b_f r^(m+2)<=C_f} at any rational candidate r. If a cap is empty, reject; otherwise test all neighborhood sums at M. This recovers the exact fixed-payment feasible radii via monotone search, instead of always paying the worst-case 2/3 exponent. For arbitrary bundles, the same test using individual caps b_f R^(ell_f+2) is a sufficient dominance-preserving recovery, not a characterization of all feasible bundle allocations. Retain actual resource slack and original observations.

## 5. Actual checks and next

JavaScript BigInt rational computations: 75 labeled simple graphs n=1..4, three activity configurations each, 16 further overlapping cover/grid configurations, 2 gray-zone tests, total 243 solver instances (44 success, 199 failure), 33,325 exhaustive grid vectors examined (stop on first witness), 119 update rounds total, maximum 3 rounds in this sample, 7 valid inflated witness domination checks, 8 sharpness checks, zero disagreements. Exact fixed-grid experiment: 101 radii, last/first outcomes above. General termination and complexity follow the proof, not these finite round counts. No numerical convex optimizer, native BRC dynamics, full Port realization or production FPTAS benchmark executed.
Next: joint integer grading/payment search without a supplied relaxed witness; investigate bundle-cap allocation and exact Port observer realization. The present result removes payment-search debt for fixed grading and explicit margin/radius gap and shows why a universal fixed-payment rounding exponent cannot improve.

## Reproduction (JavaScript BigInt)
```javascript
function replay(){
 const gcd=(a,b)=>{while(b){[a,b]=[b,a%b]}return a<0n?-a:a};
 const F=(a,b=1n)=>{a=BigInt(a);b=BigInt(b);let g=gcd(a,b);return [a/g,b/g]};
 const add=(a,b)=>F(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
 const sub=(a,b)=>F(a[0]*b[1]-b[0]*a[1],a[1]*b[1]);
 const mul=(a,b)=>F(a[0]*b[0],a[1]*b[1]);
 const div=(a,b)=>F(a[0]*b[1],a[1]*b[0]);
 const le=(a,b)=>a[0]*b[1]<=b[0]*a[1];
 const eq=(a,b)=>le(a,b)&&le(b,a);
 const one=F(1),two=F(2);
 const pow=(a,k)=>F(a[0]**BigInt(k),a[1]**BigInt(k));
 const ok=b=>{if(!b)throw Error("assertion failed")};
 const prod=xs=>xs.reduce(mul,one);
 const make=(A,w,q,eta)=>{
  const I=A.flatMap((hs,a)=>hs.map(h=>({a,h})));
  const byA=A.map((_,a)=>I.map((v,i)=>v.a===a?i:-1).filter(i=>i>=0));
  const byH=w.map((_,h)=>I.map((v,i)=>v.h===h?i:-1).filter(i=>i>=0));
  const cap=sub(one,eta),limit=sub(two,eta);
  const grid=I.map(({h})=>{let xs=[],x=w[h];while(le(x,cap)){xs.push(x);x=mul(x,q)}return xs});
  const Q=(d,a)=>prod(byA[a].map(i=>add(one,d[i])));
  const goodMargin=d=>A.every((_,a)=>le(Q(d,a),limit));
  const phi=(d,i,inflate=one)=>{
   let {a,h}=I[i];
   return mul(mul(w[h],inflate),prod(byH[h].filter(j=>j!==i).map(j=>{
    let T=prod(byA[I[j].a].filter(k=>k!==j).map(k=>add(one,d[k])));
    return div(T,sub(two,T));
   })));
  };
  const valid=(d,inflate=one)=>goodMargin(d)&&I.every((_,i)=>le(phi(d,i,inflate),d[i]));
  return {I,byA,grid,goodMargin,phi,valid,limit};
 };
 function solve(M){
  if(M.grid.some(xs=>!xs.length))return {ok:false,steps:0,why:"BASE_CAP"};
  let k=M.grid.map(()=>0),steps=0;
  for(;;){
   let d=k.map((v,i)=>M.grid[i][v]);
   if(!M.goodMargin(d))return {ok:false,steps,why:"MARGIN",k};
   let next=k.map((v,i)=>{let x=M.phi(d,i),j=v;while(j<M.grid[i].length&&!le(x,M.grid[i][j]))j++;return j});
   steps++;
   if(next.some((v,i)=>v>=M.grid[i].length))return {ok:false,steps,why:"GRID_CAP",k};
   if(next.every((v,i)=>v===k[i])){ok(M.valid(d));return {ok:true,steps,d,k}}
   k=next;
  }
 }
 function brute(M,stats){
  if(M.grid.some(xs=>!xs.length))return false;
  let d=[];
  function visit(i){
   if(i===M.I.length){stats.bruteVectors++;return M.valid(d)}
   for(let x of M.grid[i]){d[i]=x;if(visit(i+1))return true}
   return false;
  }
  return visit(0);
 }
 let stats={graphs:0,instances:0,bruteVectors:0,success:0,failure:0,rounds:0,maxRounds:0,additionalCovers:0,inflatedWitnessChecks:0,sharpnessChecks:0,disagreements:0};
 function check(A,w,q,eta,exhaust=true){
  let M=make(A,w,q,eta),res=solve(M);stats.instances++;stats.rounds+=res.steps;stats.maxRounds=Math.max(stats.maxRounds,res.steps);stats[res.ok?"success":"failure"]++;
  if(exhaust){let b=brute(M,stats);if(b!==res.ok)stats.disagreements++;ok(b===res.ok)}
  if(res.ok)ok(M.valid(res.d));
  return {M,res};
 }
 for(let n=1;n<=4;n++){
  let es=[];for(let i=0;i<n;i++)for(let j=i+1;j<n;j++)es.push([i,j]);
  for(let mask=0;mask<2**es.length;mask++){
   stats.graphs++;let A=es.filter((_,i)=>mask&(1<<i));for(let v=0;v<n;v++)if(!A.some(a=>a.includes(v)))A.push([v]);
   for(let t=0;t<3;t++){let w=Array.from({length:n},(_,v)=>t===0?F(1,4):t===1?F(1,5):F(1,3+(v%3)));check(A,w,F(2),F(1,2))}
  }
 }
 for(let A of [[[0,1,2]],[[0,1,2],[1,2,3]],[[0,1],[1,2],[2,0]],[[0,1],[1,2],[1,3]]]){
  for(let q of [F(2),F(3,2),F(5,4),F(9,8)]){
   let n=1+Math.max(...A.flat()),w=Array.from({length:n},(_,v)=>F(1,16+v));
   let {M,res}=check(A,w,q,F(1,2),false);stats.additionalCovers++;
   let d=M.I.map(()=>F(1,5));if(M.valid(d,q)){stats.inflatedWitnessChecks++;ok(res.ok);ok(res.d.every((x,i)=>le(x,d[i])))}
  }
 }
 let {M,res}=check([[0,1],[1,2]],[F(1,10),F(1,10),F(1,10)],F(2),F(3,4));
 let witness=[F(1,10),F(11,90),F(11,90),F(1,10)];
 ok(M.valid(witness));ok(!res.ok);
 let finer=check([[0,1],[1,2]],[F(1,10),F(1,10),F(1,10)],F(9,8),F(3,4),false);
 ok(finer.res.ok);
 let sharp=[];
 for(let r of [F(8,5),F(159,100),F(127,80),F(158741,100000)]){
  ok(!le(pow(r,3),F(4)));
  let m=1;while(le(mul(sub(one,F(1,2n**BigInt(m))),pow(r,3)),F(4)))m++;
  let p=sub(one,F(1,2n**BigInt(m)));
  ok(!le(mul(p,pow(r,3)),F(4)));
  ok(le(mul(p,pow(r,2)),F(4)));stats.sharpnessChecks+=2;
  sharp.push({radius:r.map(String).join("/"),m});
 }
 return {stats,grayZone:{nominalWitness:witness.map(x=>x.map(String).join("/")),coarse:res.why,fine:finer.res.d.map(x=>x.map(String).join("/"))},sharp};
}
function radiusReplay(){
 const gcd=(a,b)=>{while(b)[a,b]=[b,a%b];return a<0n?-a:a};
 const F=(a,b=1)=>{a=BigInt(a);b=BigInt(b);let g=gcd(a,b);return [a/g,b/g]};
 const mul=(a,b)=>F(a[0]*b[0],a[1]*b[1]),add=(a,b)=>F(a[0]*b[1]+a[1]*b[0],a[1]*b[1]),sub=(a,b)=>F(a[0]*b[1]-a[1]*b[0],a[1]*b[1]),div=(a,b)=>F(a[0]*b[1],a[1]*b[0]),le=(a,b)=>a[0]*b[1]<=b[0]*a[1];
 const one=F(1),q=F(9,8),base=F(1,20),limit=F(5,4),cap=F(1,4);
 let grid=[];for(let x=base;le(x,cap);x=mul(x,q))grid.push(x);
 const round=x=>grid.find(v=>le(x,v));
 let nominalLast=null,gridLast=null,gridFirstFail=null,nominalFirstFail=null,checks=0;
 for(let i=0;i<=100;i++){
  let r=F(100+i,100),w=mul(base,mul(r,r));
  let center=mul(w,div(add(one,w),sub(one,w)));
  let nominal=le(mul(add(one,w),add(one,center)),limit);
  let l=round(w),c=l&&round(mul(w,div(add(one,l),sub(one,l))));
  let feasible=!!(l&&c&&le(mul(add(one,l),add(one,c)),limit));
  if(feasible){if(gridFirstFail!==null)throw Error("not monotone");gridLast=i;if(!nominal)throw Error("false certificate")}
  else if(gridFirstFail===null)gridFirstFail=i;
  if(nominal){if(nominalFirstFail!==null)throw Error("nominal not monotone");nominalLast=i}else if(nominalFirstFail===null)nominalFirstFail=i;
  let wp=mul(q,w),cp=mul(wp,div(add(one,wp),sub(one,wp)));
  if(le(mul(add(one,wp),add(one,cp)),limit)&&!feasible)throw Error("inflated completeness");
  checks++;
 }
 return {checks,gridPoints:grid.length,gridLastNumerator:100+gridLast,gridFirstFailNumerator:100+gridFirstFail,nominalLastNumerator:100+nominalLast,nominalFirstFailNumerator:100+nominalFirstFail,denominator:100};
}
console.log(replay(),radiusReplay());
```
