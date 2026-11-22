#!/usr/bin/env node
// Exhaustive exact CRT-weighted census for EC49FWX; no floating-point arithmetic.
const census = function census() {
 const mod=(a,m)=>(a%m+m)%m;
 const gcd=(a,b)=>b?gcd(b,a%b):a;
 const inv=a=>{for(let x=1;x<5;x++)if((a*x)%5===1)return x;throw Error("inverse")};
 const p10=(H,N)=>{const h=mod(H,10),n=mod(N,10);
   if(h%5===0&&n%5===0)return false;
   const slope=h%5===0?5:mod(n*inv(h%5),5);
   return [[ [3],[0,3,4,5] ],[ [2,3,4,5],[2,3] ]][h%2][n%2].includes(slope);
 };
 const masks=new Set();let dirs=0;
 for(let a=0;a<10;a++)for(let b=0;b<10;b++){
  if(gcd(gcd(a,b),10)!==1)continue;dirs++;
  let root;
  for(let h=0;h<10&&root===undefined;h++)for(let n=0;n<10;n++)if(mod(b*h-a*n+1,10)===0){root=[h,n];break}
  let u=0;for(let t=0;t<10;t++)if(p10(root[0]+a*t,root[1]+b*t))u|=1<<t;
  masks.add(u);
 }
 if(dirs!==72||masks.size!==50)throw Error("frozen input");
 const gap=(u)=>{const set=[];for(let x=0;x<10;x++)if(((u>>x)&1)!==((u>>mod(x-5,10))&1))set.push(x);return set};
 const hist={};let rowPairs=0;
 const add=(c,n)=>hist[c]=(hist[c]||0)+n;
 for(const u of masks){const d=gap(u);
  for(let sL=0;sL<10;sL++)for(let sR=0;sR<10;sR++){
   const L=new Set(d.map(x=>mod(sL+x,10))),R=new Set(d.map(x=>mod(-sR-x,10)));
   const k=[...L].filter(x=>R.has(x)).length;
   if(k%2!==0)throw Error("odd overlap");
   add(11*k,121);add(10*k,121);add(9*k,1210);
   rowPairs++;
  }
 }
 const sorted=Object.fromEntries(Object.keys(hist).map(Number).sort((a,b)=>a-b).map(c=>[c,hist[c]]));
 const total=Object.values(hist).reduce((a,b)=>a+b,0);
 if(total!==7260000||hist[0]!==2671680)throw Error("bad exact census");
 const casesForR={};
 for(let r=1;r<=20;r++){const m={};for(const [key,n] of Object.entries(hist)){
 const c=Number(key),a=2*r-Math.min(r,c);m[a]=(m[a]||0)+n;
 }casesForR[r]=Object.fromEntries(Object.entries(m).sort((a,b)=>Number(a[0])-Number(b[0])))}
 return {status:"ALL PASS",frozen_pin:"BRC16943",distinct_P10_masks:masks.size,primitive_directions:dirs,
  row_phase_pair_checks:rowPairs,weight_semantics:"Each of 50 masks, 12 full/one-hole factors and 110^2 independent phase pairs counted once by CRT exact multiplicities",
  weighted_joint_states:total,overlap_histogram:sorted,zero_overlap_count:hist[0],
  zero_overlap_fraction:"2671680/7260000 = 46/125 = 36.8%",
  positive_overlap_count:total-hist[0],positive_overlap_fraction:"79/125 = 63.2%",
  conditioned_adaptive_activation_histograms:casesForR,independent_review:false};
};
console.log(JSON.stringify(census(),null,2));
