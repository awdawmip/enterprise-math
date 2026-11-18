// R762FF — exact 251 shifted-return congruence test at q=9, h=7,8.
// Build: g++ -O3 -std=c++17 R762FF_Q9_H7_H8_251_RAW_CERT_TEST.cpp -lgmpxx -lgmp -o r762ff
// Run: ./r762ff 7 ; ./r762ff 8
// Full named six-branch positive BRC recurrence, exact GMP integer residues.
#include <gmpxx.h>
#include <vector>
#include <iostream>
#include <chrono>
#include <algorithm>
#include <map>
using namespace std;
constexpr int Q=9,D=729;
int ix(int x,int y,int z){return (x*Q+y)*Q+z;}
int f(int n){return n<9?0:n/3-2;}
int v3(mpz_class x,int upper){
 if(x==0)return upper;
 int k=0;
 while(k<upper&&mpz_divisible_ui_p(x.get_mpz_t(),3)){
  mpz_divexact_ui(x.get_mpz_t(),x.get_mpz_t(),3);k++;
 }
 return k;
}
int main(int argc,char**argv){
 const int h=argc>1?atoi(argv[1]):7;
 if(h!=7&&h!=8){cerr<<"expected h=7 or 8\n";return 2;}
 const int L=h==7?13122:39366,N=h==7?26:27,b=L/3;
 const int window=251,MAX_S=N+window-1,maxPrec=f(N+125)+b+h+57;
 mpz_class mod,scale;
 mpz_ui_pow_ui(mod.get_mpz_t(),3,maxPrec);
 mpz_ui_pow_ui(scale.get_mpz_t(),3,b);
 const int step[6][3]={{0,0,0},{1,0,0},{0,0,1},{1,1,0},{0,1,1},{1,1,1}};
 vector<vector<int>> src(6,vector<int>(D));
 for(int t=0;t<6;t++)for(int x=0;x<Q;x++)for(int y=0;y<Q;y++)for(int z=0;z<Q;z++)
  src[t][ix(x,y,z)]=ix((x-step[t][0]+Q)%Q,(y-step[t][1]+Q)%Q,(z-step[t][2]+Q)%Q);
 vector<mpz_class> v(D),w(D),early(window),late(window);
 v[0]=1;
 auto started=chrono::steady_clock::now();
 for(int n=0;n<=L+MAX_S;n++){
  if(n>=N&&n<=MAX_S)early[n-N]=v[0];
  if(n>=L+N&&n<=L+MAX_S)late[n-L-N]=v[0];
  if(n==L+MAX_S)break;
  for(int i=0;i<D;i++){
   w[i]=v[src[0][i]];
   for(int j=1;j<6;j++)w[i]+=v[src[j][i]];
  }
  swap(v,w);
  if(n%12==11)for(int i=0;i<D;i++)
   mpz_mod(v[i].get_mpz_t(),v[i].get_mpz_t(),mod.get_mpz_t());
  if(n%2000==1999)cerr<<"n="<<n+1<<" elapsed="
   <<chrono::duration<double>(chrono::steady_clock::now()-started).count()<<"s\n";
 }
 int baselinePass=0,strictPass=0,strictFail=0,bestMargin=1000000,worstMargin=1000000,
     firstFail=-1,firstBaselineFail=-1;
 map<int,int>baselineMargins;
 for(int i=0;i<window;i++){
  int s=N+i,baseExponent=f(s)+b+h,target=f(min(s,N+125))+b+h+57;
  mpz_class d=late[i]-scale*early[i];
  mpz_mod(d.get_mpz_t(),d.get_mpz_t(),mod.get_mpz_t());
  int val=v3(d,maxPrec);
  if(val>=baseExponent)baselinePass++;else if(firstBaselineFail<0)firstBaselineFail=s;
  if(val>=target)strictPass++;else{strictFail++;if(firstFail<0)firstFail=s;}
  int margin=val-target;
  worstMargin=min(worstMargin,margin);
  bestMargin=min(bestMargin,val-baseExponent);
  baselineMargins[val-baseExponent]++;
  if(i<5||(val<target&&firstFail==s))
   cout<<"s="<<s<<" v3(d)="<<val<<" baseline="<<baseExponent
       <<" strict="<<target<<" margin="<<margin<<"\n";
 }
 cout<<"SUMMARY {\"h\":"<<h<<",\"L\":"<<L<<",\"N\":"<<N<<",\"b\":"<<b
     <<",\"max_modulus_trits\":"<<maxPrec<<",\"samples\":"<<window
     <<",\"baseline_pass\":"<<baselinePass<<",\"strict_pass\":"<<strictPass
     <<",\"strict_fail\":"<<strictFail<<",\"first_strict_fail_s\":"<<firstFail
     <<",\"first_baseline_fail_s\":"<<firstBaselineFail
     <<",\"min_strict_margin\":"<<worstMargin
     <<",\"min_baseline_margin\":"<<bestMargin
     <<",\"baseline_margin_histogram\":{";
 bool first=true;
 for(auto [m,cnt]:baselineMargins){
  if(!first)cout<<",";
  first=false;
  cout<<"\""<<m<<"\":"<<cnt;
 }
 cout<<"}}\n";
}
