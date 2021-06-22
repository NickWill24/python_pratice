def game():
    print("welcome to NBA Playground")
    user_input=input('Do want play as lebron james or Kevin Durant?')
    if user_input == ('lebron james'):
        print('playing as lebron james')
        user_input=input('Do you want play against MJ or Kobe?')
        if user_input == ('MJ'):
            print('you chose to play against MJ')
            user_input=input('MJ just made a three point shoot. Do you want go for the two or three?')
            if user_input == ('two shot'):
                print('you made the two shot.')
        elif user_input == ('kobe'):
            print('you chose to play against kobe')
            # user_input=input('')




















game()