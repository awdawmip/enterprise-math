"use strict";
// Exact N-BRC reproduction. Run: node R762CX_VERIFY.js
function verify(){
 const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){const r=a%b;a=b;b=r}return a};
 const max=(...a)=>a.reduce((v,w)=>w>v?w:v),min=(...a)=>a.reduce((v,w)=>w<v?w:v);
 const next=(c,p,q)=>[q*c[1]+p*c[2],p*c[0]+q*c[2],p*c[1]+q*c[0]];
 const H=20,MAX=14;
 let pairs=0,gcd_checks=0,transport_checks=0,horizon_checks=0,nontrivial=0;const examples=[];
 for(let p0=1;p0<=MAX;p0++)for(let q0=1;q0<=MAX;q0++){
   let p=BigInt(p0),q=BigInt(q0);if(gcd(p,q)!==1n)continue;
   pairs++;const D=p+q;let C=[[1n,0n,0n]];
   for(let t=1;t<=H;t++)C.push(next(C[t-1],p,q));
   const Q=[];
   for(let t=0;t<=H;t++){
     const c=C[t],total=D**BigInt(t),g=gcd(gcd(c[0],c[1]),c[2]);
     const want=D%3n===0n&&t>=1?3n**BigInt(Math.floor((t-1)/2)):1n;
     if(g!==want)throw Error(`gcd p=${p} q=${q} t=${t}: ${g} vs ${want}`);
     if(c[0]+c[1]+c[2]!==total)throw Error("BRC positive mass mismatch");
     gcd_checks++;Q.push(total/g);
   }
   for(let h=0;h<=H;h++){
     const M=Q[h]; horizon_checks++;
     for(let t=0;t<=h;t++){
       if(M%Q[t]!==0n)throw Error("endpoint denominator nesting failure");
       if(t===h)continue;
       const a=C[t].map(x=>{const n=x*M,d=D**BigInt(t);if(n%d)throw Error("nonintegral left");return n/d});
       const b=C[t+1].map(x=>{const n=x*M,d=D**BigInt(t+1);if(n%d)throw Error("nonintegral right");return n/d});
       const lo=max(0n,a[2]-b[1],b[0]-a[1]);
       const hi=min(a[2],a[0]-b[1]+a[2],b[0]);
       if(lo>hi)throw Error(`integral transport infeasible p=${p} q=${q} h=${h} t=${t}`);
       transport_checks++;
     }
   }
   if(D%3n===0n)nontrivial++;
   if([[1,2],[1,5],[2,7],[1,1],[1,3]].some(([x,y])=>x===p0&&y===q0)){
     examples.push({weights:[p0,q0],samples:C.slice(0,9).map((c,t)=>({t,count:c.map(String),gcd:String(gcd(gcd(c[0],c[1]),c[2])),endpoint_seed_min:Q[t].toString(),source_word_seed_min:(D**BigInt(t)).toString()}))});
   }
 }
 return {schema:"EM_R762CX_EXACT_INTEGER_BRC_EVIDENCE_V1",model:"oriented_C3_positive_N_BRC_branch_multiplicities",weights:"coprime_positive_p_q",verified_on:"2026-11-17",max_weight:MAX,max_horizon:H,primitive_weight_pairs:pairs,pairs_with_3_dividing_D:nontrivial,gcd_checks,integer_transport_checks:transport_checks,horizon_denominator_checks:horizon_checks,all_pass:true,examples};
}
console.log(JSON.stringify(verify(),null,2));
