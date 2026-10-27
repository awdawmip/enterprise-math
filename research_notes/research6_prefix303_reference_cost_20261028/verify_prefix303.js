#!/usr/bin/env node
/** PREFIX-303 exact provenance-labelled BRC finite observer exhaustive certificate.
 * Input: PREFIX-299 RESULTS_PREFIX299.json (Git blob b6acffe158f014469235f5428d2889ff43b62810).
 * Run inside repo: node verify_prefix303.js [optional-results-path].
 * To verify 125 C4-closed states instead of the historical 216-state alphabet:
 * EM_BRC_SOURCE_ALPHABET=C4_CLOSED_5 node verify_prefix303.js [path].
 * All scientific masses are sums over ordered LABELLED source-path pairs with BigInt Gaussian coefficients.
 */
'use strict';
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const z=(r=0n,i=0n)=>[BigInt(r),BigInt(i)];
const add=(x,y)=>[x[0]+y[0],x[1]+y[1]], neg=x=>[-x[0],-x[1]];
const mul=(x,y)=>[x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]];
const cj=x=>[x[0],-x[1]], times=(x,n)=>[x[0]*BigInt(n),x[1]*BigInt(n)];
const eq=(x,y)=>x[0]===y[0]&&x[1]===y[1];
const Q=[z(1),z(0,1),z(-1),z(0,-1)];
const V_ALL=[z(0),z(1),z(-1),z(0,1),z(0,-1),z(1,1)];
const C4_CLOSED=process.env.EM_BRC_SOURCE_ALPHABET==='C4_CLOSED_5';
const V=C4_CLOSED?V_ALL.slice(0,5):V_ALL;
const REFS=[z(8),z(0,8)], PORTS=['E','C','R1','R2','R3'];
const SOURCE='research_notes/research6_prefix299_rank2_left_orbits_20261027/RESULTS_PREFIX299.json';
const INPUT=JSON.parse(fs.readFileSync(path.join(__dirname,'..','research6_prefix299_rank2_left_orbits_20261027','RESULTS_PREFIX299.json'),'utf8'));
const MATS=Object.fromEntries(['S4','S7'].map(k=>[k,INPUT.cases[k].all_orbits.map(M=>M.map(row=>row.map(c=>z(...c))))]));
const stats={gram_entries:0,instances:0,states:0,labelled_mass_readouts:0,ordered_source_pairs:0,K0_collision_pairs:0};
function sum(xs){return xs.reduce((a,b)=>add(a,b),z());}
function mass(paths){
  // Each ordered pair retains both of its original source labels.
  let acc=z();for(const p of paths)for(const t of paths) acc=add(acc,mul(p.amp,cj(t.amp)));
  assert.equal(acc[1],0n);assert(acc[0]>=0n);
  stats.ordered_source_pairs+=paths.length**2;stats.labelled_mass_readouts++;
  return acc[0].toString();
}
function read(a,q,M){
  const b=[a[0],mul(q,a[1]),mul(mul(q,q),a[2])], qb=cj(q);
  const paths=[
    [{label:'s0',amp:times(b[0],4)},{label:'s1',amp:times(b[1],4)}],
    [{label:'s1',amp:times(mul(qb,b[1]),-4)},{label:'s2',amp:times(mul(qb,b[2]),4)}],
    ...M.map(row=>row.map((v,k)=>({label:'s'+k,amp:mul(v,b[k])})))
  ];
  const base=[],extra=[];
  for(const ps of paths){base.push(mass(ps));for(let j=0;j<2;j++)extra.push(mass(ps.concat([{label:j?'UNSYNC_REF_i':'UNSYNC_REF_1',amp:REFS[j]}])));}
  return {base,extra};
}
function gramCheck(M,kind){
  const H=[[3,-1,0],[-1,2,1],[0,1,3]],S=kind==='S4'?[1,0,2]:[2,0,1];
  for(let k=0;k<3;k++)for(let l=0;l<3;l++){
    let v=z();for(let r=0;r<3;r++)v=add(v,mul(cj(M[r][k]),M[r][l]));
    assert(eq(v,z(16*H[k][l]-(k===l?S[k]:0))));stats.gram_entries++;
  }
}
const id=a=>a.map(x=>x[0]+','+x[1]).join(';');
const encode=a=>a.map(x=>x.map(y=>Number(y)));
function solve(M,q){
  const groups=new Map(),saved=new Map();
  for(const a of V)for(const b of V)for(const c of V){
    const state=[a,b,c],r=read(state,q,M),key=r.base.join('|'),sid=id(state);
    if(!groups.has(key))groups.set(key,[]);
    groups.get(key).push({state,sid});saved.set(sid,r.extra);stats.states++;
  }
  const diffs=new Set();let pairs=0,nonC4=null;
  for(const group of groups.values())for(let a=0;a<group.length;a++)for(let b=a+1;b<group.length;b++){
    const A=group[a],B=group[b],x=saved.get(A.sid),y=saved.get(B.sid);
    let diff=0;for(let j=0;j<10;j++)if(x[j]!==y[j])diff|=(1<<j);
    assert.notEqual(diff,0,'full references must distinguish the finite states');
    diffs.add(diff);pairs++;stats.K0_collision_pairs++;
    if(!nonC4&&!Q.some(q0=>id(A.state.map(s=>mul(q0,s)))===B.sid))nonC4=[encode(A.state),encode(B.state)];
  }
  const best=hit(diffs);
  stats.instances++;
  return {diffs,detail:{min_extra:best.k,optimal_masks:best.masks.map(m=>hex(m)),base_signatures:groups.size,K0_collision_pairs:pairs,nonC4_K0_pair:nonC4}};
}
function hex(m){return '0x'+m.toString(16).padStart(3,'0');}
function hit(diffs){
  const good=[];for(let k=0;k<=10;k++){
    for(let m=0;m<1024;m++)if(popcount(m)===k&&[...diffs].every(d=>(m&d)!==0))good.push(m);
    if(good.length)return {k,masks:good};
  }
  throw new Error('full-reference collision');
}
function popcount(n){let k=0;while(n){n&=n-1;k++;}return k;}
function run(){
  const cases={},universal=new Set();
  for(const kind of ['S4','S7'])for(let n=0;n<6;n++){
    const M=MATS[kind][n];gramCheck(M,kind);
    const phase=[],all=new Set();
    for(let j=0;j<4;j++){
      const s=solve(M,Q[j]);for(const x of s.diffs){all.add(x);universal.add(x);}
      phase.push({q:['1','i','-1','-i'][j],...s.detail});
    }
    const h=hit(all);
    cases[kind+'_orbit_'+(n+1)]={min_all_phases:h.k,uniform_masks:h.masks.map(hex),phase};
  }
  const h=hit(universal);
  assert.equal(h.k,4);assert(h.masks.includes(0x33));
  const total=48*(V.length**3);
  assert.deepEqual([stats.gram_entries,stats.instances,stats.states,stats.labelled_mass_readouts,stats.ordered_source_pairs],[108,48,total,15*total,167*total]);
  assert.equal(Object.values(cases).filter(c=>c.min_all_phases===2).length,8);
  assert.equal(Object.values(cases).filter(c=>c.min_all_phases===3).length,4);
  return {schema:'EM_PREFIX303_BRC_REFERENCE_MINIMUM_V1',date:'2026-10-28',
    source:{path:SOURCE,git_blob:'b6acffe158f014469235f5428d2889ff43b62810'},
    domain:{alphabet:C4_CLOSED?['0','1','-1','i','-i']:['0','1','-1','i','-i','1+i'],C4_closed_source_alphabet:C4_CLOSED,phase:['1','i','-1','-i'],q_fixed_per_instance:true,
      ports:PORTS,extras:['E+1','E+i','C+1','C+i','R1+1','R1+i','R2+1','R2+i','R3+1','R3+i'],mass_denominator:64},
    metrics:stats,cases,universal:{minimum:h.k,optimal_masks:h.masks.map(hex),example_mask:'0x033',
      example_extra:['E+1','E+i','R1+1','R1+i']},
    status:'AUTHOR_SIDE_EXACT_FINITE_CERTIFICATE_UNREVIEWED_NOT_ADMITTED_NATIVE_ATTRIBUTION_PENDING_BRC_REVALIDATION'};
}
const result=run(),json=JSON.stringify(result,null,2)+'\n';
if(process.argv[2])fs.writeFileSync(process.argv[2],json);
process.stdout.write('PASS '+JSON.stringify({metrics:result.metrics,minimum_by_class:Object.fromEntries(Object.entries(result.cases).map(([k,v])=>[k,v.min_all_phases])),universal:result.universal})+'\n');
