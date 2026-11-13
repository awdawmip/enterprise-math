/* R699 exact independent integer verifier. Run: node R699_ANISOTROPIC_PROBE_VERIFY.js */
'use strict';
const N=[24,18,6,12], byS=Array.from({length:61},()=>new Map());
const f=([e,t,c,z])=>[4*e+5*t+z,2*e+2*c+z];
for(let e=0;e<=24;e++)for(let t=0;t<=18;t++)for(let c=0;c<=6;c++)for(let z=0;z<=12;z++){
 const v=[e,t,c,z],s=e+t+c+z;if(!s)continue;
 const key=f(v).join(',');if(byS[s].has(key))throw Error('injectivity '+s);
 byS[s].set(key,v);
}
const total=byS.reduce((n,b)=>n+b.size,0);if(total!==43224)throw Error('population');
function spacing(box,fixV){
 const groups=new Map();
 for(const [k] of box){let [u,v]=k.split(',').map(Number),key=fixV?v:u,val=fixV?u:v;
  if(!groups.has(key))groups.set(key,[]);groups.get(key).push(val);}
 let ans=Infinity;for(const vals of groups.values()){vals.sort((a,b)=>a-b);
  for(let j=1;j<vals.length;j++)ans=Math.min(ans,vals[j]-vals[j-1]);}
 return Number.isFinite(ans)?ans:null;
}
function bounded(s,lo,hi){let v=lo.slice(),r=s-lo.reduce((a,b)=>a+b,0);
 for(let i=0;i<4;i++){let d=Math.min(r,hi[i]-lo[i]);v[i]+=d;r-=d;}
 if(r!==0)throw Error('bounded-fill');return v;
}
function delta(a,b){return f(a).map((x,i)=>Math.abs(x-f(b)[i]));}
function witness(s,d,lo,hi,expected){let x=bounded(s,lo,hi),y=x.map((v,i)=>v+d[i]);
 if(x.reduce((a,b)=>a+b,0)!==s||y.reduce((a,b)=>a+b,0)!==s||
  x.some((v,i)=>v<0||v>N[i])||y.some((v,i)=>v<0||v>N[i])||
  delta(x,y).join(',')!==expected.join(','))throw Error('witness '+s);
 return [x,y];
}
function complement(pair){return pair.map(v=>v.map((x,i)=>N[i]-x));}
const cert=[];for(let s=1;s<=60;s++){
 const box=byS[s],du=spacing(box,true),dv=spacing(box,false);
 let frontier=[],p=null,q=null,expected;
 if(s===1||s===59){expected=[4,null];frontier=[[1,1],[4,0]];
  p=[[0,0,1,0],[0,0,0,1]];q=[[0,0,1,0],[1,0,0,0]];
  if(s===59){p=complement(p);q=complement(q);}
 } else if(s===2||s===58){expected=[3,1];frontier=[[0,1],[3,0]];
  p=witness(s,[1,-1,-1,1],[0,1,1,0],[23,18,6,11],[0,1]);
  q=[[0,0,0,2],[0,1,1,0]];if(s===58)q=complement(q);
 } else if(s<=57){expected=[1,1];frontier=[[0,1],[1,0]];
  p=witness(s,[1,-1,-1,1],[0,1,1,0],[23,18,6,11],[0,1]);
  q=witness(s,[1,-1,-2,2],[0,1,2,0],[23,18,6,10],[1,0]);
 }else{expected=[null,null];if(box.size!==1)throw Error('full total');}
 if(du!==expected[0]||dv!==expected[1])throw Error('axis spacing '+s);
 if(p){let a=delta(...p),b=delta(...q);
  if(a.join(',')!==frontier[0].join(',')||b.join(',')!==frontier[1].join(','))
   throw Error('sharp witness '+s);}
 cert.push({s,n:box.size,min_U_given_same_V:du,min_V_given_same_U:dv,
   pareto:frontier,witnesses:p?[p,q]:null});
}
const result={schema:'EM_R699_ANISOTROPIC_PROBE_V1',status:'R699_ANISOTROPIC_SHARP_PASS',
 input:'R698@93165095e80a0b79759a3e699b7e7342c1e48373',capacities:N,
 histograms_checked:total,totals_checked:60,
 noise:'a=20s*eps3,b=10s*eps8, eps3/eps8 are raw-probability absolute errors',
 sharp_conditions:{'1,59':'a<4 && (a<1 || b<1)',
  '2,58':'a<3 && b<1','3..57':'a<1 && b<1','60':'s determines histogram'},
 by_s:cert};

console.log(JSON.stringify(result,null,2));
