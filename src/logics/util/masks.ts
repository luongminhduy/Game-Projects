import bigInt = require('big-integer');

export class Masks {
  static readonly FullBoard: bigInt.BigInteger = bigInt(0x3ffffffffff);
  static readonly EmptyBoard: bigInt.BigInteger = bigInt(0x0);
  static readonly VerticalFour: bigInt.BigInteger = bigInt(0x204081);
  static readonly HorizontalFour: bigInt.BigInteger = bigInt(0xf);

  // BLTR - bottom left, top right.
  static readonly DiagonalFourBLTR: bigInt.BigInteger = bigInt(0x208208);

  // TLBR - top left, bottom right.
  static readonly DiagonalFourTLBR: bigInt.BigInteger = bigInt(0x1010101);
}
