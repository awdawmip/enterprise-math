/* EC49DT exact independent verifier; run node VERIFY_EC49DT.js */
const verify = function verify(){
const P=1000003,O={a:[-1,-1],b:[-2,-2],c:[1,2,-1,-2],d:[2,1,-2,-1],e:[3,1,1,-3],f:[1,-1]},S=[],L=[[0,0],[0,1],[1,0],[1,1]];
for(let a=0;a<2;a++)for(let b=0;b<2;b++)for(let l=0;l<3;l++)S.push([a,b,l]);
function step(s,k){let[a,b,l]=s;return [+(!!(a||l===1&&k===2)),+(!!(b||l===2&&k===1)),k===1||k===2?k:0]}
function F(s){let[a,b,l]=s;return [+(a===0&&b===0),+(a===0&&b===1),+(a===1&&b===0),+(a===1&&b===1),+(!a&&l===1),+(!b&&l===2),+(!a&&!b&&l===2)]}
function pw(a,n){let r=1;for(;n>0;n=Math.floor(n/2),a=a*a%P)if(n%2)r=r*a%P;return r}
function rank(rows){let B=[];for(let r of rows){let v=r.map(x=>(Number(x)%P+P)%P);for(let [j,b] of B){let q=v[j];if(q)for(let k=j;k<v.length;k++)v[k]=(v[k]-q*b[k]%P+P)%P}let j=v.findIndex(x=>x!==0);if(j>=0){let inv=pw(v[j],P-2);for(let k=j;k<v.length;k++)v[k]=v[k]*inv%P;B.push([j,v]);B.sort((u,v)=>u[0]-v[0])}}return B.length}
function det(rows){let A=rows.map(r=>r.map(BigInt)),n=A.length,sign=1n,prev=1n;for(let k=0;k<n-1;k++){if(!A[k][k]){let j=k+1;while(j<n&&!A[j][k])j++;if(j===n)return 0n;[A[k],A[j]]=[A[j],A[k]];sign=-sign}let p=A[k][k];for(let i=k+1;i<n;i++){for(let j=k+1;j<n;j++){let q=A[i][j]*p-A[i][k]*A[k][j];if(q%prev)throw Error("nonexact Bareiss");A[i][j]=q/prev}A[i][k]=0n}prev=p}return sign*A[n-1][n-1]}
function nativePaths(p){let n=p.slice();n[0]+=2;let start={rp:p.slice(),rn:n,st:[0,0,0],path:[]},D=new Map([[JSON.stringify([start.rp,start.rn,start.st]),start]]);
for(let t=0;t<10;t++){let E=new Map();for(let v of D.values())for(let i=0;i<6;i++){for(let sig of [1,-1]){let r=sig===1?v.rp:v.rn;if(!r[i])continue;let nr=r.slice();nr[i]--;let rp=sig===1?nr:v.rp,rn=sig===-1?nr:v.rn,s=step(v.st,sig*(i+1));let key=JSON.stringify([rp,rn,s]);if(!E.has(key))E.set(key,{rp,rn,st:s,path:[...v.path,sig*(i+1)]})}}D=E}
let all=new Map();for(let v of D.values())if(v.rp.every(x=>!x)&&v.rn.every(x=>!x))all.set(v.st.join(","),v.path);
let rows=[],W=[];for(let s of S){let path=all.get(s.join(","));if(!path)continue;let f=F(s);if(rank([...rows,f])>rows.length){rows.push(f);W.push({state:s,path});if(rows.length===7)break}}
if(W.length!==7)throw Error("missing seven feature directions");let d=det(rows);if(d===0n)throw Error("bad witness det");
for(let w of W){let position=Array(6).fill(0),st=[0,0,0],pcount=Array(6).fill(0);for(let k of w.path){let i=Math.abs(k)-1;position[i]+=Math.sign(k);if(k>0)pcount[i]++;st=step(st,k)}if(w.path.length!==10||position.some((x,i)=>x!==(i===0?-2:0))||pcount.some((x,i)=>x!==p[i])||st.join(",")!==w.state.join(","))throw Error("bad path reconstruction")}
return {positive_counts:p,det7:d.toString(),reachable_states:all.size,witnesses:W,internal:all}
}
function future(alph,max,d){let R={};for(let h=1;h<=max;h++){let words=[];function gen(w,a,e){if(w.length===h){if(e===a+1)words.push(w);return}for(let k of alph)gen(w+k,a+(k==="a"),e+(k==="e"))}gen("",0,0);let types=new Map();
for(let w of words){let steps=[...w].flatMap(k=>O[k]),C=w.includes("c"),D=w.includes("d"),first=steps[0];let cols=L.map(()=>[]);for(let st of S){let end=st;for(let k of steps)end=step(end,k);let A=+(!!(st[0]||C||st[2]===1&&first===2)),B=+(!!(st[1]||D||st[2]===2&&first===1));if(end[0]!==A||end[1]!==B)throw Error("grammar transfer mismatch");for(let j=0;j<4;j++)cols[j].push(+(end[0]===L[j][0]&&end[1]===L[j][1]))}
let sig=JSON.stringify(cols);if(!types.has(sig))types.set(sig,cols)}
let V=[...types.values()].flat();for(let col of V){let augmented=S.map((s,i)=>F(s).slice(0,d).concat([col[i]]));if(rank(augmented)!==d)throw Error("factorization failed")}
let value=rank(V),expect=h===1?4:(d===6?(h%2===0?5:6):7);if(value!==expect)throw Error("wrong horizon rank "+h+" "+value);
R[h]={return_words:words.length,rank:value,distinct_transfer_types:types.size}}return R
}
let C=[[1,3,0,0,0,0],[2,2,0,0,0,0],[3,1,0,0,0,0]];for(let j=2;j<6;j++)for(let [a,b] of [[1,2],[2,1]]){let p=Array(6).fill(0);p[0]=a;p[1]=b;p[j]=1;C.push(p)}
let W=C.map(nativePaths),x=[2,3,1,2,3,4],y=[5,7,3,5,7,9];
function product(p,v){let a=1n;for(let i=0;i<6;i++)for(let j=0;j<p[i];j++)a*=BigInt(v[i]);return a}
function G(p){return [product(p,x),product(p,y),1n]}
let d3=det(W.slice(0,3).map(w=>G(w.positive_counts)));if(d3!==420n)throw Error("core det mismatch");
let rows=[];for(let group of W.slice(0,3)){let[a,b,c]=G(group.positive_counts);for(let w of group.witnesses){let z=F(w.state).map(BigInt);rows.push([...z.map(v=>v*a),...z.map(v=>v*b),...z.map(v=>v*c)])}}
let d21=det(rows),expected=d3**7n*W.slice(0,3).reduce((z,w)=>z*BigInt(w.det7),1n);if(!d21||d21!==expected)throw Error("21x21 det mismatch");
let samples=[[0,0,2],[0,0,0],[1,0,2],[1,0,0]],sgn=[1,-1,-1,1],native= [...O.f,...O.e],witness=W[0].internal;
for(let i=0;i<6;i++)if(samples.reduce((a,s,j)=>a+sgn[j]*F(s)[i],0)!==0)throw Error("collision features not equal");
let outcomes=samples.map(s=>{let t=s;for(let k of native)t=step(t,k);return +(t[0]===0&&t[1]===0)}),gap=outcomes.reduce((v,t,i)=>v+sgn[i]*t,0);
if(gap!==-1)throw Error("collision not separated");
let ordinary=future("acde",7,6),extended=future("acdef",5,7);
return {status:"PASS",model:"native signed X6 D=-2E1; separate returning operation words and dual positive BRC plus count",original_operator_ranks:ordinary,extended_operator_ranks:extended,check_counts:{original_return_words:Object.values(ordinary).reduce((a,b)=>a+b.return_words,0),extended_return_words:Object.values(extended).reduce((a,b)=>a+b.return_words,0),native_histories:77,instrument_patterns:11},example:{x,y,core_det:d3.toString(),det_21:d21.toString()},two_positive_populations_collision:samples.map((s,i)=>({history_state:s,sign:sgn[i],history_path:witness.get(s.join(",")),extended_fe_00:outcomes[i]})),extended_fe_output_signed_gap:gap,witness_blocks:W.map(({internal,...w})=>w)};
};
console.log(JSON.stringify(verify(),null,2));
