import java.util.ArrayList;

public class Main
{
    public static void main(String[] args)
    {
        ArrayList<Piece> pieces = new ArrayList<Piece>(0);
        Game g = new Game();
        g.setPieces(pieces);


        while(g.isNotOver)
        {
            g.choosePiece();
        }

    }
}