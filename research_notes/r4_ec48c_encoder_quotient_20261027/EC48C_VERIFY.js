"use strict";
// EC48C exact encoder-quotient verifier; all intermediate integers within IEEE-754 safe-integer range for the declared finite domain.
function gcd(a,b){while(b){const t=a%b;a=b;b=t;}return a;}

function rawRatios(P,Q){const m=new Map();for(let j=0;j<P.length;j++){const d=gcd(P[j],Q[j]),a=P[j]/d,b=Q[j]/d;m.set(a+"/"+b,j);}return [...m.values()];}

function signaturePeak(P,Q,H,Y){
 const sig=Array.from({length:H},()=>Array(Y).fill(1));
 let peak=1;const rs=rawRatios(P,Q);
 rs.sort((i,j)=>P[i]*Q[j]-P[j]*Q[i]);
 for(const i of rs){
  for(let h=0;h<H;h++)for(let y=0;y<Y;y++){
   const j=h*Y+y;
   if(P[j]*Q[i]===P[i]*Q[j])sig[h][y]=-1;
  }
  peak=Math.max(peak,new Set(sig.map(r=>r.join(","))).size);
 }
 return peak;
}

function reducedFace(P,Q,H,Y,K,ref){
 const D=P.map((v,j)=>v*Q[ref]-Q[j]*P[ref]);
 const S=D.map(v=>v>0?1:v<0?-1:0);
 const Qt=Q.reduce((a,v,j)=>a+(S[j]===0?v:0),0);
 const n=K**H,profiles=new Map(),pow=Array.from({length:H},(_,h)=>K**h);
 for(let idx=0;idx<n;idx++){
  const f=pow.map(t=>Math.floor(idx/t)%K);
  const mask=Array(K*Y).fill(0),ties=Array(K*Y).fill(0);
  for(let h=0;h<H;h++)for(let y=0;y<Y;y++){
   const j=h*Y+y,z=f[h]*Y+y;
   if(S[j]>0)mask[z]|=1;
   else if(S[j]<0)mask[z]|=2;
   else ties[z]+=Q[j];
  }
  if(mask.some(x=>x===3))continue;
  let lo=0,hi=0;
  for(let z=0;z<K*Y;z++){
   if(mask[z]===1){lo+=ties[z];hi+=ties[z];}
   if(mask[z]===0)hi+=ties[z];
  }
  profiles.set(idx,{mask,lo,hi});
 }
 const seen=new Set(), intervals=[];
 for(const idx of profiles.keys()){
  if(seen.has(idx))continue;
  seen.add(idx);const pending=[idx];let lo=Qt,hi=0;
  while(pending.length){
   const z=pending.pop(),v=profiles.get(z);
   lo=Math.min(lo,v.lo);hi=Math.max(hi,v.hi);
   for(let h=0;h<H;h++){
    const old=Math.floor(z/pow[h])%K;
    for(let m=0;m<K;m++){
     if(m===old)continue;
     const to=z+(m-old)*pow[h],u=profiles.get(to);
     if(!u||seen.has(to))continue;
     if(v.mask.every((a,i)=>(a|u.mask[i])!==3)){
      seen.add(to);pending.push(to);
     }
    }
   }
  }
  intervals.push([lo,hi]);
 }
 intervals.sort((a,b)=>a[0]-b[0]||a[1]-b[1]);
 let reach=0,complete=intervals.length>0;
 for(const [l,u] of intervals){if(l>reach)complete=false;reach=Math.max(reach,u);}
 return {Qt,intervals,components:intervals.length,valid_encoders:profiles.size,complete:complete&&reach===Qt};
}

function runAll(){
 const H=3,Y=2,K=2,N=1<<(H*Y),hist={},exampleP=[1,1,1,1,1,2],exampleQ=[1,1,1,2,1,1];
 let count=0,faces=0,multi=0,eligible=0;
 for(let i=0;i<N;i++){
  const P=Array.from({length:H*Y},(_,z)=>1+((i>>z)&1));
  for(let j=0;j<N;j++){
   const Q=Array.from({length:H*Y},(_,z)=>1+((j>>z)&1));
   count++;
   const pk=signaturePeak(P,Q,H,Y);
   hist[pk]=(hist[pk]||0)+1;
   if(pk<=K)eligible++;
   for(const ref of rawRatios(P,Q)){
    const f=reducedFace(P,Q,H,Y,K,ref);
    faces++;if(f.components>1)multi++;
   }
  }
 }
 return {schema:"EM_R4_EC48C_ENCODER_QUOTIENT_JS_EXACT_V1",model:{H,Y,K,raw_source_values:[1,2],separately_normalized:true},source_pairs:count,ratio_face_checks:faces,multicomponent_faces:multi,hull_histogram:hist,hull_eligible:eligible,example:reducedFace(exampleP,exampleQ,H,Y,K,0),math_status:"Finite integer program only. General theorem requires separate proof."};
}

if(typeof process!=="undefined" && process.stdout)process.stdout.write(JSON.stringify(runAll(),null,2)+"\n");
