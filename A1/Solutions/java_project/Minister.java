public class Minister extends Piece
{
    protected Minister(String name, int x, int y)
    {
        super(name, x, y);
        this.flag[this.y][this.x] = true;
    }

    private int turn = 0;

    @Override
    protected void move()
    {
        if(turn % 2 == 0)
        {
            switch ((int) (Math.random() * 3))
            {
                case 0: moveCastle0(); break;
                case 1: moveCastle1(); break;
                case 2: moveCastle2(); break;
            }
        }

        else
        {
            switch ((int) (Math.random() * 2))
            {
                case 0: moveElephant0(); break;
                case 1: moveElephant1(); break;
            }
        }
    }

    private void moveCastle0()
    {
        if (this.y < 7)
        {
            System.out.printf("x:%d y:%d =(Castle Move)=> ", this.x, this.y);
            this.y++;
            this.flag[this.y][this.x] = true;
            System.out.printf("x:%d y:%d\n", this.x, this.y);
            turn++;
        }
        else move();

    }

    private void moveCastle1()
    {
        if (this.x < 3)
        {
            System.out.printf("x:%d y:%d =(Castle Move)=> ", this.x, this.y);
            this.x++;
            this.flag[this.y][this.x] = true;
            System.out.printf("x:%d y:%d\n", this.x, this.y);
            turn++;
        }
        else move();
    }

    private void moveCastle2()
    {
        if (this.x > 1)
        {
            System.out.printf("x:%d y:%d =(Castle Move)=> ", this.x, this.y);
            this.x--;
            this.flag[this.y][this.x] = true;
            System.out.printf("x:%d y:%d\n", this.x, this.y);
            turn++;
        }
        else move();
    }

    private void moveElephant0()
    {
        if (this.y < 7 && this.x < 3)
        {
            System.out.printf("x:%d y:%d =(Elephant Move)=> ", this.x, this.y);
            this.y++;
            this.x++;
            this.flag[this.y][this.x] = true;
            System.out.printf("x:%d y:%d\n", this.x, this.y);
            turn++;
        }
        else move();
    }

    private void moveElephant1()
    {
        if (this.y < 7 && this.x > 1)
        {
            System.out.printf("x:%d y:%d =(Elephant Move)=> ", this.x, this.y);
            this.y++;
            this.x--;
            this.flag[this.y][this.x] = true;
            System.out.printf("x:%d y:%d\n", this.x, this.y);
            turn++;
        }
        else move();
    }
}
