#start
import time

def buchholz_ocf():
    buchholzList=['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','w',
    'w+1','w+2','w+3','w+4','w+5','w+6','w+7','w+8','w+9','w+10','w+11','w*2', '(w*2)+1','(w*2)+2','(w*2)+3']
    for i in buchholzList:
        print(i)
        time.sleep(0.04347826086)
        
        
buchholz_ocf()

#end
