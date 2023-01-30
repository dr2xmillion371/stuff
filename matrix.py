import moviepy.editor as me
import numpy as np
from bm_analyze import *
import time
t=open('!r_data.txt')
M=t.read().split('\n')
t.close()
del t
M[0]='[empty]'
start=36000
end=37000
speed=16
time.sleep(120)
render=me.VideoClip(lambda t:np.zeros([1080,1920,3]),duration=(end-start)/speed)#+3*(q+1==k))
clips=[render]
print('Finished making a void')
def parseMatrix(M):
    if M=='[empty]':return []
    if M=='Limit':return [[1]]
    return eval("[" + M.replace(")(", "],[").replace("(", "[").replace(")", "]").replace("?","") + "]")
for i in range(start,end):
    a=''
    k=0
    for j in M[i]:
        a+=j
        k+=1
        if k>=100 and j==')':a+='\n';k=0
    obj=me.TextClip(a.replace('(0)(2)','Limit of BMS'),size=(1920,500),color='white',fontsize=25,method='label',align='northwest')
    clips.append(obj.set_start((i-start)/speed).set_duration(1/speed).set_pos((10,100)))
    if parseMatrix(M[i])<[[0],[1,1,1],[2,1,1],[3,1,1],[2,1,1],[3,1],[2]]:
        obj=me.TextClip(prettyprint(toexp(matfromstr(M[i])[0])),size=(1920,600),color='white',fontsize=30,method='label',align='west',font='Courier-New')
        clips.append(obj.set_start((i-start)/speed).set_duration(1/speed).set_pos((10,500)))
    obj=me.TextClip('Frame {:,}\n≈ {}h {:02}m spent calculating'.format(i,i//6660,i//111%60),size=(1920,500),color='white',fontsize=20,method='label',align='northwest')
    clips.append(obj.set_start((i-start)/speed).set_duration(1/speed).set_pos((10,20)))
    if i%100==0:
        print(i,M[i])
        # render=me.CompositeVideoClip(clips)
        # clips=[render]
    if i%10==0 and i%100!=0:
        print(i)

print('Finished creating text')
render=me.CompositeVideoClip(clips)
del clips
print('Finished adding text to the void')
render_=me.VideoFileClip('BMSlngi.mp4')
me.concatenate([render_,render]).write_videofile(f'BMSlngi_.mp4',fps=24)
del render
del render_
