# CRTdle

A daily Wordle-style guessing game for CRT TVs and monitors.

Guess the day's CRT in ten tries. Every guess is scored on eight clues:

| Clue | Feedback |
|---|---|
| Brand | match / no match (plus a "same series" note) |
| Type | Consumer, Professional, or Computer Monitor |
| Size | viewable inches, yellow within 3", arrow points toward the answer |
| Best input | RF → Composite → S-Video → Component → RGB → Digital |
| Mask | Slot, Aperture Grille, Shadow, Monochrome |
| Tube | yellow when it's the same maker but a different line |
| Made in | country of manufacture |
| Weight | yellow within 20%, arrow points toward the answer |

Hints unlock after 3, 6, and 8 misses. A new CRT appears at midnight in the player's local time. Stats and streaks are saved in the browser.

## Data

All CRT data comes from [CRT Database](https://crtdatabase.com/) and is licensed
[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).
This project is a free, non-commercial fan game and is not affiliated with CRT Database.
Under the same license, this repo's data and derived files are also CC BY-NC-SA 4.0.

- 1,955 CRTs can be guessed
- 850 notable sets are in the daily answer rotation (pro and broadcast monitors, Hall of Fame sets, and consumer sets with component or RGB inputs or from well-known lines)

## Files

- `index.html`: the whole game, data included. Open it in a browser or serve it with GitHub Pages.
- `scraper/crtdb_scrape.py`: polite scraper (follows robots.txt, 3 second crawl delay, caches pages so reruns are cheap)
- `scraper/crts.json`: the scraped dataset
- `scraper/build_data.py` + `scraper/template.html`: rebuild `index.html` from fresh data

## Refreshing the data

```
cd scraper
py crtdb_scrape.py              # writes crts.json (cached pages are reused)
py build_data.py crts.json      # writes data.js
```

Then paste `data.js` into `template.html` in place of `/*DATA*/`, set `/*FLAGS*/` to `window.SHOW_IMG=true;`, and save the result as `index.html`.
