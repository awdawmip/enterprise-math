'use strict';
// R762DF finite exact author verifier. All congruences use exact integers.
function gcd(a,b){while(b!==0){const t=a%b;a=b;b=t;}return a;}
function mod(a,q){return ((a%q)+q)%q;}
function countInvisible(q, flips){
  const n=6, total=q**5;
  let invisible=0, checkedGradientFrames=0, triangleChecks=0;
  for(let index=0;index<total;index++){
    let z=index;
    const u=[0,0,0,0,0,0];
    for(let i=1;i<n;i++){u[i]=z%q;z=Math.floor(z/q);}
    let good=true;
    for(const flip of flips){
      checkedGradientFrames++;
      for(let i=0;i<n;i++)for(let j=i+1;j<n;j++)for(let k=j+1;k<n;k++){
        triangleChecks++;
        const s=(a)=> a===flip?-1:1;
        const c=(a,b)=>u[b]-u[a];
        const t=s(i)*s(j)*c(i,j)+s(j)*s(k)*c(j,k)+s(k)*s(i)*c(k,i);
        if(mod(t,q)!==0){good=false;break;}
      }
      if(!good)break;
    }
    if(good)invisible++;
  }
  return {invisible, checkedGradientFrames, triangleChecks};
}
function run(){
  const checks=[];
  for(let q=2;q<=8;q++){
    const d=gcd(q,2);
    const observed=[countInvisible(q,[]),countInvisible(q,[0]),countInvisible(q,[0,1])];
    const expected=[q**5,q*d**4,d**5];
    if(observed.some((o,i)=>o.invisible!==expected[i])) throw new Error('FAIL q='+q);
    checks.push({q,d,kernel_sizes:observed.map(o=>o.invisible),
      predicted_kernel_sizes:expected,
      bcr_class_sizes:[q**10,q**14/d**4,q**15/d**5],
      triangle_checks:observed.reduce((a,o)=>a+o.triangleChecks,0)});
  }
  return {status:'PASS',type:'AUTHOR_EXACT_FINITE_VERIFICATION',
    n:6,q_range:[2,8],frames:['identity','flip_axis_0','flip_axis_1'],
    checks,
    total_triangle_checks:checks.reduce((a,x)=>a+x.triangle_checks,0),
    proof_scope:'finite tests of kernel-size theorem; general all-q statement proved separately'};
}
if(typeof module!=='undefined' && require.main===module)console.log(JSON.stringify(run(),null,2));
module.exports={run,countInvisible};
