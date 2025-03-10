from eta_lab.src.phonebook import Phonebook


class TestPhonebook:

    def test_add_sucesso(self):
        # Setup
        phonebook = Phonebook()
        # Chamada
        assert phonebook.add("Jeferson", "12345") == "Numero adicionado"
        # Avaliação
        assert "Jeferson" in phonebook.entries
        assert phonebook.entries["Jeferson"] == "12345"

    def test_add_nome_ja_existente(self):
        # Setup
        phonebook = Phonebook()
        # Chamada
        phonebook.add("Jeferson", "12345")
        # Avaliação
        assert phonebook.add("Jeferson", "67890") == "Nome já existente"

    def test_lookup_sucesso(self):
        # Setup
        phonebook = Phonebook()
        # Chamada
        phonebook.add("Jeferson", "12345")
        # Avaliação
        assert phonebook.lookup("Jeferson") == "12345"

    def test_lookup_falha(self):
        # Setup
        phonebook = Phonebook()
        assert phonebook.lookup("Bob") == "Nome não encontrado"

    def test_change_number_sucesso(self):
        # Setup
        phonebook = Phonebook()
        # Chamada
        phonebook.add("Jeferson", "12345")
        # Avaliação
        assert phonebook.change_number("Jeferson", "67890") == "Numero atualizado"
        assert phonebook.entries["Jeferson"] == "67890"

    def test_change_number_nome_inexistente(self):
        # Setup
        phonebook = Phonebook()
        # Avaliação
        assert phonebook.change_number("Bob", "67890") == "Nome não encontrado"

    def test_change_number_numero_invalido(self):
        # Setup
        phonebook = Phonebook()
        # Chamada
        phonebook.add("Jeferson", "12345")
        # Avaliação
        assert phonebook.change_number("Jeferson", "abcd") == "Numero invalido"

    def test_get_name_by_number_sucesso(self):
        # Setup
        phonebook = Phonebook()
        # Chamada
        phonebook.add("Jeferson", "12345")
        # Avaliação
        assert phonebook.get_name_by_number("12345") == "Jeferson"

    def test_get_name_by_number_falha(self):
        # Setup
        phonebook = Phonebook()
        # Chamada
        phonebook.add("Jeferson", "12345")
        # Avaliação
        assert phonebook.get_name_by_number("67890") == "Numero não encontrado"
