reef_health = [20, 30, 50]
nursery_size = 0
pollution = 5
max_turns = 12

for turn in range(1, max_turns + 1):
    print("=========================")
    print("Turn", turn, "/", max_turns)
    print("Reef size:", len(reef_health))
    print("Reef Health:", reef_health)
    print("Nursery corals:", nursery_size)
    print("Pollution level:", pollution)
#================================================
    print("Available Actions:")
    print("1. Grow new coarls in nursery")
    print("2. Transport coarls to reef")
    print("3. Clear pollution")
    action = int(input("Choose an action"))
#================================================
    if action == 1:
        nursery_size += 1
    elif action == 2:
        reef_health += [3] * nursery_size
        nursery_size = 0
    elif action == 3:
        if pollution > 0:
            pollution -= 1
        else:
            print(" Why you help tha reef, ah boy :<")
    else:
        print("good boy, never help reef :>")
    
    for i in range(len(reef_health)):
        reef_health[i] += (5 - pollution)
#==================================================

score = sum(reef_health)
print("your reef heath is:", score)
