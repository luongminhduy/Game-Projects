import { Connect4Client } from "./multiplayer-client";
import { AUTO, Game, Types } from "phaser";
import { AiPlayerController } from "./gui/controllers/ai-player-controller";
import { HumanPlayerController } from "./gui/controllers/human-player-controller";
import { MultiplayerOpponentController } from "./gui/controllers/multiplayer-opponent-controller";
import { MultiplayerPlayerController } from "./gui/controllers/multiplayer-player-controller";
import { MenuScene } from "./gui/scenes/menu-scene";
import { MultiplayerPlayingScene } from "./gui/scenes/multiplayer-scene";
import { PlayingScene } from "./gui/scenes/playing-scene";
import { globalScale } from "./gui/util/scale";
import { RandomStrategy } from "./ai/random-strategy";
import { MinimaxStrategy } from "./ai/minimax_strategy";

export const multiplayerServer =
  "wss://https://kedat-connect4-server.herokuapp.com/";
// export const multiplayerServer = "ws://192.168.53.145:8000";
const client: Connect4Client = new Connect4Client();
const menu = new MenuScene({ key: "menu" });
const easyScene = new PlayingScene(
  { key: "easy" },
  new HumanPlayerController(),
  new AiPlayerController(new RandomStrategy(800))
);
const mediumScene = new PlayingScene(
  { key: "medium" },
  new HumanPlayerController(),
  new AiPlayerController(new MinimaxStrategy(3000))
);
const localScene = new PlayingScene(
  { key: "local" },
  new HumanPlayerController(),
  new HumanPlayerController()
);
const createMultiplayer = new MultiplayerPlayingScene(
  { key: "mp-create" },
  new MultiplayerPlayerController(client),
  new MultiplayerOpponentController(client),
  client,
  false
);
const joinMultiplayer = new MultiplayerPlayingScene(
  { key: "mp-join" },
  new MultiplayerPlayerController(client),
  new MultiplayerOpponentController(client),
  client,
  true
);

const config: Types.Core.GameConfig = {
  type: AUTO,
  width: globalScale(600),
  height: globalScale(600),
  scene: [
    menu,
    easyScene,
    mediumScene,
    localScene,
    createMultiplayer,
    joinMultiplayer,
  ],
  scale: {
    mode: Phaser.Scale.FIT,
    autoCenter: Phaser.Scale.CENTER_HORIZONTALLY,
  },
  dom: {
    createContainer: true,
  },
  parent: "canvas-parent",
};

const game = new Game(config);
