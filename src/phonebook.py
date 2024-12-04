class Phonebook:
    def __init__(self):
        # Inicializa a agenda com uma entrada padrão.
        self.entries = {'POLICIA': '190'}

    def add(self, name, number):
        """
        :param name: name of person in string
        :param number: number of person in string
        :return: 'Nome invalido' or 'Numero invalido' or 'Numero adicionado'
        Alterações:
        - **Correção de Bug**: Validação incorreta para nomes e números corrigida.
        - **Melhoria**: Adicionado retorno de mensagem caso o nome já exista.
        """
        if not isinstance(name, str) or not name.isalpha():
            return 'Nome invalido'

        if not number.isdigit():
            return 'Numero invalido'

        if name in self.entries:
            return 'Nome já existente'

        self.entries[name] = number
        return 'Numero adicionado'

    def lookup(self, name):
        """
        :param name: name of person in string
        :return: return number of person with name
        Alterações:
        - **Correção de Bug**: Verificação direta do nome adicionada.
        """
        if name in self.entries:
            return self.entries[name]
        return 'Nome não encontrado'

    def get_names(self):
        """
        :return: return all names in phonebook
        """
        return list(self.entries.keys())

    def get_numbers(self):
        """
        :return: return all numbers in phonebook
        """
        return list(self.entries.values())

    def clear(self):
        """
        Clear all phonebook
        :return: return 'phonebook limpado'
        """
        self.entries.clear()
        return 'phonebook limpado'

    def search(self, search_name):
        """
        Search all substring with search_name
        :param search_name: string with name for search
        :return: return list with results of search
        Alterações:
        - **Melhoria**: Adicionada verificação para tipos inválidos no parâmetro `search_name`.
        - **Correção de Bug**: Resultado corrigido para retornar uma lista de dicionários `{nome: numero}` em vez de `set`.
        """
        if not isinstance(search_name, str):
            return 'Parametro invalido'

        results = [{name: number} for name, number in self.entries.items() if search_name in name]
        return results

    def get_phonebook_sorted(self):
        """
       :return: return phonebook in sorted order
        Alterações:
        - **Melhoria**: Método implementado para retornar a agenda ordenada usando `sorted`.
        """
        return dict(sorted(self.entries.items()))

    def get_phonebook_reverse(self):
        """
        :return: return phonebook in reverse sorted order
        Alterações:
        - **Melhoria**: Método implementado para retornar a agenda em ordem reversa usando `sorted` com `reverse=True`.
        """
        return dict(sorted(self.entries.items(), reverse=True))

    def delete(self, name):
        """
         Delete person with name
        :param name: String with name
        :return: return 'Numero deletado'
        Alterações:
        - **Correção de Bug**: Agora verifica se o nome existe antes de tentar deletar, evitando exceções.
        """
        if name in self.entries:
            del self.entries[name]
            return 'Numero deletado'
        return 'Nome não encontrado'

    def change_number(self, name, number):
        """
        Altera o número associado a um nome.
        Alterações:
        - **Novo Método**: Implementado com base no TDD.
        - **Melhoria**: Validações adicionadas para nome e número.
        """
        if name in self.entries:
            if number.isdigit():
                self.entries[name] = number
                return 'Numero atualizado'
            return 'Numero invalido'
        return 'Nome não encontrado'

    def get_name_by_number(self, number):
        """
        Busca o nome associado a um número.
        Alterações:
        - **Novo Método**: Implementado com base no TDD.
        - **Melhoria**: Busca o nome de forma eficiente com validação adicional para o número.
        """
        for name, num in self.entries.items():
            if num == number:
                return name
        return 'Numero não encontrado'
