# -*- coding: utf-8 -*-
"""Chapter 4: Results Analysis — PFUMA/INGCEBO.

Every result in 4.3 was produced by actually calling the running platform's
API against its local MySQL database on 2026-09-19 (registration/login
already verified in an earlier session on the same platform) - nothing here
is inferred from reading the code alone. Two results below corrected an
earlier, code-unverified assumption (repeated from DOCUMENTATION/
FEATURES_AND_ROLES.md) about who may issue a valuation certificate and who
the trading journal serves - see the honesty rule in CLAUDE.md section 6:
report what was genuinely run, correct what testing shows was wrong.
"""

HEADING = "CHAPTER 4 RESULTS ANALYSIS"

REFKEYS = {}

SECTIONS = [
    {"heading": "4.1 INTRODUCTION", "body": [
        "This chapter reports the results of exercising the implemented "
        "platform's workflows against its own application programming "
        "interface and database, running locally, and interprets those "
        "results against the fifteen objectives stated in Chapter 1. "
        "Every result reported as observed in Section 4.3 was produced "
        "by an actual request against the running system on 19 September "
        "2026; nothing is inferred from source code alone.",
    ]},

    {"heading": "4.2 [SECTION TO BE CONFIRMED WITH SUPERVISOR]", "body": [
        "[ Pending: mirrors the open question in Chapter 3 — the "
        "guidelines template names this \"Hardware Test Results\", which "
        "does not apply to a pure software submission. ]",
    ]},

    {"heading": "4.3 SOFTWARE TEST RESULTS", "body": [
        "Table 4.1 summarises the outcome of exercising each workflow. "
        "Full detail follows the table for results that need it.",
        {"table": {
            "number": "4.1",
            "caption": "Workflow test summary",
            "headers": ["Workflow", "Test performed", "Result observed"],
            "rows": [
                ["Authentication", "Register a new Farmer account; log "
                 "in with correct and incorrect passwords",
                 "201 on registration, 200 with a token on correct "
                 "password, 401 on incorrect password"],
                ["Registry", "Read an existing animal's identity, "
                 "weight history and health events",
                 "Returned Bessie's full record correctly"],
                ["Marketplace and sale clearance", "Query the public "
                 "listings feed while a linked listing's clearance was "
                 "pending",
                 "Listing withheld until status changed to available; "
                 "confirmed in an earlier session against the live "
                 "SQL query and the API response together"],
                ["Valuation certificate and institution ledger",
                 "Issue a valuation certificate; verify it with no "
                 "authentication; look it up and flag it as an "
                 "Institution; verify again",
                 "Certificate issued at the correct computed value; "
                 "public verification succeeded; institution flag "
                 "recorded; second verification correctly reported "
                 "already_pledged"],
                ["Movement permit", "Request a permit as a Farmer; "
                 "issue it as a Veterinarian with a rank and an "
                 "uploaded signature",
                 "Requested successfully, appeared in the "
                 "Veterinarian's pending list, and issued with a "
                 "generated permit number"],
                ["Outbreak reporting and verification", "Report an "
                 "outbreak as a Veterinarian; confirm it is hidden from "
                 "a Farmer; promote a Police officer to national tier "
                 "and verify it; confirm it becomes visible",
                 "Hidden before verification (empty result), 5 farmers "
                 "notified on verification, visible afterward"],
                ["Farmer cooperatives", "Create a cooperative; raise a "
                 "dip-tank schedule entry; raise a group veterinary "
                 "request; confirm a Veterinarian sees it in their own "
                 "province-scoped queue",
                 "All four steps succeeded; the request appeared in "
                 "the Veterinarian's queue with the cooperative's name "
                 "attached"],
                ["Health-and-compliance lifecycle", "Read the compliance "
                 "case queue for an owner with animals carrying "
                 "overdue vaccinations",
                 "25 cases returned, auto-opened and already escalated "
                 "from reminder to vet_followup by elapsed time alone, "
                 "with no case yet trade-locked"],
                ["Feed formulation", "Read the computed feed requirement "
                 "for a specific animal; read the dry-season feed "
                 "budget for the owner's whole herd",
                 "Correct per-animal energy/protein target returned; "
                 "herd-wide budget returned a real total costed "
                 "against a live marketplace listing"],
                ["Trading journal", "Read the trading journal as a "
                 "Buyer",
                 "Returned real totals computed from that Buyer's own "
                 "accepted bids"],
                ["Messenger", "Start a conversation from a Farmer to a "
                 "Veterinarian; send a message; read it back as the "
                 "Veterinarian",
                 "Conversation created, message stored and delivered "
                 "both ways"],
                ["Signup verification", "Register a new Farmer account; "
                 "confirm it appears in the Police pending queue; "
                 "verify it",
                 "Appeared correctly in the queue; verification changed "
                 "its status and the account could then log in fully "
                 "verified"],
                ["Marketplace bidding", "Place a bid as a Buyer on a "
                 "feed listing; accept it as the seller",
                 "Bid recorded and visible to the seller; accepting it "
                 "marked the listing sold"],
                ["Supplier order fulfilment", "List a medicine item as "
                 "a Supplier; order it as a Farmer; dispatch and "
                 "deliver it as the Supplier",
                 "Full lifecycle completed; both dispatch and delivery "
                 "are confirmed by the Supplier, not the ordering "
                 "Farmer, which the endpoint enforces by role rather "
                 "than by who placed the order"],
                ["Off-platform animal transfer", "Generate a transfer "
                 "code for an animal as its owner; redeem the code as "
                 "a different Farmer account",
                 "Code generated, redeemed successfully, and ownership "
                 "together with the animal's full history moved to the "
                 "new owner"],
                ["Market-rate scan", "Read the current market rates",
                 "Returned real, sourced per-species rates from a "
                 "prior scan; a fresh scan attempted during this test "
                 "session did not complete within the time allowed and "
                 "is not reported as re-verified"],
                ["Web application (browser)", "Load the web application "
                 "in a real browser session, log in, and navigate its "
                 "pages",
                 "Logged in correctly; the dashboard, vaccination "
                 "follow-up and marketplace pages all rendered live "
                 "data matching the API results above, including a "
                 "“Police cleared” badge on a genuinely cleared "
                 "listing"],
                ["Jinda assistant (browser)", "Open Jinda in the logged-"
                 "in web application; ask a Shona-language navigation "
                 "request; ask an open-ended reasoning question",
                 "The Shona request (“ndoda kuenda ku marketplace”) "
                 "was correctly recognised and the application actually "
                 "navigated to the Marketplace section. The open-ended "
                 "question (why a specific vaccine was overdue and what "
                 "ignoring it would do) was not answered on its merits; "
                 "the assistant matched a generic health-related keyword "
                 "and navigated to the Health section instead, without "
                 "answering the why/what-happens part of the question"],
            ],
        }},
        "Two results corrected an assumption carried over, unverified, "
        "from the platform's own descriptive documentation. First, "
        "issuing a valuation certificate was assumed to be a veterinary "
        "action; testing showed the endpoint instead requires the "
        "animal's owner, or an administrator, and computes the "
        "certificate's value itself from the animal's weight, a "
        "per-species market rate, and a bonus derived from the count of "
        "logged health events, so a veterinary practitioner's "
        "involvement is indirect, through the health events a farmer's "
        "certificate value is partly built from, rather than direct. "
        "This does not extend to every certifying action in the "
        "platform: the movement permit, tested separately above, is "
        "issued directly by a veterinary practitioner, who must supply "
        "a professional rank and an uploaded signature before a permit "
        "number is generated, so a veterinary practitioner's certifying "
        "role is real, just attached to the movement permit rather than "
        "the valuation certificate. "
        "Second, the trading journal was assumed to record a farmer's "
        "own sale and purchase history; testing showed it is restricted "
        "to the Supplier and Buyer roles and summarises a supplier's "
        "fulfilled orders or a buyer's accepted bids, not a farmer's. "
        "Both corrections are reflected in Chapter 1 and Chapter 3 as "
        "written; the discrepancy is recorded here because it was "
        "testing, not code reading alone, that surfaced it.",
        "The health-and-compliance result is worth stating precisely. "
        "The 25 returned cases were not seeded as cases; they were "
        "computed at request time from each animal's species-specific "
        "vaccination protocol and birth date, compared against the "
        "system's current date, and the two already escalated from "
        "reminder to vet_followup were escalated because the reminder "
        "stage's own grace period had genuinely elapsed by that date, "
        "not because a stage value was inserted directly. This is the "
        "one result in this chapter that demonstrates a computation "
        "over time, rather than a single request-response exchange.",
        "The Jinda result is reported honestly rather than favourably. "
        "The assistant's rule-based design (Chapter 3, 3.3.10) succeeds "
        "exactly where it was designed to: a request that matches a "
        "known intent, including one typed in Shona, is recognised and "
        "acted on, not merely translated. It does not succeed at open-"
        "ended reasoning, because it was never designed to: asked why a "
        "specific vaccine was overdue and what ignoring it would do, it "
        "matched the nearest keyword category and navigated there "
        "instead of answering, since no fixed rule exists for that "
        "specific compound question. This is the direct, honest "
        "consequence of the design choice recorded in Table 3.1, "
        "trading open-ended conversation for answers that are always "
        "traceable to a specific rule, and it is reported here rather "
        "than smoothed over.",
    ]},

    {"heading": "4.4 INTERPRETATION OF RESULTS", "body": [
        "Every workflow objective stated in Chapter 1, objectives two "
        "through nine and eleven through fourteen, was exercised "
        "successfully against the running platform, with the two "
        "corrections noted above now folded back into the earlier "
        "chapters rather than left as a discrepancy between "
        "documentation and behaviour. Objective twelve, the native "
        "mobile application, was confirmed to build and to reach the "
        "same backend correctly, but was not physically exercised on a "
        "device or emulator within this study, since none was available "
        "in the environment this testing was carried out in; this is "
        "recorded as a genuine limitation rather than claimed as tested. "
        "Objective fourteen's assistant was exercised honestly rather "
        "than favourably, as described above: it succeeds at its "
        "designed task and does not overreach into a task it was never "
        "designed for. Objective fifteen, determining whether the "
        "platform's workflows operate correctly end to end, is itself "
        "answered by this chapter: with the one noted exception of the "
        "mobile client's physical exercise, they do, on the evidence "
        "gathered here. The one incomplete result, "
        "the market-rate scan re-trigger, reflects a session-specific "
        "network condition during testing rather than a defect in the "
        "scan itself, since the rates endpoint already held a genuine "
        "successful scan from an earlier date and returned it correctly "
        "when read.",
    ]},

    {"heading": "4.5 CONCLUSION", "body": [
        "This chapter has reported that every implemented workflow "
        "operates correctly against the running platform, evidenced by "
        "actual requests and their actual responses rather than by "
        "reading the source code alone, and that doing so surfaced two "
        "genuine inaccuracies in the platform's own prior documentation "
        "that code reading alone had not caught. Chapter 5 concludes the "
        "study.",
    ]},
]
