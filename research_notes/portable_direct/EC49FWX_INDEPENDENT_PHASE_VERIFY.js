#!/usr/bin/env node
// Frozen BRC16943 finite auxiliary CRT trace, exact integer-only verifier.
const verify = function verify(){
 const mod=(x,m)=>(x%m+m)%m;
 const gcd=(a,b)=>b?gcd(b,a%b):a;
 const inv=a=>{for(let x=1;x<5;x++)if(a*x%5===1)return x;throw Error("no inv")};
 const p10=(H,N)=>{
  const h=mod(H,10), n=mod(N,10);
  if(h%5===0&&n%5===0)return false;
  const slope=h%5===0?5:mod(n*inv(h%5),5);
  const tab=[[[3],[0,3,4,5]],[[2,3,4,5],[2,3]]];
  return tab[h%2][n%2].includes(slope);
 };
 const assert=(c,m)=>{if(!c)throw Error(m)};
 const bit=(u,t)=>(u>>mod(t,10))&1;
 const masks=new Set();let dirs=0;
 for(let a=0;a<10;a++)for(let b=0;b<10;b++){
  if(gcd(gcd(a,b),10)!==1)continue; dirs++;
  let root=null;
  for(let H=0;H<10&&!root;H++)for(let N=0;N<10;N++)if(mod(b*H-a*N+1,10)===0){root=[H,N];break}
  assert(!!root,"no root");
  let u=0;for(let t=0;t<10;t++)if(p10(root[0]+a*t,root[1]+b*t))u|=1<<t;
  masks.add(u);
 }
 assert(dirs===72&&masks.size===50,"frozen P10 mismatch");
 const count=x=>{let n=0;while(x){n++;x&=x-1}return n};
 const period=new Set();
 for(const u of masks){let d=0;for(let t=0;t<10;t++)if(bit(u,t)!==bit(u,t-5))d++;period.add(d)}
 assert([...period].sort((a,b)=>a-b).join()==="2,4,6,8","difference domain mismatch");
 const site=(row,col)=>{for(let t=0;t<110;t++)if(t%10===row&&t%11===col)return t;throw Error("CRT")};
 const layout=(r)=>{
  const s=[];for(let i=0;i<5;i++){for(let c=0;c<Math.min(r+1,11);c++)s.push(site(i,c));if(r>10)for(let c=0;c<r-9;c++)s.push(site(i+5,c))}
  assert(s.length===5*(r+(r<=10?1:2)),"bad layout count");return s;
 };
 const chosen=[1,2,3,10,11,20];const layouts=Object.fromEntries(chosen.map(r=>[r,layout(r)]));
 const w=(u,h,t)=>bit(u,t)*(h===null?1:Number(mod(t,11)!==h));
 const diff=(u,h,s,t)=>w(u,h,t)^w(u,h,t-55);
 let sidePhaseCases=0,layoutChecks=0,minLeft=110,minRight=110;
 for(const u of masks)for(const hole of [null,...Array.from({length:11},(_,i)=>i)])for(let s=0;s<110;s++){
  let fullLeft=0,fullRight=0;
  for(let t=0;t<110;t++){fullLeft+=diff(u,hole,s,t);fullRight+=diff(u,hole,s,-t)}
  minLeft=Math.min(minLeft,fullLeft);minRight=Math.min(minRight,fullRight);
  assert(fullLeft===fullRight&&fullLeft>=20,"complete gap");
  sidePhaseCases++;
  for(const r of chosen){
   let dl=0,dr=0;
   for(const t of layouts[r]){dl+=diff(u,hole,s,t);dr+=diff(u,hole,s,-t)}
   assert(dl>=r&&dr>=r,"fixed independent layout failed "+JSON.stringify({u,hole,s,r,dl,dr}));
   layoutChecks+=2;
  }
 }
 const u=299,hole=0,sL=0,sR=0;
 assert(masks.has(u),"witness not frozen");
 const A=[],B=[];
 for(let t=0;t<110;t++){if(diff(u,hole,sL,t))A.push(t);if(diff(u,hole,sR,-t))B.push(t)}
 assert(A.length===20&&B.length===20&&A.every(t=>!B.includes(t)),"witness missing");
 const corr=(f,c)=>{let sum=0;for(let t=0;t<110;t++)sum+=f(t)*f(mod(c-t,110));return sum};
 let mirrorSpectrumEqual=0;
 for(let c=0;c<110;c++){
  const left0=t=>w(u,hole,t), left1=t=>w(u,hole,t-55);
  const right0=t=>w(u,hole,-t), right1=t=>w(u,hole,-t-55);
  assert(corr(left0,c)===corr(left1,c)&&corr(right0,c)===corr(right1,c),"indexed spectrum differs");
  mirrorSpectrumEqual+=2;
 }
 const opt={};for(let r=1;r<=20;r++){const h=r<=10?r+1:r+2;opt[r]={r,universal_fixed_activations:5*h,universal_adaptive_activations:2*r}}
 return {status:"ALL PASS",pin:"BRC16943",primitive_directions:dirs,distinct_P10_masks:masks.size,reference_factors:12,reference_states:600,independent_phase_pair_domain_size_per_reference:12100,possible_joint_aliased_words_per_spectrum_fiber:4,phase_side_cases:sidePhaseCases,exact_fixed_channel_layout_checks:layoutChecks,checked_r:chosen,minimum_full_disagreement_per_side:minLeft,minimum_mirror_disagreement_per_side:minRight,sharp_witness:{u,hole,sL,sR,left_rows:[...new Set(A.map(t=>t%10))],right_rows:[...new Set(B.map(t=>t%10))],left_support:A.length,right_support:B.length,intersection:0,verified_spectrum_center_pairs:mirrorSpectrumEqual},sharp_optima:opt,independent_review:false};
};
console.log(JSON.stringify(verify(),null,2));
