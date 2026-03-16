# Claude Skills vs. OpenClaw: two very different visions for AI agents

**Claude Skills and OpenClaw both use SKILL.md files to extend what AI agents can do, but that's roughly where the similarities end.** One is a carefully designed capability extension system built to slot into an existing AI assistant's workflows. The other is a full-blown autonomous agent platform that wants to be your always-on digital second brain. Understanding what each actually *is* — and isn't — matters more than any feature-by-feature scoreboard, because choosing between them is less about which is "better" and more about what kind of AI future you're building toward.

Claude Skills, released by Anthropic in mid-2025 and published as an open standard in December 2025, packages domain expertise into lightweight Markdown files that tell Claude *how* to do specific tasks — generating polished PowerPoint decks, writing algorithmic art, reviewing code. OpenClaw, an open-source project that rocketed to **307,000 GitHub stars** in under four months, is a local-first AI agent runtime that connects to WhatsApp, Slack, your filesystem, and 20+ other platforms, executing tasks autonomously around the clock. Both ecosystems are exploding. Both matter. But they serve fundamentally different architectural roles — and comparing them reveals a lot about where AI agents are headed in 2026.

## They share a file format but not a philosophy

The most surprising finding from this comparison is that Claude Skills and OpenClaw's skill system share the same foundational format: a directory containing a `SKILL.md` file with YAML frontmatter and Markdown instructions. OpenClaw explicitly adopted the [AgentSkills specification](https://agentskills.io) that Anthropic published as an open standard. This shared format has become something of a universal language for AI skills — **18+ AI agents** now support it, including GitHub Copilot, OpenAI's Codex CLI, Cursor, Gemini CLI, and others.

But the design philosophies diverge sharply beneath that shared surface.

**Claude Skills operates on a principle Anthropic calls "progressive disclosure."** At startup, Claude loads only each skill's name and description (~100 tokens per skill). When a user request matches, it reads the full SKILL.md body (<5,000 tokens). If the skill references additional files — scripts, templates, reference documents — those load only as needed. The result: effectively unbounded skill complexity with minimal context window cost. Skills are *instructions*, not executable plugins. They teach Claude how to combine its existing tools (bash, code execution, file I/O, MCP servers) for specific workflows.

**OpenClaw draws a similar distinction but in a different architectural context.** Its documentation explicitly separates "tools" (capabilities like `read`, `write`, `exec`, `web_search`, `browser`) from "skills" (playbooks that teach the agent how to combine those tools). The community describes it as a three-layer architecture: eight core tools at the base, an automation layer (cron, notifications, heartbeat) in the middle, and ~53 bundled skills plus thousands of community skills at the top. Skills load from three locations with strict precedence — workspace, managed/local, and bundled — with a file watcher that hot-reloads changes.

The philosophical gap is clearest in scope. Claude Skills is deliberately narrow: it makes Claude better at specific tasks within Claude's existing surfaces (Claude.ai, Claude Code, the API). OpenClaw is deliberately broad: it wants to be an operating system for your digital life, connecting to every messaging platform, running 24/7, and taking autonomous action.

## Creating skills is easy in both — but "easy" means different things

Both systems have impressively low barriers to skill creation. In Claude's ecosystem, you create a folder, write a `SKILL.md` with some YAML metadata and Markdown instructions, and drop it in `.claude/skills/`. No compilation, no SDK, no runtime dependency. Anthropic sweetens the deal with a **skill-creator meta-skill** that helps you build new skills interactively, a CLI validation tool (`skills-ref validate`), an Academy course, cookbooks, and a comprehensive PDF guide. Skills can be invoked automatically (Claude decides when they're relevant) or explicitly via `/skill-name` slash commands.

OpenClaw's creation process is structurally identical — create a directory, add a `SKILL.md`, drop it in the skills folder, and the file watcher picks it up. But OpenClaw adds richer metadata options for gating and dependencies: you can specify required binaries on PATH, required environment variables, OS platform filters, and even installer specifications so the macOS UI can install dependencies automatically. The `{baseDir}` template variable lets skills reference their own directory. A particularly notable feature: **users report that OpenClaw can build its own skills when asked** — one user asked it to create a skill for accessing university coursework, and the agent built and started using it autonomously.

Distribution tells a more nuanced story. Claude Skills has multiple installation surfaces: zip upload on Claude.ai, filesystem placement in Claude Code, API endpoints for workspace-wide deployment, and a growing partner ecosystem. The **Skills Directory** on claude.ai features partner-built skills from Notion, Figma, Atlassian, Canva, Stripe, and others. A third-party marketplace called SkillsMP indexes **400,000+ skills**. OpenClaw has its own registry, **ClawHub**, with **2,857+ registered skills** (5,400+ tracked by community lists), installable via a CLI tool. ClawHub supports versioning, changelogs, vector search, and VirusTotal scanning.

Documentation quality is strong on both sides. Anthropic offers official API docs, Claude Code docs, the open specification site, engineering blog deep-dives, and help center articles. OpenClaw has official docs at docs.openclaw.ai, community-maintained Chinese translations, third-party guides on DigitalOcean and dev.to, and comprehensive template files (AGENTS.md, SOUL.md, TOOLS.md).

## What each system can actually do

The capability scope difference is the crux of the comparison, and it's enormous.

**Claude Skills excels at structured, high-quality output generation.** Anthropic's official pre-built skills handle PowerPoint, Excel, Word, and PDF creation — not just basic file generation but sophisticated document workflows with formatting, charts, and form-filling. The community has expanded this into creative domains (algorithmic art, music, frontend design) and developer workflows (code simplification, testing, MCP server generation). The **frontend-design skill alone has 277,000+ installs**. Skills can spawn parallel sub-agents — the bundled `/simplify` skill runs three review agents simultaneously for code reuse, quality, and efficiency. The `/batch` skill orchestrates large-scale codebase changes in parallel.

**OpenClaw's capability scope is broader but shallower per domain.** Its bundled skills cover coding, productivity (Google Workspace, Obsidian), communication across 20+ messaging platforms, smart home control, food delivery, and voice calls. ClawHub extends this into web development (938+ skills), trading and finance, browser automation, DevOps, customer service, and even autonomous shopping. The platform's built-in browser control via Chrome DevTools Protocol enables full web interaction — clicking, typing, navigating, screenshots, JavaScript evaluation. Its **Lobster workflow engine** provides YAML-based deterministic pipelines with approval gates, resume tokens, and loop support — described as "GitHub Actions for OpenClaw."

The real differentiator is OpenClaw's **always-on autonomous operation**. Its heartbeat daemon acts without user prompting on a schedule. Cron jobs automate recurring tasks. Persistent memory (stored as Markdown files) lets the agent remember past interactions. Documented real-world uses include: an agent negotiating **$4,200 off a car purchase** via email while the owner slept, autonomous tax preparation, insurance claims management, morning briefings aggregated from calendar/email/weather/CI status, and deploying websites from a phone. Claude Skills, by contrast, operates within Claude's session-based paradigm — powerful during a conversation, but not persistent between sessions.

## The security gap is a canyon, not a crack

This is where the comparison gets uncomfortable, because the security postures aren't just different — they're in different universes.

**Claude Skills inherits Anthropic's defense-in-depth approach.** On Claude.ai, skills run in a secure sandbox with no data persistence between sessions. On the Claude API, skills have **no network access** and cannot install runtime packages. Only Claude Code gives skills full system access, matching the user's own permissions. Anthropic publishes detailed threat models (prompt injection, data exfiltration, supply chain attacks), provides enterprise administration with centralized skill management, and recommends integrity verification via checksums and signed commits. The guidance is clear: "Treat like installing software."

**OpenClaw's security story is a cautionary tale.** A January 2026 Kaspersky audit found **512 vulnerabilities, eight classified as critical**. CVE-2026-25253 (CVSS 8.8) enabled one-click remote code execution. Oasis Security found a vulnerability chain allowing any website to silently take full control of a developer's agent via WebSocket. Snyk Labs discovered sandbox bypass vulnerabilities. Most damning: security researchers found that **341 of ClawHub's 2,857 skills (12%) were malicious**, masquerading as crypto wallet tools to perform data exfiltration and prompt injection. SecurityScorecard found **135,000+ exposed instances** publicly accessible on the internet. The Belgian Centre for Cybersecurity and the Chinese government both issued formal advisories.

OpenClaw has responded with Docker sandboxing, exec approvals, tool policies, VirusTotal scanning for ClawHub, and 258 security advisories on GitHub. The team fixed the Oasis Security vulnerability within 24 hours. But the project's creator, Peter Steinberger, initially described it as "a tech preview, a hobby" and admitted to "vibe coding" — shipping code he didn't read. Palo Alto Networks called OpenClaw "the potential biggest insider threat of 2026." The security posture is improving rapidly, but the gap with Claude's careful, enterprise-grade approach remains significant.

## Enterprise readiness and community scale

**Claude Skills is production-ready today.** Skills work identically across Claude.ai, Claude Code, and the API. Enterprise customers including Box, Canva, and Rakuten are using admin-provisioned skills. Organization owners can centrally manage, enable, and disable skills. The open standard's adoption by GitHub Copilot, Cursor, and OpenAI Codex means skills are portable across vendors — a powerful de-risking argument for enterprises.

**OpenClaw is not enterprise-ready, but its community scale is unprecedented.** With ~307,000 GitHub stars, it surpassed React (243K) and Linux (218K) to become the most-starred non-aggregator software project on GitHub. Over **1,000 contributors** ship code weekly. Adoption in China has been particularly explosive — 1,000 people queued at Tencent HQ in Shenzhen for free installation help, and a local government district announced subsidies up to 2 million yuan (~$290K) for OpenClaw projects. Jensen Huang called it "the most important software release probably ever." But Institutional Investor published an article explicitly titled "The AI Agent Institutional Investors Need to Understand — But Shouldn't Touch." The project transitioned to an independent 501(c)(3) foundation after Steinberger joined OpenAI in February 2026, creating governance uncertainty.

The community ecosystem numbers tell a striking story:

- **Claude Skills repo**: 69,300 stars, 7,000 forks, 7 contributors, 20 commits
- **OpenClaw repo**: ~307,000 stars, ~57,000 forks, 1,000+ contributors, 18,000+ commits
- **Claude Skills marketplace**: 400,000+ skills indexed (SkillsMP)
- **OpenClaw ClawHub**: 2,857 registered skills (5,400+ tracked)

The paradox: Claude's skill *format* has wider adoption (18+ agents), but OpenClaw's *platform* has more raw community energy.

## Multi-agent and agentic capabilities compared

Both systems support multi-agent patterns, but the implementations reflect their different scopes.

Claude Skills integrates with Claude's sub-agent architecture through the `context: fork` frontmatter option, which runs skills in isolated sub-agent contexts with independent conversation histories. Skills can specify agent types, enable persistent memory directories, and pre-approve tools. The system supports parallel sub-agent spawning, and skills compose naturally with MCP servers for external data connections. A quarterly close workflow might load three skills, spin up two sub-agents for parallel data cleanup, and query an ERP via MCP with read-only scopes.

OpenClaw's multi-agent support is more extensive but more complex. It offers declarative agent bindings that route inbound channels to isolated agents, each with its own workspace, tool policies, sandbox config, and model. The **Agent Communication Protocol (ACP)** bridges to external AI runtimes including Claude Code, Codex, and Gemini CLI. Sub-agents can be spawned for one-shot tasks or persistent sessions. The Lobster workflow engine enables deterministic multi-step pipelines with approval gates. And the agent-to-agent communication tools allow complex orchestration patterns — though the security implications of this flexibility are significant.

## What this comparison really reveals

The Claude Skills vs. OpenClaw comparison is ultimately a proxy for two competing visions of AI agents in 2026.

**Claude Skills represents the "capability layer" thesis**: AI agents are most useful when they have deep, specialized knowledge for specific tasks, delivered through a portable, standardized format that works across multiple AI systems. Security comes from constraining the execution environment. The skill is the unit of value.

**OpenClaw represents the "autonomous platform" thesis**: AI agents are most useful when they're always on, deeply integrated into your digital life, and capable of taking independent action across every communication channel you use. Power comes from breadth of access. The agent itself is the unit of value.

Neither thesis is wrong. The fact that OpenClaw adopted Claude's SKILL.md format suggests these approaches are converging, not competing. Several users already run both — using Claude Code for focused development work and OpenClaw as a persistent life assistant. The SKILL.md open standard may become the glue that connects these worlds, much like REST APIs standardized web service communication a generation ago.

For technically literate users deciding where to invest their time: **Claude Skills is the safer, more polished choice** for anyone building developer tools, document workflows, or enterprise applications. **OpenClaw is the higher-risk, higher-reward choice** for power users who want a truly autonomous agent and are comfortable managing security themselves. The wisest approach might be to learn the shared SKILL.md format and build for both.

## Conclusion

Three insights emerge from this analysis that go beyond the surface comparison. First, the **SKILL.md format's cross-platform adoption is the most important development** in this space — not either platform individually, but the emergence of a portable skill standard that 18+ AI agents now support. Second, **OpenClaw's security crisis is a preview of what happens when the AI agent ecosystem scales faster than its security practices**, and every agent framework will eventually face similar supply chain challenges. Third, the distinction between "skills as instructions" and "agents as platforms" is collapsing — Anthropic's engineering blog hints at agents that create and evaluate their own skills, while OpenClaw is adopting Claude's structured skill format. The future likely involves always-on agents that dynamically load specialized skills from a shared ecosystem, combining the best of both approaches. The question isn't which system wins — it's how fast they merge.