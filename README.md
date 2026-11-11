# Pujiverse Games & Sports — How to Play

How to play 1,716 games and sports from around the world, grouped into 47 categories. Each entry explains the game in three steps (set up, play, win) and links to the Pujiverse YouTube channel that covers it.

Home: [pujiverse.com](https://www.pujiverse.com/)

## Channels

| Channel | Categories |
|---|---|
| Pujiverse Sports | All 16 sports categories, plus Cue Sports & Table Games |
| Pujiverse Guess | Guessing Games |
| Pujiverse Quiz | Trivia & Quiz, Educational Games |
| Pujiverse Mind | Board, Card, Dice, Tile & Domino, Abstract Strategy, Paper & Pencil, Word, Puzzle, Memory & Brain, Mind Sports |
| Pujiverse Gaming | Party, Event & Field Day, Team Building, Kids, Tag & Chase, Role-Playing, Casino, Traditional (7 regions), Video Game Genres, Mobile Games, Esports |

## Files

- `index.html`: the complete site, one self-contained page (no build step needed to host it)
- `src/template.html`: page layout, styles and script
- `data/raw.json`: every entry extracted from the source workbooks
- `data/steps/*.txt`: the how-to-play steps, one line per game: `id|set up|play|win`
- `data/source/*.xlsx`: the original Pujiverse Games and Pujiverse Sports workbooks
- `build.py`: rebuilds `index.html` from the template and data

## Editing

- Change a game's steps: edit its line in `data/steps/`, then run `python3 build.py`
- Move a category to another channel: edit the `CH` map in `build.py`, then rebuild
- Change a channel's YouTube handle: edit the `CH` object in `src/template.html`, then rebuild

## Hosting

GitHub Pages: Settings → Pages → Deploy from branch → `main` / root.
Vercel: import this repo as a static site (no framework, no build command).
