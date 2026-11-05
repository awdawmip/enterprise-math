// PREFIX-523 independent exact-integer native-X6 / BRC / aAc certificate; Node.js.
'use strict';
const A=[[0,1],[2,3],[0,2],[1,3],[1,2],[0,3]],S=[[0,2,5],[0,3,4],[1,2,4],[1,3,5]];
const key=x=>x.join(','), neigh=(star,phase)=>S[star].filter(a=>a!==Math.abs(phase)-1).map(a=>Math.sign(-phase)*(a+1));
function next(s){const [j,p,c]=s,k=S.findIndex((v,i)=>i!==j&&v.includes(Math.abs(c)-1));return [...neigh(j,c).filter(x=>x!==p).map(x=>[j,c,x]),...neigh(k,c).map(x=>[k,c,x])];}
const ST=[];for(let j=0;j<4;j++)for(let a of S[j])for(let z of [-1,1])for(let p of neigh(j,z*(a+1)))ST.push([j,p,z*(a+1)]);
if(ST.length!==48||new Set(ST.map(key)).size!==48)throw Error('48 states');
const D=new Map(ST.map(s=>[key(s),next(s)]));const indeg=new Map(ST.map(s=>[key(s),0]));
for(let s of ST)for(let t of D.get(key(s)))indeg.set(key(t),indeg.get(key(t))+1);
if([...indeg.values()].some(x=>x!==3))throw Error('3-in regular');
function perms(x){return x.length?x.flatMap((v,i)=>perms(x.filter((_,j)=>i!==j)).map(y=>[v,...y])):[[]];}
const MAP=perms([0,1,2,3]).map(g=>A.map(e=>A.findIndex(f=>key(f)===key(e.map(v=>g[v]).sort((x,y)=>x-y)))));
function target(map){const a=map.indexOf(0)+1,c=map.indexOf(2)+1,j=S.findIndex(x=>x.includes(a-1)&&x.includes(c-1));return [j,a,-c];}
function micro(s,t,b){return b===0?[-s[2],t[2]]:[t[2],-s[2]];}
function col(x,m){let a=m[Math.abs(x)-1];return a===0?(x>0?'a':'A'):a===2?'c':'_';}
function hits(w,m){let c=w.map(x=>col(x,m)).join(''),q=0;for(let i=4;i<=c.length;i+=2)if(c.slice(i-3,i)==='aAc')q++;return q;}
let local=0;for(const map of MAP){const T=key(target(map));let n=0;for(let s of ST)for(let t of D.get(key(s)))for(let b=0;b<2;b++)for(let u of D.get(key(t)))for(let c=0;c<2;c++){
const w=[...micro(s,t,b),...micro(t,u,c)],h=hits(w,map),pred=key(u)===T&&b===0&&c===0;
if((h===1)!==pred)throw Error('local gate');if(pred)n++;
let p=(w)=>{let pos=Array(6).fill(0),neg=Array(6).fill(0);for(let x of w)(x>0?pos:neg)[Math.abs(x)-1]++;return pos.map((x,i)=>Math.min(x,neg[i]));};
if(key(p(w))!==key(p([...micro(s,t,1-b),...micro(t,u,1-c)])))throw Error('BRC micro branch');local++;
}if(n!==9)throw Error('9 hits');}
const T=target(MAP[0]),axis=MAP[0].indexOf(0)+1;
function dp(d){let X=new Map();for(let s of ST)X.set(JSON.stringify([s,2,0,0,0]),1n);
for(let i=1;i<=d;i++){let Y=new Map();for(let [k,v] of X){let [s,prev,pos,neg,h]=JSON.parse(k);for(let t of D.get(key(s))){let pp=Number(-s[2]===axis)+Number(t[2]===axis),mm=Number(-s[2]===-axis)+Number(t[2]===-axis);
for(let b=0;b<2;b++){let add=Number(i>1&&prev===0&&b===0&&key(t)===key(T)),zz=JSON.stringify([t,b,pos+pp,neg+mm,h+add]);Y.set(zz,(Y.get(zz)||0n)+v);}}}X=Y;}
let H=new Map(),sum=0n,pair=0n;for(let [k,v] of X){let [s,b,plus,minus,h]=JSON.parse(k),p=Math.min(plus,minus);if(h>p||h>Math.floor((d+2)/4))throw Error('gate BRC bound');H.set(h,(H.get(h)||0n)+v);sum+=BigInt(h)*v;pair+=BigInt(h*(h-1)/2)*v;}return {H,sum,pair};}
let ret=[1n],P=new Map([[key(T),1n]]);for(let i=1;i<=16;i++){let Q=new Map();for(let [s,v] of P)for(let t of D.get(s)){let k=key(t);Q.set(k,(Q.get(k)||0n)+v);}P=Q;if(i%2===0)ret.push(P.get(key(T))||0n);}
if(key(ret.slice(0,5))!=='1,0,5,28,297')throw Error('prior return counts');for(let m=0;m+5<ret.length;m++)if(ret[m+5]!==5n*ret[m+4]+26n*ret[m+3]+78n*ret[m+2]+135n*ret[m+1]-243n*ret[m])throw Error('return recurrence');
let moments=[];for(let d=2;d<=10;d++){let r=dp(d),expected=9n*BigInt(d-1)*6n**BigInt(d-2),pair=0n;for(let m=2;2*m+2<=d;m++)pair+=BigInt(d-2*m-1)*2n**BigInt(2*m-4)*ret[m]*6n**BigInt(d-2*m);
if(r.sum!==expected||r.pair!==pair)throw Error('moment mismatch '+d);
moments.push([d,r.sum.toString(),r.pair.toString(),[...r.H].sort((a,b)=>a[0]-b[0]).map(([h,c])=>[h,c.toString()])]);}
const result={verdict:'ALL_CHECKS_PASS',states:48,charts:MAP.length,local_two_macro_checks:local,even_phase_returns:ret.map(String),joint_BRC_event_moments: moments,
theorem:'all finite d; symbolic native X6 signed microtraces; exact BRC pairs; aAc gate; no physical time claim'};
console.log(JSON.stringify(result,null,2));
