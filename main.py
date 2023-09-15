pessoas ={
  'id0001':{'nome':'João','idade':'39', 'profissão':'medico'},
    'id0002':{'nome':'Paula','idade':'40', 'profissão':'TI'},
  'id0003':{'nome':'Cristina','idade':'50', 'profissão':'Geografo'},
}


print(f"{'Nome':^10} | {'Idade':^6} | {'Profissão':^12}")
print(f"{'-'*10} | {'-'*6} | {'-'*12}")

for registro in pessoas.values():
  print(f"{registro['nome']:<10} | {registro['idade']:6} | {registro['profissão']:>12}")
