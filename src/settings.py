import os

pymono_work_dir = os.path.dirname(os.path.abspath("src"))
album_art_dir = os.path.join(pymono_work_dir, "art")
no_go = [
    [0, 0], [80, 0], [160, 0], [240, 0], [320, 0], [400, 0], [480, 0], [560, 0], [640, 0],
    [720, 0], [0, 80], [80, 80], [160, 80], [560, 80], [640, 80], [720, 80],
    [0, 160], [80, 160], [640, 160], [720, 160], [0, 240], [640, 240], [720, 240],
    [0, 320], [640, 320], [720, 320], [720, 400], [720, 480], [0, 560], [0, 640],
    [720, 640], [0, 720], [80, 720], [640, 720], [720, 720]
]
contracts = ["Most Wanted", "Safecracker", "Intel", "Bounty"]
