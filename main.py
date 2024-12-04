from eta_lab.src.phonebook import Phonebook

def main():
    phonebook = Phonebook()

    while True:
        print("\nBem-vindo à Agenda Telefônica!")
        print("1. Adicionar número")
        print("2. Buscar número por nome")
        print("3. Listar todos os nomes")
        print("4. Listar todos os números")
        print("5. Pesquisar nomes")
        print("6. Alterar número")
        print("7. Buscar nome pelo número")
        print("8. Listar agenda ordenada")
        print("9. Listar agenda em ordem reversa")
        print("10. Excluir número")
        print("11. Excluir agenda")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome: ")
            numero = input("Digite o número: ")
            resultado = phonebook.add(nome, numero)
            print(resultado)

        elif opcao == "2":
            nome = input("Digite o nome a buscar: ")
            resultado = phonebook.lookup(nome)
            print(f"Resultado: {resultado}")

        elif opcao == "3":
            nomes = phonebook.get_names()
            print(f"Nomes na agenda: {nomes}")

        elif opcao == "4":
            numeros = phonebook.get_numbers()
            print(f"Números na agenda: {numeros}")

        elif opcao == "5":
            pesquisa = input("Digite o nome ou parte do nome para pesquisar: ")
            resultados = phonebook.search(pesquisa)
            if resultados:
                print("Resultados encontrados:")
                for item in resultados:
                    print(item)
            else:
                print("Nenhum resultado encontrado.")

        elif opcao == "6":
            nome = input("Digite o nome: ")
            numero = input("Digite o novo número: ")
            resultado = phonebook.change_number(nome, numero)
            print(resultado)

        elif opcao == "7":
            numero = input("Digite o número a buscar: ")
            resultado = phonebook.get_name_by_number(numero)
            print(f"Resultado: {resultado}")

        elif opcao == "8":
            sorted_phonebook = phonebook.get_phonebook_sorted()
            print("Agenda ordenada:")
            for nome, numero in sorted_phonebook.items():
                print(f"{nome}: {numero}")

        elif opcao == "9":
            reverse_phonebook = phonebook.get_phonebook_reverse()
            print("Agenda em ordem reversa:")
            for nome, numero in reverse_phonebook.items():
                print(f"{nome}: {numero}")

        elif opcao == "10":
            nome = input("Digite o nome para excluir: ")
            resultado = phonebook.delete(nome)
            print(resultado)

        elif opcao == "11":
            resultado = phonebook.clear()
            print(resultado)

        elif opcao == "0":
            print("Até mais!")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
