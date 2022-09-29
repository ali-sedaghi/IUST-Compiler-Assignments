import java.util.ArrayList;
public class Game
{
    protected boolean isNotOver = true;
    ArrayList<Piece> pieces = new ArrayList<Piece>(0);
    public String winner;
    protected void setPieces(ArrayList<Piece> pieces)
    {
        this.pieces = pieces;
        pieces.add(new Castle("Castle", 0, 0));
        pieces.add(new Minister("Minister", 1, 0));
        pieces.add(new Horse("Horse", 2, 0));
        pieces.add(new Elephant("Elephant", 3, 0));
    }

    protected void choosePiece()
    {
        switch ((int) (Math.random() * pieces.size()))
        {
            case 0:
                System.out.printf("%s ", pieces.get(0).name); pieces.get(0).move(); win(0); collision(0);; break;
            case 1:
                System.out.printf("%s ", pieces.get(1).name); pieces.get(1).move(); win(1); collision(1); break;
            case 2:
                System.out.printf("%s ", pieces.get(2).name); pieces.get(2).move(); win(2); collision(2); break;
            case 3:
                System.out.printf("%s ", pieces.get(3).name); pieces.get(3).move(); win(3); collision(3); break;
        }
    }

    public void collision(int n)
    {
        for (int i = 0; i < pieces.size() && i != n; i++)
        {
            if (pieces.get(n).x == pieces.get(i).x && pieces.get(n).y == pieces.get(i).y)
            {
                System.out.printf("%s has been removed.\n", pieces.get(i).name);
                pieces.remove(i);
                break;
            }
        }
    }

    private void win(int n)
    {
        if (pieces.get(n).y == 7)
        {
            System.out.printf("%s WON", pieces.get(n).name);
            isNotOver = false;
            winner = pieces.get(n).name;

        }
    }
}
