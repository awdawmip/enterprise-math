// Exact C4-BRC source-labelled readout for the rank-two optimum (PREFIX-299).
// Usage: node verify_prefix299_brc.js RESULTS_PREFIX299.json
const fs=require('fs'), R=JSON.parse(fs.readFileSync(process.argv[2]||'RESULTS_PREFIX299.json'));
const A=(x,y)=>[x[0]+y[0],x[1]+y[1]], M=(x,y)=>[x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]], C=x=>[x[0],-x[1]], N=x=>x[0]*x[0]+x[1]*x[1];
const O=[1,0],Z=[0,0],F=[Z,O,[-1,0],[0,1],[0,-1],[1,1]];
function read(paths){let total=Z;for(let j=0;j<3;j++)for(let k=0;k<3;k++)total=A(total,M(C(paths[j]),paths[k]));if(total[1]!==0||total[0]<0)throw Error('BRC mass');return total[0];}
let combos=0,bins=0,ordered=0,grams=0;
for(const key of ['S4','S7']){
 const data=R.cases[key], s=data.S;
 const G=data.Gram, L=s[0]===1?[[O,Z,Z],[Z,Z,[1,1]]]:[[[1,1],Z,Z],[Z,Z,O]];
 for(const B of data.all_orbits){
  for(let j=0;j<3;j++)for(let k=0;k<3;k++){let dot=Z;for(let t=0;t<3;t++)dot=A(dot,M(C(B[t][j]),B[t][k]));if(JSON.stringify(dot)!==JSON.stringify(G[j][k]))throw Error('Gram');grams++;}
  for(const q of [O,[0,1],[-1,0],[0,-1]])for(const a of F)for(const b of F)for(const c of F){
   const input=[a,b,c], d=[a,M(q,b),M(M(q,q),c)];
   const E=[[[4,0],[4,0],Z],[Z,[-4,0],[4,0]]];
   let masses=[];
   for(const row of [...E,...B,...L]){masses.push(read(row.map((v,j)=>M(v,d[j]))));bins++;ordered+=9;}
   if(masses.reduce((u,v)=>u+v,0)!==64*input.reduce((u,v)=>u+N(v),0))throw Error('conservation');
   if(masses[5]+masses[6]!==s[0]*N(a)+s[2]*N(c))throw Error('leak');
   let ev=16*(N(A(a,M(q,b)))+N(A([-b[0],-b[1]],M(q,c))));
   if(masses[0]+masses[1]!==ev)throw Error('event');
   combos++;
  }
 }
}
if(combos!==10368||bins!==72576||ordered!==653184||grams!==108)throw Error('counts');
console.log(JSON.stringify({source:'PREFIX299',cases:combos,direct_BRC_bin_readouts:bins,ordered_path_pairs:ordered,Gram_entries:grams,status:'PASS'}));
