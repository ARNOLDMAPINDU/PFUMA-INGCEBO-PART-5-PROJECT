# -*- coding: utf-8 -*-
"""Front matter for the TCL 5000 final project document (PFUMA/INGCEBO).

Module-level names consumed by the builder:
    TITLE_PAGE, COMMITTEE_REPORT, DEDICATION, ACKNOWLEDGEMENTS,
    COPYRIGHT, DECLARATION, ABSTRACT, KEYWORDS, ACRONYMS

Conventions follow the TCL 5000 guidelines and the departmental exemplar
(Kajawu, NT01911274D) — see CLAUDE.md section 4 for the full structure this
implements. Bracketed items are genuine placeholders the candidate must
complete; do not invent a registration number or a supervisor name here.
"""

# ---------------------------------------------------------------- title page
TITLE_PAGE = {
    "institution": "NATIONAL UNIVERSITY OF SCIENCE AND TECHNOLOGY",
    "faculty": "FACULTY OF INDUSTRIAL TECHNOLOGY",
    "department": "DEPARTMENT OF TELECOMMUNICATIONS ENGINEERING",
    "programme_banner": (
        "BACHELOR OF ENGINEERING HONORS DEGREE IN "
        "TELECOMMUNICATIONS ENGINEERING"
    ),
    "title": (
        "DEVELOPMENT OF A VERIFIED DIGITAL LIVESTOCK REGISTRY AND "
        "MARKETPLACE PLATFORM WITH POLICE-GATED SALE CLEARANCE "
        "(PFUMA/INGCEBO)"
    ),
    "student": "Arnold T. Mapindu",
    "reg_number": "[STUDENT NUMBER]",
    "supervisor": "[SUPERVISOR NAME AND TITLE]",
    "submission_statement": (
        "This Project is submitted in partial fulfillment of the requirement "
        "for the award of a Bachelor of Engineering (honors) Degree in "
        "Telecommunications Engineering"
    ),
    "date": "[SUBMISSION MONTH] 2026",
}

# ------------------------------------------------------- committee report
COMMITTEE_REPORT = (
    "We certify that we have read this graduation project report as examining "
    "committee, examined the student in its content and that in our opinion it "
    "is adequate as a project document for Bachelor of Engineering Honors "
    "Degree in Telecommunications Engineering."
)

# ---------------------------------------------------------------- dedication
DEDICATION = (
    "To my parents, who paid for the years of schooling that made this "
    "possible. To the rural farmers whose livestock keeps them fed and "
    "solvent, and who deserve better than a paper record that can be lost, "
    "forged, or never have existed in the first place."
)

# ----------------------------------------------------------- acknowledgements
ACKNOWLEDGEMENTS = [
    "The guidance of the project supervisor, [Supervisor Name], is gratefully "
    "acknowledged. Appreciation is also extended to the academic and "
    "technical staff of the Department of Telecommunications Engineering at "
    "the National University of Science and Technology, and to the Telone "
    "Centre for Learning, for the teaching and facilities that supported "
    "this study.",

    "Thanks are due to the farmers, veterinary practitioners and community "
    "members who described, in ordinary conversation, how a livestock sale "
    "or a disease outbreak is actually handled in practice — that ordinary "
    "description is what shaped the platform's role structure more than any "
    "single document did. Finally, the author thanks his family for their "
    "support and patience throughout the period of study.",
]

# ----------------------------------------------------------------- copyright
COPYRIGHT = (
    "All rights reserved. No part of this project may be reproduced, stored "
    "in any retrieval system or transmitted in any form or by any means, "
    "electronic, mechanical, photocopying, recording or otherwise from "
    "scholarly purpose without the prior written permission of the author or "
    "of National University of Science and Technology or Telone Centre for "
    "Learning on behalf of the author."
)

# --------------------------------------------------------------- declaration
DECLARATION = (
    "This project is my original work except where the sources are "
    "acknowledged. No portion of the work contained during this document has "
    "been submitted in support of any application for the other degree or "
    "qualification of this or the other university or institute of learning."
)

# ------------------------------------------------------------------ abstract
# Guidelines: past tense, third person, complete sentences, no citations, no
# abbreviations, not more than one page (about 150 words).
ABSTRACT = [
    "Livestock is frequently the largest store of wealth held by a rural "
    "Zimbabwean household, yet ownership, health and sale records for that "
    "wealth are commonly kept on paper, by memory, or not kept at all. This "
    "leaves a buyer unable to verify what is being purchased, a bank or "
    "insurer unable to lend against livestock as collateral, and a police "
    "officer without a fast way to tell a lawful sale from a stolen animal.",

    "This study addressed that gap. A role-based digital platform was "
    "designed and developed, giving each participant in a livestock "
    "transaction, namely the farmer, the veterinary practitioner, the "
    "supplier, the buyer, the police officer, and a financial institution, "
    "a shared and checkable record. The platform was implemented as a web "
    "application and a companion mobile application, backed by a single "
    "relational database. A livestock listing created by a farmer was made "
    "to remain hidden from buyers until police clearance had been recorded "
    "against it, mirroring the clearance process already used in "
    "Zimbabwean livestock trade.",

    "The platform was built, deployed on a local server, and exercised "
    "directly, and its clearance, certification, and outbreak-reporting "
    "workflows were confirmed to operate end to end. The study concluded "
    "that a verified-record pattern of this kind is achievable entirely in "
    "software, and that it directly addresses the traceability gap "
    "identified at the outset.",
]

KEYWORDS = [
    "Livestock traceability",
    "Digital registry",
    "Role-based access control",
    "Sale clearance",
    "Verification platform",
    "Mobile application",
    "Relational database",
    "Agricultural technology",
]

# ------------------------------------------------------------------ acronyms
_ACRONYMS = [
    ("API", "Application Programming Interface"),
    ("CVSZ", "Council of Veterinary Surgeons of Zimbabwe"),
    ("DVS", "Department of Veterinary Services"),
    ("HTTP", "Hypertext Transfer Protocol"),
    ("HTTPS", "Hypertext Transfer Protocol Secure"),
    ("JSON", "JavaScript Object Notation"),
    ("JWT", "JSON Web Token"),
    ("NUST", "National University of Science and Technology"),
    ("PWA", "Progressive Web Application"),
    ("REST", "Representational State Transfer"),
    ("SQL", "Structured Query Language"),
    ("UI", "User Interface"),
    ("URL", "Uniform Resource Locator"),
    ("UX", "User Experience"),
    ("ZRP", "Zimbabwe Republic Police"),
]

# Alphabetically sorted, case-insensitive, as the guidelines require.
ACRONYMS = sorted(_ACRONYMS, key=lambda pair: pair[0].upper())
