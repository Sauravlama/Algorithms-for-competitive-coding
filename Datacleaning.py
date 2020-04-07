#include<iostream>
using namespace std;
int main()
{
	int number;
	cin>>number;
	if(number&1)
	{
		cout<<"The number is odd";
	}
	else
	{
		cout<<"The number is even";
	}
	return 0;
}
