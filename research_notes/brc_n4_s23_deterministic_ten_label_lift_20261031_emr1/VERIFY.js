// Exact integer certificate: S23 deterministic 10-label lift and randomized obstruction.
// Run: node VERIFY.js
// M rows are six prepared inputs; columns AU0,AU1,AV,BU0,BU1,BV; units /20.
const M = [[10,10,0,0,0,0],[9,11,0,0,0,0],[0,0,20,0,0,0],
           [0,0,0,10,10,0],[0,0,0,2,18,0],[0,0,0,0,0,20]];
const src = [0,0,1,2,2,3], first=[0,0,1,1], second=[0,1,0,2];
const cls = [0,0,1,2,2,3];
// Each label contains two time choices per source category AU,AV,BU,BV.
const boxRows = [
  '34 24 34 24','34 23 34 34','34 34 34 23','24 24 12 12','12 12 24 34',
  '12 13 23 24','23 34 12 13','24 34 12 14','13 12 13 13','12 12 14 12'];
const boxes = boxRows.map(s=>s.split(' ').map(pair=>[Number(pair[0]),Number(pair[1])]));
function assert(x,s){if(!x) throw Error(s);}
function stop(a,b,c){return src.map((v,j)=> !(a & (1<<first[v])) ? 1 :
                  !(b & (1<<second[v])) ? 2 : (c & (1<<j)) ? 3 : 4);}
function heavy(st){return [st[1],st[2],st[4],st[5]];}
function covers(box,h){return h.every((t,j)=>box[j].includes(t));}
function exactP20(st,i,t){let z=0;for(let j=0;j<6;j++)if(st[j]===t)z+=M[i][j];return z;}
function exactQ40(box,i,t){let z=0;for(let j=0;j<6;j++)if(box[cls[j]].includes(t))z+=M[i][j];return z;}
function tv80(st,box,i){let z=0;for(let t=1;t<=4;t++)z+=Math.abs(2*exactP20(st,i,t)-exactQ40(box,i,t));return z;}
assert(M.every(row=>row.reduce((x,y)=>x+y,0)===20),'row sums');
let policies=0,matched=0,risk40=0;const signatures=new Set(), allheavy=new Set();
for(let a=0;a<4;a++)for(let b=0;b<8;b++)for(let c=0;c<64;c++){
  const st=stop(a,b,c),h=heavy(st),key=h.join('');policies++;allheavy.add(key);
  if(st[0]===st[1] && st[3]===st[4])signatures.add(key);
  const chosen=boxes.findIndex(box=>covers(box,h));
  assert(chosen>=0,'uncovered deterministic heavy signature '+key);
  matched++;
  let best=Infinity;
  for(const box of boxes){let worst=0;for(let i=0;i<6;i++)worst=Math.max(worst,tv80(st,box,i));best=Math.min(best,worst);}
  assert(best===40,'deterministic minimax is not exactly half '+a+' '+b+' '+c+': '+best);
  risk40++;
}
assert(policies===2048 && matched===2048 && risk40===2048,'policy counts');
assert(signatures.size===64 && allheavy.size===64,'signature counts');
for(const s of signatures) assert(boxes.some(b=>covers(b,s.split('').map(Number))),'64 cover');
// Policy-level behavioral randomization: B always stops at T=1; for A, at T=1
// flip a 2/3 continuation coin. If continuing, AU0 stops at T=3, AU1 at T=4,
// AV at T=3. This equals (2/3)*H0+(1/3)*H1 on all six prepared rows.
const H0=stop(1,3,21),H1=stop(0,5,18);
assert(H0.join(',')==='3,4,3,1,1,1','H0');
assert(H1.every(t=>t===1),'H1');
// For this mixture the actual p has denominator 60, q denominator 40.
// Scale both to 120; TV=sum(abs(p120-q120))/240.
const mixRisk=[];
for(const box of boxes){let worst=0;
  for(let i=0;i<6;i++){let diff=0;
    for(let t=1;t<=4;t++){
      const p120=2*(2*exactP20(H0,i,t)+exactP20(H1,i,t));
      const q120=3*exactQ40(box,i,t);
      diff+=Math.abs(p120-q120);
    }
    worst=Math.max(worst,diff);
  }
  mixRisk.push(worst);
}
const mixMin=Math.min(...mixRisk);
assert(mixMin===160,'the two-policy behavioral mixture must have worst risk 2/3');
const result={status:'PASS_BRC_N4_S23_FULL_DETERMINISTIC_M10_LIFT_AND_RANDOMIZED_WARNING_20261031',
  complete_deterministic_policies:policies,distinct_heavy_signatures:allheavy.size,
  restricted_signature_count:signatures.size,label_boxes:boxes.length,
  deterministic_minimax_numerator_over_80:40,
  mixture_stops:[H0,H1],mixture_weights:['2/3','1/3'],
  mixture_minimax_numerator_over_240:mixMin,mixture_label_max_numerators_over_240:mixRisk,
  theorem:'R^S23_deterministic_{k,m}(T)=1/2 for k>=4 and 10<=m<=63; randomized full-game not established'};
if(typeof console!=='undefined')console.log(JSON.stringify(result,null,2));
result;
