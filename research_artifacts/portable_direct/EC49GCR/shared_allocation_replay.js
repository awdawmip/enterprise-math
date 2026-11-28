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
 const stats={models:350,seed:20261128,originalSubsets:0,legalSiblingPairs:0,rejectedPairs:0,statePairsWithRoots:0,queries:0,cutChecks:0,allocationChecks:0,graphCertificates:0,baselineColdAugments:0,baselineColdScans:0,baselineWarmAugments:0,baselineWarmScans:0,baselineWarmTrim:0,baselineWarmBudget:0,rootColdAugments:0,rootColdScans:0,rootSharedAugments:0,rootSharedScans:0,rootSharedWarmAugments:0,rootSharedWarmScans:0,rootColdEdges:0,rootSharedEdges:0,rootSharedWarmEdges:0,rootColdNodes:0,rootSharedNodes:0,rootSharedWarmNodes:0,rootCreditSum:0,positiveAllocationEntries:0,zeroClassEliminations:0,singletonEliminations:0,pairEliminations:0};
 function graph(V,s,t){return{V,s,t,g:Array.from({length:V},()=>[]),edges:[]}}
 function edge(h,u,v,c){check(Number.isSafeInteger(c)&&c>=0&&u!==v,"edge");let a={to:v,cap:c,orig:c,rev:h.g[v].length},b={to:u,cap:0,orig:0,rev:h.g[u].length};h.g[u].push(a);h.g[v].push(b);h.edges.push({u,a});return a}
 function setflow(h,u,a,f){check(f>=0&&f<=a.orig,"initial flow");a.cap=a.orig-f;h.g[a.to][a.rev].cap=f}
 function finish(h){
  let {V,s,t,g}=h,aug=0,scans=0,prev,pi;
  for(;;){
   prev=Array(V).fill(-1);pi=Array(V).fill(-1);prev[s]=s;let q=[s];
   for(let i=0;i<q.length&&prev[t]<0;i++){let u=q[i];for(let j=0;j<g[u].length;j++){let a=g[u][j];scans++;if(a.cap>0&&prev[a.to]<0){prev[a.to]=u;pi[a.to]=j;q.push(a.to)}}}
   if(prev[t]<0)break;
   let d=Infinity;for(let v=t;v!==s;v=prev[v])d=Math.min(d,g[prev[v]][pi[v]].cap);
   for(let v=t;v!==s;v=prev[v]){let a=g[prev[v]][pi[v]];a.cap-=d;g[v][a.rev].cap+=d}aug++;
  }
  let bal=Array(V).fill(0),cut=0;for(let {u,a} of h.edges){let f=a.orig-a.cap;check(Number.isSafeInteger(f)&&f>=0&&f<=a.orig,"flow cap");bal[u]-=f;bal[a.to]+=f;if(prev[u]>=0&&prev[a.to]<0)cut+=a.orig}
  for(let i=0;i<V;i++)if(i!==s&&i!==t)check(bal[i]===0,"conservation");check(bal[t]===-bal[s]&&bal[t]===cut,"flow cut");
  return {value:cut,reach:prev.map(x=>x>=0),aug,scans,edges:h.edges.length,nodes:V};
 }
 function ports(e,n){return Array.from({length:n},(_,p)=>p).filter(p=>e&(1<<p))}
 function allocNet(c,E,v,root=0,init=null){
  let n=c.length,k=E.length,s=n+k,t=s+1,M=1+sum(c),h=graph(t+1,s,t),a=[],b=[],d=[];
  for(let j=0;j<k;j++){a[j]=edge(h,s,n+j,v[j]);b[j]=Array(n).fill(null);for(let p of ports(E[j],n))b[j][p]=edge(h,n+j,p,M)}
  for(let p=0;p<n;p++){d[p]=edge(h,p,t,c[p]);if(root&(1<<p))edge(h,s,p,M)}
  if(init){let load=Array(n).fill(0);for(let j=0;j<k;j++){setflow(h,s,a[j],sum(init[j]));for(let p of ports(E[j],n)){setflow(h,n+j,b[j][p],init[j][p]);load[p]+=init[j][p]}}for(let p=0;p<n;p++)setflow(h,p,d[p],load[p])}
  let r=finish(h);let A=b.map(row=>row.map(x=>x?x.orig-x.cap:0));return {...r,A,U:r.reach.slice(0,n).reduce((u,x,p)=>u|(x?1<<p:0),0)};
 }
 function validateAlloc(c,E,v,A){let n=c.length;for(let j=0;j<E.length;j++){check(sum(A[j])===v[j],"row sum");for(let p=0;p<n;p++)check(Number.isSafeInteger(A[j][p])&&A[j][p]>=0&&(A[j][p]===0||!!(E[j]&(1<<p))),"allocation support")}let z=c.map((x,p)=>x-sum(A.map(a=>a[p])));check(z.every(x=>x>=0),"port cap");stats.allocationChecks++;return z}
 function trim(A,w){let B=A.map(x=>x.slice()),L=0;for(let j=0;j<w.length;j++){let d=Math.max(0,sum(B[j])-w[j]);L+=d;for(let p=0;p<B[j].length&&d;p++){let z=Math.min(d,B[j][p]);B[j][p]-=z;d-=z}check(d===0,"trim")}return {B,L}}
 function rootQuery(c,E,v,A,root,record=true){
  let n=c.length,k=E.length,M=1+sum(c),z=validateAlloc(c,E,v,A),aux=0,P=E.map(e=>ports(e,n));for(let j=0;j<k;j++)if(v[j]&&P[j].length>=3)aux++;
  let s=n+aux,t=s+1,h=graph(t+1,s,t),jnode=n;
  for(let p=0;p<n;p++){if(z[p])edge(h,p,t,z[p]);if(root&(1<<p))edge(h,s,p,M)}
  for(let j=0;j<k;j++){
   if(!v[j]){if(record)stats.zeroClassEliminations++;continue}
   let pp=P[j];if(pp.length===1){if(record)stats.singletonEliminations++;continue}
   if(pp.length===2){if(record)stats.pairEliminations++;let [p,q]=pp;if(A[j][p])edge(h,p,q,A[j][p]);if(A[j][q])edge(h,q,p,A[j][q]);continue}
   let u=jnode++;for(let p of pp){if(A[j][p])edge(h,p,u,A[j][p]);edge(h,u,p,M)}
  }
  check(jnode===s,"nodes");let r=finish(h);return {...r,U:r.reach.slice(0,n).reduce((u,x,p)=>u|(x?1<<p:0),0)};
 }
 function direct(c,E,v,root){let best=Infinity,U=(1<<c.length)-1;for(let u=1;u<(1<<c.length);u++)if(sub(root,u)){let h=sum(c.map((x,p)=>u&(1<<p)?x:0))-sum(v.map((x,j)=>sub(E[j],u)?x:0));if(h<best){best=h;U=u}else if(h===best)U&=u}return {U,value:best}}
 function verifyRoot(c,E,v,A,B,root){
  let ref=direct(c,E,v,root),cold=allocNet(c,E,v,root),shared=rootQuery(c,E,v,A,root,true),warm=rootQuery(c,E,v,B,root,false);
  check(cold.value-sum(v)===ref.value&&cold.U===ref.U,"cold reference");
  for(let x of [shared,warm])check(x.value===ref.value&&x.U===ref.U&&x.aug<=x.value,"shared root reference and budget");
  stats.queries++;stats.cutChecks+=3;stats.graphCertificates+=3;stats.rootCreditSum+=ref.value;
  for(let [key,r] of [["rootCold",cold],["rootShared",shared],["rootSharedWarm",warm]]){stats[key+"Augments"]+=r.aug;stats[key+"Scans"]+=r.scans;stats[key+"Edges"]+=r.edges;stats[key+"Nodes"]+=r.nodes}
 }
 for(let {n,m,c,N,M,A} of models){
  const pop=new Uint8Array(M),cap=new Int16Array(N),L=new Int32Array(N);
  for(let z=1;z<M;z++)pop[z]=pop[z>>1]+(z&1);
  for(let u=1;u<N;u++){for(let p=0;p<n;p++)if(u&(1<<p))cap[u]+=c[p];for(let j=0;j<m;j++)if(sub(A[j].e,u))L[u]|=1<<j}
  const ok=new Uint8Array(M);
  for(let z=0;z<M;z++){ok[z]=1;for(let u=1;u<N;u++)if(pop[z&L[u]]>=cap[u]){ok[z]=0;break}stats.originalSubsets++}
  let groups=new Map();for(let j=0;j<m;j++)groups.set(A[j].e,(groups.get(A[j].e)||0)|(1<<j));
  const E=[...groups.keys()],H=[...groups.values()],vec=z=>H.map(h=>pop[h&z]);
  for(let tr=0;tr<8;tr++){let P=rnd(M),F=(M-1)^P,R=rnd(M)&P,R2=rnd(M)&P;if(!ok[R]||!ok[R2]){stats.rejectedPairs++;continue}stats.legalSiblingPairs++;let v=vec(R),w=vec(R2),mm=vec(F),roots=E.filter((_,j)=>mm[j]);if(!roots.length)continue;stats.statePairsWithRoots++;
   let av=allocNet(c,E,v),aw=allocNet(c,E,w),trm=trim(av.A,w),bw=allocNet(c,E,w,0,trm.B),budget=sum(w.map((x,j)=>Math.max(0,x-v[j])));
   check(av.value===sum(v)&&aw.value===sum(w)&&bw.value===sum(w)&&bw.aug<=budget&&sum(w)-sum(trm.B.map(sum))===budget,"baseline exact/repair");
   for(let [x,a] of [[v,av.A],[w,aw.A],[w,bw.A]])validateAlloc(c,E,x,a);
   stats.graphCertificates+=3;stats.baselineColdAugments+=av.aug+aw.aug;stats.baselineColdScans+=av.scans+aw.scans;stats.baselineWarmAugments+=av.aug+bw.aug;stats.baselineWarmScans+=av.scans+bw.scans;stats.baselineWarmTrim+=trm.L;stats.baselineWarmBudget+=budget;
   stats.positiveAllocationEntries+=av.A.flat().filter(x=>x>0).length+aw.A.flat().filter(x=>x>0).length;
   for(let root of roots){verifyRoot(c,E,v,av.A,av.A,root);verifyRoot(c,E,w,aw.A,bw.A,root)}
  }
 }
 const structured=[];
 for(let n=2;n<=10;n++){let c=[2,1,...Array(n-2).fill(5)],E=[1,3],v=[0,2],w=[1,1],root=1;let av=allocNet(c,E,v),bw=allocNet(c,E,w,0,trim(av.A,w).B),r0=rootQuery(c,E,v,av.A,root,false),r1=rootQuery(c,E,w,bw.A,root,false);check(r0.U===3&&r1.U===1&&r0.value===1&&r1.value===1,"structural tie");structured.push({n,old:{U:r0.U,value:r0.value},new:{U:r1.U,value:r1.value}})}
 return {stats,structured,mismatches:0};
}
console.log(JSON.stringify(replay(),null,2));
