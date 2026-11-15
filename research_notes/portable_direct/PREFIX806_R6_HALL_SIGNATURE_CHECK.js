function capSets(m,n,k){let out=[];function f(a){if(a.length===m*n){out.push(a);return;}for(let t=0;t<=k;t++)f([...a,t])}f([]);return out}

function edges(K){return K.flatMap((row,i)=>row.map((k,j)=>({i,j,k})))}

function weights(m,n){return Array.from({length:m},(_,i)=>Array.from({length:n},(_,j)=>[(i+2*j)%5-2,(2*i+3*j)%7-3]))}

function increase(h,a,v){let k=a.join(",");h.set(k,(h.get(k)||0)+v)}

function equal(a,b){return a.size===b.size&&[...a].every(([k,v])=>b.get(k)===v)}

function formatHist(h){return Object.fromEntries([...h].sort((a,b)=>a[0].localeCompare(b[0])))}

function brute(K,R,S,W){let E=edges(K),r=R.slice(),s=S.slice(),hist=new Map();function walk(z,x,y){if(z===E.length){if(r.every(v=>v===0)&&s.every(v=>v===0))increase(hist,[x,y],1);return;}let {i,j,k}=E[z];for(let v=0;v<=Math.min(k,r[i],s[j]);v++){r[i]-=v;s[j]-=v;walk(z+1,x+v*W[i][j][0],y+v*W[i][j][1]);r[i]+=v;s[j]+=v;}}walk(0,0,0);return hist}

function hallOK(K,R,S){if(R.some(x=>x<0)||S.some(x=>x<0)||R.reduce((a,b)=>a+b,0)!==S.reduce((a,b)=>a+b,0))return false;for(let mask=0;mask<(1<<R.length);mask++){let want=0,have=0;for(let i=0;i<R.length;i++)if(mask>>i&1)want+=R[i];for(let j=0;j<S.length;j++){let v=0;for(let i=0;i<R.length;i++)if(mask>>i&1)v+=K[i][j];have+=Math.min(S[j],v);}if(want>have)return false;}return true}

function separator(K,R,S,W,filter,sr,sc){let m=K.length,n=K[0].length,ar=Array.from({length:sr},(_,i)=>i),br=Array.from({length:m-sr},(_,i)=>i+sr),ac=Array.from({length:sc},(_,j)=>j),bc=Array.from({length:n-sc},(_,j)=>j+sc),ra=new Set(ar),ca=new Set(ac);
let X=edges(K).filter(e=>e.k>0&&(ra.has(e.i)!==ca.has(e.j))).map(e=>({...e,sgn:ra.has(e.i)?1:-1}));
let D=ar.reduce((a,i)=>a+R[i],0)-ac.reduce((a,j)=>a+S[j],0),KA=ar.map(i=>ac.map(j=>K[i][j])),KB=br.map(i=>bc.map(j=>K[i][j])),t=Array(X.length).fill(0),groups=new Map();
let stats={cutFreeBranches:0,cutBalancedAssignments:0,negativeResidualRejects:0,hallTests:0,hallRejected:0,groups:0,componentComputes:0,componentCacheHits:0,polyProducts:0};
function store(){stats.cutBalancedAssignments++;let r=R.slice(),s=S.slice(),w=[0,0];for(let z=0;z<X.length;z++){let e=X[z],v=t[z];r[e.i]-=v;s[e.j]-=v;w[0]+=v*W[e.i][e.j][0];w[1]+=v*W[e.i][e.j][1];}if(r.some(v=>v<0)||s.some(v=>v<0)){stats.negativeResidualRejects++;return;}let a=ar.map(i=>r[i]),b=ac.map(j=>s[j]),c=br.map(i=>r[i]),d=bc.map(j=>s[j]),id=JSON.stringify([a,b,c,d,w]);if(groups.has(id))groups.get(id).count++;else groups.set(id,{a,b,c,d,w,count:1});}
function walk(z,sum){if(z===(X.length?X.length-1:0)){stats.cutFreeBranches++;if(X.length){let e=X[z],v=e.sgn*(D-sum);if(v<0||v>e.k)return;t[z]=v;}else if(D!==0)return;store();return;}for(let v=0;v<=X[z].k;v++){t[z]=v;walk(z+1,sum+v*X[z].sgn);}}walk(0,0);stats.groups=groups.size;
let out=new Map(),cache=new Map();
function message(label,rows,cols,r,s){let k=label+"|"+r.join(",")+"|"+s.join(",");if(cache.has(k)){stats.componentCacheHits++;return cache.get(k);}stats.componentComputes++;let H=brute(rows.map(i=>cols.map(j=>K[i][j])),r,s,rows.map(i=>cols.map(j=>W[i][j])));cache.set(k,H);return H;}
for(let g of groups.values()){if(filter){stats.hallTests++;if(!hallOK(KA,g.a,g.b)||!hallOK(KB,g.c,g.d)){stats.hallRejected+=g.count;continue;}}let A=message("A",ar,ac,g.a,g.b),B=message("B",br,bc,g.c,g.d);for(let [x,v]of A)for(let [y,u]of B){let p=x.split(",").map(Number),q=y.split(",").map(Number);increase(out,[p[0]+q[0]+g.w[0],p[1]+q[1]+g.w[1]],g.count*u*v);stats.polyProducts++;}}
return {hist:out,stats}}

function margins(K){let E=edges(K),r=Array(K.length).fill(0),s=Array(K[0].length).fill(0),out=new Map();function walk(z){if(z===E.length){let k=JSON.stringify([r,s]);if(!out.has(k))out.set(k,[r.slice(),s.slice()]);return;}let e=E[z];for(let v=0;v<=e.k;v++){r[e.i]+=v;s[e.j]+=v;walk(z+1);r[e.i]-=v;s[e.j]-=v;}}walk(0);return out}

function run(){let result={schema:"PREFIX806_EXACT_HALL_SIGNATURE_CHECK_V1",frozen_scientific_input:"f42f2906d77f24085c123f3ccfe9667d41caa96d",assertions:0,capacity_patterns:0,feasible_margin_fibers:0,full_table_occurrences:0,accumulated:{plain:{cutBalancedAssignments:0,groups:0,componentComputes:0,polyProducts:0},filtered:{hallTests:0,hallRejected:0,componentComputes:0,polyProducts:0}},examples:[]};
function ok(b,t){result.assertions++;if(!b)throw Error("ASSERTION_FAILED "+t);}
for(const [m,n,c]of [[2,2,2],[2,3,1]]){let count=0;for(let v of capSets(m,n,c)){count++;result.capacity_patterns++;let K=Array.from({length:m},(_,i)=>v.slice(i*n,i*n+n)),W=weights(m,n);for(let [R,S]of margins(K).values()){result.feasible_margin_fibers++;let H=brute(K,R,S,W),P=separator(K,R,S,W,false,Math.ceil(m/2),Math.ceil(n/2)),Q=separator(K,R,S,W,true,Math.ceil(m/2),Math.ceil(n/2));ok(equal(H,P.hist),"plain");ok(equal(H,Q.hist),"filtered");ok(P.stats.cutBalancedAssignments===Q.stats.cutBalancedAssignments,"crossing");result.full_table_occurrences += [...H.values()].reduce((a,b)=>a+b,0);for(let [mode,stat] of [["plain",P.stats],["filtered",Q.stats]])for(let k of Object.keys(result.accumulated[mode]))result.accumulated[mode][k]+=stat[k];}}result.examples.push({family:m+"x"+n,capacity_patterns:count});}
const four=[{name:"4x4 named-crossing witness",K:[[1,1,1,1],[1,1,1,1],[0,0,1,1],[0,0,1,1]],R:[2,2,1,1],S:[1,1,2,2]},{name:"4x4 dense unit",K:Array.from({length:4},()=>[1,1,1,1]),R:[2,2,2,2],S:[2,2,2,2]},{name:"4x4 stressed boundary",K:Array.from({length:4},()=>[1,1,1,1]),R:[3,1,1,1],S:[1,1,2,2]}];
for(let e of four){let W=weights(4,4),H=brute(e.K,e.R,e.S,W),P=separator(e.K,e.R,e.S,W,false,2,2),Q=separator(e.K,e.R,e.S,W,true,2,2);ok(equal(H,P.hist),e.name+" plain");ok(equal(H,Q.hist),e.name+" Hall");ok(P.stats.hallRejected===0,"plain has no Hall");ok(Q.stats.componentComputes<=P.stats.componentComputes,"Hall compute bound");result.examples.push({name:e.name,K:e.K,R:e.R,S:e.S,named_table_count:[...H.values()].reduce((a,b)=>a+b,0),observer_support:H.size,plain:P.stats,filtered:Q.stats,full_histogram:formatHist(H)});}
result.status="ALL_EXACT_CHECKS_PASS";return result}

console.log(JSON.stringify(run(), null, 2));
