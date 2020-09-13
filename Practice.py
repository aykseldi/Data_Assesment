post_to_boxes = {11111: [(10, 20, 15, 25)],
149321: [(34, 10, 215, 104),
(14, 42, 503, 545),(22, 5, 312, 590)],
109334: [],
384121: [(10, 20, 100, 300)]
}


empty_keys=[]
small_keys=[]


def delete_empty_box(a):
    
    for k,v in a.items():
        if not v:
            empty_keys.append(k) 
        
    for k in empty_keys:
        del a[k]
        
def delete_small_box(a):
    for key,v in a.items():
        if ((a[key][0][2]-a[key][0][0] )* (a[key][0][3] - a[key][0][1])) < 256:
            small_keys.append(key) 
        
    for k in small_keys:
        del a[k]        
  
          

#print(len(a))
def process_hero_box_annotations(a):
    
        
    for key in a:
      
        if len(a[key]) > 1:
            print(len(a[key]))
            
            #print(len(a[key]))
            temp0=[]
            temp1=[]
            temp2=[]
            temp3=[]
            for i in range(len(a[key])):
                temp0.append(a[key][i][0])
                temp1.append(a[key][i][1])
                temp2.append(a[key][i][2])
                temp3.append(a[key][i][3])
            result1=[min(temp0),min(temp1),max(temp2),max(temp3)]
            a[key]=result1
      
    return a    

    
delete_empty_box(post_to_boxes) 
delete_small_box(post_to_boxes)       
result = process_hero_box_annotations(post_to_boxes)  

    
                
        
            
            
       


