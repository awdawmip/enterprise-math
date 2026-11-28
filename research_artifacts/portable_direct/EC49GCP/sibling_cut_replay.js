function replay(){
  let seed=20261128;
  const rnd=n=>{seed^=seed<<13;seed^=seed>>>17;seed^=seed<<5;return(seed>>>0)%n};
  const check=(p,m)=>{if(!p)throw Error(m)};
  const sub=(a,b)=>(a&b)===a;
  const sum=a=>a.reduce((s,x)=>s+x,0);
  const models=[];
  for(let it=0;it<350;it++){
    let n=2+rnd(6),m=5+rnd(8),c=Array.from({length:n},()=>1+rnd(4)),N=1<<n,M=1<<m,A=[];
    for(let j=0;j<m;j++){let aux=rnd(3)===0;A.push({e:aux?1<<rnd(n):1+rnd(N-1),p:aux?0:1+rnd(15),s:aux?1+rnd(9):0})}
    for(let x of A)if(x.s)c[Math.log2(x.e)]++;
    models.push({n,m,c,N,M,A});
  }
  const stats={seed:20261128,models:350,originalSubsets:0,legalSiblingPairs:0,rejectedPairs:0,rootQueries:0,cacheZeroLoss:0,tightLocalReuse:0,tightRepair:0,strictLocalRepair:0,fullFallback:0,flowCallsOld:0,flowCallsNew:0,baselineNewPorts:0,actualNewPorts:0,intervalChecks:0,slackOnlyFalse:0,sameInsideCounts:0,strictBound:0};
  let counterexample=null;
  function flow(c,E,v,root,limit){
    const ps=c.map((_,p)=>p).filter(p=>limit&(1<<p)),js=E.map((_,j)=>j).filter(j=>v[j]&&sub(E[j],limit)),k=js.length,n=ps.length,s=k+n,t=s+1,g=Array.from({length:t+1},()=>[]);
    const INF=1+sum(ps.map(p=>c[p]))+sum(js.map(j=>v[j]));
    function edge(a,b,w){g[a].push({to:b,rev:g[b].length,w});g[b].push({to:a,rev:g[a].length-1,w:0})}
    for(let a=0;a<k;a++){edge(s,a,v[js[a]]);for(let b=0;b<n;b++)if(E[js[a]]&(1<<ps[b]))edge(a,k+b,INF)}
    for(let b=0;b<n;b++){edge(k+b,t,c[ps[b]]);if(root&(1<<ps[b]))edge(s,k+b,INF)}
    let f=0,seen;
    while(true){
      let prev=Array(t+1).fill(-1),idx=Array(t+1).fill(-1),q=[s];prev[s]=s;
      for(let a=0;a<q.length&&prev[t]<0;a++){let u=q[a];for(let j=0;j<g[u].length;j++){let e=g[u][j];if(e.w>0&&prev[e.to]<0){prev[e.to]=u;idx[e.to]=j;q.push(e.to)}}}
      if(prev[t]<0){seen=prev;break}
      let d=INF;for(let u=t;u!==s;u=prev[u])d=Math.min(d,g[prev[u]][idx[u]].w);
      for(let u=t;u!==s;u=prev[u]){let e=g[prev[u]][idx[u]];e.w-=d;g[u][e.rev].w+=d}
      f+=d;
    }
    return {U:ps.reduce((a,p,b)=>a|(seen[k+b]>=0?1<<p:0),0),slack:f-sum(js.map(j=>v[j])),ports:n};
  }
  for(let {n,m,c,N,M,A} of models){
    const pop=new Uint8Array(M),cap=new Int16Array(N),L=new Int32Array(N);
    for(let z=1;z<M;z++)pop[z]=pop[z>>1]+(z&1);
    for(let u=1;u<N;u++){for(let p=0;p<n;p++)if(u&(1<<p))cap[u]+=c[p];for(let j=0;j<m;j++)if(sub(A[j].e,u))L[u]|=1<<j}
    const ok=new Uint8Array(M);
    for(let z=0;z<M;z++){ok[z]=1;for(let u=1;u<N;u++)if(pop[z&L[u]]>=cap[u]){ok[z]=0;break}stats.originalSubsets++}
    let groups=new Map();for(let j=0;j<m;j++)groups.set(A[j].e,(groups.get(A[j].e)||0)|(1<<j));
    const E=[...groups.keys()],H=[...groups.values()],vec=z=>H.map(h=>pop[h&z]);
    const slack=(v,u)=>cap[u]-sum(v.map((a,j)=>sub(E[j],u)?a:0));
    function direct(v,root,limit=N-1){
      let a=Infinity,U=limit;
      for(let u=1;u<N;u++)if(sub(root,u)&&sub(u,limit)){let b=slack(v,u);if(b<a){a=b;U=u}else if(b===a)U&=u}
      return {U,slack:a};
    }
    function verify(v,w,root){
      const old=flow(c,E,v,root,N-1),ref0=direct(v,root),ref=direct(w,root);
      check(old.U===ref0.U&&old.slack===ref0.slack,"old flow");
      stats.flowCallsOld++;stats.rootQueries++;stats.baselineNewPorts+=n;
      const U=old.U,h=slack(w,U),d=w.map((a,j)=>a-v[j]);
      let outside=0,inside=0,unchanged=true;
      for(let j=0;j<E.length;j++){
        if(sub(E[j],U)){if(d[j])unchanged=false;if(d[j]<0&&!sub(E[j],root))inside-=d[j]}
        else if(d[j]>0)outside+=d[j];
      }
      let B=outside+inside;
      check(Math.max(1,h-B)<=ref.slack&&ref.slack<=h,"slack sandwich");stats.intervalChecks++;
      if(B>0&&Math.max(1,h-B)>1)stats.strictBound++;
      if(unchanged)stats.sameInsideCounts++;
      if(h===old.slack&&ref.U!==U){stats.slackOnlyFalse++;if(!counterexample)counterexample={c,E,v,w,root,old:{U,slack:old.slack},new:ref};}
      let got;
      if(B===0){got={U,slack:h};stats.cacheZeroLoss++}
      else if(h===1&&inside===0){got={U,slack:1};stats.tightLocalReuse++}
      else if(h===1){got=flow(c,E,w,root,U);stats.tightRepair++;stats.flowCallsNew++;stats.actualNewPorts+=got.ports;if(U!==N-1)stats.strictLocalRepair++}
      else {got=flow(c,E,w,root,N-1);stats.fullFallback++;stats.flowCallsNew++;stats.actualNewPorts+=got.ports}
      check(got.U===ref.U&&got.slack===ref.slack,"sibling transition mismatch");
      if(h===1){const loc=direct(w,root,U);check(loc.U===ref.U&&loc.slack===1,"tight localization")}
    }
    for(let tr=0;tr<8;tr++){
      let P=rnd(M),F=(M-1)^P,R=rnd(M)&P,R2=rnd(M)&P;
      if(!ok[R]||!ok[R2]){stats.rejectedPairs++;continue}
      stats.legalSiblingPairs++;
      let v=vec(R),w=vec(R2),mm=vec(F);
      for(let j=0;j<E.length;j++)if(mm[j]){verify(v,w,E[j]);verify(w,v,E[j])}
    }
  }
  // Explicit two-port counterexample: same old cut slack, changed least rooted tight cut.
  const ex={c:[2,1],E:[1,3],v:[0,2],w:[1,1],root:1};
  const a=flow(ex.c,ex.E,ex.v,1,3),b=flow(ex.c,ex.E,ex.w,1,3);
  check(a.U===3&&b.U===1&&a.slack===1&&b.slack===1,"explicit counterexample");
  return {stats,firstSameSlackCounterexample:counterexample,explicitCounterexample:{...ex,old:a,new:b},mismatches:0};
}
console.log(JSON.stringify(replay(),null,2));
