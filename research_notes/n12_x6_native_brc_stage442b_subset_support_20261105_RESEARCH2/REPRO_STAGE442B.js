"use strict";
// Stage442-B: exact finite automaton for two restricted-original X6 path sources.
const DIRS="ABCDEFGHIJKL";
function ok(x,s){if(!x)throw Error(s)}
function configs(n,k){
 let out=[];
 function walk(i,j,last,s){if(i===n){if(j===k)out.push(s);return}
 for(let x=0;x<=(i>0&&i<n-1&&!last?1:0);x++)
 if(j+x<=k)walk(i+1,j+x,x,s+x)}
 walk(0,0,0,"");return out
}
function setup(m,n,k,l,K,p,q,r,s){
 ok(p<m&&q<n&&K>=0&&K<=Math.min(m,n),"invalid setup");
 return {m,n,k,l,K,p,q,r,s,N:Math.max(m,n),t:Math.min(m,n),
 d:Math.min(m,n)-K,c:Math.min(m-p,n-q)}
}
function label(M,i,x,y){
 let s="";
 if(i>=M.m-M.p&&i<=M.m)s+="a"+x;
 if(i>=M.n-M.q&&i<=M.n)s+="b"+y;
 if(M.s&&i>=M.n-M.q+1&&i<=Math.min(M.m,M.n+M.s))s+="A"+x;
 if(M.r&&i>=M.m-M.p+1&&i<=Math.min(M.n,M.m+M.r))s+="B"+y;
 if(i>M.c&&i<=M.t)s+="e"+(x===y?1:0);
 return s||"_"
}
function step(M,i,t,x,y){
 let [a,b,d,u,v]=t;
 if((x&&(i<=1||i>=M.m||u))||(y&&(i<=1||i>=M.n||v)))return null;
 a+=x;b+=y;if(i<=M.t&&x!==y)d++;
 if(a>M.k||b>M.l||d>M.d)return null;
 return [a,b,d,x,y]
}
function moves(M,i,t){
 let out=[];for(let x=0;x<=1;x++)for(let y=0;y<=1;y++){
 let v=step(M,i,t,x,y);if(v)out.push([label(M,i,x,y),v,x,y])}
 return out
}
function enc(t){return t.join(",")}
function dec(s){return s.split(",").map(Number)}
function accept(M,t){return t[0]===M.k&&t[1]===M.l&&t[2]===M.d}
function output(M,a,b){return Array.from({length:M.N},(_,j)=>label(M,j+1,+(a[j]||0),+(b[j]||0)))}
function automaton(M){
 const memo=new Map(),stats={nodes:0,transitions:0};
 function go(i,S){
 const a=[...S].sort(),key=i+"/"+a.join(";");
 if(memo.has(key))return memo.get(key);
 stats.nodes++;
 if(i>M.N){let z={q:a.some(x=>accept(M,dec(x)))?1n:0n,e:[]};memo.set(key,z);return z}
 let groups=new Map();
 for(const t of a)for(const [out,next] of moves(M,i,dec(t))){
 stats.transitions++;if(!groups.has(out))groups.set(out,new Set());
 groups.get(out).add(enc(next))}
 let e=[],q=0n;
 for(const out of [...groups.keys()].sort()){
 let child=go(i+1,groups.get(out));
 if(child.q){e.push([out,child]);q+=child.q}}
 let z={q,e};memo.set(key,z);return z
 }
 let root=go(1,new Set([enc([0,0,0,0,0])]));
 function rank(out){
 let node=root,z=0n;
 for(const sym of out){
 let found=false;for(const [a,child]of node.e){
 if(a===sym){node=child;found=true;break}
 z+=child.q}ok(found,"rank path")}
 ok(node.q===1n,"rank terminal");return z
 }
 function unrank(z){
 ok(z>=0n&&z<root.q,"rank bounds");let out=[],node=root;
 for(let i=1;i<=M.N;i++){
 let found=false;for(const [sym,child]of node.e){
 if(z<child.q){out.push(sym);node=child;found=true;break}
 z-=child.q}ok(found,"unrank step")}
 return out
 }
 return {root,rank,unrank,stats}
}
function codec(M,out){
 const memo=new Map();
 function suffix(i,t){
 let id=i+"/"+enc(t);
 if(memo.has(id))return memo.get(id);
 if(i>M.N){let v=accept(M,t)?1n:0n;memo.set(id,v);return v}
 let v=0n;for(const [sym,next]of moves(M,i,t))
 if(sym===out[i-1])v+=suffix(i+1,next);
 memo.set(id,v);return v
 }
 const init=[0,0,0,0,0],mass=suffix(1,init);
 function rank(a,b){
 let z=0n,t=init;
 for(let i=1;i<=M.N;i++){
 let x=+(a[i-1]||0),y=+(b[i-1]||0),found=false;
 for(const [sym,next,j,k]of moves(M,i,t))if(sym===out[i-1]){
 if(x===j&&y===k){t=next;found=true;break}
 z+=suffix(i+1,next)}
 ok(found,"raw rank")}
 ok(accept(M,t),"raw rank final");return z
 }
 function unrank(z){
 ok(z>=0n&&z<mass,"raw rank bounds");
 let t=init,a="",b="";
 for(let i=1;i<=M.N;i++){
 let found=false;
 for(const [sym,next,x,y]of moves(M,i,t))if(sym===out[i-1]){
 let w=suffix(i+1,next);
 if(z>=w){z-=w;continue}
 if(i<=M.m)a+=x;if(i<=M.n)b+=y;
 t=next;found=true;break}
 ok(found,"raw unrank")}
 return [a,b]
 }
 return {mass,rank,unrank,dp:memo.size}
}
function fiber(M){
 let out=[];
 for(const a of configs(M.m,M.k))for(const b of configs(M.n,M.l)){
 let K=0;for(let i=0;i<M.t;i++)K+=a[i]===b[i]?1:0;
 if(K===M.K)out.push([a,b])}
 return out
}
function test(M){
 let raw=fiber(M),a=automaton(M),classes=new Map(),checked=0,maxDp=0;
 for(const [x,y]of raw){
 let z=output(M,x,y).join("|");
 if(!classes.has(z))classes.set(z,[]);
 classes.get(z).push([x,y])}
 ok(BigInt(classes.size)===a.root.q,"support mismatch");
 for(const [key,items]of classes){
 let out=key.split("|"),c=codec(M,out);
 ok(c.mass===BigInt(items.length),"population mismatch");
 maxDp=Math.max(maxDp,c.dp);
 for(const [x,y]of items){
 let z=a.rank(out);ok(a.unrank(z).join("|")===key,"class inverse");
 let r=c.rank(x,y),v=c.unrank(r);
 ok(v[0]===x&&v[1]===y,"raw inverse");checked++}}
 return {m:M.m,n:M.n,kP:M.k,kQ:M.l,K:M.K,
 budgets:[M.p,M.q,M.r,M.s],raw:raw.length,q:Number(a.root.q),
 masses:[...classes.values()].map(z=>z.length).sort((x,y)=>y-x),
 subsetNodes:a.stats.nodes,nfaTransitions:a.stats.transitions,
 rawInverseChecks:checked,maxSuffixStates:maxDp}
}
function nativeObs(p,q){
 function side(x){
 let v=[0,0,0,0,0,0],J=new Map();
 for(const ch of x){let a=DIRS.indexOf(ch);ok(a>=0,"direction");v[a>>1]+=a%2?-1:1}
 for(let i=1;i<x.length;i++){let t=x[i-1]+x[i];J.set(t,(J.get(t)||0)+1)}
 return [v.join(","),[...J].sort((x,y)=>x[0].localeCompare(y[0])).map(x=>x.join(":")).join(",")]}
 let K=0;for(let i=0;i<Math.min(p.length,q.length);i++)K+=p[i]===q[i];
 return JSON.stringify([p.length,q.length,...side(p),...side(q),K])
}
function futureTraces(M,raw){
 let memo=new Map(),intern=new Map();
 function tree(p,q,a,b,c,d){
 let key=JSON.stringify([p,q,a,b,c,d]);
 if(memo.has(key))return memo.get(key);
 let children=[];
 if(a&&p.length>1)children.push(["p-",tree(p.slice(0,-1),q,a-1,b,c,d)]);
 if(b&&q.length>1)children.push(["q-",tree(p,q.slice(0,-1),a,b-1,c,d)]);
 if(c)for(const z of DIRS)children.push(["p+"+z,tree(p+z,q,a,b,c-1,d)]);
 if(d)for(const z of DIRS)children.push(["q+"+z,tree(p,q+z,a,b,c,d-1)]);
 let sig=JSON.stringify([nativeObs(p,q),children]);
 if(!intern.has(sig))intern.set(sig,intern.size+1);
 let id=intern.get(sig);memo.set(key,id);return id
 }
 let classes=new Map();
 for(const [x,y]of raw){
 let p=x.replaceAll("0","A").replaceAll("1","B");
 let q=y.replaceAll("0","A").replaceAll("1","B");
 let id=tree(p,q,M.p,M.q,M.r,M.s),key=output(M,x,y).join("|");
 if(classes.has(key))ok(classes.get(key)===id,"repair too coarse");
 else classes.set(key,id)}
 ok(new Set(classes.values()).size===classes.size,"repair too fine");
 return {raw:raw.length,classes:classes.size,nativeDirections:DIRS.length,
 completeTraceStates:memo.size,distinctTraceNodes:intern.size}
}
const cases=[
 [8,8,2,1,5,2,1,1,1],[8,8,2,1,7,2,1,1,1],
 [9,7,2,1,4,2,1,2,1],[9,7,2,1,6,2,1,2,1],
 [7,8,1,2,4,1,2,1,2],[7,8,1,2,6,1,2,1,2]];
const summary=cases.map(x=>test(setup(...x)));
const completeTrace=futureTraces(setup(...cases[0]),fiber(setup(...cases[0])));
const report={pass:"STAGE442B_SUBSET_DETERMINIZATION_AND_RECOVERY_PASS",
 model:"native X6, 12 future signed directions, A/B originals, integer POP/APPEND",
 parameters:summary,fullTrace:completeTrace};
if(typeof process!=="undefined"&&process.stdout)process.stdout.write(JSON.stringify(report)+"\n");
