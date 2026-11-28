function replay(){
const ck=(b,m,d)=>{if(!b)throw Error(m+" "+JSON.stringify(d))},sum=a=>a.reduce((s,x)=>s+x,0),sub=(a,b)=>(a&b)===a,ports=(a,n)=>Array.from({length:n},(_,p)=>p).filter(p=>a&(1<<p)),inside=(e,U)=>e.every(p=>U[p]),eq=(a,b)=>a&&b&&a.length===b.length&&a.every((x,i)=>x===b[i]);
let seed=20261128;const rnd=n=>{seed^=seed<<13;seed^=seed>>>17;seed^=seed<<5;return(seed>>>0)%n};
const mk=()=>({calls:0,aug:0,scans:0,edges:0,nodes:0});
const stats={seed,models:350,originalSubsets:0,states:0,minorStates:0,rejectedMinor:0,baseline:mk(),allocation:mk(),bounded:mk(),index:{builds:0,nodes:0,edges:0,dfsScans:0,predScans:0,intersectSteps:0,markScans:0,passes:0,queryRoots:0,queryMarkTests:0,witnessScans:0},cacheHits:0,cacheTests:0,cacheExactCutDifferences:0,rollbackUnits:0,activeClasses:0,blockedClasses:0,rootOracleChecks:0,persistentChecks:0,allocationChecks:0,rankChecks:0,partitionChecks:0,exchangeChecks:0,productChecks:0,large:[]};
function flow(V,edges,src,t,stat,limit=Infinity,rollback=false){
 let g=Array.from({length:V},()=>[]),refs=[];
 for(let [u,v,c] of edges){let a={v,c,rev:g[v].length},b={v:u,c:0,rev:g[u].length};g[u].push(a);g[v].push(b);refs.push(a)}
 stat.calls++;stat.edges+=edges.length;stat.nodes+=V;
 let F=0,reach=null,last=null;
 while(F<limit){
 let prev=Array(V).fill(-1),pi=Array(V).fill(-1),q=[src];prev[src]=src;
 for(let i=0;i<q.length&&prev[t]<0;i++){let u=q[i];for(let j=0;j<g[u].length;j++){let a=g[u][j];stat.scans++;if(a.c>0&&prev[a.v]<0){prev[a.v]=u;pi[a.v]=j;q.push(a.v)}}}
 if(prev[t]<0){reach=prev.map(x=>x>=0);break}
 let d=limit-F,path=[];for(let v=t;v!==src;v=prev[v]){let u=prev[v],a=g[u][pi[v]];d=Math.min(d,a.c);path.push(a)}
 ck(Number.isSafeInteger(d)&&d>0,"augment",d);
 for(let a of path){a.c-=d;g[a.v][a.rev].c+=d}F+=d;last=path;stat.aug++;
 }
 if(reach)ck(sum(edges.map(([u,v,c])=>reach[u]&&!reach[v]?c:0))===F,"mincut",{F});
 if(rollback){ck(F>=1&&last,"reserve",{F});for(let a of last){a.c++;g[a.v][a.rev].c--}stats.rollbackUnits++}
 let f=edges.map((e,i)=>e[2]-refs[i].c),bal=Array(V).fill(0),net=F-(rollback?1:0);
 for(let i=0;i<edges.length;i++){let [u,v,c]=edges[i],z=f[i];ck(Number.isSafeInteger(z)&&z>=0&&z<=c,"flow cap",{i,z,c});bal[u]-=z;bal[v]+=z}
 ck(bal[src]===-net&&bal[t]===net&&bal.every((z,i)=>i===src||i===t||z===0),"conservation",{bal,net});
 return{F,reach,f};
}
function ordinary(c,E,v,i=null){
 let n=c.length,k=E.length,src=n+k,t=src+1,M=1+sum(c),ed=[],slots=[];
 for(let j=0;j<k;j++)if(v[j]){ed.push([src,n+j,v[j]]);for(let p of E[j]){slots.push([j,p,ed.length]);ed.push([n+j,p,M])}}
 for(let p=0;p<n;p++)ed.push([p,t,c[p]]);
 if(i!==null)for(let p of E[i])ed.push([src,p,M]);
 let r=flow(t+1,ed,src,t,i===null?stats.allocation:stats.baseline);
 if(i!==null)return{lambda:r.F-sum(v),U:r.reach.slice(0,n)};
 ck(r.F===sum(v),"initial allocation",{v});let A=E.map(()=>c.map(()=>0));for(let [j,p,id] of slots)A[j][p]=r.f[id];return A;
}
function credit(c,E,v,U){return sum(c.filter((_,p)=>U[p]))-sum(v.filter((_,j)=>inside(E[j],U)))}
function checkA(c,E,v,A){ck(A.every((row,j)=>sum(row)===v[j]&&row.every((x,p)=>Number.isSafeInteger(x)&&x>=0&&(!x||E[j].includes(p))))&&c.every((x,p)=>sum(A.map(row=>row[p]))<=x),"allocation",{c,E,v,A});stats.allocationChecks++}
function quotient(c,E,v,A){
 const n=c.length,M=1+sum(c),ed=[],cancel=[],add=[];let next=n;
 for(let j=0;j<E.length;j++)if(v[j]){let u=next++;for(let p of E[j]){if(A[j][p]){cancel.push([j,p,ed.length]);ed.push([p,u,A[j][p]])}add.push([j,p,ed.length]);ed.push([u,p,M])}}
 for(let p=0;p<n;p++){let z=c[p]-sum(A.map(row=>row[p]));if(z)ed.push([p,next,z])}
 return{n,M,ed,cancel,add,t:next,V:next+1};
}
function bounded(c,E,v,A,i,m){
 let G=quotient(c,E,v,A),{n,M,ed,cancel,add,t,V}=G,src=V,inject=[];
 for(let p of E[i]){inject.push([i,p,ed.length]);ed.push([src,p,M])}
 let r=flow(V+1,ed,src,t,stats.bounded,m+1,true);
 for(let [j,p,id] of cancel)A[j][p]-=r.f[id];for(let [j,p,id] of add)A[j][p]+=r.f[id];for(let [j,p,id] of inject)A[j][p]+=r.f[id];
 return{a:r.F-1,U:r.reach?r.reach.slice(0,n):null};
}
// GCT reverse CHK dominators + single bridge scan, adapted to compact positive-row quotient.
// No independent per-edge deletion audit here: exact full root-cut oracle and labeled exchanges below.
function index(G){
 const {V,t,ed}=G,d=stats.index,adj=Array.from({length:V},()=>[]),rev=Array.from({length:V},()=>[]);
 ed.forEach(([u,v],i)=>{adj[u].push([v,i]);rev[v].push(u)});
 d.builds++;d.nodes+=V;d.edges+=ed.length;
 let seen=Array(V).fill(false),post=[],stack=[[t,0]];seen[t]=true;
 while(stack.length){let x=stack[stack.length-1],u=x[0];if(x[1]===rev[u].length){post.push(u);stack.pop();continue}let v=rev[u][x[1]++];d.dfsScans++;if(!seen[v]){seen[v]=true;stack.push([v,0])}}
 ck(post.length===V,"sink reachability",{V,post});
 let order=post.reverse(),pos=Array(V),par=Array(V).fill(-1);order.forEach((v,i)=>pos[v]=i);par[t]=t;
 function intersect(a,b){while(a!==b){if(pos[a]>pos[b])a=par[a];else b=par[b];d.intersectSteps++}return a}
 let changed=true;while(changed){changed=false;d.passes++;for(let v of order.slice(1)){let p=-1;for(let [u] of adj[v]){d.predScans++;if(par[u]<0)continue;p=p<0?u:intersect(p,u)}ck(p>=0,"predecessor");if(par[v]!==p){par[v]=p;changed=true}}}
 let child=Array.from({length:V},()=>[]),tin=Array(V),tout=Array(V),orderT=[t],clock=1;tin[t]=0;
 for(let v of order.slice(1))child[par[v]].push(v);
 stack=[[t,0]];while(stack.length){let x=stack[stack.length-1],u=x[0];if(x[1]===child[u].length){tout[u]=clock;stack.pop();continue}let v=child[u][x[1]++];tin[v]=clock++;orderT.push(v);stack.push([v,0])}
 let anc=(a,b)=>tin[a]<=tin[b]&&tin[b]<tout[a],count=Array(V).fill(0),sole=Array(V).fill(-1);
 for(let [id,[u,v,c]] of ed.entries()){d.markScans++;if(u!==t&&!anc(u,v)){count[u]++;sole[u]=id}}
 let mark=Array(V).fill(-1),near=Array(V).fill(-1);for(let u of orderT){if(u!==t&&count[u]===1&&ed[sole[u]][2]===1)mark[u]=sole[u];near[u]=mark[u]>=0?u:u===t?-1:near[par[u]]}
 return{adj,par,tin,anc,mark,near};
}
function tightQuery(G,I,E){
 const d=stats.index;d.queryRoots++;let lo=E[0],hi=E[0];for(let p of E){if(I.tin[p]<I.tin[lo])lo=p;if(I.tin[p]>I.tin[hi])hi=p}
 let b=I.near[lo];while(b>=0){d.queryMarkTests++;if(I.anc(b,hi))break;b=I.near[I.par[b]]}
 ck(b>=0,"deferred root lacks unit bridge",{E});let seen=Array(G.V).fill(false),q=[];for(let p of E)if(!seen[p]){seen[p]=true;q.push(p)}
 for(let i=0;i<q.length;i++)for(let [v,id] of I.adj[q[i]]){d.witnessScans++;if(id!==I.mark[b]&&!seen[v]){seen[v]=true;q.push(v)}}
 ck(!seen[G.t]&&sum(G.ed.map(([u,v,c])=>seen[u]&&!seen[v]?c:0))===1,"tight witness",{E});
 return seen.slice(0,G.n);
}

/* GCV: induced unit-bridge region SCC condensation, port-mask closure, interned root queries.
   The old GCU tightQuery is retained only as an audit/baseline, except singleton groups. */
stats.closure={groups:0,multiGroups:0,singletonQueries:0,queries:0,vertexTests:0,bridgeTests:0,rootVisits:0,buildScans:0,dfsScans:0,dagScans:0,dagArcs:0,components:0,maskOR:0,signatureHits:0,distinctMasks:0,materializedPorts:0,singletonScans:0,cutChecks:0};
function chosenBridge(I,E){
 let d=stats.closure,lo=E[0],hi=E[0];
 for(let p of E){d.rootVisits++;if(I.tin[p]<I.tin[lo])lo=p;if(I.tin[p]>I.tin[hi])hi=p}
 let b=I.near[lo];while(b>=0){d.bridgeTests++;if(I.anc(b,hi))return b;b=I.near[I.par[b]]}
 throw Error("no bridge");
}
function closureIndex(G,I,b){
 let d=stats.closure,vs=[],inD=Array(G.V).fill(false),out=Array.from({length:G.V},()=>[]),rev=Array.from({length:G.V},()=>[]);
 for(let u=0;u<G.V;u++){d.vertexTests++;if(I.anc(b,u)){vs.push(u);inD[u]=true}}
 for(let u of vs)for(let [v,id] of I.adj[u]){d.buildScans++;if(id===I.mark[b])continue;ck(inD[v],"bridge domain outgoing",{u,v,b});out[u].push(v);rev[v].push(u)}
 let seen=Array(G.V).fill(false),post=[];
 for(let root of vs)if(!seen[root]){
   let st=[[root,0]];seen[root]=true;
   while(st.length){let a=st[st.length-1],u=a[0];if(a[1]===out[u].length){post.push(u);st.pop();continue}let v=out[u][a[1]++];d.dfsScans++;if(!seen[v]){seen[v]=true;st.push([v,0])}}
 }
 let comp=Array(G.V).fill(-1),masks=[],dag=[];
 for(let root of post.reverse())if(comp[root]<0){
   let j=masks.length,q=[root],mask=0n;comp[root]=j;
   for(let z=0;z<q.length;z++){let u=q[z];if(u<G.n)mask|=1n<<BigInt(u);for(let v of rev[u]){d.dfsScans++;if(comp[v]<0){comp[v]=j;q.push(v)}}}
   masks.push(mask);dag.push(new Set());
 }
 d.components+=masks.length;
 for(let u of vs)for(let v of out[u]){d.dagScans++;let a=comp[u],z=comp[v];if(a!==z){ck(a<z,"SCC topological order");dag[a].add(z)}}
 for(let j=masks.length-1;j>=0;j--)for(let z of dag[j]){d.dagArcs++;d.maskOR++;masks[j]|=masks[z]}
 return{comp,masks,cache:new Map(),intern:new Map()};
}
function batchTight(G,I,E,defer){
 const d=stats.closure,groups=new Map(),answers=new Map();
 for(let {i} of defer){d.queries++;let b=chosenBridge(I,E[i]);if(!groups.has(b))groups.set(b,[]);groups.get(b).push(i)}
 for(let [b,ids] of groups){
  d.groups++;
  if(ids.length===1){let i=ids[0],before=stats.index.witnessScans,U=tightQuery(G,I,E[i]);d.singletonScans+=stats.index.witnessScans-before;d.singletonQueries++;answers.set(i,U);continue}
  d.multiGroups++;let C=closureIndex(G,I,b);
  for(let i of ids){
   const sig=[...new Set(E[i].map(p=>{d.rootVisits++;return C.comp[p]}))].sort((a,b)=>a-b);
   ck(sig.every(j=>j>=0),"root outside domain");
   const key=sig.join(",");let mask;
   if(C.cache.has(key)){d.signatureHits++;mask=C.cache.get(key)}else{mask=0n;for(let j of sig){d.maskOR++;mask|=C.masks[j]}C.cache.set(key,mask)}
   if(!C.intern.has(mask)){d.distinctMasks++;d.materializedPorts+=G.n;C.intern.set(mask,Array.from({length:G.n},(_,p)=>!!(mask&(1n<<BigInt(p)))))}
   let U=C.intern.get(mask),ref=tightQuery(G,I,E[i]);d.cutChecks++;ck(eq(U,ref),"SCC witness mismatch",{i,b,U,ref});answers.set(i,U);
  }
 }
 return answers;
}

function basis(c,E,S,m,oracle=null){
 let k=E.length,v=S.slice(),B=m.map(()=>0),cuts=[],defer=[],A=sum(S)?ordinary(c,E,S):E.map(()=>c.map(()=>0)),parent=m.map((_,i)=>i);
 checkA(c,E,v,A);
 const find=i=>{while(parent[i]!==i){parent[i]=parent[parent[i]];i=parent[i]}return i},join=(i,j)=>{i=find(i);j=find(j);if(i!==j)parent[j]=i};
 for(let i=0;i<k;i++)if(m[i]){
 stats.activeClasses++;let ref=ordinary(c,E,v,i);if(oracle){oracle(v,i,ref.U,ref.lambda);stats.rootOracleChecks++}
 let hit=null;for(let cut of cuts){stats.cacheTests++;if(inside(E[i],cut.U)){hit=cut.U;break}}
 let r;if(hit){stats.cacheHits++;if(!eq(hit,ref.U))stats.cacheExactCutDifferences++;defer.push({i,audit:ref.U});r={a:0,U:null}}else r=bounded(c,E,v,A,i,m[i]);
 let a=Math.min(m[i],ref.lambda-1);ck(r.a===a,"batch",{c,E,v,i,m,r,ref,hit});
 B[i]=a;v[i]+=a;checkA(c,E,v,A);
 if(a<m[i]){stats.blockedClasses++;if(!hit){ck(r.U&&eq(r.U,ref.U)&&credit(c,E,v,r.U)===1,"least blocked cut",{c,E,v,i,m,r,ref});cuts.push({i,U:r.U})}}
 else ck(!r.U,"full batch no cut",{i,r});
 for(let cut of cuts){ck(credit(c,E,v,cut.U)===1,"persistent",{cut,v});stats.persistentChecks++}
 }
 if(defer.length){let G=quotient(c,E,v,A),I=index(G);let answers=batchTight(G,I,E,defer);for(let {i,audit} of defer){let U=answers.get(i);ck(eq(U,audit)&&credit(c,E,v,U)===1,"deferred least cut persistence",{i,U,audit});cuts.push({i,U})}}
 for(let {i,U} of cuts)for(let j=0;j<k;j++)if(B[j]&&inside(E[j],U))join(i,j);
 let groups=new Map();for(let i=0;i<k;i++)if(m[i]){let p=find(i);if(!groups.has(p))groups.set(p,[]);groups.get(p).push(i)}
 return{B,cuts,groups:[...groups.values()]};
}
// Frozen GCO generator and minor sampling, same random draw order.
const models=[];
for(let it=0;it<350;it++){let n=2+rnd(6),m=5+rnd(8),c=Array.from({length:n},()=>1+rnd(4)),N=1<<n,M=1<<m,A=[];for(let j=0;j<m;j++){let aux=rnd(3)===0;A.push({e:aux?1<<rnd(n):1+rnd(N-1),p:aux?0:1+rnd(15),s:aux?1+rnd(9):0})}for(let x of A)if(x.s)c[Math.log2(x.e)]++;models.push({n,m,c,N,M,A})}
for(let {n,m,c,N,M,A} of models){
 const pop=new Uint8Array(M),cap=new Int16Array(N),L=new Int32Array(N);
 for(let z=1;z<M;z++)pop[z]=pop[z>>1]+(z&1);
 for(let u=1;u<N;u++){cap[u]=sum(ports(u,n).map(p=>c[p]));for(let j=0;j<m;j++)if(sub(A[j].e,u))L[u]|=1<<j}
 const ok=new Uint8Array(M);for(let z=0;z<M;z++){ok[z]=1;for(let u=1;u<N;u++)if(pop[z&L[u]]>=cap[u]){ok[z]=0;break}stats.originalSubsets++}
 let groups=new Map();for(let j=0;j<m;j++)groups.set(A[j].e,(groups.get(A[j].e)||0)|(1<<j));
 const masks=[...groups.keys()],H=[...groups.values()],E=masks.map(x=>ports(x,n)),vec=z=>H.map(h=>pop[h&z]),gmask=js=>js.reduce((z,j)=>z|H[j],0);
 function verify(R,F){stats.states++;let S=vec(R),mm=vec(F);
 function oracle(v,i,U,lambda){let min=Infinity,inter=N-1;for(let u=1;u<N;u++)if(sub(masks[i],u)){let z=cap[u]-sum(v.filter((_,j)=>sub(masks[j],u)));if(z<min){min=z;inter=u}else if(z===min)inter&=u}let got=U.reduce((z,b,p)=>z|(b?1<<p:0),0);ck(min===lambda&&inter===got,"root oracle",{min,lambda,inter,got})}
 let {B,cuts,groups:gs0}=basis(c,E,S,mm,oracle),Z=0;
 for(let j=0;j<H.length;j++){let h=F&H[j];for(let a=0;a<B[j];a++){let b=h&-h;ck(b!==0,"lift");Z|=b;h^=b}}
 ck(ok[R|Z],"basis");
 let maxRank=0,part=mm.map((_,i)=>1<<i),gs=gs0.map(gmask);
 for(let x=F;;x=(x-1)&F){let f=!!ok[R|x];if(f)maxRank=Math.max(maxRank,pop[x]);ck(gs.every(h=>!!ok[R|(x&h)])===f,"product");stats.productChecks++;
 if(x&&!f){let cir=true;for(let b=x;b;b&=b-1)if(!ok[R|(x^(b&-b))]){cir=false;break}if(cir){let J=vec(x).reduce((z,a,i)=>z|(a?1<<i:0),0),u=J;for(let i=0;i<mm.length;i++)if(J>>>i&1)u|=part[i];for(let i=0;i<mm.length;i++)if(u>>>i&1)part[i]=u}}
 if(!x)break}
 ck(sum(B)===maxRank,"rank");stats.rankChecks++;
 let expected=[...new Set(part.filter((_,i)=>mm[i]))].sort((a,b)=>a-b),actual=gs0.map(js=>js.reduce((z,j)=>z|1<<j,0)).sort((a,b)=>a-b);ck(JSON.stringify(expected)===JSON.stringify(actual),"partition");stats.partitionChecks++;
 for(let {i,U} of cuts){let x=H[i]&F&~Z;x&=-x;ck(x&&!ok[R|Z|x],"blocked");for(let j=0;j<H.length;j++)for(let y=Z&H[j];y;y&=y-1){ck(!!ok[R|(Z^(y&-y))|x]===inside(E[j],U),"exchange");stats.exchangeChecks++}}
 }
 verify(0,M-1);for(let tr=0;tr<8;tr++){let P=rnd(M),F=(M-1)^P,R=rnd(M)&P,R2=rnd(M)&P;if(!ok[R]||!ok[R2]){stats.rejectedMinor++;continue}stats.minorStates++;verify(R,F)}
}
const snap=()=>JSON.parse(JSON.stringify(stats)),small=snap();
for(let d of [10,30,60,100]){let c=Array(d).fill(1),E=[];for(let i=0;i<d;i++)E.push(c.map((_,p)=>p).filter(p=>p!==i));for(let i=0;i<d;i++)E.push(c.map((_,p)=>p).filter(p=>p!==i&&p!==(i+1)%d));let k=E.length,before=snap(),r=basis(c,E,Array(k).fill(0),Array(k).fill(1));ck(sum(r.B)===d-1&&r.groups.length===1&&r.groups[0].length===k&&r.cuts.every(({U})=>U.every(Boolean)),"uniform family",{d});let diff=x=>Object.fromEntries(Object.keys(stats[x]).map(z=>[z,stats[x][z]-before[x][z]]));stats.large.push({ports:d,classes:k,rank:sum(r.B),baseline:diff("baseline"),allocation:diff("allocation"),bounded:diff("bounded"),index:diff("index"),closure:diff("closure"),cacheHits:stats.cacheHits-before.cacheHits})}
return{small,total:stats,mismatches:0,scope:"Exact synthetic strict-Hall GCO frozen generator/minors; GCV per-bridge SCC closure vs original GCU deferred witness BFS on identical frozen inputs. Old BFS retained for audit and singleton fallback; closure counters exclude audit BFS. Baseline uses identical sparse BFS; operation counts, not elapsed time or physical results. Audit-only reference code excluded from candidate counters."};
}
console.log(JSON.stringify(replay(),null,2));
