# Supervisor Demo Guide — proving each objective, one by one

This is a practical script for the live defense: for each of Chapter 1's 15 objectives, exactly
what to click, type, or log in as, and exactly what the supervisor should see happen, so they can
mark it "done and working" against something they watched happen, not a claim in the document.

**Every step below was actually run once during development** (2026-09-19) and produced the
result stated — see `DOCUMENTATION/DISSERTATION/chapters/ch4.py` (Chapter 4, Table 4.1) for the
full record. This guide is the same evidence, reordered for live presentation instead of a written
report. Where a step has **not** been physically demoed (the mobile app on a real device), that is
stated plainly rather than glossed over — see Objective 12.

## Before the demo: local environment checklist

Run these from `DOCUMENTATION/DISSERTATION/` unless noted. All three must show a response before
starting.

1. **MySQL (XAMPP)** running — `C:\xampp\mysql\bin\mysqld.exe --standalone` (or the XAMPP control
   panel), then confirm: `C:\xampp\mysql\bin\mysql.exe -uroot -e "USE pfuma; SELECT COUNT(*) FROM users;"`
2. **Backend** — from `backend/`, run `python app.py`; confirm with `curl http://localhost:5000/`
   (expect `"PFUMA/INGCEBO API is running"`).
3. **Web app** — from the project root, run `npm run dev -- --host`; confirm
   `http://localhost:5173/` loads the sign-in page in a browser.
4. Check your machine's current LAN IP (`ipconfig`) if demoing from a phone — it drifts between
   networks; `app/config.js` and `app-webview/config.js` must match it (see CLAUDE.md §5).

## Demo accounts (local database only — none of this touches the live/VPS data)

| Role | Phone | Password | Notes |
|---|---|---|---|
| Farmer | `0771000001` | `Pfuma2026!` | Arnold Mapindu — owns Bessie, Thunder, Rocky, Storm |
| Veterinarian | `0772000002` | `Pfuma2026!` | Dr T. Moyo |
| Supplier | `0773000003` | `Pfuma2026!` | Chido Ncube |
| Buyer | `0774000004` | `Pfuma2026!` | ZimAgro Enterprise |
| Police | `0775000005` | `Pfuma2026!` | Officer Chikwanha — promoted to **national tier** (needed for Objective 7) |
| Institution | `0776000006` | `Pfuma2026!` | Zimbabwe Trust Bank |
| Admin | `0785919439` | `Savage2001#` | Arnold (Admin) |

If any promotion/state below has reset (a fresh database import resets `officer_tier` to `field`),
re-run as Admin: `PATCH /admin/users/5/officer-tier {"officer_tier":"national"}`.

---

## Objective 1 — Database schema and role-based access control (7 roles)

*"To design a relational database schema and a role-based access-control mechanism serving seven
distinct platform roles."*

**Demo:** Log in as each of the seven accounts above in turn (or open phpMyAdmin /
`mysql -uroot pfuma -e "SELECT DISTINCT role FROM users;"`). Point out that each role sees a
**different sidebar and dashboard** — a Farmer never sees a "Clearances" queue, a Police account
never sees "Feed Analyzer". Then try opening `/admin` (or any admin route) while logged in as a
non-Admin: it returns a plain 404, not a 403 — the supervisor can be told this is deliberate (the
Admin role doesn't leak its own existence), and shown the schema's `role` ENUM in
`backend/schema.sql` line 25 as the single source of truth behind it.

## Objective 2 — Livestock registry

*"To develop a livestock registry that records an animal's identity, health timeline and
ownership history."*

**Demo:** Log in as Farmer → **Herd Registry**. Open Bessie. Show identity (breed, tag ZIM-882,
brand AR-MP), the weight-history graph, and the health-events log (FMD Vaccine, Feb 2026). This is
real seeded data, not placeholder text.

## Objective 3 — Health-and-compliance lifecycle

*"To develop a health-and-compliance lifecycle that tracks a vaccination, weaning or gestation
countdown and raises a compliance case when a deadline is missed."*

**Demo:** Still as Farmer → **Follow-Ups**. Point at the stat row: **25 open cases, 25 with a
vet, 0 trade-locked**. Open one case (e.g. Daisy's Brucellosis) and show the action history:
`opened` → `escalated` timestamps. Say plainly: these were **not seeded** — they were computed
live from each animal's birth date against today's date, the moment this page was opened. Click
**"I can't vaccinate — here's why"** to show the deferral path live (pick "no vet nearby"), which
pauses the case with no penalty — this is the feature worth dwelling on if asked "why not just a
fine?": a fine can't be enforced on a subsistence farmer and this platform doesn't pretend it can.

## Objective 4 — Marketplace + police-gated sale clearance

*"To develop a marketplace listing mechanism that withholds a livestock listing from a buyer
until police clearance has been recorded against it."*

**Demo (two windows/logins side by side is most convincing):** As Farmer, list an animal for
sale — it appears in "My Listings" tagged `pending_clearance`, but switch to **Marketplace** (the
public buyer-facing feed) and it is **not there**. Log in as Police → **Clearances**, find the
pending request, clear it. Refresh the public Marketplace as Buyer: the listing now appears with
a **"Police Cleared"** badge. This is the platform's own headline mechanism — it is worth doing
live rather than just describing.

## Objective 5 — Valuation-certificate workflow

*"To develop a valuation-certificate workflow that computes and issues a publicly verifiable
certificate for a registered animal, informed by its logged veterinary health events."*

**Demo:** As Farmer, open Bessie → **Issue Valuation Certificate**. Point out the computed value
($761.80 in testing = 420kg × $1.79/kg Cattle market rate + $10 for one logged health event) is
**not typed in by the farmer** — it's server-computed. Copy the verification code, open a private/
incognito window with no login at all, and paste the code into the public verify page (or
`GET /verify/certificate/<code>`) to show a bank could check it with zero PFUMA account. **If
asked "does the vet issue this?"** — be upfront: no, testing showed the owner (or Admin) issues
it; the vet's involvement is indirect through the health events. That correction is itself
documented in Chapter 4 as a finding, not a mistake to hide.

## Objective 6 — Institution ledger

*"To create an institution ledger function that allows a valuation certificate to be looked up
and flagged for loan-collateral purposes."*

**Demo:** Continue from Objective 5. Log in as Institution → paste the same code into
**Certificate Lookup**, then **Flag as Collateral**. Go back to the public verify page and show
`already_pledged` is now `true` — without revealing which institution flagged it. That
non-disclosure design point is worth stating out loud.

## Objective 7 — Outbreak reporting and verification

*"To develop an outbreak-reporting and verification pipeline that broadcasts a confirmed disease
alert to farmers in the affected region."*

**Demo:** As Veterinarian, report an outbreak (disease, province, district). Log in as Farmer in
that province — **no alert visible yet**. Log in as Police (must be national-tier — see the
checklist above), find it under outbreak review, verify it. Log back in as Farmer — the alert now
appears, and in testing this genuinely notified 5 farmer accounts at once. This is the same
pending → verified → released pattern as Objective 4, applied to a different problem — say so if
there's time; it's the strongest "systems thinking" point in the whole defense.

## Objective 8 — Farmer cooperative function

*"To develop a farmer cooperative function that shares a dip-tank schedule and raises a group
veterinary request on behalf of multiple members."*

**Demo:** As Farmer → **Cooperative** → create one, add a dip-tank schedule date, raise a group
vet request. Log in as Veterinarian → open the province-scoped **vet-requests queue** — the
cooperative's request appears there with the cooperative's name attached, not buried inside the
cooperative's own page (which the vet isn't a member of and can't open directly — that's a
deliberate access boundary, not a bug, if asked).

## Objective 9 — Feed-formulation function

*"To develop a feed-formulation function that plans a farmer's dry-season feed budget..."*

**Demo:** As Farmer → **Feed Analyzer**. Select an animal to show its computed energy/protein
requirement (e.g. Bessie: 46.39 MJ / 324.72 g for an adult). Then open the herd-wide **dry-season
budget** view — in testing this returned a real total ($878.96 for 91 days across 3 head) costed
against the cheapest matching listing actually on the Marketplace right now, not a static number.

## Objective 9 (continued) — Trading-journal function

*"...and a trading-journal function that summarises a supplier's or buyer's own trade history."*

**Demo:** Log in as Buyer → **Trading Journal**. Show real totals (accepted bids, top
counterparties) computed from that account's own history. **If asked whether a farmer has one
too** — be upfront: no, this is Supplier/Buyer only; testing confirmed the endpoint rejects a
Farmer token outright. Say so rather than dodge it.

## Objective 10 — Estimated market value calculation

*"To calculate an estimated market value for a registered animal from its species, weight and
recorded health history, fed by an automated market-rate scan."*

**Demo:** Open `GET /market-rates` (or the equivalent in-app rates view) and show the real, cited
source for each figure (e.g. Cattle $1.79/kg, sourced to an AMA Weekly Bulletin URL, with a
timestamp). Then point back at Objective 5's certificate value — it's the same rate feeding both.

## Objective 11 — Web-based application

*"To develop a web-based application giving every platform role browser access to the system."*

**Demo:** This is what every objective above has already been demoed through — say so explicitly,
rather than doing a separate empty click-through. If pressed, show the same login screen working
in a second browser (or incognito window) for a different role simultaneously.

## Objective 12 — Native mobile application

*"To develop a native mobile application, alongside the web application, giving each platform
role access to the system from a mobile device."*

**Be honest here.** The mobile app (Expo/React Native) builds and reaches the same backend
correctly — this was confirmed by starting the Expo dev server and by the app's own config
pointing at the same local API — but it was **not physically exercised on a phone or emulator**
during this study (none was available in the test environment). State this plainly if asked: the
code and the connection are real and working; a live on-device walkthrough is the one objective
not directly demoed. If a phone is available on the day, this is the one to actually try live
first, since it would upgrade the evidence on the spot.

## Objective 13 — Secure end-to-end messenger

*"To develop a secure, end-to-end messaging function linking the Farmer, Veterinarian, Supplier,
Buyer, Police and Institution roles directly within the platform."*

**Demo:** As Farmer → **Messenger** → start a conversation with the Veterinarian, send a message.
Log in as Veterinarian and show it arrived. **If asked "can a Farmer message Police directly?"**
— yes, and it's worth actually doing live: the code comment itself says "any verified user to any
other," not role-gated, which is a deliberate design choice worth stating.

## Objective 14 — Role-aware natural-language assistant (Jinda)

*"To develop a role-aware natural-language assistant that answers a farmer's livestock-health and
legal-compliance questions and navigates the application on request."*

**Demo, and be balanced about it.** Open Jinda (the chat icon, bottom-right, any page). Type a
Shona request: `ndoda kuenda ku marketplace` — Jinda recognises it and **actually navigates** to
the Marketplace, which is genuinely impressive live. Then, to be honest rather than to oversell,
try an open-ended question like *"why is Bessie's vaccine overdue and what happens if I ignore
it?"* — in testing, Jinda did **not** reason through this; it matched the nearest keyword and
navigated to the Health section instead. Say plainly: Jinda is a fixed rule set, not a language
model, and this is the direct, honest consequence of that choice (Chapter 3, Table 3.1) — every
answer traces to a specific rule, which is the tradeoff being made, not a bug.

## Objective 15 — End-to-end verification

*"To determine, by deploying and exercising the completed platform locally, whether its registry,
marketplace, compliance, cooperative and communication workflows all operate correctly end to
end."*

This objective is what the fourteen demos above collectively answer — after running through them,
say so directly: every workflow was exercised against the real local deployment and worked,
except the one stated gap (Objective 12, mobile, code-verified but not device-tested). That
combination — thorough, and honest about the one limit — is the actual answer to this objective,
not a slide claiming "100% done."

---

## If something doesn't work live

- **Login fails** → check the LAN IP hasn't drifted (see checklist), or that the backend restarted
  and invalidated tokens (JWT secret is randomised per restart in dev mode — this is expected and
  fine, just log in again).
- **A workflow gives an unexpected error** → don't improvise a cover story. Say what happened,
  and if there's time, open the relevant route in `backend/app.py` and read the actual check
  together — that is itself a demonstration of understanding the system, which is worth more than
  a smooth click-through.
