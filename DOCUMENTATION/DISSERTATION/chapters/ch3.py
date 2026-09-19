# -*- coding: utf-8 -*-
"""Chapter 3: System Design — PFUMA/INGCEBO.

Grounded directly in backend/schema.sql, backend/app.py, backend/protocols.py
and src/components/IntelAI/PfumaIntelAI.jsx — every mechanism described here
was read from the running code, not inferred. 3.2 is left pending: the
guidelines template names it "Hardware Design", which does not apply to this
pure software submission (see CLAUDE.md section 4.1) — confirm the correct
heading with the supervisor before drafting it.
"""

HEADING = "CHAPTER 3 SYSTEM DESIGN"

REFKEYS = {}

SECTIONS = [
    {"heading": "3.1 INTRODUCTION", "body": [
        "This chapter presents the design of PFUMA/INGCEBO. Section 3.2 is "
        "held pending a heading decision explained below. Section 3.3 "
        "presents the software design: the overall system architecture, "
        "the alternatives considered and rejected for the technology "
        "stack, the database schema, the role-based access-control "
        "design, and the design of each of the platform's ten "
        "cross-cutting workflows in turn.",
    ]},

    {"heading": "3.2 [HEADING TO BE CONFIRMED WITH SUPERVISOR]", "body": [
        "[ Pending: the guidelines template names this section \"Hardware "
        "Design\"; PFUMA/INGCEBO has no hardware component in this "
        "submission (see CLAUDE.md section 4.1). Confirm with the "
        "supervisor whether to retitle, drop, or repurpose this section "
        "before drafting it. ]",
    ]},

    {"heading": "3.3 SOFTWARE DESIGN", "body": [

        {"subheading": "3.3.1 System Architecture"},
        "The platform follows a three-tier architecture. Two client "
        "applications, a React and Vite web application and an Expo and "
        "React Native mobile application, present the same role-tailored "
        "dashboard to a farmer, veterinary practitioner, supplier, "
        "buyer, police officer, or financial institution, each seeing "
        "only the functions relevant to that role. Both clients "
        "communicate over Hypertext Transfer Protocol with a single "
        "Flask application programming interface exposing 143 routes, "
        "which is the sole point of contact with the data tier: a single "
        "MySQL relational database. No client queries the database "
        "directly, and no business rule, such as withholding a listing "
        "from a buyer, is enforced on the client, since a client the "
        "farmer or buyer controls cannot be trusted to enforce a rule "
        "against its own user.",
        {"figure": {
            "number": "3.1",
            "caption": "Overall platform system block diagram",
            "path": "diagrams/fig_3_1_system_block.png",
        }},
        "A third client codebase, a WebView shell distributed as an "
        "installable mobile application, loads the web application's own "
        "interface rather than re-implementing it, and is therefore not "
        "a fourth architectural tier so much as an alternative packaging "
        "of the first.",

        {"subheading": "3.3.2 Design Concept Selection"},
        "Each major technology choice was made against a named "
        "alternative, not by default.",
        {"table": {
            "number": "3.1",
            "caption": "Technology choices and the alternative each was selected over",
            "headers": ["Layer", "Chosen", "Alternative considered", "Reason"],
            "rows": [
                ["Backend framework", "Flask", "Django",
                 "A role-based application programming interface with no "
                 "administrative site or templating need did not "
                 "justify Django's larger, more opinionated footprint."],
                ["Database", "MySQL", "SQLite",
                 "Two concurrent client codebases writing to a shared "
                 "database needed a real client-server engine with "
                 "proper concurrent-write handling, not a "
                 "single-file, single-writer database."],
                ["Authentication", "JSON Web Token", "Server-side session cookies",
                 "A mobile client with no shared browser cookie jar "
                 "needed a bearer token it could store and attach "
                 "itself, rather than a cookie tied to a browser "
                 "session."],
                ["Web frontend", "React with Vite", "Next.js",
                 "The platform is a role-based dashboard behind "
                 "authentication, not a public, search-indexed site, "
                 "so server-side rendering and routing conventions "
                 "aimed at public pages were not needed."],
                ["Mobile frontend", "Expo and React Native", "Flutter",
                 "Sharing one language, JavaScript, and a large share "
                 "of business logic with the web codebase outweighed "
                 "Flutter's rendering-performance advantage for a "
                 "forms-and-lists application of this kind."],
                ["In-app assistant", "Custom rule-based intent matching",
                 "A hosted third-party language model",
                 "A hosted model would have made every farmer query "
                 "leave the platform to an external provider, cost "
                 "money per call, and could answer a compliance "
                 "question incorrectly with no way to audit why; "
                 "a fixed, auditable rule set trades open-ended "
                 "conversation for answers that are always traceable "
                 "to a specific rule."],
            ],
        }},

        {"subheading": "3.3.3 Database Schema Design"},
        "The schema is organised around a single users table carrying a "
        "role column, restricted to the values Farmer, Veterinarian, "
        "Supplier, Buyer, Police, Admin and Institution, with "
        "role-specific columns, such as a veterinary licence number or a "
        "police badge number, left null for every other role rather than "
        "split across seven separate tables. Every other table names the "
        "role it belongs to through a foreign key back to users, which "
        "is what makes a single access-control layer, rather than one "
        "per role, possible. The core entities and their relationships "
        "are summarised in Table 3.2.",
        {"table": {
            "number": "3.2",
            "caption": "Core database entities and their relationships",
            "headers": ["Entity", "Key relationships", "Purpose"],
            "rows": [
                ["users", "referenced by every other table below",
                 "One account per role per person; a farmer and a "
                 "buyer sharing a phone number hold two separate rows."],
                ["animals", "belongs to a users row (owner)",
                 "Identity, breed, tag and brand marks for one "
                 "registered animal."],
                ["health_events / weight_history", "belongs to animals",
                 "An animal's health and growth timeline."],
                ["compliance_cases / compliance_actions",
                 "belongs to animals; references users (vet, owner)",
                 "The vaccination-compliance escalation ladder (3.3.6)."],
                ["marketplace_listings", "belongs to users (seller); "
                 "optionally links animals",
                 "A livestock, feed, produce, medicine or equipment "
                 "listing."],
                ["sale_clearances / movement_permits",
                 "belongs to marketplace_listings and animals; "
                 "references users (officer, vet)",
                 "Police and veterinary sign-off gating a livestock "
                 "sale (3.3.5)."],
                ["valuation_certificates / certificate_lookups",
                 "belongs to animals; references users (issuer, "
                 "institution)",
                 "Vet-issued valuation and its institution-side "
                 "ledger (3.3.7)."],
                ["outbreaks", "references users (reporter, verifier)",
                 "A disease report and its verify-then-broadcast "
                 "state (3.3.8)."],
                ["cooperatives / cooperative_members / "
                 "cooperative_dip_schedule / cooperative_vet_requests",
                 "belongs to users (creator, members)",
                 "A shared farmer group and its dip-tank schedule "
                 "(3.3.9)."],
                ["feed_types / feeding_plans", "belongs to animals, users",
                 "The feed-formulation ration builder (3.3.9)."],
                ["conversations / conversation_messages",
                 "references users (both parties)",
                 "The cross-role messenger (3.3.10)."],
            ],
        }},
        {"figure": {
            "number": "3.3",
            "caption": "Simplified entity-relationship diagram",
            "path": "diagrams/fig_3_3_entity_relationship.png",
        }},

        {"subheading": "3.3.4 Role-Based Access-Control Design"},
        "Every authenticated request carries a JSON Web Token issued at "
        "login or registration, naming the requesting user's identifier "
        "and role; the server resolves the current user from that token "
        "on every request rather than trusting a role value the client "
        "might send. Data scoping follows from the same mechanism: a "
        "farmer's query for animals is always filtered to rows the "
        "farmer owns, and a police officer's or veterinary practitioner's "
        "oversight queries are scoped to their assigned province or "
        "district unless their officer_tier column is set to national, "
        "which is an administrator-assigned distinction a user cannot "
        "grant themself. The Admin role is deliberately undiscoverable: "
        "a protected route requested by a non-administrator returns the "
        "same not-found response a route that genuinely does not exist "
        "would return, rather than a forbidden response that would "
        "confirm the route exists. A newly registered account carries a "
        "verification_status of pending and is queued for a Police "
        "officer, or, for a Veterinarian applicant, an already-verified "
        "peer, to resolve to verified or rejected before the account is "
        "treated as fully trusted elsewhere in the platform — the same "
        "pending-to-resolved pattern described fully in 3.3.5 and shown "
        "in Figure 3.2.",

        {"subheading": "3.3.5 Marketplace and Sale-Clearance Workflow Design"},
        "A marketplace listing carries a status of pending_clearance, "
        "available, sold or withdrawn. A listing created against a "
        "registered animal starts as pending_clearance and is excluded "
        "from the public listings query, which filters strictly on "
        "status equals available, until a police officer resolves a "
        "linked sale_clearances row to cleared. That row digitises the "
        "Zimbabwe Republic Police's own paper Form 392 Livestock "
        "Clearance Certificate field for field, including an optional "
        "traditional-authority attestation by a village head or chief "
        "for communal-area sales, and a separate movement_permits table "
        "digitising the Department of Veterinary Services' Form V27 for "
        "a cross-district move. Unlike a sale clearance, a movement "
        "permit is issued by a veterinary practitioner rather than a "
        "police officer, requiring the vet's professional rank, VEA, AHI "
        "or GVO, and an uploaded signature before the permit number is "
        "generated, matching the paper form's own requirement that "
        "nothing is authorised until that line is signed. A sale "
        "arranged off the platform, for "
        "example between neighbours, is additionally supported through a "
        "short transfer code a seller generates and a buyer redeems, "
        "which moves ownership and the animal's full history the same "
        "way an ordinary marketplace sale does.",
        "The clearance itself follows a single pattern reused four times "
        "across the platform, shown in Figure 3.2: an action is created "
        "and immediately held pending, an authority reviews it, and it is "
        "then either released, becoming visible or effective, or "
        "rejected and kept hidden. The same shape governs a new "
        "account's signup verification (3.3.4), a movement permit "
        "(above), and an outbreak report before it broadcasts (3.3.8) — "
        "it is one mechanism applied four times, not four separate ones.",
        {"figure": {
            "number": "3.2",
            "caption": "The shared verification-gate state pattern",
            "path": "diagrams/fig_3_2_verification_pattern.png",
        }},

        {"subheading": "3.3.6 Health-and-Compliance Lifecycle Design"},
        "A server-side protocol table, independent of anything the "
        "client sends, names every mandatory vaccination per species "
        "together with the animal age it first falls due and, where "
        "applicable, its recurrence interval. A missed mandatory "
        "vaccination does not merely mark a dashboard red; it opens a "
        "compliance_cases row that escalates through a fixed stage "
        "ladder, reminder, then vet follow-up, then a formal notice, "
        "then a penalty. The penalty is a trade lock confined to that "
        "one animal, not a monetary fine the platform has no lawful way "
        "to collect and no right to impose on a subsistence farmer. A "
        "farmer may instead declare a blocker, such as the vaccine being "
        "out of stock or no veterinary officer having visited the ward, "
        "which pauses the ladder without penalty and routes the case to "
        "whichever party, a supplier, a dispatched vet, or the farmer's "
        "cooperative, can actually resolve it. Every stage transition is "
        "written to a separate compliance_actions row, so a lockout can "
        "always be explained, and disputed, after the fact.",

        {"subheading": "3.3.7 Certification and Institution-Ledger Design"},
        "An animal's owner, or an administrator, may issue a "
        "valuation_certificates row for that animal, carrying a unique "
        "verification code; the certificate's value is not "
        "client-supplied but computed server-side from the animal's "
        "current weight, a per-species market rate, and a bonus derived "
        "from the count of health_events logged against that animal, so "
        "a veterinary practitioner's role is indirect, through the "
        "health events a certificate's value is partly built from, "
        "rather than through issuing the certificate itself. That code "
        "can be resolved through a public endpoint requiring no "
        "PFUMA/INGCEBO account, so a bank or insurer's loan officer can "
        "check it directly. A financial institution that looks a "
        "certificate up may additionally flag it in a "
        "certificate_lookups row as held collateral, which lets a second "
        "lender see that a certificate is already pledged without either "
        "institution learning who the other is.",

        {"subheading": "3.3.8 Outbreak-Reporting Pipeline Design"},
        "A disease outbreak reported by a veterinary practitioner or "
        "police officer is written with a verified_status of pending "
        "and is not visible to farmers in that province. It becomes "
        "visible, functioning as a broadcast alert, only once an officer "
        "whose own officer_tier is national resolves it to verified, "
        "which is the same pending-to-verified-to-released pattern used "
        "for sale clearance in 3.3.5, applied here to prevent a single "
        "unreviewed field report from triggering a province-wide panic "
        "notification.",

        {"subheading": "3.3.9 Cooperative, Feed and Trading-Journal Design"},
        "A cooperative row groups farmer members who share a physical "
        "dip tank; any member may propose a dip_schedule entry or raise "
        "a cooperative_vet_requests row on the group's behalf, so a "
        "veterinary practitioner sees one consolidated request rather "
        "than each member messaging individually. Independently, a "
        "feeding_plans row is generated by computing a specific animal's "
        "daily protein and energy requirement from its species, weight "
        "and life stage, then pricing candidate feed_types items against "
        "live marketplace listings where a price exists, and recording "
        "whether the resulting ration is deficient, balanced or in "
        "excess against that requirement. The trading journal is a "
        "separate, read-only summary restricted to the Supplier and "
        "Buyer roles: a supplier's view totals their own fulfilled "
        "orders, and a buyer's view totals their own accepted bids, each "
        "against the same orders and bids rows the marketplace already "
        "writes, so no farmer-facing sale/purchase history is kept "
        "under this name.",

        {"subheading": "3.3.10 Messenger and Jinda Assistant Design"},
        "The cross-role messenger is deliberately general-purpose: a "
        "conversation is a thread between any two verified users, not a "
        "mechanism restricted to a fixed pair of roles, so a farmer, a "
        "veterinary practitioner, a supplier, a buyer, a police officer "
        "and an institution can each reach any other directly. The "
        "in-app assistant, named Jinda, is implemented as deterministic "
        "rule-based intent matching rather than a hosted language model: "
        "an incoming message is scanned with whole-word regular "
        "expressions against alias dictionaries for species and role, "
        "checked against a fixed, priority-ordered list of intents, for "
        "example a police-only clearance query is only ever matched for "
        "a police account, and, where no specific intent matches, "
        "against a navigation keyword table that switches the "
        "requesting client to the relevant screen. The assistant also "
        "recognises marker words for Shona and Ndebele, Zimbabwe's two "
        "most widely spoken indigenous languages alongside English, so a "
        "query typed in either is still routed correctly. Because every "
        "answer traces back to a named rule rather than a statistical "
        "model's output, an incorrect answer can be located and fixed "
        "at its source, which a hosted model's output cannot.",
    ]},

    {"heading": "3.4 CONCLUSION", "body": [
        "This chapter has presented the platform's three-tier "
        "architecture, the alternative rejected for each major "
        "technology choice, the shared database schema underlying every "
        "role, and the design of each of the ten cross-cutting workflows "
        "in turn. Chapter 4 reports the results of exercising this "
        "design against the running platform.",
    ]},
]
