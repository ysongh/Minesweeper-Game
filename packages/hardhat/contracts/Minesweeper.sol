//SPDX-License-Identifier: MIT
pragma solidity >=0.8.0 <0.9.0;

contract Minesweeper {
  constructor() {}

  Game[] games;

  struct Game {
    string programId;
    string storeId;
  }

  function getGames() public view returns (Game[] memory){
    return games;
  }

  function createGame(string memory _programId, string memory _storeId) public {
    games.push(Game(_programId, _storeId));
  }
}