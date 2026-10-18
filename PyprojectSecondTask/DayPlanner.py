daynum = int(input())
match daynum:
    case 1:
        print("monday study day")
    case 2:
        print("tuesday study day")
    case 3:
        print("wednesday study day")
    case 4:
        print("thursday study day")
    case 5:
        print("friday study day")
    case 6:
        print("saturday WEEKEND")
    case 7:
        print("sunday WEEKEND")
    case _:
        print("Invalid day")