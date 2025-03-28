import re, random

class ValidadorTelefone:
    @staticmethod
    def validar(numero: str) -> bool:
        return bool(re.match(r'^(\(\d{2}\)\s?)?[2-9]\d{4}-\d{4}$', numero))

    @classmethod
    def gerar_telefones(cls, quantidade: int, validos: bool = True) -> list:
        return [
            f"({random.choice(('11', '21', '31', '41', '51', '61'))}) {random.randint(2000, 9999)}-{random.randint(1000, 9999)}"
            if validos else f"({random.randint(1, 99)}) {random.randint(1000, 9999)}-{random.randint(100, 999)}"
            for _ in range(quantidade)
        ]

def validador():
    opcoes = {
        "1": lambda: print(f"O número é {'válido' if ValidadorTelefone.validar(input('Digite o telefone: ')) else 'inválido'}"),
        "2": lambda: print("\nNúmeros válidos gerados:\n" + "\n".join(f"- {t}" for t in ValidadorTelefone.gerar_telefones(3, True))),
        "3": lambda: print("\nNúmeros inválidos gerados:\n" + "\n".join(f"- {t}" for t in ValidadorTelefone.gerar_telefones(3, False)))
    }

    while (opcao := input("\n=== VALIDADOR DE TELEFONE 📲 ===\n1. Validar um número\n2. Gerar 3 números válidos\n3. Gerar 3 números inválidos\n4. Sair\n\nEscolha uma opção: ")) != "4":
        opcoes.get(opcao, lambda: print("Opção inválida, tente novamente."))()
        input("\nPressione Enter para continuar...")

    print("\nSaindo... 🚪")

if __name__ == "__main__":
    validador()
