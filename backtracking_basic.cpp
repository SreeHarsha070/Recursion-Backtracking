#include<iostream>
using namespace std;
void prnt(int n){
    if(n==0){
        return ;
    }
    
    cout<<n<<endl;
    prnt(n-1);
}

int main(){
    int n;
    cin>>n;
    prnt(n);
    return 0;
}
