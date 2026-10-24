"use strict";
// Exact support-mask recurrence and independent closed-form validation.
// Auxiliary finite-label BRC probability, NOT native X6 physics.
const assert=(ok,msg)=>{if(!ok)throw Error(msg)};
const pow=(a,n)=>BigInt(a)**BigInt(n);
const N=(u,v)=>pow(2,u+v)+2n*pow(5,u)*pow(4,v)-4n-2n*pow(4,u)*pow(3,v);
const d=(a,u,v)=>a===0?6:5;
function next(dp,a){
  const weights=a===0?[1n,1n,4n]:[1n,1n,3n];
  const result=Array(8).fill(0n);
  for(let mask=0;mask<8;mask++)
    for(let label=0;label<3;label++)
      result[mask|(1<<label)]+=dp[mask]*weights[label];
  return result;
}
const good=dp=>dp[3]+dp[5]+dp[6];
function verify(){
  let dp=Array(8).fill(0n);dp[0]=1n;
  for(let t=0;t<3;t++)dp=next(dp,0);
  assert(N(3,0)===126n && good(dp)===126n,"initial 7/12");
  let nodes=[{u:3,v:0,dp}];
  let checkedWords=0,checkedNext=0;
  for(let depth=0;depth<=10;depth++){
    const successor=[];
    for(const node of nodes){
      const {u,v,dp}=node;
      assert(good(dp)===N(u,v),"mask/formula mismatch");
      checkedWords++;
      for(let a=0;a<2;a++){
        const d0=d(a,u,v),nxt=next(dp,a);
        const u1=u+(a===0?1:0),v1=v+(a===1?1:0);
        const change=good(nxt)-BigInt(d0)*good(dp);
        const closedChange=N(u1,v1)-BigInt(d0)*N(u,v);
        assert(change===closedChange && change<0n,"increment mismatch/sign");
        checkedNext++;
        if(depth<10)successor.push({u:u1,v:v1,dp:nxt});
      }
    }
    nodes=successor;
  }
  assert(checkedWords===2047 && checkedNext===4094,"enumeration coverage");
  let grid=0;
  for(let x=0;x<=50;x++)for(let y=0;y<=50;y++){
    for(let a=0;a<2;a++){
      const u=3+x,v=y,k=BigInt(d(a,u,v));
      const diff=N(u+(a===0?1:0),v+(a===1?1:0))-k*N(u,v);
      assert(diff<0n,"finite grid positivity");
      grid++;
    }
  }
  assert(grid===5202,"grid count");
  assert(N(4,0)-6n*N(3,0)===-6n,"alpha base");
  assert(N(3,1)-5n*N(3,0)===-2n,"beta base");
  return {all_word_prefixes_length_0_to_10:checkedWords,
    mask_recursion_next_action_checks:checkedNext,
    rectangular_future_count_checks: grid, grid_range:"0<=x,y<=50",
    base_closed_occupancy:"7/12",base_increments:["-1/216","-1/540"],
    independent_recursion:"8-support-mask path-weight DP with integer denominators",
    all_future_proof_source:"companion analytic ratio and one-step predecessor proof",
    finite_validation_is_infinite_proof:false};
}
if(typeof module!=="undefined" && require.main===module)
  process.stdout.write(JSON.stringify(verify(),null,2)+"\n");
