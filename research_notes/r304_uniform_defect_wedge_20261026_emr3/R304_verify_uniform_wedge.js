/* R304 exact standalone validator; run: node R304_verify_uniform_wedge.js */
const verify=function verify(){
 const MAX_N=240, FORMULA_N=112, MAX_D=8, edges=[[[2,-1,-1],[2,1,-1]],[[0,-1,-1],[0,1,-1]],[[1,1,1],[2,1,-1]]];
 function binom(n,k){if(k<0||n<k)return 0n;let v=1n;for(let i=1;i<=k;i++)v=v*BigInt(n-k+i)/BigInt(i);return v;}
 function comp(s,L){if(!L.length)return s===0?1n:0n;const v=L.reduce((a,b)=>a+b,0);return s<v?0n:binom(s-v+L.length-1,L.length-1);}
 function block(n,d,e){let v=0n;for(let b=1;b<=d+1;b++){const r=d-b+1;for(let mask=0;mask<2**b;mask++){let sig=[],sg=1;for(let i=0;i<b;i++){let x=mask&(2**i)?-1:1;sig.push(x);sg*=x;}if(sg!==e)continue;let t=1,P=[],M=[];for(let i=b-1;i>=0;i--){(t===1?P:M).push(sig[i]===-1?2:1);t*=sig[i];}v+=comp(r,M)*comp(n-2*b-r,P);}}return v;}
 const fibers=[],ctr={formula:0,ladder:0,remainder:0,window:0,polynomial:0};
 let state=new Map([["0,1,0,0",1n]]);
 for(let n=0;n<=MAX_N;n++){
   let f=new Map();for(let [key,v] of state){let [q,e,k,z]=key.split(",").map(Number);if(q===0){let h=e+","+k;f.set(h,(f.get(h)||0n)+v);}}fibers.push(f);
   if(n===MAX_N)break;
   let next=new Map();for(let [key,v] of state){let [q,e,k,z]=key.split(",").map(Number);for(let a=0;a<2;a++){if(a===0&&z===1)continue;let [qq,eta,c]=edges[q][a];let h=qq+","+(eta*e)+","+(eta*k+c)+","+(a===0?1:0);next.set(h,(next.get(h)||0n)+v);}}state=next;
 }
 function C(n,d,e){return n<0?0n:(fibers[n].get(e+","+(2-n+2*d))||0n);}
 function smallPoly(n,d){const x=BigInt(n);if(d===2)return x-9n;if(d===3)return(x*x-23n*x+128n)/2n;if(d===4)return(x-12n)*(x*x-30n*x+215n)/6n;return(x-14n)*(x-13n)*(x*x-39n*x+372n)/24n;}
 const sample={},interp={};
 for(let n=1;n<=MAX_N;n++){
   if(n<=FORMULA_N)for(let d=0;d<=MAX_D;d++)for(let e of [1,-1]){if(C(n,d,e)!==block(n,d,e))throw Error("block:"+n+":"+d+":"+e);ctr.formula++;}
   if(n>=4)for(let d=0;d<=12;d++){if(C(n,d,1)-C(n,d,-1)!==C(n-3,d-1,1)-C(n-3,d-2,-1))throw Error("ladder:"+n+":"+d);ctr.ladder++;}
   for(let d=2;d<=12;d++)if(n>=4*d+4){
      const D=C(n,d,1)-C(n,d,-1);if(D<=0n)throw Error("finite-positive:"+n+":"+d);ctr.window++;
      const negRem=C(n,d,-1)-binom(n-2*d-4,d),limit=BigInt(d-1)*(2n**BigInt(d-1))*binom(n,d-2);
      if(negRem<0n||negRem>limit)throw Error("remainder:"+n+":"+d+":"+negRem+":"+limit);ctr.remainder++;
   }
   for(let d=2;d<=5;d++)if(n>=4*d+4){if(C(n,d,1)-C(n,d,-1)!==smallPoly(n,d))throw Error("polynomial:"+n+":"+d);ctr.polynomial++;}
   if([13,14,18,19,20,24,40,80,81,112,240].includes(n)){sample[n]={};for(let d=2;d<=5;d++)sample[n][d]=(C(n,d,1)-C(n,d,-1)).toString();}
 }
 for(let d=2;d<=5;d++){let arr=[];for(let n=4*d+4;n<4*d+4+d;n++){const v=block(n,d,1)-block(n,d,-1);if(v!==smallPoly(n,d))throw Error("interpolation:"+n+":"+d);arr.push([n,v.toString()]);}interp[d]=arr;}
 return {schema:"EM_R304_UNIFORM_DEFECT_EXACT_EVIDENCE_V1",status:"PASS",arithmetic:"JavaScript BigInt (no floating point)",scope:"ordered positive-count six-edge BRC auxiliary model; no native X6 correspondence",max_length:MAX_N,first_return_formula_test_through:FORMULA_N,max_defect_formula:MAX_D,checks:ctr,interpolation_points:interp,selected_gap_values:sample,proof_status:"author-side, full mathematical argument in separate proof",driver_review:"NOT_PERFORMED"};
};
console.log(JSON.stringify(verify(),null,2));
