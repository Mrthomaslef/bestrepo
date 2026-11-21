#!/usr/bin/env python3
"""Récupère les infos GitHub (étoiles, langage, activité…) des dépôts sélectionnés
et génère data/repos.json + data/embedded_data.js (fonctionne hors-ligne / file://).

Token : variable GITHUB_TOKEN, sinon `gh auth token`.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from curated import CATEGORIES, REPOS  # noqa: E402

FIELDS = """nameWithOwner url description stargazerCount forkCount pushedAt homepageUrl isArchived
primaryLanguage { name color } licenseInfo { spdxId } owner { avatarUrl }"""


def token() -> str:
    t = os.environ.get("GITHUB_TOKEN")
    if t:
        return t
    return subprocess.run(["gh", "auth", "token"], capture_output=True, text=True, check=True).stdout.strip()


def graphql(query: str, tok: str) -> dict:
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": query}).encode(),
        headers={"Authorization": f"bearer {tok}", "User-Agent": "bestrepo-build"},
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())


LEVEL = {1: "facile", 2: "moyen", 3: "avancé"}


def stars(n: int) -> str:
    return f"{n / 1000:.0f}k" if n >= 1000 else str(n)


def write_catalog(payload: dict) -> None:
    """Catalogue compact lu par les agents (skill bestrepo-advisor)."""
    lines = [
        "# Catalogue BestRepo — dépôts recommandés pour les projets de Thomas",
        "",
        f"_Généré le {payload['generatedAt'][:10]} par scripts/build_data.py — ne pas éditer à la main "
        "(modifier scripts/curated.py)._",
        "",
        "Format : `owner/repo` (★ étoiles · niveau · type) — à quoi ça sert · **Pour Thomas :** usage · `démarrage`",
    ]
    for c in payload["categories"]:
        items = sorted((r for r in payload["repos"] if r["cat"] == c["id"]), key=lambda r: -r["stars"])
        if not items:
            continue
        lines += ["", f"## {c['emoji']} {c['title']} (`{c['id']}`)", f"_{c['intro']}_", ""]
        for r in items:
            flag = " ⭐" if r["pick"] else ""
            flag += " ⚠️archivé" if r["archived"] else ""
            inst = f" · `{r['install']}`" if r["install"] else ""
            lines.append(
                f"- `{r['repo']}`{flag} (★{stars(r['stars'])} · {LEVEL[r['level']]} · {r['kind']}) — "
                f"{r['why']} **Pour Thomas :** {r['use']}{inst}"
            )
    (ROOT / "CATALOG.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    tok = token()
    seen, entries = set(), []
    for e in REPOS:
        if e["repo"].lower() in seen:
            print(f"doublon ignoré : {e['repo']}")
            continue
        seen.add(e["repo"].lower())
        entries.append(e)

    info: dict[str, dict] = {}
    for start in range(0, len(entries), 40):
        chunk = entries[start:start + 40]
        parts = []
        for i, e in enumerate(chunk):
            owner, name = e["repo"].split("/")
            parts.append(f'r{i}: repository(owner: "{owner}", name: "{name}") {{ {FIELDS} }}')
        res = graphql("query {" + "\n".join(parts) + "}", tok)
        data = res.get("data") or {}
        for i, e in enumerate(chunk):
            if data.get(f"r{i}"):
                info[e["repo"]] = data[f"r{i}"]

    missing = [e["repo"] for e in entries if e["repo"] not in info]
    out = []
    for e in entries:
        g = info.get(e["repo"])
        if not g:
            continue
        out.append({
            "repo": g["nameWithOwner"],
            "url": g["url"],
            "cat": e["cat"],
            "kind": e["kind"],
            "level": e["level"],
            "pick": bool(e.get("pick")),
            "why": e["why"],
            "use": e["use"],
            "install": e.get("install", ""),
            "desc": g.get("description") or "",
            "stars": g["stargazerCount"],
            "forks": g["forkCount"],
            "pushedAt": g["pushedAt"],
            "homepage": g.get("homepageUrl") or "",
            "archived": g["isArchived"],
            "lang": (g.get("primaryLanguage") or {}).get("name") or "",
            "langColor": (g.get("primaryLanguage") or {}).get("color") or "",
            "license": (g.get("licenseInfo") or {}).get("spdxId") or "",
            "avatar": (g.get("owner") or {}).get("avatarUrl") or "",
        })

    payload = {
        "generatedAt": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "categories": CATEGORIES,
        "repos": out,
    }
    (ROOT / "data").mkdir(exist_ok=True)
    js = json.dumps(payload, ensure_ascii=False, indent=1)
    (ROOT / "data" / "repos.json").write_text(js + "\n", encoding="utf-8")
    (ROOT / "data" / "embedded_data.js").write_text(f"window.BESTREPO_DATA = {js};\n", encoding="utf-8")

    write_catalog(payload)

    print(f"{len(out)} dépôts écrits · {sum(r['stars'] for r in out):,} étoiles au total")
    if missing:
        print("INTROUVABLES :", ", ".join(missing))
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
