matrix=[[""," 0","1","2"],["0","-","-","-"],["1","-","-","-"],["2","-","-","-"]]
rev_matrix=[[""," 0","1","2"],["0","-","-","-"],["1","-","-","-"],["2","-","-","-"]]
win_team = None
team = ('x','0') 
marker =True 
#

def print_matrix(m): 
    for x in range(4): 
        str="" 
        for y in range(4): 
            str+=m[x][y]+" " 
        print(str)
        
        
def rotate_matrix(m): 
    for x in range(1,4): 
        for y in range(1,4):
            rev_matrix[x][y]=m[y][3-x+1]
    return rev_matrix
    
    
def print_error(): print ("нужно ввести строго 2 числа от 0 до 2 включительно")

    
def check_lines(m):
    winner = False
    central_elem = m[2][2]
    if central_elem != '-':
        if [m[i][i] for i in range(1,4)].count(central_elem)==3 :
            winner = True
    if not winner :
         for i in range(1,4):
            first_elem = m[i][1]
            if first_elem !='-':
                if m[i][1:].count(m[i][1])==3 :
                    winner = True
                    break
            
    return winner  


def no_more_moves(m):
    if [m[i][j] for i in range(1,4) for j in range(1,4)].count('-') == 0 :
        return True
    else:
        return False

    
def make_move(m, t):
    interrupt=False
    cell=""
    if t=='x': team_f = "крестики"
    else: team_f = "нолики"
    L=[0, 0]
    while True: 
        result = True 
        value = input(f"команда {team_f} введите координаты через пробел, q для выхода ")
        if value == "q": 
            print("игра прервана")
            interrupt = True
            break
            
        try: 
            L = list(map(int,value.split())) 
        except:print_error(); result = False
    
        if not result: continue
        if len(L)!=2: 
            print_error(); result = False
        else:
            try: cell = matrix[L[1]+1][L[0]+1]
            except IndexError: print_error; result = False
            except: print("что-то пошло не так");result = False
        if not result: continue
        if cell !="-" :
            print("клетка занята, выберите другой ход")
            result = False
        if result : break
    
    m[L[1]+1][L[0]+1] = t
    
    print_matrix(m)
    #print_matrix(rotate_matrix(m))
    return interrupt


while True:
    
    marker = not marker 
    if make_move(matrix, team[int(marker)]) : break
    res = [check_lines(matrix),check_lines(rotate_matrix(matrix))]
    
    if any(res):
        print(f"Игра закончена, выиграли {team[int(marker)]}")
        break
    
    if no_more_moves(matrix):
        print("больше ходов нет, ничья")
        break