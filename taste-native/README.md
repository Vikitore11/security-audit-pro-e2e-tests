# Native Taste Skill cloud experiment

This isolated **public** branch runs the **unchanged upstream Taste Skill** at commit `f6b76575f949707b4e3c37cd86cb44b0b98643e8` in Ubuntu GitHub Actions with Node.js 22 and Chrome. It uses only a synthetic public test fixture with deliberately bad design. Nothing from private user repositories is checked out or uploaded.

Workflow: `.github/workflows/taste-skill-native.yml`.

A successful workflow proves the original CLI and Chrome checkers execute and detect defects. It does **not** by itself prove Cloudflare MCP can dispatch work, that the original Stop hook can run inside ChatGPT, or that the result applies to a private site.

The default `main` branch remains unchanged. This test is intentionally isolated from the Security Audit Pro files on `main`.

Source: https://github.com/Leonxlnx/taste-skill (MIT).

This branch additionally tests whether workflows introduced outside the default branch are dispatched on subsequent pushes.
