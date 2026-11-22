// EC49FWY: exact finite auxiliary Farey/CRT observer, frozen pin BRC16943.
// No native X6 heartbeat calculation or scientific acceptance is asserted.
const mod=(a,n)=>(a%n+n)%n;
const gcd=(a,b)=>b?gcd(b,a%b):a;
const inverse5=a=>[1,2,3,4].find(x=>a*x%5===1);
const p10=(H,N)=>{const h=mod(H,10),n=mod(N,10);
 if(h%5===0&&n%5===0)return false;
 const slope=h%5===0?5:mod(n*inverse5(h%5),5);
 return [[[3],[0,3,4,5]],[[2,3,4,5],[2,3]]][h%2][n%2].includes(slope);
};
const masks=new Set();let primitive=0;
for(let x=0;x<10;x++)for(let y=0;y<10;y++){
 if(gcd(gcd(x,y),10)!==1)continue;primitive++;
 let root=null;
 for(let h=0;h<10&&root===null;h++)for(let n=0;n<10;n++)
  if(mod(y*h-x*n+1,10)===0){root=[h,n];break;}
 if(!root)throw Error('missing affine root');
 let u=0;for(let t=0;t<10;t++)if(p10(root[0]+x*t,root[1]+y*t))u|=1<<t;
 masks.add(u);
}
if(primitive!==72||masks.size!==50)throw Error('frozen P10 source mismatch');
const histogram={};
for(const u of masks){let d=0;for(let t=0;t<10;t++)d+=((u>>t)&1)!==((u>>mod(t-5,10))&1);
 histogram[d]=(histogram[d]||0)+1;}
if(JSON.stringify([2,4,6,8].map(d=>histogram[d]))!==JSON.stringify([10,26,10,4]))throw Error('P10 gap mismatch');
const crt=Array.from({length:10},()=>Array(11));
for(let t=0;t<110;t++)crt[t%10][t%11]=t;
const h=r=>r<=10?r+1:r+2;
const central=(delta,r,ip)=>{
 const fixed=Array.from({length:11},(_,j)=>j).find(j=>mod(2*j-delta,11)===0);
 const pairs=[],visited=new Set([fixed]);
 for(let j=0;j<11;j++)if(!visited.has(j)){
  const k=mod(delta-j,11);pairs.push([j,k]);visited.add(j);visited.add(k);
 }
 if(pairs.length!==5)throw Error('column orbits');
 let best=null;
 for(let a=0;a<243;a++){
  let z=a,sum=0,max=0;const occ=[];
  for(let k=0;k<5;k++){const v=z%3;z=(z-v)/3;occ.push(v);sum+=v;max=Math.max(max,v);}
  for(let b=0;b<=2;b++){
   const count=sum+b,dist=Math.min(2*sum,2*count-max);
   if(dist<r)continue;
   if(!best||count<best.count||(count===best.count&&b<best.b))best={count,b,occ};
  }
 }
 if(best.count!==Math.ceil(h(r)/2))throw Error('central bound');
 const sites=[];
 for(let k=0;k<5;k++){
  const cnt=best.occ[k];if(!cnt)continue;
  const [c,d]=pairs[k];
  const t=crt[ip][c],mirror=mod(delta-t,110);
  if(mirror%5!==ip||mirror%11!==d||t===mirror)throw Error('central pair');
  sites.push(...[t,mirror].slice(0,cnt));
 }
 const fixedsites=Array.from({length:110},(_,t)=>t).filter(t=>t%5===ip&&t%11===fixed);
 if(fixedsites.length!==2)throw Error('central fixed-column');
 sites.push(...fixedsites.slice(0,best.b));
 return sites;
};
const layout=(delta,r)=>{
 const ip=[0,1,2,3,4].find(i=>mod(2*i-delta,5)===0);
 const sites=central(delta,r,ip),seen=new Set([ip]),H=h(r);
 for(let i=0;i<5;i++){
  if(seen.has(i))continue;
  const j=mod(delta-i,5);if(j===i||seen.has(j))throw Error('row block orbits');
  seen.add(i);seen.add(j);
  for(let c=0;c<Math.min(H,11);c++)sites.push(crt[i][c]);
  for(let c=0;c<Math.max(0,H-11);c++)sites.push(crt[i+5][c]);
 }
 if(seen.size!==5||sites.length!==Math.ceil(5*H/2)||new Set(sites).size!==sites.length)throw Error('site count');
 return sites;
};
let checks=0,minimum_margin=Infinity;
for(let delta=0;delta<110;delta++)for(let r=1;r<=20;r++){
 const sites=layout(delta,r);
 for(let i=0;i<5;i++)for(let missing=0;missing<11;missing++){
  let d=0;
  for(const t of sites){const x=mod(delta-t,110);
   d+=(t%5===i&&t%11!==missing?1:0)+(x%5===i&&x%11!==missing?1:0);
  }
  if(d<r)throw Error('coverage '+JSON.stringify({delta,r,i,missing,d}));
  minimum_margin=Math.min(minimum_margin,d-r);checks++;
 }
}
for(let delta=0;delta<110;delta++){
 const xs=[0,1].flatMap(x=>[0,1].map(y=>mod(delta+55*(x-y),110)));
 if(xs.filter(x=>x===delta).length!==2||xs.filter(x=>x===mod(delta+55,110)).length!==2)
  throw Error('phase parity');
}
console.log(JSON.stringify({status:'ALL_PASS',pin:'BRC16943',directions:primitive,masks:masks.size,
 gap_histogram:histogram,offsets:110,r_values:20,exact_single_pair_missing_column_checks:checks,
 phase_parity_classes:110,minimum_margin,known_delta_fixed:'ceil(5*h(r)/2)',
 known_delta_adaptive_worst:'r',antipodal_pair_fixed:'5*h(r)',
 antipodal_pair_adaptive_worst:'2*r',independent_review:false},null,2));
