"use strict";
// Exact BigInt rational checker for the external BRC N=4 16-leaf two-law source.
const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){[a,b]=[b,a%b]}return a||1n};
const f=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);if(d<0n){n=-n;d=-d}const g=gcd(n,d);return [n/g,d/g]};
const A=(x,y)=>f(x[0]*y[1]+y[0]*x[1],x[1]*y[1]);
const M=(x,y)=>f(x[0]*y[0],x[1]*y[1]);
const N=(x,y)=>A(x,f(-y[0],y[1]));
const B=x=>f(x[0]<0n?-x[0]:x[0],x[1]);
const E=(x,y)=>x[0]===y[0]&&x[1]===y[1];
const LT=(x,y)=>x[0]*y[1]<y[0]*x[1];
const MIN=(x,y)=>LT(x,y)?x:y;
const Z=f(0),O=f(1),H=f(1,2),Q=f(1,4);
const add=(d,k,v)=>d.set(k,A(d.get(k)||Z,v));
const key=a=>JSON.stringify(a),unkey=JSON.parse;
const tv=(p,q)=>{let s=Z;for(const k of new Set([...p.keys(),...q.keys()]))s=A(s,B(N(p.get(k)||Z,q.get(k)||Z)));return M(s,H)};
const equal=(p,q)=>[...new Set([...p.keys(),...q.keys()])].every(k=>E(p.get(k)||Z,q.get(k)||Z));
const collapse=(law,ids)=>{const d=new Map();for(const [k,v] of law){const a=unkey(k);add(d,key(ids.map(i=>a[i])),v)}return d};
const qs=[f(1,6),f(1,3),Q,Q];
const rs=[[f(9,10),f(11,10)],[Q,Q],[f(1,5),f(9,5)],[f(2),f(2)]];
function leafLaw(P){
  const d=new Map();
  for(let si=0;si<4;si++)for(let j=0;j<2;j++)for(let k=0;k<2;k++)
    add(d,key([si,j,k]),M(M(qs[si],P?rs[si][j]:O),Q));
  let total=Z;for(const w of d.values()){if(!LT(Z,w))throw Error("nonpositive leaf");total=A(total,w)}
  if(d.size!==16||!E(total,O))throw Error("leaf normalization");
  return d;
}
function law(P,D,eps){
  const out=new Map();
  for(const [raw,w] of leafLaw(P)){
    const [si,j,k]=unkey(raw);
    if(si!==2){add(out,key([si===0?"A":"E",null,null,null]),w);continue}
    for(let z=0;z<2;z++){
      const sensor=z===j?N(O,eps):eps,ww=M(w,sensor);
      add(out,key(["B",z,"B3","c"]),M(ww,N(O,D)));
      const decision=j===0?"P":"Q",s=j===0?"+":"-";
      add(out,key(["B",z,"B4"+decision+k,s]),M(ww,D));
    }
  }
  return out;
}
function reconstruct(comp){
  const out=new Map();
  for(const [raw,w] of comp){
    const [c,z,s]=unkey(raw);
    const ys=s===null?[[null,O]]:s==="c"?[["B3",O]]:s==="+"?[["B4P0",H],["B4P1",H]]:[["B4Q0",H],["B4Q1",H]];
    for(const [y,v] of ys)add(out,key([c,z,y,s]),M(w,v));
  }
  return out;
}
function sequential(full){
  const out=new Map();
  for(const [raw,w] of full){
    const [c,z,y,s]=unkey(raw);
    const first=y===null?"OUT":y==="B3"?"STOP3":"K"+y.slice(-1);
    const p=first==="OUT"?Z:first==="STOP3"?f(1,3):z===Number(y.slice(-1))?f(2,3):Q;
    const branches=first==="OUT"?[["NONE",O]]:[["ASK:"+y.slice(2,3),p],["SKIP",N(O,p)]];
    for(const [second,v] of branches)add(out,key([c,z,y,s,first,second]),M(w,v));
  }
  return out;
}
function bad(full){
  const out=new Map();for(const [raw,w] of full){
    const [c,z,y]=unkey(raw),v=y==="B3"||y==="B4P0"?"MERGED":y;
    add(out,key([c,z,v]),w);
  }return out;
}
function fmt(x){return String(x[0])+"/"+String(x[1])}
function verify(){
  const ds=[f(1,4),H,f(3,4)],epsilons=[Z,f(1,8),Q,H];
  const ps=leafLaw(true),qs0=leafLaw(false);
  if(ps.size!==16||qs0.size!==16)throw Error("bad source");
  let cases=0;
  for(const D of ds)for(const eps of epsilons){
    const p=law(true,D,eps),q=law(false,D,eps);
    const cp=collapse(p,[0,1,3]),cq=collapse(q,[0,1,3]);
    if(!equal(reconstruct(cp),p)||!equal(reconstruct(cq),q))throw Error("decoder mismatch");
    const t=N(O,M(f(2),eps)),U=M(A(D,M(t,N(O,D))),f(1,10));
    if(!E(tv(p,q),U)||!E(tv(cp,cq),U))throw Error("TV mismatch");
    const ap=sequential(p),aq=sequential(q);
    if(!equal(ap,sequential(reconstruct(cp)))||!equal(aq,sequential(reconstruct(cq))))
      throw Error("adaptive transcript mismatch");
    if(!E(tv(ap,aq),U))throw Error("adaptive TV mismatch");
    const deficit=M(MIN(M(N(O,t),M(D,H)),M(M(f(2),t),N(O,D))),f(1,20));
    if(!E(tv(bad(p),bad(q)),N(U,deficit)))throw Error("lossy TV mismatch");
    cases++;
  }
  const exD=H,exE=Q,tt=N(O,M(f(2),exE));
  const upper=M(A(exD,M(tt,N(O,exD))),f(1,10));
  const loss=M(MIN(M(N(O,tt),M(exD,H)),M(M(f(2),tt),N(O,exD))),f(1,20));
  if(!E(upper,f(3,40))||!E(loss,f(1,160))||!E(N(upper,loss),f(11,160)))
    throw Error("example not exact");
  return [
    "PASS_BRC_N4_THREE_SYMBOL_EXACT_BIGINT",
    "source=16 strictly positive leaves under each P and Q; normalization exact",
    "D_epsilon_parameter_pairs="+cases,
    "full=(C,Z,Y,S) jointly reconstructed from (C,Z,S) under BOTH laws",
    "two_stage_adaptive_transcript_checked=true",
    "example D=1/2 epsilon=1/4: T_full="+fmt(upper)+" T_bad="+fmt(N(upper,loss))+" gap="+fmt(loss),
    "same_actual_K_unobserved_error_for_D_half=1/16",
    "stochastic_binary_minimality_proved_analytically_not_exhausted_by_program"
  ].join("\n");
}
if(typeof require!=="undefined"&&require.main===module)console.log(verify());
