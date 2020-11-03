#include <iostream>
#include <cmath>
#include <stdlib.h>


using namespace std;

int entree();
int main_course();
int dessert();
int soda();

int main() {
	system("color f4");
	string restaurant;
	cout<<"                             ***************WELCOME TO CAFE 6TIS*************\n"<<endl;
	cout<<"KINDLY CHOOSE WHERE YOU WOULD LIKE TO GO TO\n"<<endl;
 	LOOP2: cout<<"1.Home Page\n2.Food Menu\n3.Exit\n"<<endl;
	do {
	cin >> restaurant;
	 if (restaurant == "1") {
		system("cls");
		cout<<"Home page\nEvery dish at Caf� 6tis has its own story from the traditional recipes direct from Lebanon"<<endl;
		cout<<"to modern updates that tell the history of our team, of our cooks and chefs who have left their mark on our kitchen,"<<endl;
		cout<<"and our serving staff and managers who have been ambassadors of hospitality."<<endl;
		cout<<"Our menu is never done - we find inspiration all around, in new ingredients, new approaches, and fresh takes on old standards."<<endl;
		cout<<"                                ************WELCOME TO CAFE 6TIS*************"<<endl;
		goto LOOP2;
	}
	else if (restaurant == "2"){
	system("cls");
	string  food;
	int Breakfast = 0, Lunch = 0, Dinner = 0, Drinks = 0, Total = 0;
	cout<<"Welcome to our Menu.\nHere you can order exquisite gourmet to savour your palates..."<<endl;

	do{
		cout<<"Menu List\n1. Breakfast:"<<endl;
		cout<<"2. Lunch:"<<endl;
		cout<<"3. Dinner:"<<endl;
		cout<<"4. Drinks:"<<endl;
		cout<<"Select a menu to begin"<<endl;
		cout<<"Or you could always leave with your bill...\n"<<endl;
	cin >> food;
	if(food == "1")
	{
		system("cls");
		Breakfast = entree();
	}
	else if(food == "2")
	{
		system("cls");
		Lunch = main_course();
	}
	else if(food == "3")
	{
		system("cls");
		Dinner = dessert();
	}
	else if(food == "4")
	{
		system("cls");
		Drinks = soda();
	}
	else if(food == "0")
		{
			system("cls");
		break;
		}
	else if (!(food == "1")||(food == "2")||(food == "3")||(food == "4")||(food == "0"))
		{
			system("cls");
			cout<<"Please pick among the selected Menus...\n"<<endl;
		}
	}
	while(food == "1" || "2" || "3" || "4" || "0");
	Total = Breakfast + Lunch + Dinner + Drinks;
	if (Total > 0) {
	string money;
	long double cash = 0, atm = 0, atm_cash;
		cout<<"Thanks for your patronage. I hope you enjoy your meal.\nYour Bill:$"<<Total<<"\nSo, how do you wish to pay? \n1.Cash  \n2.ATM?"<<endl;
		do
		{
		cin >> money;
		if(money == "1"){
			system("cls");
			cout<<"Enter amount of cash you wanna pay"<<endl;
			cin >> cash;
			if((cash > Total)||(cash == Total)){
				cout<<"Transaction successful! Your change is $"<<cash-Total<<endl;
				break;
			}else if(cin.fail()){
					cout<<"Invalid Character(s)! Redirecting to payment options...\n";
					cin.clear();
					cin.ignore(256,'\n');
				}
			else if(cash < Total) {
				cout<<"Insufficient funds...Rechoose mode of payment"<<endl;
			}
			}else if(money == "2"){
				system("cls");
			cout<<"Enter your PIN"<<endl;
			cin >> atm;
			if((atm < 9999)&&(atm > 999)){
				cout<<"Enter amount"<<endl;
			cin >> atm_cash;
				if ((atm_cash > Total)||(atm_cash == Total)) {
					cout<<"Transaction successful! Your change is $"<<atm_cash-Total<<endl;
					break;
				}else if(cin.fail()){
					cout<<"Invalid Character(s)! Redirecting to payment options...\n";
					cin.clear();
					cin.ignore(256,'\n');
				}else {
					cout<<"Insufficient funds...Rechoose mode of payment"<<endl;
				}
			}else if(cin.fail()){
					cout<<"Invalid Character(s)! Redirecting to payment options...\n";
					cin.clear();
					cin.ignore(256,'\n');
				}else {
				cout<<"Wrong PIN...Rechoose mode of payment"<<endl;
			}
			}else if (!(money == "1")||(money == "2"))
		{
			cout<<"Wrong mode of payment"<<endl;
		}
		}while((money == "1"|| "2") || cash<Total);
			cout<<"See ya Later!!!"<<endl;

	}else {
		cout<<"Thank you for showing interest in our menu!\nWe'll be expecting your patronage\n"<<endl;
		goto LOOP2;
	}

}
	else if (restaurant == "3") {
		system("cls");
		cout<<"About us"<<endl;
		cout<<"                       From here or elsewhere, the dishes we have imagined and cooked\n                            for this surprise menu tell a story and invite a\n                                                   trip.\n                      An unexpected journey guided by the requirement of authenticity of\n                     products and by the freedom of the imagination, while respecting the"<<endl;
        cout<<"                                           preferences of each\n              The 6tis and their team thank you for your trust and wish you a very pleasant time."<<endl;
        cout<<"Thank you and have a blessed day!\n\n";break;
	}
	else if (!((restaurant=="1") || (restaurant=="2") || (restaurant=="3"))) {
		cout<<"Wrong item on the list"<<endl;
	}
	//using  namespace std helps to declare strings.... the std:: is not needed eventually
	}while (restaurant == "1" || "2" || "3");

}
	int entree() {
		int Breakfast_Total = 0;
	string Breakfast;
	cout<<"Entering the Breakfast menu...select what you would like to eat\n"<<endl;
	cout<<"1.French Toast $14\nTwo thick slices of Brioche bread soaked in Cr�me Anglaise served with fresh fruit and honey syrup\n\n";
	cout<<"2.Eggs Benedict $16\nTwo poached eggs served over Canadian bacon on English muffins, topped with hollandaise sauce\n\n";
	cout<<"3.Bastille Benedict $16\nTwo poached eggs served over jambon de Paris on English muffins, topped with hollandaise sauce\n\n";
	cout<<"4.Florentine Benedict $14\nTwo poached eggs served over saut�ed spinach on English muffins, topped with hollandaise sauce\n\n";
	cout<<"5.Omelette Parisienne $15\nTwo egg omelette with ham, cheese and tomatoes\n\n";
	do
	{
		cin >> Breakfast;
		if(Breakfast == "1")
		{
			Breakfast_Total+=14;
			cout<<"Order recieved...\nSelect another item on the menu or enter 0 to leave..."<<endl;
		}
		else if(Breakfast == "2")
		{

			Breakfast_Total+=16;
			cout<<"Order recieved...\nSelect another item on the menu or enter 0 to leave..."<<endl;
        }
		else if(Breakfast == "3")
		{
			Breakfast_Total+=16;
			cout<<"Order recieved...\nSelect another item on the menu or enter 0 to leave..."<<endl;
		}
		else if(Breakfast == "4")
		{
			Breakfast_Total+=14;
			cout<<"Order recieved...\nSelect another item on the menu or enter 0 to leave..."<<endl;
		}
		else if(Breakfast == "5")
		{
			Breakfast_Total+=15;
			cout<<"Order recieved...\nSelect another item on the menu or enter 0 to leave..."<<endl;
		}
		else if(Breakfast == "0")
		{
			break;
		}
		else if (!((Breakfast=="1") || (Breakfast=="2") || (Breakfast=="3") || (Breakfast=="4") ||(Breakfast=="5") || (Breakfast=="0")))
		{
			cout<<"Invalid. Select an item on the menu\n"<<endl;
		}
	}
	while(Breakfast == "0"||"1"||"2"||"3"||"4"||"5");
		system("cls");
		cout<<"Leaving the Breakfast menu...pick another menu or 0 if you please"<<endl;
		//cout << Breakfast_Total;
		return Breakfast_Total;

	}

	int main_course() {
		int Lunch_Total;
	string Lunch;
	cout<<"Entering the Lunch menu...select what you would like to eat"<<endl;
		cout<<"1.Grilled Poulet $16\nChicken breast, tomato, bacon, pesto aioli\n\n"<<endl;
		cout<<"2.Chicken Salade $18\nMesclun salad, emmental, corn, avocado and cherry tomatoes\n\n"<<endl;
		cout<<"3.Duo of Salmon $24\nSmoked & fresh, fine herbs pink peppercorn\n\n"<<endl;
		cout<<"4.Steak au Poivre $32\nPommes frites, green peppercorn sauce\n\n"<<endl;
		cout<<"5.Complete $15\nHam, cheese, egg, chicken\n\n"<<endl;
	do
	{
		cin >> Lunch;
		if(Lunch == "1")
		{
			Lunch_Total+=16;
			cout<<"Order recieved...\nSelect another item on the menu or enter 0 to leave..."<<endl;
		}
		else if(Lunch == "2")
		{

			Lunch_Total+=18;
			cout<<"Order recieved...\nSelect another item on the menu or enter 0 to leave..."<<endl;
        }
		else if(Lunch == "3")
		{
			Lunch_Total+=24;
			cout<<"Order recieved...\nSelect another item on the menu or enter 0 to leave..."<<endl;
		}else if(Lunch == "4")
		{

			Lunch_Total+=32;
			cout<<"Order recieved...\nSelect another item on the menu or enter 0 to leave..."<<endl;
        }
        else if(Lunch == "5")
		{

			Lunch_Total+=15;
			cout<<"Order recieved...\nSelect another item on the menu or enter 0 to leave..."<<endl;
        }
		else if(Lunch == "0")
		{
			break;
		}
		else if (!((Lunch =="1") || (Lunch =="2") || (Lunch =="3") || (Lunch =="4") || (Lunch =="5") || (Lunch =="0")))
		{
			cout<<"Invalid. Select an item on the menu\n"<<endl;
		}
	}
	while(Lunch == "0"||"1"||"2"||"3"||"4"||"5");
		system("cls");
		cout<<"Leaving the Lunch menu...pick another menu or 0 if you please"<<endl;

	return Lunch_Total;

	}

	int dessert() {
		int Dinner_Total;
	string Dinner;
	cout<<"Entering the Dinner menu...select what you would like to eat"<<endl;
	cout<<"1.Escargots Bourguignon $15\nGarlic, parsley butter\n\n"<<endl;
	cout<<"2. Steak Tartare $18\nTruffle cr�me fraiche, quail egg, arugula\n\n"<<endl;
	cout<<"3.Kobe Beef Carpaccio $11\nBasil pesto, truffle oil, parmesan\n\n"<<endl;
	cout<<"4.French Onion Soupe Gratinee $12\nGruyere cheese, madeira, croutons\n\n"<<endl;
	cout<<"5.Beet Salade $15\nRuby beets, belgian endives, goat cheese, arugula, orange\n\n"<<endl;
	do
	{
		cin >> Dinner;
		if(Dinner == "1")
		{
			Dinner_Total+=15;
			cout<<"Order recieved...\nSelect another item on the menu or enter 0 to leave..."<<endl;
		}
		else if(Dinner == "2")
		{

			Dinner_Total+=18;
			cout<<"Order recieved...\nSelect another item on the menu or enter 0 to leave..."<<endl;
        }
		else if(Dinner == "3")
		{
			Dinner_Total+=11;
			cout<<"Order recieved...\nSelect another item on the menu or enter 0 to leave..."<<endl;
		}
		else if(Dinner == "4")
		{

			Dinner_Total+=12;
			cout<<"Order recieved...\nSelect another item on the menu or enter 0 to leave..."<<endl;
        }
        else if(Dinner == "5")
		{

			Dinner_Total+=15;
			cout<<"Order recieved...\nSelect another item on the menu or enter 0 to leave..."<<endl;
        }
		else if(Dinner == "0")
		{
			break;
		}
		else if (!((Dinner =="1") || (Dinner =="2") || (Dinner =="3") ||(Dinner =="4") || (Dinner =="5") || (Dinner =="0")))
		{
			cout<<"Invalid. Select an item on the menu\n"<<endl;
		}
	}
	while(Dinner == "0"||"1"||"2"||"3"||"4"||"5");
		system("cls");
		cout<<"Leaving the Dinner menu...pick another menu or 0 if you please"<<endl;

	return Dinner_Total;

	}

	int soda() {
		int Drinks_Total;
	string Drinks;
	cout<<"Entering the Drinks menu...select what you would like to drink"<<endl;
	cout<<"1.Blended Scotch $11\n"<<endl;
	cout<<"2.Aperitif Beef $8\n"<<endl;
	cout<<"3.House Cocktails $13\n"<<endl;
	cout<<"4.White Wines $24\n"<<endl;
	cout<<"5.Red Wines $20\n"<<endl;
	do
	{
		cin >> Drinks;
		if(Drinks == "1")
		{
			Drinks_Total+=11;
			cout<<"Order recieved...\nSelect another item on the menu or enter 0 to leave..."<<endl;
		}
		else if(Drinks == "2")
		{
			Drinks_Total+=8;
			cout<<"Order recieved...\nSelect another item on the menu or enter 0 to leave..."<<endl;
        }
		else if(Drinks == "3")
		{
			Drinks_Total+=13;
			cout<<"Order recieved...\nSelect another item on the menu or enter 0 to leave..."<<endl;
		}
		else if(Drinks == "4")
		{
			Drinks_Total+=24;
			cout<<"Order recieved...\nSelect another item on the menu or enter 0 to leave..."<<endl;
        }
        else if(Drinks == "5")
		{
			Drinks_Total+=20;
			cout<<"Order recieved...\nSelect another item on the menu or enter 0 to leave..."<<endl;
        }
		else if(Drinks == "0")
		{
			break;
		}
		else if (!((Drinks =="1") || (Drinks =="2") || (Drinks =="3") ||(Drinks =="4") || (Drinks =="5") ||(Drinks =="0")))
		{
			cout<<"Invalid. Select an item on the menu\n"<<endl;
		}
	}
	while(Drinks == "0"||"1"||"2"||"3"||"");
		system("cls");
		cout<<"Leaving the Drinks menu...pick another menu or 0 if you please"<<endl;

	return Drinks_Total;

	}