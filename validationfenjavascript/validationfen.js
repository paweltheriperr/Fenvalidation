function isFen(fen) {
  // wyrażenie regularne do sprawdzenia poprawności notacji FEN
  var pattern = /^([rnbqkpRNBQKP1-8]+\/){7}[rnbqkpRNBQKP1-8]+ [wb] (-|[KQkq]+) (-|[a-h][36]) \d+ \d+$/;
  return pattern.test(fen);
}
