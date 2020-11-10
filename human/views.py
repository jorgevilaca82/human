from typing import Any, Dict, Optional
from django.views.generic import TemplateView
import enum

class Pessoa:

    class Genero(enum.Enum):
        MASCULINO = "M"
        FEMININO = "F"
        INDEFINIDO = "I"

    def __init__(self, nome: str, sexo: Genero) -> None:
        self.nome = nome
        self.sexo = sexo

    def eh_masculino(self) -> Optional[bool]:
        if self.sexo not in (self.Genero.MASCULINO, self.Genero.FEMININO):
            return None
        return self.sexo == self.Genero.MASCULINO


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:

        pessoa = Pessoa("Lindomar", Pessoa.Genero.INDEFINIDO)

        return {
            "pessoa": pessoa
        }
