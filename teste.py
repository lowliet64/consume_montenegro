import json
from tokenize import group


with open('rub_response.json','r',encoding="utf-8") as file:
    data = file.read()
    funcs_primary=json.loads(data)['result']

with open('rub_response2.json','r',encoding="utf-8") as file:
    data = file.read()
    funcs_secondary=json.loads(data)['result']
    print(type(funcs_secondary))


result_list=[]

flag=""
if funcs_primary[0].get('cpf'):
    flag="emp"
else:
    flag="rub"

print(flag)
file_key = open('keys.json','r+')
file_key= json.loads(file_key.read())
for emp in funcs_primary:
    action='delete'
    for emp_sec in funcs_secondary:
        if(str(emp.get("company_code")) == str(emp_sec.get("company_code"))):
            action='update'
            break
        
def generate_diff_list(new_list,old_list):
    indexes_old=[str(item.get("company_code")) for item in old_list]
    indexes_new=[str(item.get("company_code")) for item in new_list]
    file_key = open('keys.json','r+')
    file_key= json.loads(file_key.read())
    for item in new_list:
        if str(item.get("company_code")) not in indexes_old: 
            item['action']='create'
        else:
            old_item = old_list[indexes_old.index(str(item.get("company_code")))]
            if(has_changed(old_item,item)):
              
              
                item['action']='update'
                translate_object(file_key,item)
            else:
               
                item['action']='do_nothing'
                translate_object(file_key,item)

    for old_item in old_list:
        if str(old_item.get('company_code')) not in indexes_new:
            
            old_item['action']='delete'
            new_list.append(old_item)
            translate_object(file_key,old_item)
            
           
        else:
            
            translate_object(file_key,old_item)
            old_item['action']='do_nothing'
    return new_list,old_list
        
#verifica se tem diferença entre os dictionarys
def has_changed(old_item,new_item):
    return old_item != new_item
        

def translate_object(file_key,obj):
    list_keys = file_key
    for key in list_keys:
        if obj.get(key):
            obj[list_keys[key]]=obj.get(key)
            del obj[key]
   
teste ={"code":"2"}


def transform_employees_list(employee_list):
    companies_codes=[]
    companies=[]

    for employee in employee_list:
        if employee.get('company_code') in companies_codes:
            companies[companies_codes.index(employee.get('company_code'))]['empregado'].append(
                employee
            )
        else:
            print("companhia ainda n existe , bora criar")
            company = {
                "codigo":employee.get('company_code'),
                "nome":employee.get('company_name'),
                "status":employee.get('company_status'),
                "inscricao":employee.get('company_cnpj'),
                "empregado":[]
            }
            companies_codes.append(employee.get('company_code'))
            companies.append(company)
    print(companies_codes)
    return companies

def transform_rub_list(rubric_list):
    for rubric_group in rubric_list:
        if rubric_group.get('grupo_rubrica'):
            print("making this")
            translate_object(file_key,rubric_group['grupo_rubrica'])
           
            for rubric in rubric_group['grupo_rubrica']['rubricas']:
                del rubric['company_code']
                translate_object(file_key,rubric)
    
    
    return rubric_list

a,b = generate_diff_list(funcs_secondary,funcs_primary)

f = open("file_response.json","w+",encoding='utf-8')
f.write(json.dumps(a,ensure_ascii=False))
f.close()

#final_response="dont worry child"
final_response = transform_rub_list(a)
b = open("final_response.json","w+",encoding='utf-8')
b.write(json.dumps(final_response,ensure_ascii=False))
b.close()

