# PFUMA/INGCEBO — Part 5 Academic Project Brief

**Read this first, every session, before touching this repo.** Its purpose is to stop this
academic project from getting confused with GRIWD's live commercial PFUMA product, or with
Arnold's other Part 5 candidate project — both of which exist elsewhere on this machine and
share names/history with this folder.

---

## 1. What this repo is, right now

This exact folder is Arnold T. Mapindu's NUST Part 5 (Level 4.2) Telecommunications Engineering
final-year project, module **TCL 5000**.

- Repo: `https://github.com/ARNOLDMAPINDU/PFUMA-INGCEBO-PART-5-PROJECT.git` — `origin` was
  repointed here on **2026-09-18** (was `teamgriwd-del/PFUMA`, GRIWD's live product repo, whose
  code this folder originated from). This repo now exists purely to back the academic project up
  to GitHub. Do not expect a push here to reach any live deployment — there isn't one anymore.
- The codebase (React/Vite web app, Expo/React Native mobile app, Flask/MySQL backend) is the
  same one GRIWD built as a commercial product, but **this folder is now the academic fork** and
  will diverge from GRIWD's version over time (different remote, different infra, different
  documentation goal — a dissertation, not a pitch deck).

## 2. Disambiguation — do not confuse this with

- **GRIWD's live PFUMA product** — deployed on GRIWD's own VPS (`38.247.146.172`), repo
  `teamgriwd-del/PFUMA`. Same origin codebase, different project going forward. If anyone says
  "check the live site" without qualifying, assume they mean *this local build*, not the VPS —
  this academic build no longer points at the VPS at all (see §5).
- **ZUNDE** — an old/superseded name for the same commercial product, not this academic fork.
- **The Fault-Injection Testbed project** — a *completely different* Part 5 candidate project
  Arnold also has material for, at `PART5\FAULT INJECTION PROJECT\THE PROJECT` (microwave
  protection-switching testbed, ESP32/LoRa hardware). It has its own `AGENT_BRIEF.md`, its own
  chapter builder (`thesis_builder.py` + `chapters/*.py`), its own gmoyo-style pptx generator. As
  of 2026-09-18, **PFUMA/INGCEBO is the confirmed Part 5 project** — it has a repo literally named
  `PART-5-PROJECT`. Arnold has not said the Fault-Injection project is dropped, so don't assume
  that, but don't merge its content into this one either. Reusing its *method* (the gmoyo-style
  pptx builder pattern, the chapter Python-module contract, the passive-voice house style) is
  fine and encouraged; never copy its *content* — its title, objectives and hardware claims belong
  to a different project.
- **Other GRIWD/VPS-hosted projects** (BizFlow, GRIWD Forex Bot, ZESA Bypass Finder, IWMS) — all
  unrelated to this academic submission, mentioned only because they share the same VPS or the
  same author.

## 3. Student / school details

- **Student:** Arnold T. Mapindu
- **Institution:** The National University of Science and Technology (NUST), Zimbabwe — TelOne
  Centre for Learning
- **Faculty / Department:** Faculty of Industrial Technology, Department of Telecommunications
  Engineering (this is Arnold's own confirmed program; note the G.Moyo exemplar's cover page says
  "Faculty of Engineering / Department of Electronics" — that's a *different* student's program,
  do not copy that wording onto Arnold's cover page)
- **Programme:** Bachelor of Engineering Honours Degree in Telecommunications Engineering
- **Level:** 4.2 ("Part 5", final year)
- **Module code:** TCL 5000
- **Registration/Student number:** `[Registration Number]` — genuinely not known yet. Keep as a
  literal bracketed placeholder in every document. Never invent one.
- **Supervisor:** `[Supervisor's Name and Title]` — not yet assigned as of 2026-09-18. Keep as a
  placeholder. When Arnold names a supervisor, update this file immediately (it's the single
  source of truth other builder scripts should read from).
- **Day-job credibility asset:** RF/Transmission engineer, NetOne Zimbabwe, Harare Northern
  region, Huawei RTN900/RTN300 microwave backhaul network — genuinely real, usable in
  justification/background sections if it ever becomes relevant to this project's framing.

## 4. Guidelines authority — source of truth for structure and formatting

Location: `PART5\PROJECT WRITE UPPS and SCHOOL GUIDELINES FOR PART 5 PROJECTS\`

- **`TCL 5000 Final Project Guidelines (Final Review II).docx`** — the authoritative chapter
  structure and formatting rules (full breakdown below).
- **Exemplar dissertations confirmed to follow it:** `tinotenda kajawu final project
  NT01911274D (1).pdf`, Priviledge Gandira's files, Frank Sithole's file. Mitchel's file is
  useful for chapter discipline only (wrong field — social science).
- **`COVER_PAGE_Updated.docx`** in that same folder is a *generic* front-matter example from an
  unrelated program (Women's University in Africa, Social Work) — useful only as a loose
  cross-check of front-matter ordering (declaration → release form → approval form →
  acknowledgements → dedication → plagiarism/Turnitin report → abstract → TOC → list of
  figures/tables → acronyms), never as a source of NUST/TCL-specific wording.
- **Progress/defense presentation exemplar ("gmoyo style"), strict format:** `G.Moyo NT018481Z
  Telecommunication SOS System for captised boats.pdf` / `.pptx`. Structure: title page (project
  title / full name / programme / course code / supervisor / cohort, NUST crest + host-centre
  logo) → Purpose of the Project → Background → Main Elements of the Problem (What / Why / How) →
  Aim → Objectives (numbered, chronological, measurable verbs) → Tasks & Resources Required →
  Network/System diagram → Principle (with a technical figure) → Schedule of Work (Gantt) → Work
  Carried Out (kept to roughly 10 content slides total) → closing "Questions / Thank you" slide
  stating "15 minutes total: 10 to present, 5 for questions."
- **More guidelines will arrive from the supervisor over time.** When Arnold shares new
  supervisor material, log it in §8 below with a date — don't rely on conversation memory alone,
  since this file is version-controlled and survives regardless of what happens to memory.

### 4.1 Chapter/section structure (non-negotiable — exact numbers and titles)

Front matter (roman numerals; title page unnumbered): Title page, Examining Committee Report,
Dedication (optional, ~50 words), Acknowledgements (optional, brief), Copyright Statement,
Declaration, Abstract, Table of Contents, List of Tables, List of Figures, List of Acronyms and
Symbols.

Main chapters (arabic numerals, Chapter 1 starts at page 1):

- **CHAPTER 1 INTRODUCTION** — 1.1 Introduction, 1.2 Background, 1.3 Problem Statement,
  1.4 Solution, 1.5 Aim, 1.6 Objectives, 1.7 Justification, 1.8 Scope of the Study,
  1.9 Limitations and Delimitations (1.9.1 Limitations, 1.9.2 Delimitations),
  1.10 Document Organization, 1.11 Conclusion
- **CHAPTER 2 LITERATURE REVIEW** — 2.1 Introduction, 2.2 Review of Other Relevant Systems,
  2.3 Review of Relevant Technologies, 2.4 Research Gap, 2.5 Research Theories, 2.6 Conclusion
- **CHAPTER 3 SYSTEM DESIGN** (not "Methodology") — 3.1 Introduction, 3.2 **[open question —
  the template's guideline wording is "Hardware Design"; PFUMA/INGCEBO is now a pure software
  submission (IoT/hardware track removed 2026-09-18), so this heading needs the supervisor's
  confirmation — do not silently rename it without asking]**, 3.3 Software Design
  (3.3.1 System Architecture, 3.3.2 Design Concept Selection, ...), 3.4 Conclusion
- **CHAPTER 4 RESULTS ANALYSIS** — 4.1 Introduction, 4.2 **[same open question as 3.2 — the
  template says "Hardware Test Results"; likely reframed or dropped for a software-only
  project, confirm with supervisor]**, 4.3 Software Test Results, 4.4 Interpretation of Results,
  4.5 Conclusion
- **CHAPTER 5 RECOMMENDATION AND CONCLUSION** — 5.1 Introduction, 5.2 Recommendations,
  5.3 Future Work, 5.4 Conclusion

Then REFERENCES, then APPENDICES.

### 4.2 Rules that are easy to miss

- **Objectives must use measurable action verbs** — *to determine, to measure, to design, to
  formulate, to develop, to create, to calculate*. Explicitly forbidden: *to observe, to
  evaluate, to find out, to understand*. Chronological order matching project phases. Each
  objective must be something the supervisor can literally check by using the running software
  — this is where marks come from. Example of a gradeable objective: "to develop a marketplace
  that surfaces a livestock listing to buyers only after police clearance" — the supervisor can
  open the app, try to view/buy an uncleared listing, and confirm it's hidden. A vague objective
  ("to improve livestock trading") is not gradeable and will cost marks.
- **Passive voice**, third person, never "we" or "I". This is a final report, not a proposal —
  purge "(OUTLINE)", "this proposal outlines", "will be done in Chapter 4". Design decisions
  already made are past/present tense; work genuinely not yet done is stated honestly as such
  (framework + placeholder, not invented numbers).
- **Continuous prose**, not bullet dumps — bullets only for genuine lists (objectives, features,
  acceptance criteria).
- Spell out every acronym on first use, then use the acronym.
- **British/Zimbabwean spelling**: analyse, behaviour, utilise, labelled, centre.
- **References** numbered by order of appearance; most within the last five years (2020+).
- **Tables**: title above, numbered per chapter (Table 3.1, ...), entries 11pt. **Figures**:
  title below, numbered per chapter (Figure 3.1, ...), caption 11pt.
- Body text at most 60 A4 pages excluding front matter/references/appendices; at most 120 pages
  total.
- **Formatting**: Times New Roman; body 12pt; 1.5 line spacing; left margin 1.5in, others 1in.
  Chapter heading 14pt **bold** uppercase; section heading 14pt normal uppercase; sub-section
  13pt bold; sub-sub-section 12pt bold.

## 5. Current, verified state of the software (as academic artefact, 2026-09-18)

- Full-stack livestock verification + marketplace platform: Flask/Python API (`backend/app.py`,
  143 routes) + MySQL (`backend/schema.sql`) + React/Vite web app (`src/`) + Expo/React Native
  mobile app (`app/`) + a WebView-shell mobile variant (`app-webview/`).
- Roles: Farmer, Veterinarian, Supplier, Buyer, Police, Admin, Institution — see
  `DOCUMENTATION/FEATURES_AND_ROLES.md` for the full, code-verified feature breakdown. Prefer that
  folder (`PLATFORM_OVERVIEW.md`, `FEATURES_AND_ROLES.md`, `TECHNICAL_ARCHITECTURE.md`,
  `COMPLIANCE_AND_LEGAL.md`, `EVENT_ADAPTATION_GUIDE.md`) over the older root `README.md` /
  `PITCH_GUIDE.md`, which are stale (still describe a five-role version and call the `Buyer` role
  "Retailer").
- **IoT/hardware track fully removed from this academic copy (2026-09-18)** — the whole
  `hardware/` folder (Proteus simulations, PCB/KiCad, veroboard, wiring diagrams, firmware),
  `IOT_HARDWARE_GUIDE.md`, root wiring-diagram scripts/HTML, and the hardware procurement/
  component-list docs were deleted. This is now a purely software submission. IoT backend routes
  and UI (`iot-devices`, `IoTScreen.js`, `HardwareSimulation`) still exist in code but are dormant
  — do not present them as a feature or reference them in the academic objectives.
- **Runs 100% locally now — no VPS dependency** (infra change, 2026-09-18):
  - Backend: Flask dev server, `python backend/app.py`, listens on `localhost:5000` and the LAN
    IP. Connects to **XAMPP's local MySQL** (`C:\xampp`, default `root` user, no password,
    database `pfuma` — already exists locally with real schema and data; don't re-import
    `schema.sql` unless the database is genuinely missing). Start MySQL via XAMPP before running
    the backend (`C:\xampp\mysql\bin\mysqld.exe --standalone`, or the XAMPP control panel).
  - `app/config.js` (Expo mobile) and `app-webview/config.js` (WebView-shell mobile) were
    repointed from the old VPS IP (`38.247.146.172` / `38-247-146-172.sslip.io`, GRIWD's shared
    production server — never reintroduce this into the academic build) to local/LAN addresses.
    A physical phone needs the dev machine's actual LAN IP (`ipconfig` → IPv4 Address), not
    `localhost` — that IP can change between networks/sessions, so re-check it if the mobile app
    can't reach the backend.
  - Web app (`npm run dev`, Vite, port 5173) already falls back to `http://localhost:5000` for
    its API when `VITE_API_URL` is unset (`src/config.js`), so local web dev needs no config
    change.
- git `origin` repointed from `teamgriwd-del/PFUMA` to
  `ARNOLDMAPINDU/PFUMA-INGCEBO-PART-5-PROJECT` (2026-09-18) — see §1.

## 6. The honesty rule

Never fabricate results, test numbers, screenshots, or user/data counts that were not actually
produced or observed. What's genuinely built and verified (see §5, and whatever gets verified in
later sessions — log it here) can be reported as real in the dissertation. What isn't built yet
must be stated plainly as a framework/plan (Chapter 4's structure, Chapter 5's Future Work) —
never as invented data. A supervisor who asks "show me" and gets a fabricated number is the
single fastest way to lose marks and credibility.

## 7. How to work on this project

- Before writing any chapter section, objective, or claim, verify it against the actual running
  app or code — don't invent screenshots, user numbers, or test results.
- Follow the guidelines structure in §4 exactly — section numbers and titles are non-negotiable
  per the guidelines document. If a template heading doesn't fit (see the two open questions in
  §4.1), flag it and ask rather than silently deciding.
- Match the objective style described in §4.2 — every objective should be something a supervisor
  can literally test against the running platform.
- When generating a new pptx/docx builder script, prefer the reusable pattern already proven in
  the sibling Fault-Injection project (`make_gmoyo_style_ppt.py`'s helper functions) over
  hand-placing shapes from scratch.

## 8. Supervisor guidance log (dated, append-only)

- 2026-09-18 — No supervisor assigned yet. Registration number not yet issued/known.

## 9. Dissertation builder infrastructure (added 2026-09-18)

Reused the working pattern from the sibling Fault-Injection project rather than inventing a new
one. To regenerate the full document: `python thesis_builder.py` (generic renderer, implements
every formatting rule in §4.2 — Times New Roman, margins, heading sizes, roman/arabic page
numbering, `[[key]]` citation resolution, tables/figures/appendices). Content lives in
`chapters/`: `frontmatter.py` (title page, declaration, abstract, acronyms — all placeholders
kept honest, see §3) and `ch1.py`..`ch5.py` (one module per chapter, `HEADING` + `SECTIONS` +
optional `REFKEYS`, contract documented at the top of each file).

- **Chapter 1 (Introduction) is fully drafted** — all 11 sections, citing four real Zimbabwean
  statutes already researched and cross-sourced in `compliance/laws/` (Stock Theft Prevention Act,
  Animal Health Act, Brands Act, Veterinary Surgeons Act). No invented literature citations were
  used — Chapter 1 doesn't need them; Chapter 2 will, and those must be real, checkable sources,
  never fabricated.
- **Chapters 2-5 are placeholder stubs only** (`[ Pending ]` markers in every section) so the
  builder assembles a complete document without crashing. Do not treat their content as drafted.
  Chapter 3's §3.2 and Chapter 4's §4.2 both carry an explicit open question about the
  hardware-flavoured template heading (see §4.1) — resolve that with the supervisor before
  drafting those two chapters.
- Builder output: `PFUMA_INGCEBO - Project Documentation.docx` (gitignored-or-not TBD — check
  before committing whether generated docx output should be tracked or left as a build artefact).

---

*Last updated: 2026-09-18.*
