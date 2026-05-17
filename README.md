+-----------------------------------------------------------+
|                          MISTER                           |
|             Retro Football Manager Community              |
+-----------------------------------------------------------+

Language: **English** | [Português (Brasil)](README.pt-BR.md) | [Español](README.es.md)

---

# Welcome to Mister ⚽

Ever dreamed of managing your own football club from the ground up? **Mister** is a single-player, retro-styled football manager simulator inspired by the legendary *Elifoot 98* — brought into the modern era with real league data, deep tactics, and a live match engine.

Start at the very bottom of the global pyramid. Earn your reputation. Climb through nine divisions. Make history.

---

## 🎮 What Makes Mister Addictive

### 🌍 **A Real Global Football Pyramid**
Mister simulates **9 divisions** ranked by IFFHS prestige, featuring real leagues from around the world:

| Division | League | Country |
|----------|--------|---------|
| 1st | Premier League | England |
| 2nd | Série A | Brazil |
| 3rd | Serie A | Italy |
| 4th | Primera División | Spain |
| 5th | Bundesliga | Germany |
| 6th | Ligue 1 | France |
| 7th | Primeira Liga | Portugal |
| 8th | Eredivisie | Netherlands |
| 9th | Championship | England |

Every new manager starts at **Ninth Division** and must earn promotion all the way to the top. Three clubs go up and three come down at every level — every point counts.

---

### 👥 **Squad Management That Demands Strategy**
- **Fatigue & Fitness System** — players have stamina (fixed) and fitness (dynamic). A depleted forward plays at a fraction of their rated skill; rotate your squad or suffer the consequences.
- **Contract Management** — age-based contract lengths, signing bonuses, and salary reviews. Let a star's deal run down and lose them for free.
- **Up to 30 players** across your main squad, Team B, and bench. Move players in and out to build depth without blowing the wage bill.
- **Sortable squad table** — filter and rank by any attribute in one click.

---

### 📊 **Tactical Mastery**
Choose from **8 formations** and 3 mentalities — every combination produces a different attack/defence balance:

| Formation | Style |
|-----------|-------|
| 4-4-2 | Classic and balanced |
| 4-3-3 | Attack-oriented |
| 3-5-2 | Midfield control |
| 5-3-2 | Defensive solidity |
| 4-5-1 | Counter-attack |
| 3-4-3 | All-out attack |
| 4-2-3-1 | Double pivot — balanced edge |
| 4-1-4-1 | Deep defensive block |

Use **Auto mode** to let the engine pick the best XI by form score, or take **Manual control** and craft every lineup yourself. The mandatory Tactics review before each match means you always have a chance to adapt.

---

### ⚽ **Live Match Drama**
Forget instant results. Mister plays out every match event by event:

- Goals ⚽, missed chances 💥, yellow cards 🟨, and red cards 🟥 are revealed one by one
- **Yellow card accumulation** — five yellows on the season earns an automatic one-week ban
- **Red cards** remove a player from the pitch immediately and suspend them for the following week
- **Half-time substitutions** — review first-half ratings, make up to 3 changes, then watch the second half unfold in the same feed
- **Post-match analysis** — attendance, strength comparison bar, momentum update, and a colour-coded player rating for everyone who featured

---

### 🎯 **Transfer Market & Free Agency**
- Official **summer** (weeks 1–5) and **winter** (weeks 20–23) windows for contracted players; free agents are available year-round
- **AI clubs list players** when windows open — surplus, ageing, or low-skill squad members become available to buy
- **Incoming offers inbox** — AI clubs bid for your listed players; accept, reject, or let them expire
- **Loan system** — send players out for half a season; the fee arrives upfront and they return automatically
- **Advanced filters** — search by position, skill, age, nationality, contract length, stamina, market value, and more

---

### 🏆 **Cup Competition**
A two-phase knockout competition runs alongside the league all season:

- **B League Qualifying** (weeks 3–14, single-leg ties) — 63 clubs compete for 4 spots in the combined phase
- **Combined Phase** (Round of 16 through Final, weeks 17–45, two-legged ties) — aggregate scores, extra time, and penalties
- Cup prize money at every round: from $500K for a first-round exit to $40M for lifting the trophy

---

### 💰 **Finances & Stadium**
- **Prize money** flows every season — higher divisions pay more, better finishes earn a bigger share of the pool
- **Automatic ticket pricing** scales with your momentum score so crowd revenue feels earned
- **Stadium expansion** — invest profits to grow capacity and compound your income advantage

---

### 🧑‍💼 **Manager Market & Momentum**
- Every club in the game has a named AI manager with a **1–5 star reputation** that rises and falls with results
- Your own **momentum score** (0–100) tracks performance vs expectation week by week
- Momentum drives ticket prices, fan confidence, and ultimately your job security — shock defeats hurt, upset wins soar

---

### 🎨 **Retro Look, Modern Feel**
- **Classic DOS-inspired terminal UI** — the look and feel of *Elifoot 98*, rebuilt for today
- **Four themes:** Retro (green on black), Stadium Night (amber/gold dark), Light (clean red accent), Blue
- **System preference detection** — if you haven't picked a theme, the game respects your OS setting
- Fully responsive — desktop, tablet, or phone; it just works

---

### ♿ **Accessible to Everyone**
- Full **screen-reader support** with ARIA roles, labels, and live regions across every screen
- **Keyboard navigation** throughout — no mouse required
- Focus traps and `Escape`-to-close on all modals
- High-contrast colour choices verified against WCAG standards

---

### 🌐 **Multi-Language**
Play in **English**, **Português (Brasil)**, or **Español** — all screens, modals, and tooltips fully translated.

---

## 🚀 Latest Release

### **v0.13** — Security, Polish & DevOps Hardening *(May 3, 2026)*

No new gameplay features this time — just everything that makes the game feel *finished*:

- 🔒 **Security hardening** — Content Security Policy tightened, HTTP security headers added, UUID validation on all API calls, per-user rate limiting (20 req/min), and payload size caps on saves
- ♿ **Accessibility pass** — every modal, table, button, and live feed region now has full ARIA coverage
- 🎨 **Theme polish** — Retro green brightened, Stadium Night gets a warm amber/gold palette, Light theme switches to a football-red accent with system-sans font
- ⚡ **Resilience** — React ErrorBoundary on the full app, retry logic with exponential backoff on all API and Cosmos DB calls, loading and error screens instead of blank pages
- 🛠️ **CI/CD** — `lint → type-check → build` pipeline, `npm audit` on every push, production source maps disabled

[📖 Full Release Notes](changelog/v0.26.4.md)

> **Your saves are safe.** No data migrations or breaking changes in this release.

---

## 📜 Release History

| Version | Release | Highlights |
|---------|---------|-----------|
| **v0.26.4** | May 17, 2026 | v0.26.4 |
| **v0.26.3** | May 17, 2026 | v0.26.3 |
| **v0.26.2** | May 17, 2026 | v0.26.2 |
| **v0.26.1** | May 17, 2026 | v0.26.1 |
| **v0.26** | May 17, 2026 | v0.26 |
| **v0.25** | May 17, 2026 | v0.25 |
| **v0.24.1** | May 17, 2026 | v0.24.1 |
| **v0.24** | May 17, 2026 | v0.24 |
| **v0.23** | May 16, 2026 | v0.23 |
| **v0.22** | May 16, 2026 | v0.22 |
| **v0.21** | May 16, 2026 | v0.21 |
| **v0.20** | May 16, 2026 | Auth Flow Simplification |
| **v0.19** | May 16, 2026 | Accounts, Profile Settings & Password Recovery |
| **v0.18** | May 16, 2026 | 4-Segment Formation Display & Mobile Responsiveness |
| **v0.17** | May 16, 2026 | Admin Login Key Matching Hardening |
| **v0.16** | May 16, 2026 | Dashboard Layout Refresh, Top Scorers & News Actions |
| **v0.15** | May 3, 2026 | News System, Dashboard Polish & Save Reliability |
| **v0.14** | May 3, 2026 | Manager Rankings, Champions Hall & Unified Cup Calendar |
| **v0.13** | May 3, 2026 | Security, Polish & DevOps Hardening |
| **v0.12** | May 3, 2026 | Live Match, Cards & Post-Match Overhaul |
| **v0.11** | May 3, 2026 | Mobile Polish, Accessibility & Quality Pass |
| **v0.10** | May 2, 2026 | Match Day Experience & Fixture Balancing |
| **v0.09** | May 2, 2026 | Tactics Overhaul & Player Stats |
| **v0.08** | May 2, 2026 | Transfer Market Overhaul & Free Agency |
| **v0.07** | May 2, 2026 | Division-Aware Players & Match Realism |
| **v0.06** | May 2, 2026 | Finance & Stadium Overhaul |
| **v0.05** | May 2, 2026 | Manager Market & Momentum |
| **v0.04** | May 2, 2026 | Cup Competition & Calendar Redesign |
| **v0.03** | May 2, 2026 | Mobile UX, Themes, Data Pipeline |
| **v0.02** | May 2, 2026 | Squad Management, Player Depth, Fatigue System |
| **v0.01** | May 2, 2026 | League Rankings, New Manager Experience |
| **v0.00** | May 1, 2026 | Initial Release, Core Game Mechanics |

[📚 View All Changelogs →](changelog/)

---

## 💬 Help Shape Mister's Future

**Mister is built with you.** The live match feed, card system, half-time substitutions, loan market — all of it shaped by player feedback. Your report today could be tomorrow's feature.

### 🐛 Found a Bug?
Describe what happened and we'll get on it fast.
→ [Open a Bug Report](../../issues/new?template=bug_report.md)

### 💡 Got a Feature Idea?
New mechanic, quality-of-life change, or something you remember loving in an old classic?
→ [Submit a Feature Request](../../issues/new?template=feature_request.md)

### 💬 Join the Community
Talk tactics, share your promotion runs, and help steer the game's direction.
→ [Join the Discussions Forum](../../discussions)

---

## 📋 How to Give Great Feedback

1. **Be specific** — "The squad table is hard to read on mobile" lands better than "UI is bad"
2. **Search first** — add your voice to an existing report if it already exists
3. **Attach evidence** — a screenshot, a save file, or a browser console log helps us reproduce the issue fast
4. **Be kind** — everyone here loves football games and wants Mister to be great
5. **Follow up** — if someone asks a clarifying question, you're the expert on your own issue

---

## 🌐 Stay Connected

- 💬 **[WhatsApp Community](https://chat.whatsapp.com/C4r6lJ09VmQHSTBniDdlVn?mode=gi_t)** — live chat, tips & support
- **[GitHub Issues](../../issues)** — bug reports and feature requests
- **[GitHub Discussions](../../discussions)** — community chat, tactics, achievements
- **[Changelog](changelog/)** — full history of every release
- **[Security Advisories](../../security/advisories)** — responsible disclosure

---

**Mister** is made with ❤️ by the community, for the community.

**Start at the bottom. Climb to the top. Make history.** 🏆
