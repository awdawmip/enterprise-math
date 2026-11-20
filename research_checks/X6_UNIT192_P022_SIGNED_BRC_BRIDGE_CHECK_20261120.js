// X6 Unit192: exact six-signed-axis geodesic/BRC & P022 interval-bridge independent checker.
// Node.js: node X6_UNIT192_P022_SIGNED_BRC_BRIDGE_CHECK_20261120.js
function runUnit192(){
const D=6,R=6,fact=[1n];for(let i=1;i<=20;i++)fact.push(fact[i-1]*BigInt(i));
const radius=z=>z.reduce((a,v)=>a+Math.abs(v),0);
const brc=z=>{const r=radius(z);let den=1n;for(const v of z)den*=fact[Math.abs(v)];return fact[r]/den};
const memo=new Map();
function recurrence(z){if(z.every(v=>v===0))return 1n;const key=z.join(",");if(memo.has(key))return memo.get(key);let result=0n;for(let i=0;i<D;i++)if(z[i]!==0){const w=z.slice();w[i]-=Math.sign(w[i]);result+=recurrence(w)}memo.set(key,result);return result}
function shell(n,i=0,v=[]){if(i===D)return n===0?[v]:[];const ans=[];for(let a=-n;a<=n;a++)ans.push(...shell(n-Math.abs(a),i+1,v.concat(a)));return ans}
function choose(n,k){let t=1n;for(let j=1;j<=k;j++)t=t*BigInt(n-j+1)/BigInt(j);return t}
function stirling(n,k){let a=Array(k+1).fill(0n);a[0]=1n;for(let i=1;i<=n;i++){const b=Array(k+1).fill(0n);for(let j=1;j<=Math.min(i,k);j++)b[j]=BigInt(j)*a[j]+a[j-1];a=b}return a[k]}
function shellClosed(n){if(n===0)return 1n;let t=0n;for(let k=1;k<=Math.min(D,n);k++)t+=choose(D,k)*(2n**BigInt(k))*fact[k]*stirling(n,k);return t}
let endpointComparisons=0,intervalLayerComparisons=0,midpoints=0;const shells=[];
function checkLayers(z){const n=radius(z),sizes=Array(n+1).fill(0),masses=Array(n+1).fill(0n);function mid(i,y){if(i===D){const j=radius(y);sizes[j]++;masses[j]+=brc(y)*brc(z.map((v,k)=>v-y[k]));midpoints++;return}for(let q=0;q<=Math.abs(z[i]);q++)mid(i+1,y.concat(q*Math.sign(z[i])))}mid(0,[]);
let p=[1];for(const v of z){const q=Array(p.length+Math.abs(v)).fill(0);for(let i=0;i<p.length;i++)for(let j=0;j<=Math.abs(v);j++)q[i+j]+=p[i];p=q}
for(let j=0;j<=n;j++){if(p[j]!==sizes[j]||masses[j]!==brc(z))throw Error(`layer discrepancy z=${z},j=${j}`);intervalLayerComparisons++}
return {profile:sizes,mass:masses.map(String)}
}
for(let n=0;n<=R;n++){const xs=shell(n);let total=0n;for(const z of xs){const actual=brc(z);if(actual!==recurrence(z))throw Error("BRC recurrence discrepancy");endpointComparisons++;total+=actual;if(n<=5)checkLayers(z)}
if(total!==shellClosed(n))throw Error("shell closed-form discrepancy");shells.push({radius:n,endpoints:xs.length,shortest_path_mass:total.toString(),all_length_n_primitive_words:(12n**BigInt(n)).toString()})}
const example=checkLayers([2,1,1,0,0,0]);if(example.profile.join(",")!=="1,3,4,3,1"||example.mass[2]!=="12")throw Error("example mismatch");
const family=[];for(let m=1;m<=10;m++){const b=choose(2*m,m),sites=m+1,lower=(4n**BigInt(m));if(b*BigInt(2*m+1)<lower)throw Error("binomial lower bound");family.push({m,layer_m_sites:sites,layer_m_path_mass:b.toString()})}
return {schema:"X6_UNIT192_P022_BRIDGE_EXACT_CERTIFICATE_V1",date:"2026-11-20",model:"six signed primitive axes Z^6 and separate P022 SC_6 graph-isomorphic walk",frozen_science_pin:"59538f585d037d09ef687b28715c4bc1a3f9fe03",frozen_source_pin:"fd2bcff10ca6e147348b6c1236027fc0d2877df3",shell_radius_range:[0,6],endpoint_recurrence_vs_factorial: endpointComparisons,midpoint_interval_layers_checked:intervalLayerComparisons,midpoint_instances_enumerated:midpoints,recurrence_cache_states:memo.size,shells,example_z_2_1_1:{interval_profile:example.profile,layer2_weighted_path_mass:example.mass[2],shortest_paths:"12"},unbounded_family_first_ten:family,violations:0,original_p022_test_rerun:false,original_R063_benchmark_rerun:false,verification:"Executed independently in V8 with exact BigInt recurrence, midpoint enumeration, integer polynomial expansion and Stirling-shell formula; historical Python module not imported."}
}
console.log(JSON.stringify(runUnit192(),null,2));
