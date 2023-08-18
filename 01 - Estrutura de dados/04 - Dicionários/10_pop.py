contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.pop("guilherme@gmail.com")  # {'nome': 'Guilherme', 'telefone': '3333-2221'}
print(resultado)                                # Remove mas retorna o valor removido

resultado = contatos.pop("guilherme@gmail.com", {})  # {}
print(resultado)                            # Informa o valor padrão '{}' para ser retornado sem erro.
