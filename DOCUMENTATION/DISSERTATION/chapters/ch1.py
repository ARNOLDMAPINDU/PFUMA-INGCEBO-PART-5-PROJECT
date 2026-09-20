# -*- coding: utf-8 -*-
"""Chapter 1: Introduction — PFUMA/INGCEBO.

House style (see CLAUDE.md section 4.2): passive voice, third person,
continuous prose, British/Zimbabwean spelling, measurable-verb objectives.
Citations are real, sourced Zimbabwean statutes already researched and
cross-checked against multiple sources in compliance/laws/ — nothing here
is an invented literature citation.
"""

HEADING = "CHAPTER 1 INTRODUCTION"

REFKEYS = {
    "ZW-STOCK-THEFT-ACT": (
        "Zimbabwe (1959, as amended 2001). Stock Theft Prevention Act "
        "[Chapter 9:18]. Harare: Government of Zimbabwe."
    ),
    "ZW-ANIMAL-HEALTH-ACT": (
        "Zimbabwe. Animal Health Act [Chapter 19:01]. Harare: Government "
        "of Zimbabwe."
    ),
    "ZW-BRANDS-ACT": (
        "Zimbabwe (1900, as amended). Brands Act. Harare: Government of "
        "Zimbabwe."
    ),
    "ZW-VET-SURGEONS-ACT": (
        "Zimbabwe. Veterinary Surgeons Act [Chapter 27:15]. Harare: "
        "Government of Zimbabwe."
    ),
}

SECTIONS = [
    {"heading": "1.1 INTRODUCTION", "body": [
        "This chapter introduces PFUMA/INGCEBO, a role-based digital "
        "platform developed to turn livestock ownership, health history "
        "and sale history into a record that a third party can trust and "
        "check, in place of paper, memory, or a stranger's word. The "
        "chapter sets out the background against which the platform was "
        "developed, states the problem being addressed, presents the "
        "solution, the aim and the objectives of the study, justifies the "
        "work, defines its scope, states its limitations and "
        "delimitations, and describes how the remainder of the document "
        "is organised.",
    ]},

    {"heading": "1.2 BACKGROUND", "body": [
        "Livestock is frequently the largest store of wealth held by a "
        "rural Zimbabwean household, and it is commonly the least "
        "protected asset that household owns. Ownership, vaccination "
        "history, weaning and gestation dates, and past sales are "
        "typically tracked on paper, by memory, or not tracked at all. A "
        "record kept this way can be lost, forged, or simply never have "
        "existed, and it cannot be produced quickly when it is needed "
        "most: at the point of sale, at a police checkpoint, or when a "
        "bank is asked to lend against the animal as collateral.",
        "Zimbabwean law already recognises how serious the resulting gap "
        "is. The Stock Theft Prevention Act criminalises the theft of "
        "stock and produce, and receiving stock known or reasonably "
        "suspected to be stolen, and it places a duty on traders to keep "
        "transaction registers precisely because an undocumented sale is "
        "the easiest route for a stolen animal to be laundered into "
        "legitimate trade [[ZW-STOCK-THEFT-ACT]]. In ordinary practice, a "
        "livestock sale in Zimbabwe is expected to pass through an "
        "ownership check, a veterinary inspection, and a police clearance "
        "before it is considered safe, but this process is currently a "
        "manual, paper-based one, carried out separately by a village "
        "head, a veterinary officer and a police officer with no shared "
        "system connecting their records.",
        "A parallel identification framework requires cattle to be "
        "branded and, in newer regulation, tagged, with the brand "
        "encoding the owner, the village of origin, the dip tank and the "
        "district the animal belongs to [[ZW-BRANDS-ACT]]. Disease "
        "control is likewise governed by statute: notifiable diseases "
        "must be reported, and the state holds quarantine and movement "
        "powers precisely because an outbreak can spread faster than "
        "paper record-keeping and word-of-mouth warning can respond to it "
        "[[ZW-ANIMAL-HEALTH-ACT]]. Veterinary practice itself is a "
        "regulated profession, with practitioners required to be "
        "registered before they may certify an animal's health "
        "[[ZW-VET-SURGEONS-ACT]]. Each of these legal instruments assumes "
        "a functioning paper trail; none of them currently has a shared "
        "digital system behind it.",
        "A related, more commercial gap sits alongside the legal one. A "
        "farmer with an animal to sell has no reliable way to find a "
        "buyer known to be creditworthy and genuine, and no independent "
        "figure to point to when negotiating a price, so a sale is "
        "commonly conducted by word of mouth, with a wandering buyer "
        "offering whatever price the farmer cannot readily check against "
        "anything. Certified buyers and a credible valuation are, in "
        "practice, as hard to find as a clean ownership record is.",
    ]},

    {"heading": "1.3 PROBLEM STATEMENT", "body": [
        "Proof of a livestock asset's ownership and health history does "
        "not currently exist in a form that a third party, whether a "
        "buyer, a police officer, or a bank, can independently trust. The "
        "professionals who each create part of that history in the "
        "course of their work, namely the farmer, the veterinary "
        "practitioner, and the police officer performing a clearance, "
        "have no shared system in which to record it, so each keeps a "
        "separate, private, and often paper-based account. The result is "
        "that a buyer cannot verify what is being purchased before "
        "paying, a police officer cannot quickly confirm that a listed "
        "animal has actually been cleared, a bank or insurer cannot treat "
        "livestock as usable loan collateral because no verifiable record "
        "of its value or ownership history exists to lend against, and a "
        "farmer with an animal to sell has no efficient way to reach a "
        "buyer known to be certified and genuine or to point to a "
        "credible, independent valuation when a price is negotiated.",
    ]},

    {"heading": "1.4 SOLUTION", "body": [
        "PFUMA/INGCEBO was developed as a multi-role web and mobile "
        "platform that connects the farmer, the veterinary practitioner, "
        "the supplier, the buyer, the police officer, and a financial "
        "institution into one shared record. Because every account on "
        "the platform has already passed the same signup-verification "
        "gate described above, a buyer reached through the marketplace "
        "is a certified one by construction, rather than a stranger a "
        "farmer must take on faith. Every registered animal "
        "carries an identity, a health timeline and an ownership history "
        "that each authorised role can contribute to and check. A "
        "livestock listing created for sale is held back from buyers "
        "until a police officer has recorded clearance against it, "
        "reproducing in software the ownership-and-clearance sequence "
        "already expected of a lawful sale. An animal's owner can issue "
        "a valuation certificate carrying a code that anyone, including "
        "a bank or insurer, can look up independently; its value is "
        "computed by the platform itself from the animal's weight, a "
        "per-species market rate, and a bonus reflecting the animal's "
        "logged veterinary health events, turning that health record "
        "into something that can support a loan application rather than "
        "only a private note in a practitioner's file. The same shared "
        "record drives automatic vaccination, weaning and gestation "
        "countdowns that raise a compliance case when a deadline is "
        "missed, and feeds a market-rate scan that keeps an animal's "
        "estimated value current rather than static. The platform "
        "further supports a secure messenger reaching any role directly, "
        "a farmer cooperative's shared dip-tank schedule and group "
        "veterinary request, a feed-formulation function that plans a "
        "farmer's own dry-season feed budget, a trading-journal function "
        "summarising a supplier's or buyer's own trade history, an "
        "outbreak-reporting pipeline that broadcasts a verified disease "
        "alert to every affected farmer, and a role-aware "
        "natural-language assistant that answers a farmer's health and "
        "legal-compliance questions in plain language. Every function is "
        "delivered through both a web application and a native mobile "
        "application, so no role is limited to a single device.",
    ]},

    {"heading": "1.5 AIM", "body": [
        "The aim of the project is to develop a role-based digital "
        "platform connecting farmers, veterinary practitioners, "
        "suppliers, buyers, police officers and financial institutions "
        "around a single verified livestock record, giving every role a "
        "shared registry, marketplace, messaging and clearance system in "
        "place of separate paper trails.",
    ]},

    {"heading": "1.6 OBJECTIVES", "body": [
        "The objectives of the study, listed in the chronological order "
        "in which the corresponding work was undertaken, were:",
        {"numbered": [
            "To design a relational database schema and a role-based "
            "access-control mechanism serving seven distinct platform "
            "roles.",
            "To develop a livestock registry that records an animal's "
            "identity, health timeline and ownership history.",
            "To develop a health-and-compliance lifecycle that tracks a "
            "vaccination, weaning or gestation countdown and raises a "
            "compliance case when a deadline is missed.",
            "To develop a marketplace listing mechanism that withholds a "
            "livestock listing from a buyer until police clearance has "
            "been recorded against it.",
            "To develop a valuation-certificate workflow that computes "
            "and issues a publicly verifiable certificate for a "
            "registered animal, informed by its logged veterinary "
            "health events.",
            "To create an institution ledger function that allows a "
            "valuation certificate to be looked up and flagged for "
            "loan-collateral purposes.",
            "To develop an outbreak-reporting and verification pipeline "
            "that broadcasts a confirmed disease alert to farmers in the "
            "affected region.",
            "To develop a farmer cooperative function that shares a "
            "dip-tank schedule and raises a group veterinary request on "
            "behalf of multiple members.",
            "To develop a feed-formulation function that plans a "
            "farmer's dry-season feed budget, and a trading-journal "
            "function that summarises a supplier's or buyer's own "
            "trade history.",
            "To calculate an estimated market value for a registered "
            "animal from its species, weight and recorded health "
            "history, fed by an automated market-rate scan.",
            "To develop a web-based application giving every platform "
            "role browser access to the system.",
            "To develop a native mobile application, alongside the web "
            "application, giving each platform role access to the "
            "system from a mobile device.",
            "To develop a secure, end-to-end messaging function linking "
            "the Farmer, Veterinarian, Supplier, Buyer, Police and "
            "Institution roles directly within the platform.",
            "To develop a role-aware natural-language assistant that "
            "answers a farmer's livestock-health and legal-compliance "
            "questions and navigates the application on request.",
            "To determine, by deploying and exercising the completed "
            "platform locally, whether its registry, marketplace, "
            "compliance, cooperative and communication workflows all "
            "operate correctly end to end.",
        ]},
    ]},

    {"heading": "1.7 JUSTIFICATION", "body": [
        "The study is justified on both a practical and an academic "
        "basis. Practically, the platform addresses a documented, "
        "real-world gap: Zimbabwean law already assumes a paper trail "
        "linking ownership, health status and clearance, but currently "
        "provides no shared digital system to hold that trail, leaving "
        "farmers exposed to undocumented theft, buyers exposed to "
        "purchasing disputed animals, and livestock wealth largely unable "
        "to be used as loan collateral. A working version of the "
        "platform was built, deployed, and demonstrated publicly at the "
        "Zimbabwe Agricultural Show 2026, which is evidence that the "
        "problem and the proposed solution are recognised outside the "
        "academic setting in which the platform was designed.",
        "Academically, the project demonstrates a reusable software "
        "engineering pattern, namely registering an asset, attaching "
        "expert or authority sign-off to it, gating resale behind "
        "verification, and letting a third party check the resulting "
        "record, applied to a domain, livestock, in which the pattern has "
        "not previously been implemented as production software. The "
        "resulting system integrates role-based access control, a "
        "multi-role relational schema, a verification-gated marketplace "
        "workflow, a public certificate-lookup mechanism, a direct "
        "messaging function reaching every role, a verify-then-broadcast "
        "disease-reporting pipeline, and a role-aware natural-language "
        "assistant built on custom logic rather than a hosted third-party "
        "language model, delivered across both a web application and a "
        "native mobile application, within a single coherent platform, "
        "which is a demonstration of "
        "independent systems-design and full-stack software-engineering "
        "capability appropriate to a final-year Telecommunications "
        "Engineering project.",
        "The study is further justified by its direct relation to the "
        "taught programme. Introduction to Computer Engineering and "
        "Software Engineering I and II underlie the platform's layered "
        "client-server architecture and its requirements-to-design-to-"
        "test discipline, documented respectively in Chapter 3 and "
        "Chapter 4. Cryptography in Telecommunications is applied "
        "directly in the authentication layer: a password is never "
        "stored in plain text, only as a bcrypt hash, and every "
        "authenticated request carries a signed JSON Web Token rather "
        "than a bare identifier a client could forge. Telecommunications "
        "Planning and Project Management informed the phased schedule of "
        "work under which each objective was built and exercised in a "
        "fixed order rather than attempted simultaneously. Finally, the "
        "platform fuses the software design, database design, "
        "data-gathering, development and deployment discipline the "
        "author developed during his industrial attachment at NetOne "
        "Zimbabwe, where root-cause-analysis work on a live microwave "
        "backhaul network required the same combination of structured "
        "data capture, a defensible schema, and a deployable system that "
        "this project required.",
    ]},

    {"heading": "1.8 SCOPE OF THE STUDY", "body": [
        "The study covers the design and development of a software "
        "platform serving seven roles, namely Farmer, Veterinarian, "
        "Supplier, Buyer, Police, Institution and Admin, implemented as a "
        "web application, a companion mobile application, and a shared "
        "backend application programming interface and database. The "
        "platform covers four livestock species relevant to the "
        "Zimbabwean smallholder and commercial context: cattle, goats, "
        "sheep and pigs. The scope includes the marketplace and "
        "sale-clearance workflow, the valuation-certificate and "
        "institution-ledger workflow, the outbreak-reporting and "
        "verification workflow, the health-and-compliance lifecycle, the "
        "feed-formulation and trading-journal function, the role-aware "
        "natural-language assistant, and the supporting authentication, "
        "messaging and cooperative features built around them. The "
        "platform was deployed and evaluated on a local development "
        "server rather than on public infrastructure, for the purposes "
        "of this study.",
    ]},

    {"heading": "1.9 LIMITATIONS AND DELIMITATIONS", "body": [
        {"subheading": "1.9.1 Limitations"},
        "The study was constrained by factors outside the researcher's "
        "control. No live integration with the Zimbabwe Republic Police's "
        "own case-management system, the Department of Veterinary "
        "Services' own records, or a bank's core banking system was "
        "possible within the scope of an undergraduate project, so the "
        "Police, Institution and outbreak-verification roles operate "
        "against records held inside the platform's own database rather "
        "than against a live external system. The legal and regulatory "
        "material informing the platform's design was researched from "
        "publicly available statutes and secondary sources rather than "
        "certified by a qualified Zimbabwean lawyer, and should be "
        "treated as informational rather than as legal advice. No formal "
        "field trial with practising farmers, veterinary practitioners "
        "or police officers was conducted within the project timeline, "
        "and the platform's usability was therefore evaluated by the "
        "researcher and informal reviewers rather than by its intended "
        "end users under real operating conditions.",
        {"subheading": "1.9.2 Delimitations"},
        "Certain boundaries were set deliberately. Physical hardware for "
        "livestock tracking, including an earlier collar-and-base-station "
        "concept explored during the platform's design, was deliberately "
        "excluded from this submission, which is confined to software; "
        "any physical tracking hardware is left as future work. "
        "Integration with the national electronic ear-tag identification "
        "programme was not attempted, and the institution ledger was "
        "delimited to a self-contained certificate-lookup record rather "
        "than a live integration with any specific bank's core banking "
        "system. The study was further delimited to the Zimbabwean "
        "regulatory context and to the four species named in the scope; "
        "poultry and other livestock types were not covered.",
    ]},

    {"heading": "1.10 DOCUMENT ORGANIZATION", "body": [
        "The remainder of this document is organised into four further "
        "chapters. Chapter 2 reviews other relevant systems and "
        "technologies, identifies the research gap the study addresses, "
        "and sets out the research theories informing the design. "
        "Chapter 3 presents the system design, covering the software "
        "architecture, the database schema, the role-based access-control "
        "design, and the design of each of the platform's cross-cutting "
        "workflows. Chapter 4 presents the results of "
        "testing the implemented platform and interprets those results "
        "against the objectives stated in this chapter. Chapter 5 "
        "presents recommendations, identifies future work, and concludes "
        "the study.",
    ]},

    {"heading": "1.11 CONCLUSION", "body": [
        "This chapter has established that livestock ownership and "
        "health records in Zimbabwe are commonly kept in a form that "
        "cannot be independently verified, that this gap is recognised "
        "by existing statute even though no shared digital system "
        "currently fills it, and that PFUMA/INGCEBO was developed to fill "
        "it with a role-based, verification-gated software platform. The "
        "aim, objectives, justification, scope and limitations set out "
        "above frame the system design presented in Chapter 2 and "
        "Chapter 3.",
    ]},
]
