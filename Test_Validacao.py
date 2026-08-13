import pytest
from Validacao import validar_senha


@pytest.mark.parametrize(
    "senha_valida",
    [
        "Senha@123",
        "123456_A@",
        "L0ngP@ssword#",
        "A1#12345",
    ],
)
def test_validar_senha_sucesso(senha_valida):
    try:
        validar_senha(senha_valida)
    except ValueError:
        pytest.fail(
            f"A senha '{senha_valida}' é válida, mas a validação falhou!"
        )


def test_senha_curta():
    with pytest.raises(ValueError) as exc_info:
        validar_senha("A1#4567")

    assert "A senha deve ter no mínimo 8 caracteres" in str(exc_info.value)


def test_senha_sem_maiuscula():
    with pytest.raises(ValueError) as exc_info:
        validar_senha("senha@123")

    assert "A senha deve conter pelo menos uma letra maiúscula" in str(
        exc_info.value
    )


def test_senha_sem_numero():
    with pytest.raises(ValueError) as exc_info:
        validar_senha("SenhaComSimbol@")

    assert "A senha deve conter pelo menos um número" in str(exc_info.value)


def test_senha_sem_simbolo_permitido():
    with pytest.raises(ValueError) as exc_info:
        validar_senha("Senha12345")

    assert "A senha deve conter pelo menos um dos símbolos: _, # ou @" in str(
        exc_info.value
    )


def test_senha_com_multiplos_erros():
    with pytest.raises(ValueError) as exc_info:
        validar_senha("abc")

    mensagem = str(exc_info.value)

    assert "A senha deve ter no mínimo 8 caracteres" in mensagem
    assert "A senha deve conter pelo menos uma letra maiúscula" in mensagem
    assert "A senha deve conter pelo menos um número" in mensagem
    assert (
        "A senha deve conter pelo menos um dos símbolos: _, # ou @" in mensagem
    )