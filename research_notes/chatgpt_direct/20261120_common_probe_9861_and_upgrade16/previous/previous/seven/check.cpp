#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>
using namespace std;
// Rows carry their integer reduced cost after charging one dual weight per point and one per label.
using U=uint64_t;using M=__uint128_t;
int at(M x){return U(x)?countr_zero(U(x)):64+countr_zero(U(x>>64));}
int pc(M x){return popcount(U(x))+popcount(U(x>>64));}
struct Row{M m;int size,rc,price;};long long nodes=0;vector<Row> chosen,solution;
bool solve(M f,int k,int slack,const vector<Row>& pool){
 ++nodes;if(!f)return !k;if(k<1)return false;
 vector<Row>active;array<int,125>d{},low;low.fill(100000000);int mins[14];fill(mins,mins+14,100000000);
 for(auto r:pool){if(r.rc>slack||(r.m&~f))continue;
 if(k==1){if(r.m==f){solution=chosen;solution.push_back(r);return true;}continue;}
 active.push_back(r);mins[r.size]=min(mins[r.size],r.rc);int rate=r.rc/r.size;
 for(M t=r.m;t;t&=t-1){int b=at(t);d[b]++;low[b]=min(low[b],rate);}}
 if(k==1)return false;
 int sum=0,pivot=at(f),n=pc(f);
 for(M t=f;t;t&=t-1){int b=at(t);if(!d[b])return false;if(d[b]<d[pivot])pivot=b;sum+=low[b];}
 if(sum>slack)return false;
 int dp[8][94];fill(&dp[0][0],&dp[0][0]+8*94,100000000);dp[0][0]=0;
 for(int h=1;h<k;h++)for(int s=0;s<=13;s++)if(mins[s]<100000000)for(int a=s;a<=n;a++)dp[h][a]=min(dp[h][a],dp[h-1][a-s]+mins[s]);
 for(auto r:active)if((r.m>>pivot)&1){if(r.rc+dp[k-1][n-r.size]>slack)continue;
 int val=sum;for(M t=r.m;t;t&=t-1)val-=low[at(t)];if(val+r.rc>slack)continue;
 chosen.push_back(r);if(solve(f^r.m,k-1,slack-r.rc,active))return true;chosen.pop_back();}
 return false;
}

using Observation = array<U,4>;
Observation menu[125][125];
M blocked[125][125];
int cap_by_size[14],minimum_size,weights[126],slack;
int picked[13];
long long candidates;
vector<Row> attainable;

// Enumerate all admissible classes in the region and independently check the separating prices.
void generate(int size, M pool, M mask, const M *ban, const Observation *old, int spent, int charge){
 if(size>=minimum_size && spent<=cap_by_size[size]){
   candidates++;
   int reduced=1000*spent-charge;
   if(reduced<0)throw runtime_error("invalid integer point weights");
   if(reduced<=slack)attainable.push_back({mask,size,reduced,spent});
 }
 while(pool && size+pc(pool)>=minimum_size){
   int x=at(pool);pool&=pool-1;M next=pool&~ban[x];
   if(size+1+pc(next)<minimum_size)continue;
   M next_ban[125];
   for(M b=next;b;b&=b-1){int j=at(b);next_ban[j]=ban[j]|blocked[j][x];}
   Observation own{},state[14];
   int price=spent;
   for(int k=0;k<size;k++)for(int w=0;w<4;w++){
     U add=menu[picked[k]][x][w];
     state[k][w]=old[k][w]|add;price+=popcount(add&~old[k][w]);own[w]|=add;
   }
   state[size]=own;for(U w:own)price+=popcount(w);
   picked[size]=x;
   generate(size+1,next,mask|(M(1)<<x),next_ban,state,price,charge+weights[x]);
 }
}
int main(int argc,char **argv){
 ifstream native(argv[1],ios::binary);
 native.read((char*)menu,sizeof(menu));array<unsigned char,3> tri;
 while(native.read((char*)tri.data(),3))do{blocked[tri[0]][tri[1]]|=M(1)<<tri[2];}while(next_permutation(tri.begin(),tri.end()));
 ifstream jobs(argv[2]);int id,only=stoi(argv[3]),budget;U low,high;
 while(jobs>>id>>low>>high>>budget>>minimum_size){
    for(int&v:cap_by_size)jobs>>v;for(int&v:weights)jobs>>v;
    if(id!=only)continue;
    M full=(M(high)<<64)|low;
    int objective=7*weights[125];
    for(M a=full;a;a&=a-1)objective+=weights[at(a)];
    slack=1000*budget-objective;
    M none[125]{};Observation initial[14]{};
    generate(0,full,0,none,initial,0,weights[125]);
    if(slack>=0)solve(full,7,slack,attainable);
    cout<<objective<<" "<<candidates<<" "<<attainable.size()<<" "<<nodes<<" "<<solution.size();
    for(auto r:solution)cout<<" "<<U(r.m)<<" "<<U(r.m>>64);cout<<endl;
    return 0;
 }
 return 2;
}
