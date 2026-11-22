#!/usr/bin/env node
// EC49FWV; frozen BRC16943; arithmetic is exact integer arithmetic.
// Run: node EC49FWV_PHASE_ALIAS_VERIFY.js
const verify = function verify() {
 const mod=(x,m)=>(x%m+m)%m;
 const gcd=(a,b)=>b?gcd(b,a%b):a;
 const inv=(a,m)=>{for(let x=1;x<m;x++)if(mod(a*x,m)===1)return x;throw Error("inverse missing")};
 const p10=(H,N)=>{
   const h=mod(H,10),n=mod(N,10);
   if(h%5===0&&n%5===0)return false;
   const slope=h%5===0?5:mod(n*inv(h,5),5);
   return [[ [3],[0,3,4,5] ],[ [2,3,4,5],[2,3] ]][h%2][n%2].includes(slope);
 };
 const assert=(x,msg)=>{if(!x)throw Error(msg)};
 const pop=x=>{let n=0;while(x){n+=x&1;x>>=1}return n};
 const bit=(m,t)=>((m>>t)&1);
 const masks=new Set();let directions=0;
 for(let a=0;a<10;a++)for(let y=0;y<10;y++){
   if(gcd(gcd(a,y),10)!==1)continue;
   directions++;
   let root=null;
   for(let h=0;h<10&&root===null;h++)for(let n=0;n<10;n++)
     if(mod(y*h-a*n+1,10)===0){root=[h,n];break}
   assert(root!==null,"missing primitive root");
   let u=0;for(let t=0;t<10;t++)if(p10(root[0]+a*t,root[1]+y*t))u|=1<<t;
   masks.add(u);
 }
 assert(directions===72&&masks.size===50,"frozen input mismatch");
 let periods=0,direct=0,shifts=0,aliases=0,minGap=99,minOneHole=999,minFull=999;
 const gapCounts={2:0,4:0,6:0,8:0},examples={};
 const corr=(m,n)=>Array.from({length:n},(_,c)=>{
   let count=0;for(let t=0;t<n;t++)count+=bit(m,t)*bit(m,mod(c-t,n));return count
 });
 for(const u of masks){
   const ku=corr(u,10),mu=pop(u);
   for(let d=1;d<10;d++)if(ku.every((x,c)=>x===ku[mod(c-d,10)]))periods++;
   let u5=0;for(let t=0;t<10;t++)if(bit(u,mod(t-5,10)))u5|=1<<t;
   const gap=pop(u^u5);
   assert(gapCounts[gap]!==undefined,"unexpected half-turn gap "+gap);
   gapCounts[gap]++;minGap=Math.min(minGap,gap);
   if(examples[gap]===undefined)examples[gap]=u;
   for(const hole of [null,...Array.from({length:11},(_,j)=>j)]){
     const v=hole===null?2047:2047^(1<<hole),mv=pop(v),kv=corr(v,11),mass=mu*mv;
     const spec=Array.from({length:110},(_,c)=>2*(mass-ku[c%10]*kv[c%11]));
     const word=Array.from({length:110},(_,t)=>bit(u,t%10)*bit(v,t%11));
     for(let c=0;c<110;c++){
       let k=0;for(let t=0;t<110;t++)k+=word[t]*word[mod(c-t,110)];
       assert(spec[c]===2*(mass-k),"CRT/direct mismatch");
       direct++;
     }
     let diff=0;for(let t=0;t<110;t++)if(word[t]!==word[mod(t-55,110)])diff++;
     assert(diff===gap*mv,"half-turn difference mismatch");
     if(hole===null)minFull=Math.min(minFull,diff);else minOneHole=Math.min(minOneHole,diff);
     for(let s=0;s<110;s++){
       let same=true;
       for(let c=0;c<110;c++)if(spec[c]!==spec[mod(c-2*s,110)]){same=false;break}
       const expected=hole===null?s%5===0:(s===0||s===55);
       assert(same===expected,"phase-class mismatch");
       shifts++;if(same)aliases++;
     }
   }
 }
 assert(periods===0 && minGap===2 && minOneHole===20 && minFull===22,"period/gap failed");
 assert([2,4,6,8].every(x=>gapCounts[x]===[10,26,10,4][[2,4,6,8].indexOf(x)]),"gap counts failed");
 // A fixed layout is installed before the trace, hole and phase are observed.
 // For each opposite pair {i,i+5}, place one read in each of min(r+1,11)
 // distinct columns; for r>10, add a second row in r-9 columns.
 const fixed={};
 for(let r=1;r<=20;r++){
   const sites=[];
   for(let i=0;i<5;i++){
     for(let col=0;col<Math.min(r+1,11);col++)sites.push([i,col]);
     if(r>10)for(let col=0;col<r-9;col++)sites.push([i+5,col]);
   }
   const n=sites.length,target=r<=10?5*(r+1):5*(r+2);
   assert(n===target,"layout cardinality failed");
   let worst=Infinity;
   for(let i=0;i<5;i++)for(let hole=0;hole<11;hole++){
     const d=sites.filter(([row,col])=>(row===i||row===i+5)&&col!==hole).length;
     worst=Math.min(worst,d);
     assert(d>=r,"layout not robust");
   }
   assert(worst===r,"claimed optimum not attained");
   fixed[r]={sites:n,least_distance:worst};
 }
 // Directly check all 50 masks, 11 holes, 10 independent mod-10 phase choices
 // against the three operational rates r=1,2,3 and phase-gap edge r=20.
 let measured=0;
 for(const u of masks)for(let h=0;h<11;h++)for(let s=0;s<10;s++){
   for(const r of [1,2,3,10,11,20]){
     let d=0;for(let i=0;i<5;i++){
       for(let c=0;c<Math.min(r+1,11);c++){
         const t=i;
         if(bit(u,mod(t-s,10))!==bit(u,mod(t-s-5,10)) && c!==h)d++
       }
       if(r>10)for(let c=0;c<r-9;c++){
         const t=i+5;
         if(bit(u,mod(t-s,10))!==bit(u,mod(t-s-5,10)) && c!==h)d++
       }
     }
     assert(d>=r,"direct layout failure");
     measured++;
   }
 }
 // Mirror identity is algebraic, and the 110-indexed right spectrum is a
 // deterministic relabeling of the left spectrum for linked opposite drift.
 assert(minOneHole===20,"worst one-hole alias cap");
 return {status:"ALL PASS",frozen_pin:"BRC16943",primitive_direction_classes:directions,distinct_P10_masks:masks.size,
  full_or_single_hole_states:masks.size*12,exact_direct_reflection_values:direct,exact_spectral_shift_tests:shifts,
  spectral_self_alias_tests:aliases,nontrivial_P10_autocorrelation_periods:periods,
  opposite_row_difference_histogram:gapCounts,example_masks:examples,
  minimum_alias_distance_full:minFull,minimum_alias_distance_single_hole:minOneHole,
  fixed_optimum_distances:fixed,exact_fixed_layout_cross_checks:measured,
  scope:"known reference word; unknown cyclic sensor phase; complete indexed defect spectrum; Boolean site probes",
  independent_review:false};
};
const result=verify();
console.log(JSON.stringify(result,null,2));
