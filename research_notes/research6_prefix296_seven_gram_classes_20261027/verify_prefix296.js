// PREFIX-296 exact C4-BRC certificate; run with node verify_prefix296.js
function verify(){
const c=(a,b=0)=>[BigInt(a),BigInt(b)],z=c(0),o=c(1);
const plus=(a,b)=>[a[0]+b[0],a[1]+b[1]],minus=(a,b)=>[a[0]-b[0],a[1]-b[1]];
const mul=(a,b)=>[a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]],co=a=>[a[0],-a[1]];
const norm=a=>a[0]*a[0]+a[1]*a[1],eq=(a,b)=>a[0]===b[0]&&a[1]===b[1],sum=a=>a.reduce(plus,z);
const H=[[c(48),c(-16),z],[c(-16),c(32),c(16)],[z,c(16),c(48)]];
const W=[
{d:"011",e:"12",u:[0,1],m:[[[6,2],[-3,0],[-2,-1]],[[2,2],[2,-1],[3,4]],[[0,0],[-4,1],[-1,4]]]},
{d:"011",e:"12",u:[0,-1],m:[[[6,2],[-1,0],[2,-1]],[[2,2],[-2,-3],[-5,0]],[[0,0],[-4,-1],[-1,-4]]]},
{d:"101",e:"02",u:[-1,0],m:[[[6,3],[-1,-1],[1,0]],[[1,1],[-5,-2],[-4,-1]],[[0,0],[-1,0],[5,-2]]]},
{d:"102",e:null,u:null,m:[[[5,2],[0,0],[-2,0]],[[4,1],[-4,0],[2,1]],[[1,0],[0,-4],[1,-6]]]},
{d:"110",e:"01",u:[0,1],m:[[[6,3],[-1,-1],[1,0]],[[1,0],[-3,0],[-3,5]],[[1,0],[-4,2],[-3,-2]]]},
{d:"110",e:"01",u:[0,-1],m:[[[6,2],[-2,1],[-1,0]],[[2,1],[0,-5],[1,-3]],[[1,1],[-1,0],[1,6]]]},
{d:"201",e:null,u:null,m:[[[6,1],[-4,0],[0,1]],[[2,1],[4,0],[4,1]],[[2,0],[0,0],[-5,-2]]]}];
const key=(d,e,u)=>d+":"+(e?e+":"+u.join(","):"diag");
const Sfor=(d,e,u)=>{const s=[[z,z,z],[z,z,z],[z,z,z]];for(let j=0;j<3;j++)s[j][j]=c(+d[j]);
if(e){const j=+e[0],k=+e[1];s[j][k]=c(...u);s[k][j]=co(c(...u));}return s;};
const det=a=>plus(minus(mul(a[0][0],minus(mul(a[1][1],a[2][2]),mul(a[1][2],a[2][1]))),
mul(a[0][1],minus(mul(a[1][0],a[2][2]),mul(a[1][2],a[2][0])))),
mul(a[0][2],minus(mul(a[1][0],a[2][1]),mul(a[1][1],a[2][0]))));
const sumsq=new Set();for(let x=0;x<=223;x++)for(let y=0;y<=223;y++)sumsq.add(x*x+y*y);
let count=0,diagonal=0,edge=0,maxdet=0;const survivors=[];
for(let a=0;a<3;a++)for(let b=0;b<3;b++)for(let h=0;h<3;h++){
const d=""+a+b+h,opts=[[null,null]];diagonal++;
for(let i=0;i<3;i++)for(let j=i+1;j<3;j++)if(d[i]==="1"&&d[j]==="1")
for(const u of [[1,0],[-1,0],[0,1],[0,-1]]){opts.push([""+i+j,u]);edge++;}
for(const [e,u] of opts){count++;const s=Sfor(d,e,u),A=H.map((row,i)=>row.map((v,j)=>minus(v,s[i][j]))),n=det(A);
if(n[1]!==0n||n[0]<0n||n[0]>50000n)throw Error("det");
maxdet=Math.max(maxdet,Number(n[0]));if(sumsq.has(Number(n[0])))survivors.push(key(d,e,u));}}
if(count!==63||diagonal!==27||edge!==36||
JSON.stringify(survivors.sort())!==JSON.stringify(W.map(w=>key(w.d,w.e,w.u)).sort()))throw Error("class enumeration");
const gram=rows=>Array.from({length:3},(_,j)=>Array.from({length:3},(_,k)=>
sum(rows.map(r=>mul(co(r[j]),r[k])))));
const Lfor=w=>{if(w.e){const row=[z,z,z];row[+w.e[0]]=o;row[+w.e[1]]=c(...w.u);return [row];}
const out=[];for(let j=0;j<3;j++)if(w.d[j]!=="0"){const row=[z,z,z];row[j]=w.d[j]==="2"?c(1,1):o;out.push(row);}return out;};
const ph=(rows,q)=>rows.map(r=>r.map((v,j)=>mul(v,j===0?o:j===1?q:mul(q,q))));
const E=q=>[[c(4),mul(c(4),q),z],[z,c(-4),mul(c(4),q)]];
const alphabet=[c(0),c(1),c(-1),c(0,1),c(0,-1),c(1,1)];
let readouts=0,pairs=0,tests=0,grams=0,masses=0,losses=0;const details=[];
const brc=(r,a)=>{const leg=r.map((v,j)=>mul(v,a[j]));let mass=z;
for(let j=0;j<3;j++)for(let k=0;k<3;k++){mass=plus(mass,mul(co(leg[j]),leg[k]));pairs++;}
readouts++;if(mass[1]!==0n||mass[0]!==norm(sum(leg)))throw Error("direct BRC");return mass[0];};
for(const w of W){const S=Sfor(w.d,w.e,w.u),M=w.m.map(row=>row.map(v=>c(...v))),L=Lfor(w);
const gm=gram(M),gl=gram(L);for(let j=0;j<3;j++)for(let k=0;k<3;k++){
if(!eq(plus(gm[j][k],S[j][k]),H[j][k])||!eq(gl[j][k],S[j][k]))throw Error("witness gram");grams+=2;}
const dd=det(M);details.push({d:w.d,edge:w.e||"none",unit:w.u?w.u.join(","):"none",
rank:S[0][0][0]===999n?0:L.length,detM:dd[0].toString()+(dd[1]<0n?"":"+")+dd[1].toString()+"i"});
for(const q of [c(1),c(0,1),c(-1),c(0,-1)]){
const full=[...E(q),...ph(M,q),...ph(L,q)],sq=gram(ph(L,q)),gg=gram(full);
for(let j=0;j<3;j++)for(let k=0;k<3;k++){if(!eq(gg[j][k],j===k?c(64):z))throw Error("isometry");grams++;}
for(const a0 of alphabet)for(const a1 of alphabet)for(const a2 of alphabet){
const a=[a0,a1,a2],out=full.map(row=>brc(row,a));
if(out.reduce((x,y)=>x+y,0n)!==64n*(norm(a0)+norm(a1)+norm(a2)))throw Error("mass");
const leak=out.slice(5).reduce((x,y)=>x+y,0n),quad=sum(a.map((v,j)=>sum(a.map((w,k)=>mul(co(v),mul(sq[j][k],w))))));
if(quad[1]!==0n||quad[0]!==leak)throw Error("leak");tests++;masses++;losses++;}}}
const iq=c(0,1);const pm=a=>E(iq).map(row=>brc(row,a)).reduce((u,v)=>u+v,0n);
if(pm([c(1),c(0,1),c(1)])!==0n||pm([c(1),c(0,-1),c(1)])!==128n)throw Error("phase partners");
return {schema:"EM_PREFIX296_EXACT_BRC_V1",status:"PASS",number_domain:"BigInt Z[i]",
denominator:8,candidate_gram_matrices:count,diagonal_candidates:diagonal,edge_candidates:edge,
norm_survivors:survivors.length,norm_exclusions:count-survivors.length,
max_determinant:maxdet,examples:details,rank1_cases:5,rank2_cases:2,
C4_phases:4,inputs_per_phase:216,phase_model_input_cases:tests,
direct_BRC_bin_readouts:readouts,ordered_source_pairs:pairs,
Gram_entry_checks:grams,mass_checks:masses,leak_identity_checks:losses,
phase_partner_probabilities:["0","2/3"],native_Hn_checked:false};}
console.log(JSON.stringify(verify(),null,2));
