public class Elephant extends Piece
{
    protected Elephant(String name, int x, int y)
    {
        super(name, x, y);
        this.flag[this.y][this.x] = true;
    }

    @Override
    protected void move()
    {
        switch ((int) (Math.random() * 2))
        {
            case 0: move0(); break;
            case 1: move1(); break;
        }
    }

    private void move0()
    {
        if (this.y < 7 && this.x < 3)
        {
            System.out.printf("x:%d y:%d ==> ", this.x, this.y);
            this.y++;
            this.x++;
            this.flag[this.y][this.x] = true;
            System.out.printf("x:%d y:%d\n", this.x, this.y);
        }
        else move();
    }

    private void move1()
    {
        if (this.y < 7 && this.x > 1)
        {
            System.out.printf("x:%d y:%d ==> ", this.x, this.y);
            this.y++;
            this.x--;
            this.flag[this.y][this.x] = true;
            System.out.printf("x:%d y:%d\n", this.x, this.y);
        }
        else move();
    }
}
