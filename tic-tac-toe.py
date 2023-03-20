
def check_for_winner(ar):

    length = len(ar)
    diag_1 = None
    diag_2 = None
    k = length-1
    for i in range(0,length):
        row_matched = None
        column_matched = None

        print("Start new comparison ##############")

        for j in range(0,length-1):
            print("Compare rows[i:j]["+str(i)+":"+str(j)+"]" +" > "+str(ar[i][j])+":"+str(ar[i][j+1]))

            # Compare rows
            if(ar[i][j]!=ar[i][j+1]):
                print("row not matched")
                row_matched = False
            elif(ar[i][j]==ar[i][j+1] and (row_matched is None or row_matched) and (j+1)==length-1):
                print("Row matched")
                row_matched = True

            #Compare columns
            print("Compare columns [i:j]["+str(i)+":"+str(j)+"]" +" > "+str(ar[j][i])+":"+str(ar[j+1][i]))

            if(ar[j][i]!=ar[j+1][i]):
                print("column not matched")
                column_matched = False
            elif(ar[j][i]==ar[j+1][i] and (column_matched is None or column_matched) and (j+1)==length-1):
                print("column_matched")
                column_matched = True


            #Diagonal 1            
            if(i==j):
                if(ar[i][j]!=ar[i+1][j+1]):
                    diag_1 = False
                elif (ar[i][j]==ar[i+1][j+1] and (diag_1 is None or diag_1) and (i+1)==length-1 and (j+1)==length-1):
                    diag_1 = True

            #Diagonal 2
            if(i==length-1): # Last row
                #Write a separate logic 
                if(ar[k][j]!=ar[k-1][j+1]):
                    diag_2 = False
                elif(ar[k][j]==ar[k-1][j+1] and (diag_2 is None or diag_2) and (j+1)==length-1):
                    diag_2 = True

                k-=1

        if(row_matched):
            print("Won the game row no. "+str(i))
            break
        elif(column_matched):
            print("Won the game col no. "+str(i))
            break

    if(diag_1):
        print("Won the game Digonal 1")  

    if(diag_2):
        print("Won the Diagonal 2")  


if __name__ == '__main__':
    #ar = [[1,1,1],[0,-1,-1],[0,0,0]] # row 0
    #ar = [[0,1,0],[-1,-1,-1],[0,1,0]] # row 1
    #ar = [[0,0,-1],[1,1,-1],[0,0,-1]] # col 2

    #ar = [[-1,1,0],[0,1,0],[0,1,-1]]
    #ar = [[1,-1,0],[0,1,0],[0,-1,1]] # diagonal 1
    #ar = [[-1,0,1],[0,1,0],[1,0,-1]] # digonal 2
    #ar = [[0,1,0,1],[-1,-1,-1,-1],[0,1,1,0],[0,1,0,1]] # 4D row 
    ar = [[0,-1,1,-1],[0,-1,1,0],[-1,-1,1,-1],[0,0,1,0]] # 4D column 

    check_for_winner(ar)
