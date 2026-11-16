#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>
using namespace std;using Q=uint32_t;
struct R{Q q;int r,c;};
vector<R>rows,besttable,used;
int best=31251;
Q mm[4];int dp[13][2][7][13][9];
int lower(int k,Q s){return dp[k][popcount(s&mm[0])][popcount(s&mm[1])][popcount(s&mm[2])][popcount(s&mm[3])];}
long long nodes;
void search(Q free,int k,int cost,const vector<int>&pool){
 ++nodes;if(cost+lower(k,free)>=best)return;if(!free){if(k==0 && cost<best){best=cost;besttable=used;}return;}if(!k)return;
 vector<int> v;int ct[27]{};Q uni=0;
 for(int i:pool){auto&r=rows[i];if(r.q&~free||r.r>k||cost+r.c+lower(k-r.r,free^r.q)>=best)continue;uni|=r.q;v.push_back(i);for(Q b=r.q;b;b&=b-1)ct[countr_zero(b)]++;}
 if(uni!=free)return;int j=-1,n=1000000;for(Q b=free;b;b&=b-1)if(ct[countr_zero(b)]<n){j=countr_zero(b);n=ct[j];}
 for(int i:v){auto&r=rows[i];if(!(r.q&(1u<<j)))continue;used.push_back(r);search(free^r.q,k-r.r,cost+r.c,v);used.pop_back();}
}
int main(int argc,char**argv){ifstream f(argv[1]);ifstream ff(argv[2]);for(auto &v:mm)ff>>v;for(auto &w:dp)for(auto &x:w)for(auto &y:x)for(auto &z:y)for(auto &k:z)ff>>k;R r;while(f>>r.q>>r.r>>r.c)rows.push_back(r);sort(rows.begin(),rows.end(),[](auto&a,auto&b){return 1.L*a.c/max(1,popcount(a.q))<1.L*b.c/max(1,popcount(b.q));});vector<int>a;for(int i=0;i<rows.size();i++)a.push_back(i);
 best=stoi(argv[3])+1;search((1u<<27)-1,12,0,a);cout<<best<<" "<<nodes<<endl;for(auto&r:besttable)cout<<r.q<<" "<<r.r<<" "<<r.c<<endl;
}
