#include<iostream>
#include<string>
#include<iomanip>
#include<ctime>
using namespace std;

class Game
// holds the game functions and variables
{
    public:
        Game();
        virtual ~Game();

        //Functions
        void mainMenu();
        void encounter();

        //variables
        int health;
        int exp;

        //Accessors
        inline bool getPlaying() const { return this->playing; }

    private:
        //variables
        int choice;
        bool playing;
};

int main()
//main loop for the game. Keeps the game running until the player quits
//or their character dies.
{
    srand(time(NULL));
    
    Game game;

    while(game.getPlaying())
    {
        game.mainMenu();
    }

    return 0;
}

Game::Game()
//gives the games variables a starting value
{
    choice = 0;
    playing = true;
    health = 50;
    exp = 0;
}

Game::~Game()
{

}

//Functions
void Game::encounter()
//holds the scenarios that can happen when the player travels.
{
    cout << "You lost 10 health" <<endl;
    health -= 10;
    if (health<=0)
    {
        cout <<"You have died." <<endl;
        playing = false;
    }
    else {
        cout << "You gain 100 exp" <<endl;
    }

}
void Game::mainMenu()
//This is the menu the player will return to constantly.
//This is where the player makes choices.
{
    cout << "MAIN MENU" <<endl <<endl;
    cout << "0: Quit" <<endl;
    cout << "1: Travel" <<endl;
    cout << "2: Rest" <<endl;

    cout << endl << "Choice: ";
    cin >> choice;

    switch (choice)
    {
        case 0: //Quit
            playing = false;
            break;
        case 1: //Travel
            encounter();
            break;
        case 2: //Rest
            cout << "You feel refreshed";
            health = 50;
            break;
        default:
            break;
    }
}