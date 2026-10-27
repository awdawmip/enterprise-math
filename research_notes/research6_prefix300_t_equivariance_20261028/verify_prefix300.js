/* PREFIX-300 / self-contained exact source-labelled C4-BRC checker.
   Z[i] is represented as signed integer pairs; all intermediate integers fit
   safely in JS Number's exact integer range, checked by assert below.
   Readout = sum of all 9 ordered source pairs per bin, never |path| sum.
*/
const S4=[
[[[-5,2],[0,0],[2,0]],[[-4,1],[4,0],[-2,1]],[[-1,0],[0,-4],[-1,-6]]],
[[[-5,-2],[0,0],[2,0]],[[-4,-1],[4,0],[-2,-1]],[[-1,0],[0,4],[-1,6]]],
[[[-5,-2],[0,0],[2,0]],[[-3,2],[4,0],[1,4]],[[-2,1],[0,-4],[-4,-3]]],
[[[-5,2],[0,0],[2,0]],[[-3,-2],[4,0],[1,-4]],[[-2,-1],[0,4],[-4,3]]],
[[[-5,-2],[0,0],[2,0]],[[-3,1],[0,0],[-5,3]],[[-2,-2],[4,4],[2,2]]],
[[[-5,2],[0,0],[2,0]],[[-3,-1],[0,0],[-5,-3]],[[-2,-2],[4,4],[2,2]]]];
const S7=[
[[[-6,1],[4,0],[0,1]],[[-2,0],[0,0],[5,-2]],[[-2,1],[-4,0],[-4,1]]],
[[[-6,-1],[4,0],[0,-1]],[[-2,-1],[-4,0],[-4,-1]],[[-2,0],[0,0],[5,2]]],
[[[-5,3],[0,0],[-3,1]],[[-2,-2],[4,4],[2,2]],[[-2,0],[0,0],[5,2]]],
[[[-5,-3],[0,0],[-3,-1]],[[-2,-2],[4,4],[2,2]],[[-2,0],[0,0],[5,-2]]],
[[[-4,-3],[0,4],[-2,1]],[[-4,1],[0,-4],[-2,-3]],[[-2,0],[0,0],[5,2]]],
[[[-4,-1],[0,4],[-2,3]],[[-4,3],[0,-4],[-2,-1]],[[-2,0],[0,0],[5,-2]]]];
const Z=[0,0],O=[1,0],I=[0,1],PH=[O,I,[-1,0],[0,-1]];
const A=[Z,O,[-1,0],I,[0,-1],[1,1]];
function g(a,b){return [a,b]}
function ck(x){if(!Number.isSafeInteger(x))throw Error("Unsafe integer "+x);return x}
function add(a,b){return [ck(a[0]+b[0]),ck(a[1]+b[1])]}
function neg(a){return [-a[0],-a[1]]}
function mul(a,b){return [ck(a[0]*b[0]-a[1]*b[1]),ck(a[0]*b[1]+a[1]*b[0])]}
function cj(a){return [a[0],-a[1]]}
function sq(a){return ck(a[0]*a[0]+a[1]*a[1])}
function sum(v){return v.reduce(add,Z)}
function eq(a,b){return JSON.stringify(a)===JSON.stringify(b)}
function ok(cond,label){if(!cond)throw Error(label)}
function tv(a){return [a[2],neg(a[1]),a[0]]}
function tm(m){return m.map(tv)}
function gram(m){return [0,1,2].map(j=>[0,1,2].map(k=>sum(m.map(row=>mul(cj(row[j]),row[k])))))}
function rowKey(row){return PH.map(u=>JSON.stringify(row.map(z=>mul(z,u)))).sort()[0]}
function key(m){return m.map(rowKey).sort().join("|")}
const R=[[[4,0],[4,0],Z],[Z,[-4,0],[4,0]]];
const L4=[[O,Z,Z],[Z,Z,[1,1]]],L7=[[[1,1],Z,Z],[Z,Z,O]];
function d(q){return [O,q,mul(q,q)]}
function rows(m,q,k){
 const dd=d(q),event=R.map(row=>row.map((z,j)=>mul(z,dd[j])));
 event[1]=event[1].map(z=>mul(cj(q),z));
 return event.concat(m.concat(k===4?L4:L7).map(row=>row.map((z,j)=>mul(z,dd[j]))));
}
function path(row,a){return row.map((z,j)=>mul(z,a[j]))}
function brc9(p){return sum([0,1,2].flatMap(j=>[0,1,2].map(k=>mul(cj(p[j]),p[k]))))}
function pairs(vals){if(vals.length===0)return [[]];return pairs(vals.slice(1)).flatMap(t=>vals[0].map(a=>[a,...t]))}
function run(){
 const G4=[[[47,0],[-16,0],Z],[[-16,0],[32,0],[16,0]],[Z,[16,0],[46,0]]];
 const G7=[[[46,0],[-16,0],Z],[[-16,0],[32,0],[16,0]],[Z,[16,0],[47,0]]];
 const keys7=new Set(S7.map(key)),mapped=new Set();
 ok(keys7.size===6,"S7 keys");
 let gramEntries=0,sourceEntries=0,paired=0,bins=0,pairProducts=0,massChecks=0;
 for(const m of S4){
   const n=tm(m);ok(eq(gram(m),G4)&&eq(gram(n),G7),"Gram");
   gramEntries+=18;
   ok(keys7.has(key(n)),"orbit pair");mapped.add(key(n));
   for(const q of PH){
     const qc=cj(q),q2=mul(q,q),old=rows(m,q,4),neo=rows(n,qc,7);
     const trans=[neo[1].map(z=>mul(q,z)),neo[0].map(z=>mul(q,z)),
       ...neo.slice(2,5).map(row=>row.map(z=>mul(q2,z))),
       neo[6].map(z=>mul(q2,z)),neo[5].map(z=>mul(q2,z))];
     ok(eq(old.map(tv),trans),"21 labelled coefficients");
     sourceEntries+=21;
     for(const a0 of A)for(const a1 of A)for(const a2 of A){
       const a=[a0,a1,a2],ta=tv(a);
       const lp=old.map(row=>path(row,ta)),rp=neo.map(row=>path(row,a));
       const left=lp.map(row=>[row[2],row[1],row[0]]);
       const right=[rp[1].map(z=>mul(q,z)),rp[0].map(z=>mul(q,z)),
         ...rp.slice(2,5).map(row=>row.map(z=>mul(q2,z))),
         rp[6].map(z=>mul(q2,z)),rp[5].map(z=>mul(q2,z))];
       ok(eq(left,right),"labelled paths");
       const lm=lp.map(brc9),rm=rp.map(brc9);
       ok(eq(lm,[rm[1],rm[0],...rm.slice(2,5),rm[6],rm[5]]),"mass permutation");
       ok(lm.concat(rm).every(z=>z[1]===0&&z[0]>=0),"nonnegative BRC");
       const input=64*(sq(a0)+sq(a1)+sq(a2));
       ok(lm.reduce((s,z)=>s+z[0],0)===input,"S4 total");
       ok(rm.reduce((s,z)=>s+z[0],0)===input,"S7 total");
       paired++;bins+=14;pairProducts+=126;massChecks+=2;
     }
   }
 }
 ok(mapped.size===6&&paired===5184,"full coverage");
 const ex4=rows(S4[0],I,4).slice(0,2).map(row=>brc9(path(row,tv([O,Z,Z]))));
 const ex7=rows(tm(S4[0]),cj(I),7).slice(0,2).map(row=>brc9(path(row,[O,Z,Z])));
 ok(eq(ex4,[[0,0],[16,0]])&&eq(ex7,[[16,0],[0,0]]),"fixed event outcome counterexample");
 return {schema:"EM_PREFIX300_EQUIVARIANT_C4_BRC_CERTIFICATE_V1",
 status:"AUTHOR_SIDE_EXACT_UNREVIEWED_NOT_ADMITTED",
 s4_orbits_checked:6,s7_orbits_matched:mapped.size,c4_phases:4,
 source_packets_per_phase:216,paired_inputs:paired,direct_bin_readouts:bins,
 ordered_labelled_source_products:pairProducts,total_mass_checks:massChecks,
 gram_entries:gramEntries,exact_labelled_coefficient_equalities:sourceEntries,
 event_counterexample:{q:"i",new_source_a:[[1,0],[0,0],[0,0]],
 old_S4_event_mass_num64:[0,16],new_S7_event_mass_num64:[16,0]},
 strict_integer_gaussian:true,native_Detector_model_law_id:null};
}
if (typeof module!=="undefined" && module && require.main===module)
  console.log(JSON.stringify(run(),null,2));
