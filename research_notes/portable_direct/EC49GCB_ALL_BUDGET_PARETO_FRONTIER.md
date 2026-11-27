# EC49GCB — All-budget Pareto frontier and monotone cube dominance

Status: AUTHOR_PROVED / EXACT_FINITE_SYNTHETIC_BRUTE_REPLAY / NOT_REVIEWED.
Predecessor: 5d8263ad3db45ce395fb0d5ca51f7c1fdb7129a4:research_notes/portable_direct/EC49GCA_MONOTONE_RESIDUAL_THRESHOLD.md (blob 401d902d74e9abead3390272ef13925e636d2986, actually fetched). Frozen identifier BRC16943 unchanged; no raw archive replay. Auxiliary finite labeled strict-Hall model, not a typed native physical computation. No P000 change.

## 1. All-budget optimization and cross-count dominance

Let X and D be real and auxiliary labels in the GBU capacity-lift strict-Hall matroid with positive integer capacities and nonempty supports. Actual label x has nonnegative value p_x and zero savings, auxiliary e has zero value and nonnegative integer savings a_e (avoided release cost). For selected independent prefix S, record p(S), s(S)=sum_{e in S cap D} a_e, and h_S restricted to the union B of all unprocessed supports, with h_S(empty)=0. The total release cost at completion is a(D)-s. Compare states at the SAME prefix: if p(S)>=p(T), s(S)>=s(T), and h_S(U)>=h_T(U) for every U subset B, discard T for the observer consisting of maximum retained value for each budget and one attaining label witness. By GBX insertion equivalence every suffix Q feasible from T is feasible from S, and both value and savings are additive with identical suffix increments. Hence every completed solution through T is weakly dominated by a completed solution through S at every budget. This holds regardless of the two selected counts and without a common extending basis; no per-budget Lagrange parameter or prefix-count coordinate is needed in this unpruned-by-deficit DP. If GBW count constraints are additionally imposed, arbitrary cross-count pruning is not justified; a sufficient extra condition is |S|>=|T| for future lower bounds on selected count, and any other retained constraints must be checked. This is dominance for maximum value and a witness, not equality of all optimal label sets nor arbitrary future deletion/identity observations. Keep raw original inputs. For a fixed restricted insertion-only interface, future feasibility is complete by GBX.

Process each labeled item once in any fixed order, branch skip/take. Take if h(E)>=2; for nonempty U in the new boundary update h(U)=min(h(U),h(U union E)-1); h(empty)=0. Restrict on skip. Merge identical h and savings by retaining highest value; keep a selected-label witness. Then optionally delete Pareto-dominated states. At completion B=empty, sort remaining pairs by savings, retain nondominated value/savings pairs. For every integer or real B>=0, F(B)=max p over s>=a(D)-B. Inductively each discarded state has a surviving state with an equally good continuation, because dominance is transitive and suffix extension preserves order of rewards and the feasibility implication. Thus a single DP returns every budget's exact maximum plus one attaining original labeled subset. For nonnegative costs, the empty actual selection and all auxiliary labels is feasible under GBU, so all nonnegative budgets have a solution. No polynomial bound on states is claimed (GBX and GBV obstructions remain).

## 2. Monotone cube comparator (alternative to explicit antichains/SAT)

At a common prefix A, take an arbitrary basis J. By GCA, delta_S=h_S-h_J and delta_T=h_T-h_J are monotone on subsets of B even for different extending bases. For any Boolean interval [L,H]={U:L subset U subset H}, delta_S(L)>=delta_T(H) proves dominance throughout that interval, whereas delta_S(H)<delta_T(L) proves failure throughout, with L a witness. Otherwise split on any bit in H minus L into the disjoint intervals [L,H minus bit] and [L plus bit,H]. When L=H one exact comparison decides. Recursive cover of [empty,B] therefore decides dominance without materializing the minimal trigger antichains. Each visited cube uses at most four delta queries; a positive proof can be checked by the endpoint inequalities and binary partition; negative by one failing coordinate. Worst case still exponential (at most 2^(b+1)-1 binary nodes); this is an alternative certificate language, not a polynomial guarantee. A cheap full-boundary and singleton failure screen precedes recursion. Dense cached h is used in this replay, not max-flow. No measured flow/runtime acceleration or frozen archive result claimed. Equal h states can bypass the comparator entirely. For a reference basis, use ordinary strict-Hall greedy insertion.

## 3. Actual replay

350 deterministic synthetic models, 2..7 ports, 5..12 labeled items; integer capacities 1..4 before auxiliary boosts, independent singleton auxiliary labels; positive integer values and release costs. Reference enumerates every subset, checks all strict-Hall inequalities, then derives all integer budget maxima. Baseline DP merges identical h and savings only. New DP applies the cross-count Pareto comparison to the same generated inputs; both recover actual mask witnesses independently checked against original inequalities, value and budget. Exact cube comparisons checked against dense coordinate comparisons. Counts are operation/entry counts, not byte or time measurements. Witness masks suffice for small replay; larger implementation should use persistent parent nodes. Output:

```json
{
  "seed": 20261128,
  "models": 350,
  "budgets": 5096,
  "bruteSubsets": 376960,
  "bruteFeasible": 317864,
  "baselineStates": 71681,
  "paretoStates": 40618,
  "baselineGenerated": 136460,
  "paretoGenerated": 79761,
  "dominanceTests": 1090270,
  "dominanceSuccess": 7669,
  "crossCountPrunes": 2366,
  "cubeNodes": 1896642,
  "cubeQueries": 5860956,
  "denseComparatorChecks": 47981252,
  "peakBaseline": 992,
  "peakPareto": 640,
  "witnessChecks": 10192,
  "disagreements": 0
}
```

Replay code (executed in JS):
```javascript
function replay(){
 let seed=20261128;const rnd=n=>{seed^=seed<<13;seed^=seed>>>17;seed^=seed<<5;return(seed>>>0)%n};
 const stats={seed:20261128,models:0,budgets:0,bruteSubsets:0,bruteFeasible:0,baselineStates:0,paretoStates:0,baselineGenerated:0,paretoGenerated:0,dominanceTests:0,dominanceSuccess:0,crossCountPrunes:0,cubeNodes:0,cubeQueries:0,denseComparatorChecks:0,peakBaseline:0,peakPareto:0,witnessChecks:0,disagreements:0};
 const chk=(p,m)=>{if(!p){stats.disagreements++;throw Error(m)}};
 const sub=(a,b)=>(a&b)===a,pop=a=>{let k=0;while(a){a&=a-1;k++}return k};
 const masks=(c)=>Array.from({length:1<<c.length},(_,v)=>c.reduce((s,a,i)=>s+((v>>i&1)*a),0));
 const count=(A,v)=>A.reduce((s,x)=>s+Number(sub(x.e,v)),0);
 const independent=(cc,A)=>cc.every((c,v)=>!v||count(A,v)<c);
 function h(cc,A){let a=cc.map((c,v)=>c-count(A,v));for(let bit=1;bit<a.length;bit*=2)for(let v=0;v<a.length;v++)if(!(v&bit))a[v]=Math.min(a[v],a[v|bit]);return a}
 function compare(s,t,B,ref){
  stats.dominanceTests++;let got=true;
  const ds=u=>{stats.cubeQueries++;return s.h[u]-ref[u]},dt=u=>{stats.cubeQueries++;return t.h[u]-ref[u]};
  // A Boolean cube [l,u] is safe if the minimum delta_s exceeds the maximum delta_t.
  function walk(l,u){stats.cubeNodes++;if(ds(l)>=dt(u))return true;if(ds(u)<dt(l))return false;if(l===u)return false;let bit=(l^u)&-(l^u);return walk(l,u^bit)&&walk(l|bit,u)}
  // cheap endpoint rejection before recursive monotone cover
  if(s.h[B]<t.h[B])got=false;else{for(let b=1;b<=B;b*=2)if((B&b)&&s.h[b]<t.h[b]){got=false;break}if(got)got=walk(0,B)}
  let expected=true;for(let u=B;;u=(u-1)&B){stats.denseComparatorChecks++;if(s.h[u]<t.h[u])expected=false;if(!u)break}
  chk(got===expected,"cube comparator");if(got)stats.dominanceSuccess++;return got
 }
 function dp(cc,A,pareto){
  let N=cc.length, m=A.length, B=Array(m+1).fill(0);for(let j=m-1;j>=0;j--)B[j]=B[j+1]|A[j].e;
  let start={h:cc,p:0,s:0,mask:0,n:0}, states=[start],J=[];
  for(let j=0;j<m;j++){
   let x=A[j],b=B[j+1];if(independent(cc,[...J,x]))J.push(x);let ref=h(cc,J), candidates=[];
   for(let a of states){
    let skip={...a,h:a.h.map((v,u)=>sub(u,b)?v:-1)};candidates.push(skip);
    if(a.h[x.e]>=2){let q=a.h.map((v,u)=>!sub(u,b)?-1:u===0?0:Math.min(v,a.h[u|x.e]-1));candidates.push({h:q,p:a.p+x.p,s:a.s+x.s,mask:a.mask|(1<<j),n:a.n+1})}
   }
   stats[pareto?"paretoGenerated":"baselineGenerated"]+=candidates.length;
   let map=new Map();
   for(let a of candidates){let key=a.h.join(",")+"|"+a.s;let old=map.get(key);if(!old||a.p>old.p)map.set(key,a)}
   let vals=[...map.values()];
   if(pareto){vals.sort((a,b)=>b.p-a.p||b.s-a.s);let keep=[];for(let a of vals){let dominated=false;for(let q of keep){if(q.s>=a.s&&q.p>=a.p&&compare(q,a,b,ref)){if(q.n!==a.n)stats.crossCountPrunes++;dominated=true;break}}if(!dominated)keep.push(a)}vals=keep}
   states=vals;stats[pareto?"paretoStates":"baselineStates"]+=states.length;let peak=pareto?"peakPareto":"peakBaseline";stats[peak]=Math.max(stats[peak],states.length)
  }
  return states
 }
 for(let it=0;it<350;it++){
  let n=2+rnd(6),m=5+rnd(8),c=Array.from({length:n},()=>1+rnd(4)),cc=masks(c),A=[];
  for(let j=0;j<m;j++){let aux=rnd(3)===0;A.push({e:aux?1<<rnd(n):1+rnd(cc.length-1),p:aux?0:1+rnd(15),s:aux?1+rnd(9):0})}
  // Auxiliary labels must be independent. Increase their port capacity as in GBU (base >=1).
  for(let x of A)if(x.s)c[Math.log2(x.e)]++;cc=masks(c);
  let D=A.reduce((s,x)=>s+x.s,0),best=Array(D+1).fill(-1);
  for(let z=0;z<(1<<m);z++){stats.bruteSubsets++;let S=A.filter((x,j)=>z&(1<<j));if(!independent(cc,S))continue;stats.bruteFeasible++;let s=S.reduce((v,x)=>v+x.s,0),p=S.reduce((v,x)=>v+x.p,0);best[D-s]=Math.max(best[D-s],p)}
  for(let b=1;b<=D;b++)best[b]=Math.max(best[b],best[b-1]);
  let a=dp(cc,A,false),q=dp(cc,A,true);
  for(let b=0;b<=D;b++){stats.budgets++;for(let states of [a,q]){let winner=states.filter(x=>D-x.s<=b).sort((x,y)=>y.p-x.p)[0];chk(winner&&winner.p===best[b],"budget optimum");let S=A.filter((x,j)=>winner.mask&(1<<j));chk(independent(cc,S)&&S.reduce((v,x)=>v+x.p,0)===winner.p&&S.reduce((v,x)=>v+x.s,0)===winner.s&&D-winner.s<=b,"witness");stats.witnessChecks++}}
  stats.models++
 }
 return stats
}
console.log(JSON.stringify(replay()));
```

## 4. Continuation and provenance

Current exact control receipt r4-20261128-0432-ec49as-read SUCCEEDED, Source f712aea5da8337ccb84e0b1dd50ffe0ce8412e9b, RS-EC49AS NO_CANONICAL_PUBLICATION_DIRECTORY; owner projection not evaluated, no shared execution authority. Existing identity unconfirmed; historical predecessor EM-DIRECT-23537B is provenance only. No new session, CLAIM, task or promotion. Activity association pending. Global entry blobs 25ae05640c7920104820dba91a1df5e9fafca25e and 108cd58e0458070b5f1a8171d2f66c8c3d0aa613 read at main and matched immutable 095a8ee4c2f40a878574023e320dccfc3108815a. P000 V4/V5, ACTIVE worldview and joint preservation and applicable portable/control protocols read. No raw BRC16943 replay, no physical root progress; inherited GBT historical 1991 feasible,68 excluded,334 other, next root 2046, M14 in [25,27].
Next: integrate lazy cut-network h queries instead of dense arrays; compare actual time, memory and witness costs with GBY/GBW and test identical frozen inputs when available. Assess the worst-case cube certificate and when shared-base GBZ can shortcut it. Preserve original labels and observer scope; this is a candidate optimization tool not an admitted native result.
