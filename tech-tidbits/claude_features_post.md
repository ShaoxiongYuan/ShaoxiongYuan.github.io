---
layout: tech-tidbit
title: "Claude's New Era: Every Feature That Matters in 2026"
headline: "Claude's New Era: Every Feature That Matters"
kicker: "Tech Tidbits"
category: "AI Features"
date: 2026-03-21
read_time: "12 min read"
summary: "Voice mode, agent teams, remote control from your phone, the /btw side-channel, 50+ MCP connections, Cowork, and a million-token context window. Here's what changed, why it matters, and where it's all heading."
head_image: "/images/tech-claude-features-post.jpg"
permalink: /tech-tidbits/claude-features-post/
---

Six months ago, Claude was a chatbot. Today it's an operating layer that lives in your terminal, your browser, your Office apps, and your phone — simultaneously. Q1 2026 has been the most feature-dense quarter in Anthropic's history, and the cumulative effect isn't incremental improvement. It's a category shift.

This post covers everything new, with enough depth to actually be useful. Let's get into it.

### At a glance

- **1M** — Token context window
- **50+** — MCP connectors
- **$2.5B** — Claude Code ARR

## 01 Claude Code: Not a Coding Assistant Anymore

Claude Code went from v2.1.63 to v2.1.76 in March alone. The aggregate effect transforms it from a terminal copilot into a full development environment with voice, multi-agent orchestration, persistent monitoring, and mobile control.

### 🎙️ Voice Mode

Activated via `/voice`, push-to-talk lets you hold spacebar to speak, release to send. The key is rebindable in `keybindings.json`. Twenty languages are now supported, and transcription has been tuned for developer vocabulary — terms like regex, OAuth, and JSON are recognized accurately. You can dictate complex refactoring instructions while your hands are on a whiteboard.

### 🤖 Agent Teams (Research Preview)

This is the architectural headline. Set `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` and Claude can spawn multiple autonomous agents, each working in an isolated git worktree on different components of a project. Supporting infrastructure includes **TeammateIdle** and **TaskCompleted** hooks, agent memory scoped to user/project/local, and sub-agent tool restrictions via `Task(agent_type)` syntax.

In practice: you describe a feature, and three agents simultaneously build the database schema, the API layer, and the frontend — then coordinate their merge.

### 🔁 /loop — Recurring Task Automation

```text
/loop 5m
 check the deploy status
/loop 30m
 run the test suite and report failures
/loop 1h
 pull latest market data and update the dashboard
```

The `/loop` command (v2.1.71) turns Claude Code into a monitoring daemon. Define an interval and a prompt, and it executes automatically for the duration of the session. Combined with cron scheduling tools, this enables CI/CD monitoring, periodic log analysis, and deployment health checks — all within your Claude Code session. Disable with `CLAUDE_CODE_DISABLE_CRON`.

*★ Game Changer*

### Remote Control — Code From Your Phone

Launched February 25, 2026, Remote Control lets you start a Claude Code session at your desk, then pick it up from your phone, tablet, or any browser. Run `claude remote-control` or type `/rc` mid-session. A URL and QR code appear — scan it and your full local environment (filesystem, MCP servers, tools, project config) is accessible remotely. **Nothing moves to the cloud.** Execution stays on your machine; the mobile interface is just a viewport.

The conversation stays in sync across all connected devices. If your laptop sleeps, the session reconnects automatically when it wakes. You can approve file changes, steer Claude away from bad approaches, and monitor progress — all from the Claude iOS/Android app while you're in a meeting or on the couch.

> **Why this matters:** Claude Code hit a $2.5B annualized run rate and 29 million daily VS Code installs. Remote Control means developers no longer need to be physically tethered to their workstation for long-running AI sessions. The "walk-away refactor" — start a task, step away, monitor from your phone — is now a native workflow.

*★ Sleeper Hit*

### /btw — Side Questions Without Context Pollution

Built by Erik Schluntz from the Anthropic team as a side project, `/btw` is deceptively simple: ask Claude a quick question *without adding it to the conversation history*. The answer appears in an overlay, your main task keeps running, and the exchange never enters the context window.

This solves a genuine pain point. In long sessions, every mid-task question inflates context, compounding token costs and degrading focus. `/btw` sees your full conversation (so it can answer about code Claude already read), but has no tool access — it's the inverse of a subagent. Users report up to **50% token reduction** in sessions with frequent mid-task questions.

```text
# You're mid-refactor. Quick question without breaking flow:
/btw
 what was the name of that utility function we saw in utils.py?
# Answer appears in overlay. Press Space/Enter/Escape to dismiss.
# Main task continues uninterrupted. Context stays clean.
```

### 📋 New Commands at a Glance

| Command | Purpose |
|---|---|
| `/voice` | Push-to-talk, 20 languages |
| `/loop` | Recurring prompt automation |
| `/btw` | Side question, no history |
| `/rc` | Remote control from phone |
| `/effort` | Low / medium / high reasoning |
| `/color` | Visual session distinction |
| `/simplify` | Simplify selected code |
| `/batch` | Multi-file operations |
| `/rewind` | Undo code changes |
| `/compact` | Manual context compaction |

### Other Notable Additions

- **1M token context** — 5x increase from 200K. Hold entire codebases in context. Available on Max, Team, Enterprise with Opus 4.6.
- **Automatic memory** — Claude remembers coding conventions, architecture decisions, and preferred workflows across sessions. Managed via `/memory`.
- **Plugin marketplace** — Discover, install, and manage third-party extensions. Plugins can bundle MCP servers.
- **MCP elicitation** — MCP servers can request structured input mid-task via interactive forms, without interrupting workflow.
- **Ultrathink** — Keyword to force maximum reasoning depth on any individual prompt when default medium effort isn't enough.
- **Background tasks (Ctrl+B)** — Push any running command to background. Combine with `/btw` to ask questions while tasks run.
- **HTTP hooks** — POST JSON to a URL and receive JSON back, replacing shell-based hooks for webhook/notification integrations.

## 02 Cowork: Claude Code for Everyone Else

Launched January 12, 2026, Cowork is "Claude Code without the terminal." Point it at a folder, describe an outcome, and let it work autonomously. It runs in a sandboxed VM within the Claude Desktop app, with direct access to local files and MCP integrations.

The real power emerges when you chain surfaces: **Chrome navigates the web and gathers data → Cowork compiles it into Excel workbooks, Word documents, or PowerPoint decks → MCP connectors push results to Slack or email.** Since the March 11 update, Excel and PowerPoint share full conversational context, so analysis in one automatically informs the other.

*Example Workflow*

### Quarterly Earnings Analysis

Chrome agent navigates your analytics dashboard and extracts KPIs. Cowork receives the data, builds an Excel model with pivot tables and scenario analysis. The PowerPoint add-in reads the Excel context and generates a board-ready deck with charts and narrative — all template-compliant. A custom Skill encodes the entire flow for one-click repetition next quarter.

Cowork expanded from Mac-only/Max-only at launch to Pro plans by mid-January, added Windows support in February, and Enterprise self-serve purchasing went live in March.

## 03 MCP: The Universal Integration Layer

The Model Context Protocol has matured from a local developer tool into the standard for AI-to-application communication. The Connectors Directory now features **50+ curated integrations**, all available on paid plans at no extra charge.

`Gmail`, `Google Calendar`, `Slack`, `Notion`, `Figma`, `Canva`, `GitHub`, `Jira`, `Confluence`, `Amplitude`, `Hex`, `Salesforce`, `Shopify`, `LSEG`, `Zapier`, `Box`, `Linear`, `ElevenLabs`, `Block`, `BioRender`, `MS 365`

### Interactive MCP Apps

Launched January 2026, MCP Apps go beyond text exchange. Any MCP server can supply an interactive UI that renders directly inside Claude's conversation. Request a chart from Amplitude data and the chart appears in-context. Draft a Slack message and preview formatting before sending. Generate a Figma diagram without leaving the chat.

### Custom Connectors

Paid users can add custom connectors by entering an MCP server URL in Settings. This connects Claude to proprietary internal tools, databases, and operational platforms. In Claude Code, MCP servers support three scope levels (local, project, user) with environment variable expansion for team configurations.

## 04 API: The Developer Platform Grows Up

The Claude API shipped a suite of features that collectively enable a new class of production-grade AI applications.

*Infrastructure*

### Compaction API — Infinite Conversations

Server-side context summarization that automatically triggers when input tokens exceed a threshold. The API generates a summary, creates a compaction block, and continues from compressed context. Critical for long-running agents, customer support bots, and multi-step research workflows.

- **Tool Search** — Dynamic on-demand tool discovery from large catalogs. 85% context reduction. Accuracy jumped from 49% → 74% (Opus 4) and 79.5% → 88.1% (Opus 4.5).
- **Programmatic Tool Calling** — Invoke tools from within a code execution sandbox. Powers Claude for Excel's ability to manipulate thousands of rows without context overflow.
- **Dynamic Filtering** — Web search results filtered by code execution before entering context. Less noise, more accuracy, fewer tokens.
- **Data Residency** — `inference_geo` parameter for US-only inference at 1.1x pricing. Critical for financial services and healthcare compliance.
- **Fast Mode** — Up to 2.5x faster Opus output at premium pricing ($30/$150 per MTok). Same model, same intelligence, faster inference.
- **Structured Outputs** — GA. Moved to `output_config.format`. Reliable JSON schemas for production pipelines.

## 05 Opus 4.6 & Sonnet 4.6

**Opus 4.6** is Anthropic's most intelligent model: 1M token context (GA as of March 13), 128K max output, extended thinking, compaction, tool search, and fast mode. It's the default for Claude Code and the Office add-ins.

**Sonnet 4.6** delivers improved agentic search with fewer tokens. Same 1M context, 64K max output, extended thinking. Positioned for everyday tasks and cost-sensitive production workloads.

Both models deprecate Opus 4.0 and 4.1 (removed from selector). Haiku 3 retirement is scheduled for April 19, 2026.

## 06 Enterprise & The $100M Bet

The enterprise story is aggressive. Claude now lives natively inside Excel and PowerPoint, with shared cross-app context and reusable Skills. The add-ins work through direct Claude accounts or via LLM gateways on Amazon Bedrock, Google Vertex AI, or Microsoft Foundry.

The **Claude Partner Network**, announced March 2026 with $100 million for the year, provides training, the **Claude Certified Architect** credential, dedicated applied AI engineers, and co-marketing. Self-serve Enterprise eliminates the sales conversation — any org can buy directly. Fortune 500 pilots are already running at L'Oréal, Deloitte, and Thomson Reuters.

Claude in Chrome rounds it out: contextual prompt suggestions per-website, web navigation and form filling, scheduled tasks for recurring reports, and integration with Claude Code for build-test-verify developer workflows.

## 07 Q1 2026 Timeline

- **Jan 12:** **Cowork launches** — Mac-only, Max plans. Claude Code for non-developers.
- **Jan 27:** **MCP Apps go live** — Interactive UIs inside Claude conversations. 50+ connectors.
- **Feb 6:** **Opus 4.6 + Agent Teams** — Multi-agent collaboration. Auto-memory. Plugin marketplace.
- **Feb 25:** **Remote Control** — Control local Claude Code sessions from phone/browser.
- **Mar 1:** **Enterprise plugins** — Excel, PowerPoint, Chrome, Slack integration bundle.
- **Mar 11:** **Shared Office context** — Excel ↔ PowerPoint full session awareness. Skills + LLM gateways.
- **Mar 13:** **1M context GA** — Opus 4.6 and Sonnet 4.6. /loop, /btw, voice mode mature.
- **Mar 18:** **Partner Network** — $100M investment. Claude Certified Architect credential.

## 08 Where This Is All Going

The Q1 2026 feature set isn't a collection of incremental improvements. It's a structural shift in how AI integrates into professional work. Five vectors define the trajectory:

**From assistant to agent.** Agent teams, /loop, Cowork, and browser automation collectively demonstrate AI that can be delegated multi-step, multi-system workflows running to completion without continuous guidance. Remote Control extends this into "fire and forget" territory — start a task, walk away, steer from your phone.

**From single-app to cross-app context.** Shared state between Excel and PowerPoint previews a broader pattern: AI that maintains understanding across every application in your workflow. MCP's universal protocol makes this extensible to any system.

**From text protocol to interactive interface.** MCP Apps transform Claude from text-in/text-out to an interactive workspace. Charts render in-context, messages are previewed, diagrams generate inline. The boundary between the AI conversation and the application itself is dissolving.

**From finite context to infinite memory.** 1M tokens + compaction + auto-memory = an AI that effectively never forgets. /btw keeps context clean by diverting side conversations. The combination means AI that accumulates institutional knowledge over time without degrading from context bloat.

**From platform to ecosystem.** The Partner Network, plugin marketplace, certifications, and self-serve Enterprise signal that Anthropic is building an ecosystem, not just a product. With $100M committed to partner enablement and Claude embedded inside Microsoft 365 via Copilot, the distribution leverage is formidable.

> The question is no longer whether AI will be integrated into professional workflows. The question is which protocol and ecosystem becomes the standard interface between human intent and digital action. With MCP's open standard, 50+ integrations, and a $100M ecosystem investment, Anthropic is making a credible case that Claude is the answer.
