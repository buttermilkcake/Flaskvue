import random 

songs = ['Little Red Rooster, Key of G', 'Basic 12-bar Blues, Any Key',
         'Sweet Jane, Key of D', 'Gimme Some Lovin\', Key of E',
         'Secret Agent Man, Key of G', 'I Wanna be Sedated, Key of E',
        'Should I Stay or Should I Go?, Key of E']

songs_active = True
prompt = "\nRandom Song Generator"
while True:
    ask = input(prompt)    
    print(random.choice(songs))

    
