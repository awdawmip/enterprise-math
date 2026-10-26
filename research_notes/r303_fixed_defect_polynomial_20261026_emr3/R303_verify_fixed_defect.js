/* R303 exact verified executable, Node.js or compatible modern JS runtime. */
const verify = function verify(){
 const MAX_N=140, MAX_D=7;
 const edges=[[[2,-1,-1],[2,1,-1]],[[0,-1,-1],[0,1,-1]],[[1,1,1],[2,1,-1]]];
 function binom(n,k){if(k<0||n<k)return 0n;let x=1n;for(let j=1;j<=k;j++)x=x*BigInt(n-j+1)/BigInt(j);return x}
 function comp(s,L){const q=L.length;if(q===0)return s===0?1n:0n;const m=L.reduce((a,b)=>a+b,0);return s<m?0n:binom(s-m+q-1,q-1)}
 function block(n,eps,d){let sum=0n;for(let b=1;b<=d+1;b++){const r=d-b+1;for(let mask=0;mask<(1<<b);mask++){const sig=Array.from({length:b},(_,i)=>mask&(1<<i)?-1:1);if(sig.reduce((x,y)=>x*y,1)!==eps)continue;let tail=1;let P=[],M=[];for(let i=b-1;i>=0;i--){(tail===1?P:M).push(sig[i]===-1?2:1);tail*=sig[i]}sum+=comp(r,M)*comp(n-2*b-r,P)}}return sum}
 let states=new Map([["0,1,0,0",1n]]),history=new Map(),identity=0,compchecks=0,lowchecks=0,smpl={};
 for(let n=0;n<=MAX_N;n++){
  const fib=new Map();
  for(const [key,count] of states){const [q,e,k,z]=key.split(",").map(Number);if(q===0){const v=e+","+k;fib.set(v,(fib.get(v)||0n)+count)}}
  if(n>=1){const prev=history.get(n-3)||new Map(),ks=new Set();for(const key of fib.keys())ks.add(Number(key.split(",")[1]));for(const key of prev.keys()){const k=Number(key.split(",")[1]);ks.add(k-1);ks.add(k+1)}for(const k of ks){const v=(fib.get("1,"+k)||0n)-(fib.get("-1,"+k)||0n);const w=(prev.get("1,"+(k+1))||0n)-(prev.get("-1,"+(k-1))||0n);if(v!==w)throw Error("identity "+n+" "+k+" "+v+" "+w);identity++}}
  for(let d=0;d<=MAX_D;d++){const k=2-n+2*d;for(const eps of [1,-1]){const v=fib.get(eps+","+k)||0n,w=block(n,eps,d);if(v!==w)throw Error("block "+n+" "+eps+" "+d+" "+v+" "+w);compchecks++}}
  if(n>=13){const f=(e,d)=>fib.get(e+","+(2-n+2*d))||0n;const x=[[1n,1n],[BigInt(n-5),BigInt(n-6)],[binom(n-7,2),binom(n-8,2)+1n],[binom(n-9,3)+1n,binom(n-10,3)+BigInt(n-8)]];for(let d=0;d<4;d++){if(f(1,d)!==x[d][0]||f(-1,d)!==x[d][1])throw Error("low "+n+" "+d);lowchecks++}}
  if([13,14,40,80,81,140].includes(n)){smpl[n]={};for(let d=0;d<=5;d++){const k=2-n+2*d;smpl[n][d]=[(fib.get("1,"+k)||0n).toString(),(fib.get("-1,"+k)||0n).toString()]}}
  history.set(n,fib);history.delete(n-4);
  if(n===MAX_N)break;const nxt=new Map();for(const [key,value] of states){const [q,e,k,z]=key.split(",").map(Number);for(let bit=0;bit<2;bit++){if(bit===0&&z===1)continue;const [nq,eta,c]=edges[q][bit];const t=nq+","+(e*eta)+","+(eta*k+c)+","+(bit===0?1:0);nxt.set(t,(nxt.get(t)||0n)+value)}}states=nxt
 }
 let poly=0;for(let d=0;d<=MAX_D;d++){const lo=4*d+4;for(const e of [1,-1]){let row=Array.from({length:2*d+8},(_,i)=>block(lo+i,e,d));for(let deg=0;deg<=d;deg++){if(deg===d&&row.some(v=>v!==1n))throw Error("lead "+d+" "+e);row=row.slice(1).map((x,i)=>x-row[i]);}if(row.some(v=>v!==0n))throw Error("poly "+d+" "+e);poly+=2*d+8}}
 return {schema:"EM_R303_INDEPENDENT_JS_VERIFICATION_V1",status:"PASS",max_n:MAX_N,max_defect:MAX_D,all_k_identity_checks:identity,fixed_defect_coeff_checks:compchecks,low_defect_closed_form_checks:lowchecks,polynomial_samples:poly,examples:smpl,mode:"JavaScript BigInt; independently enumerated raw six-edge DP, finite sign-word/composition formula; no floating-point",scope:"positive-count ordered BRC auxiliary model only, no native X6 mapping or phase amplitudes",logical_limit:"the infinite claims require the separately supplied combinatorial proof"};
};
console.log(JSON.stringify(verify(),null,2));
