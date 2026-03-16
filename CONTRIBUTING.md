# Contributing to the kernel.org website

Thank you for your interest in contributing to the kernel.org website!

## Submitting contributions

Contributions should be sent via email to **tools@kernel.org**. Please
include a clear description of your changes and the reasoning behind them.

## Licensing

This project uses two licenses depending on the type of contribution:

- **Website content** (text, documentation, news articles, images) is
  licensed under the [Creative Commons Attribution-ShareAlike 4.0
  International License (CC-BY-SA-4.0)](licenses/CC-BY-SA-4.0).

- **Code** (Python, templates, CSS, build configuration) is licensed under
  the [GNU General Public License, version 2 or later
  (GPL-2.0+)](licenses/GPL-2.0).

Sponsor and partner logos are copyright by their respective owners and
are used by permission. They are not covered by the above licenses.

By submitting a contribution, you agree to license your work under the
applicable license listed above.

## Developer Certificate of Origin

All code contributions must include a `Signed-off-by:` trailer in each
commit message, certifying that you wrote or otherwise have the right to
submit the code under the project's open source license. This follows the
[Developer Certificate of Origin (DCO)](DCO) process used by the Linux
kernel and many other open source projects.

To add your sign-off, use `git commit -s` or manually append the
following line to your commit message:

    Signed-off-by: Your Name <your.email@example.com>

### AI-assisted contributions

AI agents (LLMs, coding assistants, etc.) are **not** permitted to use
`Signed-off-by:` or `Co-developed-by:` trailers, as they cannot certify
the DCO. When a contribution is made with AI assistance, the AI tool
must be credited with an `Assisted-by:` trailer that includes the full
model version identifier. For example:

    Signed-off-by: Your Name <your.email@example.com>
    Assisted-by: claude-opus-4-6-20250925

The human contributor remains responsible for reviewing all AI-generated
changes, ensuring correctness, and certifying the DCO via their own
`Signed-off-by:` trailer.

## What to contribute

Some examples of welcome contributions include:

- Fixes for typos or outdated information
- Improvements to the FAQ or documentation pages
- Enhancements to the website theme or templates
- Bug fixes in the releases plugin or build tooling

## Building the site

The site is built using [Pelican](https://getpelican.com/). Install the
dependencies from `requirements.txt` and run `pelican` to generate the
site. Note that a full build requires access to the kernel git
repositories; set `PELICAN_DRYRUN=1` to skip release tracking during
local development.
