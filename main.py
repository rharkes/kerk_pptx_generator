"""
Open config.toml en maak kerkpptx
"""

import tomllib as toml
from pathlib import Path

import kerkpptxgenerator
from kerkpptxgenerator import SongList, add_pictureslide, make_presentation

try:
    print(f"Kerk pptx generator, versie {kerkpptxgenerator.__version__}")
    print("Config.toml laden")
    with open("config.toml", "rb") as f:
        cfg = toml.load(f)
    print("Presentatie klaarzetten")
    prs = make_presentation(cfg["slideproperties"])
    print("Liederen ophalen")
    songlist = SongList(Path(cfg["directory"]), Path(cfg["directory"], cfg["liedbestand"]))
    for song in songlist.paths:
        prs = add_pictureslide(prs, song, cfg["slideproperties"])
    print("Presentatie opslaan")
    prs.save(Path(cfg["directory"], cfg["pptxbestand"]))
except Exception as e:
    print(e)
finally:
    input("Press ENTER to exit")
