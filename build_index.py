"""Build the public index from UTF-8 skills on main. No external dependencies."""
import hashlib
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parent
skills = []
for path in sorted(root.glob("skills/*/SKILL.md")):
    data = path.read_bytes()
    text = data.decode("utf-8")
    first, meta, body = text.split("---\n", 2)
    fields = dict(line.split(": ", 1) for line in meta.splitlines())
    name = fields["name"]
    assert not first and len(text) <= 4000 and name == path.parent.name
    assert len(name) <= 64 and re.fullmatch("[a-z0-9]+(?:-[a-z0-9]+)*", name)
    assert 0 < len(fields["display"]) <= 80 and 0 < len(fields["description"]) <= 300
    for section in ("入口", "步骤", "容易出错的地方", "怎样算办成", "什么时候停下交给用户"):
        assert f"## {section}" in body.splitlines()
    skills.append({key: fields[key] for key in ("name", "display", "description")} |
                  {"sha256": hashlib.sha256(data).hexdigest()})
assert len(skills) <= 100
(root / "index.json").write_text(json.dumps({"version": 1, "skills": skills},
    ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
