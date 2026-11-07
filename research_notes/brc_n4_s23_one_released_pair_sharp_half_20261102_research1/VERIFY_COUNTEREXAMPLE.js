// Executed exact BigInt rational certificate. Node.js 18+; original six-source BRC S23.
function verify(){
  function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){const t=a%b;a=b;b=t;}return a;}
  function f(n,d=1n){n=BigInt(n);d=BigInt(d);if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return [n/g,d/g];}
  function parse(s){const a=String(s).split("/");return f(a[0],a[1]||1);}
  function add(a,b){return f(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);}
  function sub(a,b){return f(a[0]*b[1]-b[0]*a[1],a[1]*b[1]);}
  function mul(a,b){return f(a[0]*b[0],a[1]*b[1]);}
  function div(a,b){return f(a[0]*b[1],a[1]*b[0]);}
  function abs(a){return f(a[0]<0n?-a[0]:a[0],a[1]);}
  function cmp(a,b){const d=a[0]*b[1]-b[0]*a[1];return d<0n?-1:d>0n?1:0;}
  function eq(a,b){return cmp(a,b)===0;}
  function str(a){return a[1]===1n?String(a[0]):`${a[0]}/${a[1]}`;}
  function sum(a){return a.reduce(add,f(0));}
  function max(a){return a.reduce((x,y)=>cmp(x,y)>=0?x:y);}
  function min(a){return a.reduce((x,y)=>cmp(x,y)<=0?x:y);}
  function assert(x,s){if(!x)throw new Error(s);}
  const M=[[10,10,0,0,0,0],[9,11,0,0,0,0],[0,0,20,0,0,0],[0,0,0,10,10,0],[0,0,0,2,18,0],[0,0,0,0,0,20]];
  const AA=[0,0,0,1,1,1],BB=[2,2,3,2,2,4],CC=[5,6,7,8,9,10],GROUP=[0,0,1,2,2,3];
  function rows(z){const latent=AA.map((a,s)=>{const A=z[a],B=z[BB[s]],C=z[CC[s]],u=sub(f(1),A),v=mul(u,sub(f(1),B));return [A,mul(u,B),mul(v,C),mul(v,sub(f(1),C))];});return M.map(row=>[0,1,2,3].map(j=>sum(row.map((m,s)=>mul(f(m,20),latent[s][j])))));}
  function dec(d){return M.map(row=>[0,1,2,3].map(j=>sum(row.map((m,s)=>mul(f(m,20),d[GROUP[s]][j])))));}
  function pair(s){return s.split(" ").map(ab=>[0,1,2,3].map(j=>f((ab.match(new RegExp(String(j+1),"g"))||[]).length,2)));}
  function tv(p,q){return div(sum(p.map((x,j)=>abs(sub(x,q[j])))),f(2));}
  function loss(p,q){return max(p.map((row,i)=>tv(row,q[i])));}
  const A=(s,t)=>[s,t,"0","0","0","0","1","1","1","0","1"];
  const N=(s,t)=>[s,t,"0","0","0","1","0","0","0","0","0"];
  const raw={
    W:["1","0","0","0","1","0","0","0","0","0","0"],
    J:["1","1/3","0","0","0","0","0","0","0","1","0"],
    A:A("1/7","1"),B:A("1","1/7"),C:N("1/7","1"),X:A("1","1/15"),
    Y:["1","0","0","0","0","0","0","0","1","1","1"]};
  const base=["34 24 34 24","34 23 34 34","34 34 34 23","24 24 12 12","12 12 24 34","12 13 23 24","23 34 12 13","24 34 12 14"];
  const D9=["1 0 0 0","1 0 0 0","0 0 1/2 1/2","0 1/2 1/2 0"].map(x=>x.split(" ").map(parse));
  const D10=["1 0 0 0","1 0 0 0","1/3 0 1/3 1/3","1/3 0 0 2/3"].map(x=>x.split(" ").map(parse));
  const prep=Object.fromEntries(Object.entries(raw).map(([k,v])=>[k,rows(v.map(parse))]));
  const banks=base.map(x=>dec(pair(x))).concat([dec(D9),dec(D10)]);
  for(const [k,p] of Object.entries(prep))for(const row of p)assert(eq(sum(row),f(1))&&row.every(x=>cmp(x,f(0))>=0),`P ${k}`);
  for(const d of [D9,D10])for(const row of d)assert(eq(sum(row),f(1))&&row.every(x=>cmp(x,f(0))>=0),"stochastic kernel");
  const frozen=Object.fromEntries(Object.entries(prep).map(([k,p])=>[k,str(min(banks.slice(0,8).map(q=>loss(p,q))))]));
  assert(JSON.stringify(frozen)==JSON.stringify({W:"1",J:"2/3",A:"4/7",B:"4/7",C:"4/7",X:"8/15",Y:"1"}),"frozen");
  const cert={
    WJB:[6,"2/14/3","20/7"],WJY:[6,"2/14/3","3"],WAB:[6,"24/1/3","20/7"],
    WAC:[3,"12/3/4","19/7"],WAY:[6,"24/1/3","3"],WBC:[6,"24/3/1","20/7"],
    WCY:[6,"24/1/3","3"],JAC:[3,"12/3/4","19/7"],ABC:[3,"23/1/4","19/7"],
    ABY:[5,"12/4/3","97/35"],ACY:[3,"23/4/1","19/7"],BCY:[5,"24/1/3","97/35"]};
  for(const [triple,[row,event,mass]] of Object.entries(cert)){
    const pieces=event.split("/"),atoms=pieces.join("").split("");assert(atoms.length===new Set(atoms).size,`not disjoint ${triple}`);
    const ev=sum([...triple].map((k,j)=>sum(pieces[j].split("").map(a=>prep[k][row-1][Number(a)-1]))));
    assert(eq(ev,parse(mass))&&cmp(div(sub(ev,f(1)),f(3)),f(4,7))>=0,`bad event ${triple}`);
  }
  const colors={};
  for(let mask=0;mask<32;mask++){
    const c={W:0};"JABCY".split("").forEach((k,j)=>c[k]=(mask>>j)&1);
    const edge=Object.keys(cert).find(k=>new Set(k.split("").map(x=>c[x])).size===1);
    assert(!!edge,`color ${mask}`);colors[String(mask).padStart(2,"0")]=edge;
  }
  const achieved=Object.fromEntries(Object.entries(prep).map(([k,p])=>[k,str(min(banks.map(q=>loss(p,q))))]));
  assert(JSON.stringify(achieved)==JSON.stringify({W:"1/2",J:"4/15",A:"4/7",B:"1/2",C:"4/7",X:"1/2",Y:"1/2"}),"upper risks");

  // Arbitrary real stochastic D9,D10 plus any one released old pair label.
  const Dstar=["1/7 0 3/7 3/7","1/7 0 3/7 3/7","1 0 0 0","1 0 0 0"].map(x=>x.split(" ").map(parse));
  const triples=[dec(D9),dec(D10),dec(Dstar)];
  const compulsory="WJACY".split("");
  const pairs=[["W","J",5],["W","A",3],["W","C",3],["W","Y",3],
               ["Y","J",5],["Y","A",3],["Y","C",3]];
  for(const [a,b,i] of pairs)assert(eq(tv(prep[a][i],prep[b][i]),f(1)), "disjoint pair "+a+b);
  const mass=add(add(prep.J[2][0],prep.J[2][1]),add(prep.A[2][2],prep.C[2][3]));
  assert(eq(mass,f(19,7))&&eq(div(sub(mass,f(1)),f(3)),f(4,7)),"JAC disjoint events");
  for(let v=0;v<243;v++){
    const colors={},order=compulsory;let n=v;
    for(const k of order){colors[k]=n%3;n=Math.floor(n/3);}
    assert(pairs.some(([a,b])=>colors[a]===colors[b]) ||
           (colors.J===colors.A&&colors.A===colors.C),"3-label coloring "+v);
  }
  let released={},fixedOthersMin={};
  for(let h=0;h<8;h++){
    const fixedOthers=banks.slice(0,8).filter((_,j)=>j!==h);
    const minima=Object.fromEntries(compulsory.map(k=>[k,str(min(fixedOthers.map(q=>loss(prep[k],q))))]));
    assert(compulsory.every(k=>cmp(parse(minima[k]),f(1,2))>0),"fixed seven insufficient "+h);
    fixedOthersMin[String(h+1)]=minima;
    const candidate=fixedOthers.concat(triples);
    const risks=Object.fromEntries(Object.entries(prep).map(([k,p])=>[k,str(min(candidate.map(q=>loss(p,q))))]));
    assert(eq(max(Object.values(risks).map(parse)),f(1,2)),"upper "+h);
    released[String(h+1)]=risks;
  }
  const freeOnly=Object.fromEntries(Object.entries(prep).map(([k,p])=>[k,str(min(triples.map(q=>loss(p,q))))]));
  assert(JSON.stringify(freeOnly)==JSON.stringify({W:"1/2",J:"4/15",A:"3/7",B:"1/2",C:"3/7",X:"1/2",Y:"1/2"}),"new kernel upper");
  

  // Full-source exact legal off-witness where every trial kernel has TV risk one.
  const zOff=["0","1","0","1","0","1","1","0","0","0","0"].map(parse);
  const pOff=rows(zOff);
  const expectedOff=["0010","0010","0100","1000","1000","1000"];
  for(let i=0;i<6;i++)assert(pOff[i].map(str).join("")===expectedOff[i], "off witness target "+i);
  const rowIdx=[3,3,3,0,0,0,2,0,0,0,2];
  const atomIdx=[0,0,0,2,2,2,1,2,2,2,1];
  const allKernels=base.map(x=>dec(pair(x))).concat([dec(D9),dec(D10),dec(Dstar)]);
  const offRisk=[];
  for(let i=0;i<allKernels.length;i++){
    const row=rowIdx[i], atom=atomIdx[i];
    assert(eq(pOff[row][atom],f(1)) && eq(allKernels[i][row][atom],f(0)),"zero event risk "+i);
    const exactRisk=loss(pOff,allKernels[i]);
    assert(eq(exactRisk,f(1)),"full risk "+i);
    offRisk.push(str(exactRisk));
  }
  for(let h=0;h<8;h++)assert(eq(min(offRisk.filter((_,j)=>j!==h).map(parse)),f(1)),"released label "+h);

  return {result:"PASS_BRC_N4_S23_TRIAL_BANK_EXACT_COUNTEREXAMPLE_20261102",off_witness:["0","1","0","1","0","1","1","0","0","0","0"],off_target_rows:expectedOff,off_all_eleven_risks:offRisk,off_bad_rows_one_based:rowIdx.map(x=>x+1),off_zero_atom_one_based:atomIdx.map(x=>x+1),all_eight_freed_label_cases_have_loss_one:true,exact_optimum:"1/2",strict_drop_from_prior:"1/14",pair_disjoint_certificates:pairs.length,three_label_colorings:243,triple_event_mass:str(mass),freed_label_risks:released,fixed_seven_minima:fixedOthersMin,free_only_risks:freeOnly,pin:"43ec6098b1330ae86d0a7863be336c5d97f6ef34",frozen,achieved,events_checked:Object.keys(cert).length,colorings_checked:Object.keys(colors).length,colors,exact_rational:true,scope:"fixed eight decoders; seven lawful witnesses; arbitrary real free decoder kernels",mathematical_status:"AUTHOR_PROOF_UNREVIEWED_NOT_ADMITTED"};
}
console.log(JSON.stringify(verify(), null, 2));
