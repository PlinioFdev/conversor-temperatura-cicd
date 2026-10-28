# Conversor de Temperatura

Projeto da atividade da Aula 07 (Cultura e Prática DevOps - UNIPÊ). Mini-app em Python
que converte temperatura entre Celsius, Fahrenheit e Kelvin, usada para demonstrar uma
pipeline de CI/CD com GitHub Actions.

## O que é

`src/conversor.py` tem funções de conversão (`celsius_para_fahrenheit`,
`fahrenheit_para_celsius`, `celsius_para_kelvin`, `kelvin_para_celsius`) e uma função
genérica `converter(valor, origem, destino)` que aceita `"C"`, `"F"` ou `"K"`.

## Como rodar

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

python3 -m src.conversor      # roda o exemplo em __main__
pytest                        # roda os testes
```

## Como funciona a pipeline

O workflow em `.github/workflows/ci-cd.yml` roda a cada push/pull request em `main` e
`develop`, usando Python 3.12, com 3 jobs em sequência (cada um depende do anterior via
`needs`):

1. **build**: instala as dependências (`pip install -r requirements.txt`) e valida que
   o código compila sem erro (`python -m compileall src`). Guarda `src/` como artefato
   (`codigo-fonte`).
2. **test**: depende do `build`; instala as dependências de novo (job roda em runner
   limpo) e executa `python -m pytest`.
3. **deploy**: depende do `test`; só roda na branch `main`
   (`if: github.ref == 'refs/heads/main'`). Simula a publicação com `echo`, usando a
   variável de ambiente `AMBIENTE_DEPLOY` (sem valor sensível) só pra ilustrar onde um
   secret real entraria.

## Estrutura

```
src/conversor.py        # lógica de conversão
tests/test_conversor.py # testes pytest
.github/workflows/      # pipeline CI/CD
```
