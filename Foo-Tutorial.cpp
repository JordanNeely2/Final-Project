//Alex Seagle 3-28-2019 10:35 A.M. to 10:57 A.M.
//Modified LazyFoo Tutorial01. Outputs a purple window for 5 seconds.
//Modified LazyFoo Tutorial03. Outputs purple window until user quits. 1:37 P.M.
////to 1:58 P.M.
//Modified LazyFoo Tutorial04. Outputs Black for down key. Red for Left key.
//Blue for right key. Purple for up key.
//
#include <SDL2/SDL.h>
#include<iostream>
const int SCREEN_W = 640;
const int SCREEN_H = 480;
using namespace std;

enum KeyPressSurfaces{
	KEY_PRESS_SURFACE_DEFAULT,
	KEY_PRESS_SURFACE_UP,
	KEY_PRESS_SURFACE_DOWN,
	KEY_PRESS_SURFACE_LEFT,
	KEY_PRESS_SURFACE_RIGHT,
	KEY_PRESS_SURFACE_TOTAL
};



int main(int argc, char* argv[]){

	SDL_Window* window = NULL;

	SDL_Surface* screenSurface = NULL;

	if(SDL_Init(SDL_INIT_VIDEO) < 0){
		cout << "SDL could not initilize. SDL_Error: " << endl;
		cout << SDL_GetError() << endl;
	}
	else{
		window = SDL_CreateWindow("SDL Tutorial", SDL_WINDOWPOS_UNDEFINED,
				SDL_WINDOWPOS_UNDEFINED, SCREEN_W, SCREEN_H, SDL_WINDOW_SHOWN);
		if(window == NULL){
			cout << "Window could not be created. SDL_Error:" << endl;
				cout << SDL_GetError() << endl;
		}
		else{
			bool quit = false;
			SDL_Event e;
			while(!quit){
				while(SDL_PollEvent(&e) != 0){
					  if(e.type == SDL_QUIT){
					      quit = true;
					  }
				}

			screenSurface = SDL_GetWindowSurface(window);
//Purple window
			SDL_FillRect(screenSurface, NULL, SDL_MapRGB(screenSurface->format,
						0xFF, 0x00, 0xFF));

			SDL_UpdateWindowSurface(window);
		//	SDL_Delay(5000);
			}
		}
	}
	SDL_DestroyWindow(window);
	SDL_Quit();
	return 0;
}

