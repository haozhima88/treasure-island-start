print('''
                 ._
              .-'  `-.
           .-'        \
          ;    .-'\    ;
          `._.'    ;   |
                   |   |
                   ;   :
                  ;   :
                  ;   :
                 /   /
                ;   :                   ,
                ;   |               .-"7|
              .-'"  :            .-' .' :
           .-'       \         .'  .'   `.
         .'           `-. ""-.-'`""    `",`-._..--"7
         ;    .          `-.J `-,    ;"`.;|,_,    ;
       _.'    |         `"" `. ."""--. o \:.-. _.'
    .""       :            ,--`;   ,  `--/}o,' ;
    ;   .___.'        /     ,--.`-. `-..7_.-  /_
     \   :   `..__.._;    .'__;    `---..__.-'-.`"-,
     .'   `--. |   \_;    \\'   `-._.-")     \\\  `-,
     `.   -.`_):      `.   `-"""`.   ;__.' ;/ ;   "
       `-.__7"  `-..._.'`7     -._;'  ``"-''
                         `--.,__.'              fsc
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

choice = input('Type "left" or "right"')
if choice == "left":
  choice2 = input('Type "swim" or "wait"')
  if choice2 == "wait":
    choice3 = input('Which door? "red" or "blue" or "yellow"')
    if choice3 == "yellow":
      print('You Win!')
    else:
      print('Game Over.')
  else:
    print('Game Over.')
else:
  print('Game Over.')