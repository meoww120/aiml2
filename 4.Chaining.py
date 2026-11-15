rules = {
    "raining": "ground is wet",
    "ground is wet": "ground is slippery",
    "ground is slippery": "can not play cricket",
    "can not play cricket": None,

    "not raining": "the ground is dry",
    "the ground is dry": "ground is not slippery",
    "ground is not slippery": "can play cricket",
    "can play cricket": None
}


def forward_chaining():

    weather = int(input("What is happening:\n1. Raining\n2. Not Raining\n-> "))

    fact = None
    goal = "can play cricket"

    if weather == 1:
        fact = "raining"
    elif weather == 2:
        fact = "not raining"
    else:
        print("Invalid choice!")
        return None

    output = []
    statement = fact

    output.append(statement)

    while statement is not None:

        statement = rules[statement]
        output.append(statement)

        if statement == goal:
            break

    if statement == goal:
        print("\n----x Goal Reached x----")
    else:
        print("\n----x Goal Cannot be Reached x----")

    print("\nForward Chaining:")
    for i in output:
        print(i, "->")

    return fact


def backward_chaining(fact):

    reverse_rules = {
        v: k for k, v in rules.items() if v is not None
    }

    dooing = int(input("\nCan we play cricket:\n1. Yes\n2. No\n-> "))

    if dooing == 1:
        goal = "can play cricket"
    elif dooing == 2:
        goal = "can not play cricket"
    else:
        print("Invalid choice!")
        return

    output = []
    statement = goal

    output.append(statement)

    while statement != fact:

        if statement not in reverse_rules:
            break

        statement = reverse_rules[statement]
        output.append(statement)

    if statement == fact:
        print("\n----x Fact Can be Derived x----")
    else:
        print("\n----x Fact Cannot be Derived x----")

    print("\nBackward Chaining:")
    for i in output:
        print(i, "<-")


fact = forward_chaining()

if fact is not None:
    backward_chaining(fact)