function replay(){
 let seed=20261128;const rnd=n=>{seed^=seed<<13;seed^=seed>>>17;seed^=seed<<5;return(seed>>>0)%n};
 const stats={seed:20261128,models:0,bruteSubsets:0,budgets:0,witnessChecks:0,initialRankChecks:0,generatedRankChecks:0,batchRankChecks:0,batchFeasibilityChecks:0,batchInfeasible:0,batchVectors:0,batchMultiClassVectors:0,stages:0,generated:0,states:0,peak:0,comparisons:0,rankEntries:0,initialEntries:0,initialIndependenceCalls:0,transitionMinima:0,stageSupportEntries:0,maxClasses:0,maxInitialEntries:0,modelsWithAtMost4Classes:0,lowClassRankEntries:0,lowClassSupportEntries:0,disagreements:0};
 const ck=(p,m)=>{if(!p)throw Error(m)},sub=(a,b)=>(a&b)===a;
 for(let it=0;it<350;it++){
  let n=2+rnd(6),m=5+rnd(8),c=Array.from({length:n},()=>1+rnd(4)),N=1<<n,M=1<<m,A=[];
  for(let j=0;j<m;j++){let aux=rnd(3)===0;A.push({e:aux?1<<rnd(n):1+rnd(N-1),p:aux?0:1+rnd(15),s:aux?1+rnd(9):0})}
  for(let x of A)if(x.s)c[Math.log2(x.e)]++;
  const cc=Array.from({length:N},(_,v)=>c.reduce((s,a,i)=>s+((v>>i&1)*a),0)),pop=new Uint8Array(M),contained=Array(N).fill(0);
  for(let z=1;z<M;z++)pop[z]=pop[z>>1]+(z&1);
  for(let v=0;v<N;v++)for(let j=0;j<m;j++)if(sub(A[j].e,v))contained[v]|=1<<j;
  const independent=z=>cc.every((cv,v)=>!v||pop[z&contained[v]]<cv);
  const gs=new Map();for(let j=0;j<m;j++)gs.set(A[j].e,(gs.get(A[j].e)||0)|(1<<j));
  const groups=[...gs.values()],supports=[...gs.keys()],k=groups.length, L=1<<k, unions=new Uint16Array(L),rank=new Uint8Array(M),ok=new Uint8Array(M),P=new Uint16Array(M),S=new Uint16Array(M);
  stats.models++;stats.maxClasses=Math.max(stats.maxClasses,k);stats.maxInitialEntries=Math.max(stats.maxInitialEntries,L-1);if(k<=4)stats.modelsWithAtMost4Classes++;
  // Independent brute rank reference: exhaust every labeled subset, then subset rank recurrence.
  for(let z=0;z<M;z++){stats.bruteSubsets++;ok[z]=+independent(z);if(z){let y=z&-z,j=31-Math.clz32(y);P[z]=P[z^y]+A[j].p;S[z]=S[z^y]+A[j].s}if(ok[z])rank[z]=pop[z];else for(let q=z;q;q&=q-1)rank[z]=Math.max(rank[z],rank[z^(q&-q)])}
  // Initial full-class rank table built using greedy extension of a cached basis of J minus its highest bit.
  const base=new Uint16Array(L),rho=new Uint8Array(L);
  for(let J=1;J<L;J++){let i=31-Math.clz32(J),J0=J^(1<<i);unions[J]=unions[J0]|groups[i];let B=base[J0];for(let q=groups[i];q;q&=q-1){let y=q&-q;stats.initialIndependenceCalls++;if(independent(B|y))B|=y}base[J]=B;rho[J]=pop[B];stats.initialRankChecks++;ck(rho[J]===rank[unions[J]],"initial rank")}
  stats.initialEntries+=L-1;
  // Multi-class corner formula for a batch of the first min(3,k) classes, every count vector, every union of remaining full classes.
  // For k>=2 this tests at least two classes, including all infeasible vectors.
  const h=Math.min(3,k),H=1<<h,chosen=new Uint8Array(h);
  function checkBatch(i,R){
   if(i<h){let b=0,t=0;for(;;){chosen[i]=t;checkBatch(i+1,R|b);if(t===pop[groups[i]])break;let q=groups[i]&~b;b|=q&-q;t++}return}
   stats.batchVectors++;if(chosen.filter(x=>x>0).length>=2)stats.batchMultiClassVectors++;
   let ts=new Uint8Array(H);for(let J=1;J<H;J++){let y=J&-J;ts[J]=ts[J^y]+chosen[31-Math.clz32(y)]}
   const legal=ts.every((v,J)=>v<=rho[J]);stats.batchFeasibilityChecks++;ck(legal===!!ok[R],"batch feasibility");
   if(!legal){stats.batchInfeasible++;return}
   for(let K=0;K<(1<<(k-h));K++){let Q=K<<h,best=Infinity;for(let J=0;J<H;J++)best=Math.min(best,rho[Q|J]-ts[J]);stats.batchRankChecks++;ck(best===rank[unions[Q]|R]-pop[R],"batch rank")}
  }
  checkBatch(0,0);
  // All-budget DP: only rank values and actual objective witness, no transition basis or greedy rank oracle.
  function options(H){let real=[],aux=[];for(let j=0;j<m;j++)if(H>>j&1)(A[j].s?aux:real).push(j);real.sort((i,j)=>A[j].p-A[i].p||i-j);aux.sort((i,j)=>A[j].s-A[i].s||i-j);const pre=ls=>{let v=[0];for(let j of ls)v.push(v[v.length-1]|(1<<j));return v};let out=[];for(let r of pre(real))for(let a of pre(aux)){let z=r|a;out.push({z,t:pop[z],p:P[z],s:S[z]})}return out}
  let states=[{v:rho,p:0,s:0,z:0}];
  for(let i=0;i<k;i++){
   let l=1<<(k-i-1),opts=options(groups[i]),map=new Map(),closure=new Set([0]);
   for(let j=i+1;j<k;j++)for(let w of [...closure])closure.add(w|supports[j]);
   for(let a of states){let byT=new Map();for(let o of opts)if(o.t<=a.v[1]){
    let v=byT.get(o.t);if(!v){v=new Uint8Array(l);for(let J=0;J<l;J++){v[J]=Math.min(a.v[2*J],a.v[2*J+1]-o.t);stats.transitionMinima++}byT.set(o.t,v)}
    let z=a.z|o.z;ck(ok[z],"transition legal");
    for(let J=0;J<l;J++){stats.generatedRankChecks++;ck(v[J]===rank[z|unions[J<<(i+1)]]-pop[z],"child union rank")}
    stats.generated++;let key=v.join(",")+"|"+(a.s+o.s),old=map.get(key),p=a.p+o.p,s=a.s+o.s;if(!old||p>old.p)map.set(key,{v,p,s,z})
   }}
   let keep=[];for(let a of [...map.values()].sort((a,b)=>b.p-a.p||b.s-a.s)){let dominated=false;for(let q of keep){if(q.s<a.s||q.p<a.p)continue;stats.comparisons++;if(q.v.every((x,j)=>x>=a.v[j])){dominated=true;break}}if(!dominated)keep.push(a)}
   states=keep;stats.stages++;stats.states+=states.length;stats.peak=Math.max(stats.peak,states.length);stats.rankEntries+=states.length*(l-1);stats.stageSupportEntries+=states.length*(closure.size-1);if(k<=4){stats.lowClassRankEntries+=states.length*(l-1);stats.lowClassSupportEntries+=states.length*(closure.size-1)}
  }
  const D=S[M-1],best=Array(D+1).fill(-1);for(let z=0;z<M;z++)if(ok[z])best[D-S[z]]=Math.max(best[D-S[z]],P[z]);for(let j=1;j<=D;j++)best[j]=Math.max(best[j],best[j-1]);
  for(let j=0;j<=D;j++){stats.budgets++;let win=states.find(x=>D-x.s<=j);ck(win&&win.p===best[j],"optimum");ck(ok[win.z]&&P[win.z]===win.p&&S[win.z]===win.s&&D-win.s<=j,"witness");stats.witnessChecks++}
 }
 return stats
}
console.log(JSON.stringify(replay(),null,2));
