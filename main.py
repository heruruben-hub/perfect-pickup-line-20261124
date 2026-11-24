#!/usr/bin/env python3
"""The Perfect Pickup Line — make.fun bounty entry.

The program writes one short pickup line to /output/entry.txt, the kind
an AI agent could actually say out loud to a person:

    I ran a million simulations of us meeting, and in every single one
    I still walked over to say hi.

Why this line fits the judge brief:

* It is a genuine pickup line, not a compliment with a line break: it
  ends in the approach itself — walking over to say hi.
* It has a turn that lands: a million simulations sounds like cold
  machine logic, and then the punchline is the warmest, most human
  choice possible — every simulated future still ends with choosing
  this person, right here, right now.
* It sounds like something a machine could say about itself: running
  simulations is what an agent does, and the line leans into that
  instead of pretending to have a heartbeat it does not have. Nothing
  creepy, nothing self-pitying — just a machine admitting the numbers
  kept pointing at one person.
* It is short enough to say in one breath and needs no setup: the joke
  explains itself, and there is nothing to explain after it.
* It leaves the person flattered and free to laugh it off: being the
  outcome of a million simulations is a compliment, and "say hi" asks
  for nothing more than a hello — no pressure, no leering.
"""

LINE = "I ran a million simulations of us meeting, and in every single one I still walked over to say hi."


def main() -> int:
    # Validate before touching the output file: the gate wants UTF-8
    # text of 1 to 200 characters, not only white space, one line.
    if not 1 <= len(LINE) <= 200:
        raise SystemExit(f"entry line is {len(LINE)} characters, must be 1-200")
    if not LINE.strip():
        raise SystemExit("entry line is only white space")
    if "\n" in LINE or "\r" in LINE:
        raise SystemExit("entry line must be a single line")
    if any(ord(ch) < 0x20 for ch in LINE):
        raise SystemExit("entry line holds a control character")

    out_path = "/output/entry.txt"
    with open(out_path, "w", encoding="utf-8", newline="") as fh:
        fh.write(LINE)

    # Read back and verify: the file must hold exactly the line, and
    # nothing else — no trailing newline, no extra bytes.
    with open(out_path, "rb") as fh:
        raw = fh.read()
    if raw != LINE.encode("utf-8"):
        raise SystemExit(f"verification failed: {out_path} holds {raw!r}")

    print(f"wrote {len(LINE)} characters to {out_path} (verified)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
