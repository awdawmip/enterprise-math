'use strict';
const cache=new Map();
function bin(n,k){if(n<0||k<0||k>n)return 0n;k=Math.min(k,n-k);if(k===0)return 1n;const key=n+':'+k;if(cache.has(key))return cache.get(key);let z=1n;for(let i=1;i<=k;i++)z=z*BigInt(n+1-i)/BigInt(i);cache.set(key,z);return z}
const cat=k=>bin(2*k,k)/BigInt(k+1);
function raw(k,t){const r=2*k+1;if(t<2||t>r)return 0n;let s=0n;for(let q=0;q<=r-t;q++)s+=bin(r-t,q)*(bin(2*t,r-2*q)-bin(2*t,r-2*q-1));return bin(r+t,2*t)*s}
function ballot(k,t){const r=2*k+1;if(t<2||t>r)return 0n;let s=0n;for(let q=0;q<=Math.min(Math.floor((t-1)/2),k);q++)s+=bin(t-1,2*q)*4n**BigInt(q)*cat(k-q);return bin(r+t,2*t)*s}
for(let k=1;k<=331;k++)for(let t=2;t<=57;t++)if(raw(k,t)!==ballot(k,t))throw Error('coefficient mismatch k='+k+' t='+t);
console.log(JSON.stringify({status:'R532_FULL_COEFFICIENT_GRID_PASS',date:'2026-11-04',scientific_pin:'18783e01e3646c72b7aab3b16d3f565e83e6446f',k_grid:[1,331],t_grid:[2,57],exact_comparisons:18536,arithmetic:'JS BigInt integers',scope:'All original signed BRC matrix coefficients used for m=55 at every polynomial identity interpolation point; no general-all-k ballot identity claimed'},null,2));
