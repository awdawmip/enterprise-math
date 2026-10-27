#!/usr/bin/env node
"use strict";
/* PREFIX-305 exact BRC certificate. Matrix input: research_notes/research6_prefix299_rank2_left_orbits_20261027/RESULTS_PREFIX299.json
 * Verified source blob: b6acffe158f014469235f5428d2889ff43b62810. No native detector authority.
 * Run: node research_notes/research6_prefix305_adaptive_two_refs_20261028/verify_prefix305.js > results.json
 */
const fs=require("node:fs"),path=require("node:path");
const input=JSON.parse(fs.readFileSync(path.join(__dirname,"..","research6_prefix299_rank2_left_orbits_20261027","RESULTS_PREFIX299.json"),"utf8"));
function run(MS){
 const expect=(x,m)=>{if(!x)throw Error(m)};
 const eq=(x,y)=>x[0]===y[0]&&x[1]===y[1];
 const z=(a,b)=>[BigInt(a),BigInt(b)];
 const add=(a,b)=>[a[0]+b[0],a[1]+b[1]];
 const cj=a=>[a[0],-a[1]];
 const mul=(a,b)=>[a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]];
 const scale=(a,k)=>[a[0]*BigInt(k),a[1]*BigInt(k)];
 const norm=a=>a[0]*a[0]+a[1]*a[1];
 const V=[z(0,0),z(1,0),z(-1,0),z(0,1),z(0,-1)], Q=V.slice(1), refs=[z(8,0),z(0,8)];
 const stats={configurations:0,source_states:0,brc_readouts:0,ordered_source_pairs:0,gram_entries:0};
 function mass(paths){
   let s=z(0,0);
   for(const a of paths)for(const b of paths){s=add(s,mul(a.amp,cj(b.amp)));stats.ordered_source_pairs++;}
   expect(s[1]===0n&&s[0]>=0n,"non-real or negative BRC mass");
   stats.brc_readouts++;
   expect(s[0]<=BigInt(Number.MAX_SAFE_INTEGER),"unsafe mass cast");
   return Number(s[0]);
 }
 function observe(M,q,a){
   const b=[a[0],mul(q,a[1]),mul(mul(q,q),a[2])],qc=cj(q);
   const ps=[
     [{source:0,amp:scale(b[0],4)},{source:1,amp:scale(b[1],4)}],
     [{source:1,amp:scale(mul(qc,b[1]),-4)},{source:2,amp:scale(mul(qc,b[2]),4)}],
     ...M.map(row=>row.map((co,k)=>({source:k,amp:mul(z(...co),b[k])})))
   ];
   return {base:ps.map(mass),extra:ps.flatMap((p,j)=>refs.map((r,k)=>mass([...p,{source:"unsynced-reference-"+j+"-"+k,amp:r}])))};
 }
 function gram(M,kind){
   const H=[[3,-1,0],[-1,2,1],[0,1,3]],S=kind==="S4"?[1,0,2]:[2,0,1];
   for(let j=0;j<3;j++)for(let k=0;k<3;k++){
     let v=z(0,0);for(let row=0;row<3;row++)v=add(v,mul(cj(z(...M[row][j])),z(...M[row][k])));
     expect(eq(v,z(16*H[j][k]-(j===k?S[j]:0),0)),kind+": bad exact Gram");
     stats.gram_entries++;
   }
 }
 const states=[];for(let a=0;a<5;a++)for(let b=0;b<5;b++)for(let c=0;c<5;c++)states.push([a,b,c]);
 const grouped=new Map(),couplings={};let lowerWitnesses=0;
 for(const kind of ["S4","S7"])for(let k=0;k<6;k++)for(let qi=0;qi<4;qi++){
   const M=MS[kind][k],q=Q[qi],cfg=kind+"-"+(k+1)+"-q"+qi;
   gram(M,kind);stats.configurations++;
   const Ts=M.map(row=>add(add(z(...row[1]),z(...row[2])),scale(z(...row[0]),-1)));
   const sq=Ts.map(v=>Number(norm(v)));
   expect(sq.reduce((a,b)=>a+b,0)===189&&Math.max(...sq)>=68,"coupling certificate mismatch");
   couplings[cfg]=sq;
   const four=[];
   for(let id=0;id<states.length;id++){
     const state=states[id],o=observe(M,q,state.map(t=>V[t])),key=o.base.join(",");
     if(!grouped.has(key))grouped.set(key,[]);
     grouped.get(key).push({cfg,id,ex:o.extra});
     stats.source_states++;
     if(state[0]===0&&state[2]===0&&state[1]!==0)four.push(o);
   }
   expect(four.length===4&&four.every(x=>x.base.join()===four[0].base.join()),"four-state K0 collision failed");
   for(let t=0;t<10;t++)expect(new Set(four.map(x=>x.extra[t])).size<4,"four-state lower bound failed");
   lowerWitnesses++;
 }
 function colliding(records){
   const seen=new Set();for(const r of records){if(seen.has(r.cfg))return true;seen.add(r.cfg);}return false;
 }
 function second(records){
   if(!colliding(records))return null;
   for(let t=0;t<10;t++){
     const seen=new Set();let ok=true;
     for(const r of records){const key=r.cfg+"|"+r.ex[t];if(seen.has(key)){ok=false;break;}seen.add(key);}
     if(ok)return t;
   }
   return undefined;
 }
 function candidate(records,first){
   const bins=new Map();for(const r of records){let y=r.ex[first];if(!bins.has(y))bins.set(y,[]);bins.get(y).push(r);}
   const subsequent={};let depth=1;
   for(const [y,part] of bins){const s=second(part);if(s===undefined)return null;subsequent[y]=s;if(s!==null)depth=2;}
   return {first,subsequent,depth};
 }
 const policy={},fixedFirstFails=Array(10).fill(null),firstCounts=Array(10).fill(0);
 let depthTwo=0,depthOne=0,withoutCollisions=0,maxRecords=0;
 for(const [base,rs] of grouped){
   maxRecords=Math.max(maxRecords,rs.length);
   if(!colliding(rs)){withoutCollisions++;continue;}
   let winner=null;
   for(let t=0;t<10;t++){const trial=candidate(rs,t);if(trial&&!winner)winner=trial;if(!trial&&fixedFirstFails[t]===null)fixedFirstFails[t]=base;}
   expect(winner!==null,"no two-step universal policy");
   policy[base]=winner;
   firstCounts[winner.first]++;
   if(winner.depth===2)depthTwo++;else depthOne++;
   for(const r of rs){
     const y=r.ex[winner.first],s=winner.subsequent[y];
     const matching=rs.filter(x=>x.cfg===r.cfg&&x.ex[winner.first]===y&&(s===null||x.ex[s]===r.ex[s]));
     expect(matching.length===1,"ambiguous source after policy");
   }
 }
 expect(stats.configurations===48&&stats.source_states===6000&&stats.brc_readouts===90000&&stats.ordered_source_pairs===1002000&&stats.gram_entries===432,"unexpected direct BRC coverage");
 expect(grouped.size===219&&withoutCollisions===1&&depthOne===0&&depthTwo===218,"unexpected fiber classification");
 expect(fixedFirstFails.every(x=>x!==null),"fixed-first obstruction missing");
 return {schema:"EM_PREFIX305_EXACT_ADAPTIVE_BRC_V1",scope:"A5^3, S4/S7 12 left-Port representatives, 4 C4 phases, 10 independent-reference menu",matrix_git_blob:"b6acffe158f014469235f5428d2889ff43b62810",stats,base_fibers:grouped.size,without_collisions:withoutCollisions,depth_one_fibers:depthOne,depth_two_fibers:depthTwo,max_records_per_base_fiber:maxRecords,lower_bound_C4_fibers:lowerWitnesses,first_choice_counts:firstCounts,fixed_first_failure_base_fibers:fixedFirstFails,coupling_norms_squared_by_config:couplings,policy};
}
const results=run({S4:input.cases.S4.all_orbits,S7:input.cases.S7.all_orbits});
process.stdout.write(JSON.stringify(results,null,2)+"\n");
