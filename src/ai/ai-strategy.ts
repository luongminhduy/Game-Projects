import { Logic, Player } from "../logics";

export interface AiStrategy {
  getOptimalMove(player: Player, logic: Logic): Promise<number>;
}
