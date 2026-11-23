#!/bin/sh
# Nainstaluje cs.json do noctalie a pacman hook, který ho vrací po aktualizacích.
set -e
cd "$(dirname "$0")"
python3 -c 'import json; json.load(open("cs.json"))'        # neplatný JSON neinstalovat
sudo install -Dm644 cs.json /usr/local/share/noctalia-cs/cs.json
sudo install -Dm644 noctalia-cs.hook /etc/pacman.d/hooks/noctalia-cs.hook
sudo install -m644 cs.json /usr/share/noctalia/assets/translations/cs.json
echo "Hotovo. Restartuj noctalii, aby načetla nový překlad."
