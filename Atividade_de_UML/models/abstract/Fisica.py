import os
from models.enums.genero import Genero
from meto

class Fisica(Pessoas, ABC):
    def __init__(self, cpf: str, rg: str, dataNascimento: str, sexo: Sexo) -> None:
         self.cpf = cpf
         self.rg = rg
         self.dataNacimento = dataNascimento
         self.sexo = Genero

    def __str__(self) -> str:
          f"\nCPF: {self.cpf} \nRG: {self.rg} \nDataNascimento: {self.dataNacimento} \nSexo: {self.sexo}"      