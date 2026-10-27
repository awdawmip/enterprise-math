"use strict";
// PREFIX-290 exact Q(i) C4-BRC source-pair verifier. No float/time propagation.
const ph=[[1,0],[0,1],[-1,0],[0,-1]],o=[1,0],n=[-1,0],z=[0,0];
const plus=(x,y)=>[x[0]+y[0],x[1]+y[1]], neg=x=>[-x[0],-x[1]];
const cj=x=>[x[0],-x[1]], mul=(x,y)=>[x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]];
const eq=(x,y)=>x[0]===y[0]&&x[1]===y[1], sub=(x,y)=>plus(x,neg(y));
function terms(q){let q2=mul(q,q);return [
 [[0,o],[1,q]],[[1,n],[2,q]],
 [[0,o],[1,neg(q)]],[[0,o],[2,q2]],
 [[0,o],[2,neg(q2)]],[[1,q],[2,q2]]
];}
function amp(t,a){let s=z;for(const [j,v]of t)s=plus(s,mul(v,a[j]));return s;}
function pair(t,a,b){let s=z;for(const [j,v]of t)for(const [k,w]of t)
 s=plus(s,mul(mul(v,a[j]),cj(mul(w,b[k]))));return s;}
function dot(a,b){let s=z;for(let j=0;j<3;j++)s=plus(s,mul(a[j],cj(b[j])));return s;}
function det(m){return plus(sub(mul(m[0][0],sub(mul(m[1][1],m[2][2]),mul(m[1][2],m[2][1]))),
 mul(m[0][1],sub(mul(m[1][0],m[2][2]),mul(m[1][2],m[2][0])))),
 mul(m[0][2],sub(mul(m[1][0],m[2][1]),mul(m[1][1],m[2][0]))));}
function insist(ok,msg){if(!ok)throw Error(msg);}
function run(){
 let packets=[];for(let m0=1;m0<=4;m0++)for(let m1=1;m1<=4;m1++)
 for(let k1=0;k1<4;k1++)for(let m2=1;m2<=4;m2++)for(let k2=0;k2<4;k2++)
 packets.push([[m0,0],mul([m1,0],ph[k1]),mul([m2,0],ph[k2])]);
 insist(packets.length===1024,"packet count");
 let bins=0,masses=0,crosses=0,decodes=0;
 for(let qi=0;qi<4;qi++){
  let q=ph[qi],q2=mul(q,q),T=terms(q),G=[];
  for(let i=0;i<3;i++){G[i]=[];for(let j=0;j<3;j++){
   const ai=[z,z,z],bj=[z,z,z];ai[i]=o;bj[j]=o;
   let s=z;for(let k=2;k<6;k++)s=plus(s,pair(T[k],ai,bj));
   G[i][j]=s;
  }}
  insist(eq(det(G),[12,0]),"complement determinant qi="+qi);
  for(let pi=0;pi<packets.length;pi++){
   let a=packets[pi],c=T.map(t=>amp(t,a)),total=z;
   for(let k=0;k<6;k++){
    let p=pair(T[k],a,a);
    insist(p[1]===0&&p[0]>=0&&eq(p,mul(c[k],cj(c[k]))),"bin q/p="+qi+"/"+pi);
    total=plus(total,p);bins++;
   }
   let Z=dot(a,a);insist(eq(total,[4*Z[0],0]),"total mass");masses++;
   const r0=plus(c[3],c[4]);
   const r2=mul(cj(q2),sub(c[3],c[4]));
   const r1=mul(cj(q),plus(sub(mul([2,0],c[5]),c[3]),c[4]));
   insist([r0,r1,r2].every((r,i)=>eq(r,mul([2,0],a[i]))),"Ec decode");decodes++;
   let b=[a[2],a[0],a[1]],s=z;
   for(let t of T)s=plus(s,pair(t,a,b));
   let v=dot(a,b);insist(eq(s,mul([4,0],v)),"cross-packet isometry");crosses++;
  }
 }
 let q=ph[1],T=terms(q),test={};
 for(const [label,a] of [["a",[[1,0],[0,1],[1,0]]],["b",[[1,0],[0,-1],[1,0]]]]){
  let e=pair(T[0],a,a)[0]+pair(T[1],a,a)[0];
  let den=4*dot(a,a)[0];
  test[label]=e===0?"0":e===8&&den===12?"2/3":e+"/"+den;
 }
 insist(test.a==="0"&&test.b==="2/3","phase partner readout");
 return {schema:"EM_PREFIX290_GAUSSIAN_BRC_V1",result:"PASS",source_packets:packets.length,
 source_phase_cases:masses,direct_ordered_brc_bin_checks:bins,
 total_mass_equalities:masses,cross_packet_isometry_equalities:crosses,
 complement_source_decoder_equalities:decodes,
 determinant_all_c4:"det(4G_q)=12, det(G_q)=3/16",
 q_i_E_probabilities:test,arithmetic:"Gaussian integer ordered source pairs /4",
 native_H_n_Detector:"NOT_EXECUTED",project_admission:"UNREVIEWED_NOT_ADMITTED"};
}
if(typeof module!=="undefined"&&require.main===module)process.stdout.write(JSON.stringify(run(),null,2)+"\n");
