def verificar_link(link):
    if "bit.ly" in link or "tinyurl" in link:
        return "⚠️ Link encurtado. Cuidado!"
    elif "@" in link or "//" in link[8:]:
        return "⚠️ Pode ser um redirecionamento perigoso!"
    elif link.startswith("http://"):
        return "⚠️ Site sem HTTPS!"
    return "✅ Link parece seguro."

link = input("Cole o link para verificar: ")
print(verificar_link(link))
