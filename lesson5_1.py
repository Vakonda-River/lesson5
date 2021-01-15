file_name = input('file: ')
fn = open(file_name,'w', encoding="utf-8")
while True:
     a = input()
     if a == '':
         break
     fn.write(a + '\n')
fn.close()


