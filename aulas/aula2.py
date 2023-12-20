# Para modificar os separadores, usa-se sep="", como por exemplo sep="-"
# Com o tracinho selecionado como separador, o print vai printar o código abaixo
# Como 12-34  
print(12, 34, sep="-")
# Para usar quebras de linha, usa-se CRLF, \r\n -> CRLF
# \n mac, linux, windows mais atuais -> LF
# Por padrão, sempre vai se executar \n no final de cada print
# Para mudar isto, basta adicionar o argumento end="" e mudar, como por exemplo 
print("Estou quebrando linhas!", "Este print está separado por um traço", sep="-", end="@@@")
print("Este texto está na linha de baixo do código,", "mas está exibindo na mesma linha!", sep=" ")
