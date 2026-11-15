function checker(){
const gcd=(a,b)=>{a=Math.abs(a);b=Math.abs(b);while(b)[a,b]=[b,a%b];return a};
const suites=[
  {name:"K22_cap012",U:2,V:2,E:[[0,0],[0,1],[1,0],[1,1]],max:2},
  {name:"K23_binary",U:2,V:3,E:[[0,0],[0,1],[0,2],[1,0],[1,1],[1,2]],max:1},
  {name:"K33_binary",U:3,V:3,E:Array.from({length:9},(_,i)=>[Math.floor(i/3),i%3]),max:1},
  {name:"K22_named_parallel",U:2,V:2,E:[[0,0],[0,0],[0,1],[1,0],[1,1]],max:1},
  {name:"P3_cap012",U:1,V:1,E:[[0,0],[0,0],[0,0]],max:2}
];
function fiberKey(g,x){const d=new Array(g.U+g.V).fill(0);x.forEach((v,i)=>{d[g.E[i][0]]+=v;d[g.U+g.E[i][1]]+=v});return d.join(",")}
function scc(g,K,x,ban=-1){
 const n=g.U+g.V,R=Array.from({length:n},(_,i)=>Array.from({length:n},(_,j)=>i===j));
 for(let i=0;i<K.length;i++){if(i===ban||K[i]===0)continue;const u=g.E[i][0],v=g.U+g.E[i][1];if(x[i]<K[i])R[u][v]=true;if(x[i]>0)R[v][u]=true}
 for(let k=0;k<n;k++)for(let i=0;i<n;i++)if(R[i][k])for(let j=0;j<n;j++)if(R[k][j])R[i][j]=true;
 const label=new Array(n).fill(-1);let groups=0;
 for(let i=0;i<n;i++){if(label[i]>=0)continue;for(let j=i;j<n;j++)if(R[i][j]&&R[j][i])label[j]=groups;groups++}
 return {label,groups};
}
function latticeGCD(g,K,s,w,ban=-1){
 const n=g.U+g.V,adj=Array.from({length:n},()=>[]);
 for(let e=0;e<K.length;e++){if(e===ban||K[e]===0)continue;const u=g.E[e][0],v=g.U+g.E[e][1];if(s.label[u]!==s.label[v])continue;adj[u].push([v,e,w[e]]);adj[v].push([u,e,-w[e]])}
 const vis=new Array(n).fill(false),potential=new Array(n).fill(0),tree=new Set();
 for(let i=0;i<n;i++){if(vis[i])continue;const q=[i];vis[i]=true;for(let at=0;at<q.length;at++)for(const [v,e,delta] of adj[q[at]])if(!vis[v]){vis[v]=true;potential[v]=potential[q[at]]+delta;tree.add(e);q.push(v)}}
 let d=0;
 for(let e=0;e<K.length;e++){if(e===ban||K[e]===0||tree.has(e))continue;const u=g.E[e][0],v=g.U+g.E[e][1];if(s.label[u]===s.label[v])d=gcd(d,w[e]+potential[u]-potential[v])}
 return d;
}
function bruteGCD(x,F,w){let d=0;for(const y of F){let z=0;for(let i=0;i<w.length;i++)z+=w[i]*(y[i]-x[i]);d=gcd(d,z)}return d}
const counts={capacity_patterns:0,margin_fibers:0,source_tables:0,seed_checks:0,pin_checks:0,observer_gcd_assertions:0,reach_refinement_assertions:0,locality_assertions:0,divisibility_assertions:0,cross_scc_pin_cases:0,same_scc_pin_cases:0,old_scc_unchanged_pin_cases:0},details=[];
for(const g of suites){
 const E=g.E.length,obs=[Array.from({length:E},(_,i)=>i+1),Array.from({length:E},(_,i)=>(i%2?-1:1)*(i*i+1)),Array.from({length:E},(_,i)=>i===0?1:0),new Array(E).fill(0)];
 const local={suite:g.name,capacity_patterns:0,margin_fibers:0,tables:0,pins:0,observer_checks:0};
 for(let config=0;config<(g.max+1)**E;config++){
   local.capacity_patterns++;counts.capacity_patterns++;
   const K=[];let code=config;for(let e=0;e<E;e++){K.push(code%(g.max+1));code=Math.floor(code/(g.max+1))}
   const fibers=new Map();
   function enumerate(i,x){if(i===E){const key=fiberKey(g,x);if(!fibers.has(key))fibers.set(key,[]);fibers.get(key).push(x.slice());return}for(let t=0;t<=K[i];t++){x[i]=t;enumerate(i+1,x)}}
   enumerate(0,new Array(E).fill(0));
   for(const F of fibers.values()){
     local.margin_fibers++;counts.margin_fibers++;local.tables+=F.length;counts.source_tables+=F.length;
     for(const x of F){
       const old=scc(g,K,x),oldG=obs.map(w=>latticeGCD(g,K,old,w));counts.seed_checks++;
       for(let j=0;j<obs.length;j++){if(oldG[j]!==bruteGCD(x,F,obs[j]))throw Error("old lattice mismatch");counts.observer_gcd_assertions++}
       for(let e=0;e<E;e++){if(K[e]===0)continue;counts.pin_checks++;local.pins++;
         const after=scc(g,K,x,e),u=g.E[e][0],v=g.U+g.E[e][1],inter=old.label[u]!==old.label[v],subset=F.filter(y=>y[e]===x[e]);
         if(inter)counts.cross_scc_pin_cases++;else counts.same_scc_pin_cases++;
         let unchanged=true;
         for(let a=0;a<old.label.length;a++)for(let b=0;b<old.label.length;b++){
           const was=old.label[a]===old.label[b],now=after.label[a]===after.label[b];
           if(now&&!was)throw Error("SCC merge after deletion");
           if(old.label[a]!==old.label[u]&&old.label[b]!==old.label[u]&&now!==was)throw Error("unaffected SCC changed");
           if(now!==was)unchanged=false;counts.reach_refinement_assertions++;
         }
         if(unchanged)counts.old_scc_unchanged_pin_cases++;
         if(inter&&(!unchanged||subset.length!==F.length))throw Error("cross SCC pin not redundant");
         counts.locality_assertions++;
         for(let j=0;j<obs.length;j++){
           const afterG=latticeGCD(g,K,after,obs[j],e);
           if(afterG!==bruteGCD(x,subset,obs[j]))throw Error("pinned lattice mismatch "+JSON.stringify({K,x,e,j,afterG}));
           if((oldG[j]===0&&afterG!==0)||(oldG[j]>0&&afterG%oldG[j]!==0))throw Error("gcd non-divisibility");
           counts.observer_gcd_assertions++;local.observer_checks++;counts.divisibility_assertions++;
         }
       }
     }
   }
 }
 details.push(local);
}
const parallel={U:1,V:1,E:[[0,0],[0,0],[0,0]]},K=[2,2,2],x=[1,1,1],w=[1,2,0],old=scc(parallel,K,x),after=scc(parallel,K,x,0);
const a=latticeGCD(parallel,K,old,w),b=latticeGCD(parallel,K,after,w,0);
if(a!==1||b!==2||old.groups!==1||after.groups!==1)throw Error("unchanged SCC witness failed");
const square={U:2,V:2,E:[[0,0],[0,1],[1,0],[1,1]]},k2=[1,1,1,1],x2=[1,0,0,1],w2=[1,0,0,1],s0=scc(square,k2,x2),s1=scc(square,k2,x2,0);
if(s0.groups!==1||s1.groups!==4||latticeGCD(square,k2,s0,w2)!==2||latticeGCD(square,k2,s1,w2,0)!==0)throw Error("SCC split witness failed");
return {schema:"PREFIX813_R6_LOCAL_PIN_SCC_LATTICE_RESULTS_V1",arithmetic:"exact safe integers within declared bounded suites",suites:details,counts,witnesses:{same_scc_but_gcd_jumps:{capacity:K,seed:x,observer_weights:w,old_scc:old.groups,new_scc:after.groups,gcd_before:a,gcd_after:b},scc_split:{capacity:k2,seed:x2,observer_weights:w2,old_scc:s0.groups,new_scc:s1.groups,gcd_before:2,gcd_after:0}},status:"ALL_EXACT_ASSERTIONS_PASSED",limits:"Finite complete enumeration of the five suites; mathematical universality rests on the accompanying proof; no native X6 event admissibility established"};
}
const result=checker();
console.log(JSON.stringify(result,null,2));
