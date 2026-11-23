# Noctalia-cs – Czech translation of noctalia

[Česky](README.md) · **English**

A complete Czech translation of the [noctalia](https://github.com/noctalia-dev/noctalia) user
interface (shell and panel for niri / Wayland). The official `cs.json` shipped in the package is
incomplete (about 2000 of 3400 strings in version 5.6.0). This translation is complete (3401/3401
for 5.6.0), and a pacman hook restores it after every noctalia update.

> Comments in the scripts and their output are in Czech.

## Quick start

```sh
./kontrola.py      # how much is translated compared to the installed noctalia, what's missing
./instaluj.sh      # installs the translation + pacman hook (asks for sudo)
```

Then restart noctalia. The language is set in noctalia (Settings → language `cs`, or
`"language": "cs"` in `~/.config/noctalia/settings.json`).

## Files

| File | Purpose |
|---|---|
| `cs.json` | the translation; same key structure as noctalia's `en.json` |
| `kontrola.py` | compares `cs.json` with `en.json` of the installed noctalia |
| `instaluj.sh` | validates the JSON, installs the translation and the hook |
| `noctalia-cs.hook` | pacman hook: after installing/upgrading `noctalia`, copies the translation back |

## Check – `kontrola.py`

```sh
./kontrola.py [path/to/en.json]   # default /usr/share/noctalia/assets/translations/en.json
```

It lists:
- **chybí** (missing): keys from `en.json` not present in `cs.json` (noctalia shows English text),
- **navíc** (extra): keys noctalia no longer uses (harmless, can be removed),
- **jiné zástupné symboly** (different placeholders): strings whose `{name}`, `{copy}` etc. differ
  from the original (noctalia then can't fill in the value).

Exit code 1 if something is missing or placeholders don't match, otherwise 0.

## How it works

- Noctalia 5.x loads translations only from `/usr/share/noctalia/assets/translations/<lang>.json`.
  Neither a user directory nor an environment variable can override it.
- `instaluj.sh` stores a copy in `/usr/local/share/noctalia-cs/cs.json` and installs
  `/etc/pacman.d/hooks/noctalia-cs.hook`. After every install or upgrade of the `noctalia`
  package, the hook overwrites the packaged `cs.json` with that copy.
- After editing `cs.json`, run `./instaluj.sh` again to update the copy used by the hook.

## Maintenance after a noctalia update

1. `./kontrola.py`: shows new keys added by noctalia.
2. Add them to `cs.json` (at the same place in the tree as in `en.json`) and fix any placeholders.
3. `./instaluj.sh`, restart noctalia, commit.

## Dependencies

`python3` (check and JSON validation), `sudo`, `pacman` (hook), an installed `noctalia`.

## Troubleshooting

- **English / incomplete again after an update:** the hook is missing or
  `/usr/local/share/noctalia-cs/cs.json` doesn't exist. Run `./instaluj.sh`.
- **Some strings are in English:** missing keys, see `./kontrola.py`.
- **`{something}` is visible or a value is missing:** placeholders don't match, see
  `./kontrola.py`.
- **`pacman -Qk noctalia` reports a modified file:** expected, `cs.json` is replaced by this
  translation.
- **The official translation becomes more complete than this one:** remove the hook
  (`sudo rm /etc/pacman.d/hooks/noctalia-cs.hook`) and reinstall the package
  (`sudo pacman -S noctalia`).
- **Uninstall:** same as above, plus `sudo rm -r /usr/local/share/noctalia-cs`.

## Upstream

The translation is also meant to be submitted to noctalia (a pull request to
[noctalia-dev/noctalia](https://github.com/noctalia-dev/noctalia), the `cs.json` file among the
translations). Once noctalia ships it in full, the hook is no longer needed.

## Support

If the translation is useful to you, you can buy me a coffee:

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/Q7Z72B5QVS)

## License

MIT, see [`LICENSE`](LICENSE). Noctalia itself is MIT-licensed as well.
