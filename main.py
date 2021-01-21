with open('31.txt') as fo:
        op = ''
        read = 0
        count = 1
        page = 1
        for x in fo.read().split("\n"):
            if(x=="             INDIRA GANDHI NATIONAL OPEN UNIVERSITY             PAGE :   " + str(page)):
                 page+=1
                 if(read==1):
                   with open(str(count) + '.txt','w') as opf:
                      opf.write(op)
                      opf.close()
                      op = ''
                      count+=1
                      read = 0
                 if(read==0):
                      op = op + '\n' + x
                      read = 1

            else:
                op = op + '\n' + x


        fo.close()
'''
if(x=="**********"):
                if(read==1):
                   with open(str(count) + '.txt','w') as opf:
                      opf.write(op)
                      opf.close()
                      op = ''
                      count+=1
                else:
                   read = 1
            else:
                op = op + '\n' + x
'''
