#!/usr/bin/env python3
"""Verifica ligações entre rascunho, catálogo e bibliografia. Não certifica fatos."""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
errors: list[str] = []

def check(condition: bool, label: str):
    if not condition:
        errors.append(label)

def main():
    fontes = json.loads((ROOT / "pesquisa/fontes/liberalismo.json").read_text(encoding="utf-8"))
    catalogo = json.loads((ROOT / "catalogo/catalogo.json").read_text(encoding="utf-8"))
    conteudo = (ROOT / "verbetes/ideologias/liberalismo.md").read_text(encoding="utf-8")
    ficha = (ROOT / "pesquisa/fichamentos/liberalismo.md").read_text(encoding="utf-8")
    check(fontes.get("verbete_id") == "liberalismo", "Fonte não corresponde a verbete")
    entradas = [e for e in catalogo["entries"] if e["id"] == "liberalismo"]
    check(len(entradas) == 1, "Entrada ausente/duplicada")
    if entradas:
        check(entradas[0]["status"] == "rascunho", "Status diferente do conteúdo")
        check("F03" in entradas[0]["familias"], "Família transversal F03 ausente")
    check(re.search(r"(?m)^status: rascunho\s*$", conteudo) is not None, "Status de verbete incorreto")
    section_numbers = [int(i) for i in re.findall(r"(?m)^## (\d{1,2})\. ", conteudo)]
    check(section_numbers == list(range(1, 16)), "15 seções numeradas incompletas")
    srcs = fontes.get("fontes", [])
    ids = [x.get("id") for x in srcs]
    check(len(srcs) == 8 and len(set(ids)) == len(ids), "Referências duplicadas ou faltantes")
    check(sum(x.get("tipo") == "primaria" for x in srcs) == 3, "Contagem de fontes primárias divergente")
    check(sum(x.get("tipo") == "secundaria" for x in srcs) == 5, "Contagem de fontes secundárias divergente")
    for x in srcs:
        u = urlparse(x.get("url", ""))
        check(u.scheme == "https" and bool(u.netloc), "URL inválida para " + str(x.get("id")))
        check(bool(x.get("localizadores")) and bool(x.get("verificacao")), "Metadados faltantes para " + str(x.get("id")))
    # Tags de fonte referenciadas no verbete e no fichamento
    for name, document in (("verbete", conteudo), ("fichamento", ficha)):
        used = set(re.findall(r"\[(LIB-S\d{2})\]", document))
        check(set(ids).issubset(used), f"IDs sem referência no {name}: {set(ids) - used}")
        check(used.issubset(set(ids)), f"IDs inexistentes no {name}: {used - set(ids)}")
    if errors:
        for error in errors:
            print("ERRO:", error)
        sys.exit(1)
    print("OK: Liberalismo — 15 seções; 8 referências; 3 fontes primárias e 5 secundárias; status de rascunho.")

if __name__ == "__main__":
    main()
