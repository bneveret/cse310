#include<iostream>
#include<string>
#include<iomanip>
#include<ctime>
using namespace std;

class Game
{
    public:
        Game();
        virtual ~Game();

        //Functions
        void mainMenu();
        void encounter();
        int health;
        int exp;

        //Accessors
        inline bool getPlaying() const { return this->playing; }

    private:
        int choice;
        bool playing;
};

int main()
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
{
    cout << "MAIN MENU" <<endl <<endl;
    cout << "0: Quit" <<endl;
    cout << "1: Travel" <<endl;
    cout << "2: Rest" <<endl;

    cout << endl << "Choice: ";
    cin >> choice;

    switch (choice)
    {
        case 0:
            playing = false;
            break;
        case 1:
            encounter();
            break;
        case 2:
            cout << "You feel refreshed";
            health = 50;
            break;
        default:
            break;
    }
}