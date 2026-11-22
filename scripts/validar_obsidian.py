#!/usr/bin/env python3
"""Valida integridade estrutural do vault Obsidian. Não verifica alegações históricas."""
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
errors = []

def error(message):
    errors.append(message)

def read_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

def frontmatter(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        error(f"Frontmatter ausente: {path.relative_to(ROOT)}")
        return {}
    end = text.find("\n---\n", 4)
    if end < 0:
        error(f"Frontmatter sem fechamento: {path.relative_to(ROOT)}")
        return {}
    meta = {}
    for line in text[4:end].splitlines():
        match = re.match(r"^([a-z_]+):\s*(.*)$", line)
        if match:
            key, value = match.group(1), match.group(2).strip().strip('"').strip("'")
            if key in meta:
                error(f"Chave YAML duplicada: {path.relative_to(ROOT)} / {key}")
            meta[key] = value
    return meta

def check_link(base, target):
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    if re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", target) or target.startswith("//"):
        return True
    dest = unquote(target.split("#", 1)[0].split("?", 1)[0])
    if not dest:
        return True
    p = ROOT / dest.lstrip("/") if dest.startswith("/") else base.parent / dest
    try:
        p.resolve().relative_to(ROOT.resolve())
    except ValueError:
        return False
    return p.exists()

def check_markdown_links():
    count = 0
    tick = chr(96)
    for p in ROOT.rglob("*.md"):
        if ".obsidian" in p.parts or ".git" in p.parts:
            continue
        text = p.read_text(encoding="utf-8")
        # Remove fenced code blocks and inline-code examples before scanning links.
        fence = r"(?ms)^((?:" + re.escape(tick) + r"{3,}|~{3,})).*?^\1\s*$"
        text = re.sub(fence, "", text)
        text = re.sub(re.escape(tick) + r"[^" + re.escape(tick) + r"\n]+" + re.escape(tick), "", text)
        for m in re.finditer(r"(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)", text):
            target = m.group(1).split(' "', 1)[0]
            count += 1
            if not check_link(p, target):
                error(f"Link quebrado: {p.relative_to(ROOT)} => {target}")
        for m in re.finditer(r"!\[\[([^\]\n]+)\]\]", text):
            target = m.group(1).split("|", 1)[0].split("#", 1)[0]
            count += 1
            if not check_link(ROOT / "INICIO.md", target):
                error(f"Embed Obsidian quebrado: {p.relative_to(ROOT)} => {target}")
    return count

def main():
    catalog = read_json("catalogo/catalogo.json")
    entries = catalog["entries"]
    if len(entries) != 168:
        error("Esperados 168 conceitos canônicos")
    ids = [e["id"] for e in entries]
    if len(set(ids)) != len(ids):
        error("IDs duplicados")
    notes = set()
    for e in entries:
        path = e.get("nota")
        if not path:
            error(f"Nota ausente no catálogo: {e['id']}")
            continue
        if path in notes:
            error(f"Notas duplicadas: {path}")
        notes.add(path)
        note = ROOT / path
        if not note.is_file():
            error("Nota não existe: " + path)
            continue
        meta = frontmatter(note)
        for k, expected in [("id", e["id"]), ("classe", "verbete"), ("tipo", e["tipo"]),
                            ("status", e["status"]), ("volume_principal", str(e["volume_principal"]))]:
            if meta.get(k) != expected:
                error(f"Metadado divergente: {path} {k}: {meta.get(k)} vs {expected}")
        fm = note.read_text(encoding="utf-8").split("\n---\n", 1)[0]
        if "familias" not in meta or any(fam not in fm for fam in e["familias"]):
            error("Famílias inválidas: " + path)
        if "aliases" not in meta or "tags" not in meta:
            error("Aliases ou tags ausentes: " + path)
    for number in range(1, 13):
        path = ROOT / f"mapas/VOLUME-{number:02d}.md"
        if not path.is_file():
            error("Mapa ausente: " + str(path))
            continue
        meta = frontmatter(path)
        if meta.get("classe") != "volume" or meta.get("volume_numero") != str(number):
            error("Metadados de volume inválidos: " + path.name)
        body = path.read_text(encoding="utf-8")
        for e in entries:
            if f"F{number:02d}" in e["familias"] and e["id"] not in body:
                error(f"Mapa V{number:02d} sem {e['id']}")
    for name in ["VERBETES.base", "VOLUMES.base", "PESQUISA.base"]:
        p = ROOT / "bases" / name
        if not p.is_file() or "views:" not in p.read_text(encoding="utf-8"):
            error("Base ausente ou inválida: " + name)
    canvas = read_json("canvas/ENCICLOPEDIA.canvas")
    node_ids = [node["id"] for node in canvas["nodes"]]
    if len(set(node_ids)) != len(node_ids):
        error("IDs de Canvas repetidos")
    for node in canvas["nodes"]:
        if node["type"] == "file" and not (ROOT / node["file"]).is_file():
            error("Arquivo ausente no Canvas: " + node["file"])
    for edge in canvas["edges"]:
        if edge["fromNode"] not in node_ids or edge["toNode"] not in node_ids:
            error("Aresta inválida: " + edge["id"])
    for path in ["INICIO.md", "docs/OBSIDIAN.md", ".obsidian/app.json",
                 ".obsidian/templates.json", "painel/PAINEL-EDITORIAL.md"]:
        if not (ROOT / path).is_file():
            error("Configuração ausente: " + path)
    links = check_markdown_links()
    if errors:
        print("Falha na auditoria Obsidian:", len(errors))
        for message in errors:
            print("-", message)
        return 1
    print(f"OK: {len(entries)} verbetes, 12 mapas, {len(canvas['nodes'])} nós Canvas, {links} links/embeds examinados.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
