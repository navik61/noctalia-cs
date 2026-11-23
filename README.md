# Noctalia-cs – český překlad noctalie

**Česky** · [English](README.en.md)

Český překlad rozhraní [noctalia](https://github.com/noctalia-dev/noctalia) (shell a panel pro
niri / Wayland). Oficiální `cs.json` v balíčku je neúplný (u verze 5.6.0 přibližně 2000 ze 3400
textů). Tento překlad je úplný (3401/3401 u verze 5.6.0) a pacman hook ho po každé aktualizaci
noctalie vrátí.

## Rychlé použití

```sh
./kontrola.py      # kolik textů je přeloženo vůči nainstalované noctalii, co chybí
./instaluj.sh      # nainstaluje překlad + pacman hook (ptá se na sudo)
```

Pak restartuj noctalii. Jazyk se nastavuje v noctalii (Nastavení → jazyk `cs`, v
`~/.config/noctalia/settings.json` klíč `"language": "cs"`).

## Soubory

| Soubor | Účel |
|---|---|
| `cs.json` | překlad; stejná struktura klíčů jako `en.json` noctalie |
| `kontrola.py` | porovná `cs.json` s `en.json` nainstalované noctalie |
| `instaluj.sh` | zkontroluje JSON, nainstaluje překlad a hook |
| `noctalia-cs.hook` | pacman hook: po instalaci/aktualizaci balíčku `noctalia` zkopíruje překlad zpět |

## Kontrola – `kontrola.py`

```sh
./kontrola.py [cesta/k/en.json]   # výchozí /usr/share/noctalia/assets/translations/en.json
```

Vypíše:
- **chybí**: klíče z `en.json`, které v `cs.json` nejsou (noctalia ukáže anglický text),
- **navíc**: klíče, které už noctalia nepoužívá (neškodí, můžeš je smazat),
- **jiné zástupné symboly**: text, kde se liší `{name}`, `{copy}` apod. oproti originálu (noctalia
  pak nedosadí hodnotu).

Návratový kód je 1, když něco chybí nebo nesedí zástupné symboly, jinak 0.

## Jak to funguje

- Noctalia 5.x načítá překlady jen z `/usr/share/noctalia/assets/translations/<jazyk>.json`.
  Uživatelský adresář ani proměnná prostředí to přepsat neumí.
- `instaluj.sh` uloží kopii do `/usr/local/share/noctalia-cs/cs.json` a nainstaluje
  `/etc/pacman.d/hooks/noctalia-cs.hook`. Hook po každé instalaci nebo aktualizaci balíčku
  `noctalia` přepíše balíčkový `cs.json` touto kopií.
- Po úpravě `cs.json` spusť `./instaluj.sh` znovu, aby se aktualizovala i kopie pro hook.

## Údržba po aktualizaci noctalie

1. `./kontrola.py`: ukáže nové klíče, které noctalia přidala.
2. Doplň je do `cs.json` (na stejné místo ve stromu jako v `en.json`) a oprav případné zástupné
   symboly.
3. `./instaluj.sh`, restart noctalie, commit.

## Závislosti

`python3` (kontrola a validace JSON), `sudo`, `pacman` (hook), nainstalovaná `noctalia`.

## Řešení problémů

- **Po aktualizaci je zase anglicky / neúplně:** hook chybí nebo neexistuje
  `/usr/local/share/noctalia-cs/cs.json`. Spusť `./instaluj.sh`.
- **Některé texty jsou anglicky:** chybějící klíče, viz `./kontrola.py`.
- **V textu je vidět `{něco}` nebo chybí hodnota:** nesedí zástupné symboly, viz
  `./kontrola.py`.
- **`pacman -Qk noctalia` hlásí změněný soubor:** očekávané, `cs.json` je přepsaný tímto
  překladem.
- **Oficiální překlad je jednou úplnější než tento:** odstraň hook
  (`sudo rm /etc/pacman.d/hooks/noctalia-cs.hook`) a přeinstaluj balíček
  (`sudo pacman -S noctalia`).
- **Odinstalace:** totéž jako výše a navíc `sudo rm -r /usr/local/share/noctalia-cs`.

## Upstream

Překlad je určený i pro zaslání do noctalie (pull request na
[noctalia-dev/noctalia](https://github.com/noctalia-dev/noctalia), soubor `cs.json` mezi
překlady). Až ho noctalia převezme celý, hook už nebude potřeba.

## Podpora

Pokud se ti překlad hodí, můžeš mi koupit kafe:

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/Q7Z72B5QVS)

## Licence

MIT, viz soubor [`LICENSE`](LICENSE). Noctalia samotná je také pod licencí MIT.
