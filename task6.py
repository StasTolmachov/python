ticket1 = "385913"
ticket2 = "385916"


def luckyTicket(ticket):
    begin = sum(int(item) for item in ticket[:3])
    end = sum(int(item) for item in ticket[3:])

    if begin == end:
        print("true")
    else:
        print("false")

luckyTicket(ticket1)
luckyTicket(ticket2)
