input_data = open('input.txt', 'r') 

N = input_data.read() 
#--------------------------------------------------------------------
N = int(N)
aut = N + 1


#--------------------------------------------------------------------
output_data = open('output.txt', 'w') # Открываем для записи (литера 'w') файл и кладем его в переменную
output_data.write(str(aut))


# Закрываем открытые ранее файлы!
input_data.close() 
output_data.close()