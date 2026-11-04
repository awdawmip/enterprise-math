'use strict';
// Standalone integer certificate for the all-n suffix theorem (fixed gates aab, aba).
const colors=['a','b','B','c','x'], native=['a','A','b','B','c','C','d','D','e','E'];
const group={a:'a',A:'x',b:'b',B:'B',c:'c',C:'c',d:'x',D:'x',e:'x',E:'x'};
const cc=[0,1,0,2,1],dd=[0,0,1,0,1];
function q(g,w){for(let j=3;j>=0;j--)if(w.endsWith(g.slice(0,j)))return j;}
function t(w){for(const x of w){if(x==='b'||x==='B')return 'B';if(x==='c')return 'C';}return 'N';}
function upd(g,s,c){let [q0,t0]=s.split(':');let z=({c:'c',x:'A'})[c]||c;if(t0==='N'){if(c==='b'||c==='B')t0='B';else if(c==='c')t0='C';}return q(g,g.slice(0,Number(q0))+z)+':'+t0;}
function suffixes(n){let a=[''];for(let i=0;i<Math.min(3,n);i++)a=a.flatMap(x=>colors.map(c=>x+c));return a;}
function count(v){return colors.map(c=>[...v].filter(d=>d===c).length);}
function suffix(g,k){let n=k.reduce((a,b)=>a+b,0),r=new Set();for(const v of suffixes(n)){let vc=count(v);if(vc.some((z,i)=>z>k[i]))continue;let rem=k.map((z,i)=>z-vc[i]);let b=rem[1]+rem[2],c=rem[3],qq=q(g,v);if(b)r.add(qq+':B');if(c)r.add(qq+':C');if(!b&&!c)r.add(qq+':'+t(v));}return r;}
function eq(a,b){return a.size===b.size&&[...a].every(x=>b.has(x));}
function key(x){return x.join(',');}
function independent(g,N){let states=new Map([['0,0,0,0,0',new Set(['0:N'])]]),tested=0;
for(let n=0;n<=N;n++){for(const [k,s] of states){let z=suffix(g,k.split(',').map(Number));if(!eq(z,s))throw Error('five-color mismatch '+g+' '+k);tested++;}
let next=new Map();for(const [k,items] of states){let a=k.split(',').map(Number);for(let i=0;i<5;i++){let aa=a.slice();aa[i]++;let id=key(aa),out=next.get(id)||new Set();for(const s of items)out.add(upd(g,s,colors[i]));next.set(id,out);}}states=next;}return tested;}
function nativeBase(s,c){let [n,y,V,W]=s,ix='abcde'.indexOf(c.toLowerCase()),sgn=(c===c.toLowerCase()?1:-1),cross=y[ix]*sgn<0?1:0;let yy=y.slice();yy[ix]+=sgn;return [n+1,yy,V+cc[ix]*cross,W+dd[ix]*cross];}
function baseKey(s){return JSON.stringify(s);}
function fiberWithLattice(g,x){let [n,y,V,W]=x,m=(n-y.reduce((a,b)=>a+Math.abs(b),0))/2,out=new Set();if(!Number.isInteger(m)||m<0)return out;
for(let e=0;e<=Math.min(V,W);e++)for(let d=0;2*d+e<=V;d++){let pa=m-V-W+d+e,pb=V-2*d-e,pc=W-e;if(Math.min(pa,pb,pc)<0)continue;
let k=[pa+Math.max(0,y[0]),pb+Math.max(0,y[1]),pb+Math.max(0,-y[1]),2*pc+Math.abs(y[2]),pa+Math.max(0,-y[0])+2*(d+e)+Math.abs(y[3])+Math.abs(y[4])];for(const s of suffix(g,k))out.add(s);}return out;}
function nativeCheck(g,N){let start=[0,[0,0,0,0,0],0,0],states=new Map([[baseKey(start),{x:start,s:new Set(['0:N'])}]]);let total=0;
for(let n=0;n<=N;n++){for(const {x,s} of states.values()){if(!eq(s,fiberWithLattice(g,x)))throw Error('BRC fiber mismatch '+g+' '+baseKey(x));total++;}
let next=new Map();for(const {x,s} of states.values())for(const c of native){let xx=nativeBase(x,c),id=baseKey(xx),z=next.get(id)||{x:xx,s:new Set()};for(const old of s)z.s.add(upd(g,old,group[c]));next.set(id,z);}states=next;}return total;}
let report={id:'PREFIX-499-JS',checks:[],status:'RUNNING'};
for(const gate of ['aab','aba'])report.checks.push({gate,exact_fivecolor_signatures_n0_to_10:independent(gate,10),native_base_fibers_n0_to_6:nativeCheck(gate,6)});
report.status='ALL_CHECKS_PASS';console.log(JSON.stringify(report));
