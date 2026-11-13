// Executable exact-integer BRC finite observer checks; Node.js 18+; no dependencies.

function main() {
  const ok=(p,s)=>{if(!p)throw Error("CHECK_FAILED "+s)};
  const M=[[10,10,0,0,0,0],[9,11,0,0,0,0],[0,0,20,0,0,0],[0,0,0,10,10,0],[0,0,0,2,18,0],[0,0,0,0,0,20]];
  const raw={Q:{AU:[10,10],AV:[20,20],BU:[15,15],BV:[15,15]},P:{AU:[9,11],AV:[5,5],BU:[3,27],BV:[30,30]}};
  const groups=["AU","AV","BU","BV"];
  const lookup={AU:{Q:0,P:1},AV:{Q:2,P:2},BU:{Q:3,P:4},BV:{Q:5,P:5}};
  const classes={AU:[0,1],AV:[2,2],BU:[3,4],BV:[5,5]};
  const sum=a=>a.reduce((s,x)=>s+x,0);
  let normalization=0, timeChecks=0, witnessChecks=0, upperChecks=0, inversePairs=0;
  for(const B of ["Q","P"]) {
    let total=0;
    for(const S of groups) {
      const [a,b]=raw[B][S], idx=lookup[S][B];
      ok(a>0&&b>0,"strict positivity");
      total+=2*(a+b);
      if(classes[S][0]===classes[S][1]) ok(M[idx][classes[S][0]]===20,"combined LR class");
      else {ok(M[idx][classes[S][0]]*(a+b)===20*a,"conditional J0");
            ok(M[idx][classes[S][1]]*(a+b)===20*b,"conditional J1");}
      normalization++;
    }
    ok(total===240,"P/Q sixteen leaves");
  }
  for(let b=0;b<64;b++) {
    const choice=Array.from({length:6},(_,j)=>(b>>j)&1);
    for(const B of ["Q","P"])for(const S of groups) {
      const [a,c]=raw[B][S], [j0,j1]=classes[S];
      const p3=20*(a*choice[j0]+c*choice[j1])/(a+c);
      const m3=sum(M[lookup[S][B]].map((x,j)=>x*choice[j]));
      ok(Number.isInteger(p3)&&p3===m3&&p3>=0&&p3<=20,"64 time policies on eight preparations");
      timeChecks++;
    }
  }
  for(const n of [0,1,2,4])for(const B of ["Q","P"])for(const S of groups) {
    const y={t2_bottom:0,t3_bottom:0,t4_bottom:0,t3_z0:0,t3_z1:0};
    if(S==="AV")y.t2_bottom=160;
    if(S==="AU")y.t3_bottom=160;
    if(S==="BV")y.t4_bottom=160;
    if(S==="BU") {
      const [a,b]=raw[B][S], p0=160*(a*(8-n)+b*n)/((a+b)*8);
      ok(Number.isInteger(p0),"sensor rational grid");
      y.t3_z0=p0;y.t3_z1=160-p0;
      ok(p0===(B==="Q"?80:16*(n+1)),"BU sensor law");
    }
    ok(sum(Object.values(y))===160,"Hdagger normalized");
    ok(S!=="BU" ? y.t3_z0+y.t3_z1===0 : y.t2_bottom+y.t3_bottom+y.t4_bottom===0,"tagged group separation");
    witnessChecks++;
  }
  const d1=[5,5,10,2,8,10], d2L=[10,10,20,0,0,0], d2R=[0,0,0,4,16,20];
  const d4=[[19,21,0,0,0,0],[19,21,0,0,0,0],[0,0,40,0,0,0],[0,0,0,12,28,0],[0,0,0,12,28,0],[0,0,0,0,0,40]];
  const d5=[[19,21,0,0,0,0],[19,21,0,0,0,0],[0,0,40,0,0,0],[0,0,0,20,20,0],[0,0,0,4,36,0],[0,0,0,0,0,40]];
  const maxima={k1:0,k2:0,k4:0,k5:0};
  for(let i=0;i<6;i++) {
    const truth=M[i].map(x=>2*x);
    for(const [k,d] of [["k1",d1],["k2",i<3?d2L:d2R],["k4",d4[i]],["k5",d5[i]]]){
      ok(sum(d)===40,"reference probability normalization");
      const err=40-sum(d.map((x,j)=>Math.min(x,truth[j])));
      maxima[k]=Math.max(maxima[k],err);upperChecks++;
    }
  }
  ok(maxima.k1===30&&maxima.k2===20&&maxima.k4===8&&maxima.k5===1,"sharp full-carrier upper reference distances");
  const A=[[11,-10,0,0,0,0],[-9,10,0,0,0,0],[0,0,1,0,0,0],
           [0,0,0,9/4,-5/4,0],[0,0,0,-1/4,5/4,0],[0,0,0,0,0,1]];
  let diameter=0;
  for(let i=0;i<6;i++)for(let j=i+1;j<6;j++){
    const distance=sum(A[i].map((x,z)=>Math.abs(x-A[j][z])));
    ok(distance<=40,"inverse column diameter");diameter=Math.max(diameter,distance);inversePairs++;
  }
  ok(diameter===40,"inverse column diameter sharpness");
  return {marker:"PASS_BRC_N4_TIME_VISIBLE_STOPPING_SHATTERING_20261031",
    counts:{normalization,time_policy_rows:timeChecks,tagged_witness_rows:witnessChecks,
      full_carrier_upper_checks:upperChecks,inverse_column_pairs:inversePairs},
    reference_error_numerators_over_40:maxima,inverse_diameter:diameter,
    epsilon_grid:["0","1/8","1/4","1/2"],proof_scope:"finite checks are audits; arbitrary stochastic encoders/policies and the real-epsilon interval follow from PROOF.md"};
}

console.log(JSON.stringify(main(),null,2));
