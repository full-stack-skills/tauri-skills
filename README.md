<div align="center">

# tauri-skills

**Tauri v2 cross-platform desktop and mobile app development skills**

[![GitHub](https://img.shields.io/badge/github-full--stack--skills%2Ftauri-skills-green.svg)](https://github.com/full-stack-skills/tauri-skills)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-Compatible-purple.svg)](https://agentskills.io)

English | [简体中文](./README.zh-CN.md)

[Introduction](#-introduction) ·
[Install](#-install) ·
[Skills](#-skills) ·
[Supported Agents](#-supported-agents) ·
[Ecosystem](#-ecosystem)

</div>

---

## 📖 Introduction

**Tauri Skills** is a curated collection of Agent Skills for AI coding agents, part of the [Full Stack Skills](https://github.com/partme-ai/full-stack-skills) ecosystem maintained by [PartMe.AI](https://github.com/partme-ai).

This package includes **52 skills**. Each skill is a self-contained `SKILL.md` file that AI agents load on-demand.

## 📦 Install

```bash
npx skills add full-stack-skills/tauri-skills
```

Or install specific skills:

```bash
npx skills add full-stack-skills/tauri-skills --skill <skill-name>
```

## 🎯 Skills (52)

| Skill | Description |
|-------|-------------|
| `tauri-app-autostart` | Guidance for Tauri v2 autostart setup with platform differences and rollback. |
| `tauri-app-barcode-scanner` | Guidance for Tauri v2 barcode scanner plugin with permissions and scan lifecycle. |
| `tauri-app-biometric` | Guidance for Tauri v2 biometric plugin with authentication flow and fallback strategy. |
| `tauri-app-cli` | Guidance for Tauri v2 CLI plugin with argument schema and app command routing. |
| `tauri-app-clipboard` | Guidance for Tauri v2 clipboard plugin with safe copy, paste, and monitoring flows. |
| `tauri-app-creator` | Guidance for creating Tauri v2 projects using official create-tauri-app workflows and minimal run verification. |
| `tauri-app-deep-linking` | Guidance for Tauri v2 deep-linking plugin with URL schemes and safe routing. |
| `tauri-app-develop` | Guidance for Tauri v2 daily development workflow, debugging, resources, sidecar usage, and testing strategies. |
| `tauri-app-dialog` | Guidance for Tauri v2 dialog plugin with native dialogs and unified API design. |
| `tauri-app-file-system` | Guidance for Tauri v2 file-system plugin with scoped access and safe file operations. |
| `tauri-app-frontend-selection` | Guidance for selecting and configuring frontend frameworks for Tauri v2 with static export compatibility. |
| `tauri-app-geolocation` | Guidance for Tauri v2 geolocation plugin with permission handling and privacy controls. |
| `tauri-app-global-shortcut` | Guidance for Tauri v2 global-shortcut plugin with conflict handling and release. |
| `tauri-app-haptics` | Guidance for Tauri v2 haptics plugin with feedback patterns and graceful fallback. |
| `tauri-app-http-client` | Guidance for Tauri v2 http-client plugin with allowlisted requests and secure transport. |
| `tauri-app-localhost` | Guidance for Tauri v2 localhost plugin with local service access and minimal exposure. |
| `tauri-app-logging` | Guidance for Tauri v2 logging plugin with levels, filtering, and safe diagnostics. |
| `tauri-app-nfc` | Guidance for Tauri v2 NFC plugin with session handling and data validation. |
| `tauri-app-notification` | Guidance for Tauri v2 notification plugin with permission flow and click handling. |
| `tauri-app-opener` | Guidance for Tauri v2 opener plugin with safe external links and file handling. |
| `tauri-app-os-info` | Guidance for Tauri v2 os-info plugin with safe system diagnostics and reporting. |
| `tauri-app-persisted-scope` | Guidance for Tauri v2 persisted-scope plugin with expiration and revocation flows. |
| `tauri-app-planning` | Comprehensive project planning, requirements analysis, and architectural orchestration for Tauri 2.0 applications. |
| `tauri-app-plugin-permissions` | Guidance for Tauri v2 plugin permission authoring, capability generation, and platform differences. |
| `tauri-app-positioner` | Guidance for Tauri v2 positioner plugin with multi-display alignment strategies. |
| `tauri-app-process` | Guidance for Tauri v2 process plugin with controlled process information exposure. |
| `tauri-app-shell` | Guidance for Tauri v2 shell plugin with secure command execution and open behavior. |
| `tauri-app-sidecar-nodejs` | Guidance for Tauri v2 sidecar Node.js integration with lifecycle and packaging. |
| `tauri-app-single-instance` | Guidance for Tauri v2 single-instance behavior and second-launch argument handling. |
| `tauri-app-splashscreen` | Guidance for Tauri v2 splashscreen setup and lifecycle control to avoid white screens. |
| `tauri-app-sql` | Guidance for Tauri v2 SQL plugin setup, migrations, and safe query access. |
| `tauri-app-store` | Guidance for Tauri v2 store plugin with key-value persistence and lazy loading. |
| `tauri-app-stronghold` | Guidance for Tauri v2 stronghold plugin with encrypted storage and sensitive data handling. |
| `tauri-app-system-tray` | Guidance for Tauri v2 system tray interactions and platform behavior differences. |
| `tauri-app-updater` | Guidance for Tauri v2 updater plugin with OTA updates and signing keys. |
| `tauri-app-upload` | Guidance for Tauri v2 upload plugin with file transfer, progress reporting, and headers. |
| `tauri-app-wasm` | Guidance for running Rust-compiled WASM in the Tauri v2 frontend. |
| `tauri-app-websocket` | Guidance for Tauri v2 websocket plugin with Rust-managed connections and lifecycle handling. |
| `tauri-app-window-menu` | Guidance for Tauri v2 window menu definition, event handling, and shortcuts. |
| `tauri-app-window-state` | Guidance for Tauri v2 window-state plugin to persist window size and position. |
| `tauri-build` | Guidance for Tauri v2 production builds, signing, and distribution artifacts. |
| `tauri-concept` | Guidance for Tauri v2 architecture concepts, process model, and IPC isolation patterns. |
| `tauri-config` | Guidance for Tauri v2 tauri.conf.json structure, lifecycle management, and CSP configuration. |
| `tauri-framework-security` | Guidance for Tauri v2 security model, baseline hardening, and runtime authority controls. |
| `tauri-framework-upgrade` | Guidance for upgrading to stable Tauri v2 from v1 or v2 beta with migration checks. |
| `tauri-ipc` | Guidance for Tauri v2 IPC with frontend invoke calls, Rust commands, and type-safe bindings. |
| `tauri-mobile` | Guidance for Tauri v2 mobile development setup, debugging, and bundle identifiers. |
| `tauri-scaffold` | Guidance for Tauri v2 project scaffolding with create-tauri-app, project structure, and frontend static export config... |
| `tauri-security` | Guidance for Tauri v2 capabilities, scope configuration, and ACL-based permission control. |
| `tauri-setup` | Guidance for Tauri v2 prerequisites and environment setup across macOS, Windows, Linux, and mobile Android iOS targets. |
| `tauri-window` | Guidance for Tauri v2 window creation, configuration, lifecycle management, and custom titlebar UI. |
| `tauri` | Comprehensive index for Tauri framework development, including Rust backend, frontend integration, and full plugin ec... |

## 🤖 Supported Agents

Works with [Claude Code](https://code.claude.com), [Codex](https://developers.openai.com/codex), [Cursor](https://cursor.com), [OpenCode](https://opencode.ai), [Gemini CLI](https://geminicli.com), [GitHub Copilot](https://github.com/features/copilot), [Windsurf](https://codeium.com/windsurf), and [70+ others](https://agentskills.io/clients).

### Claude Code Installation

**Option 1: npx skills CLI (Recommended)**

```bash
npx skills add full-stack-skills/tauri-skills
```

**Option 2: Manual Installation**

```bash
git clone https://github.com/full-stack-skills/tauri-skills.git
cp -r tauri-skills/skills/* .claude/skills/
```

For more details, see the [Claude Code Skills Guide](https://code.claude.com/docs/en/skills) and [Agent Skills Spec](https://agentskills.io/).

## 🌐 Ecosystem

| Resource | Link |
|----------|------|
| **Full Stack Skills** | [github.com/partme-ai/full-stack-skills](https://github.com/partme-ai/full-stack-skills) |
| **All Skill Groups** | [github.com/full-stack-skills](https://github.com/full-stack-skills) |
| **Agent Skills Spec** | [agentskills.io](https://agentskills.io) |
| **Skills CLI** | [github.com/vercel-labs/skills](https://github.com/vercel-labs/skills) |

## 📄 License

Apache 2.0 — see [LICENSE](LICENSE).
