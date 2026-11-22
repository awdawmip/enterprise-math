// EC49FXK exact verifier, no dependencies; run: node EC49FXK_SYMBOL_R2_VERIFY.js
const mod=(x,n)=>(x%n+n)%n;
const activationSet=function activationSet(k){
 if(k<=2)return [74,98,99,100,101,102,105,108];
 if(k<=4)return [61,62,70,73,76,78,79,85,89];
 const s=Math.max(0,Math.min(5,Math.floor((56-k)/2))),S=[],lightColors=new Set();
 for(let x=28-s;x<=27;x++){S.push(x,x+55);lightColors.add(x%5);}
 for(let i=0;i<5;i++)if(!lightColors.has(i))for(let a=0;a<3;a++)S.push(i+5*a);
 return S.sort((a,b)=>a-b);
};
const symbolDistance=function symbolDistance(S,d,i,j){let z=0;for(const t of S)if((t%5===i && t%11!==j)||(mod(d-t,5)===i && mod(d-t,11)!==j))z++;return z;};
const lightCandidates=function lightCandidates(k){const c=Array.from({length:5},()=>[]);for(let i=0;i<5;i++){const a=[];for(let t=0;t<110;t++)if(t%5===i&&mod(2*t,55)>=k)a.push(t);for(let x=0;x<a.length;x++)for(let y=x+1;y<a.length;y++)c[i].push([a[x],a[y]])}return c};
const pairCompatible=function pairCompatible(k,p,q){const i=p[0]%5,h=q[0]%5;for(let d=0;d<k;d++)if(d%5===(i+h)%5)for(let j=0;j<11;j++)if(symbolDistance(p.concat(q),d,i,j)<2)return false;return true};
const maxLight=function maxLight(k){const all=lightCandidates(k);let best=0,checks=0;function dfs(i,ch){if(ch.length+5-i<=best)return;if(i===5){best=Math.max(best,ch.length);return;}dfs(i+1,ch);for(const a of all[i]){let ok=true;for(const b of ch){checks++;if(!pairCompatible(k,a,b)){ok=false;break;}}if(ok)dfs(i+1,ch.concat([a]));}}dfs(0,[]);return {k,candidates_by_color:all.map(a=>a.length),max_compatible_light_colors:best,pair_compatibility_calls:checks}};
const runVerification=function runVerification(){
 const rows=[];let checks=0;for(let k=1;k<=55;k++){
  let min=1000,S=activationSet(k);const expected=k<=2?8:k<=4?9:15-Math.max(0,Math.min(5,Math.floor((56-k)/2)));
  if(S.length!==expected||new Set(S).size!==S.length)throw Error("wrong witness size k="+k);
  for(let d=0;d<k;d++)for(let i=0;i<5;i++)for(let j=0;j<11;j++){
   const val=symbolDistance(S,d,i,j);checks++;min=Math.min(min,val);if(val<2)throw Error(`FAIL k=${k} d=${d} i=${i} j=${j} val=${val}`);
  }
  rows.push({k,activations:S.length,minimum_symbol_distance:min,sites:S});
 }
 const thresholds=[47,49,51,53,55].map(maxLight);
 for(const z of thresholds){const expected=Math.max(0,Math.min(5,Math.floor((56-z.k)/2)));if(z.max_compatible_light_colors!==expected)throw Error("lower_bound_error k="+z.k);}
 return {schema:"EC49FXK_INTERVAL_SYMBOL_R2_VERIFIER_V1",scientific_pin:"BRC16943",metric:"whole physical activation two-bit-symbol distance",required_symbol_distance:2,range:"all k=1..55, all d∈Dk, five CRT colors, eleven missing columns",upper_row_evaluations:checks,necessary_light_color_exhaustive_thresholds:thresholds,optimal_cost_profile:rows,status:"PASS",independent_review:"NOT_REVIEWED"};
};
process.stdout.write(JSON.stringify(runVerification(),null,2)+"\n");
