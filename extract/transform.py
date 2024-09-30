from get import req_by_ingredients,apikey,get_reci_info
import json
D=req_by_ingredients(['milk','eggs'],2,apikey)

def clean_by_ingredients(data) :   #recieves from req_by_ingredients
    F=[]
    for reciep in data:
        dic={}
        dic['reciep']=reciep['title']
        dic['reciep_id']=reciep['id']
        dic['img']=reciep['image']
        F.append(dic)
    return F
def get_reciept_ingredients(data): #recieves from get_reci_info
    steps=data['instructions']
    reciept=data['title']
    ingred=data['extendedIngredients']
    ing=[x['original'] for x in ingred]
    id=data['id']
    dic={'name':reciept ,'id':id, 'ingredients':ing,'steps':steps}
    
    return dic
dat=get_reciept_ingredients(get_reci_info(991625,apikey))
with open('nenwfl.json','w') as json_file:
    json.dump(dat,json_file,indent=4)



