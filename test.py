# Napišite program, ki izpiše praštevila do 200

print(2)
print(3)

for i in range(4, 200):
    je_prastevilo = True
    for mozni_delitelj in range (2,i): # dovolj je, da gremo do vključno korena
        if i % mozni_delitelj == 0:
            je_prastevilo = False
            # break ... ga ne rabimo, ker če je false, ne naredimo nič

    if je_prastevilo:
        print(i)