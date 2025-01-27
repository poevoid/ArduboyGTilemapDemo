#include "Arduino.h"
#include "Arduboy2Core.h"
#include "vars.h"
// Fills the map with random tiles.
void generateMap() {
  for (uint8_t tileY = 0; tileY < mapHeight; ++tileY)
    for (uint8_t tileX = 0; tileX < mapWidth; ++tileX)
      tileMap[tileY][tileX] = static_cast<TileType>(random() % 4);
}

void handleInput() {
  // If the left button is pressed.
  if (arduboy.pressed(LEFT_BUTTON)) {
    // If cameraX is greater than its allowed minimum.
    if (cameraX > cameraXMinimum)
      // Decrease cameraX by 1.
      --cameraX;
  }

  // If the right button is pressed.
  if (arduboy.pressed(RIGHT_BUTTON)) {
    // If cameraX is less than its allowed maximum.
    if (cameraX < cameraXMaximum)
      // Increase cameraX by 1.
      ++cameraX;
  }

  // If the up button is pressed.
  if (arduboy.pressed(UP_BUTTON)) {
    // If cameraY is greater than its allowed minimum.
    if (cameraY > cameraYMinimum)
      // Decrease cameraY by 1.
      --cameraY;
  }

  // If the down button is pressed.
  if (arduboy.pressed(DOWN_BUTTON)) {
    // If cameraY is less than its allowed maximum.
    if (cameraY < cameraYMaximum)
      // Increase cameraY by 1.
      ++cameraY;
  }
}

void drawTileMap() {
  for (uint8_t tileY = 0; tileY < mapHeight; ++tileY) {
    // Calculate the y position to draw the tile at.
    // (Making sure to factor in the camera.)
    int16_t drawY = ((tileY * tileHeight) - cameraY);

    // If the tile would be offscreen.
    if ((drawY < -tileHeight) || (drawY > HEIGHT))
      // Skip this row and continue with the next row.
      continue;

    for (uint8_t tileX = 0; tileX < mapWidth; ++tileX) {
      // Calculate the x position to draw the tile at.
      // (Making sure to factor in the camera.)
      int16_t drawX = ((tileX * tileWidth) - cameraX);

      // If the tile would be offscreen.
      if ((drawX < -tileWidth) || (drawX > WIDTH))
        // Skip this tile and continue with the next one.
        continue;

      // Read the tile from the map.
      TileType tileType = tileMap[tileY][tileX];

      // Figure out the tile index
      uint8_t tileIndex = toTileIndex(tileType);

      // Draw the tile at the calculated position.
      SpritesU::drawPlusMaskFX(drawX, drawY, exteriortileset, FRAME(tileIndex));
    }
  }
}


void update() {
  switch (screen) {

    case Screen::Splash:
    if (startcounter != 0) {
        startcounter--;
      } else {
        screen = Screen::Game;
      }

      break;

    case Screen::Game:

      handleInput();
      break;
  }
}


void render() {
  uint16_t currentPlane = arduboy.currentPlane();
  switch (screen) {
    case Screen::Splash:
      SpritesU::drawPlusMaskFX(0, 0, punklogooutlined, FRAME(0));
      break;

    case Screen::Game:
      if (currentPlane <= 0) {  //dark gray
      }

      if (currentPlane <= 1) {  //gray
        //arduboy.setCursor(0, 0);
        //arduboy.println();
      }

      if (currentPlane <= 2) {  //white
      }

      drawTileMap();
      break;
  }
}
