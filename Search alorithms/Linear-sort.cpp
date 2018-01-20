#include <bits/stdc++.h>
using namespace std;

int main()
{
	int arr[10];
	int j;
	int key;
	cout << "Enter the values in the array !";
	for (int i=0;i<10;i++)
	{
		cin >> arr[i];
	}
	cin >> key;
	for (int i=0;i<n;i++)
	{
		if (key==arr[i])
		{
           j=i;
           cout << "Your key" << key <<" is found in place "<<j;
		}
		else
		{
			cout << "Your Key is not Found!";
			break
		}
	}
	
	

}