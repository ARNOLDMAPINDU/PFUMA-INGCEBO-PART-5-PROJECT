# PFUMA/INGCEBO — Documentation Set

This folder is the platform-level documentation for PFUMA/INGCEBO, written so the project can be
presented and understood independent of any single event. The original show-specific written
materials (pitch scripts, `README.md`, `SETUP.md`, `IMPACT_AND_COMPLIANCE.md`) still live in the
project root and have been corrected to match the current build (see below) — this folder does not
replace them, it sits above them as the reusable core. All original **docx/pdf/pptx artifacts**
(posters, decks, procurement lists, budget/commercialization docs) have been moved out of the
project root into [`source-materials/`](source-materials/) so the root isn't cluttered with binary
files; `compliance/` (legal research) stays where it is since other docs link into it by path.

**Why this folder exists:** PFUMA/INGCEBO was built for the Zimbabwe Agricultural Show, but the
platform itself — verified digital livestock records, role-gated marketplace clearance, AI
assistant, compliance engine — is not agric-show-specific. It is being positioned for reuse at
other expos and innovation competitions (e.g. POTRAZ innovation drives), each of which needs its
own pitch framing but the same underlying product story. Documents that said "built for the
Zimbabwe Agricultural Show" everywhere made that reuse harder, so this is the neutral version.

## Read in this order

1. **[PLATFORM_OVERVIEW.md](PLATFORM_OVERVIEW.md)** — what PFUMA/INGCEBO is, the problem it solves,
   current build status, and what is real vs. dormant (including the current IoT status).
2. **[FEATURES_AND_ROLES.md](FEATURES_AND_ROLES.md)** — every role, every feature, and how they
   connect, described functionally rather than as show-floor talking points.
3. **[TECHNICAL_ARCHITECTURE.md](TECHNICAL_ARCHITECTURE.md)** — stack, repo layout, data model,
   security model, and how/where it runs (local dev + the live GRIWD VPS deployment).
4. **[COMPLIANCE_AND_LEGAL.md](COMPLIANCE_AND_LEGAL.md)** — how the product maps to Zimbabwean law
   today, and how that same "map features to the governing rules" approach generalizes to a
   different domain/regulator.
5. **[EVENT_ADAPTATION_GUIDE.md](EVENT_ADAPTATION_GUIDE.md)** — the actual how-to for taking this
   platform to a *different* expo or competition: what to re-skin per event, what never changes,
   and a worked example for a POTRAZ-style innovation/tech competition instead of an agricultural
   show.

## Source-of-truth notes

- These documents describe the codebase as of **2026-09-18**. Where something in here conflicts
  with the code, the code wins — re-check before relying on a specific route, table, or role name.
- The root-level `README.md`, `PITCH_GUIDE.md`, `SETUP.md`, and `IMPACT_AND_COMPLIANCE.md` are
  **event-specific artifacts for the Zimbabwe Agricultural Show** — they're kept as-is
  event-focused documents, but as of 2026-09-18 they've been corrected to match the current build:
  role name fixed (`Buyer`, not "Retailer"), and the `Institution` role, farmer cooperatives, and
  national outbreak reporting/verification are now documented in them. `IOT_HARDWARE_GUIDE.md` was
  intentionally left untouched — the hardware track is dormant (see PLATFORM_OVERVIEW.md) and that
  file is a historical hardware design reference, not an active pitch document.
- [`source-materials/`](source-materials/) holds the original docx/pdf/pptx files (posters, the
  ZAS2026 deck, procurement lists, budget/commercialization requests, wiring-diagram exports) moved
  out of the project root. Hardware manufacturing PDFs that live inside `hardware/` (KiCad/Vero
  handoff exports) were left where they are — they're tied to their own project subfolders, not
  pitch material.
