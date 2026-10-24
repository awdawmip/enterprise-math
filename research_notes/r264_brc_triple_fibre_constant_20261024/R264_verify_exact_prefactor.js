#!/usr/bin/env node
// R264 author-side exact positive BRC toy-automaton verifier.
// Input R260–R262 frozen q/a/eta/b law. Scope original ordered raw words,
// provenance r and full affine effect (eps,k); t=eps*k is reversible.
// Integer only; no original enterprise_math package or native physical step.
const edges = [
 [[2,-1,-1],[2,1,-1]],
 [[0,-1,-1],[0,1,-1]],
 [[1,1,1],[2,1,-1]]
];
function nxt(q,r,e,t,a) {
 const [nq,eta,b]=edges[q][a]; const ne=e*eta;
 return [nq,a===0?[1,2,2][r]:[0,0,2][r],ne,t+ne*b];
}
function run(){
 let D=new Map([["0,0,1,0",1n]]), out={};
 const selected=new Set([8,13,16,32,64,96,128,140,160,200]);
 let rawWords=0, rawAtoms=0;
 for(let m=0;m<=200;m++){
   if(m<=13){
     // Independent raw-word interpreter vs aggregate integer DP.
     const B=new Map();
     for(let w=0;w<2**m;w++){
       let q=0,r=0,e=1,t=0;
       for(let j=m-1;j>=0;j--){[q,r,e,t]=nxt(q,r,e,t,(w>>j)&1);}
       const key=[q,r,e,t].join(","); B.set(key,(B.get(key)||0n)+1n);
     }
     if(B.size!==D.size)throw Error("raw support mismatch "+m);
     for(const [k,v] of D)if(B.get(k)!==v)throw Error("raw integer mismatch "+m+" "+k);
     rawWords+=2**m;rawAtoms+=B.size;
   }
   let sum=0n;
   for(const [key,v] of D){
     const [q,r,e,t]=key.split(",").map(Number);
     if((t-m)%2!==0 || v<=0n)throw Error("parity or weight");
     if((r===0 && q!==0 && q!==2)||(r===1 && q!==1 && q!==2))
       throw Error("impossible state "+key);
     sum+=v;
   }
   if(sum!==2n**BigInt(m))throw Error("mass invariant "+m);
   if(selected.has(m)){
     const trip=new Map();
     for(const [key,v] of D){
       const [q,r,e,t]=key.split(",").map(Number);
       const key3=[q,e,t].join(",");
       if(!trip.has(key3))trip.set(key3,[0n,0n,0n]);
       trip.get(key3)[r]=v;
     }
     let M=0n,peak=0n;
     for(const [key,v] of trip){
       const minimum=v.reduce((a,b)=>a<b?a:b);
       if(minimum>M) M=minimum;
       if(key.split(",")[0]==="2"&&v[1]>peak)peak=v[1];
     }
     const center=[0,1,2].map(r=>D.get("2,"+r+",1,"+(m%2))||0n);
     out[m]={M:String(M),peak_r1_q2:String(peak),center_r0:String(center[0]),
       center_r1:String(center[1]),center_r2:String(center[2]),peak_equal:M===peak};
   }
   if(m===200)break;
   const E=new Map();
   for(const [key,v] of D){
     const [q,r,e,t]=key.split(",").map(Number);
     for(let a=0;a<2;a++){const k=nxt(q,r,e,t,a).join(",");E.set(k,(E.get(k)||0n)+v);}
   }
   D=E;
 }
 if(out[128].M!=="1426814983819745518311507")throw Error("R261 M128 mismatch");
 if(out[140].M!=="438611399828372525268845634")throw Error("R262 M140 mismatch");
 return {schema:"EM_R264_REMOTE_EXACT_DP_V1",rawWords,rawAtoms,maxLength:200,
    samples:out,analyticProof:"separate mathematical proof; finite checks are not asymptotic proof",
    nativeSourceExecuted:false,independentDriverReviewed:false};
}
if(typeof require!=="undefined" && require.main===module)
  process.stdout.write(JSON.stringify(run(),null,2));
