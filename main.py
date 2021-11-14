"""
Open config.toml en maak kerkpptx
"""

from pathlib import Path
import toml

from kerkpptxgenerator.util import add_pictureslide, make_presentation, SongList
try:
    print("Config.toml laden")
    with open('config.toml', 'r') as f:
        cfg = toml.load(f)
    print("Presentatie klaarzetten")
    prs = make_presentation(cfg['slideproperties'])
    print("Liederen ophalen")
    songlist = SongList(cfg['directory'], Path(cfg['directory'], cfg['liedbestand']))
    for song in songlist:
        prs = add_pictureslide(prs, song, cfg['slideproperties'])
    print("Presentatie opslaan")
    prs.save(Path(cfg['directory'], cfg['pptxbestand']))
except Exception as e:
    print(e)
finally:
    input('Press ENTER to exit')
