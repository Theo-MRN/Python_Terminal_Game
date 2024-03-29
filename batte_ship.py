import random
import os

board = { 'A': [' ', ' ', ' ', ' ', ' '], 'B': [' ', ' ', ' ', ' ', ' '], 'C': [' ', ' ', ' ', ' ', ' '], 'D': [' ', ' ', ' ', ' ', ' '], 'E': [' ', ' ', ' ', ' ', ' ']}
board_1 = { 'A': [' ', ' ', ' ', ' ', ' '], 'B': [' ', ' ', ' ', ' ', ' '], 'C': [' ', ' ', ' ', ' ', ' '], 'D': [' ', ' ', ' ', ' ', ' '], 'E': [' ', ' ', ' ', ' ', ' ']}
board_2 = { 'A': [' ', ' ', ' ', ' ', ' '], 'B': [' ', ' ', ' ', ' ', ' '], 'C': [' ', ' ', ' ', ' ', ' '], 'D': [' ', ' ', ' ', ' ', ' '], 'E': [' ', ' ', ' ', ' ', ' ']}
guess_board_1 = { 'A': [' ', ' ', ' ', ' ', ' '], 'B': [' ', ' ', ' ', ' ', ' '], 'C': [' ', ' ', ' ', ' ', ' '], 'D': [' ', ' ', ' ', ' ', ' '], 'E': [' ', ' ', ' ', ' ', ' ']}
guess_board_2 = { 'A': [' ', ' ', ' ', ' ', ' '], 'B': [' ', ' ', ' ', ' ', ' '], 'C': [' ', ' ', ' ', ' ', ' '], 'D': [' ', ' ', ' ', ' ', ' '], 'E': [' ', ' ', ' ', ' ', ' ']}

class Ships():
    
    def __init__(self, board, opponent):
       self.board = board
       self.opponent = opponent
   
    def __repr__(self):
       return self.board_image

    def final_board(self):
        self.ship_len3() 
        self.ship_len2()
        self.ship_len1()
     

 
    def ship_len3(self):
       if self.opponent == 0:       
         self.ship_1 = []
         abc = 'ABCDE'
         abc_num = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}
         start_colum = random.choices(abc)
         start_row = random.randint(0, 4)      
         self.board[start_colum[0]][start_row] = 'X'
         position_one = self.board[start_colum[0]][start_row]
         for letter in abc_num:
              if letter == start_colum[0]:
                   c_num = abc_num[letter]
                   if start_colum[0] == 'A' or start_colum[0] == 'B':
                        second_colum = random.randint(c_num, c_num + 1)
                   elif  start_colum[0] == 'E' or start_colum[0] == 'D':
                        second_colum = random.randint(c_num - 1, c_num)
                   else:
                        second_colum = random.randint(c_num - 1, c_num + 1)
                   if second_colum == c_num:
                       if start_row == 0 or start_row == 1:
                           second_row = start_row + 1
                           self.board[start_colum[0]][second_row] = 'X'
                           position_two = self.board[start_colum[0]][second_row]
                           third_row = start_row + 2
                           self.board[start_colum[0]][third_row] = 'X'
                           position_three = self.board[start_colum[0]][third_row]
                       elif start_row == 4 or start_row == 3:
                           second_row = start_row - 1
                           self.board[start_colum[0]][second_row] = 'X'
                           position_two = self.board[start_colum[0]][second_row]
                           third_row = start_row - 2
                           self.board[start_colum[0]][third_row] = 'X'
                           position_three = self.board[start_colum[0]][third_row]
                       else:
                           second_row = random.randrange(start_row - 1, start_row + 2, 2)
                           self.board[start_colum[0]][second_row] = 'X'
                           position_two = self.board[start_colum[0]][second_row]
                           if second_row == start_row - 1:
                             third_row = start_row - 2
                             self.board[start_colum[0]][third_row] = 'X'
                             position_three = self.board[start_colum[0]][third_row]
                           else:
                             third_row = start_row + 2
                             self.board[start_colum[0]][third_row] = 'X'
                             position_three = self.board[start_colum[0]][third_row] 
                   elif second_colum == c_num - 1:
                        for le, nu in abc_num.items():
                             if c_num - 1 == nu:
                              second_colum_letter = le
                              self.board[second_colum_letter][start_row] = 'X'
                              position_two = self.board[second_colum_letter][start_row]
                             if c_num - 2 == nu:
                              third_colum_letter = le
                              self.board[third_colum_letter][start_row] = 'X'
                              position_three = self.board[third_colum_letter][start_row]
                   else:
                        for le, nu in abc_num.items():
                             if c_num + 1 == nu:
                                second_colum_letter = le
                                self.board[second_colum_letter][start_row] = 'X'
                                position_two = self.board[second_colum_letter][start_row]
                             if c_num + 2 == nu:
                              third_colum_letter = le
                              self.board[third_colum_letter][start_row] = 'X'
                              position_three = self.board[third_colum_letter][start_row]
         self.ship_1.append(position_one)
         self.ship_1.append(position_two)
         self.ship_1.append(position_three)
                            
         return self.board, self.ship_1
       
       else:
         self.board_image()
         self.ship_1 = []
         abc = 'ABCDE'
         abc_num = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}
         print('Choose your first colum and row for the 3 spaces ship:')
         start_colum = input('Colum:').upper()
         while start_colum not in abc:
             print('Invalid Colum. Please choose again: ')
             start_colum = input('Colum:').upper()
         start_row = input('Row: ')
         while start_row.isnumeric() == False or int(start_row) not in range(1, 6):
          print('Not a valid number. Please select a number between 1 - 5 for the row: ')
          start_row = input('Row: ')
         else:
             start_row = int(start_row)
         self.board[start_colum][start_row - 1] = 'X'
         position_one = self.board[start_colum][start_row - 1]
         print('Choose your second colum and row for the 3 spaces ship:')
         second_colum = input('Second colum: ').upper()
         while second_colum not in abc:
             print('Invalid Colum. Please choose again: ')
             second_colum = input('Second colum:').upper()
         for letter in abc_num:
              if letter == start_colum:
                   start_c_num = abc_num[letter]
              if letter == second_colum:
                   second_c_num = abc_num[letter]
         while second_colum not in abc or (second_colum != start_colum) and (second_c_num != start_c_num + 1) and (second_c_num != start_c_num - 1):
                    print('Second colum is invalid. Please select the same colum or one of the colums next to it: ')
                    second_colum = input('Second colum: ').upper()
                    for letter in abc_num:
                      if letter == start_colum:
                         start_c_num = abc_num[letter]
                      if letter == second_colum:
                          second_c_num = abc_num[letter]
         if start_colum == second_colum:
               second_row = input('Row: ')
               while second_row.isnumeric() == False or int(second_row) not in range(1, 6) or (int(second_row) != start_row +1) and (int(second_row) != start_row - 1):
                    print('Second row is invalid. Please select one of the rows next to it: ')
                    second_row = input('Second row: ')
               else:
                   second_row = int(second_row)
               self.board[second_colum][second_row - 1] = 'X'      
               position_two = self.board[second_colum][second_row - 1]
               third_colum = second_colum
               print('Your third colum will be ', third_colum)
               third_row = input("Select the last row of your ship: ")
               if second_row == start_row + 1:
                while third_row.isnumeric() == False or int(third_row) not in range(1, 6) or (int(third_row) == second_row or int(third_row) == start_row) or (int(third_row) != start_row + 2 and int(third_row) != start_row - 1):
                     print('Third row is invalid. Please select one of the rows next to it: ')
                     third_row = input("Select the last row of your ship: ")

                else:
                 third_row = int(third_row)
                 self.board[third_colum][third_row - 1] ='X'
                 position_three = self.board[third_colum][third_row - 1]
               else:
                while third_row.isnumeric() == False or int(third_row) not in range(1, 6) or (int(third_row) == second_row or int(third_row) == start_row) or (int(third_row) != start_row - 2 and int(third_row) != start_row + 1):
                    print('Third row is invalid. Please select one of the rows next to it: ')
                    third_row = input("Select the last row of your ship: ")
                else:
                    third_row = int(third_row)
                self.board[third_colum][third_row - 1] ='X'
                position_three = self.board[third_colum][third_row - 1]
         else: 
               second_row = start_row
               print('Your secon row is: ', second_row) 
               self.board[second_colum][second_row - 1] = 'X'      
               position_two = self.board[second_colum][second_row - 1]      
               print('Choose your last colum and row for the 3 spaces ship:')
               third_colum = input('Thrid colum: ').upper()
               while third_colum not in abc:
                   print('Invalid Colum. Please choose again:')
                   third_colum = input('Thrid colum: ').upper()
               for letter in abc_num:
                    if letter == third_colum:
                         third_c_num = abc_num[letter]
                    if letter == second_colum:
                            second_c_num = abc_num[letter]
                    if letter == start_colum:
                         start_c_num = abc_num[letter]
               if second_c_num == start_c_num + 1:
                    while second_colum not in abc or (third_c_num == start_c_num or third_c_num == second_c_num) or (third_c_num != start_c_num + 2 and third_c_num != start_c_num - 1):
                         print('Third colum is invalid. Please select the same colum or one of the colums next to it: ')
                         third_colum = input('Third colum: ').upper()
                         for letter in abc_num:
                              if letter == third_colum:
                                   third_c_num = abc_num[letter]
                              if letter == second_colum:
                                   second_c_num = abc_num[letter]
                              if letter == start_colum:
                                   start_c_num = abc_num[letter]
               else:
                    while second_colum not in abc or (third_c_num == start_c_num or third_c_num == second_c_num) or (third_c_num != start_c_num - 2 and third_c_num != start_c_num + 1):
                         print('Third colum is invalid. Please select the same colum or one of the colums next to it: ')
                         third_colum = input('Third colum: ').upper()
                         for letter in abc_num:
                              if letter == third_colum:
                                   third_c_num = abc_num[letter]
                              if letter == second_colum:
                                   second_c_num = abc_num[letter] 
                              if letter == start_colum:
                                   start_c_num = abc_num[letter] 
               third_row = second_row
               print('Your third row is: ', third_row)
               self.board[third_colum][third_row - 1] ='X'
               position_three = self.board[third_colum][third_row - 1]
                  
         self.ship_1.append(position_one)
         self.ship_1.append(position_two)
         self.ship_1.append(position_three)
                            
         return self.board, self.ship_1
      

          
            
    def ship_len2(self):
       if self.opponent == 0:
         self.ship_2 = []
         abc = 'ABCDE'
         abc_num = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}
         start_colum = random.choices(abc)
         start_row = random.randint(0, 4)   
         start_position = self.board[start_colum[0]][start_row] 
         while start_position == 'X':
            start_colum = random.choices(abc)
            start_row = random.randint(0, 4)   
            start_position = self.board[start_colum[0]][start_row]                     
         self.board[start_colum[0]][start_row] = 'X'
         position_one = self.board[start_colum[0]][start_row]
         for letter in abc_num:
              if letter == start_colum[0]:
                   c_num = abc_num[letter]
                   if start_colum[0] == 'A':
                        second_colum = random.randint(c_num, c_num + 1)
                   elif  start_colum[0] == 'E':
                        second_colum = random.randint(c_num - 1, c_num)
                   else:
                        second_colum = random.randint(c_num - 1, c_num + 1)
                   if second_colum == c_num:
                       random_start = start_row - 1 
                       random_end = start_row + 1
                       if start_row == 0:
                           second_row = start_row + 1
                           position_two = self.board[start_colum[0]][second_row]
                           if position_two == 'X':
                               if start_colum[0] == 'A':
                                  second_colum =  c_num + 1
                               elif  start_colum[0] == 'E':
                                  second_colum = c_num - 1
                               else:
                                  second_colum = random.randrange(c_num - 1, c_num + 2, 1) 
                               if second_colum == c_num - 1:
                                   for le, nu in abc_num.items():
                                      if c_num - 1 == nu:
                                         second_colum_letter = le
                                         position_two = self.board[second_colum_letter][start_row]
                                         if position_two == 'X':
                                           for le, nu in abc_num.items():
                                             if c_num + 1 == nu:
                                               second_colum_letter = le
                                               self.board[second_colum_letter][start_row] = 'X'
                                               position_two = self.board[second_colum_letter][start_row]    
                                         else:
                                            self.board[second_colum_letter][start_row] = 'X'                              
                               else:
                                   for le, nu in abc_num.items():
                                      if c_num + 1 == nu:
                                        second_colum_letter = le
                                        position_two = self.board[second_colum_letter][start_row]
                                        self.board[second_colum_letter][start_row] = 'X'        
                           else:
                             self.board[start_colum[0]][second_row] = 'X'
                       elif start_row == 4:
                           second_row = start_row - 1
                           position_two = self.board[start_colum[0]][second_row]
                           if position_two == 'X':
                               if start_colum[0] == 'A':
                                  second_colum =  c_num + 1
                               elif  start_colum[0] == 'E':
                                  second_colum = c_num - 1
                               else:
                                  second_colum = random.randrange(c_num - 1, c_num + 2, 1) 
                               if second_colum == c_num - 1:
                                   for le, nu in abc_num.items():
                                      if c_num - 1 == nu:
                                         second_colum_letter = le
                                         position_two = self.board[second_colum_letter][start_row]
                                         if position_two == 'X':
                                           for le, nu in abc_num.items():
                                             if c_num + 1 == nu:
                                               second_colum_letter = le
                                               self.board[second_colum_letter][start_row] = 'X'
                                               position_two = self.board[second_colum_letter][start_row]    
                                         else:
                                            self.board[second_colum_letter][start_row] = 'X'                              
                               else:
                                   for le, nu in abc_num.items():
                                      if c_num + 1 == nu:
                                        second_colum_letter = le
                                        position_two = self.board[second_colum_letter][start_row]
                                        self.board[second_colum_letter][start_row] = 'X'        
                           else:
                             self.board[start_colum[0]][second_row] = 'X'
                           
                       else:
                           second_row = random.randrange(start_row - 1, start_row + 2, 2)
                           position_two = self.board[start_colum[0]][second_row]
                           while position_two == 'X':
                               second_row = random.randrange(random_start, random_end + 1, 2)
                               position_two = self.board[start_colum[0]][second_row]
                           self.board[start_colum[0]][second_row] = 'X'
                   elif second_colum == c_num - 1:
                        for le, nu in abc_num.items():
                             if c_num - 1 == nu:
                               second_colum_letter = le
                               position_two = self.board[second_colum_letter][start_row]
                               if position_two == 'X':
                                   for le, nu in abc_num.items():
                                      if c_num + 1 == nu:
                                        second_colum_letter = le
                                        self.board[second_colum_letter][start_row] = 'X'
                                        position_two = self.board[second_colum_letter][start_row]    
                               else:
                                   self.board[second_colum_letter][start_row] = 'X'
                   elif second_colum == c_num + 1:
                       for le, nu in abc_num.items():
                             if c_num + 1 == nu:
                               second_colum_letter = le
                               position_two = self.board[second_colum_letter][start_row]
                               self.board[second_colum_letter][start_row] = 'X'   
                    
         self.ship_2.append(position_one)
         self.ship_2.append(position_two)   
         return self.ship_2, self.board
       
       else:
          self.board_image()
          self.ship_2 = []
          abc = 'ABCDE'
          abc_num = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}
          print('Choose your first colum and row for the 2 spaces ship:')
          start_colum = input('Colum: ').upper()
          while start_colum not in abc:
             print('Invalid Colum. Please choose again: ')
             start_colum = input('Colum:').upper()
          start_row = input('Row: ')
          while start_row.isnumeric() == False or int(start_row) not in range(1, 6):
             print('Invalid row. Please Choose again')
             start_row = input('Row: ')
          else:
              start_row = int(start_row)
          position_one = self.board[start_colum][start_row - 1] 
          while position_one == 'X':
            print('You already has sonthing on this position. Choose another one: ')
            start_colum = input("Colum: ")
            while start_colum not in abc:
             print('Invalid Colum. Please choose again: ')
             start_colum = input('Colum:').upper()
            start_row = input('Row: ')
            while start_row.isnumeric() == False or int(start_row )not in range(1, 6):
             print('Invalid row. Please Choose again')
             start_row = input('Row: ')
            else:
                start_row = int(start_row)
          position_one = self.board[start_colum][start_row - 1]                         
          self.board[start_colum][start_row - 1] = 'X'
          position_one = self.board[start_colum][start_row - 1]
          print('Choose your second colum and row for the 2 spaces ship:')
          second_colum = input('Second colum: ').upper()
          while second_colum not in abc:
             print('Invalid colum. Please choose again:')
             second_colum = input('Second colum: ').upper()
          for letter in abc_num:
               if letter == start_colum:
                    start_c_num = abc_num[letter]
               if letter == second_colum:
                  second_c_num = abc_num[letter]
          while second_colum not in abc or (second_colum != start_colum) and (second_c_num != start_c_num + 1) and (second_c_num != start_c_num - 1):
                    print('Second colum is invalid. Please select the same colum or one of the colums next to it: ')
                    second_colum = input('Second colum: ').upper()
                    for letter in abc_num:
                       if letter == start_colum:
                          start_c_num = abc_num[letter]
                       if letter == second_colum:
                          second_c_num = abc_num[letter]
          if start_colum == second_colum:
                   second_row = input('Second row: test_1')
                   while second_row.isnumeric() == False or int(second_row) not in range(1, 6) or (int(second_row) != start_row + 1) and (int(second_row) != start_row - 1):
                     print('Second row is invalid. Please select one of the rows next to it: ')
                     second_row = input('Second row: test_2')
                   else:
                       second_row = int(second_row)
                       
                   position_two = self.board[second_colum][second_row - 1]
          else:
                 second_row = start_row
                 print('This is your second row:', second_row)
                 position_two = self.board[second_colum][second_row - 1]
                   
          while position_two == 'X':
                    print('You already have something there. Choose the second position again: ')
                    second_colum = input('Second colum: ').upper()
                    while second_colum not in abc:
                        print('Invalid Colum. Please choose again: ')
                        second_colum = input('Second colum: ').upper()
                    for letter in abc_num:
                       if letter == start_colum:
                            start_c_num = abc_num[letter]
                       if letter == second_colum:
                            second_c_num = abc_num[letter]
                       while second_colum not in abc or (second_colum != start_colum) and (second_c_num != start_c_num + 1) and (second_c_num != start_c_num - 1):
                            print('Second colum is invalid. Please select the same colum or one of the colums next to it: ')
                            second_colum = input('Second colum: ').upper()
                            for letter in abc_num:
                              if letter == start_colum:
                                 start_c_num = abc_num[letter]
                              if letter == second_colum:
                                  second_c_num = abc_num[letter]
                       if start_colum == second_colum:
                              second_row = input('Second row: ')
                              while second_row.isnumeric() == False or int(second_row) not in range(1, 6) or (int(second_row) != start_row +1) and (int(second_row) != start_row - 1) :
                                print('Second row is invalid. Please select one of the rows next to it: ')
                                second_row = input('Second row: ')
                              else:
                                second_row = int(second_row)
                              position_two = self.board[second_colum][second_row - 1]
                       else:
                            second_row = start_row
                            print('This is your second row: ', second_row)
                            position_two = self.board[second_colum][second_row - 1]
                      
          self.board[second_colum][second_row - 1] = 'X'
         
            
          self.ship_2.append(position_one)
          self.ship_2.append(position_two)   
          return self.ship_2, self.board



    def ship_len1(self):
       if self.opponent == 0:
         self.ship_3 = []
         abc = 'ABCDE'
         start_colum = random.choices(abc)
         start_row = random.randint(0, 4)   
         start_position = self.board[start_colum[0]][start_row] 
         while start_position == 'X':   
            start_colum = random.choices(abc)
            start_row = random.randint(0, 4)   
         start_position = self.board[start_colum[0]][start_row]
         self.board[start_colum[0]][start_row] = 'X'
         self.ship_3.append(start_position)
         return self.board, self.ship_3
       
       else:
         self.board_image()
         self.ship_3 = []
         abc = 'ABCDE'
         print('Choose your colum and row for the 1 spaces ship:')
         start_colum = input('Colum: ').upper()
         while start_colum not in abc:
             print('Invalid colum. Choose again: ')
             start_colum = input('Colum: ').upper()   

         start_row = input('Row: ')
         while start_row.isnumeric() == False or int(start_row) not in range(1, 6):
             print('Not a valid row. Please choose a number between 1 - 5')
             start_row = input('Row: ')
         else:
             start_row = int(start_row)   
         position_one = self.board[start_colum][start_row - 1] 
         while position_one == 'X':
            print('You already has sonthing on this position. Choose another one: ')
            start_colum = input("Colum: ").upper()
            while start_colum not in abc:
             print('Invalid colum. Choose again: ')
             start_colum = input('Colum: ').upper()

            start_row = input('Row: ')
            while start_row.isnumeric() == False or int(start_row) not in range(1, 6):
              print('Not a valid row. Please choose a number between 1 - 5')
              start_row = input('Row: ')
            else:
             start_row = int(start_row)   
             position_one = self.board[start_colum][start_row - 1] 

         self.board[start_colum][start_row - 1] = 'X'
         position_one = self.board[start_colum][start_row - 1]
         self.ship_3.append(position_one)
         return self.board, self.ship_3, self.board_image()





    def board_image(self):  
      
      print('   |   A   |   B   |   C   |   D   |   E   | ')
      print('   |_______|_______|_______|_______|_______| ')
      print('   |       |       |       |       |       | ')
      print(' 1 |   {A0}   |   {B0}   |   {C0}   |   {D0}   |   {E0}   | '.format(A0=self.board['A'][0], B0=self.board['B'][0], C0=self.board['C'][0], D0=self.board['D'][0], E0=self.board['E'][0]))
      print('   |_______|_______|_______|_______|_______| ')
      print('   |       |       |       |       |       | ')
      print(' 2 |   {A1}   |   {B1}   |   {C1}   |   {D1}   |   {E1}   | '.format(A1=self.board['A'][1], B1=self.board['B'][1], C1=self.board['C'][1], D1=self.board['D'][1], E1=self.board['E'][1]))
      print('   |_______|_______|_______|_______|_______| ')
      print('   |       |       |       |       |       | ')
      print(' 3 |   {A2}   |   {B2}   |   {C2}   |   {D2}   |   {E2}   | '.format(A2=self.board['A'][2], B2=self.board['B'][2], C2=self.board['C'][2], D2=self.board['D'][2], E2=self.board['E'][2]))
      print('   |_______|_______|_______|_______|_______| ')
      print('   |       |       |       |       |       | ')
      print(' 4 |   {A3}   |   {B3}   |   {C3}   |   {D3}   |   {E3}   | '.format(A3=self.board['A'][3], B3=self.board['B'][3], C3=self.board['C'][3], D3=self.board['D'][3], E3=self.board['E'][3]))
      print('   |_______|_______|_______|_______|_______| ')
      print('   |       |       |       |       |       | ')
      print(' 5 |   {A4}   |   {B4}   |   {C4}   |   {D4}   |   {E4}   | '.format(A4=self.board['A'][4], B4=self.board['B'][4], C4=self.board['C'][4], D4=self.board['D'][4], E4=self.board['E'][4]))
      print('   |_______|_______|_______|_______|_______| ')


class Players():
  
  def __init__(self, ships, board, guess_board):
     self.ships = ships
     self.board = board
     self.guess_board = guess_board

           
  def guess_board_image(self):  
      
      print('   |   A   |   B   |   C   |   D   |   E   | ')
      print('   |_______|_______|_______|_______|_______| ')
      print('   |       |       |       |       |       | ')
      print(' 1 |   {A0}   |   {B0}   |   {C0}   |   {D0}   |   {E0}   | '.format(A0=self.guess_board['A'][0], B0=self.guess_board['B'][0], C0=self.guess_board['C'][0], D0=self.guess_board['D'][0], E0=self.guess_board['E'][0]))
      print('   |_______|_______|_______|_______|_______| ')
      print('   |       |       |       |       |       | ')
      print(' 2 |   {A1}   |   {B1}   |   {C1}   |   {D1}   |   {E1}   | '.format(A1=self.guess_board['A'][1], B1=self.guess_board['B'][1], C1=self.guess_board['C'][1], D1=self.guess_board['D'][1], E1=self.guess_board['E'][1]))
      print('   |_______|_______|_______|_______|_______| ')
      print('   |       |       |       |       |       | ')
      print(' 3 |   {A2}   |   {B2}   |   {C2}   |   {D2}   |   {E2}   | '.format(A2=self.guess_board['A'][2], B2=self.guess_board['B'][2], C2=self.guess_board['C'][2], D2=self.guess_board['D'][2], E2=self.guess_board['E'][2]))
      print('   |_______|_______|_______|_______|_______| ')
      print('   |       |       |       |       |       | ')
      print(' 4 |   {A3}   |   {B3}   |   {C3}   |   {D3}   |   {E3}   | '.format(A3=self.guess_board['A'][3], B3=self.guess_board['B'][3], C3=self.guess_board['C'][3], D3=self.guess_board['D'][3], E3=self.guess_board['E'][3]))
      print('   |_______|_______|_______|_______|_______| ')
      print('   |       |       |       |       |       | ')
      print(' 5 |   {A4}   |   {B4}   |   {C4}   |   {D4}   |   {E4}   | '.format(A4=self.guess_board['A'][4], B4=self.guess_board['B'][4], C4=self.guess_board['C'][4], D4=self.guess_board['D'][4], E4=self.guess_board['E'][4]))
      print('   |_______|_______|_______|_______|_______| ')

 
  def attack(self, colum, row, other_player): # check for hits and output guess board
     attack_1 = other_player.board[colum][row]
     if attack_1 == 'X':
      print('You hit a ship!')
      self.guess_board[colum][row] = 'Y'
      self.guess_board_image()
      end_game() 
      
     else:
      print('You missed!')
      self.guess_board[colum][row] = 'N'
      self.guess_board_image()
      end_game()



def attack_colum_row(count): # two players attack selection
   abc = 'ABCDEFGHIJ'
   if count == 1:
     player = player_1
     other_player = player_2
     print('Player 1 turn:')
     player_1.guess_board_image()
     print('Select one colum and one row to attack:')
     colum = input('Colum: ').upper()
     while colum not in abc:
       print('Not a valid colum, choose again:')
       colum = input('Colum: ').upper()
     row = input('Row: ')
     while row.isnumeric() == False or int(row) not in range(1, 6):
       print('Not a valid row, choose again:')
       row = input('Row: ')
     row = int(row) - 1
     player.attack(colum, row, other_player)   
     count += 1
   elif count == 2:
     player = player_2
     other_player = player_1
     print('Player 2 turn:')
     player_2.guess_board_image()
     print('Select one colum and one row to attack:')
     colum = input('Colum: ').upper()
     while colum not in abc:
       print('Not a valid colum, choose again:')
       colum = input('Colum: ').upper()
     row = input('Row: ')
     while row.isnumeric() == False or int(row) not in range(1, 6):
       row = input('Row: ')
     row = int(row) - 1
     player.attack(colum, row, other_player)
     count -= 1


def end_game(): # check if there is a winner
    winner = False
    hits_1 = 0
    hits_2 = 0
    for key in guess_board_1.keys():
     for colum in key:
       for row in range(0, 5):
         if guess_board_1[colum][row] == 'Y':
          hits_1 += 1
    for key in guess_board_2.keys():
      for colum in key:
       for row in range(0, 5):
         if guess_board_2[colum][row] == 'Y':
           hits_2 += 1
 
    if hits_1 == 6: 
         print('Player 1 won!')
         winner = True
         exit()
       
    elif hits_2 == 6:
         print('Player 2 won!')
         winner = True
         exit()
    
    return winner

      

def next_round(): #Change for next player if no winner
   count = 1
   while end_game() == False:
      if count == 1:
       attack_colum_row(count)
       count += 1
      else:
       attack_colum_row(count)
       count -= 1
   exit()


   
def round_count_down(): # count down the 30 chances
   round = 0
   total_try = 30
   abc = 'ABCDEFGHIJ'
   
   while round < 31:
     left_try = total_try - round
     if end_game() == False:
       print('You have {left_try} tries left'.format(left_try = left_try))
       print('Select one colum and one row to attack:')
       colum = input('Colum: ').upper()
       while colum not in abc:
         print('Not a valid colum, choose again:')
         colum = input('Colum: ').upper()
       row = input('Row: ')
       while row.isnumeric() == False or int(row) not in range(1, 11):
         print('Not a valid row, choose again:')
         row = input('Row: ')
       row = int(row) - 1
       player_1.attack(colum, row, player_2)   
       round += 1

   else:
      print('No more tries. You lost!')
      exit()
     
     
   
    

  


# start game


print('''This game has three modes:
         1 - Just you. You will have 30 chances to find the three ships on a hidden board
         2 - You against another player with both havening random hidden boards to attack
         3 - You against another player with both creating your own ships
         All modes will have three ships to be found. One ship with 3 spaces, one ship with two spaces and one ship with only one space''')
choice = input('Which mode do you like to play? Select 1, 2 or 3: ')
while choice.isnumeric == False or int(choice) not in range(1, 4):
    print("Invalid option. Choose between 1, 2 or 3: ")
    print('Invalid option. Please select again:')
    print('''This game has three modes:
         1 - Just you. You will have 30 chances to find the three ships on a hidden board
         2 - You against another player with both havening random hidden boards to attack
         3 - You against another player with both creating your own ships
         All modes will have three ships to be found. One ship with 3 spaces, one ship with two spaces and one ship with only one space''')
    choice = input('Which mode do you like to play? Select 1, 2 or 3: ')
else:
    choice = int(choice)

if choice == 1: #30 chances with random ships / 1 board
     opponent = 0
     ships_player_1 = Ships(board_1, opponent)
     ships_player_1.final_board()
     player_1 = Players(ships_player_1, board_1, guess_board_1)
     ships_player_2 = Ships(board_2, opponent)
     ships_player_2.final_board()
     ships_player_2.board_image()
     player_2 = Players(ships_player_2, board_2, guess_board_2)
     round_count_down()


elif choice == 2: # random ships / 2 boards
     opponent = 0
     ships_player_1 = Ships(board_1, opponent)
     ships_player_1.final_board()
     player_1 = Players(ships_player_1, board_1, guess_board_1)
     ships_player_2 = Ships(board_2, opponent)
     ships_player_2.final_board()
     player_2 = Players(ships_player_2, board_2, guess_board_2)
     next_round()
else: #players create ships / 2 boards
     opponent = 1
     ships_player_1 = Ships(board_1, opponent)
     ships_player_1.final_board()
     player_1 = Players(ships_player_1, board_1, guess_board_1)
     print('Press any key to hide your board and pass to the other player and start the attacks: ')
     input()
     os.system('clear')
     ships_player_2 = Ships(board_2, opponent)
     ships_player_2.final_board()
     player_2 = Players(ships_player_2, board_2, guess_board_2)
     print('Press any key to hide your board and pass to the other player and start the attacks: ')
     input()
     os.system('clear')
     next_round()
   

