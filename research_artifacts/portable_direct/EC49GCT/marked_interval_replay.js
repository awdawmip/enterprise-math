function replay(){
 const ck=(b,m)=>{if(!b)throw Error(m)},sum=a=>a.reduce((s,x)=>s+x,0),sub=(a,b)=>(a&b)===a;
 let seed=20261128;const rnd=n=>{seed^=seed<<13;seed^=seed>>>17;seed^=seed<<5;return(seed>>>0)%n};
 const models=[];
 for(let it=0;it<350;it++){let n=2+rnd(6),m=5+rnd(8),c=Array.from({length:n},()=>1+rnd(4)),N=1<<n,M=1<<m,A=[];for(let j=0;j<m;j++){let aux=rnd(3)===0;A.push({e:aux?1<<rnd(n):1+rnd(N-1),p:aux?0:1+rnd(15),s:aux?1+rnd(9):0})}for(let x of A)if(x.s)c[Math.log2(x.e)]++;models.push({n,m,c,N,M,A})}
 const stats={seed:20261128,models:350,originalSubsets:0,legalSiblingPairs:0,rejectedPairs:0,states:0,roots:0,unitQueries:0,nonunitQueries:0,arbitraryRootChecks:0,arbitraryTightRoots:0,unitEdges:0,activeBridges:0,laminarChecks:0,bridgePreprocessEdgeScans:0,bridgeQueryMembershipTests:0,bridgeQueryReachScans:0,coldRootSearchScans:0,hybridFallbackSearchScans:0,coldRootAugments:0,hybridFallbackAugments:0,allocationScans:0,allocationAugments:0,cutChecks:0,allocationChecks:0,structuredChecks:0};
 function flow(V,edges,s,t){let g=Array.from({length:V},()=>[]),refs=[];for(let [u,v,c] of edges){let a={v,c,rev:g[v].length},b={v:u,c:0,rev:g[u].length};g[u].push(a);g[v].push(b);refs.push(a)}let value=0,scans=0,aug=0,prev,pi;for(;;){prev=Array(V).fill(-1);pi=Array(V).fill(-1);prev[s]=s;let q=[s];for(let i=0;i<q.length&&prev[t]<0;i++){let u=q[i];for(let j=0;j<g[u].length;j++){let a=g[u][j];scans++;if(a.c>0&&prev[a.v]<0){prev[a.v]=u;pi[a.v]=j;q.push(a.v)}}}if(prev[t]<0)break;let d=Infinity;for(let v=t;v!==s;v=prev[v])d=Math.min(d,g[prev[v]][pi[v]].c);for(let v=t;v!==s;v=prev[v]){let a=g[prev[v]][pi[v]];a.c-=d;g[v][a.rev].c+=d}value+=d;aug++}let reach=prev.map(x=>x>=0),bal=Array(V).fill(0),cut=0;let f=edges.map(([u,v,c],i)=>{let z=c-refs[i].c;ck(z>=0&&z<=c&&Number.isSafeInteger(z),"flow capacity");bal[u]-=z;bal[v]+=z;if(reach[u]&&!reach[v])cut+=c;return z});ck(cut===value&&bal[t]===value&&bal[s]===-value&&bal.every((x,i)=>i===s||i===t||x===0),"flow certificate");return{value,reach,f,scans,aug}}
 function ports(mask,n){return Array.from({length:n},(_,i)=>i).filter(i=>mask&(1<<i))}
 function quotient(c,E,v){let n=c.length,k=E.length,s=n+k,t=s+1,M=1+sum(c),edges=[],slots=[];for(let j=0;j<k;j++){edges.push([s,n+j,v[j]]);for(let p of ports(E[j],n)){slots.push([j,p,edges.length]);edges.push([n+j,p,M])}}for(let p=0;p<n;p++)edges.push([p,t,c[p]]);let f=flow(t+1,edges,s,t);stats.allocationScans+=f.scans;stats.allocationAugments+=f.aug;ck(f.value===sum(v),"allocation total");let A=E.map(()=>Array(n).fill(0));for(let [j,p,i] of slots)A[j][p]=f.f[i];let z=c.map((a,p)=>a-sum(A.map(row=>row[p])));ck(z.every(x=>x>=0)&&A.every((row,j)=>sum(row)===v[j]),"allocation");stats.allocationChecks++;let aux=n,arcs=[];for(let j=0;j<k;j++){if(!v[j])continue;let pp=ports(E[j],n);if(pp.length===1)continue;if(pp.length===2){let [p,q]=pp;if(A[j][p])arcs.push([p,q,A[j][p]]);if(A[j][q])arcs.push([q,p,A[j][q]]);continue}let u=aux++;for(let p of pp){if(A[j][p])arcs.push([p,u,A[j][p]]);arcs.push([u,p,M])}}for(let p=0;p<n;p++)if(z[p])arcs.push([p,aux,z[p]]);return{n,V:aux+1,t:aux,M,arcs}}
 function reach(G,starts,skip,reverse){let adj=reverse?G.rev:G.adj,seen=Array(G.V).fill(false),q=[],scans=0;for(let x of starts)if(!seen[x]){seen[x]=true;q.push(x)}for(let i=0;i<q.length;i++)for(let [w,id] of adj[q[i]]){scans++;if(id!==skip&&!seen[w]){seen[w]=true;q.push(w)}}return{seen,scans}}

function index(G){
 G.adj=Array.from({length:G.V},()=>[]);G.rev=Array.from({length:G.V},()=>[]);
 G.arcs.forEach(([u,v],i)=>{G.adj[u].push([v,i]);G.rev[v].push([u,i])});
 const n=G.V,t=G.t,seen=Array(n).fill(false),post=[],stack=[[t,0]];
 const d=stats.dom??(stats.dom={vertices:0,arcs:0,dfsScans:0,predScans:0,intersectSteps:0,bridgeScans:0,treeVertices:0,lcaCells:0,passes:0,maxPasses:0,queryLcaTests:0,domainChecks:0,domainVertexChecks:0,referenceDeletionScans:0,genericGraphs:0,genericRoots:0,largestGraph:0,storedBridgeDomainBits:0});
 d.vertices+=n;d.arcs+=G.arcs.length;d.largestGraph=Math.max(d.largestGraph,n);
 seen[t]=true;
 while(stack.length){let top=stack[stack.length-1],u=top[0];if(top[1]===G.rev[u].length){post.push(u);stack.pop();continue}let v=G.rev[u][top[1]++][0];d.dfsScans++;if(!seen[v]){seen[v]=true;stack.push([v,0])}}
 ck(post.length===n,"all vertices reach sink");const order=post.reverse(),pos=Array(n);order.forEach((v,i)=>pos[v]=i);
 const par=Array(n).fill(-1);par[t]=t;
 function intersect(a,b){while(a!==b){if(pos[a]>pos[b])a=par[a];else b=par[b];d.intersectSteps++}return a}
 let changed=true,passes=0;
 while(changed){changed=false;passes++;for(let v of order.slice(1)){let p=-1;for(let [u] of G.adj[v]){d.predScans++;if(par[u]<0)continue;p=p<0?u:intersect(p,u)}ck(p>=0,"processed predecessor");if(p!==par[v]){par[v]=p;changed=true}}}
 d.passes+=passes;d.maxPasses=Math.max(d.maxPasses,passes);
 const children=Array.from({length:n},()=>[]),tin=Array(n),tout=Array(n),depth=Array(n).fill(0),treeOrder=[];for(let v of order.slice(1))children[par[v]].push(v);
 let clock=0;const treeStack=[[t,0]];tin[t]=clock++;treeOrder.push(t);
 while(treeStack.length){let x=treeStack[treeStack.length-1],u=x[0];if(x[1]===children[u].length){tout[u]=clock;treeStack.pop();continue}let v=children[u][x[1]++];tin[v]=clock++;depth[v]=depth[u]+1;treeOrder.push(v);treeStack.push([v,0])}
 d.treeVertices+=n;const anc=(a,b)=>tin[a]<=tin[b]&&tin[b]<tout[a];
 const count=Array(n).fill(0),sole=Array(n).fill(-1);
 // Reverse arc (v -> u) enters subtree(u) from outside iff u does not dominate v.
 for(let [id,[u,v,c]] of G.arcs.entries()){d.bridgeScans++;if(u!==t&&!anc(u,v)){count[u]++;sole[u]=id}}
 const mark=Array(n).fill(-1),nearest=Array(n).fill(-1);let B=0;
 for(let u of treeOrder){if(u!==t&&count[u]===1&&G.arcs[sole[u]][2]===1){mark[u]=sole[u];B++;d.storedBridgeDomainBits+=n}nearest[u]=mark[u]>=0?u:u===t?-1:nearest[par[u]]}
 stats.activeBridges+=B;
 // The marked-ancestor query requires no binary lifting table.
 // Independent audit, not part of index build: exact per-arc removal domain.
 for(let id=0;id<G.arcs.length;id++){let [u,,c]=G.arcs[id];if(c!==1)continue;stats.unitEdges++;const r=reach(G,[t],id,true);d.referenceDeletionScans+=r.scans;d.domainChecks++;for(let v=0;v<n;v++){ck(!r.seen[v]===(mark[u]===id&&anc(u,v)),"exact bridge domain");d.domainVertexChecks++}}
 return{length:B,anc,mark,nearest,par,tin,tout};
}
function query(G,B,root,record){
 const R=ports(root,G.n),d=stats.dom;let lo=R[0],hi=R[0];
 if(record){d.queryRootVisits=(d.queryRootVisits??0)+R.length;d.queryMarkTests??=0;d.queryMarkClimbs??=0}
 for(let p of R.slice(1)){if(B.tin[p]<B.tin[lo])lo=p;if(B.tin[p]>B.tin[hi])hi=p}
 let b=B.nearest[lo];
 while(b>=0){if(record)d.queryMarkTests++;if(B.anc(b,hi))break;if(record)d.queryMarkClimbs++;b=B.nearest[B.par[b]]}
 if(b<0)return null;
 let r=reach(G,R,B.mark[b],false);if(record)stats.bridgeQueryReachScans+=r.scans;
 ck(!r.seen[G.t]&&r.seen.every((x,i)=>!x||B.anc(b,i)),"root bridge");
 let cut=sum(G.arcs.map(([u,v,c])=>r.seen[u]&&!r.seen[v]?c:0));ck(cut===1,"unit cut certificate");
 return{value:1,U:r.seen.slice(0,G.n).reduce((a,x,i)=>a|(x?1<<i:0),0)}
}
 function cold(G,root){let s=G.V,edges=G.arcs.concat(ports(root,G.n).map(p=>[s,p,G.M]));let f=flow(G.V+1,edges,s,G.t);return{...f,U:f.reach.slice(0,G.n).reduce((a,x,i)=>a|(x?1<<i:0),0)}}
 function reference(c,E,v){let N=1<<c.length,h=Array(N).fill(0);for(let u=1;u<N;u++){h[u]=sum(c.map((x,p)=>u&(1<<p)?x:0))-sum(v.map((x,j)=>sub(E[j],u)?x:0));ck(h[u]>=1,"strict Hall")}return root=>{let value=Infinity,U=N-1;for(let u=1;u<N;u++)if(sub(root,u)){if(h[u]<value){value=h[u];U=u}else if(h[u]===value)U&=u}return{value,U}}}
 function state(c,E,v,roots,all){let G=quotient(c,E,v),B=index(G),ref=reference(c,E,v);stats.states++;for(let root of roots){let a=ref(root),b=query(G,B,root,true),f=cold(G,root);stats.roots++;stats.cutChecks++;ck(a.value===f.value&&a.U===f.U,"cold ref");ck((b!==null)===(a.value===1),"bridge decision");stats.coldRootSearchScans+=f.scans;stats.coldRootAugments+=f.aug;if(b){ck(b.U===a.U,"least unit cut");stats.unitQueries++}else{stats.nonunitQueries++;stats.hybridFallbackSearchScans+=f.scans;stats.hybridFallbackAugments+=f.aug}}if(all)for(let r=1;r<(1<<c.length);r++){let a=ref(r),b=query(G,B,r,false);ck((b!==null)===(a.value===1)&&(!b||b.U===a.U),"arbitrary root");stats.arbitraryRootChecks++;if(b)stats.arbitraryTightRoots++}}
 for(let {n,m,c,N,M,A} of models){const pop=new Uint8Array(M),cap=new Int16Array(N),L=new Int32Array(N);for(let z=1;z<M;z++)pop[z]=pop[z>>1]+(z&1);for(let u=1;u<N;u++){for(let p=0;p<n;p++)if(u&(1<<p))cap[u]+=c[p];for(let j=0;j<m;j++)if(sub(A[j].e,u))L[u]|=1<<j}const ok=new Uint8Array(M);for(let z=0;z<M;z++){ok[z]=1;for(let u=1;u<N;u++)if(pop[z&L[u]]>=cap[u]){ok[z]=0;break}stats.originalSubsets++}let groups=new Map();for(let j=0;j<m;j++)groups.set(A[j].e,(groups.get(A[j].e)||0)|(1<<j));let E=[...groups.keys()],H=[...groups.values()],vec=z=>H.map(h=>pop[h&z]),first=true;for(let tr=0;tr<8;tr++){let P=rnd(M),F=(M-1)^P,R=rnd(M)&P,R2=rnd(M)&P;if(!ok[R]||!ok[R2]){stats.rejectedPairs++;continue}stats.legalSiblingPairs++;let roots=E.filter((_,j)=>vec(F)[j]);if(!roots.length)continue;state(c,E,vec(R),roots,first);first=false;state(c,E,vec(R2),roots,false)}}
 // Nested unit bridges and a two-root union crossing independent tight components.
 const structured=[];
 for(let n=2;n<=10;n++){let c=Array(n).fill(1),E=[],v=[];for(let p=0;p<n-1;p++){E.push((1<<p)|(1<<(p+1)));v.push(1)}let G=quotient(c,E,v),B=index(G),ref=reference(c,E,v);for(let r=1;r<(1<<n);r++){let a=ref(r),b=query(G,B,r,false);ck(a.value===1&&b&&b.U===a.U,"chain");stats.structuredChecks++}structured.push({n,kind:"path",bridges:B.length})}
 for(let n=2;n<=10;n++){let c=Array(n).fill(1),G=quotient(c,[],[]),B=index(G),ref=reference(c,[],[]);for(let r=1;r<(1<<n);r++){let a=ref(r),b=query(G,B,r,false);ck((b!==null)===(a.value===1)&&(!b||b.U===a.U),"disjoint");stats.structuredChecks++}structured.push({n,kind:"isolated",bridges:B.length})}

function generic(){
 const d=stats.dom;
 // Every graph has a sink-reaching backbone. Add cycles, parallel arcs and nonunit edges.
 for(let n=2;n<=8;n++)for(let rep=0;rep<100;rep++){
   let arcs=[];for(let u=0;u<n;u++)arcs.push([u,u+1+rnd(n-u),1+rnd(3)]);
   for(let j=0;j<3*n;j++){let u=rnd(n+1),v=rnd(n+1);if(u!==v)arcs.push([u,v,1+rnd(3)])}
   const G={n,V:n+1,t:n,arcs,M:1+sum(arcs.map(a=>a[2]))},B=index(G);d.genericGraphs++;
   const h=Array(1<<n).fill(0);for(let s=1;s<h.length;s++)for(let [u,v,c] of arcs)if((s&(1<<u))&&!(s&(1<<v)))h[s]+=c;
   for(let r=1;r<h.length;r++){let val=Infinity,U=h.length-1;for(let s=r;s<h.length;s++)if(sub(r,s)){if(h[s]<val){val=h[s];U=s}else if(h[s]===val)U&=s}let a=query(G,B,r,false);ck((a!==null)===(val===1)&&(!a||a.U===U),"generic root");d.genericRoots++}
 }
 // Large exact chain; all bridge domains are independently checked by deletion.
 for(let n of [100,500]){let G={n,V:n+1,t:n,M:n+1,arcs:Array.from({length:n},(_,i)=>[i,i+1,1])};let B=index(G);ck(B.length===n,"large chain bridge count");for(let i=0;i<n;i++)ck(B.mark[i]===i&&B.nearest[i]===i,"large chain nearest");d.genericGraphs++}
}
 generic();
 return{stats,structured,mismatches:0,scope:"GCS pinned deterministic replay; reverse CHK dominators plus single incoming arc test, extreme preorder roots and marked-ancestor climb (no binary lifting); independent per-unit-edge deletion audit; additional 700 generic seeded graphs and 2 long chains. Counters distinguish reference audit and index work. No wall time or bytes claimed."}
}
console.log(JSON.stringify(replay(),null,2));
