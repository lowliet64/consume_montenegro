import requests
import json
from requests.structures import CaseInsensitiveDict

url="http://api.montenegrolabs.com.br:82"

token ="NA.pOjnwareDbSMVpMjAHA-G9nfMfQyR-2g2CzzvaVSA_r4PH3BwuNvr5dx_1ME"
headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = f"Bearer {token}"

# resp = requests.post(url+"/v1/dominio/company/events/",headers=headers)

resp = requests.post(url+"/v1/dominio/employees",headers=headers)
print(resp.status_code)
print(resp.json())
f = open("emp_response2.json","w+",encoding='utf-8')
f.write(json.dumps(resp.json(),ensure_ascii=False))
f.close()



# g={
#     "name": "GLEYDSON DE AZEVEDO FERREIRA LIMA",
#     "employee_email": None,
#     "cpf": "01231423420",
#     "code": 154,
#     "office_name": "DIRETOR (A)",
#     "function_name": None,
#     "departament_name": "ADMINISTRACAO",
#     "cost_name": "GERAL",
#     "service_name": "SIG SOFTWARE & CONSULTORIA EM TECNOLOGIA",
#     "admission": "2011-03-22",
#     "vacation_expiration": "1900-01-01",
#     "pis": "13029873640",
#     "salary": 5839.45,
#     "time_type": 1,
#     "journey_name": None,
#     "sex": "M",
#     "pay_union_contribution": "N",
#     "birth_date": "1983-01-13",
#     "address": "DA LAGOSTA",
#     "address_number": 466,
#     "neighborhood": "PONTA NEGRA",
#     "county_name": "NATAL",
#     "uf_name": "RIO GRANDE DO NORTE",
#     "cep": "59090500",
#     "country_name": "BRASIL",
#     "rg_number": "1738478",
#     "rg_dispatch_agency_number": 1,
#     "rg_uf_dispatch_number": "RN",
#     "rg_dispatch_date": None,
#     "professional_card": None,
#     "professional_card_series": None,
#     }


# g2= {
#             "name": "GLEYDSON DE AZEVEDO FERREIRA LIMA",
#             "employee_email": None,
#             "cpf": "01231423420",
#             "code": 154,
#             "office_name": "DIRETOR (A)",
#             "function_name": None,
#             "departament_name": "ADMINISTRACAO",
#             "cost_name": "GERAL",
#             "service_name": "SIG SOFTWARE & CONSULTORIA EM TECNOLOGIA",
#             "admission": "2011-03-22",
#             "vacation_expiration": "1900-01-01",
#             "pis": "13029873640",
#             "salary": 5839.45,
#             "time_type": 1,
#             "journey_name": None,
#             "sex": "M",
#             "pay_union_contribution": "N",
#             "birth_date": "1983-01-13",
#             "address": "DA LAGOSTA",
#             "address_number": 466,
#             "neighborhood": "PONTA NEGRA",
#             "county_name": "NATAL",
#             "uf_name": "RIO GRANDE DO NORTE",
#             "cep": "59090500",
#             "country_name": "BRASIL",
#             "rg_number": "1738478",
#             "rg_dispatch_agency_number": 1,
#             "rg_uf_dispatch_number": "RN",
#             "rg_dispatch_date": None,
#             "professional_card": None,
#             "professional_card_series": None
#         }


# print(g==g2)