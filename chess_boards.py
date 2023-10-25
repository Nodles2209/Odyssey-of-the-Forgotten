"""
Example chess layout:

8 |  ♜    ♞    ♝     ♛    ♚     ♝    ♞     ♜
  |
7 |  ♟    ♟    ♟     ♟    ♟     ♟    ♟     ♟
  |
6 |  □     ■     □     ■     □     ■     □     ■
  |
5 |  ■     □     ■     □     ■     □     ■     □
  |
4 |  □     ■     □     ■     □     ■     □     ■
  |
3 |  ■     □     ■     □     ■     □     ■     □
  |
2 |  ♙    ♙    ♙     ♙    ♙     ♙    ♙     ♙
  |
1 |  ♖    ♘    ♗     ♕    ♔     ♗    ♘     ♖
   ----------------------------------------------
     A     B     C     D     E     F     G     H


    Character      chr  unicode
white chess king	♔	U+2654
white chess queen	♕	U+2655
white chess rook	♖	U+2656
white chess bishop	♗	U+2657
white chess knight	♘	U+2658
white chess pawn	♙	U+2659
black chess king	♚	U+265A
black chess queen	♛	U+265B
black chess rook	♜	U+265C
black chess bishop	♝	U+265D
black chess knight	♞	U+265E
black chess pawn	♟  U+265F

"""

chess_init = ("8 |  ♜    ♞    ♝     ♛    ♚     ♝    ♞     ♜\n"
              "  |                                              \n"
              "7 |  ♟    ♟    ♟     ♟    ♟     ♟    ♟     ♟\n"
              "  |                                              \n"
              "6 |                                              \n"
              "  |                                              \n"
              "5 |                                              \n"
              "  |                                              \n"
              "4 |                                              \n"
              "  |                                              \n"
              "3 |                                              \n"
              "  |                                              \n"
              "2 |  ♙    ♙    ♙     ♙    ♙     ♙    ♙     ♙\n"
              "  |                                              \n"
              "1 |  ♖    ♘    ♗     ♕    ♔     ♗    ♘     ♖\n"
              "   ----------------------------------------------\n"
              "     A     B     C     D     E     F     G     H\n")

chess_1_p0_cutscene = ("   ------------------------------------------------\n"
                       "8 |  ♜    ♞     ♜                      ♚        \n"
                       "  |------------------------------------------------\n"
                       "7 |        ♟          ♟           ♟          ♟  \n"
                       "  |------------------------------------------------\n"
                       "6 |  ♟                ♟           ♝    ♟     ♗  \n"
                       "  |------------------------------------------------\n"
                       "5 |                    ♙                          \n"
                       "  |------------------------------------------------\n"
                       "4 |  ♙                      ♕                    \n"
                       "  |------------------------------------------------\n"
                       "3 |              ♙    ♗                          \n"
                       "  |------------------------------------------------\n"
                       "2 |  ♙          ♙                ♙     ♙    ♙  \n"
                       "  |------------------------------------------------\n"
                       "1 |              ♖          ♖           ♔        \n"
                       "   ------------------------------------------------\n"
                       "     A     B     C     D     E     F     G     H\n")

chess_1_p1 = ("   ------------------------------------------------\n"
              "8 |  ♜    ♞          ♜                 ♚        \n"
              "  |------------------------------------------------\n"
              "7 |        ♟          ♟           ♟          ♟  \n"
              "  |------------------------------------------------\n"
              "6 |  ♟                ♟           ♝    ♟     ♗  \n"
              "  |------------------------------------------------\n"
              "5 |                    ♙                          \n"
              "  |------------------------------------------------\n"
              "4 |  ♙                      ♕                    \n"
              "  |------------------------------------------------\n"
              "3 |              ♙    ♗                          \n"
              "  |------------------------------------------------\n"
              "2 |  ♙          ♙                ♙     ♙    ♙  \n"
              "  |------------------------------------------------\n"
              "1 |              ♖          ♖           ♔        \n"
              "   ------------------------------------------------\n"
              "     A     B     C     D     E     F     G     H\n")

chess_1_p1_cutscene = ("   ------------------------------------------------\n"
                       "8 |  ♜    ♞          ♜    ♕            ♚        \n"
                       "  |------------------------------------------------\n"
                       "7 |        ♟          ♟           ♟          ♟  \n"
                       "  |------------------------------------------------\n"
                       "6 |  ♟                ♟           ♝    ♟     ♗  \n"
                       "  |------------------------------------------------\n"
                       "5 |                    ♙                          \n"
                       "  |------------------------------------------------\n"
                       "4 |  ♙                                            \n"
                       "  |------------------------------------------------\n"
                       "3 |              ♙    ♗                          \n"
                       "  |------------------------------------------------\n"
                       "2 |  ♙          ♙                ♙     ♙    ♙  \n"
                       "  |------------------------------------------------\n"
                       "1 |              ♖          ♖           ♔        \n"
                       "   ------------------------------------------------\n"
                       "     A     B     C     D     E     F     G     H\n")

chess_1_p2 = ("   ------------------------------------------------\n"
              "8 |  ♜    ♞                ♜           ♚        \n"
              "  |------------------------------------------------\n"
              "7 |        ♟          ♟          ♟          ♟  \n"
              "  |------------------------------------------------\n"
              "6 |  ♟                ♟           ♝    ♟     ♗  \n"
              "  |------------------------------------------------\n"
              "5 |                    ♙                          \n"
              "  |------------------------------------------------\n"
              "4 |  ♙                                            \n"
              "  |------------------------------------------------\n"
              "3 |              ♙    ♗                          \n"
              "  |------------------------------------------------\n"
              "2 |  ♙          ♙                ♙     ♙    ♙  \n"
              "  |------------------------------------------------\n"
              "1 |              ♖          ♖           ♔        \n"
              "   ------------------------------------------------\n"
              "     A     B     C     D     E     F     G     H\n")

chess_1_p2_cutscene = ("   ------------------------------------------------\n"
                       "8 |  ♜    ♞                ♖           ♚        \n"
                       "  |------------------------------------------------\n"
                       "7 |        ♟          ♟           ♟          ♟  \n"
                       "  |------------------------------------------------\n"
                       "6 |  ♟                ♟           ♝    ♟     ♗  \n"
                       "  |------------------------------------------------\n"
                       "5 |                    ♙                          \n"
                       "  |------------------------------------------------\n"
                       "4 |  ♙                                            \n"
                       "  |------------------------------------------------\n"
                       "3 |              ♙    ♗                          \n"
                       "  |------------------------------------------------\n"
                       "2 |  ♙          ♙                ♙     ♙    ♙  \n"
                       "  |------------------------------------------------\n"
                       "1 |              ♖                      ♔        \n"
                       "   ------------------------------------------------\n"
                       "     A     B     C     D     E     F     G     H\n")
