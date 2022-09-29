import java.util.ArrayList;

public class Main2
{


    public static String play()
    {
        ArrayList<Piece> pieces = new ArrayList<Piece>(0);
        Game g = new Game();
        g.setPieces(pieces);




        while(g.isNotOver)
        {
            g.choosePiece();
        }

        return g.winner;

    }

    public static void main(String[] args)
    {
        int horseWin=0;
        int ministerWin=0;
        int castleWin=0;
        int elephantWin=0;

        for(int i = 0; i < 10000; i++)
        {

            String a = play();
            System.out.println();

            if (a.equals("Castle"))
            {
                castleWin++;
            }

            else if (a.equals("Minister"))
            {
                ministerWin++;
            }

            else if (a.equals("Horse"))
            {
                horseWin++;
            }

            else if (a.equals("Elephant"))
            {
                elephantWin++;
            }
        }

        System.out.println(castleWin);
        System.out.println(horseWin);
        System.out.println(ministerWin);
        System.out.println(elephantWin);

    }
}
