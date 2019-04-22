/*This source code copyrighted by Lazy Foo' Productions (2004-2019)
 * and may not be redistributed without written permission.*/

//Using SDL, SDL_image, standard math, and strings
//Modified by Alex Seagle for CS302 Final Project-Reversi
#include <SDL2/SDL.h>
#include <SDL2/SDL_image.h>
#include <cstdio>
#include <string>
#include <iostream>
#include <fstream>
using namespace std;
//Screen dimension constants
const int SCREEN_WIDTH = 1024;
const int SCREEN_HEIGHT = 800;
//Button Constants
const int BUTTON_WIDTH = 800;
const int BUTTON_HEIGHT = 800;
const int TOTAL_BUTTONS = 1;
//8 by 8 game board.
char Board[8][8];
ofstream fout;

enum LButtonSprite
{
	BUTTON_SPRITE_MOUSE_DOWN = 0
};

//Texture wrapper class
class LTexture
{
	public:
		//Initializes variables
		LTexture();

		//Deallocates memory
		~LTexture();

		//Loads image at specified path
		bool loadFromFile( std::string path );

		//Deallocates texture
		void free();

		//Renders texture at given point
		void render( int x, int y, SDL_Rect* clip = NULL );

		//Gets image dimensions
		int getWidth();
		int getHeight();

	private:
		//The actual hardware texture
		SDL_Texture* mTexture;

		//Image dimensions
		int mWidth;
		int mHeight;
};

//Mouse button;
class LButton{
	public:
		//Initializes internal variables.		
		LButton();
		//Sets top left position.
		void setPosition(int x, int y);
		//Handle mouse event.
		void handleEvent(SDL_Event* e);
	private:
		//Top left position.
		SDL_Point mPosition;
};

//Starts up SDL and creates window
bool init();

//Loads media
bool loadMedia();

//Frees media and shuts down SDL
void close();

//The window we'll be rendering to
SDL_Window* gWindow = NULL;

//The window renderer
SDL_Renderer* gRenderer = NULL;

//Scene sprites
SDL_Rect gSpriteClips[ 4 ];
LTexture gSpriteSheetTexture;

//Button objects.
LButton gButtons[ TOTAL_BUTTONS ];

LTexture::LTexture()
{
	//Initialize
	mTexture = NULL;
	mWidth = 0;
	mHeight = 0;
}

LTexture::~LTexture()
{
	//Deallocate
	free();
}

bool LTexture::loadFromFile( std::string path )
{
	//Get rid of preexisting texture
	free();

	//The final texture
	SDL_Texture* newTexture = NULL;

	//Load image at specified path
	SDL_Surface* loadedSurface = IMG_Load( path.c_str() );
	if( loadedSurface == NULL )
	{
		printf( "Unable to load image %s! SDL_image Error: %s\n", path.c_str(), IMG_GetError() );
	}
	else
	{
		//Color key image
		SDL_SetColorKey( loadedSurface, SDL_TRUE, SDL_MapRGB( loadedSurface->format, 0, 0xFF, 0xFF ) );

		//Create texture from surface pixels
		newTexture = SDL_CreateTextureFromSurface( gRenderer, loadedSurface );
		if( newTexture == NULL )
		{
			printf( "Unable to create texture from %s! SDL Error: %s\n", path.c_str(), SDL_GetError() );
		}
		else
		{
			//Get image dimensions
			mWidth = loadedSurface->w;
			mHeight = loadedSurface->h;
		}

		//Get rid of old loaded surface
		SDL_FreeSurface( loadedSurface );
	}

	//Return success
	mTexture = newTexture;
	return mTexture != NULL;
}

void LTexture::free()
{
	//Free texture if it exists
	if( mTexture != NULL )
	{
		SDL_DestroyTexture( mTexture );
		mTexture = NULL;
		mWidth = 0;
		mHeight = 0;
	}
}

void LTexture::render( int x, int y, SDL_Rect* clip )
{
	//Set rendering space and render to screen
	SDL_Rect renderQuad = { x, y, mWidth, mHeight };

	//Set clip rendering dimensions
	if( clip != NULL )
	{
		renderQuad.w = clip->w;
		renderQuad.h = clip->h;
	}

	//Render to screen
	SDL_RenderCopy( gRenderer, mTexture, clip, &renderQuad );
}

int LTexture::getWidth()
{
	return mWidth;
}

int LTexture::getHeight()
{
	return mHeight;
}

LButton::LButton(){
	mPosition.x = 0;
	mPosition.y = 0;

}

void LButton::setPosition(int x, int y){
	mPosition.x = x;
	mPosition.y = y;
}

void LButton::handleEvent( SDL_Event* e )
{
	//If mouse event happened.
	if(e->type == SDL_MOUSEBUTTONDOWN){
		cout << "Mouse Down" << endl;
		int x, y;
		SDL_GetMouseState( &x, &y );
		//Check if mouse is in button.
		//		bool inside = true;
		//Mouse left
		if( x < mPosition.x )
		{
			cout << "x < mPos.x" << endl;
			//			inside = false;
		}
		//Mouse right
		else if( x > mPosition.x + BUTTON_WIDTH )
		{
			cout << "x > M" << endl;
			//			inside = false;
		}
		//Mouse above
		else if( y < mPosition.y )
		{
			cout << "y < M" << endl;
			//			inside = false;
		}
		//Mouse below
		else if( y > mPosition.y + BUTTON_HEIGHT )
		{
			cout << "y > M" << endl;
			//			inside = false;
		}
		else{
			cout << "Button Pushed" << endl;

			int newi,newj;
			if(x >= 0 && x <= 100){
				newi = 0;
			}
			else if( x > 100 && x <= 200){
				newi = 1;
			}
			else if( x > 200 && x <= 300){
				newi = 2;
			}
			else if( x > 300 && x <= 400){
				newi = 3;
			}
			else if( x > 400 && x <= 500){
				newi = 4;
			}
			else if(x > 500 && x <= 600){
				newi = 5;
			}
			else if(x > 600 && x <= 700){
				newi = 6;
			}
			else{
				newi = 7;
			}


			if(y >= 0 && y <= 100){
				newj = 0;
			}
			else if( y > 100 && y <= 200){
				newj = 1;
			}
			else if( y > 200 && y <= 300){
				newj = 2;
			}
			else if( y > 300 && y <= 400){
				newj = 3;
			}
			else if( y > 400 && y <= 500){
				newj = 4;
			}
			else if(y > 500 && y <= 600){
				newj = 5;
			}
			else if(y > 600 && y <= 700){
				newj = 6;
			}
			else{
				newj = 7;
			}
			//			Board[newi][newj] = 'B';

			fout.open("/home/aseagle/COSC-302/Final/Final-Project/move.txt", ios::out);
			fout << newi << " " << newj << " ";
			fout.close();

		}
	}
}










bool init()
{
	//Initialization flag
	bool success = true;

	//Initialize SDL
	if( SDL_Init( SDL_INIT_VIDEO ) < 0 )
	{
		printf( "SDL could not initialize! SDL Error: %s\n", SDL_GetError() );
		success = false;
	}
	else
	{
		//Set texture filtering to linear
		if( !SDL_SetHint( SDL_HINT_RENDER_SCALE_QUALITY, "1" ) )
		{
			printf( "Warning: Linear texture filtering not enabled!" );
		}

		//Create window
		gWindow = SDL_CreateWindow( "SDL Tutorial", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, SCREEN_WIDTH, SCREEN_HEIGHT, SDL_WINDOW_SHOWN );
		if( gWindow == NULL )
		{
			printf( "Window could not be created! SDL Error: %s\n", SDL_GetError() );
			success = false;
		}
		else
		{
			//Create renderer for window
			gRenderer = SDL_CreateRenderer( gWindow, -1, SDL_RENDERER_ACCELERATED );
			if( gRenderer == NULL )
			{
				printf( "Renderer could not be created! SDL Error: %s\n", SDL_GetError() );
				success = false;
			}
			else
			{
				//Initialize renderer color
				SDL_SetRenderDrawColor( gRenderer, 0xFF, 0xFF, 0xFF, 0xFF );

				//Initialize PNG loading
				int imgFlags = IMG_INIT_PNG;
				if( !( IMG_Init( imgFlags ) & imgFlags ) )
				{
					printf( "SDL_image could not initialize! SDL_mage Error: %s\n", IMG_GetError() );
					success = false;
				}
			}
		}
	}

	return success;
}

bool loadMedia()
{
	//Loading success flag
	bool success = true;

	//Load sprite sheet texture
	if( !gSpriteSheetTexture.loadFromFile( "/home/aseagle/COSC-302/Final/Final-Project/11_clip_rendering_and_sprite_sheets/Pieces2.xcf" ) )
	{
		printf( "Failed to load sprite sheet texture!\n" );
		success = false;
	}
	else
	{
		//Set top left sprite
		//White Piece
		gSpriteClips[ 0 ].x =   0;
		gSpriteClips[ 0 ].y =   0;
		gSpriteClips[ 0 ].w = 100;
		gSpriteClips[ 0 ].h = 100;

		//Set top right sprite
		//Empty
		gSpriteClips[ 1 ].x = 100;
		gSpriteClips[ 1 ].y =   0;
		gSpriteClips[ 1 ].w = 100;
		gSpriteClips[ 1 ].h = 100;

		//Set bottom left sprite
		//Black Piece
		gSpriteClips[ 2 ].x =   0;
		gSpriteClips[ 2 ].y = 100;
		gSpriteClips[ 2 ].w = 100;
		gSpriteClips[ 2 ].h = 100;

		//Set bottom right sprite
		//Ghost
		gSpriteClips[ 3 ].x = 100;
		gSpriteClips[ 3 ].y = 100;
		gSpriteClips[ 3 ].w = 100;
		gSpriteClips[ 3 ].h = 100;
	}

	return success;
}

void close()
{
	//Free loaded images
	gSpriteSheetTexture.free();

	//Destroy window	
	SDL_DestroyRenderer( gRenderer );
	SDL_DestroyWindow( gWindow );
	gWindow = NULL;
	gRenderer = NULL;

	//Quit SDL subsystems
	IMG_Quit();
	SDL_Quit();
}

//void SET_UP_BOARD(){
//char (&Board) [8][8]){
//int i,j;
//char input;
//for(i = 0; i < 8; i++){
//for(j = 0; j < 8; j++){
//cin >> input;
//if(input == 'w'){
//gSpriteSheetTexture.render( j*100, i*100, &gSpriteClips[ 0 ] );
//}
//else if(input == 'B'){
//gSpriteSheetTexture.render( j*100, i*100, &gSpriteClips[ 2 ] );
//}
//else{
//gSpriteSheetTexture.render( j*100, i*100, &gSpriteClips[ 1 ] );
//}
//}
//}
//}

//char Board[8][8];
int main( int argc, char* args[] )
{
	 fout.open("/home/aseagle/COSC-302/Final/Final-Project/move.txt", ios::out);
	             fout << 0 << " " << 0 << " ";
				             fout.close();

	ifstream fin;
	int count_i = 0;
	int count_j = 0;
	fin.open("/home/aseagle/COSC-302/Final/Final-Project/board.txt", ios::in);
	int i,j;
	char input;
	//	char Board[8][8];
	for(i = 0; i < 8; i++){
		for(j = 0; j < 8; j++){
			fin >> input;
			Board[i][j] = input;
		}
	}
	fin.close();
	//			if(input == 'w'){
	//				gSpriteSheetTexture.render( j*100, i*100, &gSpriteClips[ 0 ] );
	///			}
	//			else if(input == 'B'){
	//				gSpriteSheetTexture.render( j*100, i*100, &gSpriteClips[ 2 ] );
	//			}
	//			else{
	//				gSpriteSheetTexture.render( j*100, i*100, &gSpriteClips[ 1 ] );
	//			}
	//		}
	//	}

	//Start up SDL and create window
if( !init() )
{
	printf( "Failed to initialize!\n" );
}
else
{
	//Load media
	if( !loadMedia() )
	{
		printf( "Failed to load media!\n" );
	}
	else
	{	
		//Main loop flag
		bool quit = false;

		//Event handler
		SDL_Event e;

		//While application is running
		while( !quit )
		{
			//Handle events on queue
			while( SDL_PollEvent( &e ) != 0 )
			{
				//User requests quit
				if( e.type == SDL_QUIT )
				{
					quit = true;
					
				}
				gButtons[0].handleEvent( &e );
			}

			//Clear screen
			SDL_SetRenderDrawColor( gRenderer, 0xFF, 0xFF, 0xFF, 0xFF );
			SDL_RenderClear( gRenderer );
	        fin.open("/home/aseagle/COSC-302/Final/Final-Project/board.txt", ios::in);
			if(fin.eof() == 0)
            {
				for(i = 0; i < 8; i++){
					for(j = 0; j < 8; j++){
						fin >> input;
						Board[i][j] = input;
//						cout << Board[i][j] << " ";
					}
				}

			}
			fin.close();

			for(i = 0; i < 8; i++){
				for(j = 0; j < 8; j++){

			if(Board[i][j] == 'W'){
				gSpriteSheetTexture.render( j*100, i*100, &gSpriteClips[ 0 ]);
//				SDL_RenderPresent( gRenderer );
			}
			else if(Board[i][j] == 'B'){
				gSpriteSheetTexture.render( j*100, i*100, &gSpriteClips[ 2 ] );
//				SDL_RenderPresent( gRenderer );
			}
			else if(Board[i][j] == 'o'){
				gSpriteSheetTexture.render( j*100, i*100, &gSpriteClips[ 3 ] );
//				SDL_RenderPresent( gRenderer );
			}
			else{
				gSpriteSheetTexture.render( j*100, i*100, &gSpriteClips[ 1 ] );
//				SDL_RenderPresent(gRenderer);
				}

//				SDL_RenderPresent( gRenderer );
				//						cout << Board[i][j] << " ";
			}
			}
			SDL_RenderPresent(gRenderer);

			//
			//				SET_UP_BOARD();
			//Render top left sprite
			//		gSpriteSheetTexture.render( 0, 0, &gSpriteClips[ 0 ] );

			//Render top right sprite
			//		gSpriteSheetTexture.render( SCREEN_WIDTH - gSpriteClips[ 1 ].w, 0, &gSpriteClips[ 1 ] );
			//		gSpriteSheetTexture.render(SCREEN_WIDTH - 2*gSpriteClips[1].w, 0, &gSpriteClips[1]);

			//Render bottom left sprite
			//		gSpriteSheetTexture.render( 0, SCREEN_HEIGHT - gSpriteClips[ 2 ].h, &gSpriteClips[ 2 ] );

			//Render bottom right sprite
			//		gSpriteSheetTexture.render( SCREEN_WIDTH - gSpriteClips[ 3 ].w, SCREEN_HEIGHT - gSpriteClips[ 3 ].h, &gSpriteClips[ 3 ] );

			//Update screen
			//			SDL_RenderPresent( gRenderer );
		}
	}
}

//Free resources and close SDL
close();

return 0;
}
