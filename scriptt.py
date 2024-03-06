#!/bin/python3
import subprocess
import os

comando = 'find pass*.txt'
processo = subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, erro = processo.communicate()

output_filename = '/tmp/password_discovery.txt'

if processo.returncode == 0:
    resultados = output.decode('utf-8').split('\n')  # Divide os resultados em uma lista

    with open(output_filename, 'w') as output_file:
        for resultado in resultados:
            resultado = resultado.strip()  # Remove espaços em branco extras
            if resultado:
                print(resultado)
                output_file.write(resultado + '\n')

                cat_processo = subprocess.Popen(['cat', resultado], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                cat_output, cat_erro = cat_processo.communicate()

                if cat_processo.returncode == 0:
                    cat_output_str = cat_output.decode('utf-8')
                    print(cat_output_str)
                    output_file.write(cat_output_str + '\n')
                else:
                    cat_erro_str = cat_erro.decode('utf-8')
                    print(f"Erro ao executar 'cat {resultado}': {cat_erro_str}")
                    output_file.write(f"Erro ao executar 'cat {resultado}': {cat_erro_str}\n")

    print(f"Resultados salvos em {output_filename}")
else:
    print("Nada encontrado")
