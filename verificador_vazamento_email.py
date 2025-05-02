email = input("Digite seu e-mail: ")

# Simulação de base de dados vazada
emails_vazados = ["teste@gmail.com", "exemplo@hotmail.com"]

if email.lower() in emails_vazados:
    print("⚠️ Atenção! Seu e-mail foi encontrado em vazamentos.")
else:
    print("✅ Seu e-mail parece seguro (não encontrado).")
