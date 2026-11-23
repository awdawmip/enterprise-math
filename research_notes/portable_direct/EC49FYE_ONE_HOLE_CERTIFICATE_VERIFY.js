'use strict';
// EC49FYE — self-contained exact integer enumeration and full readout validation.
// Node: node EC49FYE_ONE_HOLE_CERTIFICATE_VERIFY.js > EC49FYE_ONE_HOLE_CERTIFICATE_OUTPUT.json
// Freeze BRC16943, indexed P10/C11 one-hole product observer.
const assert=(x,s)=>{if(!x)throw new Error(s);};
const fixed=[23,86,91,101,123,157,175,203,211,243,245,281,287,299,301,327,346,367,371,389,394,410,412,447,457,460,486,491,567,599,602,613,615,646,673,697,701,718,721,753,788,789,828,833,857,867,949,965,980,1005];
const mod=(x,n)=>(x%n+n)%n;
const gcd=(a,b)=>b?gcd(b,a%b):a;
const slopeSets={'0,0':[3],'0,1':[0,3,4,5],'1,0':[2,3,4,5],'1,1':[2,3]};
function p10(h,n){
 h=mod(h,10);n=mod(n,10);
 if(h%5===0&&n%5===0)return false;
 let r=5;
 if(h%5!==0){let inv=1;while((inv*h)%5!==1)inv++;r=mod(n*inv,5);}
 return slopeSets[(h%2)+','+(n%2)].includes(r);
}
const seen=new Set();let directions=0;
for(let a=0;a<10;a++)for(let c=0;c<10;c++)if(gcd(gcd(a,c),10)===1){
 directions++;let xy=null;
 for(let x=0;x<10&&xy===null;x++)for(let y=0;y<10;y++)if(mod(c*x-a*y+1,10)===0){xy=[x,y];break;}
 assert(xy!==null,'missing primitive line');
 let u=0;for(let t=0;t<10;t++)if(p10(xy[0]+a*t,xy[1]+c*t))u|=1<<t;
 seen.add(u);
}
assert(directions===72 && JSON.stringify([...seen].sort((a,b)=>a-b))===JSON.stringify(fixed),'frozen P10 atlas changed');
const best=Array(50).fill(999), witnesses=Array(50).fill(null);
let candidates=0,examined=0;
function test(a,low,twice,cost){
 candidates++;
 for(let i=0;i<50;i++){
  const U=fixed[i];if(cost>=best[i] || !(a&U))continue;
  let valid=true;
  for(let j=0;j<50;j++)if(j!==i){
   const V=fixed[j],D=U^V,hit=D&low;
   if(!hit || (!(a&V)&&!(D&twice)&&!(hit&(hit-1)))){valid=false;break;}
  }
  examined++;
  if(valid){best[i]=cost;witnesses[i]={a,low,twice};}
 }
}
// Six possibilities per row: (a,x) in {0,1} x {0,1,2}.
// Enumerate all with objective at most seven.
function dfs(t,a,low,twice,cost){
 if(cost>7)return;
 if(t===10){test(a,low,twice,cost);return;}
 const b=1<<t;
 dfs(t+1,a,low,twice,cost);
 dfs(t+1,a|b,low,twice,cost+1);
 dfs(t+1,a,low|b,twice,cost+1);
 dfs(t+1,a|b,low|b,twice,cost+2);
 dfs(t+1,a,low|b,twice|b,cost+2);
 dfs(t+1,a|b,low|b,twice|b,cost+3);
}
dfs(0,0,0,0,0);
assert(candidates===351240,'search coverage count');
const distribution={5:[],6:[],7:[]};const all=[];
const read=(U,z,t,j)=>Number(Boolean(U&(1<<t)) && z!==j);
let pairChecks=0;
for(let i=0;i<50;i++){
 const U=fixed[i],c=best[i],w=witnesses[i];
 assert(c>=5&&c<=7,'certificate not found / unexpected minimum');
 const sites=[];
 for(let t=0;t<10;t++)if(w.a&(1<<t))sites.push([t,0]);
 for(let t=0;t<10;t++)if(w.low&(1<<t)){
  sites.push([t,t+1]);
  if(w.twice&(1<<t))sites.push([t,(t+1)%10+1]);
 }
 assert(sites.length===c,'witness length');
 assert(new Set(sites.map(v=>v.join(','))).size===c,'duplicate site');
 for(const V of fixed)for(let z=-1;z<11;z++)if(V!==U||z!==0){
  assert(sites.some(([t,j])=>read(U,0,t,j)!==read(V,z,t,j)),'certificate failed '+U+':'+V+':'+z);
  pairChecks++;
 }
 distribution[c].push(U);
 all.push({mask:U,cost:c,at_hole_rows:w.a,nonhole_rows_once_or_more:w.low,nonhole_rows_twice:w.twice,sites:sites.map(([t,j])=>11*t+j)});
}
assert(distribution[5].length===13&&distribution[6].length===34&&distribution[7].length===3,'classification changed');
assert(JSON.stringify(distribution[7])===JSON.stringify([91,701,965]),'hard holes changed');
assert(pairChecks===29950,'pair checks');
console.log(JSON.stringify({schema:'EC49FYE_ONE_HOLE_TWO_MULTICOVER_V1',frozen_science:'BRC16943',status:'ALL_PASS',primitive_directions:directions,masks:50,states:600,candidates,examined,pairChecks,distribution,witnesses:all},null,2));
