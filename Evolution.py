from matplotlib import image
from matplotlib import pyplot
import matplotlib.patches as patches
import numpy as np
import random
import math as m

"Matplot Lib Import image in an array fromate so no need to convert in numpy array"
"                                       Inititalizing Start"
"Optimize Fitesss if both parents have corelation less than 0.3 discard them"
small_img = image.imread('boothiGray.jpg')
large_img = image.imread('groupGray.jpg')
max_threshold=0.9
inital_size=50
fitness=[]
binary_cross=[]
h,w=small_img.shape
fig,ax = pyplot.subplots(1)
ax.imshow(large_img)
"                                           Initializing End"
def coreelation_function(real_img,crop_img):
    
    a=np.array(list(np.concatenate(real_img).flat))
    b=np.array(list(np.concatenate(crop_img).flat))
    k=sum(a)/len(a)
    l=sum(b)/len(b) 
    l1=np.array(a-k)
    l2=np.array(b-l)
    l3=np.array(l1*l2)
    l4=np.array(l1*l1)
    l5=np.array(l2*l2)
    n=sum(l3)
    d=sum(l4)*sum(l5)
    result=n/m.sqrt(d)
   
    return(result)

 
def binary_to_decimal(binary): 
    decimal = 0 
    #binary = list(str(binary)) #convert binary to a list 
    binary = binary[::-1]      #reverse the list 
    power = 0   #declare power variable (for 1st elem == 0) 
    for number in binary: 
        if number == '1': 
            decimal += 2**power     
        power += 1 #increase power by 1    
    return decimal 


"Setting Intital Population"
"Slices And Correlation Computation"

def initial_population(small_img,large_img):
    for i in range(0,inital_size):
        x=(np.random.randint(0,(995)))
        y=(np.random.randint(0,(447)))
            
        crop_img = large_img[y:y+h, x:x+w]
        z=coreelation_function(small_img,crop_img)
        # print(x,y)
        fitness.append((x,y,z))
        if(z>=max_threshold):
            rect = patches.Rectangle((x,y),35,29,linewidth=2,edgecolor='r',facecolor='none')
            ax.set_title(("X=",x,"Y=",y,"Cor=",z))
            ax.add_patch(rect)
            pyplot.show()
            exit(0)

            
"Slices End"
def Selection(fitness):
    "Selective Sort"
    "Converting Dict Into Sorted List"
    "Converting List Into Binary List"
    after_sort=(sorted(fitness,key=lambda x:x[2],reverse=True))
    

    fitness.clear()
    binary_cross.clear()
    print(after_sort[0][2])
   

    for i in range(0,len(after_sort)):
        x,y,z=after_sort[i]
        x1=np.binary_repr(x,width=10)
        y1=np.binary_repr(y,width=10)
        binary_cross.append((x1+y1))
    after_sort.clear()
    
    for i in range(0,len(binary_cross),2):
        Cross_over(binary_cross[i],binary_cross[i+1])
    binary_cross.clear()
  
     
def Cross_over(parent1,parent2):
    "Cross Over"
    
    ran=np.random.randint(0,19)
    a=np.array(list(parent1))
    b=np.array(list(parent2))
 

    "Swap"
    a[ran:],b[ran:]=b[ran:],a[ran:]
    "Mutation"
    ran=np.random.randint(1,100)
    "First Half"
    if(ran<=20):
        ran=np.random.randint(0,19)
        if(a[ran]==0):
            a[ran]=1
        else:
            a[ran]=0
        if(b[ran]==0):
            b[ran]=1
        else:
            b[ran]=0
    "Mutation End"
    "Binary to Decimal"

    x1=binary_to_decimal(a[0:10])
    y1=binary_to_decimal(a[10:20])
    x2=binary_to_decimal(b[0:10])
    y2=binary_to_decimal(b[10:20])
    if(x1>=995 or x1==0 or x1==x2):
        x1=np.random.randint(0,995)
    if(x2>=995 or x2==0 or x1==x2):
        x2=np.random.randint(0,995)
    if(y1>=477 or y1==0 or y1==y2):
        y1=np.random.randint(0,477)
    if(y2>=477 or y2==0 or y1==y2):
        y2=np.random.randint(0,477)

    c1=large_img[y1:y1+h, x1:x1+w]
    c2=large_img[y2:y2+h, x2:x2+w]
    # print(x1,y1)
    # print(x2,y2)

    z1=coreelation_function(small_img,c1)
    if(z1>=max_threshold):
        rect = patches.Rectangle((x1,y1),35,29,linewidth=2,edgecolor='r',facecolor='none')
        ax.set_title(("X=",x1,"Y=",y1,"Cor=",z1))

        ax.add_patch(rect)
        pyplot.show()
        exit(0)
       
    z2=coreelation_function(small_img,c2)
    if( z2>=max_threshold):
        rect = patches.Rectangle((x2,y2),35,29,linewidth=2,edgecolor='r',facecolor='none')
        ax.set_title(("X=",x2,"Y=",y2,"Cor=",z2))
        ax.add_patch(rect)
        pyplot.show()
        exit(0)
    fitness.append((x1,y1,z1))
    fitness.append((x2,y2,z2))
    
    
    "Cross Over End"

initial_population(small_img,large_img)
while(True):
    Selection(fitness)