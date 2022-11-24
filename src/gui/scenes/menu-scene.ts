import { Scene } from "phaser";
import background from "../../assets/menu_background.png";
import { Button } from "../components/button";
import { MultiplayerModal } from "../components/multiplayer-modal";
import { globalScale } from "../util/scale";

export class MenuScene extends Scene {
  private multiplayerModal: MultiplayerModal;

  preload() {
    Button.preload(this);
    this.load.image("menu-background", background);
  }

  create() {
    this.add.image(0, 0, "menu-background").setOrigin(0, 0);
    this.multiplayerModal = new MultiplayerModal(
      this,
      900,
      900,
      (displayName) => this.scene.start("mp-join", { displayName }),
      (displayName) => this.scene.start("mp-create", { displayName })
    );
    new Button(this, globalScale(138), globalScale(400), "Easy", () =>
      this.scene.switch("easy")
    );
    new Button(this, globalScale(138), globalScale(460), "Medium", () =>
      this.scene.switch("medium")
    );
    // new Button(this, globalScale(138), globalScale(520), 'Hard', () =>
    //   this.scene.switch('hard')
    // );
    new Button(this, globalScale(352), globalScale(400), "Local", () =>
      this.scene.switch("local")
    );
    new Button(this, globalScale(352), globalScale(460), "Multiplayer", () =>
      this.multiplayerModal.show()
    );
  }

  update() {}
}
