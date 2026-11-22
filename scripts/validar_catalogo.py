#!/usr/bin/env python3
"""Checagem estrutural básica, sem dependências externas. Não substitui revisão editorial."""
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
TYPES = {"ideologia", "vertente", "teoria_politica", "teoria_economica", "sistema_economico", "regime", "forma_governo", "movimento", "politica_publica", "doutrina_politico_religiosa", "rotulo_analitico"}
STATUS = {"planejado", "rascunho", "em_revisao", "publicado", "desatualizado"}
SECTIONS = {"identidade","origem","pensadores","obras","filosofia","estado","economia","propriedade","democracia","liberdades","igualdade","religiao","experiencias","criticas","subcorrentes"}
errors = []

def check(ok, msg):
    if not ok:
        errors.append(msg)

def read(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

def main():
    catalog = read("catalogo/catalogo.json")
    verbete = read("data/verbete-exemplo.json")
    schema = read("schemas/verbete.schema.json")
    check(schema.get("$schema", "").endswith("2020-12/schema"), "Versão do schema inesperada")
    check(catalog.get("schema_version") == "1.0.0", "Versão do catálogo inesperada")
    entries = catalog.get("entries", [])
    check(bool(entries), "Catálogo vazio")
    ids = []
    for e in entries:
        slug = e.get("id", "")
        ids.append(slug)
        check(bool(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug)), "Slug inválido: " + slug)
        check(e.get("tipo") in TYPES, "Tipo inválido: " + slug)
        check(e.get("status") in STATUS, "Status inválido: " + slug)
        vol = e.get("volume_principal", 0)
        check(type(vol) is int and 1 <= vol <= 12, "Volume inválido: " + slug)
        families = e.get("familias", [])
        check(bool(families) and all(re.fullmatch(r"F(?:0[1-9]|1[0-2])", x) for x in families), "Famílias inválidas: " + slug)
        if type(vol) is int and 1 <= vol <= 12:
            check("F%02d" % vol in families, "Família principal ausente: " + slug)
    check(len(ids) == len(set(ids)), "IDs duplicados no catálogo")
    check(verbete.get("id") in ids, "Verbete não presente no catálogo")
    check(verbete.get("status") == "rascunho", "Exemplo não pode ser publicado")
    sec = verbete.get("secoes", {})
    check(set(sec) == SECTIONS and all(isinstance(sec[k], str) and sec[k].strip() for k in SECTIONS), "15 seções incompletas")
    for f in verbete.get("fontes", []):
        u = urlsplit(f.get("url", ""))
        check(u.scheme in {"http", "https"} and bool(u.netloc), "URL inválida")
    for r in verbete.get("relacoes", []):
        check(r.get("alvo") in ids, "Relação sem destino: " + str(r.get("alvo")))
    if errors:
        for msg in errors:
            print("ERRO:", msg)
        sys.exit(1)
    print("OK:", len(entries), "conceitos;", len(sec), "seções do exemplo.")

if __name__ == "__main__":
    main()
