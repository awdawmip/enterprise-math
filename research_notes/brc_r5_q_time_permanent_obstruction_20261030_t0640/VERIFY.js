"use strict";
// Standalone exact integer verifier. Unit for Psi/eta: 1/27000.
function verify() {
  const rows = [
    ["A",1,120,240,0,["A0","A1"]],
    ["B",1,240,120,1,["B0","B1"]],
    ["A0",2,60,180,2,["A00","A01"]],
    ["A1",2,60,60,3,["A10","A11"]],
    ["B0",2,180,60,4,["B00","B01"]],
    ["B1",2,60,60,3,["B10","B11"]],
    ["A00",3,30,108,5,[]],["A01",3,30,72,6,[]],
    ["A10",3,30,45,7,[]],["A11",3,30,15,8,[]],
    ["B00",3,90,36,9,[]],["B01",3,90,24,10,[]],
    ["B10",3,20,40,11,[]],["B11",3,40,20,8,[]]
  ];
  const map=Object.fromEntries(rows.map((r,i)=>[r[0],{name:r[0],t:r[1],p:r[2],q:r[3],key:r[4],children:r[5],ix:i}]));
  function need(x,label){if(!x)throw Error("FAIL_"+label);}
  need(rows.length===14&&new Set(rows.map(r=>r[4])).size===12,"node_count");
  need(map.A1.p*map.B1.q===map.B1.p*map.A1.q,"time2_collision");
  need(map.A11.p*map.B11.q===map.B11.p*map.A11.q,"time3_collision");
  need(map.A11.p===30&&map.A11.q===15&&map.B11.p===40&&map.B11.q===20,"BRC_masses_360");
  for(const row of rows) {
    const n=map[row[0]];
    need(n.p>0&&n.q>0,"positive_"+n.name);
    if(n.children.length){
      need(n.children.reduce((s,id)=>s+map[id].p,0)===n.p,"P_normalization_"+n.name);
      need(n.children.reduce((s,id)=>s+map[id].q,0)===n.q,"Q_normalization_"+n.name);
    }
    for(const t of n.t===3?[3,4]:[n.t]){
      // P0=((20+5t)p+(t+1)q)/(100p); Q0=((240-20t)q+3(t+2)p)/(600q).
      // At epsilon=eta=1/1000: A1/B1 P(+/-), A11/B11 P(+), A11/B11 Q(+/-).
      const psign=t===2&&n.name==="A1"?1:t===2&&n.name==="B1"?-1:t===3&&(n.name==="A11"||n.name==="B11")?1:0;
      const qsign=t===3&&n.name==="A11"?1:t===3&&n.name==="B11"?-1:0;
      const pn=10*((20+5*t)*n.p+(t+1)*n.q)+psign*n.p, pd=1000*n.p;
      const qn=1000*((240-20*t)*n.q+3*(t+2)*n.p)+qsign*600*n.q, qd=600000*n.q;
      need(pn>0&&pn<pd&&qn>0&&qn<qd,"Bernoulli_rates_"+n.name+"_"+t);
    }
  }
  // At an early stop h, contribution to (Psi/eta)*27000 equals
  // 75*[+q360(A11) -q360(B11)] -(4-t)*(p360+q360).
  for(const n of Object.values(map)){
    const signed=n.name==="A11"?n.q:n.name==="B11"?-n.q:0;
    n.pay=75*signed-(4-n.t)*(n.p+n.q);
  }
  function walk(id,mask,kind){
    const n=map[id],bit=kind==="FULL"?n.ix:n.key;
    if(mask & (1<<bit))return n.pay;
    if(n.t===3)return 0;
    return n.children.reduce((s,x)=>s+walk(x,mask,kind),0);
  }
  const maxima={};
  for(const [kind,count] of [["FULL",16384],["LR",4096]]){
    let best=-1e100,winners=0;
    for(let mask=0;mask<count;mask++){
      const result=walk("A",mask,kind)+walk("B",mask,kind);
      if(result>best){best=result;winners=1;}
      else if(result===best){winners++;}
    }
    maxima[kind]=[best,winners];
  }
  need(maxima.FULL[0]===1080 && maxima.LR[0]===0,"all_deterministic_supports");
  need(maxima.FULL[1]===1 && maxima.LR[1]===17,"maximizer_counts");
  // Witness O=(891/2000,21433/72000,47/12,95/24) for previous rho=1 P rates.
  // Multiply inequality by 72000 for an exact integer identity.
  const leftNumerator=75000n*21433n-374n*47n*6000n+2501n*95n*3000n;
  need(leftNumerator===30761n*72000n,"integer_separation_witness");
  // P residual cone formula in units epsilon/1584; 216 exact signed grid examples.
  let tested=0;
  for(const a of [-2,-1,0,1,2,3])
  for(const b of [-2,-1,0,1,2,3])
  for(const c of [-2,-1,0,1,2,3]){
    const h=Math.max(0,264*c-96);
    const full=h+Math.max(216,132*a-9)+Math.max(0,176*b-12);
    const lr=Math.max(h,-432+Math.max(0,207+132*a+h)+Math.max(0,204+176*b));
    need(full>=lr&&((full===lr)===(132*a>=225&&176*b>=12)),"P_envelopes");
    tested++;
  }
  return [
    "ENTERPRISE_MATH_R5_Q_TIME_SEPARATION_EXACT",
    "positive_natural_nodes=14; LR_decision_keys=12; P_Q_cylinder_mass_denominator=360",
    "FULL_binary_policies=16384; LR_binary_policies=4096",
    "FULL_max_Psi_over_eta=1080/27000=1/25; LR_max_Psi_over_eta=0",
    "FULL_maximizers=1; LR_maximizers=17",
    "Q_optimal_penalty_lambda=1/75; gap=eta/25",
    "FULL_witness_rho1=891/2000,21433/72000,47/12,95/24",
    "LR_integer_support=75000 eQ -374 TP +2501 TQ <=30758",
    "FULL_integer_LHS=30761; integer_gap=3; Linf_distance>=3/77875",
    "P_envelope_exact_signed_grid="+tested+" cases",
    "PASS_EXACT_R5_Q_SIDE_PERMANENT_OBSTRUCTION"
  ].join("\n")+"\n";
}
return verify();
console.log(verify());
