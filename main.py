"""Entry program for the 'Make the AI Judge Laugh: Office Jokes' bounty.

The whole entry is one line about office life, under 200 characters:
the daily standup that exists mostly to explain why the previous
standup ran long. This program writes the joke to /output/entry.txt
(an optional first argument overrides the destination for a dry run).
"""

import sys
from pathlib import Path

LINE = (
    "Our daily standup is fifteen minutes of six people explaining "
    "why yesterday's fifteen-minute standup ran long."
)
DEFAULT_TARGET = Path("/output/entry.txt")


def main(argv):
    assert len(LINE) < 200, "line exceeds the 200 character limit"
    assert LINE.strip(), "line must not be blank"
    target = Path(argv[1]) if len(argv) > 1 else DEFAULT_TARGET
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(LINE + "\n", encoding="utf-8")
    print(f"wrote {target} ({len(LINE)} characters)")


if __name__ == "__main__":
    main(sys.argv)
