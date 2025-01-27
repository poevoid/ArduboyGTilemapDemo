#pragma once

#define FRAME(x) x * 3 + arduboy.currentPlane()

// Represents different tile types
enum class TileType : uint8_t {
  Tile0,
  Tile1,
  Tile2,
  Tile3,
  Tile4,
  Tile5,
  Tile6,
  Tile7,
  Tile8,
  Tile9,
  Tile10,
  Tile11,
  Tile12,
  Tile13,
  Tile14,
  Tile15,
  Tile16,
  Tile17,
  Tile18,
  Tile19,
  Tile20,
  Tile21,
  Tile22,
  Tile23,
  Tile24,
  Tile25,
  Tile26,
  Tile27,
  Tile28,
  Tile29,
  Tile30,
  Tile31,
  Tile32,
  Tile33,
  Tile34,
  Tile35,
  Tile36,
  Tile37,
  Tile38,
  Tile39,
  Tile40,
  Tile41,

};

// Gets the sprite index from the tile type.
inline constexpr uint8_t toTileIndex(TileType tileType) {
  // The basic implementation just converts the
  // tile type to its underlying integer representation.
  return static_cast<uint8_t>(tileType);
}
// Tile Dimensions
constexpr uint8_t tileWidth = 16;
constexpr uint8_t tileHeight = 16;

// Map Dimensions (in tiles)
constexpr uint8_t mapWidth = 7;
constexpr uint8_t mapHeight = 6;

// Map Dimensions (in pixels)
constexpr uint16_t fullMapWidth = (mapWidth * tileWidth);
constexpr uint16_t fullMapHeight = (mapHeight * tileHeight);

// Tile Map
TileType tileMap[mapHeight][mapWidth]{
  { TileType::Tile0, TileType::Tile1, TileType::Tile2, TileType::Tile3, TileType::Tile4, TileType::Tile5, TileType::Tile6 },
  { TileType::Tile7, TileType::Tile8, TileType::Tile9, TileType::Tile10, TileType::Tile11, TileType::Tile12, TileType::Tile13 },
  { TileType::Tile14, TileType::Tile15, TileType::Tile16, TileType::Tile17, TileType::Tile18, TileType::Tile19, TileType::Tile20 },
  { TileType::Tile21, TileType::Tile22, TileType::Tile23, TileType::Tile24, TileType::Tile25, TileType::Tile26, TileType::Tile27 },
  { TileType::Tile28, TileType::Tile29, TileType::Tile30, TileType::Tile31, TileType::Tile32, TileType::Tile33, TileType::Tile34 },
  { TileType::Tile35, TileType::Tile36, TileType::Tile37, TileType::Tile38, TileType::Tile39, TileType::Tile40, TileType::Tile41 },

};
int startcounter =75;
enum class Screen : uint8_t {
  Splash,
  Game
};
Screen screen = {Screen::Splash};
// Camera Position
//int16_t cameraX = (fullMapWidth / 2);
//int16_t cameraY = (fullMapHeight / 2);
int16_t cameraX = (0);
int16_t cameraY = (0);

// Camera Boundaries
constexpr int16_t cameraXMinimum = 0;
constexpr int16_t cameraXMaximum = (fullMapWidth - WIDTH);
constexpr int16_t cameraYMinimum = 0;
constexpr int16_t cameraYMaximum = (fullMapHeight - HEIGHT);
