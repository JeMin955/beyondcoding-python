with open(r"Class,py\FileIO\Hello.txt", "r") as f:
    content = f.read()
f = str(f)
with open(r"Class,py\FileIO\Blahblah.txt", "w", encoding="utf-8") as F:
    F.write(content)