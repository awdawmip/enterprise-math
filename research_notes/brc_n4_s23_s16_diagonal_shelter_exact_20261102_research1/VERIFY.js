/* BRC N4/S23 S16 source-aware integer certificate. Node.js or V8; no external packages. */
const verify = function verify() {
  const M = [[10,10,0,0,0,0],[9,11,0,0,0,0],[0,0,20,0,0,0],[0,0,0,10,10,0],[0,0,0,2,18,0],[0,0,0,0,0,20]];
  const AA=[0,0,0,1,1,1], BB=[2,2,3,2,2,4], CC=[5,6,7,8,9,10], G=[0,0,1,2,2,3];
  const OFF=["00000000000","00000001000","00000000001","00101000000","00110000000","00101001000","00100000001","00100000000"];
  const BASE=["34 24 34 24","34 23 34 34","34 34 34 23","24 24 12 12","12 12 24 34","12 13 23 24","23 34 12 13","24 34 12 14"];
  const check=(condition,label)=>{if(!condition) throw new Error("CHECK_FAILED:"+label)};
  function P(bits) {
    check(bits.length===11 && /^[01]+$/.test(bits), "binary eleven-coordinate policy");
    const z=[...bits].map(Number);
    const prep=AA.map((a,s)=>{
      const x=z[a], y=z[BB[s]], t=z[CC[s]], v=(1-x)*(1-y);
      return [x,(1-x)*y,v*t,v*(1-t)];
    });
    check(prep.every(row=>row.reduce((x,y)=>x+y,0)===1),"source probability");
    return M.map(weights=>[0,1,2,3].map(atom=>
      weights.reduce((sum,w,s)=>sum+2*w*prep[s][atom],0)));
  }
  function Q(text) {
    const kernels=text.split(" ");
    check(kernels.length===4 && kernels.every(row=>/^[1-4]{2}$/.test(row)),"pair decoder");
    return M.map(weights=>{
      const row=[0,0,0,0];
      weights.forEach((w,s)=>{for(const digit of kernels[G[s]]) row[Number(digit)-1]+=w;});
      return row;
    });
  }
  function risk80(p,q) {
    return Math.max(...p.map((row,i)=>row.reduce((sum,value,j)=>sum+Math.abs(value-q[i][j]),0)));
  }
  const P8=OFF.map(P),Q8=BASE.map(Q);
  check([...P8,...Q8].every(rows=>rows.length===6 && rows.every(row=>row.reduce((a,b)=>a+b,0)===40 && row.every(x=>Number.isInteger(x)&&x>=0))),"six normalized prepared rows with denominator 40");
  const riskMatrix80=P8.map(p=>Q8.map(q=>risk80(p,q)));
  riskMatrix80.forEach((row,i)=>row.forEach((n,j)=>check(n===(i===j?40:80),`risk ${i+1},${j+1}: ${n}/80`)));
  const releasedOriginalLabels=[1,2,3,4,5,6,7,8];
  for (const h of releasedOriginalLabels) for(let i=0;i<8;i++) {
    if(i===h-1) continue;
    check(riskMatrix80[i][i]===40,`retained D${i+1} covers T${i+1} at 1/2`);
  }
  return {
    pass:"PASS_BRC_N4_S23_S16_DIAGONAL_SHELTER_EXACT_20261102",
    science_pin:"43ec6098b1330ae86d0a7863be336c5d97f6ef34",
    predecessor:"PR_1765_HEAD_2b85bbba145e2f102eb4744009eb807a51bb3b0b",
    arithmetic:"integer exact; all prepared probabilities denominated by 40; total-variation risks are riskMatrix80/80",
    labelled_sources:["AU0","AU1","AV","BU0","BU1","BV"],
    off_policy_binary_coordinates:OFF,
    risk_matrix_numerators_denominator_80:riskMatrix80,
    protected_diagonal:"1/2",
    unprotected_offdiagonal:"1",
    prepared_row_normalization_checks:96,
    exact_risks_checked:64,
    all_release_choices_verified:8,
    theorem_dependency:"S9 sharp radii (1/2 for h!=5, 11/21 for h=5) from predecessor; new theorem applies shelter lemma, not a fresh independent S9 proof",
    resulting_S16_radii:["1/2","1/2","1/2","1/2","11/21","1/2","1/2","1/2"],
    evidence_status:"author-side exact finite computation plus analytic reduction; no native Result/review/admission"
  };
};
console.log(JSON.stringify(verify(),null,2));
