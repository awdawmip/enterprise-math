#!/usr/bin/env node
// R749SPX exact integer source-fiber flux and sign-chamber certificate.
// Usage: node R749SPX_WALSH_CONDITIONAL_TAIL_FLUX_CERT.js > R749SPX_WALSH_CONDITIONAL_TAIL_FLUX_RESULTS.json
function verify(){
  const ok=(v,m)=>{if(!v)throw Error(m)};
  const facets=[[-1,-1,-1,-2],[-1,-1,1,-2],[-1,1,-1,-2],[-1,1,1,-2],[1,-1,-1,-2],[1,-1,1,-4],[1,1,-1,-4],[1,1,1,-2]];
  const P=[];
  for(let h=-2;h<=2;h++)for(let u=-2;u<=2;u++)for(let v=-2;v<=2;v++)if(facets.every(([a,b,c,d])=>a*h+b*u+c*v>=d))P.push([h,u,v]);
  ok(P.length===33,"base lattice points");
  const key=x=>x.join(","), pairs=new Map();
  for(let i=0;i<P.length;i++)for(let j=i;j<P.length;j++){
    let s=key(P[i].map((v,d)=>v+P[j][d]));
    let p=pairs.get(s);if(!p){p={count:0,i,j};pairs.set(s,p)}p.count++;
  }
  const needed=new Set();
  for(const p of pairs.values())if(p.count===1){needed.add(p.i);needed.add(p.j)}
  const F=[...needed].sort((a,b)=>a-b).map(i=>P[i]);
  ok(F.length===25,"forced lattice letters");
  const N=7;
  const dp=letters=>{
    let D=Array.from({length:N+1},()=>new Map());D[0].set("0,0,0",1);
    for(const a of letters)for(let n=1;n<=N;n++)for(const [k,c] of D[n-1]){
      let x=k.split(",").map(Number), y=key(x.map((v,i)=>v+a[i]));
      D[n].set(y,(D[n].get(y)||0)+c);
    }
    return D;
  };
  const MF=dp(F),M0=dp([...F,[0,0,0]]),M1=dp([...F,[-1,0,0]]);
  const levels=[];
  for(let n=1;n<=N;n++){
    let a=M0[n],b=M1[n],slices=new Map();
    for(const s of new Set([...a.keys(),...b.keys()])){
      let [h,u,v]=s.split(",").map(Number),uv=key([u,v]);
      if(!slices.has(uv))slices.set(uv,[]);
      slices.get(uv).push([h,(a.get(s)||0)-(b.get(s)||0)]);
    }
    let multicrossing=0,maxchanges=0,flux_checks=0;
    for(const [uv,row] of slices){
      let [u,v]=uv.split(",").map(Number);
      row.sort((x,y)=>x[0]-y[0]);
      const signs=row.filter(x=>x[1]).map(x=>Math.sign(x[1]));
      let changes=0;for(let i=1;i<signs.length;i++)if(signs[i]!==signs[i-1])changes++;
      if(changes>1)multicrossing++;
      maxchanges=Math.max(changes,maxchanges);
      ok(row.reduce((acc,x)=>acc+x[1],0)===0,"slice count balance");
      let suffix=0;
      for(let h=2*n+1;h>=-2*n-1;h--){
        suffix+=(a.get(key([h,u,v]))||0)-(b.get(key([h,u,v]))||0);
        let flux=0;
        for(let k=1;k<=n;k++)for(let r=0;r<k;r++)flux+=MF[n-k].get(key([h+r,u,v]))||0;
        ok(suffix===flux&&flux>=0,`flux mismatch n=${n} H=${h} U=${u} V=${v}`);
        flux_checks++;
      }
    }
    let total0=[...a.values()].reduce((x,y)=>x+y,0),total1=[...b.values()].reduce((x,y)=>x+y,0);
    ok(total0===total1,"ensemble balance");
    const data={n,multisets:total0,readouts:a.size,slices:slices.size,maximum_sign_changes:maxchanges,multi_crossing_slices:multicrossing,verified_flux_cells:flux_checks,max_fiber_0:Math.max(...a.values()),max_fiber_1:Math.max(...b.values())};
    if(n===3){
      const cert=[-2,-1,0].map(h=>({H:h,M0:a.get(key([h,0,0]))||0,M1:b.get(key([h,0,0]))||0,difference:(a.get(key([h,0,0]))||0)-(b.get(key([h,0,0]))||0)}));
      ok(cert.map(x=>x.difference).join(",")==="3,-6,2"&&multicrossing===3,"three-level witness");
      let mass=0,ksum=0;
      for(const [s,c] of a){let [h,u,v]=s.split(",").map(Number);if(u===0&&v===0)mass+=c}
      for(let k=0;k<=3;k++)for(const [s,c] of MF[3-k]){let [h,u,v]=s.split(",").map(Number);if(u===0&&v===0)ksum+=k*c}
      ok(mass===158&&ksum===32,"conditional k moment");
      data.counterexample=cert;
      data.conditional_0_0={mass,optional_count_sum:ksum,expected_K:"16/79",conditional_W1_TV:"4/1185"};
    }
    if(n===4)ok(multicrossing===0,"n4 single crossing all slices");
    levels.push(data);
  }
  return {schema:"R749SPX_CONDITIONAL_TAIL_FLUX_V1",status:"PASS",frozen_input:"awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389",model:"16-atom auxiliary signed Walsh; (t,s)=(1/10,1/2)",alphabet_size:26,forced_letters:F,formula:"C_n(H,U,V)=sum_{k=1}^n sum_{r=0}^{k-1}MF(n-k,H+r,U,V) >= 0",n1_to_n7_exhaustive:true,levels,review:"AUTHOR_EXACT_NOT_REVIEWED"};
}
process.stdout.write(JSON.stringify(verify(),null,2)+'\n');
