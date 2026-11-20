"use strict";
// R762GY: exact finite checker for an endpoint-choice extension of R762GX.
const assert = (c, msg) => { if (!c) throw Error(msg); };
const V = [0, 1, 2, 3];
const EDGES = [[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]];
const EKEY = e => e.join("");
const SORT = a => a.slice().sort((x,y)=>x-y);
const EINDEX = Object.fromEntries(EDGES.map((e,i)=>[EKEY(e),i]));
const PHASE = {"01":0,"23":0,"02":1,"13":1,"03":2,"12":2};
function parity(a) {
  let swaps=0; for(let i=0;i<a.length;i++) for(let j=i+1;j<a.length;j++) if(a[i]>a[j]) swaps++;
  return swaps%2 ? -1 : 1;
}
function turn(v,u,chi) {
  const ab=V.filter(x=>x!==v && x!==u);
  return parity([v,u,ab[0],ab[1]])===chi ? ab[0] : ab[1];
}
function steps(edge,chi) {
  return edge.map(v=>{
    const u=edge.find(w=>w!==v);
    return {active:v, next:SORT([v,turn(v,u,chi)])};
  });
}
function permutations(a) {
  if(a.length===0) return [[]];
  return a.flatMap((v,i)=>permutations(a.filter((_,j)=>j!==i)).map(t=>[v,...t]));
}
function exactDP(chi,maxM=12) {
  let cur=new Map([["0|0,0,0,0",1]]); // initial edge 01 at index 0
  const out=[];
  for(let m=0;m<=maxM;m++) {
    let port=0,cell=0,joint=0,total=0;
    for(const [k,c] of cur){
      const [idx,ztext]=k.split("|"); const z=ztext.split(",").map(Number);
      const atPort=Number(idx)===0; const atCell=z.every(v=>v===0);
      if(atPort)port+=c; if(atCell)cell+=c;
      if(atPort&&atCell)joint+=c; total+=c;
    }
    assert(total===4**m,"branch total at "+m);
    out.push({m,port,cell,joint,total,stateCount:cur.size});
    if(m===maxM)break;
    const next=new Map();
    for(const [k,c] of cur){
      const [idx,ztext]=k.split("|"); const z=ztext.split(",").map(Number);
      for(const {active,next:nextEdge} of steps(EDGES[Number(idx)],chi)){
        for(const sign of [-1,1]){
          const zz=z.slice(); zz[active]+=sign;
          const kk=EINDEX[EKEY(nextEdge)]+"|"+zz.join(",");
          next.set(kk,(next.get(kk)||0)+c);
        }
      }
    }
    cur=next;
  }
  return out;
}
function sixPathCertificate(chi) {
  let paths=[{edge:[0,1],vertices:[]}];
  for(let k=0;k<6;k++){
    paths=paths.flatMap(p=>steps(p.edge,chi).map(s=>({edge:s.next,vertices:[...p.vertices,s.active]})));
  }
  const returned=paths.filter(p=>EKEY(p.edge)==="01");
  const even=returned.filter(p=>V.every(v=>p.vertices.filter(x=>x===v).length%2===0));
  const patternCounts={"6":0,"2+2+2":0};
  for(const p of even){
    const vals=V.map(v=>p.vertices.filter(x=>x===v).length).filter(n=>n>0).sort((a,b)=>b-a).join("+");
    assert(Object.hasOwn(patternCounts,vals),"unexpected six-step balanced vertex pattern "+vals);
    patternCounts[vals]++;
  }
  assert(returned.length===32,"six-step port words");
  assert(patternCounts["6"]===2 && patternCounts["2+2+2"]===6,"six-step pattern histogram");
  return {portEndpointWords:returned.length,balancedPatternCount:patternCounts,zeroCellAndPortSignWords:2*20+6*8};
}
function main(){
  let phaseCases=0, equivariantCases=0;
  for(const chi of [-1,1])for(const e of EDGES){
    const opts=steps(e,chi);
    assert(opts.length===2 && EKEY(opts[0].next)!==EKEY(opts[1].next),"different next edges");
    for(const opt of opts){
      assert(PHASE[EKEY(opt.next)] === ((PHASE[EKEY(e)]+(chi===1?1:2))%3),"matching phase");
      phaseCases++;
    }
  }
  for(const pi of permutations(V))for(const chi of [-1,1])for(const e of EDGES){
    const ep=SORT(e.map(x=>pi[x])); const cp=parity(pi)*chi;
    for(const {active,next} of steps(e,chi))for(const sign of [-1,1]){
      const transformed=SORT(next.map(x=>pi[x]));
      const computed=steps(ep,cp).find(s=>s.active===pi[active]);
      assert(EKEY(computed.next)===EKEY(transformed),"S4 port covariance");
      const hv=EDGES.map(([a,b])=>+(a===active||b===active));
      const hp=EDGES.map(([a,b])=>+(a===pi[active]||b===pi[active]));
      for(let i=0;i<EDGES.length;i++){
        const image=EINDEX[EKEY(SORT(EDGES[i].map(x=>pi[x])))];
        assert(sign*hv[i]===sign*hp[image],"S4 signed six-axis covariance");
      }
      equivariantCases++;
    }
  }
  assert(equivariantCases===1152,"S4 covariance coverage");
  const plus=exactDP(1), minus=exactDP(-1);
  for(let m=0;m<plus.length;m++){
    const a=plus[m], b=minus[m];
    assert(a.port===b.port && a.cell===b.cell && a.joint===b.joint,"chiral symmetry m="+m);
    const wantPort=m===0?1:m%3===0?4**m/2:0;
    assert(a.port===wantPort,"port-return formula m="+m);
    if(m%6!==0) assert(a.joint===0,"joint return divisibility m="+m);
  }
  const cert=sixPathCertificate(1);
  assert(plus[6].joint===cert.zeroCellAndPortSignWords,"m6 independent enumeration");
  assert(plus[6].joint===88 && plus[12].joint===61160,"frozen regression counts");
  return {schema:"R762GY_EXACT_FINITE_EVIDENCE_V1", model:"K4-STAR_ENDPOINT_CHOICE_SIGNED_CHIRAL_CANDIDATE", phaseCases, equivariantCases, maxExactLength:12, branchCountPerStep:4, phasePartitions:[["01","23"],["02","13"],["03","12"]], sixStepCertificate:cert, counts:plus, negativeChiralityCrossCheck:"PASS", authorCheck:"PASS", independentReview:"NOT_REVIEWED"};
}
const result=main();
if(typeof module!=="undefined") module.exports={main,turn,steps,exactDP};
if(typeof require!=="undefined" && require.main===module) console.log(JSON.stringify(result,null,2));
