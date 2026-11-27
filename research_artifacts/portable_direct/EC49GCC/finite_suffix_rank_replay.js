function replay(){
 let seed=20261128;const rnd=n=>{seed^=seed<<13;seed^=seed>>>17;seed^=seed<<5;return(seed>>>0)%n};
 const stats={seed:20261128,models:0,budgets:0,bruteSubsets:0,baselineStates:0,finiteStates:0,baselineGenerated:0,finiteGenerated:0,baselineComparisons:0,finiteComparisons:0,baselineCoordinateTests:0,finiteCoordinateTests:0,baselineEntries:0,finiteEntries:0,finiteRankCalls:0,finiteIndependenceCoordinateTests:0,finiteExtraDominance:0,finiteExtraEqualMerge:0,rankSampleChecks:0,witnessChecks:0,peakBaseline:0,peakFinite:0,disagreements:0};
 const check=(p,m)=>{if(!p){stats.disagreements++;throw Error(m)}};
 const sub=(a,b)=>(a&b)===a;
 for(let it=0;it<350;it++){
  let n=2+rnd(6),m=5+rnd(8),c=Array.from({length:n},()=>1+rnd(4)),N=1<<n,M=1<<m,A=[];
  for(let j=0;j<m;j++){let aux=rnd(3)===0;A.push({e:aux?1<<rnd(n):1+rnd(N-1),p:aux?0:1+rnd(15),s:aux?1+rnd(9):0})}
  for(let x of A)if(x.s)c[Math.log2(x.e)]++;
  let cc=Array.from({length:N},(_,v)=>c.reduce((s,a,i)=>s+((v>>i&1)*a),0)),pop=new Uint8Array(M),contained=Array(N).fill(0);
  for(let z=1;z<M;z++)pop[z]=pop[z>>1]+(z&1);
  for(let v=0;v<N;v++)for(let j=0;j<m;j++)if(sub(A[j].e,v))contained[v]|=1<<j;
  const independent=z=>cc.every((cv,v)=>!v||pop[z&contained[v]]<cv);
  function h(z){let a=cc.map((cv,v)=>cv-pop[z&contained[v]]);for(let bit=1;bit<N;bit*=2)for(let v=0;v<N;v++)if(!(v&bit))a[v]=Math.min(a[v],a[v|bit]);return a}
  const B=Array(m+1).fill(0),stages=[];
  for(let j=m-1;j>=0;j--)B[j]=B[j+1]|A[j].e;
  for(let j=0;j<=m;j++){
   let suffix=(M-1)^((1<<j)-1),unions=new Set([0]);
   for(let t=j;t<m;t++)for(let w of [...unions])unions.add(w|A[t].e);
   let w=[...unions].sort((a,b)=>a-b).filter(x=>x!==0),f=w.map(x=>contained[x]&suffix);
   stages.push({w,f,suffix});
  }
  const rankDirect=(z,Q)=>{let I=z,k=0;for(let q=Q;q;q&=q-1){let bit=q&-q;if(independent(I|bit)){I|=bit;k++}}return k};
  const denseDom=(s,t,b)=>{for(let u=b;;u=(u-1)&b){stats.baselineCoordinateTests++;if(s.v[u]<t.v[u])return false;if(!u)break}return true};
  const actualDenseDom=(s,t,b)=>{let hs=h(s.mask),ht=h(t.mask);for(let u=b;;u=(u-1)&b){if(hs[u]<ht[u])return false;if(!u)break}return true};
  function dp(finite){
   let states=[{v:finite?stages[0].f.map(Q=>rankDirect(0,Q)):cc,p:0,s:0,mask:0}];
   for(let j=0;j<m;j++){
    let x=A[j],b=B[j+1],bit=1<<j,old=stages[j],next=stages[j+1],map=new Map();
    for(let a of states){
     let skip,take=null;
     if(finite){
      const cache=new Map();
      function feasible(Q){for(let i=0;i<old.f.length;i++){stats.finiteIndependenceCoordinateTests++;if(pop[Q&old.f[i]]>a.v[i])return false}return true}
      function rank(Q){if(cache.has(Q))return cache.get(Q);stats.finiteRankCalls++;let I=0;for(let q=Q;q;q&=q-1){let y=q&-q;if(feasible(I|y))I|=y}let r=pop[I];cache.set(Q,r);return r}
      const prior=next.w.map(w=>old.w.indexOf(w));
      skip={...a,v:next.f.map((Q,i)=>(old.f[prior[i]]&bit)?rank(Q):a.v[prior[i]])};
      if(feasible(bit))take={v:next.f.map((Q,i)=>(old.f[prior[i]]&bit)?a.v[prior[i]]-1:rank(Q|bit)-1),p:a.p+x.p,s:a.s+x.s,mask:a.mask|bit};
     }else{
      skip={...a,v:a.v.map((v,u)=>sub(u,b)?v:-1)};
      if(a.v[x.e]>=2)take={v:a.v.map((v,u)=>!sub(u,b)?-1:u===0?0:Math.min(v,a.v[u|x.e]-1)),p:a.p+x.p,s:a.s+x.s,mask:a.mask|bit};
     }
     for(let z of take?[skip,take]:[skip]){
      stats[finite?"finiteGenerated":"baselineGenerated"]++;
      let key=z.v.join(",")+"|"+z.s,prev=map.get(key);
      if(finite&&prev&&(!actualDenseDom(z,prev,b)||!actualDenseDom(prev,z,b)))stats.finiteExtraEqualMerge++;
      if(!prev||z.p>prev.p)map.set(key,z);
     }
    }
    let vals=[...map.values()].sort((a,b)=>b.p-a.p||b.s-a.s),keep=[];
    for(let a of vals){let dominated=false;for(let q of keep){if(q.s<a.s||q.p<a.p)continue;stats[finite?"finiteComparisons":"baselineComparisons"]++;let ok;
      if(finite){ok=true;for(let i=0;i<a.v.length;i++){stats.finiteCoordinateTests++;if(q.v[i]<a.v[i]){ok=false;break}}}else ok=denseDom(q,a,b);
      if(ok){if(finite&&!actualDenseDom(q,a,b))stats.finiteExtraDominance++;dominated=true;break}
     }if(!dominated)keep.push(a)}
    states=keep;stats[finite?"finiteStates":"baselineStates"]+=states.length;
    stats[finite?"finiteEntries":"baselineEntries"]+=states.length*(finite?next.f.length:2**b.toString(2).replace(/0/g,"").length);
    let peak=finite?"peakFinite":"peakBaseline";stats[peak]=Math.max(stats[peak],states.length);
    if(finite&&states.length){for(let a of [states[0],states[states.length-1]])for(let i=0;i<next.f.length;i++){stats.rankSampleChecks++;check(a.v[i]===rankDirect(a.mask,next.f[i]),"rank transition")}}
   }return states;
  }
  let D=A.reduce((s,x)=>s+x.s,0),best=Array(D+1).fill(-1);
  function value(z){let p=0,s=0;for(let j=0;j<m;j++)if(z>>j&1){p+=A[j].p;s+=A[j].s}return {p,s}}
  for(let z=0;z<M;z++){stats.bruteSubsets++;if(!independent(z))continue;let {p,s}=value(z);best[D-s]=Math.max(best[D-s],p)}
  for(let k=1;k<=D;k++)best[k]=Math.max(best[k],best[k-1]);
  let a=dp(false),q=dp(true);
  for(let k=0;k<=D;k++){stats.budgets++;for(let states of [a,q]){let winner=states.find(x=>D-x.s<=k);check(winner&&winner.p===best[k],"budget optimum");let v=value(winner.mask);check(independent(winner.mask)&&v.p===winner.p&&v.s===winner.s&&D-v.s<=k,"label witness");stats.witnessChecks++}}
  stats.models++;
 }return stats;
}
console.log(JSON.stringify(replay(),null,2));
