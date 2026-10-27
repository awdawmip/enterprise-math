"use strict";
// Exact Gaussian-integer C4-BRC Port-orbit verifier; Node.js 18+.
const verifyPrefix298=function verifyPrefix298() {
  // All arithmetic uses safe-range integer pairs (real,imag); no floating magnitude/sqrt.
  const Z=[0,0], ONE=[1,0], I=[0,1], NEG=[-1,0];
  const add=(x,y)=>[x[0]+y[0],x[1]+y[1]];
  const sub=(x,y)=>[x[0]-y[0],x[1]-y[1]];
  const mul=(x,y)=>[x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]];
  const conj=x=>[x[0],-x[1]];
  const norm=x=>x[0]*x[0]+x[1]*x[1];
  const eq=(x,y)=>x[0]===y[0]&&x[1]===y[1];
  const assert=(ok,why)=>{if(!ok)throw Error(why)};
  function divexact(x,y) {
    const k=norm(y); assert(k!==0,"division by zero");
    const z=mul(x,conj(y));
    if(z[0]%k||z[1]%k)return null;
    return [z[0]/k,z[1]/k];
  }
  function dot(x,y) {
    let t=Z;
    for(let j=0;j<3;j++)t=add(t,mul(conj(x[j]),y[j]));
    return t;
  }
  const G=[[[47,0],[-16,0],[1,0]],[[-16,0],[32,0],[16,0]],[[1,0],[16,0],[47,0]]];
  function checkGram(M){
    for(let j=0;j<3;j++)for(let k=0;k<3;k++){
      if(!eq(dot(M.map(r=>r[j]),M.map(r=>r[k])),G[j][k]))return false;
    }
    return true;
  }
  const units=[ONE,NEG,I,[0,-1]];
  function canonical(M) {
    const R=M.map(row=>{
      const variants=units.map(u=>row.map(z=>mul(u,z)));
      variants.sort((x,y)=>{
        const a=JSON.stringify(x),b=JSON.stringify(y);
        return a<b?-1:a>b?1:0;
      });
      return variants[0];
    });
    R.sort((x,y)=>{
      const a=JSON.stringify(x),b=JSON.stringify(y);
      return a<b?-1:a>b?1:0;
    });
    return {key:JSON.stringify(R), rows:R};
  }
  const pools=Array.from({length:48},()=>[]);
  for(let x=-7;x<=7;x++)for(let y=-7;y<=7;y++){
    const z=[x,y],q=norm(z);
    if(q<=47)pools[q].push(z);
  }
  const v32=pools.slice(0,33).flat(),v47=pools.flat();
  const quadrant=[Z];
  for(let x=1;x<=7;x++)for(let y=0;y<=7;y++)
    if(x*x+y*y<=47)quadrant.push([x,y]);
  quadrant.sort((x,y)=>norm(x)-norm(y)||x[0]-y[0]||x[1]-y[1]);
  const classMap=new Map();
  let firstColumns=0,uvPairs=0,uvwMatrices=0;
  for(let h=0;h<quadrant.length;h++)
   for(let t=h;t<quadrant.length;t++)
    for(let p=t;p<quadrant.length;p++){
      const u=[quadrant[h],quadrant[t],quadrant[p]];
      if(u.reduce((s,x)=>s+norm(x),0)!==47)continue;
      firstColumns++;
      let pivot=0;
      for(let j=1;j<3;j++)if(norm(u[j])>norm(u[pivot]))pivot=j;
      const free=[0,1,2].filter(j=>j!==pivot),x=free[0],y=free[1];
      const cu=u.map(conj);
      for(const vx of v32)for(let r=0;r<=32-norm(vx);r++)for(const vy of pools[r]){
        const vk=divexact(sub(sub([-16,0],mul(cu[x],vx)),mul(cu[y],vy)),cu[pivot]);
        if(vk===null||norm(vx)+norm(vy)+norm(vk)!==32)continue;
        const v=[Z,Z,Z];v[x]=vx;v[y]=vy;v[pivot]=vk;
        uvPairs++;
        const cv=v.map(conj);
        let chosen=null;
        for(let j=0;j<3;j++)for(let k=j+1;k<3;k++){
          const delta=sub(mul(cu[j],cv[k]),mul(cu[k],cv[j]));
          if(chosen===null||norm(delta)>norm(chosen.delta))chosen={j,k,delta};
        }
        assert(norm(chosen.delta)>0,"positive two-column Gram determinant");
        const j=chosen.j,k=chosen.k,f=[0,1,2].find(z=>z!==j&&z!==k);
        for(const wf of v47){
          const r1=sub(ONE,mul(cu[f],wf)),r2=sub([16,0],mul(cv[f],wf));
          const wj=divexact(sub(mul(r1,cv[k]),mul(cu[k],r2)),chosen.delta);
          if(wj===null)continue;
          const wk=divexact(sub(mul(cu[j],r2),mul(r1,cv[j])),chosen.delta);
          if(wk===null||norm(wj)+norm(wk)+norm(wf)!==47)continue;
          const w=[Z,Z,Z];w[j]=wj;w[k]=wk;w[f]=wf;
          const M=[0,1,2].map(h=>[u[h],v[h],w[h]]);
          assert(checkGram(M),"exact G");
          uvwMatrices++;
          const canon=canonical(M);
          classMap.set(canon.key,canon.rows);
        }
      }
    }
  assert(firstColumns===130,"canonical first-column count "+firstColumns);
  assert(uvPairs===1942,"two-column count "+uvPairs);
  assert(uvwMatrices===1108,"raw solution count "+uvwMatrices);
  assert(classMap.size===984,"Port-orbit count "+classMap.size);
  const M0=[[[6,3],[-1,-1],[1,0]],[[1,1],[-5,-2],[-4,-1]],[Z,[-1,0],[5,-2]]];
  const N0=[[[2,1],[-1,-1],[5,2]],[[1,1],[-5,-2],[-4,-1]],[[6,-2],[-1,0],[-1,0]]];
  assert(classMap.has(canonical(M0).key)&&classMap.has(canonical(N0).key),"previous cases included");
  assert(canonical(M0).key!==canonical(N0).key,"previous cases inequivalent");
  const E=[[[4,0],[4,0],Z],[Z,[-4,0],[4,0]]],L=[ONE,Z,NEG];
  const phases=[ONE,I,NEG,[0,-1]];
  const samples=[
    [ONE,Z,Z],[Z,ONE,Z],[Z,Z,ONE],[ONE,ONE,ONE],
    [ONE,I,ONE],[ONE,[0,-1],ONE],[ONE,ONE,Z],[ONE,Z,ONE],
    [Z,ONE,ONE],[[1,1],ONE,Z],[Z,[1,-1],ONE],[NEG,I,[0,-1]]
  ];
  let gramChecks=0,binReadouts=0,pairProducts=0,totalMassChecks=0,leakChecks=0;
  const normGroups=new Map(),allOrbits=[];
  const sorted=[...classMap.entries()].sort(([a],[b])=>a<b?-1:a>b?1:0);
  for(let index=0;index<sorted.length;index++){
    const M=sorted[index][1];
    assert(checkGram(M),"Gram after canonicalization");
    gramChecks+=9;
    const norms=M.map(row=>row.reduce((sum,z)=>sum+norm(z),0)).sort((a,b)=>a-b);
    const nk=norms.join(",");
    normGroups.set(nk,(normGroups.get(nk)||0)+1);
    allOrbits.push({orbit:index+1,M,row_norm_multiset:norms});
    for(const q of phases){
      const q2=mul(q,q),D=[ONE,q,q2];
      const rows=[
        E[0].map((z,j)=>mul(z,D[j])),
        E[1].map((z,j)=>mul(conj(q),mul(z,D[j]))),
        ...M.map(row=>row.map((z,j)=>mul(z,D[j]))),
        L.map((z,j)=>mul(z,D[j]))
      ];
      for(const src of samples){
        const masses=[];
        for(const row of rows){
          const paths=row.map((z,j)=>mul(z,src[j]));
          let brcScore=Z;
          for(let j=0;j<3;j++)for(let k=0;k<3;k++){
            brcScore=add(brcScore,mul(conj(paths[j]),paths[k]));
            pairProducts++;
          }
          assert(brcScore[1]===0&&brcScore[0]>=0,"nonnegative exact ordered-BRC mass");
          assert(brcScore[0]===norm(add(add(paths[0],paths[1]),paths[2])),"labelled paths readout");
          masses.push(brcScore[0]);binReadouts++;
        }
        assert(masses.reduce((s,x)=>s+x,0)===64*src.reduce((s,z)=>s+norm(z),0),"full mass");
        totalMassChecks++;
        assert(masses[5]===norm(sub(src[0],mul(q2,src[2]))),"single leakage branch");
        leakChecks++;
      }
    }
  }
  assert(normGroups.size===50,"row-norm groups");
  assert(gramChecks===8856&&binReadouts===283392&&pairProducts===2550528&&totalMassChecks===47232,"sample counts");
  const result={
    schema:"ENTERPRISE_MATH_PREFIX298_GAUSSIAN_PORT_ORBIT_CERTIFICATE_V1",
    source_model:"C4-BRC auxiliary 3 labelled sources, 2 fixed event bins, 3 kept bins, 1 leak bin; denominator 8",
    fixed_gram:G,
    fixed_residual_S:[[[1,0],Z,[-1,0]],[Z,Z,Z],[[-1,0],Z,ONE]],
    rank_2col_minor:"47*32-(-16)^2=1248 > 0",
    canonical_first_columns:firstColumns,
    candidate_first_second_columns:uvPairs,
    exact_matrices_after_fixed_first_column_gauge:uvwMatrices,
    distinct_left_U3_Zi_port_orbits:classMap.size,
    distinct_row_norm_multisets:normGroups.size,
    orbit_count_with_nonunique_norms:[...normGroups.values()].filter(n=>n>1).reduce((a,b)=>a+b,0),
    full_gram_entries_checked:gramChecks,
    C4_phases:phases.length,
    labelled_source_samples_per_orbit_phase:samples.length,
    sampled_full_output_cases:totalMassChecks,
    direct_brc_bin_readouts:binReadouts,
    ordered_labelled_source_pair_products:pairProducts,
    total_mass_checks:totalMassChecks,
    leakage_checks:leakChecks,
    PREFIX297_M_and_N_in_distinct_orbits:true,
    exact_completeness:"all first columns normalized under row unit and permutation; exact norm-bound Gaussian enumeration of second and third columns; exact Gaussian divisibility, exact Gram equalities; full monomial row canonicalization",
    sample_scope:"Samples check labelled BRC implementation; universal Gram and finite completeness follow exact finite arithmetic and proof, not sample extrapolation.",
    all_orbits:allOrbits
  };
  return result;
};
const result=verifyPrefix298();
if(typeof process!=="undefined"&&process.stdout)process.stdout.write(JSON.stringify(result,null,2)+"\n");
