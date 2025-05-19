from timer import Timer

def main():

    # Create timer instances
    timer1 = Timer("Workout", 45)
    timer2 = Timer("Meditation", 10)


    # print each timer
    print(timer1)
    print(timer2)

    print(f"timer1: {timer1.name}, {timer1.duration}, {timer1.started_at}")
    print(f"timer2: {timer2.name}, {timer2.duration}, {timer2.started_at}")


    # print each timer using __str__
    print(timer1.__str__())
    print(timer2.__str__())


    # store timers in a list and print using __repr__
    # print(timer1.__repr__())
    # print(timer2.__repr__())

    timers = [timer1, timer2]
    print(timers)


if __name__ == "__main__":
    main()
