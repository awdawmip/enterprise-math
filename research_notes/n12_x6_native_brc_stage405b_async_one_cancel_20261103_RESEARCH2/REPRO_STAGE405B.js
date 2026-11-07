// Stage405-B exact integer verifier, Node.js or equivalent JS BigInt runtime.
// Node: node REPRO_STAGE405B.js
const A=1,B=-1,T=3;
const dirs=Array.from({length:6},(_,i)=>[i+1,-(i+1)]).flat();
function keyJ(w) {const m={};for(let i=1;i<w.length;i++){let k=w[i-1]+","+w[i];m[k]=(m[k]||0)+1;}return Object.entries(m).sort().map(x=>x.join(":")).join("|");}
function end(w){let a=Array(6).fill(0);for(const x of w)a[Math.abs(x)-1]+=x>0?1:-1;return a.join(",");}
function sign(w){return w.reduce((a,x)=>a*(x===A?2:x===B?-3:1),1);}
function coinc(p,q){let k=0;for(let i=0;i<Math.min(p.length,q.length);i++)k+=(p[i]===q[i]);return k;}
function obs(p,q){return [p.length,q.length,end(p),end(q),keyJ(p),keyJ(q),coinc(p,q),sign(p),sign(q)].join("#");}
function op(s,a){let [p,q,r,c]=s;if(a[0]==="add")return [[...p,a[1]],[...q,a[2]],r,c];
if(a[0]==="pop")return r||q.length===0?null:[p,q.slice(0,-1),1,c];
if(a[0]==="cancel")return c||p.length<2||q.length<2||p.at(-1)!==-p.at(-2)||q.at(-1)!==-q.at(-2)?null:[p.slice(0,-2),q.slice(0,-2),r,1];
throw Error("unknown action");}
function allWords(n,abc){let out=[[]];for(let i=0;i<n;i++)out=out.flatMap(x=>abc.map(y=>[...x,y]));return out;}
function nativeBRC(n,weighted){let d=new Map([["0,0,0,0,0,0",1n]]);for(let step=0;step<n;step++){let t=new Map();for(const [k,count] of d){let vec=k.split(",").map(Number);for(const a of dirs){let v=[...vec];v[Math.abs(a)-1]+=Math.sign(a);let kk=v.join(",");let ww=weighted?(a===A?2n:a===B?3n:1n):1n;t.set(kk,(t.get(kk)||0n)+count*ww);}}d=t;}return d;}
function verify(){
const ps=["AAABA","AABAA","ABAAA"].map(s=>[...s].map(x=>x==="A"?A:B));
const q=Array(5).fill(A);const fiber=allWords(5,[A,B]).filter(w=>keyJ(w)===keyJ(ps[0])&&end(w)===end(ps[0])&&coinc(w,q)===4);
if(fiber.length!==3||!ps.every(p=>fiber.some(w=>w.join()===p.join())))throw Error("Euler fiber");
if(!ps.every(p=>obs(p,q)===obs(ps[0],q)))throw Error("current observer");
const actions=[["pop"],["cancel"],...([A,B,T].flatMap(a=>[A,B,T].map(b=>["add",a,b])))];
let queue=[[[ps[1],q,0,0],[ps[2],q,0,0],0]], head=0, edges=0;const depth=5;
const visited=new Set();
while(head<queue.length){const [s,t,d]=queue[head++];if(obs(s[0],s[1])!==obs(t[0],t[1]))throw Error("observation mismatch depth "+d);
if(d===depth)continue;
const id=JSON.stringify([s,t]);if(visited.has(id))continue;visited.add(id);
for(const a of actions){const ns=op(s,a),nt=op(t,a);edges++;
if((ns===null)!==(nt===null))throw Error("enabledness mismatch");
if(ns)queue.push([ns,nt,d+1]);}}
for(const i of [1,2]){let s=[ps[0],q,0,0],t=[ps[i],q,0,0];for(const a of [["add",B,B],["cancel"]]){s=op(s,a);t=op(t,a);if(!s||!t)throw Error("witness disabled");}if(obs(s[0],s[1])===obs(t[0],t[1]))throw Error("witness failed");}
let nb=nativeBRC(5,false),wb=nativeBRC(5,true);
if(nb.get("3,0,0,0,0,0")!==105n||nb.get("5,0,0,0,0,0")!==1n||wb.get("3,0,0,0,0,0")!==1040n||wb.get("5,0,0,0,0,0")!==32n)throw Error("native BRC");
if(new Set(ps.map(p=>p.slice(-4).join())).size!==3)throw Error("suffix fibers");
return {marker:"STAGE405B_ONE_CANCEL_STRICT_QUOTIENT_PASS",alphabet:"all native 12 for mathematical proof; verifier appends +E1,-E1,+E3",fiber:["AAABA","AABAA","ABAAA"],current_K:4,exact_classes:[["AAABA"],["AABAA","ABAAA"]],q:2,uniform_suffix4:3,bits:"2 -> 1",depth,explored_nodes:head,explored_action_edges:edges,distinct_prefix_states:visited.size,separating_trace:"APP(-E1,-E1); CANCEL",N5_3E1:"105",N5_5E1:"1",W5_3E1:"1040",W5_5E1:"32"};
}
if(typeof console!=="undefined")console.log(JSON.stringify(verify()));
