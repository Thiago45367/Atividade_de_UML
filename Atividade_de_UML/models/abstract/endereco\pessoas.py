import os
from models.enums.unidade_federativa import UnidadeFederativa
from abc import ABC, abstractclassmethod


class Endereco():
    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: str, ufnome: str, ufsigla: str) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade
        self.ufnome = ufnome
        self.ufsigla = ufsigla

    def __str__(self) -> str:
        f"\nLogradouro: {self.logradouro} \nNúmero: {self.numero} \nComplemento: {self.complemento} \nCEP: {self.cep} \nCidade: {self.cidade} \nUfnome: {self.ufnome} \nUfsigla: {self.ufsigla}"

class Pessoas(ABC):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def __str__(self) -> str:
        f"\nNome: {self.nome} \nTelefone: {self.telefone} \nEmail: {self.email} \nEndereco: {self.endereco}"            