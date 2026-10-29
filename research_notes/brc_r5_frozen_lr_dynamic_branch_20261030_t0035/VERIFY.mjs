console.log((function verify(){
  const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b!==0n){const t=a%b;a=b;b=t;}return a;};
  const R=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);if(d===0n)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}const k=gcd(n,d);return {n:n/k,d:d/k};};
  const add=(a,b)=>R(a.n*b.d+b.n*a.d,a.d*b.d);
  const neg=a=>R(-a.n,a.d);
  const sub=(a,b)=>add(a,neg(b));
  const mul=(a,b)=>R(a.n*b.n,a.d*b.d);
  const div=(a,b)=>R(a.n*b.d,a.d*b.n);
  const eq=(a,b)=>a.n===b.n&&a.d===b.d;
  const lt=(a,b)=>a.n*b.d<b.n*a.d;
  const str=a=>a.d===1n?String(a.n):a.n+"/"+a.d;
  const assert=(yes,msg)=>{if(!yes)throw Error(msg);};
  const Z=R(0),O=R(1),F=(n,d=1)=>R(n,d);
  const sum=arr=>arr.reduce(add,Z);
  const A={name:"A",P:F(1,8),Q:F(1,4),a:F(3,4),p:[F(1,5),F(3,10),F(1,5),F(1,2)],q:[F(1,5),F(1,5),F(3,10),F(2,5)]};
  const B={name:"B",P:F(1,8),Q:F(1,4),a:F(1,4),p:[F(1,4),F(7,20),F(1,4),F(11,20)],q:[F(1,4),F(1,4),F(7,20),F(9,20)]};
  const C={name:"C",P:F(3,4),Q:F(1,2),a:F(1,2),p:[F(1,4),F(1,4),F(1,2),F(1,3)],q:[F(1,4),F(1,2),F(1,4),F(2,3)]};
  const S=[A,B,C];
  assert(eq(sum(S.map(x=>x.P)),O)&&eq(sum(S.map(x=>x.Q)),O),"P/Q initial masses");
  assert(eq(div(A.P,A.Q),F(1,2))&&eq(div(B.P,B.Q),F(1,2))&&eq(div(C.P,C.Q),F(3,2)),"ratios");
  const zOne=y=>y===1?F(2,3):F(1,3);
  const natY=(s,y)=>y===1?s.a:sub(O,s.a);
  const natZ=(y,z)=>z===1?zOne(y):sub(O,zOne(y));
  const b=s=>add(F(1,3),div(s.a,F(3)));
  const pRate=(s,j,y,z)=>j===2?add(s.p[1],div(sub(F(y),s.a),F(4))):s.p[j-1];
  const qRate=(s,j,y,z)=>j===2?add(s.q[1],div(sub(F(y),s.a),F(8))):(j===3?add(s.q[2],div(sub(F(z),b(s)),F(8))):s.q[j-1]);
  const obsZero=()=>[Z,Z,Z,Z];
  const obsAdd=(v,s,j,weight,p,q)=>{
    v[0]=add(v[0],mul(mul(s.P,weight),p));
    v[1]=add(v[1],mul(mul(s.Q,weight),q));
    v[2]=add(v[2],mul(mul(s.P,weight),F(j)));
    v[3]=add(v[3],mul(mul(s.Q,weight),F(j)));
  };
  let totalBranches=0, checkedTerminalPairs=0;
  for(const s of S){
    let probabilities=Z;
    const E_p=[Z,Z,Z,Z],E_q=[Z,Z,Z,Z];
    for(let y=0;y<=1;y++)for(let z=0;z<=1;z++){
      const wy=natY(s,y),wz=natZ(y,z),w=mul(wy,wz);
      assert(lt(Z,wy)&&lt(wy,O)&&lt(Z,wz)&&lt(wz,O),"nature positivity");
      probabilities=add(probabilities,w);totalBranches++;
      const qFull=mul(s.Q,w),pFull=mul(s.P,w);
      assert(eq(div(pFull,qFull),div(s.P,s.Q)),"likelihood-ratio changed on a continuation path");
      for(let j=1;j<=4;j++){
        const p=pRate(s,j,y,z),q=qRate(s,j,y,z);
        assert(lt(Z,p)&&lt(p,O)&&lt(Z,q)&&lt(q,O),"terminal probability outside (0,1)");
        checkedTerminalPairs++;
        E_p[j-1]=add(E_p[j-1],mul(w,p));
        E_q[j-1]=add(E_q[j-1],mul(w,q));
      }
    }
    assert(eq(probabilities,O),"nature leaf normalization");
    for(let j=1;j<=4;j++){
      assert(eq(E_p[j-1],s.p[j-1]),"P centered error average mismatch "+s.name+j);
      assert(eq(E_q[j-1],s.q[j-1]),"Q centered error average mismatch "+s.name+j);
    }
  }
  function lrChoices(choiceAB,choiceC){
    const o=obsZero();
    for(const s of S){
      const j=s.name==="C"?choiceC:choiceAB;
      obsAdd(o,s,j,O,s.p[j-1],s.q[j-1]);
    }
    return o;
  }
  let minLR=null;let nLR=0;
  for(let a=1;a<=4;a++)for(let c=1;c<=4;c++){
    const o=lrChoices(a,c);nLR++;
    if(minLR===null||lt(o[0],minLR))minLR=o[0];
  }
  assert(nLR===16&&eq(minLR,F(39,160)),"exact LR deterministic support");
  const full=obsZero();
  for(const s of S)for(let y=0;y<=1;y++)for(let z=0;z<=1;z++){
    const j=s.name==="A"?(y===0?2:3):1;
    obsAdd(full,s,j,mul(natY(s,y),natZ(y,z)),pRate(s,j,y,z),qRate(s,j,y,z));
  }
  const expectedFull=[F(617,2560),F(323,1280),F(39,32),F(23,16)];
  assert(full.every((v,i)=>eq(v,expectedFull[i])),"FULL witness mismatch");
  const gap=sub(minLR,full[0]);
  assert(eq(gap,F(7,2560))&&lt(Z,gap),"signed support separation");
  const matched=obsZero(),dAB=[F(1,2),F(1,8),F(3,8),Z],dC=[O,Z,Z,Z];
  for(const s of S){
    const d=s.name==="C"?dC:dAB;
    for(let j=1;j<=4;j++)obsAdd(matched,s,j,d[j-1],s.p[j-1],s.q[j-1]);
  }
  assert(eq(matched[0],F(79,320))&&eq(matched[1],F(41,160)),"matched LR errors");
  assert(eq(matched[2],full[2])&&eq(matched[3],full[3]),"time flows must match");
  assert(eq(sub(full[0],matched[0]),F(-3,512))&&eq(sub(full[1],matched[1]),F(-1,256)),"BRC covariance residual");
  const baseline=lrChoices(1,1);
  const cols=[[2,1],[3,1],[1,2],[1,3]].map(([a,c])=>lrChoices(a,c).map((v,i)=>sub(v,baseline[i])));
  const mat=[0,1,2,3].map(i=>cols.map(col=>col[i]));
  let det=O;
  for(let i=0;i<4;i++){
    let pivot=i;while(pivot<4&&eq(mat[pivot][i],Z))pivot++;
    assert(pivot<4,"rank deficient");
    if(pivot!==i){const temp=mat[i];mat[i]=mat[pivot];mat[pivot]=temp;det=neg(det);}
    const a=mat[i][i];det=mul(det,a);
    for(let k=i+1;k<4;k++){
      const t=div(mat[k][i],a);
      for(let j=i;j<4;j++)mat[k][j]=sub(mat[k][j],mul(t,mat[i][j]));
    }
  }
  assert(eq(det,F(1,1280)),"4D affine determinant");
  return [
    "SCOPE: finite 2-law stop/continue model; 3 initially labeled sources; two exogenous positive binary stages; 3 LR decision times and forced time 4.",
    "CHECK: P/Q initial normalization; 12 positive full nature leaves; 48 strictly positive P/Q terminal-error pairs; all continuation prefix likelihood ratios; sourcewise centered averages.",
    "EXACT_BRANCHES="+totalBranches+" TERMINAL_PAIR_CHECKS="+checkedTerminalPairs+" LR_DETERMINISTIC="+nLR,
    "LR_MIN_eP="+str(minLR),
    "FULL_OBSERVER=("+full.map(str).join(",")+")",
    "MATCHED_LR_OBSERVER=("+matched.map(str).join(",")+")",
    "FULL_MINUS_MATCHED_LR_ERRORS=("+str(sub(full[0],matched[0]))+","+str(sub(full[1],matched[1]))+")",
    "STRICT_SIGNED_SUPPORT_GAP="+str(gap),
    "LR_AFFINE_DETERMINANT="+str(det),
    "CHECKER_SCOPE: exact finite rational arithmetic for this instance; universal all-real claims require the separate algebraic flow proof in RESEARCH.md.",
    "PASS_EXACT_R5_FROZEN_LR_DYNAMIC_BRANCH"
  ].join("\n");
})());
