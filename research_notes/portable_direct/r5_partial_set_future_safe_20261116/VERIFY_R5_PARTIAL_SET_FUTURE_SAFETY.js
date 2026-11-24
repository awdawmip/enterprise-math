"use strict";
// Exact integer/Boolean checks for the partial named Set future-safety theorem.
// Run with: node VERIFY_R5_PARTIAL_SET_FUTURE_SAFETY.js
function run(){
 const cycle=(k,x)=>{let z=0;for(let i=0;i<k;i++)if((x>>i&1)&&(x>>((i+1)%k)&1))z++;return z};
 const pop=x=>{let c=0;for(;x;x&=x-1)c++;return c};
 function cost(k,J,r,u,h){const D=r&~u,E=r|(J&~D);return h[E]-h[E&~D]}
 function calcCounts(k,J,h,s=2){
   let total=0;
   for(let r=0;r<1<<k;r++){
     const us=[];for(let u=r;;u=(u-1)&r){if(cost(k,J,r,u,h)<=s)us.push(u);if(u===0)break;}
     let c=0;
     for(let S=r;;S=(S-1)&r){
       let n=0;for(const u of us)if(!(u&S))n++;
       c+=(pop(S)%2?-1:1)*(2**n-1);
       if(S===0)break;
     }
     total+=c;
   }
   return total;
 }
 let ringTests=0,hyperTests=0,familyTests=0;
 for(let k=3;k<=6;k++){
  const h=Array.from({length:1<<k},(_,x)=>cycle(k,x));
  for(let J=0;J<1<<k;J++)for(let r=0;r<1<<k;r++)for(let u=r;;u=(u-1)&r){
   const predicted=cost(k,J,r,u,h);let actual=0;
   for(let S=J;;S=(S-1)&J){
    for(let b=S;;b=(b-1)&S){
     const rr=(r&~S)|b,uu=(u&~S)|b,d=h[rr]-h[uu];
     if(d>actual)actual=d;ringTests++;
     if(b===0)break;
    }
    if(S===0)break;
   }
   if(actual!==predicted)throw Error(`ring mismatch ${k} ${J} ${r} ${u} ${actual} ${predicted}`);
   if(u===0)break;
  }
 }
 for(let code=0;code<3**7;code++){
   const w=[];let t=code;for(let i=0;i<7;i++){w.push(t%3);t=Math.floor(t/3);}
   const h=Array.from({length:8},(_,x)=>w.reduce((a,weight,i)=>a+(((x&(i+1))===(i+1))?weight:0),0));
   const k=3;
   for(let J=0;J<8;J++)for(let r=0;r<8;r++)for(let u=r;;u=(u-1)&r){
     const predicted=cost(k,J,r,u,h);let actual=0;
     for(let S=J;;S=(S-1)&J){
       for(let b=S;;b=(b-1)&S){
         const rr=(r&~S)|b,uu=(u&~S)|b,d=h[rr]-h[uu];
         if(d>actual)actual=d;hyperTests++;
         if(b===0)break;
       }
       if(S===0)break;
     }
     if(actual!==predicted)throw Error(`hyper mismatch ${code} ${J} ${r} ${u}`);
     if(u===0)break;
   }
 }
 const counts=[];
 for(let k=3;k<=7;k++){
   const h=Array.from({length:1<<k},(_,x)=>cycle(k,x));
   const m=(1<<k)-1;
   const v={k,none:calcCounts(k,0,h),one:calcCounts(k,1,h),adjacent:calcCounts(k,3,h),all:calcCounts(k,m,h)};
   if(k%2===0)v.opposite=calcCounts(k,1|(1<<(k/2)),h);
   const full=2*3**k-(k+2)*2**(k-1);
   if(v.all!==full)throw Error('full-control identity mismatch k='+k);
   counts.push(v);
   if(k<=4){
      for(let J=0;J<1<<k;J++){
       const target=calcCounts(k,J,h); let actual=0;
       for(let F=1;F<2**(1<<k);F++){
         let r=0;for(let u=0;u<1<<k;u++)if((F/2**u|0)%2)r|=u;
         let safe=true;
         for(let u=0;u<1<<k;u++)if((F/2**u|0)%2 && cost(k,J,r,u,h)>2){safe=false;break}
         if(safe)actual++;
         familyTests++;
       }
       if(actual!==target)throw Error(`family mismatch k=${k} J=${J}: ${actual} vs ${target}`);
      }
   }
 }
 const h6=Array.from({length:64},(_,x)=>cycle(6,x));
 const w={k:6,J:1,r:42,u:0,budget:2,partial:cost(6,1,42,0,h6),all:cost(6,63,42,0,h6)};
 if(w.partial!==2||w.all!==6)throw Error('witness mismatch');
 return {status:"PASS_R5_PARTIAL_SET_FUTURE_SAFETY",frozen_science_pin:"435e77af0d180eac32bd1f9c4c464bc4010b7551",scope:"auxiliary integer cycle source-observer, not native X6",weights:"all 3-vertex hyperedge weight vectors in {0,1,2}^7",ring_command_checks:ringTests,hypergraph_command_checks:hyperTests,family_enumerations:familyTests,counts,witness:w,independent_review:"NOT_REVIEWED"};
}
console.log(JSON.stringify(run(), null, 2));
