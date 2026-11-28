function replay(){
 const check=(p,m)=>{if(!p)throw Error(m)},sub=(a,b)=>(a&b)===a,sum=a=>a.reduce((s,x)=>s+x,0);
 let seed=20261128;const rnd=n=>{seed^=seed<<13;seed^=seed>>>17;seed^=seed<<5;return(seed>>>0)%n};
 const models=[];
 for(let it=0;it<350;it++){
  let n=2+rnd(6),m=5+rnd(8),c=Array.from({length:n},()=>1+rnd(4)),N=1<<n,M=1<<m,A=[];
  for(let j=0;j<m;j++){let aux=rnd(3)===0;A.push({e:aux?1<<rnd(n):1+rnd(N-1),p:aux?0:1+rnd(15),s:aux?1+rnd(9):0})}
  for(let x of A)if(x.s)c[Math.log2(x.e)]++;
  models.push({n,m,c,N,M,A});
 }
 const stats={models:350,seed:20261128,originalSubsets:0,legalSiblingPairs:0,rejectedPairs:0,queries:0,gcpReuse:0,gcpLocal:0,gcpFull:0,coldAugmentsAll:0,warmAugmentsAll:0,coldBfsScansAll:0,warmBfsScansAll:0,oldAugmentsAll:0,oldBfsScansAll:0,coldAugmentsFallback:0,warmAugmentsFallback:0,coldScansFallback:0,warmScansFallback:0,fallbackZeroAugments:0,fallbackCutEquality:0,allZeroAugments:0,allCutEquality:0,trimmedUnits:0,maxGapBound:0,boundChecks:0,flowCertificates:0,changedCutAtEquality:0,warmWorseAugmentsFallback:0};
 function network(c,E,v,root){
  const k=E.length,n=c.length,s=k+n,t=s+1,V=t+1,INF=1+sum(c),C=Array.from({length:V},()=>Array(V).fill(0)),F=C.map(a=>a.slice());
  for(let j=0;j<k;j++){C[s][j]=v[j];for(let p=0;p<n;p++)if(E[j]&(1<<p))C[j][k+p]=INF;}
  for(let p=0;p<n;p++){C[k+p][t]=c[p];if(root&(1<<p))C[s][k+p]=INF;}
  return {k,n,s,t,V,C,F};
 }
 function certificate(g){
  let {s,t,V,C,F}=g,bal=Array(V).fill(0);
  for(let a=0;a<V;a++)for(let b=0;b<V;b++){check(Number.isSafeInteger(F[a][b])&&F[a][b]>=0&&F[a][b]<=C[a][b],"capacity");bal[a]-=F[a][b];bal[b]+=F[a][b]}
  for(let a=0;a<V;a++)if(a!==s&&a!==t)check(bal[a]===0,"conservation");
  check(-bal[s]===bal[t],"value");return bal[t];
 }
 function finish(g){
  let {k,n,s,t,V,C,F}=g,aug=0,scans=0,prev;
  for(;;){
   prev=Array(V).fill(-1);prev[s]=s;let q=[s];
   for(let i=0;i<q.length&&prev[t]<0;i++){let a=q[i];for(let b=0;b<V;b++){scans++;if(prev[b]<0&&C[a][b]-F[a][b]+F[b][a]>0){prev[b]=a;q.push(b)}}}
   if(prev[t]<0)break;
   let d=Infinity;for(let b=t;b!==s;b=prev[b]){let a=prev[b];d=Math.min(d,C[a][b]-F[a][b]+F[b][a])}
   for(let b=t;b!==s;b=prev[b]){let a=prev[b],z=Math.min(d,F[b][a]);F[b][a]-=z;F[a][b]+=d-z;}aug++;
  }
  let U=0,cut=0;
  for(let p=0;p<n;p++)if(prev[k+p]>=0)U|=1<<p;
  for(let a=0;a<V;a++)if(prev[a]>=0)for(let b=0;b<V;b++)if(prev[b]<0)cut+=C[a][b];
  let value=certificate(g);check(value===cut,"max flow min cut");
  return {U,value,aug,scans};
 }
 function trim(old,c,E,w,root){
  let g=network(c,E,w,root),{k,n,s,t,F}=g;
  for(let a=0;a<g.V;a++)F[a]=old.F[a].slice();
  let L=0;
  for(let j=0;j<k;j++){
   let d=Math.max(0,F[s][j]-w[j]);L+=d;F[s][j]-=d;
   for(let p=0;p<n&&d;p++){let z=Math.min(d,F[j][k+p]);F[j][k+p]-=z;F[k+p][t]-=z;d-=z;}
   check(d===0,"trim path decomposition");
  }
  return {g,L,value:certificate(g)};
 }
 function direct(c,E,v,root){
  let n=c.length,N=1<<n,best=Infinity,U=N-1;
  for(let u=1;u<N;u++)if(sub(root,u)){
   let h=0;for(let p=0;p<n;p++)if(u&(1<<p))h+=c[p];for(let j=0;j<E.length;j++)if(sub(E[j],u))h-=v[j];
   if(h<best){best=h;U=u}else if(h===best)U&=u;
  }return {U,slack:best};
 }
 function verify(c,E,v,w,root,record=true){
  const oldg=network(c,E,v,root),old=finish(oldg),ref0=direct(c,E,v,root),ref=direct(c,E,w,root);
  check(old.U===ref0.U&&old.value-sum(v)===ref0.slack,"old reference");
  const U=old.U,delta=w.map((x,j)=>x-v[j]);let out=0,inside=0,signedOutside=0,h=old.value-sum(v);
  for(let j=0;j<E.length;j++){let d=delta[j];if(sub(E[j],U)){h-=d;if(d<0&&!sub(E[j],root))inside-=d}else {if(d>0)out+=d;signedOutside+=d}}
  let reuse=out+inside===0||(h===1&&inside===0);
  const cold=finish(network(c,E,w,root)),tr=trim(oldg,c,E,w,root),gap=tr.L+signedOutside;
  check(tr.value===old.value-tr.L&&gap>=0,"trim value/gap");
  check(tr.value-sum(w)<=ref.slack&&ref.slack<=h,"dual sandwich");
  const warm=finish(tr.g);
  check(warm.U===ref.U&&cold.U===ref.U&&warm.value-sum(w)===ref.slack&&cold.value===warm.value,"new exact reference");
  check(warm.value-tr.value<=gap&&warm.aug<=gap,"augmentation bound");
  if(gap===0)check(warm.aug===0,"cut equality implies no augment");
  if(record){
   stats.queries++;stats.flowCertificates+=4;stats.boundChecks++;stats.oldAugmentsAll+=old.aug;stats.oldBfsScansAll+=old.scans;
   stats.coldAugmentsAll+=cold.aug;stats.warmAugmentsAll+=warm.aug;stats.coldBfsScansAll+=cold.scans;stats.warmBfsScansAll+=warm.scans;
   stats.trimmedUnits+=tr.L;stats.maxGapBound=Math.max(stats.maxGapBound,gap);
   if(!warm.aug)stats.allZeroAugments++;if(gap===0){stats.allCutEquality++;if(U!==warm.U)stats.changedCutAtEquality++}
   if(reuse){stats.gcpReuse++;check(U===warm.U&&h===ref.slack,"GCP reuse")}else{
    if(h===1)stats.gcpLocal++;else stats.gcpFull++;
    stats.coldAugmentsFallback+=cold.aug;stats.warmAugmentsFallback+=warm.aug;stats.coldScansFallback+=cold.scans;stats.warmScansFallback+=warm.scans;
    if(!warm.aug)stats.fallbackZeroAugments++;if(gap===0)stats.fallbackCutEquality++;if(warm.aug>cold.aug)stats.warmWorseAugmentsFallback++;
   }
  }
  return {old:{U:old.U,slack:ref0.slack},new:{U:warm.U,slack:ref.slack},trimLoss:tr.L,gap,coldAugments:cold.aug,warmAugments:warm.aug,oldCutNewSlack:h,reuse};
 }
 for(let {n,m,c,N,M,A} of models){
  const pop=new Uint8Array(M),cap=new Int16Array(N),L=new Int32Array(N);
  for(let z=1;z<M;z++)pop[z]=pop[z>>1]+(z&1);
  for(let u=1;u<N;u++){for(let p=0;p<n;p++)if(u&(1<<p))cap[u]+=c[p];for(let j=0;j<m;j++)if(sub(A[j].e,u))L[u]|=1<<j}
  const ok=new Uint8Array(M);
  for(let z=0;z<M;z++){ok[z]=1;for(let u=1;u<N;u++)if(pop[z&L[u]]>=cap[u]){ok[z]=0;break}stats.originalSubsets++}
  let groups=new Map();for(let j=0;j<m;j++)groups.set(A[j].e,(groups.get(A[j].e)||0)|(1<<j));
  const E=[...groups.keys()],H=[...groups.values()],vec=z=>H.map(h=>pop[h&z]);
  for(let tr=0;tr<8;tr++){let P=rnd(M),F=(M-1)^P,R=rnd(M)&P,R2=rnd(M)&P;if(!ok[R]||!ok[R2]){stats.rejectedPairs++;continue}stats.legalSiblingPairs++;let v=vec(R),w=vec(R2),mm=vec(F);for(let j=0;j<E.length;j++)if(mm[j]){verify(c,E,v,w,E[j]);verify(c,E,w,v,E[j])}}
 }
 const structured=[];
 for(let n=2;n<=10;n++){let c=[2,1,...Array(n-2).fill(5)],E=[1,3],v=[0,2],w=[1,1],root=1;let r=verify(c,E,v,w,root,false);check(r.old.U===3&&r.new.U===1&&r.old.slack===1&&r.new.slack===1,"proper repair family");structured.push({n,...r})}
 return {stats,structured,mismatches:0};
}
console.log(JSON.stringify(replay(),null,2));
