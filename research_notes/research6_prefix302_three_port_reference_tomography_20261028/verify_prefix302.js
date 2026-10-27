"use strict";
/*
 * PREFIX-302 exact Gaussian C4-BRC reference tomography.
 * All dynamic readouts are ordered LABELLED source-path-pair sums.
 * Input matrices: awdawmip/enterprise-math@470fa5a3b73e45f05a1f66d2e4b708d46052630f:research_notes/research6_prefix299_rank2_left_orbits_20261027/RESULTS_PREFIX299.json Git Blob b6acffe158f014469235f5428d2889ff43b62810.
 * Auxiliary Q(i) three-source/2-event/3-kept-port model only; not native X6.
 * Run: node verify_prefix302.js
 */
const MATRICES = {"S4":[[[[-5,2],[0,0],[2,0]],[[-4,1],[4,0],[-2,1]],[[-1,0],[0,-4],[-1,-6]]],[[[-5,-2],[0,0],[2,0]],[[-4,-1],[4,0],[-2,-1]],[[-1,0],[0,4],[-1,6]]],[[[-5,-2],[0,0],[2,0]],[[-3,2],[4,0],[1,4]],[[-2,1],[0,-4],[-4,-3]]],[[[-5,2],[0,0],[2,0]],[[-3,-2],[4,0],[1,-4]],[[-2,-1],[0,4],[-4,3]]],[[[-5,-2],[0,0],[2,0]],[[-3,1],[0,0],[-5,3]],[[-2,-2],[4,4],[2,2]]],[[[-5,2],[0,0],[2,0]],[[-3,-1],[0,0],[-5,-3]],[[-2,-2],[4,4],[2,2]]]],"S7":[[[[-6,1],[4,0],[0,1]],[[-2,0],[0,0],[5,-2]],[[-2,1],[-4,0],[-4,1]]],[[[-6,-1],[4,0],[0,-1]],[[-2,-1],[-4,0],[-4,-1]],[[-2,0],[0,0],[5,2]]],[[[-5,3],[0,0],[-3,1]],[[-2,-2],[4,4],[2,2]],[[-2,0],[0,0],[5,2]]],[[[-5,-3],[0,0],[-3,-1]],[[-2,-2],[4,4],[2,2]],[[-2,0],[0,0],[5,-2]]],[[[-4,-3],[0,4],[-2,1]],[[-4,1],[0,-4],[-2,-3]],[[-2,0],[0,0],[5,2]]],[[[-4,-1],[0,4],[-2,3]],[[-4,3],[0,-4],[-2,-1]],[[-2,0],[0,0],[5,-2]]]]};
function runPrefix302() {
  const Z=(r=0n,i=0n)=>[r,i];
  const add=(a,b)=>[a[0]+b[0],a[1]+b[1]];
  const neg=a=>[-a[0],-a[1]];
  const sub=(a,b)=>add(a,neg(b));
  const mul=(a,b)=>[a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]];
  const conj=a=>[a[0],-a[1]];
  const n2=a=>a[0]*a[0]+a[1]*a[1];
  const eq=(a,b)=>a[0]===b[0]&&a[1]===b[1];
  const ga=a=>[BigInt(a[0]),BigInt(a[1])];
  const units=[ga([1,0]),ga([0,1]),ga([-1,0]),ga([0,-1])];
  const V=[[0,0],[1,0],[-1,0],[0,1],[0,-1],[1,1]].map(ga);
  const H=[[3,-1,0],[-1,2,1],[0,1,3]];
  function ensure(cond,why){if(!cond)throw Error(why)}
  const s={schema:"ENTERPRISE_MATH_PREFIX302_THREE_PORT_REFERENCE_BRC_V1",
    status:"AUTHOR_SIDE_EXACT_CHECK_UNREVIEWED_NOT_ADMITTED",
    source_enterprise_main:"470fa5a3b73e45f05a1f66d2e4b708d46052630f",
    source_global_main:"e0be92d15b820a2687d3e2b56fa4c2b55433ed65",
    source_prefix299_path:"research_notes/research6_prefix299_rank2_left_orbits_20261027/RESULTS_PREFIX299.json",
    source_prefix299_git_blob:"b6acffe158f014469235f5428d2889ff43b62810",
    cases:12, phases:4, input_alphabet:["0","1","-1","i","-i","1+i"],
    source_input_triplets:0, direct_labelled_brc_mass_readouts:0,
    ordered_source_path_pairs:0, gram_entries:0,
    coherent_tomography_recoveries:0, mass_conservation_checks:0,
    three_port_invertibility_checks:0, nonzero_t_rows:0,
    orbit_results:[], min_t_squared:null, min_case_max_t_squared:null};
  function pathsMass(ps){
    let s0=Z();
    for(const p of ps)for(const t of ps){
      const prod=mul(p.amp,conj(t.amp));
      s0=add(s0,prod);
      s.ordered_source_path_pairs++;
    }
    ensure(s0[1]===0n,"BRC ordered-pair imaginary remainder");
    ensure(s0[0]>=0n,"BRC mass negative");
    s.direct_labelled_brc_mass_readouts++;
    return s0[0];
  }
  function observer(ps,d){
    const all=ps.map(x=>({source:x.source,amp:x.amp}));
    const m0=pathsMass(all);
    const m1=pathsMass([...all,{source:"UNSYNC_REFERENCE_UNIT",amp:Z(d,0n)}]);
    const mi=pathsMass([...all,{source:"UNSYNC_REFERENCE_I",amp:Z(0n,d)}]);
    const twoD=2n*d;
    ensure((m1-m0-d*d)%twoD===0n,"unit reference divisibility");
    ensure((mi-m0-d*d)%twoD===0n,"i reference divisibility");
    const observed=Z((m1-m0-d*d)/twoD,(mi-m0-d*d)/twoD);
    const actual=all.reduce((a,p)=>add(a,p.amp),Z());
    ensure(eq(observed,actual),"reference tomography mismatch");
    s.coherent_tomography_recoveries++;
    return {observed,m0};
  }
  for(const kind of ["S4","S7"]){
    const diag=kind==="S4"?[1,0,2]:[2,0,1];
    let oi=0;
    for(const numericM of MATRICES[kind]){
      oi++;
      const M=numericM.map(row=>row.map(ga));
      for(let k=0;k<3;k++)for(let l=0;l<3;l++){
        let g=Z();
        for(let row=0;row<3;row++)g=add(g,mul(conj(M[row][k]),M[row][l]));
        const expected=Z(BigInt(16*H[k][l]-(k===l?diag[k]:0)),0n);
        ensure(eq(g,expected),"Gram mismatch "+kind+"/"+oi+"/"+k+"/"+l);
        s.gram_entries++;
      }
      const t=M.map(row=>add(sub(row[1],row[0]),row[2]));
      const nt=t.map(v=>Number(n2(v)));
      ensure(nt.every(x=>x>0),"zero retained-port kernel coupling");
      ensure(nt.reduce((a,b)=>a+b,0)===189,"sum kernel energy not 189");
      s.nonzero_t_rows+=3;
      const low=Math.min(...nt), high=Math.max(...nt);
      s.min_t_squared=s.min_t_squared===null?low:Math.min(s.min_t_squared,low);
      s.min_case_max_t_squared=s.min_case_max_t_squared===null?high:Math.min(s.min_case_max_t_squared,high);
      s.orbit_results.push({type:kind,orbit:oi,t:t.map(z=>[Number(z[0]),Number(z[1])]),norms_squared:nt});
      for(const q of units){
        const q2=mul(q,q);
        for(const a0 of V)for(const a1 of V)for(const a2 of V){
          const a=[a0,a1,a2],b=[a0,mul(q,a1),mul(q2,a2)];
          const Ep=[{source:"s0",amp:b[0]},{source:"s1",amp:b[1]}];
          const Cp=[{source:"s1",amp:neg(a[1])},{source:"s2",amp:mul(q,a[2])}];
          const keep=M.map(row=>row.map((m,i)=>({source:"s"+i,amp:mul(m,b[i])})));
          const out=[observer(Ep,2n),observer(Cp,2n),...keep.map(p=>observer(p,8n))];
          const conserved=16n*(out[0].m0+out[1].m0)+out[2].m0+out[3].m0+out[4].m0
            +BigInt(diag[0])*n2(a0)+BigInt(diag[2])*n2(a2);
          const source=64n*(n2(a0)+n2(a1)+n2(a2));
          ensure(conserved===source,"BRC mass/loss law mismatch");
          s.mass_conservation_checks++;
          const E=out[0].observed,C=out[1].observed;
          for(let row=0;row<3;row++){
            const rhs=sub(sub(out[row+2].observed,mul(M[row][0],E)),
              mul(M[row][2],mul(q,C)));
            ensure(eq(rhs,mul(t[row],b[1])),"coherent inverse equation mismatch");
            ensure(eq(sub(E,b[1]),b[0]),"source b0 reconstruction mismatch");
            ensure(eq(add(mul(q,C),b[1]),b[2]),"source b2 reconstruction mismatch");
            s.three_port_invertibility_checks++;
          }
          s.source_input_triplets++;
        }
      }
    }
  }
  ensure(s.source_input_triplets===10368,"coverage incomplete");
  ensure(s.direct_labelled_brc_mass_readouts===155520,"readout count");
  ensure(s.ordered_source_path_pairs===1731456,"path count");
  ensure(s.gram_entries===108&&s.nonzero_t_rows===36,"representative count");
  ensure(s.coherent_tomography_recoveries===51840,"tomography count");
  ensure(s.mass_conservation_checks===10368,"conservation count");
  ensure(s.three_port_invertibility_checks===31104,"inverse count");
  ensure(s.min_t_squared===8&&s.min_case_max_t_squared===68,"sharp finite minima");
  return s;
}
const output=runPrefix302();
if(typeof process!=="undefined"&&typeof console!=="undefined")
  console.log(JSON.stringify(output,null,2));
