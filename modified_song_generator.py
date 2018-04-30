import random 

songs = ['Little Red Rooster, Key of G', 'Basic 12-bar Blues, Any Key',
         'Sweet Jane, Key of D', 'Gimme Some Lovin\', Key of E',
         'Secret Agent Man, G', 'I Wanna be Sedated, E',
        'Should I Stay or Should I Go?, E']

#rand_songs = random.choice(list(songs.items()))

songs_active = True
prompt = "\nWould you like to play a song?"
prompt += "\n(Enter 'quit' if you do not.)"

while True:
    ask = input(prompt)    

    if ask == 'quit':
        break
    else: 
        if ask == 'Yes' or 'yes' or 'YES' or 'Y' or 'y':
            print(random.choice(songs))

    
