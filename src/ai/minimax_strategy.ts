import { Logic, Constants, Player } from "../logics";
import { AiStrategy } from "./ai-strategy";

export class MinimaxStrategy implements AiStrategy {

  private simulatedThinkingTime?: number;

  constructor(simulatedThinkingTime?: number) {
    this.simulatedThinkingTime = simulatedThinkingTime;
  }

  private allPossibleMoves(logic: Logic): number[] {
    const availableColumns: number[] = [];
    for (let column = 0; column < Constants.columns; column++) {
      if (logic.canPlaceChip(column)) availableColumns.push(column);
    }
    return availableColumns;
  }

  getOptimalMove(player: Player, logic: Logic): Promise<number> {
    // calculate move
    let scores: number[] = [];
    let moves: number[] = this.allPossibleMoves(logic);
    moves.forEach(move =>
      {
        const board: Logic = logic.createCopy();
        board.placeChip(player, move);
        let score = this.minimax(3, board, -Infinity, +Infinity, Player.One);
        scores.push(score);
      })
    const idxColumn: number = scores.indexOf(Math.max(...scores));
    
    return new Promise((resolve) => {
      setTimeout(() => resolve(moves[idxColumn]), this.simulatedThinkingTime);
    });
  }

  private heuristicEvaluate(player: Player, isWin: boolean): number
  {
    if (isWin && player === Player.Two) return 1;
    else if (isWin && player === Player.One) return -1;
    else return 0;
  }

  private minimax(depth: number, logic: Logic, alpha: number, beta: number, player: Player): number
  {
    // game is complete
    const isWin = logic.didWin(player);
    const isFull = logic.boardIsFull();
    if (isWin || isFull || depth === 0)
      return this.heuristicEvaluate(player, isWin);

    const moves: number[] = this.allPossibleMoves(logic);
    const updatedLogic: Logic = logic.createCopy();
    if (player === Player.Two)
    { // maximize
      let score = -Infinity;
      for (let move of moves)
      {
        updatedLogic.placeChip(player, move);
        const evaluation = this.minimax(depth - 1, updatedLogic, alpha, beta, Player.One);
        score = Math.max(score, evaluation);
        alpha = Math.max(alpha, score);
        if (beta <= alpha)
          break;
      }
      return score;
    }
    else {
      let score = +Infinity;
      for (let move of moves)
      {
        updatedLogic.placeChip(player, move);
        const evaluation = this.minimax(depth - 1, updatedLogic, alpha, beta, Player.Two);
        score = Math.min(score, evaluation);
        beta = Math.min(beta, score)
        if (beta <= alpha)
          break;
      }
      return score;
    }
  }
}